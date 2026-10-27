# Unit 3: Growth, impingement and transformation kinetics

**Guiding question:** How does nucleation become a measurable transformed fraction?

## A physical orientation for this unit

A DSC-based transformed fraction appears sigmoidal but the sample may contain overlapping precipitate reactions and thermal gradients. A high-quality curve fit could hide multiple mechanisms. A complete analysis separates the phase identities, the relevant conserved quantities, the imposed temperature–time path, and the measurable response. It is not enough to state that 'a new phase formed': the experiment must establish what is new, where it appeared, whether composition changed and whether the rate is constrained by diffusion, interface kinetics or transformation strain. This unit emphasizes **conversion fraction**, using a **nucleation-plus-growth history** to test plausible mechanisms instead of treating a suggestive curve as proof.

Use ideal JMAK fractions as a null model; fit in separate conversion windows and compare the parameters. Predict heat-flow and diffraction changes that single- and double-step scenarios would produce. Before analyzing each lesson, prepare a ledger of observations, assumed boundary conditions and competing interpretations. Distinguish thermodynamic possibility from a nucleation pathway, a transformation rate and eventual property evolution. Include the thermal program and a practical measurement time resolution. Repeat a calculation at two values of a chosen input; the sensitivity often exposes whether the dominant uncertainty lies in material constants, microstructure or instrumentation.

## Vocabulary and conservation checkpoints

State the initial constituent, product state, composition basis and time origin. A phase fraction may be on a mass, volume, mole or diffraction-intensity basis, and those scales cannot be exchanged without a conversion model. State precisely whether each coefficient is a measured value, an empirical correlation, a thermodynamic state function or a synthetic teaching assumption. For this unit, pay particular attention to **time-dependent impingement** and to possible confusion from **growth rate and transport control**. A suitable cross-check would be **an independent conversion probe**.

## Lesson 3.1: Interface-controlled growth

### Concept, boundary conditions and physical meaning

When attachment at a phase boundary limits advance, interface velocity can scale with thermodynamic driving force near equilibrium. Crystallographic steps, facet orientation and interface mobility matter. A measured radius-versus-time slope indicates a velocity only if the interface geometry is known and the growth law remains constant. Impurity drag and interface segregation can make apparent mobility temperature and history dependent.

**Working relationship.** v=M Delta G_driver with units of mobility adjusted to whether the driving force is per mole, area or volume. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **interface-controlled growth**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Use a fictional spherical particle expanding from 2 to 5 micrometers in 120 seconds; obtain an average radial growth speed of 0.025 micrometers per second. Ask how much a 10 s detection delay changes the inferred slope.

The nearby calculator **Diffusion penetration scale** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Elapsed time = 147.1429 s**, with all other model values held as published: the response is **1.2130246 µm**. At **Elapsed time = 289.2857 s**, the response is **1.7008401 µm**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.0034318684 µm per s**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Diffusion-controlled growth can mimic a short interval of linear radius growth; growth geometry and solute gradients must be independently checked.

### Examination, synthesis and a failure test

**Challenge question:** Which interrupted-growth experiment would distinguish constant interface velocity from square-root-in-time diffusion advance? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 3.2: Diffusion-controlled front motion

### Concept, boundary conditions and physical meaning

If long-range solute transport is required, growth commonly slows as diffusion fields extend. In simple self-similar limits a characteristic penetration or radius increment scales with square root of D times time. Interface mass balance couples front speed to the discontinuity in solute flux and composition, known as a Stefan-type condition. The coefficient depends on supersaturation and boundary conditions, not just diffusivity.

**Working relationship.** ell~sqrt(Dt) for simple Fickian diffusion; interface flux balance requires solute conservation. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **diffusion-controlled front motion**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

With an invented D=1e-14 m²/s, evaluate sqrt(Dt) at 100, 400 and 900 s and explain why quadrupling time doubles the diffusion length rather than quadrupling it.

The nearby calculator **Isothermal Avrami transformed fraction** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Hold time = 257.1429 s**, with all other model values held as published: the response is **0.65800749 fraction**. At **Hold time = 385.7143 s**, the response is **0.94801229 fraction**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.0022555928 fraction per s**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Real grains have finite dimensions, cross-diffusion and varying interface compositions; sqrt(Dt) is a scale estimate, not a complete moving-boundary solution.

### Examination, synthesis and a failure test

**Challenge question:** How would you test whether an observed growth exponent changes when grain size becomes limiting? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 3.3: Avrami models and impingement

### Concept, boundary conditions and physical meaning

The Johnson–Mehl–Avrami–Kolmogorov family models transformed fraction as one minus the exponential of an extended transformed volume. A constant effective exponent can summarize site-saturated or continuing nucleation with idealized growth geometry. Fitted n is not by itself a unique fingerprint of mechanism. Impingement prevents new-phase regions from overlapping physically even when a mathematical extended-volume construction counts the overlap.

**Working relationship.** X=1-exp[-(kt)^n], and ln[-ln(1-X)]=n ln t+n ln k for ideal isothermal kinetics. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **avrami models and impingement**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

For X=1-exp[-(kt)^n], take k=0.004 s^-1 and n=2.5. Evaluate X after 100 and 300 seconds and compare slopes on a double-log Avrami plot.

The nearby calculator **Diffusion penetration scale** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Elapsed time = 431.4286 s**, with all other model values held as published: the response is **2.0770859 µm**. At **Elapsed time = 573.5714 s**, the response is **2.3949351 µm**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.0022361255 µm per s**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

Changing nucleation rates, anisotropic grains, finite sample size and multiple overlapping reactions often invalidate a single exponent over the entire conversion interval.

### Examination, synthesis and a failure test

**Challenge question:** What residual pattern would reject a single-stage Avrami fit even if the coefficient of determination is high? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 3.4: Time–temperature–transformation diagrams

### Concept, boundary conditions and physical meaning

A TTT diagram describes transformation progress after rapid transfer to a chosen isothermal temperature, typically using onset and completion curves for a specified alloy and prior microstructure. Near the equilibrium temperature there is low driving force; at much lower temperatures diffusion may become slow. This can generate the characteristic C-shaped nose of some diffusional transformations. Different transformation products may have separate start regions.

**Working relationship.** Isothermal fractions can be fitted using JMAK only when a single dominant process and a fixed temperature are plausible. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **time–temperature–transformation diagrams**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Give an illustrative nose at 650 degrees C and 8 seconds; compare isothermal holds at 700 and 550 degrees C without asserting they yield the same microstructure merely because equal time has passed.

The nearby calculator **Isothermal Avrami transformed fraction** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Hold time = 514.2857 s**, with all other model values held as published: the response is **0.99768794 fraction**. At **Hold time = 642.8571 s**, the response is **0.99997516 fraction**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **1.7789541e-05 fraction per s**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

TTT charts are experimental and alloy-specific; they do not directly represent continuous cooling and they require a defined austenitizing or starting-state procedure.

### Examination, synthesis and a failure test

**Challenge question:** Why does the fastest isothermal transformation temperature often differ from the temperature of greatest undercooling? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Lesson 3.5: Continuous cooling and thermal gradients

### Concept, boundary conditions and physical meaning

Under continuous cooling the specimen visits changing temperatures and consequently changing nucleation and growth rates. A CCT diagram is not obtained by directly tracing a path across a TTT diagram. Cross-section size, heat-transfer coefficient, agitation and latent heat influence local cooling history. The center of a large part may avoid a desired product even if a surface thermocouple shows rapid quenching.

**Working relationship.** t_window=Delta T/|dT/dt| is a bookkeeping estimate, not a CCT transformation predictor. Read the terms in this relationship as quantities attached to a specific state, geometry or path. Do not assume that a convenient equation has proved the physical mechanism. For **continuous cooling and thermal gradients**, define the initial state and possible product before assigning a fraction, temperature or rate. A bulk average can conceal a sharp local concentration field, different lattice orientations or particles too small for the selected imaging method. When temperature or composition is not uniform, a single numerical parameter is at best a spatially weighted approximation; every reported number should state which part of the specimen it represents.

### Guided experiment and a concrete numerical anchor

Compare two illustrative cooling slopes of 5 and 50 K/s through a 300 K transformation window; estimate exposure durations of 60 and 6 seconds before investigating position-dependent rate histories.

The nearby calculator **Diffusion penetration scale** offers one deliberately simplified numerical anchor, chosen to practice dimensional analysis rather than to represent the material in the vignette. Set **Elapsed time = 715.7143 s**, with all other model values held as published: the response is **2.6752837 µm**. At **Elapsed time = 857.8571 s**, the response is **2.9289198 µm**; within this idealization it increases. The finite-difference sensitivity for these two settings is approximately **0.0017843749 µm per s**. Check the direction analytically and consider whether the change would be distinguishable from your measurement resolution. Do not confuse this sensitivity with the effect of changing every correlated process variable in a real furnace.

### Rival interpretations and evidence that could separate them

A nominal furnace ramp differs from specimen center temperature; alloy-specific CCT data and thermal simulation are needed for responsible heat-treatment decisions.

### Examination, synthesis and a failure test

**Challenge question:** Which two thermocouple positions best reveal section-thickness effects on product fractions? In a full solution, draw or describe the initial phase boundary, list governing assumptions, and calculate the two synthetic responses shown above from the published formula. Interpret the sign of their difference physically rather than merely repeating the mathematical trend. Next propose two mutually discriminating outcomes of an experiment, each compatible with known conservation laws. Identify one uncertainty that could reverse your mechanistic conclusion and an instrument capable of measuring it.

## Integrated investigation: A misleading Avrami exponent

### Scientific problem and hypotheses

A DSC-based transformed fraction appears sigmoidal but the sample may contain overlapping precipitate reactions and thermal gradients. A high-quality curve fit could hide multiple mechanisms. Define a primary observable and a rival mechanism. Hypothesis A should predict the observed conversion from the intended transformation; hypothesis B should explain a similar gross signal through a competing event. Name the observations needed to prefer one. A theory that can be made to fit every possible thermal or structural trace is not adequately discriminating. Describe a negative control, a second spatial sampling location, and an independent physical modality capable of challenging the initial phase identification.

### Mathematical framework

Use ideal JMAK fractions as a null model; fit in separate conversion windows and compare the parameters. Predict heat-flow and diffraction changes that single- and double-step scenarios would produce. Distinguish equilibrium state functions from kinetic rate parameters, then write the relevant conservation law. If a temperature is specified, record whether it is a furnace set point, actual specimen center, interface point or surface reading. If a phase fraction is inferred, identify the normalization and its endpoint calibration. Compare output at two values using the unit's interactive models; report the numerical change, dimension and range of acceptable inputs. Where a constitutive relation is approximate, propagate rather than conceal parameter uncertainty.

A rigorous explanation should include what would happen at slow cooling compared with quenching, and explain the conditions under which both trajectories would arrive at similar or different microstructures. Include whether substitutional diffusion, interstitial transport, cooperative lattice change, or interface movement supplies the controlling timescale. If the sample contains gradients, explain how a local transformation result might differ between edge and core. The comparison should be phrased as testable predicted signatures, not a guessed dramatic micrograph.

### Measurement and validation sequence

Use an isothermal hold, second calorimetric heating rate, matched diffraction series and direct microscopy on arrested states. First capture the untreated material's structure and chemistry. Then document time-temperature history using two relevant temperature locations. Finally collect phase-sensitive and morphology-sensitive data at several interrupted processing states. Specify whether each observation is destructive, whether thermal cycling alters the sample, and how replicate variance will be measured. Blind a second analyst to the proposed mechanism and ask them to calculate a phase fraction or kinetic parameter from the primary traces. Record disagreements before revising interpretation.

### Claim boundaries and report requirements

The Avrami exponent is an effective shape parameter unless nucleation history, growth geometry and impingement are independently supported. A polished final report must include: starting microstructure; phase definitions; a reaction or chemical-potential argument; a checked worked estimate; a temperature–time diagram annotated with sensor location; synthetic model graphs clearly marked as simulated; a second-method validation plan; and a concise list of conditions that would make the engineering conclusion unsafe or invalid. Numerical compatibility is a necessary implementation check but is not sufficient evidence of mechanism or service suitability. Explain precisely what further data would turn the exercise into a candidate processing procedure.

### Interact with this unit's models

<!-- MODEL_4 -->

<!-- MODEL_5 -->

