#!/usr/bin/env python3
"""
create_inorg1_unit6.py
Generates build_inorg1_unit6.py for Unit 6:
Quantum Theories of Bonding: Valence Bond Theory & Molecular Orbital Theory
"""

import sys

content = r'''# -*- coding: utf-8 -*-
"""
Unit 6: Quantum Theories of Bonding: Valence Bond Theory & Molecular Orbital Theory
Contains 5 comprehensive sections and 3 tiered solved problems with full derivations.
"""

def get_unit6():
    return {
        "id": "unit6",
        "title": "Unit 6: Quantum Theories of Bonding: Valence Bond Theory & Molecular Orbital Theory",
        "simId": "sim_chem_molecular_orbital_lcao",
        "simTitle": "LCAO Molecular Orbital & Diatomic Engine",
        "sections": [
            {
                "id": "sec6_1",
                "title": "§6.1 Valence Bond (VB) Theory: Orbital Overlap, $\\sigma$ and $\\pi$ Bonds, Resonance Hybrids",
                "content": r"""### The Quantum Mechanical Origins of Valence Bond Theory

In 1927, Walter Heitler and Fritz London provided the very first quantum mechanical explanation of the chemical bond by solving the electronic Schrödinger equation for the neutral hydrogen molecule, $\text{H}_2$. Their approach laid the foundation for **Valence Bond (VB) Theory**, later expanded and popularized by Linus Pauling and John C. Slater.

In the Heitler-London treatment of $\text{H}_2$, consider two isolated hydrogen atoms, $A$ and $B$, each with a single electron ($1$ and $2$). At infinite separation, the total spatial electronic wavefunction is simply the product of isolated $1s$ hydrogenic orbitals:
$$\psi_{\text{isolated}} = \phi_A(1) \phi_B(2)$$
However, quantum mechanics requires indistinguishability: electrons are identical fermions. Therefore, an equally valid configuration is $\phi_A(2) \phi_B(1)$, in which electron 2 is near nucleus $A$ and electron 1 is near nucleus $B$.

By applying the Pauli Principle, the total state function $\Psi(1,2) = \psi_{\text{space}}(1,2) \cdot \chi_{\text{spin}}(1,2)$ must be antisymmetric under electron permutation ($\hat{P}_{12} \Psi = -\Psi$). This yields two distinct spatial eigenstates:

#### 1. Symmetric Spatial Singlet State (Bonding, $S = 0$):
$$\psi_+ = \frac{1}{\sqrt{2(1 + S^2)}} \left[ \phi_A(1) \phi_B(2) + \phi_A(2) \phi_B(1) \right]$$
Paired with an antisymmetric spin singlet:
$$\chi_{\text{singlet}} = \frac{1}{\sqrt{2}} [\alpha(1)\beta(2) - \beta(1)\alpha(2)]$$

#### 2. Antisymmetric Spatial Triplet State (Antibonding, $S = 1$):
$$\psi_- = \frac{1}{\sqrt{2(1 - S^2)}} \left[ \phi_A(1) \phi_B(2) - \phi_A(2) \phi_B(1) \right]$$
Paired with symmetric spin triplet components ($\alpha\alpha, \beta\beta, \frac{1}{\sqrt{2}}(\alpha\beta+\beta\alpha)$).

```
   Heitler-London Energy Curves for H2:
   
   Energy E(R)
    ^
    |          Triplet State E_- (Antisymmetric, Pure Repulsion)
    |          /--------------------------------- (Dissociated atoms E = 0)
    |         /
    |  0 ----/-----------------------------------
    |       /
    |      /
    |     \____    Singlet State E_+ (Symmetric, Bound Covalent State)
    |          \
    |           \______/ <-- Well Depth D_e ≈ 365 kJ/mol at R_0 = 74 pm
    +-------------------------------------------> Internuclear Distance R
```

#### The Heitler-London Energy Expectation Values:
Evaluating the expectation value of the electronic Hamiltonian $\hat{H} = -\frac{\hbar^2}{2m}(\nabla_1^2 + \nabla_2^2) - \frac{e^2}{4\pi\varepsilon_0}\left(\frac{1}{r_{1A}} + \frac{1}{r_{2B}} + \frac{1}{r_{1B}} + \frac{1}{r_{2A}} - \frac{1}{r_{12}} - \frac{1}{R_{AB}}\right)$:
$$E_\pm(R) = 2E_{1s} + \frac{J \pm K}{1 \pm S^2}$$
where:
- $S = \langle \phi_A | \phi_B \rangle$ is the **spatial overlap integral**.
- $J$ is the **Coulomb integral** (classical electrostatic interaction between electron charge densities and nuclei, negative but modest).
- $K$ is the **Exchange integral** (a purely quantum mechanical interference term arising from electron indistinguishability, deeply negative and responsible for over $85\%$ of the covalent binding energy):
  $$K = \iint \phi_A(1) \phi_B(2) \left( \frac{e^2}{4\pi\varepsilon_0 r_{12}} \right) \phi_A(2) \phi_B(1) \, d\mathbf{r}_1 d\mathbf{r}_2 + \dots$$

---

### Classification of Covalent Overlap: $\sigma$ and $\pi$ Frameworks

In Valence Bond theory, a covalent bond forms when two half-filled atomic orbitals overlap constructively in space, with their electron spins antiparallel ($\uparrow\downarrow$).

#### 1. $\sigma$ (Sigma) Bonds:
- **Symmetry**: Spherically symmetric with respect to rotation about the internuclear bond axis ($C_\infty$ symmetry).
- **Geometry**: Head-on (*axial*) overlap of atomic orbitals ($s-s$, $s-p_z$, $p_z-p_z$, or hybrid orbitals).
- **Electron Density**: Maximized directly along the internuclear axis between the nuclei.

#### 2. $\pi$ (Pi) Bonds:
- **Symmetry**: Possesses a nodal plane containing the internuclear axis; antisymmetric under reflection across this nodal plane.
- **Geometry**: Sideways (*lateral*) overlap of parallel unhybridized $p$ orbitals ($p_x-p_x$ or $p_y-p_y$) or $d$ orbitals ($d_{xz}, d_{yz}$).
- **Bond Strength**: Because lateral overlap is spatially less effective than axial overlap ($S_\pi \approx 0.2\text{–}0.3$ vs $S_\sigma \approx 0.5\text{–}0.7$), a $\pi$ bond is intrinsically weaker than a $\sigma$ bond formed between the same atoms ($D_\pi \approx 260\text{ kJ}\cdot\text{mol}^{-1}$ vs $D_\sigma \approx 350\text{ kJ}\cdot\text{mol}^{-1}$ in carbon-carbon systems)."""
            },
            {
                "id": "sec6_2",
                "title": "§6.2 Orbital Hybridization: $sp$, $sp^2$, $sp^3$, $sp^3d$, $sp^3d^2$ Wavefunction Formulations & Orthogonality Proofs",
                "content": r"""### Mathematical Formulation of Hybrid Orbitals

In the isolated ground-state carbon atom ($1s^2 2s^2 2p_x^1 2p_y^1 2p_z^0$), only two unpaired electrons exist, predicting a valence of 2 with $90^\circ$ bond angles (as in $\text{CH}_2$). Yet carbon forms four equivalent, tetrahedrally directed bonds in methane ($\text{CH}_4$, $109.5^\circ$). To resolve this discrepancy, Linus Pauling introduced **Orbital Hybridization**: the mathematical mixing of non-equivalent atomic wavefunctions on the same atom to generate a set of equivalent directed hybrid wavefunctions that maximize spatial overlap integrals with ligand orbitals.

Any hybrid orbital $h_i$ is a normalized linear combination of atomic orbitals:
$$h_i = c_{is} \phi_s + c_{ip_x} \phi_{p_x} + c_{ip_y} \phi_{p_y} + c_{ip_z} \phi_{p_z}$$

The coefficients $c_{ij}$ are rigorously constrained by two fundamental quantum mechanical conditions:
1. **Normalization Condition**: $\langle h_i | h_i \rangle = 1 \implies \sum_j c_{ij}^2 = 1$.
2. **Mutual Orthogonality Condition**: $\langle h_i | h_j \rangle = \delta_{ij} \implies \sum_k c_{ik} c_{jk} = 0 \quad (i \neq j)$.
3. **Conservation of Total Orbital Density**: Across $N$ hybrid orbitals, the sum of squared coefficients for each constituent atomic orbital must equal unity ($\sum_{i=1}^N c_{is}^2 = 1$, $\sum_{i=1}^N c_{ip_x}^2 = 1$, etc.).

---

### Rigorous Derivation of $sp^3$ Hybrid Wavefunctions

For four equivalent $sp^3$ hybrid orbitals directed toward the vertices of a regular tetrahedron inscribed inside a Cartesian coordinate cube:
- The four vertices point along vectors: $(+1,+1,+1), (+1,-1,-1), (-1,+1,-1), (-1,-1,+1)$.
- Because the four hybrid orbitals are symmetry-equivalent, each must contain exactly one-fourth of the $2s$ orbital density:
  $$c_{is}^2 = \frac{1}{4} \implies c_{is} = \frac{1}{2} \quad \text{for } i = 1, 2, 3, 4$$

```
       Orientation of sp3 Hybrids:
              h1 = (1/2) [ s + px + py + pz ]  -->  (+1, +1, +1)
              h2 = (1/2) [ s + px - py - pz ]  -->  (+1, -1, -1)
              h3 = (1/2) [ s - px + py - pz ]  -->  (-1, +1, -1)
              h4 = (1/2) [ s - px - py + pz ]  -->  (-1, -1, +1)
```

#### Analytical Expressions:
$$h_1 = \frac{1}{2} \left( \phi_s + \phi_{p_x} + \phi_{p_y} + \phi_{p_z} \right)$$
$$h_2 = \frac{1}{2} \left( \phi_s + \phi_{p_x} - \phi_{p_y} - \phi_{p_z} \right)$$
$$h_3 = \frac{1}{2} \left( \phi_s - \phi_{p_x} + \phi_{p_y} - \phi_{p_z} \right)$$
$$h_4 = \frac{1}{2} \left( \phi_s - \phi_{p_x} - \phi_{p_y} + \phi_{p_z} \right)$$

#### Proof of Normalization:
$$\langle h_1 | h_1 \rangle = \left(\frac{1}{2}\right)^2 \left[ \langle s|s \rangle + \langle p_x|p_x \rangle + \langle p_y|p_y \rangle + \langle p_z|p_z \rangle \right] = \frac{1}{4} [1 + 1 + 1 + 1] = 1.000 \quad \mathbf{(Verified)}$$

#### Proof of Mutual Orthogonality:
$$\langle h_1 | h_2 \rangle = \left(\frac{1}{2}\right) \left(\frac{1}{2}\right) \left[ \langle s|s \rangle + \langle p_x|p_x \rangle - \langle p_y|p_y \rangle - \langle p_z|p_z \rangle \right]$$
$$\langle h_1 | h_2 \rangle = \frac{1}{4} [1 + 1 - 1 - 1] = 0.000 \quad \mathbf{(Verified)}$$

#### Proof of the Tetrahedral Angle ($109.47^\circ$):
The interorbital angle $\theta$ between $h_1$ and $h_2$ is obtained from the dot product of their $p$-orbital directional vectors $\vec{v}_1 = (1, 1, 1)$ and $\vec{v}_2 = (1, -1, -1)$:
$$\cos(\theta) = \frac{\vec{v}_1 \cdot \vec{v}_2}{|\vec{v}_1| |\vec{v}_2|} = \frac{(1)(1) + (1)(-1) + (1)(-1)}{\sqrt{1^2+1^2+1^2} \sqrt{1^2+(-1)^2+(-1)^2}} = \frac{1 - 1 - 1}{\sqrt{3}\sqrt{3}} = -\frac{1}{3}$$
$$\theta = \arccos\left(-\frac{1}{3}\right) \approx 109.4712^\circ \quad \mathbf{(Exact)}$$

---

### Derivations for $sp^2$ and $sp$ Hybrids

#### 1. Trigonal Planar $sp^2$ Hybrids (Lie in $xy$-plane):
Each hybrid contains $\frac{1}{3}$ $s$-character ($c_{is} = \frac{1}{\sqrt{3}}$). Align $h_1$ along the $x$-axis:
$$h_1 = \frac{1}{\sqrt{3}} \phi_s + \sqrt{\frac{2}{3}} \phi_{p_x}$$
$$h_2 = \frac{1}{\sqrt{3}} \phi_s - \frac{1}{\sqrt{6}} \phi_{p_x} + \frac{1}{\sqrt{2}} \phi_{p_y}$$
$$h_3 = \frac{1}{\sqrt{3}} \phi_s - \frac{1}{\sqrt{6}} \phi_{p_x} - \frac{1}{\sqrt{2}} \phi_{p_y}$$
$$\langle h_1 | h_2 \rangle = \left(\frac{1}{\sqrt{3}}\right)\left(\frac{1}{\sqrt{3}}\right) + \left(\sqrt{\frac{2}{3}}\right)\left(-\frac{1}{\sqrt{6}}\right) = \frac{1}{3} - \frac{\sqrt{2}}{3\sqrt{2}} = \frac{1}{3} - \frac{1}{3} = 0$$
$$\cos(\theta) = -\frac{s}{1-s} = -\frac{1/3}{2/3} = -\frac{1}{2} \implies \theta = 120.0^\circ$$

#### 2. Linear $sp$ Hybrids (Collinear along $z$-axis):
$$h_1 = \frac{1}{\sqrt{2}} (\phi_s + \phi_{p_z}), \quad h_2 = \frac{1}{\sqrt{2}} (\phi_s - \phi_{p_z})$$
$$\cos(\theta) = -\frac{s}{1-s} = -\frac{1/2}{1/2} = -1 \implies \theta = 180.0^\circ$$"""
            },
            {
                "id": "sec6_3",
                "title": "§6.3 Molecular Orbital (MO) Theory Fundamentals: LCAO Approximation, Secular Determinant & Overlap Integrals",
                "content": r"""### The Molecular Orbital Paradigm: Robert Mulliken & Friedrich Hund

While Valence Bond theory constructs wavefunctions by pairing electrons in localized atomic or hybrid orbitals, **Molecular Orbital (MO) Theory** asserts that electrons in a molecule belong to the entire molecular architecture as a whole, moving under the influence of all atomic nuclei simultaneously within delocalized, polycentric wavefunctions termed **Molecular Orbitals ($\psi$)**.

---

### The Linear Combination of Atomic Orbitals (LCAO) Approximation

In the LCAO approximation, a one-electron molecular orbital $\psi_j$ is expanded as a linear combination of $N$ known basis atomic orbitals $\chi_i$:
$$\psi_j = \sum_{i=1}^N c_{ji} \chi_i$$

To find the optimal coefficients $c_{ji}$ and orbital energies $E_j$, we apply the Rayleigh-Ritz Variational Principle:
$$E = \frac{\langle \psi | \hat{H} | \psi \rangle}{\langle \psi | \psi \rangle} = \frac{\sum_{i} \sum_{k} c_i c_k H_{ik}}{\sum_{i} \sum_{k} c_i c_k S_{ik}}$$
where:
- $H_{ik} = \langle \chi_i | \hat{H} | \chi_k \rangle$ is the **Hamiltonian Matrix Element**:
  - For $i = k$: $H_{ii} = \alpha_i$ is the **Coulomb Integral**, representing the energy of an electron in atomic orbital $\chi_i$ under the field of all nuclei (negative value, correlated with valence orbital ionization energy).
  - For $i \neq k$: $H_{ik} = \beta_{ik}$ is the **Resonance Integral** (Transfer Integral), representing the electronic interaction energy between overlapping orbitals $\chi_i$ and $\chi_k$ (negative value, driving covalent bonding).
- $S_{ik} = \langle \chi_i | \chi_k \rangle$ is the **Spatial Overlap Integral**:
  - $S_{ii} = 1$ (normalized atomic orbitals).
  - $S_{ik}$ measures the spatial volume coincidence between wavefunctions $\chi_i$ and $\chi_k$ ($0 \le |S_{ik}| < 1$).

---

### Derivation of the Secular Determinant

Minimizing the variational energy $E$ with respect to each variational parameter $c_m$:
$$\frac{\partial E}{\partial c_m} = 0 \quad \text{for all } m = 1, 2, \dots, N$$

Differentiating the Rayleigh quotient gives the system of **Roothaan Secular Equations**:
$$\sum_{k=1}^N c_k (H_{mk} - E S_{mk}) = 0 \quad (m = 1, 2, \dots, N)$$

In matrix notation:
$$\mathbf{H} \mathbf{c} = E \mathbf{S} \mathbf{c}$$

A non-trivial solution ($\mathbf{c} \neq \mathbf{0}$) exists if and only if the secular determinant vanishes identically:
$$\det(\mathbf{H} - E \mathbf{S}) = 0$$

$$\begin{vmatrix}
H_{11} - E S_{11} & H_{12} - E S_{12} & \cdots & H_{1N} - E S_{1N} \\
H_{21} - E S_{21} & H_{22} - E S_{22} & \cdots & H_{2N} - E S_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
H_{N1} - E S_{N1} & H_{N2} - E S_{N2} & \cdots & H_{NN} - E S_{NN}
\end{vmatrix} = 0$$

---

### Exact Analytical Solution for a Homonuclear Diatomic System ($A_2$)

Consider two identical atomic orbitals $\chi_A$ and $\chi_B$ with $H_{AA} = H_{BB} = \alpha$, $H_{AB} = H_{BA} = \beta$, and overlap $S_{AB} = S_{BA} = S$:
$$\begin{vmatrix} \alpha - E & \beta - E S \\ \beta - E S & \alpha - E \end{vmatrix} = 0$$
$$(\alpha - E)^2 - (\beta - E S)^2 = 0 \implies (\alpha - E) = \pm (\beta - E S)$$

#### 1. Bonding Molecular Orbital ($E_+$):
$$\alpha - E_+ = -(\beta - E_+ S) \implies \alpha + \beta = E_+ (1 + S)$$
$$E_{\text{bonding}} = E_+ = \frac{\alpha + \beta}{1 + S}$$
Wavefunction:
$$\psi_{\text{bonding}} = \frac{1}{\sqrt{2(1 + S)}} (\chi_A + \chi_B)$$

#### 2. Antibonding Molecular Orbital ($E_-$):
$$\alpha - E_- = +(\beta - E_- S) \implies \alpha - \beta = E_- (1 - S)$$
$$E_{\text{antibonding}} = E_- = \frac{\alpha - \beta}{1 - S}$$
Wavefunction:
$$\psi_{\text{antibonding}} = \frac{1}{\sqrt{2(1 - S)}} (\chi_A - \chi_B)$$

```
   Energy Level Diagram for A2 (including overlap S > 0):
   
         E_- (Antibonding)  -----------  ΔE_anti = (|β| - αS) / (1 - S)
                                    ^
                                    |  Notice: ΔE_anti > ΔE_bond!
   α (Atomic Levels) ------   ------|-------
                                    |
         E_+ (Bonding)      -----------  ΔE_bond = (|β| + αS) / (1 + S)
```

#### Fundamental Theorem: The Antibonding Orbital is MORE Destabilizing than the Bonding Orbital is Stabilizing!
Because $0 < S < 1$:
$$1 - S < 1 + S \implies \frac{1}{1 - S} > \frac{1}{1 + S}$$
Subtracting atomic level $\alpha$:
$$\Delta E_{\text{destabilization}} = E_- - \alpha = \frac{\alpha - \beta - \alpha(1-S)}{1-S} = \frac{-\beta + \alpha S}{1 - S}$$
$$\Delta E_{\text{stabilization}} = \alpha - E_+ = \alpha - \frac{\alpha + \beta}{1+S} = \frac{\alpha S - \beta}{1 + S}$$
Since $\beta < 0$, let $|\beta| = -\beta$:
$$\Delta E_{\text{destabilization}} = \frac{|\beta| + \alpha S}{1 - S} \quad \text{and} \quad \Delta E_{\text{stabilization}} = \frac{|\beta| - \alpha S}{1 + S}$$
Because the denominator $(1-S)$ is smaller than $(1+S)$:
$$\mathbf{\Delta E_{\text{destabilization}} > \Delta E_{\text{stabilization}}}$$
**Physical Consequence**: Populating an equal number of bonding and antibonding electrons (e.g., in $\text{He}_2$, with configuration $\sigma_{1s}^2 \sigma_{1s}^{*2}$) results in **net repulsion**, preventing molecule formation."""
            },
            {
                "id": "sec6_4",
                "title": "§6.4 Homonuclear Diatomic Molecules ($H_2$ through $Ne_2$): $2s$-$2p$ Mixing, Paramagnetism of $O_2$ & Bond Orders",
                "content": r"""### Construction of Second-Row Homonuclear Diatomic MOs

When constructing molecular orbitals for the second-row homonuclear diatomics ($\text{Li}_2, \text{Be}_2, \text{B}_2, \text{C}_2, \text{N}_2, \text{O}_2, \text{F}_2, \text{Ne}_2$):
- Core $1s$ orbitals form non-bonding core molecular orbitals: $\sigma_g(1s)^2 \sigma_u^*(1s)^2$.
- Valence $2s$ orbitals form $\sigma_g(2s)$ and $\sigma_u^*(2s)$.
- Valence $2p_z$ orbitals (oriented along the bond axis) form head-on $\sigma_g(2p_z)$ and $\sigma_u^*(2p_z)$.
- Valence $2p_x$ and $2p_y$ orbitals overlap laterally to form doubly degenerate $\pi_u(2p_{x,y})$ and $\pi_g^*(2p_{x,y})$.

---

### The Phenomenon of $2s-2p_z$ Orbital Mixing (Orbital Sprossover)

In an idealized scheme where orbitals of different angular momentum do not interact, $\sigma_g(2p_z)$ has stronger spatial overlap than lateral $\pi$ orbitals, predicting that $\sigma_g(2p_z)$ should lie below $\pi_u(2p)$ in energy.

However, quantum mechanical symmetry rules dictate that **any molecular orbitals belonging to identical irreducible representations can mix if they are energetically proximate**. Both $\sigma_g(2s)$ and $\sigma_g(2p_z)$ possess identical $\sigma_g^+$ symmetry under $D_{\infty h}$.

```
   Normal Ordering (O2, F2):             Inverted Ordering (B2, C2, N2) due to s-p mixing:
   
   σ_u*(2p)    ---                       σ_u*(2p)    ---
   π_g*(2p)    - -                       π_g*(2p)    - -
   π_u(2p)     - -                       σ_g(2p)     ---  <-- Pushed ABOVE π_u!
   σ_g(2p)     ---                       π_u(2p)     - -
   σ_u*(2s)    ---                       σ_u*(2s)    ---  <-- Pushed DOWN
   σ_g(2s)     ---                       σ_g(2s)     ---
```

#### Physical Mechanism:
1. In the lighter elements ($\text{Li, Be, B, C, N}$), the energy separation between the valence $2s$ and $2p$ atomic orbitals is small:
   $$\Delta E(2p - 2s)[\text{C}] \approx 10.7\text{ eV}, \quad \Delta E(2p - 2s)[\text{N}] \approx 12.4\text{ eV}$$
2. Strong configuration interaction (quantum mixing) occurs between $\sigma_g(2s)$ and $\sigma_g(2p_z)$:
   - The lower orbital, $\sigma_g(2s)$, is pushed **further down** in energy.
   - The upper orbital, $\sigma_g(2p_z)$, is pushed **substantially up** in energy, rising **above the degenerate $\pi_u(2p)$ level**!
3. In heavier elements ($\text{O, F, Ne}$), the escalating nuclear charge $Z_{\text{eff}}$ binds the compact $2s$ electrons much more tightly than $2p$, widening the energy gap:
   $$\Delta E(2p - 2s)[\text{O}] \approx 16.5\text{ eV}, \quad \Delta E(2p - 2s)[\text{F}] \approx 21.6\text{ eV}$$
   Because the energy denominator in second-order perturbation theory $(\Delta E)^{-1}$ is large, mixing is negligible, restoring the **normal orbital sequence** where $\sigma_g(2p_z)$ lies below $\pi_u(2p)$.

---

### Master Correlation Table of Second-Row Diatomics

$$\text{Bond Order} = \frac{N_{\text{bonding}} - N_{\text{antibonding}}}{2}$$

| Molecule | Valence Valence Electrons | Ground State Electron Configuration | Bond Order | Bond Length (pm) | Dissociation Energy ($\text{kJ}\cdot\text{mol}^{-1}$) | Magnetic Character |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\text{Li}_2$ | $2$ | $\sigma_g(2s)^2$ | $1$ | $267$ | $106$ | Diamagnetic |
| $\text{Be}_2$ | $4$ | $\sigma_g(2s)^2 \sigma_u^*(2s)^2$ | $0$ | $245$ (vdW) | $\sim 9$ (unbound) | Diamagnetic |
| $\text{B}_2$ | $6$ | $\sigma_g(2s)^2 \sigma_u^*(2s)^2 \pi_u(2p)^2$ | $1$ | $159$ | $297$ | **Paramagnetic** ($2$ unpaired $e^-$) |
| $\text{C}_2$ | $8$ | $\sigma_g(2s)^2 \sigma_u^*(2s)^2 \pi_u(2p)^4$ | $2$ | $124$ | $607$ | Diamagnetic (pure $\pi$ double bond!) |
| $\text{N}_2$ | $10$ | $\sigma_g(2s)^2 \sigma_u^*(2s)^2 \pi_u(2p)^4 \sigma_g(2p)^2$ | $3$ | $109.8$ | $945$ | Diamagnetic |
| $\text{O}_2$ | $12$ | $\sigma_g(2s)^2 \sigma_u^*(2s)^2 \sigma_g(2p)^2 \pi_u(2p)^4 \pi_g^*(2p)^2$ | $2$ | $120.7$ | $498$ | **Paramagnetic** ($2$ unpaired $e^-$) |
| $\text{F}_2$ | $14$ | $\sigma_g(2s)^2 \sigma_u^*(2s)^2 \sigma_g(2p)^2 \pi_u(2p)^4 \pi_g^*(2p)^4$ | $1$ | $141.2$ | $159$ | Diamagnetic |
| $\text{Ne}_2$ | $16$ | $\dots \pi_g^*(2p)^4 \sigma_u^*(2p)^2$ | $0$ | $310$ (vdW) | $\sim 0.35$ (unbound) | Diamagnetic |

#### The Triumphant Proof: Paramagnetism of Dioxygen ($\text{O}_2$)
Valence Bond theory predicted that $\text{O}_2$ has a double bond with all electrons paired ($\ddot{\text{O}}=\ddot{\text{O}}$), implying diamagnetism. Experimentally, liquid oxygen is strongly attracted to the poles of a magnet.
Molecular Orbital theory explains this effortlessly: the last two electrons enter the degenerate antibonding $\pi_g^*(2p_x)$ and $\pi_g^*(2p_y)$ orbitals. By **Hund's Rule of Maximum Multiplicity**, the lowest-energy state has parallel spins:
$$\pi_g^*(2p_x)^1 \quad \pi_g^*(2p_y)^1 \implies S = \frac{1}{2} + \frac{1}{2} = 1 \quad (\text{Triplet Ground State } ^3\Sigma_g^-)$$
This provides a spin magnetic moment of $\mu_s = \sqrt{n(n+2)} \mu_B = \sqrt{2(4)} \mu_B = 2.83\text{ Bohr Magnetons}$, exactly matching experimental magnetic susceptibility measurements."""
            },
            {
                "id": "sec6_5",
                "title": "§6.5 Heteronuclear Diatomic Molecules ($CO$, $NO$, $HF$, $CN^-$): Polarization, Frontier Orbitals & $\\pi$-Backbonding",
                "content": r"""### Heteronuclear Diatomic Architecture & Electronegativity Asymmetry

In a heteronuclear diatomic molecule $AB$, the constituent atomic orbitals possess unequal valence orbital ionization energies (VOIEs):
$$H_{AA} = \alpha_A \neq H_{BB} = \alpha_B$$

The more electronegative atom ($B$) holds its electrons in a deeper potential well ($\alpha_B$ is more negative than $\alpha_A$).
Solving the secular determinant for unequal Coulomb integrals:
$$E = \frac{\alpha_A + \alpha_B}{2} \pm \sqrt{\left(\frac{\alpha_A - \alpha_B}{2}\right)^2 + \beta^2}$$

#### Fundamental Asymmetry Theorem:
1. **Bonding Molecular Orbitals**: Lie closer in energy to the more electronegative atom ($B$), and their wavefunction is dominated by $B$ ($|c_B| > |c_A|$). Bonding electron density is polarized toward the electronegative ligand.
2. **Antibonding Molecular Orbitals**: Lie closer in energy to the more electropositive atom ($A$), and their wavefunction is dominated by $A$ ($|c_A| > |c_B|$). The unoccupied frontier orbital ($LUMO$) is polarized toward the electropositive atom.

---

### The Molecular Orbital Architecture of Carbon Monoxide ($CO$)

Carbon monoxide is isoelectronic with dinitrogen ($\text{N}_2$, 10 valence electrons), yet possesses extraordinarily unique chemical reactivity as the prototypical ligand in coordination chemistry.

- Valence atomic levels:
  - Carbon: $2s = -19.4\text{ eV}$, $2p = -10.7\text{ eV}$
  - Oxygen: $2s = -32.4\text{ eV}$, $2p = -15.9\text{ eV}$
- Because the energy of carbon $2s$ ($-19.4\text{ eV}$) is remarkably close to oxygen $2p$ ($-15.9\text{ eV}$), extensive symmetry mixing occurs along the $\sigma$ framework.

```
   Carbon Monoxide MO Diagram:
   
   C Orbitals                  CO Molecular Orbitals                 O Orbitals
                  
   2p (-10.7 eV) ---           4σ* (LUMO+1)   ---
                               2π* (LUMO)     - -  <-- 70% localized on Carbon!
                               3σ  (HOMO)     ---  <-- 80% localized on Carbon! (Lone pair)
                               1π             - -  <-- 70% localized on Oxygen!
                               2σ             ---
   2s (-19.4 eV) ---                                                 --- 2p (-15.9 eV)
                               1σ             ---  <-- Pure O(2s) non-bonding
                                                                     --- 2s (-32.4 eV)
```

#### Detailed Assignment of the Occupied Orbitals of $CO$:
1. $1\sigma$: Essentially the non-bonding $2s$ core lone pair of oxygen ($-38\text{ eV}$).
2. $2\sigma$: Bonding $\sigma$ interaction between carbon $2s$ and oxygen $2p_z$.
3. $1\pi$: Doubly degenerate bonding $\pi$ orbitals, heavily polarized toward oxygen ($\sim 70\%$ oxygen character).
4. $3\sigma$ (**HOMO**, Highest Occupied Molecular Orbital): An orbital weakly bonding or non-bonding with respect to the $\text{C}-\text{O}$ axis, but with an **enormous directional electron lobe projecting outward from the carbon nucleus into space** ($\sim 80\%$ carbon character).
5. $2\pi^*$ (**LUMO**, Lowest Unoccupied Molecular Orbital): Doubly degenerate empty antibonding $\pi^*$ orbitals, heavily localized on carbon ($\sim 70\%$ carbon character).

---

### The Mechanism of Dew-Chatt-Duncanson $\pi$-Backbonding

The MO architecture explains the profound chemical paradox of $CO$: **Why does carbon monoxide coordinate to transition metals exclusively through the carbon atom, despite oxygen being vastly more electronegative?**

The coordination involves a synergistic push-pull mechanism:
1. **$\sigma$-Donation**: The carbon-localized $3\sigma$ HOMO donates its electron pair directly into an empty transition metal $d$ orbital (such as $d_{z^2}$ or $d_{x^2-y^2}$), forming a dative metal-carbon $\sigma$ bond:
   $$\text{M} \xleftarrow{\sigma} \text{C}\equiv\text{O}$$
2. **$\pi$-Backbonding ($\pi$-Backdonation)**: Filled transition metal $d_\pi$ orbitals ($d_{xy}, d_{xz}, d_{yz}$) overlap laterally with the empty, low-lying $2\pi^*$ LUMO of $CO$, transferring electron density back from the metal to the ligand:
   $$\text{M} \xrightarrow{\pi} \text{C}\equiv\text{O}$$

Because the $2\pi^*$ LUMO is polarized toward carbon, its spatial overlap with the metal $d$ orbitals is maximized at the carbon terminus.

#### Spectroscopic Consequences of $\pi$-Backbonding:
- As electron density populates the $\text{C}-\text{O}$ antibonding $2\pi^*$ orbital, the $\text{C}-\text{O}$ bond order decreases from $3.0$ toward $2.5$.
- Consequently, the $\text{C}-\text{O}$ bond length expands ($112.8\text{ pm} \rightarrow 115\text{–}120\text{ pm}$).
- The infrared stretching frequency drops precipitously:
  $$\tilde{\nu}_{\text{free } CO} = 2143\text{ cm}^{-1} \xrightarrow{\text{complexation}} \tilde{\nu}_{\text{coordinated } CO} = 1850\text{–}2000\text{ cm}^{-1}$$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 6.1: Comprehensive MO Analysis of the Dioxygen Redox Series",
                "statement": r"""Consider the four species of the dioxygen redox series:
- Dioxygen cation: $\text{O}_2^+$
- Neutral dioxygen: $\text{O}_2$
- Superoxide radical anion: $\text{O}_2^-$
- Peroxide dianion: $\text{O}_2^{2-}$

1. Write out the complete valence molecular orbital electron configuration for all four chemical species (using the unmixed $D_{\infty h}$ ordering: $\sigma_g(2s), \sigma_u^*(2s), \sigma_g(2p), \pi_u(2p), \pi_g^*(2p), \sigma_u^*(2p)$).
2. Calculate the formal bond order for each species using $BO = \frac{N_b - N_a}{2}$.
3. Predict the number of unpaired electrons ($n$) and the magnetic spin-only moment $\mu_s = \sqrt{n(n+2)} \mu_B$ for each species.
4. Rank the four species in order of:
   - Increasing equilibrium bond length ($d_0$).
   - Increasing bond dissociation enthalpy ($D_0$).
   - Increasing fundamental vibrational infrared stretching frequency ($\tilde{\nu}$).""",
                "solution": r"""### Part 1: Valence Electron Counts and MO Configurations
For atomic oxygen, valence configuration is $2s^2 2p^4$ (6 valence electrons).

1. **Dioxygen Cation ($\text{O}_2^+$)**: $12 - 1 = 11$ valence electrons.
   $$\sigma_g(2s)^2 \sigma_u^*(2s)^2 \sigma_g(2p)^2 \pi_u(2p)^4 \pi_g^*(2p)^1$$
2. **Neutral Dioxygen ($\text{O}_2$)**: $12$ valence electrons.
   $$\sigma_g(2s)^2 \sigma_u^*(2s)^2 \sigma_g(2p)^2 \pi_u(2p)^4 \pi_g^*(2p)^2$$
3. **Superoxide Anion ($\text{O}_2^-$)**: $12 + 1 = 13$ valence electrons.
   $$\sigma_g(2s)^2 \sigma_u^*(2s)^2 \sigma_g(2p)^2 \pi_u(2p)^4 \pi_g^*(2p)^3$$
4. **Peroxide Dianion ($\text{O}_2^{2-}$)**: $12 + 2 = 14$ valence electrons.
   $$\sigma_g(2s)^2 \sigma_u^*(2s)^2 \sigma_g(2p)^2 \pi_u(2p)^4 \pi_g^*(2p)^4$$

---

### Part 2: Bond Order Calculations
Bonding orbitals: $\sigma_g(2s)$ (2), $\sigma_g(2p)$ (2), $\pi_u(2p)$ (4). Total bonding electrons = $8$.
Antibonding orbitals: $\sigma_u^*(2s)$ (2), $\pi_g^*(2p)$ ($k$).

$$BO = \frac{N_b - N_a}{2} = \frac{8 - (2 + k)}{2} = \frac{6 - k}{2}$$

1. **$\text{O}_2^+$** ($k = 1$):
   $$BO = \frac{8 - 3}{2} = \frac{5}{2} = \mathbf{2.5}$$
2. **$\text{O}_2$** ($k = 2$):
   $$BO = \frac{8 - 4}{2} = \frac{4}{2} = \mathbf{2.0}$$
3. **$\text{O}_2^-$** ($k = 3$):
   $$BO = \frac{8 - 5}{2} = \frac{3}{2} = \mathbf{1.5}$$
4. **$\text{O}_2^{2-}$** ($k = 4$):
   $$BO = \frac{8 - 6}{2} = \frac{2}{2} = \mathbf{1.0}$$

---

### Part 3: Unpaired Electrons and Magnetic Moments
1. **$\text{O}_2^+$**: $1$ electron in $\pi_g^*(2p)$ ($n = 1$).
   $$\mu_s = \sqrt{1(1+2)} = \sqrt{3} \approx \mathbf{1.73\text{ }\mu_B} \quad \text{(Paramagnetic)}$$
2. **$\text{O}_2$**: $2$ electrons in degenerate $\pi_g^*(2p_x)^1 \pi_g^*(2p_y)^1$ with parallel spins by Hund's rule ($n = 2$).
   $$\mu_s = \sqrt{2(2+2)} = \sqrt{8} \approx \mathbf{2.83\text{ }\mu_B} \quad \text{(Paramagnetic)}$$
3. **$\text{O}_2^-$**: $3$ electrons in $\pi_g^*(2p)$ leaves $1$ unpaired electron ($n = 1$).
   $$\mu_s = \sqrt{1(3)} = \sqrt{3} \approx \mathbf{1.73\text{ }\mu_B} \quad \text{(Paramagnetic)}$$
4. **$\text{O}_2^{2-}$**: $4$ electrons completely fill $\pi_g^*(2p_x)^2 \pi_g^*(2p_y)^2$ ($n = 0$).
   $$\mu_s = \mathbf{0\text{ }\mu_B} \quad \text{(Diamagnetic)}$$

---

### Part 4: Comparative Physical Properties Ranking
By the fundamental inverse relationship: $\text{Bond Order } \uparrow \implies \text{Bond Length } \downarrow \implies \text{Bond Enthalpy } \uparrow \implies \text{Vibrational Frequency } \uparrow$.

| Property | Monotonic Trend Sequence | Experimental Values |
| :--- | :--- | :--- |
| **Bond Length ($d_0$)** | $\mathbf{\text{O}_2^+ < \text{O}_2 < \text{O}_2^- < \text{O}_2^{2-}}$ | $112\text{ pm} < 121\text{ pm} < 133\text{ pm} < 149\text{ pm}$ |
| **Bond Dissociation Enthalpy ($D_0$)** | $\mathbf{\text{O}_2^{2-} < \text{O}_2^- < \text{O}_2 < \text{O}_2^+}$ | $210 < 395 < 498 < 623\text{ kJ}\cdot\text{mol}^{-1}$ |
| **Stretching Frequency ($\tilde{\nu}$)** | $\mathbf{\text{O}_2^{2-} < \text{O}_2^- < \text{O}_2 < \text{O}_2^+}$ | $790 < 1108 < 1556 < 1876\text{ cm}^{-1}$ |"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 6.2: Quantitative Molecular Orbital Analysis of Carbon Monoxide vs Dinitrogen",
                "statement": r"""Dinitrogen ($\text{N}_2$) and carbon monoxide ($\text{CO}$) are isoelectronic diatomic molecules sharing identical formal bond orders of $3.0$.
1. Explain using valence orbital ionization energies why the highest occupied molecular orbital (HOMO, $3\sigma$) of $CO$ is predominantly centered on the carbon atom rather than oxygen, despite oxygen possessing a vastly higher Pauling electronegativity.
2. High-resolution Ultraviolet Photoelectron Spectroscopy (UPS) of gaseous $CO$ exhibits three distinct ionization bands corresponding to electron ejection from:
   - Band 1: $14.0\text{ eV}$
   - Band 2: $16.9\text{ eV}$
   - Band 3: $19.7\text{ eV}$
   Assign these experimental ionization energies to the $3\sigma$ (HOMO), $1\pi$, and $2\sigma$ molecular orbitals.
3. Upon reacting with zero-valent transition metals to form metal hexacarbonyls $\text{M}(\text{CO})_6$, the experimental $\text{C}-\text{O}$ infrared stretching frequency decreases from $2143\text{ cm}^{-1}$ in free $CO$ to $\sim 1980\text{ cm}^{-1}$ in $\text{Cr}(\text{CO})_6$. Provide a complete quantum mechanical derivation explaining why this frequency reduction occurs via the Dewar-Chatt-Duncanson model.""",
                "solution": r"""### Part 1: Asymmetry of the $3\sigma$ HOMO Wavefunction
The valence orbital ionization energies (VOIEs) for carbon and oxygen are:
- Carbon: $\alpha_{2s} = -19.4\text{ eV}$, $\alpha_{2p} = -10.7\text{ eV}$
- Oxygen: $\alpha_{2s} = -32.4\text{ eV}$, $\alpha_{2p} = -15.9\text{ eV}$

In the $C_{\infty v}$ point group of $CO$:
1. The oxygen $2s$ orbital ($-32.4\text{ eV}$) is so deeply bound that it behaves predominantly as a core non-bonding lone pair ($1\sigma$).
2. The carbon $2s$ orbital ($-19.4\text{ eV}$) has almost identical energy to the oxygen $2p_z$ orbital ($-15.9\text{ eV}$). They interact strongly to form the bonding $2\sigma$ orbital.
3. The $3\sigma$ orbital is formed from the out-of-phase combination of carbon $2s$ and oxygen $2p_z$, mixed with carbon $2p_z$:
   $$\psi(3\sigma) \approx c_{\text{C}, 2s} \phi_{\text{C}}(2s) + c_{\text{C}, 2p_z} \phi_{\text{C}}(2p_z) - c_{\text{O}, 2p_z} \phi_{\text{O}}(2p_z)$$
4. Because the carbon $2p_z$ atomic orbital lies closest in energy to the $3\sigma$ state ($-10.7\text{ eV}$ vs $\sim -14.0\text{ eV}$), perturbation theory dictates that the coefficient $c_{\text{C}}$ dominates:
   $$|c_{\text{C}}|^2 \approx 0.80 \quad \text{and} \quad |c_{\text{O}}|^2 \approx 0.20$$
   Thus, the $3\sigma$ HOMO is heavily polarized toward carbon, with its electron cloud projecting outward as a stereochemically active carbon lone pair.

---

### Part 2: Photoelectron Spectroscopy (UPS) Orbital Assignments
By Koopmans' Theorem, the experimental vertical ionization energy ($IE$) corresponds to the negative of the Hartree-Fock orbital energy: $IE_k \approx -\epsilon_k$.

From the calculated MO energy levels:
$$E(3\sigma) > E(1\pi) > E(2\sigma)$$
Therefore, the easiest electron to eject (lowest ionization energy) comes from the HOMO ($3\sigma$):
- **Band 1 ($14.0\text{ eV}$)**: Ejection from the **$3\sigma$ orbital (HOMO)**.
  - Spectroscopic shape: Sharp, narrow peak with minimal vibrational progression, confirming that the $3\sigma$ orbital is weakly non-bonding.
- **Band 2 ($16.9\text{ eV}$)**: Ejection from the **$1\pi$ orbital**.
  - Spectroscopic shape: Broad band with extensive vibrational progression ($\tilde{\nu}$ spacing contracts), confirming that $1\pi$ is a strongly bonding orbital.
- **Band 3 ($19.7\text{ eV}$)**: Ejection from the **$2\sigma$ orbital**.
  - Strongly bonding $\sigma$ interaction between carbon $2s$ and oxygen $2p$.

---

### Part 3: Dewar-Chatt-Duncanson Model & Infrared Frequency Red-Shift
When $CO$ binds to chromium in $\text{Cr}(\text{CO})_6$:
1. **Forward $\sigma$-Donation**: The carbon-localized $3\sigma$ HOMO donates electron density into the empty $d_{z^2}$ or $e_g$ orbital of the chromium atom:
   $$\text{Cr} \xleftarrow{\sigma} \text{CO}$$
   Because $3\sigma$ is weakly antibonding/non-bonding, removing electron density from $3\sigma$ actually slightly strengthens the $\text{C}-\text{O}$ framework.
2. **Reverse $\pi$-Backbonding**: The occupied $t_{2g}$ $d$-orbitals of chromium ($d_{xy}, d_{xz}, d_{yz}$, containing 6 electrons in $d^6$ low-spin $\text{Cr}^0$) possess identical symmetry to the empty $2\pi^*$ LUMO of $CO$. Chromium back-donates electron density into the $2\pi^*$ LUMO:
   $$\text{Cr}(t_{2g}) \xrightarrow{\pi} \text{CO}(2\pi^*)$$
3. **Weakening of the $\text{C}-\text{O}$ Bond**:
   - The $2\pi^*$ orbital is strictly **antibonding** with respect to the $\text{C}-\text{O}$ axis.
   - Populating $2\pi^*$ reduces the effective $\text{C}-\text{O}$ bond order from $3.0$ toward $2.6$.
   - Harmonic vibrational frequency is related to force constant $k$ and reduced mass $\mu$ by:
     $$\tilde{\nu} = \frac{1}{2\pi c} \sqrt{\frac{k}{\mu}}$$
   - As bond order drops, the force constant $k$ decreases from $1900\text{ N/m}$ to $\sim 1600\text{ N/m}$.
   - Consequently, the stretching frequency plummets from $2143\text{ cm}^{-1}$ in free $CO$ down to $\mathbf{1980\text{ cm}^{-1}}$ in $\text{Cr}(\text{CO})_6$."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 6.3: Analytic Solution of the $H_2^+$ Secular Equation with Spatial Overlap",
                "statement": r"""Consider the hydrogen molecule ion, $\text{H}_2^+$, consisting of two protons $A$ and $B$ separated by internuclear distance $R$, and a single electron.
Let the molecular orbital trial wavefunction be expressed as a linear combination of two identical normalized $1s$ atomic orbitals:
$$\psi = c_A \phi_A + c_B \phi_B$$
Given:
- Coulomb integrals: $H_{AA} = H_{BB} = \alpha$
- Resonance integral: $H_{AB} = H_{BA} = \beta$
- Overlap integral: $S_{AB} = S_{BA} = S \quad (0 < S < 1)$

1. Formulate the Rayleigh-Ritz secular equation and solve analytically for both energy eigenvalues ($E_+$ and $E_-$).
2. Determine the normalized eigenvector coefficients $(c_A, c_B)$ for both states.
3. Given the explicit quantum mechanical expressions for the integrals as a function of internuclear distance $R$ (in atomic units, $a_0 = 1$):
   $$S(R) = e^{-R} \left( 1 + R + \frac{R^2}{3} \right)$$
   $$\alpha(R) = E_{1s} + \frac{1}{R} - \langle \phi_A | \frac{1}{r_B} | \phi_A \rangle = -\frac{1}{2} + \frac{1}{R} - \left[ \frac{1}{R} - e^{-2R}\left(1 + \frac{1}{R}\right) \right]$$
   $$\beta(R) = E_{1s} S + \frac{S}{R} - \langle \phi_A | \frac{1}{r_A} | \phi_B \rangle = -\frac{1}{2}S + \frac{S}{R} - e^{-R}(1 + R)$$
   Prove analytically that the antibonding state $E_-$ is strictly unbound for all $R > 0$, while the bonding state $E_+$ possesses a true global potential minimum.""",
                "solution": r"""### Part 1: Secular Determinant and Analytical Eigenvalues
The Rayleigh-Ritz variational condition $\frac{\partial E}{\partial c_A} = 0$ and $\frac{\partial E}{\partial c_B} = 0$ yields the secular matrix:
$$\begin{pmatrix} \alpha - E & \beta - E S \\ \beta - E S & \alpha - E \end{pmatrix} \begin{pmatrix} c_A \\ c_B \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

Setting the determinant to zero:
$$(\alpha - E)^2 - (\beta - E S)^2 = 0$$
Factoring as a difference of squares:
$$[(\alpha - E) - (\beta - E S)] [(\alpha - E) + (\beta - E S)] = 0$$

#### Case 1: Bonding Eigenvalue ($E_+$):
$$(\alpha - E_+) + (\beta - E_+ S) = 0 \implies (\alpha + \beta) = E_+ (1 + S)$$
$$\mathbf{E_+ = \frac{\alpha + \beta}{1 + S}}$$

#### Case 2: Antibonding Eigenvalue ($E_-$):
$$(\alpha - E_-) - (\beta - E_- S) = 0 \implies (\alpha - \beta) = E_- (1 - S)$$
$$\mathbf{E_- = \frac{\alpha - \beta}{1 - S}}$$

---

### Part 2: Normalization and Eigenvector Coefficients
Substitute $E_+$ back into the first secular equation:
$$(\alpha - E_+) c_A + (\beta - E_+ S) c_B = 0$$
Since $\alpha - E_+ = -(\beta - E_+ S)$:
$$-(\beta - E_+ S) c_A + (\beta - E_+ S) c_B = 0 \implies c_A = c_B$$

Normalizing the wavefunction $\psi_+ = c_A (\phi_A + \phi_B)$:
$$\langle \psi_+ | \psi_+ \rangle = c_A^2 \left[ \langle \phi_A|\phi_A \rangle + \langle \phi_B|\phi_B \rangle + 2\langle \phi_A|\phi_B \rangle \right] = 1$$
$$c_A^2 [1 + 1 + 2S] = 1 \implies c_A = \frac{1}{\sqrt{2(1 + S)}}$$
$$\mathbf{\psi_+ = \frac{1}{\sqrt{2(1 + S)}} (\phi_A + \phi_B)}$$

Similarly, for the antibonding state $E_-$, substituting yields $c_A = -c_B$:
$$\mathbf{\psi_- = \frac{1}{\sqrt{2(1 - S)}} (\phi_A - \phi_B)}$$

---

### Part 3: Analytical Potential Energy Curves and Bound State Proof
The electronic energy includes the internuclear proton-proton repulsion $\frac{1}{R}$.
Let us evaluate the total molecular potential energy curves relative to the separated atom limit ($\text{H}(1s) + \text{H}^+$, where $E_\infty = E_{1s} = -\frac{1}{2}\text{ Hartree}$):
$$\Delta E_\pm(R) = E_\pm(R) - E_{1s}$$

#### 1. Evaluation of Coulomb Integral:
$$\alpha(R) = E_{1s} + e^{-2R}\left(1 + \frac{1}{R}\right) = E_{1s} + j(R)$$
where $j(R) = e^{-2R}\left(1 + \frac{1}{R}\right) > 0$ represents the classical attractive interaction between the proton and electron cloud plus nuclear repulsion.

#### 2. Evaluation of Resonance Integral:
$$\beta(R) = E_{1s} S(R) + \frac{S(R)}{R} - e^{-R}(1 + R) = E_{1s} S(R) + k(R)$$
where $k(R) = \frac{S(R)}{R} - e^{-R}(1 + R)$.
For all $R > 0$:
$$e^{-R}(1 + R) > \frac{S(R)}{R} \implies k(R) < 0$$

#### 3. Total Energy of Antibonding State ($E_-$):
$$E_-(R) = \frac{\alpha - \beta}{1 - S} = \frac{E_{1s}(1 - S) + j(R) - k(R)}{1 - S} = E_{1s} + \frac{j(R) - k(R)}{1 - S}$$
Since $j(R) > 0$ and $k(R) < 0$:
$$j(R) - k(R) = j(R) + |k(R)| > 0$$
Furthermore, $1 - S > 0$ for all finite $R$.
Therefore:
$$\Delta E_-(R) = \frac{j(R) - k(R)}{1 - S} > 0 \quad \mathbf{\text{for ALL } R > 0}$$
$$\mathbf{\frac{d \Delta E_-}{dR} < 0 \quad \text{monotonically}}$$
The antibonding state potential energy curve is strictly positive and repulsive at every internuclear distance $R$; it possesses zero local minima and is **unbound for all $R$**.

#### 4. Total Energy of Bonding State ($E_+$):
$$E_+(R) = \frac{\alpha + \beta}{1 + S} = E_{1s} + \frac{j(R) + k(R)}{1 + S}$$
At large $R$, $j(R) + k(R) \approx -R e^{-R} < 0$.
At very small $R \rightarrow 0$, nuclear repulsion dominates: $j(R) \sim \frac{1}{R} \rightarrow +\infty$.
Because $\Delta E_+(R)$ is positive at $R \rightarrow 0$, becomes negative at intermediate $R$, and approaches zero from below as $R \rightarrow \infty$, by the Extreme Value Theorem there must exist at least one point $R_0$ where:
$$\left. \frac{d\Delta E_+}{dR} \right|_{R = R_0} = 0 \quad \text{and} \quad \left. \frac{d^2\Delta E_+}{dR^2} \right|_{R = R_0} > 0$$
Evaluating numerically:
$$R_0 \approx 2.49\text{ a.u.} = 1.32\text{ \AA} = 132\text{ pm}$$
$$\Delta E_+(R_0) \approx -0.0648\text{ Hartree} = -1.76\text{ eV} = -170\text{ kJ}\cdot\text{mol}^{-1}$$
This proves analytically that the constructive interference in $\psi_+$ accumulates sufficient electron density between the two nuclei to overcome internuclear Coulombic repulsion, creating a thermodynamically stable chemical bond."""
            }
        ]
    }
'''

with open("build_inorg1_unit6.py", "w", encoding="utf-8") as f:
    f.write(content)

print("build_inorg1_unit6.py written successfully.")
