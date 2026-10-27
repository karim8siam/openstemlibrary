# Unit 5: Phase diagrams and transitions

**Guiding question:** How do equilibrium constraints map onto the phases observed in solidification and heat treatment?

## Unit overview and conceptual map

A phase diagram compresses many equilibrium constraints into a geometric picture, but each line presumes a defined pressure, composition basis and allowed set of phases. Counting components and coexisting phases helps interpret an invariant reaction. The lever rule adds conservation: the same pair of coexistence compositions can accommodate a continuum of overall compositions through different amounts of phases. Thermodynamic coexistence describes what is possible after exchange and equilibration, not necessarily what a rapidly solidified microstructure actually contains.

Solidification is a convenient demonstration of the difference between state and path. An equilibrium path permits the solid to continually re-equilibrate by diffusion. In practical casting, diffusion through the solid can be slow compared with front advancement, so local composition differs from the ideal tie-line distribution. A familiar schematic Scheil approximation enforces mixing in liquid and suppresses diffusion in solid. These are limiting kinetic assumptions outside the strictly equilibrium diagram. Experimental microsegregation should be discussed with the cooling history attached.



## Lesson 5.1: Phase rule and degrees of freedom

### 1. Physical idea and what is actually specified

The Gibbs phase rule for a nonreacting system is F=C−P+2; at fixed pressure one common condensed-system form is F=C−P+1. Count independent components and phases carefully. Constraints imposed by chemical reactions, charged species or fixed oxygen reservoirs can alter the naive count.

### 2. Worked laboratory thought experiment

Use a binary two-phase alloy at fixed pressure to obtain one degree of freedom, commonly chosen as temperature or a phase composition coordinate. Contrast with a triple phase invariant reaction at fixed pressure.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Lever-rule B-rich phase fraction**. Set **Overall mole fraction B** to **0.3376 fraction**; all other model parameters remain at the reference values stated below. The output is **0.2293333 mole fraction**. State the model assumptions explicitly: Tie-line end compositions Cα=0.20 and Cβ=0.80, fixed T,P. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.4072 fraction** to obtain **0.3453333 mole fraction**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A single polished micrograph cannot reveal the number of independently equilibrated phases under operating conditions. A phase that exists transiently during quenching may not be an equilibrium phase.

Compare two interpretations of the imagined observations. Interpretation A uses **phase rule and degrees of freedom** as its leading explanation. Interpretation B attributes some of the same signal to **surface-driven or defect-driven energy**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which degrees of freedom remain if both temperature and pressure are externally fixed? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **0.2293333 mole fraction** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A single polished micrograph cannot reveal the number of independently equilibrated phases under operating conditions. A phase that exists transiently during quenching may not be an equilibrium phase.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 5.2: Lever rule and phase fractions

### 1. Physical idea and what is actually specified

At a binary two-phase equilibrium at fixed T,P, mass balance gives fβ=(C0−Cα)/(Cβ−Cα) for phase compositions measured on a consistent basis. The lever rule returns a molar phase fraction for mole-based compositions when all assumptions hold. Conversion to volume fraction needs molar volumes.

### 2. Worked laboratory thought experiment

For a two-phase tie line with 20 and 80 atomic percent B, evaluate the fraction of the B-rich phase at overall 44 percent B. Confirm by reversing the mass balance: fαCα+fβCβ=C0.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Clapeyron coexistence slope**. Set **Transformation molar volume change** to **2.975 cm³/mol**; all other model parameters remain at the reference values stated below. The output is **3.361345 MPa/K**. State the model assumptions explicitly: ΔS=10 J/(mol K); ΔV=variable in cm³/mol; slope=ΔS/ΔV. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **3.635 cm³/mol** to obtain **2.751032 MPa/K**; the reported output falls as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

The formula becomes invalid outside the two-phase interval or if the endpoints are not actual coexistence compositions. Interpreting a microscope area fraction as an exact mole fraction may also mislead.

Compare two interpretations of the imagined observations. Interpretation A uses **lever rule and phase fractions** as its leading explanation. Interpretation B attributes some of the same signal to **an unmodeled competing phase**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which measurements distinguish a phase composition from the overall alloy composition? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **3.361345 MPa/K** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **The formula becomes invalid outside the two-phase interval or if the endpoints are not actual coexistence compositions. Interpreting a microscope area fraction as an exact mole fraction may also mislead.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 5.3: Clapeyron and coexistence slopes

### 1. Physical idea and what is actually specified

For coexistence between two pure phases, dP/dT=ΔS/ΔV. A small transformation volume can make pressure-sensitive boundaries steep; latent heat connects ΔS=ΔH/T at reversible coexistence. This relation describes equilibrium slope, not how rapidly an interface propagates.

### 2. Worked laboratory thought experiment

Choose illustrative molar entropy and volume changes to estimate a boundary slope. Recalculate when the volume change is halved and interpret why its sign depends on relative phase volume.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Lever-rule B-rich phase fraction**. Set **Overall mole fraction B** to **0.6044 fraction**; all other model parameters remain at the reference values stated below. The output is **0.674 mole fraction**. State the model assumptions explicitly: Tie-line end compositions Cα=0.20 and Cβ=0.80, fixed T,P. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.674 fraction** to obtain **0.79 mole fraction**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A numerical slope from one reference condition should not be extrapolated over huge pressure intervals without considering changes in ΔS and ΔV or new phases.

Compare two interpretations of the imagined observations. Interpretation A uses **clapeyron and coexistence slopes** as its leading explanation. Interpretation B attributes some of the same signal to **an invalid reference volume or stress**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which measured thermophysical property must be supplied before inferring dP/dT from calorimetry? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **0.674 mole fraction** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A numerical slope from one reference condition should not be extrapolated over huge pressure intervals without considering changes in ΔS and ΔV or new phases.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 5.4: Eutectic, peritectic and solidus features

### 1. Physical idea and what is actually specified

A binary eutectic is a liquid transforming to two solids at invariant temperature and composition under fixed pressure; a peritectic involves liquid plus one solid transforming to another solid. Liquidus and solidus delimit different phase regions and should not be confused with the temperature at which an alloy completely melts.

### 2. Worked laboratory thought experiment

Trace cooling paths for compositions left, at and right of a eutectic composition. For each, predict primary phase formation and the residual liquid reaction, then explain what a differential scanning calorimetry peak might reveal.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Clapeyron coexistence slope**. Set **Transformation molar volume change** to **1.71 cm³/mol**; all other model parameters remain at the reference values stated below. The output is **5.847953 MPa/K**. State the model assumptions explicitly: ΔS=10 J/(mol K); ΔV=variable in cm³/mol; slope=ΔS/ΔV. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **2.37 cm³/mol** to obtain **4.219409 MPa/K**; the reported output falls as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Solidification pathways in castings reflect thermal gradients, solute partitioning and non-equilibrium undercooling. A visible eutectic morphology need not prove equilibrium phase fractions.

Compare two interpretations of the imagined observations. Interpretation A uses **eutectic, peritectic and solidus features** as its leading explanation. Interpretation B attributes some of the same signal to **fitted mixing interactions with weak extrapolation**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** What extra data would distinguish a peritectic reaction from a solid-state transformation? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **5.847953 MPa/K** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Solidification pathways in castings reflect thermal gradients, solute partitioning and non-equilibrium undercooling. A visible eutectic morphology need not prove equilibrium phase fractions.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 5.5: Metastability, nucleation and hysteresis

### 1. Physical idea and what is actually specified

An equilibrium phase boundary indicates free-energy equality, but transformations require nucleation and growth pathways. A specimen can supercool below a liquidus or retain a high-temperature phase when diffusion or nucleation is slow. Hysteresis often records kinetics and defects rather than an uncertainty in the equilibrium definition.

### 2. Worked laboratory thought experiment

Compare two cooling rates for the same alloy and predict differences in onset temperature, microsegregation and retained microstructure. Distinguish an equilibrium diagram prediction from a Scheil-type limiting solidification estimate.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Lever-rule B-rich phase fraction**. Set **Overall mole fraction B** to **0.471 fraction**; all other model parameters remain at the reference values stated below. The output is **0.4516667 mole fraction**. State the model assumptions explicitly: Tie-line end compositions Cα=0.20 and Cβ=0.80, fixed T,P. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.5406 fraction** to obtain **0.5676667 mole fraction**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A transformation start temperature on cooling is not automatically a precise equilibrium phase boundary. Reheating, hold experiments and compositional measurements help separate path effects.

Compare two interpretations of the imagined observations. Interpretation A uses **metastability, nucleation and hysteresis** as its leading explanation. Interpretation B attributes some of the same signal to **latent heat or fixture energy**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** How would a sequence of isothermal holds test whether observed hysteresis is kinetic? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **0.4516667 mole fraction** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A transformation start temperature on cooling is not automatically a precise equilibrium phase boundary. Reheating, hold experiments and compositional measurements help separate path effects.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Integrated unit project — Equilibrium solidification versus industrial cooling

### Research situation and falsifiable objective

An invented A–B alloy with a eutectic diagram is cast into molds of two thicknesses. The two castings show different interdendritic compositions and residual liquid patterns, despite equal nominal chemistry.



### Analysis plan and mathematical constraints

Draw an equilibrium phase path with tie lines and lever-rule quantities. Draw a separate limiting non-equilibrium path assuming complete liquid mixing and negligible solid diffusion, making clear that this is an additional kinetic idealization.



### Experimental discriminators

Compare post-cast energy-dispersive chemical maps, hold treatments, and DSC cooling/heating curves. A convergence of compositions after long homogenization is consistent with diffusion-driven movement toward equilibrium.



### Limitations and responsible reporting

Cooling rate and fluid flow can drive segregation, dendrite arm spacing and interface morphology. The equilibrium phase diagram alone cannot predict the as-cast microstructure.



### Project deliverables and assessment rubric





### Interactive demonstrations for this unit

<!-- MODEL_8 -->

<!-- MODEL_9 -->

