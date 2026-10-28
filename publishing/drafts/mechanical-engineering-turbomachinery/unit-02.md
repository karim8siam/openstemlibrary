# Unit 02: Centrifugal Pumps, Fans and Hydraulic Systems

**Course Code**: TBM 302 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Centrifugal Pumps, Fans and Hydraulic Systems**.

## U02-L01 — Pump head from pressure and velocity

**Outcome.** Use conservation laws and appropriate reference stations to analyze **pump head from pressure and velocity**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.

### 1. Physical setting and governing reasoning

An engineer should be able to explain the direction of power transfer before touching a calculator. In this lesson the system boundary encloses the relevant machine component; the chosen inlet and outlet stations are part of the model, not details added after computing a value. The shared design brief is: An industrial water loop needs a specified flow against changing friction loss; the chosen pump must satisfy system head without approaching cavitation or excessive power demand. This particular lesson tests how pump head from pressure and velocity influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Pump head is specific mechanical energy divided by gravitational acceleration, not simply a pressure gauge reading. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `H=Delta_p/(rho g)+Delta(V^2)/(2g)+Delta_z`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Energy costing should account for pump hydraulic output, shaft input, motor and drive efficiency. Affinity laws compare corresponding conditions for the same machine and fluid. A speed change must be combined with a fresh intersection against the actual network head curve.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** For water at 998 kg/m3, 200 kPa pressure rise and negligible elevation or velocity difference give H≈20.43 m.

**Explicit substitution:** H = 200,000/(998×9.81); therefore **20.43 m**. This is pressure head only; add velocity and elevation terms if nonzero.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Ignoring pipe diameter differences between pressure taps creates a hidden kinetic-energy bias. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Survey tap elevations and pipe areas and calibrate differential pressure against independent reference. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. An adverse trend can result from fouling, poor installation, instrumentation drift or genuine wear. Avoid replacing components on the basis of one efficiency number. Compare independent signals such as vibration, temperature, flow, differential pressure and operating history before diagnosing cause.

**Provisional decision:** Choose measurement locations and pipe transitions that minimize installation-induced error. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `H=Delta_p/(rho g)+Delta(V^2)/(2g)+Delta_z`, reproduce **20.43 m** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Ignoring pipe diameter differences between pressure taps creates a hidden kinetic-energy bias. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Survey tap elevations and pipe areas and calibrate differential pressure against independent reference. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Choose measurement locations and pipe transitions that minimize installation-induced error. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **H = 200,000/(998×9.81)**, yielding **20.43 m** under the stated simplifications. This is pressure head only; add velocity and elevation terms if nonzero. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Pump head is specific mechanical energy divided by gravitational acceleration, not simply a pressure gauge reading. Survey tap elevations and pipe areas and calibrate differential pressure against independent reference. Link one cause to an independent measurement and report uncertainty.

**5.** Choose measurement locations and pipe transitions that minimize installation-induced error. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U02-L02 — System curves and operating-point intersection

**Outcome.** Use conservation laws and appropriate reference stations to analyze **system curves and operating-point intersection**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.

### 1. Physical setting and governing reasoning

The first challenge is to connect the observed state to a physical balance. A pressure, velocity or temperature measurement alone is incomplete until the flow direction, station definition and performance quantity have been fixed. The shared design brief is: An industrial water loop needs a specified flow against changing friction loss; the chosen pump must satisfy system head without approaching cavitation or excessive power demand. This particular lesson tests how system curves and operating-point intersection influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Frictional head typically increases approximately with square flow for turbulent networks with fixed configuration. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `H_sys=H_static+K Q^2`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A pump has a machine curve; the network has a system curve. Their intersection, not either rating in isolation, fixes the operating point. A static lift introduces an offset in head while turbulent friction is often modeled as approximately K Q². Parallel and series operation require explicit curve reconstruction.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A test loop with 12 m static head and K=8000 s2/m5 requires 32 m at Q=0.050 m3/s.

**Explicit substitution:** H=12+8000×(0.050)²; therefore **32.0 m**. Square law here assumes the fixed system resistance coefficient remains appropriate.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** A nominal pump flow is not delivered if the system curve intersects the pump curve elsewhere. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Measure flow versus differential head and fit a curve only over the observed valve configuration. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Real flow deviates from uniform one-dimensional pictures because of wakes, secondary flow, wall boundary layers and tip leakage. An equation that gives a plausible central value does not establish the distribution over the blade span. This is why credible performance assessment combines integrated measurements with local diagnostics and a transparent loss model.

**Provisional decision:** Resize piping or modify speed to move duty toward best efficiency instead of oversizing the impeller. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `H_sys=H_static+K Q^2`, reproduce **32.0 m** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: A nominal pump flow is not delivered if the system curve intersects the pump curve elsewhere. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Measure flow versus differential head and fit a curve only over the observed valve configuration. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Resize piping or modify speed to move duty toward best efficiency instead of oversizing the impeller. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **H=12+8000×(0.050)²**, yielding **32.0 m** under the stated simplifications. Square law here assumes the fixed system resistance coefficient remains appropriate. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Frictional head typically increases approximately with square flow for turbulent networks with fixed configuration. Measure flow versus differential head and fit a curve only over the observed valve configuration. Link one cause to an independent measurement and report uncertainty.

**5.** Resize piping or modify speed to move duty toward best efficiency instead of oversizing the impeller. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U02-L03 — Pump efficiency and power

**Outcome.** Use conservation laws and appropriate reference stations to analyze **pump efficiency and power**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.

### 1. Physical setting and governing reasoning

An apparently simple equipment decision becomes difficult when the operating envelope shifts. Work from conservation laws to a tractable approximation, and only then decide what constitutes evidence for the performance claim. The shared design brief is: An industrial water loop needs a specified flow against changing friction loss; the chosen pump must satisfy system head without approaching cavitation or excessive power demand. This particular lesson tests how pump efficiency and power influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Hydraulic output power is lower than shaft and electrical inputs because of hydraulic, leakage, disk and motor losses. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `P_elec=rho g Q H/(eta_p eta_motor)`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

NPSH available uses suction absolute pressure relative to local vapor pressure, expressed as head. NPSH required is a manufacturer test criterion, often referenced to a particular head-drop definition; it is not a proof that all cavitation is absent. Temperature changes both vapor pressure and sometimes density.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** Water at 1000 kg/m3 and Q=0.035 m3/s over 25 m, with pump eta=0.76 and motor eta=0.93, uses about 12.13 kW.

**Explicit substitution:** P = 1000×9.81×0.035×25/(0.76×0.93); therefore **12.13 kW**. Fluid power is 8.584 kW, less than electrical input.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Calling hydraulic power the electricity bill understates energy and heat losses. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Measure three-phase electrical input and independent water-flow/head channels with uncertainty estimates. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Keep hydraulic or aerodynamic useful power separate from shaft power and electric input. It is possible for a component to improve while the entire installation consumes more electricity due to throttling, controls or auxiliary devices. Show each energy boundary and the associated loss.

**Provisional decision:** Compare a high-efficiency pump option using annual energy rather than purchase cost alone. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `P_elec=rho g Q H/(eta_p eta_motor)`, reproduce **12.13 kW** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Calling hydraulic power the electricity bill understates energy and heat losses. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Measure three-phase electrical input and independent water-flow/head channels with uncertainty estimates. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Compare a high-efficiency pump option using annual energy rather than purchase cost alone. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **P = 1000×9.81×0.035×25/(0.76×0.93)**, yielding **12.13 kW** under the stated simplifications. Fluid power is 8.584 kW, less than electrical input. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Hydraulic output power is lower than shaft and electrical inputs because of hydraulic, leakage, disk and motor losses. Measure three-phase electrical input and independent water-flow/head channels with uncertainty estimates. Link one cause to an independent measurement and report uncertainty.

**5.** Compare a high-efficiency pump option using annual energy rather than purchase cost alone. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U02-L04 — Cavitation and NPSH margin

**Outcome.** Use conservation laws and appropriate reference stations to analyze **cavitation and npsh margin**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.

### 1. Physical setting and governing reasoning

Every turbomachine exchanges energy and momentum through moving surfaces. This lesson isolates one effect while retaining enough of the surrounding machine to prevent an unrealistic interpretation of its result. The shared design brief is: An industrial water loop needs a specified flow against changing friction loss; the chosen pump must satisfy system head without approaching cavitation or excessive power demand. This particular lesson tests how cavitation and npsh margin influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Local static pressure falls through an inlet acceleration; vapor bubbles may collapse downstream and erode surfaces. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `NPSHa=(p_suction_abs-p_vapor)/(rho g)+V_s^2/(2g) relative to datum`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Energy costing should account for pump hydraulic output, shaft input, motor and drive efficiency. Affinity laws compare corresponding conditions for the same machine and fluid. A speed change must be combined with a fresh intersection against the actual network head curve.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** At suction absolute pressure 65 kPa, vapor pressure 3 kPa, rho=1000 kg/m3 and negligible velocity correction, NPSHa≈6.32 m.

**Explicit substitution:** NPSHa = (65,000−3,000)/(1000×9.81); therefore **6.32 m**. Absolute suction and vapor pressures must share the same reference.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Treating gauge pressure as absolute or assuming NPSHr is a universal cavitation-free limit is unsafe. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Monitor suction absolute pressure, fluid temperature, inlet losses, acoustic signature and vendor NPSHr curve. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. When comparing before-and-after tests, hold corrected flow or an equivalent meaningful operating state close enough that changing duty does not masquerade as better hardware. Temperature and gas composition influence corrected variables, while a hydraulic network may change substantially with valve setting. State the comparison tolerance rather than assuming curves can be overlaid without adjustment.

**Provisional decision:** Increase suction pipe diameter or liquid level before increasing impeller speed. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `NPSHa=(p_suction_abs-p_vapor)/(rho g)+V_s^2/(2g) relative to datum`, reproduce **6.32 m** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Treating gauge pressure as absolute or assuming NPSHr is a universal cavitation-free limit is unsafe. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Monitor suction absolute pressure, fluid temperature, inlet losses, acoustic signature and vendor NPSHr curve. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Increase suction pipe diameter or liquid level before increasing impeller speed. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **NPSHa = (65,000−3,000)/(1000×9.81)**, yielding **6.32 m** under the stated simplifications. Absolute suction and vapor pressures must share the same reference. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Local static pressure falls through an inlet acceleration; vapor bubbles may collapse downstream and erode surfaces. Monitor suction absolute pressure, fluid temperature, inlet losses, acoustic signature and vendor NPSHr curve. Link one cause to an independent measurement and report uncertainty.

**5.** Increase suction pipe diameter or liquid level before increasing impeller speed. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U02-L05 — Fans and compressible ventilation flow

**Outcome.** Use conservation laws and appropriate reference stations to analyze **fans and compressible ventilation flow**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.

### 1. Physical setting and governing reasoning

Consider the difference between predicting a single performance number and qualifying a rotating machine. This lesson develops one measurable calculation, then asks which assumptions fail outside the demonstration state. The shared design brief is: An industrial water loop needs a specified flow against changing friction loss; the chosen pump must satisfy system head without approaching cavitation or excessive power demand. This particular lesson tests how fans and compressible ventilation flow influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** A fan consumes shaft power to create a total-pressure increase, but static-pressure rating depends on test arrangement. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `P_air=Delta_p_total Q; P_input=P_air/(eta_fan eta_drive)`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A pump has a machine curve; the network has a system curve. Their intersection, not either rating in isolation, fixes the operating point. A static lift introduces an offset in head while turbulent friction is often modeled as approximately K Q². Parallel and series operation require explicit curve reconstruction.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A fan delivering 2.5 m3/s against 800 Pa total-pressure rise gives 2.0 kW air power and 3.08 kW input at overall eta=0.65.

**Explicit substitution:** P_air=800×2.5=2000 W; P_input=2000/0.65; therefore **2.00 kW useful; 3.08 kW input**. Static pressure must not be substituted for total pressure without correction.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Confusing total and static fan pressure exaggerates performance in a ducted installation. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Use calibrated traverses, pressure station corrections and measured drive input. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Estimate which measured inputs dominate the output by perturbing them individually. If a 1% sensor shift changes a design recommendation, the decision is not robust without calibration and repeat testing. Report the measurement chain and the test range, not only the final digits.

**Provisional decision:** Choose fan arrangement for a real duct resistance curve rather than free-delivery volumetric flow. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `P_air=Delta_p_total Q; P_input=P_air/(eta_fan eta_drive)`, reproduce **2.00 kW useful; 3.08 kW input** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Confusing total and static fan pressure exaggerates performance in a ducted installation. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Use calibrated traverses, pressure station corrections and measured drive input. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Choose fan arrangement for a real duct resistance curve rather than free-delivery volumetric flow. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **P_air=800×2.5=2000 W; P_input=2000/0.65**, yielding **2.00 kW useful; 3.08 kW input** under the stated simplifications. Static pressure must not be substituted for total pressure without correction. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** A fan consumes shaft power to create a total-pressure increase, but static-pressure rating depends on test arrangement. Use calibrated traverses, pressure station corrections and measured drive input. Link one cause to an independent measurement and report uncertainty.

**5.** Choose fan arrangement for a real duct resistance curve rather than free-delivery volumetric flow. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

