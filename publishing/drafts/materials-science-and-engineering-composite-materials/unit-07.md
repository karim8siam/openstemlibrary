# Unit 7: Advanced composite families and multifunctionality

**Guiding question:** How do metal, ceramic, natural-fiber and multifunctional composites change the design problem?

## Why this unit matters to composite materials

A proposed conductive hybrid laminate reduces electrical resistance but loses interlaminar durability. This is a question about **non-polymer and multifunctional composite architectures** and the distinction between **one improved functional property versus complete system trade-off**. A defensible answer identifies fiber architecture, reinforcement and matrix properties, fabrication route, part geometry and loading direction before comparing measured performance. It also names the relevant failure mechanism: a design that maximizes axial stiffness can simultaneously increase sensitivity to delamination, compression after impact, moisture, manufacturing wrinkles or difficult field repairs. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Functional fillers and hybridized architectures can improve targeted performance while introducing new routes to embrittlement, corrosion, processing difficulty and environmental loss.

A fair comparison requires the same system function and service conditions; compare more than a conductivity or specific-stiffness number.

## Measurement and conservation checkpoints

Write down constituent identities, reinforcement form, interphase treatment, stacking sequence, process history and part geometry; define whether fractions are measured by area, mass or volume; and record the process history that could alter **hybrid geometry, matrix chemistry and loading**. For any local observation, describe why its sampling plan represents the part. Treat **added porosity or interface embrittlement** as an explicit rival explanation and plan **three-direction electrical/thermal measurements and fracture tests** as an independent check.

## Lesson 7.1: Metal matrix composites and wear

### Scientific foundation

Metal matrix composites retain a ductile or metallic continuous phase while adding ceramic particles, fibers or other reinforcements to tune stiffness, wear, thermal expansion or hot strength. The processing window must manage wetting and chemical reactions at interfaces; some systems form brittle reaction products. Particle addition can improve abrasion resistance but reduce machinability or ductility, and the resulting properties may be highly anisotropic after deformation processing.

**Governing relationship or decision rule:** A useful wear comparison reports volume loss per distance and load together with the regime and counterface. Read every term in the equation as part of a declared specimen condition. In **metal matrix composites and wear**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare two aluminum-matrix particle fractions under an equal wear-test geometry and actual recorded normal loads. Distinguish mass loss from volume loss using density and identify whether altered roughness or detached hard particles drive counterface wear.

A companion calculator called **Ideal particulate composite density** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Particle volume fraction = 0.1214286 fraction**, the declared formula returns **2.8457143 g/cm3**; at **Particle volume fraction = 0.1928571 fraction**, it returns **2.9314286 g/cm3**. On this interval the modeled value increases, and the two-point slope is **1.2 g/cm3 per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `3.9*Vp+2.7*(1-Vp)`. Model validity is limited to: **No voids, hypothetical ceramic particle density 3.9 g/cm3 and metal matrix density 2.7 g/cm3**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Wear rankings depend on load, speed, lubrication, counterface and contact temperature; no one 'wear coefficient' serves every regime.

### Exercises and self-assessment

**Exercise 7.1A — Physical mechanism.** How could increasing hard-particle fraction make sliding wear worse under different contact conditions? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.1B — Numerical cross-check.** Recalculate **2.8457143 g/cm3** from the companion formula at **0.1214286 fraction** and compare with **2.9314286 g/cm3** at **0.1928571 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 7.1C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **added porosity or interface embrittlement**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_12 -->

## Lesson 7.2: Ceramic matrix composites at high temperature

### Scientific foundation

Ceramic matrix composites can gain damage tolerance through fiber bridging and engineered interfaces, avoiding some abrupt monolithic ceramic failures. Their response depends on oxidation, crack deflection and environmental barrier coatings. Reinforcing carbon fibers in oxidizing atmospheres poses particular limitations, and SiC-based systems have their own recession and coating issues. High-temperature strength is not synonymous with high-temperature lifetime under combined stress, water vapor and cycles.

**Governing relationship or decision rule:** Composite toughening relies on controlled crack/interface interactions and must be balanced with environmental stability. Read every term in the equation as part of a declared specimen condition. In **ceramic matrix composites at high temperature**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare a notched monolithic ceramic sample and a fiber-reinforced ceramic at temperature. Plan microscopy of crack paths and unloading-reloading hysteresis, along with environmental exposures. Specify why observing multiple matrix cracks does not automatically indicate impending catastrophic failure.

A companion calculator called **Toy percolation threshold behavior** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Conductive filler fraction = 0.1285714 fraction**, the declared formula returns **0.61734694 S/m**; at **Conductive filler fraction = 0.1628571 fraction**, it returns **1.2736735 S/m**. On this interval the modeled value increases, and the two-point slope is **19.142857 S/m per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `100*Math.pow(Math.max(0,phi-0.05),2)`. Model validity is limited to: **Synthetic percolation-like response, phi_c=0.05, exponent 2 and coefficient 100 chosen for teaching, not a material prediction**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Coupon behavior in dry inert test gas is not proof of durability in a turbine-like combustion environment.

### Exercises and self-assessment

**Exercise 7.2A — Physical mechanism.** What interfacial property allows crack deflection but may introduce a new oxidation vulnerability? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.2B — Numerical cross-check.** Recalculate **0.61734694 S/m** from the companion formula at **0.1285714 fraction** and compare with **1.2736735 S/m** at **0.1628571 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 7.2C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **added porosity or interface embrittlement**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_13 -->

## Lesson 7.3: Natural-fiber and bio-based composites

### Scientific foundation

Natural fibers can reduce some feedstock impacts but exhibit moisture sensitivity, property variability and extraction-related damage. Cellulose-rich reinforcements can suffer from incompatible polymer wetting, thermal processing limits and anisotropic swelling. Calling a material bio-based does not establish compostability, food safety, low life-cycle impact or mechanical equivalence to glass fiber. Fiber origin, length distribution, surface treatment and agricultural variability must be traced.

**Governing relationship or decision rule:** Materials must be compared on a service-equivalent functional unit with measured conditioned properties. Read every term in the equation as part of a declared specimen condition. In **natural-fiber and bio-based composites**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare flax/polymer and glass/polymer panels designed for identical bending stiffness in the same humidity condition. Calculate approximate mass requirements using measured specific stiffness rather than comparing kilograms of raw fiber. Propose water uptake and conditioning protocols plus an audited functional-unit assessment.

A companion calculator called **Ideal particulate composite density** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Particle volume fraction = 0.2642857 fraction**, the declared formula returns **3.0171429 g/cm3**; at **Particle volume fraction = 0.3357143 fraction**, it returns **3.1028571 g/cm3**. On this interval the modeled value increases, and the two-point slope is **1.2 g/cm3 per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Natural-fiber strength dispersions can be broad and correlated with harvest, moisture and processing history.

### Exercises and self-assessment

**Exercise 7.3A — Physical mechanism.** Why might an apparently lighter bio-composite require a thicker, heavier part in humid service? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.3B — Numerical cross-check.** Recalculate **3.0171429 g/cm3** from the companion formula at **0.2642857 fraction** and compare with **3.1028571 g/cm3** at **0.3357143 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 7.3C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **added porosity or interface embrittlement**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_12 -->

## Lesson 7.4: Electrical and thermal multifunctionality

### Scientific foundation

Conductive fibers, graphene, carbon particles and aligned fillers can change electrical pathways and directional heat conduction. Percolation means that conductivity can rise sharply over a restricted filler range, but thresholds depend on filler shape, dispersion, contact and processing. An electrically conductive surface can alter lightning-strike behavior and galvanic coupling yet introduce dielectric risks. Thermal conductivity along carbon fibers may greatly exceed through-thickness conductivity across polymer interfaces.

**Governing relationship or decision rule:** A simplified above-threshold percolation law sigma=C(phi−phi_c)^t needs system-specific parameters. Read every term in the equation as part of a declared specimen condition. In **electrical and thermal multifunctionality**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Create an illustrative percolation-style conductivity plot, explicitly labeled synthetic rather than universal. Compare measured in-plane and through-thickness resistances over humidity and thermal cycle conditions. Evaluate how conductivity improvements compete with viscosity, porosity and interlaminar toughness.

A companion calculator called **Toy percolation threshold behavior** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Conductive filler fraction = 0.1971429 fraction**, the declared formula returns **2.165102 S/m**; at **Conductive filler fraction = 0.2314286 fraction**, it returns **3.2916327 S/m**. On this interval the modeled value increases, and the two-point slope is **32.857143 S/m per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

A smooth power law fit near a threshold should not be extrapolated across different dispersion states or switching mechanisms.

### Exercises and self-assessment

**Exercise 7.4A — Physical mechanism.** Why can a part show strong in-plane conduction but poor heat extraction through thickness? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.4B — Numerical cross-check.** Recalculate **2.165102 S/m** from the companion formula at **0.1971429 fraction** and compare with **3.2916327 S/m** at **0.2314286 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 7.4C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **added porosity or interface embrittlement**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_13 -->

## Lesson 7.5: Hybrid architectures and topology

### Scientific foundation

Combining carbon and glass, continuous and chopped fibers, or fiber and particle phases can tailor impact, cost, damping and stiffness. Hybrid effects depend on where reinforcements are placed, strain-to-failure mismatch and interfacial load transfer. An apparent synergy may simply arise from a changed total fiber fraction or laminate thickness; compare against a controlled rule-of-mixtures baseline. Spatial topology matters for crack arrest and manufacturability more than a single bulk composition label.

**Governing relationship or decision rule:** Hybrid optimization must control geometry, fraction and the complete damage sequence to evaluate synergy. Read every term in the equation as part of a declared specimen condition. In **hybrid architectures and topology**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Design a hybrid beam with stiff carbon face plies and impact-tolerant glass or polymer layers near a likely strike surface. Use a bending-section sketch to establish which placement is effective, then plan matched-mass and matched-bending-rigidity tests to expose different trade-offs.

A companion calculator called **Ideal particulate composite density** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Particle volume fraction = 0.4071429 fraction**, the declared formula returns **3.1885714 g/cm3**; at **Particle volume fraction = 0.4785714 fraction**, it returns **3.2742857 g/cm3**. On this interval the modeled value increases, and the two-point slope is **1.2 g/cm3 per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Brittle outer carbon layers may fail early under local compression and negate a naive stiffness gain.

### Exercises and self-assessment

**Exercise 7.5A — Physical mechanism.** What matched baseline distinguishes a genuine positive hybrid effect from adding extra reinforcement mass? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.5B — Numerical cross-check.** Recalculate **3.1885714 g/cm3** from the companion formula at **0.4071429 fraction** and compare with **3.2742857 g/cm3** at **0.4785714 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 7.5C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **added porosity or interface embrittlement**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_12 -->

## Integrated investigation: A multifunctional structure with a hidden trade-off

### The evidence problem

A proposed conductive hybrid laminate reduces electrical resistance but loses interlaminar durability. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which reinforcement architecture or processing route seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Identify dispersion topology, conductive direction, interface chemistry, filler-induced viscosity and bonding changes. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **non-polymer and multifunctional composite architectures** and **one improved functional property versus complete system trade-off** through the map. For micromechanics, state axial or transverse boundary assumptions and measure fiber fraction independently. For an orthotropic lamina, transform elastic constants with explicit material axes. For a laminate, calculate through-thickness stiffness and test bending-extension coupling. For manufacturing, distinguish commanded temperature from actual part cure and flow history. For damage, match local crack or impact driving force with mode-appropriate conditioned fracture resistance.

### Validation plan, report, and counterfactual

Measure anisotropic conduction, porosity, interlaminar fracture and cyclic environmental performance in matched configurations. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing composite families, write down the constraints that matter for directional stiffness, delamination toughness, impact damage, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** A fitted percolation threshold does not extrapolate across processing routes. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **non-polymer and multifunctional composite architectures** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **one improved functional property versus complete system trade-off** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **added porosity or interface embrittlement** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_13 -->

