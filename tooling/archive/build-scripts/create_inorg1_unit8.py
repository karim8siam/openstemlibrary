#!/usr/bin/env python3
"""
create_inorg1_unit8.py
Generates build_inorg1_unit8.py for Unit 8:
Inorganic Chemical Reactions: Precipitation, Redox Spontaneity & Potential Diagrams
"""

import sys

content = r'''# -*- coding: utf-8 -*-
"""
Unit 8: Inorganic Chemical Reactions: Precipitation, Redox Spontaneity & Potential Diagrams
Contains 5 comprehensive sections and 3 tiered solved problems with full derivations.
"""

def get_unit8():
    return {
        "id": "unit8",
        "title": "Unit 8: Inorganic Chemical Reactions: Precipitation, Redox Spontaneity & Potential Diagrams",
        "simId": "sim_chem_redox_latimer_frost_diagram",
        "simTitle": "Latimer, Frost & Pourbaix Potential Engine",
        "sections": [
            {
                "id": "sec8_1",
                "title": "§8.1 Precipitation Equilibria & Solubility Product Constant ($K_{sp}$), Common-Ion Effect & Complexation",
                "content": r"""### Heterogeneous Ionic Dissolution Equilibria

In aqueous inorganic chemistry, the dissolution of a sparingly soluble symmetrical or asymmetrical crystalline salt $\text{M}_p\text{X}_q(s)$ establishes a dynamic heterogeneous equilibrium between the solid phase and solvated ions:
$$\text{M}_p\text{X}_q(s) \rightleftharpoons p\,\text{M}^{z+}(aq) + q\,\text{X}^{z-}(aq)$$

Thermodynamic equilibrium is defined by the equality of chemical potentials:
$$\mu[\text{M}_p\text{X}_q(s)] = p\,\mu[\text{M}^{z+}(aq)] + q\,\mu[\text{X}^{z-}(aq)]$$
Since the activity of a pure solid phase at standard state is unity ($a_{\text{solid}} = 1$), the thermodynamic equilibrium constant is the **Solubility Product Constant** ($K_{sp}^\circ$):
$$K_{sp}^\circ = (a_{\text{M}^{z+}})^p (a_{\text{X}^{z-}})^q = (\gamma_+ [\text{M}^{z+}])^p (\gamma_- [\text{X}^{z-}])^q$$

In dilute solutions where activity coefficients approach unity ($\gamma_\pm \approx 1$), the concentration-based solubility product is:
$$K_{sp} \approx [\text{M}^{z+}]^p [\text{X}^{z-}]^q$$

#### Molar Solubility ($S$) Formulations:
If $S$ denotes the molar solubility of $\text{M}_p\text{X}_q$ in pure water (mol/L):
$$[\text{M}^{z+}] = p S \quad \text{and} \quad [\text{X}^{z-}] = q S$$
$$K_{sp} = (p S)^p (q S)^q = p^p q^q S^{p+q}$$
$$S = \left( \frac{K_{sp}}{p^p q^q} \right)^{\frac{1}{p+q}}$$

- For a $1:1$ salt ($\text{AgCl}, \text{BaSO}_4$): $p=1, q=1 \implies K_{sp} = S^2 \implies S = \sqrt{K_{sp}}$.
- For a $1:2$ or $2:1$ salt ($\text{PbI}_2, \text{Ag}_2\text{CrO}_4, \text{CaF}_2$): $p=1, q=2 \implies K_{sp} = 4 S^3 \implies S = \left(\frac{K_{sp}}{4}\right)^{1/3}$.
- For a $1:3$ salt ($\text{Fe(OH)}_3, \text{Al(OH)}_3$): $p=1, q=3 \implies K_{sp} = 27 S^4 \implies S = \left(\frac{K_{sp}}{27}\right)^{1/4}$.
- For a $2:3$ salt ($\text{Bi}_2\text{S}_3, \text{Ca}_3(\text{PO}_4)_2$): $p=2, q=3 \implies K_{sp} = 108 S^5 \implies S = \left(\frac{K_{sp}}{108}\right)^{1/5}$.

---

### The Common-Ion Effect & Le Chatelier's Principle

When an electrolyte containing an ion common to the sparingly soluble salt is added to the saturated solution, Le Chatelier's Principle dictates that the dissolution equilibrium shifts to the left, precipitating additional solid and drastically suppressing molar solubility.

Consider the dissolution of $\text{PbI}_2$ ($K_{sp} = 7.9 \times 10^{-9}$) in the presence of $0.10\text{ M }\text{KI}$:
- Iodide concentration: $[\text{I}^-] = 0.10 + 2S' \approx 0.10\text{ M}$ (since $2S' \ll 0.10$).
- Lead concentration: $[\text{Pb}^{2+}] = S'$.
$$K_{sp} = [\text{Pb}^{2+}][\text{I}^-]^2 \implies 7.9 \times 10^{-9} = S' (0.10)^2 \implies S' = \frac{7.9 \times 10^{-9}}{0.010} = \mathbf{7.9 \times 10^{-7}\text{ M}}$$
Compared to its solubility in pure water ($S = \left(\frac{7.9\times 10^{-9}}{4}\right)^{1/3} = 1.25 \times 10^{-3}\text{ M}$), the presence of $0.10\text{ M}$ common ion depresses solubility by a factor of nearly **$1600$-fold**!

---

### Dissolution via Coordination Complex Formation

Precipitates can be quantitatively redissolved by introducing competing Lewis base ligands that sequester the metal cation into an extraordinarily stable coordination complex with an astronomical formation constant ($\beta_n \gg 1$).

```
        AgCl(s) <===========> Ag+(aq) + Cl-(aq)           K_sp = 1.8 x 10^-10
                                 ^
                                 |  + 2 NH3(aq)           β_2 = 1.7 x 10^7
                                 v
                            [Ag(NH3)2]+(aq)
        ----------------------------------------------------------------------
        Net: AgCl(s) + 2 NH3(aq) <===> [Ag(NH3)2]+(aq) + Cl-(aq)   K_net = 3.0 x 10^-3
```

#### Analytical Coupling of Equilibria:
1. Precipitation: $\text{AgCl}(s) \rightleftharpoons \text{Ag}^+(aq) + \text{Cl}^-(aq), \quad K_{sp} = 1.8 \times 10^{-10}$
2. Complexation: $\text{Ag}^+(aq) + 2\,\text{NH}_3(aq) \rightleftharpoons [\text{Ag}(\text{NH}_3)_2]^+(aq), \quad \beta_2 = 1.7 \times 10^7$
3. Overall Dissolution Reaction:
   $$\text{AgCl}(s) + 2\,\text{NH}_3(aq) \rightleftharpoons [\text{Ag}(\text{NH}_3)_2]^+(aq) + \text{Cl}^-(aq)$$
   $$K_{\text{net}} = K_{sp} \times \beta_2 = (1.8 \times 10^{-10}) \times (1.7 \times 10^7) = \mathbf{3.06 \times 10^{-3}}$$
This coupled equilibrium explains why sparingly soluble silver chloride dissolves completely in excess aqueous ammonia, whereas silver iodide ($\text{AgI}$, $K_{sp} = 8.5 \times 10^{-17}$, $K_{\text{net}} \approx 1.4 \times 10^{-9}$) remains completely insoluble in aqueous ammonia."""
            },
            {
                "id": "sec8_2",
                "title": "§8.2 Oxidation Numbers, Balancing Redox Equations in Acidic and Basic Media",
                "content": r"""### The Formalism of Oxidation Numbers

An **oxidation number** (oxidation state, $OS$) is a formal bookkeeping number assigned to an atom in a chemical compound representing the hypothetical electrical charge the atom would retain if all shared covalent electron pairs were cleaved purely heterolytically, allocating both bonding electrons entirely to the more electronegative bonding partner.

#### Priority Rules for Assigning Oxidation States:
1. **Elemental State**: Atoms in uncombined pure elements have $OS = 0$ ($\text{Na}, \text{O}_2, \text{P}_4, \text{S}_8$).
2. **Monatomic Ions**: Oxidation state equals ionic charge ($\text{Fe}^{3+} \implies +3$, $\text{Cl}^- \implies -1$).
3. **Fluorine**: Almost universally $-1$ in all compounds due to highest electronegativity ($\chi = 3.98$).
4. **Oxygen**: Almost universally $-2$, with rigorous exceptions:
   - In peroxides ($\text{H}_2\text{O}_2, \text{O}_2^{2-}$): $-1$.
   - In superoxides ($\text{KO}_2, \text{O}_2^-$): $-\frac{1}{2}$.
   - In oxygen difluoride ($\text{OF}_2$): $+2$ (since fluorine is more electronegative).
5. **Hydrogen**: $+1$ when bonded to nonmetals; $-1$ when bonded to electropositive metals (hydrides like $\text{NaH}, \text{CaH}_2$).
6. **Alkali & Alkaline Earth Metals**: Group 1 metals are strictly $+1$; Group 2 metals are strictly $+2$.
7. **Conservation**: The algebraic sum of oxidation numbers across all atoms in a neutral molecule must equal zero; in a polyatomic ion, it must equal the net charge $q$.

---

### The Ion-Electron (Half-Reaction) Method

Balancing complex polyatomic oxidation-reduction reactions requires partitioning the process into two simultaneous half-reactions: the **oxidation half-reaction** (loss of electrons) and the **reduction half-reaction** (gain of electrons).

```
   Stepwise Algorithm for Balancing Redox Equations:
   
   1. Identify oxidized and reduced species and split into two half-reactions.
   2. Balance all atoms other than Hydrogen and Oxygen.
   3. Balance Oxygen atoms by adding H2O molecules.
   4. Balance Hydrogen atoms:
      * In ACIDIC media: add H+ ions.
      * In BASIC media: add H2O to the deficient side and OH- to the opposite side.
   5. Balance electrical charges by adding electrons (e-).
   6. Multiply half-reactions by integers to equate electrons transferred.
   7. Add half-reactions, cancel identical spectator species, and verify conservation.
```

#### Detailed Example: Permanganate Oxidation of Nitrite in Acidic Solution
$$\text{MnO}_4^-(aq) + \text{NO}_2^-(aq) \xrightarrow{\text{acidic}} \text{Mn}^{2+}(aq) + \text{NO}_3^-(aq)$$

1. **Reduction Half-Reaction ($\text{Mn}^{+7} \rightarrow \text{Mn}^{+2}$)**:
   - Balance Mn: $\text{MnO}_4^- \rightarrow \text{Mn}^{2+}$.
   - Balance Oxygen by adding $4\,\text{H}_2\text{O}$ to product side: $\text{MnO}_4^- \rightarrow \text{Mn}^{2+} + 4\,\text{H}_2\text{O}$.
   - Balance Hydrogen by adding $8\,\text{H}^+$ to reactant side: $\text{MnO}_4^- + 8\,\text{H}^+ \rightarrow \text{Mn}^{2+} + 4\,\text{H}_2\text{O}$.
   - Balance charge ($+7$ on left, $+2$ on right $\implies$ add $5e^-$ to left):
     $$\text{MnO}_4^- + 8\,\text{H}^+ + 5e^- \longrightarrow \text{Mn}^{2+} + 4\,\text{H}_2\text{O} \quad [\times 2]$$

2. **Oxidation Half-Reaction ($\text{N}^{+3} \rightarrow \text{N}^{+5}$)**:
   - Balance N: $\text{NO}_2^- \rightarrow \text{NO}_3^-$.
   - Balance Oxygen by adding $1\,\text{H}_2\text{O}$ to reactant side: $\text{NO}_2^- + \text{H}_2\text{O} \rightarrow \text{NO}_3^-$.
   - Balance Hydrogen by adding $2\,\text{H}^+$ to product side: $\text{NO}_2^- + \text{H}_2\text{O} \rightarrow \text{NO}_3^- + 2\,\text{H}^+$.
   - Balance charge ($-1$ on left, $+1$ on right $\implies$ add $2e^-$ to right):
     $$\text{NO}_2^- + \text{H}_2\text{O} \longrightarrow \text{NO}_3^- + 2\,\text{H}^+ + 2e^- \quad [\times 5]$$

3. **Electron Harmonization and Net Equation**:
   Multiply reduction by 2 ($10e^-$) and oxidation by 5 ($10e^-$):
   $$2\,\text{MnO}_4^- + 16\,\text{H}^+ + 10e^- + 5\,\text{NO}_2^- + 5\,\text{H}_2\text{O} \longrightarrow 2\,\text{Mn}^{2+} + 8\,\text{H}_2\text{O} + 5\,\text{NO}_3^- + 10\,\text{H}^+ + 10e^-$$
   Canceling $10e^-$, $10\,\text{H}^+$, and $5\,\text{H}_2\text{O}$:
   $$\mathbf{2\,\text{MnO}_4^-(aq) + 5\,\text{NO}_2^-(aq) + 6\,\text{H}^+(aq) \longrightarrow 2\,\text{Mn}^{2+}(aq) + 5\,\text{NO}_3^-(aq) + 3\,\text{H}_2\text{O}(l)}$$
   - Mass check: $2\text{ Mn}, 23\text{ O}, 5\text{ N}, 6\text{ H}$ on both sides.
   - Charge check: $2(-1) + 5(-1) + 6(+1) = -1$ on both sides! Verified."""
            },
            {
                "id": "sec8_3",
                "title": "§8.3 Electrochemical Thermodynamics: Potentials, Gibbs Energy & The Nernst Equation",
                "content": r"""### Thermodynamics of Reversible Electrochemical Cells

The fundamental link uniting thermodynamics and electrochemistry is that the maximum non-expansion electrical work ($w_{\text{elec}}$) obtainable from a reversible electrochemical reaction under isothermal, isobaric conditions equals the decrease in Gibbs Free Energy ($\Delta G$):
$$w_{\text{max}} = \Delta G$$

For an electrochemical process transferring $n$ moles of electrons across a potential difference of cell electromotive force $E_{\text{cell}}$:
$$w_{\text{elec}} = -q E_{\text{cell}} = -n F E_{\text{cell}}$$
where $F = N_A e = 96485.33\text{ C}\cdot\text{mol}^{-1}$ is the **Faraday Constant**.
Therefore:
$$\Delta G = -n F E_{\text{cell}} \quad \text{and} \quad \Delta G^\circ = -n F E_{\text{cell}}^\circ$$

#### Thermodynamic Spontaneity Criteria at Constant $T$ and $P$:
- If $E_{\text{cell}} > 0 \implies \Delta G < 0$: The forward redox reaction is **thermodynamically spontaneous**.
- If $E_{\text{cell}} < 0 \implies \Delta G > 0$: The reaction is **non-spontaneous** in the forward direction.
- If $E_{\text{cell}} = 0 \implies \Delta G = 0$: The electrochemical system is at **dynamic equilibrium**.

---

### Derivation of the Nernst Equation

From classical chemical thermodynamics, the Gibbs free energy change of a chemical mixture is related to the reaction quotient $Q$ by:
$$\Delta G = \Delta G^\circ + RT \ln Q$$

Substituting $\Delta G = -n F E_{\text{cell}}$ and $\Delta G^\circ = -n F E_{\text{cell}}^\circ$:
$$-n F E_{\text{cell}} = -n F E_{\text{cell}}^\circ + RT \ln Q$$

Dividing through by $-n F$ yields the **Nernst Equation**:
$$E_{\text{cell}} = E_{\text{cell}}^\circ - \frac{RT}{n F} \ln Q$$

At standard temperature $T = 298.15\text{ K}$ ($25.0^\circ\text{C}$), evaluating the numerical constant:
$$\frac{RT}{F} \ln(10) = \frac{(8.31446\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (298.15\text{ K})}{96485.33\text{ C}\cdot\text{mol}^{-1}} \times 2.302585 = 0.05916\text{ V}$$

Thus, the practical operational form of the Nernst equation is:
$$E = E^\circ - \frac{0.05916}{n} \log_{10} Q \quad (\text{at } 298.15\text{ K})$$

---

### Equilibrium Constant and Electrochemical Potential

At dynamic electrochemical equilibrium, the cell potential vanishes ($E = 0$) and the reaction quotient equals the equilibrium constant ($Q = K$):
$$0 = E^\circ - \frac{RT}{n F} \ln K \implies \ln K = \frac{n F E^\circ}{RT}$$
$$\log_{10} K = \frac{n E^\circ}{0.05916} \quad (\text{at } 298.15\text{ K})$$
$$K = 10^{\frac{n E^\circ}{0.05916}}$$

#### Temperature Dependence of EMF:
Differentiating $\Delta G^\circ = -n F E^\circ$ with respect to temperature:
$$\left( \frac{\partial \Delta G^\circ}{\partial T} \right)_P = -\Delta S^\circ \implies -n F \left( \frac{\partial E^\circ}{\partial T} \right)_P = -\Delta S^\circ$$
$$\Delta S^\circ = n F \left( \frac{\partial E^\circ}{\partial T} \right)_P$$
$$\Delta H^\circ = \Delta G^\circ + T \Delta S^\circ = -n F E^\circ + n F T \left( \frac{\partial E^\circ}{\partial T} \right)_P$$
By measuring the temperature coefficient of cell EMF $\left(\frac{\partial E^\circ}{\partial T}\right)_P$, the standard enthalpy and entropy of reaction can be directly determined without calorimetric measurements!"""
            },
            {
                "id": "sec8_4",
                "title": "§8.4 Latimer Diagrams: Sequential Redox Steps, Disproportionation & Comproportionation",
                "content": r"""### Principles of Latimer Potential Diagrams

A **Latimer Diagram** (introduced by Wendell M. Latimer in 1938) provides a concise, quantitative graphical representation of the standard reduction potentials connecting consecutive oxidation states of a chemical element.

In a Latimer diagram:
- Chemical species are arranged horizontally from left to right in order of **decreasing oxidation state**.
- Numerical standard reduction potentials ($E^\circ$, in Volts) are written above the connecting arrows.
- Potential diagrams are strongly $pH$-dependent and are reported either for standard acidic solution ($pH = 0$, $[H^+] = 1.0\text{ M}$) or standard basic solution ($pH = 14$, $[OH^-] = 1.0\text{ M}$).

```
   Archetype Latimer Diagram for Chlorine in Acidic Solution (pH = 0):
   
   +7             +5             +3             +1             0              -1
   ClO4- --+1.20--> ClO3- --+1.18--> HClO2 --+1.67--> HClO --+1.63--> Cl2 --+1.36--> Cl-
     \                                                                         /
      \----------------------------- +1.39 V ---------------------------------/
```

---

### The Fundamental Rule for Non-Adjacent Redox Steps

**CRITICAL PRINCIPLE**: *Electrochemical potentials are intensive variables and CANNOT be added directly! ($E^\circ_{\text{net}} \neq E^\circ_1 + E^\circ_2$)*.
Standard Gibbs free energies, however, are extensive state functions and **must add algebraically**:
$$\Delta G_{\text{net}}^\circ = \Delta G_1^\circ + \Delta G_2^\circ + \dots + \Delta G_k^\circ$$
Substituting $\Delta G^\circ = -n F E^\circ$:
$$-n_{\text{net}} F E_{\text{net}}^\circ = -n_1 F E_1^\circ - n_2 F E_2^\circ - \dots - n_k F E_k^\circ$$
Canceling $-F$ yields the **Latimer Potential Rule**:
$$\mathbf{E_{\text{net}}^\circ = \frac{\sum_{i=1}^k n_i E_i^\circ}{n_{\text{net}}} = \frac{n_1 E_1^\circ + n_2 E_2^\circ + \dots + n_k E_k^\circ}{n_1 + n_2 + \dots + n_k}}$$

---

### Thermodynamic Criteria for Disproportionation and Comproportionation

#### 1. Disproportionation:
Disproportionation is a redox reaction in which an intermediate chemical species in oxidation state $N$ simultaneously undergoes self-oxidation to $N+x$ and self-reduction to $N-y$:
$$2\,\text{A}^{(N)} \longrightarrow \text{A}^{(N+x)} + \text{A}^{(N-y)}$$

Consider the sequence in a Latimer diagram:
$$A \xrightarrow{E_{\text{left}}^\circ} B \xrightarrow{E_{\text{right}}^\circ} C$$
For species $B$ to disproportionate into $A$ and $C$:
- Reduction half-reaction: $B + n_R e^- \rightarrow C, \quad E_{\text{red}}^\circ = E_{\text{right}}^\circ$
- Oxidation half-reaction: $B \rightarrow A + n_L e^-, \quad E_{\text{ox}}^\circ = -E_{\text{left}}^\circ$
- Net Cell Potential:
  $$E_{\text{cell}}^\circ = E_{\text{red}}^\circ - E_{\text{ox-potential}} = E_{\text{right}}^\circ - E_{\text{left}}^\circ$$

For the reaction to be thermodynamically spontaneous ($\Delta G^\circ < 0 \iff E_{\text{cell}}^\circ > 0$):
$$\mathbf{E_{\text{right}}^\circ > E_{\text{left}}^\circ}$$

> **The Disproportionation Rule**: *In a Latimer diagram, an intermediate oxidation state is thermodynamically unstable toward disproportionation if the standard reduction potential to its right is GREATER than the reduction potential to its left!*

#### 2. Comproportionation (Synproportionation):
The reverse of disproportionation: two different species containing the same element in distinct oxidation states react spontaneously to generate a single intermediate oxidation state:
$$A + C \longrightarrow 2\,B$$
Comproportionation is thermodynamically spontaneous when:
$$\mathbf{E_{\text{left}}^\circ > E_{\text{right}}^\circ}$$"""
            },
            {
                "id": "sec8_5",
                "title": "§8.5 Frost & Pourbaix ($pH$-Potential) Diagrams: Thermodynamic Landscapes & Passivation",
                "content": r"""### Frost Diagrams (Arthur Frost, 1951)

While a Latimer diagram encodes numerical potentials, a **Frost Diagram** (also called an oxidation state diagram) provides an intuitive, comprehensive visual plot of the thermodynamic stability landscape of an entire element across all its oxidation states.

- **Abscissa ($x$-axis)**: Formal oxidation state ($N$).
- **Ordinate ($y$-axis)**: Standard free energy parameter $-n F E^\circ / F$ relative to the zero-valent element, plotted as:
  $$\frac{\Delta G^\circ}{F} = -N E^\circ(A^{(N)} / A^{(0)}) \quad \text{(measured in Volts)}$$

```
   Frost Diagram Anatomy:
   
   ΔG° / F (Volts)
    ^
    |          Oxidizing Agent (Top Left)
    |             *
    |            / \
    |           /   * <-- Convex Peak (Thermodynamically unstable to DISPROPORTIONATION!)
    |          /     \
    |   0 --- *-------*------------------- (Zero-valent element N = 0)
    |          \     /
    |           \   * <-- Concave Well (Thermodynamically STABLE species!)
    |            \ /
    |             *  <-- Thermodynamic Sink (Most stable state in system)
    +-------------------------------------------> Oxidation State N
```

#### Fundamental Graphical Theorems of Frost Diagrams:
1. **Slope Represents Standard Potential**: The slope of the line segment connecting two species in oxidation states $N_1$ and $N_2$ equals the standard reduction potential $E^\circ$ of the couple connecting them:
   $$\text{Slope} = \frac{(\Delta G_2^\circ / F) - (\Delta G_1^\circ / F)}{N_2 - N_1} = E^\circ(N_2 / N_1)$$
   - Steeper positive slope $\implies$ more powerful oxidizing couple.
   - Steeper negative slope $\implies$ more powerful reducing couple.
2. **Concave Wells (Valleys) are Thermodynamically Stable**: If a species lies in a concave trough below the chord connecting its flanking neighbors, it is thermodynamically immune to disproportionation, and the flanking species will spontaneously comproportionate into it.
3. **Convex Peaks (Humps) Undergo Disproportionation**: If a species lies above the straight line connecting two adjacent states, it is thermodynamically unstable and will spontaneously disproportionate into those states.
4. **Thermodynamic Sink**: The lowest point on the entire diagram is the most thermodynamically stable oxidation state of that element in the specified medium.

---

### Pourbaix ($pH$-Potential) Phase Diagrams (Marcel Pourbaix, 1945)

A **Pourbaix Diagram** maps out the predominant, thermodynamically stable chemical forms of an element in aqueous solution as a function of both **Electrochemical Potential ($E$)** (oxidizing/reducing driving force) and **Solution Acidity ($pH$)**.

#### The Three Structural Types of Phase Boundaries:
1. **Horizontal Boundaries (Pure Electron Transfer, pH-Independent)**:
   Involve redox reactions with zero proton participation:
   $$\text{Fe}^{3+}(aq) + e^- \rightleftharpoons \text{Fe}^{2+}(aq), \quad E = E^\circ - 0.05916 \log\left(\frac{[\text{Fe}^{2+}]}{[\text{Fe}^{3+}]}\right)$$
   The boundary is a strictly horizontal line independent of $pH$.
2. **Vertical Boundaries (Pure Acid-Base Transfer, Potential-Independent)**:
   Involve non-redox acid-base precipitation equilibria with zero electron transfer:
   $$\text{Fe}^{3+}(aq) + 3\,\text{H}_2\text{O}(l) \rightleftharpoons \text{Fe(OH)}_3(s) + 3\,\text{H}^+(aq)$$
   Equilibrium depends purely on $[\text{H}^+]$ ($pH$), forming a strictly vertical line.
3. **Slanted Boundaries (Simultaneous Redox and Proton Transfer)**:
   Involve both electrons and protons:
   $$\text{Fe(OH)}_3(s) + 3\,\text{H}^+(aq) + e^- \rightleftharpoons \text{Fe}^{2+}(aq) + 3\,\text{H}_2\text{O}(l)$$
   By the Nernst equation:
   $$E = E^\circ - \frac{0.05916}{1} \log\left(\frac{[\text{Fe}^{2+}]}{[\text{H}^+]^3}\right) = E^\circ - 0.05916 \log[\text{Fe}^{2+}] - 3(0.05916) pH$$
   The boundary is a slanted line with slope $-0.1775\text{ V}/pH$.

---

### The Thermodynamic Stability Limits of Water

Liquid water decomposes at extreme potentials, defining the upper and lower thermodynamic stability envelope of all aqueous chemistry:
- **Upper Limit (Water Oxidation to Oxygen)**:
  $$\text{O}_2(g) + 4\,\text{H}^+(aq) + 4e^- \rightleftharpoons 2\,\text{H}_2\text{O}(l), \quad E = 1.229 - 0.05916\,pH$$
  Any oxidant with potential above line (b) can spontaneously oxidize water to $\text{O}_2(g)$.
- **Lower Limit (Water Reduction to Hydrogen)**:
  $$2\,\text{H}^+(aq) + 2e^- \rightleftharpoons \text{H}_2(g), \quad E = 0.000 - 0.05916\,pH$$
  Any reductant with potential below line (a) can spontaneously reduce water to $\text{H}_2(g)$.

#### The Three Operational Corrosion Domains:
- **Immunity Zone**: The metal exists as the elemental solid $\text{M}^0$; thermodynamically immune to corrosion.
- **Corrosion Zone**: The metal dissolves into soluble aquo-cations ($\text{M}^{2+}, \text{M}^{3+}$); active corrosion.
- **Passivation Zone**: The metal forms an insoluble, dense, adherent oxide or hydroxide surface film ($\text{Fe}_2\text{O}_3, \text{TiO}_2, \text{Al}_2\text{O}_3$) that kinetically shields the underlying bulk metal from further chemical attack."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 8.1: Redox Balancing in Basic Solution & Concentration Cell EMF",
                "statement": r"""1. Balance the following oxidation-reduction reaction occurring in basic aqueous solution using the ion-electron method:
   $$\text{MnO}_4^-(aq) + \text{I}^-(aq) \xrightarrow{\text{basic}} \text{MnO}_2(s) + \text{IO}_3^-(aq)$$
   Show every intermediate step, including the balance of mass, water, hydroxide ions, and charge.
2. An electrochemical cell is constructed at $298.15\text{ K}$ operating with the zinc-copper Daniell reaction:
   $$\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightleftharpoons \text{Zn}^{2+}(aq) + \text{Cu}(s), \quad E^\circ = +1.100\text{ V}$$
   The zinc compartment contains $[\text{Zn}^{2+}] = 0.850\text{ M}$ and the copper compartment contains $[\text{Cu}^{2+}] = 0.00150\text{ M}$.
   - Compute the reaction quotient $Q$.
   - Calculate the cell potential $E_{\text{cell}}$ using the Nernst equation.
   - Calculate the maximum non-expansion electrical work obtainable per mole of zinc consumed under these conditions.""",
                "solution": r"""### Part 1: Balancing in Basic Aqueous Media

#### 1. Reduction Half-Reaction ($\text{Mn}^{+7} \rightarrow \text{Mn}^{+4}$):
- $\text{MnO}_4^- \rightarrow \text{MnO}_2$
- Balance Oxygen by adding $2\,\text{H}_2\text{O}$ to product side:
  $$\text{MnO}_4^- \longrightarrow \text{MnO}_2 + 2\,\text{H}_2\text{O}$$
- Balance Hydrogen by adding $4\,\text{H}_2\text{O}$ to reactant side and $4\,\text{OH}^-$ to product side:
  $$\text{MnO}_4^- + 4\,\text{H}_2\text{O} \longrightarrow \text{MnO}_2 + 2\,\text{H}_2\text{O} + 4\,\text{OH}^-$$
  Simplifying water:
  $$\text{MnO}_4^- + 2\,\text{H}_2\text{O} \longrightarrow \text{MnO}_2 + 4\,\text{OH}^-$$
- Balance charge ($-1$ on left, $-4$ on right $\implies$ add $3e^-$ to left):
  $$\text{MnO}_4^- + 2\,\text{H}_2\text{O} + 3e^- \longrightarrow \text{MnO}_2 + 4\,\text{OH}^- \quad [\times 2]$$

#### 2. Oxidation Half-Reaction ($\text{I}^{-1} \rightarrow \text{I}^{+5}$):
- $\text{I}^- \rightarrow \text{IO}_3^-$
- Balance Oxygen by adding $3\,\text{H}_2\text{O}$ to product side, balanced by $6\,\text{OH}^-$ on reactant side:
  $$\text{I}^- + 6\,\text{OH}^- \longrightarrow \text{IO}_3^- + 3\,\text{H}_2\text{O}$$
- Balance charge ($-1 + (-6) = -7$ on left, $-1$ on right $\implies$ add $6e^-$ to right):
  $$\text{I}^- + 6\,\text{OH}^- \longrightarrow \text{IO}_3^- + 3\,\text{H}_2\text{O} + 6e^- \quad [\times 1]$$

#### 3. Summing and Canceling:
Multiply reduction half-reaction by 2 ($6e^-$ transferred):
$$2\,\text{MnO}_4^- + 4\,\text{H}_2\text{O} + 6e^- + \text{I}^- + 6\,\text{OH}^- \longrightarrow 2\,\text{MnO}_2 + 8\,\text{OH}^- + \text{IO}_3^- + 3\,\text{H}_2\text{O} + 6e^-$$
Cancel $6e^-$, $3\,\text{H}_2\text{O}$, and $6\,\text{OH}^-$:
$$\mathbf{2\,\text{MnO}_4^-(aq) + \text{I}^-(aq) + \text{H}_2\text{O}(l) \longrightarrow 2\,\text{MnO}_2(s) + \text{IO}_3^-(aq) + 2\,\text{OH}^-(aq)}$$
- Mass verification: $2\text{ Mn}, 1\text{ I}, 9\text{ O}, 2\text{ H}$ on each side.
- Charge verification: $2(-1) + (-1) = -3$ on left; $-1 + 2(-1) = -3$ on right! Verified.

---

### Part 2: Electrochemical Potential via the Nernst Equation

Reaction:
$$\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightleftharpoons \text{Zn}^{2+}(aq) + \text{Cu}(s), \quad n = 2$$
$$E^\circ = +1.100\text{ V}$$

#### 1. Reaction Quotient $Q$:
$$Q = \frac{[\text{Zn}^{2+}]}{[\text{Cu}^{2+}]} = \frac{0.850}{0.00150} \approx 566.67$$
$$\log_{10} Q = \log_{10}(566.67) \approx 2.7533$$

#### 2. Cell Potential $E_{\text{cell}}$:
$$E_{\text{cell}} = E^\circ - \frac{0.05916}{n} \log_{10} Q$$
$$E_{\text{cell}} = 1.100 - \frac{0.05916}{2} \times 2.7533 = 1.100 - (0.02958 \times 2.7533)$$
$$E_{\text{cell}} = 1.100 - 0.08144 = \mathbf{+1.0186\text{ V} \approx 1.019\text{ V}}$$

#### 3. Maximum Non-Expansion Electrical Work:
$$w_{\text{max}} = \Delta G = -n F E_{\text{cell}}$$
$$w_{\text{max}} = -2 \times (96485.33\text{ C}\cdot\text{mol}^{-1}) \times 1.0186\text{ V} = -196558\text{ J}\cdot\text{mol}^{-1} = \mathbf{-196.6\text{ kJ}\cdot\text{mol}^{-1}}$$
The cell can perform up to $196.6\text{ kJ}$ of electrical work per mole of zinc dissolved."""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 8.2: Latimer Diagram Analysis & Disproportionation Thermodynamics for Chlorine",
                "statement": r"""The Latimer diagram for chlorine in acidic solution ($pH = 0$, $a_{\text{H}^+} = 1.0$) is:
$$\text{ClO}_4^- \xrightarrow{+1.20\text{ V}} \text{ClO}_3^- \xrightarrow{+1.18\text{ V}} \text{HClO}_2 \xrightarrow{+1.67\text{ V}} \text{HClO} \xrightarrow{+1.63\text{ V}} \text{Cl}_2 \xrightarrow{+1.36\text{ V}} \text{Cl}^-$$

1. Calculate the standard reduction potential $E^\circ$ for the direct conversion of chlorate to elemental chlorine:
   $$\text{ClO}_3^- + 6\,\text{H}^+ + 5e^- \longrightarrow \frac{1}{2}\,\text{Cl}_2 + 3\,\text{H}_2\text{O}$$
2. Determine whether hypochlorous acid ($\text{HClO}$) is thermodynamically stable with respect to disproportionation into $\text{HClO}_2$ and $\text{Cl}_2$.
   Calculate $E_{\text{cell}}^\circ$, $\Delta G^\circ$, and the equilibrium constant $K_{\text{eq}}$ for the disproportionation reaction:
   $$2\,\text{HClO} \rightleftharpoons \text{HClO}_2 + \frac{1}{2}\,\text{Cl}_2 + \frac{1}{2}\,\text{H}_2\text{O} \dots$$
3. By comparing $E^\circ(\text{HClO}/\text{Cl}_2) = +1.63\text{ V}$ with the water oxidation potential $E^\circ(\text{O}_2/\text{H}_2\text{O}) = +1.23\text{ V}$, explain why household bleach solutions and hypochlorous acid are kinetically persistent despite being thermodynamically capable of violently oxidizing water.""",
                "solution": r"""### Part 1: Calculation of $E^\circ(\text{ClO}_3^- \rightarrow \text{Cl}_2)$
The path from $\text{ClO}_3^-$ to $\text{Cl}_2$ traverses three intermediate redox couples:
1. $\text{ClO}_3^- (+5) \rightarrow \text{HClO}_2 (+3)$: $n_1 = 2$, $E_1^\circ = +1.18\text{ V}$
2. $\text{HClO}_2 (+3) \rightarrow \text{HClO} (+1)$: $n_2 = 2$, $E_2^\circ = +1.67\text{ V}$
3. $\text{HClO} (+1) \rightarrow \frac{1}{2}\text{Cl}_2 (0)$: $n_3 = 1$, $E_3^\circ = +1.63\text{ V}$

Total electrons transferred:
$$n_{\text{net}} = n_1 + n_2 + n_3 = 2 + 2 + 1 = 5\text{ electrons}$$

Applying the Latimer rule:
$$E_{\text{net}}^\circ = \frac{n_1 E_1^\circ + n_2 E_2^\circ + n_3 E_3^\circ}{n_{\text{net}}}$$
$$E_{\text{net}}^\circ = \frac{(2 \times 1.18) + (2 \times 1.67) + (1 \times 1.63)}{5} = \frac{2.36 + 3.34 + 1.63}{5} = \frac{7.33}{5} = \mathbf{+1.466\text{ V} \approx +1.47\text{ V}}$$

---

### Part 2: Disproportionation Analysis of Hypochlorous Acid ($\text{HClO}$)
In the Latimer sequence:
$$\text{HClO}_2 \xrightarrow{E_L^\circ = +1.67\text{ V}} \mathbf{HClO} \xrightarrow{E_R^\circ = +1.63\text{ V}} \text{Cl}_2$$

Applying the Disproportionation Rule:
- Potential to the right: $E_R^\circ = +1.63\text{ V}$ (Reduction of $\text{HClO}$ to $\text{Cl}_2$).
- Potential to the left: $E_L^\circ = +1.67\text{ V}$ (Oxidation of $\text{HClO}$ to $\text{HClO}_2$ has potential $-1.67\text{ V}$).

Net potential for disproportionation into $\text{HClO}_2$ and $\text{Cl}_2$:
$$E_{\text{cell}}^\circ = E_R^\circ - E_L^\circ = 1.63 - 1.67 = \mathbf{-0.040\text{ V}}$$
Because $E_{\text{cell}}^\circ < 0$ ($E_R^\circ < E_L^\circ$), this specific disproportionation pathway is **thermodynamically non-spontaneous** ($\Delta G^\circ > 0$).

#### HOWEVER: Consider Disproportionation of $\text{HClO}$ into Chlorate ($\text{ClO}_3^-$) and Chloride ($\text{Cl}^-$):
Latimer potentials for overall disproportionation to $\text{Cl}^-$:
- Reduction to chloride: $E^\circ(\text{HClO} / \text{Cl}^-) = \frac{1(1.63) + 1(1.36)}{2} = \frac{2.99}{2} = +1.495\text{ V}$
- Oxidation to chlorate: $E^\circ(\text{ClO}_3^- / \text{HClO}) = \frac{2(1.18) + 2(1.67)}{4} = +1.425\text{ V}$
Here:
$$E_{\text{cell}}^\circ = +1.495 - (+1.425) = \mathbf{+0.070\text{ V}} > 0$$
$$\Delta G^\circ = -n F E^\circ = -4 \times 96485 \times 0.070 = -27.0\text{ kJ}\cdot\text{mol}^{-1}$$
Thus, $\text{HClO}$ **is unstable toward disproportionation into chlorate and chloride**:
$$3\,\text{HClO} \longrightarrow \text{ClO}_3^- + 2\,\text{Cl}^- + 3\,\text{H}^+, \quad K_{\text{eq}} \approx 10^{\frac{4 \times 0.070}{0.05916}} = 10^{4.73} \approx 5.4 \times 10^4$$

---

### Part 3: Kinetic Persistence and Water Oxidation Barrier
The reduction potential of $\text{HClO} \rightarrow \text{Cl}_2$ is $+1.63\text{ V}$, which exceeds the water oxidation potential ($+1.23\text{ V}$):
$$4\,\text{HClO} + 2\,\text{H}_2\text{O} \longrightarrow 2\,\text{Cl}_2 + 4\,\text{H}_3\text{O}^+ + \text{O}_2(g), \quad E_{\text{cell}}^\circ = +1.63 - 1.23 = +0.40\text{ V}$$
The reaction is thermodynamically spontaneous ($\Delta G^\circ \ll 0$).
However, oxidation of water to gaseous $\text{O}_2$ requires a complex **four-electron, four-proton transfer** involving cleavage of two $\text{O}-\text{H}$ bonds and formation of an $\text{O}=\text{O}$ double bond:
$$2\,\text{H}_2\text{O} \longrightarrow \text{O}_2 + 4\,\text{H}^+ + 4e^-$$
This multi-step concerted mechanism possesses an immense **kinetic activation barrier** ($\Delta G^\ddagger \gg 100\text{ kJ}\cdot\text{mol}^{-1}$) and a massive electrochemical overpotential ($\eta_{\text{overpotential}} > 0.5\text{ V}$). In the absence of heterogeneous catalysts (such as $\text{RuO}_2$ or ultraviolet light), the reaction rate is virtually zero at ambient temperature, allowing aqueous bleach to persist metastably for years."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 8.3: Thermodynamic Construction of the Iron Pourbaix Diagram",
                "statement": r"""Construct the quantitative mathematical equations delineating the thermodynamic phase boundaries for the Iron-Water system ($\text{Fe}-\text{H}_2\text{O}$) at $298.15\text{ K}$, assuming standard soluble ion activities $a_{\text{Fe}^{2+}} = a_{\text{Fe}^{3+}} = 1.0 \times 10^{-6}\text{ M}$ (the universal metallurgical standard threshold for active corrosion vs immunity).
Given:
- Standard reduction potentials:
  - $E^\circ(\text{Fe}^{2+} / \text{Fe}) = -0.440\text{ V}$
  - $E^\circ(\text{Fe}^{3+} / \text{Fe}^{2+}) = +0.771\text{ V}$
- Solubility product constants:
  - $\text{Fe(OH)}_2(s): K_{sp} = 8.0 \times 10^{-16} \quad (pK_{sp} = 15.10)$
  - $\text{Fe(OH)}_3(s): K_{sp} = 1.0 \times 10^{-38} \quad (pK_{sp} = 38.00)$
  - Ion product of water: $K_w = 1.0 \times 10^{-14}$

1. Derive the equation for the boundary between elemental iron $\text{Fe}(s)$ and soluble ferrous ion $\text{Fe}^{2+}(aq)$ (Immunity / Corrosion boundary).
2. Derive the equation for the boundary between soluble $\text{Fe}^{2+}(aq)$ and soluble ferric ion $\text{Fe}^{3+}(aq)$.
3. Derive the critical $pH$ boundary for the precipitation of ferrous hydroxide $\text{Fe(OH)}_2(s)$ from soluble $\text{Fe}^{2+}(aq)$.
4. Derive the slanted $E-pH$ boundary equation for the oxidation of soluble $\text{Fe}^{2+}(aq)$ to insoluble passivating ferric hydroxide $\text{Fe(OH)}_3(s)$:
   $$\text{Fe(OH)}_3(s) + 3\,\text{H}^+(aq) + e^- \rightleftharpoons \text{Fe}^{2+}(aq) + 3\,\text{H}_2\text{O}(l)$$
5. Delineate the three classic metallurgical zones (Immunity, Active Corrosion, Passivation) and explain how cathodic protection prevents industrial steel pipeline corrosion by shifting the operating potential into the Immunity zone.""",
                "solution": r"""### Step 1: Boundary 1: $\text{Fe}(s) / \text{Fe}^{2+}(aq)$ (Immunity / Corrosion)
Reaction:
$$\text{Fe}^{2+}(aq) + 2e^- \rightleftharpoons \text{Fe}(s)$$
Nernst equation at $298.15\text{ K}$:
$$E = E^\circ - \frac{0.05916}{2} \log\left(\frac{1}{[\text{Fe}^{2+}]}\right) = -0.440 + 0.02958 \log[\text{Fe}^{2+}]$$
At the standard metallurgical corrosion threshold $[\text{Fe}^{2+}] = 1.0 \times 10^{-6}\text{ M}$ ($\log[\text{Fe}^{2+}] = -6.00$):
$$E = -0.440 + 0.02958(-6.00) = -0.440 - 0.1775 = \mathbf{-0.618\text{ V}}$$
- **Equation**: $\mathbf{E = -0.618\text{ V}}$ (Strictly horizontal line independent of $pH$).
- Below $-0.618\text{ V}$: Elemental $\text{Fe}(s)$ is thermodynamically stable (**Immunity Zone**).

---

### Step 2: Boundary 2: $\text{Fe}^{2+}(aq) / \text{Fe}^{3+}(aq)$
Reaction:
$$\text{Fe}^{3+}(aq) + e^- \rightleftharpoons \text{Fe}^{2+}(aq)$$
Nernst equation:
$$E = E^\circ - 0.05916 \log\left(\frac{[\text{Fe}^{2+}]}{[\text{Fe}^{3+}]}\right) = +0.771 - 0.05916 \log\left(\frac{10^{-6}}{10^{-6}}\right) = \mathbf{+0.771\text{ V}}$$
- **Equation**: $\mathbf{E = +0.771\text{ V}}$ (Horizontal line independent of $pH$ in acidic media).

---

### Step 3: Boundary 3: $\text{Fe}^{2+}(aq) / \text{Fe(OH)}_2(s)$ (Acid-Base Precipitation)
Reaction:
$$\text{Fe(OH)}_2(s) \rightleftharpoons \text{Fe}^{2+}(aq) + 2\,\text{OH}^-(aq), \quad K_{sp} = 8.0 \times 10^{-16}$$
At precipitation threshold $[\text{Fe}^{2+}] = 1.0 \times 10^{-6}\text{ M}$:
$$[\text{OH}^-]^2 = \frac{K_{sp}}{[\text{Fe}^{2+}]} = \frac{8.0 \times 10^{-16}}{1.0 \times 10^{-6}} = 8.0 \times 10^{-10}$$
$$[\text{OH}^-] = \sqrt{8.0 \times 10^{-10}} \approx 2.83 \times 10^{-5}\text{ M}$$
$$pOH = -\log(2.83 \times 10^{-5}) \approx 4.55 \implies pH = 14.00 - 4.55 = \mathbf{9.45}$$
- **Equation**: $\mathbf{pH = 9.45}$ (Strictly vertical line independent of potential $E$).
- At $pH > 9.45$, $\text{Fe}^{2+}$ precipitates as solid ferrous hydroxide.

---

### Step 4: Boundary 4: $\text{Fe}^{2+}(aq) / \text{Fe(OH)}_3(s)$ (Slanted Redox Boundary)
Reaction:
$$\text{Fe(OH)}_3(s) + 3\,\text{H}^+(aq) + e^- \rightleftharpoons \text{Fe}^{2+}(aq) + 3\,\text{H}_2\text{O}(l)$$
We find standard potential $E^\circ$ by coupling $\text{Fe}^{3+}/ \text{Fe}^{2+}$ with $K_{sp}[\text{Fe(OH)}_3]$:
1. $\text{Fe}^{3+} + e^- \rightleftharpoons \text{Fe}^{2+}, \quad \Delta G_1^\circ = -1 F (+0.771)$
2. $\text{Fe(OH)}_3(s) \rightleftharpoons \text{Fe}^{3+} + 3\,\text{OH}^-, \quad \Delta G_2^\circ = -RT \ln(10^{-38})$
3. $3\,\text{H}_2\text{O} \rightleftharpoons 3\,\text{H}^+ + 3\,\text{OH}^-, \quad \Delta G_3^\circ = +3 RT \ln(10^{-14})$

Net Standard Potential:
$$E^\circ = 0.771 + 0.05916 \log\left(\frac{K_{sp}[\text{Fe(OH)}_3]}{K_w^3}\right) = 0.771 + 0.05916 \log\left(\frac{10^{-38}}{10^{-42}}\right) = 0.771 + 0.05916(4) = +1.008\text{ V}$$

Applying Nernst equation:
$$E = 1.008 - 0.05916 \log\left(\frac{[\text{Fe}^{2+}]}{[\text{H}^+]^3}\right) = 1.008 - 0.05916 \log[\text{Fe}^{2+}] - 3(0.05916) pH$$
Substitute $[\text{Fe}^{2+}] = 10^{-6}\text{ M}$ ($\log[\text{Fe}^{2+}] = -6$):
$$E = 1.008 - 0.05916(-6) - 0.1775\,pH = 1.008 + 0.355 - 0.1775\,pH$$
$$\mathbf{E = 1.363 - 0.1775\,pH \quad (\text{V})}$$

---

### Step 5: Metallurgical Corrosion Zones & Cathodic Protection
1. **Immunity Zone ($E < -0.618\text{ V}$)**:
   Thermodynamic reduction to metallic iron $\text{Fe}(s)$ is favored. Iron cannot dissolve into ions regardless of kinetic factors.
2. **Corrosion Zone ($-0.618\text{ V} < E < 1.363 - 0.1775\,pH$ and $pH < 9.45$)**:
   Soluble divalent ion $\text{Fe}^{2+}(aq)$ is the thermodynamically stable species. Iron actively corrodes, dissolves, and degrades.
3. **Passivation Zone ($E > 1.363 - 0.1775\,pH$ or $pH > 9.45$)**:
   Insoluble $\text{Fe(OH)}_3(s)$ or hydrated $\text{Fe}_2\text{O}_3$ forms an adherent, insoluble surface oxide film, passivating the metal.

#### Mechanism of Cathodic Protection:
In industrial steel oil/gas pipelines or maritime ship hulls:
- An underground steel pipe naturally rests in moist soil at $E \approx -0.2\text{ to } -0.4\text{ V}$ at neutral $pH \approx 7$. Looking at the Pourbaix diagram, this coordinates directly inside the **Active Corrosion Zone**!
- To prevent corrosion, engineers apply **Cathodic Protection**:
  1. **Sacrificial Galvanic Anode**: Connecting the pipeline electrically to a more active metal with a more negative reduction potential ($\text{Mg}$ with $E^\circ = -2.37\text{ V}$, or $\text{Zn}$ with $E^\circ = -0.76\text{ V}$).
  2. **Impressed Current**: Applying an external DC power source pumping electrons into the steel pipeline.
- The continuous supply of electrons polarizes the steel, driving its electrochemical potential down from $-0.3\text{ V}$ to **below the $-0.618\text{ V}$ threshold into the Immunity Zone**.
- As long as $E < -0.618\text{ V}$, the thermodynamic driving force for iron oxidation is completely extinguished ($\Delta G > 0$), granting indefinite thermodynamic immunity from corrosion."""
            }
        ]
    }
'''

with open("build_inorg1_unit8.py", "w", encoding="utf-8") as f:
    f.write(content)

print("build_inorg1_unit8.py written successfully.")
