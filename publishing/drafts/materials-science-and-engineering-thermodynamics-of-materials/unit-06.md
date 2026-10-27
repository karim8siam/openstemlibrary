# Unit 6: Defects, interfaces and nanoscale thermodynamics

**Guiding question:** Why can a real microstructure deviate from bulk equilibrium without violating thermodynamics?

## Unit overview and conceptual map

Reducing interfacial area can reduce Gibbs free energy even without changing the bulk phase composition. This explains the tendency of fine grains to coarsen and particles to ripen, provided boundaries can move. Crystalline interface energy is not generally isotropic, and segregation can change it. Bulk equilibrium diagrams omit some finite-size terms; as characteristic dimensions approach the nanoscale, those terms can become comparable to the bulk free-energy differences that stabilize phases.

Classical nucleation provides a sharp but limited calculation: a spherical nucleus gains bulk free energy proportional to radius cubed while paying an interfacial cost proportional to radius squared. The competition produces a maximum and a critical radius when the volume term is favorable. Below that radius the model predicts shrinkage; above it growth is thermodynamically favored, not kinetically guaranteed. Real nuclei usually form near defects, interfaces or pre-existing clusters and can be strongly affected by strain and anisotropic surface energy.



## Lesson 6.1: Equilibrium vacancies

### 1. Physical idea and what is actually specified

A simple dilute noninteracting vacancy model gives xv≈exp(−Gf/kBT), where Gf includes formation free energy. The number of vacancies increases with temperature when formation energetics are treated consistently. Real solids have temperature-dependent defects, multiple charge states and non-negligible interactions at high concentrations.

### 2. Worked laboratory thought experiment

Compute vacancy fractions at two temperatures for an illustrative 1 eV formation free energy. Then compare this equilibrium prediction with a quenched specimen retaining excess vacancies, explaining how diffusion limits equilibration.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Equilibrium vacancy fraction**. Set **Temperature** to **864 K**; all other model parameters remain at the reference values stated below. The output is **1.468667e-06 fraction**. State the model assumptions explicitly: Dilute independent vacancies, formation free energy 1 eV; no trapping. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **1008 K** to obtain **1.000507e-05 fraction**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Quenching can freeze in defects and create a non-equilibrium state; a textbook equilibrium expression cannot predict a measured retained fraction without kinetics.

Compare two interpretations of the imagined observations. Interpretation A uses **equilibrium vacancies** as its leading explanation. Interpretation B attributes some of the same signal to **fitted mixing interactions with weak extrapolation**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which temperature-history data are needed before treating defect concentrations as equilibrium values? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **1.468667e-06 fraction** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Quenching can freeze in defects and create a non-equilibrium state; a textbook equilibrium expression cannot predict a measured retained fraction without kinetics.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 6.2: Interfacial free energy and curvature

### 1. Physical idea and what is actually specified

Creating an interface at fixed relevant thermodynamic constraints costs approximately γA for isotropic surface energy γ and area A. Highly dispersed microstructures have high area per unit volume, so interfaces can strongly affect stability. Real crystalline boundaries have anisotropic energy depending on orientation, composition and complexion.

### 2. Worked laboratory thought experiment

Estimate the free-energy cost of doubling interfacial area for a nanostructured film with a stated γ. Compare the result with a hypothetical bulk free-energy advantage, keeping energy units and material amount consistent.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Interfacial Gibbs energy**. Set **Additional interface area** to **0.9055 m²**; all other model parameters remain at the reference values stated below. The output is **0.63385 J**. State the model assumptions explicitly: Isotropic interface γ=0.7 J/m²; fixed chemistry and temperature. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **1.1443 m²** to obtain **0.80101 J**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A constant surface energy assumed at all temperatures and facet orientations is a rough teaching approximation. Adsorbed solutes can lower interface free energy.

Compare two interpretations of the imagined observations. Interpretation A uses **interfacial free energy and curvature** as its leading explanation. Interpretation B attributes some of the same signal to **latent heat or fixture energy**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which microstructural control would isolate area from boundary chemistry in a coarsening experiment? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **0.63385 J** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A constant surface energy assumed at all temperatures and facet orientations is a rough teaching approximation. Adsorbed solutes can lower interface free energy.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 6.3: Classical nucleation barrier

### 1. Physical idea and what is actually specified

For a spherical homogeneous nucleus with positive interfacial energy and negative volume driving energy, ΔG(r)=4πr²γ+(4π/3)r³Δgv. The critical radius r*=2γ/|Δgv| separates shrinking from growing embryos in this simplified treatment; the critical state is a barrier maximum.

### 2. Worked laboratory thought experiment

Calculate critical radii for several driving-force magnitudes. Relate the smaller critical radius at stronger undercooling to the separate issue of atomic mobility, which can be lower at low temperatures.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Equilibrium vacancy fraction**. Set **Temperature** to **1416 K**; all other model parameters remain at the reference values stated below. The output is **0.0002759527 fraction**. State the model assumptions explicitly: Dilute independent vacancies, formation free energy 1 eV; no trapping. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **1560 K** to obtain **0.0005879941 fraction**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Actual nucleation may be heterogeneous, anisotropic, strain-coupled or structurally complex. The formula does not predict observable nucleation rates without kinetic prefactors.

Compare two interpretations of the imagined observations. Interpretation A uses **classical nucleation barrier** as its leading explanation. Interpretation B attributes some of the same signal to **trapped metastability or undercooling**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** How might a heterogeneous surface change the barrier while leaving the bulk thermodynamic preference unchanged? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **0.0002759527 fraction** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Actual nucleation may be heterogeneous, anisotropic, strain-coupled or structurally complex. The formula does not predict observable nucleation rates without kinetic prefactors.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 6.4: Grain growth and capillarity

### 1. Physical idea and what is actually specified

Curved boundaries can move to reduce total interfacial energy, subject to boundary mobility, pinning and solute drag. The thermodynamic driving tendency often scales with curvature, but grain growth rate is kinetic and microstructure-dependent. Stored dislocation energy from deformation adds a separate driving contribution.

### 2. Worked laboratory thought experiment

Compare a cold-worked alloy and a fully recrystallized alloy held at identical temperature. Predict which has additional driving energy and how precipitate pinning can suppress grain growth in both.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Interfacial Gibbs energy**. Set **Additional interface area** to **0.4478 m²**; all other model parameters remain at the reference values stated below. The output is **0.31346 J**. State the model assumptions explicitly: Isotropic interface γ=0.7 J/m²; fixed chemistry and temperature. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.6866 m²** to obtain **0.48062 J**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A simple interface-energy minimization does not imply all grains become spherical or that coarsening laws are universal. Grain boundary anisotropy creates faceted boundaries.

Compare two interpretations of the imagined observations. Interpretation A uses **grain growth and capillarity** as its leading explanation. Interpretation B attributes some of the same signal to **a phase misidentification or microsegregation**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which time-resolved observations separate boundary driving pressure from mobility? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **0.31346 J** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A simple interface-energy minimization does not imply all grains become spherical or that coarsening laws are universal. Grain boundary anisotropy creates faceted boundaries.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 6.5: Segregation and nanoscale phase equilibria

### 1. Physical idea and what is actually specified

Grain boundaries and surfaces may enrich certain solutes because transferring atoms to an interface changes Gibbs free energy. Segregation changes boundary cohesion, corrosion resistance, and precipitate nucleation. Nanoscale phase equilibria can shift due to capillarity; size effects need not match bulk phase diagrams.

### 2. Worked laboratory thought experiment

Study a hypothetical doped ceramic nanoparticle. Predict how a solute favoring interfaces might change measured near-surface composition relative to the bulk, then identify a chemically sensitive microscopy or spectroscopy method.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Equilibrium vacancy fraction**. Set **Temperature** to **1140 K**; all other model parameters remain at the reference values stated below. The output is **3.79439e-05 fraction**. State the model assumptions explicitly: Dilute independent vacancies, formation free energy 1 eV; no trapping. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **1284 K** to obtain **0.0001188336 fraction**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Surface sensitivity, contamination and preferential sputtering can distort composition measurements. An observed enrichment is not enough to calculate a segregation free energy without a suitable model.

Compare two interpretations of the imagined observations. Interpretation A uses **segregation and nanoscale phase equilibria** as its leading explanation. Interpretation B attributes some of the same signal to **polarization and interfacial overpotential**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Would an independently measured bulk activity help constrain the inferred segregation thermodynamics? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **3.79439e-05 fraction** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Surface sensitivity, contamination and preferential sputtering can distort composition measurements. An observed enrichment is not enough to calculate a segregation free energy without a suitable model.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Integrated unit project — Interface-rich ceramic nanoparticles

### Research situation and falsifiable objective

A compositionally uniform ceramic powder is measured in two average particle-size batches. One batch displays altered transformation temperature and boundary segregation. Surface chemistry differs slightly between processing runs.



### Analysis plan and mathematical constraints

Calculate a hypothetical interfacial energy from reported area and γ, then use the critical-nucleus equation to explore how bulk driving energy changes a capillarity barrier. Compare these energies to a phase fraction conversion on a common basis.



### Experimental discriminators

Make a surface-sensitive composition measurement and compare it with bulk diffraction. Repeat after controlled annealing at equal atmosphere and monitor particle coarsening alongside the transformation.



### Limitations and responsible reporting

Surface energy and Gibbs–Thomson shifts depend on facet and environment. Nanoparticles may agglomerate and be thermally nonuniform; a simple spherical model is only a diagnostic analogy.



### Project deliverables and assessment rubric





### Interactive demonstrations for this unit

<!-- MODEL_10 -->

<!-- MODEL_11 -->

