# Unit 4: Solution thermodynamics and mixing

**Guiding question:** When do mixing entropy and interactions stabilize one phase or favor phase separation?

## Unit overview and conceptual map

The entropy gain from mixing has an especially simple ideal form, but the phase diagram is decided by total free energy. A positive interaction energy can counter the favorable entropy term at low temperature; increasing temperature enhances the entropy contribution and can stabilize a random mixture. The symmetric regular solution is valuable because its critical-temperature estimate can be derived analytically. It is not a universal alloy model; compound formation, magnetic transitions and multiple crystallographic sublattices can reshape the landscape.

Coexistence compositions are obtained from equality of chemical potentials, not by eye from local curvature alone. The common-tangent construction compares a heterogeneous mixture against a homogeneous state with the same overall composition. For intermediate bulk compositions, a tie-line mass balance controls the fraction of each phase. This illustrates a recurring rule: equilibrium phase composition and phase fraction are different pieces of information. A microscopy map may measure the former after careful calibration, but converting its pixel areas into mole fractions requires density and sampling assumptions.



## Lesson 4.1: Configurational mixing entropy

### 1. Physical idea and what is actually specified

For a random binary ideal solution, ΔSmix=−R[x ln x+(1−x)ln(1−x)]. It is positive for intermediate compositions and zero for pure components. The formula counts configurations under ideal lattice assumptions; ordered structures and correlated site occupations need different entropy models.

### 2. Worked laboratory thought experiment

Use equal and unequal compositions to compute mixing entropy and identify its maximum for the symmetric ideal binary model. Explain why an alloy with two distinct sublattices cannot necessarily be represented by one unconstrained random-site fraction.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Ideal binary mixing free energy**. Set **Mole fraction B** to **0.2312 fraction**; all other model parameters remain at the reference values stated below. The output is **-3.596652 kJ/mol**. State the model assumptions explicitly: Ideal random binary solution at 800 K. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.3464 fraction** to obtain **-4.291524 kJ/mol**; the reported output falls as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

An increased configurational entropy does not guarantee a homogeneous solid solution when enthalpy favors separation or multiple crystal structures compete. Temperature determines the weight TΔS.

Compare two interpretations of the imagined observations. Interpretation A uses **configurational mixing entropy** as its leading explanation. Interpretation B attributes some of the same signal to **trapped metastability or undercooling**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which feature of a calorimetry curve could contradict a purely ideal-mixing picture? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **-3.596652 kJ/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **An increased configurational entropy does not guarantee a homogeneous solid solution when enthalpy favors separation or multiple crystal structures compete. Temperature determines the weight TΔS.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 4.2: Regular-solution free energy

### 1. Physical idea and what is actually specified

The symmetric regular solution adds Ωx(1−x) to the ideal free energy of mixing. Positive Ω penalizes unlike neighbors and can produce demixing below a critical temperature Tc=Ω/(2R) in the simplest mean-field treatment. Negative Ω instead encourages mixing but may signal ordering requiring richer models.

### 2. Worked laboratory thought experiment

Take an illustrative Ω=16 kJ/mol. Calculate Tc and compare a curve at 700 K with one at 1200 K. On each curve, identify whether the midpoint is locally stable by evaluating the second derivative.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Symmetric regular-solution mixing free energy**. Set **Mole fraction B** to **0.452 fraction**; all other model parameters remain at the reference values stated below. The output is **-0.04420595 kJ/mol**. State the model assumptions explicitly: 700 K, Ω=16,000 J/mol; mean-field random mixing. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.5672 fraction** to obtain **-0.05373096 kJ/mol**; the reported output falls as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

The regular solution assumes a temperature-independent interaction parameter and random mixing. Real alloys have magnetic, vibrational and structural free-energy contributions, often changing with temperature.

Compare two interpretations of the imagined observations. Interpretation A uses **regular-solution free energy** as its leading explanation. Interpretation B attributes some of the same signal to **a phase misidentification or microsegregation**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** How would you distinguish an asymmetric measured miscibility gap from limitations of the symmetric Ω model? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **-0.04420595 kJ/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **The regular solution assumes a temperature-independent interaction parameter and random mixing. Real alloys have magnetic, vibrational and structural free-energy contributions, often changing with temperature.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 4.3: Common tangent and coexistence compositions

### 1. Physical idea and what is actually specified

At fixed T,P, phase coexistence in a binary system follows equality of the two component chemical potentials; geometrically, this is expressed by a common tangent to the molar Gibbs-energy curve. The two tangent points identify compositions, not arbitrary endpoints of a visually flat region.

### 2. Worked laboratory thought experiment

Sketch the tangent joining two minima on a hypothetical free-energy curve. Use a tie line to explain why the overall alloy composition changes phase amounts but not the coexistence compositions for a fixed pair of phases at the same T,P.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Ideal binary mixing free energy**. Set **Mole fraction B** to **0.6728 fraction**; all other model parameters remain at the reference values stated below. The output is **-4.204976 kJ/mol**. State the model assumptions explicitly: Ideal random binary solution at 800 K. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.788 fraction** to obtain **-3.436164 kJ/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

A curve can have a negative-curvature spinodal region smaller than the two-phase binodal range. Numerical differentiation amplifies noisy free-energy fits and may create false tangents.

Compare two interpretations of the imagined observations. Interpretation A uses **common tangent and coexistence compositions** as its leading explanation. Interpretation B attributes some of the same signal to **polarization and interfacial overpotential**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** What is wrong with reading the miscibility gap directly from the points where curvature becomes negative? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **-4.204976 kJ/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **A curve can have a negative-curvature spinodal region smaller than the two-phase binodal range. Numerical differentiation amplifies noisy free-energy fits and may create false tangents.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 4.4: Ordered compounds and sublattice models

### 1. Physical idea and what is actually specified

Intermetallic ordering changes allowed occupancies of crystallographically distinct sites, so the configurational entropy is often modeled with explicit sublattices. CALPHAD assessments may represent compounds through endmember Gibbs energies and interaction terms. A nominal AB composition does not imply zero constitutional defects.

### 2. Worked laboratory thought experiment

Consider A3B with one minority sublattice and one majority sublattice. List which antisite defects can vary composition while preserving a parent structure, then state what diffraction and calorimetry each constrain.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Symmetric regular-solution mixing free energy**. Set **Mole fraction B** to **0.2312 fraction**; all other model parameters remain at the reference values stated below. The output is **-0.3031255 kJ/mol**. State the model assumptions explicitly: 700 K, Ω=16,000 J/mol; mean-field random mixing. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.3464 fraction** to obtain **-0.1325705 kJ/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

Treating an ordered phase as a single ideal mixing lattice can predict excessive disorder entropy. A good fit to a narrow dataset may still extrapolate poorly to higher temperatures or off-stoichiometric compositions.

Compare two interpretations of the imagined observations. Interpretation A uses **ordered compounds and sublattice models** as its leading explanation. Interpretation B attributes some of the same signal to **surface-driven or defect-driven energy**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** Which measurement would directly constrain sublattice occupancy rather than bulk composition alone? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **-0.3031255 kJ/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **Treating an ordered phase as a single ideal mixing lattice can predict excessive disorder entropy. A good fit to a narrow dataset may still extrapolate poorly to higher temperatures or off-stoichiometric compositions.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Lesson 4.5: Multicomponent and high-entropy alloys

### 1. Physical idea and what is actually specified

For ideal random substitution on one sublattice, the configurational entropy extends to −RΣxi ln xi. Equiatomic multicomponent mixtures can have large ideal entropy, but this is one contribution to phase stability. Enthalpy, competing compounds, vibrational and magnetic terms matter, as do accessible processing paths.

### 2. Worked laboratory thought experiment

Compare the entropy of equiatomic two-, four- and five-component ideal solutions at the same T. Identify the entropy gain from adding species and discuss why it does not automatically eliminate sigma, B2 or Laves phases.

For a reproducible calculation, connect this lesson to the unit’s companion expression **Ideal binary mixing free energy**. Set **Mole fraction B** to **0.452 fraction**; all other model parameters remain at the reference values stated below. The output is **-4.579819 kJ/mol**. State the model assumptions explicitly: Ideal random binary solution at 800 K. This value is calculated using a mathematical teaching model and is **not** a result measured for the imagined specimen. Recalculate at **0.5672 fraction** to obtain **-4.55026 kJ/mol**; the reported output rises as the chosen input increases. Explain that tendency from the algebra before interpreting its physical significance.



### 3. Competing explanation and scope

The label high-entropy alloy is not a phase-equilibrium certificate. Database quality for complex compositions may be poorer than for common binaries; uncertainties can be large.

Compare two interpretations of the imagined observations. Interpretation A uses **multicomponent and high-entropy alloys** as its leading explanation. Interpretation B attributes some of the same signal to **an unmodeled competing phase**, a mechanism that may change the measured response without confirming the intended thermodynamic conclusion. The comparison is not rhetorical: A and B should make different predictions for at least one additional measurement. State what would be held constant while conducting that discrimination and identify the sign or shape of the expected difference. If the predictions overlap within reasonable measurement uncertainty, keep the conclusion conditional rather than choosing a preferred story because it seems more familiar.

### 5. Assessment: reasoning, sensitivity and falsification

**Decision problem.** What would you measure to falsify a predicted single-phase region in a multicomponent alloy? Write a short answer that (i) defines the dependent quantity and its units; (ii) specifies the sample or reservoir boundary; (iii) gives the equation and each idealization; (iv) calculates the reference output above, showing intermediate unit conversions; (v) names a rival cause for the same measurement; and (vi) identifies one control whose negative result would undermine the proposed interpretation. For extra credit, predict the result of changing the slider beyond the reference value without calculating it first. Then use the simulation to check your prediction and explain any discrepancy in physical or numerical terms.

**Instructor reasoning guide.** Full credit requires **-4.579819 kJ/mol** to the shown rounding and a statement that the source is synthetic. The conditional interpretation must be consistent with **The label high-entropy alloy is not a phase-equilibrium certificate. Database quality for complex compositions may be poorer than for common binaries; uncertainties can be large.** and may not claim that the illustrative value validates a real material. The best answers identify the limiting observation and propose a measurement that would change the conclusion, not simply repeat that uncertainty exists. A correct numerical result with an incorrect experimental boundary is not a complete solution.

## Integrated unit project — Solubility gap in a binary alloy

### Research situation and falsifiable objective

Synthetic free-energy calculations for a binary A–B alloy show a homogeneous phase at high temperature and a two-minimum landscape at lower temperature. A specimen with overall B fraction 0.40 shows composition contrast after long annealing.



### Analysis plan and mathematical constraints

Calculate the ideal and regular-solution mixing terms on a common molar basis. Solve the stability curvature of the symmetric model, then use common-tangent reasoning to distinguish binodal endpoints from spinodal bounds. Express the composition balance through a tie line.



### Experimental discriminators

Obtain two phase-specific chemical compositions via a calibrated method and compare heat treatments above and below the model critical region. Check whether observed contrast persists in multiple specimens.



### Limitations and responsible reporting

A one-parameter regular solution may miss crystallographic ordering, coherency strain and solute segregation to boundaries. Apparent two-phase contrast does not authenticate the chosen Ω.



### Project deliverables and assessment rubric





### Interactive demonstrations for this unit

<!-- MODEL_6 -->

<!-- MODEL_7 -->

