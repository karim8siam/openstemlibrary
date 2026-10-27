# Unit 2: Nucleation and early-stage events

**Guiding question:** How does an embryo become a persistent new phase?

## A physical orientation for this unit

Two alloys share nominal composition but differ in inclusion populations and initial grain boundary density. One exhibits an earlier detected transformation on cooling, tempting a careless conclusion about a 'better' alloy. A complete analysis separates the phase identities, the relevant conserved quantities, the imposed temperature–time path, and the measurable response. It is not enough to state that 'a new phase formed': the experiment must establish what is new, where it appeared, whether composition changed and whether the rate is constrained by diffusion, interface kinetics or transformation strain. This unit emphasizes **interface embryo**, using a **surface-to-volume competition** to test plausible mechanisms instead of treating a suggestive curve as proof.

Use the classical nucleation barrier as a sensitivity model, then construct waiting-time predictions for specified sample volumes, temperatures and detection thresholds. Before analyzing each lesson, prepare a ledger of observations, assumed boundary conditions and competing interpretations. Distinguish thermodynamic possibility from a nucleation pathway, a transformation rate and eventual property evolution. Include the thermal program and a practical measurement time resolution. Repeat a calculation at two values of a chosen input; the sensitivity often exposes whether the dominant uncertainty lies in material constants, microstructure or instrumentation.

## Vocabulary and conservation checkpoints

State the initial constituent, product state, composition basis and time origin. A phase fraction may be on a mass, volume, mole or diffraction-intensity basis, and those scales cannot be exchanged without a conversion model. State precisely whether each coefficient is a measured value, an empirical correlation, a thermodynamic state function or a synthetic teaching assumption. For this unit, pay particular attention to **site-density and coherency effects** and to possible confusion from **interfacial and elastic penalty**. A suitable cross-check would be **an inclusion-count comparison**.

## Lesson 2.1: Fluctuations, embryos and the critical radius

### Concept, boundary conditions and physical meaning

A homogeneous spherical nucleus gains negative bulk free energy proportional to radius cubed but pays positive interfacial energy proportional to radius squared. The free-energy curve therefore has a maximum at a critical radius. Subcritical embryos are statistically unstable against shrinkage in the classical capillarity picture, while supercritical ones can grow if matter transport is possible. Criticality is a statistical barrier, not a microscopic switch guaranteeing survival.

**Working relationship.** r*=2gamma/|Delta g_v| and Delta G*=16pi gamma³/(3|Delta g_v|²) for an unstrained spherical nucleus. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **fluctuations, embryos and the critical radius**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Assume gamma=0.12 J/m² and volumetric driving-force magnitude 2.0e8 J/m³. Compute classical critical radius 1.2 nm and discuss why atomic discreteness compromises the continuum model at this scale.

The nearby calculator **Classical critical nucleus radius** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Interfacial energy = 0.06857143 J/m²**, with all other model values held as published: the response is **0.68571429 nm**. At **Interfacial energy = 0.09714286 J/m²**, the response is **0.97142857 nm**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **10 nm per J/m²**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Spherical shapes, isotropic interfacial energy, constant composition and neglect of elastic strain rarely hold exactly for coherent precipitates.

### Examination, synthesis and a failure test

**Challenge question:** Would doubling the driving force halve the predicted critical radius and quarter the barrier? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 2.2: Homogeneous versus heterogeneous nucleation

### Concept, boundary conditions and physical meaning

Nucleation on grain boundaries, container walls and inclusions can reduce the geometric interfacial-energy barrier through wetting. For the classical spherical-cap treatment the barrier is multiplied by a contact-angle shape factor. A lower barrier need not mean a higher measured rate if attachment kinetics or site density differ. Sample cleanliness and surface condition often change apparent transformation start much more than a small nominal composition change.

**Working relationship.** f(theta)=(2+cos theta)(1-cos theta)^2/4 for an ideal cap on a planar substrate. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **homogeneous versus heterogeneous nucleation**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Take a notional wetting angle of 60 degrees, evaluate the spherical-cap factor (2+cos theta)(1-cos theta)^2/4, and estimate the heterogeneous barrier as 0.15625 times the homogeneous value.

The nearby calculator **Heterogeneous shape factor** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Contact angle = 57.14286 degrees**, with all other model values held as published: the response is **0.1330158 fraction**. At **Contact angle = 80.71429 degrees**, the response is **0.38003197 fraction**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.010479474 fraction per degrees**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Contact angle is geometry- and chemistry-sensitive and may not describe coherent solid-state nuclei; dislocation cores and ledges have different elastic terms.

### Examination, synthesis and a failure test

**Challenge question:** What specimen-preparation control would isolate the effect of inclusion density on incubation time? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 2.3: Nucleation rate and incubation

### Concept, boundary conditions and physical meaning

A rate model combines available site density, an atomic attempt frequency, attachment or diffusion mobility and Boltzmann weighting of a barrier. When temperature falls, driving force usually increases while atomic mobility decreases. Their competition can yield a maximum nucleation rate at intermediate undercooling, not necessarily at the lowest possible temperature. A recorded incubation time also includes instrumental detection thresholds and sample volume.

**Working relationship.** J≈J0 exp[-(Delta G*+Q_attach)/(k_B T)] is schematic, with J0 and barrier conventions specified. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **nucleation rate and incubation**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Compare two fictional rate expressions at 600 K and 700 K using a fixed activation energy and prefactor. Hold site count constant first, then ask how tenfold more inclusions changes an estimated waiting time in a fixed observation volume.

The nearby calculator **Classical critical nucleus radius** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Interfacial energy = 0.1257143 J/m²**, with all other model values held as published: the response is **1.2571429 nm**. At **Interfacial energy = 0.1542857 J/m²**, the response is **1.5428571 nm**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **10 nm per J/m²**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Arrhenius rate fits cannot identify nucleation mechanism by themselves because different prefactors, barrier shapes and site populations can reproduce similar slopes.

### Examination, synthesis and a failure test

**Challenge question:** How can measurements on different specimen volumes distinguish rare-event nucleation from a deterministic delay? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 2.4: Elastic coherency and shape selection

### Concept, boundary conditions and physical meaning

Coherent inclusions maintain approximate lattice registry with the matrix, storing elastic strain energy when lattice parameters differ. Shape selection then balances anisotropic interfacial cost against coherent-strain fields and local chemistry. The effective free-energy barrier can differ sharply from a spherical capillarity prediction; coherent precipitates often evolve toward semicoherency by introducing misfit dislocations as they grow.

**Working relationship.** e_strain≈(1/2)C epsilon_m² is a restricted scalar estimate, not full Eshelby inclusion theory. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **elastic coherency and shape selection**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Estimate an idealized volumetric elastic penalty 0.5 C epsilon_m^2 with C=100 GPa and misfit strain 0.015; compare about 11.25 MJ/m³ with a chemical driving force of 40 MJ/m³.

The nearby calculator **Heterogeneous shape factor** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Contact angle = 104.2857 degrees**, with all other model values held as published: the response is **0.68131183 fraction**. At **Contact angle = 127.8571 degrees**, the response is **0.90248846 fraction**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.009383251 fraction per degrees**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

A scalar modulus neglects elastic anisotropy, complex inclusion geometry and relaxation; measured mismatch strain is not always equal to coherent eigenstrain.

### Examination, synthesis and a failure test

**Challenge question:** Which diffraction measurement could reveal loss of coherent registry during particle growth? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 2.5: Pre-existing defects as nucleation sites

### Concept, boundary conditions and physical meaning

Dislocations, stacking faults, grain edges, free surfaces and dissimilar interfaces offer distinct local environments for nucleation. They can lower elastic penalties, provide fast diffusion paths or supply structural templates. More defects do not always improve a useful transformation: boundary precipitation may promote corrosion sensitivity, brittle paths or uncontrolled particle distributions. An experiment must separate changes in defect population from the stored energy caused by prior deformation.

**Working relationship.** Total rate depends on rate per site multiplied by the evolving population of eligible sites; a single Arrhenius slope is insufficient. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **pre-existing defects as nucleation sites**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Compare annealed and 10%-cold-worked hypothetical coupons subjected to equal solutionizing and aging schedules. Propose electron microscopy, grain-size measurement and DSC as complementary outputs.

The nearby calculator **Classical critical nucleus radius** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Interfacial energy = 0.1828571 J/m²**, with all other model values held as published: the response is **1.8285714 nm**. At **Interfacial energy = 0.2114286 J/m²**, the response is **2.1142857 nm**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **10 nm per J/m²**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Cold work may alter grain size, recrystallization kinetics and transport as well as nucleation; a faster transition is not proof of a single dislocation mechanism.

### Examination, synthesis and a failure test

**Challenge question:** How would you distinguish boundary nucleation from bulk nucleation in a time-resolved microscope series? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Integrated investigation: The cleanliness-versus-nucleation experiment

### Scientific problem and hypotheses

Two alloys share nominal composition but differ in inclusion populations and initial grain boundary density. One exhibits an earlier detected transformation on cooling, tempting a careless conclusion about a 'better' alloy. Define a primary observable and a rival mechanism. Hypothesis A should predict the observed conversion from the intended transformation; hypothesis B should explain a similar gross signal through a competing event. Name the observations needed to prefer one. A theory that can be made to fit every possible thermal or structural trace is not adequately discriminating. Describe a negative control, a second spatial sampling location, and an independent physical modality capable of challenging the initial phase identification.

### Mathematical framework

Use the classical nucleation barrier as a sensitivity model, then construct waiting-time predictions for specified sample volumes, temperatures and detection thresholds. Distinguish equilibrium state functions from kinetic rate parameters, then write the relevant conservation law. If a temperature is specified, record whether it is a furnace set point, actual specimen center, interface point or surface reading. If a phase fraction is inferred, identify the normalization and its endpoint calibration. Compare output at two values using the unit's interactive models; report the numerical change, dimension and range of acceptable inputs. Where a constitutive relation is approximate, propagate rather than conceal parameter uncertainty.

A rigorous explanation should include what would happen at slow cooling compared with quenching, and explain the conditions under which both trajectories would arrive at similar or different microstructures. Include whether substitutional diffusion, interstitial transport, cooperative lattice change, or interface movement supplies the controlling timescale. If the sample contains gradients, explain how a local transformation result might differ between edge and core. The comparison should be phrased as testable predicted signatures, not a guessed dramatic micrograph.

### Measurement and validation sequence

Count inclusions and boundaries independently, calibrate temperature response and repeat on at least two specimen volumes with identical heat paths. First capture the untreated material's structure and chemistry. Then document time-temperature history using two relevant temperature locations. Finally collect phase-sensitive and morphology-sensitive data at several interrupted processing states. Specify whether each observation is destructive, whether thermal cycling alters the sample, and how replicate variance will be measured. Blind a second analyst to the proposed mechanism and ask them to calculate a phase fraction or kinetic parameter from the primary traces. Record disagreements before revising interpretation.

### Claim boundaries and report requirements

Any inference about preferential nucleation must account for site density, elastic mismatch, chemistry changes and instrumental time resolution. A polished final report must include: starting microstructure; phase definitions; a reaction or chemical-potential argument; a checked worked estimate; a temperature–time diagram annotated with sensor location; synthetic model graphs clearly marked as simulated; a second-method validation plan; and a concise list of conditions that would make the engineering conclusion unsafe or invalid. Numerical compatibility is a necessary implementation check but is not sufficient evidence of mechanism or service suitability. Explain precisely what further data would turn the exercise into a candidate processing procedure.

### Interact with this unit's models

<!-- MODEL_2 -->

<!-- MODEL_3 -->

