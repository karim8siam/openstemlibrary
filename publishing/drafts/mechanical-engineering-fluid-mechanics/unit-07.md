# Unit 7: Pumps, Turbomachinery and Open-Channel Flow

# Pump curves, hydraulic power and efficiency

## Unit 7, Lesson 1 — Pump curves, hydraulic power and efficiency

### Physical question and learning outcome

A centrifugal pump head normally falls as volumetric discharge increases at fixed speed. Hydraulic power is ρgQH and input power is greater by the inverse of appropriate efficiency. Electric-to-water efficiency may differ substantially from pump-only efficiency. A maximum-efficiency point is an operating region, not necessarily the system duty point.

The reader should be able to describe **pump curves, hydraulic power and efficiency** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **pumps, turbomachinery and open-channel flow**.

### Governing statement and assumptions

**Working relationship:** `P_h=ρgQH; P_in=P_h/η`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

Water at Q=0.020 m³/s and H=15 m needs 2.943 kW hydraulic power; at η=0.70 input is about 4.20 kW.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Confusing liters per second with cubic meters per second or treating 70% pump efficiency as overall motor-to-water efficiency.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **pump curves, hydraulic power and efficiency**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Confusing liters per second with cubic meters per second or treating 70% pump efficiency as overall motor-to-water efficiency.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** What happens to input power if fouling makes the pump operate at a lower-efficiency point? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Flow around immersed objects and experimental coefficients** and then to **Pump affinity laws and operating-point shifts**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Pump affinity laws and operating-point shifts

## Unit 7, Lesson 2 — Pump affinity laws and operating-point shifts

### Physical question and learning outcome

For geometrically similar operation at approximately constant efficiency, pump affinity rules connect speed to flow, head and power. They are useful estimates, not guarantees when Reynolds effects, cavitation or motor limits shift. Pumps connected in parallel add flow at a shared head; pumps in series add head at shared flow.

The reader should be able to describe **pump affinity laws and operating-point shifts** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **pumps, turbomachinery and open-channel flow**.

### Governing statement and assumptions

**Working relationship:** `Q∝N; H∝N²; P∝N³ (similarity approximation)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

If speed rises by 10%, approximate head rises by 1.1²=1.21 and power by 1.1³=1.331.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Applying affinity powers to fixed-system operating points without recomputing the intersection with the system curve.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **pump affinity laws and operating-point shifts**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Applying affinity powers to fixed-system operating points without recomputing the intersection with the system curve.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** Why can variable-speed control save energy when throttling a pump? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Pump curves, hydraulic power and efficiency** and then to **Cavitation and net positive suction head**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Cavitation and net positive suction head

## Unit 7, Lesson 3 — Cavitation and net positive suction head

### Physical question and learning outcome

Net positive suction head available is the pump inlet absolute total head above vapor-pressure head under a chosen datum. Available NPSH must exceed pump requirements with appropriate engineering margin over the operating envelope. Pressure, altitude, liquid temperature, suction lift and friction all matter. A simple NPSH formula is a screening tool, not an empirical cavitation qualification.

The reader should be able to describe **cavitation and net positive suction head** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **pumps, turbomachinery and open-channel flow**.

### Governing statement and assumptions

**Working relationship:** `NPSH_A=(p_surface,abs−p_vapor)/(ρg)+z_surface−z_pump−h_f,suction`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

For water with (p_surface−p_vapor)/(ρg)=10 m, elevation difference −2 m and suction loss 1 m, NPSH_A=7 m.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Using atmospheric gauge pressure instead of absolute surface pressure, or claiming cavitation is impossible because the bulk liquid is below its boiling temperature.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **cavitation and net positive suction head**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Using atmospheric gauge pressure instead of absolute surface pressure, or claiming cavitation is impossible because the bulk liquid is below its boiling temperature.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** What happens to NPSH available when suction temperature rises? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Pump affinity laws and operating-point shifts** and then to **Turbines and angular-momentum transfer**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Turbines and angular-momentum transfer

## Unit 7, Lesson 4 — Turbines and angular-momentum transfer

### Physical question and learning outcome

A hydraulic turbine extracts head and produces shaft power. The net mechanical head drop between upstream and downstream stations supplies an upper bound; actual output depends on hydraulic and mechanical losses. For rotating devices Euler-type angular-momentum analysis relates specific work to tangential velocity and blade speed. Site flows and seasonal changes influence turbine selection.

The reader should be able to describe **turbines and angular-momentum transfer** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **pumps, turbomachinery and open-channel flow**.

### Governing statement and assumptions

**Working relationship:** `P_out=ηρgQH (defined water-to-shaft efficiency)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

At Q=2 m³/s, H=8 m and η=0.80, turbine shaft power is about 125.6 kW.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Using rated efficiency for an entire changing operating envelope or forgetting environmental flow requirements.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **turbines and angular-momentum transfer**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Using rated efficiency for an entire changing operating envelope or forgetting environmental flow requirements.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** Why might a low-head turbine require a very different runner than a high-head one? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Cavitation and net positive suction head** and then to **Open-channel specific energy and hydraulic jumps**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Open-channel specific energy and hydraulic jumps

## Unit 7, Lesson 5 — Open-channel specific energy and hydraulic jumps

### Physical question and learning outcome

Specific energy relative to the channel bottom is E=y+V²/(2g) for steady one-dimensional analysis. Critical flow arises near a minimum in E for fixed Q and geometry. A hydraulic jump can occur when rapid supercritical flow transitions to deeper subcritical flow, dissipating mechanical energy. Momentum, not lossless Bernoulli, is often the useful jump balance.

The reader should be able to describe **open-channel specific energy and hydraulic jumps** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **pumps, turbomachinery and open-channel flow**.

### Governing statement and assumptions

**Working relationship:** `Fr=V/√(gy) (rectangular channel hydraulic depth y)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

At V=3 m/s, y=0.25 m, Fr≈1.92, indicating supercritical flow in this idealized rectangular channel.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Assuming every surface ripple has the same relevance as a hydraulic jump or applying pipe Re thresholds to open-channel regime.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **open-channel specific energy and hydraulic jumps**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Assuming every surface ripple has the same relevance as a hydraulic jump or applying pipe Re thresholds to open-channel regime.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** Which observations distinguish supercritical from subcritical water surface behavior? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Turbines and angular-momentum transfer** and then to **the next unit’s subject**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

