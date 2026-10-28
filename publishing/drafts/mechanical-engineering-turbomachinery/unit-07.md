# Unit 07: Rotor Dynamics, Blades and Mechanical Reliability

**Course Code**: TBM 307 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Rotor Dynamics, Blades and Mechanical Reliability**.

## U07-L01 — Centrifugal blade stress scaling

**Outcome.** Use conservation laws and appropriate reference stations to analyze **centrifugal blade stress scaling**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.

### 1. Physical setting and governing reasoning

An engineer should be able to explain the direction of power transfer before touching a calculator. In this lesson the system boundary encloses the relevant machine component; the chosen inlet and outlet stations are part of the model, not details added after computing a value. The shared design brief is: A high-speed rotor operates with alternating pressure loads and thermal transients; vibratory modes, bearings, seals and blade stress limit safe operation. This particular lesson tests how centrifugal blade stress scaling influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Rotational inertia generates large hoop and radial stress that grow with speed squared. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `sigma_char~rho_m U_tip^2 for comparable rotor geometry`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A rotor is not merely a set of fluid passages. Centrifugal stress, thermal gradients, burst margin, bearing dynamics, seal rubbing and high-cycle fatigue restrict attainable U and service life. One-dimensional scaling has teaching value but is never a substitute for qualified rotating equipment design.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** For steel-like rho_m=7800 kg/m3 and tip speed 250 m/s, the scaling stress is 487.5 MPa before shape factors.

**Explicit substitution:** sigma_char≈7800×250²; therefore **487.5 MPa**. Characteristic stress scaling is not an allowable stress or burst proof.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Treating a dimensional scaling estimate as finite-element certification risks rotor burst. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Use measured geometry, high-cycle fatigue data, material traceability and validated FEA. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Real flow deviates from uniform one-dimensional pictures because of wakes, secondary flow, wall boundary layers and tip leakage. An equation that gives a plausible central value does not establish the distribution over the blade span. This is why credible performance assessment combines integrated measurements with local diagnostics and a transparent loss model.

**Provisional decision:** Reduce tip speed or redesign the disk instead of extrapolating stress below allowable from one scalar. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `sigma_char~rho_m U_tip^2 for comparable rotor geometry`, reproduce **487.5 MPa** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Treating a dimensional scaling estimate as finite-element certification risks rotor burst. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Use measured geometry, high-cycle fatigue data, material traceability and validated FEA. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Reduce tip speed or redesign the disk instead of extrapolating stress below allowable from one scalar. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **sigma_char≈7800×250²**, yielding **487.5 MPa** under the stated simplifications. Characteristic stress scaling is not an allowable stress or burst proof. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Rotational inertia generates large hoop and radial stress that grow with speed squared. Use measured geometry, high-cycle fatigue data, material traceability and validated FEA. Link one cause to an independent measurement and report uncertainty.

**5.** Reduce tip speed or redesign the disk instead of extrapolating stress below allowable from one scalar. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U07-L02 — Rotor unbalance and bearing load

**Outcome.** Use conservation laws and appropriate reference stations to analyze **rotor unbalance and bearing load**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.

### 1. Physical setting and governing reasoning

The first challenge is to connect the observed state to a physical balance. A pressure, velocity or temperature measurement alone is incomplete until the flow direction, station definition and performance quantity have been fixed. The shared design brief is: A high-speed rotor operates with alternating pressure loads and thermal transients; vibratory modes, bearings, seals and blade stress limit safe operation. This particular lesson tests how rotor unbalance and bearing load influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Unbalance forces scale with speed squared and may excite structural resonances. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `F_unbalance=m_e e omega^2`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Critical-speed diagrams need coupling to rotor-bearing mode shapes and speed-dependent gyroscopic effects. Unbalance force increases with omega squared; excitation orders may intersect bending or blade modes during run-up or coast-down.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** An eccentric mass of 0.02 kg at 1 mm radius and 3000 rpm produces about 1.97 N of rotating force.

**Explicit substitution:** F=0.02×0.001×(2π×3000/60)²; therefore **1.974 N**. At twice speed the force becomes four times as large.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Measuring low-speed vibration alone does not ensure acceptable high-speed response. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Document balance grade, probes, phase reference, run-up and run-down spectra. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Keep hydraulic or aerodynamic useful power separate from shaft power and electric input. It is possible for a component to improve while the entire installation consumes more electricity due to throttling, controls or auxiliary devices. Show each energy boundary and the associated loss.

**Provisional decision:** Set balancing and trip requirements by rotor type and verified operating envelope. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `F_unbalance=m_e e omega^2`, reproduce **1.974 N** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Measuring low-speed vibration alone does not ensure acceptable high-speed response. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Document balance grade, probes, phase reference, run-up and run-down spectra. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Set balancing and trip requirements by rotor type and verified operating envelope. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **F=0.02×0.001×(2π×3000/60)²**, yielding **1.974 N** under the stated simplifications. At twice speed the force becomes four times as large. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Unbalance forces scale with speed squared and may excite structural resonances. Document balance grade, probes, phase reference, run-up and run-down spectra. Link one cause to an independent measurement and report uncertainty.

**5.** Set balancing and trip requirements by rotor type and verified operating envelope. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U07-L03 — Critical speed and Campbell diagrams

**Outcome.** Use conservation laws and appropriate reference stations to analyze **critical speed and campbell diagrams**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.

### 1. Physical setting and governing reasoning

An apparently simple equipment decision becomes difficult when the operating envelope shifts. Work from conservation laws to a tractable approximation, and only then decide what constitutes evidence for the performance claim. The shared design brief is: A high-speed rotor operates with alternating pressure loads and thermal transients; vibratory modes, bearings, seals and blade stress limit safe operation. This particular lesson tests how critical speed and campbell diagrams influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Real rotor-bearing systems have multiple gyroscopic modes whose frequencies vary with rotation. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `omega_n=sqrt(k/m) for a simple single-mass model`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Reliability evidence may include controlled balancing, mechanical overspeed testing when required, nondestructive evaluation, rotor stress simulation, temperature monitoring and fatigue-life assessment. Serious failures can be catastrophic; students should never attempt hazardous rotor spin tests.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** With stiffness 2.0 MN/m and equivalent mass 50 kg, natural angular frequency is 200 rad/s, about 1910 rpm.

**Explicit substitution:** omega_n=sqrt(2,000,000/50)=200 rad/s; n=omega_n×60/(2π); therefore **1909.9 rpm**. Real rotors have multiple damped gyroscopic critical speeds.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** A single rigid-rotor frequency is not sufficient for stability or critical-speed separation. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Measure modal response during safe run-up and compare with multi-degree-of-freedom predictions. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. When comparing before-and-after tests, hold corrected flow or an equivalent meaningful operating state close enough that changing duty does not masquerade as better hardware. Temperature and gas composition influence corrected variables, while a hydraulic network may change substantially with valve setting. State the comparison tolerance rather than assuming curves can be overlaid without adjustment.

**Provisional decision:** Select bearings and operating bands that avoid resonance and instability. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `omega_n=sqrt(k/m) for a simple single-mass model`, reproduce **1909.9 rpm** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: A single rigid-rotor frequency is not sufficient for stability or critical-speed separation. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Measure modal response during safe run-up and compare with multi-degree-of-freedom predictions. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Select bearings and operating bands that avoid resonance and instability. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **omega_n=sqrt(2,000,000/50)=200 rad/s; n=omega_n×60/(2π)**, yielding **1909.9 rpm** under the stated simplifications. Real rotors have multiple damped gyroscopic critical speeds. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Real rotor-bearing systems have multiple gyroscopic modes whose frequencies vary with rotation. Measure modal response during safe run-up and compare with multi-degree-of-freedom predictions. Link one cause to an independent measurement and report uncertainty.

**5.** Select bearings and operating bands that avoid resonance and instability. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U07-L04 — Bearing losses, seals and leakage

**Outcome.** Use conservation laws and appropriate reference stations to analyze **bearing losses, seals and leakage**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.

### 1. Physical setting and governing reasoning

Every turbomachine exchanges energy and momentum through moving surfaces. This lesson isolates one effect while retaining enough of the surrounding machine to prevent an unrealistic interpretation of its result. The shared design brief is: A high-speed rotor operates with alternating pressure loads and thermal transients; vibratory modes, bearings, seals and blade stress limit safe operation. This particular lesson tests how bearing losses, seals and leakage influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Seals also leak mass across pressure differences; leakage affects compressor and turbine maps as well as net output. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `P_friction=T_loss omega`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A rotor is not merely a set of fluid passages. Centrifugal stress, thermal gradients, burst margin, bearing dynamics, seal rubbing and high-cycle fatigue restrict attainable U and service life. One-dimensional scaling has teaching value but is never a substitute for qualified rotating equipment design.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** If bearing torque is 8 N m at 3000 rpm, mechanical dissipation is about 2.51 kW.

**Explicit substitution:** P=8×(2π×3000/60); therefore **2513 W = 2.513 kW**. This heat appears in bearings and associated systems, not useful output.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Assigning all lost energy to aerodynamic inefficiency conceals bearing faults or clearance changes. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Measure oil temperature rise, seal differential pressure, leak flow and shaft torque. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Estimate which measured inputs dominate the output by perturbing them individually. If a 1% sensor shift changes a design recommendation, the decision is not robust without calibration and repeat testing. Report the measurement chain and the test range, not only the final digits.

**Provisional decision:** Compare tighter seals against rub risk, thermal growth and maintenance cost. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `P_friction=T_loss omega`, reproduce **2513 W = 2.513 kW** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Assigning all lost energy to aerodynamic inefficiency conceals bearing faults or clearance changes. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Measure oil temperature rise, seal differential pressure, leak flow and shaft torque. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Compare tighter seals against rub risk, thermal growth and maintenance cost. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **P=8×(2π×3000/60)**, yielding **2513 W = 2.513 kW** under the stated simplifications. This heat appears in bearings and associated systems, not useful output. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Seals also leak mass across pressure differences; leakage affects compressor and turbine maps as well as net output. Measure oil temperature rise, seal differential pressure, leak flow and shaft torque. Link one cause to an independent measurement and report uncertainty.

**5.** Compare tighter seals against rub risk, thermal growth and maintenance cost. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U07-L05 — Blade fatigue and thermal transients

**Outcome.** Use conservation laws and appropriate reference stations to analyze **blade fatigue and thermal transients**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.

### 1. Physical setting and governing reasoning

Consider the difference between predicting a single performance number and qualifying a rotating machine. This lesson develops one measurable calculation, then asks which assumptions fail outside the demonstration state. The shared design brief is: A high-speed rotor operates with alternating pressure loads and thermal transients; vibratory modes, bearings, seals and blade stress limit safe operation. This particular lesson tests how blade fatigue and thermal transients influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Restrained expansion creates stress, while transient hot spots and vibratory modes produce cumulative damage. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `Delta_epsilon_thermal≈alpha Delta_T for free expansion`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Critical-speed diagrams need coupling to rotor-bearing mode shapes and speed-dependent gyroscopic effects. Unbalance force increases with omega squared; excitation orders may intersect bending or blade modes during run-up or coast-down.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A metal with alpha=12e-6 1/K subjected to a 250 K rise has free strain near 0.003.

**Explicit substitution:** epsilon_free=12×10^(−6)×250; therefore **0.003 or 0.3%**. Restrained expansion and modulus are needed to estimate stress.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Using free thermal strain directly as a certified stress without constraint and material model is misleading. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Inspect temperature gradients, strain response, inspection records and cycle histories. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. A classroom correlation is not a qualification standard. The transition from calculation to product release requires traceable material data, instrument calibration, component testing and safety review. Where code compliance applies, record its edition and jurisdiction instead of claiming that an illustrative number confers approval.

**Provisional decision:** Reduce thermal ramp rate or change cooling distribution before extending service intervals. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `Delta_epsilon_thermal≈alpha Delta_T for free expansion`, reproduce **0.003 or 0.3%** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Using free thermal strain directly as a certified stress without constraint and material model is misleading. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Inspect temperature gradients, strain response, inspection records and cycle histories. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Reduce thermal ramp rate or change cooling distribution before extending service intervals. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **epsilon_free=12×10^(−6)×250**, yielding **0.003 or 0.3%** under the stated simplifications. Restrained expansion and modulus are needed to estimate stress. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Restrained expansion creates stress, while transient hot spots and vibratory modes produce cumulative damage. Inspect temperature gradients, strain response, inspection records and cycle histories. Link one cause to an independent measurement and report uncertainty.

**5.** Reduce thermal ramp rate or change cooling distribution before extending service intervals. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

