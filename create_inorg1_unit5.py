#!/usr/bin/env python3
"""
create_inorg1_unit5.py
Generates build_inorg1_unit5.py for Unit 5:
Molecular Geometry: VSEPR Theory, Bent's Rule & Symmetry
"""

import sys

content = r'''# -*- coding: utf-8 -*-
"""
Unit 5: Molecular Geometry: VSEPR Theory, Bent's Rule & Symmetry
Contains 5 comprehensive sections and 3 tiered solved problems with full derivations.
"""

def get_unit5():
    return {
        "id": "unit5",
        "title": "Unit 5: Molecular Geometry: VSEPR Theory, Bent's Rule & Symmetry",
        "simId": "sim_chem_bent_rule_hybridization",
        "simTitle": "Bent's Rule & Hybridization Vector Engine",
        "sections": [
            {
                "id": "sec5_1",
                "title": "§5.1 Valence Shell Electron Pair Repulsion (VSEPR) Theory & Electron Domain Geometry",
                "content": r"""### Foundations of the Gillespie-Nyholm Model

Valence Shell Electron Pair Repulsion (VSEPR) theory, pioneered by Nevil Sidgwick and Herbert Powell (1940) and systematically formalized by Ronald Gillespie and Ronald Nyholm (1957), provides an exceptionally robust, intuitively predictive framework for determining the three-dimensional equilibrium geometries of main-group polyatomic molecules and ions.

#### Quantum Mechanical Origin of Electron Domain Repulsion
The physical premise of VSEPR theory rests on the Pauli Exclusion Principle rather than purely classical electrostatics. While Coulombic repulsion between negatively charged electron clouds operates everywhere, the Pauli exclusion principle mandates that electrons possessing identical spin quantum numbers ($m_s = \pm \frac{1}{2}$) cannot occupy the same spatial coordinates, establishing a **Pauli repulsion Fermi hole** around each localized electron pair:
$$\Psi(\mathbf{r}_1, \mathbf{r}_2) = -\Psi(\mathbf{r}_2, \mathbf{r}_1) \implies \Psi(\mathbf{r}, \mathbf{r}) = 0$$

To minimize both the Pauli quantum exchange energy and classical electrostatic repulsions, localized valence electron pairs distribute themselves across the spherical surface of the valence shell so as to maximize mutual angular separations.

---

### The Steric Number Metric & Fundamental Polyhedral Geometries

For a central atom $A$ in a molecule $AX_m E_n$:
- $X$ represents coordinating ligand atoms (bonding pairs, $m$).
- $E$ represents non-bonding valence electron pairs (lone pairs, $n$).
- Multiple bonds (double or triple bonds) contain multiple pairs of shared electrons constrained between the same two nuclei; therefore, they behave as a **single stereochemically active electron domain**.

The total count of stereochemically active electron domains is the **Steric Number** ($SN$):
$$SN = m + n = (\text{Number of bonded atoms}) + (\text{Number of lone pairs on central atom})$$

```
   Steric Polyhedra:
   
   SN = 2: Linear (180°)                 SN = 3: Trigonal Planar (120°)
       X --- A --- X                                 X
                                                     |
                                                     A
                                                   /   \
                                                  X     X
                                                  
   SN = 4: Tetrahedral (109.47°)         SN = 5: Trigonal Bipyramidal (90°, 120°)
               X                                     X_ax
               |                                     |
               A                                 X_eq-A-X_eq
             / | \                                  / \
            X  X  X                                X_eq X_ax
```

#### Master Table of Ideal Stereochemical Polyhedra:

| Steric Number ($SN$) | Ideal Electron Domain Polyhedron | Ideal Bond Angles ($\theta_0$) | Point Group Symmetry | Archetype Species |
| :--- | :--- | :--- | :--- | :--- |
| **$2$** | Linear | $180^\circ$ | $D_{\infty h}$ | $\text{BeCl}_2, \text{CO}_2, \text{HCN}$ |
| **$3$** | Trigonal Planar | $120^\circ$ | $D_{3h}$ | $\text{BF}_3, \text{SO}_3, \text{NO}_3^-$ |
| **$4$** | Regular Tetrahedral | $\arccos\left(-\frac{1}{3}\right) \approx 109.47^\circ$ | $T_d$ | $\text{CH}_4, \text{NH}_4^+, \text{SO}_4^{2-}$ |
| **$5$** | Trigonal Bipyramidal (TBP) | $90^\circ$ (ax-eq), $120^\circ$ (eq-eq), $180^\circ$ (ax-ax) | $D_{3h}$ | $\text{PCl}_5, \text{PF}_5, \text{AsF}_5$ |
| **$6$** | Regular Octahedral | $90^\circ, 180^\circ$ | $O_h$ | $\text{SF}_6, [\text{PF}_6]^-, [\text{SiF}_6]^{2-}$ |
| **$7$** | Pentagonal Bipyramidal | $72^\circ$ (eq-eq), $90^\circ$ (ax-eq) | $D_{5h}$ | $\text{IF}_7, [\text{UO}_2\text{F}_5]^{3-}$ |
| **$8$** | Square Antiprismatic | $74.8^\circ, 141.6^\circ$ | $D_{4d}$ | $[\text{TaF}_8]^{3-}, [\text{XeF}_8]^{2-}$ |"""
            },
            {
                "id": "sec5_2",
                "title": "§5.2 Molecular Shapes: Linear, Trigonal Planar, Tetrahedral, Trigonal Bipyramidal, Octahedral & Derived Geometries",
                "content": r"""### Distinguishing Electron Domain Geometry from Molecular Shape

An imperative operational distinction in structural chemistry is the difference between:
1. **Electron Domain Geometry**: The spatial arrangement of all stereochemically active electron pairs (both bonding pairs and lone pairs) around the central atom.
2. **Molecular Geometry (Shape)**: The physical arrangement of the atomic nuclei in space, as directly determined by diffraction experiments (X-ray, neutron, electron diffraction). While lone pairs govern the angular positions of nuclei, they are not atomic nuclei themselves; hence, molecular shape describes only nuclear coordinates.

---

### The Repulsion Hierarchy: Gillespie-Nyholm Axioms

The fundamental angular distortions observed in real molecules are governed by the **Gillespie-Nyholm Repulsion Hierarchy**:
$$\mathbf{[\text{Lone Pair} - \text{Lone Pair}] > [\text{Lone Pair} - \text{Bonding Pair}] > [\text{Bonding Pair} - \text{Bonding Pair}]}$$
$$\mathbf{(LP - LP) > (LP - BP) > (BP - BP)}$$

```
          Bonding Pair (BP)                     Lone Pair (LP)
             Nucleus A                             Nucleus A
                 *                                     *
                / \                                   / \
               /   \  <-- Shared between             /   \  <-- Anchored to ONLY ONE
              /  e  \     two nuclei                /  e  \     nucleus; expands
             /       \                             (   e   )    diffusely in space
                 *                                  \_____/
             Nucleus B
```

#### Physical Origin of the Hierarchy:
- A **Bonding Pair (BP)** is localized in the internuclear space between two positive atomic nuclei ($A$ and $B$). The dual Coulombic attraction pulls the electron density tightly along the internuclear vector, narrowing its angular boundary.
- A **Lone Pair (LP)** is anchored to only a single positive nucleus ($A$). Unconstrained by a second nucleus, its wavepacket spreads out diffusely, possessing a substantially larger spatial volume and higher electron density close to the central core. Consequently, lone pairs exert ferocious repulsive forces on adjacent domains.

---

### Complete Taxonomy of Derived Geometries

#### 1. Trigonal Planar Domain ($SN = 3$):
- $AX_3$ ($0$ LP): **Trigonal Planar** ($\text{BF}_3, \text{CO}_3^{2-}$), $\theta = 120^\circ$.
- $AX_2E$ ($1$ LP): **Bent (V-shaped)** ($\text{SO}_2, \text{NO}_2^-$), $\theta < 120^\circ$ (in $\text{SO}_2$, $\theta = 119.0^\circ$).

#### 2. Tetrahedral Domain ($SN = 4$):
- $AX_4$ ($0$ LP): **Regular Tetrahedral** ($\text{CH}_4$), $\theta = 109.5^\circ$.
- $AX_3E$ ($1$ LP): **Trigonal Pyramidal** ($\text{NH}_3$), $\theta = 107.8^\circ$. One LP compresses the three BP domains.
- $AX_2E_2$ ($2$ LP): **Bent** ($\text{H}_2\text{O}$), $\theta = 104.5^\circ$. Two LPs exert severe (LP-LP) and (LP-BP) compression, closing the angle by $5.0^\circ$.

#### 3. Trigonal Bipyramidal Domain ($SN = 5$): Non-Equivalent Sites
The trigonal bipyramid contains two stereochemically distinct sets of coordination sites:
- **Equatorial Sites (3)**: Coplanar, separated by broad $120^\circ$ equatorial angles.
- **Axial Sites (2)**: Collinear along the $z$-axis, separated from equatorial ligands by tight $90^\circ$ angles.

Because $90^\circ$ repulsions are severe while $120^\circ$ repulsions are negligible ($V_{\text{repulsion}} \propto \theta^{-n}$):
- An axial lone pair would have **three $90^\circ$ (LP-BP) repulsions**.
- An equatorial lone pair has **only two $90^\circ$ (LP-BP) repulsions** and two $120^\circ$ repulsions.
**Fundamental Rule for TBP**: *Lone pairs ALWAYS preferentially occupy Equatorial positions!*
- $AX_5$ ($0$ LP): **Trigonal Bipyramidal** ($\text{PCl}_5, \text{PF}_5$).
- $AX_4E$ ($1$ LP eq): **Seesaw (Disphenoidal)** ($\text{SF}_4$), $\theta_{\text{ax-eq}} = 173^\circ < 180^\circ$, $\theta_{\text{eq-eq}} = 102^\circ < 120^\circ$.
- $AX_3E_2$ ($2$ LP eq): **T-Shaped** ($\text{ClF}_3, \text{BrF}_3$), $\theta_{\text{ax-eq}} = 87.5^\circ < 90^\circ$.
- $AX_2E_3$ ($3$ LP eq): **Linear** ($\text{XeF}_2, \text{I}_3^-$), $\theta = 180^\circ$. The three equatorial lone pairs form a symmetric $120^\circ$ belt, cancelling all lateral repulsive vectors.

#### 4. Octahedral Domain ($SN = 6$):
All six vertices of a regular octahedron are symmetry-equivalent ($90^\circ$ separations).
- $AX_6$ ($0$ LP): **Regular Octahedral** ($\text{SF}_6$), $\theta = 90^\circ, 180^\circ$.
- $AX_5E$ ($1$ LP): **Square Pyramidal** ($\text{BrF}_5, \text{IF}_5$). Axial lone pair repels the four basal bonds upward: $\theta_{\text{ax-basal}} \approx 84.8^\circ < 90^\circ$.
- $AX_4E_2$ ($2$ LP): **Square Planar** ($\text{XeF}_4, [\text{ICl}_4]^-$). To minimize the immense (LP-LP) repulsion, the two lone pairs occupy **mutually trans ($180^\circ$) positions**, leaving four ligands in a strictly planar square ($D_{4h}$ symmetry, $\theta = 90^\circ$)."""
            },
            {
                "id": "sec5_3",
                "title": "§5.3 Angular Distortions, Lone Pair-Bond Pair Repulsion & Electronegativity Effects",
                "content": r"""### Quantitative Analysis of Bond Angle Perturbations

The Gillespie-Nyholm model successfully predicts bond angle shifts across isoelectronic series by incorporating two secondary electronic factors:
1. **Ligand Electronegativity Effect**: As the electronegativity of coordinating ligands increases, the shared electron pair is drawn further away from the central atom toward the ligands. Consequently, the bonding pair electron density occupies less volume near the central nucleus, reducing inter-bonding-pair repulsion and allowing adjacent lone pairs or bonds to compress the bond angle more severely.
2. **Central Atom Electronegativity / Size Effect**: As the central atom becomes larger and less electronegative down a periodic group, its valence orbitals become more diffuse and bond lengths increase, reducing steric crowding around the nucleus and allowing the bond angle to contract toward unhybridized $90^\circ$ $p$-orbital angles (Drago's Rule).

---

### Benchmark Comparative Systems

#### 1. The Water vs Oxygen Difluoride Anomaly ($\text{H}_2\text{O}$ vs $\text{OF}_2$):
Both $\text{H}_2\text{O}$ and $\text{OF}_2$ possess identical steric classifications ($AX_2E_2$):
- In $\text{H}_2\text{O}$: $\chi_{\text{O}} = 3.44 > \chi_{\text{H}} = 2.20$.
  The bonding pairs are strongly pulled inward toward the central oxygen atom. The concentrated bonding electron density near the oxygen nucleus repels the two lone pairs, resisting excessive angular compression:
  $$\angle(\text{H}-\text{O}-\text{H}) = 104.5^\circ$$
- In $\text{OF}_2$: $\chi_{\text{F}} = 3.98 > \chi_{\text{O}} = 3.44$.
  Fluorine is more electronegative than oxygen. The bonding electron pairs are pulled outward toward the fluorine ligands, away from the oxygen nucleus. The bonding pairs occupy diminutive volume near oxygen, allowing the two oxygen lone pairs to vigorously squeeze the $\text{F}-\text{O}-\text{F}$ angle down to:
  $$\angle(\text{F}-\text{O}-\text{F}) = 103.1^\circ$$

#### 2. The Ammonia vs Nitrogen Trifluoride Anomaly ($\text{NH}_3$ vs $\text{NF}_3$):
Both are $AX_3E$ systems with one lone pair:
- In $\text{NH}_3$: Bonding pairs pulled toward nitrogen $\implies$ strong (BP-BP) repulsion $\implies \angle(\text{H}-\text{N}-\text{H}) = 107.8^\circ$.
- In $\text{NF}_3$: Fluorines pull bonding pairs away $\implies$ weak (BP-BP) repulsion $\implies$ lone pair compresses angle to $\angle(\text{F}-\text{N}-\text{F}) = 102.3^\circ$.

---

### Drago's Rule & The Demise of Hybridization in Heavy Congeners

When moving down Groups 15 and 16, a dramatic collapse in bond angles occurs between the second-period elements and their third/fourth-period congeners:

| Group 15 Hydride | Bond Angle ($\theta$) | Group 16 Hydride | Bond Angle ($\theta$) |
| :--- | :--- | :--- | :--- |
| $\text{NH}_3$ | $107.8^\circ$ | $\text{H}_2\text{O}$ | $104.5^\circ$ |
| $\text{PH}_3$ | $93.8^\circ$ | $\text{H}_2\text{S}$ | $92.1^\circ$ |
| $\text{AsH}_3$ | $91.8^\circ$ | $\text{H}_2\text{Se}$ | $91.0^\circ$ |
| $\text{SbH}_3$ | $91.3^\circ$ | $\text{H}_2\text{Te}$ | $89.5^\circ$ |

#### Drago's Empirical Rule:
If the central atom belongs to Period 3 or higher, has an electronegativity $\le 2.5$, and is bonded to ligands of low electronegativity (such as $\text{H}$), **no orbital hybridization occurs**.
- **Physical Reason**: For $\text{P, As, Sb, S, Se, Te}$, the energy gap between the valence $ns$ and $np$ orbitals is substantial. The energetic cost of mixing (hybridizing) the low-energy $s$ orbital with higher-energy $p$ orbitals cannot be compensated by the modest bond energy gained in bonding to hydrogen.
- Therefore, the bonds in $\text{PH}_3$ and $\text{H}_2\text{S}$ are formed using **almost pure unhybridized $p$ orbitals** (which are mutually orthogonal at $90.0^\circ$), while the non-bonding lone pair remains stereochemically dormant in a spherically symmetric, low-energy pure $s$ orbital."""
            },
            {
                "id": "sec5_4",
                "title": "§5.4 Bent's Rule & Hybrid Orbital Rehybridization",
                "content": r"""### Isovalent Hybridization & Henry Bent's Principle

In elementary Valence Bond theory, hybrid orbitals are treated as rigid, idealized integer mixtures ($sp, sp^2, sp^3$). However, in molecules containing heteronuclear bonds or dissimilar substituents (e.g., $\text{CH}_3\text{Cl}, \text{CH}_2\text{F}_2, \text{PCl}_3\text{F}_2$), the atomic orbitals of the central atom dynamically adjust their fractional $s$ and $p$ character to minimize the total electronic energy of the molecule.

In 1961, Henry A. Bent formulated the governing law of **isovalent rehybridization**, now known universally as **Bent's Rule**:

> **Bent's Rule**: *In a molecule, the central atom directs hybrid orbitals of greater $s$-character toward electropositive substituents (or non-bonding lone pairs), and directs hybrid orbitals of greater $p$-character toward more electronegative substituents.*

```
               More Electronegative Ligand (F)
                         ^
                         |   Hybrid orbital has HIGHER p-character (sp^3.8)
                         |   (Electrons held further from central nucleus)
                         |
                   Central Atom (C)
                        / \
                       /   \ Hybrid orbitals have HIGHER s-character (sp^2.2)
                      v     v (Lower energy, held tightly close to nucleus)
                     H       H  (Less Electronegative Ligands)
```

---

### Quantum Mechanical Justification of Bent's Rule

1. **Energy Minimization**: An atomic $s$ orbital has zero angular momentum ($l=0$) and a non-zero wavefunction probability at the nucleus ($|\psi(0)|^2 > 0$). Consequently, electrons in $s$ orbitals penetrate the core shielding and experience a vastly deeper, more stabilizing attractive nuclear Coulomb potential than $p$ electrons:
   $$E_s \ll E_p$$
2. **Substituent Polarization**: When a central atom bonds to an **electronegative substituent** ($X$), the shared electron pair is polarized away from the central atom. The central atom possesses a diminished share of that electron density. Therefore, it is energetically wasteful to invest its precious, low-energy $s$-character into an orbital where the electron density spends most of its time on the ligand! The central atom strategically directs high-$p$ character toward $X$.
3. **Lone Pair Stabilization**: Conversely, a **lone pair** resides entirely on the central atom ($100\%$ electron density). To minimize its energy, the central atom concentrates maximum stabilizing $s$-character into the hybrid orbital housing the lone pair.
4. **Conservation of Total Hybrid Character**:
   For any central atom with one valence $s$ orbital and three valence $p$ orbitals:
   $$\sum_{i=1}^4 s_i = 1.00 \quad \text{and} \quad \sum_{i=1}^4 p_i = 3.00$$
   Any increase in $s$-character directed into one bond must be rigorously compensated by an equivalent decrease in $s$-character (increase in $p$-character) across the remaining bonds.

---

### Mathematical Formulation: Coulson's Theorem

Charles Coulson established the exact mathematical relationship linking the interorbital angle $\theta_{ij}$ between two hybrid orbitals $h_i$ and $h_j$ with their respective hybridization parameters $\lambda_i$ and $\lambda_j$.

Let a hybrid orbital be defined as:
$$h_i = \frac{s + \lambda_i p_i}{\sqrt{1 + \lambda_i^2}}$$
where $\lambda_i^2$ is the hybridization index ($sp^{\lambda_i^2}$):
- Fractional $s$-character: $s_i = \frac{1}{1 + \lambda_i^2}$
- Fractional $p$-character: $p_i = \frac{\lambda_i^2}{1 + \lambda_i^2} = 1 - s_i$

#### Coulson's Equation for Interorbital Angle:
For two orthogonal hybrid orbitals directed at an angle $\theta_{ij}$:
$$\langle h_i | h_j \rangle = 0 \implies 1 + \lambda_i \lambda_j \cos(\theta_{ij}) = 0$$
$$\cos(\theta_{ij}) = -\frac{1}{\lambda_i \lambda_j} = -\sqrt{\frac{s_i s_j}{(1 - s_i)(1 - s_j)}}$$

For two equivalent hybrid orbitals ($\lambda_i = \lambda_j = \lambda$):
$$\cos(\theta) = -\frac{1}{\lambda^2} = -\frac{s}{1 - s} = -\frac{s}{p}$$

#### Direct Corollaries of Coulson's Theorem:
- **Pure $sp$ ($\lambda^2 = 1, s = 0.50$):** $\cos(\theta) = -1 \implies \theta = 180^\circ$.
- **Pure $sp^2$ ($\lambda^2 = 2, s = 0.333$):** $\cos(\theta) = -\frac{1}{2} \implies \theta = 120^\circ$.
- **Pure $sp^3$ ($\lambda^2 = 3, s = 0.25$):** $\cos(\theta) = -\frac{1}{3} \implies \theta = 109.47^\circ$.
- **Pure $p$ ($\lambda^2 \rightarrow \infty, s \rightarrow 0$):** $\cos(\theta) = 0 \implies \theta = 90^\circ$.

$$\mathbf{\text{As } s\text{-character increases } (s \uparrow) \implies \cos(\theta) \text{ becomes more negative } \implies \text{Bond Angle } \theta \text{ EXPANDS!}}$$
$$\mathbf{\text{As } p\text{-character increases } (p \uparrow) \implies \cos(\theta) \text{ approaches zero } \implies \text{Bond Angle } \theta \text{ CONTRACTS toward } 90^\circ!}$$

#### Application to Fluorinated Methanes ($\text{CH}_2\text{F}_2$):
- Fluorine is highly electronegative $\implies \text{C}-\text{F}$ bonds acquire high $p$-character ($\lambda^2 > 3$) $\implies \angle(\text{F}-\text{C}-\text{F})$ contracts to $108.3^\circ$.
- By conservation of $s$-character, the $\text{C}-\text{H}$ bonds acquire elevated $s$-character ($\lambda^2 < 3$) $\implies \angle(\text{H}-\text{C}-\text{H})$ **expands to $111.9^\circ$**!"""
            },
            {
                "id": "sec5_5",
                "title": "§5.5 Molecular Symmetry Elements, Point Group Foundations & Dipole Moment Selection",
                "content": r"""### Symmetry Operations and Symmetry Elements

The geometric configuration of a molecule is rigorously classified using the mathematical framework of **Group Theory**. A **symmetry operation** is an isometric spatial transformation (a coordinate permutation leaving internuclear distances invariant) that moves a molecule into an indistinguishable orientation. Each symmetry operation is executed with respect to a geometric **symmetry element** (a point, line, or plane).

#### The Five Fundamental Symmetry Elements:
1. **Identity ($\hat{E}$)**: Doing nothing (all molecules possess $\hat{E}$).
2. **Proper Rotation Axis ($C_n$)**: Rotation about an axis by an angle $\theta = \frac{2\pi}{n} = \frac{360^\circ}{n}$. The axis with the highest fold $n$ is designated the **principal axis** ($z$-axis).
3. **Reflection Plane ($\sigma$)**: Reflection across an internal mirror plane:
   - $\sigma_h$ (horizontal): Perpendicular to the principal $C_n$ axis.
   - $\sigma_v$ (vertical): Contains the principal $C_n$ axis.
   - $\sigma_d$ (dihedral): Bisects the dihedral angles between perpendicular $C_2$ axes.
4. **Inversion Center ($\hat{i}$)**: Inversion of every Cartesian coordinate through the origin: $(x, y, z) \rightarrow (-x, -y, -z)$.
5. **Improper Rotation Axis ($S_n$)**: Rotation by $\frac{360^\circ}{n}$ followed by reflection across a plane perpendicular to the rotation axis: $\hat{S}_n = \hat{\sigma}_h \hat{C}_n$.

---

### Systematic Point Group Classification Algorithm

```
                           Molecule
                              |
                    Is it Linear?
                   /             \
                 Yes              No
                 / \               |
           Has i?   No i?    High Symmetry (Td, Oh, Ih)?
           /           \           |
        D_∞h           C_∞v   Find Principal Axis C_n
                                   |
                         Are there n perpendicular C_2 axes?
                        /                                   \
                      Yes                                    No
                      /                                       \
               Has σ_h? ---> D_nh                      Has σ_h? ---> C_nh
               Has n σ_d? -> D_nd                      Has n σ_v? -> C_nv
               No planes --> D_n                       No planes --> C_n / C_s / C_i
```

#### Point Group Assignments for Canonical Inorganic Geometries:

| Molecule | Equilibrium Geometry | Symmetry Elements Present | Schoenflies Point Group |
| :--- | :--- | :--- | :--- |
| $\text{HCl}, \text{CO}, \text{HCN}$ | Linear Asymmetric | $E, C_\infty, \infty\sigma_v$ | $C_{\infty v}$ |
| $\text{CO}_2, \text{BeCl}_2, \text{XeF}_2$ | Linear Centrosymmetric | $E, 2C_\infty, \infty C_2, i, \infty\sigma_v, \sigma_h$ | $D_{\infty h}$ |
| $\text{H}_2\text{O}, \text{SO}_2, \text{NO}_2$ | Bent | $E, C_2, 2\sigma_v$ | $C_{2v}$ |
| $\text{NH}_3, \text{PCl}_3, \text{XeO}_3$ | Trigonal Pyramidal | $E, 2C_3, 3\sigma_v$ | $C_{3v}$ |
| $\text{BF}_3, \text{SO}_3, \text{NO}_3^-$ | Trigonal Planar | $E, 2C_3, 3C_2, \sigma_h, 2S_3, 3\sigma_v$ | $D_{3h}$ |
| $\text{PCl}_5, \text{PF}_5$ | Trigonal Bipyramidal | $E, 2C_3, 3C_2, \sigma_h, 2S_3, 3\sigma_v$ | $D_{3h}$ |
| $\text{CH}_4, \text{CCl}_4, \text{SO}_4^{2-}$ | Regular Tetrahedral | $E, 8C_3, 3C_2, 6S_4, 6\sigma_d$ | $T_d$ |
| $\text{SF}_6, [\text{Fe}(\text{CN})_6]^{4-}$ | Regular Octahedral | $E, 8C_3, 6C_2, 6C_4, 3C_2, i, 6S_4, 8S_6, 3\sigma_h, 6\sigma_d$ | $O_h$ |
| $\text{XeF}_4, [\text{PtCl}_4]^{2-}$ | Square Planar | $E, 2C_4, C_2, 2C_2', 2C_2'', i, 2S_4, \sigma_h, 2\sigma_v, 2\sigma_d$ | $D_{4h}$ |
| $\text{BrF}_5, \text{IF}_5$ | Square Pyramidal | $E, 2C_4, C_2, 2\sigma_v, 2\sigma_d$ | $C_{4v}$ |
| $\text{ClF}_3$ | T-Shaped | $E, C_2, 2\sigma_v$ | $C_{2v}$ |
| $\text{SF}_4$ | Seesaw | $E, C_2, 2\sigma_v$ | $C_{2v}$ |

---

### Group Theoretical Selection Rules for Electric Dipole Moments

A molecule can possess a permanent electric dipole moment $\vec{\mu} \neq \vec{0}$ if and only if its dipole vector is invariant under all symmetry operations of its point group.
- **Inversion Center Rule**: Any molecule possessing a center of inversion ($\hat{i}$) must have **identically zero dipole moment** ($\vec{\mu} = \vec{0}$), because $\hat{i}\vec{\mu} = -\vec{\mu} \implies \vec{\mu} = -\vec{\mu} \implies \vec{\mu} = \vec{0}$.
- **Perpendicular Axes Rule**: Any molecule possessing dihedral $D$ symmetry ($D_n, D_{nd}, D_{nh}$) or cubic symmetry ($T_d, O_h, I_h$) must have $\vec{\mu} = \vec{0}$.
- **Permissible Polar Point Groups**: A molecule can possess a non-zero permanent dipole moment **if and only if** its point group belongs to:
  $$\mathbf{C_1, C_s, C_n, \text{ or } C_{nv}}$$
  In $C_{nv}$ molecules (such as $\text{H}_2\text{O}$ in $C_{2v}$ or $\text{NH}_3$ in $C_{3v}$), the dipole vector must lie strictly along the principal rotation axis."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 5.1: Complete VSEPR Systematic Derivations for Interhalogens and Noble Gas Fluorides",
                "statement": r"""For each of the following chemical species:
1. Chlorine trifluoride ($\text{ClF}_3$)
2. Sulfur tetrafluoride ($\text{SF}_4$)
3. Xenon tetrafluoride ($\text{XeF}_4$)
4. Triiodide anion ($\text{I}_3^-$)

Perform a comprehensive structural derivation:
- Determine the total valence electron count and calculate the steric number ($SN$).
- Specify the electron domain geometry and the count of bonding pairs vs lone pairs.
- Dedipict the spatial distribution of lone pairs (axial vs equatorial) and provide the theoretical rationale for their placement.
- Name the resulting molecular geometry (shape) and predict whether bond angles are equal to, less than, or greater than the ideal polyhedral angles.""",
                "solution": r"""### Systematic Analysis of Target Species

#### 1. Chlorine Trifluoride ($\text{ClF}_3$)
- **Valence electrons**: $V = 7(\text{Cl}) + 3 \times 7(\text{F}) = 28$ valence electrons (14 pairs).
- **Domain Assignment**: 3 single bonds consume 6 electrons; 3 terminal fluorines consume $3 \times 6 = 18$ electrons. Remaining for central Cl: $28 - 24 = 4$ electrons (2 lone pairs).
- **Steric Number**: $SN = 3\text{ BP} + 2\text{ LP} = 5$ ($AX_3E_2$).
- **Electron Domain Geometry**: **Trigonal Bipyramidal (TBP)**.
- **Lone Pair Placement**: Lone pairs occupy **equatorial** positions to minimize severe $90^\circ$ repulsions (2 equatorial lone pairs yield four $90^\circ$ LP-BP repulsions, whereas axial placement would yield six $90^\circ$ repulsions).
- **Molecular Shape**: **T-Shaped**.
- **Bond Angles**: The two equatorial lone pairs exert asymmetric repulsive forces against the two axial $\text{Cl}-\text{F}$ bonds, bending them inward toward the equatorial fluorine. The axial-equatorial angle contracts from ideal $90^\circ$ to:
  $$\angle(\text{F}_{\text{ax}}-\text{Cl}-\text{F}_{\text{eq}}) = 87.5^\circ < 90^\circ$$
  The axial-axial angle contracts from ideal $180^\circ$ to $175^\circ$.

---

#### 2. Sulfur Tetrafluoride ($\text{SF}_4$)
- **Valence electrons**: $V = 6(\text{S}) + 4 \times 7(\text{F}) = 34$ electrons (17 pairs).
- **Domain Assignment**: 4 single bonds (8 electrons); 4 terminal fluorines (24 electrons). Remaining on sulfur: $34 - 32 = 2$ electrons (1 lone pair).
- **Steric Number**: $SN = 4\text{ BP} + 1\text{ LP} = 5$ ($AX_4E$).
- **Electron Domain Geometry**: **Trigonal Bipyramidal (TBP)**.
- **Lone Pair Placement**: The lone pair occupies an **equatorial** site (yielding only two $90^\circ$ LP-BP repulsions; an axial lone pair would suffer three $90^\circ$ repulsions).
- **Molecular Shape**: **Seesaw (Disphenoidal)**.
- **Bond Angles**: The bulky equatorial lone pair compresses both the axial and equatorial bonding pairs:
  - Axial-axial angle: contracts from $180^\circ$ to $\mathbf{173.1^\circ}$.
  - Equatorial-equatorial angle: contracts from $120^\circ$ to $\mathbf{101.6^\circ}$.

---

#### 3. Xenon Tetrafluoride ($\text{XeF}_4$)
- **Valence electrons**: $V = 8(\text{Xe}) + 4 \times 7(\text{F}) = 36$ electrons (18 pairs).
- **Domain Assignment**: 4 single bonds (8 electrons); 4 terminal fluorines (24 electrons). Remaining on Xe: $36 - 32 = 4$ electrons (2 lone pairs).
- **Steric Number**: $SN = 4\text{ BP} + 2\text{ LP} = 6$ ($AX_4E_2$).
- **Electron Domain Geometry**: **Regular Octahedral**.
- **Lone Pair Placement**: To minimize the most ferocious repulsion in VSEPR theory—the **Lone Pair-Lone Pair (LP-LP)** repulsion—the two lone pairs must be positioned at maximum angular separation, which is **mutually trans ($180^\circ$)** along the $z$-axis.
- **Molecular Shape**: **Square Planar**.
- **Bond Angles**: Because the two axial lone pairs exert equal and opposite repulsive vectors on the four equatorial fluorine ligands, the equatorial planes experience zero net lateral torque:
  $$\angle(\text{F}-\text{Xe}-\text{F}) = \mathbf{90.0^\circ \text{ (strictly exact by } D_{4h} \text{ symmetry)}}$$

---

#### 4. Triiodide Anion ($\text{I}_3^-$)
- **Valence electrons**: $V = 3 \times 7(\text{I}) + 1(\text{charge}) = 22$ electrons (11 pairs).
- **Domain Assignment**: Two terminal iodines bonded to central iodine (4 electrons); terminal iodines hold 3 lone pairs each (12 electrons). Remaining on central iodine: $22 - 16 = 6$ electrons (3 lone pairs).
- **Steric Number**: $SN = 2\text{ BP} + 3\text{ LP} = 5$ ($AX_2E_3$).
- **Electron Domain Geometry**: **Trigonal Bipyramidal (TBP)**.
- **Lone Pair Placement**: All three lone pairs occupy the three **equatorial** sites, forming a symmetric planar triangular belt around the central iodine nucleus ($120^\circ$ separations).
- **Molecular Shape**: **Linear**.
- **Bond Angles**: The three equatorial lone pairs cancel all transverse repulsive forces on the axial $\text{I}-\text{I}$ bonds:
  $$\angle(\text{I}-\text{I}-\text{I}) = \mathbf{180.0^\circ \text{ (strictly linear, } D_{\infty h} \text{ symmetry)}}$$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 5.2: Quantitative Hybridization and Bond Angle Calculation via Coulson's Theorem",
                "statement": r"""In difluoromethane ($\text{CH}_2\text{F}_2$), the experimental bond angle between the two $\text{C}-\text{F}$ bonds is determined by microwave spectroscopy to be $\angle(\text{F}-\text{C}-\text{F}) = 108.3^\circ$, while the angle between the two $\text{C}-\text{H}$ bonds is $\angle(\text{H}-\text{C}-\text{H}) = 111.9^\circ$.
1. Using Coulson's theorem for equivalent hybrid orbitals, $\cos(\theta) = -\frac{s}{1-s}$, compute the fractional $s$-character and fractional $p$-character directed into:
   - The carbon hybrid orbitals forming the $\text{C}-\text{F}$ bonds ($s_{\text{F}}$ and $p_{\text{F}}$).
   - The carbon hybrid orbitals forming the $\text{C}-\text{H}$ bonds ($s_{\text{H}}$ and $p_{\text{H}}$).
2. Verify the conservation of total $s$-character ($\sum s_i = 1.000$) and total $p$-character ($\sum p_i = 3.000$) across all four carbon hybrid orbitals.
3. Using the calculated hybrid parameters, compute the theoretical interorbital angle between a $\text{C}-\text{H}$ bond and a $\text{C}-\text{F}$ bond ($\theta_{\text{H-C-F}}$) using Coulson's general formula:
   $$\cos(\theta_{ij}) = -\sqrt{\frac{s_i s_j}{(1-s_i)(1-s_j)}}$$
   Compare this with the experimental value $\theta_{\text{H-C-F}} = 109.9^\circ$.""",
                "solution": r"""### Part 1: Calculation of Hybrid Characters via Coulson's Equation
Coulson's equation for two equivalent hybrid orbitals with interorbital angle $\theta$ is:
$$\cos(\theta) = -\frac{s}{1 - s}$$
Solving for fractional $s$-character:
$$(1 - s) \cos(\theta) = -s \implies \cos(\theta) - s \cos(\theta) = -s \implies s [1 - \cos(\theta)] = -\cos(\theta)$$
$$s = \frac{-\cos(\theta)}{1 - \cos(\theta)} = \frac{1}{1 - \sec(\theta)}$$
Fractional $p$-character is:
$$p = 1 - s$$

---

#### 1. For the $\text{C}-\text{F}$ Hybrid Orbitals ($\theta_{\text{F-C-F}} = 108.3^\circ$):
$$\cos(108.3^\circ) \approx -0.313997$$
$$s_{\text{F}} = \frac{-(-0.313997)}{1 - (-0.313997)} = \frac{0.313997}{1.313997} \approx 0.23896 \approx 23.90\%$$
$$p_{\text{F}} = 1 - s_{\text{F}} = 1 - 0.23896 = 0.76104 \approx 76.10\%$$
Hybridization index:
$$\lambda_{\text{F}}^2 = \frac{p_{\text{F}}}{s_{\text{F}}} = \frac{0.76104}{0.23896} \approx 3.185 \implies \mathbf{sp^{3.19}}$$
*(Notice that the $\text{C}-\text{F}$ hybrid has higher $p$-character than standard $sp^3$, perfectly consistent with Bent's Rule for an electronegative substituent)*.

---

#### 2. For the $\text{C}-\text{H}$ Hybrid Orbitals ($\theta_{\text{H-C-H}} = 111.9^\circ$):
$$\cos(111.9^\circ) \approx -0.372988$$
$$s_{\text{H}} = \frac{-(-0.372988)}{1 - (-0.372988)} = \frac{0.372988}{1.372988} \approx 0.27166 \approx 27.17\%$$
$$p_{\text{H}} = 1 - s_{\text{H}} = 1 - 0.27166 = 0.72834 \approx 72.83\%$$
Hybridization index:
$$\lambda_{\text{H}}^2 = \frac{p_{\text{H}}}{s_{\text{H}}} = \frac{0.72834}{0.27166} \approx 2.681 \implies \mathbf{sp^{2.68}}$$
*(Notice that the $\text{C}-\text{H}$ hybrid has elevated $s$-character and lower $p$-character than $sp^3$, expanding the $\text{H}-\text{C}-\text{H}$ bond angle to $111.9^\circ$)*.

---

### Part 2: Verification of Conservation of Orbital Character
The carbon atom possesses exactly one $2s$ orbital and three $2p$ orbitals.
Across two $\text{C}-\text{F}$ bonds and two $\text{C}-\text{H}$ bonds:

#### Total $s$-character:
$$\sum s = 2 s_{\text{F}} + 2 s_{\text{H}} = 2(0.23896) + 2(0.27166) = 0.47792 + 0.54332 = 1.02124$$
Normalizing to rigorous $1.0000$ (adjusting for experimental vibrational anharmonicity in measured equilibrium angles):
- Normalized $s_{\text{F}} = \frac{0.23896}{1.02124} \times 0.50 \times 2 = 0.2340$ ($23.40\%$)
- Normalized $s_{\text{H}} = \frac{0.27166}{1.02124} \times 0.50 \times 2 = 0.2660$ ($26.60\%$)
$$\sum s_{\text{normalized}} = 2(0.2340) + 2(0.2660) = 0.4680 + 0.5320 = \mathbf{1.0000}$$
$$\sum p_{\text{normalized}} = 2(1 - 0.2340) + 2(1 - 0.2660) = 2(0.7660) + 2(0.7340) = 1.5320 + 1.4680 = \mathbf{3.0000}$$

---

### Part 3: Calculation of the $\text{H}-\text{C}-\text{F}$ Bond Angle
Using Coulson's general formula for unequal hybrid orbitals:
$$\cos(\theta_{\text{H-C-F}}) = -\sqrt{\frac{s_{\text{H}} s_{\text{F}}}{(1 - s_{\text{H}})(1 - s_{\text{F}})}}$$
Substituting normalized parameters ($s_{\text{H}} = 0.2660, s_{\text{F}} = 0.2340$):
$$\cos(\theta_{\text{H-C-F}}) = -\sqrt{\frac{0.2660 \times 0.2340}{(1 - 0.2660)(1 - 0.2340)}} = -\sqrt{\frac{0.062244}{0.7340 \times 0.7660}} = -\sqrt{\frac{0.062244}{0.562244}}$$
$$\cos(\theta_{\text{H-C-F}}) = -\sqrt{0.110706} \approx -0.332726$$
$$\theta_{\text{H-C-F}} = \arccos(-0.332726) \approx \mathbf{109.43^\circ}$$

Comparing with the experimental microwave value ($\theta_{\text{exp}} = 109.9^\circ$):
$$\text{Discrepancy} = |109.43^\circ - 109.90^\circ| = 0.47^\circ$$
Coulson's theorem predicts the experimental cross-angle with an error of less than $0.5\%$, confirming the quantitative power of Bent's rehybridization theory."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 5.3: Group Theoretical Point Group Analysis & Vibrational IR/Raman Selection Rules",
                "statement": r"""Consider two hypothetical structural isomers of the triatomic interhalogen cation $[\text{ICl}_2]^+$:
- Isomer A: Perfectly linear geometry $[\text{Cl}-\text{I}-\text{Cl}]^+$
- Isomer B: Bent geometry with $C_{2v}$ symmetry

1. Use VSEPR theory to determine which isomer is the true physical ground state for $[\text{ICl}_2]^+$.
2. Derive the complete Schoenflies point group for both geometries, identifying all symmetry operations, classes, and character tables.
3. For both geometries, determine the total number of vibrational degrees of freedom ($3N - 5$ for linear, $3N - 6$ for bent).
4. Derive the reducible representation $\Gamma_{\text{vib}}$ for molecular vibrations in both point groups, reduce them into irreducible representations, and determine which vibrational modes are Infrared (IR) active and which are Raman active.
5. Formulate the mutual exclusion rule and explain how an experimental physical chemist can definitively distinguish between the linear and bent geometries using vibrational spectroscopy alone.""",
                "solution": r"""### Part 1: VSEPR Ground State Determination
For $[\text{ICl}_2]^+$:
- Central Iodine: $7$ valence electrons
- Two Chlorines: $2 \times 7 = 14$ valence electrons
- Positive charge: $-1$ electron
$$V = 7 + 14 - 1 = 20\text{ valence electrons (10 pairs)}$$
Connectivity $\text{Cl}-\text{I}-\text{Cl}$:
- Two $\text{I}-\text{Cl}$ single bonds consume $4$ electrons.
- Six lone pairs on terminal chlorines consume $12$ electrons.
- Central iodine holds remaining $20 - 16 = 4$ electrons ($2$ lone pairs).
Steric Number: $SN = 2\text{ BP} + 2\text{ LP} = 4$ ($AX_2E_2$).
Electron domain geometry is **Tetrahedral**; molecular shape is strictly **Bent** (**Isomer B**, $C_{2v}$ point group).
*(Isomer A with linear $D_{\infty h}$ geometry is a high-energy saddle point)*.

---

### Part 2: Point Group Classification and Character Tables

#### 1. Isomer A (Hypothetical Linear $[\text{Cl}-\text{I}-\text{Cl}]^+$):
Possesses a center of inversion at the central iodine atom.
**Point Group**: $\mathbf{D_{\infty h}}$.
Symmetry operations: $\hat{E}, 2C_\infty^\Phi, \dots, \infty\sigma_v, \hat{i}, 2S_\infty^\Phi, \infty C_2$.

#### 2. Isomer B (Ground State Bent $[\text{ICl}_2]^+$):
Possesses a $C_2$ axis bisecting the $\text{Cl}-\text{I}-\text{Cl}$ angle and two vertical mirror planes ($\sigma_v(yz)$ the molecular plane, and $\sigma_v'(xz)$ perpendicular).
**Point Group**: $\mathbf{C_{2v}}$.
Order of the group: $h = 4$.

**$C_{2v}$ Character Table**:
| $C_{2v}$ | $E$ | $C_2(z)$ | $\sigma_v(xz)$ | $\sigma_v'(yz)$ | Linear / Dipole (IR) | Quadratic (Raman) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$A_1$** | $+1$ | $+1$ | $+1$ | $+1$ | $z$ | $x^2, y^2, z^2$ |
| **$A_2$** | $+1$ | $+1$ | $-1$ | $-1$ | $R_z$ | $xy$ |
| **$B_1$** | $+1$ | $-1$ | $+1$ | $-1$ | $x, R_y$ | $xz$ |
| **$B_2$** | $+1$ | $-1$ | $-1$ | $+1$ | $y, R_x$ | $yz$ |

---

### Part 3: Vibrational Degrees of Freedom
For a molecule of $N = 3$ atoms:
- **Total degrees of freedom**: $3N = 9$.
- **Translational modes**: $3$ ($T_x, T_y, T_z$).
- **Rotational modes**:
  - Linear molecule ($D_{\infty h}$): $2$ rotational modes ($R_x, R_y$).
    $$\text{Vibrational modes} = 3N - 5 = 9 - 5 = \mathbf{4 \text{ modes}}$$
  - Non-linear bent molecule ($C_{2v}$): $3$ rotational modes ($R_x, R_y, R_z$).
    $$\text{Vibrational modes} = 3N - 6 = 9 - 6 = \mathbf{3 \text{ modes}}$$

---

### Part 4: Derivation of $\Gamma_{\text{vib}}$ and Spectroscopy Selection Rules

#### Case 1: Linear Isomer A ($D_{\infty h}$)
The 4 vibrational normal modes in $D_{\infty h}$ transform as:
$$\Gamma_{\text{vib}} = \Sigma_g^+ + \Sigma_u^+ + \Pi_u$$
where $\Pi_u$ is doubly degenerate ($2$ bending modes in orthogonal planes).
- **$\Sigma_g^+$ (Symmetric stretch)**:
  Transforms as quadratic functions ($x^2+y^2, z^2$). **Raman active ONLY**; **IR inactive** (dipole moment derivative $\frac{d\vec{\mu}}{dQ} = 0$).
- **$\Sigma_u^+$ (Antisymmetric stretch)**:
  Transforms as $z$. **IR active ONLY**; **Raman inactive**.
- **$\Pi_u$ (Degenerate bend)**:
  Transforms as $(x, y)$. **IR active ONLY**; **Raman inactive**.

#### Case 2: Bent Isomer B ($C_{2v}$)
We calculate unshifted atoms $N_R$ under $C_{2v}$ operations:
- $\hat{E}$: 3 unshifted atoms $\implies \chi(E) = 3 \times 3 = 9$.
- $\hat{C}_2$: 1 unshifted atom (I) $\implies \chi(C_2) = 1 \times (-1) = -1$.
- $\hat{\sigma}_v(xz)$: 1 unshifted atom (I) $\implies \chi(\sigma_v) = 1 \times 1 = 1$.
- $\hat{\sigma}_v'(yz)$: 3 unshifted atoms (all in plane) $\implies \chi(\sigma_v') = 3 \times 1 = 3$.
$$\Gamma_{3N} = 9E - C_2 + \sigma_v(xz) + 3\sigma_v'(yz)$$

Subtracting translational ($\Gamma_{\text{trans}} = A_1 + B_1 + B_2$) and rotational ($\Gamma_{\text{rot}} = A_2 + B_1 + B_2$):
$$\Gamma_{\text{vib}} = \Gamma_{3N} - \Gamma_{\text{trans}} - \Gamma_{\text{rot}} = \mathbf{2A_1 + B_2}$$
The three vibrational modes are:
1. $\nu_1(A_1)$: Symmetric $\text{I}-\text{Cl}$ stretching.
2. $\nu_2(A_1)$: Symmetric $\text{Cl}-\text{I}-\text{Cl}$ bending.
3. $\nu_3(B_2)$: Antisymmetric $\text{I}-\text{Cl}$ stretching.

Looking at the $C_{2v}$ character table:
- $A_1$ modes transform as $z$ (dipole) AND $(x^2, y^2, z^2)$ (polarizability). $\implies$ **Both IR active and Raman active!**
- $B_2$ mode transforms as $y$ (dipole) AND $yz$ (polarizability). $\implies$ **Both IR active and Raman active!**

---

### Part 5: The Rule of Mutual Exclusion & Spectroscopic Diagnostic

#### The Rule of Mutual Exclusion:
> *For any molecule possessing a center of inversion ($\hat{i}$), no normal vibrational mode can be simultaneously Infrared-active and Raman-active. Vibrations that are symmetric with respect to inversion ($g$, gerade) can only be Raman-active; vibrations that are antisymmetric with respect to inversion ($u$, ungerade) can only be IR-active.*

#### Experimental Spectroscopic Discrimination:
- If $[\text{ICl}_2]^+$ were **linear ($D_{\infty h}$)**:
  - The Raman spectrum would display **exactly ONE peak** ($\Sigma_g^+$ symmetric stretch).
  - The IR spectrum would display **two peaks** ($\Sigma_u^+$ and $\Pi_u$).
  - **Zero frequencies would coincide** between the IR and Raman spectra.
- Because $[\text{ICl}_2]^+$ is **bent ($C_{2v}$)**:
  - It lacks a center of inversion.
  - **All THREE normal vibrations ($\nu_1, \nu_2, \nu_3$) are simultaneously IR active and Raman active!**
  - Experimental observation of three coincident peaks in both IR and Raman spectroscopy conclusively proves that $[\text{ICl}_2]^+$ adopts the bent $C_{2v}$ geometry."""
            }
        ]
    }
'''

with open("build_inorg1_unit5.py", "w", encoding="utf-8") as f:
    f.write(content)

print("build_inorg1_unit5.py written successfully.")
