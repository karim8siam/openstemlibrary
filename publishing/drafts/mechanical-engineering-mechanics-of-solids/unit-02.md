# Unit 2: Axial Members and Compatibility

# Unit 2, Lesson 1 — Uniform axial bars

**Learning target.** Calculate elastic axial shortening or extension and resolve load redistribution caused by assembly constraints and temperature. Explain the terms of `δ=PL/(AE)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Axial elongation for a prismatic straight elastic member under uniform force follows δ=PL/(AE). The load P must be the internal axial force; externally applied loads can redistribute when other members participate. The formula assumes small strain and constant E and A throughout the segment. Use a consistent unit system or the dimensions will silently be wrong.

The essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.

**Context:** A steel bar of length 2 m, area 400 mm², E=200 GPa, carries 20 kN tension. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `δ=PL/(AE)`.

A correctly balanced set of axial forces can still violate the physical constraint that two fastened points move together. A rigid-plate assumption can be checked by measuring relative displacements. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **uniform axial bars**.

If the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.

## Worked example and interpretation

**Situation:** A steel bar of length 2 m, area 400 mm², E=200 GPa, carries 20 kN tension.

**Equation:** `δ=PL/(AE)`.

**Reference answer:** **0.5 mm extension**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Tie rods require both allowable tensile stress and alignment displacement checks. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using E=200 as though it were measured in pascals.

A negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For compatibility of connected parts, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.5 mm extension**, including units.

*Answer guidance:* Use `δ=PL/(AE)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using e=200 as though it were measured in pascals.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Confirm whether temperature, preload, and contact slip change the reference length before reusing the formula. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 2, Lesson 2 — Stepped members and internal force variation

**Learning target.** Calculate elastic axial shortening or extension and resolve load redistribution caused by assembly constraints and temperature. Explain the terms of `δ_total=δ1+δ2`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

For a succession of prismatic elements, sum each segment elongation δ_i=P_i L_i/(A_i E_i). It is unsafe to use one global P when forces enter at intermediate nodes. A cross-section cut finds the force in the segment and the equilibrium of its separated piece. If a bar has varying area, the corresponding limit is an axial integral.

Use the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.

**Context:** Two same-force segments extend 0.3 mm and 0.5 mm respectively. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `δ_total=δ1+δ2`.

A correctly balanced set of axial forces can still violate the physical constraint that two fastened points move together. A rigid-plate assumption can be checked by measuring relative displacements. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **stepped members and internal force variation**.

The model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.

## Worked example and interpretation

**Situation:** Two same-force segments extend 0.3 mm and 0.5 mm respectively.

**Equation:** `δ_total=δ1+δ2`.

**Reference answer:** **0.8 mm**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** A transition of cross-section often drives peak stress even when its length is short. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Averaging segment areas before calculating deformation in a variable-area bar.

Linear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For compatibility of connected parts, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.8 mm**, including units.

*Answer guidance:* Use `δ_total=δ1+δ2` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *averaging segment areas before calculating deformation in a variable-area bar.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Confirm whether temperature, preload, and contact slip change the reference length before reusing the formula. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 2, Lesson 3 — Restricted thermal expansion

**Learning target.** Calculate elastic axial shortening or extension and resolve load redistribution caused by assembly constraints and temperature. Explain the terms of `sigma=−E alpha ΔT`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

A free bar can expand by αLΔT without developing mechanical thermal stress. A fully restrained uniform linear elastic bar develops stress of magnitude Eα|ΔT|, with compression on heating. Compliance of supports or plastic flow reduces or redistributes the stress. Temperature gradients may bend or distort a member even if average temperature is known.

An instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.

**Context:** A fully fixed steel bar has E=200 GPa, alpha=12e-6/K and temperature rise 40 K. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `sigma=−E alpha ΔT`.

A correctly balanced set of axial forces can still violate the physical constraint that two fastened points move together. A rigid-plate assumption can be checked by measuring relative displacements. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **restricted thermal expansion**.

An independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.

## Worked example and interpretation

**Situation:** A fully fixed steel bar has E=200 GPa, alpha=12e-6/K and temperature rise 40 K.

**Equation:** `sigma=−E alpha ΔT`.

**Reference answer:** **−96 MPa compressive**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Thermal restraints in machine frames need a temperature-dependent stress evaluation. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Assigning thermal stress to an otherwise free, unconstrained bar.

Safety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For compatibility of connected parts, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **−96 MPa compressive**, including units.

*Answer guidance:* Use `sigma=−E alpha ΔT` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *assigning thermal stress to an otherwise free, unconstrained bar.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Confirm whether temperature, preload, and contact slip change the reference length before reusing the formula. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 2, Lesson 4 — Parallel rods and rigid plates

**Learning target.** Calculate elastic axial shortening or extension and resolve load redistribution caused by assembly constraints and temperature. Explain the terms of `P1=50×40/(40+60)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

When rigid end plates force connected rods to experience equal displacement, load shares in proportion to each rod axial stiffness EA/L under small linear response. Force balance alone does not fix the split. For dissimilar materials their thermal strains can also create self-equilibrated forces. Check both the force sum and identical end displacement as independent constraints.

The word “strength” is not interchangeable with “stiffness.” Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.

**Context:** Two rods have axial stiffness 40 and 60 kN/mm and share 50 kN. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `P1=50×40/(40+60)`.

A correctly balanced set of axial forces can still violate the physical constraint that two fastened points move together. A rigid-plate assumption can be checked by measuring relative displacements. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **parallel rods and rigid plates**.

A true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.

## Worked example and interpretation

**Situation:** Two rods have axial stiffness 40 and 60 kN/mm and share 50 kN.

**Equation:** `P1=50×40/(40+60)`.

**Reference answer:** **20 kN in the first rod**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Bolted parallel load paths can become uneven as connections settle. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Dividing the load equally without checking stiffness.

Failure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For compatibility of connected parts, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **20 kN in the first rod**, including units.

*Answer guidance:* Use `P1=50×40/(40+60)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *dividing the load equally without checking stiffness.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Confirm whether temperature, preload, and contact slip change the reference length before reusing the formula. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 2, Lesson 5 — Shear pins and joint bearing

**Learning target.** Calculate elastic axial shortening or extension and resolve load redistribution caused by assembly constraints and temperature. Explain the terms of `tau=F/(2πd²/4)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Connections can control strength while the attached bars remain elastic. Average shear in a pin is transmitted force divided by resisting shear area; a double-shear configuration has two effective planes if each plane is engaged as idealized. Bearing pressure on a plate involves projected pin diameter times plate thickness. Neither average stress resolves edge tear-out or bending in a long pin.

For a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.

**Context:** A 12 mm diameter pin carries 18 kN in ideal double shear. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `tau=F/(2πd²/4)`.

A correctly balanced set of axial forces can still violate the physical constraint that two fastened points move together. A rigid-plate assumption can be checked by measuring relative displacements. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **shear pins and joint bearing**.

Checking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.

## Worked example and interpretation

**Situation:** A 12 mm diameter pin carries 18 kN in ideal double shear.

**Equation:** `tau=F/(2πd²/4)`.

**Reference answer:** **79.58 MPa average shear**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** A pin selection also needs bearing, clearance, fatigue and edge-distance assessment. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using a single shear plane for an ideal double-shear clevis.

Do not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For compatibility of connected parts, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **79.58 MPa average shear**, including units.

*Answer guidance:* Use `tau=F/(2πd²/4)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using a single shear plane for an ideal double-shear clevis.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Confirm whether temperature, preload, and contact slip change the reference length before reusing the formula. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

