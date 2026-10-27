# Unit 7: Reactive, electrochemical and thermal processes

**Guiding question:** How can equilibrium calculations inform oxidation, batteries and real processing without posing as rate predictions?

## Unit overview and conceptual map

A negative reaction Gibbs energy at a specified chemical environment indicates a thermodynamic driving force, not a corrosion rate, extraction yield or battery power. Ellingham plots compare standard-state redox tendencies, while the gas reservoir and nonideal activities change the actual reaction potential. In electrochemistry, the Nernst equation ties an equilibrium electrical potential to activities and reaction stoichiometry. Significant current leads to transport and activation losses; the measured operating voltage does not equal the ideal reversible voltage.

Calorimetric peaks and voltage plateaus are observations requiring calibration and interpretation. A peak on a differential scanning calorimeter can represent melting, precipitation, recovery, decomposition or instrument-related effects; integrated area, heating-rate shifts, mass changes and complementary diffraction are often necessary. Similar caution applies to oxide-scale growth: an equilibrium stability diagram indicates possible species, but scale adherence, defect diffusion, cyclic stress and local chemistry affect actual durability.



## Lesson 7.1: Chemical reaction Gibbs energy

### 1. Physical idea and what is actually specified

For reaction progress ξ, dG/dξ=ΔrG; at equilibrium ΔrG=0 when the permitted species exchange and phases are modeled consistently. ΔrG=ΔrG°+RT lnQ links standard reaction energy with activities or fugacities. Reaction stoichiometry fixes exponents and standard-state conventions.

### 2. Worked laboratory thought experiment

Consider reduction of a generic metal oxide under a mixed-gas atmosphere. Construct Q from activities and partial pressures before calculating which reaction direction lowers G. Check the balanced equation before writing thermodynamic conclusions.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Equilibrium-reaction constant**. Set **Temperature** to **576 K**; all other model parameters remain at the reference values stated below. The output is **1.373532 dimensionless**. State the model assumptions explicitly: ΔG°=10 kJ/mol−0.020 kJ/(mol K)·T; activities dimensionless. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **672 K** to obtain **1.850915 dimensionless**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Reaction favorability does not guarantee rapid reduction through a dense surface layer. Activity coefficients, nonstoichiometric solids and multi-reaction equilibria can change the answer.

Compare two interpretations of the imagined observations. Interpretation A uses **chemical reaction gibbs energy** as its leading explanation. Interpretation B attributes some of the same signal to **a phase misidentification or microsegregation**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which equilibrium parameter should change if inert diluent is added at constant total pressure? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **1.373532 dimensionless** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Reaction favorability does not guarantee rapid reduction through a dense surface layer. Activity coefficients, nonstoichiometric solids and multi-reaction equilibria can change the answer.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 7.2: Ellingham-style oxide stability

### 1. Physical idea and what is actually specified

Oxide formation free energy plotted against T is useful for comparing oxidation and reduction tendencies at specified standard states. Straight-line sketches assume approximately constant reaction enthalpy and entropy. Actual stable phases and oxygen activity matter; crossing of lines alone does not define process yield.

### 2. Worked laboratory thought experiment

Compare schematic oxidation free energies for two metals and identify which oxide is more stable at one temperature under standard oxygen activity. Then vary oxygen partial pressure and note the shifted reaction potential.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Equilibrium Nernst potential**. Set **Dimensionless reaction quotient** to **45.0055 ratio**; all other model parameters remain at the reference values stated below. The output is **1.051122 V**. State the model assumptions explicitly: Two-electron balanced cell; T=298 K, E°=1.10 V, ideal activities. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **57.0043 ratio** to obtain **1.048087 V**; the reported output falls as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Ellingham comparisons do not account for heat transport, reaction fronts, slag chemistry, passivating scales or impurity-driven phases; manufacturing feasibility needs broader evidence.

Compare two interpretations of the imagined observations. Interpretation A uses **ellingham-style oxide stability** as its leading explanation. Interpretation B attributes some of the same signal to **polarization and interfacial overpotential**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** What changes when the oxidizing atmosphere is not at the chosen standard oxygen pressure? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **1.051122 V** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Ellingham comparisons do not account for heat transport, reaction fronts, slag chemistry, passivating scales or impurity-driven phases; manufacturing feasibility needs broader evidence.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 7.3: Electrochemical potential and Nernst relation

### 1. Physical idea and what is actually specified

In charged systems, electrochemical potential adds an electric-potential contribution to chemical potential. For a specified electrochemical cell reaction, the ideal Nernst relation E=E°−(RT/nF)lnQ connects equilibrium voltage with reaction activities. Here n is electrons per balanced reaction.

### 2. Worked laboratory thought experiment

Change a model reaction quotient by two orders of magnitude and quantify the ideal voltage shift at room temperature. Explain why a measured cell voltage under significant current includes overpotential and ohmic drop.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Equilibrium-reaction constant**. Set **Temperature** to **944 K**; all other model parameters remain at the reference values stated below. The output is **3.099918 dimensionless**. State the model assumptions explicitly: ΔG°=10 kJ/mol−0.020 kJ/(mol K)·T; activities dimensionless. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **1040 K** to obtain **3.486792 dimensionless**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A Nernst voltage does not specify rate capability, degradation, energy density or safety. Concentrated electrolytes need activities rather than uncorrected concentrations.

Compare two interpretations of the imagined observations. Interpretation A uses **electrochemical potential and nernst relation** as its leading explanation. Interpretation B attributes some of the same signal to **surface-driven or defect-driven energy**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which rest condition allows a measured voltage to approach the equilibrium prediction? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **3.099918 dimensionless** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A Nernst voltage does not specify rate capability, degradation, energy density or safety. Concentrated electrolytes need activities rather than uncorrected concentrations.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 7.4: Thermal processing and calorimetric signals

### 1. Physical idea and what is actually specified

DSC and DTA record thermal responses as a programmed temperature changes, while thermogravimetry tracks mass evolution. Interpreting a heat-flow peak requires baseline corrections, scan rate, sample mass and reference behavior. A reaction enthalpy per mole is not read directly from peak height.

### 2. Worked laboratory thought experiment

Design heating and cooling scans for an alloy suspected of undergoing precipitation. Compare onset, peak position, integrated heat and reheating behavior, and use isothermal holds to test if a peak is kinetically delayed.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Equilibrium Nernst potential**. Set **Dimensionless reaction quotient** to **22.0078 ratio**; all other model parameters remain at the reference values stated below. The output is **1.060307 V**. State the model assumptions explicitly: Two-electron balanced cell; T=298 K, E°=1.10 V, ideal activities. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **34.0066 ratio** to obtain **1.05472 V**; the reported output falls as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

An observed calorimetry peak may combine multiple reactions. Heating rate shifts a kinetic onset and can distort what might otherwise look like an equilibrium transition.

Compare two interpretations of the imagined observations. Interpretation A uses **thermal processing and calorimetric signals** as its leading explanation. Interpretation B attributes some of the same signal to **an unmodeled competing phase**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** What measurement distinguishes a mass-loss oxidation process from a reversible solid-state phase change? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **1.060307 V** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **An observed calorimetry peak may combine multiple reactions. Heating rate shifts a kinetic onset and can distort what might otherwise look like an equilibrium transition.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 7.5: Open systems, corrosion and environmental constraints

### 1. Physical idea and what is actually specified

An operating material can exchange oxygen, hydrogen, moisture and heat with its environment. Corrosion and oxidation are coupled problems in chemical potentials, transport, electronic structure and interfacial chemistry. Equilibrium maps identify possible stable phases or potentials, not service lifetimes.

### 2. Worked laboratory thought experiment

Compare stainless alloy exposure to dry air and chloride solution. List which species reservoirs, ionic activities, pH and electrochemical potential must be defined before using a stability diagram.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Equilibrium-reaction constant**. Set **Temperature** to **760 K**; all other model parameters remain at the reference values stated below. The output is **2.277131 dimensionless**. State the model assumptions explicitly: ΔG°=10 kJ/mol−0.020 kJ/(mol K)·T; activities dimensionless. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **856 K** to obtain **2.719359 dimensionless**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Thermodynamically stable passivation can break down locally, while some unstable interfaces persist kinetically. Safety claims require empirical performance testing and standards.

Compare two interpretations of the imagined observations. Interpretation A uses **open systems, corrosion and environmental constraints** as its leading explanation. Interpretation B attributes some of the same signal to **an invalid reference volume or stress**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which field observation could falsify a thermodynamic corrosion prediction without falsifying the underlying Gibbs minimization? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **2.277131 dimensionless** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Thermodynamically stable passivation can break down locally, while some unstable interfaces persist kinetically. Safety claims require empirical performance testing and standards.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Integrated unit project — Thermochemical battery-screening memo

### Research situation and falsifiable objective

A team wants to choose between two hypothetical electrode chemistries solely by comparing ideal Nernst voltages. One candidate has apparently high voltage but rapid degradation in a trial cell. The thermochemical tables use different reaction conventions.



### Analysis plan and mathematical constraints

Balance each redox reaction, align activity definitions and compute ΔrG=−nFE for its defined cell reaction. Sweep the reaction quotient over a modest range at fixed temperature. Separate equilibrium voltage and useful energy from deliverable current, cycle life and packaging mass.



### Experimental discriminators

Collect open-circuit voltage after relaxation, impedance, cycling results and actual phase characterization. Disagreement between voltages may indicate nonideal activity or unwanted reactions, not an invalid Nernst equation.



### Limitations and responsible reporting

Safety and performance cannot be inferred from the sign of free energy. A design decision requires abuse testing and materials qualification outside these educational models.



### Project deliverables and assessment rubric





### Interactive demonstrations for this unit

<!-- MODEL_12 -->

<!-- MODEL_13 -->

