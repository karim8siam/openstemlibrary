# Unit 2: Fluid Statics and Hydrostatic Forces

# Pressure, head and hydrostatic equilibrium

## Unit 2, Lesson 1 — Pressure, head and hydrostatic equilibrium

### Physical question and learning outcome

A static fluid element has zero net force. With z measured upward and constant density, dp/dz=−ρg. Pressure head p/(ρg) is convenient in liquid systems; however pressure is not itself an elevation. Absolute pressure includes atmospheric pressure and cannot be negative for an ordinary equilibrium fluid.

The reader should be able to describe **pressure, head and hydrostatic equilibrium** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **fluid statics and hydrostatic forces**.

### Governing statement and assumptions

**Working relationship:** `p₂−p₁ = ρg(z₁−z₂)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

At 3.0 m depth in still water, gauge pressure ≈1000×9.81×3=29.43 kPa.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Applying a pressure-depth formula across a density-stratified layer without integration.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **pressure, head and hydrostatic equilibrium**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Applying a pressure-depth formula across a density-stratified layer without integration.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** What changes if both the top and bottom pressures are expressed as absolute pressure? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Dimensional homogeneity and similarity** and then to **Manometers and differential pressure**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Manometers and differential pressure

## Unit 2, Lesson 2 — Manometers and differential pressure

### Physical question and learning outcome

A liquid manometer converts pressure differences into vertical column lengths. Traversing the connected fluid columns with a consistent sign convention yields pressure changes. A differential manometer with a denser manometric fluid has a simple formula only for a specific geometry and equal-elevation taps.

The reader should be able to describe **manometers and differential pressure** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **fluid statics and hydrostatic forces**.

### Governing statement and assumptions

**Working relationship:** `Δp=(ρm−ρf)gΔh (equal-level taps, two liquids)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

With ρm=13600, ρf=1000 kg/m³ and Δh=0.05 m: Δp≈6.18 kPa.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Using Δp=ρm g h where the displaced process-fluid columns matter.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **manometers and differential pressure**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Using Δp=ρm g h where the displaced process-fluid columns matter.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** Why might air bubbles or capillary menisci invalidate a precise reading? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Pressure, head and hydrostatic equilibrium** and then to **Forces on plane submerged surfaces**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Forces on plane submerged surfaces

## Unit 2, Lesson 3 — Forces on plane submerged surfaces

### Physical question and learning outcome

A submerged surface receives a spatially varying normal load. Integration gives resultant R=ρg h̄A for a plane wholly below a constant-pressure free surface when h̄ is centroid depth and gauge pressure is used. The center of pressure is generally deeper than the centroid for a tilted or vertical plane.

The reader should be able to describe **forces on plane submerged surfaces** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **fluid statics and hydrostatic forces**.

### Governing statement and assumptions

**Working relationship:** `R=ρg h̄ A; h_cp=h̄+I_G sin²θ/(h̄A)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

A 1 m² vertical plate with centroid 2 m deep has hydrostatic resultant R≈19.62 kN.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Putting the resultant at the centroid even though the pressure field grows with depth.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **forces on plane submerged surfaces**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Putting the resultant at the centroid even though the pressure field grows with depth.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** Why is a center-of-pressure calculation essential when finding hinge torque? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Manometers and differential pressure** and then to **Buoyancy, floatation and metacentric stability**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Buoyancy, floatation and metacentric stability

## Unit 2, Lesson 4 — Buoyancy, floatation and metacentric stability

### Physical question and learning outcome

The net hydrostatic force on a submerged body is upward by the weight of displaced fluid, provided gravity and density are suitably uniform. Floating equilibrium requires displaced-fluid weight to match total weight. A floating hull may still be unstable in roll; small-angle metacentric arguments rely on a waterplane geometry and are not a substitute for full stability analysis.

The reader should be able to describe **buoyancy, floatation and metacentric stability** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **fluid statics and hydrostatic forces**.

### Governing statement and assumptions

**Working relationship:** `F_B=ρfluid gVdisplaced`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

A body displacing 0.015 m³ of water receives F_B≈147.15 N.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Assuming a heavy object cannot float or claiming positive buoyant force automatically ensures rotational stability.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **buoyancy, floatation and metacentric stability**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Assuming a heavy object cannot float or claiming positive buoyant force automatically ensures rotational stability.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** How does seawater density affect the draft for the same ship loading? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Forces on plane submerged surfaces** and then to **Curved-surface forces and hydraulic devices**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Curved-surface forces and hydraulic devices

## Unit 2, Lesson 5 — Curved-surface forces and hydraulic devices

### Physical question and learning outcome

A curved surface has varying pressure directions. Resolve the integrated pressure force into horizontal and vertical components: the horizontal force corresponds to a vertical projection, while the vertical component connects to the weight of an imaginary fluid volume above the surface under the stated geometry. Hydraulic actuators transfer pressure but do not create energy.

The reader should be able to describe **curved-surface forces and hydraulic devices** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **fluid statics and hydrostatic forces**.

### Governing statement and assumptions

**Working relationship:** `F_out/F_in=A_out/A_in (ideal connected static hydraulic system)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

Ideal pistons with area ratio 12 receive F_in=150 N and produce F_out=1800 N; the output travel is 1/12 the input travel.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Ignoring friction, seal leakage, system compliance and actuator pressure limits.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **curved-surface forces and hydraulic devices**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Ignoring friction, seal leakage, system compliance and actuator pressure limits.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** What experimental test would reveal if an actuator departs from ideal Pascal-law behavior? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Buoyancy, floatation and metacentric stability** and then to **the next unit’s subject**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

