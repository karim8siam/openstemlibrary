# Unit 1: Constituents, architectures, and composite identity

**Guiding question:** What structural features distinguish a composite from a nominal mixture of material phases?

## Why this unit matters to composite materials

An engineering team compares woven glass, carbon tape, and chopped fiber with insufficiently defined design loads. This is a question about **constituent identity and reinforcement orientation** and the distinction between **material recipe versus manufactured microstructure**. A defensible answer identifies fiber architecture, reinforcement and matrix properties, fabrication route, part geometry and loading direction before comparing measured performance. It also names the relevant failure mechanism: a design that maximizes axial stiffness can simultaneously increase sensitivity to delamination, compression after impact, moisture, manufacturing wrinkles or difficult field repairs. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Many composite identity errors arise when a vendor reports a constituent recipe as though it were the local phase geometry of a cured part. Resolve the distinction with measured density, fiber direction, material history and representative defect imaging.

Different architecture scales require different evidence: a filament image cannot establish laminate thickness uniformity; a whole-panel scan may miss the interphase chemistry that governs local transfer.

The five lessons use distinct physical ideas but follow a common audit: establish a material state, derive an equation with dimensions, vary an input in the declared simulation range, articulate a rival explanation, and propose a separate instrument-based observation. The unit's two interactive models are deliberately narrower than any validated composite-property and damage database. Use them to understand sensitivity, not to certify processing parameters.

## Measurement and conservation checkpoints

Write down constituent identities, reinforcement form, interphase treatment, stacking sequence, process history and part geometry; define whether fractions are measured by area, mass or volume; and record the process history that could alter **phase density, fiber form and part-level architecture**. For any local observation, describe why its sampling plan represents the part. Treat **unseen voids or orientation gradients** as an explicit rival explanation and plan **tomography plus representative cross-sectional microscopy** as an independent check.

## Lesson 1.1: Composite phases and material identity

### Scientific foundation

A composite contains distinguishable constituents and architecture that jointly determine properties. A continuous-fiber carbon/epoxy lamina is fundamentally unlike a carbon-filled epoxy particulate mixture: both combine phases, but their load paths, anisotropy and typical defects are not interchangeable. Identify matrix, reinforcement, interphase, voids and optional coatings before quoting a property. Architecture includes orientation, size, spatial correlation, layering and manufacturing history, not merely chemistry. The term composite is a description of a heterogeneous material, not a guarantee of high specific strength.

**Governing relationship or decision rule:** Report constituents, morphology, orientation distribution and void content before making structure–property comparisons. Read every term in the equation as part of a declared specimen condition. In **composite phases and material identity**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare an aligned glass-fiber panel with an injection-molded chopped-fiber housing at similar fiber mass fraction. Sketch two representative volume elements, noting discontinuities and likely shear transfer lengths. Explain why a tabulated single axial modulus cannot predict a bolt-hole stress field or out-of-plane compression.

A companion calculator called **Nominal fiber volume from mass fraction** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fiber mass fraction = 0.2857143 fraction**, the declared formula returns **0.21052632 fraction**; at **Fiber mass fraction = 0.3714286 fraction**, it returns **0.2826087 fraction**. On this interval the modeled value increases, and the two-point slope is **0.8409611 fraction per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `(w/1.8)/(w/1.8+(1-w)/1.2)`. Model validity is limited to: **No voids, two phases, hypothetical fiber and matrix densities 1.8 and 1.2 g/cm3; no sizing or fillers**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

A phase may not be resolved at the chosen imaging length scale, and effective properties change with the scale of observation.

Begin with constituent volume and mass ledgers, a ply/part geometry sketch with material-axis orientation, and an actual time–temperature–pressure history where fabrication conditions matter. Mark the quantities that came from direct measurement and those adopted from the toy model. Evaluate a limiting case such as zero fiber fraction, a ply angle of zero or ninety degrees, vanishing thickness, a flaw outside the assumed fracture regime, or a thermal condition inconsistent with model calibration. A failed limiting case does not mean algebra is wrong; it may mean the model has left its physical domain.

### Exercises and self-assessment

**Exercise 1.1A — Physical mechanism.** Why is equal constituent mass fraction insufficient to establish equal stiffness? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 1.1B — Numerical cross-check.** Recalculate **0.21052632 fraction** from the companion formula at **0.2857143 fraction** and compare with **0.2826087 fraction** at **0.3714286 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 1.1C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **unseen voids or orientation gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_0 -->

## Lesson 1.2: Reinforcement forms and length scales

### Scientific foundation

Reinforcements include continuous tows, woven fabrics, noncrimp multiaxial fabrics, chopped strands, flakes and particles. Fiber aspect ratio controls whether useful tensile force can develop before a fiber end, while waviness changes the direction of a local load path. The crimp of a woven fabric can change tensile stiffness and compression response. Layup notation must distinguish tow direction from fabric style and balanced arrangements. Fibers have orientation distributions in three-dimensional molded flow and should not be assigned a single nominal angle.

**Governing relationship or decision rule:** Geometry and the statistical distribution of reinforcement are independent design variables. Read every term in the equation as part of a declared specimen condition. In **reinforcement forms and length scales**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

For a hypothetical sheet compare unidirectional tape and plain-weave fabric of the same constituents. Assign a plausible area covered by warp and weft but do not assume the fabric is a pair of straight unidirectional plies. Plan microscopy over multiple locations to quantify tow waviness and distinguish it from a misaligned ply.

A companion calculator called **Void-free mixture density** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fiber volume fraction = 0.3214286 fraction**, the declared formula returns **1.3928571 g/cm3**; at **Fiber volume fraction = 0.4071429 fraction**, it returns **1.4442857 g/cm3**. On this interval the modeled value increases, and the two-point slope is **0.6 g/cm3 per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `1.8*Vf+1.2*(1-Vf)`. Model validity is limited to: **Two constituents with densities 1.8 and 1.2 g/cm3, zero voids, no chemical volume change**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Tow crossovers create resin pockets, and noncrimp stitching can introduce local imperfections. A measured planar orientation may hide through-thickness changes.

### Exercises and self-assessment

**Exercise 1.2A — Physical mechanism.** Under what geometry could a woven composite outperform a higher-modulus unidirectional sheet? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 1.2B — Numerical cross-check.** Recalculate **1.3928571 g/cm3** from the companion formula at **0.3214286 fraction** and compare with **1.4442857 g/cm3** at **0.4071429 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 1.2C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **unseen voids or orientation gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_1 -->

## Lesson 1.3: Matrix materials and temperature constraints

### Scientific foundation

A polymer matrix supports and separates reinforcing fibers, transfers local shear, controls much of transverse response, and influences toughness and service temperature. Epoxy, polyester and high-performance thermoplastic matrices offer different processing routes and residual stress histories. Metals and ceramics can also serve as matrices where temperatures or wear conditions make polymers inappropriate, but introduce other reactivity and processing limits. Matrix tensile strength alone cannot define a fiber-dominated axial laminate strength; failure often depends on the weakest local stress state.

**Governing relationship or decision rule:** Temperature, strain rate and moisture can strongly alter matrix-dominated response without changing intrinsic fiber elasticity. Read every term in the equation as part of a declared specimen condition. In **matrix materials and temperature constraints**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Analyze a panel that becomes soft above its wet glass-transition region but whose carbon fibers retain high stiffness. Compare dry and moisture-conditioned DMA and short-beam or off-axis results. Require actual cured resin state and service thermal excursions, not datasheet neat-resin temperature alone.

A companion calculator called **Nominal fiber volume from mass fraction** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fiber mass fraction = 0.4571429 fraction**, the declared formula returns **0.35955056 fraction**; at **Fiber mass fraction = 0.5428571 fraction**, it returns **0.44186047 fraction**. On this interval the modeled value increases, and the two-point slope is **0.96028221 fraction per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

A glass-transition temperature is protocol-dependent and not a universal maximum-use temperature. Interface chemistry and cure state must be considered.

### Exercises and self-assessment

**Exercise 1.3A — Physical mechanism.** Why can the axial modulus look stable when matrix-dominated shear capacity falls severely? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 1.3B — Numerical cross-check.** Recalculate **0.35955056 fraction** from the companion formula at **0.4571429 fraction** and compare with **0.44186047 fraction** at **0.5428571 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 1.3C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **unseen voids or orientation gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_0 -->

## Lesson 1.4: Fiber properties and failure statistics

### Scientific foundation

Glass, carbon, aramid and basalt fibers differ in stiffness, density, damage sensitivity, surface treatment and failure strain. Brittle fibers exhibit strength variability from flaws and gauge-length effects; nominal fiber tensile strength cannot be transferred directly to a large cured part. Carbon fibers often have pronounced axial/transverse asymmetry and electrical conductivity that can matter for galvanic contact. Aramid responds differently in compression than in axial tension. Selection therefore depends on the complete use case and integration into a matrix.

**Governing relationship or decision rule:** Specific axial modulus is E/rho only for a defined direction and comparable performance requirement. Read every term in the equation as part of a declared specimen condition. In **fiber properties and failure statistics**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Propose a tension member with a strict mass budget and an impact-sensitive casing with a different constraint. Compare specific stiffness using representative symbolic densities rather than inventing a manufacturer's qualified values. List tests necessary to establish fiber lot variability, actual composite compression and environmental durability.

A companion calculator called **Void-free mixture density** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fiber volume fraction = 0.4928571 fraction**, the declared formula returns **1.4957143 g/cm3**; at **Fiber volume fraction = 0.5785714 fraction**, it returns **1.5471429 g/cm3**. On this interval the modeled value increases, and the two-point slope is **0.6 g/cm3 per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Fiber sizing changes bonding and handling but may not be captured by the nominal fiber designation.

### Exercises and self-assessment

**Exercise 1.4A — Physical mechanism.** Why is the strongest single filament not evidence of the strongest laminate? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 1.4B — Numerical cross-check.** Recalculate **1.4957143 g/cm3** from the companion formula at **0.4928571 fraction** and compare with **1.5471429 g/cm3** at **0.5785714 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 1.4C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **unseen voids or orientation gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_1 -->

## Lesson 1.5: Volume fraction, voids, and density

### Scientific foundation

Fiber fraction is generally needed by volume in micromechanics whereas suppliers often report mass fraction. Conversion requires constituent densities and an explicit allowance for voids, sizing and filler. Measured part density can diagnose nonuniform compaction but is not unique proof of void morphology. A mixture mass balance gives a nominal void-free density that is distinct from an actual porous sample. Increasing fiber fraction may raise axial modulus but simultaneously worsen wet-out, permeability and delamination resistance.

**Governing relationship or decision rule:** Vf=(wf/rhof)/[(wf/rhof)+(1-wf)/rhom] in a void-free two-phase mixture. Read every term in the equation as part of a declared specimen condition. In **volume fraction, voids, and density**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Take a fiber mass fraction of 0.60, fiber density 1.80 g/cm3 and resin density 1.20 g/cm3. Calculate nominal fiber volume fraction as (0.60/1.80)/[(0.60/1.80)+(0.40/1.20)]=0.50 for zero voids. Evaluate what part density is expected if 2% porosity is introduced under stated assumptions and what additional measurement distinguishes closed pores from resin-rich regions.

A companion calculator called **Nominal fiber volume from mass fraction** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fiber mass fraction = 0.6285714 fraction**, the declared formula returns **0.53012048 fraction**; at **Fiber mass fraction = 0.7142857 fraction**, it returns **0.625 fraction**. On this interval the modeled value increases, and the two-point slope is **1.1069277 fraction per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Void fraction cannot be derived reliably from one section or a single hydrostatic measurement when absorbed water and open porosity are uncontrolled.

### Exercises and self-assessment

**Exercise 1.5A — Physical mechanism.** How can two panels with the same fiber mass fraction exhibit different measured densities? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 1.5B — Numerical cross-check.** Recalculate **0.53012048 fraction** from the companion formula at **0.6285714 fraction** and compare with **0.625 fraction** at **0.7142857 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 1.5C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **unseen voids or orientation gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_0 -->

## Integrated investigation: Architecture selection for a lightweight panel

### The evidence problem

An engineering team compares woven glass, carbon tape, and chopped fiber with insufficiently defined design loads. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which reinforcement architecture or processing route seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Specify material axes, fiber fraction, matrix, moisture, local joints and damage modes; avoid a mass-only ranking. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **constituent identity and reinforcement orientation** and **material recipe versus manufactured microstructure** through the map. For micromechanics, state axial or transverse boundary assumptions and measure fiber fraction independently. For an orthotropic lamina, transform elastic constants with explicit material axes. For a laminate, calculate through-thickness stiffness and test bending-extension coupling. For manufacturing, distinguish commanded temperature from actual part cure and flow history. For damage, match local crack or impact driving force with mode-appropriate conditioned fracture resistance.

Calculate outputs from both unit models at the midpoint and at an off-center slider position. Provide output units, fractional change, and a reason that the two mathematical relationships are related to different portions of the composite-materials question. Explain which constant would require independent experimental calibration and whether a plausible change in that constant could reverse the proposed design conclusion. A sensitivity result without a credible physical uncertainty model is a map of an equation, not evidence of service reliability.

### Validation plan, report, and counterfactual

Verify bulk fraction, three-dimensional orientation and conditioned coupon response before a component-level downselect. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing composite families, write down the constraints that matter for directional stiffness, delamination toughness, impact damage, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** Nominal constituents do not establish through-thickness strength or defect tolerance. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **constituent identity and reinforcement orientation** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **material recipe versus manufactured microstructure** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **unseen voids or orientation gradients** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_1 -->

