# -*- coding: utf-8 -*-
"""
create_unit8.py
Generates build_pchem1_unit8.py with 3x content depth, complete derivations,
chemical equations, and zero course numbers.
"""

content = r'''# -*- coding: utf-8 -*-
"""
build_pchem1_unit8.py
Unit 8: Electrochemistry: Galvanic Cells, Nernst Equation, Batteries, Corrosion & Electrolysis
Exhaustive honors-level master digital textbook module with 3x depth,
complete mathematical derivations, and zero course numbers.
"""

def get_unit8():
    return {
        "number": 8,
        "title": "Electrochemistry: Galvanic Cells, Nernst Equation, Batteries, Corrosion & Electrolysis",
        "leadSummary": "Thermodynamics and physical chemistry of electrochemistry and electrochemical systems: microscopic electron transfer and ion-electron half-reaction balancing in acidic and alkaline media, electronic versus electrolytic conduction and ionic mobility, thermodynamic architecture of galvanic cells and the Standard Hydrogen Electrode (SHE), standard reduction potential series and IUPAC cell conventions, derivation of electromotive force and standard Gibbs free energy (ΔG° = -nFE°_cell), the Nernst equation for non-standard states and concentration cells, thermodynamic entropy and enthalpy determinations from temperature coefficients (∂E°/∂T)_P, commercial primary and secondary batteries (alkaline, lead-acid, lithium-ion intercalation), PEM and alkaline fuel cells, electrochemical corrosion mechanisms of iron and cathodic protection, and electrolytic cells, Faraday's laws of electrolysis, overpotentials, and industrial chlor-alkali and electrometallurgical processes.",
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Redox Reactions, Electrochemical Fundamentals & Half-Reactions",
                "content": r"""Electrochemistry is the branch of physical chemistry that investigates the interconversion between chemical energy and electrical energy. At the molecular level, all electrochemical processes are governed by **oxidation-reduction (redox)** phenomena—concerted electron transfer reactions between chemical species.

### Oxidation States & The Nature of Electron Transfer

Every redox reaction can be dissected into two complementary, simultaneously occurring half-reactions:
1. **Oxidation**: The loss of electrons by a chemical species, corresponding to an increase in formal oxidation state. The species undergoing oxidation acts as the **reducing agent (reductant)**:
   $$\text{Red}_1 \longrightarrow \text{Ox}_1 + n e^- \tag{8.1}$$
2. **Reduction**: The gain of electrons by a chemical species, corresponding to a decrease in formal oxidation state. The species undergoing reduction acts as the **oxidizing agent (oxidant)**:
   $$\text{Ox}_2 + n e^- \longrightarrow \text{Red}_2 \tag{8.2}$$

Because free electrons do not exist in appreciable concentrations in condensed chemical solutions, oxidation cannot occur without an equivalent and simultaneous reduction:
$$\text{Red}_1 + \text{Ox}_2 \longrightarrow \text{Ox}_1 + \text{Red}_2 \tag{8.3}$$

### Rigorous Ion-Electron Balancing in Acidic and Basic Media

To analyze redox thermodynamics, reaction equations must be balanced stoichiometrically and electronically. The **ion-electron (half-reaction) method** provides an algorithmic procedure:

#### Balancing in Acidic Solution ($\text{H}^+, \text{H}_2\text{O}$)
Consider the oxidation of iron(II) by dichromate ions in acidic solution:
$$\text{Fe}^{2+} + \text{Cr}_2\text{O}_7^{2-} \longrightarrow \text{Fe}^{3+} + \text{Cr}^{3+}$$

1. **Separate into skeleton half-reactions**:
   $$\text{Oxidation: } \text{Fe}^{2+} \longrightarrow \text{Fe}^{3+}$$
   $$\text{Reduction: } \text{Cr}_2\text{O}_7^{2-} \longrightarrow \text{Cr}^{3+}$$
2. **Balance elements other than $\text{O}$ and $\text{H}$**:
   $$\text{Cr}_2\text{O}_7^{2-} \longrightarrow 2\text{Cr}^{3+}$$
3. **Balance oxygen atoms by adding $\text{H}_2\text{O}$ molecules**:
   $$\text{Cr}_2\text{O}_7^{2-} \longrightarrow 2\text{Cr}^{3+} + 7\text{H}_2\text{O}$$
4. **Balance hydrogen atoms by adding $\text{H}^+$ ions**:
   $$\text{Cr}_2\text{O}_7^{2-} + 14\text{H}^+ \longrightarrow 2\text{Cr}^{3+} + 7\text{H}_2\text{O}$$
5. **Balance electrical charge by adding electrons ($e^-$)**:
   $$\text{Fe}^{2+} \longrightarrow \text{Fe}^{3+} + e^- \quad (\times 6)$$
   $$\text{Cr}_2\text{O}_7^{2-} + 14\text{H}^+ + 6e^- \longrightarrow 2\text{Cr}^{3+} + 7\text{H}_2\text{O} \quad (\times 1)$$
6. **Sum and cancel electrons**:
   $$\text{Cr}_2\text{O}_7^{2-}(aq) + 14\text{H}^+(aq) + 6\text{Fe}^{2+}(aq) \longrightarrow 2\text{Cr}^{3+}(aq) + 6\text{Fe}^{3+}(aq) + 7\text{H}_2\text{O}(l) \tag{8.4}$$

#### Balancing in Basic Solution ($\text{OH}^-, \text{H}_2\text{O}$)
For alkaline media, balance as in acid, then add $\text{OH}^-$ ions to both sides equal to the number of $\text{H}^+$ ions, neutralizing $\text{H}^+ + \text{OH}^- \rightarrow \text{H}_2\text{O}$, and cancel common water molecules. For example, oxidation of sulfite by permanganate:
$$\text{MnO}_4^- + \text{SO}_3^{2-} \longrightarrow \text{MnO}_2 + \text{SO}_4^{2-}$$
In basic solution, the balanced equation becomes:
$$2\text{MnO}_4^-(aq) + 3\text{SO}_3^{2-}(aq) + \text{H}_2\text{O}(l) \longrightarrow 2\text{MnO}_2(s) + 3\text{SO}_4^{2-}(aq) + 2\text{OH}^-(aq) \tag{8.5}$$

### Electronic Conductors vs. Electrolytic Conductors

Electrical current is the directed flow of electric charge. In physical chemistry, conduction occurs through two fundamentally distinct physical mechanisms:

| Conduction Property | Electronic (Metallic) Conduction | Electrolytic (Ionic) Conduction |
| :--- | :--- | :--- |
| **Charge Carriers** | Delocalized valence electrons ($e^-$) | Solvated cations ($M^{z+}$) and anions ($X^{z-}$) |
| **Material Transport** | Zero net mass transfer of atomic nuclei | Macroscopic transport of ions toward electrodes |
| **Chemical Change** | No chemical decomposition of conductor | Chemical oxidation/reduction at phase boundaries |
| **Temperature Effect** | Conductivity decreases as $T \uparrow$ (lattice phonon scattering) | Conductivity increases as $T \uparrow$ (lower solvent viscosity, higher mobility) |
| **Carrier Mobility** | $\sim 10^{-3} \text{ to } 10^{-2}\text{ m}^2\text{V}^{-1}\text{s}^{-1}$ | $\sim 10^{-8} \text{ to } 10^{-7}\text{ m}^2\text{V}^{-1}\text{s}^{-1}$ |

### Ionic Drift Velocity, Mobility & Transport Numbers

Under an applied electric field $\vec{E} = -\nabla \phi$ of magnitude $E = \Delta V / d$, an ion of charge $z_i e$ experiences an electrostatic force $\vec{F}_e = z_i e \vec{E}$. In a viscous medium of dynamic viscosity $\eta$, the ion is retarded by hydrodynamic drag given by Stokes' Law for an effective hydrodynamic (solvated) radius $r_{h,i}$:
$$\vec{F}_{\text{drag}} = 6 \pi \eta r_{h,i} \vec{v}_i$$
At terminal drift velocity $\vec{v}_i$, forces balance ($\vec{F}_e + \vec{F}_{\text{drag}} = 0$), yielding:
$$v_i = \frac{|z_i| e}{6 \pi \eta r_{h,i}} E = u_i E \tag{8.6}$$
Where $u_i$ is the **ionic mobility** ($\text{m}^2\text{s}^{-1}\text{V}^{-1}$):
$$u_i \equiv \frac{v_i}{E} = \frac{|z_i| e}{6 \pi \eta r_{h,i}} \tag{8.7}$$

The fraction of total electrical current carried by ionic species $i$ is defined as its **transport number (transference number)** $t_i$:
$$t_i = \frac{I_i}{I_{\text{total}}} = \frac{z_i c_i u_i}{\sum_j z_j c_j u_j} \tag{8.8}$$
For a simple 1:1 electrolyte ($\text{NaCl}$), $t_+ + t_- = 1$. Anomalously high mobilities are observed for $\text{H}^+(aq)$ ($u \approx 36.2 \times 10^{-8}\text{ m}^2\text{s}^{-1}\text{V}^{-1}$) and $\text{OH}^-(aq)$ ($u \approx 20.6 \times 10^{-8}\text{ m}^2\text{s}^{-1}\text{V}^{-1}$) due to the **Grotthuss proton-hopping mechanism**, where proton transfer occurs through coordinated hydrogen-bond network rearrangement rather than hydrodynamic drag of a hydrated hydronium ball.

### Electrochemical Cell Architecture

An electrochemical cell consists of:
1. **Two electrodes**: Electronic conductors (metals, graphite, conducting polymers) that interface with the electrolyte.
2. **Anode**: The electrode at which **oxidation** occurs ($e^-$ exit the cell into the external circuit).
3. **Cathode**: The electrode at which **reduction** occurs ($e^-$ enter the cell from the external circuit).
4. **Electrolyte phase**: One or more liquid, gel, or solid phases containing mobile ions.
5. **Phase separator / Salt Bridge**: A porous frit or gel (e.g., agar-agar saturated with $\text{KCl}$ or $\text{KNO}_3$) that permits ionic migration to maintain electrical neutrality while preventing convective mechanical mixing of the two different half-cell solutions."""
            },
            {
                "secNumber": "8.2",
                "title": "Galvanic Cells, Standard Hydrogen Electrode (SHE) & Standard Electrode Potentials",
                "content": r"""A **Galvanic (Voltaic) Cell** is an electrochemical system in which a thermodynamically spontaneous chemical reaction ($\Delta G < 0$) is physically partitioned into separate half-cells, forcing electron transfer to proceed through an external electronic circuit, thereby performing electrical work on the surroundings.

### The Classic Daniell Cell

The canonical archetype of a galvanic cell is the Daniell cell, invented in 1836 by John Frederic Daniell:
* **Anode Half-Cell**: A metallic zinc rod immersed in an aqueous zinc sulfate ($\text{ZnSO}_4$) solution.
* **Cathode Half-Cell**: A metallic copper rod immersed in an aqueous copper(II) sulfate ($\text{CuSO}_4$) solution.
* **Salt Bridge**: An inverted U-tube filled with agar gel saturated with $\text{KCl}(aq)$ or $\text{KNO}_3(aq)$ dipping into both beakers.

The operational half-reactions are:
$$\text{Anode (Oxidation): } \text{Zn}(s) \longrightarrow \text{Zn}^{2+}(aq) + 2e^- \quad [E^\circ_{\text{ox}} = +0.763\text{ V}]$$
$$\text{Cathode (Reduction): } \text{Cu}^{2+}(aq) + 2e^- \longrightarrow \text{Cu}(s) \quad [E^\circ_{\text{red}} = +0.342\text{ V}]$$
$$\text{Overall Cell Reaction: } \text{Zn}(s) + \text{Cu}^{2+}(aq) \longrightarrow \text{Zn}^{2+}(aq) + \text{Cu}(s) \tag{8.9}$$

As electrons spontaneously flow from the zinc electrode (anode) through the external wire to the copper electrode (cathode), $\text{Zn}^{2+}$ cations accumulate around the zinc electrode, while $\text{Cu}^{2+}$ cations are depleted at the copper electrode. To prevent massive electrostatic space-charge buildup that would instantly halt current flow, anions ($\text{Cl}^-$ or $\text{NO}_3^-$) migrate from the salt bridge into the anode compartment, and cations ($\text{K}^+$) migrate into the cathode compartment.

### IUPAC Cell Notation & Conventions

Under IUPAC conventions, a galvanic cell is written as a shorthand linear diagram:
1. The **anode** (oxidation half-cell) is written on the **left**.
2. The **cathode** (reduction half-cell) is written on the **right**.
3. A single vertical line ($|$) denotes a **phase boundary** across which an electrical potential difference develops.
4. A double vertical line ($||$) denotes a **salt bridge** or porous barrier where liquid junction potentials are minimized.
5. Species in the same phase are separated by commas ($,$).

For the standard Daniell cell:
$$\text{Zn}(s) \mid \text{Zn}^{2+}(aq, 1.0\text{ M}) \parallel \text{Cu}^{2+}(aq, 1.0\text{ M}) \mid \text{Cu}(s) \tag{8.10}$$

For an inert platinum electrode participating in a solution redox couple (e.g., $\text{Fe}^{3+}/\text{Fe}^{2+}$):
$$\text{Pt}(s) \mid \text{Fe}^{2+}(aq), \text{Fe}^{3+}(aq) \parallel \text{Ag}^+(aq) \mid \text{Ag}(s) \tag{8.11}$$

### The Standard Hydrogen Electrode (SHE)

Because it is physically impossible to measure the absolute electrical potential of an isolated individual electrode/electrolyte interface without introducing a second probe electrode, standard electrode potentials must be measured relative to an internationally agreed arbitrary zero reference: the **Standard Hydrogen Electrode (SHE)**.

The SHE consists of a platinized platinum foil (coated with finely divided platinum black to provide immense catalytic surface area) immersed in an aqueous solution where hydronium ion activity is unity ($a_{\text{H}^+} = 1.000\text{ M}$), over which pure, dry hydrogen gas bubbles at standard pressure ($P_{\text{H}_2} = 1.000\text{ bar} = 10^5\text{ Pa}$):
$$\text{Pt}(s) \mid \text{H}_2(g, 1\text{ bar}) \mid \text{H}^+(aq, a = 1)$$
The reduction half-reaction at the SHE is defined to have identically zero standard electrode potential at all temperatures:
$$2\text{H}^+(aq, a = 1) + 2e^- \rightleftharpoons \text{H}_2(g, 1\text{ bar}) \quad E^\circ \equiv 0.0000\text{ V} \tag{8.12}$$

### Standard Reduction Potentials & Cell EMF Calculation

By convention adopted universally by IUPAC in 1953 (the Stockholm Convention), all tabulated standard electrode potentials $E^\circ$ are written as **reduction potentials**:
$$\text{Ox} + n e^- \rightleftharpoons \text{Red} \quad E^\circ$$

The standard electromotive force (EMF) of any galvanic cell is calculated by:
$$E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} \tag{8.13}$$
Where both $E^\circ_{\text{cathode}}$ and $E^\circ_{\text{anode}}$ are standard *reduction* potentials taken directly from the electrochemical series.

Representative Standard Reduction Potentials at $298.15\text{ K}$ ($1\text{ bar}$):
* $\text{F}_2(g) + 2e^- \rightarrow 2\text{F}^-(aq): \quad E^\circ = +2.866\text{ V}$ (Most powerful thermodynamic oxidant)
* $\text{Au}^3+(aq) + 3e^- \rightarrow \text{Au}(s): \quad E^\circ = +1.498\text{ V}$
* $\text{Cl}_2(g) + 2e^- \rightarrow 2\text{Cl}^-(aq): \quad E^\circ = +1.358\text{ V}$
* $\text{O}_2(g) + 4\text{H}^+(aq) + 4e^- \rightarrow 2\text{H}_2\text{O}(l): \quad E^\circ = +1.229\text{ V}$
* $\text{Ag}^+(aq) + e^- \rightarrow \text{Ag}(s): \quad E^\circ = +0.7996\text{ V}$
* $\text{Fe}^{3+}(aq) + e^- \rightarrow \text{Fe}^{2+}(aq): \quad E^\circ = +0.771\text{ V}$
* $\text{Cu}^{2+}(aq) + 2e^- \rightarrow \text{Cu}(s): \quad E^\circ = +0.3419\text{ V}$
* $2\text{H}^+(aq) + 2e^- \rightarrow \text{H}_2(g): \quad E^\circ \equiv 0.0000\text{ V}$
* $\text{Pb}^{2+}(aq) + 2e^- \rightarrow \text{Pb}(s): \quad E^\circ = -0.126\text{ V}$
* $\text{Fe}^{2+}(aq) + 2e^- \rightarrow \text{Fe}(s): \quad E^\circ = -0.447\text{ V}$
* $\text{Zn}^{2+}(aq) + 2e^- \rightarrow \text{Zn}(s): \quad E^\circ = -0.7628\text{ V}$
* $\text{Al}^{3+}(aq) + 3e^- \rightarrow \text{Al}(s): \quad E^\circ = -1.662\text{ V}$
* $\text{Mg}^{2+}(aq) + 2e^- \rightarrow \text{Mg}(s): \quad E^\circ = -2.372\text{ V}$
* $\text{Na}^+(aq) + e^- \rightarrow \text{Na}(s): \quad E^\circ = -2.714\text{ V}$
* $\text{Li}^+(aq) + e^- \rightarrow \text{Li}(s): \quad E^\circ = -3.040\text{ V}$ (Most powerful thermodynamic reductant)

For the Daniell cell:
$$E^\circ_{\text{cell}} = E^\circ(\text{Cu}^{2+}/\text{Cu}) - E^\circ(\text{Zn}^{2+}/\text{Zn}) = (+0.3419\text{ V}) - (-0.7628\text{ V}) = +1.1047\text{ V}$$

### Thermodynamic Spontaneity: Free Energy & Cell Potential

When an electrochemical cell operates reversibly at constant temperature and pressure, the maximum electrical work $w_{\text{elec,max}}$ delivered to the surroundings is identically equal to the decrease in Gibbs free energy of the system:
$$\Delta G = -w_{\text{elec,max}} \tag{8.14}$$
For each mole of chemical reaction progressing by advance $\xi = 1\text{ mol}$, a total charge $Q = n F$ moves through a potential difference $E_{\text{cell}}$, where:
* $n$ is the number of moles of electrons transferred per mole of reaction.
* $F = e N_A \approx 96485.332\text{ C mol}^{-1}$ is **Faraday's Constant**.

The electrical work done by the charge flow is $w_{\text{elec}} = Q \cdot E_{\text{cell}} = n F E_{\text{cell}}$. Therefore:
$$\Delta G = -n F E_{\text{cell}} \tag{8.15}$$
Under standard state conditions ($a_i = 1$, $P = 1\text{ bar}$, $T = 298.15\text{ K}$):
$$\Delta G^\circ = -n F E^\circ_{\text{cell}} \tag{8.16}$$

From the Second Law of Thermodynamics, a spontaneous process at constant $T, P$ requires $\Delta G < 0$. Therefore:
* **$E_{\text{cell}} > 0 \iff \Delta G < 0$**: The forward reaction is **spontaneous** (Galvanic operation).
* **$E_{\text{cell}} < 0 \iff \Delta G > 0$**: The forward reaction is **non-spontaneous**; the reverse reaction is spontaneous.
* **$E_{\text{cell}} = 0 \iff \Delta G = 0$**: The cell reaction is at **dynamic thermodynamic equilibrium** (dead battery)."""
            },
            {
                "secNumber": "8.3",
                "title": "Thermodynamics of Cells, The Nernst Equation & Concentration Cells",
                "content": r"""In real chemical systems, reactant and product activities deviate markedly from unit standard-state activities. The **Nernst Equation**, formulated by Walther Nernst in 1889, provides the exact mathematical framework governing electrochemical cell potentials under arbitrary, non-standard conditions.

### Derivation of the Nernst Equation

From classical chemical thermodynamics, the change in Gibbs free energy for any chemical reaction $a A + b B \rightleftharpoons c C + d D$ at arbitrary composition is related to the standard free energy change $\Delta G^\circ$ by:
$$\Delta G = \Delta G^\circ + R T \ln Q \tag{8.17}$$
Where $Q$ is the dimensionless **reaction quotient**:
$$Q = \frac{a_C^c a_D^d}{a_A^a a_B^b}$$
Substituting the electrochemical thermodynamic identities $\Delta G = -n F E$ and $\Delta G^\circ = -n F E^\circ$:
$$-n F E = -n F E^\circ + R T \ln Q$$
Dividing throughout by $-n F$:
$$E = E^\circ - \frac{R T}{n F} \ln Q \tag{8.18}$$
Equation (8.18) is the **Nernst Equation**. Converting from natural logarithm to base-10 logarithm ($\ln Q = \ln(10) \log_{10} Q \approx 2.302585 \log_{10} Q$):
$$E = E^\circ - \frac{2.302585 R T}{n F} \log_{10} Q \tag{8.19}$$

At the standard reference temperature $T = 298.15\text{ K}$ ($25.0^\circ\text{C}$):
$$\frac{2.302585 R T}{F} = \frac{2.302585 \times (8.314462\text{ J mol}^{-1}\text{K}^{-1}) \times (298.15\text{ K})}{96485.332\text{ C mol}^{-1}} = 0.059159\text{ V} \approx 0.0592\text{ V}$$
Thus, at $298.15\text{ K}$:
$$E = E^\circ - \frac{0.05916\text{ V}}{n} \log_{10} Q \tag{8.20}$$

### Evaluation of the Thermodynamic Equilibrium Constant ($K$)

When a galvanic cell discharges until dynamic equilibrium is reached, chemical driving force vanishes identically: $\Delta G = 0$ and $E = 0$. At this point, the reaction quotient equals the thermodynamic equilibrium constant: $Q = K$.
Setting $E = 0$ in the Nernst equation:
$$0 = E^\circ - \frac{R T}{n F} \ln K \implies E^\circ = \frac{R T}{n F} \ln K \tag{8.21}$$
Solving explicitly for $K$:
$$\ln K = \frac{n F E^\circ}{R T} \iff K = \exp\left(\frac{n F E^\circ}{R T}\right) \tag{8.22}$$
At $298.15\text{ K}$:
$$\log_{10} K = \frac{n E^\circ}{0.05916\text{ V}} \iff K = 10^{\frac{n E^\circ}{0.05916\text{ V}}} \tag{8.23}$$

> **Profound Sensitivity of Equilibrium Constants to Potential**:
> A modest cell potential of $E^\circ = +1.105\text{ V}$ with $n = 2$ (the Daniell cell) yields:
> $$\log_{10} K = \frac{2 \times 1.1047}{0.05916} \approx 37.35 \implies K \approx 2.2 \times 10^{37}$$
> This demonstrates that potentiometry provides access to equilibrium constants spanning tens of orders of magnitude—far beyond the measurement capability of conventional spectroscopic or gravimetric titrations!

### Cell Temperature Coefficients & Determination of $\Delta S^\circ, \Delta H^\circ$

Potentiometry is uniquely powerful because measuring the reversible cell EMF as a function of temperature directly yields the thermodynamic entropy $\Delta S^\circ$ and enthalpy $\Delta H^\circ$ of a reaction without measuring heat flows in a calorimeter.

From fundamental Maxwell relations:
$$dG = -S dT + V dP \implies \left(\frac{\partial G}{\partial T}\right)_P = -S$$
Applying this to the reaction free energy $\Delta G = -n F E$:
$$\left(\frac{\partial \Delta G}{\partial T}\right)_P = -\Delta S = -n F \left(\frac{\partial E}{\partial T}\right)_P$$
Therefore, the **reaction entropy** is given by:
$$\Delta S = n F \left(\frac{\partial E}{\partial T}\right)_P \tag{8.24}$$
Where $\left(\frac{\partial E}{\partial T}\right)_P$ is the **temperature coefficient of cell potential**.

Recalling the definition of Gibbs free energy $\Delta G = \Delta H - T \Delta S$:
$$\Delta H = \Delta G + T \Delta S = -n F E + n F T \left(\frac{\partial E}{\partial T}\right)_P = -n F \left[ E - T \left(\frac{\partial E}{\partial T}\right)_P \right] \tag{8.25}$$

Furthermore, differentiating entropy with respect to temperature gives the change in constant-pressure heat capacity:
$$\Delta C_p = T \left(\frac{\partial \Delta S}{\partial T}\right)_P = n F T \left(\frac{\partial^2 E}{\partial T^2}\right)_P \tag{8.26}$$

### Concentration Cells

A **concentration cell** is an electrochemical cell in which both half-cells employ the exact same chemical components (identical electrodes and identical ions), differing only in the concentration (activity) of the electrolyte solution in each compartment.
Because both electrodes are identical in composition, $E^\circ_{\text{cathode}} = E^\circ_{\text{anode}}$, which guarantees:
$$E^\circ_{\text{cell}} = 0 \tag{8.27}$$

Consider a concentration cell with copper electrodes dipping into two $\text{Cu}^{2+}$ solutions of differing concentrations $c_1 < c_2$:
$$\text{Cu}(s) \mid \text{Cu}^{2+}(aq, c_1) \parallel \text{Cu}^{2+}(aq, c_2) \mid \text{Cu}(s)$$
* **Anode (dilute half-cell, $c_1$)**: $\text{Cu}(s) \rightarrow \text{Cu}^{2+}(c_1) + 2e^-$ (dissolution to increase concentration)
* **Cathode (concentrated half-cell, $c_2$)**: $\text{Cu}^{2+}(c_2) + 2e^- \rightarrow \text{Cu}(s)$ (deposition to decrease concentration)
* **Net Cell Reaction**: $\text{Cu}^{2+}(c_2) \longrightarrow \text{Cu}^{2+}(c_1)$

Applying the Nernst equation ($n = 2$):
$$E_{\text{cell}} = E^\circ - \frac{R T}{2 F} \ln\left(\frac{a_1}{a_2}\right) = 0 - \frac{R T}{2 F} \ln\left(\frac{c_1}{c_2}\right) = \frac{R T}{2 F} \ln\left(\frac{c_2}{c_1}\right) \tag{8.28}$$
At $298.15\text{ K}$:
$$E_{\text{cell}} = \frac{0.05916\text{ V}}{2} \log_{10}\left(\frac{c_2}{c_1}\right) \tag{8.29}$$
Since $c_2 > c_1$, $\log_{10}(c_2/c_1) > 0$, guaranteeing $E_{\text{cell}} > 0$. The cell discharges until $c_1 = c_2$, at which point $E_{\text{cell}} = 0$.

### Potentiometric pH Measurement & The Glass Electrode

The linear logarithmic response of cell potential to ion activity is the operational foundation of potentiometric pH meters. A glass electrode contains an internal $\text{Ag}/\text{AgCl}$ reference electrode in $0.1\text{ M HCl}$, enclosed by a thin, proton-conducting glass membrane (typically composed of a silicate glass with $\text{Na}_2\text{O}$ and $\text{CaO}$ modifiers).

When immersed in a test solution of unknown hydronium activity:
$$E_{\text{cell}} = E_{\text{const}} - 0.05916\text{ V} \times \text{pH} \tag{8.30}$$
By measuring the potential difference against an external reference electrode (such as a saturated calomel electrode, SCE, or $\text{Ag}/\text{AgCl}$ reference), the instrument computes the solution pH with an accuracy of $\pm 0.001\text{ pH}$ units."""
            },
            {
                "secNumber": "8.4",
                "title": "Commercial Batteries, Fuel Cells & The Electrochemistry of Corrosion",
                "content": r"""Electrochemical devices power modern civilization—from portable consumer electronics and electric vehicles to grid-scale energy storage. Concurrently, electrochemical degradation (corrosion) inflicts annual global economic losses exceeding \$2.5 trillion USD (over 3% of global GDP).

### Primary Batteries (Non-Rechargeable)

Primary batteries are galvanic cells engineered for one-time discharge; their chemical reactions cannot be reversed efficiently by passing an external recharging current because the electrode materials irreversibly disintegrate or form passivating non-conducting films.

#### 1. The Leclanché Dry Cell (Zinc-Carbon Battery)
Invented in 1866 by Georges Leclanché:
* **Anode (Can)**: Metallic zinc can:
  $$\text{Zn}(s) \longrightarrow \text{Zn}^{2+}(aq) + 2e^- \quad [E^\circ \approx -0.76\text{ V}]$$
* **Cathode (Central Rod)**: Graphite rod surrounded by a moist paste of $\text{MnO}_2$, $\text{NH}_4\text{Cl}$, $\text{ZnCl}_2$, and powdered carbon:
  $$2\text{MnO}_2(s) + 2\text{NH}_4^+(aq) + 2e^- \longrightarrow \text{Mn}_2\text{O}_3(s) + 2\text{NH}_3(aq) + \text{H}_2\text{O}(l)$$
* **Overall Reaction**:
  $$\text{Zn}(s) + 2\text{MnO}_2(s) + 2\text{NH}_4^+(aq) \longrightarrow \text{Zn}^{2+}(aq) + \text{Mn}_2\text{O}_3(s) + 2\text{NH}_3(aq) + \text{H}_2\text{O}(l) \tag{8.31}$$
  To prevent gas pressure accumulation from $\text{NH}_3$, zinc ions coordinate ammonia: $\text{Zn}^{2+} + 4\text{NH}_3 \rightarrow [\text{Zn}(\text{NH}_3)_4]^{2+}$. Nominal voltage is $1.5\text{ V}$, but declines rapidly under heavy continuous load due to polarization and electrolyte drying.

#### 2. The Alkaline Battery
An advanced evolution of the Leclanché cell utilizing an alkaline electrolyte ($\text{KOH}$ paste):
* **Anode**: Granulated zinc powder dispersed in a gel:
  $$\text{Zn}(s) + 2\text{OH}^-(aq) \longrightarrow \text{ZnO}(s) + \text{H}_2\text{O}(l) + 2e^- \quad [E^\circ = -1.28\text{ V}]$$
* **Cathode**: High-density manganese dioxide ($\text{MnO}_2$):
  $$2\text{MnO}_2(s) + \text{H}_2\text{O}(l) + 2e^- \longrightarrow \text{Mn}_2\text{O}_3(s) + 2\text{OH}^-(aq) \quad [E^\circ = +0.15\text{ V}]$$
* **Overall Reaction**:
  $$\text{Zn}(s) + 2\text{MnO}_2(s) \longrightarrow \text{ZnO}(s) + \text{Mn}_2\text{O}_3(s) \quad [E_{\text{cell}} \approx 1.54\text{ V}] \tag{8.32}$$
  Because $\text{OH}^-$ is consumed at the anode and regenerated at the cathode, the electrolyte concentration remains nearly invariant during discharge, delivering 3–5× greater energy density and far flatter discharge profiles than zinc-carbon cells.

### Secondary Batteries (Rechargeable)

Secondary batteries undergo reversible electrochemical transformations; applying an external DC voltage greater than $E_{\text{cell}}$ in the reverse direction regenerates the original active electrode materials.

#### 1. The Lead-Acid Storage Battery
Invented in 1859 by Gaston Planté; ubiquitous in automotive starting, lighting, and ignition (SLI) systems:
* **Anode**: Spongy metallic lead ($\text{Pb}$).
* **Cathode**: Lead(IV) dioxide ($\text{PbO}_2$) packed on lead-alloy grids.
* **Electrolyte**: Concentrated aqueous sulfuric acid ($\text{H}_2\text{SO}_4$, $\sim 4.5\text{ M}$, specific gravity $\approx 1.28$ when fully charged).

**Discharge Reactions**:
$$\text{Anode: } \text{Pb}(s) + \text{HSO}_4^-(aq) \longrightarrow \text{PbSO}_4(s) + \text{H}^+(aq) + 2e^- \quad [E^\circ_{\text{ox}} = +0.356\text{ V}]$$
$$\text{Cathode: } \text{PbO}_2(s) + \text{HSO}_4^-(aq) + 3\text{H}^+(aq) + 2e^- \longrightarrow \text{PbSO}_4(s) + 2\text{H}_2\text{O}(l) \quad [E^\circ_{\text{red}} = +1.685\text{ V}]$$
$$\text{Overall Discharge: } \text{Pb}(s) + \text{PbO}_2(s) + 2\text{H}_2\text{SO}_4(aq) \xrightleftharpoons[\text{charge}]{\text{discharge}} 2\text{PbSO}_4(s) + 2\text{H}_2\text{O}(l) \tag{8.33}$$
Each single cell delivers $E_{\text{cell}} \approx 2.05\text{ V}$. A standard $12\text{ V}$ car battery connects 6 cells in series ($6 \times 2.05\text{ V} \approx 12.3\text{ V}$).
During discharge, both electrodes convert to insoluble lead(II) sulfate ($\text{PbSO}_4$), which adheres to the grid plates, and $\text{H}_2\text{SO}_4$ is consumed, lowering the electrolyte density (providing an immediate gravimetric measure of state of charge via hydrometer).

#### 2. The Lithium-Ion Battery (Intercalation Mechanism)
Awarded the 2019 Nobel Prize in Chemistry (Goodenough, Whittingham, Yoshino), lithium-ion batteries operate via **topotactic intercalation**—the reversible insertion and de-insertion of $\text{Li}^+$ ions into layered host crystal lattices without destroying the host framework:
* **Anode**: Lithiated graphite ($\text{Li}_x\text{C}_6$):
  $$\text{Li}_x\text{C}_6 \xrightleftharpoons[\text{charge}]{\text{discharge}} \text{C}_6 + x \text{Li}^+ + x e^- \quad [E^\circ \approx -3.0\text{ V vs SHE}]$$
* **Cathode**: Layered transition metal oxide (e.g., $\text{Li}_{1-x}\text{CoO}_2$ or $\text{LiFePO}_4$):
  $$\text{Li}_{1-x}\text{CoO}_2 + x \text{Li}^+ + x e^- \xrightleftharpoons[\text{charge}]{\text{discharge}} \text{LiCoO}_2 \quad [E^\circ \approx +0.9\text{ V vs SHE}]$$
* **Overall Discharge**:
  $$\text{Li}_x\text{C}_6 + \text{Li}_{1-x}\text{CoO}_2 \xrightleftharpoons[\text{charge}]{\text{discharge}} \text{C}_6 + \text{LiCoO}_2 \quad [E_{\text{cell}} \approx 3.7\text{ V to } 4.2\text{ V}] \tag{8.34}$$
  Because no metallic lithium is plated (avoiding dangerous dendritic short-circuits) and lithium has the lowest atomic mass ($6.94\text{ g mol}^{-1}$) and most negative standard potential of any metal, Li-ion systems achieve extraordinary gravimetric energy densities ($> 260\text{ Wh kg}^{-1}$).

### Fuel Cells: Continuous Electrochemical Energy Converters

Unlike batteries which store a fixed quantity of chemical reactants within closed containers, a **fuel cell** is an open electrochemical reactor that converts the chemical energy of continuously supplied fuel ($\text{H}_2$, $\text{CH}_4$, methanol) and oxidant ($\text{O}_2$) directly into electricity:
* **The Hydrogen-Oxygen Proton Exchange Membrane (PEM) Fuel Cell**:
  $$\text{Anode: } 2\text{H}_2(g) \longrightarrow 4\text{H}^+(aq) + 4e^- \quad [E^\circ = 0.000\text{ V}]$$
  $$\text{Cathode: } \text{O}_2(g) + 4\text{H}^+(aq) + 4e^- \longrightarrow 2\text{H}_2\text{O}(l) \quad [E^\circ = +1.229\text{ V}]$$
  $$\text{Overall Reaction: } 2\text{H}_2(g) + \text{O}_2(g) \longrightarrow 2\text{H}_2\text{O}(l) \quad [E^\circ_{\text{cell}} = +1.229\text{ V}] \tag{8.35}$$

#### Thermodynamic Efficiency vs. Carnot Limit
In a conventional thermal heat engine (combusting $\text{H}_2$ to heat steam), efficiency is strictly bounded by the Carnot limit:
$$\eta_{\text{Carnot}} = 1 - \frac{T_{\text{cold}}}{T_{\text{hot}}} \quad (\approx 40\% - 50\%)$$
In stark contrast, an electrochemical fuel cell is not a heat engine and is **not constrained by the Carnot cycle**. Its theoretical thermodynamic maximum efficiency is given by the ratio of usable electrical work ($\Delta G^\circ$) to total combustion enthalpy ($\Delta H^\circ$):
$$\eta_{\text{thermo}} = \frac{\Delta G^\circ}{\Delta H^\circ} = \frac{-n F E^\circ}{\Delta H^\circ} \tag{8.36}$$
For the reaction $\text{H}_2(g) + \frac{1}{2}\text{O}_2(g) \rightarrow \text{H}_2\text{O}(l)$ at $298.15\text{ K}$:
$$\Delta G^\circ = -237.13\text{ kJ mol}^{-1}, \quad \Delta H^\circ = -285.83\text{ kJ mol}^{-1}$$
$$\eta_{\text{thermo}} = \frac{-237.13}{-285.83} \approx 82.96\% \tag{8.37}$$

### Electrochemical Mechanism of Metallic Corrosion (Rusting of Iron)

Corrosion is the spontaneous, unintended oxidative degradation of a metal through electrochemical interaction with its environmental surroundings. The rusting of iron is a classical multi-step electrochemical corrosion process driven by microscopic galvanic cells formed on the metal surface:

1. **Anodic Sites (Pits, Stressed Grain Boundaries, Scratches)**:
   In regions of mechanical strain or low oxygen concentration, iron oxidizes:
   $$\text{Fe}(s) \longrightarrow \text{Fe}^{2+}(aq) + 2e^- \quad [E^\circ = -0.447\text{ V}] \tag{8.38}$$
2. **Cathodic Sites (Oxygen-Rich Droplet Periphery)**:
   Electrons travel through the bulk conducting iron to oxygenated regions where dissolved oxygen is reduced:
   $$\text{O}_2(g) + 4\text{H}^+(aq) + 4e^- \longrightarrow 2\text{H}_2\text{O}(l) \quad [E^\circ = +1.229\text{ V}]$$
   Or in neutral/alkaline moisture films:
   $$\text{O}_2(g) + 2\text{H}_2\text{O}(l) + 4e^- \longrightarrow 4\text{OH}^-(aq) \quad [E^\circ = +0.401\text{ V}] \tag{8.39}$$
3. **Precipitation of Iron(II) Hydroxide**:
   $\text{Fe}^{2+}$ ions diffuse toward cathodic sites, reacting with $\text{OH}^-$:
   $$\text{Fe}^{2+}(aq) + 2\text{OH}^-(aq) \longrightarrow \text{Fe}(\text{OH})_2(s) \tag{8.40}$$
4. **Further Aerobic Oxidation to Hydrated Iron(III) Oxide (Rust)**:
   $$4\text{Fe}(\text{OH})_2(s) + \text{O}_2(g) + x \text{H}_2\text{O}(l) \longrightarrow 2\text{Fe}_2\text{O}_3 \cdot (x+4)\text{H}_2\text{O}(s) \tag{8.41}$$
   Unlike aluminum or chromium, which form dense, coherent passivating oxide films ($\text{Al}_2\text{O}_3, \text{Cr}_2\text{O}_3$), iron rust is porous and flakes off, constantly exposing fresh underlying metal to accelerated corrosion.

### Corrosion Prevention Strategies

1. **Galvanic Sacrificial Anodes (Cathodic Protection)**:
   Attaching a more electrochemically active metal with a more negative reduction potential than iron (e.g., zinc $E^\circ = -0.76\text{ V}$ or magnesium $E^\circ = -2.37\text{ V}$) forces the iron structure to act entirely as the cathode. The sacrificial zinc or magnesium oxidizes preferentially:
   $$\text{Zn}(s) \longrightarrow \text{Zn}^{2+}(aq) + 2e^-$$
   Used extensively on ocean ship hulls, underground gas pipelines, and offshore oil platforms.
2. **Impressed Current Cathodic Protection (ICCP)**:
   An external DC power supply forces electrons into the protected steel structure, maintaining its electrode potential in the immune region of its thermodynamic Pourbaix diagram.
3. **Barrier Coatings & Passivating Inhibitors**:
   Electroplating (tin plating in food cans, chrome plating), organic polymers (epoxy, paint), and chemical passivators (chromates, nitrites) that promote uniform impervious passivation films."""
            },
            {
                "secNumber": "8.5",
                "title": "Electrolytic Cells, Faraday's Laws & Industrial Electrochemistry",
                "content": r"""In direct contrast to galvanic cells which generate spontaneous electrical energy from chemical reactions, an **Electrolytic Cell** consumes electrical energy from an external DC power source to drive thermodynamically non-spontaneous chemical reactions ($\Delta G > 0$).

### Fundamental Distinctions: Galvanic vs. Electrolytic Cells

| Parameter | Galvanic (Voltaic) Cell | Electrolytic Cell |
| :--- | :--- | :--- |
| **Thermodynamic Spontaneity** | Spontaneous ($\Delta G < 0, E_{\text{cell}} > 0$) | Non-spontaneous ($\Delta G > 0, E_{\text{cell}} < 0$) |
| **Energy Conversion** | Chemical Energy $\longrightarrow$ Electrical Energy | Electrical Energy $\longrightarrow$ Chemical Energy |
| **Anode Sign & Reaction** | **Negative ($-$)**, Oxidation occurs | **Positive ($+$)**, Oxidation occurs |
| **Cathode Sign & Reaction** | **Positive ($+$)**, Reduction occurs | **Negative ($-$)**, Reduction occurs |
| **Electron Flow Direction** | Anode $\longrightarrow$ Cathode (through external circuit) | Anode $\longrightarrow$ Cathode (forced by external DC supply) |
| **Applied Voltage ($V_{\text{app}}$)** | Delivers voltage ($V_{\text{app}} = 0$) | Must exceed decomposition voltage: $V_{\text{app}} > |E_{\text{cell}}| + \eta$ |

> **Universal Invariant Rule of Electrochemistry**:
> In **all** electrochemical cells—without exception:
> * **ANODE is ALWAYS the site of OXIDATION**.
> * **CATHODE is ALWAYS the site of REDUCTION**.
> The polarity sign ($+/-$) switches depending on whether the cell is producing or consuming electrical work!

### Faraday's Laws of Electrolysis

In 1834, Michael Faraday formulated the quantitative laws governing electrolytic transformations:

#### Faraday's First Law
The mass ($m$) of any substance deposited, dissolved, or liberated at an electrode is directly proportional to the total electrical charge ($Q$) passed through the electrolyte:
$$m \propto Q \implies m = Z Q = Z I t \tag{8.42}$$
Where $Z$ is the **electrochemical equivalent** of the substance ($\text{kg C}^{-1}$ or $\text{g C}^{-1}$), $I$ is constant electric current in amperes ($\text{A}$), and $t$ is duration in seconds ($\text{s}$).

#### Faraday's Second Law
When the same quantity of electric charge $Q$ is passed through several different electrolytic solutions connected in series, the masses of different substances liberated are directly proportional to their respective chemical equivalent weights ($\text{EW} = M / z$):
$$\frac{m_1}{\text{EW}_1} = \frac{m_2}{\text{EW}_2} = \dots = \frac{Q}{F} \tag{8.43}$$

#### Unified Mathematical Formulation
Each mole of electrons transferred carries an absolute charge equal to Faraday's constant $F = e N_A \approx 96485.332\text{ C mol}^{-1}$. To discharge one mole of a chemical species with valence / electron stoichiometry $z$, exactly $z$ moles of electrons are required ($Q_{\text{mol}} = z F$).
For a total charge $Q = \int_0^t I(t') dt'$, the total moles of substance produced $n$ is:
$$n = \frac{Q}{z F} = \frac{I t}{z F} \tag{8.44}$$
Multiplying by the molar mass $M$ ($\text{g mol}^{-1}$):
$$m = \frac{I t M}{z F} \tag{8.45}$$
Solving for the electrochemical equivalent $Z$:
$$Z = \frac{M}{z F} \tag{8.46}$$

### Overpotential, Overvoltage & Decomposition Potential

Thermodynamics dictates that to reverse a cell reaction whose standard potential is $E^\circ_{\text{cell}}$, an external voltage $V_{\text{app}} \ge |E^\circ_{\text{cell}}|$ must be applied. However, in practice, a substantially higher voltage—the **decomposition potential ($V_{\text{decomp}}$)**—is required to sustain current flow:
$$V_{\text{decomp}} = |E_{\text{rev}}| + \eta_{\text{anode}} + |\eta_{\text{cathode}}| + I R_{\text{cell}} \tag{8.47}$$
Where:
* $E_{\text{rev}}$ is the reversible equilibrium cell potential.
* $\eta$ is the **overpotential (overvoltage)**: $\eta \equiv E_{\text{actual}} - E_{\text{rev}}$, representing the extra kinetic potential necessary to drive charge transfer at a finite rate.
* $I R_{\text{cell}}$ is the ohmic potential drop across the electrolyte and separator.

Overpotential arises from three distinct physical phenomena:
1. **Activation Overpotential ($\eta_{\text{act}}$)**: Governed by the Butler-Volmer equation; the kinetic barrier to charge transfer across the double layer. Gas evolution reactions ($\text{H}_2$ and $\text{O}_2$) exhibit large activation overpotentials, especially on metals like mercury, lead, or zinc, but very low overpotentials on platinized platinum.
2. **Concentration Overpotential ($\eta_{\text{conc}}$)**: Caused by mass-transport limitations; depletion of reactant ions in the Nernst diffusion layer adjacent to the electrode surface relative to the bulk solution.
3. **Ohmic Overpotential ($\eta_{\text{ohmic}}$)**: Finite ionic conductivity of the electrolyte solution and surface passivation films.

### Competitive Electrode Discharges in Aqueous Solutions

When an aqueous solution is electrolyzed, water itself can undergo competitive oxidation and reduction alongside dissolved solute ions:
* **Possible Cathodic Reductions**:
  $$\text{Metal reduction: } M^{z+}(aq) + z e^- \longrightarrow M(s)$$
  $$\text{Water reduction: } 2\text{H}_2\text{O}(l) + 2e^- \longrightarrow \text{H}_2(g) + 2\text{OH}^-(aq) \quad [E^\circ = -0.828\text{ V at pH } 7]$$
  Cations with standard potentials far more negative than water (such as $\text{Na}^+, \text{K}^+, \text{Ca}^{2+}, \text{Al}^{3+}$) **cannot** be reduced to pure metal in aqueous solution at ordinary cathode materials; water is reduced preferentially to evolve $\text{H}_2$ gas!
* **Possible Anodic Oxidations**:
  $$\text{Anion oxidation: } 2X^-(aq) \longrightarrow X_2 + 2e^-$$
  $$\text{Water oxidation: } 2\text{H}_2\text{O}(l) \longrightarrow \text{O}_2(g) + 4\text{H}^+(aq) + 4e^- \quad [E^\circ = +0.815\text{ V at pH } 7]$$
  Oxoanions with central atoms in their highest oxidation states ($\text{SO}_4^{2-}, \text{NO}_3^-, \text{ClO}_4^-$) are thermodynamically resistant to further oxidation; water is oxidized preferentially to evolve $\text{O}_2$ gas.

### Major Industrial Electrochemical Processes

1. **The Chlor-Alkali Process (Membrane Cell Technology)**:
   Electrolysis of concentrated brine ($\text{NaCl}(aq)$) produces chlorine, hydrogen, and caustic soda ($\text{NaOH}$):
   $$\text{Anode (Titanium coated with RuO}_2/\text{TiO}_2): 2\text{Cl}^-(aq) \longrightarrow \text{Cl}_2(g) + 2e^-$$
   $$\text{Cathode (Nickel mesh)}: 2\text{H}_2\text{O}(l) + 2e^- \longrightarrow \text{H}_2(g) + 2\text{OH}^-(aq)$$
   A perfluorosulfonate cation-exchange membrane (e.g., Nafion) selectively allows $\text{Na}^+$ to migrate from the anolyte to the catholyte while blocking $\text{Cl}^-$ and $\text{OH}^-$, preventing explosive mixing of $\text{Cl}_2$ and $\text{H}_2$ and preventing hypochlorite disproportionation:
   $$2\text{NaCl}(aq) + 2\text{H}_2\text{O}(l) \xrightarrow{\text{electrolysis}} 2\text{NaOH}(aq) + \text{Cl}_2(g) + \text{H}_2(g) \tag{8.48}$$
2. **The Hall-Héroult Process (Aluminum Smelting)**:
   Because $\text{Al}^{3+}$ cannot be reduced in water, alumina ($\text{Al}_2\text{O}_3$) is dissolved in molten cryolite ($\text{Na}_3\text{AlF}_6$) at $\sim 960^\circ\text{C}$:
   $$\text{Cathode (Carbon lining)}: \text{Al}^{3+} + 3e^- \longrightarrow \text{Al}(l)$$
   $$\text{Anode (Consumable Carbon anodes)}: 2\text{O}^{2-} + \text{C}(s) \longrightarrow \text{CO}_2(g) + 4e^-$$
   $$\text{Overall Reaction}: 2\text{Al}_2\text{O}_3(\text{dissolved}) + 3\text{C}(s) \longrightarrow 4\text{Al}(l) + 3\text{CO}_2(g) \tag{8.49}$$
3. **Electrorefining and Electroplating of Copper**:
   Crude impure copper cast as thick slabs acts as the anode in an acidified $\text{CuSO}_4$ bath, while thin pure copper sheets serve as cathodes. At controlled potential ($\sim 0.3\text{ V}$), only copper and more electropositive base impurities ($\text{Fe}, \text{Ni}, \text{Zn}$) dissolve at the anode. At the cathode, only $\text{Cu}^{2+}$ plates out ($E^\circ = +0.34\text{ V}$). Noble impurities ($\text{Ag}, \text{Au}, \text{Pt}$) do not oxidize and fall to the cell floor as valuable **anode slime**."""
            }
        ],
        "problems": [
            {
                "problemNumber": "8.1",
                "tier": "Foundational Level",
                "title": "Comprehensive Daniell Cell Thermodynamic & Potentiometric Analysis",
                "statement": r"""A standard Daniell galvanic cell is assembled at $298.15\text{ K}$ ($25.0^\circ\text{C}$):
$$\text{Zn}(s) \mid \text{Zn}^{2+}(aq, 0.0500\text{ M}) \parallel \text{Cu}^{2+}(aq, 2.500\text{ M}) \mid \text{Cu}(s)$$
Given the standard reduction potentials at $298.15\text{ K}$:
$$E^\circ(\text{Zn}^{2+}/\text{Zn}) = -0.7628\text{ V}, \quad E^\circ(\text{Cu}^{2+}/\text{Cu}) = +0.3419\text{ V}$$
Faraday's constant $F = 96485.332\text{ C mol}^{-1}$, universal gas constant $R = 8.314462\text{ J mol}^{-1}\text{K}^{-1}$.

Calculate:
1. The standard electromotive force $E^\circ_{\text{cell}}$ of the Daniell cell.
2. The standard Gibbs free energy change $\Delta G^\circ$ and the thermodynamic equilibrium constant $K$ at $298.15\text{ K}$.
3. The actual non-standard electromotive force $E_{\text{cell}}$ of this constructed cell.
4. The maximum electrical work $w_{\text{elec}}$ available when $0.150\text{ moles}$ of $\text{Zn}$ dissolve at this cell potential.""",
                "solution": r"""### Step 1: Standard Cell Electromotive Force ($E^\circ_{\text{cell}}$)

Identify the half-reactions and standard reduction potentials:
* **Cathode (Right, Reduction)**: $\text{Cu}^{2+}(aq) + 2e^- \rightarrow \text{Cu}(s) \quad [E^\circ_{\text{cathode}} = +0.3419\text{ V}]$
* **Anode (Left, Oxidation)**: $\text{Zn}(s) \rightarrow \text{Zn}^{2+}(aq) + 2e^- \quad [E^\circ_{\text{anode}} = -0.7628\text{ V}]$

Applying the standard EMF relation:
$$E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = (+0.3419\text{ V}) - (-0.7628\text{ V}) = +1.1047\text{ V}$$

---

### Step 2: Standard Gibbs Free Energy Change ($\Delta G^\circ$) & Equilibrium Constant ($K$)

The balanced cell reaction transfers $n = 2$ moles of electrons:
$$\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightleftharpoons \text{Zn}^{2+}(aq) + \text{Cu}(s)$$
Calculate $\Delta G^\circ$:
$$\Delta G^\circ = -n F E^\circ_{\text{cell}} = -2 \times (96485.332\text{ C mol}^{-1}) \times (1.1047\text{ V})$$
$$\Delta G^\circ = -213193.8\text{ J mol}^{-1} \approx -213.19\text{ kJ mol}^{-1}$$
Since $\Delta G^\circ \ll 0$, the forward reaction is overwhelmingly thermodynamically spontaneous under standard conditions.

Calculate the equilibrium constant $K$:
$$\ln K = \frac{n F E^\circ_{\text{cell}}}{R T} = \frac{2 \times 96485.332 \times 1.1047}{8.314462 \times 298.15} = \frac{213193.8}{2478.956} \approx 86.0014$$
$$K = e^{86.0014} \approx 2.24 \times 10^{37}$$
Using base-10 logarithms:
$$\log_{10} K = \frac{n E^\circ_{\text{cell}}}{0.059159} = \frac{2 \times 1.1047}{0.059159} = 37.3468 \implies K = 10^{37.3468} \approx 2.22 \times 10^{37}$$

---

### Step 3: Non-Standard Cell Potential ($E_{\text{cell}}$) via Nernst Equation

Write the reaction quotient $Q$ for the cell reaction:
$$Q = \frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]} = \frac{0.0500\text{ M}}{2.500\text{ M}} = 0.0200 = \frac{1}{50}$$
Apply the Nernst equation at $298.15\text{ K}$:
$$E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{R T}{n F} \ln Q = 1.1047\text{ V} - \frac{0.059159\text{ V}}{2} \log_{10}(0.0200)$$
$$\log_{10}(0.0200) = \log_{10}(2.0 \times 10^{-2}) = -1.69897$$
$$E_{\text{cell}} = 1.1047\text{ V} - (0.0295795\text{ V}) \times (-1.69897)$$
$$E_{\text{cell}} = 1.1047\text{ V} + 0.05025\text{ V} = +1.1550\text{ V}$$
As predicted by Le Châtelier's principle, diluting the product ion ($\text{Zn}^{2+}$) and concentrating the reactant ion ($\text{Cu}^{2+}$) shifts the chemical driving force forward, raising the cell potential above the standard value by $+0.0503\text{ V}$.

---

### Step 4: Maximum Electrical Work Available

For the reaction of $n_{\text{Zn}} = 0.150\text{ moles}$:
Total moles of electrons transferred: $n_e = 2 \times 0.150 = 0.300\text{ moles of } e^-$.
Total charge passed:
$$Q_{\text{charge}} = n_e F = 0.300\text{ mol} \times 96485.332\text{ C mol}^{-1} = 28945.6\text{ C}$$
The maximum electrical work delivered at $E_{\text{cell}} = 1.1550\text{ V}$ is:
$$w_{\text{elec,max}} = Q_{\text{charge}} \times E_{\text{cell}} = 28945.6\text{ C} \times 1.1550\text{ V} = 33432\text{ J} \approx 33.43\text{ kJ}$$"""
            },
            {
                "problemNumber": "8.2",
                "tier": "Advanced Level",
                "title": "Potentiometric Determination of Silver Chloride $K_{sp}$ & Unknown pH",
                "statement": r"""A high-precision potentiometric cell is designed to evaluate both the solubility product constant $K_{sp}$ of silver chloride ($\text{AgCl}$) and the pH of an unknown acidic solution at $298.15\text{ K}$.

**Part A**: A concentration cell is constructed:
$$\text{Ag}(s) \mid \text{Ag}^+(aq, \text{saturated in } 0.100\text{ M KCl}) \parallel \text{Ag}^+(aq, 0.100\text{ M AgNO}_3) \mid \text{Ag}(s)$$
The measured cell potential is $E_{\text{cell}} = +0.4172\text{ V}$ at $298.15\text{ K}$. Assuming ideal solution behavior ($\gamma_\pm = 1$):
Determine the solubility product constant $K_{sp}$ of $\text{AgCl}$ at $298.15\text{ K}$.

**Part B**: The cathode half-cell is replaced with a Standard Hydrogen Electrode (SHE), and the anode half-cell is replaced with a hydrogen electrode bubbling $\text{H}_2(g)$ at $1.000\text{ bar}$ dipping into an unknown gastric juice sample:
$$\text{Pt}(s) \mid \text{H}_2(g, 1.000\text{ bar}) \mid \text{Gastric Juice (unknown pH)} \parallel \text{H}^+(aq, 1.000\text{ M}) \mid \text{H}_2(g, 1.000\text{ bar}) \mid \text{Pt}(s)$$
The measured cell potential is $E_{\text{cell}} = +0.0986\text{ V}$ at $298.15\text{ K}$.
Determine the hydronium ion activity $[\text{H}^+]$ and the pH of the gastric juice.""",
                "solution": r"""### Part A: Evaluation of $K_{sp}(\text{AgCl})$

In this silver concentration cell:
* **Cathode**: $\text{Ag}^+(aq, c_2) + e^- \rightarrow \text{Ag}(s)$, where $c_2 = [\text{Ag}^+]_{\text{cathode}} = 0.100\text{ M}$.
* **Anode**: $\text{Ag}(s) \rightarrow \text{Ag}^+(aq, c_1) + e^-$, where $c_1 = [\text{Ag}^+]_{\text{anode}}$ is governed by the solubility equilibrium of $\text{AgCl}$ in $0.100\text{ M KCl}$.

Because both electrodes are pure silver, $E^\circ_{\text{cell}} = 0$. The Nernst equation for a 1-electron process ($n = 1$) at $298.15\text{ K}$ gives:
$$E_{\text{cell}} = 0 - \frac{R T}{F} \ln\left(\frac{c_1}{c_2}\right) = \frac{0.059159\text{ V}}{1} \log_{10}\left(\frac{c_2}{c_1}\right)$$
Substitute the measured potential $E_{\text{cell}} = 0.4172\text{ V}$ and $c_2 = 0.100\text{ M}$:
$$0.4172 = 0.059159 \times \log_{10}\left(\frac{0.100}{c_1}\right)$$
$$\log_{10}\left(\frac{0.100}{c_1}\right) = \frac{0.4172}{0.059159} = 7.05218$$
$$\frac{0.100}{c_1} = 10^{7.05218} \approx 1.12767 \times 10^7$$
$$c_1 = [\text{Ag}^+]_{\text{anode}} = \frac{0.100}{1.12767 \times 10^7} = 8.8678 \times 10^{-9}\text{ M}$$

In the anode compartment, the chloride ion concentration is provided overwhelmingly by the strong electrolyte $0.100\text{ M KCl}$:
$$[\text{Cl}^-]_{\text{anode}} \approx 0.100\text{ M}$$
The solubility product expression for $\text{AgCl}(s) \rightleftharpoons \text{Ag}^+(aq) + \text{Cl}^-(aq)$ is:
$$K_{sp} = [\text{Ag}^+][\text{Cl}^-] = (8.8678 \times 10^{-9}\text{ M}) \times (0.100\text{ M}) \approx 1.77 \times 10^{-10}$$
The calculated value $K_{sp} \approx 1.77 \times 10^{-10}$ matches literature values perfectly.

---

### Part B: Evaluation of Unknown Gastric Juice pH

The cell diagram represents a hydrogen concentration cell:
* **Cathode (SHE)**: $2\text{H}^+(aq, 1.000\text{ M}) + 2e^- \rightarrow \text{H}_2(g, 1\text{ bar}) \quad [E^\circ = 0.000\text{ V}]$
* **Anode**: $\text{H}_2(g, 1\text{ bar}) \rightarrow 2\text{H}^+(aq, \text{unknown}) + 2e^-$
* **Net Cell Reaction**: $2\text{H}^+(aq, 1.000\text{ M}) \rightarrow 2\text{H}^+(aq, \text{unknown})$

Applying the Nernst equation ($n = 2$):
$$E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{R T}{2 F} \ln\left(\frac{[\text{H}^+]_{\text{unknown}}^2}{[\text{H}^+]_{\text{SHE}}^2}\right)$$
Since $E^\circ_{\text{cell}} = 0$ and $[\text{H}^+]_{\text{SHE}} = 1.000\text{ M}$:
$$E_{\text{cell}} = -\frac{R T}{2 F} \ln\left([\text{H}^+]_{\text{unknown}}^2\right) = -\frac{R T}{F} \ln[\text{H}^+]_{\text{unknown}} = \frac{2.302585 R T}{F} \times \left(-\log_{10}[\text{H}^+]_{\text{unknown}}\right)$$
Recalling the definition of pH: $\text{pH} \equiv -\log_{10}[\text{H}^+]$:
$$E_{\text{cell}} = 0.059159\text{ V} \times \text{pH}$$
Solving directly for $\text{pH}$:
$$\text{pH} = \frac{E_{\text{cell}}}{0.059159\text{ V}} = \frac{0.0986\text{ V}}{0.059159\text{ V}} \approx 1.667 \approx 1.67$$
Calculate the hydronium ion activity:
$$[\text{H}^+] = 10^{-\text{pH}} = 10^{-1.667} \approx 0.0215\text{ M}$$
The gastric juice has a pH of $1.67$, characteristic of human stomach acid."""
            },
            {
                "problemNumber": "8.3",
                "tier": "Honors / Proof Challenge",
                "title": "Thermodynamic State Function Profiling ($\Delta G^\circ, \Delta S^\circ, \Delta H^\circ, \Delta C_p^\circ$) from Quadratic Potentiometric Temperature Data",
                "statement": r"""A reversible electrochemical cell is constructed:
$$\text{Pt}(s) \mid \text{H}_2(g, 1.000\text{ bar}) \mid \text{HCl}(aq, m = 0.0100\text{ mol kg}^{-1}) \mid \text{AgCl}(s) \mid \text{Ag}(s)$$
Over the temperature interval $273.15\text{ K} \le T \le 343.15\text{ K}$, the measured standard cell electromotive force $E^\circ(T)$ in volts is parameterized by the quadratic polynomial function:
$$E^\circ(T) = a + b(T - T_0) + c(T - T_0)^2$$
Where the reference temperature $T_0 = 298.15\text{ K}$, and the empirical coefficients are:
$$a = 0.22240\text{ V}, \quad b = -6.450 \times 10^{-4}\text{ V K}^{-1}, \quad c = -3.200 \times 10^{-6}\text{ V K}^{-2}$$
Constants: $F = 96485.332\text{ C mol}^{-1}, R = 8.314462\text{ J mol}^{-1}\text{K}^{-1}$.

1. **Derive the general analytical expressions** for $\Delta G^\circ(T)$, $\Delta S^\circ(T)$, $\Delta H^\circ(T)$, and $\Delta C_p^\circ(T)$ as explicit functions of temperature $T$.
2. **Calculate the precise numerical values** of $E^\circ$, $\Delta G^\circ$, $\Delta S^\circ$, $\Delta H^\circ$, and $\Delta C_p^\circ$ for the cell reaction at standard temperature $T = 298.15\text{ K}$.
3. **Prove whether the cell absorbs or releases heat** when operated reversibly and isothermally at $298.15\text{ K}$, and calculate the reversible heat flow $q_{\text{rev}}$ per mole of reaction.
4. **Determine the inversion temperature $T_{\text{inv}}$** at which the reaction entropy $\Delta S^\circ$ changes sign, if one exists within or near the physical range.""",
                "solution": r"""### Step 1: Analytical Derivations of Thermodynamic Functions

The overall cell reaction is:
$$\frac{1}{2}\text{H}_2(g) + \text{AgCl}(s) \longrightarrow \text{Ag}(s) + \text{H}^+(aq) + \text{Cl}^-(aq)$$
The number of electrons transferred per mole of reaction is $n = 1$.

Given the polynomial expansion:
$$E^\circ(T) = a + b(T - T_0) + c(T - T_0)^2$$
Compute the first and second temperature derivatives:
$$\left(\frac{\partial E^\circ}{\partial T}\right)_P = b + 2c(T - T_0) \tag{1}$$
$$\left(\frac{\partial^2 E^\circ}{\partial T^2}\right)_P = 2c \tag{2}$$

#### 1. Standard Gibbs Free Energy Change:
$$\Delta G^\circ(T) = -n F E^\circ(T) = -F [a + b(T - T_0) + c(T - T_0)^2] \tag{3}$$

#### 2. Standard Reaction Entropy:
From fundamental thermodynamics, $\left(\frac{\partial \Delta G^\circ}{\partial T}\right)_P = -\Delta S^\circ$, therefore:
$$\Delta S^\circ(T) = n F \left(\frac{\partial E^\circ}{\partial T}\right)_P = F [b + 2c(T - T_0)] \tag{4}$$

#### 3. Standard Reaction Enthalpy:
From $\Delta G^\circ = \Delta H^\circ - T \Delta S^\circ$:
$$\Delta H^\circ(T) = \Delta G^\circ + T \Delta S^\circ = -F E^\circ(T) + T F \left(\frac{\partial E^\circ}{\partial T}\right)_P$$
$$\Delta H^\circ(T) = -F \left[ a + b(T - T_0) + c(T - T_0)^2 \right] + F T [b + 2c(T - T_0)]$$
$$\Delta H^\circ(T) = -F \left\{ a + b(T - T_0) - T [b + 2c(T - T_0)] + c(T - T_0)^2 \right\} \tag{5}$$

#### 4. Constant-Pressure Heat Capacity Change:
$$\Delta C_p^\circ(T) = T \left(\frac{\partial \Delta S^\circ}{\partial T}\right)_P = n F T \left(\frac{\partial^2 E^\circ}{\partial T^2}\right)_P = 2 c F T \tag{6}$$

---

### Step 2: Numerical Evaluations at Standard Reference Temperature ($T = T_0 = 298.15\text{ K}$)

At $T = T_0$, the terms $(T - T_0) = 0$.

1. **Standard Cell Potential**:
   $$E^\circ(298.15\text{ K}) = a = 0.22240\text{ V}$$
2. **First Derivative**:
   $$\left(\frac{\partial E^\circ}{\partial T}\right)_P = b = -6.450 \times 10^{-4}\text{ V K}^{-1}$$
3. **Second Derivative**:
   $$\left(\frac{\partial^2 E^\circ}{\partial T^2}\right)_P = 2c = 2 \times (-3.200 \times 10^{-6}) = -6.400 \times 10^{-6}\text{ V K}^{-2}$$

#### Calculate $\Delta G^\circ(298.15\text{ K})$:
$$\Delta G^\circ = -1 \times (96485.332\text{ C mol}^{-1}) \times (0.22240\text{ V}) = -21458.34\text{ J mol}^{-1} \approx -21.46\text{ kJ mol}^{-1}$$

#### Calculate $\Delta S^\circ(298.15\text{ K})$:
$$\Delta S^\circ = 1 \times (96485.332\text{ C mol}^{-1}) \times (-6.450 \times 10^{-4}\text{ V K}^{-1}) = -62.233\text{ J K}^{-1}\text{mol}^{-1}$$

#### Calculate $\Delta H^\circ(298.15\text{ K})$:
$$\Delta H^\circ = \Delta G^\circ + T \Delta S^\circ$$
$$\Delta H^\circ = -21458.34\text{ J mol}^{-1} + (298.15\text{ K}) \times (-62.233\text{ J K}^{-1}\text{mol}^{-1})$$
$$\Delta H^\circ = -21458.34 - 18554.77 = -40013.11\text{ J mol}^{-1} \approx -40.01\text{ kJ mol}^{-1}$$

#### Calculate $\Delta C_p^\circ(298.15\text{ K})$:
$$\Delta C_p^\circ = 2 c F T = 2 \times (-3.200 \times 10^{-6}\text{ V K}^{-2}) \times (96485.332\text{ C mol}^{-1}) \times (298.15\text{ K})$$
$$\Delta C_p^\circ = (-6.175 \times 10^{-1}\text{ J K}^{-2}\text{mol}^{-1}) \times 298.15\text{ K} = -184.11\text{ J K}^{-1}\text{mol}^{-1}$$

---

### Step 3: Reversible Heat Flow ($q_{\text{rev}}$) & Thermal Behavior

For a reversible isothermal electrochemical process:
$$q_{\text{rev}} = T \Delta S^\circ = (298.15\text{ K}) \times (-62.233\text{ J K}^{-1}\text{mol}^{-1}) = -18554.8\text{ J mol}^{-1} \approx -18.55\text{ kJ mol}^{-1}$$
Since $q_{\text{rev}} < 0$, the cell **releases heat to the surroundings** (exothermic thermal exchange) during reversible discharge.
Notice that the electrical work produced ($w_{\text{elec}} = -\Delta G^\circ = +21.46\text{ kJ}$) is less than the total enthalpy released ($-\Delta H^\circ = +40.01\text{ kJ}$); the surplus energy ($18.55\text{ kJ}$) is discharged as waste heat because the reaction produces an ordered system ($\Delta S^\circ < 0$, due to organizing water dipoles around hydrated $\text{H}^+$ and $\text{Cl}^-$ ions).

---

### Step 4: Inversion Temperature Analysis ($T_{\text{inv}}$)

The condition for $\Delta S^\circ(T) = 0$ requires:
$$b + 2c(T_{\text{inv}} - T_0) = 0 \implies T_{\text{inv}} - T_0 = -\frac{b}{2c}$$
Substitute numerical values:
$$T_{\text{inv}} - 298.15 = -\frac{-6.450 \times 10^{-4}}{2 \times (-3.200 \times 10^{-6})} = -\frac{-6.450 \times 10^{-4}}{-6.400 \times 10^{-6}} = -100.78\text{ K}$$
$$T_{\text{inv}} = 298.15 - 100.78 = 197.37\text{ K} \quad (-75.8^\circ\text{C})$$
At $T_{\text{inv}} \approx 197.4\text{ K}$, the temperature coefficient vanishes $\left(\frac{\partial E^\circ}{\partial T}\right)_P = 0$, meaning cell EMF reaches an extremum (maximum) and the cell operates with zero reversible heat exchange ($q_{\text{rev}} = 0$, $100\%$ conversion of reaction enthalpy into electrical work). However, this temperature lies well below the freezing point of the aqueous electrolyte ($273.15\text{ K}$), confirming that $\Delta S^\circ$ remains negative across the entire liquid operating range."""
            }
        ]
    }
'''

with open("build_pchem1_unit8.py", "w", encoding="utf-8") as f:
    f.write(content)

print("build_pchem1_unit8.py written successfully.")
