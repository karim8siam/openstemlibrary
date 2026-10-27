# Unit 7: Polymorphic, ordering and glass transitions

**Guiding question:** What transformations occur beyond conventional alloy precipitation?

## A physical orientation for this unit

A manufacturer wants a phase-transforming component that survives repeated thermal cycles but treats all hysteresis and dimensional shifts as equivalent. A complete analysis separates the phase identities, the relevant conserved quantities, the imposed temperature–time path, and the measurable response. It is not enough to state that 'a new phase formed': the experiment must establish what is new, where it appeared, whether composition changed and whether the rate is constrained by diffusion, interface kinetics or transformation strain. This unit emphasizes **structural and kinetic transition**, using a **symmetry, ordering or amorphous relaxation** to test plausible mechanisms instead of treating a suggestive curve as proof.

Separate order-disorder, martensitic, glass and ceramic transformations; build state diagrams and compare latent heat, mechanical recovery and permanent damage. Before analyzing each lesson, prepare a ledger of observations, assumed boundary conditions and competing interpretations. Distinguish thermodynamic possibility from a nucleation pathway, a transformation rate and eventual property evolution. Include the thermal program and a practical measurement time resolution. Repeat a calculation at two values of a chosen input; the sensitivity often exposes whether the dominant uncertainty lies in material constants, microstructure or instrumentation.

## Vocabulary and conservation checkpoints

State the initial constituent, product state, composition basis and time origin. A phase fraction may be on a mass, volume, mole or diffraction-intensity basis, and those scales cannot be exchanged without a conversion model. State precisely whether each coefficient is a measured value, an empirical correlation, a thermodynamic state function or a synthetic teaching assumption. For this unit, pay particular attention to **driving-force and path dependence** and to possible confusion from **hysteresis and transformation strain**. A suitable cross-check would be **coupled calorimetry and diffraction**.

## Lesson 7.1: Order–disorder transitions in crystals

### Concept, boundary conditions and physical meaning

Ordering changes occupation probabilities of crystallographic sublattices and can produce superlattice diffraction peaks without large changes to the underlying lattice type. Long-range order parameters quantify site preference relative to complete randomness. Some ordering transitions are continuous whereas others are first order, depending on symmetry and interaction energies. Short-range order may survive above a long-range transition and influence properties.

**Working relationship.** S≈sqrt(I_super/I_reference) under identical normalization and intensity proportional to S². Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **order–disorder transitions in crystals**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

At fixed nominal alloy composition, compare a normalized superlattice intensity ratio 0.16 to a fully ordered reference ratio 1.00; in the simplest matched-geometry model infer order parameter about 0.4.

The nearby calculator **Order parameter from intensity** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Normalized superlattice intensity = 0.1428571 fraction**, with all other model values held as published: the response is **0.37796447 dimensionless**. At **Normalized superlattice intensity = 0.2857143 fraction**, the response is **0.53452248 dimensionless**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **1.0959061 dimensionless per fraction**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Intensity also depends on structure factor, texture, extinction, absorption and instrument effects; sqrt intensity ratio is only an ideal comparison.

### Examination, synthesis and a failure test

**Challenge question:** What diffraction control would distinguish a loss of ordering from a change in sample texture? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 7.2: Allotropy and reconstructive transitions

### Concept, boundary conditions and physical meaning

A chemical element can adopt different structures at different temperatures or pressures; pure iron provides a familiar example. Reconstructive transitions involve bond rearrangement and atom movement, sometimes with slow interfaces and nucleation. A structural change can coexist with thermal expansion and magnetic changes, making single-signal interpretation difficult. Pressure can shift stability through the volume term in Gibbs energy.

**Working relationship.** At fixed T, dG=V dp for a one-component stable phase; phase differences use corresponding Delta V. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **allotropy and reconstructive transitions**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Compare hypothetical molar volumes of two polymorphs and calculate a small approximate pressure-induced Gibbs difference Delta G≈Delta V Delta p; state why temperature remains another control variable.

The nearby calculator **Free isotropic linear expansion** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Transformation volume change = 2.285714 percent**, with all other model values held as published: the response is **0.75617238 percent**. At **Transformation volume change = 3.428571 percent**, the response is **1.1300392 percent**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.32713343 percent per percent**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

A lattice transition seen during heating may shift with heating rate; observed onset is not an exact equilibrium boundary without kinetic analysis.

### Examination, synthesis and a failure test

**Challenge question:** What simultaneous calorimetry and diffraction signature would strengthen a polymorph assignment? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 7.3: Martensitic shape memory and hysteresis

### Concept, boundary conditions and physical meaning

Some thermoelastic martensitic transformations support reversible movement of crystallographic variants and deformation recoverable on heating. Shape-memory and superelastic behavior depend on twinning, detwinning, stress-induced transformation and stable transformation temperatures. Hysteresis reflects dissipative processes and compatibility constraints; not all martensitic materials are useful shape-memory alloys. Cycle life, training, oxidation and environmental effects matter in practice.

**Working relationship.** Transformation temperatures are protocol-dependent operational markers, not a complete constitutive description. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **martensitic shape memory and hysteresis**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

For a fictitious actuator with martensite-start at 35 degrees C and austenite-finish at 70 degrees C, propose a bounded temperature cycle and explain why two transition endpoints do not define the entire force–displacement response.

The nearby calculator **Order parameter from intensity** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Normalized superlattice intensity = 0.4285714 fraction**, with all other model values held as published: the response is **0.65465367 dimensionless**. At **Normalized superlattice intensity = 0.5714286 fraction**, the response is **0.75592895 dimensionless**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.70892693 dimensionless per fraction**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Transformation strain depends strongly on texture, loading direction and training; catalog strain values cannot be used without stress and cycling conditions.

### Examination, synthesis and a failure test

**Challenge question:** How can a DSC thermal signal be compared with a mechanical recovery curve during repeated actuation? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 7.4: Glass transition, crystallization and devitrification

### Concept, boundary conditions and physical meaning

The glass transition of an amorphous solid reflects kinetic arrest and a sharp change in structural relaxation time, not generally the same first-order mechanism as melting. A fictive temperature summarizes aspects of the frozen-in thermal history. When an amorphous material crystallizes on heating, exothermic signals and diffraction peaks can emerge, but glass transition alone need not generate crystalline order. Scan rate alters observed transition temperatures.

**Working relationship.** Tg is operational and time-scale dependent; a heat-capacity step is not a direct equilibrium two-phase tie line. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **glass transition, crystallization and devitrification**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Compare hypothetical DSC heat-capacity steps from two scan rates and propose XRD before and after a separate crystallization exotherm. Ask which measurement establishes actual crystalline phase formation.

The nearby calculator **Free isotropic linear expansion** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Transformation volume change = 4.571429 percent**, with all other model values held as published: the response is **1.5011619 percent**. At **Transformation volume change = 5.714286 percent**, the response is **1.8695904 percent**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.32237494 percent per percent**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Peak temperature shifts with scan rate and thermal lag; heating curves alone are insufficient to infer equilibrium latent heat for a glass transition.

### Examination, synthesis and a failure test

**Challenge question:** What distinction would you make between Tg, crystallization onset Tx and melting temperature Tm? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 7.5: Ceramic polymorphs and reconstructive cracking

### Concept, boundary conditions and physical meaning

Polymorphic transitions in ceramics can alter molar volume, elastic properties and thermal expansion; constrained microstructures may crack during heating or cooling. Zirconia-based toughening illustrates how stress-induced transformation can be useful when composition and microstructure stabilize appropriate phases. Other reconstructive changes produce damaging volume changes if thermal cycles are poorly controlled. Porosity and grain size complicate bulk observations.

**Working relationship.** For isotropic free expansion, epsilon_linear=(1+Delta V/V)^(1/3)-1. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **ceramic polymorphs and reconstructive cracking**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

For a fictional ceramic with 3% transformation-associated volumetric expansion, calculate isotropic free linear strain about (1.03)^(1/3)-1 and discuss why constrained strain differs.

The nearby calculator **Order parameter from intensity** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Normalized superlattice intensity = 0.7142857 fraction**, with all other model values held as published: the response is **0.84515425 dimensionless**. At **Normalized superlattice intensity = 0.8571429 fraction**, the response is **0.9258201 dimensionless**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.56466092 dimensionless per fraction**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Do not substitute this illustrative expansion into the real tetragonal–monoclinic zirconia system without appropriate measured data.

### Examination, synthesis and a failure test

**Challenge question:** Which dilatometry-plus-diffraction experiment could separate microcrack dilation from an actual phase-volume change? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Integrated investigation: A shape-memory actuator and a ceramic analogue

### Scientific problem and hypotheses

A manufacturer wants a phase-transforming component that survives repeated thermal cycles but treats all hysteresis and dimensional shifts as equivalent. Define a primary observable and a rival mechanism. Hypothesis A should predict the observed conversion from the intended transformation; hypothesis B should explain a similar gross signal through a competing event. Name the observations needed to prefer one. A theory that can be made to fit every possible thermal or structural trace is not adequately discriminating. Describe a negative control, a second spatial sampling location, and an independent physical modality capable of challenging the initial phase identification.

### Mathematical framework

Separate order-disorder, martensitic, glass and ceramic transformations; build state diagrams and compare latent heat, mechanical recovery and permanent damage. Distinguish equilibrium state functions from kinetic rate parameters, then write the relevant conservation law. If a temperature is specified, record whether it is a furnace set point, actual specimen center, interface point or surface reading. If a phase fraction is inferred, identify the normalization and its endpoint calibration. Compare output at two values using the unit's interactive models; report the numerical change, dimension and range of acceptable inputs. Where a constitutive relation is approximate, propagate rather than conceal parameter uncertainty.

A rigorous explanation should include what would happen at slow cooling compared with quenching, and explain the conditions under which both trajectories would arrive at similar or different microstructures. Include whether substitutional diffusion, interstitial transport, cooperative lattice change, or interface movement supplies the controlling timescale. If the sample contains gradients, explain how a local transformation result might differ between edge and core. The comparison should be phrased as testable predicted signatures, not a guessed dramatic micrograph.

### Measurement and validation sequence

Use synchronized DSC, diffraction and length tracking across multiple cycles while recording stress and atmosphere. First capture the untreated material's structure and chemistry. Then document time-temperature history using two relevant temperature locations. Finally collect phase-sensitive and morphology-sensitive data at several interrupted processing states. Specify whether each observation is destructive, whether thermal cycling alters the sample, and how replicate variance will be measured. Blind a second analyst to the proposed mechanism and ask them to calculate a phase fraction or kinetic parameter from the primary traces. Record disagreements before revising interpretation.

### Claim boundaries and report requirements

Shared phenomenology such as a loop or heat peak does not establish shared transformation mechanism or cycling reliability. A polished final report must include: starting microstructure; phase definitions; a reaction or chemical-potential argument; a checked worked estimate; a temperature–time diagram annotated with sensor location; synthetic model graphs clearly marked as simulated; a second-method validation plan; and a concise list of conditions that would make the engineering conclusion unsafe or invalid. Numerical compatibility is a necessary implementation check but is not sufficient evidence of mechanism or service suitability. Explain precisely what further data would turn the exercise into a candidate processing procedure.

### Interact with this unit's models

<!-- MODEL_12 -->

<!-- MODEL_13 -->

