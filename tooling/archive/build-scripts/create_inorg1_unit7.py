#!/usr/bin/env python3
"""
create_inorg1_unit7.py
Generates build_inorg1_unit7.py for Unit 7:
Secondary Bonding, Intermolecular Forces & Acid-Base Equilibria
"""

import sys

content = r'''# -*- coding: utf-8 -*-
"""
Unit 7: Secondary Bonding, Intermolecular Forces & Acid-Base Equilibria
Contains 5 comprehensive sections and 3 tiered solved problems with full derivations.
"""

def get_unit7():
    return {
        "id": "unit7",
        "title": "Unit 7: Secondary Bonding, Intermolecular Forces & Acid-Base Equilibria",
        "simId": "sim_chem_acid_base_titration_speciation",
        "simTitle": "Polyprotic Titration & Speciation Simulator",
        "sections": [
            {
                "id": "sec7_1",
                "title": "§7.1 Secondary Chemical Bonding: Hydrogen Bonding, Dipole Interactions & Dispersion Forces",
                "content": r"""### The Continuum of Non-Covalent Intermolecular Interactions

While primary chemical bonds (ionic, covalent, metallic) possess bond energies typically ranging from $150$ to $1000\text{ kJ}\cdot\text{mol}^{-1}$, intermolecular forces (van der Waals interactions and hydrogen bonds) operate over lower energetic scales ($0.5$ to $160\text{ kJ}\cdot\text{mol}^{-1}$). Despite their lower energies, secondary interactions govern the three-dimensional architecture of inorganic supramolecular networks, crystal packing, solvent cohesion, boiling points, and solubility phenomena.

---

### Classification and Physics of Intermolecular Potentials

```
               Intermolecular Potential Hierarchy:
               
   Type                           Potential V(r)              Typical Energy
   -------------------------------------------------------------------------
   Ion - Dipole                   ∝ - 1 / r^2                 40 - 600 kJ/mol
   Dipole - Dipole (Keesom)       ∝ - 1 / r^6  (Thermal avg)  5 - 25 kJ/mol
   Dipole - Induced Dipole (Debye)∝ - 1 / r^6                 2 - 10 kJ/mol
   London Dispersion (Fluctuating)∝ - 1 / r^6                 0.5 - 40 kJ/mol
   Hydrogen Bonding               Electrostatic + Covalent    10 - 165 kJ/mol
```

#### 1. Keesom Dipole-Dipole Orientational Forces ($V \propto -r^{-6}$):
Between two freely rotating permanent dipoles $\mu_1$ and $\mu_2$ in thermal equilibrium at temperature $T$, Boltzmann-weighted averaging yields:
$$V_{\text{Keesom}}(r) = -\frac{2 \mu_1^2 \mu_2^2}{3 (4\pi\varepsilon_0)^2 k_B T r^6}$$

#### 2. Debye Induction Polarization Forces ($V \propto -r^{-6}$):
A permanent dipole $\mu_1$ polarizes the electron cloud of an adjacent neutral particle with electronic polarizability $\alpha_2$:
$$V_{\text{Debye}}(r) = -\frac{\mu_1^2 \alpha_2}{(4\pi\varepsilon_0) r^6}$$

#### 3. London Dispersion Forces (Fritz London, 1930):
Even in completely nonpolar, spherically symmetric noble gas atoms ($\text{He, Ar, Xe}$), quantum fluctuations in instantaneous electronic charge distribution create transient, fleeting dipole moments $\mu(t) \neq 0$. This instantaneous dipole induces a correlated dipole in adjacent atoms.
Using second-order quantum perturbation theory:
$$V_{\text{London}}(r) = -\frac{3}{4} \frac{I_1 I_2}{I_1 + I_2} \frac{\alpha_1 \alpha_2}{(4\pi\varepsilon_0)^2 r^6}$$
where $I_1, I_2$ are the first ionization energies.
- **Ubiquity**: London dispersion forces are **always present** in all matter, universally attractive, and scale directly with atomic polarizability $\alpha$ (which increases with atomic size and electron count). In large polar molecules (such as $\text{CCl}_4$ or $\text{I}_2$), dispersion forces overwhelmingly dominate the total cohesive energy.

---

### The Nature of the Hydrogen Bond ($D-\text{H}\cdots A$)

A hydrogen bond is an attractive interaction between a hydrogen atom covalently bonded to a highly electronegative donor atom ($D \in \{\text{F, O, N}\}$, and under certain circumstances $\text{Cl, C}$) and an electron-rich acceptor atom ($A$) possessing a localized lone pair or $\pi$ electron density.

#### The Energetic Spectrum of Hydrogen Bonds:
1. **Weak Hydrogen Bonds** ($10\text{–}20\text{ kJ}\cdot\text{mol}^{-1}$): Predominantly electrostatic dipole-dipole interactions ($\text{C}-\text{H}\cdots\text{O}$ in organometallic crystals).
2. **Moderate Hydrogen Bonds** ($20\text{–}60\text{ kJ}\cdot\text{mol}^{-1}$): Normal hydrogen bonds found in liquid water, ice ($21\text{ kJ}\cdot\text{mol}^{-1}$), and alcohols.
3. **Strong / Very Strong Hydrogen Bonds** ($60\text{–}165\text{ kJ}\cdot\text{mol}^{-1}$): Possess significant covalent character with partial charge transfer.
   - Archetype: The bifluoride ion, $[\text{F}-\text{H}-\text{F}]^-$, with dissociation enthalpy $\Delta H_{\text{diss}}^\circ \approx 163\text{ kJ}\cdot\text{mol}^{-1}$.

#### Symmetric vs Asymmetric Potential Energy Wells:
In a typical asymmetric hydrogen bond (e.g., in liquid water), the proton moves in an asymmetric double-well potential with a substantial barrier separating the deep covalent donor well from the shallow acceptor well:
$$D-\text{H} \cdots A \quad (d(D-\text{H}) \approx 100\text{ pm}, \quad d(\text{H}\cdots A) \approx 180\text{ pm})$$
In the bifluoride ion $[\text{F}\cdots\text{H}\cdots\text{F}]^-$, the donor-acceptor distance is so short ($d(\text{F}\cdots\text{F}) = 226\text{ pm}$) that the central potential barrier collapses entirely below the zero-point vibrational level, creating a **single-well symmetric hydrogen bond** where the proton resides at the exact geometric midpoint ($d(\text{F}-\text{H}) = 113\text{ pm}$)."""
            },
            {
                "id": "sec7_2",
                "title": "§7.2 Arrhenius, Brønsted-Lowry & Lewis Acid-Base Theories",
                "content": r"""### Evolution of the Acid-Base Paradigm

The definition of acids and bases has evolved through successive conceptual generalizations, broadening the scope from aqueous proton transfer to universal electronic coordinate covalent bonding.

---

### The Three Foundational Formulations

#### 1. Arrhenius Theory (Svante Arrhenius, 1887)
- **Acid**: A substance that dissociates in water to yield hydrogen ions (protons, $\text{H}^+$):
  $$\text{HA}(aq) \rightleftharpoons \text{H}^+(aq) + \text{A}^-(aq)$$
- **Base**: A substance that dissociates in water to yield hydroxide ions ($\text{OH}^-$):
  $$\text{MOH}(aq) \rightleftharpoons \text{M}^+(aq) + \text{OH}^-(aq)$$
- **Limitation**: Strictly confined to aqueous solutions; fails to explain basicity in non-aqueous solvents (e.g., $\text{NH}_3$ in liquid ammonia or gas-phase reactions like $\text{NH}_3(g) + \text{HCl}(g) \rightarrow \text{NH}_4\text{Cl}(s)$).

---

#### 2. Brønsted-Lowry Theory (Johannes Brønsted & Thomas Lowry, 1923)
- **Acid**: A species capable of donating a proton ($\text{H}^+$): a **proton donor**.
- **Base**: A species capable of accepting a proton: a **proton acceptor**.
- **Conjugate Acid-Base Pairs**: Every proton transfer reaction involves two conjugate pairs:
  $$\text{HA} + \text{B} \rightleftharpoons \text{A}^- + \text{HB}^+$$
  $$\text{Acid}_1 + \text{Base}_2 \rightleftharpoons \text{Base}_1 + \text{Acid}_2$$
- **Thermodynamics of Proton Affinity**: In the gas phase, the intrinsic basicity of a neutral species $B$ is quantified by its **Proton Affinity (PA)**:
  $$\text{B}(g) + \text{H}^+(g) \longrightarrow \text{BH}^+(g), \quad \Delta H = -\text{PA} < 0$$
- **Solvent Leveling and Differentiating Effects**:
  - In liquid water, no acid stronger than hydronium ($\text{H}_3\text{O}^+$) can exist in equilibrium; all strong acids ($\text{HClO}_4, \text{HCl}, \text{HNO}_3$) are quantitatively leveled to $\text{H}_3\text{O}^+$.
  - In glacial acetic acid ($\text{CH}_3\text{COOH}$), a weaker proton acceptor, the differentiating effect operates:
    $$\text{HClO}_4 > \text{HBr} > \text{H}_2\text{SO}_4 > \text{HCl} > \text{HNO}_3$$

---

#### 3. Lewis Theory (Gilbert N. Lewis, 1923)
- **Acid**: An electron-pair acceptor (possessing an energetically accessible vacant orbital or LUMO).
- **Base**: An electron-pair donor (possessing an available lone pair or HOMO).
- **Neutralization**: Formation of a coordinate covalent (dative) bond generating a Lewis acid-base adduct:
  $$A + :B \longrightarrow A \xleftarrow{:} B \quad \text{or} \quad A-B$$

```
   Frontier Molecular Orbital View of Lewis Acid-Base Adduct Formation:
   
   Lewis Acid (A)                  Adduct (A-B)                 Lewis Base (:B)
   
   LUMO (Empty)  ---                                              
                                 σ* (LUMO)   ---
                                                
                                 σ  (HOMO)   ---  <-- Dative stabilization!
                                                                  ---  HOMO (Filled lone pair)
```

#### Wide Scope of Inorganic Lewis Acids:
1. **Molecules with incomplete octets**: $\text{BF}_3, \text{BCl}_3, \text{AlCl}_3, \text{BeCl}_2$.
2. **Transition metal and main-group cations**: $\text{Fe}^{3+}, \text{Cu}^{2+}, \text{Ag}^+, \text{Al}^{3+}$.
3. **Molecules with polar multiple bonds**: $\text{CO}_2, \text{SO}_3, \text{SO}_2$ (acting via nucleophilic attack on electrophilic central atom).
4. **Molecules with expandable octets (hypervalent acceptors)**: $\text{SiF}_4 + 2\,\text{F}^- \rightarrow [\text{SiF}_6]^{2-}$, $\text{SnCl}_4 + 2\,\text{Cl}^- \rightarrow [\text{SnCl}_6]^{2-}$."""
            },
            {
                "id": "sec7_3",
                "title": "§7.3 Lux-Flood & Usanovich Generalized Solvo-System Acid-Base Concepts",
                "content": r"""### Non-Aqueous and High-Temperature Acid-Base Formulations

In advanced inorganic metallurgy, ceramic processing, molten salts, and non-aqueous solvents, proton transfer models are entirely inapplicable. Two generalized frameworks provide essential analytical tools:

---

### The Lux-Flood Oxide-Ion Transfer Concept (Hermann Lux, 1939; Håkon Flood, 1947)

Developed specifically to treat high-temperature molten oxide systems, silicate slags, and geochemical magmas:
- **Lux-Flood Base**: An **oxide-ion ($\text{O}^{2-}$) donor**:
  $$\text{Base} \longrightarrow \text{Acid} + \text{O}^{2-}$$
- **Lux-Flood Acid**: An **oxide-ion ($\text{O}^{2-}$) acceptor**:
  $$\text{Acid} + \text{O}^{2-} \longrightarrow \text{Base}$$

#### Archetypal High-Temperature Slag Reactions:
1. **Silicate Slag Formation in Blast Furnaces**:
   $$\underbrace{\text{CaO}(s)}_{\text{Base (donor)}} + \underbrace{\text{SiO}_2(s)}_{\text{Acid (acceptor)}} \longrightarrow \underbrace{\text{CaSiO}_3(l)}_{\text{Neutral Salt (Slag)}}$$
   Here, $\text{CaO}$ donates $\text{O}^{2-}$ to form $\text{Ca}^{2+}$, while polymeric acidic silica $\text{SiO}_2$ accepts $\text{O}^{2-}$ to cleave bridging $\text{Si}-\text{O}-\text{Si}$ bonds into orthosilicate $[\text{SiO}_4]^{4-}$ units.
2. **Sulfate and Pyrosulfate Equilibria**:
   $$\text{SO}_3(g) + \text{O}^{2-} \rightleftharpoons \text{SO}_4^{2-} \quad (\text{SO}_3 \text{ is an acidic oxide})$$
   $$\text{SO}_4^{2-} + \text{SO}_3 \rightleftharpoons \text{S}_2\text{O}_7^{2-}$$
3. **Titanate Synthesis**:
   $$\text{BaO} + \text{TiO}_2 \longrightarrow \text{BaTiO}_3 \quad (\text{Perovskite dielectric ceramic})$$

---

### The Solvo-System Concept (Cady & Elsey, 1928)

In any autoionizing amphiprotic or aprotic polar solvent, the solvent undergoes self-ionization:
$$2\,\text{Solvent} \rightleftharpoons \text{Lyate Cation} + \text{Lyate Anion}$$
- **Solvo-System Acid**: Any solute that increases the concentration of the characteristic solvent **cation**.
- **Solvo-System Base**: Any solute that increases the concentration of the characteristic solvent **anion**.

#### Comparison Across Representative Autoionizing Solvents:

| Solvent System | Autoionization Equilibrium | Lyate Cation (Acid) | Lyate Anion (Base) | Neutralization Reaction |
| :--- | :--- | :--- | :--- | :--- |
| **Water** | $2\,\text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{OH}^-$ | $\text{H}_3\text{O}^+$ | $\text{OH}^-$ | $\text{H}_3\text{O}^+ + \text{OH}^- \rightarrow 2\,\text{H}_2\text{O}$ |
| **Liquid Ammonia** | $2\,\text{NH}_3 \rightleftharpoons \text{NH}_4^+ + \text{NH}_2^-$ | $\text{NH}_4^+$ (Ammonium) | $\text{NH}_2^-$ (Amide) | $\text{NH}_4^+ + \text{NH}_2^- \rightarrow 2\,\text{NH}_3$ |
| **Liquid $\text{SO}_2$** | $2\,\text{SO}_2 \rightleftharpoons \text{SO}^{2+} + \text{SO}_3^{2-}$ | $\text{SO}^{2+}$ (Thionyl) | $\text{SO}_3^{2-}$ (Sulfite) | $\text{SOCl}_2 + \text{Cs}_2\text{SO}_3 \rightarrow 2\,\text{CsCl} + 2\,\text{SO}_2$ |
| **Liquid $\text{BrF}_3$** | $2\,\text{BrF}_3 \rightleftharpoons \text{BrF}_2^+ + \text{BrF}_4^-$ | $\text{BrF}_2^+$ | $\text{BrF}_4^-$ | $\text{BrF}_2\text{SbF}_6 + \text{KBrF}_4 \rightarrow \text{KSbF}_6 + 2\,\text{BrF}_3$ |

---

### The Usanovich Theory (Mikhail Usanovich, 1939)

The ultimate generalization subsuming all chemical reactions:
- **Acid**: Any species that can donate cations, accept anions, or **accept electrons** (acts as an oxidant).
- **Base**: Any species that can donate anions, accept cations, or **donate electrons** (acts as a reductant).
Under Usanovich theory, every redox reaction is recognized as a limiting case of an acid-base process."""
            },
            {
                "id": "sec7_4",
                "title": "§7.4 Pearson's Hard and Soft Acids and Bases (HSAB) Principle",
                "content": r"""### Ralph Pearson's Principle of Chemical Hardness

In 1963, Ralph G. Pearson established the **Hard and Soft Acids and Bases (HSAB) Principle** to predict the thermodynamic stability, kinetic rate constants, and preferential coordination selectivity of Lewis acid-base adducts:

> **The HSAB Principle**: *Hard acids prefer to coordinate with hard bases, and soft acids prefer to coordinate with soft bases.*

---

### Classification Criteria for Hard and Soft Species

```
                 HARD SPECIES                           SOFT SPECIES
   * Small ionic radius                    * Large ionic radius
   * High formal oxidation state           * Low or zero formal oxidation state
   * Low electronic polarizability         * High electronic polarizability (diffuse)
   * High electronegativity (bases)        * Intermediate / low electronegativity
   * Large HOMO-LUMO energy gap            * Small HOMO-LUMO energy gap
```

#### Master Classification Table:

| Category | Hard | Borderline | Soft |
| :--- | :--- | :--- | :--- |
| **Lewis Acids** | $\text{H}^+, \text{Li}^+, \text{Na}^+, \text{K}^+, \text{Mg}^{2+}, \text{Ca}^{2+}, \text{Al}^{3+}, \text{Cr}^{3+}, \text{Fe}^{3+}, \text{Ti}^{4+}, \text{BF}_3$ | $\text{Fe}^{2+}, \text{Co}^{2+}, \text{Ni}^{2+}, \text{Cu}^{2+}, \text{Zn}^{2+}, \text{Pb}^{2+}, \text{SO}_2$ | $\text{Cu}^+, \text{Ag}^+, \text{Au}^+, \text{Tl}^+, \text{Hg}_2^{2+}, \text{Hg}^{2+}, \text{Cd}^{2+}, \text{Pt}^{2+}, \text{Pd}^{2+}, \text{BH}_3$ |
| **Lewis Bases** | $\text{F}^-, \text{OH}^-, \text{O}^{2-}, \text{H}_2\text{O}, \text{NH}_3, \text{CO}_3^{2-}, \text{NO}_3^-, \text{PO}_4^{3-}, \text{SO}_4^{2-}, \text{ClO}_4^-$ | $\text{Cl}^-, \text{Br}^-, \text{NO}_2^-, \text{SO}_3^{2-}, \text{C}_5\text{H}_5\text{N} \text{ (py)}$ | $\text{I}^-, \text{H}^-, \text{S}^{2-}, \text{CN}^-, \text{SCN}^-, \text{CO}, \text{PR}_3, \text{R}_2\text{S}, \text{C}_2\text{H}_4$ |

---

### Quantum Mechanical Foundations of Absolute Hardness

In 1983, Ralph Pearson and Robert Parr placed the empirical HSAB principle on a rigorous quantum mechanical footing using **Density Functional Theory (DFT)**.

Let $E(N)$ be the ground-state electronic energy of an $N$-electron system under external potential $v(\mathbf{r})$.
The **Electronic Chemical Potential** ($\mu$) is:
$$\mu = \left( \frac{\partial E}{\partial N} \right)_{v(\mathbf{r})} = -\chi$$
where $\chi$ is the **Absolute Electronegativity**.

The **Absolute Chemical Hardness** ($\eta$) is defined as the second derivative of energy with respect to electron count:
$$\eta = \frac{1}{2} \left( \frac{\partial^2 E}{\partial N^2} \right)_{v(\mathbf{r})} = \frac{1}{2} \left( \frac{\partial \mu}{\partial N} \right)_{v(\mathbf{r})}$$
Chemical **Softness** ($\sigma$) is simply the reciprocal:
$$\sigma = \frac{1}{\eta}$$

#### Operational Finite-Difference Approximations:
Using the three-point finite-difference approximation for $E(N-1), E(N), E(N+1)$:
- $E(N-1) - E(N) = IE$ (Ionization Energy)
- $E(N) - E(N+1) = EA$ (Electron Affinity)

$$\chi = \frac{IE + EA}{2}$$
$$\eta = \frac{IE - EA}{2}$$

#### Connection to Frontier Molecular Orbitals (HOMO and LUMO):
By Koopmans' theorem, $IE \approx -E_{\text{HOMO}}$ and $EA \approx -E_{\text{LUMO}}$:
$$\eta = \frac{-E_{\text{HOMO}} - (-E_{\text{LUMO}})}{2} = \frac{E_{\text{LUMO}} - E_{\text{HOMO}}}{2} = \frac{\Delta E_{\text{gap}}}{2}$$

$$\mathbf{\text{Absolute Hardness is strictly proportional to the HOMO-LUMO energy gap!}}$$
- **Hard molecules**: Wide bandgap $\Delta E_{\text{gap}} \gg 0$; resistant to electronic deformation and charge transfer.
- **Soft molecules**: Narrow bandgap $\Delta E_{\text{gap}} \approx 0$; highly polarizable, prone to covalent charge transfer.

---

### Thermodynamic Driving Forces: Klopman-Salem Equation

The interaction energy $\Delta E$ between acid $A$ and base $B$ is given by the Klopman-Salem equation:
$$\Delta E = -\underbrace{\frac{q_A q_B}{4\pi\varepsilon_0 \epsilon r_{AB}}}_{\text{Electrostatic Term}} + \underbrace{\sum_{m}^{\text{occ}} \sum_{n}^{\text{unocc}} \frac{2 (c_m c_n \beta_{AB})^2}{E_m - E_n}}_{\text{Covalent / Orbital Term}}$$

1. **Hard-Hard Interactions**: Governed by the **Electrostatic Term**. Small radii and high charges produce dominant Coulombic attraction (ionic bonding, high lattice energies).
2. **Soft-Soft Interactions**: Governed by the **Covalent / Orbital Term**. Energetically proximate frontier orbitals ($E_m \approx E_n$) minimize the energy denominator, driving covalent wavefunction overlap and massive covalent stabilization."""
            },
            {
                "id": "sec7_5",
                "title": "§7.5 Quantitative Aqueous Acid-Base Equilibria: Polyprotic Acids, Speciation Diagrams, Buffer Capacity & Hydrolysis",
                "content": r"""### Analytical Formulation of Polyprotic Acid Equilibria

A polyprotic acid $\text{H}_n\text{A}$ undergoes $n$ successive macroscopic step-dissociation equilibria in aqueous solution:
$$\text{H}_n\text{A} \rightleftharpoons \text{H}^+ + \text{H}_{n-1}\text{A}^-, \quad K_{a1} = \frac{[\text{H}^+][\text{H}_{n-1}\text{A}^-]}{[\text{H}_n\text{A}]}$$
$$\text{H}_{n-1}\text{A}^- \rightleftharpoons \text{H}^+ + \text{H}_{n-2}\text{A}^{2-}, \quad K_{a2} = \frac{[\text{H}^+][\text{H}_{n-2}\text{A}^{2-}]}{[\text{H}_{n-1}\text{A}^-]}$$
$$\vdots$$
$$\text{HA}^{-(n-1)} \rightleftharpoons \text{H}^+ + \text{A}^{n-}, \quad K_{an} = \frac{[\text{H}^+][\text{A}^{n-}]}{[\text{HA}^{-(n-1)}]}$$

By electrostatic necessity, each successive proton removal becomes progressively more difficult because the proton must detach from an increasingly negatively charged anion:
$$K_{a1} \gg K_{a2} \gg \dots \gg K_{an} \quad (\text{typically successive } pK_a \text{ values differ by } 4\text{ to } 5 \text{ units})$$

---

### Derivation of General Speciation Fractional Coefficients ($\alpha_k$)

Let $C_A$ be the total analytical concentration of all conjugate species containing the conjugate moiety $\text{A}$:
$$C_A = [\text{H}_n\text{A}] + [\text{H}_{n-1}\text{A}^-] + [\text{H}_{n-2}\text{A}^{2-}] + \dots + [\text{A}^{n-}]$$

Expressing every conjugate species in terms of $[\text{H}_n\text{A}]$ and $[\text{H}^+]$:
$$[\text{H}_{n-1}\text{A}^-] = \frac{K_{a1}}{[\text{H}^+]} [\text{H}_n\text{A}]$$
$$[\text{H}_{n-2}\text{A}^{2-}] = \frac{K_{a1} K_{a2}}{[\text{H}^+]^2} [\text{H}_n\text{A}]$$
$$[\text{A}^{n-}] = \frac{K_{a1} K_{a2} \cdots K_{an}}{[\text{H}^+]^n} [\text{H}_n\text{A}]$$

Substituting into the mass balance:
$$C_A = [\text{H}_n\text{A}] \left( 1 + \frac{K_{a1}}{[\text{H}^+]} + \frac{K_{a1} K_{a2}}{[\text{H}^+]^2} + \dots + \frac{\prod_{j=1}^n K_{aj}}{[\text{H}^+]^n} \right)$$
Define the fundamental polynomial denominator $D$:
$$D = [\text{H}^+]^n + K_{a1} [\text{H}^+]^{n-1} + K_{a1} K_{a2} [\text{H}^+]^{n-2} + \dots + \prod_{j=1}^n K_{aj}$$

The fractional concentration $\alpha_k = \frac{[\text{H}_{n-k}\text{A}^{k-}]}{C_A}$ of the $k$-th deprotonated species is:
$$\alpha_0 = \frac{[\text{H}_n\text{A}]}{C_A} = \frac{[\text{H}^+]^n}{D}$$
$$\alpha_1 = \frac{[\text{H}_{n-1}\text{A}^-]}{C_A} = \frac{K_{a1} [\text{H}^+]^{n-1}}{D}$$
$$\alpha_2 = \frac{[\text{H}_{n-2}\text{A}^{2-}]}{C_A} = \frac{K_{a1} K_{a2} [\text{H}^+]^{n-2}}{D}$$
$$\alpha_n = \frac{[\text{A}^{n-}]}{C_A} = \frac{K_{a1} K_{a2} \cdots K_{an}}{D}$$

```
   Speciation Curves for Phosphoric Acid (H3PO4):
   
   Fraction α
   1.0 |    α0 (H3PO4)       α1 (H2PO4-)      α2 (HPO4^2-)     α3 (PO4^3-)
       |    \             /    \             /    \             /
   0.5 |     \  pK1=2.15 /      \  pK2=7.20 /      \  pK3=12.38/
       |      \         /        \         /        \         /
   0.0 +-------X-------+----------X-------+----------X-------+---> pH
              2.15                   7.20               12.38
```

Notice that at $pH = pK_{ak}$, the concentrations of the adjacent conjugate pair are strictly equal: $\alpha_{k-1} = \alpha_k = 0.50$.

---

### Donald Van Slyke's Buffer Capacity Equation

The **Buffer Capacity** ($\beta$) measures a solution's resistance to $pH$ alteration upon addition of strong base ($C_b$) or strong acid ($C_a$):
$$\beta = \frac{dC_b}{dpH} = -\frac{dC_a}{dpH}$$

For an aqueous solution containing strong electrolytes and a monoprotic weak conjugate acid-base buffer system of total analytical concentration $C$:
$$\beta = 2.303 \left( [\text{H}^+] + [\text{OH}^-] + \frac{C \cdot K_a [\text{H}^+]}{(K_a + [\text{H}^+])^2} \right)$$
$$= 2.303 \left( [\text{H}^+] + \frac{K_w}{[\text{H}^+]} + C \alpha_0 \alpha_1 \right)$$

#### Maximum Buffer Capacity Condition:
Differentiating $\beta$ with respect to $[\text{H}^+]$ shows that buffer capacity peaks precisely when:
$$[\text{H}^+] = K_a \iff pH = pK_a$$
At this point, $\alpha_0 = \alpha_1 = 0.5$, yielding maximum buffer capacity:
$$\beta_{\text{max}} = 2.303 \left( \frac{C}{4} \right) \approx 0.576 \cdot C$$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 7.1: Rigorous Buffer Capacity Derivation & Polyprotic Phosphate Speciation",
                "statement": r"""A physiological phosphate buffer is prepared by dissolving sodium dihydrogen phosphate ($\text{NaH}_2\text{PO}_4$) and disodium hydrogen phosphate ($\text{Na}_2\text{HPO}_4$) in water such that the total analytical phosphate concentration is $C_{\text{phos}} = 0.050\text{ M}$.
The dissociation constants of phosphoric acid at $25^\circ\text{C}$ are:
- $K_{a1} = 7.11 \times 10^{-3} \quad (pK_{a1} = 2.148)$
- $K_{a2} = 6.32 \times 10^{-8} \quad (pK_{a2} = 7.199)$
- $K_{a3} = 4.50 \times 10^{-13} \quad (pK_{a3} = 12.347)$

1. For human arterial blood plasma buffered at physiological $pH = 7.400$:
   - Calculate the exact speciation fractions $\alpha_0, \alpha_1, \alpha_2, \alpha_3$.
   - Calculate the molar concentration of all four phosphate species ($[\text{H}_3\text{PO}_4], [\text{H}_2\text{PO}_4^-], [\text{HPO}_4^{2-}], [\text{PO}_4^{3-}]$).
2. Calculate the quantitative buffer capacity $\beta$ of this solution at $pH = 7.400$.
3. What volume of $0.100\text{ M }\text{HCl}$ must be added to $1.000\text{ L}$ of this buffer to lower the $pH$ to $7.200$?""",
                "solution": r"""### Part 1: Speciation Fractions at pH = 7.400
At $pH = 7.400$:
$$[\text{H}^+] = 10^{-7.400} = 3.981 \times 10^{-8}\text{ M}$$

#### Calculate polynomial terms for denominator $D$:
$$D = [\text{H}^+]^3 + K_{a1} [\text{H}^+]^2 + K_{a1} K_{a2} [\text{H}^+] + K_{a1} K_{a2} K_{a3}$$

1. $[\text{H}^+]^3 = (3.981 \times 10^{-8})^3 = 6.31 \times 10^{-23}$
2. $K_{a1} [\text{H}^+]^2 = (7.11 \times 10^{-3}) \times (3.981 \times 10^{-8})^2 = (7.11 \times 10^{-3}) \times (1.585 \times 10^{-15}) = 1.127 \times 10^{-17}$
3. $K_{a1} K_{a2} [\text{H}^+] = (7.11 \times 10^{-3}) \times (6.32 \times 10^{-8}) \times (3.981 \times 10^{-8}) = 1.789 \times 10^{-17}$
4. $K_{a1} K_{a2} K_{a3} = (7.11 \times 10^{-3}) \times (6.32 \times 10^{-8}) \times (4.50 \times 10^{-13}) = 2.02 \times 10^{-22}$

Notice that terms 1 and 4 are virtually zero ($10^{-23}$). The system is dominated entirely by the conjugate pair $\text{H}_2\text{PO}_4^-$ and $\text{HPO}_4^{2-}$!
$$D \approx 1.127 \times 10^{-17} + 1.789 \times 10^{-17} = 2.916 \times 10^{-17}$$

#### Fractions:
$$\alpha_0(\text{H}_3\text{PO}_4) = \frac{[\text{H}^+]^3}{D} = \frac{6.31 \times 10^{-23}}{2.916 \times 10^{-17}} \approx \mathbf{2.16 \times 10^{-6}}$$
$$\alpha_1(\text{H}_2\text{PO}_4^-) = \frac{1.127 \times 10^{-17}}{2.916 \times 10^{-17}} = \mathbf{0.3865} \quad (38.65\%)$$
$$\alpha_2(\text{HPO}_4^{2-}) = \frac{1.789 \times 10^{-17}}{2.916 \times 10^{-17}} = \mathbf{0.6135} \quad (61.35\%)$$
$$\alpha_3(\text{PO}_4^{3-}) = \frac{2.02 \times 10^{-22}}{2.916 \times 10^{-17}} = \mathbf{6.93 \times 10^{-6}}$$

#### Molar Concentrations ($C_{\text{phos}} = 0.050\text{ M}$):
$$[\text{H}_3\text{PO}_4] = 2.16 \times 10^{-6} \times 0.050 = \mathbf{1.08 \times 10^{-7}\text{ M}}$$
$$[\text{H}_2\text{PO}_4^-] = 0.3865 \times 0.050 = \mathbf{0.01933\text{ M} \approx 19.33\text{ mM}}$$
$$[\text{HPO}_4^{2-}] = 0.6135 \times 0.050 = \mathbf{0.03068\text{ M} \approx 30.68\text{ mM}}$$
$$[\text{PO}_4^{3-}] = 6.93 \times 10^{-6} \times 0.050 = \mathbf{3.46 \times 10^{-7}\text{ M}}$$

---

### Part 2: Buffer Capacity Calculation
At $pH = 7.400$, $[\text{H}^+] = 3.98 \times 10^{-8}\text{ M}$ and $[\text{OH}^-] = 2.51 \times 10^{-7}\text{ M}$, both negligible compared to buffer terms.
$$\beta = 2.303 \left( C_{\text{phos}} \cdot \alpha_1 \cdot \alpha_2 \right)$$
$$\beta = 2.303 \times 0.050 \times (0.3865 \times 0.6135) = 2.303 \times 0.050 \times 0.2371 = \mathbf{0.0273\text{ mol}\cdot\text{L}^{-1}\cdot pH^{-1}}$$

---

### Part 3: Acid Addition to Lower pH to 7.200
In $1.000\text{ L}$:
- Initial amounts: $n(\text{H}_2\text{PO}_4^-) = 0.01933\text{ mol}$, $n(\text{HPO}_4^{2-}) = 0.03068\text{ mol}$.
- Target $pH = 7.200$:
  Using Henderson-Hasselbalch equation:
  $$pH = pK_{a2} + \log\left(\frac{n_{\text{base}}}{n_{\text{acid}}}\right)$$
  $$7.200 = 7.199 + \log\left(\frac{0.03068 - x}{0.01933 + x}\right) \implies \log\left(\frac{0.03068 - x}{0.01933 + x}\right) = 0.001$$
  $$\frac{0.03068 - x}{0.01933 + x} = 10^{0.001} \approx 1.0023$$
  $$0.03068 - x = 1.0023(0.01933 + x) = 0.01937 + 1.0023 x$$
  $$2.0023 x = 0.03068 - 0.01937 = 0.01131 \implies x = 5.65 \times 10^{-3}\text{ mol of }\text{H}^+$$

Volume of $0.100\text{ M }\text{HCl}$:
$$V = \frac{n}{M} = \frac{5.65 \times 10^{-3}\text{ mol}}{0.100\text{ mol/L}} = 0.0565\text{ L} = \mathbf{56.5\text{ mL}}$$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 7.2: Quantitative Pearson HSAB Matching & Ligand Displacement Thermodynamics",
                "statement": r"""Consider the competitive displacement equilibrium between two classic coordination complexes in aqueous solution:
$$[\text{Co}(\text{NH}_3)_5\text{F}]^{2+}(aq) + [\text{Co}(\text{NH}_3)_5\text{I}]^{2+}(aq) + \text{Hg}^{2+}(aq) \rightleftharpoons \dots$$
Specifically, examine the exchange reaction:
$$[\text{Co}(\text{NH}_3)_5\text{I}]^{2+}(aq) + \text{H}_2\text{O}(l) + \text{Hg}^{2+}(aq) \longrightarrow [\text{Co}(\text{NH}_3)_5(\text{OH}_2)]^{3+}(aq) + \text{HgI}^+(aq)$$
and compare it to the analogous fluoro-complex reaction:
$$[\text{Co}(\text{NH}_3)_5\text{F}]^{2+}(aq) + \text{H}_2\text{O}(l) + \text{Hg}^{2+}(aq) \longrightarrow [\text{Co}(\text{NH}_3)_5(\text{OH}_2)]^{3+}(aq) + \text{HgF}^+(aq)$$

1. Classify all participating Lewis acids ($\text{Co}^{3+}, \text{Hg}^{2+}, \text{H}^+$) and Lewis bases ($\text{F}^-, \text{I}^-, \text{H}_2\text{O}, \text{NH}_3$) according to Pearson's HSAB principle, explicitly stating their oxidation states, polarizabilities, and frontier orbital characters.
2. Given the stability constants in water:
   - For mercury(II) complexes: $\log \beta_1(\text{HgF}^+) = 1.03$, $\log \beta_1(\text{HgI}^+) = 12.87$.
   - For cobalt(III) aquo exchange: $\log K_{\text{form}}([\text{Co}(\text{NH}_3)_5\text{F}]^{2+}) = 2.50$, $\log K_{\text{form}}([\text{Co}(\text{NH}_3)_5\text{I}]^{2+}) = -1.80$.
   Calculate the equilibrium constant $K_{\text{eq}}$ and $\Delta G^\circ$ for both displacement reactions.
3. Formulate the concept of **Symbiosis** (Jørgensen, 1968) and explain why coordinating soft ligands onto a metal center enhances its affinity for additional soft ligands.""",
                "solution": r"""### Part 1: HSAB Classification of Chemical Species

#### 1. Lewis Acids:
- **$\text{Co}^{3+}$**: Hard Lewis Acid. High positive charge ($+3$), small ionic radius ($r = 54.5\text{ pm}$ low-spin), low polarizability, widely separated HOMO-LUMO gap.
- **$\text{Hg}^{2+}$**: Soft Lewis Acid. Heavy post-transition metal cation with $5d^{10}$ closed core, large ionic radius ($r = 102\text{ pm}$), high polarizability, easily deformable electron cloud, small HOMO-LUMO gap.
- **$\text{H}^+$**: Hard Lewis Acid. Infinitesimally small radius (bare nucleus), zero electrons to polarize.

#### 2. Lewis Bases:
- **$\text{F}^-$**: Hard Lewis Base. Small ionic radius ($133\text{ pm}$), high Pauling electronegativity ($\chi = 3.98$), tightly held valence electrons, non-polarizable.
- **$\text{I}^-$**: Soft Lewis Base. Massive ionic radius ($220\text{ pm}$), low electronegativity ($\chi = 2.66$), diffuse $5p$ electron cloud, exceptionally high polarizability ($\alpha$).
- **$\text{H}_2\text{O}$ and $\text{NH}_3$**: Hard Lewis Bases. Oxygen and nitrogen donor atoms with high electronegativities.

---

### Part 2: Thermodynamic Driving Force Calculations

#### Reaction 1: Mercury-assisted iodide extraction
$$[\text{Co}(\text{NH}_3)_5\text{I}]^{2+} + \text{Hg}^{2+} + \text{H}_2\text{O} \longrightarrow [\text{Co}(\text{NH}_3)_5(\text{OH}_2)]^{3+} + \text{HgI}^+$$

This reaction represents the difference between mercury-halide complex formation and cobalt-halide complex formation:
$$\Delta \log K_1 = \log \beta_1(\text{HgI}^+) - \log K_{\text{form}}([\text{Co}-\text{I}])$$
$$\log K_{\text{eq}, 1} = 12.87 - (-1.80) = 12.87 + 1.80 = \mathbf{+14.67}$$
$$K_{\text{eq}, 1} = 10^{14.67} \approx \mathbf{4.68 \times 10^{14}}$$
$$\Delta G_1^\circ = -2.303 RT \log K_{\text{eq}, 1} = -2.303 \times (8.314\text{ J/mol}\cdot\text{K}) \times (298.15\text{ K}) \times 14.67$$
$$\Delta G_1^\circ = -5.708\text{ kJ/mol} \times 14.67 = \mathbf{-83.7\text{ kJ}\cdot\text{mol}^{-1}}$$
*The reaction is overwhelmingly spontaneous by over $83\text{ kJ}\cdot\text{mol}^{-1}$!*

#### Reaction 2: Mercury-assisted fluoride extraction
$$[\text{Co}(\text{NH}_3)_5\text{F}]^{2+} + \text{Hg}^{2+} + \text{H}_2\text{O} \longrightarrow [\text{Co}(\text{NH}_3)_5(\text{OH}_2)]^{3+} + \text{HgF}^+$$
$$\log K_{\text{eq}, 2} = \log \beta_1(\text{HgF}^+) - \log K_{\text{form}}([\text{Co}-\text{F}])$$
$$\log K_{\text{eq}, 2} = 1.03 - 2.50 = \mathbf{-1.47}$$
$$K_{\text{eq}, 2} = 10^{-1.47} \approx \mathbf{0.0339}$$
$$\Delta G_2^\circ = -5.708 \times (-1.47) = \mathbf{+8.39\text{ kJ}\cdot\text{mol}^{-1}}$$
*The fluoro-displacement is thermodynamically unfavorable and does not occur.*

#### Physical Interpretation via HSAB:
- $\text{Hg}^{2+}$ is an archetypal soft acid; $\text{I}^-$ is an archetypal soft base. Their pairing is stabilized by massive covalent resonance integrals and favorable orbital overlaps ($\Delta \log K = +14.67$).
- Conversely, pairing soft $\text{Hg}^{2+}$ with hard $\text{F}^-$ is mismatched and disfavored; hard $\text{F}^-$ remains tenaciously bound to hard $\text{Co}^{3+}$.

---

### Part 3: Jørgensen's Principle of Symbiosis
Christian K. Jørgensen established the principle of **Symbiosis**:
> *Hard ligands tend to cluster together on a central metal atom, making the metal harder; similarly, soft ligands tend to cluster together, making the metal softer.*

#### Electronic Mechanism:
- When soft, highly polarizable ligands with $\pi$-acceptor or low electronegativity characteristics (such as $\text{CN}^-, \text{CO}, \text{I}^-$) coordinate to a metal, they donate extensive electron density into the metal's valence orbitals.
- This electron donation decreases the metal's effective positive nuclear charge ($Z_{\text{eff}}$), expanding the remaining metal $d$ orbitals and increasing their polarizability.
- The metal cation becomes electronically **softer**, dramatically enhancing its affinity for additional soft ligands.
- Conversely, coordinating hard, electronegative ligands ($\text{F}^-, \text{O}^{2-}$) withdraws electron density, contracting the metal's orbitals and making the metal substantially **harder**."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 7.3: Thermodynamic Derivation of EDTA-Metal Chelate Speciation & Conditional Formation Constants",
                "statement": r"""Ethylenediaminetetraacetic acid ($\text{H}_4\text{Y}$, EDTA) is an hexadentate aminopolycarboxylic acid chelating agent possessing four carboxylic acid protons and two ammonium protons. Its six stepwise acid dissociation constants at $25^\circ\text{C}$ and $I = 0.1\text{ M}$ are:
- $pK_{a1} = 0.00$, $pK_{a2} = 1.50$, $pK_{a3} = 2.00$
- $pK_{a4} = 2.69$, $pK_{a5} = 6.13$, $pK_{a6} = 10.37$

The unprotonated tetraanion $\text{Y}^{4-}$ binds divalent zinc ($\text{Zn}^{2+}$) with a true thermodynamic formation constant:
$$\text{Zn}^{2+} + \text{Y}^{4-} \rightleftharpoons [\text{ZnY}]^{2-}, \quad K_f = \frac{[[\text{ZnY}]^{2-}]}{[\text{Zn}^{2+}][\text{Y}^{4-}]} = 3.16 \times 10^{16} \quad (\log K_f = 16.50)$$

1. Derive the analytical expression for the fractional concentration of fully deprotonated EDTA, $\alpha_{\text{Y}^{4-}}$, as a function of $[\text{H}^+]$ and the acid dissociation constants.
2. Define the **Conditional Formation Constant** $K_f'$:
   $$K_f' = \alpha_{\text{Y}^{4-}} \cdot K_f$$
   Calculate the exact numerical value of $\alpha_{\text{Y}^{4-}}$ and $K_f'$ at $pH = 2.00$, $pH = 5.00$, and $pH = 10.00$.
3. For an analytical solution containing total zinc concentration $C_{\text{Zn}} = 0.010\text{ M}$ and total EDTA concentration $C_{\text{EDTA}} = 0.010\text{ M}$ at $pH = 5.00$, calculate the concentration of uncomplexed free zinc ions $[\text{Zn}^{2+}]$ at equilibrium and determine the percentage of zinc chelated.""",
                "solution": r"""### Part 1: Analytical Derivation of $\alpha_{\text{Y}^{4-}}$
Let total uncomplexed EDTA analytical concentration be $C_{\text{EDTA}}'$:
$$C_{\text{EDTA}}' = [\text{H}_6\text{Y}^{2+}] + [\text{H}_5\text{Y}^+] + [\text{H}_4\text{Y}] + [\text{H}_3\text{Y}^-] + [\text{H}_2\text{Y}^{2-}] + [\text{HY}^{3-}] + [\text{Y}^{4-}]$$

Expressing all species in terms of $[\text{Y}^{4-}]$ and $[\text{H}^+]$:
$$[\text{HY}^{3-}] = \frac{[\text{H}^+]}{K_{a6}} [\text{Y}^{4-}]$$
$$[\text{H}_2\text{Y}^{2-}] = \frac{[\text{H}^+]^2}{K_{a5} K_{a6}} [\text{Y}^{4-}]$$
$$\dots$$
$$[\text{H}_6\text{Y}^{2+}] = \frac{[\text{H}^+]^6}{\prod_{j=1}^6 K_{aj}} [\text{Y}^{4-}]$$

Factoring out $[\text{Y}^{4-}]$ yields:
$$\frac{1}{\alpha_{\text{Y}^{4-}}} = \frac{C_{\text{EDTA}}'}{[\text{Y}^{4-}]} = 1 + \frac{[\text{H}^+]}{K_{a6}} + \frac{[\text{H}^+]^2}{K_{a5} K_{a6}} + \frac{[\text{H}^+]^3}{K_{a4} K_{a5} K_{a6}} + \frac{[\text{H}^+]^4}{K_{a3} K_{a4} K_{a5} K_{a6}} + \dots$$
$$\mathbf{\alpha_{\text{Y}^{4-}} = \frac{K_{a1} K_{a2} K_{a3} K_{a4} K_{a5} K_{a6}}{[\text{H}^+]^6 + K_{a1}[\text{H}^+]^5 + \dots + \prod_{j=1}^6 K_{aj}}}$$

---

### Part 2: Numerical Calculation of $\alpha_{\text{Y}^{4-}}$ and $K_f'$ Across $pH$

At typical analytical $pH \ge 2$, the first three deprotonations ($pK_{a1}=0, pK_{a2}=1.50, pK_{a3}=2.00$) are largely complete, so the denominator is dominated by the last four terms:
$$\frac{1}{\alpha_{\text{Y}^{4-}}} \approx 1 + \frac{[\text{H}^+]}{10^{-10.37}} + \frac{[\text{H}^+]^2}{10^{-16.50}} + \frac{[\text{H}^+]^3}{10^{-19.19}} + \frac{[\text{H}^+]^4}{10^{-21.19}}$$

#### 1. At $pH = 2.00$ ($[\text{H}^+] = 10^{-2}\text{ M}$):
$$\frac{[\text{H}^+]}{10^{-10.37}} = 10^{8.37}$$
$$\frac{[\text{H}^+]^2}{10^{-16.50}} = 10^{12.50}$$
$$\frac{[\text{H}^+]^3}{10^{-19.19}} = 10^{13.19}$$
$$\frac{[\text{H}^+]^4}{10^{-21.19}} = 10^{13.19}$$
Summing:
$$\frac{1}{\alpha_{\text{Y}^{4-}}} \approx 10^{13.19} + 10^{13.19} \approx 3.1 \times 10^{13} \implies \mathbf{\alpha_{\text{Y}^{4-}} \approx 3.7 \times 10^{-14}}$$
$$K_f'(pH=2.00) = (3.7 \times 10^{-14}) \times (3.16 \times 10^{16}) \approx \mathbf{1.17 \times 10^3} \quad (\log K_f' = 3.07)$$
*(At $pH = 2$, EDTA is too heavily protonated to chelate zinc effectively; quantitative titration is impossible)*.

#### 2. At $pH = 5.00$ ($[\text{H}^+] = 10^{-5}\text{ M}$):
$$\frac{[\text{H}^+]}{10^{-10.37}} = 10^{5.37} = 2.34 \times 10^5$$
$$\frac{[\text{H}^+]^2}{10^{-16.50}} = 10^{6.50} = 3.16 \times 10^6$$
$$\frac{[\text{H}^+]^3}{10^{-19.19}} = 10^{4.19} = 1.55 \times 10^4$$
$$\frac{1}{\alpha_{\text{Y}^{4-}}} \approx 3.16 \times 10^6 + 2.34 \times 10^5 \approx 3.40 \times 10^6 \implies \mathbf{\alpha_{\text{Y}^{4-}} \approx 2.94 \times 10^{-7}}$$
$$K_f'(pH=5.00) = (2.94 \times 10^{-7}) \times (3.16 \times 10^{16}) = \mathbf{9.29 \times 10^9} \quad (\log K_f' = 9.97)$$
*(Since $K_f' \gg 10^8$, complexation is strictly quantitative!)*

#### 3. At $pH = 10.00$ ($[\text{H}^+] = 10^{-10}\text{ M}$):
$$\frac{[\text{H}^+]}{10^{-10.37}} = 10^{0.37} = 2.34$$
$$\frac{1}{\alpha_{\text{Y}^{4-}}} \approx 1 + 2.34 = 3.34 \implies \mathbf{\alpha_{\text{Y}^{4-}} \approx 0.299} \quad (29.9\%)$$
$$K_f'(pH=10.00) = 0.299 \times (3.16 \times 10^{16}) = \mathbf{9.45 \times 10^{15}} \quad (\log K_f' = 15.98)$$

---

### Part 3: Equilibrium Speciation at $pH = 5.00$
Given $C_{\text{Zn}} = 0.010\text{ M}$ and $C_{\text{EDTA}} = 0.010\text{ M}$ at stoichiometric equivalence:
$$K_f' = \frac{[[\text{ZnY}]^{2-}]}{[\text{Zn}^{2+}]' [C_{\text{EDTA}}']}$$
Let $x = [\text{Zn}^{2+}]' = [C_{\text{EDTA}}']$.
Then $[[\text{ZnY}]^{2-}] = 0.010 - x \approx 0.010\text{ M}$.

$$K_f' = \frac{0.010}{x^2} = 9.29 \times 10^9$$
$$x^2 = \frac{0.010}{9.29 \times 10^9} = 1.076 \times 10^{-12}$$
$$x = \sqrt{1.076 \times 10^{-12}} = \mathbf{1.04 \times 10^{-6}\text{ M}}$$

#### Equilibrium Free Zinc Concentration:
$$[\text{Zn}^{2+}] = \mathbf{1.04 \times 10^{-6}\text{ M} = 1.04\text{ }\mu\text{M}}$$

#### Percentage of Zinc Chelated:
$$\% \text{ Chelation} = \frac{0.010 - 1.04 \times 10^{-6}}{0.010} \times 100\% = \frac{0.00999896}{0.010} \times 100\% = \mathbf{99.99\%}$$
This proves analytically why analytical chemists can quantitatively titrate transition metal ions with EDTA at buffered $pH = 5.00$ with $> 99.99\%$ completion."""
            }
        ]
    }
'''

with open("build_inorg1_unit7.py", "w", encoding="utf-8") as f:
    f.write(content)

print("build_inorg1_unit7.py written successfully.")
