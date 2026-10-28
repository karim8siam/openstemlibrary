# Unit 5: Beam Deflection and Energy Methods

# Unit 5, Lesson 1 — Moment–curvature relation

**Learning target.** Predict elastic slopes, deflections and strain energy, including compatibility constraints and load displacement relationships. Explain the terms of `kappa=M/(EI)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Euler–Bernoulli beam theory assumes sections remain plane and normal to a deformed centerline, producing curvature κ=M/(EI) for small slopes. A curvature result cannot be integrated without boundary conditions. In thick short beams, transverse shear deformation can be non-negligible; a Timoshenko model may be better. Deflection and rotation sign conventions should be stated before integration.

The essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.

**Context:** Uniform E=200 GPa, I=500 cm⁴ and bending moment 2 kN m. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `kappa=M/(EI)`.

Changing boundary constraints can alter a deformation coefficient by a large factor even when E, I and loading remain unchanged. Superposition cannot be used indiscriminately with changing contacts or plastic hinges. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **moment–curvature relation**.

If the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.

## Worked example and interpretation

**Situation:** Uniform E=200 GPa, I=500 cm⁴ and bending moment 2 kN m.

**Equation:** `kappa=M/(EI)`.

**Reference answer:** **0.002 1/m**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Curvature is the local change in beam slope per length. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using I in cm⁴ as if it were m⁴.

A negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For boundary-condition dependency, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.002 1/m**, including units.

*Answer guidance:* Use `kappa=M/(EI)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using i in cm⁴ as if it were m⁴.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Write all deflection and slope boundary conditions beside the governing differential equation. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 5, Lesson 2 — Simply supported beam deflection

**Learning target.** Predict elastic slopes, deflections and strain energy, including compatibility constraints and load displacement relationships. Explain the terms of `delta=PL³/(48EI)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

For a simply supported prismatic beam with a midspan point load and constant EI, the central elastic deflection has magnitude PL³/(48EI). Its cubic span dependence is a major design sensitivity. Changing the support to a fixed end invalidates the coefficient 48 even if the load and section are unchanged. Account for self-weight separately when it is not negligible.

Use the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.

**Context:** P=8 kN at midspan, L=3 m, E=200 GPa, I=800 cm⁴. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `delta=PL³/(48EI)`.

Changing boundary constraints can alter a deformation coefficient by a large factor even when E, I and loading remain unchanged. Superposition cannot be used indiscriminately with changing contacts or plastic hinges. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **simply supported beam deflection**.

The model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.

## Worked example and interpretation

**Situation:** P=8 kN at midspan, L=3 m, E=200 GPa, I=800 cm⁴.

**Equation:** `delta=PL³/(48EI)`.

**Reference answer:** **2.8125 mm**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Long-span design may be governed by deflection before yielding. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Keeping the simply supported coefficient after changing the support type.

Linear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For boundary-condition dependency, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **2.8125 mm**, including units.

*Answer guidance:* Use `delta=PL³/(48EI)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *keeping the simply supported coefficient after changing the support type.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Write all deflection and slope boundary conditions beside the governing differential equation. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 5, Lesson 3 — Cantilever tip displacement

**Learning target.** Predict elastic slopes, deflections and strain energy, including compatibility constraints and load displacement relationships. Explain the terms of `delta_tip=PL³/(3EI)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

A cantilever with a free-end transverse point load deflects at its tip by PL³/(3EI) and rotates by PL²/(2EI) under linear small-deflection theory. The sign reflects load direction, and a rigid support is idealized. Compare deflection prediction to measured motion without including fixture settlement in the same number. For large rotations, geometric nonlinear analysis is required.

An instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.

**Context:** A cantilever has P=500 N, L=1 m, E=200 GPa, I=400 cm⁴. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `delta_tip=PL³/(3EI)`.

Changing boundary constraints can alter a deformation coefficient by a large factor even when E, I and loading remain unchanged. Superposition cannot be used indiscriminately with changing contacts or plastic hinges. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **cantilever tip displacement**.

An independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.

## Worked example and interpretation

**Situation:** A cantilever has P=500 N, L=1 m, E=200 GPa, I=400 cm⁴.

**Equation:** `delta_tip=PL³/(3EI)`.

**Reference answer:** **0.20833 mm**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** A flexible cantilever mechanism can meet strength limits but miss positional tolerances. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using simply supported beam formulas for a cantilever.

Safety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For boundary-condition dependency, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.20833 mm**, including units.

*Answer guidance:* Use `delta_tip=PL³/(3EI)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using simply supported beam formulas for a cantilever.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Write all deflection and slope boundary conditions beside the governing differential equation. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 5, Lesson 4 — Strain energy and Castigliano

**Learning target.** Predict elastic slopes, deflections and strain energy, including compatibility constraints and load displacement relationships. Explain the terms of `U=0.5Pdelta`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Elastic axial energy U=P²L/(2EA) follows from integrating P dδ in a linear system. Castigliano’s displacement theorem differentiates total elastic strain energy with respect to a corresponding force for a linear elastic structure, under its conditions of use. The method is particularly useful when several members deform together. A single term is insufficient if bending, shear or torsion also contributes significantly.

The word “strength” is not interchangeable with “stiffness.” Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.

**Context:** Bar with axial load 12 kN and extension 0.3 mm in a linear test. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `U=0.5Pdelta`.

Changing boundary constraints can alter a deformation coefficient by a large factor even when E, I and loading remain unchanged. Superposition cannot be used indiscriminately with changing contacts or plastic hinges. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **strain energy and castigliano**.

A true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.

## Worked example and interpretation

**Situation:** Bar with axial load 12 kN and extension 0.3 mm in a linear test.

**Equation:** `U=0.5Pdelta`.

**Reference answer:** **1.8 J**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Energy methods provide independent displacement checks and stiffness estimates. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Omitting the factor one-half for a load increased quasistatically from zero.

Failure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For boundary-condition dependency, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **1.8 J**, including units.

*Answer guidance:* Use `U=0.5Pdelta` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *omitting the factor one-half for a load increased quasistatically from zero.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Write all deflection and slope boundary conditions beside the governing differential equation. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 5, Lesson 5 — Redundant supports and superposition

**Learning target.** Predict elastic slopes, deflections and strain energy, including compatibility constraints and load displacement relationships. Explain the terms of `F=k delta`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

A statically indeterminate beam or bar requires compatibility as well as equilibrium. One approach removes a redundant restraint, computes displacements from separate loads, and selects the redundant so the required displacement is recovered. Linear superposition fails after yielding, contact change or nonlinear large motion. A zero displacement at a support is a boundary condition, not an arbitrary convenience.

For a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.

**Context:** A linear axial spring of stiffness 60 kN/mm is restrained to stretch 0.25 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `F=k delta`.

Changing boundary constraints can alter a deformation coefficient by a large factor even when E, I and loading remain unchanged. Superposition cannot be used indiscriminately with changing contacts or plastic hinges. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **redundant supports and superposition**.

Checking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.

## Worked example and interpretation

**Situation:** A linear axial spring of stiffness 60 kN/mm is restrained to stretch 0.25 mm.

**Equation:** `F=k delta`.

**Reference answer:** **15 kN**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Support settlement and fit-up can create forces without a new external payload. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Solving a redundant support by force balance alone.

Do not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For boundary-condition dependency, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **15 kN**, including units.

*Answer guidance:* Use `F=k delta` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *solving a redundant support by force balance alone.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Write all deflection and slope boundary conditions beside the governing differential equation. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

