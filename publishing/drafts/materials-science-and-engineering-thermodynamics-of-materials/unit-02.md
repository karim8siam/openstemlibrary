# Unit 2: Entropy, free energies and stability

**Guiding question:** Which inequalities determine whether a process is allowed and what the equilibrium state can be?

## Unit overview and conceptual map

The second law becomes useful when the equilibrium criterion is matched to the apparatus. In a closed system with controlled T,P, the combined thermal and mechanical reservoirs justify a Gibbs-energy minimum. In a rigid vessel with controlled T,V, a Helmholtz description is generally appropriate. Applying the wrong potential can change the predicted order of candidate states, especially when density, chemical composition or reservoir exchange is significant. The natural-variable statement is a compact way of recording boundary conditions, not a trick of notation.

An equilibrium calculation can answer which phase should eventually be favored without locating the saddle-point barrier between structures. That distinction explains supercooling, precipitation delays and retained phases. If a free-energy plot shows two minima, local curvature determines small-fluctuation stability while the global minimum determines equilibrium preference within the candidate set. Inspecting curvature at one composition cannot replace a common-tangent construction when a mixture of distant compositions lowers the overall free energy.



## Lesson 2.1: The second law as an inequality

### 1. Physical idea and what is actually specified

For an isolated composite, total entropy cannot decrease. In a real heating event, entropy production is nonnegative even though the specimen alone may cool or become more ordered. A reversible path is a calculation device; finite temperature gradients and viscous or plastic flow generate irreversibility.

### 2. Worked laboratory thought experiment

A hot copper block contacts a cooler alloy. Compute entropy changes for the blocks using logarithmic temperature ratios and show that the combined entropy is positive when they equilibrate. Track energy conservation separately from the entropy inequality.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Entropy increment under constant molar heat capacity**. Set **Final temperature** to **469.6 K**; all other model parameters remain at the reference values stated below. The output is **11.20247 J/(mol K)**. State the model assumptions explicitly: ΔS=Cp ln(T/300), Cp=25 J/(mol K), reversible state-function path. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **551.2 K** to obtain **15.20788 J/(mol K)**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

It is wrong to assert that entropy of every subsystem increases; entropy may leave a selected region with expelled heat. The combined boundary must be clear.

Compare two interpretations of the imagined observations. Interpretation A uses **the second law as an inequality** as its leading explanation. Interpretation B attributes some of the same signal to **polarization and interfacial overpotential**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** How would you test whether a reversible approximation is adequate for a rapid quench? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **11.20247 J/(mol K)** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **It is wrong to assert that entropy of every subsystem increases; entropy may leave a selected region with expelled heat. The combined boundary must be clear.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 2.2: Enthalpy and Gibbs energy

### 1. Physical idea and what is actually specified

At fixed temperature and pressure, the relevant equilibrium criterion for a closed, simple compressible system is minimizing Gibbs free energy G=H−TS. Negative ΔG indicates a thermodynamically favorable change between defined states, not necessarily an observable transformation within laboratory time.

### 2. Worked laboratory thought experiment

Consider a metastable glass and a more stable crystal at identical composition, pressure and temperature. Plot schematic free energy against transformation coordinate to distinguish an endpoint preference from an activation barrier.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Reaction Gibbs energy versus temperature**. Set **Temperature** to **570 K**; all other model parameters remain at the reference values stated below. The output is **0.6 kJ/mol**. State the model assumptions explicitly: ΔH=−45 kJ/mol and ΔS=−0.080 kJ/(mol K), assumed constant; defined reaction basis. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **642 K** to obtain **6.36 kJ/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Enthalpy reduction alone does not establish the stable phase because entropy matters; a negative free-energy change does not provide a kinetic rate or mechanism.

Compare two interpretations of the imagined observations. Interpretation A uses **enthalpy and gibbs energy** as its leading explanation. Interpretation B attributes some of the same signal to **surface-driven or defect-driven energy**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** What extra measurement would reveal a nucleation barrier when the equilibrium phase is already known? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **0.6 kJ/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Enthalpy reduction alone does not establish the stable phase because entropy matters; a negative free-energy change does not provide a kinetic rate or mechanism.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 2.3: Helmholtz energy and mechanical constraints

### 1. Physical idea and what is actually specified

At fixed T,V and particle numbers, Helmholtz free energy A=U−TS is minimized at equilibrium. Switching from a constant-pressure experiment to one in a rigid sealed volume can change the appropriate potential and the predicted equilibrium. Legendre transforms replace one natural variable by its conjugate.

### 2. Worked laboratory thought experiment

Compare an oxide pellet sealed in a rigid container with a pellet under externally imposed oxygen pressure. State which variables the apparatus actually controls, and write the free-energy function appropriate to each boundary condition.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Entropy increment under constant molar heat capacity**. Set **Final temperature** to **782.4 K**; all other model parameters remain at the reference values stated below. The output is **23.96459 J/(mol K)**. State the model assumptions explicitly: ΔS=Cp ln(T/300), Cp=25 J/(mol K), reversible state-function path. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **864 K** to obtain **26.44476 J/(mol K)**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A nominally sealed vessel may still contain gas headspace that changes pressure as temperature rises. Assuming pressure and volume both fixed while applying ideal gas expansion is internally inconsistent.

Compare two interpretations of the imagined observations. Interpretation A uses **helmholtz energy and mechanical constraints** as its leading explanation. Interpretation B attributes some of the same signal to **an unmodeled competing phase**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which boundary measurements are essential before choosing Gibbs rather than Helmholtz energy? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **23.96459 J/(mol K)** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A nominally sealed vessel may still contain gas headspace that changes pressure as temperature rises. Assuming pressure and volume both fixed while applying ideal gas expansion is internally inconsistent.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 2.4: Differentials and Maxwell relations

### 1. Physical idea and what is actually specified

For a simple multicomponent equilibrium system, dG=−S dT+V dP+Σμi dni. Maxwell relations arise from equality of mixed second derivatives when the potential is smooth. They connect difficult measurements to more accessible thermal and mechanical responses.

### 2. Worked laboratory thought experiment

Use the pressure derivative of chemical potential to explain why the equilibrium of a condensed phase can shift under high pressure. A schematic test compares volume estimates from dilatometry with free-energy curvature from fitted thermodynamic data.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Reaction Gibbs energy versus temperature**. Set **Temperature** to **432 K**; all other model parameters remain at the reference values stated below. The output is **-10.44 kJ/mol**. State the model assumptions explicitly: ΔH=−45 kJ/mol and ΔS=−0.080 kJ/(mol K), assumed constant; defined reaction basis. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **504 K** to obtain **-4.68 kJ/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A first-order phase transition introduces nonanalyticities: derivatives inside a single phase do not automatically describe the jump across coexistence. Non-equilibrium specimens need additional internal variables.

Compare two interpretations of the imagined observations. Interpretation A uses **differentials and maxwell relations** as its leading explanation. Interpretation B attributes some of the same signal to **an invalid reference volume or stress**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which derivative discontinuity would identify latent heat in a free-energy-versus-temperature plot? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **-10.44 kJ/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A first-order phase transition introduces nonanalyticities: derivatives inside a single phase do not automatically describe the jump across coexistence. Non-equilibrium specimens need additional internal variables.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 2.5: Stability, curvature and fluctuations

### 1. Physical idea and what is actually specified

Equilibrium needs not only equal competing potentials but local stability against small perturbations. A stable homogeneous phase has positive relevant curvature with respect to composition at fixed T,P, subject to constraints. Negative curvature predicts instability in a simple mean-field model, whereas positive curvature does not rule out a distant lower-energy state.

### 2. Worked laboratory thought experiment

Sketch two regular-solution free-energy curves at high and low temperature. Mark spinodal regions where local curvature changes sign and distinguish them from the full miscibility-gap region found by a common tangent.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Entropy increment under constant molar heat capacity**. Set **Final temperature** to **626 K**; all other model parameters remain at the reference values stated below. The output is **18.3892 J/(mol K)**. State the model assumptions explicitly: ΔS=Cp ln(T/300), Cp=25 J/(mol K), reversible state-function path. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **707.6 K** to obtain **21.45241 J/(mol K)**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A schematic energy landscape cannot substitute for quantitative assessed thermodynamic parameters. Finite particles may remain trapped in metastable states despite an apparently favorable bulk separation.

Compare two interpretations of the imagined observations. Interpretation A uses **stability, curvature and fluctuations** as its leading explanation. Interpretation B attributes some of the same signal to **fitted mixing interactions with weak extrapolation**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** What different response would a tiny composition fluctuation show inside and outside the spinodal interval? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **18.3892 J/(mol K)** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A schematic energy landscape cannot substitute for quantitative assessed thermodynamic parameters. Finite particles may remain trapped in metastable states despite an apparently favorable bulk separation.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Integrated unit project — Thermodynamic stability versus transformation kinetics

### Research situation and falsifiable objective

A designed oxide has two structural polymorphs. One hypothetical free-energy branch becomes lower at a target temperature, but a sample quenched from high temperature preserves the other structure for weeks. A student claims the measured persistence violates the second law.



### Analysis plan and mathematical constraints

Construct both free-energy branches using schematic ΔH and ΔS terms. Explain where equality defines a coexistence boundary, and add a free-energy barrier against a reaction coordinate. Record how a reversible reference path for entropy differs from the real quenched pathway.



### Experimental discriminators

Propose aging at multiple temperatures, in situ diffraction and repeated calorimetric cycles. A transformation rate that accelerates with temperature may reveal kinetic barriers even where the lower-G phase is already predicted.



### Limitations and responsible reporting

Thermodynamics does not identify nucleation sites, interface mobilities or detailed reaction mechanisms. Do not confuse a lower free-energy phase with an automatic instantaneous transition.



### Project deliverables and assessment rubric





### Interactive demonstrations for this unit

<!-- MODEL_2 -->

<!-- MODEL_3 -->

