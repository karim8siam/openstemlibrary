# Unit 08: Performance Testing, Controls and Sustainable Operations

**Course Code**: TBM 308 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Performance Testing, Controls and Sustainable Operations**.

## U08-L01 — Design and off-design performance maps

**Outcome.** Use conservation laws and appropriate reference stations to analyze **design and off-design performance maps**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.

### 1. Physical setting and governing reasoning

An engineer should be able to explain the direction of power transfer before touching a calculator. In this lesson the system boundary encloses the relevant machine component; the chosen inlet and outlet stations are part of the model, not details added after computing a value. The shared design brief is: An operator observes changing efficiency, sensor bias and part-load conditions; improvement requires a traceable test, calibrated instruments, and a defensible economic comparison. This particular lesson tests how design and off-design performance maps influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Best-efficiency points do not persist when flow, speed, fluid properties or vane setting move. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `eta=P_useful/P_input with consistent power boundary`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Lifecycle evaluation integrates duty hours, variable efficiency, maintenance, process downtime, environmental impacts and safety compliance. The chosen control policy should protect against surge, cavitation, overspeed and loss of lubrication before optimizing electricity consumption.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A pump at 32 kW hydraulic and 43 kW shaft power operates at eta≈0.744.

**Explicit substitution:** eta=32/43; therefore **0.7442**. Hydraulic or aerodynamic power and shaft power must share a time boundary.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Joining map points from inconsistent test standards yields a fictitious contour plot. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Use common reference speed and fluid conditions with repeat runs and reported uncertainties. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Identify every mass stream crossing the control volume, including leakage, bleed and cooling injections. For a steady insulated machine, power transfer is tied to the change in stagnation enthalpy, but heat leakage and unsteady stored energy can matter in a real test. If the energy residual is large, do not force it into an unexplained efficiency factor.

**Provisional decision:** Schedule dispatch to favor efficient duty points while respecting stall, NPSH and emissions constraints. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `eta=P_useful/P_input with consistent power boundary`, reproduce **0.7442** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Joining map points from inconsistent test standards yields a fictitious contour plot. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Use common reference speed and fluid conditions with repeat runs and reported uncertainties. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Schedule dispatch to favor efficient duty points while respecting stall, NPSH and emissions constraints. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **eta=32/43**, yielding **0.7442** under the stated simplifications. Hydraulic or aerodynamic power and shaft power must share a time boundary. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Best-efficiency points do not persist when flow, speed, fluid properties or vane setting move. Use common reference speed and fluid conditions with repeat runs and reported uncertainties. Link one cause to an independent measurement and report uncertainty.

**5.** Schedule dispatch to favor efficient duty points while respecting stall, NPSH and emissions constraints. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U08-L02 — Instrumentation and propagated uncertainty

**Outcome.** Use conservation laws and appropriate reference stations to analyze **instrumentation and propagated uncertainty**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.

### 1. Physical setting and governing reasoning

The first challenge is to connect the observed state to a physical balance. A pressure, velocity or temperature measurement alone is incomplete until the flow direction, station definition and performance quantity have been fixed. The shared design brief is: An operator observes changing efficiency, sensor bias and part-load conditions; improvement requires a traceable test, calibrated instruments, and a defensible economic comparison. This particular lesson tests how instrumentation and propagated uncertainty influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Uncertainty is part of any credible efficiency claim, especially when differences are smaller than measurement limits. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `u_y/y≈sqrt((u_Q/Q)^2+(u_H/H)^2) for independent relative errors in Q H`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Performance testing must specify station locations, instrument calibration, fluid properties, operating point, stabilization period and method for reducing raw data. Comparing two efficiencies at unmatched operating states does not prove degradation or improvement.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A product with 2% independent flow error and 1% head error has ≈2.24% relative standard uncertainty.

**Explicit substitution:** u_rel=sqrt(2²+1²); therefore **2.236%**. The root-sum-square is justified only if the errors are independent.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Reporting several decimal places from coarse sensors creates false confidence. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Track calibrations, correlated channels, sampling windows and data rejection criteria. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. The best-efficiency point is merely one location on a map. Startup, shutdown, reduced duty, elevated temperature and equipment aging may create more restrictive limits. A specification should include allowable flow, speed, vibration, pressure and temperature, with a defined trip or mitigation strategy.

**Provisional decision:** Decide if a claimed 1% improvement is statistically distinguishable from test noise. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `u_y/y≈sqrt((u_Q/Q)^2+(u_H/H)^2) for independent relative errors in Q H`, reproduce **2.236%** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Reporting several decimal places from coarse sensors creates false confidence. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Track calibrations, correlated channels, sampling windows and data rejection criteria. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Decide if a claimed 1% improvement is statistically distinguishable from test noise. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **u_rel=sqrt(2²+1²)**, yielding **2.236%** under the stated simplifications. The root-sum-square is justified only if the errors are independent. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Uncertainty is part of any credible efficiency claim, especially when differences are smaller than measurement limits. Track calibrations, correlated channels, sampling windows and data rejection criteria. Link one cause to an independent measurement and report uncertainty.

**5.** Decide if a claimed 1% improvement is statistically distinguishable from test noise. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U08-L03 — Control loops and actuator constraints

**Outcome.** Use conservation laws and appropriate reference stations to analyze **control loops and actuator constraints**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.

### 1. Physical setting and governing reasoning

An apparently simple equipment decision becomes difficult when the operating envelope shifts. Work from conservation laws to a tractable approximation, and only then decide what constitutes evidence for the performance claim. The shared design brief is: An operator observes changing efficiency, sensor bias and part-load conditions; improvement requires a traceable test, calibrated instruments, and a defensible economic comparison. This particular lesson tests how control loops and actuator constraints influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Anti-surge valves, variable guide vanes and bypasses have finite motion time and constraints. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `e(t)=setpoint(t)-measurement(t); P control u=Kp e`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Uncertainty bars are essential where claimed improvements are small. Flow, pressure, temperature, power and corrected operating point can have correlated systematic errors. Apparent decimal precision is not evidence of real precision.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A proportional controller with gain 0.15 per kPa sees 10 kPa error and requests a 1.5 unit actuator correction before saturation.

**Explicit substitution:** Delta u=Kp e=0.15×10; therefore **1.5 actuator units**. Saturation and derivative control are not included in this illustrative P action.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Tuning on a steady map without plant dynamics can cause actuator hunting or unsafe transients. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Validate controlled step tests with trips, saturation and fail-safe state checks. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. An adverse trend can result from fouling, poor installation, instrumentation drift or genuine wear. Avoid replacing components on the basis of one efficiency number. Compare independent signals such as vibration, temperature, flow, differential pressure and operating history before diagnosing cause.

**Provisional decision:** Prioritize a robust safe operating corridor instead of aggressive efficiency-only control. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `e(t)=setpoint(t)-measurement(t); P control u=Kp e`, reproduce **1.5 actuator units** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Tuning on a steady map without plant dynamics can cause actuator hunting or unsafe transients. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Validate controlled step tests with trips, saturation and fail-safe state checks. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Prioritize a robust safe operating corridor instead of aggressive efficiency-only control. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **Delta u=Kp e=0.15×10**, yielding **1.5 actuator units** under the stated simplifications. Saturation and derivative control are not included in this illustrative P action. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Anti-surge valves, variable guide vanes and bypasses have finite motion time and constraints. Validate controlled step tests with trips, saturation and fail-safe state checks. Link one cause to an independent measurement and report uncertainty.

**5.** Prioritize a robust safe operating corridor instead of aggressive efficiency-only control. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U08-L04 — Condition monitoring and degradation diagnosis

**Outcome.** Use conservation laws and appropriate reference stations to analyze **condition monitoring and degradation diagnosis**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.

### 1. Physical setting and governing reasoning

Every turbomachine exchanges energy and momentum through moving surfaces. This lesson isolates one effect while retaining enough of the surrounding machine to prevent an unrealistic interpretation of its result. The shared design brief is: An operator observes changing efficiency, sensor bias and part-load conditions; improvement requires a traceable test, calibrated instruments, and a defensible economic comparison. This particular lesson tests how condition monitoring and degradation diagnosis influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Fouling, erosion and seal leakage produce different patterns in map shifts, vibration and temperatures. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `delta_eta=eta_reference-eta_current at matched corrected state`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Lifecycle evaluation integrates duty hours, variable efficiency, maintenance, process downtime, environmental impacts and safety compliance. The chosen control policy should protect against surge, cavitation, overspeed and loss of lubrication before optimizing electricity consumption.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** Efficiency falling from 0.84 to 0.80 at matched conditions corresponds to 4 percentage points, not 4% relative.

**Explicit substitution:** eta_ref−eta_now=0.84−0.80; therefore **0.04 = 4 percentage points**. Relative decrease is 0.04/0.84≈4.76%, a different statistic.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Comparing different inlet states or flows may falsely label normal off-design change as degradation. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Trend corrected measurements, filters, blade inspections, spectral vibration and maintenance interventions. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Real flow deviates from uniform one-dimensional pictures because of wakes, secondary flow, wall boundary layers and tip leakage. An equation that gives a plausible central value does not establish the distribution over the blade span. This is why credible performance assessment combines integrated measurements with local diagnostics and a transparent loss model.

**Provisional decision:** Schedule cleaning only when recovered output justifies outage and risk. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `delta_eta=eta_reference-eta_current at matched corrected state`, reproduce **0.04 = 4 percentage points** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Comparing different inlet states or flows may falsely label normal off-design change as degradation. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Trend corrected measurements, filters, blade inspections, spectral vibration and maintenance interventions. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Schedule cleaning only when recovered output justifies outage and risk. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **eta_ref−eta_now=0.84−0.80**, yielding **0.04 = 4 percentage points** under the stated simplifications. Relative decrease is 0.04/0.84≈4.76%, a different statistic. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Fouling, erosion and seal leakage produce different patterns in map shifts, vibration and temperatures. Trend corrected measurements, filters, blade inspections, spectral vibration and maintenance interventions. Link one cause to an independent measurement and report uncertainty.

**5.** Schedule cleaning only when recovered output justifies outage and risk. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U08-L05 — Lifecycle assessment and integrated design review

**Outcome.** Use conservation laws and appropriate reference stations to analyze **lifecycle assessment and integrated design review**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.

### 1. Physical setting and governing reasoning

Consider the difference between predicting a single performance number and qualifying a rotating machine. This lesson develops one measurable calculation, then asks which assumptions fail outside the demonstration state. The shared design brief is: An operator observes changing efficiency, sensor bias and part-load conditions; improvement requires a traceable test, calibrated instruments, and a defensible economic comparison. This particular lesson tests how lifecycle assessment and integrated design review influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Lifecycle evaluation needs duty distribution, reliability, spare components, efficiency loss and end-of-life impacts. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `annual_energy=sum_i(P_i t_i); annual_cost=annual_energy tariff`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Performance testing must specify station locations, instrument calibration, fluid properties, operating point, stabilization period and method for reducing raw data. Comparing two efficiencies at unmatched operating states does not prove degradation or improvement.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A 12 kW mean auxiliary load running 5000 h/y uses 60 MWh/y; at $0.12/kWh its electricity cost is $7200/y.

**Explicit substitution:** E=12 kW×5000 h=60,000 kWh; cost=60,000×0.12; therefore **60 MWh and USD 7200 per year**. No discounted cash flow or maintenance cost is included.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Comparing capital costs alone ignores years of operating energy and unplanned outage loss. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Combine load histograms with measured electric draw, carbon factors and uncertainty bounds. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Keep hydraulic or aerodynamic useful power separate from shaft power and electric input. It is possible for a component to improve while the entire installation consumes more electricity due to throttling, controls or auxiliary devices. Show each energy boundary and the associated loss.

**Provisional decision:** Recommend a machine using discounted lifecycle value and verified safety rather than best-point efficiency alone. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `annual_energy=sum_i(P_i t_i); annual_cost=annual_energy tariff`, reproduce **60 MWh and USD 7200 per year** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Comparing capital costs alone ignores years of operating energy and unplanned outage loss. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Combine load histograms with measured electric draw, carbon factors and uncertainty bounds. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Recommend a machine using discounted lifecycle value and verified safety rather than best-point efficiency alone. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **E=12 kW×5000 h=60,000 kWh; cost=60,000×0.12**, yielding **60 MWh and USD 7200 per year** under the stated simplifications. No discounted cash flow or maintenance cost is included. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Lifecycle evaluation needs duty distribution, reliability, spare components, efficiency loss and end-of-life impacts. Combine load histograms with measured electric draw, carbon factors and uncertainty bounds. Link one cause to an independent measurement and report uncertainty.

**5.** Recommend a machine using discounted lifecycle value and verified safety rather than best-point efficiency alone. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

