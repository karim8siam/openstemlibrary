# Unit 3: Chemical potentials, activities and open systems

**Guiding question:** How does matter exchange change equilibrium and transform a nominal composition into phase-specific driving forces?

## Unit overview and conceptual map

Chemical potential links atomic transfer to macroscopic constraints. The slope of the appropriate Gibbs-energy surface matters more than a simple average energy. Two phases can exchange a species until chemical potentials equalize, but conservation of all other species and possible charge-neutrality conditions must simultaneously hold. Oxygen in a flowing furnace is governed by a reservoir potential that depends on fugacity and temperature, while interstitial oxygen inside a solid interacts with defects and structural sites.

Chemical-potential conventions deserve explicit annotation. A standard-state shift changes reference chemical potentials but not consistent equilibrium constants. Experimental inference of an activity can require vapor pressure, electrochemical response or partition measurements. An activity coefficient is not always a direct species concentration and often varies with temperature. When activity curves are assessed independently, Gibbs–Duhem consistency helps expose hidden fitting problems.



## Lesson 3.1: Partial molar Gibbs energy

### 1. Physical idea and what is actually specified

Chemical potential μi=(∂G/∂ni)T,P,nj is the marginal free-energy cost of adding species i while holding other species amounts fixed. It is not generally equal to total G divided by total moles. At equilibrium for exchangeable species, chemical potentials must match across accessible phases.

### 2. Worked laboratory thought experiment

An alloy contains A and B; adding a trace of B changes composition. Compare the partial molar response predicted from a tangent slope with a naive average formation energy. Construct a thought experiment allowing B diffusion between two grains.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Ideal B chemical-potential mixing term**. Set **Mole fraction B** to **0.2368 fraction**; all other model parameters remain at the reference values stated below. The output is **-10180.71 J/mol**. State the model assumptions explicitly: μB−μB°=RT ln x at 850 K; ideal solution. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.3496 fraction** to obtain **-7427.482 J/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A chemical-potential equality requires a pathway for mass exchange and a time scale adequate for redistribution. If a passivating layer blocks transfer, measured compositions may stay unequal.

Compare two interpretations of the imagined observations. Interpretation A uses **partial molar gibbs energy** as its leading explanation. Interpretation B attributes some of the same signal to **an invalid reference volume or stress**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which quantity, not total Gibbs energy per mole, governs diffusion direction for a species? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **-10180.71 J/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A chemical-potential equality requires a pathway for mass exchange and a time scale adequate for redistribution. If a passivating layer blocks transfer, measured compositions may stay unequal.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 3.2: Ideal solution activity

### 1. Physical idea and what is actually specified

In an ideal solution, μi=μi°+RT ln xi with a carefully specified standard state. Since 0<xi≤1, ln xi is nonpositive and the mixing contribution decreases chemical potential as a component becomes dilute. Different standard states change the numerical μ° but not physically measurable equilibrium predictions.

### 2. Worked laboratory thought experiment

Compute the chemical-potential change of B when its mole fraction doubles from 0.10 to 0.20 at a given temperature. Then repeat in a real alloy using activity instead of mole fraction; discuss how an unknown activity coefficient prevents a confident numerical conclusion.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Ideal-gas reservoir contribution to chemical potential**. Set **Partial pressure ratio P/P°** to **4.5055 ratio**; all other model parameters remain at the reference values stated below. The output is **11264.18 J/mol**. State the model assumptions explicitly: Δμ=RT ln(P/P°), at 900 K; ideal-gas fugacity approximation. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **5.7043 ratio** to obtain **13029.58 J/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A zero mole fraction cannot be inserted directly into ln xi; its chemical potential is treated as a limiting value. Real mixing is not universally ideal, especially near ordering and separation.

Compare two interpretations of the imagined observations. Interpretation A uses **ideal solution activity** as its leading explanation. Interpretation B attributes some of the same signal to **fitted mixing interactions with weak extrapolation**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** What compositional data can test whether the ideal activity assumption is defensible? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **11264.18 J/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A zero mole fraction cannot be inserted directly into ln xi; its chemical potential is treated as a limiting value. Real mixing is not universally ideal, especially near ordering and separation.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 3.3: Activity coefficients and standard states

### 1. Physical idea and what is actually specified

Nonideal chemical potentials are expressed using activities ai=γixi for an appropriate convention. The coefficient γi bundles interaction effects, so its temperature and composition dependence are essential for extrapolation. Raoult and Henry standard states may be chosen for different concentration regimes; they cannot be mixed invisibly.

### 2. Worked laboratory thought experiment

Interpret an alloy measurement where vapor pressure over the melt differs from an ideal prediction. Separate the partial-pressure observation from the thermodynamic inference of activity, documenting the reference state and whether the solute is dilute.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Ideal B chemical-potential mixing term**. Set **Mole fraction B** to **0.6692 fraction**; all other model parameters remain at the reference values stated below. The output is **-2838.736 J/mol**. State the model assumptions explicitly: μB−μB°=RT ln x at 850 K; ideal solution. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.782 fraction** to obtain **-1737.851 J/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

An estimated γi for one temperature cannot automatically be used to model another where ordering, association or phase changes occur. Numerical activity can be standard-state dependent even though equilibrium outcomes are not.

Compare two interpretations of the imagined observations. Interpretation A uses **activity coefficients and standard states** as its leading explanation. Interpretation B attributes some of the same signal to **latent heat or fixture energy**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which observable would constrain an activity coefficient without direct calorimetry? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **-2838.736 J/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **An estimated γi for one temperature cannot automatically be used to model another where ordering, association or phase changes occur. Numerical activity can be standard-state dependent even though equilibrium outcomes are not.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 3.4: Gibbs–Duhem relation

### 1. Physical idea and what is actually specified

The Gibbs–Duhem equation imposes Σni dμi=−S dT+V dP; at fixed T,P, Σxi dμi=0. Component chemical potentials are therefore not independent functions of composition. This supplies a thermodynamic consistency test for measured activity curves.

### 2. Worked laboratory thought experiment

Suppose experiments determine one component activity over an alloy composition range. Explain how the Gibbs–Duhem constraint supports inference of the second component and why error integration and endpoint conventions must be examined.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Ideal-gas reservoir contribution to chemical potential**. Set **Partial pressure ratio P/P°** to **2.2078 ratio**; all other model parameters remain at the reference values stated below. The output is **5926.523 J/mol**. State the model assumptions explicitly: Δμ=RT ln(P/P°), at 900 K; ideal-gas fugacity approximation. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **3.4066 ratio** to obtain **9172.043 J/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Two independently fitted activity equations may appear individually smooth yet violate Gibbs–Duhem. Such a database is internally inconsistent and can yield fictitious phase boundaries.

Compare two interpretations of the imagined observations. Interpretation A uses **gibbs–duhem relation** as its leading explanation. Interpretation B attributes some of the same signal to **trapped metastability or undercooling**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** How could you detect a consistency violation before passing data to an equilibrium solver? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **5926.523 J/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Two independently fitted activity equations may appear individually smooth yet violate Gibbs–Duhem. Such a database is internally inconsistent and can yield fictitious phase boundaries.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 3.5: Gas reservoirs and defect chemical potentials

### 1. Physical idea and what is actually specified

Oxygen potential, hydrogen potential and vapor pressure can control defect equilibria in solids. A surrounding reservoir can exchange species even when the solid appears compositionally constant in bulk measurements. Relevant potentials include the gas partial-pressure contribution and solid-phase site constraints.

### 2. Worked laboratory thought experiment

A metal oxide is annealed under controlled oxygen partial pressure. Predict whether raising oxygen potential favors oxidation relative to reduction, while stating that the actual defect response depends on charge balance and defect chemistry.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Ideal B chemical-potential mixing term**. Set **Mole fraction B** to **0.453 fraction**; all other model parameters remain at the reference values stated below. The output is **-5596.329 J/mol**. State the model assumptions explicitly: μB−μB°=RT ln x at 850 K; ideal solution. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.5658 fraction** to obtain **-4024.927 J/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A plotted oxygen-pressure boundary is not a kinetic corrosion law. Surface transport, diffusion, protective scale integrity and gas impurities may dominate observed rates.

Compare two interpretations of the imagined observations. Interpretation A uses **gas reservoirs and defect chemical potentials** as its leading explanation. Interpretation B attributes some of the same signal to **a phase misidentification or microsegregation**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which gas composition measurements are needed before interpreting a defect-concentration change? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **-5596.329 J/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A plotted oxygen-pressure boundary is not a kinetic corrosion law. Surface transport, diffusion, protective scale integrity and gas impurities may dominate observed rates.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Integrated unit project — Oxygen potential and a high-temperature material

### Research situation and falsifiable objective

A hypothetical oxide coating exchanges oxygen with an atmosphere whose nominal composition is recorded only as “air.” At fixed furnace temperature a change of gas flow produces a different apparent equilibrium composition, but the sample may not have reached steady state.



### Analysis plan and mathematical constraints

Write the oxygen chemical potential relative to a stated reference pressure. Define the gas-reservoir boundary and any internal charge neutrality conditions; distinguish the oxygen partial pressure at the gas inlet from that adjacent to the hot specimen.



### Experimental discriminators

Use a calibrated oxygen probe, repeat at different flow rates and hold times, and verify near-surface chemistry separately from bulk oxygen uptake. Compare a mass-balance estimate to one based only on lattice parameter change.



### Limitations and responsible reporting

The simplified ideal-gas expression is not a full nonstoichiometric oxide defect model. A fixed oxygen potential does not ensure that the oxide equilibrates throughout its thickness.



### Project deliverables and assessment rubric





### Interactive demonstrations for this unit

<!-- MODEL_4 -->

<!-- MODEL_5 -->

