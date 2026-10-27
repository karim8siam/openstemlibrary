# Unit 5: Junctions, depletion regions, and metal contacts

**Central research question:** How do electrostatics and injection set the electrical response of actual semiconductor interfaces?

## Material and device context

Built-in fields, contact chemistry and device edges make a junction far more complex than a single exponential law. The idealized model has value for sensitivity but not breakdown qualification.

Reverse-bias measurements can irreversibly alter devices; controlled compliance and appropriate laboratory supervision are required.

**Scope of this unit:** Study **electrostatic depletion and injection** while distinguishing **equilibrium field profiles versus real contact and junction I–V**. Practical interpretation requires **doping distributions, area, bias, measurement frequency and surface leakage**. An important alternative is **contact resistance, edge fields and deep-level trap dispersion**, which is why **temperature-dependent guarded I–V and frequency-resolved C–V** must be part of a credible validation programme. These topics are inseparable from geometry, scale and specimen history; a nominal textbook material is not a sufficiently specified industrial sample.

## Measurement-first reading checkpoint

## Lesson 5.1: Equilibrium p–n junction electrostatics

### A physical explanation before any numerical fit

When acceptor- and donor-doped regions meet, diffusion redistributes carriers and leaves ionized impurities, creating an internal field. The depletion approximation neglects mobile charge inside the space-charge region while using charge neutrality far away. For a one-dimensional abrupt junction, depletion width follows Poisson’s equation and depends on dielectric permittivity, reciprocal doping densities, and total potential drop. Highly doped abrupt junctions, graded profiles, and nanoscale geometries can violate the simple model.

**Primary relationship:** W=sqrt[(2εs/q)(1/Na+1/Nd)(Vbi+VR)] in the abrupt one-dimensional depletion approximation. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **equilibrium p–n junction electrostatics**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Estimate depletion width for a symmetric Si p–n junction at 10^16 cm⁻³ on each side, with assumed built-in voltage 0.70 V. Vary reverse bias and compare width scaling with capacitance–voltage data.

For a realistic assessment, distinguish directly controlled inputs from inferred ones. In this lesson, the relevant controls include **doping distributions, area, bias, measurement frequency and surface leakage**; measure each where possible and report the resolution or calibration of the instrument. A model fit that adjusts an unmeasured constant to match one observable does not establish that the associated mechanism is correct. Ask whether **contact resistance, edge fields and deep-level trap dispersion** could produce the same sign of change and what independent feature would differ. If the two proposed mechanisms are observationally indistinguishable under the existing design, the next scientific contribution is a better experiment rather than a more elaborate fit.

### Transparent worked numerical example

The offline calculator **Abrupt junction depletion width** is deliberately simpler than the phenomenon being discussed. Let **Applied reverse bias = 3.3333333 V**. From the implemented expression `10000*Math.sqrt(2*11.7*8.8541878128e-14/1.602176634e-19*(2/1e16)*(0.7+Vr))`, the predicted value is **1.02134896 micrometers**. Change only the designated control to **5 V** and the result becomes **1.21417007 micrometers**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **0.115692663 (micrometers)/(V)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Si εr=11.7, Na=Nd=10^16 cm^-3, built-in potential 0.7 V, ideal abrupt 1D depletion; VR≥0**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

An assumed built-in voltage is not a measured property; incomplete ionization and interface traps can change the interpretation.

Perform a **statistical independence audit**: Distinguish repeated scans of a single wafer from independent process lots and predeclare rejection criteria. Follow with a **charge neutrality audit**: Verify the sign and physical units of electrons, holes, ionized donors and acceptors; document compensation. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **electrostatic depletion and injection** with a response in **equilibrium p–n junction electrostatics**. Now suppose instead that the change is controlled by **contact resistance, edge fields and deep-level trap dispersion**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **temperature-dependent guarded I–V and frequency-resolved C–V** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 5.1A — Conceptual mechanism.** Explain in your own words what **equilibrium p–n junction electrostatics** changes about the relation between **equilibrium field profiles versus real contact and junction I–V**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 5.1B — Quantitative verification.** Reproduce the values **1.02134896 micrometers** and **1.21417007 micrometers** using `10000*Math.sqrt(2*11.7*8.8541878128e-14/1.602176634e-19*(2/1e16)*(0.7+Vr))` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 5.1C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **contact resistance, edge fields and deep-level trap dispersion**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Abrupt junction depletion width** should not be treated as predictive.

<!-- MODEL_8 -->

## Lesson 5.2: Diode injection and ideality factors

### A physical explanation before any numerical fit

The textbook ideal diode law J=J0[exp(qV/nkT)−1] describes a current contribution characterized by saturation current J0 and ideality factor n. In a real junction, diffusion, depletion-region recombination, series resistance, shunt leakage, temperature gradients, and high-level injection may dominate in different intervals. An apparent n extracted from a narrow semilog slope is not a unique fingerprint of one defect. Define applied voltage polarity and contact series resistance before comparing semilog plots.

**Primary relationship:** J=J0(exp[V/(nVt)]−1), where Vt=kT/q. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **diode injection and ideality factors**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Model J(V) using J0=10^-12 A/cm² and n=1.5 at 300 K. Plot 0–0.65 V; identify when the current rises exponentially and where laboratory series resistance might become measurable.

### Transparent worked numerical example

The offline calculator **Illustrative diode current density** is deliberately simpler than the phenomenon being discussed. Let **Forward voltage = 0.21666667 V**. From the implemented expression `1e12*(1e-12*(Math.exp(V/(1.5*8.617333262145e-5*300))-1))`, the predicted value is **266.029884 pA/cm2**. Change only the designated control to **0.28888889 V** and the result becomes **1718.54346 pA/cm2**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **20111.7264 (pA/cm2)/(V)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Current in pA/cm2; J0=1e-12 A/cm2, n=1.5, T=300 K; no series resistance, heating, shunts, or reverse breakdown**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

The model excludes reverse breakdown, capacitance, self-heating, and resistance losses; it cannot predict solar cell efficiency.

Perform a **charge neutrality audit**: Verify the sign and physical units of electrons, holes, ionized donors and acceptors; document compensation. Follow with a **geometry and dimensionality audit**: Distinguish three-dimensional volume density from two-dimensional sheet density and separate area from length. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **electrostatic depletion and injection** with a response in **diode injection and ideality factors**. Now suppose instead that the change is controlled by **contact resistance, edge fields and deep-level trap dispersion**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **temperature-dependent guarded I–V and frequency-resolved C–V** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 5.2A — Conceptual mechanism.** Explain in your own words what **diode injection and ideality factors** changes about the relation between **equilibrium field profiles versus real contact and junction I–V**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 5.2B — Quantitative verification.** Reproduce the values **266.029884 pA/cm2** and **1718.54346 pA/cm2** using `1e12*(1e-12*(Math.exp(V/(1.5*8.617333262145e-5*300))-1))` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 5.2C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **contact resistance, edge fields and deep-level trap dispersion**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Illustrative diode current density** should not be treated as predictive.

## Lesson 5.3: Schottky barriers and Ohmic contacts

### A physical explanation before any numerical fit

At metal–semiconductor interfaces, energy-band alignment, interface dipoles, Fermi-level pinning, doping, and processing determine current transport. A simple Schottky–Mott barrier estimate from work function and electron affinity often fails where interfacial states dominate. Thermionic emission is plausible at some temperatures and barriers, while tunneling and thermionic-field emission become important at heavy doping. An Ohmic contact is operationally defined by sufficiently low resistance and nearly linear response in the relevant operating range.

**Primary relationship:** Separate contact specific resistivity, sheet resistance, and geometrical current crowding. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **schottky barriers and ohmic contacts**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Two metals have different work functions but nearly identical measured barriers on the same semiconductor. Investigate pinning, interfacial oxide, and annealing reactions, then use temperature-dependent and transmission-line measurements.

### Transparent worked numerical example

The offline calculator **Abrupt junction depletion width** is deliberately simpler than the phenomenon being discussed. Let **Applied reverse bias = 6.6666667 V**. From the implemented expression `10000*Math.sqrt(2*11.7*8.8541878128e-14/1.602176634e-19*(2/1e16)*(0.7+Vr))`, the predicted value is **1.38031308 micrometers**. Change only the designated control to **8.3333333 V** and the result becomes **1.52850236 micrometers**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **0.0889135648 (micrometers)/(V)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

An apparently linear two-terminal I–V trace may still hide a large contact resistance relative to channel resistance.

Perform a **thermodynamic regime audit**: Identify whether equilibrium, degenerate statistics, hot carriers, low injection, or finite-bias gradients alter validity. Follow with a **statistical independence audit**: Distinguish repeated scans of a single wafer from independent process lots and predeclare rejection criteria. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **electrostatic depletion and injection** with a response in **schottky barriers and ohmic contacts**. Now suppose instead that the change is controlled by **contact resistance, edge fields and deep-level trap dispersion**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **temperature-dependent guarded I–V and frequency-resolved C–V** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 5.3A — Conceptual mechanism.** Explain in your own words what **schottky barriers and ohmic contacts** changes about the relation between **equilibrium field profiles versus real contact and junction I–V**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 5.3B — Quantitative verification.** Reproduce the values **1.38031308 micrometers** and **1.52850236 micrometers** using `10000*Math.sqrt(2*11.7*8.8541878128e-14/1.602176634e-19*(2/1e16)*(0.7+Vr))` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 5.3C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **contact resistance, edge fields and deep-level trap dispersion**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Abrupt junction depletion width** should not be treated as predictive.

## Lesson 5.4: Junction capacitance and profiling

### A physical explanation before any numerical fit

A reverse-biased junction stores charge as space-charge width varies, so a small-signal capacitance can encode doping profile under ideal assumptions. Abrupt one-sided junction analysis often uses a 1/C² versus bias relationship; extraction assumes a meaningful device area, negligible deep-trap dispersion, and an appropriate frequency. Interface states and series resistance can add frequency dependence and false inferred gradients. Optical or thermal effects may change measured charge response without changing physical doping.

**Primary relationship:** State geometry, small-signal amplitude, frequency, temperature, and equivalent circuit during C–V interpretation. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **junction capacitance and profiling**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Measure junction capacitance at several frequencies. If the apparent dopant density shifts strongly, test deep-level response and series resistance before interpreting a complex doping profile.

### Transparent worked numerical example

The offline calculator **Illustrative diode current density** is deliberately simpler than the phenomenon being discussed. Let **Forward voltage = 0.36111111 V**. From the implemented expression `1e12*(1e-12*(Math.exp(V/(1.5*8.617333262145e-5*300))-1))`, the predicted value is **11072.0292 pA/cm2**. Change only the designated control to **0.43333333 V** and the result becomes **71303.9589 pA/cm2**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **833980.565 (pA/cm2)/(V)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Nanoscale or strongly nonuniform junctions are not well represented by a one-dimensional abrupt approximation.

Perform a **geometry and dimensionality audit**: Distinguish three-dimensional volume density from two-dimensional sheet density and separate area from length. Follow with a **thermodynamic regime audit**: Identify whether equilibrium, degenerate statistics, hot carriers, low injection, or finite-bias gradients alter validity. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **electrostatic depletion and injection** with a response in **junction capacitance and profiling**. Now suppose instead that the change is controlled by **contact resistance, edge fields and deep-level trap dispersion**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **temperature-dependent guarded I–V and frequency-resolved C–V** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 5.4A — Conceptual mechanism.** Explain in your own words what **junction capacitance and profiling** changes about the relation between **equilibrium field profiles versus real contact and junction I–V**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 5.4B — Quantitative verification.** Reproduce the values **11072.0292 pA/cm2** and **71303.9589 pA/cm2** using `1e12*(1e-12*(Math.exp(V/(1.5*8.617333262145e-5*300))-1))` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 5.4C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **contact resistance, edge fields and deep-level trap dispersion**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Illustrative diode current density** should not be treated as predictive.

<!-- MODEL_9 -->

## Lesson 5.5: Breakdown, tunneling, and electrothermal failure

### A physical explanation before any numerical fit

Large reverse field can initiate impact ionization or interband tunneling; their relative importance depends on gap, doping, field distribution, and temperature. Avalanche multiplication is not the same as a thermal runaway event, and breakdown voltage is not a safe operating specification absent current limitation and energy rating. Local field enhancement near edges, surface contamination, and microplasma paths often reduce actual withstand voltage. Guard-ring design and passivation are part of junction materials engineering.

**Primary relationship:** High-field qualification requires spatial field simulation, measured leakage, thermal design, and protective instrumentation. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **breakdown, tunneling, and electrothermal failure**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

A measured diode fails below the one-dimensional predicted breakdown voltage. Compare edge curvature, mobile ionic contamination, and junction termination. Use pulsed experiments with current compliance to minimize destructive self-heating.

### Transparent worked numerical example

The offline calculator **Abrupt junction depletion width** is deliberately simpler than the phenomenon being discussed. Let **Applied reverse bias = 10 V**. From the implemented expression `10000*Math.sqrt(2*11.7*8.8541878128e-14/1.602176634e-19*(2/1e16)*(0.7+Vr))`, the predicted value is **1.66354282 micrometers**. Change only the designated control to **11.666667 V** and the result becomes **1.78841549 micrometers**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **0.074923602 (micrometers)/(V)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Breakdown testing can damage hardware; no interactive teaching model should be used to set a safe destructive-test threshold.

Perform a **instrument de-embedding audit**: Check contact resistance, substrate channels, parasitic capacitance, optical reflection and thermal offsets. Follow with a **instrument de-embedding audit**: Check contact resistance, substrate channels, parasitic capacitance, optical reflection and thermal offsets. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **electrostatic depletion and injection** with a response in **breakdown, tunneling, and electrothermal failure**. Now suppose instead that the change is controlled by **contact resistance, edge fields and deep-level trap dispersion**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **temperature-dependent guarded I–V and frequency-resolved C–V** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 5.5A — Conceptual mechanism.** Explain in your own words what **breakdown, tunneling, and electrothermal failure** changes about the relation between **equilibrium field profiles versus real contact and junction I–V**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 5.5B — Quantitative verification.** Reproduce the values **1.66354282 micrometers** and **1.78841549 micrometers** using `10000*Math.sqrt(2*11.7*8.8541878128e-14/1.602176634e-19*(2/1e16)*(0.7+Vr))` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 5.5C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **contact resistance, edge fields and deep-level trap dispersion**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Abrupt junction depletion width** should not be treated as predictive.

## Integrated case study: Separating junction leakage mechanisms

### Problem statement and evidence hierarchy

An abrupt-junction diode passes a low-voltage screening test but develops high leakage after thermal cycling. Treat the problem as a comparison of several causes, not a request to select one formula. First write down what was controlled and directly measured; separate that from what is an inference about **electrostatic depletion and injection**. Material recipes, deposition logs and temperature setpoints should not be substituted for actual measured carrier concentrations, layer thicknesses, microstructural maps or local junction responses. In high-stakes applications, state what level of evidence would be sufficient before committing design resources or fabrication capacity.

### Linked calculations and missing-variable audit

Measure temperature-dependent J–V and C–V, estimate depletion width, and compare contact behavior before fitting a diode ideality factor. Work both interactive models for the unit, first at their default conditions and then after changing one input by 10% within slider bounds. Recalculate one output manually and compare it to a second independent program or calculator. The two formulas address different features of the material, so their combination is not automatically a multi-physics simulation. Build a box-and-arrow account of how processing influences structure, carrier populations, electrical or optical response and eventual device performance. Label any link that is still only hypothetical.

### Experimental discrimination and judgment

Use guarded contacts, current compliance, low- versus high-frequency measurements and independent defect imaging. Distinguish a paired repeat on the same device from an independently fabricated replicate; predeclare what discrepancy requires reassessment. Preserve raw observations, geometry, uncertainties and model configurations. A credible conclusion identifies an observation that a rival explanation could not produce under the same controls. **Warning:** Breakdown and leakage involve local fields that a uniform 1D model does not capture. Report evidence status separately as demonstrated, provisional, or not yet assessed. The cost of overclaiming a semiconductor property rises sharply when it becomes a process-selection or field-reliability decision.

### Five cumulative university examination prompts

1. Draw an atomistic-to-device diagram for **electrostatic depletion and injection**, with a label on each directly measured or assumed arrow.
2. Compare **equilibrium field profiles versus real contact and junction I–V** and state the governing assumptions and units for one calculation.
3. Recompute one unit model in two independent ways and perform one limiting-case or monotonicity check.
4. Formulate a rival explanation using **contact resistance, edge fields and deep-level trap dispersion** and specify the result of **temperature-dependent guarded I–V and frequency-resolved C–V** that would distinguish it.
5. Deliver a one-page technical decision note that separates known facts, conditional calculations, uncertainty and additional qualification before scale-up.

