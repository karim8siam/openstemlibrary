# Unit 3: Doping, equilibrium, and electrical transport

**Central research question:** When does chemical doping create useful carriers, and what limits their conductivity?

## Material and device context

Bulk resistivity is the product of several coupled physical quantities. A conductivity measurement cannot distinguish greater carrier population from better mobility without an independent observable.

Electrical activation and chemical composition are different quantities, especially after implantation, compensation, annealing or high concentration.

**Scope of this unit:** Study **impurity activation and low-field carrier conductivity** while distinguishing **chemical dopant atoms versus measured free carriers**. Practical interpretation requires **activation, compensation, mobility, geometry and contact resistance**. An important alternative is **temperature-dependent scattering and parallel conduction**, which is why **Hall analysis plus four-probe measurements and chemical depth profiling** must be part of a credible validation programme. These topics are inseparable from geometry, scale and specimen history; a nominal textbook material is not a sufficiently specified industrial sample.

## Measurement-first reading checkpoint

## Lesson 3.1: Donors, acceptors, and charge neutrality

### A physical explanation before any numerical fit

A donor or acceptor changes carrier balance only to the degree that it incorporates in an electrically active configuration and ionizes at the measurement temperature. Substitutional donors in silicon are not equivalent to implanted dopant atoms until activation and redistribution have occurred. At equilibrium, charge neutrality balances holes and ionized donor charge against electrons and ionized acceptor charge. Compensation means the net majority population can be much smaller than the total chemical dopant concentration.

**Primary relationship:** Charge neutrality requires p+Nd⁺=n+Na⁻ in a simple compensated bulk system. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **donors, acceptors, and charge neutrality**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

A secondary-ion mass spectrometry profile shows 10^18 cm⁻³ of a donor, but Hall measurements indicate 3×10^17 cm⁻³ electrons. Compare incomplete activation, compensating acceptors, and Hall-factor issues before concluding that the chemical profile is wrong.

For a realistic assessment, distinguish directly controlled inputs from inferred ones. In this lesson, the relevant controls include **activation, compensation, mobility, geometry and contact resistance**; measure each where possible and report the resolution or calibration of the instrument. A model fit that adjusts an unmeasured constant to match one observable does not establish that the associated mechanism is correct. Ask whether **temperature-dependent scattering and parallel conduction** could produce the same sign of change and what independent feature would differ. If the two proposed mechanisms are observationally indistinguishable under the existing design, the next scientific contribution is a better experiment rather than a more elaborate fit.

### Transparent worked numerical example

The offline calculator **Intrinsic carrier density, fixed-gap model** is deliberately simpler than the phenomenon being discussed. Let **Absolute temperature = 283.33333 K**. From the implemented expression `1e10*Math.pow(T/300,1.5)*Math.exp(-1.12/(2*8.617333262145e-5)*(1/T-1/300))/1e10`, the predicted value is **0.256671244 10^10 cm^-3**. Change only the designated control to **300 K** and the result becomes **1 10^10 cm^-3**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **0.0445997253 (10^10 cm^-3)/(K)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Normalized ni at 300 K=1e10 cm^-3, constant Eg=1.12 eV and effective masses; no band-gap narrowing**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

Shallow-level full-ionization assumptions fail at low temperature, near deep levels, and in heavily disordered samples.

Perform a **geometry and dimensionality audit**: Distinguish three-dimensional volume density from two-dimensional sheet density and separate area from length. Follow with a **instrument de-embedding audit**: Check contact resistance, substrate channels, parasitic capacitance, optical reflection and thermal offsets. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **impurity activation and low-field carrier conductivity** with a response in **donors, acceptors, and charge neutrality**. Now suppose instead that the change is controlled by **temperature-dependent scattering and parallel conduction**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **Hall analysis plus four-probe measurements and chemical depth profiling** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 3.1A — Conceptual mechanism.** Explain in your own words what **donors, acceptors, and charge neutrality** changes about the relation between **chemical dopant atoms versus measured free carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 3.1B — Quantitative verification.** Reproduce the values **0.256671244 10^10 cm^-3** and **1 10^10 cm^-3** using `1e10*Math.pow(T/300,1.5)*Math.exp(-1.12/(2*8.617333262145e-5)*(1/T-1/300))/1e10` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 3.1C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **temperature-dependent scattering and parallel conduction**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Intrinsic carrier density, fixed-gap model** should not be treated as predictive.

<!-- MODEL_4 -->

## Lesson 3.2: Mobility and resistivity from carrier flow

### A physical explanation before any numerical fit

Under low electric field, electron and hole drift mobilities connect mean drift velocity and electric field; conductivity in a two-carrier medium is σ=q(nμn+pμp). Carrier concentrations have units cm⁻³ and mobilities cm²/(V s) when conductivity is desired in S/cm. Mobility is not constant with temperature or dopant density: phonon scattering commonly strengthens on heating, while ionized-impurity scattering can dominate in heavily doped material. A tabulated value represents a sample and measurement regime, not a universal constant.

**Primary relationship:** Resistivity ρ=1/σ, with σ=q n μn for one dominant carrier species. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **mobility and resistivity from carrier flow**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

For hypothetical n=10^16 cm⁻³, μn=1350 cm²/(V s), and negligible holes, calculate σ and resistivity. Now increase doping without changing μ and explain why actual mobility degradation prevents direct extrapolation.

### Transparent worked numerical example

The offline calculator **Single-carrier conductivity** is deliberately simpler than the phenomenon being discussed. Let **Electron density = 3.34e+16 cm^-3**. From the implemented expression `1.602176634e-19*n*1350`, the predicted value is **7.22421444 S/cm**. Change only the designated control to **4.45e+16 cm^-3** and the result becomes **9.62507613 S/cm**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **2.16293846e-16 (S/cm)/(cm^-3)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Electrons dominate; fixed μn=1350 cm2/(V s), uniform low-field conditions; ignores concentration-dependent scattering**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

A two-probe resistance mixes metal contact resistance with bulk resistance; four-probe and Hall data disentangle mechanisms.

Perform a **instrument de-embedding audit**: Check contact resistance, substrate channels, parasitic capacitance, optical reflection and thermal offsets. Follow with a **charge neutrality audit**: Verify the sign and physical units of electrons, holes, ionized donors and acceptors; document compensation. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **impurity activation and low-field carrier conductivity** with a response in **mobility and resistivity from carrier flow**. Now suppose instead that the change is controlled by **temperature-dependent scattering and parallel conduction**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **Hall analysis plus four-probe measurements and chemical depth profiling** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 3.2A — Conceptual mechanism.** Explain in your own words what **mobility and resistivity from carrier flow** changes about the relation between **chemical dopant atoms versus measured free carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 3.2B — Quantitative verification.** Reproduce the values **7.22421444 S/cm** and **9.62507613 S/cm** using `1.602176634e-19*n*1350` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 3.2C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **temperature-dependent scattering and parallel conduction**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Single-carrier conductivity** should not be treated as predictive.

## Lesson 3.3: Hall effect and carrier-sign interpretation

### A physical explanation before any numerical fit

In a simple single-carrier, weak-field Drude model, RH≈−1/(qn) for electrons and RH≈+1/(qp) for holes. Real semiconductor Hall factors depend on scattering, multiple carrier types, anisotropy, and magnetic field strength. Combining Hall coefficient and conductivity estimates a Hall mobility, which is not automatically the microscopic drift mobility. In mixed conduction, Hall sign can behave counterintuitively. Record field orientation, current direction, sample thickness, contact geometry, and temperature.

**Primary relationship:** Hall-derived density is model dependent; Hall signal and its field dependence are the observables. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **hall effect and carrier-sign interpretation**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

A Hall trace reverses sign as temperature rises. Test whether intrinsic holes, multilayer conduction, or geometry drift caused the effect by performing field antisymmetrization and independent contact checks.

### Transparent worked numerical example

The offline calculator **Intrinsic carrier density, fixed-gap model** is deliberately simpler than the phenomenon being discussed. Let **Absolute temperature = 316.66667 K**. From the implemented expression `1e10*Math.pow(T/300,1.5)*Math.exp(-1.12/(2*8.617333262145e-5)*(1/T-1/300))/1e10`, the predicted value is **3.39123391 10^10 cm^-3**. Change only the designated control to **333.33333 K** and the result becomes **10.2186807 10^10 cm^-3**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **0.409646809 (10^10 cm^-3)/(K)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Van der Pauw analysis assumes suitable sample uniformity and contacts; multilayer films often violate its ideal geometry.

Perform a **statistical independence audit**: Distinguish repeated scans of a single wafer from independent process lots and predeclare rejection criteria. Follow with a **geometry and dimensionality audit**: Distinguish three-dimensional volume density from two-dimensional sheet density and separate area from length. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **impurity activation and low-field carrier conductivity** with a response in **hall effect and carrier-sign interpretation**. Now suppose instead that the change is controlled by **temperature-dependent scattering and parallel conduction**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **Hall analysis plus four-probe measurements and chemical depth profiling** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 3.3A — Conceptual mechanism.** Explain in your own words what **hall effect and carrier-sign interpretation** changes about the relation between **chemical dopant atoms versus measured free carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 3.3B — Quantitative verification.** Reproduce the values **3.39123391 10^10 cm^-3** and **10.2186807 10^10 cm^-3** using `1e10*Math.pow(T/300,1.5)*Math.exp(-1.12/(2*8.617333262145e-5)*(1/T-1/300))/1e10` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 3.3C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **temperature-dependent scattering and parallel conduction**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Intrinsic carrier density, fixed-gap model** should not be treated as predictive.

## Lesson 3.4: Diffusion, drift, and the Einstein relation

### A physical explanation before any numerical fit

Concentration gradients drive diffusion while electric fields drive drift. In a nondegenerate, isothermal semiconductor, diffusion coefficient D and mobility μ are linked by D/μ=kT/q. This equality follows from detailed balance and fails in its elementary form when carrier degeneracy, hot carriers, or strongly nonuniform systems invalidate the assumptions. Drift–diffusion modeling couples Poisson and continuity equations rather than adding independent currents without boundary conditions. Positive conventional current directions differ from electron particle flow.

**Primary relationship:** For nondegenerate conditions, D (cm²/s)=μ(cm²/Vs)kT/q (V). The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **diffusion, drift, and the einstein relation**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Calculate electron diffusion coefficient at 300 K from a hypothetical mobility of 1000 cm²/(V s). Compare an equilibrium density gradient with and without an electric field and explain how opposing drift and diffusion can yield zero net current.

### Transparent worked numerical example

The offline calculator **Single-carrier conductivity** is deliberately simpler than the phenomenon being discussed. Let **Electron density = 5.56e+16 cm^-3**. From the implemented expression `1.602176634e-19*n*1350`, the predicted value is **12.0259378 S/cm**. Change only the designated control to **6.67e+16 cm^-3** and the result becomes **14.4267995 S/cm**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **2.16293846e-16 (S/cm)/(cm^-3)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Graded band gaps and strongly degenerate carrier statistics require generalized transport relations.

Perform a **charge neutrality audit**: Verify the sign and physical units of electrons, holes, ionized donors and acceptors; document compensation. Follow with a **statistical independence audit**: Distinguish repeated scans of a single wafer from independent process lots and predeclare rejection criteria. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **impurity activation and low-field carrier conductivity** with a response in **diffusion, drift, and the einstein relation**. Now suppose instead that the change is controlled by **temperature-dependent scattering and parallel conduction**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **Hall analysis plus four-probe measurements and chemical depth profiling** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 3.4A — Conceptual mechanism.** Explain in your own words what **diffusion, drift, and the einstein relation** changes about the relation between **chemical dopant atoms versus measured free carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 3.4B — Quantitative verification.** Reproduce the values **12.0259378 S/cm** and **14.4267995 S/cm** using `1.602176634e-19*n*1350` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 3.4C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **temperature-dependent scattering and parallel conduction**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Single-carrier conductivity** should not be treated as predictive.

<!-- MODEL_5 -->

## Lesson 3.5: Temperature and high-field transport

### A physical explanation before any numerical fit

At moderate fields, scattering limits drift velocity. Under strong electric field, carriers may heat relative to the lattice, intervalley transfer may occur, and velocity can saturate; a constant mobility is no longer a complete description. Contact heating, Joule dissipation, and changes in dopant ionization can alter measurements in the same device. A negative differential resistance feature must be separated from circuit loading and electrothermal instability before assigning an intervalley mechanism.

**Primary relationship:** Report whether measured field, mobility, and carrier temperature occupy the linear-response regime. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **temperature and high-field transport**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Compare low-bias four-terminal current–voltage data with high-pulse-field measurements. Vary pulse width to test whether self-heating or genuine high-field transport is responsible for a slope change.

### Transparent worked numerical example

The offline calculator **Intrinsic carrier density, fixed-gap model** is deliberately simpler than the phenomenon being discussed. Let **Absolute temperature = 350 K**. From the implemented expression `1e10*Math.pow(T/300,1.5)*Math.exp(-1.12/(2*8.617333262145e-5)*(1/T-1/300))/1e10`, the predicted value is **27.8202504 10^10 cm^-3**. Change only the designated control to **366.66667 K** and the result becomes **69.3737923 10^10 cm^-3**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **2.49321252 (10^10 cm^-3)/(K)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

An empirical saturation-velocity curve is not universal across crystal orientations, material quality, and temperature.

Perform a **thermodynamic regime audit**: Identify whether equilibrium, degenerate statistics, hot carriers, low injection, or finite-bias gradients alter validity. Follow with a **thermodynamic regime audit**: Identify whether equilibrium, degenerate statistics, hot carriers, low injection, or finite-bias gradients alter validity. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **impurity activation and low-field carrier conductivity** with a response in **temperature and high-field transport**. Now suppose instead that the change is controlled by **temperature-dependent scattering and parallel conduction**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **Hall analysis plus four-probe measurements and chemical depth profiling** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 3.5A — Conceptual mechanism.** Explain in your own words what **temperature and high-field transport** changes about the relation between **chemical dopant atoms versus measured free carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 3.5B — Quantitative verification.** Reproduce the values **27.8202504 10^10 cm^-3** and **69.3737923 10^10 cm^-3** using `1e10*Math.pow(T/300,1.5)*Math.exp(-1.12/(2*8.617333262145e-5)*(1/T-1/300))/1e10` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 3.5C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **temperature-dependent scattering and parallel conduction**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Intrinsic carrier density, fixed-gap model** should not be treated as predictive.

## Integrated case study: Investigating a poor Hall mobility

### Problem statement and evidence hierarchy

A doped semiconductor thin film carries the expected chemical impurity concentration but has unexpectedly high sheet resistance. Treat the problem as a comparison of several causes, not a request to select one formula. First write down what was controlled and directly measured; separate that from what is an inference about **impurity activation and low-field carrier conductivity**. Material recipes, deposition logs and temperature setpoints should not be substituted for actual measured carrier concentrations, layer thicknesses, microstructural maps or local junction responses. In high-stakes applications, state what level of evidence would be sufficient before committing design resources or fabrication capacity.

### Linked calculations and missing-variable audit

Convert chemical concentration to activated carriers, calculate σ, and independently estimate Hall density and mobility; vary temperature and probe geometry. Work both interactive models for the unit, first at their default conditions and then after changing one input by 10% within slider bounds. Recalculate one output manually and compare it to a second independent program or calculator. The two formulas address different features of the material, so their combination is not automatically a multi-physics simulation. Build a box-and-arrow account of how processing influences structure, carrier populations, electrical or optical response and eventual device performance. Label any link that is still only hypothetical.

### Experimental discrimination and judgment

Use transmission-line contact testing, four-probe resistivity, Hall mapping, and interface microscopy on the same batch. Distinguish a paired repeat on the same device from an independently fabricated replicate; predeclare what discrepancy requires reassessment. Preserve raw observations, geometry, uncertainties and model configurations. A credible conclusion identifies an observation that a rival explanation could not produce under the same controls. **Warning:** A single measured resistance cannot isolate carrier density, mobility, and contact effects. Report evidence status separately as demonstrated, provisional, or not yet assessed. The cost of overclaiming a semiconductor property rises sharply when it becomes a process-selection or field-reliability decision.

### Five cumulative university examination prompts

1. Draw an atomistic-to-device diagram for **impurity activation and low-field carrier conductivity**, with a label on each directly measured or assumed arrow.
2. Compare **chemical dopant atoms versus measured free carriers** and state the governing assumptions and units for one calculation.
3. Recompute one unit model in two independent ways and perform one limiting-case or monotonicity check.
4. Formulate a rival explanation using **temperature-dependent scattering and parallel conduction** and specify the result of **Hall analysis plus four-probe measurements and chemical depth profiling** that would distinguish it.
5. Deliver a one-page technical decision note that separates known facts, conditional calculations, uncertainty and additional qualification before scale-up.

