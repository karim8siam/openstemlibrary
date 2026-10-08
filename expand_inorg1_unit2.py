#!/usr/bin/env python3
"""
expand_inorg1_unit2.py
Expands build_inorg1_unit2.py to ~10,500+ words with deep mathematical, historical,
and electronic structure derivations of periodic periodicity, Slater's rules,
relativistic effects, electronegativity frameworks, and heavy p-block chemistry.
"""

import sys

content = r'''# -*- coding: utf-8 -*-
"""
Unit 2: Periodicity of the Elements, Electronic Shielding & Relativistic Effects
Comprehensive master digital textbook unit containing 5 deep sections and 3 tiered solved problems.
"""

def get_unit2():
    return {
        "id": "unit2",
        "title": "Unit 2: Periodicity of the Elements, Electronic Shielding & Relativistic Effects",
        "simId": "sim_chem_periodic_trends_explorer",
        "simTitle": "Periodic Trends & Slater Effective Nuclear Charge Engine",
        "sections": [
            {
                "id": "sec2_1",
                "title": "§2.1 Historical Development, Moseley's Law & The Modern Periodic Law",
                "content": r"""### The Epistemological Evolution of Elemental Classification

The systematic organization of the chemical elements represents one of the greatest intellectual triumphs in physical science. In the late 18th and 19th centuries, early chemists sought order among the burgeoning catalog of discovered elements by identifying recurring patterns in their physical and chemical behaviors:
1. **Antoine Lavoisier (1789)**: Published the first modern list of 33 elements, classifying them into gases, non-metals, metals, and earths, though including heat (*caloric*) and light.
2. **Johann Wolfgang Döbereiner (1829)**: Identified **Döbereiner's Triads**, groups of three elements with analogous chemical properties where the atomic weight of the intermediate element was the arithmetic mean of the two extremes:
   - Halogen triad: $\text{Cl} (35.45)$, $\text{Br} (79.90)$, $\text{I} (126.90) \implies \frac{35.45 + 126.90}{2} = 81.18 \approx 79.90$.
   - Alkali triad: $\text{Li} (6.94)$, $\text{Na} (22.99)$, $\text{K} (39.10) \implies \frac{6.94 + 39.10}{2} = 23.02 \approx 22.99$.
   - Alkaline earth triad: $\text{Ca} (40.08)$, $\text{Sr} (87.62)$, $\text{Ba} (137.33) \implies \frac{40.08 + 137.33}{2} = 88.71 \approx 87.62$.
3. **Alexandre-Émile Béguyer de Chancourtois (1862)**: Devised the *vis tellurique* (telluric screw), mapping elements on a cylinder inscribed with a helix inclined at $45^\circ$, where elements with similar properties aligned on vertical generating lines at multiples of atomic weight 16.
4. **John Newlands (1865)**: Formulated the **Law of Octaves**, observing that when elements were arranged by increasing atomic weight, every eighth element displayed similar properties, mirroring the musical octave. While ridiculed at the Chemical Society for comparing chemistry to musical scales, Newlands correctly anticipated the octet periodicity.
5. **Dmitri Mendeleev & Julius Lothar Meyer (1869)**: Independently constructed periodic tables organizing elements by increasing atomic weight and valency. Mendeleev's enduring genius lay in two crucial decisions:
   - He prioritized chemical homology over strict atomic weight progression, deliberately inverting the ordering of **Tellurium** ($127.60$) and **Iodine** ($126.90$), as well as **Cobalt** ($58.93$) and **Nickel** ($58.69$).
   - He left blank gaps in his table and made stunningly accurate quantitative predictions of the existence and properties of undiscovered elements: *Eka-aluminum* (Gallium, discovered 1875 by Lecoq de Boisbaudran), *Eka-boron* (Scandium, discovered 1879 by Nilson), and *Eka-silicon* (Germanium, discovered 1886 by Winkler).

```
   Mendeleev's Quantitative Predictions vs Experimental Discoveries:
   
   Property                    Eka-Silicon (Predicted 1871)    Germanium (Discovered 1886)
   ---------------------------------------------------------------------------------------
   Atomic Weight               72                              72.64
   Density (g/cm³)             5.5                             5.35
   Atomic Volume (cm³/mol)     13                              13.2
   Color                       Dirty gray                      Grayish-white
   Formula of Oxide            EsO2 (density ~4.7 g/cm³)       GeO2 (density 4.70 g/cm³)
   Formula of Chloride         EsCl4 (bp < 100 °C, d 1.9)      GeCl4 (bp 84 °C, d 1.88)
   Formula of Ethyl Derivative Es(C2H5)4 (bp 160 °C, d 0.96)  Ge(C2H5)4 (bp 163.5 °C, d 0.99)
```

---

### Henry Moseley's High-Frequency X-Ray Spectra & The True Definition of Atomic Number

Despite Mendeleev's triumph, the fundamental physical parameter governing elemental identity remained mysterious. In 1913–1914, 26-year-old British physicist **Henry Moseley**, working in Ernest Rutherford's laboratory in Manchester, bombarded solid elemental targets (from aluminum to gold) with high-energy cathode rays (electrons) in an evacuated X-ray tube. He dispersed the emitted characteristic X-rays using a potassium ferrocyanide crystal diffraction spectrometer and recorded the spectral lines photographically.

Moseley measured the wavelengths of the characteristic **$K_\alpha$** and **$L_\alpha$** emission lines across thirty-eight consecutive elements.

```
       Moseley's Experimental Discovery:
       
       ν^(1/2) (Square root of X-ray frequency)
        ^
        |                                        / (Slope = a)
        |                                      /
        |                                    /
        |                                  /
        |                                /
        |                              /
        |                            /
        |                          /
        |                        /
        0 ---------------------*-----------------------------> Atomic Number Z
                             (Intercept = σ ≈ 1.0 for K-alpha)
```

#### Mathematical Formulation of Moseley's Law:
Moseley discovered that the square root of the frequency $\nu$ of the characteristic $K_\alpha$ X-ray line is strictly linearly proportional to the element's position $Z$ in the periodic table:
$$\sqrt{\nu} = a (Z - \sigma)$$
$$\nu = a^2 (Z - \sigma)^2$$
where:
- $\nu$ is the frequency of the emitted $K_\alpha$ photon.
- $Z$ is the **Atomic Number**, which Moseley definitively proved is the **integer fundamental positive nuclear charge** of the nucleus ($Z = \frac{Q_{\text{nucleus}}}{e}$).
- $a$ is a proportionality constant: for $K_\alpha$ transitions ($n=2 \rightarrow n=1$), $a = \sqrt{\frac{3}{4} R c} \approx 4.97 \times 10^7\text{ s}^{-1/2}$.
- $\sigma$ is the **Screening Constant** (screening parameter): for $K_\alpha$ emission, $\sigma \approx 1.0$, because an electron transitioning from $n=2$ to $n=1$ is shielded from the full nuclear charge $Z$ by the single remaining $1s$ core electron.

#### Theoretical Derivation from Bohr's Model:
In the Bohr-Rydberg framework, the transition frequency from level $n_2$ to $n_1$ under effective nuclear charge $Z_{\text{eff}} = Z - \sigma$ is:
$$\nu = R c (Z - \sigma)^2 \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right)$$
For the $K_\alpha$ line ($n_1 = 1, n_2 = 2$):
$$\nu = R c (Z - 1)^2 \left( \frac{1}{1^2} - \frac{1}{2^2} \right) = \frac{3}{4} R c (Z - 1)^2$$
Taking the square root:
$$\sqrt{\nu} = \sqrt{\frac{3}{4} R c} \, (Z - 1)$$
This precisely reproduces Moseley's empirical relation with $a = \sqrt{\frac{3}{4} R c}$ and $\sigma = 1.0$!

#### Revolutionary Scientific Impacts of Moseley's Law:
1. **Definitive Grounding of the Periodic Law**: The Modern Periodic Law states:
   $$\mathbf{\text{The physical and chemical properties of the elements are periodic functions of their ATOMIC NUMBERS } (Z).}$$
2. **Resolution of Anomalous Pairs**: Moseley proved that Argon ($Z=18, A=39.95$) legitimately precedes Potassium ($Z=19, A=39.10$), Cobalt ($Z=27, A=58.93$) precedes Nickel ($Z=28, A=58.69$), and Tellurium ($Z=52, A=127.60$) precedes Iodine ($Z=53, A=126.90$).
3. **Exact Accounting of Missing Elements**: Moseley established that between Hydrogen ($Z=1$) and Uranium ($Z=92$), there existed exactly 92 elements. He identified precisely where missing elements remained to be discovered: $Z = 43$ (Technetium), $Z = 61$ (Promethium), $Z = 72$ (Hafnium), and $Z = 75$ (Rhenium).
4. **Clarification of Rare Earth Elements**: Moseley proved that the enigmatic lanthanide series comprised exactly fourteen elements spanning $Z = 58$ (Cerium) through $Z = 71$ (Lutetium)."""
            },
            {
                "id": "sec2_2",
                "title": "§2.2 Effective Nuclear Charge, Slater's Rules & Clementi-Raimondi Wavefunctions",
                "content": r"""### The Many-Electron Hamiltonian and Screening Mechanics

In a many-electron atom containing $N$ electrons and nuclear charge $Z$, the non-relativistic electronic Schrödinger equation involves the Hamiltonian:
$$\hat{H} = \sum_{i=1}^N \left( -\frac{\hbar^2}{2m_e} \nabla_i^2 - \frac{Z e^2}{4\pi\varepsilon_0 r_i} \right) + \sum_{i<j}^N \frac{e^2}{4\pi\varepsilon_0 r_{ij}}$$

The interelectronic Coulombic repulsion term $\sum_{i<j} \frac{e^2}{4\pi\varepsilon_0 r_{ij}}$ couples the coordinates of all electrons, rendering the multi-electron Schrödinger equation analytically insolvable.

To construct an effective one-electron orbital model, we approximate the interelectronic repulsion experienced by a specific valence electron as a spherically averaged screening field produced by all other electrons. The electron moves in a central field governed by the **Effective Nuclear Charge** ($Z_{\text{eff}}$ or $Z^*$):
$$Z_{\text{eff}} = Z - \sigma$$
where $Z$ is the true nuclear charge and $\sigma$ is the dimensionless **Screening Constant** (shielding constant).

```
          Core Screening Geometry:
          
             [ +Z Nucleus ]
                 /     \
         ( Core Electrons )  <-- Shielding cloud (σ)
                 \     /
                    *  <-- Valence Electron feels reduced Z_eff = Z - σ
```

The effective Coulombic potential experienced by the electron at distance $r$ is:
$$V_{\text{eff}}(r) \approx -\frac{Z_{\text{eff}} e^2}{4\pi\varepsilon_0 r}$$

---

### John C. Slater's Empirical Screening Rules (1930)

John C. Slater established a semi-empirical set of rules to compute $\sigma$ and construct approximate analytic wavefunctions.

#### 1. Grouping of Orbitals:
Orbitals are partitioned into sorted principal quantum shells and angular symmetry groups:
$$[1s] \quad [2s, 2p] \quad [3s, 3p] \quad [3d] \quad [4s, 4p] \quad [4d] \quad [4f] \quad [5s, 5p] \dots$$

#### 2. Rules for an Electron in an $[ns, np]$ Group:
1. **Electrons in groups to the right** (higher principal quantum number $n$ or higher subshell): contribute **$0.00$** to $\sigma$ (outer electrons do not shield inner electrons).
2. **Other electrons within the same $[ns, np]$ group**: each contributes **$0.35$** to $\sigma$ (except for the $1s$ group, where the other electron contributes **$0.30$**).
3. **Electrons in the $(n-1)$ principal shell**: each contributes **$0.85$** to $\sigma$.
4. **Electrons in $(n-2)$ and deeper core shells**: each contributes **$1.00$** to $\sigma$ (complete electrostatic screening).

#### 3. Rules for an Electron in an $[nd]$ or $[nf]$ Group:
1. **Electrons in groups to the right**: contribute **$0.00$** to $\sigma$.
2. **Other electrons within the same $[nd]$ or $[nf]$ group**: each contributes **$0.35$** to $\sigma$.
3. **All electrons in all groups to the left** (all $(n-1)$, $(n-2)$, etc., as well as $[ns, np]$ of the same $n$): each contributes **$1.00$** to $\sigma$.

#### 4. Effective Principal Quantum Number ($n^*$):
For high principal quantum numbers, Slater adjusted $n$ to $n^*$ to prevent orbital over-expansion:
- For $n = 1$: $n^* = 1.0$
- For $n = 2$: $n^* = 2.0$
- For $n = 3$: $n^* = 3.0$
- For $n = 4$: $n^* = 3.7$
- For $n = 5$: $n^* = 4.0$
- For $n = 6$: $n^* = 4.2$

Slater orbital energy is given by:
$$E_n = -\frac{13.6\text{ eV} \cdot (Z_{\text{eff}})^2}{(n^*)^2}$$

---

### Stepwise Exemplars of Slater's Rules

#### Case 1: First-Row Transition Metal ($4s$ vs $3d$ in Zinc, $Z = 30$)
Electron configuration of $\text{Zn}$: $[1s^2] [2s^2, 2p^6] [3s^2, 3p^6] [3d^{10}] [4s^2]$.

1. **Screening experienced by a $4s$ valence electron**:
   - Other electron in $[4s]$: $1 \times 0.35 = 0.35$
   - Electrons in $(n-1) = 3$ shell ($3s, 3p, 3d$): $(2 + 6 + 10) = 18 \implies 18 \times 0.85 = 15.30$
   - Electrons in $(n-2)$ and $(n-3)$ shells ($1s, 2s, 2p$): $(2 + 2 + 6) = 10 \implies 10 \times 1.00 = 10.00$
   $$\sigma(4s) = 0.35 + 15.30 + 10.00 = 25.65$$
   $$Z_{\text{eff}}(4s) = 30 - 25.65 = \mathbf{4.35}$$

2. **Screening experienced by a $3d$ electron**:
   - Electrons to the right ($4s$): contribute $0.00$
   - Other electrons in same $[3d]$ group: $9 \times 0.35 = 3.15$
   - All electrons to the left ($1s, 2s, 2p, 3s, 3p$): $(2 + 2 + 6 + 2 + 6) = 18 \implies 18 \times 1.00 = 18.00$
   $$\sigma(3d) = 3.15 + 18.00 = 21.15$$
   $$Z_{\text{eff}}(3d) = 30 - 21.15 = \mathbf{8.85}$$

#### Profound Chemical Insight:
Notice that $Z_{\text{eff}}(3d) = 8.85$ is vastly larger than $Z_{\text{eff}}(4s) = 4.35$.
The $3d$ electrons feel more than twice the effective nuclear pull compared to $4s$ electrons!
- This explains why, upon ionization, transition metals **always lose their $4s$ electrons first**:
  $$\text{Zn} \longrightarrow \text{Zn}^{2+} + 2e^- \quad (\text{configuration changes from } [\text{Ar}]3d^{10}4s^2 \text{ to } [\text{Ar}]3d^{10})$$
  Because $4s$ has much lower $Z_{\text{eff}}$ and higher radial extension, its ionization energy is lower than that of $3d$ in the neutral atom.

---

### Clementi-Raimondi Self-Consistent Field (SCF) Effective Nuclear Charges

While Slater's rules are an invaluable heuristic, Enrico Clementi and D. L. Raimondi (1963, 1967) computed rigorous quantum mechanical values of $Z_{\text{eff}}$ using Roothaan-Hartree-Fock self-consistent field wavefunctions.

```
   Comparison of Slater vs Clementi-Raimondi Z_eff for Second-Row Atoms:
   
   Element   Z    Orbital   Slater Z_eff   Clementi-Raimondi Z_eff   Physical Reason
   -----------------------------------------------------------------------------------
   Li        3    2s        1.30           1.28                      Core 1s contracts
   Be        4    2s        1.95           1.91                      Similar screening
   B         5    2p        2.60           2.42                      2p does not penetrate core
   C         6    2p        3.25           3.14                      Subshell splitting
   N         7    2p        3.90           3.83                      Spin exchange correlation
   O         8    2p        4.55           4.45                      Pairing repulsion
   F         9    2p        5.20           5.10                      Strong contraction
   Ne        10   2p        5.85           5.76                      Closed shell octet
```

#### Core Penetration and Subshell Splitting:
Slater's rules assign identical screening constants to $ns$ and $np$ orbitals within the same group. Clementi-Raimondi calculations reveal that:
$$Z_{\text{eff}}(ns) > Z_{\text{eff}}(np) > Z_{\text{eff}}(nd) > Z_{\text{eff}}(nf)$$
The radial distribution function $4\pi r^2 R_{nl}^2(r)$ proves that $ns$ orbitals possess $(n-1)$ radial nodes, with substantial probability density very close to the nucleus ($r \rightarrow 0$), successfully *penetrating* the inner core electron cloud. In contrast, $nd$ and $nf$ orbitals have zero or few radial nodes, remaining non-penetrating and heavily shielded."""
            },
            {
                "id": "sec2_3",
                "title": "§2.3 Periodic Trends: Radii, Ionization Energies & Electron Affinities",
                "content": r"""### Systematic Anatomy of Periodic Trends

All macroscopic chemical and physical properties of the elements—from lattice constants and bond energies to reduction potentials and catalytic activities—are direct manifestations of three foundational atomic parameters:
1. **Atomic and Ionic Radii**
2. **Ionization Energies ($\text{IE}$)**
3. **Electron Affinities ($\text{EA}$)**

---

### 1. Atomic and Ionic Radii

Because an electron's wavefunction $\psi(\mathbf{r})$ decays exponentially toward infinity without a hard geometric boundary, an atom has no rigid physical edge. Atomic size is experimentally defined by interatomic distances in condensed phases:
- **Covalent Radius ($r_{\text{cov}}$)**: Half the internuclear separation between identical atoms joined by a single covalent bond: $r_{\text{cov}}(\text{Cl}) = \frac{198\text{ pm}}{2} = 99\text{ pm}$.
- **Van der Waals Radius ($r_{\text{vdW}}$)**: Half the shortest internuclear distance between non-bonded atoms in a crystal lattice ($r_{\text{vdW}}(\text{Cl}) \approx 175\text{ pm}$).
- **Ionic Radius ($r_{\text{ion}}$)**: Shannon-Prewitt crystal radii determined from X-ray crystallographic unit cell dimensions (anchored to $r(\text{O}^{2-}) = 140\text{ pm}$ or $r(\text{F}^-) = 133\text{ pm}$ in octahedral coordination).
- **Metallic Radius ($r_{\text{met}}$)**: Half the distance between adjacent metal cations in a metallic close-packed crystal lattice.

```
       Comparative Radial Scales for Chlorine:
       
       Covalent Radius (r_cov = 99 pm)      Van der Waals Radius (r_vdW = 175 pm)
            [ Cl ]---[ Cl ]                      (   Cl   ) . . . (   Cl   )
            |<-- 198 pm ->|                      |<------- 350 pm -------->|
```

#### Governing Periodic Trajectories:
1. **Across a Period (Left to Right)**:
   Atomic radius **strictly decreases**. As $Z$ increases, additional electrons enter the same principal shell, shielding each other poorly ($\sigma \sim 0.35$). Consequently, $Z_{\text{eff}}$ increases by $\approx 0.65$ per element, drawing the valence electron cloud inward:
   $$r(\text{Li}) = 152\text{ pm} \longrightarrow r(\text{F}) = 71\text{ pm}$$
2. **Down a Group (Top to Bottom)**:
   Atomic radius **increases**. Each successive row adds a new principal electronic shell ($n \rightarrow n+1$). The larger average radial expectation value $\langle r \rangle \propto \frac{n^2 a_0}{Z_{\text{eff}}}$ overwhelms the modest increase in $Z_{\text{eff}}$:
   $$r(\text{F}) = 71\text{ pm} \longrightarrow r(\text{Cl}) = 99\text{ pm} \longrightarrow r(\text{Br}) = 114\text{ pm} \longrightarrow r(\text{I}) = 133\text{ pm}$$
3. **Cations vs Anions**:
   - Cations are **substantially smaller** than their parent neutral atoms ($r(\text{Na}^+) = 102\text{ pm}$ vs $r(\text{Na}) = 186\text{ pm}$) due to loss of the valence shell and increased $\frac{Z}{N_e}$ ratio.
   - Anions are **substantially larger** than their parent neutral atoms ($r(\text{Cl}^-) = 181\text{ pm}$ vs $r(\text{Cl}) = 99\text{ pm}$) due to interelectronic Coulombic repulsion expanding the diffuse valence shell.

---

### 2. Ionization Energy ($\text{IE}$) and Its Fine-Structure Anomalies

The First Ionization Energy ($\text{IE}_1$) is the minimum energy required to remove an electron from an isolated, neutral gas-phase atom in its ground state:
$$\text{X}(g) \longrightarrow \text{X}^+(g) + e^-, \quad \Delta H = \text{IE}_1 > 0$$

#### General Trend:
$\text{IE}_1$ increases across a period (escalating $Z_{\text{eff}}$) and decreases down a group (increasing $n$ and orbital radius). However, high-precision spectroscopy reveals **two profound periodic anomalies** across every representative row:

```
   Fine Structure of First Ionization Energies Across Period 2:
   
   IE1 (kJ/mol)
   2500 |                                                 Ne (2081)
        |                                                /
   2000 |                                         F (1681)
        |                                        /
   1500 |                         N (1402)      O (1314) <-- Pairing Repulsion Anomaly!
        |                        /        \    /
   1000 |         Be (899)      C (1086)   \--/
        |        /        \    /
    500 |  Li(520)         B (801) <-- Subshell Penetration Anomaly!
        +------------------------------------------------------------> Element
```

#### Anomaly 1: Beryllium ($Z=4$) vs Boron ($Z=5$) [Group 2 vs Group 13]:
- $\text{Be}: 1s^2 2s^2 \implies \text{IE}_1 = 899\text{ kJ}\cdot\text{mol}^{-1}$
- $\text{B}: 1s^2 2s^2 2p^1 \implies \text{IE}_1 = 801\text{ kJ}\cdot\text{mol}^{-1}$
**Quantum Origin**: The $2s$ electrons in Be possess high radial penetration, feeling elevated $Z_{\text{eff}}$. In B, the single $2p$ electron occupies an orbital with a radial node at the nucleus; it is completely shielded from the nucleus by the $1s^2$ and $2s^2$ core electrons ($\sigma \approx 2.57$), making it energetically easier to remove despite higher nuclear charge $Z=5$.

#### Anomaly 2: Nitrogen ($Z=7$) vs Oxygen ($Z=8$) [Group 15 vs Group 16]:
- $\text{N}: 1s^2 2s^2 2p_x^1 2p_y^1 2p_z^1 \implies \text{IE}_1 = 1402\text{ kJ}\cdot\text{mol}^{-1}$
- $\text{O}: 1s^2 2s^2 2p_x^2 2p_y^1 2p_z^1 \implies \text{IE}_1 = 1314\text{ kJ}\cdot\text{mol}^{-1}$
**Quantum Origin**: Nitrogen possesses a spherically symmetric, half-filled $2p^3$ subshell maximizing exchange stabilization energy ($K_{\text{ex}} = \frac{n(n-1)}{2} K = 3K$). In oxygen ($2p^4$), two electrons are forced to occupy the same spatial $2p_x$ orbital. The intense interelectronic Coulombic repulsion ($\Pi_c$) between this spin-paired electron pair raises the orbital energy, facilitating electron ejection.

---

### 3. Electron Affinity ($\text{EA}$) and the Fluorine-Chlorine Anomaly

The Electron Affinity ($\text{EA}$) is the energy change accompanying the capture of an electron by an isolated gaseous atom:
$$\text{X}(g) + e^- \longrightarrow \text{X}^-(g), \quad \Delta H_{\text{gain}} = -\text{EA}$$

#### The Halogen Electron Affinity Inversion:
One of the most celebrated anomalies in inorganic chemistry is that **Chlorine has a higher electron affinity than Fluorine**:
$$\text{EA}(\text{Cl}) = +349.0\text{ kJ}\cdot\text{mol}^{-1} \quad \text{vs} \quad \text{EA}(\text{F}) = +328.0\text{ kJ}\cdot\text{mol}^{-1}$$
Similarly, for Group 16: $\text{EA}(\text{S}) = +200.4\text{ kJ}\cdot\text{mol}^{-1} > \text{EA}(\text{O}) = +141.0\text{ kJ}\cdot\text{mol}^{-1}$.

**Quantum Mechanical Explanation**:
- Atomic fluorine is exceptionally compact ($r_{\text{cov}} = 71\text{ pm}$). Its seven valence electrons are crowded into diminutive $2p$ orbitals.
- Adding an eighth electron into this dense electron cloud creates enormous **interelectronic Coulombic repulsion**, which partially offsets the stabilizing nuclear attraction.
- In chlorine, the valence shell is $3p$, with an atomic radius of $99\text{ pm}$ and more than double the spatial volume ($\propto r^3$). The incoming electron is dispersed over a larger volume, minimizing repulsion and yielding a more exothermic electron capture enthalpy."""
            },
            {
                "id": "sec2_4",
                "title": "§2.4 Electronegativity Formulations: Pauling, Mulliken, Allred-Rochow & Allen Scales",
                "content": r"""### Defining the Elusive Concept of Electronegativity

While ionization energy and electron affinity are rigorous thermodynamic observables of isolated gas-phase atoms, **Electronegativity** ($\chi$) is an intrinsic chemical property of an atom *embedded within a bonded chemical compound*. First conceptualized by Jöns Jacob Berzelius (1811) and formally defined by Linus Pauling (1932):

> **Pauling's Definition**: *Electronegativity is the power of an atom in a molecule to attract electrons to itself.*

Because electronegativity depends on chemical environment and orbital hybridization, several distinct theoretical frameworks have been formulated to quantify it:

---

### 1. Pauling's Thermochemical Scale (1932)

Pauling anchored electronegativity to the extra stabilization energy observed in heteronuclear bonds relative to homonuclear bonds.
If a bond between $A$ and $B$ were purely covalent, its bond dissociation enthalpy $D(A-B)$ should approximate the geometric (or arithmetic) mean of the homonuclear covalent bonds $D(A-A)$ and $D(B-B)$:
$$D_{\text{covalent}}(A-B) = \sqrt{D(A-A) \cdot D(B-B)}$$

In reality, whenever $A$ and $B$ differ in electronegativity, the experimental bond enthalpy $D(A-B)$ is strictly greater than the geometric mean due to **ionic resonance stabilization** ($A^+ B^-$):
$$\Delta_{AB} = D(A-B) - \sqrt{D(A-A) \cdot D(B-B)} \ge 0$$

Pauling defined the difference in electronegativity $|\chi_A - \chi_B|$ as proportional to the square root of this excess resonance energy:
$$|\chi_A - \chi_B| = 0.102 \sqrt{\Delta_{AB}} \quad (\text{with } D \text{ in kJ}\cdot\text{mol}^{-1})$$
$$|\chi_A - \chi_B| = 0.208 \sqrt{\Delta_{AB}} \quad (\text{with } D \text{ in kcal}\cdot\text{mol}^{-1})$$

To establish an absolute scale, Pauling arbitrarily set **Fluorine at $\chi_{\text{Pauling}} = 4.00$** (later refined to $3.98$).

---

### 2. Mulliken's Absolute Electronic Scale (Robert Mulliken, 1934)

Mulliken established an absolute physical scale based solely on spectroscopic properties of the isolated atom. He reasoned that an atom's tendency to attract electrons is the average of its resistance to losing an electron ($\text{IE}$) and its desire to gain an electron ($\text{EA}$):
$$\chi_{\text{Mulliken}} = \frac{\text{IE} + \text{EA}}{2}$$
where $\text{IE}$ and $\text{EA}$ are evaluated in electron-volts ($\text{eV}$).

To map Mulliken values onto Pauling's dimensionless scale:
$$\chi_{\text{Pauling}} \approx 0.336 (\chi_{\text{Mulliken}} - 0.615)$$

#### Quantum Mechanical Significance:
In Density Functional Theory (DFT), the negative of Mulliken electronegativity corresponds identically to the **Electronic Chemical Potential** ($\mu$):
$$\chi = -\mu = -\left( \frac{\partial E}{\partial N} \right)_{v(\mathbf{r})}$$
When two atoms form a chemical bond, electrons spontaneously flow from the atom of lower $\chi$ (higher chemical potential) to the atom of higher $\chi$ (lower chemical potential) until their chemical potentials equalize: $\mu_A = \mu_B$ (**Electronegativity Equalization Principle**, Roberto Sanderson).

---

### 3. Allred-Rochow Electrostatic Scale (1958)

A. Louis Allred and Eugene G. Rochow treated electronegativity as the classical electrostatic Coulombic electric field force exerted by an atom's effective nuclear charge on an electron positioned at its covalent boundary:
$$F_{\text{Coulomb}} = \frac{e^2 Z_{\text{eff}}}{4\pi\varepsilon_0 r_{\text{cov}}^2}$$

Using Slater's rules to calculate $Z_{\text{eff}}$ and expressing covalent radius $r_{\text{cov}}$ in Ångströms ($\text{\AA}$):
$$\chi_{\text{AR}} = 0.359 \frac{Z_{\text{eff}}}{r_{\text{cov}}^2} + 0.744$$
The empirical constants $0.359$ and $0.744$ were calibrated via linear regression to maximize numerical coincidence with Pauling's scale.

---

### 4. Allen's Spectroscopic Electronegativity (Leland Allen, 1989)

Leland Allen defined the "third dimension of the periodic table" as the configuration energy ($CE$), the average one-electron energy of valence electrons in ground-state free atoms:
$$\chi_{\text{Allen}} = \frac{m \epsilon_s + n \epsilon_p}{m + n}$$
where $m$ and $n$ are the number of valence $s$ and $p$ electrons, and $\epsilon_s, \epsilon_p$ are their spectroscopic multiplet-averaged ionization potentials measured via high-resolution atomic spectroscopy.

```
   Comprehensive Electronegativity Comparison Across Selected Elements:
   
   Element   Pauling (χ_P)   Mulliken (χ_M, eV)   Allred-Rochow (χ_AR)   Allen (χ_spec)
   -----------------------------------------------------------------------------------
   H         2.20            7.18                 2.20                   2.300
   Li        0.98            3.00                 0.97                   0.912
   C         2.55            6.27                 2.50                   2.544
   N         3.04            7.30                 3.07                   3.066
   O         3.44            7.54                 3.50                   3.610
   F         3.98            10.41                4.10                   4.193
   Na        0.93            2.85                 1.01                   0.869
   Cl        3.16            8.30                 2.83                   2.869
   Cs        0.79            2.18                 0.86                   0.659
```"""
            },
            {
                "id": "sec2_5",
                "title": "§2.5 Relativistic Contraction, The Lanthanide Contraction & The Inert Pair Effect",
                "content": r"""### When Quantum Mechanics Meets Special Relativity

In standard non-relativistic quantum mechanics, the electron mass $m_e$ is treated as an invariant constant. However, for heavy elements with large nuclear charge $Z$ (particularly Period 6 and Period 7: $Z \ge 70$, such as $\text{Au, Hg, Tl, Pb, Bi}$), the Coulombic attractive velocity of inner core $1s$ electrons approaches a substantial fraction of the speed of light $c \approx 3.0 \times 10^8\text{ m/s}$.

In the Bohr model, the average velocity of an electron in level $n$ is:
$$\langle v \rangle = \frac{Z e^2}{2\varepsilon_0 n h} = \frac{Z c \alpha}{n} \approx \frac{Z}{137 n} c$$
where $\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c} \approx \frac{1}{137.036}$ is the fine-structure constant.

For gold ($Z = 79$):
$$v_{1s} \approx \frac{79}{137} c \approx 0.58 c$$
Core $1s$ electrons in gold travel at nearly **$58\%$ the speed of light**!

According to Einstein's Special Theory of Relativity, an object moving at velocity $v$ experiences relativistic mass dilation:
$$m_{\text{rel}} = \frac{m_0}{\sqrt{1 - (v/c)^2}}$$
For $v = 0.58c$:
$$m_{\text{rel}} = \frac{m_0}{\sqrt{1 - (0.58)^2}} = \frac{m_0}{\sqrt{1 - 0.3364}} = \frac{m_0}{0.815} \approx 1.23 m_0$$
The electron's effective inertial mass increases by **$23\%$**!

```
   Cascade of Relativistic Orbital Effects in Heavy Atoms:
   
   v ≈ 0.6 c  -->  Relativistic Mass m_rel Increases (by ~20%)
                           |
                           v
   Bohr Radius a_0 = ħ² / (m e²) CONTRACTS Relativistically
                           |
                           v
   Direct Contraction & Stabilization of s and p Orbitals (l = 0, 1)
                           |
                           v
   Enhanced Core Screening of Nuclear Charge
                           |
                           v
   Indirect Expansion & Destabilization of d and f Orbitals (l = 2, 3)
```

---

### The Dirac Relativistic Orbital Effects

Pekka Pyykkö and Kenneth Pitzer formalized three primary relativistic consequences in heavy inorganic elements:

#### 1. Direct Relativistic Contraction and Stabilization of $s$ and $p_{1/2}$ Orbitals:
The relativistic Bohr radius is inversely proportional to mass:
$$a_{\text{rel}} = \frac{4\pi\varepsilon_0 \hbar^2}{m_{\text{rel}} e^2} = a_0 \frac{m_0}{m_{\text{rel}}}$$
Because $s$ and $p_{1/2}$ wavefunctions have non-zero probability density at the nucleus, their relativistic mass increase causes the orbitals to **contract spatially** and drop significantly in energy (**relativistic stabilization**). For the $6s$ orbital in gold and mercury, this contraction reaches $15\text{–}18\%$!

#### 2. Indirect Relativistic Expansion and Destabilization of $d$ and $f$ Orbitals:
Because the contracted core $s$ and $p$ electron clouds form a denser, more tightly bound electrostatic screen around the nucleus, the outer $d$ and $f$ electrons (which have zero probability at the nucleus, $l \ge 2$) experience a reduced $Z_{\text{eff}}$. Consequently, $5d$ and $4f$ orbitals **expand radially** and rise in energy (**relativistic destabilization**).

#### 3. Spin-Orbit Coupling Splitting ($\vec{J} = \vec{L} + \vec{S}$):
Relativistic coupling between electron spin and orbital magnetic moments splits $p, d, f$ subshells into distinct energy eigenvalues ($p_{1/2}$ and $p_{3/2}$, $d_{3/2}$ and $d_{5/2}$). In bismuth ($Z=83$), the $6p_{1/2}-6p_{3/2}$ splitting exceeds $2.16\text{ eV}$!

---

### Macroscopic Physical Manifestations of Relativistic Effects

#### 1. The Color of Metallic Gold:
Silver ($4d^{10} 5s^1$) reflects all visible light uniformly, appearing lustrous white because its $4d \rightarrow 5s$ electronic transition absorbs in the ultraviolet ($\lambda < 300\text{ nm}$).
In Gold ($5d^{10} 6s^1$), relativistic effects simultaneously **stabilize the $6s$ orbital downward** and **destabilize the $5d$ band upward**, compressing the energy gap:
$$\Delta E(5d \rightarrow 6s) \approx 2.3\text{ to } 2.4\text{ eV}$$
A photon of $2.4\text{ eV}$ corresponds to blue-violet light ($\lambda \approx 515\text{ nm}$). Gold strongly absorbs blue and violet light, reflecting green, yellow, and red wavelengths, imparting its iconic warm golden hue! Without Einstein's relativity, gold would be silver-colored!

#### 2. Why Mercury is Liquid at Room Temperature:
In Mercury ($\text{Hg}, Z = 80, [Xe] 4f^{14} 5d^{10} 6s^2$):
The relativistic contraction of the $6s^2$ shell is so severe that the two $6s$ electrons form a tightly held, inert, closed-shell spherical singlet, behaving almost like a noble gas atom ($\text{He}$). The metallic bonding between adjacent $\text{Hg}$ atoms is exceedingly weak, dominated merely by van der Waals forces. Consequently, mercury possesses an anomalously low melting point ($-38.83^\circ\text{C}$), remaining liquid at ambient temperatures.

---

### The Lanthanide Contraction and The Inert Pair Effect

#### The Lanthanide Contraction:
Between Lanthanum ($Z=57$) and Hafnium ($Z=72$), fourteen electrons are added to the buried $4f$ subshell ($4f^1$ to $4f^{14}$).
Because $4f$ orbitals possess three nodal planes and diffuse radial distributions, their spatial shielding efficiency is exceptionally poor ($\sigma_{4f} \ll 1.00$). Across the lanthanide series:
$$Z_{\text{eff}} \text{ steadily increases} \implies r(\text{La}^{3+}) = 103.2\text{ pm} \longrightarrow r(\text{Lu}^{3+}) = 86.1\text{ pm}$$
This steady contraction of $17.1\text{ pm}$ is the **Lanthanide Contraction**.

**Remarkable Consequence on Group 4 Congeners**:
- Zirconium ($4d$, Period 5, $Z=40$): $r_{\text{cov}} = 145\text{ pm}$, ionic radius $r(\text{Zr}^{4+}) = 72\text{ pm}$.
- Hafnium ($5d$, Period 6, $Z=72$): $r_{\text{cov}} = 144\text{ pm}$, ionic radius $r(\text{Hf}^{4+}) = 71\text{ pm}$!
Despite possessing 32 additional protons and an entire extra electron shell, **Hafnium is almost identical in size to Zirconium**! As a result, $\text{Zr}$ and $\text{Hf}$ exhibit virtually indistinguishable chemical properties and are notoriously difficult to separate in metallurgy.

#### The Inert Pair Effect:
In the heavy $p$-block elements of Period 6 ($\text{Tl, Pb, Bi}$), the valence $s$ electrons ($6s^2$) show reluctance to participate in covalent or ionic chemical bonding:
- Group 13: Thallium forms stable $\text{Tl(I)}$ salts ($\text{TlCl}$ is stable like $\text{NaCl}$), while $\text{Tl(III)}$ is a fierce oxidizing agent.
- Group 14: Lead forms stable $\text{Pb(II)}$ compounds ($\text{PbO}, \text{PbCl}_2$), while $\text{Pb(IV)}$ ($\text{PbO}_2$) is easily reduced.
- Group 15: Bismuth forms stable $\text{Bi(III)}$ salts, while $\text{Bi(V)}$ is virtually non-existent except as an extreme oxidant in $\text{NaBiO}_3$.

**Origin**: The combined impact of the **Lanthanide Contraction** and **Dirac Relativistic $6s$ Contraction** pulls the $6s^2$ electron pair so deeply into the core potential well that the bond energy gained by forming two additional covalent bonds cannot compensate for the enormous promotional energy required to unpair and hybridize the $6s$ electrons."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 2.1: Quantitative Slater Effective Nuclear Charge Derivation and Ionization Potential Prediction",
                "statement": r"""Using Slater's rules:
1. Calculate the screening constant ($\sigma$) and the effective nuclear charge ($Z_{\text{eff}}$) experienced by:
   - A valence $2p$ electron in a neutral Nitrogen atom ($Z = 7$).
   - A valence $2p$ electron in a neutral Oxygen atom ($Z = 8$).
   - A valence $4s$ electron in a neutral Calcium atom ($Z = 20$).
   - A $3d$ electron in a neutral Iron atom ($Z = 26$).
   - A $4s$ electron in a neutral Iron atom ($Z = 26$).
2. Based on your calculated $Z_{\text{eff}}$ values for Iron, explain with rigorous thermodynamic and orbital arguments why the first two electrons lost during the oxidation of iron to ferrous iron ($\text{Fe} \rightarrow \text{Fe}^{2+} + 2e^-$) are removed from the $4s$ subshell rather than the $3d$ subshell, even though the Aufbau principle populates $4s$ before $3d$ in the neutral atom.
3. Compute the approximate Slater orbital energy $E_{2p} = -13.6\text{ eV} \frac{Z_{\text{eff}}^2}{(n^*)^2}$ for Nitrogen and Oxygen and compare the predicted trend with the experimental first ionization energies ($\text{IE}_1(\text{N}) = 14.53\text{ eV}$, $\text{IE}_1(\text{O}) = 13.62\text{ eV}$). Explain why Slater's rules fail to predict the experimental inversion.""",
                "solution": r"""### Part 1: Stepwise Slater Screening Constant Calculations

#### 1. Valence $2p$ electron in Nitrogen ($Z = 7$):
- Electron configuration: $[1s^2] [2s^2, 2p^3]$
- Target electron: one of the $2p$ electrons in the $[2s, 2p]$ group.
- Remaining electrons in same $[2s, 2p]$ group: $4 \text{ electrons} \implies 4 \times 0.35 = 1.40$
- Electrons in $(n-1) = 1$ group ($[1s]$): $2 \text{ electrons} \implies 2 \times 0.85 = 1.70$
$$\sigma(\text{N}, 2p) = 1.40 + 1.70 = 3.10$$
$$Z_{\text{eff}}(\text{N}, 2p) = 7 - 3.10 = \mathbf{3.90}$$

#### 2. Valence $2p$ electron in Oxygen ($Z = 8$):
- Electron configuration: $[1s^2] [2s^2, 2p^4]$
- Target electron: one of the $2p$ electrons in the $[2s, 2p]$ group.
- Remaining electrons in same $[2s, 2p]$ group: $5 \text{ electrons} \implies 5 \times 0.35 = 1.75$
- Electrons in $(n-1) = 1$ group ($[1s]$): $2 \text{ electrons} \implies 2 \times 0.85 = 1.70$
$$\sigma(\text{O}, 2p) = 1.75 + 1.70 = 3.45$$
$$Z_{\text{eff}}(\text{O}, 2p) = 8 - 3.45 = \mathbf{4.55}$$

#### 3. Valence $4s$ electron in Calcium ($Z = 20$):
- Electron configuration: $[1s^2] [2s^2, 2p^6] [3s^2, 3p^6] [4s^2]$
- Target electron: one $4s$ electron in $[4s]$ group.
- Other electron in $[4s]$: $1 \times 0.35 = 0.35$
- Electrons in $(n-1) = 3$ group ($[3s, 3p]$): $8 \times 0.85 = 6.80$
- Electrons in $(n-2)$ and deeper ($[1s], [2s, 2p]$): $10 \times 1.00 = 10.00$
$$\sigma(\text{Ca}, 4s) = 0.35 + 6.80 + 10.00 = 17.15$$
$$Z_{\text{eff}}(\text{Ca}, 4s) = 20 - 17.15 = \mathbf{2.85}$$

#### 4. $3d$ electron in Iron ($Z = 26$):
- Electron configuration: $[1s^2] [2s^2, 2p^6] [3s^2, 3p^6] [3d^6] [4s^2]$
- Target: one $3d$ electron in $[3d]$ group.
- Electrons to the right ($4s$): contribute $0.00$
- Other electrons in same $[3d]$ group: $5 \times 0.35 = 1.75$
- All 18 electrons to the left ($[1s], [2s, 2p], [3s, 3p]$): $18 \times 1.00 = 18.00$
$$\sigma(\text{Fe}, 3d) = 1.75 + 18.00 = 19.75$$
$$Z_{\text{eff}}(\text{Fe}, 3d) = 26 - 19.75 = \mathbf{6.25}$$

#### 5. $4s$ electron in Iron ($Z = 26$):
- Target: one $4s$ electron in $[4s]$ group.
- Other electron in $[4s]$: $1 \times 0.35 = 0.35$
- All 14 electrons in $(n-1) = 3$ shell ($3s^2, 3p^6, 3d^6$): $14 \times 0.85 = 11.90$
- All 10 electrons in $(n-2)$ and deeper ($1s^2, 2s^2, 2p^6$): $10 \times 1.00 = 10.00$
$$\sigma(\text{Fe}, 4s) = 0.35 + 11.90 + 10.00 = 22.25$$
$$Z_{\text{eff}}(\text{Fe}, 4s) = 26 - 22.25 = \mathbf{3.75}$$

---

### Part 2: Physical Explanation of Transition Metal Ionization Sequence
From the calculations above:
$$Z_{\text{eff}}(\text{Fe}, 3d) = 6.25 \quad \text{vs} \quad Z_{\text{eff}}(\text{Fe}, 4s) = 3.75$$
- The effective nuclear charge holding the $3d$ electrons is **$6.25$**, whereas that holding the $4s$ electrons is only **$3.75$**.
- Because the $3d$ electrons experience nearly twice the effective nuclear charge, their radial distribution is drawn closer to the nucleus once the $3d$ subshell begins to populate.
- The average radial distance $\langle r \rangle_{4s}$ of the $4s$ orbital is significantly larger than $\langle r \rangle_{3d}$.
- Therefore, the $4s$ electrons occupy a shallower potential energy well in the neutral atom and are removed first during chemical oxidation:
  $$\text{Fe} ([\text{Ar}]3d^6 4s^2) \longrightarrow \text{Fe}^{2+} ([\text{Ar}]3d^6) + 2e^-$$
- Once the two $4s$ electrons are removed, the screening experienced by the remaining $3d$ electrons drops further, causing the $3d$ orbitals to contract even more and become deeply stabilized.

---

### Part 3: Slater Energy Evaluation vs Experimental Inversion
For $n = 2$, $n^* = 2.0$:
$$E_{2p} = -13.6\text{ eV} \frac{Z_{\text{eff}}^2}{4.0}$$

1. **For Nitrogen ($Z_{\text{eff}} = 3.90$)**:
   $$E_{2p}(\text{N}) = -13.6 \times \frac{3.90^2}{4.0} = -13.6 \times \frac{15.21}{4.0} = -13.6 \times 3.8025 = \mathbf{-51.71\text{ eV}}$$
2. **For Oxygen ($Z_{\text{eff}} = 4.55$)**:
   $$E_{2p}(\text{O}) = -13.6 \times \frac{4.55^2}{4.0} = -13.6 \times \frac{20.7025}{4.0} = -13.6 \times 5.1756 = \mathbf{-70.39\text{ eV}}$$

#### Why Slater's Model Fails to Predict the Inversion:
Slater's model predicts that oxygen electrons are held significantly more tightly than nitrogen electrons ($-70.39\text{ eV}$ vs $-51.71\text{ eV}$), implying that $\text{IE}_1(\text{O}) \gg \text{IE}_1(\text{N})$.
However, experimentally:
$$\text{IE}_1(\text{N}) = 14.53\text{ eV} \quad > \quad \text{IE}_1(\text{O}) = 13.62\text{ eV}$$

Slater's rules fail because they are a **purely electrostatic central-field approximation** that neglects:
1. **Exchange Stabilization Energy**: Nitrogen has a half-filled $2p^3$ configuration with all three electrons having parallel spins ($\uparrow\uparrow\uparrow$), maximizing quantum exchange energy ($3K_{\text{ex}}$). Ejecting an electron from nitrogen destroys two favorable exchange interactions.
2. **Interelectronic Pairing Repulsion**: In oxygen ($2p^4$), two electrons must pair up in the same $p_x$ orbital ($\uparrow\downarrow$). The spatial coincidence of two negative charges in the identical orbital creates a powerful repulsive pairing energy ($\Pi_c \approx 1\text{–}2\text{ eV}$) that destabilizes the ground state, lowering the energy needed to eject the electron."""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 2.2: Analytical Formulation of the Allred-Rochow and Pauling Electronegativity Relationship",
                "statement": r"""Given the following thermochemical bond dissociation enthalpies at $298.15\text{ K}$:
- $D(\text{H}-\text{H}) = 436.0\text{ kJ}\cdot\text{mol}^{-1}$
- $D(\text{F}-\text{F}) = 159.0\text{ kJ}\cdot\text{mol}^{-1}$
- $D(\text{Cl}-\text{Cl}) = 242.0\text{ kJ}\cdot\text{mol}^{-1}$
- $D(\text{H}-\text{F}) = 568.0\text{ kJ}\cdot\text{mol}^{-1}$
- $D(\text{H}-\text{Cl}) = 431.0\text{ kJ}\cdot\text{mol}^{-1}$

1. Calculate the Pauling electronegativity difference $|\chi_{\text{F}} - \chi_{\text{H}}|$ and $|\chi_{\text{Cl}} - \chi_{\text{H}}|$ using the geometric mean formulation:
   $$\Delta_{AB} = D(A-B) - \sqrt{D(A-A) \cdot D(B-B)}$$
   Taking $\chi_{\text{H}} = 2.20$, compute the Pauling electronegativities of Fluorine and Chlorine.
2. Calculate the Allred-Rochow electronegativity ($\chi_{\text{AR}}$) for Silicon ($Z = 14$, $r_{\text{cov}} = 1.17\text{ \AA}$) and Chlorine ($Z = 17$, $r_{\text{cov}} = 0.99\text{ \AA}$) using Slater's rules to evaluate $Z_{\text{eff}}$:
   $$\chi_{\text{AR}} = 0.359 \frac{Z_{\text{eff}}}{r_{\text{cov}}^2} + 0.744$$
3. Discuss why Pauling's thermochemical scale and the Allred-Rochow electrostatic scale show slight deviations for elements involving multiple bonding or heavy polarizable cores.""",
                "solution": r"""### Part 1: Pauling Electronegativity Calculations

Pauling's formula with bond enthalpies in $\text{kJ}\cdot\text{mol}^{-1}$:
$$|\chi_A - \chi_B| = 0.102 \sqrt{\Delta_{AB}}$$
$$\Delta_{AB} = D(A-B) - \sqrt{D(A-A) \cdot D(B-B)}$$

#### 1. For Hydrogen Fluoride ($\text{H}-\text{F}$):
$$D(\text{H}-\text{H}) = 436.0\text{ kJ}\cdot\text{mol}^{-1}, \quad D(\text{F}-\text{F}) = 159.0\text{ kJ}\cdot\text{mol}^{-1}, \quad D(\text{H}-\text{F}) = 568.0\text{ kJ}\cdot\text{mol}^{-1}$$
$$\sqrt{D(\text{H}-\text{H}) \cdot D(\text{F}-\text{F})} = \sqrt{436.0 \times 159.0} = \sqrt{69324.0} \approx 263.29\text{ kJ}\cdot\text{mol}^{-1}$$
$$\Delta_{\text{HF}} = 568.0 - 263.29 = 304.71\text{ kJ}\cdot\text{mol}^{-1}$$
$$|\chi_{\text{F}} - \chi_{\text{H}}| = 0.102 \times \sqrt{304.71} = 0.102 \times 17.456 = \mathbf{1.780}$$
Given $\chi_{\text{H}} = 2.20$:
$$\chi_{\text{F}} = 2.20 + 1.780 = \mathbf{3.98}$$
*(Matches the standard modern accepted Pauling value of $3.98$ exactly!)*

---

#### 2. For Hydrogen Chloride ($\text{H}-\text{Cl}$):
$$D(\text{Cl}-\text{Cl}) = 242.0\text{ kJ}\cdot\text{mol}^{-1}, \quad D(\text{H}-\text{Cl}) = 431.0\text{ kJ}\cdot\text{mol}^{-1}$$
$$\sqrt{D(\text{H}-\text{H}) \cdot D(\text{Cl}-\text{Cl})} = \sqrt{436.0 \times 242.0} = \sqrt{105512.0} \approx 324.83\text{ kJ}\cdot\text{mol}^{-1}$$
$$\Delta_{\text{HCl}} = 431.0 - 324.83 = 106.17\text{ kJ}\cdot\text{mol}^{-1}$$
$$|\chi_{\text{Cl}} - \chi_{\text{H}}| = 0.102 \times \sqrt{106.17} = 0.102 \times 10.304 = \mathbf{1.051}$$
Given $\chi_{\text{H}} = 2.20$:
$$\chi_{\text{Cl}} = 2.20 + 1.051 = \mathbf{3.25} \quad (\approx 3.16)$$

---

### Part 2: Allred-Rochow Electronegativity Calculations

Formula: $\chi_{\text{AR}} = 0.359 \frac{Z_{\text{eff}}}{r_{\text{cov}}^2} + 0.744$ (with $r_{\text{cov}}$ in $\text{\AA}$).

#### 1. Silicon ($Z = 14, r_{\text{cov}} = 1.17\text{ \AA}$):
- Configuration: $[1s^2] [2s^2, 2p^6] [3s^2, 3p^2]$
- Target electron: $3p$
- Other electrons in $[3s, 3p]$: $3 \times 0.35 = 1.05$
- Electrons in $(n-1) = 2$: $8 \times 0.85 = 6.80$
- Electrons in $(n-2) = 1$: $2 \times 1.00 = 2.00$
$$\sigma(\text{Si}) = 1.05 + 6.80 + 2.00 = 9.85$$
$$Z_{\text{eff}}(\text{Si}) = 14 - 9.85 = 4.15$$
$$\chi_{\text{AR}}(\text{Si}) = 0.359 \times \frac{4.15}{(1.17)^2} + 0.744 = 0.359 \times \frac{4.15}{1.3689} + 0.744 = 0.359 \times 3.0316 + 0.744$$
$$\chi_{\text{AR}}(\text{Si}) = 1.088 + 0.744 = \mathbf{1.83} \quad (\approx 1.90)$$

#### 2. Chlorine ($Z = 17, r_{\text{cov}} = 0.99\text{ \AA}$):
- Configuration: $[1s^2] [2s^2, 2p^6] [3s^2, 3p^5]$
- Other electrons in $[3s, 3p]$: $6 \times 0.35 = 2.10$
- Electrons in $(n-1)$: $8 \times 0.85 = 6.80$
- Electrons in $(n-2)$: $2 \times 1.00 = 2.00$
$$\sigma(\text{Cl}) = 2.10 + 6.80 + 2.00 = 10.90$$
$$Z_{\text{eff}}(\text{Cl}) = 17 - 10.90 = 6.10$$
$$\chi_{\text{AR}}(\text{Cl}) = 0.359 \times \frac{6.10}{(0.99)^2} + 0.744 = 0.359 \times \frac{6.10}{0.9801} + 0.744 = 0.359 \times 6.2238 + 0.744$$
$$\chi_{\text{AR}}(\text{Cl}) = 2.234 + 0.744 = \mathbf{2.98} \quad (\approx 2.83)$$

---

### Part 3: Physical Discussion of Scale Divergences
The slight discrepancies between Pauling and Allred-Rochow values arise from fundamental differences in what each scale measures:
1. **Pauling's scale is macroscopic and thermochemical**: It measures the extra thermodynamic stability of bonds in specific molecules. Consequently, Pauling values reflect secondary effects such as $\pi$-bonding contributions, lone pair repulsions, and steric crowding in the reference molecules chosen.
2. **Allred-Rochow's scale is microscopic and electrostatic**: It measures the classical electrostatic force exerted on an electron at the covalent radius. It assumes a spherically symmetric atom and relies on Slater's approximate screening rules, which underestimate core penetration by $s$ orbitals and overestimate screening by $d$ electrons."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 2.3: Mathematical Modeling of Dirac Relativistic Orbital Contraction and the Chemistry of Gold and Mercury",
                "statement": r"""1. Derive the relativistic contraction ratio $\frac{a_{\text{rel}}}{a_0}$ for a $1s$ electron as a function of atomic number $Z$, using the relativistic mass dilation formula $m_{\text{rel}} = \frac{m_0}{\sqrt{1 - (v/c)^2}}$ and the Bohr orbital velocity $v_{1s} = Z \alpha c$, where $\alpha \approx \frac{1}{137.036}$ is the fine-structure constant.
2. Calculate the theoretical percentage contraction of the $1s$ orbital for:
   - Carbon ($Z = 6$)
   - Copper ($Z = 29$)
   - Gold ($Z = 79$)
   - Element 118 (Oganesson, $Z = 118$)
3. Using second-order relativistic perturbation theory, explain the **indirect relativistic expansion** of the $5d$ orbitals in gold. Demonstrate how the combined direct $6s$ contraction and indirect $5d$ expansion reduce the $5d \rightarrow 6s$ energy separation to $\sim 2.4\text{ eV}$, quantitatively accounting for the yellow optical absorption spectrum of metallic gold.""",
                "solution": r"""### Part 1: Derivation of the Relativistic Orbital Contraction Ratio

In the Bohr atomic model, the balance between Coulombic attraction and centripetal force yields:
$$\frac{m v^2}{r} = \frac{Z e^2}{4\pi\varepsilon_0 r^2} \implies v = \frac{Z e^2}{4\pi\varepsilon_0 n \hbar}$$
For the ground state ($n = 1$):
$$v_{1s} = \frac{Z e^2}{4\pi\varepsilon_0 \hbar c} c = Z \alpha c$$
where $\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c} \approx \frac{1}{137.036}$ is the dimensionless fine-structure constant.

The relativistic mass of the electron moving at speed $v_{1s}$ is:
$$m_{\text{rel}} = \frac{m_0}{\sqrt{1 - (v_{1s}/c)^2}} = \frac{m_0}{\sqrt{1 - (Z\alpha)^2}}$$

The Bohr radius is given by:
$$a_0 = \frac{4\pi\varepsilon_0 \hbar^2}{m_0 e^2}$$
Substituting the relativistic mass $m_{\text{rel}}$ yields the relativistic orbital radius $a_{\text{rel}}$:
$$a_{\text{rel}} = \frac{4\pi\varepsilon_0 \hbar^2}{m_{\text{rel}} e^2} = a_0 \frac{m_0}{m_{\text{rel}}}$$
$$a_{\text{rel}} = a_0 \sqrt{1 - (Z\alpha)^2}$$

$$\mathbf{\frac{a_{\text{rel}}}{a_0} = \sqrt{1 - \left(\frac{Z}{137.036}\right)^2} \quad \text{(Proven)}}$$

---

### Part 2: Percentage Contraction Calculations
The fractional percentage contraction is:
$$\% \text{ Contraction} = \left( 1 - \frac{a_{\text{rel}}}{a_0} \right) \times 100\% = \left( 1 - \sqrt{1 - (Z\alpha)^2} \right) \times 100\%$$

#### 1. Carbon ($Z = 6$):
$$Z \alpha = \frac{6}{137.036} \approx 0.04378$$
$$(Z\alpha)^2 \approx 0.001917$$
$$\frac{a_{\text{rel}}}{a_0} = \sqrt{1 - 0.001917} = \sqrt{0.998083} \approx 0.99904$$
$$\% \text{ Contraction}(\text{C}) = (1 - 0.99904) \times 100\% = \mathbf{0.096\%} \quad (\text{Negligible})$$

#### 2. Copper ($Z = 29$):
$$Z \alpha = \frac{29}{137.036} \approx 0.21162$$
$$(Z\alpha)^2 \approx 0.04478$$
$$\frac{a_{\text{rel}}}{a_0} = \sqrt{1 - 0.04478} = \sqrt{0.95522} \approx 0.97735$$
$$\% \text{ Contraction}(\text{Cu}) = (1 - 0.97735) \times 100\% = \mathbf{2.26\%}$$

#### 3. Gold ($Z = 79$):
$$Z \alpha = \frac{79}{137.036} \approx 0.57649$$
$$(Z\alpha)^2 \approx 0.33234$$
$$\frac{a_{\text{rel}}}{a_0} = \sqrt{1 - 0.33234} = \sqrt{0.66766} \approx 0.81710$$
$$\% \text{ Contraction}(\text{Au}) = (1 - 0.81710) \times 100\% = \mathbf{18.29\%}$$
*(In gold, the $1s$ core orbital contracts by over $18\%$!)*

#### 4. Oganesson ($Z = 118$):
$$Z \alpha = \frac{118}{137.036} \approx 0.86109$$
$$(Z\alpha)^2 \approx 0.74147$$
$$\frac{a_{\text{rel}}}{a_0} = \sqrt{1 - 0.74147} = \sqrt{0.25853} \approx 0.50846$$
$$\% \text{ Contraction}(\text{Og}) = (1 - 0.50846) \times 100\% = \mathbf{49.15\%}$$
*(In superheavy elements, the inner core is compressed by nearly half!)*

---

### Part 3: Quantum Mechanical Origin of Gold's Golden Color
1. **Direct Contraction of $6s$ Orbital**:
   Because higher $s$ orbitals ($2s, 3s, \dots, 6s$) must remain mutually orthogonal to the core $1s$ orbital ($\langle n s | 1s \rangle = 0$), the severe contraction of $1s$ propagates outward through all $s$ subshells. The $6s$ valence orbital of gold experiences a direct relativistic contraction of $\sim 16\%$, pulling it into a deeper potential well and **stabilizing its energy level downward** by $\sim 1.6\text{ eV}$.
2. **Indirect Expansion of $5d$ Orbitals**:
   The contracted core $s$ and $p$ electrons form a denser, more tightly bound electrostatic screening shell around the nucleus. The $5d$ electrons possess angular momentum $l = 2$ and have zero probability density at the nucleus ($|\psi_{5d}(0)|^2 = 0$). Because they reside outside the contracted core, they experience an increased screening constant ($\sigma \uparrow$) and a diminished effective nuclear charge ($Z_{\text{eff}} \downarrow$).
   Consequently, the $5d$ orbitals **expand radially outward** and are **destabilized upward in energy** by $\sim 0.8\text{ eV}$.
3. **Bandgap Reduction and Optical Absorption**:
   In non-relativistic calculations, the transition energy between the filled $5d$ band and the Fermi level (dominated by the half-filled $6s$ band) is predicted to be:
   $$\Delta E_{\text{non-rel}}(5d \rightarrow 6s) \approx 3.7\text{ eV}$$
   A transition of $3.7\text{ eV}$ requires ultraviolet light ($\lambda \approx 335\text{ nm}$). Non-relativistic gold would reflect all visible wavelengths, appearing silvery-white like silver.
   However, accounting for relativity:
   $$\Delta E_{\text{rel}} = \Delta E_{\text{non-rel}} - \Delta E_{\text{stabilization}}(6s) - \Delta E_{\text{destabilization}}(5d)$$
   $$\Delta E_{\text{rel}} \approx 3.7 - 1.6 - 0.8 \approx \mathbf{2.3\text{ to } 2.4\text{ eV}}$$
   A photon energy of $2.3\text{–}2.4\text{ eV}$ corresponds to:
   $$\lambda = \frac{h c}{\Delta E} = \frac{1239.8\text{ eV}\cdot\text{nm}}{2.35\text{ eV}} \approx 527\text{ nm} \quad (\text{Blue-Green Light})$$
   Metallic gold strongly absorbs blue and violet photons ($\lambda \le 520\text{ nm}$), while green, yellow, and red light are efficiently reflected. The superposition of these reflected wavelengths gives gold its characteristic brilliant yellow-gold luster."""
            }
        ]
    }
'''

with open("build_inorg1_unit2.py", "w", encoding="utf-8") as f:
    f.write(content)

print("build_inorg1_unit2.py expanded successfully.")
