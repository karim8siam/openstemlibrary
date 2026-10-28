# Unit 5: Friction, Contact, and Wedges

# Unit 5 · Lesson 1 — Coulomb friction and contact normal

**Unit objective:** Understand the onset of sliding, dissipation, and assumptions of dry and rolling contact.

## Why this concept matters

For many dry macroscopic contacts, static friction adjusts to maintain no sliding up to |F_s|≤μ_s N; kinetic friction magnitude is often approximated as μ_k N during sliding. Static friction is not always μ_s N. The coefficient is empirical and can depend on surface condition, speed, temperature, and contamination. A contact normal acts perpendicular to a local surface, while friction opposes relative or impending tangential motion.

We will use a deliberately simplified model first, then ask which real phenomena were discarded to obtain the simple equation. The difference between a teaching example and a credible design decision is largely in how those omissions are measured, documented, and tested.

State the relative motion that friction resists. Static friction is an inequality and only reaches its limiting magnitude at imminent sliding. A measured coefficient belongs to specific material and environment conditions, so it should not be treated as a universal constant.

## Deriving an appropriate model

Begin with a physically labeled drawing of **crate pushed across a level floor**. Choose the boundary of the body or subassembly to be analyzed. Identify external actions, directions, distances, and material or contact hypotheses. Record data in a compact SI table before evaluating the mathematical relationship. If a force or moment depends on geometry, add the reference point and angle definition to the same drawing. This first modeling step should be intelligible without any calculation.

Next write the governing relation **`F_s,max=μ_s mg`**. State why it is applicable to the chosen idealization. Ask which quantities are known, which are unknown, and which additional balance or compatibility equations would be required if a quantity were changed. Algebra is the final step in a reasoning process, not the beginning. In particular, a mathematical solution may be internally consistent even though a physical connection has been modeled incorrectly.

A surface can remain motionless while static friction varies continuously from zero up to its allowable limit. Test whether the chosen direction of impending slip is internally consistent with the other force arrows.

## Worked engineering illustration

**Context:** Crate pushed across a level floor.

**Known information and task:** m=30 kg, μ_s=0.4, g=9.81 m/s².

**Equation:** `F_s,max=μ_s mg`.

**Reference outcome:** **117.72 N**.

To reproduce the worked result, substitute the given numerical data with their units, evaluate the operations in a documented order, and round only the reported result. Label any signed component with its defined positive direction. Where the case is qualitative, present a symbolic balance and explain which remaining data determine its numerical value. A quick independent estimate should establish the expected order of magnitude before you trust the calculator. Do not confuse a condition derived for a particular ideal configuration with a general law that applies at every operating point.

**Engineering interpretation:** A movement threshold can change dramatically with oil or surface wear. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Assigning maximum static friction before checking whether it is required.

Do not apply a single friction coefficient beyond conditions for which it was measured. For a stationary contact, solve the tangential force required first, then test whether its absolute value is below the static-friction limit. For a capstan model, the wrap angle must be in radians, and the predicted ratio is a limiting idealization rather than a universal measured value.

Complete two checks before closing your notebook. First, verify the physical dimensions of each side of the main equation. Second, reverse or perturb an input that has a clear geometric interpretation, then predict the effect on the output without touching a calculator. If the prediction and numerical evaluation disagree, investigate the axis definition, units, or selected formula. For a contact-bound problem, also verify that the computed state is compatible with the direction in which the contact can act.

## Guided questions with answer criteria

**Q1 · Representation.** For crate pushed across a level floor, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `F_s,max=μ_s mg`.

**Q2 · Computation and trend.** Reproduce the calculation **m=30 kg, μ_s=0.4, g=9.81 m/s²**, comparing with **117.72 N**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `F_s,max=μ_s mg` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for crate pushed across a level floor but appears to be assigning maximum static friction before checking whether it is required. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.

## Transfer investigation

A technician asks whether the result **117.72 N** is enough to choose a replacement component. Write a short evaluation addressing (1) what has actually been computed, (2) which relevant loading states are absent, and (3) what evidence would establish a defensible rating. Relate each answer to the modeled device: crate pushed across a level floor. Explain why an exact numerical prediction of an ideal model may still be a poor predictor of an unmeasured real machine. Your recommendation must distinguish mathematics, assumptions, experimental measurements, and external engineering approval.



---

# Unit 5 · Lesson 2 — Impending slip on inclines

**Unit objective:** Understand the onset of sliding, dissipation, and assumptions of dry and rolling contact.

## Why this concept matters

On an incline with angle alpha, the tangential gravity component is mg sin(alpha) and normal reaction for a simple unconstrained block is mg cos(alpha). The impending downhill-slip condition mg sin(alpha)=μ_s mg cos(alpha), so tan(alpha)=μ_s. A separate applied force changes both tangential and sometimes normal balance depending on its direction. Always draw friction to oppose the relative motion being tested.

Sign conventions are part of the model, not cosmetic decorations. A negative result is meaningful only after the assumed positive direction has been defined. It may indicate a real reversal, an unexpected contact state, or a modeling error; the diagram and independent checks decide which explanation fits.

State the relative motion that friction resists. Static friction is an inequality and only reaches its limiting magnitude at imminent sliding. A measured coefficient belongs to specific material and environment conditions, so it should not be treated as a universal constant.

## Deriving an appropriate model

A surface can remain motionless while static friction varies continuously from zero up to its allowable limit. Test whether the chosen direction of impending slip is internally consistent with the other force arrows.

## Worked engineering illustration

**Context:** Loaded supply tray.

**Known information and task:** Incline 20°, coefficient static friction 0.35.

**Equation:** `tan20°≈0.364>0.35`.

**Reference outcome:** **Unassisted tray begins to slip**.

**Engineering interpretation:** Shelf tilt controls should be assessed with uncertain coefficients, not just nominal values. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Using μN with the wrong contact normal when another angled force pushes on the body.

Do not apply a single friction coefficient beyond conditions for which it was measured. For a stationary contact, solve the tangential force required first, then test whether its absolute value is below the static-friction limit. For a capstan model, the wrap angle must be in radians, and the predicted ratio is a limiting idealization rather than a universal measured value.

## Guided questions with answer criteria

**Q1 · Representation.** For loaded supply tray, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `tan20°≈0.364>0.35`.

**Q2 · Computation and trend.** Reproduce the calculation **incline 20°, coefficient static friction 0.35**, comparing with **Unassisted tray begins to slip**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `tan20°≈0.364>0.35` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for loaded supply tray but appears to be using μn with the wrong contact normal when another angled force pushes on the body. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 5 · Lesson 3 — Wedges and mechanical amplification

**Unit objective:** Understand the onset of sliding, dissipation, and assumptions of dry and rolling contact.

## Why this concept matters

A wedge transforms a horizontal insertion motion into separation, usually amplifying normal force at the cost of travel distance. Ideal geometry produces a simple relationship between force and displacement; contact friction can dominate actual insertion and extraction forces. A full analysis requires separate free-body diagrams for wedge, load, and support, with consistent directions of normal and tangential actions. A wedge may self-lock under particular friction-angle conditions, but surface irregularities can break the ideal prediction.

A mechanical principle can be learned from more than one representation: a labeled drawing, a scalar equation, a vector equation, an experimental trend, and a limiting case. Translating between these forms is a valuable skill because real engineering work rarely arrives as a perfectly prepared algebra exercise.

State the relative motion that friction resists. Static friction is an inequality and only reaches its limiting magnitude at imminent sliding. A measured coefficient belongs to specific material and environment conditions, so it should not be treated as a universal constant.

## Deriving an appropriate model

A surface can remain motionless while static friction varies continuously from zero up to its allowable limit. Test whether the chosen direction of impending slip is internally consistent with the other force arrows.

## Worked engineering illustration

**Context:** Machine alignment wedge.

**Known information and task:** Ideal wedge with rise/run = 0.1 and horizontal input 200 N.

**Equation:** `F_lift≈F_input/0.1`.

**Reference outcome:** **2000 N idealized lift**.

**Engineering interpretation:** Installation instructions need both insertion-load and back-driving risk assessments. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Claiming ideal wedge amplification in a high-friction application.

Do not apply a single friction coefficient beyond conditions for which it was measured. For a stationary contact, solve the tangential force required first, then test whether its absolute value is below the static-friction limit. For a capstan model, the wrap angle must be in radians, and the predicted ratio is a limiting idealization rather than a universal measured value.

## Guided questions with answer criteria

**Q1 · Representation.** For machine alignment wedge, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `F_lift≈F_input/0.1`.

**Q2 · Computation and trend.** Reproduce the calculation **ideal wedge with rise/run = 0.1 and horizontal input 200 n**, comparing with **2000 N idealized lift**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `F_lift≈F_input/0.1` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for machine alignment wedge but appears to be claiming ideal wedge amplification in a high-friction application. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 5 · Lesson 4 — Belt friction and capstan effect

**Unit objective:** Understand the onset of sliding, dissipation, and assumptions of dry and rolling contact.

## Why this concept matters

A flexible belt contacting a cylindrical drum can sustain different tensions at its ends. Under limiting friction and a standard ideal capstan model, T_tight/T_slack=e^(μθ), where wrap angle θ is in radians. The exponential dependence means additional wrap angle can have a stronger effect than expected from a linear intuition. Elastic stretching, groove profiles, moisture, and changing coefficients can cause substantial deviations from the ideal formula.

The central difficulty here is not remembering a formula but deciding whether the physical interaction has been represented faithfully. A successful calculation is one whose geometry, units, and chosen body can be explained to a colleague before the numerical result is shown. That discipline becomes more important as an assembly contains more components.

State the relative motion that friction resists. Static friction is an inequality and only reaches its limiting magnitude at imminent sliding. A measured coefficient belongs to specific material and environment conditions, so it should not be treated as a universal constant.

## Deriving an appropriate model

A surface can remain motionless while static friction varies continuously from zero up to its allowable limit. Test whether the chosen direction of impending slip is internally consistent with the other force arrows.

## Worked engineering illustration

**Context:** Brake band around a drum.

**Known information and task:** μ=0.25; wrap angle π rad; slack tension 100 N.

**Equation:** `T_tight=100 exp(0.25π)`.

**Reference outcome:** **≈219.32 N**.

**Engineering interpretation:** Band brakes and rope-handling systems can become hazardous if friction changes. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Substituting degrees directly into the exponential formula.

Do not apply a single friction coefficient beyond conditions for which it was measured. For a stationary contact, solve the tangential force required first, then test whether its absolute value is below the static-friction limit. For a capstan model, the wrap angle must be in radians, and the predicted ratio is a limiting idealization rather than a universal measured value.

## Guided questions with answer criteria

**Q1 · Representation.** For brake band around a drum, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `T_tight=100 exp(0.25π)`.

**Q2 · Computation and trend.** Reproduce the calculation **μ=0.25; wrap angle π rad; slack tension 100 n**, comparing with **≈219.32 N**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `T_tight=100 exp(0.25π)` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for brake band around a drum but appears to be substituting degrees directly into the exponential formula. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 5 · Lesson 5 — Rolling resistance and friction limits

**Unit objective:** Understand the onset of sliding, dissipation, and assumptions of dry and rolling contact.

## Why this concept matters

Rolling resistance is often modeled using an equivalent resisting force or a resisting moment, but it is not the same physical process as kinetic sliding friction. Deformation hysteresis, tire pressure, roughness, and bearing drag can all contribute. Use a coefficient whose definition and units are specified; different textbooks adopt different rolling-resistance conventions. Stability and traction impose independent constraints on a vehicle, and a wheel may roll without slipping while experiencing static contact forces.

Engineers often approach this subject in two directions: from a physical drawing to an equation, and from a computed answer back to a plausible physical action. Both directions matter. An unexplained number can be correct by coincidence, whereas a reproducible model can be corrected when assumptions change.

State the relative motion that friction resists. Static friction is an inequality and only reaches its limiting magnitude at imminent sliding. A measured coefficient belongs to specific material and environment conditions, so it should not be treated as a universal constant.

## Deriving an appropriate model

A surface can remain motionless while static friction varies continuously from zero up to its allowable limit. Test whether the chosen direction of impending slip is internally consistent with the other force arrows.

## Worked engineering illustration

**Context:** Utility cart wheel.

**Known information and task:** Normal load 800 N and dimensionless rolling coefficient 0.015.

**Equation:** `F_rr≈C_rr N`.

**Reference outcome:** **12 N**.

**Engineering interpretation:** Energy and motor sizing require measured rolling losses for realistic conditions. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Applying sliding μ_k as if it were a rolling-resistance coefficient.

Do not apply a single friction coefficient beyond conditions for which it was measured. For a stationary contact, solve the tangential force required first, then test whether its absolute value is below the static-friction limit. For a capstan model, the wrap angle must be in radians, and the predicted ratio is a limiting idealization rather than a universal measured value.

## Guided questions with answer criteria

**Q1 · Representation.** For utility cart wheel, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `F_rr≈C_rr N`.

**Q2 · Computation and trend.** Reproduce the calculation **normal load 800 n and dimensionless rolling coefficient 0.015**, comparing with **12 N**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `F_rr≈C_rr N` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for utility cart wheel but appears to be applying sliding μ_k as if it were a rolling-resistance coefficient. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

