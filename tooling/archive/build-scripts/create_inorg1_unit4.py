#!/usr/bin/env python3
"""
create_inorg1_unit4.py
Generates build_inorg1_unit4.py for Unit 4:
The Chemical Bond II: Covalent Bonding, Lewis Structures, Resonance & Bond Enthalpies
"""

import sys

content = r'''# -*- coding: utf-8 -*-
"""
Unit 4: The Chemical Bond II: Covalent Bonding, Lewis Structures, Resonance & Bond Enthalpies
Contains 5 comprehensive sections and 3 tiered solved problems with full derivations.
"""

def get_unit4():
    return {
        "id": "unit4",
        "title": "Unit 4: The Chemical Bond II: Covalent Bonding, Lewis Structures, Resonance & Bond Enthalpies",
        "simId": "sim_chem_vsepr_molecular_geometry",
        "simTitle": "VSEPR Geometry & Steric Repulsion Suite",
        "sections": [
            {
                "id": "sec4_1",
                "title": "§4.1 Classical Lewis Formalism, Octet Rule & Formal Charge Topologies",
                "content": r"""### The Electronic Basis of Covalent Bonding

In 1916, Gilbert N. Lewis revolutionized chemical structure theory by proposing that a covalent bond consists of a pair of valence electrons shared between two atomic nuclei. In this framework, atoms share electron pairs until each participating atom attains an energetically favored, closed-shell noble gas valence electron configuration—typically an octet of eight valence electrons ($ns^2 np^6$) for main-group elements, or a duet ($1s^2$) for hydrogen and helium.

#### The Octet Rule and Electron Counting
The driving force for electron sharing is the stabilization attained when electron density accumulates in the internuclear bonding region, simultaneously experiencing attractive Coulombic potentials from both positively charged nuclei while shielding the nuclei from mutual repulsion.

For a molecule or polyatomic ion containing $N$ atoms, the total number of valence electrons available ($V$) is:
$$V = \sum_{i=1}^N v_i - q$$
where $v_i$ is the number of valence electrons of the $i$-th neutral atom (corresponding to its periodic group number) and $q$ is the net ionic charge of the chemical species ($q > 0$ for cations, $q < 0$ for anions).

The total number of electrons required for all atoms to attain complete closed shells ($N_{\text{octet}}$) is:
$$N_{\text{octet}} = 2 \cdot n_{\text{H}} + 8 \cdot n_{\text{heavy}}$$
where $n_{\text{H}}$ is the count of hydrogen atoms and $n_{\text{heavy}}$ is the count of non-hydrogen main-group atoms.

The minimum number of shared bonding electrons ($S$) is given by:
$$S = N_{\text{octet}} - V$$
Hence, the total number of shared electron pairs (covalent bonds) is $B = \frac{S}{2}$. The remaining unshared electrons ($U = V - S$) are assigned as non-bonding lone pairs ($L = \frac{U}{2}$) localized on terminal and central atoms.

---

### Formal Charge as an Electron Bookkeeping Metric

Because electrons in covalent bonds are shared rather than localized purely on one atom, we define **Formal Charge** ($FC$) to assess the hypothetical charge an atom would possess if all shared electron pairs were partitioned equally (purely homolytically, disregarding electronegativity differences):
$$FC = V_{\text{free}} - N_{\text{non-bonding}} - \frac{1}{2} N_{\text{bonding}}$$
where:
- $V_{\text{free}}$ is the number of valence electrons in the isolated, neutral gas-phase atom.
- $N_{\text{non-bonding}}$ is the number of unshared valence electrons (electrons residing in lone pairs, $2 \times L$).
- $N_{\text{bonding}}$ is the total number of electrons participating in covalent bonds directly attached to the atom ($2 \times \text{bonds}$).

#### Fundamental Charge Conservation Theorem:
The algebraic sum of the formal charges of all atoms in a molecule or polyatomic ion must identically equal the total net electrical charge $q$ of the species:
$$\sum_{i=1}^N FC_i = q$$

```
   Proof:
   \sum FC_i = \sum \left( V_i - N_{\text{non-bonding}, i} - \frac{1}{2} N_{\text{bonding}, i} \right)
             = \sum V_i - \left( \sum N_{\text{non-bonding}, i} + \sum \frac{1}{2} N_{\text{bonding}, i} \right)
   Since each bonding pair contributes 1 to each of the two bonded atoms,
   \sum \frac{1}{2} N_{\text{bonding}, i} = N_{\text{total bonding electrons}}.
   Therefore:
   \sum FC_i = V_{\text{total}} - (N_{\text{non-bonding}} + N_{\text{bonding}}) = V_{\text{total}} - V_{\text{assigned}} = q.
```

---

### Criteria for Determining Optimal Lewis Structures

When multiple valid topological arrangements of bonds and lone pairs satisfy the octet rule, the chemically dominant Lewis structure is identified by applying the following hierarchical stability criteria:
1. **Octet Maximization**: Structures that provide every second-period atom ($\text{C, N, O, F}$) with a complete octet take absolute precedence over open-shell structures, even if formal charges are non-zero. Second-period elements strictly cannot exceed an octet under any circumstances due to the absence of low-energy energetically accessible $d$ orbitals.
2. **Minimization of Formal Charge Magnitude**: Structures with formal charges closest to zero on all constituent atoms are favored ($\sum |FC_i|$ minimized).
3. **Electronegativity Alignment**: Where formal charges cannot be eliminated, negative formal charges must reside on the most electronegative atoms ($\chi_{\text{Pauling}}$: $\text{F} > \text{O} > \text{Cl} \approx \text{N} > \text{Br} > \text{I} \approx \text{S} > \text{C} > \text{H}$), while positive formal charges should reside on the least electronegative atoms.
4. **Adjacent Like-Charge Avoidance**: Structures with identical formal charges on directly bonded adjacent atoms ($+1$ adjacent to $+1$, or $-1$ adjacent to $-1$) are strongly disfavored due to severe local destabilizing Coulombic repulsion."""
            },
            {
                "id": "sec4_2",
                "title": "§4.2 Expanded Octets & Hypervalency",
                "content": r"""### The Phenomenon of Hypercoordination

Elements of the third and higher periods of the periodic table ($\text{P, S, Cl, As, Se, Br, Te, I, Xe}$) frequently form stable compounds in which the central atom is surrounded by $10$, $12$, or even $14$ valence electrons. Archetypal examples include phosphorus pentachloride ($\text{PCl}_5$, 10 electrons), sulfur hexafluoride ($\text{SF}_6$, 12 electrons), iodine heptafluoride ($\text{IF}_7$, 14 electrons), and xenon tetrafluoride ($\text{XeF}_4$, 12 electrons).

Such chemical species are historically termed **hypervalent** (first coined by Jeremy I. Musher in 1969 to denote molecules having an apparent formal valence shell exceeding eight electrons).

---

### The Classical Model: $d$-Orbital Hybridization ($sp^3d$ and $sp^3d^2$)

For decades, the standard textbook rationalization for hypervalency invoked the participation of low-lying empty $nd$ orbitals from the central atom:
- For $\text{PCl}_5$ ($10e^-$): Excitation of a $3s$ electron to an empty $3d$ orbital, generating five unpaired electrons hybridized into five $sp^3d$ orbitals arranged in a trigonal bipyramid.
- For $\text{SF}_6$ ($12e^-$): Promotion of two electrons into $3d_{z^2}$ and $3d_{x^2-y^2}$, forming six equivalent $sp^3d^2$ hybrid orbitals directed toward the vertices of an octahedron.

#### Quantum Mechanical Demise of the $d$-Orbital Hybridization Model
Extensive high-level *ab initio* quantum chemical calculations (by Coulson, Reed, Weinhold, and Magnusson) in the late 20th century conclusively refuted significant $d$-orbital covalent participation:
1. **Energy Gap**: In neutral sulfur or phosphorus, the energy gap between the valence $3p$ and empty $3d$ atomic orbitals is immense ($\Delta E(3p \rightarrow 3d) \approx 10\text{ to }12\text{ eV} \approx 1000\text{ kJ}\cdot\text{mol}^{-1}$). The energy gained by forming additional two-electron covalent bonds cannot compensate for this enormous promotional energy.
2. **Radial Extent**: The radial distribution function $4\pi r^2 R_{3d}^2(r)$ reveals that uncontracted $3d$ orbitals in neutral third-period atoms are extremely diffuse, extending far outside the valence bonding region, resulting in negligible spatial overlap integrals with compact ligand orbitals ($S \ll 0.1$).
3. **Population Analysis**: Modern Natural Bond Orbital (NBO) calculations demonstrate that the actual $d$-orbital occupancy in $\text{SF}_6$ is less than $0.2e^-$, functioning merely as weak polarization functions rather than primary bonding valence orbitals.

---

### The Modern Bonding Framework: Three-Center Four-Electron (3c-4e) Bonds

The rigorously verified quantum mechanical description of hypervalent molecules is the **Pimentel-Rundle Three-Center Four-Electron (3c-4e) Bonding Model**, formulated by George Pimentel and Robert E. Rundle.

Consider the linear axial fragment of sulfur hexafluoride ($\text{F}_{\text{ax}}-\text{S}-\text{F}_{\text{ax}}$) or xenon difluoride ($\text{F}-\text{Xe}-\text{F}$):
- Three collinear atomic orbitals participate: the central atom $p_z$ orbital and two ligand fluorine $2p_z$ orbitals ($\phi_{\text{F}_1}$ and $\phi_{\text{F}_2}$).
- Linear Combination of Atomic Orbitals (LCAO) generates three molecular orbitals:

```
  MO Architecture:
  
  ψ3* (Antibonding)  ---  (φ_F1 - c1·p_z - φ_F2)     [Unoccupied]
                         ^
                         |  ΔE
  ψ2  (Non-bonding)  ---  (φ_F1 - φ_F2)              [Occupied: 2 electrons]
                         ^
                         |  ΔE
  ψ1  (Bonding)      ---  (φ_F1 + c2·p_z + φ_F2)     [Occupied: 2 electrons]
```

#### Analytical Wavefunctions:
1. **Bonding Molecular Orbital ($\psi_1$)**:
   $$\psi_1 = c_1 (\phi_{\text{F}_1} + \phi_{\text{F}_2}) + c_2 \phi_{\text{S}(p_z)}$$
   Net bonding between central atom and both axial ligands.
2. **Non-Bonding Molecular Orbital ($\psi_2$)**:
   $$\psi_2 = \frac{1}{\sqrt{2}} (\phi_{\text{F}_1} - \phi_{\text{F}_2})$$
   By symmetry (ungerade inversion center), the central sulfur $p_z$ orbital has zero overlap with this ligand combination. Thus, the electron pair in $\psi_2$ resides entirely on the terminal electronegative fluorine ligands as non-bonding electron density!
3. **Antibonding Molecular Orbital ($\psi_3^*$)**:
   $$\psi_3^* = c_2 (\phi_{\text{F}_1} + \phi_{\text{F}_2}) - c_1 \phi_{\text{S}(p_z)}$$
   Strongly destabilized; remains empty in the ground state.

#### Quantitative Consequences of 3c-4e Bonding:
- **Total Electron Count**: 4 electrons occupy $\psi_1$ (2 electrons) and $\psi_2$ (2 electrons).
- **Formal Bond Order per Linkage**:
  $$\text{Bond Order} = \frac{2 \text{ bonding } e^- - 0 \text{ antibonding } e^-}{2 \times (\text{two linkages})} = \frac{2}{4} = 0.5$$
  Each axial $\text{S}-\text{F}$ bond is effectively a **half-bond** with significant ionic character ($\text{F}^{\delta-}-\text{S}^{2\delta+}-\text{F}^{\delta-}$).
- **Axial Bond Elongation**: Because the bond order is $0.5$ rather than $1.0$, the axial bonds in trigonal bipyramidal $\text{PCl}_5$ are significantly longer and weaker than the equatorial two-center two-electron (2c-2e) bonds:
  $$d(\text{P}-\text{Cl}_{\text{ax}}) = 214\text{ pm} \quad \text{vs} \quad d(\text{P}-\text{Cl}_{\text{eq}}) = 202\text{ pm}$$
- **Ligand Electronegativity Requirement**: 3c-4e bonds are stable only when terminal ligands are highly electronegative ($\text{F}, \text{O}, \text{Cl}$), stabilizing the non-bonding electron pair localized on the ligand ends in $\psi_2$. This explains why $\text{SF}_6$ and $\text{PCl}_5$ exist, but $\text{SH}_6$ and $\text{PH}_5$ are nonexistent."""
            },
            {
                "id": "sec4_3",
                "title": "§4.3 Resonance Theory, Canonical Structures & Fractional Bond Orders",
                "content": r"""### The Inadequacy of a Single Lewis Formula

In many polyatomic molecules and ions, experimental spectroscopic measurements (such as X-ray crystallography, microwave rotational spectroscopy, and Raman spectroscopy) reveal that multiple adjacent bonds possess completely identical equilibrium bond lengths and vibrational force constants, contradicting the prediction of any single classical Lewis structure featuring distinct single and double bonds.

The archetypal inorganic example is the nitrate anion, $\text{NO}_3^-$. A single Lewis structure predicts one nitrogen-oxygen double bond ($\text{N}=\text{O}$) and two nitrogen-oxygen single bonds ($\text{N}-\text{O}$):
$$\text{Single bond length } d(\text{N}-\text{O}) \approx 140\text{ pm}, \quad \text{Double bond length } d(\text{N}=\text{O}) \approx 120\text{ pm}$$
However, experimental crystallography reveals that all three $\text{N}-\text{O}$ bonds are **strictly indistinguishable and identical in every respect**:
$$d(\text{N}-\text{O}) = 124.6\text{ pm}, \quad \angle(\text{O}-\text{N}-\text{O}) = 120.0^\circ \quad (D_{3h} \text{ point group symmetry})$$

---

### Quantum Mechanical Formulation of Resonance

Linus Pauling formulated **Resonance Theory** within the Valence Bond (VB) framework to reconcile experimental molecular equivalence with localized Lewis representations.

According to quantum mechanics, if a molecular system can be represented by $K$ distinct, valid Lewis structures (termed **canonical contributing structures**) with corresponding wavefunctions $\psi_1, \psi_2, \dots, \psi_K$, the true physical ground-state wavefunction $\Psi_{\text{true}}$ is a stationary linear superposition:
$$\Psi_{\text{true}} = \sum_{k=1}^K c_k \psi_k$$
where $c_k$ are variational weighting coefficients determined by minimizing the expectation value of the electronic Hamiltonian:
$$E = \frac{\langle \Psi_{\text{true}} | \hat{H} | \Psi_{\text{true}} \rangle}{\langle \Psi_{\text{true}} | \Psi_{\text{true}} \rangle}$$

```
                         [:O:]-                       [:O:]-                      [:O:]
                            |                            |                           ||
                            N+                           N+                          N+
                         /     \\                     //     \                    /     \
                     [:O:]-    [:O:]              [:O:]     [:O:]-            [:O:]-    [:O:]-
                       (Structure I)               (Structure II)              (Structure III)
```

#### Resonance Energy ($\Delta E_{\text{res}}$):
The variational principle proves that the true ground-state energy $E_{\text{true}}$ of the resonance hybrid is strictly lower than the calculated energy of any individual hypothetical canonical structure $\psi_k$:
$$E_{\text{true}} < \min_k \langle \psi_k | \hat{H} | \psi_k \rangle$$
The energy difference is the **Resonance Stabilization Energy**:
$$\Delta E_{\text{res}} = E_{\text{lowest canonical}} - E_{\text{true}} > 0$$

---

### Calculation of Fractional Bond Orders and Partial Charges

In a resonance hybrid formed from $K$ canonical structures with weights $w_k = |c_k|^2 / \sum |c_j|^2$:

#### 1. Fractional Bond Order ($BO$):
The bond order between atoms $A$ and $B$ is the weighted average of the formal bond orders $b_{k}(AB)$ across all canonical structures:
$$BO(AB) = \sum_{k=1}^K w_k b_k(AB)$$

For the nitrate anion ($\text{NO}_3^-$), symmetry dictates equal weights $w_1 = w_2 = w_3 = \frac{1}{3}$. Across the three structures, each $\text{N}-\text{O}$ linkage contains one double bond ($b=2$) and two single bonds ($b=1$):
$$BO(\text{N}-\text{O}) = \frac{2 + 1 + 1}{3} = \frac{4}{3} \approx 1.333$$
This $1.333$ fractional bond order perfectly explains why the experimental bond length ($124.6\text{ pm}$) lies between an idealized single bond ($140\text{ pm}$) and an idealized double bond ($120\text{ pm}$).

#### 2. Partial Atomic Charge ($\delta_i$):
The net fractional charge residing on atom $i$ in the hybrid is:
$$\delta_i = \sum_{k=1}^K w_k FC_{k,i}$$

For $\text{NO}_3^-$:
- Central Nitrogen: $FC = +1$ in all three structures:
  $$\delta_{\text{N}} = \frac{1}{3}(+1) + \frac{1}{3}(+1) + \frac{1}{3}(+1) = +1.00$$
- Each Oxygen: $FC = -1$ in two structures and $0$ in one structure:
  $$\delta_{\text{O}} = \frac{1}{3}(-1) + \frac{1}{3}(-1) + \frac{1}{3}(0) = -\frac{2}{3} \approx -0.67$$
- Check charge conservation: $\sum \delta_i = (+1) + 3\left(-\frac{2}{3}\right) = +1 - 2 = -1.00 = q_{\text{net}}$."""
            },
            {
                "id": "sec4_4",
                "title": "§4.4 Bond Enthalpies, Bond Lengths & Thermochemical Bond Dissociation Cycles",
                "content": r"""### Homolytic Cleavage and Bond Dissociation Enthalpy

The fundamental metric characterizing the strength of a covalent bond between atoms $A$ and $B$ is the **Bond Dissociation Enthalpy** ($D(A-B)$ or $\text{BDE}$). It is defined as the standard enthalpy change accompanying the homolytic cleavage of the specific bond in a gas-phase molecule at $298.15\text{ K}$, yielding neutral radical fragments:
$$A-B(g) \longrightarrow A^\bullet(g) + B^\bullet(g), \quad \Delta H_{298}^\circ = D(A-B) > 0$$

```
   Potential Energy Curve (Morse Potential):
   
   V(r)
    ^
    |             /----------------------------  V = 0 (Dissociated Atoms)
    |            /
    |           / |  <-- D_0 (Spectroscopic Dissociation Energy)
    |          /  |  <-- D_e (Well Depth from minimum)
    |         /   |
    |  \     /
    |   \___/  <-- Equilibrium separation r_0
    |
    0------------------------------------------> r
```

#### Morse Potential Formulation:
The potential energy curve of a diatomic covalent bond is accurately described by the Morse potential:
$$V(r) = D_e \left[ 1 - e^{-a(r - r_0)} \right]^2$$
where $D_e$ is the classical well depth from the potential minimum, $r_0$ is the equilibrium internuclear bond length, and $a = \sqrt{\frac{k_e}{2 D_e}}$ is the curvature parameter related to the harmonic vibrational force constant $k_e$.

The thermodynamic dissociation enthalpy differs from the spectroscopic well depth $D_e$ by the **Zero-Point Vibrational Energy (ZPVE)**:
$$D_0 = D_e - \frac{1}{2} h\nu_0$$
$$D(A-B) = D_0 + \Delta H_{\text{thermal}}(298\text{ K})$$

---

### Stepwise vs Mean Bond Enthalpies in Polyatomic Molecules

In polyatomic molecules, successive cleavage of identical chemical bonds does not require identical quantities of energy because the electronic and geometric environment of the remaining radical fragment reorganizes upon each bond rupture.

Consider the stepwise homolytic dissociation of water ($\text{H}_2\text{O}$):
1. $\text{H}-\text{OH}(g) \longrightarrow \text{H}^\bullet(g) + ^\bullet\text{OH}(g), \quad D_1(\text{O}-\text{H}) = +498.7\text{ kJ}\cdot\text{mol}^{-1}$
2. $^\bullet\text{OH}(g) \longrightarrow \text{H}^\bullet(g) + \text{O}(g), \quad D_2(\text{O}-\text{H}) = +428.0\text{ kJ}\cdot\text{mol}^{-1}$

The second dissociation energy is significantly lower ($428.0$ vs $498.7\text{ kJ}\cdot\text{mol}^{-1}$) because the hydroxyl radical $^\bullet\text{OH}$ experiences orbital relaxation and altered electronic screening.

The **Mean (Average) Bond Enthalpy** ($\bar{D}(\text{O}-\text{H})$) is the arithmetic mean across total atomization:
$$\bar{D}(\text{O}-\text{H}) = \frac{D_1 + D_2}{2} = \frac{498.7 + 428.0}{2} = +463.4\text{ kJ}\cdot\text{mol}^{-1}$$

---

### Enthalpy of Reaction from Mean Bond Enthalpies

Using Hess's law, any gas-phase chemical reaction can be modeled as breaking all reactant bonds into isolated gas-phase atoms, followed by reassembling those atoms into product bonds:
$$\Delta H_{\text{rxn}}^\circ \approx \sum D_{\text{bonds broken (reactants)}} - \sum D_{\text{bonds formed (products)}}$$

#### Fundamental Inverse Relationship Between Bond Length and Bond Strength:
For bonds between identical pairs of elements:
$$\text{Bond Order } \uparrow \implies \text{Bond Length } d \downarrow \implies \text{Bond Enthalpy } D \uparrow \implies \text{Force Constant } k \uparrow$$

| Bond | Bond Order | Equilibrium Length ($d$, pm) | Mean Dissociation Enthalpy ($D$, $\text{kJ}\cdot\text{mol}^{-1}$) | Stretching Frequency ($\tilde{\nu}$, $\text{cm}^{-1}$) |
| :--- | :--- | :--- | :--- | :--- |
| $\text{C}-\text{C}$ | $1$ | $154$ | $347$ | $\sim 900\text{–}1050$ |
| $\text{C}=\text{C}$ | $2$ | $134$ | $614$ | $\sim 1650$ |
| $\text{C}\equiv\text{C}$ | $3$ | $120$ | $839$ | $\sim 2150$ |
| $\text{N}-\text{N}$ | $1$ | $145$ | $160$ | $\sim 900$ |
| $\text{N}=\text{N}$ | $2$ | $125$ | $418$ | $\sim 1550$ |
| $\text{N}\equiv\text{N}$ | $3$ | $109.8$ | $945$ | $2330$ |
| $\text{C}-\text{O}$ | $1$ | $143$ | $358$ | $\sim 1050$ |
| $\text{C}=\text{O}$ (ketone) | $2$ | $122$ | $745$ | $\sim 1715$ |
| $\text{C}\equiv\text{O}$ ($CO$) | $3$ | $112.8$ | $1072$ | $2143$ |"""
            },
            {
                "id": "sec4_5",
                "title": "§4.5 Dipole Moments, Percent Ionic Character & Pauling Electronegativity Difference",
                "content": r"""### Electric Dipole Moments in Heteronuclear Bonds

In any chemical bond between two atoms of unequal electronegativity ($\chi_A \neq \chi_B$), the bonding electron cloud is polarized toward the more electronegative partner, inducing partial opposite charges $+\delta$ and $-\delta$ separated by equilibrium internuclear distance $\vec{r}$.

The classical **Bond Dipole Moment** ($\vec{\mu}$) is defined as:
$$\vec{\mu} = q \cdot \vec{r}$$
where $q = \delta \cdot e$ is the separated charge.
- In SI units, dipole moment is measured in Coulomb-meters ($\text{C}\cdot\text{m}$).
- In molecular physics and chemistry, the standard non-SI unit is the **Debye (D)**:
  $$1\text{ D} = 3.33564 \times 10^{-30}\text{ C}\cdot\text{m}$$

#### Dipole Moment of an Ideal Complete Charge Transfer Pair:
If a hypothetical diatomic molecule with bond length $r_0 = 100\text{ pm} = 1.0\text{ \AA}$ transferred a full elementary electronic charge ($q = e = 1.60218 \times 10^{-19}\text{ C}$), its purely ionic dipole moment would be:
$$\mu_{\text{ionic}} = e \cdot r_0 = (1.60218 \times 10^{-19}\text{ C}) \times (1.0 \times 10^{-10}\text{ m}) = 1.60218 \times 10^{-29}\text{ C}\cdot\text{m}$$
$$\mu_{\text{ionic}} = \frac{1.60218 \times 10^{-29}\text{ C}\cdot\text{m}}{3.33564 \times 10^{-30}\text{ C}\cdot\text{m/D}} \approx 4.803\text{ D}$$
Thus, for any bond length $r_0$ (in Ångströms, $\text{\AA}$):
$$\mu_{\text{ionic}}(\text{D}) \approx 4.803 \times r_0(\text{\AA})$$

---

### Percent Ionic Character

Pauling defined the **Percent Ionic Character** of a heteronuclear bond as the ratio of the experimentally observed dipole moment ($\mu_{\text{exp}}$) to the hypothetical theoretical dipole moment calculated assuming complete unit charge transfer ($\mu_{\text{ionic}} = e \cdot r_0$):
$$\% \text{ Ionic Character} = \frac{\mu_{\text{exp}}}{\mu_{\text{ionic}}} \times 100\% = \frac{\mu_{\text{exp}}}{e \cdot r_0} \times 100\%$$

#### Pauling's Empirical Correlation with Electronegativity Difference:
By correlating experimental dipole moments with electronegativity differences $\Delta\chi = |\chi_A - \chi_B|$, Linus Pauling proposed the empirical equation:
$$\% \text{ Ionic Character} = \left[ 1 - \exp\left( -\frac{(\Delta\chi)^2}{4} \right) \right] \times 100\%$$

#### The Hannay-Smith Modification:
N. B. Hannay and C. P. Smyth refined Pauling's relation into a computationally direct polynomial widely used in inorganic chemistry:
$$\% \text{ Ionic Character} = \left[ 16 |\Delta\chi| + 3.5 |\Delta\chi|^2 \right] \%$$

#### The 50% Ionic-Covalent Boundary Criterion:
Setting Pauling's equation to $50\%$ ionic character:
$$1 - \exp\left(-\frac{(\Delta\chi)^2}{4}\right) = 0.5 \implies \exp\left(-\frac{(\Delta\chi)^2}{4}\right) = 0.5$$
$$-\frac{(\Delta\chi)^2}{4} = \ln(0.5) = -0.69315 \implies (\Delta\chi)^2 = 2.7726 \implies \Delta\chi \approx 1.665 \approx 1.7$$
- When $\Delta\chi > 1.7$: The bond is predominantly **ionic** ($> 50\%$ ionic character).
- When $\Delta\chi < 1.7$: The bond is predominantly **covalent** ($< 50\%$ ionic character).

---

### Vector Addition of Dipole Moments & Molecular Geometry

The overall molecular dipole moment $\vec{\mu}_{\text{mol}}$ of a polyatomic molecule is the rigorous three-dimensional vector sum of all individual bond dipole moments plus the contributions from unshared electron lone pairs ($\vec{\mu}_{\text{lp}}$):
$$\vec{\mu}_{\text{mol}} = \sum_{k=1}^{n_{\text{bonds}}} \vec{\mu}_k + \sum_{m=1}^{n_{\text{lp}}} \vec{\mu}_{\text{lp}, m}$$

```
     Carbon Dioxide (CO2)                      Water (H2O)
     O <====== C ======> O                          O
                                                  // \\
     <-- μ1 --   -- μ2 -->                       //   \\  (Bond dipoles + Lone pairs)
                                                H       H
        μ_net = μ1 - μ2 = 0                       μ_net = 1.85 D (Net upward vector)
```

- **Symmetric Cancellation**: Highly symmetrical molecules possessing a center of inversion ($i$) or improper rotation axes ($S_n$) have zero net dipole moment ($\vec{\mu}_{\text{net}} = \vec{0}$) despite possessing highly polar individual bonds:
  - Linear $\text{CO}_2$ ($D_{\infty h}$): $\vec{\mu}_1 + \vec{\mu}_2 = \vec{0}$.
  - Trigonal planar $\text{BF}_3$ ($D_{3h}$): $\sum_{i=1}^3 \vec{\mu}_i = \vec{0}$.
  - Tetrahedral $\text{CCl}_4$ ($T_d$): $\sum_{i=1}^4 \vec{\mu}_i = \vec{0}$.
  - Octahedral $\text{SF}_6$ ($O_h$): $\sum_{i=1}^6 \vec{\mu}_i = \vec{0}$.
- **Vector Reinforcement**: In asymmetric geometries, bond dipoles reinforce:
  - Bent $\text{H}_2\text{O}$ ($C_{2v}$, bond angle $104.5^\circ$): $\mu_{\text{net}} = 2 \mu(\text{O}-\text{H}) \cos(52.25^\circ) + \mu_{\text{lone pairs}} = 1.85\text{ D}$.
  - Trigonal pyramidal $\text{NH}_3$ ($C_{3v}$, bond angle $107.8^\circ$): $\mu_{\text{net}} = 1.47\text{ D}$."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 4.1: Lewis Structures, Formal Charges & Resonance for Thiocyanate and Cyanate Isomers",
                "statement": r"""For the cyanate anion $[\text{OCN}]^-$ and its isomer fulminate $[\text{CNO}]^-$:
1. Determine the total valence electron count ($V$) for both isomers.
2. Draw all three major canonical resonance structures for $[\text{OCN}]^-$, calculate the formal charge on every atom for each structure, and determine the most significant contributing structure.
3. Draw the corresponding three canonical resonance structures for $[\text{CNO}]^-$, evaluate all formal charges, and explain on thermodynamic and electrostatic grounds why cyanate $[\text{OCN}]^-$ is an exceptionally stable, non-toxic commercial salt whereas fulminate $[\text{CNO}]^-$ is dangerously explosive and sensitive to shock.""",
                "solution": r"""### Part 1: Total Valence Electron Count
Both $[\text{OCN}]^-$ and $[\text{CNO}]^-$ are triatomic pseudo-halide anions with net charge $q = -1$:
- Oxygen (Group 16): $6$ valence electrons
- Carbon (Group 14): $4$ valence electrons
- Nitrogen (Group 15): $5$ valence electrons
- Net ionic charge: $+1$ electron
$$V = 6 + 4 + 5 + 1 = 16\text{ valence electrons (8 pairs)}$$

---

### Part 2: Resonance Analysis of the Cyanate Anion $[\text{O}-\text{C}-\text{N}]^-$
In $[\text{OCN}]^-$, carbon is the central atom (lowest electronegativity: $\chi_{\text{C}} = 2.55, \chi_{\text{N}} = 3.04, \chi_{\text{O}} = 3.44$).
We construct three canonical structures:

#### Structure A: Single $\text{O}-\text{C}$ and Triple $\text{C}\equiv\text{N}$
$$[:\ddot{\text{O}}-\text{C}\equiv\text{N}:]^-$$
- Oxygen: $FC(\text{O}) = 6 - 6 - \frac{1}{2}(2) = -1$
- Carbon: $FC(\text{C}) = 4 - 0 - \frac{1}{2}(8) = 0$
- Nitrogen: $FC(\text{N}) = 5 - 2 - \frac{1}{2}(6) = 0$
- Formal charge distribution: $\mathbf{\text{O}(-1), \text{C}(0), \text{N}(0)}$. Total charge: $-1$.

#### Structure B: Double $\text{O}=\text{C}$ and Double $\text{C}=\text{N}$
$$[\ddot{\text{O}}=\text{C}=\ddot{\text{N}}]^-$$
- Oxygen: $FC(\text{O}) = 6 - 4 - \frac{1}{2}(4) = 0$
- Carbon: $FC(\text{C}) = 4 - 0 - \frac{1}{2}(8) = 0$
- Nitrogen: $FC(\text{N}) = 5 - 4 - \frac{1}{2}(4) = -1$
- Formal charge distribution: $\mathbf{\text{O}(0), \text{C}(0), \text{N}(-1)}$. Total charge: $-1$.

#### Structure C: Triple $\text{O}\equiv\text{C}$ and Single $\text{C}-\ddot{\text{N}}:$
$$[:\text{O}\equiv\text{C}-\ddot{\text{N}}:]^-$$
- Oxygen: $FC(\text{O}) = 6 - 2 - \frac{1}{2}(6) = +1$
- Carbon: $FC(\text{C}) = 4 - 0 - \frac{1}{2}(8) = 0$
- Nitrogen: $FC(\text{N}) = 5 - 6 - \frac{1}{2}(2) = -2$
- Formal charge distribution: $\mathbf{\text{O}(+1), \text{C}(0), \text{N}(-2)}$. Total charge: $-1$.

#### Evaluation of Cyanate Canonical Weights:
- **Structure A** places the $-1$ charge on oxygen, the most electronegative element ($\chi = 3.44$). This is the **major contributor** ($\sim 65\%$).
- **Structure B** places the $-1$ charge on nitrogen, also electronegative ($\chi = 3.04$). This is an important **secondary contributor** ($\sim 33\%$).
- **Structure C** places a positive $+1$ charge on highly electronegative oxygen and $-2$ on nitrogen. Its contribution is **negligible** ($< 2\%$).

---

### Part 3: Resonance Analysis of the Fulminate Anion $[\text{C}-\text{N}-\text{O}]^-$
In the fulminate isomer, nitrogen occupies the central position:

#### Structure A': Single $\text{C}-\text{N}$ and Triple $\text{N}\equiv\text{O}$
$$[:\ddot{\text{C}}-\text{N}\equiv\text{O}:]^-$$
- Carbon: $FC(\text{C}) = 4 - 6 - \frac{1}{2}(2) = -3$
- Nitrogen: $FC(\text{N}) = 5 - 0 - \frac{1}{2}(8) = +1$
- Oxygen: $FC(\text{O}) = 6 - 2 - \frac{1}{2}(6) = +1$
- Charges: $\mathbf{\text{C}(-3), \text{N}(+1), \text{O}(+1)}$. Enormously destabilized!

#### Structure B': Double $\text{C}=\text{N}$ and Double $\text{N}=\text{O}$
$$[\ddot{\text{C}}=\text{N}=\ddot{\text{O}}]^-$$
- Carbon: $FC(\text{C}) = 4 - 4 - \frac{1}{2}(4) = -2$
- Nitrogen: $FC(\text{N}) = 5 - 0 - \frac{1}{2}(8) = +1$
- Oxygen: $FC(\text{O}) = 6 - 4 - \frac{1}{2}(4) = 0$
- Charges: $\mathbf{\text{C}(-2), \text{N}(+1), \text{O}(0)}$.

#### Structure C': Triple $\text{C}\equiv\text{N}$ and Single $\text{N}-\text{O}$
$$[:\text{C}\equiv\text{N}-\ddot{\text{O}}:]^-$$
- Carbon: $FC(\text{C}) = 4 - 2 - \frac{1}{2}(6) = -1$
- Nitrogen: $FC(\text{N}) = 5 - 0 - \frac{1}{2}(8) = +1$
- Oxygen: $FC(\text{O}) = 6 - 6 - \frac{1}{2}(2) = -1$
- Charges: $\mathbf{\text{C}(-1), \text{N}(+1), \text{O}(-1)}$.

---

### Part 4: Comparative Stability & Explosive Origin
1. **Electrostatic Grounding of Instability**:
   In every canonical structure of fulminate, nitrogen carries a formal charge of $+1$, while the least electronegative element (carbon, $\chi = 2.55$) is forced to bear formal charges of $-1, -2,$ or even $-3$. Placing intense negative formal charge on carbon while electronegative oxygen is neutral or positive represents a severe violation of electronegativity matching.
2. **Exothermic Isomerization Driving Force**:
   The electrostatic strain and high potential energy make mercury fulminate $\text{Hg}(\text{CNO})_2$ an infamous primary high explosive sensitive to friction and shock. It decomposes catastrophically into stable elements and gases:
   $$\text{Hg}(\text{CNO})_2(s) \longrightarrow \text{Hg}(g) + 2\,\text{CO}(g) + \text{N}_2(g), \quad \Delta H_{\text{explosion}}^\circ \ll 0$$
   Cyanate, in contrast, places zero or negative charge on the most electronegative atoms ($\text{O}$ and $\text{N}$), making it a stable, unreactive species."""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 4.2: Pimentel-Rundle 3c-4e Molecular Orbital Analysis of Xenon Difluoride",
                "statement": r"""Xenon difluoride ($\text{XeF}_2$) is a linear, hypercoordinate noble gas fluoride containing $22$ valence electrons.
1. Formulate the classical Lewis structure and demonstrate why a naive octet expansion would require placing $10$ electrons around xenon.
2. Construct the rigorous Pimentel-Rundle three-center four-electron (3c-4e) molecular orbital model for the linear $\text{F}-\text{Xe}-\text{F}$ axis:
   - Identify the symmetry-adapted linear combinations (SALCs) of the two ligand fluorine $2p_z$ orbitals under the $D_{\infty h}$ point group.
   - Formulate the linear combination with the central xenon $5p_z$ orbital.
   - Sketch the resulting MO energy level diagram, populate the orbitals with electrons, and determine the formal bond order of each $\text{Xe}-\text{F}$ linkage.
3. Calculate the net Mulliken partial atomic charges on xenon and fluorine, and explain why $\text{XeF}_2$ is thermodynamically stable despite possessing a formal bond order of only $0.5$ per bond.""",
                "solution": r"""### Part 1: Classical Lewis Structure and Octet Violation
Valence electron inventory:
- Xenon (Group 18): $8$ valence electrons
- Two Fluorines (Group 17): $2 \times 7 = 14$ valence electrons
$$V = 8 + 14 = 22\text{ valence electrons (11 pairs)}$$

Linear connectivity $[\text{F}-\text{Xe}-\text{F}]$:
- Form two $\text{Xe}-\text{F}$ single bonds: consumes $4$ electrons.
- Satisfy octets of terminal fluorines: $3$ lone pairs per fluorine = consumes $12$ electrons.
- Remaining electrons: $22 - (4 + 12) = 6$ electrons ($3$ lone pairs).
- The $3$ remaining lone pairs are placed on the central xenon atom.
Around xenon: $2$ bonding pairs $+ 3$ lone pairs = $5$ electron domains ($10$ valence electrons). In the classical depiction, this was rationalized by assuming $sp^3d$ hybridization with empty $5d$ orbitals.

---

### Part 2: Rigorous 3c-4e Molecular Orbital Model
Orient the linear molecule along the $z$-axis: $\text{F}_1 - \text{Xe} - \text{F}_2$.
The three equatorial lone pairs on xenon occupy non-bonding hybrid orbitals formed from $5s, 5p_x, 5p_y$. The axial bonding involves purely the collinear $p_z$ atomic orbitals:
- Central Xenon: $\phi_{\text{Xe}} = 5p_z$ (antisymmetric with respect to inversion center, $u$ symmetry in $D_{\infty h}$).
- Terminal Fluorines: $\phi_1 = 2p_{z,1}$ and $\phi_2 = 2p_{z,2}$ (oriented pointing toward central Xe).

#### 1. Symmetry-Adapted Linear Combinations (SALCs) of Fluorine Orbitals:
Under the inversion center $i$ of the $D_{\infty h}$ point group:
- Gerade SALC (symmetric):
  $$\Phi_g = \frac{1}{\sqrt{2}} (\phi_1 - \phi_2), \quad \hat{i}\Phi_g = +\Phi_g$$
- Ungerade SALC (antisymmetric):
  $$\Phi_u = \frac{1}{\sqrt{2}} (\phi_1 + \phi_2), \quad \hat{i}\Phi_u = -\Phi_u$$

#### 2. MO Interaction with Central Xenon $5p_z$ Orbital:
The central xenon $5p_z$ orbital is ungerade ($\sigma_u^+$).
- **Overlaps**:
  - $\langle \phi_{\text{Xe}}(5p_z) | \Phi_g \rangle = 0$ (orthogonal by parity: ungerade $\times$ gerade integrates to zero).
  - $\langle \phi_{\text{Xe}}(5p_z) | \Phi_u \rangle = S \neq 0$ (allowed by parity).

#### 3. Molecular Orbital Wavefunctions:
1. **Bonding MO ($\psi_1$, $\sigma_u^+$)**:
   $$\psi_1 = c_1 \phi_{\text{Xe}}(5p_z) + c_2 \frac{1}{\sqrt{2}}(\phi_1 + \phi_2)$$
   Energy: Strongly stabilized below the unperturbed atomic orbital levels.
2. **Non-Bonding MO ($\psi_2$, $\sigma_g^+$)**:
   $$\psi_2 = \Phi_g = \frac{1}{\sqrt{2}}(\phi_1 - \phi_2)$$
   Energy: Strictly non-bonding; contains zero xenon orbital coefficient. The electron density resides $100\%$ on the terminal fluorine ligands.
3. **Antibonding MO ($\psi_3^*$, $\sigma_u^{+*}$)**:
   $$\psi_3^* = c_2 \phi_{\text{Xe}}(5p_z) - c_1 \frac{1}{\sqrt{2}}(\phi_1 + \phi_2)$$
   Energy: Strongly destabilized above atomic levels; remains unoccupied.

---

### Part 3: Electron Population, Bond Order & Charge Distribution
The axial 3c-4e framework contains 4 electrons (1 from each F, 2 from Xe):
- $2$ electrons occupy bonding $\psi_1$.
- $2$ electrons occupy non-bonding $\psi_2$.
- Antibonding $\psi_3^*$ is empty.

#### Formal Bond Order:
$$\text{Total Bonding Electron Pairs} = 1$$
$$\text{Number of } \text{Xe}-\text{F} \text{ Linkages} = 2$$
$$\text{Bond Order per } \text{Xe}-\text{F} \text{ Bond} = \frac{1}{2} = 0.5$$

#### Charge Distribution:
Because the non-bonding orbital $\psi_2$ is localized solely on the terminal fluorines, and the bonding orbital $\psi_1$ is polarized toward electronegative fluorine ($\chi_{\text{F}} = 3.98 \gg \chi_{\text{Xe}} = 2.60$), substantial electron density is transferred from xenon to the fluorines:
$$\delta_{\text{F}} \approx -0.5\text{ to } -0.6e, \quad \delta_{\text{Xe}} \approx +1.0\text{ to } +1.2e$$

#### Thermodynamic Stability:
$\text{XeF}_2$ is stable ($\Delta H_f^\circ = -109\text{ kJ}\cdot\text{mol}^{-1}$) because:
1. The immense electronegativity of fluorine pulls electron density into the low-energy non-bonding MO $\psi_2$.
2. The partial charge separation creates strong **Coulombic attractive stabilization** ($\text{F}^{\delta-}-\text{Xe}^{2\delta+}-\text{F}^{\delta-}$), which reinforces the covalent half-bond without needing fictitious high-energy $5d$ hybridization."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 4.3: Analytical Dipole Moment Modeling & Partial Ionic Character of Hydrogen Halides",
                "statement": r"""Given the following experimental physical constants for gaseous hydrogen halides at $298\text{ K}$:
- Hydrogen fluoride ($\text{HF}$): $r_0 = 91.7\text{ pm} = 0.917\text{ \AA}$, $\mu_{\text{exp}} = 1.826\text{ D}$
- Hydrogen chloride ($\text{HCl}$): $r_0 = 127.4\text{ pm} = 1.274\text{ \AA}$, $\mu_{\text{exp}} = 1.080\text{ D}$
- Hydrogen bromide ($\text{HBr}$): $r_0 = 141.4\text{ pm} = 1.414\text{ \AA}$, $\mu_{\text{exp}} = 0.827\text{ D}$
- Hydrogen iodide ($\text{HI}$): $r_0 = 160.9\text{ pm} = 1.609\text{ \AA}$, $\mu_{\text{exp}} = 0.448\text{ D}$

1. Compute the theoretical purely ionic dipole moment $\mu_{\text{ionic}} = e \cdot r_0$ (in Debye) for all four hydrogen halides.
2. Calculate the experimental percent ionic character for each molecule.
3. Using Pauling's electronegativity values ($\chi_{\text{H}} = 2.20$, $\chi_{\text{F}} = 3.98$, $\chi_{\text{Cl}} = 3.16$, $\chi_{\text{Br}} = 2.96$, $\chi_{\text{I}} = 2.66$), calculate the predicted percent ionic character using:
   - Pauling's exponential formula: $\% IC = [1 - \exp(-(\Delta\chi)^2 / 4)] \times 100\%$
   - Hannay-Smith polynomial formula: $\% IC = [16|\Delta\chi| + 3.5(\Delta\chi)^2]\%$
4. Perform a rigorous comparative error analysis and explain why the experimental percent ionic character of $\text{HF}$ is noticeably lower than predicted by simple rigid-ion electrostatic models, citing the opposing contribution of the halogen lone-pair atomic dipole.""",
                "solution": r"""### Step 1: Theoretical Purely Ionic Dipole Moments
Recall that $1\text{ D} = 3.33564 \times 10^{-30}\text{ C}\cdot\text{m}$, and $e = 1.60218 \times 10^{-19}\text{ C}$.
For any bond length $r_0$ in picometers:
$$\mu_{\text{ionic}} = \frac{(1.60218 \times 10^{-19}\text{ C}) \times (r_0 \times 10^{-12}\text{ m})}{3.33564 \times 10^{-30}\text{ C}\cdot\text{m/D}} = 0.048032 \times r_0(\text{pm})\text{ D}$$

1. **HF**:
   $$\mu_{\text{ionic}} = 0.048032 \times 91.7 = 4.405\text{ D}$$
2. **HCl**:
   $$\mu_{\text{ionic}} = 0.048032 \times 127.4 = 6.119\text{ D}$$
3. **HBr**:
   $$\mu_{\text{ionic}} = 0.048032 \times 141.4 = 6.792\text{ D}$$
4. **HI**:
   $$\mu_{\text{ionic}} = 0.048032 \times 160.9 = 7.728\text{ D}$$

---

### Step 2: Experimental Percent Ionic Character
$$\% IC_{\text{exp}} = \frac{\mu_{\text{exp}}}{\mu_{\text{ionic}}} \times 100\%$$

1. **HF**:
   $$\% IC_{\text{exp}} = \frac{1.826}{4.405} \times 100\% = 41.45\%$$
2. **HCl**:
   $$\% IC_{\text{exp}} = \frac{1.080}{6.119} \times 100\% = 17.65\%$$
3. **HBr**:
   $$\% IC_{\text{exp}} = \frac{0.827}{6.792} \times 100\% = 12.18\%$$
4. **HI**:
   $$\% IC_{\text{exp}} = \frac{0.448}{7.728} \times 100\% = 5.80\%$$

---

### Step 3: Theoretical Predictions via Pauling and Hannay-Smith Formulas

#### Electronegativity Differences ($\Delta\chi = \chi_X - \chi_H$):
- $\text{HF}$: $\Delta\chi = 3.98 - 2.20 = 1.78$
- $\text{HCl}$: $\Delta\chi = 3.16 - 2.20 = 0.96$
- $\text{HBr}$: $\Delta\chi = 2.96 - 2.20 = 0.76$
- $\text{HI}$: $\Delta\chi = 2.66 - 2.20 = 0.46$

#### 1. Pauling Exponential Formula: $\% IC = [1 - \exp(-(\Delta\chi)^2 / 4)] \times 100\%$
- **HF**:
  $$\frac{(\Delta\chi)^2}{4} = \frac{1.78^2}{4} = \frac{3.1684}{4} = 0.7921$$
  $$\% IC = [1 - \exp(-0.7921)] \times 100\% = [1 - 0.4529] \times 100\% = 54.71\%$$
- **HCl**:
  $$\frac{0.96^2}{4} = 0.2304 \implies \% IC = [1 - \exp(-0.2304)] \times 100\% = 20.58\%$$
- **HBr**:
  $$\frac{0.76^2}{4} = 0.1444 \implies \% IC = [1 - \exp(-0.1444)] \times 100\% = 13.44\%$$
- **HI**:
  $$\frac{0.46^2}{4} = 0.0529 \implies \% IC = [1 - \exp(-0.0529)] \times 100\% = 5.15\%$$

#### 2. Hannay-Smith Formula: $\% IC = [16|\Delta\chi| + 3.5(\Delta\chi)^2]\%$
- **HF**: $\% IC = 16(1.78) + 3.5(1.78)^2 = 28.48 + 11.09 = 39.57\%$
- **HCl**: $\% IC = 16(0.96) + 3.5(0.96)^2 = 15.36 + 3.23 = 18.59\%$
- **HBr**: $\% IC = 16(0.76) + 3.5(0.76)^2 = 12.16 + 2.02 = 14.18\%$
- **HI**: $\% IC = 16(0.46) + 3.5(0.46)^2 = 7.36 + 0.74 = 8.10\%$

---

### Step 4: Summary Table & Physical Explanation of Discrepancy

| Molecule | $\Delta\chi$ | $r_0$ (pm) | $\mu_{\text{exp}}$ (D) | $\mu_{\text{ionic}}$ (D) | $\% IC_{\text{exp}}$ | $\% IC_{\text{Pauling}}$ | $\% IC_{\text{Hannay-Smith}}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **HF** | $1.78$ | $91.7$ | $1.826$ | $4.405$ | **$41.45\%$** | $54.71\%$ | $39.57\%$ |
| **HCl** | $0.96$ | $127.4$ | $1.080$ | $6.119$ | **$17.65\%$** | $20.58\%$ | $18.59\%$ |
| **HBr** | $0.76$ | $141.4$ | $0.827$ | $6.792$ | **$12.18\%$** | $13.44\%$ | $14.18\%$ |
| **HI** | $0.46$ | $160.9$ | $0.448$ | $7.728$ | **$5.80\%$** | $5.15\%$ | $8.10\%$ |

#### Physical Quantum Mechanical Origin of the HF Discrepancy:
Pauling's model predicts $54.7\%$ ionic character for $\text{HF}$, yet the experimental dipole moment yields only $41.45\%$.
This discrepancy occurs because the measured dipole moment is a vector sum of two opposing quantum contributions:
$$\vec{\mu}_{\text{exp}} = \vec{\mu}_{\text{charge separation}} + \vec{\mu}_{\text{atomic lone pair}}$$
1. **Bond Polarity Vector ($\vec{\mu}_{\text{bond}}$)**: Directs from $\text{H}^{\delta+}$ toward $\text{F}^{\delta-}$.
2. **Halogen Lone Pair Polarization Vector ($\vec{\mu}_{\text{lp}}$)**: In $\text{HF}$, the non-bonding electron pairs on fluorine undergo $sp$ hybridization due to polarizing interaction with the proton. The centroid of the back-directed lone pairs shifts away from the nucleus in the direction opposite to the bond ($-\hat{z}$).
3. Because $\vec{\mu}_{\text{lp}}$ opposes $\vec{\mu}_{\text{bond}}$, the net experimental dipole moment $\mu_{\text{exp}}$ is depressed, artificially reducing the apparent $\% IC_{\text{exp}}$. Hannay-Smith's modified polynomial empirically compensates for this effect, yielding $39.57\%$, in close agreement with the experimental $41.45\%$."""
            }
        ]
    }
'''

with open("build_inorg1_unit4.py", "w", encoding="utf-8") as f:
    f.write(content)

print("build_inorg1_unit4.py written successfully.")
