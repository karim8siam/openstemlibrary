# Unit 7: Stability, Fatigue and Fracture

# Unit 7, Lesson 1 — Euler column buckling

**Learning target.** Separate loss of elastic stability from yielding and introduce mechanical damage under repeated and crack-like loading. Explain the terms of `Pcr=π²EI/L²`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

A sufficiently slender ideal elastic column can lose stability at Euler load Pcr=π²EI/(KL)². K is the effective-length factor determined by end rotation and translation restraints, not a material property. Yielding and imperfections become important outside the ideal slender elastic regime. An equilibrium-based critical load is not the same as a recommended safe working load.

The essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.

**Context:** Pinned-pinned steel column E=200 GPa, I=400 cm⁴, L=3 m. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `Pcr=π²EI/L²`.

An instantaneous elastic calculation says little about growth of a crack under repeated stress. Conversely, a measured fatigue limit cannot prevent buckling of a very slender compression member. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **euler column buckling**.

If the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.

## Worked example and interpretation

**Situation:** Pinned-pinned steel column E=200 GPa, I=400 cm⁴, L=3 m.

**Equation:** `Pcr=π²EI/L²`.

**Reference answer:** **877.3 kN**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Column selection requires geometric imperfection and code-based strength checks. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using an unrestrained length for a column with different end conditions without setting K.

A negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For failure mode and service history, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **877.3 kN**, including units.

*Answer guidance:* Use `Pcr=π²EI/L²` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using an unrestrained length for a column with different end conditions without setting k.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Classify expected response as strength, stability, fracture, environmental degradation or fatigue before selecting a criterion. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 7, Lesson 2 — Eccentric compression and combined bending

**Learning target.** Separate loss of elastic stability from yielding and introduce mechanical damage under repeated and crack-like loading. Explain the terms of `M=P e`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

A compressive force whose line of action misses a section centroid introduces bending moment M=Pe. For an elastic section, compressive axial stress and bending stress superimpose before stability effects. The sign at each fiber depends on moment orientation; opposite edges may face very different stresses. For slender members, second-order P–delta amplification may invalidate a first-order formula.

Use the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.

**Context:** Compression P=30 kN acts with eccentricity e=20 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `M=P e`.

An instantaneous elastic calculation says little about growth of a crack under repeated stress. Conversely, a measured fatigue limit cannot prevent buckling of a very slender compression member. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **eccentric compression and combined bending**.

The model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.

## Worked example and interpretation

**Situation:** Compression P=30 kN acts with eccentricity e=20 mm.

**Equation:** `M=P e`.

**Reference answer:** **0.6 kN m**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Alignment tolerances can influence peak stress in brackets and columns. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using only P/A when the load is eccentric.

Linear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For failure mode and service history, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.6 kN m**, including units.

*Answer guidance:* Use `M=P e` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using only p/a when the load is eccentric.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Classify expected response as strength, stability, fracture, environmental degradation or fatigue before selecting a criterion. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 7, Lesson 3 — Stress concentration and notch sensitivity

**Learning target.** Separate loss of elastic stability from yielding and introduce mechanical damage under repeated and crack-like loading. Explain the terms of `sigma_peak=Kt sigma_nom`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

A hole or fillet changes local elastic stress even when nominal section force is unchanged. The theoretical elastic stress concentration factor Kt relates peak elastic stress to a nominal reference; its definition depends on gross or net nominal stress convention. Fatigue effective concentration Kf may differ from Kt due to material notch sensitivity. Do not use a chart factor without checking its specified geometry.

An instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.

**Context:** A geometry has nominal tension 60 MPa and Kt=2.5. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `sigma_peak=Kt sigma_nom`.

An instantaneous elastic calculation says little about growth of a crack under repeated stress. Conversely, a measured fatigue limit cannot prevent buckling of a very slender compression member. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **stress concentration and notch sensitivity**.

An independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.

## Worked example and interpretation

**Situation:** A geometry has nominal tension 60 MPa and Kt=2.5.

**Equation:** `sigma_peak=Kt sigma_nom`.

**Reference answer:** **150 MPa elastic peak estimate**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Smooth transitions can lower local elastic stress gradients. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Multiplying fatigue stress by a theoretical Kt without checking the fatigue notch factor.

Safety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For failure mode and service history, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **150 MPa elastic peak estimate**, including units.

*Answer guidance:* Use `sigma_peak=Kt sigma_nom` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *multiplying fatigue stress by a theoretical kt without checking the fatigue notch factor.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Classify expected response as strength, stability, fracture, environmental degradation or fatigue before selecting a criterion. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 7, Lesson 4 — Fatigue under fluctuating stress

**Learning target.** Separate loss of elastic stability from yielding and introduce mechanical damage under repeated and crack-like loading. Explain the terms of `sigma_a=(100−20)/2; sigma_m=(100+20)/2`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Alternating stress amplitude sigma_a=(sigma_max−sigma_min)/2 and mean stress sigma_m=(sigma_max+sigma_min)/2 describe constant-amplitude uniaxial cycling. A linear Goodman screening relation can compare tensile mean stress with a specified endurance-like strength and ultimate tensile strength. It is not a universal life prediction, especially for nonferrous materials without a clear fatigue limit. Loading spectra and surface finish matter.

The word “strength” is not interchangeable with “stiffness.” Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.

**Context:** A cycle ranges from 20 to 100 MPa in uniaxial tension. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `sigma_a=(100−20)/2; sigma_m=(100+20)/2`.

An instantaneous elastic calculation says little about growth of a crack under repeated stress. Conversely, a measured fatigue limit cannot prevent buckling of a very slender compression member. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **fatigue under fluctuating stress**.

A true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.

## Worked example and interpretation

**Situation:** A cycle ranges from 20 to 100 MPa in uniaxial tension.

**Equation:** `sigma_a=(100−20)/2; sigma_m=(100+20)/2`.

**Reference answer:** **40 MPa amplitude and 60 MPa mean**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Motor shafts and fasteners can fail from repeated load variations. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using maximum stress as fatigue amplitude.

Failure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For failure mode and service history, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **40 MPa amplitude and 60 MPa mean**, including units.

*Answer guidance:* Use `sigma_a=(100−20)/2; sigma_m=(100+20)/2` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using maximum stress as fatigue amplitude.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Classify expected response as strength, stability, fracture, environmental degradation or fatigue before selecting a criterion. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 7, Lesson 5 — Crack driving force and toughness

**Learning target.** Separate loss of elastic stability from yielding and introduce mechanical damage under repeated and crack-like loading. Explain the terms of `K_I=Y sigma sqrt(πa)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

For a cracked component in a suitable linear elastic mode I regime, KI=Y sigma sqrt(πa). Y describes geometry and crack configuration; a is a defined crack size in metres. Comparing KI to toughness KIc is meaningful only when the material state, thickness, environment and fracture regime are appropriate. Crack growth under cyclic loading requires additional data beyond this instantaneous intensity.

For a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.

**Context:** For a simplified crack Y=1, sigma=100 MPa, a=1 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `K_I=Y sigma sqrt(πa)`.

An instantaneous elastic calculation says little about growth of a crack under repeated stress. Conversely, a measured fatigue limit cannot prevent buckling of a very slender compression member. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **crack driving force and toughness**.

Checking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.

## Worked example and interpretation

**Situation:** For a simplified crack Y=1, sigma=100 MPa, a=1 mm.

**Equation:** `K_I=Y sigma sqrt(πa)`.

**Reference answer:** **5.605 MPa sqrt(m)**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Inspection intervals require crack growth and detection-limit evidence. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using millimetres directly inside sqrt(πa) when toughness uses sqrt(m).

Do not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For failure mode and service history, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **5.605 MPa sqrt(m)**, including units.

*Answer guidance:* Use `K_I=Y sigma sqrt(πa)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using millimetres directly inside sqrt(πa) when toughness uses sqrt(m).* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Classify expected response as strength, stability, fracture, environmental degradation or fatigue before selecting a criterion. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

