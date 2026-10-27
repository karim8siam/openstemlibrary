# Unit 4: Scattering, recombination, and minority-carrier dynamics

**Central research question:** Which microscopic mechanisms control how far minority carriers travel before disappearing?

## Material and device context

A carrier may lose momentum many times yet live long enough to traverse a micron-scale region; mobility, recombination lifetime and diffusion length are distinct observables.

Defect identification requires a mechanism-specific signature; changing a decay time following passivation does not establish which atomic defect changed.

**Scope of this unit:** Study **momentum scattering, lifetime and diffusion** while distinguishing **transport mobility versus survival of excess carriers**. Practical interpretation requires **carrier injection, doping, temperature, boundary recombination and D**. An important alternative is **trapping, surface loss, injection-dependent recombination or heating**, which is why **time-resolved photoconductance and thickness-dependent lifetime testing** must be part of a credible validation programme. These topics are inseparable from geometry, scale and specimen history; a nominal textbook material is not a sufficiently specified industrial sample.

## Measurement-first reading checkpoint

## Lesson 4.1: Phonon and impurity scattering

### A physical explanation before any numerical fit

Electron momentum relaxation arises from acoustic and optical phonons, ionized impurities, neutral disorder, interface roughness, and defects. Matthiessen’s rule approximately adds inverse mobilities when independent scattering processes permit it, but correlations and a nontrivial energy distribution can break that approximation. Mobility fitted as T^(−m) over a short interval need not reveal a unique mechanism. Structural and electronic disorder can alter density and mobility simultaneously.

**Primary relationship:** Carrier concentration and relaxation must be analyzed jointly rather than extracting scattering from resistance alone. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **phonon and impurity scattering**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Measure conductivity and Hall coefficient across temperature and compare lightly doped and strongly doped samples. Test whether a rising mobility upon heating implies ionized-impurity scattering or merely freeze-out changing the Hall carrier population.

For a realistic assessment, distinguish directly controlled inputs from inferred ones. In this lesson, the relevant controls include **carrier injection, doping, temperature, boundary recombination and D**; measure each where possible and report the resolution or calibration of the instrument. A model fit that adjusts an unmeasured constant to match one observable does not establish that the associated mechanism is correct. Ask whether **trapping, surface loss, injection-dependent recombination or heating** could produce the same sign of change and what independent feature would differ. If the two proposed mechanisms are observationally indistinguishable under the existing design, the next scientific contribution is a better experiment rather than a more elaborate fit.

### Transparent worked numerical example

The offline calculator **Mobility–diffusivity relation** is deliberately simpler than the phenomenon being discussed. Let **Mobility = 522.22222 cm2/(V s)**. From the implemented expression `mu*8.617333262145e-5*300`, the predicted value is **13.5004888 cm2/s**. Change only the designated control to **733.33333 cm2/(V s)** and the result becomes **18.9581332 cm2/s**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **0.0258519998 (cm2/s)/(cm2/(V s))**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **300 K, nondegenerate equilibrium, Einstein relation D=μkT/q; kT/q numerically 0.025852 V**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

A good power-law fit is not direct evidence for a microscopic scattering channel.

Perform a **instrument de-embedding audit**: Check contact resistance, substrate channels, parasitic capacitance, optical reflection and thermal offsets. Follow with a **statistical independence audit**: Distinguish repeated scans of a single wafer from independent process lots and predeclare rejection criteria. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **momentum scattering, lifetime and diffusion** with a response in **phonon and impurity scattering**. Now suppose instead that the change is controlled by **trapping, surface loss, injection-dependent recombination or heating**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **time-resolved photoconductance and thickness-dependent lifetime testing** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 4.1A — Conceptual mechanism.** Explain in your own words what **phonon and impurity scattering** changes about the relation between **transport mobility versus survival of excess carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 4.1B — Quantitative verification.** Reproduce the values **13.5004888 cm2/s** and **18.9581332 cm2/s** using `mu*8.617333262145e-5*300` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 4.1C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **trapping, surface loss, injection-dependent recombination or heating**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Mobility–diffusivity relation** should not be treated as predictive.

<!-- MODEL_6 -->

## Lesson 4.2: Radiative and nonradiative recombination

### A physical explanation before any numerical fit

Band-to-band radiative recombination competes with Shockley–Read–Hall capture through defects and Auger processes involving a third carrier. An illustrative low-injection total rate may combine linear, quadratic, and cubic carrier-density dependences, but coefficients are material, temperature, and excitation dependent. A shorter photoluminescence lifetime does not automatically mean worse optoelectronic efficiency: transport, extraction, surface loss, and doping can change the measured transient.

**Primary relationship:** Recombination mechanisms should be distinguished through carrier-density and temperature dependence plus calibrated extraction. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **radiative and nonradiative recombination**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

A passivated silicon wafer shows a longer lifetime after a chemical treatment. Use injection-dependent photoconductance and surface-sensitive controls to separate reduced surface recombination from a changed bulk defect population.

### Transparent worked numerical example

The offline calculator **Minority-carrier diffusion length** is deliberately simpler than the phenomenon being discussed. Let **Effective lifetime = 3.3666667 microseconds**. From the implemented expression `10000*Math.sqrt(25*tau*1e-6)`, the predicted value is **91.742393 micrometers**. Change only the designated control to **4.4722222 microseconds** and the result becomes **105.738146 micrometers**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **12.6594753 (micrometers)/(microseconds)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Uniform D=25 cm2/s, τ in microseconds, low-injection homogeneous transport, no surface recombination boundaries**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

Room-temperature steady-state photoluminescence intensity alone cannot determine absolute internal quantum efficiency.

Perform a **statistical independence audit**: Distinguish repeated scans of a single wafer from independent process lots and predeclare rejection criteria. Follow with a **thermodynamic regime audit**: Identify whether equilibrium, degenerate statistics, hot carriers, low injection, or finite-bias gradients alter validity. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **momentum scattering, lifetime and diffusion** with a response in **radiative and nonradiative recombination**. Now suppose instead that the change is controlled by **trapping, surface loss, injection-dependent recombination or heating**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **time-resolved photoconductance and thickness-dependent lifetime testing** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 4.2A — Conceptual mechanism.** Explain in your own words what **radiative and nonradiative recombination** changes about the relation between **transport mobility versus survival of excess carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 4.2B — Quantitative verification.** Reproduce the values **91.742393 micrometers** and **105.738146 micrometers** using `10000*Math.sqrt(25*tau*1e-6)` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 4.2C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **trapping, surface loss, injection-dependent recombination or heating**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Minority-carrier diffusion length** should not be treated as predictive.

## Lesson 4.3: Minority-carrier lifetime and injection level

### A physical explanation before any numerical fit

A characteristic low-injection lifetime τ can describe exponential decay of a small excess carrier population when a single effective loss channel dominates. Under nonuniform generation, surfaces, multiple traps, or large injection, a transient can be multiexponential or even nonexponential. The measured lifetime may be effective rather than intrinsic bulk lifetime. A good experiment states excitation pulse, recombination boundary conditions, probe sensitivity, and the portion of the decay used for fitting.

**Primary relationship:** The single-lifetime teaching model is Δn(t)=Δn0 exp(−t/τ). The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **minority-carrier lifetime and injection level**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Compute remaining excess-carrier percentage 4 µs after an excitation pulse if τ=2 µs. Then compare with a real trace whose slow tail could arise from trapping; determine whether one fitted τ is defensible.

### Transparent worked numerical example

The offline calculator **Mobility–diffusivity relation** is deliberately simpler than the phenomenon being discussed. Let **Mobility = 944.44444 cm2/(V s)**. From the implemented expression `mu*8.617333262145e-5*300`, the predicted value is **24.4157776 cm2/s**. Change only the designated control to **1155.5556 cm2/(V s)** and the result becomes **29.873422 cm2/s**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **0.0258519998 (cm2/s)/(cm2/(V s))**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Trapped-carrier release can create long tails unrelated to mobile-minority-carrier survival.

Perform a **charge neutrality audit**: Verify the sign and physical units of electrons, holes, ionized donors and acceptors; document compensation. Follow with a **instrument de-embedding audit**: Check contact resistance, substrate channels, parasitic capacitance, optical reflection and thermal offsets. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **momentum scattering, lifetime and diffusion** with a response in **minority-carrier lifetime and injection level**. Now suppose instead that the change is controlled by **trapping, surface loss, injection-dependent recombination or heating**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **time-resolved photoconductance and thickness-dependent lifetime testing** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 4.3A — Conceptual mechanism.** Explain in your own words what **minority-carrier lifetime and injection level** changes about the relation between **transport mobility versus survival of excess carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 4.3B — Quantitative verification.** Reproduce the values **24.4157776 cm2/s** and **29.873422 cm2/s** using `mu*8.617333262145e-5*300` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 4.3C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **trapping, surface loss, injection-dependent recombination or heating**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Mobility–diffusivity relation** should not be treated as predictive.

## Lesson 4.4: Diffusion length and collection

### A physical explanation before any numerical fit

Minority-carrier diffusion length L=sqrt(Dτ) estimates the root-mean-square transport scale associated with lifetime in a homogeneous, diffusive, low-injection approximation. A solar-cell base thicker than L may show poor collection for carriers generated far from the junction, but actual collection also depends on built-in field, surfaces, absorption profile, depletion width, and recombination. D and τ must correspond to the same carrier type, temperature, and injection regime.

**Primary relationship:** L(cm)=sqrt[D(cm²/s)τ(s)] and 1 cm=10^4 µm. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **diffusion length and collection**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

For D=25 cm²/s and τ=1 µs, compute L in micrometers. Explore whether passivating the back surface or increasing lifetime is more impactful for a device whose absorber thickness is comparable with L.

### Transparent worked numerical example

The offline calculator **Minority-carrier diffusion length** is deliberately simpler than the phenomenon being discussed. Let **Effective lifetime = 5.5777778 microseconds**. From the implemented expression `10000*Math.sqrt(25*tau*1e-6)`, the predicted value is **118.086597 micrometers**. Change only the designated control to **6.6833333 microseconds** and the result becomes **129.260718 micrometers**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **10.1072453 (micrometers)/(microseconds)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Diffusion length is not equal to ballistic mean free path or full device collection length.

Perform a **thermodynamic regime audit**: Identify whether equilibrium, degenerate statistics, hot carriers, low injection, or finite-bias gradients alter validity. Follow with a **charge neutrality audit**: Verify the sign and physical units of electrons, holes, ionized donors and acceptors; document compensation. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **momentum scattering, lifetime and diffusion** with a response in **diffusion length and collection**. Now suppose instead that the change is controlled by **trapping, surface loss, injection-dependent recombination or heating**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **time-resolved photoconductance and thickness-dependent lifetime testing** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 4.4A — Conceptual mechanism.** Explain in your own words what **diffusion length and collection** changes about the relation between **transport mobility versus survival of excess carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 4.4B — Quantitative verification.** Reproduce the values **118.086597 micrometers** and **129.260718 micrometers** using `10000*Math.sqrt(25*tau*1e-6)` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 4.4C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **trapping, surface loss, injection-dependent recombination or heating**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Minority-carrier diffusion length** should not be treated as predictive.

<!-- MODEL_7 -->

## Lesson 4.5: Surface recombination and passivation

### A physical explanation before any numerical fit

A surface introduces states and band bending that can capture electrons and holes, with an effective surface recombination velocity S entering a flux boundary condition. Chemical passivation reduces electronic defect activity; field-effect passivation repels minority carriers with interface charge. These strategies may produce similar lifetime improvements through different mechanisms. Roughness, native oxide, contamination, and ambient adsorption can change apparent effects.

**Primary relationship:** At a simple surface, minority diffusion flux is coupled to excess concentration through an S-dependent boundary condition. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **surface recombination and passivation**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Compare lifetime data on different wafer thicknesses before and after dielectric deposition; use thickness dependence to test whether the treatment improved surface S or bulk τ. Measure fixed charge and interface states separately.

### Transparent worked numerical example

The offline calculator **Mobility–diffusivity relation** is deliberately simpler than the phenomenon being discussed. Let **Mobility = 1366.6667 cm2/(V s)**. From the implemented expression `mu*8.617333262145e-5*300`, the predicted value is **35.3310664 cm2/s**. Change only the designated control to **1577.7778 cm2/(V s)** and the result becomes **40.7887108 cm2/s**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **0.0258519998 (cm2/s)/(cm2/(V s))**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

A single effective S can conceal spatially varying contamination and injection dependence; reported S is not a pure material constant.

Perform a **geometry and dimensionality audit**: Distinguish three-dimensional volume density from two-dimensional sheet density and separate area from length. Follow with a **geometry and dimensionality audit**: Distinguish three-dimensional volume density from two-dimensional sheet density and separate area from length. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **momentum scattering, lifetime and diffusion** with a response in **surface recombination and passivation**. Now suppose instead that the change is controlled by **trapping, surface loss, injection-dependent recombination or heating**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **time-resolved photoconductance and thickness-dependent lifetime testing** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 4.5A — Conceptual mechanism.** Explain in your own words what **surface recombination and passivation** changes about the relation between **transport mobility versus survival of excess carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 4.5B — Quantitative verification.** Reproduce the values **35.3310664 cm2/s** and **40.7887108 cm2/s** using `mu*8.617333262145e-5*300` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 4.5C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **trapping, surface loss, injection-dependent recombination or heating**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Mobility–diffusivity relation** should not be treated as predictive.

## Integrated case study: Finding the cause of a short lifetime

### Problem statement and evidence hierarchy

After fabrication, a light-emitting wafer exhibits a significantly shorter fitted carrier lifetime. Treat the problem as a comparison of several causes, not a request to select one formula. First write down what was controlled and directly measured; separate that from what is an inference about **momentum scattering, lifetime and diffusion**. Material recipes, deposition logs and temperature setpoints should not be substituted for actual measured carrier concentrations, layer thicknesses, microstructural maps or local junction responses. In high-stakes applications, state what level of evidence would be sufficient before committing design resources or fabrication capacity.

### Linked calculations and missing-variable audit

Compute the diffusion length for independently measured D and τ; identify whether surface processing, bulk defects or photon recycling changes the apparent decay. Work both interactive models for the unit, first at their default conditions and then after changing one input by 10% within slider bounds. Recalculate one output manually and compare it to a second independent program or calculator. The two formulas address different features of the material, so their combination is not automatically a multi-physics simulation. Build a box-and-arrow account of how processing influences structure, carrier populations, electrical or optical response and eventual device performance. Label any link that is still only hypothetical.

### Experimental discrimination and judgment

Repeat with different wafer thickness, excitation depth, and injection level; validate with surface and bulk-sensitive measurements. Distinguish a paired repeat on the same device from an independently fabricated replicate; predeclare what discrepancy requires reassessment. Preserve raw observations, geometry, uncertainties and model configurations. A credible conclusion identifies an observation that a rival explanation could not produce under the same controls. **Warning:** A single-exponential fit is not a microscopic defect identification. Report evidence status separately as demonstrated, provisional, or not yet assessed. The cost of overclaiming a semiconductor property rises sharply when it becomes a process-selection or field-reliability decision.

### Five cumulative university examination prompts

1. Draw an atomistic-to-device diagram for **momentum scattering, lifetime and diffusion**, with a label on each directly measured or assumed arrow.
2. Compare **transport mobility versus survival of excess carriers** and state the governing assumptions and units for one calculation.
3. Recompute one unit model in two independent ways and perform one limiting-case or monotonicity check.
4. Formulate a rival explanation using **trapping, surface loss, injection-dependent recombination or heating** and specify the result of **time-resolved photoconductance and thickness-dependent lifetime testing** that would distinguish it.
5. Deliver a one-page technical decision note that separates known facts, conditional calculations, uncertainty and additional qualification before scale-up.

