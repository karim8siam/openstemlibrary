# Unit 3: Polymerization chemistry and reaction engineering

**Guiding question:** How do reaction pathways and conversion determine composition, chain length and process safety?

## Why this unit matters to polymer science

A bench reaction gave the targeted molar mass, but a larger batch has unexpected viscosity increase and strong exotherm. This is a question about **chain growth and conversion** and the distinction between **functional-group conversion versus processability and thermal control**. A defensible answer identifies chain chemistry, molecular distribution, processing path and morphology before comparing measured properties. It also names the potentially controlling failure mode: a formulation that optimizes short-term stiffness, melt-flow index or optical clarity can still worsen creep resistance, process stability, environmental cracking or barrier lifetime. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Reaction chemistry and transport interact through heat release, conversion, solvent removal and molecular mobility. A useful laboratory conversion does not guarantee scalable safe heat removal.

Treat initiator concentration and conversion sliders as hypothetical kinetic sensitivity tools only; never select a reactor temperature or charge mass from them.

## Measurement and conservation checkpoints

Write down the starting chain chemistry, distribution, additive package and processing history; define whether reported fractions are by area, mass, moles or volume; and record the process history that could alter **stoichiometric ratio, inhibitor residues and heat removal**. For any local observation, describe why its sampling plan represents the part. Treat **unmeasured exotherm, chain transfer or cyclization** as an explicit rival explanation and plan **reaction calorimetry and compositional/molar-mass tracking** as an independent check.

## Lesson 3.1: Step-growth conversion and stoichiometry

### Scientific foundation

Step-growth polymerization allows any compatible functional species to react, and high average chain length requires very high functional-group conversion when all reactants are bifunctional and balanced. For an ideal equal-reactivity linear case, the Carothers relation is DPn=1/(1−p). A small conversion error near completion dramatically changes predicted DPn. Any stoichiometric offset limits maximum degree of polymerization even at complete consumption of limiting groups. Water removal can be required when the reaction is condensation-based.

**Governing relationship or decision rule:** Balanced ideal step growth: DPn=1/(1−p); with A/B imbalance r≤1, DPn=(1+r)/(1+r−2rp). Read every term in the equation as part of a declared specimen condition. In **step-growth conversion and stoichiometry**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Compute ideal DPn for p=0.90, 0.99, and 0.999: 10, 100, and 1000. Then examine 1% A/B imbalance with DPn=(1+r)/(1+r−2rp). Identify whether conversion measurement is accurate enough to distinguish 100 from 200 chains. Plan an FTIR or end-group titration cross-check.

A companion calculator called **Ideal balanced step-growth DPn** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Functional-group conversion = 0.8712857 fraction**, the declared formula returns **7.7691454 repeat units**; at **Functional-group conversion = 0.8925714 fraction**, it returns **9.3085106 repeat units**. On this interval the modeled value increases, and the two-point slope is **72.319173 repeat units per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

The browser expression is `1/(1-p)`. Model validity is limited to: **Ideal bifunctional, stoichiometrically balanced equal-reactivity step growth with no cycles or side reactions**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Monofunctional impurities, cyclization, side reactions and unequal reactivity violate the ideal relation. A very large numerical DPn is not evidence that the melt can be processed without degradation.

### Exercises and self-assessment

**Exercise 3.1A — Physical mechanism.** Why does '99% reaction complete' still permit substantially different end-use viscosities for two formulations? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.1B — Numerical cross-check.** Recalculate **7.7691454 repeat units** from the companion formula at **0.8712857 fraction** and compare with **9.3085106 repeat units** at **0.8925714 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 3.1C — Test design.** Propose a synthesis, processing or test matrix that addresses **unmeasured exotherm, chain transfer or cyclization**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_4 -->

## Lesson 3.2: Free-radical chain-growth kinetics

### Scientific foundation

Radical polymerization proceeds by initiation, propagation and termination. Under steady-state radical concentration, propagation rate scales with monomer concentration and approximately the square root of effective initiator source, assuming bimolecular termination and no strong diffusion limitation. Initiator efficiency, chain transfer and autoacceleration complicate actual rates. Heating can accelerate initiator decomposition and reaction simultaneously, requiring careful heat-removal design in bulk systems.

**Governing relationship or decision rule:** With d[R•]/dt≈0 and effective radical loss rate kt[R•]², Rp=kp[M]sqrt(2fkd[I]/kt); clarify kt convention before comparing literature. Read every term in the equation as part of a declared specimen condition. In **free-radical chain-growth kinetics**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

For a hypothetical batch with kp=100 L mol−1 s−1, kd=1e−5 s−1, efficiency f=0.6, termination constant kt=1e7 L mol−1 s−1 and [M]=2 mol/L, calculate Rp as initiator concentration varies from 0.001 to 0.1 mol/L. Identify the square-root dependence and the corresponding limits for heat generation.

A companion calculator called **Steady-state radical propagation rate** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Initiator concentration = 0.02928571 mol/L**, the declared formula returns **3.7492856e-05 mol/(L s)**; at **Initiator concentration = 0.04342857 mol/L**, it returns **4.5657107e-05 mol/(L s)**. On this interval the modeled value increases, and the two-point slope is **0.00057727025 mol/(L s) per mol/L**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

The browser expression is `100*2*Math.sqrt(2*0.6*1e-5*I/1e7)`. Model validity is limited to: **Hypothetical kp=100 L/(mol s), [M]=2 mol/L, f=0.6, kd=1e-5 s⁻¹, kt=1e7 L/(mol s) defined for effective radical disappearance kt[R•]²; steady state, isothermal, no gel effect**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

The steady-state expression fails if radical reactions become diffusion-controlled, inhibitor concentrations change or heat release overwhelms cooling. These are teaching values, not process recipes.

### Exercises and self-assessment

**Exercise 3.2A — Physical mechanism.** Why can viscosity and temperature rise sharply late in a radical polymerization despite declining monomer concentration? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.2B — Numerical cross-check.** Recalculate **3.7492856e-05 mol/(L s)** from the companion formula at **0.02928571 mol/L** and compare with **4.5657107e-05 mol/(L s)** at **0.04342857 mol/L**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 3.2C — Test design.** Propose a synthesis, processing or test matrix that addresses **unmeasured exotherm, chain transfer or cyclization**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_5 -->

## Lesson 3.3: Copolymer composition and sequence drift

### Scientific foundation

Comonomers may have different propensities to add to each terminal radical, so instantaneous copolymer composition often differs from the initial feed ratio. Reactivity ratios r1 and r2 summarize terminal-model preferences but require reliable reactivity measurements. During batch conversion the feed composition may drift, causing gradients among chains; apparent average composition can therefore conceal a broad sequence distribution. Sequence placement matters for Tg, hydrolysis susceptibility and crystallization.

**Governing relationship or decision rule:** The Mayo–Lewis terminal equation predicts instantaneous copolymer mole fractions from monomer feed fraction and two measured reactivity ratios. Read every term in the equation as part of a declared specimen condition. In **copolymer composition and sequence drift**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Plan a low-conversion copolymerization matrix over several feed fractions, determine instantaneous polymer composition by NMR, then estimate reactivity ratios with explicit uncertainty. Explain why observing total batch composition at near-full conversion does not reveal whether individual chains were compositionally uniform. Compare a sequential feed with a fixed-ratio semibatch strategy conceptually.

A companion calculator called **Ideal balanced step-growth DPn** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Functional-group conversion = 0.9138571 fraction**, the declared formula returns **11.608624 repeat units**; at **Functional-group conversion = 0.9351429 fraction**, it returns **15.418502 repeat units**. On this interval the modeled value increases, and the two-point slope is **178.98759 repeat units per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Terminal-model predictions can fail for penultimate-unit effects, phase partitioning and heterogeneous processes. Calorimetry alone does not measure copolymer sequences.

### Exercises and self-assessment

**Exercise 3.3A — Physical mechanism.** What observation would reveal composition drift when final bulk elemental composition appears correct? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.3B — Numerical cross-check.** Recalculate **11.608624 repeat units** from the companion formula at **0.9138571 fraction** and compare with **15.418502 repeat units** at **0.9351429 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 3.3C — Test design.** Propose a synthesis, processing or test matrix that addresses **unmeasured exotherm, chain transfer or cyclization**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_4 -->

## Lesson 3.4: Network gelation and branching reactions

### Scientific foundation

Introducing three-functional or higher monomers can produce a branching network. A gel point marks appearance of a system-spanning connected structure under suitable idealized conditions, not necessarily full chemical conversion or optimum mechanical toughness. Before gelation, viscosity may rise steeply; after gelation, soluble molecules and unreacted functional groups may remain. Gel fraction and swelling are different measurements with different sensitivities.

**Governing relationship or decision rule:** Network connectivity requires a branching process; functional conversion, gel fraction and network modulus are distinct observables. Read every term in the equation as part of a declared specimen condition. In **network gelation and branching reactions**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Design a conversion sweep through the onset of insoluble fraction for a hypothetical multifunctional polyester or epoxy. Record oscillatory rheology, extraction mass balance and spectroscopic conversion. Distinguish the first elastic spanning network from final cure. Report instrument geometry and temperature to avoid confusing wall slip with apparent gelation.

A companion calculator called **Steady-state radical propagation rate** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Initiator concentration = 0.05757143 mol/L**, the declared formula returns **5.2568323e-05 mol/(L s)**; at **Initiator concentration = 0.07171429 mol/L**, it returns **5.8670996e-05 mol/(L s)**. On this interval the modeled value increases, and the two-point slope is **0.0004315021 mol/(L s) per mol/L**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Ideal Flory–Stockmayer thresholds presume random functionality, reactivity and absent loops; intramolecular cyclization and vitrification can alter the observed gel point.

### Exercises and self-assessment

**Exercise 3.4A — Physical mechanism.** Why does a high gel fraction not prove that an epoxy network is fully cured or has high fracture resistance? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.4B — Numerical cross-check.** Recalculate **5.2568323e-05 mol/(L s)** from the companion formula at **0.05757143 mol/L** and compare with **5.8670996e-05 mol/(L s)** at **0.07171429 mol/L**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 3.4C — Test design.** Propose a synthesis, processing or test matrix that addresses **unmeasured exotherm, chain transfer or cyclization**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_5 -->

## Lesson 3.5: Controlled polymerization and chain-end fidelity

### Scientific foundation

Reversible-deactivation radical processes and controlled ring-opening methods can make chain growth more predictable than uncontrolled radical polymerization, but 'living' should not be claimed without tests for irreversible termination and chain transfer. A narrow molar-mass distribution does not guarantee sequence fidelity or absence of residual catalysts. Sequential monomer additions may form designed blocks only if sufficient chains retain active or reactivatable ends.

**Governing relationship or decision rule:** Chain-extension success depends on retained reactive ends and kinetics; measured Mn versus conversion and distribution shape test, but do not alone prove, control. Read every term in the equation as part of a declared specimen condition. In **controlled polymerization and chain-end fidelity**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Compare SEC distributions after successive monomer feeds for a hypothetical block synthesis and perform end-group analysis or chain extension as stronger evidence. Evaluate whether all chains shift together or a low-mass population persists. Document dispersity changes without assuming the reaction is perfectly living because a single chromatogram narrows.

A companion calculator called **Ideal balanced step-growth DPn** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Functional-group conversion = 0.9564286 fraction**, the declared formula returns **22.95082 repeat units**; at **Functional-group conversion = 0.9777143 fraction**, it returns **44.871795 repeat units**. On this interval the modeled value increases, and the two-point slope is **1029.8445 repeat units per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Oxygen exposure, transfer, initiation delay and trace water can destroy end-group fidelity; fluorescence tags may perturb behavior. The rate slider shown in the unit models illustrates basic radical kinetics only, not living-polymerization control.

### Exercises and self-assessment

**Exercise 3.5A — Physical mechanism.** Which experiment distinguishes high monomer conversion from high fraction of chains able to grow another block? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.5B — Numerical cross-check.** Recalculate **22.95082 repeat units** from the companion formula at **0.9564286 fraction** and compare with **44.871795 repeat units** at **0.9777143 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 3.5C — Test design.** Propose a synthesis, processing or test matrix that addresses **unmeasured exotherm, chain transfer or cyclization**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_4 -->

## Integrated investigation: Scaling up polymer synthesis

### The evidence problem

A bench reaction gave the targeted molar mass, but a larger batch has unexpected viscosity increase and strong exotherm. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which polymerization route or formulated resin seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Create kinetic, stoichiometric and heat-transfer ledgers. Compare monomer conversion with reaction temperature and molecular distribution. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **chain growth and conversion** and **functional-group conversion versus processability and thermal control** through the map. For polymer mixing, show composition conservation and do not infer processing kinetics from a static phase diagram. For a melt-state relation, distinguish relaxation time from shear-rate-dependent flow and actual process heating. For chemical function, distinguish molecular diffusion, partitioning, chain mobility and chemical degradation. Use the actual specimen time–temperature history instead of only a machine-temperature set point. For damage, compare local flaw driving force with rate- and environment-dependent measured fracture resistance.

### Validation plan, report, and counterfactual

Measure heat release and heat-removal capacity with qualified reaction calorimetry, sample molecular distributions, and evaluate a safer processing design. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing polymer families, write down the constraints that matter for stiffness, creep, permeability, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** Educational rate equations are not safe operating procedures for hazardous polymerization. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **chain growth and conversion** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **functional-group conversion versus processability and thermal control** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **unmeasured exotherm, chain transfer or cyclization** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_5 -->

