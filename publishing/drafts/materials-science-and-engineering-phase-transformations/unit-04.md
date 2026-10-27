# Unit 4: Solidification and casting transformations

**Guiding question:** How do liquids form microstructures as they freeze?

## A physical orientation for this unit

An imagined binary melt freezes in a thick mould and later shows unexpected low-melting interdendritic regions. A reviewer blames insufficient stirring without measuring either composition or thermal history. A complete analysis separates the phase identities, the relevant conserved quantities, the imposed temperature–time path, and the measurable response. It is not enough to state that 'a new phase formed': the experiment must establish what is new, where it appeared, whether composition changed and whether the rate is constrained by diffusion, interface kinetics or transformation strain. This unit emphasizes **freezing morphology**, using a **liquid-solid solute balance** to test plausible mechanisms instead of treating a suggestive curve as proof.

Compute Scheil-like terminal-liquid enrichment, compare with a complete-equilibrium bound and use partitioning to predict where microscale chemistry should differ. Before analyzing each lesson, prepare a ledger of observations, assumed boundary conditions and competing interpretations. Distinguish thermodynamic possibility from a nucleation pathway, a transformation rate and eventual property evolution. Include the thermal program and a practical measurement time resolution. Repeat a calculation at two values of a chosen input; the sensitivity often exposes whether the dominant uncertainty lies in material constants, microstructure or instrumentation.

## Vocabulary and conservation checkpoints

State the initial constituent, product state, composition basis and time origin. A phase fraction may be on a mass, volume, mole or diffraction-intensity basis, and those scales cannot be exchanged without a conversion model. State precisely whether each coefficient is a measured value, an empirical correlation, a thermodynamic state function or a synthetic teaching assumption. For this unit, pay particular attention to **thermal and solutal undercooling** and to possible confusion from **segregation and thermal gradients**. A suitable cross-check would be **a center-to-surface casting section**.

## Lesson 4.1: Liquid-to-solid nucleation and undercooling

### Concept, boundary conditions and physical meaning

Freezing requires a solid-liquid free-energy advantage and formation of an interface. Heterogeneous sites typically govern ordinary castings, while strong undercooling may support finer grains if many nuclei form before significant growth. Thermal undercooling, curvature undercooling and solutal undercooling have different origins. The temperature measured at a thermocouple is not necessarily the instantaneous temperature at a growing dendrite tip.

**Working relationship.** Delta T=T_liquidus-T_actual with identical temperature scale increments in K or °C. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **liquid-to-solid nucleation and undercooling**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

For a fictional melt with liquidus 800 degrees C and first nucleation at 782 degrees C, report 18 K thermal undercooling. Contrast this observation with the independent growth velocity needed to predict grain size.

The nearby calculator **Scheil residual-liquid composition** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Fraction solidified = 0.1285714 fraction**, with all other model values held as published: the response is **0.05356167 fraction**. At **Fraction solidified = 0.2571429 fraction**, the response is **0.058011935 fraction**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.034613176 fraction per fraction**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Undercooling is not itself proof of homogeneous nucleation or a single solidification morphology; contamination and mould surfaces matter.

### Examination, synthesis and a failure test

**Challenge question:** Why can a cleaner melt sometimes form larger grains despite reaching a larger undercooling? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 4.2: Dendritic growth and constitutional undercooling

### Concept, boundary conditions and physical meaning

An advancing solid-liquid boundary rejects or absorbs solute depending on the equilibrium partition coefficient. Solute-enriched liquid ahead of an interface may have a locally depressed liquidus, allowing the imposed thermal profile to support cellular or dendritic instability. Primary arm spacing depends on growth rate, thermal gradient, alloy composition and selection history. It is not determined by the equilibrium phase diagram alone.

**Working relationship.** k=c_s/c_l at the local interface under an explicit local-equilibrium approximation. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **dendritic growth and constitutional undercooling**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Take a fictional liquid solute fraction 0.08 and an interfacial solid fraction 0.032; calculate partition coefficient k=0.4. Describe how enrichment accumulates ahead of the freezing front.

The nearby calculator **Cooling-window residence time** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Cooling rate = 23.57143 K/s**, with all other model values held as published: the response is **12.727273 s**. At **Cooling rate = 34.85714 K/s**, the response is **8.6065574 s**; within this idealization it decreases. The finite-difference sensitivity for these two settings is approximately **-0.36512668 s per K/s**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

A steady planar-interface criterion is not interchangeable with transient multicomponent casting; flow and convection often reshape the solute boundary layer.

### Examination, synthesis and a failure test

**Challenge question:** What experiment could separate convective solute redistribution from molecular diffusion ahead of a dendrite? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 4.3: Scheil solidification and segregation

### Concept, boundary conditions and physical meaning

The Scheil approximation assumes perfect mixing in the liquid, negligible solid-state diffusion and interface partitioning by an equilibrium k. As solid forms the remaining liquid can become increasingly enriched in rejected solute. The model represents an extreme segregation limit rather than a typical alloy exactly; finite solid diffusion and back-diffusion soften the result. Near terminal liquid fractions, numerical extrapolation can become unphysical.

**Working relationship.** c_l=c0(1-f_s)^(k-1) for constant k, mixed liquid and no solid back-diffusion. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **scheil solidification and segregation**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Evaluate c_l=c0(1-f_s)^(k-1) for c0=0.05, k=0.5 and f_s=0.64, obtaining about 0.0833; note that this is a fraction, not a mass-percent value until converted.

The nearby calculator **Scheil residual-liquid composition** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Fraction solidified = 0.3857143 fraction**, with all other model values held as published: the response is **0.063794729 fraction**. At **Fraction solidified = 0.5142857 fraction**, the response is **0.071743005 fraction**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.061819928 fraction per fraction**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

If the partition coefficient varies with temperature or a new compound forms, continuing a single-branch Scheil formula can misrepresent terminal freezing.

### Examination, synthesis and a failure test

**Challenge question:** How would a measured interdendritic composition profile distinguish equilibrium solidification from Scheil-like behavior? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 4.4: Eutectic colonies and coupled growth

### Concept, boundary conditions and physical meaning

At eutectic conditions liquid can transform to two solids simultaneously. Lamellar or rod-like morphologies arise from the need to remove solute over short diffusion distances while creating interphase boundary area. Small spacing shortens diffusion paths but adds more interface energy. Growth spacing depends on velocity and kinetic selection; a eutectic composition is not sufficient to predict a universal interlamellar spacing.

**Working relationship.** lambda≈L/N from a transverse line measurement, only under consistent geometrical sampling. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **eutectic colonies and coupled growth**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Take a fictitious eutectic region with 15 micrometers of lamellar width containing 30 repeated alpha-plus-beta periods; compute approximate spacing 0.5 micrometers and specify the line-selection bias of this measurement.

The nearby calculator **Cooling-window residence time** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Cooling rate = 46.14286 K/s**, with all other model values held as published: the response is **6.501548 s**. At **Cooling rate = 57.42857 K/s**, the response is **5.2238806 s**; within this idealization it decreases. The finite-difference sensitivity for these two settings is approximately **-0.11321103 s per K/s**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

A polished section intersects three-dimensional colonies at arbitrary angles; observed spacing can differ from true spacing and cannot establish growth velocity without history.

### Examination, synthesis and a failure test

**Challenge question:** What orientation correction or serial-section method would reduce spacing bias? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 4.5: Recalescence, shrinkage and defects

### Concept, boundary conditions and physical meaning

During freezing released latent heat can temporarily reduce a local cooling rate or even raise measured temperature, called recalescence. Liquid-to-solid density changes, inadequate feeding and dissolved-gas evolution can create porosity. Porosity is a defect state rather than a thermodynamic phase in the alloy phase diagram. Cooling curves are therefore valuable only when combined with sectioning and heat-flow information.

**Working relationship.** A heat balance includes m c_p dT/dt and latent heat mL df_s/dt together with external heat flux. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **recalescence, shrinkage and defects**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

A hypothetical temperature trace drops 15 K below liquidus and then rises 6 K as solid develops; distinguish the observed 6 K recalescence from the total latent heat and estimate none of the latter without heat capacity and thermal losses.

The nearby calculator **Scheil residual-liquid composition** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Fraction solidified = 0.6428571 fraction**, with all other model values held as published: the response is **0.083666003 fraction**. At **Fraction solidified = 0.7714286 fraction**, the response is **0.1045825 fraction**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.16268389 fraction per fraction**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Apparent temperature rises can come from thermocouple position or furnace control; independently calibrated sensors are necessary.

### Examination, synthesis and a failure test

**Challenge question:** What evidence would distinguish shrinkage porosity from gas porosity after sectioning? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Integrated investigation: Segregation during a fictional casting

### Scientific problem and hypotheses

An imagined binary melt freezes in a thick mould and later shows unexpected low-melting interdendritic regions. A reviewer blames insufficient stirring without measuring either composition or thermal history. Define a primary observable and a rival mechanism. Hypothesis A should predict the observed conversion from the intended transformation; hypothesis B should explain a similar gross signal through a competing event. Name the observations needed to prefer one. A theory that can be made to fit every possible thermal or structural trace is not adequately discriminating. Describe a negative control, a second spatial sampling location, and an independent physical modality capable of challenging the initial phase identification.

### Mathematical framework

Compute Scheil-like terminal-liquid enrichment, compare with a complete-equilibrium bound and use partitioning to predict where microscale chemistry should differ. Distinguish equilibrium state functions from kinetic rate parameters, then write the relevant conservation law. If a temperature is specified, record whether it is a furnace set point, actual specimen center, interface point or surface reading. If a phase fraction is inferred, identify the normalization and its endpoint calibration. Compare output at two values using the unit's interactive models; report the numerical change, dimension and range of acceptable inputs. Where a constitutive relation is approximate, propagate rather than conceal parameter uncertainty.

A rigorous explanation should include what would happen at slow cooling compared with quenching, and explain the conditions under which both trajectories would arrive at similar or different microstructures. Include whether substitutional diffusion, interstitial transport, cooperative lattice change, or interface movement supplies the controlling timescale. If the sample contains gradients, explain how a local transformation result might differ between edge and core. The comparison should be phrased as testable predicted signatures, not a guessed dramatic micrograph.

### Measurement and validation sequence

Acquire center/surface cooling curves, compositional maps, line-scan calibration and porosity measurements at known sections. First capture the untreated material's structure and chemistry. Then document time-temperature history using two relevant temperature locations. Finally collect phase-sensitive and morphology-sensitive data at several interrupted processing states. Specify whether each observation is destructive, whether thermal cycling alters the sample, and how replicate variance will be measured. Blind a second analyst to the proposed mechanism and ask them to calculate a phase fraction or kinetic parameter from the primary traces. Record disagreements before revising interpretation.

### Claim boundaries and report requirements

A single fitted k value or an unmeasured dendrite spacing cannot certify the casting's mechanical safety. A polished final report must include: starting microstructure; phase definitions; a reaction or chemical-potential argument; a checked worked estimate; a temperature–time diagram annotated with sensor location; synthetic model graphs clearly marked as simulated; a second-method validation plan; and a concise list of conditions that would make the engineering conclusion unsafe or invalid. Numerical compatibility is a necessary implementation check but is not sufficient evidence of mechanism or service suitability. Explain precisely what further data would turn the exercise into a candidate processing procedure.

### Interact with this unit's models

<!-- MODEL_6 -->

<!-- MODEL_7 -->

