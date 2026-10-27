# Unit 2: Polymer thermodynamics and phase transitions

**Guiding question:** When do polymer systems mix, vitrify, crystallize or form two phases?

## Why this unit matters to polymer science

Two films have similar DSC crystalline fractions but different haze and shrinkage after heat treatment. This is a question about **polymer phase stability and morphology** and the distinction between **thermodynamic tendency versus kinetically arrested structure**. A defensible answer identifies chain chemistry, molecular distribution, processing path and morphology before comparing measured properties. It also names the potentially controlling failure mode: a formulation that optimizes short-term stiffness, melt-flow index or optical clarity can still worsen creep resistance, process stability, environmental cracking or barrier lifetime. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Phase behavior combines composition, chain length, interaction energies and strong kinetic restrictions. A quenched film can remain amorphous even where a slowly cooled analog crystallizes.

Compare first-heat and second-heat transitions; report whether the sample changed while being measured rather than assuming its initial morphology remained fixed.

## Measurement and conservation checkpoints

Write down the starting chain chemistry, distribution, additive package and processing history; define whether reported fractions are by area, mass, moles or volume; and record the process history that could alter **temperature history, composition and solvent activity**. For any local observation, describe why its sampling plan represents the part. Treat **a changed nucleation density or trapped solvent** as an explicit rival explanation and plan **DSC and SAXS/WAXS plus microscopy** as an independent check.

## Lesson 2.1: Free energy of mixing and solvent quality

### Scientific foundation

Dissolution is governed by Gibbs free-energy change, not by a visual resemblance between solvent and repeat unit. The Flory–Huggins lattice picture combines configurational mixing entropy with an interaction term χ; polymer chains lose relatively little entropy upon mixing compared with small molecules because one chain occupies many segments. This helps explain why solvent quality and temperature can change phase behavior sharply. Mixtures may be metastable despite negative total mixing free energy if local curvature allows phase separation.

**Governing relationship or decision rule:** The simplified Flory–Huggins dimensionless mixing free energy per lattice site is (φ/N)lnφ+(1−φ)ln(1−φ)+χφ(1−φ). Read every term in the equation as part of a declared specimen condition. In **free energy of mixing and solvent quality**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Construct a qualitative free-energy curve versus polymer volume fraction for several χ values at fixed ideal chain length. Indicate a stable one-phase state, coexistence by common tangent and instability signaled by negative curvature. Compare a film that appears clear immediately after solvent casting with one that turns cloudy after annealing; discuss nucleation versus spinodal decomposition.

A companion calculator called **Fox estimate of miscible blend Tg** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Mass fraction of component one = 0.1428571 fraction**, the declared formula returns **353.7234 K**; at **Mass fraction of component one = 0.2857143 fraction**, it returns **330.84577 K**. On this interval the modeled value decreases, and the two-point slope is **-160.14343 K per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

The browser expression is `1/(w/250+(1-w)/380)`. Model validity is limited to: **Hypothetical miscible binary amorphous blend Tg1=250 K, Tg2=380 K; Fox reciprocal rule only; no phase separation**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

χ can depend on composition and temperature, and a lattice model ignores specific interactions and many nonequilibrium solution histories. Do not infer medical solvent safety from a phase diagram.

### Exercises and self-assessment

**Exercise 2.1A — Physical mechanism.** Why can a small amount of polymer precipitate in a solvent mixture that dissolves each monomer separately? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.1B — Numerical cross-check.** Recalculate **353.7234 K** from the companion formula at **0.1428571 fraction** and compare with **330.84577 K** at **0.2857143 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 2.1C — Test design.** Propose a synthesis, processing or test matrix that addresses **a changed nucleation density or trapped solvent**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_2 -->

## Lesson 2.2: Glass transition and segmental mobility

### Scientific foundation

A glass transition is a kinetic range in which segmental relaxation times cross the observation timescale; it is not an equilibrium first-order melting event. Heating rate, physical aging and plasticizer concentration shift measured responses. DSC detects a heat-capacity step, DMA detects changes in storage and loss moduli, and dilatometry detects thermal expansion changes. An operational Tg must identify technique and criterion. Polymer chains do not all abruptly become mobile at a single unique molecular temperature.

**Governing relationship or decision rule:** The Fox estimate is 1/Tg≈w1/Tg1+(1−w1)/Tg2 with all transition temperatures in kelvin. Read every term in the equation as part of a declared specimen condition. In **glass transition and segmental mobility**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Use the ideal Fox reciprocal rule for a hypothetical miscible binary polymer blend with Tg1=250 K and Tg2=380 K and changing mass fraction. Compare the prediction with independently obtained DSC traces; if two separated transitions appear, discuss whether the sample is truly miscible. Identify the influence of residual solvent and heating rate.

A companion calculator called **Ideal Gibbs-Thomson lamellar melting point** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Crystal lamellar thickness = 13.57143 nm**, the declared formula returns **414.63158 K**; at **Crystal lamellar thickness = 18.85714 nm**, it returns **424.54545 K**. On this interval the modeled value increases, and the two-point slope is **1.8755981 K per nm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

The browser expression is `450*(1-2*0.08/(1.5e8*l*1e-9))`. Model validity is limited to: **Planar lamella equilibrium approximation Tm_inf=450 K, fold surface energy 0.08 J/m², enthalpy density 1.5e8 J/m³; no recrystallization**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

The Fox relation is empirical for compatible blends in a limited regime; it can fail with strong interactions or phase separation. It cannot diagnose miscibility by itself.

### Exercises and self-assessment

**Exercise 2.2A — Physical mechanism.** Why may DMA and DSC yield different numerical Tg for the same specimen without either instrument being broken? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.2B — Numerical cross-check.** Recalculate **414.63158 K** from the companion formula at **13.57143 nm** and compare with **424.54545 K** at **18.85714 nm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 2.2C — Test design.** Propose a synthesis, processing or test matrix that addresses **a changed nucleation density or trapped solvent**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_3 -->

## Lesson 2.3: Crystalline lamellae and spherulitic growth

### Scientific foundation

Many commercial polymers are semicrystalline, containing crystals, constrained amorphous material and more mobile amorphous regions. Chains fold into lamellae, which can aggregate into spherulitic textures. Lamellar thickness affects melting-point depression through the cost of crystal fold surfaces; the melting interval also reflects reorganization, imperfect crystals and distributions. The morphology is process-dependent and may change on reheating, which complicates interpreting DSC.

**Governing relationship or decision rule:** A planar-lamella estimate is Tm(l)=Tm∞[1−2σe/(Δhv l)], provided l is sufficient that the bracket remains positive. Read every term in the equation as part of a declared specimen condition. In **crystalline lamellae and spherulitic growth**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Compare thin and thick ideal lamellae with a Gibbs–Thomson expression. Use Tm∞=450 K, fold-surface energy=0.08 J/m² and fusion enthalpy density=1.5e8 J/m³. Determine why thin lamellae have lower equilibrium-type melting estimates. Use polarized microscopy and SAXS to discriminate spherulite size from lamellar long period.

A companion calculator called **Fox estimate of miscible blend Tg** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Mass fraction of component one = 0.4285714 fraction**, the declared formula returns **310.74766 K**; at **Mass fraction of component one = 0.5714286 fraction**, it returns **292.95154 K**. On this interval the modeled value decreases, and the two-point slope is **-124.57285 K per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Gibbs–Thomson assumes a particular lamellar geometry and interfacial energy; DSC peaks can be altered by recrystallization during heating. The slider is not a universal material grade calibration.

### Exercises and self-assessment

**Exercise 2.3A — Physical mechanism.** How could identical total crystalline fraction coexist with different melting curves? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.3B — Numerical cross-check.** Recalculate **310.74766 K** from the companion formula at **0.4285714 fraction** and compare with **292.95154 K** at **0.5714286 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 2.3C — Test design.** Propose a synthesis, processing or test matrix that addresses **a changed nucleation density or trapped solvent**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_2 -->

## Lesson 2.4: Crystallization kinetics and nucleation

### Scientific foundation

Crystallization rate depends on nucleation, chain transport and thermodynamic driving force. Slow cooling may permit lamellar thickening, while too rapid cooling can trap amorphous material; the fastest growth is often intermediate between the glass transition and equilibrium melting temperature. Avrami-type transformations describe an effective time dependence for some isothermal conditions but do not identify a unique crystal geometry without additional microscopy.

**Governing relationship or decision rule:** In a limited isothermal regime, X(t)=1−exp(−K t^n); K and n require measured fitting and constrained interpretation. Read every term in the equation as part of a declared specimen condition. In **crystallization kinetics and nucleation**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Design an isothermal DSC experiment with several hold temperatures, equal prior melt-erasure conditions, and repeat samples. Plot transformed fraction from integrated crystallization exotherm versus time and distinguish induction period from growth. Consider how talc nucleation changes density of spherulites without guaranteeing a larger final crystalline fraction.

A companion calculator called **Ideal Gibbs-Thomson lamellar melting point** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Crystal lamellar thickness = 24.14286 nm**, the declared formula returns **430.11834 K**; at **Crystal lamellar thickness = 29.42857 nm**, it returns **433.68932 K**. On this interval the modeled value increases, and the two-point slope is **0.67559028 K per nm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

An Avrami exponent can reflect overlapping nucleation and growth phenomena. Applying isothermal parameters to continuous cooling without correction is not sound.

### Exercises and self-assessment

**Exercise 2.4A — Physical mechanism.** Why might nucleating additives shorten a cycle without greatly changing the final enthalpy of melting? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.4B — Numerical cross-check.** Recalculate **430.11834 K** from the companion formula at **24.14286 nm** and compare with **433.68932 K** at **29.42857 nm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 2.4C — Test design.** Propose a synthesis, processing or test matrix that addresses **a changed nucleation density or trapped solvent**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_3 -->

## Lesson 2.5: Phase separation in blends and block copolymers

### Scientific foundation

Polymer blends can form dispersed droplets, co-continuous structures or a single mixed phase depending on interactions, viscosity ratio, composition and mixing history. Block copolymers link incompatible blocks and can microphase-separate into nanoscale domains because macroscopic separation would stretch the covalent connection. Interfacial compatibilizers can reduce droplet size yet change rheology and fracture modes. The same bulk composition can have radically different interface densities.

**Governing relationship or decision rule:** Morphology selection balances mixing free energy, interfacial energy, chain stretching and kinetic arrest; no single scalar parameter suffices. Read every term in the equation as part of a declared specimen condition. In **phase separation in blends and block copolymers**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Compare blend morphology after mild compounding and high-shear mixing, keeping composition fixed. Record domain size distributions rather than one micrograph. Design SAXS and microscopy controls for a block copolymer, including whether the measured periodicity persists after annealing. Explain why a cloudy sample cannot alone distinguish phase separation from crystallization.

A companion calculator called **Fox estimate of miscible blend Tg** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Mass fraction of component one = 0.7142857 fraction**, the declared formula returns **277.08333 K**; at **Mass fraction of component one = 0.8571429 fraction**, it returns **262.84585 K**. On this interval the modeled value decreases, and the two-point slope is **-99.662385 K per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Optical clarity also depends on size contrast and refractive indices. Processing history may lock in nonequilibrium domains that later coarsen; do not use one equilibrium χ to predict final processing morphology.

### Exercises and self-assessment

**Exercise 2.5A — Physical mechanism.** What measurement would identify a repeating nanoscale morphology in an apparently homogeneous block copolymer? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.5B — Numerical cross-check.** Recalculate **277.08333 K** from the companion formula at **0.7142857 fraction** and compare with **262.84585 K** at **0.8571429 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 2.5C — Test design.** Propose a synthesis, processing or test matrix that addresses **a changed nucleation density or trapped solvent**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_2 -->

## Integrated investigation: A transparent semicrystalline film

### The evidence problem

Two films have similar DSC crystalline fractions but different haze and shrinkage after heat treatment. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which polymerization route or formulated resin seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Separate crystal fraction, lamellar thickness, spherulitic texture, residual stress and surface roughness. Map cooling and annealing histories. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **polymer phase stability and morphology** and **thermodynamic tendency versus kinetically arrested structure** through the map. For polymer mixing, show composition conservation and do not infer processing kinetics from a static phase diagram. For a melt-state relation, distinguish relaxation time from shear-rate-dependent flow and actual process heating. For chemical function, distinguish molecular diffusion, partitioning, chain mobility and chemical degradation. Use the actual specimen time–temperature history instead of only a machine-temperature set point. For damage, compare local flaw driving force with rate- and environment-dependent measured fracture resistance.

### Validation plan, report, and counterfactual

Compare DSC first and second heating, SAXS/WAXS, optical scattering and thermomechanical shrinkage with repeated lots. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing polymer families, write down the constraints that matter for stiffness, creep, permeability, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** Equilibrium phase diagrams and ideal lamellar equations do not predict final film texture. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **polymer phase stability and morphology** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **thermodynamic tendency versus kinetically arrested structure** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **a changed nucleation density or trapped solvent** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_3 -->

