# Unit 5: Viscous Internal Flow and Pipe Networks

# Reynolds number and transition

## Unit 5, Lesson 1 — Reynolds number and transition

### Physical question and learning outcome

Re measures inertial-to-viscous effects based on a chosen characteristic length. In round pipes, approximately Re<2300 is often used as a practical laminar regime indicator; turbulent behavior is typical well above transition, but inlet disturbances and roughness affect the onset. Reynolds numbers for wings, jets and channels cannot be classified using a single pipe threshold.

The reader should be able to describe **reynolds number and transition** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **viscous internal flow and pipe networks**.

### Governing statement and assumptions

**Working relationship:** `Re=ρVD/μ`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

For water ρ=1000 kg/m³, V=0.15 m/s, D=0.02 m, μ=0.001 Pa·s: Re=3000 (transitional estimate).

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Automatically using turbulent correlations in the transitional region with high confidence.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **reynolds number and transition**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Automatically using turbulent correlations in the transitional region with high confidence.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** How do temperature-driven viscosity changes shift regime at constant Q? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Angular momentum and swirling flows** and then to **Laminar pipe flow and Hagen–Poiseuille law**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Laminar pipe flow and Hagen–Poiseuille law

## Unit 5, Lesson 2 — Laminar pipe flow and Hagen–Poiseuille law

### Physical question and learning outcome

An ideal steady Newtonian laminar fully developed flow in a circular tube has a parabolic velocity distribution, with centerline velocity twice mean velocity. The pressure drop is proportional to length and viscosity but inversely proportional to the fourth power of radius at fixed flow. Entrance and exit losses can matter in very short tubes.

The reader should be able to describe **laminar pipe flow and hagen–poiseuille law** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **viscous internal flow and pipe networks**.

### Governing statement and assumptions

**Working relationship:** `Δp=128 μLQ/(πD⁴); f_D=64/Re`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

With μ=0.001 Pa·s, L=5 m, Q=1×10⁻⁵ m³/s and D=0.01 m: Δp≈204 Pa; verify Reynolds regime before trusting the number.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Applying Poiseuille to turbulent flow or forgetting the fourth-power diameter sensitivity.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **laminar pipe flow and hagen–poiseuille law**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Applying Poiseuille to turbulent flow or forgetting the fourth-power diameter sensitivity.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** Why can a tiny diameter measurement error dominate the result? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Reynolds number and transition** and then to **Turbulence, roughness and friction factors**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Turbulence, roughness and friction factors

## Unit 5, Lesson 3 — Turbulence, roughness and friction factors

### Physical question and learning outcome

The Darcy–Weisbach expression converts a dimensionless Darcy friction factor to head loss. In turbulent pipes friction factor depends on Reynolds number and relative roughness; Colebrook-type relations are empirical approximations. Fully rough behavior loses sensitivity to Reynolds number at sufficiently high Re. Minor-loss coefficients also change with fitting geometry and sometimes Re.

The reader should be able to describe **turbulence, roughness and friction factors** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **viscous internal flow and pipe networks**.

### Governing statement and assumptions

**Working relationship:** `h_f=f_D(L/D)V²/(2g)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

If f_D=0.025, L=40 m, D=0.08 m and V=2 m/s, h_f≈2.55 m.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Using a Fanning friction factor directly in the Darcy formula, underpredicting by a factor near four.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **turbulence, roughness and friction factors**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Using a Fanning friction factor directly in the Darcy formula, underpredicting by a factor near four.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** How would a more accurate inner-diameter survey improve the prediction? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Laminar pipe flow and Hagen–Poiseuille law** and then to **Minor losses and fittings**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Minor losses and fittings

## Unit 5, Lesson 4 — Minor losses and fittings

### Physical question and learning outcome

Bends, contractions, expansions and valves change the pressure and velocity field. The local-loss form h_m=K V_ref²/(2g) uses a defined reference speed; K is not universal and often depends on configuration and flow regime. Equivalent-length methods are helpful only if the underlying friction factor and reference diameter are consistent.

The reader should be able to describe **minor losses and fittings** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **viscous internal flow and pipe networks**.

### Governing statement and assumptions

**Working relationship:** `h_m=K V²/(2g)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

For K=1.5 and V=3 m/s, local head loss is 1.5×9/(19.62)≈0.688 m.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Adding an expansion loss calculated with downstream V to another term based on upstream V without identifying conventions.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **minor losses and fittings**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Adding an expansion loss calculated with downstream V to another term based on upstream V without identifying conventions.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** Why might the same valve have different K values at different openings? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Turbulence, roughness and friction factors** and then to **Networks and system curves**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

# Networks and system curves

## Unit 5, Lesson 5 — Networks and system curves

### Physical question and learning outcome

Pipes in series carry a common flow at steady state, while parallel branches share endpoint head difference under appropriate connection conditions. Network solutions combine continuity and nonlinear resistance equations. The operating point is an intersection between required system head and available pump head, not automatically the pump nameplate flow.

The reader should be able to describe **networks and system curves** using a diagram, distinguish the primary observed quantity from the inferred response, use the equation below with compatible SI units, and explain one condition under which the result may fail. The relevant boundary can be a portion of water in a reservoir, fluid inside a duct, a freely moving external-flow body, or a test rig. Describe the boundary before inserting numbers: an unknown pressure, mass flux or force will have a different meaning when the boundary changes. This topic sits within the larger unit on **viscous internal flow and pipe networks**.

### Governing statement and assumptions

**Working relationship:** `H_system(Q)=H_static+aQ² (illustrative turbulent approximation)`.

Identify each symbol before substitution. Ask whether velocity denotes centerline, cross-sectional mean, tangential or free-stream speed. Determine whether pressure is gauge, absolute, static or stagnation pressure. Note whether the geometric length is pipe bore, vertical depth, capillary radius or another reference dimension. A dimensionless correlation is not interchangeable with a conservation principle: its coefficient can be specific to flow regime, geometry and experimental calibration. Classify the working statement as an exact balance, a constitutive law, a mathematical definition or an idealized empirical approximation. If a term is neglected, justify that omission with order-of-magnitude reasoning where possible.

Study sensitivity by changing one input over a justified range, but reconsider the regime: velocity, Reynolds number, friction factor, and density may change together. A one-parameter classroom model does not establish equipment performance.

### Worked illustrative example

If static head is 8 m and losses are 2 m at Q=0.010 m³/s, assuming Q² scaling gives H≈16 m at Q=0.020 m³/s.

To reconstruct the calculation, first express inputs in base SI units, write the symbolic relationship, replace symbols with measured or stated quantities, retain units through arithmetic, and round only at the end. Assess whether the magnitude is physically sensible. Where useful, reverse the calculation: if the predicted response were measured, could it reveal the unknown parameter uniquely? A single pressure reading may have several explanations, including geometry error, property variation, transient motion or sensor bias. State which second observation would discriminate between them. Calculated values in this lesson are synthetic teaching examples, not plant measurements.

### Research and design interpretation

**Common failure mode:** Assuming quadratic loss scaling remains exact in laminar or mixed regimes.

Analyze why this fails: it may discard an important gradient, confuse a local speed with a cross-sectional mean, mix absolute and gauge pressures, ignore a storage term, use a coefficient outside its regime, or assume an ideal device has no losses. A small algebra error and an invalid physical approximation are different problems. In the first case, recompute carefully; in the second, select a more appropriate model or require additional experimental evidence. Examine the units first, then sign conventions, then limiting behavior, then parameter sensitivity, and finally comparison with observations. Reporting an apparent match at one operating point is not validation.

**Applied setting:** Return to the laboratory or field investigation described in the introduction to this unit, and apply this lesson’s relationship to one measurable component of that setting.

For **networks and system curves**, decide which geometric dimensions, flow variables and fluid properties matter most. Specify one primary measurement and one independent check, identify a plausible uncertainty source, and explain how a second operating point would help expose an inaccurate assumption. If the instrument samples only one location while the equation needs an integral or an average, explain the required sampling method. In a safety-relevant application, consult the applicable standards and use competent technical review. The simple classroom result must never be treated as a certified equipment rating or field guarantee.

### Three guided exercises

1. **Quantitative adaptation:** Recalculate the worked example after changing one stated driving parameter by 20%, provided the same physical regime remains plausible. Show intermediate SI units. Explain whether a proportional shortcut is justified or whether the complete relation must be re-evaluated.
2. **Model critique:** A colleague claims: “Assuming quadratic loss scaling remains exact in laminar or mixed regimes.” Locate the incorrect assumption or definition, describe the likely direction of error if it is predictable, and propose a minimal correction with an observable input.
3. **Experimental design:** How can two pressure taps help identify which branch carries excess resistance? Specify a plot with physically meaningful axes and units, two controlled operating conditions, an independent measurement, and a falsification criterion. State how you would detect instrument offset, drift or non-repeatability.

**Answer guidance.** Full credit requires mathematical consistency, stated scope, a plausible second measurement and a justified discussion of error. A numerical answer without an identified physical boundary cannot establish the correctness of a fluid-mechanics model. Connect this skill to **Minor losses and fittings** and then to **the next unit’s subject**. Keep a short data ledger containing symbol, source, unit, uncertainty and whether the value was measured, assumed or computed.


---

