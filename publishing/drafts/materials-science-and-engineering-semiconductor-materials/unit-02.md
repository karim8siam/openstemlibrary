# Unit 2: Band structure and carrier statistics

**Central research question:** How do electronic states and temperature determine the available mobile carrier populations?

## Material and device context

Band structure is a population problem as well as an energy diagram. Measured carriers depend on available states, occupation, dopant ionization, traps and chemical potential, each with its own temperature dependence.

A correct photon-energy conversion does not determine whether an optical transition is radiatively efficient; k-selection, matrix elements and nonradiative competition remain separate.

**Scope of this unit:** Study **electronic density of states and occupation statistics** while distinguishing **bulk energy bands versus measured carrier population**. Practical interpretation requires **temperature, Fermi-level reference, effective mass and band-gap definition**. An important alternative is **nonparabolic bands, degeneracy or band-tail states**, which is why **Hall carrier density paired with absorption and temperature-dependent spectroscopy** must be part of a credible validation programme. These topics are inseparable from geometry, scale and specimen history; a nominal textbook material is not a sufficiently specified industrial sample.

## Measurement-first reading checkpoint

## Lesson 2.1: From Bloch states to electronic bands

### A physical explanation before any numerical fit

In a perfect periodic potential, Bloch wavefunctions carry crystal momentum. Allowed energy states disperse with wavevector E(k); band curvature near an extremum defines an effective mass through the second derivative of E with respect to k. A single parabolic pocket approximation is useful near a band edge but may fail with strong nonparabolicity, multiple valleys, or high carrier concentration. Direct and indirect band gaps are defined by the locations of the relevant band extrema in momentum space, not by the wavelength alone.

**Primary relationship:** Effective mass is an energy-curvature parameter; it need not equal a free-electron mass or be isotropic. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **from bloch states to electronic bands**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Compare direct-gap GaAs and indirect-gap Si as light emitters. Explain why phonon participation changes radiative transition probability even when both samples contain electrons and holes. Use a band diagram in k-space, not merely a real-space band-edge sketch.

For a realistic assessment, distinguish directly controlled inputs from inferred ones. In this lesson, the relevant controls include **temperature, Fermi-level reference, effective mass and band-gap definition**; measure each where possible and report the resolution or calibration of the instrument. A model fit that adjusts an unmeasured constant to match one observable does not establish that the associated mechanism is correct. Ask whether **nonparabolic bands, degeneracy or band-tail states** could produce the same sign of change and what independent feature would differ. If the two proposed mechanisms are observationally indistinguishable under the existing design, the next scientific contribution is a better experiment rather than a more elaborate fit.

### Transparent worked numerical example

The offline calculator **Band gap and photon wavelength** is deliberately simpler than the phenomenon being discussed. Let **Photonic transition energy = 1.4 eV**. From the implemented expression `1239.841984/eg`, the predicted value is **885.601417 nm**. Change only the designated control to **1.7 eV** and the result becomes **729.318814 nm**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-520.94201 (nm)/(eV)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Vacuum wavelength equivalent to E=hc/λ; not a prediction of absorption strength or radiative efficiency**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

The density of states and optical matrix element matter as well as the gap; simplified parabolic models have restricted energy ranges.

Perform a **thermodynamic regime audit**: Identify whether equilibrium, degenerate statistics, hot carriers, low injection, or finite-bias gradients alter validity. Follow with a **geometry and dimensionality audit**: Distinguish three-dimensional volume density from two-dimensional sheet density and separate area from length. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **electronic density of states and occupation statistics** with a response in **from bloch states to electronic bands**. Now suppose instead that the change is controlled by **nonparabolic bands, degeneracy or band-tail states**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **Hall carrier density paired with absorption and temperature-dependent spectroscopy** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 2.1A — Conceptual mechanism.** Explain in your own words what **from bloch states to electronic bands** changes about the relation between **bulk energy bands versus measured carrier population**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 2.1B — Quantitative verification.** Reproduce the values **885.601417 nm** and **729.318814 nm** using `1239.841984/eg` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 2.1C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **nonparabolic bands, degeneracy or band-tail states**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Band gap and photon wavelength** should not be treated as predictive.

<!-- MODEL_2 -->

## Lesson 2.2: Density of states and effective mass

### A physical explanation before any numerical fit

The three-dimensional parabolic-band density of states rises approximately as the square root of kinetic energy above an edge. Integrating this over a Boltzmann occupation yields an effective conduction-band density Nc proportional to T^(3/2) when effective mass is held constant. Valence bands commonly include heavy and light hole contributions that are not adequately represented by one isotropic branch in precision work. The dimensions of density of states per energy per volume differ from Nc per volume; mixing them leads to numerical errors.

**Primary relationship:** For a parabolic nondegenerate band, Nc(T)=Nc(300 K)(T/300 K)^(3/2). The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **density of states and effective mass**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

A student uses a density-of-states value at one energy as though it were the full carrier density. Reconstruct the necessary energy integral and show why warming from 300 to 360 K raises Nc by (360/300)^(3/2) in the simplified model.

### Transparent worked numerical example

The offline calculator **Effective conduction density of states** is deliberately simpler than the phenomenon being discussed. Let **Temperature = 293.33333 K**. From the implemented expression `2.8e19*Math.pow(T/300,1.5)/1e19`, the predicted value is **2.70718712 10^19 cm^-3**. Change only the designated control to **317.77778 K** and the result becomes **3.0525405 10^19 cm^-3**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **0.0141280928 (10^19 cm^-3)/(K)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Fixed conduction-band effective mass, 3D parabolic band, nondegenerate approximation; 2.8e19 cm^-3 at 300 K is an illustrative reference**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

Band-edge effective mass may be temperature dependent; strain and confinement change band degeneracy.

Perform a **geometry and dimensionality audit**: Distinguish three-dimensional volume density from two-dimensional sheet density and separate area from length. Follow with a **statistical independence audit**: Distinguish repeated scans of a single wafer from independent process lots and predeclare rejection criteria. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **electronic density of states and occupation statistics** with a response in **density of states and effective mass**. Now suppose instead that the change is controlled by **nonparabolic bands, degeneracy or band-tail states**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **Hall carrier density paired with absorption and temperature-dependent spectroscopy** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 2.2A — Conceptual mechanism.** Explain in your own words what **density of states and effective mass** changes about the relation between **bulk energy bands versus measured carrier population**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 2.2B — Quantitative verification.** Reproduce the values **2.70718712 10^19 cm^-3** and **3.0525405 10^19 cm^-3** using `2.8e19*Math.pow(T/300,1.5)/1e19` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 2.2C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **nonparabolic bands, degeneracy or band-tail states**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Effective conduction density of states** should not be treated as predictive.

## Lesson 2.3: Fermi level, occupation, and degeneracy

### A physical explanation before any numerical fit

The Fermi–Dirac function f(E)=1/[1+exp((E−Ef)/kT)] gives state occupation, with the chemical potential approximately represented by Ef. For a nondegenerate conduction band, n≈Nc exp(−(Ec−Ef)/kT). Once the Fermi level enters or approaches a band edge, the Boltzmann approximation loses accuracy and Fermi–Dirac integrals are required. In equilibrium the electrochemical potential is spatially constant, though band edges can bend. A plotted Fermi level must specify the energy reference.

**Primary relationship:** Distinguish occupation probability f(E), density of states g(E), and integrated carrier concentration. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **fermi level, occupation, and degeneracy**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

For a material at 300 K, compare conduction-band occupations 0.05 eV and 0.20 eV above Ef. Explain why the ratio is exponential and why a bulk free-carrier density also depends on available states.

### Transparent worked numerical example

The offline calculator **Band gap and photon wavelength** is deliberately simpler than the phenomenon being discussed. Let **Photonic transition energy = 2 eV**. From the implemented expression `1239.841984/eg`, the predicted value is **619.920992 nm**. Change only the designated control to **2.3 eV** and the result becomes **539.061732 nm**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-269.530866 (nm)/(eV)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Degenerate populations and strong disorder require more than a Boltzmann gas; occupation alone is not a measurement of mobility.

Perform a **instrument de-embedding audit**: Check contact resistance, substrate channels, parasitic capacitance, optical reflection and thermal offsets. Follow with a **thermodynamic regime audit**: Identify whether equilibrium, degenerate statistics, hot carriers, low injection, or finite-bias gradients alter validity. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **electronic density of states and occupation statistics** with a response in **fermi level, occupation, and degeneracy**. Now suppose instead that the change is controlled by **nonparabolic bands, degeneracy or band-tail states**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **Hall carrier density paired with absorption and temperature-dependent spectroscopy** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 2.3A — Conceptual mechanism.** Explain in your own words what **fermi level, occupation, and degeneracy** changes about the relation between **bulk energy bands versus measured carrier population**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 2.3B — Quantitative verification.** Reproduce the values **619.920992 nm** and **539.061732 nm** using `1239.841984/eg` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 2.3C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **nonparabolic bands, degeneracy or band-tail states**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Band gap and photon wavelength** should not be treated as predictive.

## Lesson 2.4: Intrinsic carrier concentration and mass action

### A physical explanation before any numerical fit

For a nondegenerate semiconductor in thermal equilibrium, np=ni², where ni depends on gap, temperature, and effective densities of states. This equilibrium relation is not automatically true for electron and hole populations under illumination or electrical injection. The intrinsic carrier density changes steeply with temperature because the exponential activation usually dominates the slower density-of-states temperature factor. Use k in eV/K when Eg is expressed in eV, and avoid mixing a reference ni with inconsistent effective-mass assumptions.

**Primary relationship:** ni(T)=ni(300)(T/300)^(3/2)exp[−Eg/(2k)(1/T−1/300)] under fixed-gap assumptions. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **intrinsic carrier concentration and mass action**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

At a fixed hypothetical 1.12 eV band gap and ni(300 K)=10^10 cm⁻³, estimate ni at 330 K using a normalized Arrhenius form. Then identify why the result should not be exported as a certified silicon reference curve at high temperature.

### Transparent worked numerical example

The offline calculator **Effective conduction density of states** is deliberately simpler than the phenomenon being discussed. Let **Temperature = 342.22222 K**. From the implemented expression `2.8e19*Math.pow(T/300,1.5)/1e19`, the predicted value is **3.41144568 10^19 cm^-3**. Change only the designated control to **366.66667 K** and the result becomes **3.78340902 10^19 cm^-3**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **0.0152166823 (10^19 cm^-3)/(K)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Actual gap narrows with temperature, high doping modifies bands, and intrinsic approximations need temperature-range qualification.

Begin with **microstructural and chemical imaging**; record **pixel sampling, surface preparation, field of view, composition detection floor, and measurement uncertainty** and independently compare against **diffraction plus spatially resolved chemical profile**. Because the original measurement and the independent technique interrogate different aspects of a sample, agreement strengthens a claim, while disagreement can locate the missing effect. A structural analysis might average over a large volume while an electrical test disproportionately samples a thin channel. Temperature-dependent optical data can distinguish activation from transport in some settings, but only if spectral calibration and carrier injection are independently controlled.

Perform a **statistical independence audit**: Distinguish repeated scans of a single wafer from independent process lots and predeclare rejection criteria. Follow with a **instrument de-embedding audit**: Check contact resistance, substrate channels, parasitic capacitance, optical reflection and thermal offsets. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **electronic density of states and occupation statistics** with a response in **intrinsic carrier concentration and mass action**. Now suppose instead that the change is controlled by **nonparabolic bands, degeneracy or band-tail states**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **Hall carrier density paired with absorption and temperature-dependent spectroscopy** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 2.4A — Conceptual mechanism.** Explain in your own words what **intrinsic carrier concentration and mass action** changes about the relation between **bulk energy bands versus measured carrier population**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 2.4B — Quantitative verification.** Reproduce the values **3.41144568 10^19 cm^-3** and **3.78340902 10^19 cm^-3** using `2.8e19*Math.pow(T/300,1.5)/1e19` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 2.4C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **nonparabolic bands, degeneracy or band-tail states**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Effective conduction density of states** should not be treated as predictive.

<!-- MODEL_3 -->

## Lesson 2.5: Band diagrams and heterojunction offsets

### A physical explanation before any numerical fit

A real-space band diagram plots conduction and valence edges versus position while respecting electrochemical equilibrium, applied bias, electrostatics, and interface charge. At a heterojunction, offsets partition the gap difference; electron affinity is an approximate starting point but interface dipoles and chemical bonding can alter actual lineups. Type-I, type-II, and broken-gap alignments reflect relative edges, not quality rankings. A band diagram alone cannot establish growth interdiffusion, trap density, or tunneling transparency.

**Primary relationship:** Always specify the reference energy, coordinate, equilibrium or nonequilibrium condition, and interface composition. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **band diagrams and heterojunction offsets**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Sketch a type-I quantum well with barrier conduction and valence band edges, then apply a small bias. Identify which changes are due to electrostatic potential and which are material discontinuities. List one measurable spectroscopic offset technique.

### Transparent worked numerical example

The offline calculator **Band gap and photon wavelength** is deliberately simpler than the phenomenon being discussed. Let **Photonic transition energy = 2.6 eV**. From the implemented expression `1239.841984/eg`, the predicted value is **476.862302 nm**. Change only the designated control to **2.9 eV** and the result becomes **427.531719 nm**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-164.435276 (nm)/(eV)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Band edges inferred from different surface preparations may disagree because electrochemical boundary conditions change.

Perform a **charge neutrality audit**: Verify the sign and physical units of electrons, holes, ionized donors and acceptors; document compensation. Follow with a **charge neutrality audit**: Verify the sign and physical units of electrons, holes, ionized donors and acceptors; document compensation. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **electronic density of states and occupation statistics** with a response in **band diagrams and heterojunction offsets**. Now suppose instead that the change is controlled by **nonparabolic bands, degeneracy or band-tail states**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **Hall carrier density paired with absorption and temperature-dependent spectroscopy** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 2.5A — Conceptual mechanism.** Explain in your own words what **band diagrams and heterojunction offsets** changes about the relation between **bulk energy bands versus measured carrier population**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 2.5B — Quantitative verification.** Reproduce the values **476.862302 nm** and **427.531719 nm** using `1239.841984/eg` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 2.5C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **nonparabolic bands, degeneracy or band-tail states**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Band gap and photon wavelength** should not be treated as predictive.

## Integrated case study: Diagnosing a Fermi-level error

### Problem statement and evidence hierarchy

A simulation predicts ten times the measured electron density even though it uses a plausible band gap. Treat the problem as a comparison of several causes, not a request to select one formula. First write down what was controlled and directly measured; separate that from what is an inference about **electronic density of states and occupation statistics**. Material recipes, deposition logs and temperature setpoints should not be substituted for actual measured carrier concentrations, layer thicknesses, microstructural maps or local junction responses. In high-stakes applications, state what level of evidence would be sufficient before committing design resources or fabrication capacity.

### Linked calculations and missing-variable audit

Recalculate densities with Nc, Ef, actual temperature, dopant ionization and an independent Hall response; test whether Boltzmann occupation is valid. Work both interactive models for the unit, first at their default conditions and then after changing one input by 10% within slider bounds. Recalculate one output manually and compare it to a second independent program or calculator. The two formulas address different features of the material, so their combination is not automatically a multi-physics simulation. Build a box-and-arrow account of how processing influences structure, carrier populations, electrical or optical response and eventual device performance. Label any link that is still only hypothetical.

### Experimental discrimination and judgment

Compare Hall, capacitance and optical signatures with uncertainties and inspect nondegenerate versus degenerate solutions. Distinguish a paired repeat on the same device from an independently fabricated replicate; predeclare what discrepancy requires reassessment. Preserve raw observations, geometry, uncertainties and model configurations. A credible conclusion identifies an observation that a rival explanation could not produce under the same controls. **Warning:** The model is an equilibrium, bulk approximation and cannot stand in for a nonequilibrium device simulator. Report evidence status separately as demonstrated, provisional, or not yet assessed. The cost of overclaiming a semiconductor property rises sharply when it becomes a process-selection or field-reliability decision.

### Five cumulative university examination prompts

1. Draw an atomistic-to-device diagram for **electronic density of states and occupation statistics**, with a label on each directly measured or assumed arrow.
2. Compare **bulk energy bands versus measured carrier population** and state the governing assumptions and units for one calculation.
3. Recompute one unit model in two independent ways and perform one limiting-case or monotonicity check.
4. Formulate a rival explanation using **nonparabolic bands, degeneracy or band-tail states** and specify the result of **Hall carrier density paired with absorption and temperature-dependent spectroscopy** that would distinguish it.
5. Deliver a one-page technical decision note that separates known facts, conditional calculations, uncertainty and additional qualification before scale-up.

