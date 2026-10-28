# Unit 7: Planar Rigid-Body Dynamics and Work-Energy

# Unit 7 · Lesson 1 — Angular position, speed, and acceleration

**Unit objective:** Model rotating and translating rigid bodies with angular kinematics, moments, and kinetic energy.

## Why this concept matters

For rotation about a fixed axis, angular speed ω=dθ/dt and angular acceleration α=dω/dt. Tangential speed at radius r is v=rω, tangential acceleration is rα, and normal acceleration is rω². Angular variables must be in radians for these formulas. A point near the axis has lower tangential speed than a point on the rim at the same ω, but both share angular speed in an ideal rigid body.

We will use a deliberately simplified model first, then ask which real phenomena were discarded to obtain the simple equation. The difference between a teaching example and a credible design decision is largely in how those omissions are measured, documented, and tested.

Specify the axis about which rotational inertia and moment are taken. Angular displacement and angular velocity are expressed in radians and radians per second. For rolling and planar motion, combine translation of the mass center with rotation about that center.

## Deriving an appropriate model

Begin with a physically labeled drawing of **mixer shaft**. Choose the boundary of the body or subassembly to be analyzed. Identify external actions, directions, distances, and material or contact hypotheses. Record data in a compact SI table before evaluating the mathematical relationship. If a force or moment depends on geometry, add the reference point and angle definition to the same drawing. This first modeling step should be intelligible without any calculation.

Next write the governing relation **`ω=120(2π/60), v=rω`**. State why it is applicable to the chosen idealization. Ask which quantities are known, which are unknown, and which additional balance or compatibility equations would be required if a quantity were changed. Algebra is the final step in a reasoning process, not the beginning. In particular, a mathematical solution may be internally consistent even though a physical connection has been modeled incorrectly.

Two wheels of equal mass can have different rotational inertia because the location of that mass matters. Compare an angular quantity and its linear counterpart at the relevant radius rather than at an arbitrary point.

## Worked engineering illustration

**Context:** Mixer shaft.

**Known information and task:** ω=120 rpm on a radius r=0.15 m.

**Equation:** `ω=120(2π/60), v=rω`.

**Reference outcome:** **12.57 rad/s; 1.885 m/s**.

To reproduce the worked result, substitute the given numerical data with their units, evaluate the operations in a documented order, and round only the reported result. Label any signed component with its defined positive direction. Where the case is qualitative, present a symbolic balance and explain which remaining data determine its numerical value. A quick independent estimate should establish the expected order of magnitude before you trust the calculator. Do not confuse a condition derived for a particular ideal configuration with a general law that applies at every operating point.

**Engineering interpretation:** Guarding distances often depend on outer-rim tangential speed. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Using revolutions per minute as if they were radians per second.

Before using a fixed-axis scalar equation, confirm that the axis and inertia really are fixed. Torque multiplied by angular speed gives power in watts, while torque integrated through angular displacement gives work in joules. A rigid disk has mass moment I=mr²/2, while an ideal thin ring of the same mass and radius has I=mr².

Complete two checks before closing your notebook. First, verify the physical dimensions of each side of the main equation. Second, reverse or perturb an input that has a clear geometric interpretation, then predict the effect on the output without touching a calculator. If the prediction and numerical evaluation disagree, investigate the axis definition, units, or selected formula. For a contact-bound problem, also verify that the computed state is compatible with the direction in which the contact can act.

## Guided questions with answer criteria

**Q1 · Representation.** For mixer shaft, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `ω=120(2π/60), v=rω`.

**Q2 · Computation and trend.** Reproduce the calculation **ω=120 rpm on a radius r=0.15 m**, comparing with **12.57 rad/s; 1.885 m/s**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `ω=120(2π/60), v=rω` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for mixer shaft but appears to be using revolutions per minute as if they were radians per second. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.

## Transfer investigation

A technician asks whether the result **12.57 rad/s; 1.885 m/s** is enough to choose a replacement component. Write a short evaluation addressing (1) what has actually been computed, (2) which relevant loading states are absent, and (3) what evidence would establish a defensible rating. Relate each answer to the modeled device: mixer shaft. Explain why an exact numerical prediction of an ideal model may still be a poor predictor of an unmeasured real machine. Your recommendation must distinguish mathematics, assumptions, experimental measurements, and external engineering approval.



---

# Unit 7 · Lesson 2 — Rotational equation of motion

**Unit objective:** Model rotating and translating rigid bodies with angular kinematics, moments, and kinetic energy.

## Why this concept matters

For a rigid body rotating about a fixed principal axis with constant mass moment of inertia, ΣM=Iα. The mass moment I is measured in kg·m² and depends on mass distribution relative to the axis. Bearing reactions may be needed in addition to torque balance. A torque can cause angular acceleration; it does not inherently determine the operating speed without initial conditions and time. Resistance torque should appear with appropriate sign and may depend on speed.

Sign conventions are part of the model, not cosmetic decorations. A negative result is meaningful only after the assumed positive direction has been defined. It may indicate a real reversal, an unexpected contact state, or a modeling error; the diagram and independent checks decide which explanation fits.

Specify the axis about which rotational inertia and moment are taken. Angular displacement and angular velocity are expressed in radians and radians per second. For rolling and planar motion, combine translation of the mass center with rotation about that center.

## Deriving an appropriate model

Two wheels of equal mass can have different rotational inertia because the location of that mass matters. Compare an angular quantity and its linear counterpart at the relevant radius rather than at an arbitrary point.

## Worked engineering illustration

**Context:** Solid flywheel.

**Known information and task:** Mass 10 kg, radius 0.25 m, applied net torque 5 N·m.

**Equation:** `I=0.5 mr²; α=M/I`.

**Reference outcome:** **I=0.3125 kg·m²; α=16 rad/s²**.

**Engineering interpretation:** Start-up control must address both torque capacity and transient speed rise. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Confusing area second moment I with mass moment of inertia.

Before using a fixed-axis scalar equation, confirm that the axis and inertia really are fixed. Torque multiplied by angular speed gives power in watts, while torque integrated through angular displacement gives work in joules. A rigid disk has mass moment I=mr²/2, while an ideal thin ring of the same mass and radius has I=mr².

## Guided questions with answer criteria

**Q1 · Representation.** For solid flywheel, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `I=0.5 mr²; α=M/I`.

**Q2 · Computation and trend.** Reproduce the calculation **mass 10 kg, radius 0.25 m, applied net torque 5 n·m**, comparing with **I=0.3125 kg·m²; α=16 rad/s²**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `I=0.5 mr²; α=M/I` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for solid flywheel but appears to be confusing area second moment i with mass moment of inertia. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 7 · Lesson 3 — General planar motion and kinetic energy

**Unit objective:** Model rotating and translating rigid bodies with angular kinematics, moments, and kinetic energy.

## Why this concept matters

A planar rigid body may translate and rotate simultaneously. For mass center G, kinetic energy is T=0.5 m v_G²+0.5 I_G ω². This separation is valid for planar motion of a rigid body and often simplifies mechanisms. A selected contact point that is instantaneously stationary can help with velocity analysis, but care is needed when using it for acceleration or dynamics. Always state the rotational axis used for inertia.

A mechanical principle can be learned from more than one representation: a labeled drawing, a scalar equation, a vector equation, an experimental trend, and a limiting case. Translating between these forms is a valuable skill because real engineering work rarely arrives as a perfectly prepared algebra exercise.

Specify the axis about which rotational inertia and moment are taken. Angular displacement and angular velocity are expressed in radians and radians per second. For rolling and planar motion, combine translation of the mass center with rotation about that center.

## Deriving an appropriate model

Two wheels of equal mass can have different rotational inertia because the location of that mass matters. Compare an angular quantity and its linear counterpart at the relevant radius rather than at an arbitrary point.

## Worked engineering illustration

**Context:** Rolling cylinder.

**Known information and task:** Mass 4 kg, radius 0.2 m, mass center speed 2 m/s.

**Equation:** `I_G=0.5mr²; ω=v/r`.

**Reference outcome:** **T=12 J**.

**Engineering interpretation:** Flywheel and wheel energy storage is sensitive to how mass is distributed. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Neglecting rotational kinetic energy because the mass center translates.

Before using a fixed-axis scalar equation, confirm that the axis and inertia really are fixed. Torque multiplied by angular speed gives power in watts, while torque integrated through angular displacement gives work in joules. A rigid disk has mass moment I=mr²/2, while an ideal thin ring of the same mass and radius has I=mr².

## Guided questions with answer criteria

**Q1 · Representation.** For rolling cylinder, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `I_G=0.5mr²; ω=v/r`.

**Q2 · Computation and trend.** Reproduce the calculation **mass 4 kg, radius 0.2 m, mass center speed 2 m/s**, comparing with **T=12 J**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `I_G=0.5mr²; ω=v/r` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for rolling cylinder but appears to be neglecting rotational kinetic energy because the mass center translates. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 7 · Lesson 4 — Rolling without slipping

**Unit objective:** Model rotating and translating rigid bodies with angular kinematics, moments, and kinetic energy.

## Why this concept matters

Pure rolling on a stationary surface imposes v_G=rω instantaneously for a circular wheel. The contact point has zero instantaneous ground-frame velocity, yet may have nonzero acceleration. Rolling resistance and deformation can still dissipate energy without gross slip. When a torque drives a wheel, static friction at the contact can transmit force subject to traction limits. Choose a sign convention that makes translation and rotation equations compatible.

The central difficulty here is not remembering a formula but deciding whether the physical interaction has been represented faithfully. A successful calculation is one whose geometry, units, and chosen body can be explained to a colleague before the numerical result is shown. That discipline becomes more important as an assembly contains more components.

Specify the axis about which rotational inertia and moment are taken. Angular displacement and angular velocity are expressed in radians and radians per second. For rolling and planar motion, combine translation of the mass center with rotation about that center.

## Deriving an appropriate model

Two wheels of equal mass can have different rotational inertia because the location of that mass matters. Compare an angular quantity and its linear counterpart at the relevant radius rather than at an arbitrary point.

## Worked engineering illustration

**Context:** Solid cylinder rolling at 3 m/s.

**Known information and task:** Radius 0.3 m, no slip.

**Equation:** `ω=v/r`.

**Reference outcome:** **10 rad/s**.

**Engineering interpretation:** Wheel torque must be evaluated alongside traction and surface conditions. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Assuming a point with zero instantaneous velocity also has zero acceleration.

Before using a fixed-axis scalar equation, confirm that the axis and inertia really are fixed. Torque multiplied by angular speed gives power in watts, while torque integrated through angular displacement gives work in joules. A rigid disk has mass moment I=mr²/2, while an ideal thin ring of the same mass and radius has I=mr².

## Guided questions with answer criteria

**Q1 · Representation.** For solid cylinder rolling at 3 m/s, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `ω=v/r`.

**Q2 · Computation and trend.** Reproduce the calculation **radius 0.3 m, no slip**, comparing with **10 rad/s**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `ω=v/r` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for solid cylinder rolling at 3 m/s but appears to be assuming a point with zero instantaneous velocity also has zero acceleration. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 7 · Lesson 5 — Angular impulse and momentum

**Unit objective:** Model rotating and translating rigid bodies with angular kinematics, moments, and kinetic energy.

## Why this concept matters

For a fixed-axis rigid body, angular momentum H=Iω and angular impulse changes it: ∫M dt=ΔH. In systems with changing geometry or moving axes, use the more general vector formulation rather than a fixed scalar shortcut. An impulse may alter rotational speed very quickly; this is relevant in clutch engagement or sudden braking. If external angular impulse about a point is negligible, total system angular momentum about that point may be conserved.

Engineers often approach this subject in two directions: from a physical drawing to an equation, and from a computed answer back to a plausible physical action. Both directions matter. An unexplained number can be correct by coincidence, whereas a reproducible model can be corrected when assumptions change.

Specify the axis about which rotational inertia and moment are taken. Angular displacement and angular velocity are expressed in radians and radians per second. For rolling and planar motion, combine translation of the mass center with rotation about that center.

## Deriving an appropriate model

Two wheels of equal mass can have different rotational inertia because the location of that mass matters. Compare an angular quantity and its linear counterpart at the relevant radius rather than at an arbitrary point.

## Worked engineering illustration

**Context:** Motor shaft brake.

**Known information and task:** I=0.8 kg·m²; speed decreases from 20 rad/s to 5 rad/s.

**Equation:** `ΔH=I(ω2−ω1)`.

**Reference outcome:** **-12 N·m·s**.

**Engineering interpretation:** Brake sizing needs torque-time and thermal checks, not impulse alone. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Assuming angular momentum is conserved even with large external braking torque.

Before using a fixed-axis scalar equation, confirm that the axis and inertia really are fixed. Torque multiplied by angular speed gives power in watts, while torque integrated through angular displacement gives work in joules. A rigid disk has mass moment I=mr²/2, while an ideal thin ring of the same mass and radius has I=mr².

## Guided questions with answer criteria

**Q1 · Representation.** For motor shaft brake, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `ΔH=I(ω2−ω1)`.

**Q2 · Computation and trend.** Reproduce the calculation **i=0.8 kg·m²; speed decreases from 20 rad/s to 5 rad/s**, comparing with **-12 N·m·s**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `ΔH=I(ω2−ω1)` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for motor shaft brake but appears to be assuming angular momentum is conserved even with large external braking torque. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

