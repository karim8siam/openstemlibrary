# Unit 3: Fluid Kinematics and Conservation of Mass

# Eulerian and Lagrangian descriptions

## Unit 3, Lesson 1 — Eulerian and Lagrangian descriptions

### Physical question and learning outcome

Eulerian fields assign velocity and pressure to each spatial position and time; Lagrangian trajectories follow individual particles. A streamline is tangent to the instantaneous velocity vector, while a pathline traces a particle history. A streakline collects particles that crossed a designated release location at different times. In unsteady flow the three objects generally differ.

The reader should be able to describe **eulerian and lagrangian descriptions** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **fluid kinematics and conservation of mass**.

### Governing statement and assumptions

**Working relationship:** `Dφ/Dt=∂φ/∂t+u·∇φ`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

For u(x)=2x s⁻¹ in one dimension and steady temperature T(x)=300+5x K: DT/Dt=u dT/dx=10x K/s.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Equating zero local time derivative with zero change experienced by a moving fluid parcel.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **eulerian and lagrangian descriptions**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Equating zero local time derivative with zero change experienced by a moving fluid parcel.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** When can a streamline image be interpreted as a particle trajectory? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Curved-surface forces and hydraulic devices** and then to **Streamlines, vorticity and circulation**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Streamlines, vorticity and circulation

## Unit 3, Lesson 2 — Streamlines, vorticity and circulation

### Physical question and learning outcome

Vorticity is curl of velocity and characterizes local rotation; a visibly curved streamline is not necessarily evidence of nonzero vorticity. Circulation is a line integral of tangential velocity around a closed contour. A potential flow can have circulation around an excluded vortex core despite zero vorticity where the potential model is smooth.

The reader should be able to describe **streamlines, vorticity and circulation** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **fluid kinematics and conservation of mass**.

### Governing statement and assumptions

**Working relationship:** `ω=∇×u; Γ=∮u·dl`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

For a solid-body rotation uθ=Ωr with Ω=4 s⁻¹, axial vorticity is 2Ω=8 s⁻¹.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Mistaking swirl, vorticity, turbulence and streamline curvature as interchangeable concepts.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **streamlines, vorticity and circulation**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Mistaking swirl, vorticity, turbulence and streamline curvature as interchangeable concepts.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** What measurement grid is required to estimate a two-dimensional vorticity field? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Eulerian and Lagrangian descriptions** and then to **Volume flow, mass flow and continuity**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Volume flow, mass flow and continuity

## Unit 3, Lesson 3 — Volume flow, mass flow and continuity

### Physical question and learning outcome

Flow rate through an area is the integral of the velocity component normal to the surface. In a duct using average axial speed, Q=A V̄; mass flow is ṁ=ρQ for uniform density at the section. If density varies, integrate ρu·n over the section instead of pulling density outside without justification.

The reader should be able to describe **volume flow, mass flow and continuity** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **fluid kinematics and conservation of mass**.

### Governing statement and assumptions

**Working relationship:** `Q=∫A u·n dA; ṁ=ρQ (uniform section density)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

A pipe of diameter 0.08 m with average speed 2 m/s carries Q=π(0.08)²×2/4≈0.01005 m³/s.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Using centerline speed as area-average speed in laminar flow.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **volume flow, mass flow and continuity**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Using centerline speed as area-average speed in laminar flow.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** How does measured mean velocity change when diameter doubles at constant volumetric flow? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Streamlines, vorticity and circulation** and then to **Control-volume mass balances and junctions**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Control-volume mass balances and junctions

## Unit 3, Lesson 4 — Control-volume mass balances and junctions

### Physical question and learning outcome

Mass enters and leaves a control volume and can accumulate within it. The steady-state relation Σṁ_in=Σṁ_out is not valid during tank filling unless accumulation is negligible. Branch networks must use consistent signed directions; reverse flow appears as a negative flux under the chosen convention.

The reader should be able to describe **control-volume mass balances and junctions** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **fluid kinematics and conservation of mass**.

### Governing statement and assumptions

**Working relationship:** `d/dt∫CVρdV+∮CSρu·n dA=0`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

At steady state, 6 kg/s enters a junction and 2 kg/s leaves one outlet; the other must carry 4 kg/s outward.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Suppressing storage terms in transient situations or quietly changing sign conventions mid-calculation.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **control-volume mass balances and junctions**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Suppressing storage terms in transient situations or quietly changing sign conventions mid-calculation.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** How could the sign of a measured branch flow diagnose an unexpected valve configuration? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Volume flow, mass flow and continuity** and then to **Compressible continuity and flow measurement**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Compressible continuity and flow measurement

## Unit 3, Lesson 5 — Compressible continuity and flow measurement

### Physical question and learning outcome

In a steady one-inlet, one-outlet streamtube, ρ₁A₁V₁=ρ₂A₂V₂. Incompressible treatment of gases can fail when significant density change occurs. Orifice, venturi and pitot methods infer flow from pressure differences only after accounting for model assumptions and calibration coefficients.

The reader should be able to describe **compressible continuity and flow measurement** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **fluid kinematics and conservation of mass**.

### Governing statement and assumptions

**Working relationship:** `ρ₁A₁V₁=ρ₂A₂V₂`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

If air density halves and the area is unchanged in steady one-dimensional flow with fixed ṁ, the mean speed doubles.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Applying the incompressible pitot relation at high Mach number without a compressible correction.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **compressible continuity and flow measurement**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Applying the incompressible pitot relation at high Mach number without a compressible correction.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** What independent measurement would best validate an inferred flow rate? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Control-volume mass balances and junctions** and then to **the next unit’s subject**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

