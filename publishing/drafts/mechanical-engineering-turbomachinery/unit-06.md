# Unit 06: Hydraulic Turbines and Renewable Power

**Course Code**: TBM 306 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Hydraulic Turbines and Renewable Power**.

## U06-L01 — Gross versus net hydraulic head

**Outcome.** Use conservation laws and appropriate reference stations to analyze **gross versus net hydraulic head**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.

### 1. Physical setting and governing reasoning

An engineer should be able to explain the direction of power transfer before touching a calculator. In this lesson the system boundary encloses the relevant machine component; the chosen inlet and outlet stations are part of the model, not details added after computing a value. The shared design brief is: A river scheme has a seasonal flow-duration curve and limited net head; turbine selection must account for civil losses, operating range and environmental constraints. This particular lesson tests how gross versus net hydraulic head influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Available runner head changes with flow because pipe friction and local entrance losses increase. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `H_net=H_gross-h_losses`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Impulse turbines use jets and largely atmospheric runner pressure; reaction turbines operate filled with water and need suction-side and draft-tube analysis. Specific speed aids selection only when its numerical unit convention is fixed.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A water scheme with 43 m gross head and 5 m penstock losses has 38 m net head at that flow.

**Explicit substitution:** H_net=43−5; therefore **38 m**. Penstock friction depends on discharge and must be reassessed off-design.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Rating equipment on survey elevation alone systematically overpredicts output. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Survey elevations, measure head at runner stations and characterize loss across seasonal flow. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Estimate which measured inputs dominate the output by perturbing them individually. If a 1% sensor shift changes a design recommendation, the decision is not robust without calibration and repeat testing. Report the measurement chain and the test range, not only the final digits.

**Provisional decision:** Resize the penstock and compare extra capital cost against recovered annual energy. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `H_net=H_gross-h_losses`, reproduce **38 m** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Rating equipment on survey elevation alone systematically overpredicts output. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Survey elevations, measure head at runner stations and characterize loss across seasonal flow. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Resize the penstock and compare extra capital cost against recovered annual energy. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **H_net=43−5**, yielding **38 m** under the stated simplifications. Penstock friction depends on discharge and must be reassessed off-design. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Available runner head changes with flow because pipe friction and local entrance losses increase. Survey elevations, measure head at runner stations and characterize loss across seasonal flow. Link one cause to an independent measurement and report uncertainty.

**5.** Resize the penstock and compare extra capital cost against recovered annual energy. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U06-L02 — Hydroelectric turbine power and efficiency

**Outcome.** Use conservation laws and appropriate reference stations to analyze **hydroelectric turbine power and efficiency**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.

### 1. Physical setting and governing reasoning

The first challenge is to connect the observed state to a physical balance. A pressure, velocity or temperature measurement alone is incomplete until the flow direction, station definition and performance quantity have been fixed. The shared design brief is: A river scheme has a seasonal flow-duration curve and limited net head; turbine selection must account for civil losses, operating range and environmental constraints. This particular lesson tests how hydroelectric turbine power and efficiency influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Flow and head set the hydraulic resource, while mechanical and electrical losses reduce exportable energy. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `P_elec=rho g Q H_net eta_total`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A high annual energy yield may come from matching a lower peak-output machine to the site flow-duration curve. Uncertainty in water availability, sediment, ecology and licensing can outweigh the precision of runner optimization.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A plant using Q=2.4 m3/s, H=28 m, rho=1000 kg/m3 and eta_total=0.87 supplies about 573.7 kW.

**Explicit substitution:** P=1000×9.81×2.4×28×0.87/1000; therefore **573.55 kW**. Here total efficiency includes generator loss and is only an assumed value.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Substituting installed nameplate output for available river flow exaggerates capacity factor. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Log hourly flow, head and electrical power with outages and bypass flows separately identified. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. A classroom correlation is not a qualification standard. The transition from calculation to product release requires traceable material data, instrument calibration, component testing and safety review. Where code compliance applies, record its edition and jurisdiction instead of claiming that an illustrative number confers approval.

**Provisional decision:** Estimate energy under a flow-duration curve rather than assuming year-round design flow. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `P_elec=rho g Q H_net eta_total`, reproduce **573.55 kW** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Substituting installed nameplate output for available river flow exaggerates capacity factor. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Log hourly flow, head and electrical power with outages and bypass flows separately identified. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Estimate energy under a flow-duration curve rather than assuming year-round design flow. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **P=1000×9.81×2.4×28×0.87/1000**, yielding **573.55 kW** under the stated simplifications. Here total efficiency includes generator loss and is only an assumed value. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Flow and head set the hydraulic resource, while mechanical and electrical losses reduce exportable energy. Log hourly flow, head and electrical power with outages and bypass flows separately identified. Link one cause to an independent measurement and report uncertainty.

**5.** Estimate energy under a flow-duration curve rather than assuming year-round design flow. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U06-L03 — Impulse turbine jet and runner speed

**Outcome.** Use conservation laws and appropriate reference stations to analyze **impulse turbine jet and runner speed**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.

### 1. Physical setting and governing reasoning

An apparently simple equipment decision becomes difficult when the operating envelope shifts. Work from conservation laws to a tractable approximation, and only then decide what constitutes evidence for the performance claim. The shared design brief is: A river scheme has a seasonal flow-duration curve and limited net head; turbine selection must account for civil losses, operating range and environmental constraints. This particular lesson tests how impulse turbine jet and runner speed influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Pelton buckets exchange impulse with a free jet under near-atmospheric runner pressure. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `Vjet≈sqrt(2 g H) for lossless nozzle`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Hydroelectric potential depends on net head and discharge. Gross head is a civil elevation difference; penstocks, intake, valves and runners experience losses that vary with flow. Environmental bypass requirements reduce usable discharge and must not be treated as optional.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** With H=80 m, ideal water jet speed is about 39.6 m/s before nozzle losses.

**Explicit substitution:** V=sqrt(2×9.81×80); therefore **39.62 m/s ideal**. Actual jet velocity is reduced by nozzle losses.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Modeling an impulse wheel with a sealed reaction draft tube misrepresents the mechanism. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Measure nozzle pressure, jet diameter, needle position and runner rpm. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Identify every mass stream crossing the control volume, including leakage, bleed and cooling injections. For a steady insulated machine, power transfer is tied to the change in stagnation enthalpy, but heat leakage and unsteady stored energy can matter in a real test. If the energy residual is large, do not force it into an unexplained efficiency factor.

**Provisional decision:** Choose nozzle count and jet ratio for a variable-flow high-head site. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `Vjet≈sqrt(2 g H) for lossless nozzle`, reproduce **39.62 m/s ideal** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Modeling an impulse wheel with a sealed reaction draft tube misrepresents the mechanism. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Measure nozzle pressure, jet diameter, needle position and runner rpm. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Choose nozzle count and jet ratio for a variable-flow high-head site. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **V=sqrt(2×9.81×80)**, yielding **39.62 m/s ideal** under the stated simplifications. Actual jet velocity is reduced by nozzle losses. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Pelton buckets exchange impulse with a free jet under near-atmospheric runner pressure. Measure nozzle pressure, jet diameter, needle position and runner rpm. Link one cause to an independent measurement and report uncertainty.

**5.** Choose nozzle count and jet ratio for a variable-flow high-head site. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U06-L04 — Francis and Kaplan reaction runners

**Outcome.** Use conservation laws and appropriate reference stations to analyze **francis and kaplan reaction runners**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.

### 1. Physical setting and governing reasoning

Every turbomachine exchanges energy and momentum through moving surfaces. This lesson isolates one effect while retaining enough of the surrounding machine to prevent an unrealistic interpretation of its result. The shared design brief is: A river scheme has a seasonal flow-duration curve and limited net head; turbine selection must account for civil losses, operating range and environmental constraints. This particular lesson tests how francis and kaplan reaction runners influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** The draft tube decelerates exit flow to recover pressure while protecting against excessive local suction. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `P_hyd=rho g Q H; V_out^2/(2g) quantifies recoverable exit kinetic head`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Impulse turbines use jets and largely atmospheric runner pressure; reaction turbines operate filled with water and need suction-side and draft-tube analysis. Specific speed aids selection only when its numerical unit convention is fixed.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** With outlet velocity 6 m/s, recoverable ideal velocity head is 1.84 m before losses.

**Explicit substitution:** V²/(2g)=6²/(2×9.81); therefore **1.835 m of velocity head**. Recoverable portion is lower because draft tubes dissipate energy.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Counting draft tube ideal recovery as extra gravitational head creates double counting. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Compare draft-tube pressures, downstream water level and cavitation observations. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. The best-efficiency point is merely one location on a map. Startup, shutdown, reduced duty, elevated temperature and equipment aging may create more restrictive limits. A specification should include allowable flow, speed, vibration, pressure and temperature, with a defined trip or mitigation strategy.

**Provisional decision:** Refine runner outlet and draft-tube geometry and compare Kaplan pitch control under sediment and low-tailwater constraints. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `P_hyd=rho g Q H; V_out^2/(2g) quantifies recoverable exit kinetic head`, reproduce **1.835 m of velocity head** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Counting draft tube ideal recovery as extra gravitational head creates double counting. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Compare draft-tube pressures, downstream water level and cavitation observations. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Refine runner outlet and draft-tube geometry and compare Kaplan pitch control under sediment and low-tailwater constraints. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **V²/(2g)=6²/(2×9.81)**, yielding **1.835 m of velocity head** under the stated simplifications. Recoverable portion is lower because draft tubes dissipate energy. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** The draft tube decelerates exit flow to recover pressure while protecting against excessive local suction. Compare draft-tube pressures, downstream water level and cavitation observations. Link one cause to an independent measurement and report uncertainty.

**5.** Refine runner outlet and draft-tube geometry and compare Kaplan pitch control under sediment and low-tailwater constraints. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U06-L05 — Runner specific speed and selection

**Outcome.** Use conservation laws and appropriate reference stations to analyze **runner specific speed and selection**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.

### 1. Physical setting and governing reasoning

Consider the difference between predicting a single performance number and qualifying a rotating machine. This lesson develops one measurable calculation, then asks which assumptions fail outside the demonstration state. The shared design brief is: A river scheme has a seasonal flow-duration curve and limited net head; turbine selection must account for civil losses, operating range and environmental constraints. This particular lesson tests how runner specific speed and selection influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Specific-speed conventions are empirical coordinates for runner families; values differ with units and whether power or flow is used. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `N_s=n sqrt(P)/H^(5/4) with explicitly defined power and unit convention`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A high annual energy yield may come from matching a lower peak-output machine to the site flow-duration curve. Uncertainty in water availability, sediment, ecology and licensing can outweigh the precision of runner optimization.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** Using n=300 rpm, P=500 kW and H=30 m gives a numerical metric about 95.6 in rpm-kW-m convention.

**Explicit substitution:** N_s=300×sqrt(500)/30^1.25; therefore **95.54 (rpm–kW–m convention)**. Specific-speed values from different numerical conventions must not be compared directly.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Comparing numerical specific-speed values from incompatible conventions leads to incorrect equipment selection. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Label every variable and unit convention on selection charts. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. An adverse trend can result from fouling, poor installation, instrumentation drift or genuine wear. Avoid replacing components on the basis of one efficiency number. Compare independent signals such as vibration, temperature, flow, differential pressure and operating history before diagnosing cause.

**Provisional decision:** Shortlist turbine family only after site flow, cavitation and operating range are understood. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `N_s=n sqrt(P)/H^(5/4) with explicitly defined power and unit convention`, reproduce **95.54 (rpm–kW–m convention)** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Comparing numerical specific-speed values from incompatible conventions leads to incorrect equipment selection. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Label every variable and unit convention on selection charts. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Shortlist turbine family only after site flow, cavitation and operating range are understood. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **N_s=300×sqrt(500)/30^1.25**, yielding **95.54 (rpm–kW–m convention)** under the stated simplifications. Specific-speed values from different numerical conventions must not be compared directly. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Specific-speed conventions are empirical coordinates for runner families; values differ with units and whether power or flow is used. Label every variable and unit convention on selection charts. Link one cause to an independent measurement and report uncertainty.

**5.** Shortlist turbine family only after site flow, cavitation and operating range are understood. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

