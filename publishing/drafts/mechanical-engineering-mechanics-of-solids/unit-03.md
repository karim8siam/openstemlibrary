# Unit 3: Shafts, Shear and Torsion

# Unit 3, Lesson 1 — Shear stress in solid circular shafts

**Learning target.** Connect transmitted torque to shear stress, angle of twist and load transfer through sections and connections. Explain the terms of `tau_max=16T/(πd³)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

For a linearly elastic circular shaft under uniform torsion, tau(r)=Tr/J and reaches its maximum at the surface. For a solid round, J=πd⁴/32 so tau_max=16T/(πd³). This theory assumes Saint-Venant torsion, a sufficient length away from discontinuities and no significant restrained warping. A keyway can dominate actual local stress.

The essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.

**Context:** A solid round shaft of diameter 30 mm carries torque 400 N m. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `tau_max=16T/(πd³)`.

Stiffness and nominal stress often scale differently with diameter: torsional stiffness varies as d to the fourth power while peak solid-shaft torsional stress varies inversely as d cubed. A transition or keyway destroys the smooth uniform geometry. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **shear stress in solid circular shafts**.

If the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.

## Worked example and interpretation

**Situation:** A solid round shaft of diameter 30 mm carries torque 400 N m.

**Equation:** `tau_max=16T/(πd³)`.

**Reference answer:** **75.45 MPa**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** A motor shaft must transmit peak transient torque, not only nominal steady torque. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using area I=πd⁴/64 instead of polar J=πd⁴/32.

A negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For geometry at torque transfer interfaces, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **75.45 MPa**, including units.

*Answer guidance:* Use `tau_max=16T/(πd³)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using area i=πd⁴/64 instead of polar j=πd⁴/32.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Confirm whether a constant torque is present over the entire segment or changes at a pulley, gear, or motor connection. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 3, Lesson 2 — Angle of twist and torsional stiffness

**Learning target.** Connect transmitted torque to shear stress, angle of twist and load transfer through sections and connections. Explain the terms of `θ=32TL/(πGd⁴)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Uniform circular-shaft twist is θ=TL/(GJ), with θ in radians. A shaft with high nominal strength can still rotate too much for positioning accuracy. In a stepped shaft, integrate local torque divided by GJ along the shaft; a section may reverse torque or have a different stiffness. Angular alignment measurements can test the assumption of elastic behavior.

Use the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.

**Context:** A 25 mm solid shaft, L=1 m, G=80 GPa carries 100 N m. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `θ=32TL/(πGd⁴)`.

Stiffness and nominal stress often scale differently with diameter: torsional stiffness varies as d to the fourth power while peak solid-shaft torsional stress varies inversely as d cubed. A transition or keyway destroys the smooth uniform geometry. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **angle of twist and torsional stiffness**.

The model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.

## Worked example and interpretation

**Situation:** A 25 mm solid shaft, L=1 m, G=80 GPa carries 100 N m.

**Equation:** `θ=32TL/(πGd⁴)`.

**Reference answer:** **0.03259 rad ≈ 1.867°**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Long drive shafts require angular deflection limits separate from stress limits. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Reporting a radian output as degrees without conversion.

Linear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For geometry at torque transfer interfaces, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.03259 rad ≈ 1.867°**, including units.

*Answer guidance:* Use `θ=32TL/(πGd⁴)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *reporting a radian output as degrees without conversion.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Confirm whether a constant torque is present over the entire segment or changes at a pulley, gear, or motor connection. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 3, Lesson 3 — Hollow shafts and weight efficiency

**Learning target.** Connect transmitted torque to shear stress, angle of twist and load transfer through sections and connections. Explain the terms of `tau_max=T(D/2)/[π(D⁴−d⁴)/32]`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Moving material away from the axis can raise torsional stiffness relative to mass, but a tube can face local instability or manufacturing limits. For a circular annulus J=π(D⁴−d⁴)/32 and tau_max=T(D/2)/J. The inner diameter must be smaller than the outer diameter and both must use the same length units. Compare designs at equal torque and material strength, not merely equal outer diameter.

An instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.

**Context:** A tube has outer D=40 mm, inner d=20 mm and torque 500 N m. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `tau_max=T(D/2)/[π(D⁴−d⁴)/32]`.

Stiffness and nominal stress often scale differently with diameter: torsional stiffness varies as d to the fourth power while peak solid-shaft torsional stress varies inversely as d cubed. A transition or keyway destroys the smooth uniform geometry. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **hollow shafts and weight efficiency**.

An independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.

## Worked example and interpretation

**Situation:** A tube has outer D=40 mm, inner d=20 mm and torque 500 N m.

**Equation:** `tau_max=T(D/2)/[π(D⁴−d⁴)/32]`.

**Reference answer:** **42.44 MPa**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Transmission tubes balance stiffness, mass, fatigue and connection detailing. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Computing J with (D−d)⁴ instead of D⁴−d⁴.

Safety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For geometry at torque transfer interfaces, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **42.44 MPa**, including units.

*Answer guidance:* Use `tau_max=T(D/2)/[π(D⁴−d⁴)/32]` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *computing j with (d−d)⁴ instead of d⁴−d⁴.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Confirm whether a constant torque is present over the entire segment or changes at a pulley, gear, or motor connection. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 3, Lesson 4 — Transverse shear and load transfer

**Learning target.** Connect transmitted torque to shear stress, angle of twist and load transfer through sections and connections. Explain the terms of `tau_max=1.5V/(bh)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Shear stress in a beam cross-section is not generally uniform. In elementary prismatic beams, the distribution follows tau=VQ/(It), where Q is a first moment of an area subset and t the local section width. For a rectangular section, the maximum is 1.5 times the average V/A. Thin-walled joint design also uses shear flow q=VQ/I, expressed as force per unit length.

The word “strength” is not interchangeable with “stiffness.” Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.

**Context:** Rectangular beam section b=30 mm, h=60 mm under shear force V=9 kN. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `tau_max=1.5V/(bh)`.

Stiffness and nominal stress often scale differently with diameter: torsional stiffness varies as d to the fourth power while peak solid-shaft torsional stress varies inversely as d cubed. A transition or keyway destroys the smooth uniform geometry. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **transverse shear and load transfer**.

A true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.

## Worked example and interpretation

**Situation:** Rectangular beam section b=30 mm, h=60 mm under shear force V=9 kN.

**Equation:** `tau_max=1.5V/(bh)`.

**Reference answer:** **7.5 MPa**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Adhesive joints may be governed by interface shear flow rather than beam face bending stress. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Applying the rectangular 1.5 factor to an I-section web without derivation.

Failure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For geometry at torque transfer interfaces, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **7.5 MPa**, including units.

*Answer guidance:* Use `tau_max=1.5V/(bh)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *applying the rectangular 1.5 factor to an i-section web without derivation.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Confirm whether a constant torque is present over the entire segment or changes at a pulley, gear, or motor connection. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 3, Lesson 5 — Torque transfer through connections

**Learning target.** Connect transmitted torque to shear stress, angle of twist and load transfer through sections and connections. Explain the terms of `F=T/r`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

An ideal keyed connection transmits tangential force F=T/r at an effective radius. This relation gives a starting load but cannot predict actual contact distribution at key corners. Contact pressure, fretting, bending and dynamic reversals matter. For a chain of shaft segments in series, transmitted torque is established from equilibrium including any gears or external couples.

For a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.

**Context:** A coupling transmits 800 N m at effective radius 40 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `F=T/r`.

Stiffness and nominal stress often scale differently with diameter: torsional stiffness varies as d to the fourth power while peak solid-shaft torsional stress varies inversely as d cubed. A transition or keyway destroys the smooth uniform geometry. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **torque transfer through connections**.

Checking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.

## Worked example and interpretation

**Situation:** A coupling transmits 800 N m at effective radius 40 mm.

**Equation:** `F=T/r`.

**Reference answer:** **20 kN tangential force**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** A coupling must be checked for contact pressure and shock loading. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using diameter rather than radius in T=Fr.

Do not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For geometry at torque transfer interfaces, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **20 kN tangential force**, including units.

*Answer guidance:* Use `F=T/r` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using diameter rather than radius in t=fr.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Confirm whether a constant torque is present over the entire segment or changes at a pulley, gear, or motor connection. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

