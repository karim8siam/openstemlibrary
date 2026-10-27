# Unit 1: Systems, energy and material state

**Guiding question:** What energy bookkeeping remains valid when a material is heated, compressed or transformed?

## Unit overview and conceptual map

The most common energy error in an early materials analysis is a boundary error rather than an arithmetic error. Compare a specimen-only control volume, a fixture-plus-specimen control volume and an entire heat-treatment machine. When the boundary moves, some flows become internal and some disappear from the external balance. This does not change physics; it changes which measurements belong on the right-hand side. When an operator claims “we delivered 15 kJ to the alloy,” ask whether 15 kJ is electrical input to the heater, calorimeter-baseline-corrected heat, net specimen enthalpy rise or only an ideal heat-capacity integral.

A physically plausible account must represent multiple energy stores. Deformation can store elastic energy and dislocation energy; heat can leave through convection, conduction and radiation; heating can alter magnetic or structural degrees of freedom. Over a purely reversible closed path, a well-defined state function returns to its original value, while net heat and work may be exchanged over a cycle. A first-law check is therefore necessary but not sufficient for showing reversibility. Deliberately propose two processes having the same final temperature but different histories and ask how the latent heat or defect content might differ.

Before doing the calculations, write a one-paragraph model statement naming the system, independent components, energy reference, physical constraints and candidate phases. In this unit, all numerical inputs are synthetic and deliberately chosen to make trends observable with pencil and calculator. The resulting plots teach mathematical sensitivity, not measured equilibrium locations. Keep at least one genuine competing hypothesis alive until a discriminating observation has been identified.

## Lesson 1.1: System boundaries and material state

### 1. Physical idea and what is actually specified

Define the closed material system and specify which species, phases, external fields and interfaces belong within it. Extensive quantities such as internal energy and entropy scale with system size, whereas intensive temperature and pressure describe equilibrium state. State variables do not depend on the imagined path; work and heat do.

### 2. Worked laboratory thought experiment

A sealed metal capsule is heated inside a furnace while a load cell records expansion force. Draw three alternative boundaries around capsule, furnace and atmosphere. The same measured temperature can enter different balance equations because each boundary admits different heat and work flows.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Sensible heat for a fixed specimen**. Set **Specimen mass** to **0.816 kg**; all other model parameters remain at the reference values stated below. The output is **88.128 kJ**. State the model assumptions explicitly: Q=m c ΔT, c=0.9 kJ/(kg K), ΔT=120 K; no phase change. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **1.152 kg** to obtain **124.416 kJ**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.

A worked case becomes scientifically informative only when the units and domain of the expression are examined. The calculator holds the parameters in its assumptions fixed and varies a single input. A real heat treatment, phase transformation or interfacial measurement might change several parameters together. If the equation contains a logarithm, document the reference state and confirm the argument is positive and dimensionless. If the result depends on a molar basis, document the corresponding formula unit. If it describes a phase fraction, check that the overall composition lies between the coexistence compositions.

### 3. Competing explanation and scope

A thermal camera gives surface radiance-derived temperature, not internal energy. Alloy mass, heat capacity and latent heat must be known or measured. A reaction inside a sealed capsule may change phase proportions without adding mass.

Compare two interpretations of the imagined observations. Interpretation A uses **system boundaries and material state** as its leading explanation. Interpretation B attributes some of the same signal to **latent heat or fixture energy**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which two independent measurements can distinguish thermal input from stored mechanical energy during loading? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **88.128 kJ** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A thermal camera gives surface radiance-derived temperature, not internal energy. Alloy mass, heat capacity and latent heat must be known or measured. A reaction inside a sealed capsule may change phase proportions without adding mass.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 1.2: First law and sign conventions

### 1. Physical idea and what is actually specified

For a closed system choose ΔU=Q−W_by, with W_by positive when the system does work on surroundings. The same experiment may be presented as ΔU=Q+W_on, but the sign convention must remain explicit. An apparent missing energy term can be electrical work, chemical heat, mechanical deformation, or a neglected mass flow.

### 2. Worked laboratory thought experiment

Consider a hot working press: a specimen absorbs thermal energy, is plastically deformed and cools by convection. Assign positive or negative signs to every term while keeping the specimen as the system. Check the accounting over a complete heating-and-deformation cycle.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Temperature-dependent molar enthalpy increment**. Set **Final temperature** to **732.5 K**; all other model parameters remain at the reference values stated below. The output is **11.74778 kJ/mol**. State the model assumptions explicitly: Cp(T)=25+0.01(T−300) J/(mol K), integrated from 300 K; one-phase illustrative fit. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **834.5 K** to obtain **14.79095 kJ/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Measured electrical supply energy is not equal to heat deposited in a sample; fixture heating, radiation and power conversion losses intervene. Temperature change alone does not identify the net work contribution.

Compare two interpretations of the imagined observations. Interpretation A uses **first law and sign conventions** as its leading explanation. Interpretation B attributes some of the same signal to **trapped metastability or undercooling**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Would the conclusion survive moving the control surface from the sample to the entire furnace? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **11.74778 kJ/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Measured electrical supply energy is not equal to heat deposited in a sample; fixture heating, radiation and power conversion losses intervene. Temperature change alone does not identify the net work contribution.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 1.3: Heat capacities of solids

### 1. Physical idea and what is actually specified

At constant pressure, heating an equilibrium material through a single phase often uses ΔH=∫Cp(T)dT. Cp may change with temperature and composition, and a phase transition adds latent heat not captured by extrapolating one smooth capacity fit. Cp and Cv differ when thermal expansion and compressibility matter.

### 2. Worked laboratory thought experiment

A ceramic coupon is heated from 300 K to 1000 K. Compare a constant heat-capacity estimate against one with Cp increasing with T. Identify a calibration run for the empty calorimeter and describe how mass loss would invalidate a simple closed-system analysis.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Sensible heat for a fixed specimen**. Set **Specimen mass** to **2.104 kg**; all other model parameters remain at the reference values stated below. The output is **227.232 kJ**. State the model assumptions explicitly: Q=m c ΔT, c=0.9 kJ/(kg K), ΔT=120 K; no phase change. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **2.44 kg** to obtain **263.52 kJ**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Using a one-point heat-capacity value across a transformation can hide a large enthalpy jump. The instrument baseline and sample mass uncertainty may dominate numerical precision.

Compare two interpretations of the imagined observations. Interpretation A uses **heat capacities of solids** as its leading explanation. Interpretation B attributes some of the same signal to **a phase misidentification or microsegregation**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which temperature interval should be excluded before fitting a single-phase heat-capacity polynomial? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **227.232 kJ** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Using a one-point heat-capacity value across a transformation can hide a large enthalpy jump. The instrument baseline and sample mass uncertainty may dominate numerical precision.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 1.4: Mechanical, surface and electrical work

### 1. Physical idea and what is actually specified

Materials can exchange pV work, tensile deformation work, electrical work and interfacial work. A generalized energy equation contains work terms pairing each generalized force with its conjugate displacement. Pressure–volume work alone cannot describe growth of a crack surface or charging of a capacitor-like interface.

### 2. Worked laboratory thought experiment

Compare uniaxial elastic stretching with hydrostatic compression. Use a stress–strain graph to identify mechanical energy input per unit volume and state why elastic unloading returns energy while plastic deformation leaves dissipation.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Temperature-dependent molar enthalpy increment**. Set **Final temperature** to **537 K**; all other model parameters remain at the reference values stated below. The output is **6.205845 kJ/mol**. State the model assumptions explicitly: Cp(T)=25+0.01(T−300) J/(mol K), integrated from 300 K; one-phase illustrative fit. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **639 K** to obtain **9.049605 kJ/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Stress, strain, pressure and volume cannot be casually interchanged without geometry and sign conventions. A crack can grow at nearly unchanged bulk volume while consuming surface energy.

Compare two interpretations of the imagined observations. Interpretation A uses **mechanical, surface and electrical work** as its leading explanation. Interpretation B attributes some of the same signal to **polarization and interfacial overpotential**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** What measurable conjugate force belongs with newly created surface area? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **6.205845 kJ/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Stress, strain, pressure and volume cannot be casually interchanged without geometry and sign conventions. A crack can grow at nearly unchanged bulk volume while consuming surface energy.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 1.5: Reference states and energy data

### 1. Physical idea and what is actually specified

Absolute enthalpy is convention-dependent; reaction enthalpies and differences between defined states are observable. Set reference conditions, composition basis, pressure and temperature before combining tabulated numbers. Some data are reported per mole of formula units and others per mole of atoms.

### 2. Worked laboratory thought experiment

Imagine comparing oxide formation energies from two sources: one normalizes to one mole of oxygen molecules while the other normalizes to one mole of oxide. Rebalance the chemical equation and reproduce a common basis before ranking candidate processes.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Sensible heat for a fixed specimen**. Set **Specimen mass** to **1.46 kg**; all other model parameters remain at the reference values stated below. The output is **157.68 kJ**. State the model assumptions explicitly: Q=m c ΔT, c=0.9 kJ/(kg K), ΔT=120 K; no phase change. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **1.796 kg** to obtain **193.968 kJ**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

An excellent numerical match obtained from incompatible reference conventions is a bookkeeping accident. Raw database entries often contain stated standard states, uncertainties and validity intervals.

Compare two interpretations of the imagined observations. Interpretation A uses **reference states and energy data** as its leading explanation. Interpretation B attributes some of the same signal to **surface-driven or defect-driven energy**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Can two compounds with different stoichiometries be ranked by unnormalized reaction-energy values? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **157.68 kJ** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **An excellent numerical match obtained from incompatible reference conventions is a bookkeeping accident. Raw database entries often contain stated standard states, uncertainties and validity intervals.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Integrated unit project — Heat accounting for an alloy specimen

### Research situation and falsifiable objective

A sealed capsule containing a model Al-rich specimen is raised from 300 K to 900 K inside a laboratory furnace. Electrical power is logged for the heater, but only a fraction reaches the sample. A holder of similar heat capacity is separately characterized. An observed endothermic feature may be a transformation or a sample/fixture artifact.

Frame the research question as a comparison that could be disproved. For example, decide whether the hypothesis predicts one measurable thermal, compositional or structural pattern that a competing explanation does not. Define an operational observable with units and a plausible accuracy. The project should remain a thought experiment until actual measurements are available. Its fictional data may be used for coding practice, but the deliverable must not be represented as an experiment conducted by the author or student.

### Analysis plan and mathematical constraints

Build three energy balances: sample, furnace, and specimen-plus-holder. Integrate a single-phase Cp(T) expression; insert a symbolic latent heat term and calculate the systematic difference if the feature is mistakenly assigned to sensible heat. Maintain a table identifying measured and estimated quantities. Compare mass-normalized and molar-normalized results.

To keep the analysis reproducible, provide an explicit conserved-quantity check, one energy or free-energy balance, and a table separating directly stated synthetic values from quantities computed by the model. State whether the environment is temperature controlled, pressure controlled, volume controlled or open to chemical reservoirs. Include the reference state for each chemical potential or reaction free energy. If an inferred phase amount appears, recalculate the mixture composition as a mass-balance check. If an interfacial energy appears, make sure it is referenced to area, not volume without conversion.

### Experimental discriminators

Repeat an empty-holder baseline at different ramp speeds, and check a post-heating mass measurement. If the feature survives the controls and correlates with a new phase signature, the transformation interpretation strengthens; otherwise it remains ambiguous.

Each proposed measurement should have a reason for being included. A blank or standard isolates a possible instrument offset; a second chemistry or treatment path tests transferability; and a time series tests whether kinetic delays are likely. Set a criterion for rejecting the original hypothesis, such as a contrary phase fraction, a new crystallographic phase, a change in sign, or a disagreement larger than the uncertainty range. A claim that simply “fits the model” is weak when the same dataset was used to choose its parameters.

### Limitations and responsible reporting

No synthetic energy trace proves that a real alloy has a transition at the selected temperature. Furnace losses, radiation, and surface oxidation can invalidate a simple calorimetric reduction.

A final report should contain four clearly separated sections: observations (or explicitly labelled synthetic inputs), assumptions and fitted parameters, predictions with uncertainty or sensitivity, and decisions or additional tests. Explain how an engineer might act if the evidence were later confirmed and what decision should be postponed while uncertainty remains. Provide a second paragraph describing the limitations of assuming equilibrium when the actual treatment may involve rapid cooling, diffusion limits, reaction barriers or nonuniform temperature. No safety-critical decision should rest on the simplified models in this chapter.

### Project deliverables and assessment rubric

| Deliverable | Acceptable evidence | Typical failure |
|---|---|---|
| Boundary definition | Identifies all mass, heat and work exchanges | Treats a flowing reactive system as closed |
| Mathematical derivation | Explicit potential, conservation equations, units | Combines quantities on incompatible bases |
| Model check | Recomputable numerical script or hand solution | Undocumented calculator output |
| Independent test | Specific measured quantity expected to differ by hypothesis | Fits original data a second time |
| Interpretation | Separates equilibrium, kinetics and uncertainty | Calls a simulated prediction an observed phase |
| Ethics | Reveals synthetic inputs and publication limits | Claims manufacturing or safety validation |

**Unit review:** Which lesson’s central assumption would most likely fail in this investigation? Which added measurement would reduce uncertainty most efficiently? Explain both choices through physical constraints rather than by listing more instruments. Prepare a one-page response and include the assumptions behind both companion interactive models.

### Interactive demonstrations for this unit

<!-- MODEL_0 -->

<!-- MODEL_1 -->

