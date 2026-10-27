# Unit 2: Electronic and Atomistic Methods

**Guiding question:** When do electronic and atomistic approximations predict real material trends?

## Problem framing and scale selection

Two predicted coatings have close cohesive energies but only one resists cracking. Differentiate energy-minimization assumptions, finite-temperature disorder, interatomic-potential scope, electronic-structure approximations and interface failure. No materials simulation is interpretable until its target observable, reference material state, environmental range and intended downstream decision are fixed. Distinguish a calculated ideal crystal from an actual manufactured material, a numerical fit from independent validation, and a candidate ranking from an authorized design decision. A model should be evaluated by whether it rules out alternatives or informs an observable experiment, not by the complexity of its software or resolution of its graphics.

The unit's evidence record starts with **atomic structure and electronic parameter provenance**. Collect **lattice, composition, potential/functional, electronic convergence and temperature/sampling** and prioritize tests such as **potential validation, convergence across cells and independently measured structure/property trends**. The most dangerous untested assumption is **whether the method handles unseen bonding, charges, defects or long time scales**. Work backward from that possible failure: identify at least two competing explanations, a calculation that could distinguish them, an independently measurable outcome and a decision threshold. Be explicit if available observations cannot constrain the model. The five lessons progressively build a defensible case record.

## Unit field notebook — initial protocol

State a material formulation, one measurable target property, units, intended temperature/time/composition limits, specimen or simulated domain, governing hypotheses and error tolerance. Record a reference model with minimal complexity; describe where added atomistic, mesoscale, continuum or statistical detail would be necessary. List input uncertainty sources, computational convergence tests, independent measurement plans, future update conditions and rejection criteria. At the end of the unit, turn the notebook into a one-page auditable model-use statement.

## Lesson 2.1 — Crystals, symmetry and periodic supercells

### Concept, governing relationships and physical intuition

A crystal is described by a basis and lattice translations. Periodic boundary conditions replace a bulk region with a repeating cell, which omits free surfaces and may couple defects to their periodic images. Atomic coordinates alone are insufficient without lattice vectors, species, occupancies and temperature. Symmetry reduces calculations only when it is truly preserved by the state under study.

**Modeling rule:** The supercell approximates an infinite periodic medium; finite-size corrections depend on defect and electrostatics. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A vacancy formation energy changes markedly when the calculation cell doubles in size. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Periodic images can distort strain fields and charged-defect energetics. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Harmonic pair energy relative to minimum** with mathematical expression `0.5*40*Math.pow(r-2,2)`. Its adjustable input is **Atom separation**, measured in Å; output is reported in eV. At an illustrative input of 1.76 Å, the displayed result is **1.152 eV**. A second invented input of 2.18 Å gives **0.648 eV**. The finite-difference response is -1.2 eV per Å. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** One invented pair with equilibrium distance 2 Å and curvature 40 eV/Å²; does not represent a calibrated crystal potential, phase diagram, or real atomic pair. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Refine cell size and sampling consistently, report symmetry, and inspect relaxed local bonding. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Larger cells represent defects better but increase electronic and sampling costs. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “The supercell approximates an infinite periodic medium; finite-size corrections depend on defect and electrostatics.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `0.5*40*Math.pow(r-2,2)`, independently derive 1.152 eV for 1.76 Å and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A vacancy formation energy changes markedly when the calculation cell doubles in size.”, design the smallest credible cross-check using **Refine cell size and sampling consistently, report symmetry, and inspect relaxed local bonding.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_2 -->

## Lesson 2.3 — Electronic-structure methods and energy comparisons

### Concept, governing relationships and physical intuition

Density-functional theory is a framework for ground-state electronic calculations using an approximate exchange-correlation functional in practical implementations. Plane-wave cutoff, Brillouin-zone sampling, pseudopotentials, spin state and structural relaxation affect total energies. Small energy differences often compete with methodological errors; use comparable references and convergence settings across candidate structures.

**Modeling rule:** Formation energy subtracts reference constituent energies from the calculated compound energy. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** Two polymorphs differ by only a few meV per atom in nominal calculated energy. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Computed zero-kelvin total energies do not directly include full finite-temperature stability and kinetic effects. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Harmonic pair energy relative to minimum** with mathematical expression `0.5*40*Math.pow(r-2,2)`. Its adjustable input is **Atom separation**, measured in Å; output is reported in eV. At an illustrative input of 1.83 Å, the displayed result is **0.578 eV**. A second invented input of 2.23 Å gives **1.058 eV**. The finite-difference response is 1.2 eV per Å. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** One invented pair with equilibrium distance 2 Å and curvature 40 eV/Å²; does not represent a calibrated crystal potential, phase diagram, or real atomic pair. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Converge k-point meshes, basis cutoffs, spin configurations and relaxation criteria for the energy difference itself. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Highly converged electronic calculations improve internal accuracy but may not fix functional bias. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Formation energy subtracts reference constituent energies from the calculated compound energy.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `0.5*40*Math.pow(r-2,2)`, independently derive 0.578 eV for 1.83 Å and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “Two polymorphs differ by only a few meV per atom in nominal calculated energy.”, design the smallest credible cross-check using **Converge k-point meshes, basis cutoffs, spin configurations and relaxation criteria for the energy difference itself.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_3 -->

## Lesson 2.5 — Vibrational modes, temperature and defects

### Concept, governing relationships and physical intuition

Phonons describe harmonic vibrational excitations of a stable reference structure and help analyze vibrational free energy, heat capacity and instability. Defects add local modes and scattering. Harmonic or quasiharmonic approximations can fail at large anharmonicity, phase changes, strong disorder and non-equilibrium transport. Different observables demand different approximations.

**Modeling rule:** Stable harmonic modes have nonnegative squared frequencies for a genuine local energy minimum. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** An unstable phonon branch disappears only after forcing a high-symmetry unit cell. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Numerical convergence artifacts and genuine structural instabilities can look similar. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Harmonic pair energy relative to minimum** with mathematical expression `0.5*40*Math.pow(r-2,2)`. Its adjustable input is **Atom separation**, measured in Å; output is reported in eV. At an illustrative input of 1.9 Å, the displayed result is **0.2 eV**. A second invented input of 2.28 Å gives **1.568 eV**. The finite-difference response is 3.6 eV per Å. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** One invented pair with equilibrium distance 2 Å and curvature 40 eV/Å²; does not represent a calibrated crystal potential, phase diagram, or real atomic pair. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Inspect force-constant convergence, acoustic sum rules, alternative structures and temperature-sensitive measurements. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Simple harmonic calculations are efficient but may miss thermal expansion and phase transition physics. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Stable harmonic modes have nonnegative squared frequencies for a genuine local energy minimum.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `0.5*40*Math.pow(r-2,2)`, independently derive 0.2 eV for 1.9 Å and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “An unstable phonon branch disappears only after forcing a high-symmetry unit cell.”, design the smallest credible cross-check using **Inspect force-constant convergence, acoustic sum rules, alternative structures and temperature-sensitive measurements.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

## Unit 2 capstone: integrate calculations with evidence

**Practical challenge:** Two predicted coatings have close cohesive energies but only one resists cracking. Differentiate energy-minimization assumptions, finite-temperature disorder, interatomic-potential scope, electronic-structure approximations and interface failure.

1. **Define material state and performance.** State composition, phase/microstructure, processing history, external constraints, independent material specimens and the exact observable to be predicted. State the intended decision and penalty of a wrong choice.
2. **Reproduce quantitative work.** Run both synthetic interactive formulas at three inputs, independently recompute the results, and identify the nonphysical or unmeasured assumptions. Develop one additional first-principles or measured-model benchmark that would test the physics rather than just the code.
3. **Test alternative explanations.** Use **atomic structure and electronic parameter provenance**, explicitly log **lattice, composition, potential/functional, electronic convergence and temperature/sampling**, and challenge the model with **potential validation, convergence across cells and independently measured structure/property trends**. Describe an observation that would falsify the preferred hypothesis. Separate calibration, validation and engineering qualification evidence.
4. **Quantify uncertainty and feasibility.** Include one numerical convergence test, one physical or statistical uncertainty propagation, one out-of-domain stress test, one materials supply or production constraint and a feasible low-cost validation plan.
5. **Deliver an auditable recommendation.** Produce a two-page technical decision, reproducibility checklist, complete candidate table and stop/go rule. Explicitly revisit **whether the method handles unseen bonding, charges, defects or long time scales**. No synthetic formula output authorizes use of a safety-critical material or device.

### Concluding reflection

A physical model earns trust by surviving attempts to falsify its assumptions within a defined application, not by producing a large dataset or intricate graphics. Distinguish numerical convergence, agreement on fitted points, generalization to new material states and functional qualification of real parts. If any step remains missing, state which research question is answerable and which engineering recommendation must be deferred.

