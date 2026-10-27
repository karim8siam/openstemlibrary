# Unit 8: Computational thermodynamics and evidence

**Guiding question:** How can a phase-equilibrium prediction become reproducible and testable rather than merely colorful software output?

## Unit overview and conceptual map

Computational thermodynamics is a workflow with assumptions, not a substitute for them. The database encodes the phase models and interaction terms; the solver enforces constraints; the output gives a conditional equilibrium state. Unknown phases cannot emerge merely because optimization is accurate. Extrapolation from well-measured binary corners into an unevaluated quinary alloy can be especially unreliable even when the software reports many digits.

A robust decision is built through adversarial validation. Recompute with different initial guesses, perturb uncertain assessed parameters, include plausible competing phases and compare against at least one independent experimental constraint. If the predicted safe processing interval is narrow, report a conservative margin rather than a single precise temperature. Finally, couple an equilibrium result to kinetics only when diffusion, nucleation and mobility parameters are independently justified; otherwise distinguish equilibrium preference from predicted microstructure.



## Lesson 8.1: Thermodynamic databases and assessment

### 1. Physical idea and what is actually specified

A CALPHAD-style database encodes Gibbs energies of candidate phases as functions of temperature, composition and other state variables, using models fitted to critically evaluated evidence. Its equilibrium solver minimizes total Gibbs energy under constraints. Coverage depends on which phases, endmembers and assessed interactions were included.

### 2. Worked laboratory thought experiment

A designer searches for an alloy with a desired processing window. Inspect database phase coverage before computing liquidus and solidus, and compare predictions against at least one independent invariant temperature or phase composition.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Regular-solution critical temperature**. Set **Binary interaction energy** to **8400 J/mol**; all other model parameters remain at the reference values stated below. The output is **505.1439 K**. State the model assumptions explicitly: Symmetric composition-independent Ω, mean-field critical point at x=0.5. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **10800 J/mol** to obtain **649.4707 K**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

High numerical optimizer precision cannot correct a missing phase or poorly assessed ternary interaction. A predicted phase absence may simply reflect a database gap.

Compare two interpretations of the imagined observations. Interpretation A uses **thermodynamic databases and assessment** as its leading explanation. Interpretation B attributes some of the same signal to **an unmodeled competing phase**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** What would make a database prediction unreliable in an extrapolated five-component composition? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **505.1439 K** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **High numerical optimizer precision cannot correct a missing phase or poorly assessed ternary interaction. A predicted phase absence may simply reflect a database gap.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 8.2: Constrained Gibbs-energy minimization

### 1. Physical idea and what is actually specified

Total Gibbs minimization must enforce element conservation, nonnegative phase amounts, charge constraints where relevant and imposed reservoir chemical potentials. Comparing minima of individual phase functions without solving composition balance can produce impossible equilibrium assemblages.

### 2. Worked laboratory thought experiment

For an overall AB mixture, consider two candidate phases whose compositions differ. Set up mass-balance equations and minimize the weighted free energy while keeping total A and B fixed.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Homogeneous critical nucleus radius**. Set **Bulk free-energy driving magnitude** to **252.5 MJ/m³**; all other model parameters remain at the reference values stated below. The output is **2.376238 nm**. State the model assumptions explicitly: Spherical γ=0.30 J/m²; Δgv=−drive×10⁶ J/m³; capillarity-only. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **306.5 MJ/m³** to obtain **1.957586 nm**; the reported output falls as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Numerical convergence to one stationary point does not prove the global minimum. Multiphase models with metastable local solutions demand independent initialization and sensitivity checks.

Compare two interpretations of the imagined observations. Interpretation A uses **constrained gibbs-energy minimization** as its leading explanation. Interpretation B attributes some of the same signal to **an invalid reference volume or stress**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** How can a conservation residual reveal a plausible-looking but invalid solver output? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **2.376238 nm** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Numerical convergence to one stationary point does not prove the global minimum. Multiphase models with metastable local solutions demand independent initialization and sensitivity checks.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 8.3: Sensitivity and uncertainty in assessed parameters

### 1. Physical idea and what is actually specified

Thermodynamic fitting parameters carry covariance and model-form uncertainty. Phase boundaries can move when enthalpy or interaction parameters change within plausible ranges. Sensitivity studies should propagate such changes to the practical decision, rather than only reporting a perfect nominal curve.

### 2. Worked laboratory thought experiment

Vary a regular-solution interaction parameter by ±10% and quantify the shift in estimated critical temperature. Then explain why a range of phase fractions may matter more for manufacturing risk than a small change in an abstract fit score.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Regular-solution critical temperature**. Set **Binary interaction energy** to **17600 J/mol**; all other model parameters remain at the reference values stated below. The output is **1058.397 K**. State the model assumptions explicitly: Symmetric composition-independent Ω, mean-field critical point at x=0.5. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **20000 J/mol** to obtain **1202.724 K**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

One-at-a-time perturbations ignore parameter correlations and missing phases. Synthetic data can test code behavior but not calibrate a predictive alloy database.

Compare two interpretations of the imagined observations. Interpretation A uses **sensitivity and uncertainty in assessed parameters** as its leading explanation. Interpretation B attributes some of the same signal to **fitted mixing interactions with weak extrapolation**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which independent measured phase boundary would best reduce the uncertainty relevant to the design? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **1058.397 K** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **One-at-a-time perturbations ignore parameter correlations and missing phases. Synthetic data can test code behavior but not calibrate a predictive alloy database.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 8.4: Coupling thermodynamics to kinetics

### 1. Physical idea and what is actually specified

Equilibrium sets potential driving forces; diffusion, nucleation, boundary mobility and heat extraction influence what is observed in finite time. Scheil solidification, diffusion simulations and phase-field methods introduce distinct approximations beyond bulk free-energy minimization.

### 2. Worked laboratory thought experiment

Compare equilibrium solidification with complete liquid mixing and negligible solid diffusion. Predict segregation trends, then identify a condition such as long high-temperature hold that may bring the sample closer to equilibrium.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Homogeneous critical nucleus radius**. Set **Bulk free-energy driving magnitude** to **149 MJ/m³**; all other model parameters remain at the reference values stated below. The output is **4.026846 nm**. State the model assumptions explicitly: Spherical γ=0.30 J/m²; Δgv=−drive×10⁶ J/m³; capillarity-only. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **203 MJ/m³** to obtain **2.955665 nm**; the reported output falls as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A better-looking microstructure simulation can still be misleading if mobility parameters and interface boundary conditions are unvalidated. Equilibrium diagrams alone cannot specify final grain size.

Compare two interpretations of the imagined observations. Interpretation A uses **coupling thermodynamics to kinetics** as its leading explanation. Interpretation B attributes some of the same signal to **latent heat or fixture energy**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which time-series dataset can reveal whether a kinetic calibration transfers to a new processing rate? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **4.026846 nm** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A better-looking microstructure simulation can still be misleading if mobility parameters and interface boundary conditions are unvalidated. Equilibrium diagrams alone cannot specify final grain size.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 8.5: Reproducibility, ethics and materials decisions

### 1. Physical idea and what is actually specified

A thermodynamic claim should identify specimen composition, phase list, parameter database version, reference states, minimization constraints, residual tolerances and uncertainty. Publish raw measurements with rights and units, separate measured from fitted and simulated values, and disclose excluded mechanisms.

### 2. Worked laboratory thought experiment

Draft a decision memo for a hypothetical heat-treatment temperature: use a prediction, one independent measurement, sensitivity range and a conservative recommendation. State how this would change for a regulated implant or a safety-critical turbine part.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Regular-solution critical temperature**. Set **Binary interaction energy** to **13000 J/mol**; all other model parameters remain at the reference values stated below. The output is **781.7703 K**. State the model assumptions explicitly: Symmetric composition-independent Ω, mean-field critical point at x=0.5. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **15400 J/mol** to obtain **926.0971 K**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A teaching calculator cannot certify component fitness or replace destructive tests, fatigue studies, regulatory approvals or real chemical analysis. Transparency requires documenting what is not yet known.

Compare two interpretations of the imagined observations. Interpretation A uses **reproducibility, ethics and materials decisions** as its leading explanation. Interpretation B attributes some of the same signal to **trapped metastability or undercooling**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which independent replication result would be strong enough to change the engineering recommendation? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **781.7703 K** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A teaching calculator cannot certify component fitness or replace destructive tests, fatigue studies, regulatory approvals or real chemical analysis. Transparency requires documenting what is not yet known.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Integrated unit project — Database-driven processing window with uncertainty

### Research situation and falsifiable objective

An engineer uses a generic CALPHAD database to select an annealing temperature for a multicomponent alloy. The calculated window between precipitate dissolution and unwanted melting is narrow. No phase-diagram experimental check exists near the intended composition.



### Analysis plan and mathematical constraints

List included phases and assessed interaction ranges, then compute a sensitivity ensemble varying a relevant Ω parameter. Recalculate feasible processing bounds using conservative margins that accommodate measurement and modeling uncertainty.



### Experimental discriminators

Plan an independent DSC and phase-composition validation, then compare predictions with hold-out data rather than only with measurements used in assessment. If results disagree, check missing phase models before changing fit parameters.



### Limitations and responsible reporting

Without validated phase coverage, a narrow processing window may be imaginary. Computational equilibrium is necessary evidence for planning, not enough for safety-critical production authorization.



### Project deliverables and assessment rubric





### Interactive demonstrations for this unit

<!-- MODEL_14 -->

<!-- MODEL_15 -->

