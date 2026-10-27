# Unit 4: Laminate theory, stacking sequences, and stability

**Guiding question:** How do individual ply responses combine into membrane and bending behavior?

## Why this unit matters to composite materials

A thin laminated access cover curves after cure and twists during an in-plane tension test. This is a question about **extension and bending of stacked plies** and the distinction between **ply-level stiffness versus laminate coupling**. A defensible answer identifies fiber architecture, reinforcement and matrix properties, fabrication route, part geometry and loading direction before comparing measured performance. It also names the relevant failure mechanism: a design that maximizes axial stiffness can simultaneously increase sensitivity to delamination, compression after impact, moisture, manufacturing wrinkles or difficult field repairs. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Laminate stiffness depends on both the proportion and depth placement of plies. Balanced and symmetric stacks remove different coupling effects and should be tested separately.

A plate theory provides global force/curvature relations but cannot by itself resolve a free-edge delamination or bearing stress near a drilled hole.

## Measurement and conservation checkpoints

Write down constituent identities, reinforcement form, interphase treatment, stacking sequence, process history and part geometry; define whether fractions are measured by area, mass or volume; and record the process history that could alter **ply order, actual thickness and reference midplane**. For any local observation, describe why its sampling plan represents the part. Treat **cure-induced curvature or unexpected D16/D26 coupling** as an explicit rival explanation and plan **full-field curvature and ply stack inspection** as an independent check.

## Lesson 4.1: Ply orientation and stack notation

### Scientific foundation

A laminate specification records not only angles but also material axes, ply order, thickness and reference surface. A balanced sequence has equal amounts of +theta and −theta plies, while a symmetric sequence mirrors material and geometry about the midplane. Balance and symmetry address different stiffness couplings and are not interchangeable. A [0/90] stack is not generally identical in bending response to [90/0] when referenced to the same physical surface. Ply drops create termination stresses.

**Governing relationship or decision rule:** For symmetric material/thickness distribution, B=0 in classical laminate theory. Read every term in the equation as part of a declared specimen condition. In **ply orientation and stack notation**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Write explicit full stacking sequences for [0/45/−45/90]s and a balanced nonsymmetric alternative. Identify which plies cross the midplane and why a symmetric pair can have zero extension-bending B matrix under ideal assumptions. Discuss consequences of a misplaced 90-degree layer near a loaded surface.

A companion calculator called **A11 for a homogeneous aligned panel** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Laminate thickness = 1.571429 mm**, the declared formula returns **212142.86 N/mm**; at **Laminate thickness = 2.642857 mm**, it returns **356785.71 N/mm**. On this interval the modeled value increases, and the two-point slope is **135000 N/mm per mm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `135000*t`. Model validity is limited to: **Qbar11=135000 MPa; for thickness t in mm, A11=Qbar11*t in N/mm; single homogeneous aligned region**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Layup shorthand must state convention for angle direction, top-to-bottom ordering and whether thicknesses match.

### Exercises and self-assessment

**Exercise 4.1A — Physical mechanism.** Why does a mirror-symmetric stack reduce B without ensuring absence of all shear-extension coupling? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.1B — Numerical cross-check.** Recalculate **212142.86 N/mm** from the companion formula at **1.571429 mm** and compare with **356785.71 N/mm** at **2.642857 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 4.1C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **cure-induced curvature or unexpected D16/D26 coupling**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_6 -->

## Lesson 4.2: The ABD constitutive matrix

### Scientific foundation

Classical laminate theory integrates the transformed reduced stiffness Qbar through the thickness. The A matrix maps midplane strains to in-plane forces, B couples strains with curvature, and D maps curvatures to bending moments. A terms have units force per length, B terms force, and D terms force times length for SI per-unit-width resultants. It is a thin-plate idealization; transverse shear strains and delamination are not resolved directly. Plies must be integrated with actual z coordinates.

**Governing relationship or decision rule:** Aij=Σ Qbarij(z_k−z_{k−1}); Dij=(1/3)Σ Qbarij(z_k³−z_{k−1}³). Read every term in the equation as part of a declared specimen condition. In **the abd constitutive matrix**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Consider a homogeneous unidirectional plate of thickness t with constant Qbar11. Calculate A11=Qbar11 t and D11=Qbar11 t³/12 for a midplane origin. Doubling t doubles membrane stiffness but increases bending stiffness eightfold in this restricted case. Explain how this differs from simply doubling plies at fixed total thickness.

A companion calculator called **D11 for a homogeneous aligned panel** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Laminate thickness = 2.642857 mm**, the declared formula returns **207669.92 N mm**; at **Laminate thickness = 3.714286 mm**, it returns **576472.3 N mm**. On this interval the modeled value increases, and the two-point slope is **344215.56 N mm per mm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `135000*Math.pow(t,3)/12`. Model validity is limited to: **Qbar11=135000 N/mm2; D11=Qbar11*t^3/12 in N mm per unit width under classical thin plate assumptions**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Classical plate theory ignores interlaminar stress concentration and may be inadequate for thick sandwiches or soft cores.

### Exercises and self-assessment

**Exercise 4.2A — Physical mechanism.** Why does moving stiff plies toward the surfaces change bending more than membrane stiffness? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.2B — Numerical cross-check.** Recalculate **207669.92 N mm** from the companion formula at **2.642857 mm** and compare with **576472.3 N mm** at **3.714286 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 4.2C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **cure-induced curvature or unexpected D16/D26 coupling**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_7 -->

## Lesson 4.3: Symmetry, balance, and coupling

### Scientific foundation

Symmetry removes classical extension-bending coupling B, whereas balance commonly reduces extensional A16 and A26 terms in angle-ply arrangements under matching thickness. Neither property guarantees zero D16 and D26 bending-twisting coupling. Unsymmetric laminates can twist or bend under membrane loads and thermal excursions. Treating an unexpected twist as defective manufacturing without reviewing B and D coupling can misdiagnose the problem. Mechanical response also depends on boundary restraints.

**Governing relationship or decision rule:** Stacking symmetry is sufficient for B=0 under ideal classical assumptions, not for all couplings to vanish. Read every term in the equation as part of a declared specimen condition. In **symmetry, balance, and coupling**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare a symmetric balanced [0/45/−45/90]s stack with an unsymmetric [0/90/45/−45] stack. Sketch plausible A, B and D nonzero patterns without computing fictional exact constants. Propose an extension test with full-field tracking to detect load-induced curvature and identify thermal warp as a confounder.

A companion calculator called **A11 for a homogeneous aligned panel** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Laminate thickness = 3.714286 mm**, the declared formula returns **501428.57 N/mm**; at **Laminate thickness = 4.785714 mm**, it returns **646071.43 N/mm**. On this interval the modeled value increases, and the two-point slope is **135000 N/mm per mm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Residual cure distortion can mask or imitate elastic coupling, and slight thickness imbalance undermines ideal symmetry.

### Exercises and self-assessment

**Exercise 4.3A — Physical mechanism.** Can a symmetric balanced laminate still bend and twist under bending? Explain which D terms must be checked. State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.3B — Numerical cross-check.** Recalculate **501428.57 N/mm** from the companion formula at **3.714286 mm** and compare with **646071.43 N/mm** at **4.785714 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 4.3C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **cure-induced curvature or unexpected D16/D26 coupling**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_6 -->

## Lesson 4.4: Laminate optimization and manufacturability

### Scientific foundation

An optimization that maximizes a scalar stiffness while ignoring loads, buckling, thickness, access, defects and permissible ply patterns is incomplete. Many manufacturable layups constrain changes of angle between adjacent layers, group plies, require minimum percentages of key directions or enforce blending across neighboring panels. Design variables are discrete and often create nonconvex search spaces. Optimizing nominal elastic response does not automatically preserve damage tolerance.

**Governing relationship or decision rule:** Optimize multiple measured or validated performance criteria under explicit geometric and process constraints. Read every term in the equation as part of a declared specimen condition. In **laminate optimization and manufacturability**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Define two competing objectives for a hypothetical aircraft access panel: in-plane buckling reserve and impact damage tolerance. Set constraints on thickness, symmetric stacking, allowed ply angles, tool access and manufacturing inspection. Compare Pareto alternatives rather than calling a single A11-maximizing stack 'optimal'.

A companion calculator called **D11 for a homogeneous aligned panel** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Laminate thickness = 4.785714 mm**, the declared formula returns **1233084.5 N mm**; at **Laminate thickness = 5.857143 mm**, it returns **2260528.4 N mm**. On this interval the modeled value increases, and the two-point slope is **958947.7 N mm per mm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

A numerical optimum is conditional on uncertain material allowables and may be infeasible to lay up or inspect.

### Exercises and self-assessment

**Exercise 4.4A — Physical mechanism.** What evidence would justify replacing a manufacturable conservative layup with a lighter calculated optimum? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.4B — Numerical cross-check.** Recalculate **1233084.5 N mm** from the companion formula at **4.785714 mm** and compare with **2260528.4 N mm** at **5.857143 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 4.4C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **cure-induced curvature or unexpected D16/D26 coupling**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_7 -->

## Lesson 4.5: Sandwich panels and local instability

### Scientific foundation

Sandwich structures separate relatively stiff face sheets with a lightweight core to improve bending stiffness and specific stability. The core transfers transverse shear and stabilizes faces, but can fail in shear, indentation, wrinkling, debonding or local crushing. Classical single-layer laminate plate theory can miss those mechanisms. Core density gradients, adhesive bondlines and thermal mismatches complicate analysis. Panel performance depends strongly on support spans, load footprints and edge closeout design.

**Governing relationship or decision rule:** Face contribution to bending scales roughly with Ef tf h² when faces are thin and well bonded. Read every term in the equation as part of a declared specimen condition. In **sandwich panels and local instability**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Estimate the bending rigidity trend of a symmetric sandwich by treating two equal face sheets as area concentrated at distance h/2 from the midplane. Compare face separation of 10 and 20 mm at the same face properties, and describe what must be measured to avoid core-shear-limited performance.

A companion calculator called **A11 for a homogeneous aligned panel** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Laminate thickness = 5.857143 mm**, the declared formula returns **790714.29 N/mm**; at **Laminate thickness = 6.928571 mm**, it returns **935357.14 N/mm**. On this interval the modeled value increases, and the two-point slope is **135000 N/mm per mm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Face-sheet separation improves bending capacity only while local instability, shear and bond failure remain adequately controlled.

### Exercises and self-assessment

**Exercise 4.5A — Physical mechanism.** Why can a sandwich beam with enormous ideal bending stiffness still deflect excessively? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.5B — Numerical cross-check.** Recalculate **790714.29 N/mm** from the companion formula at **5.857143 mm** and compare with **935357.14 N/mm** at **6.928571 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 4.5C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **cure-induced curvature or unexpected D16/D26 coupling**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_6 -->

## Integrated investigation: A laminate that twists unexpectedly

### The evidence problem

A thin laminated access cover curves after cure and twists during an in-plane tension test. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which reinforcement architecture or processing route seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Compute appropriate A, B and D tendencies from measured ply order and thickness; contrast thermal distortion with elastic coupling. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **extension and bending of stacked plies** and **ply-level stiffness versus laminate coupling** through the map. For micromechanics, state axial or transverse boundary assumptions and measure fiber fraction independently. For an orthotropic lamina, transform elastic constants with explicit material axes. For a laminate, calculate through-thickness stiffness and test bending-extension coupling. For manufacturing, distinguish commanded temperature from actual part cure and flow history. For damage, match local crack or impact driving force with mode-appropriate conditioned fracture resistance.

### Validation plan, report, and counterfactual

Map ply geometry and temperature history, compare symmetric control layup, and measure full-field curvature under known loads. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing composite families, write down the constraints that matter for directional stiffness, delamination toughness, impact damage, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** Thin-plate results do not resolve bondline peel or damage at ply drops. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **extension and bending of stacked plies** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **ply-level stiffness versus laminate coupling** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **cure-induced curvature or unexpected D16/D26 coupling** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_7 -->

