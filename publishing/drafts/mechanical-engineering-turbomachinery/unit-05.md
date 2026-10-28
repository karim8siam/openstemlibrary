# Unit 05: Gas and Steam Turbines

**Course Code**: TBM 305 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Gas and Steam Turbines**.

## U05-L01 — Gas turbine specific work and power

**Outcome.** Use conservation laws and appropriate reference stations to analyze **gas turbine specific work and power**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.

### 1. Physical setting and governing reasoning

An engineer should be able to explain the direction of power transfer before touching a calculator. In this lesson the system boundary encloses the relevant machine component; the chosen inlet and outlet stations are part of the model, not details added after computing a value. The shared design brief is: A thermal power plant extracts shaft power across a turbine with significant expansion, thermal constraints and changing outlet pressure. This particular lesson tests how gas turbine specific work and power influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** The turbine extracts fluid total enthalpy; shaft output is lower after leakage and mechanical loss. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `P_t=m_dot cp (T01-T02)`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Shaft matching means the turbine must cover compressor power and mechanical auxiliaries with an allowance for losses. Raising firing temperature can improve cycle potential while sharply increasing material, cooling and lifetime requirements.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** Gas with m_dot=18 kg/s, cp=1.15 kJ/(kg K) and a 210 K total-temperature drop develops about 4.35 MW fluid power.

**Explicit substitution:** P=18×1.15×210; therefore **4347 kW = 4.347 MW**. The cp is a given mean value over the temperature interval.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Comparing turbine inlet static temperature with outlet total temperature mixes reference states. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Record mass flow and total temperatures with correct thermocouple recovery assessment. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. The best-efficiency point is merely one location on a map. Startup, shutdown, reduced duty, elevated temperature and equipment aging may create more restrictive limits. A specification should include allowable flow, speed, vibration, pressure and temperature, with a defined trip or mitigation strategy.

**Provisional decision:** Choose expansion stages and shaft matching for required net delivered power. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `P_t=m_dot cp (T01-T02)`, reproduce **4347 kW = 4.347 MW** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Comparing turbine inlet static temperature with outlet total temperature mixes reference states. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Record mass flow and total temperatures with correct thermocouple recovery assessment. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Choose expansion stages and shaft matching for required net delivered power. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **P=18×1.15×210**, yielding **4347 kW = 4.347 MW** under the stated simplifications. The cp is a given mean value over the temperature interval. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** The turbine extracts fluid total enthalpy; shaft output is lower after leakage and mechanical loss. Record mass flow and total temperatures with correct thermocouple recovery assessment. Link one cause to an independent measurement and report uncertainty.

**5.** Choose expansion stages and shaft matching for required net delivered power. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U05-L02 — Turbine isentropic efficiency

**Outcome.** Use conservation laws and appropriate reference stations to analyze **turbine isentropic efficiency**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.

### 1. Physical setting and governing reasoning

The first challenge is to connect the observed state to a physical balance. A pressure, velocity or temperature measurement alone is incomplete until the flow direction, station definition and performance quantity have been fixed. The shared design brief is: A thermal power plant extracts shaft power across a turbine with significant expansion, thermal constraints and changing outlet pressure. This particular lesson tests how turbine isentropic efficiency influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Turbine efficiency is actual enthalpy drop divided by ideal drop at the same inlet state and exit pressure. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `eta_t=(T01-T02)/(T01-T02s) for calorically perfect gas`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A turbine extracts stagnation enthalpy from a high-energy stream. In an axial turbine, a stator nozzle may accelerate flow, while the rotor converts angular momentum change to shaft torque. Cooling and bleed flows make a simple constant-mass model incomplete.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** With T01=1100 K, T02=900 K and ideal T02s=865 K, turbine efficiency is about 0.851.

**Explicit substitution:** eta_t=(1100−900)/(1100−865)=200/235; therefore **0.8511**. For a turbine the actual enthalpy drop is less than ideal.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Taking the reciprocal compressor definition for a turbine can generate efficiency above unity. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Measure total pressure at suitable stations and use property consistency when cp varies. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. An adverse trend can result from fouling, poor installation, instrumentation drift or genuine wear. Avoid replacing components on the basis of one efficiency number. Compare independent signals such as vibration, temperature, flow, differential pressure and operating history before diagnosing cause.

**Provisional decision:** Assess whether heat transfer, cooling injection or leaks invalidate simple single-stream treatment. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `eta_t=(T01-T02)/(T01-T02s) for calorically perfect gas`, reproduce **0.8511** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Taking the reciprocal compressor definition for a turbine can generate efficiency above unity. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Measure total pressure at suitable stations and use property consistency when cp varies. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Assess whether heat transfer, cooling injection or leaks invalidate simple single-stream treatment. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **eta_t=(1100−900)/(1100−865)=200/235**, yielding **0.8511** under the stated simplifications. For a turbine the actual enthalpy drop is less than ideal. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Turbine efficiency is actual enthalpy drop divided by ideal drop at the same inlet state and exit pressure. Measure total pressure at suitable stations and use property consistency when cp varies. Link one cause to an independent measurement and report uncertainty.

**5.** Assess whether heat transfer, cooling injection or leaks invalidate simple single-stream treatment. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U05-L03 — Impulse, reaction and stage velocity triangles

**Outcome.** Use conservation laws and appropriate reference stations to analyze **impulse, reaction and stage velocity triangles**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.

### 1. Physical setting and governing reasoning

An apparently simple equipment decision becomes difficult when the operating envelope shifts. Work from conservation laws to a tractable approximation, and only then decide what constitutes evidence for the performance claim. The shared design brief is: A thermal power plant extracts shaft power across a turbine with significant expansion, thermal constraints and changing outlet pressure. This particular lesson tests how impulse, reaction and stage velocity triangles influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Nozzle acceleration and rotor expansion distribute pressure change and turning differently in impulse and reaction stages. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `w_extracted=U1 Vtheta1 - U2 Vtheta2`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Turbine isentropic efficiency uses actual drop divided by ideal drop at equal inlet and outlet pressures. Wet steam is not a calorically perfect ideal gas; quality and enthalpy must come from trustworthy steam-property data. Blade erosion and moisture impact must be considered separately from nominal efficiency.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** At constant U=240 m/s, inlet whirl=160 m/s and exit whirl=-40 m/s, extraction is 48 kJ/kg.

**Explicit substitution:** w=240×160−240×(−40); therefore **48,000 J/kg**. Rotor extracts power; outlet counter-swirl increases extracted work.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Equal velocity triangles do not imply equal losses if blade speed and stage pressure distribution differ. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Compare measured vane exit angle, rotor exit swirl and loss coefficients. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Real flow deviates from uniform one-dimensional pictures because of wakes, secondary flow, wall boundary layers and tip leakage. An equation that gives a plausible central value does not establish the distribution over the blade span. This is why credible performance assessment combines integrated measurements with local diagnostics and a transparent loss model.

**Provisional decision:** Select an aerodynamic loading split consistent with structural and cooling limits. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `w_extracted=U1 Vtheta1 - U2 Vtheta2`, reproduce **48,000 J/kg** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Equal velocity triangles do not imply equal losses if blade speed and stage pressure distribution differ. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Compare measured vane exit angle, rotor exit swirl and loss coefficients. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Select an aerodynamic loading split consistent with structural and cooling limits. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **w=240×160−240×(−40)**, yielding **48,000 J/kg** under the stated simplifications. Rotor extracts power; outlet counter-swirl increases extracted work. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Nozzle acceleration and rotor expansion distribute pressure change and turning differently in impulse and reaction stages. Compare measured vane exit angle, rotor exit swirl and loss coefficients. Link one cause to an independent measurement and report uncertainty.

**5.** Select an aerodynamic loading split consistent with structural and cooling limits. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U05-L04 — Steam expansion, quality and moisture

**Outcome.** Use conservation laws and appropriate reference stations to analyze **steam expansion, quality and moisture**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.

### 1. Physical setting and governing reasoning

Every turbomachine exchanges energy and momentum through moving surfaces. This lesson isolates one effect while retaining enough of the surrounding machine to prevent an unrealistic interpretation of its result. The shared design brief is: A thermal power plant extracts shaft power across a turbine with significant expansion, thermal constraints and changing outlet pressure. This particular lesson tests how steam expansion, quality and moisture influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Expansion into the two-phase region can erode downstream blades and increase aerodynamic loss. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `h_mix=x h_g+(1-x) h_f at saturation`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

Shaft matching means the turbine must cover compressor power and mechanical auxiliaries with an allowance for losses. Raising firing temperature can improve cycle potential while sharply increasing material, cooling and lifetime requirements.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** At x=0.90, hg=2600 kJ/kg and hf=200 kJ/kg, mixture enthalpy is 2360 kJ/kg.

**Explicit substitution:** h=0.90×2600+0.10×200; therefore **2360 kJ/kg**. Saturation quality is mass fraction of vapor.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Using vapor quality as a volume fraction or extrapolating ideal-gas formulas into wet steam is incorrect. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Use validated steam tables, exit pressure, moisture measurement and stage erosion inspection. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. Keep hydraulic or aerodynamic useful power separate from shaft power and electric input. It is possible for a component to improve while the entire installation consumes more electricity due to throttling, controls or auxiliary devices. Show each energy boundary and the associated loss.

**Provisional decision:** Set reheat or exhaust condition to limit downstream wetness. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `h_mix=x h_g+(1-x) h_f at saturation`, reproduce **2360 kJ/kg** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Using vapor quality as a volume fraction or extrapolating ideal-gas formulas into wet steam is incorrect. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Use validated steam tables, exit pressure, moisture measurement and stage erosion inspection. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Set reheat or exhaust condition to limit downstream wetness. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **h=0.90×2600+0.10×200**, yielding **2360 kJ/kg** under the stated simplifications. Saturation quality is mass fraction of vapor. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Expansion into the two-phase region can erode downstream blades and increase aerodynamic loss. Use validated steam tables, exit pressure, moisture measurement and stage erosion inspection. Link one cause to an independent measurement and report uncertainty.

**5.** Set reheat or exhaust condition to limit downstream wetness. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

## U05-L05 — Turbine cooling and net cycle balance

**Outcome.** Use conservation laws and appropriate reference stations to analyze **turbine cooling and net cycle balance**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.

### 1. Physical setting and governing reasoning

Consider the difference between predicting a single performance number and qualifying a rotating machine. This lesson develops one measurable calculation, then asks which assumptions fail outside the demonstration state. The shared design brief is: A thermal power plant extracts shaft power across a turbine with significant expansion, thermal constraints and changing outlet pressure. This particular lesson tests how turbine cooling and net cycle balance influences the balance among useful power, operating stability, mechanical limits and lifetime expense. The model applies only to its stated fluid and duty conditions.

**Physical mechanism:** Cooling and bleed flows change both turbine thermodynamics and available work; thermal protection trades against performance. Mark the control-volume stations, flow direction, shaft boundary and whether the stated measurements use absolute or relative velocity, total or static state.

### 2. Model and derivation

**Core equation:** `P_net=P_turbine-P_compressor-P_aux`.

The equation follows from the appropriate balance of energy, mass or angular momentum. Define the inlet, outlet and reference frame first; state whether an efficiency uses fluid, shaft or electric power and whether a pressure is static or total.

A turbine extracts stagnation enthalpy from a high-energy stream. In an axial turbine, a stator nozzle may accelerate flow, while the rotor converts angular momentum change to shaft torque. Cooling and bleed flows make a simple constant-mass model incomplete.

Check dimensions: J/kg = m²/s², hydraulic head uses metres, efficiency is dimensionless, and torque times rad/s gives watts.

### 3. Worked example and sensitivity

**Teaching case:** A 12 MW turbine driving a 7.5 MW compressor and 0.4 MW auxiliaries leaves 4.1 MW net before electrical losses.

**Explicit substitution:** P_net=12−7.5−0.4; therefore **4.1 MW**. Generator and other downstream electrical losses not included.

Check arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.

### 4. Loss mechanisms, diagnostics and design limits

**Critical misconception:** Subtracting compressor power but omitting coolant bleed and accessory loads overstates net output. Consider off-design incidence, leakage, wakes and local mechanical or thermal limits; different machine types have distinct damage mechanisms.

**Test evidence:** Account for all mass branches, cooling temperature, shaft torque and generator losses. Record calibration and uncertainty, check the station definitions, and separate real losses from sensor or operating-point differences. When comparing before-and-after tests, hold corrected flow or an equivalent meaningful operating state close enough that changing duty does not masquerade as better hardware. Temperature and gas composition influence corrected variables, while a hydraulic network may change substantially with valve setting. State the comparison tolerance rather than assuming curves can be overlaid without adjustment.

**Provisional decision:** Evaluate turbine inlet temperature increases jointly with material and cooling limits. Revise this recommendation if an independently verified safety or stability constraint is violated.

### 5. Assessment (five tasks)

1. **Calculation:** Using `P_net=P_turbine-P_compressor-P_aux`, reproduce **4.1 MW** and show every unit conversion. Explain why the chosen sign convention is necessary.
2. **Design variation:** Perturb the dominant flow, temperature, speed or head input by 10% and recompute. Which physical assumption fails first at a very different duty point?
3. **Failure investigation:** Use this misconception as the starting hypothesis: Subtracting compressor power but omitting coolant bleed and accessory loads overstates net output. Propose an alternative explanation and one observation that distinguishes the two.
4. **Measurement plan:** Operationalize this requirement: Account for all mass branches, cooling temperature, shaft torque and generator losses. State one calibration check, one expected systematic error and how results are normalized to the same operating state.
5. **Decision memo:** Evaluate the provisional change: Evaluate turbine inlet temperature increases jointly with material and cooling limits. Identify a constraint or observation that would force the opposite decision.

### 6. Worked-answer guidance

**1.** The substitution is **P_net=12−7.5−0.4**, yielding **4.1 MW** under the stated simplifications. Generator and other downstream electrical losses not included. A complete answer identifies pressure, temperature and rotor-frame conventions where relevant.

**2.** Apply the functional dependence of the displayed relation and calculate the changed case. State whether the perturbation preserves the real operating point; update thermodynamic properties if needed.

**3–4.** Cooling and bleed flows change both turbine thermodynamics and available work; thermal protection trades against performance. Account for all mass branches, cooling temperature, shaft torque and generator losses. Link one cause to an independent measurement and report uncertainty.

**5.** Evaluate turbine inlet temperature increases jointly with material and cooling limits. It is provisional pending independent safety, structural and performance review.

**Status:** All values are invented classroom inputs; this chapter is not a measured field study, machine certification or safe operating procedure.


---

