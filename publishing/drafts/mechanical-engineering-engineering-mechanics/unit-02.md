# Unit 2: Equilibrium of Particles and Rigid Bodies

# Unit 2 · Lesson 1 — Free-body diagrams and idealization

**Unit objective:** Isolate bodies, model reactions, and solve force and moment balances within the limits of static equilibrium.

## Why this concept matters

A free-body diagram removes surrounding matter and replaces each physical interaction by an external force or couple. Include weight, applied actions, contact effects, and support reactions, but not internal forces unless a section cut is made. Use a point mass approximation only when the rotational effects of size are immaterial. Every symbol in the equilibrium equations must appear on the sketch. Poor diagram boundaries cannot be rescued with sophisticated algebra; omitted forces simply propagate as confident errors.

We will use a deliberately simplified model first, then ask which real phenomena were discarded to obtain the simple equation. The difference between a teaching example and a credible design decision is largely in how those omissions are measured, documented, and tested.

Distinguish the external interactions that hold the body still from the internal load transmitted through its joints. A support reaction is a consequence of geometry, contact and equilibrium rather than an arbitrary force guessed in advance. A negative result must be reconciled with the physical abilities of the support.

## Deriving an appropriate model

Begin with a physically labeled drawing of **a hanging inspection camera**. Choose the boundary of the body or subassembly to be analyzed. Identify external actions, directions, distances, and material or contact hypotheses. Record data in a compact SI table before evaluating the mathematical relationship. If a force or moment depends on geometry, add the reference point and angle definition to the same drawing. This first modeling step should be intelligible without any calculation.

Next write the governing relation **`ΣFy=T−mg=0`**. State why it is applicable to the chosen idealization. Ask which quantities are known, which are unknown, and which additional balance or compatibility equations would be required if a quantity were changed. Algebra is the final step in a reasoning process, not the beginning. In particular, a mathematical solution may be internally consistent even though a physical connection has been modeled incorrectly.

A pin, roller, or contact surface is a physical mechanism for transferring an action, not merely an algebraic unknown. Estimate reactions from the location of weight before using the exact equilibrium equations.

## Worked engineering illustration

**Context:** A hanging inspection camera.

**Known information and task:** Draw the camera isolated from the mounting cable.

**Equation:** `ΣFy=T−mg=0`.

**Reference outcome:** **T=mg for rest**.

To reproduce the worked result, substitute the given numerical data with their units, evaluate the operations in a documented order, and round only the reported result. Label any signed component with its defined positive direction. Where the case is qualitative, present a symbolic balance and explain which remaining data determine its numerical value. A quick independent estimate should establish the expected order of magnitude before you trust the calculator. Do not confuse a condition derived for a particular ideal configuration with a general law that applies at every operating point.

**Engineering interpretation:** The drawing must identify which object the equation describes. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Including a cable tension acting on both sides of an isolated camera.

Any computed tension-only cable in compression or compression-only contact in tension requires a revised support model. On a simply supported member, the sum of upward reactions must equal downward loading. Taking moments about the left support and independently about the right support should produce consistent values. If a compression-only contact reaction is negative, the assumed support may have lifted off.

Complete two checks before closing your notebook. First, verify the physical dimensions of each side of the main equation. Second, reverse or perturb an input that has a clear geometric interpretation, then predict the effect on the output without touching a calculator. If the prediction and numerical evaluation disagree, investigate the axis definition, units, or selected formula. For a contact-bound problem, also verify that the computed state is compatible with the direction in which the contact can act.

## Guided questions with answer criteria

**Q1 · Representation.** For a hanging inspection camera, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `ΣFy=T−mg=0`.

**Q2 · Computation and trend.** Reproduce the calculation **draw the camera isolated from the mounting cable**, comparing with **T=mg for rest**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `ΣFy=T−mg=0` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for a hanging inspection camera but appears to be including a cable tension acting on both sides of an isolated camera. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.

## Transfer investigation

A technician asks whether the result **T=mg for rest** is enough to choose a replacement component. Write a short evaluation addressing (1) what has actually been computed, (2) which relevant loading states are absent, and (3) what evidence would establish a defensible rating. Relate each answer to the modeled device: a hanging inspection camera. Explain why an exact numerical prediction of an ideal model may still be a poor predictor of an unmeasured real machine. Your recommendation must distinguish mathematics, assumptions, experimental measurements, and external engineering approval.



---

# Unit 2 · Lesson 2 — Support constraints and reactions

**Unit objective:** Isolate bodies, model reactions, and solve force and moment balances within the limits of static equilibrium.

## Why this concept matters

An ideal roller supports one force normal to its guide. A smooth pin in the plane generally provides two reaction components but no direct moment. A fixed support can transmit two force components and a couple moment. Real bearings and bolted joints deviate from these idealizations under clearance and friction; a model should indicate when their complexity becomes important. Counting unknowns versus independent equilibrium equations flags underdeterminate or overconstrained systems without solving them.

Sign conventions are part of the model, not cosmetic decorations. A negative result is meaningful only after the assumed positive direction has been defined. It may indicate a real reversal, an unexpected contact state, or a modeling error; the diagram and independent checks decide which explanation fits.

Distinguish the external interactions that hold the body still from the internal load transmitted through its joints. A support reaction is a consequence of geometry, contact and equilibrium rather than an arbitrary force guessed in advance. A negative result must be reconciled with the physical abilities of the support.

## Deriving an appropriate model

A pin, roller, or contact surface is a physical mechanism for transferring an action, not merely an algebraic unknown. Estimate reactions from the location of weight before using the exact equilibrium equations.

## Worked engineering illustration

**Context:** Simply supported access platform.

**Known information and task:** One pin at A and a roller at B over 4 m support a centered 800 N load.

**Equation:** `R_A=R_B=800/2`.

**Reference outcome:** **400 N each**.

**Engineering interpretation:** Support idealization controls whether a statically determinate answer is available. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Assigning an unnecessary moment reaction to an ideal pin.

Any computed tension-only cable in compression or compression-only contact in tension requires a revised support model. On a simply supported member, the sum of upward reactions must equal downward loading. Taking moments about the left support and independently about the right support should produce consistent values. If a compression-only contact reaction is negative, the assumed support may have lifted off.

## Guided questions with answer criteria

**Q1 · Representation.** For simply supported access platform, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `R_A=R_B=800/2`.

**Q2 · Computation and trend.** Reproduce the calculation **one pin at a and a roller at b over 4 m support a centered 800 n load**, comparing with **400 N each**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `R_A=R_B=800/2` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for simply supported access platform but appears to be assigning an unnecessary moment reaction to an ideal pin. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 2 · Lesson 3 — Planar equilibrium and reaction solution

**Unit objective:** Isolate bodies, model reactions, and solve force and moment balances within the limits of static equilibrium.

## Why this concept matters

For a rigid body at rest in a plane, the algebraic sums of Fx, Fy, and moment about any chosen point vanish. Select the moment center so as many unknown reaction forces as possible have zero moment arms. After solving, return the reactions to the original force balance as a consistency check. Negative reaction components often mean the true force direction is opposite the assumed arrow; they do not automatically mean a calculation failure. A roller can detach if its computed compression force is negative, invalidating the contact assumption.

A mechanical principle can be learned from more than one representation: a labeled drawing, a scalar equation, a vector equation, an experimental trend, and a limiting case. Translating between these forms is a valuable skill because real engineering work rarely arrives as a perfectly prepared algebra exercise.

Distinguish the external interactions that hold the body still from the internal load transmitted through its joints. A support reaction is a consequence of geometry, contact and equilibrium rather than an arbitrary force guessed in advance. A negative result must be reconciled with the physical abilities of the support.

## Deriving an appropriate model

A pin, roller, or contact surface is a physical mechanism for transferring an action, not merely an algebraic unknown. Estimate reactions from the location of weight before using the exact equilibrium equations.

## Worked engineering illustration

**Context:** Offset load on support beam.

**Known information and task:** Beam span 5 m; 600 N downward at x=2 m.

**Equation:** `R_B=600(2)/5, R_A=600−R_B`.

**Reference outcome:** **R_A=360 N, R_B=240 N**.

**Engineering interpretation:** Lift-off and capacity limits must be evaluated separately after force balance. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Forgetting that a distributed weight also creates a moment.

Any computed tension-only cable in compression or compression-only contact in tension requires a revised support model. On a simply supported member, the sum of upward reactions must equal downward loading. Taking moments about the left support and independently about the right support should produce consistent values. If a compression-only contact reaction is negative, the assumed support may have lifted off.

## Guided questions with answer criteria

**Q1 · Representation.** For offset load on support beam, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `R_B=600(2)/5, R_A=600−R_B`.

**Q2 · Computation and trend.** Reproduce the calculation **beam span 5 m; 600 n downward at x=2 m**, comparing with **R_A=360 N, R_B=240 N**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `R_B=600(2)/5, R_A=600−R_B` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for offset load on support beam but appears to be forgetting that a distributed weight also creates a moment. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 2 · Lesson 4 — Multi-body equilibrium

**Unit objective:** Isolate bodies, model reactions, and solve force and moment balances within the limits of static equilibrium.

## Why this concept matters

Separating connected bodies reveals internal action-reaction pairs that cancel when the assembly is treated as one body. Solve the overall system first when possible, then isolate sub-bodies to recover pin forces. A force exerted by body A on B is opposite the force exerted by B on A; these are never two forces on the same free-body diagram. Intermediate joints often carry forces far larger than an external load because of small mechanical advantage.

The central difficulty here is not remembering a formula but deciding whether the physical interaction has been represented faithfully. A successful calculation is one whose geometry, units, and chosen body can be explained to a colleague before the numerical result is shown. That discipline becomes more important as an assembly contains more components.

Distinguish the external interactions that hold the body still from the internal load transmitted through its joints. A support reaction is a consequence of geometry, contact and equilibrium rather than an arbitrary force guessed in advance. A negative result must be reconciled with the physical abilities of the support.

## Deriving an appropriate model

A pin, roller, or contact surface is a physical mechanism for transferring an action, not merely an algebraic unknown. Estimate reactions from the location of weight before using the exact equilibrium equations.

## Worked engineering illustration

**Context:** Two linked arms carrying a load.

**Known information and task:** Two horizontal reactions at a joint from opposite members.

**Equation:** `F_AB=−F_BA`.

**Reference outcome:** **Equal magnitudes, opposite senses**.

**Engineering interpretation:** Joint load calculations often govern pin and bearing selection. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Counting action and reaction on the same isolated body.

Any computed tension-only cable in compression or compression-only contact in tension requires a revised support model. On a simply supported member, the sum of upward reactions must equal downward loading. Taking moments about the left support and independently about the right support should produce consistent values. If a compression-only contact reaction is negative, the assumed support may have lifted off.

## Guided questions with answer criteria

**Q1 · Representation.** For two linked arms carrying a load, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `F_AB=−F_BA`.

**Q2 · Computation and trend.** Reproduce the calculation **two horizontal reactions at a joint from opposite members**, comparing with **Equal magnitudes, opposite senses**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `F_AB=−F_BA` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for two linked arms carrying a load but appears to be counting action and reaction on the same isolated body. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 2 · Lesson 5 — Static equilibrium reliability

**Unit objective:** Isolate bodies, model reactions, and solve force and moment balances within the limits of static equilibrium.

## Why this concept matters

An equilibrium solution is conditional on geometry, support state, and linear rigid-body assumptions. Repeatedly measuring one support reaction can expose a missing load or a shifting center of gravity. Yet exact agreement with ΣF=0 and ΣM=0 does not establish that the body is stable, stiff enough, or below allowable stress. Compare results with rough symmetry arguments, dimensional consistency, and upper-bound estimates. Maintain a clear distinction between statics, strength, serviceability, and buckling.

Engineers often approach this subject in two directions: from a physical drawing to an equation, and from a computed answer back to a plausible physical action. Both directions matter. An unexplained number can be correct by coincidence, whereas a reproducible model can be corrected when assumptions change.

Distinguish the external interactions that hold the body still from the internal load transmitted through its joints. A support reaction is a consequence of geometry, contact and equilibrium rather than an arbitrary force guessed in advance. A negative result must be reconciled with the physical abilities of the support.

## Deriving an appropriate model

A pin, roller, or contact surface is a physical mechanism for transferring an action, not merely an algebraic unknown. Estimate reactions from the location of weight before using the exact equilibrium equations.

## Worked engineering illustration

**Context:** Supported maintenance rack.

**Known information and task:** 1000 N vertical load at 1 m of a 4 m span.

**Equation:** `R_B=1000×1/4`.

**Reference outcome:** **250 N at far support**.

**Engineering interpretation:** An independent overturning check is needed for freestanding machinery. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Assuming reactions alone certify that a rack will not buckle or tip.

Any computed tension-only cable in compression or compression-only contact in tension requires a revised support model. On a simply supported member, the sum of upward reactions must equal downward loading. Taking moments about the left support and independently about the right support should produce consistent values. If a compression-only contact reaction is negative, the assumed support may have lifted off.

## Guided questions with answer criteria

**Q1 · Representation.** For supported maintenance rack, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `R_B=1000×1/4`.

**Q2 · Computation and trend.** Reproduce the calculation **1000 n vertical load at 1 m of a 4 m span**, comparing with **250 N at far support**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `R_B=1000×1/4` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for supported maintenance rack but appears to be assuming reactions alone certify that a rack will not buckle or tip. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

