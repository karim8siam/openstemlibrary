# Unit 4: Distributed Forces, Centroids, and Moments of Inertia

# Unit 4 · Lesson 1 — Centroids of composite areas

**Unit objective:** Locate resultants of extended loads and compute geometric properties needed for bending and stiffness.

## Why this concept matters

The centroid of a planar area is the area-weighted mean of its coordinates: x_bar=ΣAi xi/ΣAi. A hole is represented by negative area in a composite calculation. The centroid is a property of geometry; it coincides with center of mass only for suitable uniform-density distributions and constant thickness. Carefully decompose a complex cross-section into nonoverlapping primitives, then check whether the answer lies in a physically plausible position. Symmetry should be used before arithmetic.

We will use a deliberately simplified model first, then ask which real phenomena were discarded to obtain the simple equation. The difference between a teaching example and a credible design decision is largely in how those omissions are measured, documented, and tested.

Identify the reference axis and whether the calculated quantity is a mass property or an area property. A composite section must be decomposed into non-overlapping pieces. Area moments preserve the correct length power and should be checked by evaluating a symmetric limiting geometry.

## Deriving an appropriate model

Begin with a physically labeled drawing of **l-shaped plate from two rectangles**. Choose the boundary of the body or subassembly to be analyzed. Identify external actions, directions, distances, and material or contact hypotheses. Record data in a compact SI table before evaluating the mathematical relationship. If a force or moment depends on geometry, add the reference point and angle definition to the same drawing. This first modeling step should be intelligible without any calculation.

Next write the governing relation **`x_bar=(.06×.1+.04×.35)/.10`**. State why it is applicable to the chosen idealization. Ask which quantities are known, which are unknown, and which additional balance or compatibility equations would be required if a quantity were changed. Algebra is the final step in a reasoning process, not the beginning. In particular, a mathematical solution may be internally consistent even though a physical connection has been modeled incorrectly.

Moving material away from a bending axis can increase stiffness while leaving total cross-sectional area unchanged. Sketch the positive and negative pieces of a composite section before taking moments.

## Worked engineering illustration

**Context:** L-shaped plate from two rectangles.

**Known information and task:** Areas 0.06 m² at x=0.1 m and 0.04 m² at x=0.35 m.

**Equation:** `x_bar=(.06×.1+.04×.35)/.10`.

**Reference outcome:** **0.20 m**.

To reproduce the worked result, substitute the given numerical data with their units, evaluate the operations in a documented order, and round only the reported result. Label any signed component with its defined positive direction. Where the case is qualitative, present a symbolic balance and explain which remaining data determine its numerical value. A quick independent estimate should establish the expected order of magnitude before you trust the calculator. Do not confuse a condition derived for a particular ideal configuration with a general law that applies at every operating point.

**Engineering interpretation:** Cross-section centroid position determines the neutral axis in simple bending. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Double-counting the overlap between the component rectangles.

A credible numerical result includes its reference axis, geometric dimension, and SI unit power. An area centroid is expressed in metres, a second moment of area in m^4, and a mass moment of inertia in kg·m². These are not interchangeable. If a section's depth doubles at constant width, its centroidal rectangular Ix increases by a factor of eight.

Complete two checks before closing your notebook. First, verify the physical dimensions of each side of the main equation. Second, reverse or perturb an input that has a clear geometric interpretation, then predict the effect on the output without touching a calculator. If the prediction and numerical evaluation disagree, investigate the axis definition, units, or selected formula. For a contact-bound problem, also verify that the computed state is compatible with the direction in which the contact can act.

## Guided questions with answer criteria

**Q1 · Representation.** For l-shaped plate from two rectangles, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `x_bar=(.06×.1+.04×.35)/.10`.

**Q2 · Computation and trend.** Reproduce the calculation **areas 0.06 m² at x=0.1 m and 0.04 m² at x=0.35 m**, comparing with **0.20 m**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `x_bar=(.06×.1+.04×.35)/.10` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for l-shaped plate from two rectangles but appears to be double-counting the overlap between the component rectangles. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.

## Transfer investigation

A technician asks whether the result **0.20 m** is enough to choose a replacement component. Write a short evaluation addressing (1) what has actually been computed, (2) which relevant loading states are absent, and (3) what evidence would establish a defensible rating. Relate each answer to the modeled device: l-shaped plate from two rectangles. Explain why an exact numerical prediction of an ideal model may still be a poor predictor of an unmeasured real machine. Your recommendation must distinguish mathematics, assumptions, experimental measurements, and external engineering approval.



---

# Unit 4 · Lesson 2 — Center of gravity and variable density

**Unit objective:** Locate resultants of extended loads and compute geometric properties needed for bending and stiffness.

## Why this concept matters

Center of mass is a mass-weighted position, whereas center of gravity is determined by the distributed gravitational force; they agree in a nearly uniform gravitational field. Material inhomogeneity shifts the mass center even when external dimensions are symmetric. The equivalent weight force acts at the center of gravity for moment calculations. For a discrete assembly, x_G=Σmi xi/Σmi. A continuous model replaces sums with integrals over mass or volume.

Sign conventions are part of the model, not cosmetic decorations. A negative result is meaningful only after the assumed positive direction has been defined. It may indicate a real reversal, an unexpected contact state, or a modeling error; the diagram and independent checks decide which explanation fits.

Identify the reference axis and whether the calculated quantity is a mass property or an area property. A composite section must be decomposed into non-overlapping pieces. Area moments preserve the correct length power and should be checked by evaluating a symmetric limiting geometry.

## Deriving an appropriate model

Moving material away from a bending axis can increase stiffness while leaving total cross-sectional area unchanged. Sketch the positive and negative pieces of a composite section before taking moments.

## Worked engineering illustration

**Context:** Motor mounted on a lightweight trolley.

**Known information and task:** 20 kg at x=0.2 m plus 5 kg at x=0.8 m.

**Equation:** `x_G=(20×.2+5×.8)/25`.

**Reference outcome:** **0.32 m**.

**Engineering interpretation:** Trolley wheel reactions depend on mass placement, not merely outline shape. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Using shape centroid for an assembly of dissimilar materials.

A credible numerical result includes its reference axis, geometric dimension, and SI unit power. An area centroid is expressed in metres, a second moment of area in m^4, and a mass moment of inertia in kg·m². These are not interchangeable. If a section's depth doubles at constant width, its centroidal rectangular Ix increases by a factor of eight.

## Guided questions with answer criteria

**Q1 · Representation.** For motor mounted on a lightweight trolley, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `x_G=(20×.2+5×.8)/25`.

**Q2 · Computation and trend.** Reproduce the calculation **20 kg at x=0.2 m plus 5 kg at x=0.8 m**, comparing with **0.32 m**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `x_G=(20×.2+5×.8)/25` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for motor mounted on a lightweight trolley but appears to be using shape centroid for an assembly of dissimilar materials. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 4 · Lesson 3 — Second moments of area

**Unit objective:** Locate resultants of extended loads and compute geometric properties needed for bending and stiffness.

## Why this concept matters

The second moment of area Ix=∫y²dA describes distribution of area relative to an axis and appears in beam deflection and bending stress. It has units m^4, not kilograms times metres squared. For a rectangle of breadth b and height h about its centroidal horizontal axis, Ix=bh³/12. A small increase in section depth may increase Ix substantially. This geometric property alone does not set stiffness; the product EI includes elastic modulus.

A mechanical principle can be learned from more than one representation: a labeled drawing, a scalar equation, a vector equation, an experimental trend, and a limiting case. Translating between these forms is a valuable skill because real engineering work rarely arrives as a perfectly prepared algebra exercise.

Identify the reference axis and whether the calculated quantity is a mass property or an area property. A composite section must be decomposed into non-overlapping pieces. Area moments preserve the correct length power and should be checked by evaluating a symmetric limiting geometry.

## Deriving an appropriate model

Moving material away from a bending axis can increase stiffness while leaving total cross-sectional area unchanged. Sketch the positive and negative pieces of a composite section before taking moments.

## Worked engineering illustration

**Context:** Rectangular aluminum strip.

**Known information and task:** b=0.02 m, h=0.06 m.

**Equation:** `Ix=0.02×0.06³/12`.

**Reference outcome:** **3.60×10^-7 m^4**.

**Engineering interpretation:** Section geometry often changes deflection more efficiently than material substitution. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Confusing the mass moment of inertia with the area second moment.

A credible numerical result includes its reference axis, geometric dimension, and SI unit power. An area centroid is expressed in metres, a second moment of area in m^4, and a mass moment of inertia in kg·m². These are not interchangeable. If a section's depth doubles at constant width, its centroidal rectangular Ix increases by a factor of eight.

## Guided questions with answer criteria

**Q1 · Representation.** For rectangular aluminum strip, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `Ix=0.02×0.06³/12`.

**Q2 · Computation and trend.** Reproduce the calculation **b=0.02 m, h=0.06 m**, comparing with **3.60×10^-7 m^4**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `Ix=0.02×0.06³/12` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for rectangular aluminum strip but appears to be confusing the mass moment of inertia with the area second moment. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 4 · Lesson 4 — Parallel-axis theorem and composite inertia

**Unit objective:** Locate resultants of extended loads and compute geometric properties needed for bending and stiffness.

## Why this concept matters

For an area component whose centroidal axis is parallel to the target axis, I=I_c+A d². Use consistent coordinate units before summing pieces. The displacement term is always nonnegative for second moments about parallel axes; subtracting a hole means subtracting its complete contribution. For rotated axes or unsymmetric sections the product of inertia can also matter. The theorem is about relating parallel axes, not an automatic formula for every rotation.

The central difficulty here is not remembering a formula but deciding whether the physical interaction has been represented faithfully. A successful calculation is one whose geometry, units, and chosen body can be explained to a colleague before the numerical result is shown. That discipline becomes more important as an assembly contains more components.

Identify the reference axis and whether the calculated quantity is a mass property or an area property. A composite section must be decomposed into non-overlapping pieces. Area moments preserve the correct length power and should be checked by evaluating a symmetric limiting geometry.

## Deriving an appropriate model

Moving material away from a bending axis can increase stiffness while leaving total cross-sectional area unchanged. Sketch the positive and negative pieces of a composite section before taking moments.

## Worked engineering illustration

**Context:** Plate strip measured about edge.

**Known information and task:** b=0.03 m, h=0.08 m, centroid 0.04 m from edge.

**Equation:** `I_edge=bh³/12+bh×0.04²`.

**Reference outcome:** **5.12×10^-6 m^4**.

**Engineering interpretation:** The edge and centroidal axes give very different stiffness calculations. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Applying d instead of d squared.

A credible numerical result includes its reference axis, geometric dimension, and SI unit power. An area centroid is expressed in metres, a second moment of area in m^4, and a mass moment of inertia in kg·m². These are not interchangeable. If a section's depth doubles at constant width, its centroidal rectangular Ix increases by a factor of eight.

## Guided questions with answer criteria

**Q1 · Representation.** For plate strip measured about edge, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `I_edge=bh³/12+bh×0.04²`.

**Q2 · Computation and trend.** Reproduce the calculation **b=0.03 m, h=0.08 m, centroid 0.04 m from edge**, comparing with **5.12×10^-6 m^4**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `I_edge=bh³/12+bh×0.04²` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for plate strip measured about edge but appears to be applying d instead of d squared. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 4 · Lesson 5 — Distributed loads and equivalent reactions

**Unit objective:** Locate resultants of extended loads and compute geometric properties needed for bending and stiffness.

## Why this concept matters

A distributed load q(x) in N/m has resultant R=∫q(x)dx, applied at x_R=(∫xq(x)dx)/R if R≠0. Uniform loading produces a centered resultant. A triangular load has its centroid one third of the base length from the high-intensity end. These reductions preserve overall force and moment for reaction calculations, but shear and bending distributions inside the loaded member still depend on the original q(x).

Engineers often approach this subject in two directions: from a physical drawing to an equation, and from a computed answer back to a plausible physical action. Both directions matter. An unexplained number can be correct by coincidence, whereas a reproducible model can be corrected when assumptions change.

Identify the reference axis and whether the calculated quantity is a mass property or an area property. A composite section must be decomposed into non-overlapping pieces. Area moments preserve the correct length power and should be checked by evaluating a symmetric limiting geometry.

## Deriving an appropriate model

Moving material away from a bending axis can increase stiffness while leaving total cross-sectional area unchanged. Sketch the positive and negative pieces of a composite section before taking moments.

## Worked engineering illustration

**Context:** Uniform beam load.

**Known information and task:** q=350 N/m over a 3.0 m span.

**Equation:** `R=qL; x_R=L/2`.

**Reference outcome:** **1050 N at 1.50 m**.

**Engineering interpretation:** Accurate q(x) representation matters in downstream bending design. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Replacing a load by its resultant and then forgetting original distribution for internal-force diagrams.

A credible numerical result includes its reference axis, geometric dimension, and SI unit power. An area centroid is expressed in metres, a second moment of area in m^4, and a mass moment of inertia in kg·m². These are not interchangeable. If a section's depth doubles at constant width, its centroidal rectangular Ix increases by a factor of eight.

## Guided questions with answer criteria

**Q1 · Representation.** For uniform beam load, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `R=qL; x_R=L/2`.

**Q2 · Computation and trend.** Reproduce the calculation **q=350 n/m over a 3.0 m span**, comparing with **1050 N at 1.50 m**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `R=qL; x_R=L/2` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for uniform beam load but appears to be replacing a load by its resultant and then forgetting original distribution for internal-force diagrams. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

