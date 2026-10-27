# Unit 5: Thermal behavior, refractories and protective coatings

**Guiding question:** How do heat flow, expansion mismatch and high-temperature chemistry set service limits?

## Why this unit matters to ceramic engineering

A promising ceramic coating lowers the estimated steady heat flux but develops spallation after repeated service cycles. This is a question about **thermal gradients and material interfaces** and the distinction between **insulation benefit versus spallation risk**. A defensible answer identifies feedstock composition, chemistry, processing path and microstructure before comparing measured properties. It also names the potentially controlling failure mode: a recipe that optimizes density, dielectric response or simple bend strength can still worsen thermal cycling, porosity topology, lifetime or chemical compatibility. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Thermal design couples conduction, contact resistance, expansion incompatibility and chemical reaction at hot interfaces. A material that reduces average heat flow may still fail by cycling-induced damage.

Map real part geometry, boundary conditions, atmosphere and the position of tensile stress peaks. Report where a simplified slab model is invalid because temperature fields are transient or three-dimensional.

## Measurement and conservation checkpoints

Write down the starting composition, defect-sensitive atmosphere and powder or glass history; define whether reported fractions are by area, mass, moles or volume; and record the process history that could alter **thermal cycling, atmosphere and interface chemistry**. For any local observation, describe why its sampling plan represents the part. Treat **unmeasured contact and radiative losses** as an explicit rival explanation and plan **thermal mapping and post-cycle microscopy** as an independent check.

## Lesson 5.1: Phonon transport and thermal diffusivity

### Scientific foundation

Heat conduction in most electrically insulating crystals is mainly carried by phonons. Defects, boundaries, isotopes, porosity and high-temperature phonon scattering limit their mean free paths. Microstructural refinement can improve strength while reducing conductivity, so optimizing a ceramic requires a service-relevant thermal gradient rather than one room-temperature property. Thermal diffusivity alpha equals k/(rho c_p) only with consistent bulk properties and a well-defined measurement temperature.

**Governing relationship or decision rule:** For steady one-dimensional conduction R_th=L/(k A); for thermal diffusivity alpha=k/(rho c_p). Read every term in the equation as part of a declared specimen condition. In **phonon transport and thermal diffusivity**, a valid calculation requires the state of the ceramic, unit system and physical or geometrical meaning of each quantity. A nominally identical oxide composition can conceal different dopant distributions, porosity, grain-boundary glass and processing damage. Equal bulk density does not guarantee equivalent fracture, transport or thermal stability. Interpret measurements only after identifying which feature of the state they can support.

### Worked ceramic investigation

Use the slab thermal-resistance slider to compare two hypothetical thermal conductivities at fixed geometry; then calculate diffusion time scaling with part thickness using an independently assumed diffusivity. Design a laser-flash measurement plus specific-heat and bulk-density measurements to reconstruct k and discuss radiation corrections at elevated temperature.

A companion calculator called **Ideal slab thermal resistance** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Thermal conductivity = 3.285714 W/(m K)**, the declared formula returns **0.60869565 K/W**; at **Thermal conductivity = 6.071429 W/(m K)**, it returns **0.32941176 K/W**. On this interval the modeled value decreases, and the two-point slope is **-0.10025575 K/W per W/(m K)**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real ceramic formulation.

The browser expression is `0.01/(k*0.005)`. Model validity is limited to: **Single layer thickness=10 mm and area=0.005 m², 1D steady conduction with k constant, no contacts or radiation**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

A steady one-dimensional heat-resistance formula does not predict transient thermal gradients. A porous ceramic may conduct through solid, gas and radiation paths whose relative importance changes strongly with temperature.

### Exercises and self-assessment

**Exercise 5.1A — Physical mechanism.** How can two ceramics have similar density but opposite trends of thermal conductivity with firing temperature? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.1B — Numerical cross-check.** Recalculate **0.60869565 K/W** from the companion formula at **3.285714 W/(m K)** and compare with **0.32941176 K/W** at **6.071429 W/(m K)**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real ceramic specimen.

**Exercise 5.1C — Test design.** Propose a preparation or test matrix that addresses **unmeasured contact and radiative losses**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Lesson 5.2: Thermal expansion and constrained thermal stress

### Scientific foundation

Ceramics often have anisotropic thermal expansion and phase-dependent coefficients. An unconstrained body can expand without generating the simple uniform stress of a fully restrained model, but geometric mismatch, gradients and joining to metals can create local tension. A thermal shock problem must consider heat-transfer coefficient, surface cracks, toughness, strength, elastic modulus and time scale. Lower average expansion does not automatically confer safe rapid quenching.

**Governing relationship or decision rule:** A simple ideal biaxial constraint estimate gives sigma=E alpha_T DeltaT/(1-nu); real thermal-shock design needs a spatial heat-transfer solution. Read every term in the equation as part of a declared specimen condition. In **thermal expansion and constrained thermal stress**, a valid calculation requires the state of the ceramic, unit system and physical or geometrical meaning of each quantity. A nominally identical oxide composition can conceal different dopant distributions, porosity, grain-boundary glass and processing damage. Equal bulk density does not guarantee equivalent fracture, transport or thermal stability. Interpret measurements only after identifying which feature of the state they can support.

### Worked ceramic investigation

With a declared elastic modulus, expansion coefficient and Poisson ratio, compute an upper-bound fully constrained equibiaxial thermal stress for a range of temperature changes. Compare predicted nominal stresses with an independent fracture threshold from a separately measured flaw size; discuss why the sign and spatial distribution of actual stress depend on heating versus cooling geometry.

A companion calculator called **Fully constrained thermal stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Absolute temperature difference = 128.5714 K**, the declared formula returns **300 MPa**; at **Absolute temperature difference = 182.8571 K**, it returns **426.66667 MPa**. On this interval the modeled value increases, and the two-point slope is **2.3333333 MPa per K**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real ceramic formulation.

The browser expression is `250e9*7e-6*dT/(1-0.25)/1e6`. Model validity is limited to: **Uniform equibiaxial elastic constraint; E=250 GPa, alpha=7e-6 /K, nu=0.25; stress magnitude only; ignores temperature fields and fracture**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

The model assumes constant elastic coefficients and perfect constraint. It ignores stress relaxation, cracking, nonlinear phase transformations and transient surface-to-core temperature differences.

### Exercises and self-assessment

**Exercise 5.2A — Physical mechanism.** Why does a thin plate sometimes survive a thermal jump that cracks a thicker part of the same material? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.2B — Numerical cross-check.** Recalculate **300 MPa** from the companion formula at **128.5714 K** and compare with **426.66667 MPa** at **182.8571 K**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real ceramic specimen.

**Exercise 5.2C — Test design.** Propose a preparation or test matrix that addresses **unmeasured contact and radiative losses**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_9 -->

## Lesson 5.3: Refractory corrosion, slag attack and creep

### Scientific foundation

Refractory linings must survive combined thermal load, mechanical contact, atmospheric chemistry and reactive melts. Acidic and basic slag descriptors provide useful qualitative guidance but do not replace phase equilibria, wetting and kinetic corrosion tests. Penetrating liquid can create spallation by reaction products or temperature-dependent expansion mismatch. At high temperature, creep and grain-boundary sliding also change dimensions under sustained stress.

**Governing relationship or decision rule:** Total degradation reflects coupled chemical potential gradients, transport and mechanical damage; a single material hardness or porosity value is insufficient. Read every term in the equation as part of a declared specimen condition. In **refractory corrosion, slag attack and creep**, a valid calculation requires the state of the ceramic, unit system and physical or geometrical meaning of each quantity. A nominally identical oxide composition can conceal different dopant distributions, porosity, grain-boundary glass and processing damage. Equal bulk density does not guarantee equivalent fracture, transport or thermal stability. Interpret measurements only after identifying which feature of the state they can support.

### Worked ceramic investigation

Construct a compatibility study of three candidate refractory compositions using synthetic slag chemistries and temperature holds. Measure infiltration depth, reaction-layer thickness and hot modulus of rupture after exposure. Simulate heat-flow sensitivity only for a representative layer whose k and thickness have been declared; never turn the ideal slab resistance into a furnace lifetime warranty.

A companion calculator called **Ideal slab thermal resistance** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Thermal conductivity = 8.857143 W/(m K)**, the declared formula returns **0.22580645 K/W**; at **Thermal conductivity = 11.64286 W/(m K)**, it returns **0.17177914 K/W**. On this interval the modeled value decreases, and the two-point slope is **-0.019394419 K/W per W/(m K)**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real ceramic formulation.

### Evidence, uncertainty, and a competing mechanism

Real slag composition varies during production and localized oxygen potential changes valence states. Laboratory static crucible tests may not capture flowing erosion and cyclic contact.

### Exercises and self-assessment

**Exercise 5.3A — Physical mechanism.** Why can a refractory with good room-temperature crushing strength fail quickly in a flowing slag service? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.3B — Numerical cross-check.** Recalculate **0.22580645 K/W** from the companion formula at **8.857143 W/(m K)** and compare with **0.17177914 K/W** at **11.64286 W/(m K)**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real ceramic specimen.

**Exercise 5.3C — Test design.** Propose a preparation or test matrix that addresses **unmeasured contact and radiative losses**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Lesson 5.4: Thermal barrier coatings and interface adhesion

### Scientific foundation

Thermal barrier systems use a low-conductivity ceramic layer over bond coats and an alloy substrate. Their reliability depends not only on ceramic insulation but also on thermally grown oxide growth, interfacial roughness, residual stress, sintering and foreign-particle damage. Coating processes generate very different architectures, including lamellar splats or columnar pores; one bulk thermal conductivity number does not capture an entire multilayer stack.

**Governing relationship or decision rule:** For ideal serial layers, R_total=sum_j L_j/(k_j A), subject to contact and temperature-dependence corrections. Read every term in the equation as part of a declared specimen condition. In **thermal barrier coatings and interface adhesion**, a valid calculation requires the state of the ceramic, unit system and physical or geometrical meaning of each quantity. A nominally identical oxide composition can conceal different dopant distributions, porosity, grain-boundary glass and processing damage. Equal bulk density does not guarantee equivalent fracture, transport or thermal stability. Interpret measurements only after identifying which feature of the state they can support.

### Worked ceramic investigation

Estimate ideal one-dimensional resistance for a series of hypothetical ceramic coat conductivities at fixed thickness and exposed area. Then augment the network with bond-coat and substrate resistances symbolically and list thermal contact resistances to be measured. Propose cyclic thermal exposure and adhesion tests rather than selecting a coating solely from room-temperature k.

A companion calculator called **Fully constrained thermal stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Absolute temperature difference = 237.1429 K**, the declared formula returns **553.33333 MPa**; at **Absolute temperature difference = 291.4286 K**, it returns **680 MPa**. On this interval the modeled value increases, and the two-point slope is **2.3333333 MPa per K**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real ceramic formulation.

### Evidence, uncertainty, and a competing mechanism

The 1D estimate ignores radiation, through-thickness gradients in porosity and moving oxide interfaces. Residual stress can induce delamination even as the ideal thermal resistance looks attractive.

### Exercises and self-assessment

**Exercise 5.4A — Physical mechanism.** What evidence distinguishes an interface-driven spallation event from ceramic cohesive cracking? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.4B — Numerical cross-check.** Recalculate **553.33333 MPa** from the companion formula at **237.1429 K** and compare with **680 MPa** at **291.4286 K**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real ceramic specimen.

**Exercise 5.4C — Test design.** Propose a preparation or test matrix that addresses **unmeasured contact and radiative losses**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_9 -->

## Lesson 5.5: Oxidation, water vapor and environmental durability

### Scientific foundation

Silicon-containing nonoxide ceramics can form protective silica-rich scales in some environments, yet high-temperature water vapor can volatilize certain silica-containing surface species and undermine recession resistance. Oxide ceramics can also degrade by hydration, phase transformation, molten-salt fluxing or oxygen chemical potential changes. Specimens should be tested in representative gas compositions, not only in laboratory air, and surface recession should be separated from bulk creep and thermal cycling.

**Governing relationship or decision rule:** Species mass conservation and measured reaction-product fluxes, not just specimen net weight, are required for a reliable oxidation/recession rate. Read every term in the equation as part of a declared specimen condition. In **oxidation, water vapor and environmental durability**, a valid calculation requires the state of the ceramic, unit system and physical or geometrical meaning of each quantity. A nominally identical oxide composition can conceal different dopant distributions, porosity, grain-boundary glass and processing damage. Equal bulk density does not guarantee equivalent fracture, transport or thermal stability. Interpret measurements only after identifying which feature of the state they can support.

### Worked ceramic investigation

Plan paired tests in dry air and a water-vapor-rich gas at the same nominal temperature. Record mass gain, mass loss, scale thickness and dimensional recession separately because vaporization and oxidation can partially cancel in a net weight trace. Use thermal stress estimates to evaluate whether the resulting reacted layer may spall during cooldown.

A companion calculator called **Ideal slab thermal resistance** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Thermal conductivity = 14.42857 W/(m K)**, the declared formula returns **0.13861386 K/W**; at **Thermal conductivity = 17.21429 W/(m K)**, it returns **0.11618257 K/W**. On this interval the modeled value decreases, and the two-point slope is **-0.0080522575 K/W per W/(m K)**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real ceramic formulation.

### Evidence, uncertainty, and a competing mechanism

Net mass change is not a unique reaction rate; volatile products can disappear while oxygen incorporation adds mass. Gas velocity and pressure can change degradation pathways.

### Exercises and self-assessment

**Exercise 5.5A — Physical mechanism.** How could a specimen have nearly zero net mass change while undergoing significant corrosive recession? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.5B — Numerical cross-check.** Recalculate **0.13861386 K/W** from the companion formula at **14.42857 W/(m K)** and compare with **0.11618257 K/W** at **17.21429 W/(m K)**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real ceramic specimen.

**Exercise 5.5C — Test design.** Propose a preparation or test matrix that addresses **unmeasured contact and radiative losses**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Integrated investigation: Design a thermally cycled ceramic liner

### The evidence problem

A promising ceramic coating lowers the estimated steady heat flux but develops spallation after repeated service cycles. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which powder process or ceramic composition seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Separate heat-transfer resistance from thermally grown oxide stress, chemical attack and geometric constraint. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **thermal gradients and material interfaces** and **insulation benefit versus spallation risk** through the map. For phase equilibria, show composition conservation and do not infer processing kinetics from a phase diagram. For a densification relation, separate pore disappearance from neck growth and grain coarsening. For electrical function, distinguish ion migration, electronic leakage, electrode polarization and nonlinear ferroelectric switching. Use the actual specimen time–temperature history instead of only a furnace setting. For damage, compare local flaw driving force with the appropriate fracture resistance.

### Validation plan, report, and counterfactual

Map temperature and layer interfaces before and after thermal cycling and independently assess residual stress. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing ceramic families, write down the constraints that matter for weight, stiffness, temperature, oxidation and availability rather than reporting only one maximum strength metric.

**Known limits:** One-dimensional heat conduction is not lifetime prediction. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **thermal gradients and material interfaces** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **insulation benefit versus spallation risk** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **unmeasured contact and radiative losses** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_9 -->

