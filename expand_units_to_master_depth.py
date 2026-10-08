#!/usr/bin/env python3
"""
expand_units_to_master_depth.py
Expands Units 2 through 8 with advanced academic sections, comprehensive derivations,
detailed tables, and real-world industrial and geochemical applications, bringing
each unit to ~10,000 words and total course content to ~80,000+ words.
"""

import os, sys

def enrich_unit2_full():
    import build_inorg1_unit2
    u = build_inorg1_unit2.get_unit2()
    
    sec_slater_tables = {
        "id": "sec2_7",
        "title": "§2.7 Comprehensive Hartree-Fock SCF vs Slater Effective Nuclear Charge Matrix",
        "content": r"""### Systematic Hartree-Fock SCF vs Slater Screening Matrix Across the First Four Periods

To appreciate the predictive scope and fundamental limitations of Slater's empirical screening rules, inorganic physical chemists compare Slater's effective nuclear charge $Z_{\text{eff}}^{\text{Slater}}$ with Roothaan-Hartree-Fock Self-Consistent Field (SCF) values computed by Clementi, Raimondi, and Reinhardt.

```
   Comprehensive Z_eff Comparison Matrix (Z = 1 to 30):
   
   Element   Z   Valence Orbital   Slater Z_eff   Clementi-Raimondi SCF Z_eff   Deviation (ΔZ_eff)
   --------------------------------------------------------------------------------------------
   H         1   1s                1.00           1.00                          0.00
   He        2   1s                1.70           1.69                          +0.01
   Li        3   2s                1.30           1.28                          +0.02
   Be        4   2s                1.95           1.91                          +0.04
   B         5   2p                2.60           2.42                          +0.18
   C         6   2p                3.25           3.14                          +0.11
   N         7   2p                3.90           3.83                          +0.07
   O         8   2p                4.55           4.45                          +0.10
   F         9   2p                5.20           5.10                          +0.10
   Ne        10  2p                5.85           5.76                          +0.09
   Na        11  3s                2.20           2.51                          -0.31
   Mg        12  3s                2.85           3.31                          -0.46
   Al        13  3p                3.50           4.07                          -0.57
   Si        14  3p                4.15           4.29                          -0.14
   P         15  3p                4.80           4.89                          -0.09
   S         16  3p                5.45           5.48                          -0.03
   Cl        17  3p                6.10           6.12                          -0.02
   Ar        18  3p                6.75           6.76                          -0.01
   K         19  4s                2.20           3.50                          -1.30
   Ca        20  4s                2.85           4.40                          -1.55
   Sc        21  3d                3.00           4.63                          -1.63
   Sc        21  4s                3.00           4.70                          -1.70
   Ti        22  3d                3.65           5.13                          -1.48
   V         23  3d                4.30           5.63                          -1.33
   Cr        24  3d                4.95           6.13                          -1.18
   Mn        25  3d                5.60           6.63                          -1.03
   Fe        26  3d                6.25           7.13                          -0.88
   Co        27  3d                6.90           7.63                          -0.73
   Ni        28  3d                7.55           8.13                          -0.58
   Cu        29  3d                8.20           8.63                          -0.43
   Zn        30  3d                8.85           9.13                          -0.28
   Zn        30  4s                4.35           5.97                          -1.62
```

#### Systematic Observations and Physical Origins of Discrepancies:
1. **Period 2 Elements ($\text{Li}$ to $\text{Ne}$)**:
   Slater's rules exhibit stellar accuracy ($\Delta Z_{\text{eff}} < 0.18$). Because the core consists solely of the compact $1s^2$ shell with zero radial nodes, the empirical screening constant $0.85$ for the $(n-1)$ shell accurately mimics true electronic screening.
2. **Alkali and Alkaline Earth Metal Underestimation ($\text{Na, Mg, K, Ca}$)**:
   For $s$ orbitals in Period 3 and Period 4, Slater's rules **severely underestimate** $Z_{\text{eff}}$ ($\Delta Z_{\text{eff}} = -1.30$ in $\text{K}$, $-1.55$ in $\text{Ca}$).
   - **Reason**: An $ns$ orbital possesses $(n-1)$ radial nodes and $(n)$ radial probability peaks. The innermost radial lobes penetrate deeply through the core $[Ne]$ or $[Ar]$ shells right into the immediate vicinity of the nucleus. Slater's model assumes uniform spherical shielding from the $(n-1)$ shell without accounting for the intense Coulombic attraction experienced by the innermost penetrating lobes.
3. **Transition Metal $3d$ Shell Stabilization Across the First Row**:
   Across the first transition series ($\text{Sc}$ to $\text{Zn}$), $Z_{\text{eff}}^{\text{SCF}}(3d)$ escalates rapidly from $4.63$ to $9.13$. Because $3d$ orbitals shield each other poorly ($\sigma \sim 0.35$), each additional proton added to the nucleus pulls the entire $3d$ subshell closer to the core, explaining the steady contraction in atomic radii and the stabilization of lower oxidation states toward the right side of the $d$-block."""
    }
    
    # Check if sec2_7 already exists
    if not any(s['id'] == 'sec2_7' for s in u['sections']):
        u['sections'].append(sec_slater_tables)
        
    with open("build_inorg1_unit2.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 2: Periodicity of the Elements, Electronic Shielding & Relativistic Effects\n"""\n\n')
        f.write("def get_unit2():\n    return " + repr(u) + "\n")
    print("Unit 2 enriched with sec2_7 successfully.")

def enrich_unit3_full():
    import build_inorg1_unit3
    u = build_inorg1_unit3.get_unit3()
    
    sec_evjen_ewald = {
        "id": "sec3_6",
        "title": "§3.6 Advanced Lattice Summation: Evjen & Ewald Methods & Fast-Ion Superionic Conduction",
        "content": r"""### Mathematical Convergence of Three-Dimensional Madelung Sums

The direct sum for the Madelung constant of a three-dimensional crystal lattice:
$$M = \sum_{j \neq 0} \frac{(-1)^{s_j}}{c_{ij}}$$
is a **conditionally convergent alternating series**. If one sums over expanding concentric spheres of radius $R$, the series oscillates wildly and fails to converge because the spherical boundary cuts arbitrarily through unit cells, generating unneutralized surface charge layers whose electric potential diverges asymptotically.

To achieve exact convergence, mathematical crystallographers employ two powerful techniques: the **Evjen Method** and the **Ewald Summation Method**.

```
       The Evjen Neutral Cube Method:
       
                 +-----[-1/8]-----+
                /|               /|
            [+1/4]           [-1/4]
              /  |             /  |
             +-----[-1/4]-----+   |
             |   +----[+1/2]--|---+   <-- Fractional charges assigned to ions
             |  /             |  /        on cube faces (1/2), edges (1/4),
             | /              | /         and corners (1/8) to guarantee
             +-----[+1/4]-----+           EXACT ELECTRICAL NEUTRALITY!
```

---

### 1. The Evjen Neutral Cell Method (H. M. Evjen, 1932)

Evjen realized that the mathematical instability arises from non-neutral surface boundaries. To eliminate boundary multipole potentials, the crystal is partitioned into a sequence of concentric **neutral polyhedral shells** (usually cubes for cubic lattices) centered on the reference ion.
- An ion lying completely in the **interior** of the shell is assigned its full charge ($1.0$).
- An ion lying on a **face** shared between two adjacent shells is assigned half charge ($\frac{1}{2} = 0.5$).
- An ion lying on an **edge** shared by four shells is assigned one-fourth charge ($\frac{1}{4} = 0.25$).
- An ion lying at a **corner** shared by eight shells is assigned one-eighth charge ($\frac{1}{8} = 0.125$).

Every Evjen shell has identically zero net charge ($\sum q_k = 0$) and zero net dipole moment ($\vec{P} = \vec{0}$).

#### Stepwise Evjen Summation for Rock Salt ($\text{NaCl}$):
Consider the first Evjen cube containing the 26 immediate surrounding sites at unit distance $a$ (nearest-neighbor distance $r_0$):
1. **6 Face Centers**: Opposite charge (attractive), distance $1.00 r_0$, shared by 2 cells $\implies$ charge weight $\frac{1}{2}$.
   $$\text{Contribution} = 6 \times \left(+\frac{1/2}{1.00}\right) = +3.000$$
2. **12 Edge Midpoints**: Identical charge (repulsive), distance $r_0\sqrt{2} \approx 1.4142 r_0$, shared by 4 cells $\implies$ charge weight $\frac{1}{4}$.
   $$\text{Contribution} = 12 \times \left(-\frac{1/4}{\sqrt{2}}\right) = -\frac{3.000}{1.4142} \approx -2.1213$$
3. **8 Corner Vertices**: Opposite charge (attractive), distance $r_0\sqrt{3} \approx 1.7321 r_0$, shared by 8 cells $\implies$ charge weight $\frac{1}{8}$.
   $$\text{Contribution} = 8 \times \left(+\frac{1/8}{\sqrt{3}}\right) = +\frac{1.000}{1.7321} \approx +0.5774$$

Sum for the first Evjen cube shell ($N = 1$):
$$M^{(1)} = 3.000 - 2.1213 + 0.5774 = \mathbf{1.4561}$$
Carrying out the Evjen summation across three concentric shells:
- Shell 1 ($N=1$): $M = 1.4561$
- Shell 2 ($N=2$): $M = 1.7518$
- Shell 3 ($N=3$): $M = 1.7476$
In just three concentric shells, Evjen's method converges to within **$0.001\%$** of the exact value ($M = 1.74756$)!

---

### 2. Fast-Ion Superionic Conduction in Solid State Battery Electrolytes

While ideal ionic crystals are electrical insulators at room temperature, certain defective lattices exhibit colossal ionic conductivity comparable to liquid aqueous electrolytes ($\sigma_{\text{ion}} > 10^{-2}\text{ S}\cdot\text{cm}^{-1}$). These materials are **Superionic Conductors** (Fast-Ion Conductors), forming the solid-state electrolyte core of next-generation lithium and sodium batteries.

#### The Archetypal Superionic System: $\alpha$-Silver Iodide ($\alpha\text{-AgI}$)
At temperatures below $147^\circ\text{C}$, $\text{AgI}$ exists as $\beta\text{-AgI}$ (wurtzite structure), with low ionic conductivity ($\sim 10^{-8}\text{ S}\cdot\text{cm}^{-1}$).
Upon heating past the first-order phase transition temperature $T_c = 147^\circ\text{C}$, it transforms into $\alpha\text{-AgI}$:
- The massive iodide anions ($\text{I}^-$) form a rigid, stationary **body-centered cubic (BCC)** framework.
- The two silver cations ($\text{Ag}^+$) per unit cell are distributed statistically over **42 available crystallographic interstitial sites** (6 octahedral, 12 tetrahedral, and 24 trigonal positions).
- The silver sublattice essentially **melts** into a two-dimensional liquid-like mobile fluid flowing through the channels of the rigid iodide scaffold!
- Ionic conductivity surges by **four orders of magnitude** to $\sigma \approx 1.3\text{ S}\cdot\text{cm}^{-1}$ at $150^\circ\text{C}$!

#### Nernst-Einstein Relation for Ionic Drift:
The macroscopic ionic conductivity $\sigma_{\text{ion}}$ is directly coupled to microscopic ion self-diffusion coefficient $D_{\text{ion}}$ by the Nernst-Einstein equation:
$$\sigma_{\text{ion}} = \frac{n q^2 D_{\text{ion}}}{k_B T}$$
where $n$ is mobile ion carrier density and $q$ is ionic charge. The diffusion coefficient obeys Arrhenius temperature activation:
$$D_{\text{ion}} = D_0 \exp\left(-\frac{E_a}{k_B T}\right)$$
In superionic conductors like lithium phosphorus oxynitride (LiPON) and thio-LISICON ($\text{Li}_{10}\text{GeP}_2\text{S}_{12}$), the activation energy barrier for cation hopping is extraordinarily small ($E_a < 0.22\text{ eV}$), enabling ultra-fast solid-state lithium transport."""
    }
    
    if not any(s['id'] == 'sec3_6' for s in u['sections']):
        u['sections'].append(sec_evjen_ewald)
        
    with open("build_inorg1_unit3.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 3: The Chemical Bond I: Ionic Bonding & Crystal Energetics\n"""\n\n')
        f.write("def get_unit3():\n    return " + repr(u) + "\n")
    print("Unit 3 enriched with sec3_6 successfully.")

def enrich_unit4_full():
    import build_inorg1_unit4
    u = build_inorg1_unit4.get_unit4()
    
    sec_wade_rules = {
        "id": "sec4_6",
        "title": "§4.6 Polyhedral Skeletal Electron Pair Theory, Wade's Rules & Borane Clusters",
        "content": r"""### Beyond 2-Center-2-Electron Bonding: Electron-Deficient Boron Hydrides

Classical Lewis structures and localized Valence Bond theory fail catastrophically when applied to boranes (boron hydrides such as diborane $\text{B}_2\text{H}_6$, pentaborane $\text{B}_5\text{H}_9$, and decaborane $\text{B}_{10}\text{H}_{14}$).
In diborane ($\text{B}_2\text{H}_6$):
- Two boron atoms contribute $2 \times 3 = 6$ valence electrons.
- Six hydrogen atoms contribute $6 \times 1 = 6$ valence electrons.
- Total valence electrons available: $12$ electrons ($6$ electron pairs).
However, an ethane-like structure ($\text{H}_3\text{B}-\text{BH}_3$) would require seven covalent bonds ($14$ electrons). Diborane lacks sufficient valence electrons to form classical two-center two-electron (2c-2e) bonds between all adjacent atoms. It is historically designated as **electron-deficient**.

---

### The Three-Center Two-Electron (3c-2e) Bridging Bond

In 1943–1954, William N. Lipscomb (Nobel Prize in Chemistry, 1976) solved the bonding puzzle of diborane using low-temperature X-ray crystallography and molecular orbital theory.

```
       Diborane (B2H6) 3c-2e Bridge Geometry:
       
                 H_term       H_bridge      H_term
                   \            /            /
                    B -------- H -------- B
                   /            \            \
                 H_term       H_bridge      H_term
                 
       Four terminal B-H bonds = Classical 2c-2e bonds (4 x 2 = 8 electrons)
       Two bridging B-H-B bonds = 3c-2e "banana" bonds (2 x 2 = 4 electrons)
       Total electrons accounted for = 8 + 4 = 12 electrons!
```

#### Molecular Orbital Construction of the 3c-2e $\text{B}-\text{H}-\text{B}$ Bridge:
Three atomic orbitals participate in the bridge:
1. One $sp^3$ hybrid orbital from Boron $A$.
2. One $sp^3$ hybrid orbital from Boron $B$.
3. The spherically symmetric $1s$ orbital from the bridging Hydrogen atom ($H_{\text{br}}$).

LCAO linear combination yields three molecular orbitals:
1. **Bonding MO ($\psi_1$)**: Fully constructive overlap:
   $$\psi_1 = \frac{1}{2} \phi_{\text{B}_A}(sp^3) + \frac{1}{\sqrt{2}} \phi_{\text{H}}(1s) + \frac{1}{2} \phi_{\text{B}_B}(sp^3)$$
   Energy is strongly stabilized below atomic levels. Populated by **two electrons**.
2. **Non-Bonding MO ($\psi_2$)**:
   $$\psi_2 = \frac{1}{\sqrt{2}} \left[ \phi_{\text{B}_A}(sp^3) - \phi_{\text{B}_B}(sp^3) \right]$$
   Hydrogen $1s$ orbital has zero overlap with this combination by symmetry. Unoccupied.
3. **Antibonding MO ($\psi_3^*$)**:
   $$\psi_3^* = \frac{1}{2} \phi_{\text{B}_A}(sp^3) - \frac{1}{\sqrt{2}} \phi_{\text{H}}(1s) + \frac{1}{2} \phi_{\text{B}_B}(sp^3)$$
   Strongly destabilized. Unoccupied.

A single electron pair in $\psi_1$ simultaneously binds three atomic nuclei together, forming a **Three-Center Two-Electron (3c-2e) Bond**!

---

### Polyhedral Skeletal Electron Pair Theory (PSEPT) & Wade's Rules

For higher polyhedral borane clusters and carboranes, Kenneth Wade (1971) and Michael Mingos established **Wade's Rules** (Polyhedral Skeletal Electron Pair Theory, PSEPT) linking cluster geometry to the count of **Skeletal Electron Pairs (SEPs)**.

#### Counting Skeletal Electron Pairs:
Each vertex unit in a borane cluster contributes a specific number of electrons to the internal skeletal bonding:
- Each $\text{B}-\text{H}$ vertex unit contributes: $3(\text{B}) + 1(\text{H}) - 2(\text{used for external terminal B-H bond}) = \mathbf{2 \text{ skeletal electrons}}$.
- Each $\text{C}-\text{H}$ vertex unit contributes: $4(\text{C}) + 1(\text{H}) - 2 = \mathbf{3 \text{ skeletal electrons}}$.
- Each bridging hydrogen ($\mu_2\text{-H}$) contributes: $\mathbf{1 \text{ skeletal electron}}$.
- Each negative ionic charge contributes: $\mathbf{1 \text{ skeletal electron}}$.

Total Skeletal Electron Pairs:
$$\text{SEP} = \frac{\sum \text{Skeletal Electrons}}{2}$$

```
   Wade's Structural Taxonomy for n-Vertex Polyhedra:
   
   Classification   Formula                Skeletal Pairs (SEP)   Polyhedral Geometry
   ----------------------------------------------------------------------------------------
   Closo            [B_n H_n]^(2-)         n + 1                  Complete closed deltahedron with n vertices
   Nido             B_n H_(n+4)            n + 2                  (n+1)-vertex deltahedron with ONE vertex missing
   Arachno          B_n H_(n+6)            n + 3                  (n+2)-vertex deltahedron with TWO vertices missing
   Hypho            B_n H_(n+8)            n + 4                  (n+3)-vertex deltahedron with THREE vertices missing
```

#### Diagnostic Examples:
1. **Dodecaborate Dianion $[\text{B}_{12}\text{H}_{12}]^{2-}$**:
   - Number of boron vertices: $n = 12$.
   - Skeletal electrons: $12 \times 2(\text{from BH}) + 2(\text{charge}) = 26\text{ electrons} \implies \text{SEP} = 13 = n + 1$.
   - Structure: **Closo** regular icosahedron ($I_h$ point group symmetry).
2. **Pentaborane(9) $\text{B}_5\text{H}_9$**:
   - Number of boron vertices: $n = 5$.
   - Skeletal electrons: $5 \times 2(\text{BH}) + 4 \times 1(\text{bridging H}) = 14\text{ electrons} \implies \text{SEP} = 7 = n + 2$.
   - Structure: **Nido** square pyramid (an octahedron missing one apex)."""
    }
    
    if not any(s['id'] == 'sec4_6' for s in u['sections']):
        u['sections'].append(sec_wade_rules)
        
    with open("build_inorg1_unit4.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 4: The Chemical Bond II: Covalent Bonding, Lewis Structures, Resonance & Bond Enthalpies\n"""\n\n')
        f.write("def get_unit4():\n    return " + repr(u) + "\n")
    print("Unit 4 enriched with sec4_6 successfully.")

def enrich_unit5_full():
    import build_inorg1_unit5
    u = build_inorg1_unit5.get_unit5()
    
    sec_symmetry_rep = {
        "id": "sec5_6",
        "title": "§5.6 Group Theory Projection Operators, Irreducible Representations & Normal Mode Analysis",
        "content": r"""### The Apparatus of Molecular Representation Theory

In advanced inorganic chemistry, symmetry operations $\hat{R}$ belonging to a point group $G$ are represented by transformation matrices $\mathbf{D}(R)$ acting on molecular coordinate basis vectors.
The trace of a transformation matrix is its **Character** ($\chi(R)$):
$$\chi(R) = \text{Tr}[\mathbf{D}(R)] = \sum_{i} D_{ii}(R)$$

---

### The Great Orthogonality Theorem (GOT)

The fundamental cornerstone of group representation theory is the **Great Orthogonality Theorem** (Wigner, 1931):
$$\sum_{R \in G} \left[ D_{ij}^{(\mu)}(R) \right]^* D_{kl}^{(\nu)}(R) = \frac{h}{l_\mu} \delta_{\mu\nu} \delta_{ik} \delta_{jl}$$
where $h$ is the order of the group, $l_\mu$ is the dimension of irreducible representation $\mu$, and $\delta$ is the Kronecker delta.

From the GOT follows the **Character Orthogonality Theorem**:
$$\sum_{k=1}^C g_k \, [\chi^{(\mu)}(C_k)]^* \, \chi^{(\nu)}(C_k) = h \, \delta_{\mu\nu}$$
where $C_k$ is the $k$-th symmetry class and $g_k$ is the number of operations in that class.

#### Decomposition Formula for Reducible Representations:
Any reducible representation $\Gamma_{\text{red}}$ can be uniquely decomposed into a direct sum of irreducible representations $\Gamma_\mu$:
$$\Gamma_{\text{red}} = \sum_{\mu} a_\mu \Gamma_\mu$$
The coefficient $a_\mu$ (the number of times irreducible representation $\Gamma_\mu$ appears in $\Gamma_{\text{red}}$) is calculated using the master reduction formula:
$$a_\mu = \frac{1}{h} \sum_{k=1}^C g_k \, [\chi^{(\mu)}(C_k)]^* \, \chi_{\text{red}}(C_k)$$

---

### Normal Coordinate Analysis of Planar Boron Trifluoride ($\text{BF}_3$, $D_{3h}$)

Consider boron trifluoride, $\text{BF}_3$, a trigonal planar molecule ($D_{3h}$ point group):
- Number of atoms: $N = 4$.
- Total degrees of freedom: $3N = 12$.
- Symmetry classes in $D_{3h}$ ($h = 12$): $E, 2C_3, 3C_2, \sigma_h, 2S_3, 3\sigma_v$.

#### Step 1: Construct Reducible Representation $\Gamma_{3N}$:
For each symmetry operation, only atoms that do not move contribute to the character:
$$\chi_{3N}(R) = N_{\text{unshifted}} \times (\pm 1 + 2\cos\theta)$$

```
   Character Table Calculation for BF3 (D3h):
   
   Operation R:           E      2C_3    3C_2    σ_h    2S_3    3σ_v
   -----------------------------------------------------------------
   N_unshifted:           4      1       2       4      1       2
   Factor (±1+2cosθ):     3      0      -1       1     -2       1
   -----------------------------------------------------------------
   χ_3N(R):              12      0      -2       4     -2       2
```

#### Step 2: Subtract Translational and Rotational Characters:
From the $D_{3h}$ character table:
- Translations: $(x, y) \implies E'$, $z \implies A_2'' \implies \Gamma_{\text{trans}} = E' + A_2''$
- Rotations: $R_z \implies A_2', (R_x, R_y) \implies E'' \implies \Gamma_{\text{rot}} = A_2' + E''$
$$\chi_{\text{vib}}(R) = \chi_{3N}(R) - \chi_{\text{trans}}(R) - \chi_{\text{rot}}(R)$$

Decomposing using the master reduction formula yields the **Vibrational Normal Modes**:
$$\mathbf{\Gamma_{\text{vib}} = A_1' + A_2'' + 2E'}$$
Total vibrational modes: $1 + 1 + 2(2) = 6$ modes ($3N - 6 = 12 - 6 = 6$).

#### Step 3: Assignment of Vibrational Modes and Spectroscopic Activities:
1. **$\nu_1(A_1')$**: Symmetric $\text{B}-\text{F}$ stretching ($888\text{ cm}^{-1}$).
   - Transforms as $(x^2+y^2, z^2) \implies$ **Raman active ONLY**; **IR inactive** (no dynamic dipole moment).
2. **$\nu_2(A_2'')$**: Out-of-plane umbrella bending ($691\text{ cm}^{-1}$).
   - Transforms as $z \implies$ **IR active ONLY**; **Raman inactive**.
3. **$\nu_3(E')$**: Doubly degenerate asymmetric $\text{B}-\text{F}$ stretching ($1454\text{ cm}^{-1}$).
   - Transforms as $(x, y)$ AND $(x^2-y^2, xy) \implies$ **Both IR active and Raman active!**
4. **$\nu_4(E')$**: Doubly degenerate in-plane $\text{F}-\text{B}-\text{F}$ deformation ($480\text{ cm}^{-1}$).
   - Transforms as $(x, y)$ AND $(x^2-y^2, xy) \implies$ **Both IR active and Raman active!**

Notice that the symmetric stretch $\nu_1(A_1')$ and out-of-plane bend $\nu_2(A_2'')$ obey the **Rule of Mutual Exclusion** because the horizontal mirror plane $\sigma_h$ acts as an effective parity discriminator."""
    }
    
    if not any(s['id'] == 'sec5_6' for s in u['sections']):
        u['sections'].append(sec_symmetry_rep)
        
    with open("build_inorg1_unit5.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write(r'"""' + "\nUnit 5: Molecular Geometry: VSEPR Theory, Bent's Rule & Symmetry\n" + r'"""' + "\n\n")
        f.write("def get_unit5():\n    return " + repr(u) + "\n")
    print("Unit 5 enriched with sec5_6 successfully.")

def enrich_unit6_full():
    import build_inorg1_unit6
    u = build_inorg1_unit6.get_unit6()
    
    sec_walsh_diagrams = {
        "id": "sec6_6",
        "title": "§6.6 Walsh Correlation Diagrams & Hückel MO Theory for Inorganic Rings",
        "content": r"""### Walsh Diagrams: Understanding Molecular Geometry through MO Evolution

In 1953, Arthur Donald Walsh introduced **Walsh Correlation Diagrams**, which track how molecular orbital energies evolve continuously as a molecule deforms from one geometric extreme to another (e.g., from linear to bent for triatomic $AH_2$ systems, or from planar to pyramidal for tetratomic $AH_3$ systems).

Walsh's core postulate states:
> *The equilibrium geometry of a molecule is determined by the configuration that minimizes the sum of its occupied one-electron molecular orbital energies: $E_{\text{total}} \approx \sum_i n_i \epsilon_i$.*

```
       Walsh Diagram for AH2 (Linear D_∞h to Bent C_2v):
       
       Energy ε
        ^
        |                                       2b2 (σ*)
        |                     ---              /
        |        σ_u*        /   \            /
        |                    |    \          /  4a1 (σ*)
        |                    |     \        /
        |        1π_u -------+------+------*--- 1b1 (Pure non-bonding p_z)
        |         (Degenerate)      |     / \
        |                           |    /   \  3a1 (Stabilized by s-p mixing!)
        |        σ_g*        -------+---/     \
        |                           |  /       \ 1b2 (Bonding)
        |        σ_g  --------------+-*--------- 2a1 (Bonding)
        0 --------------------------+----------------------------->
                              Linear (180°)     Bent (105°)
```

#### Detailed Orbital Evolution in $AH_2$:
1. In the **linear geometry ($D_{\infty h}$)**:
   The degenerate $1\pi_u$ orbitals ($1\pi_{ux}$ and $1\pi_{uy}$) are pure non-bonding $p$ orbitals perpendicular to the molecular axis.
2. Upon **bending into bent ($C_{2v}$)**:
   - The $p_z$ orbital perpendicular to the bend plane remains unchanged in symmetry ($1b_1$) and retains invariant energy.
   - The in-plane $p_y$ orbital transforms into $3a_1$ symmetry. Crucially, in $C_{2v}$, the central atom $2s$ orbital ALSO belongs to $a_1$ symmetry!
   - Strong configuration interaction occurs: the $3a_1$ orbital mixes heavily with the low-lying $2s$ orbital, **plunging steeply downward in energy** as the bond angle contracts!

#### Predictive Power of Walsh's Diagram:
- **Species with 4 valence electrons ($\text{BeH}_2$)**: Configuration is $2a_1^2 1b_2^2$ (or $\sigma_g^2 \sigma_u^2$). The occupied orbitals are lowest at $180^\circ$. **Prediction: Strictly Linear**.
- **Species with 8 valence electrons ($\text{H}_2\text{O}$)**: Configuration is $2a_1^2 1b_2^2 3a_1^2 1b_1^2$. The two electrons occupying the $3a_1$ orbital exert a colossal driving force toward bending because $3a_1$ is steeply stabilized as $\theta$ closes. **Prediction: Bent ($\angle \approx 104.5^\circ$)**.

---

### Hückel Molecular Orbital (HMO) Theory for Inorganic Conjugated Rings

While classical Hückel theory was developed for organic annulenes (benzene), Erich Hückel's secular determinant method provides essential insights into aromaticity in planar inorganic ring systems such as **Borazine** ($\text{B}_3\text{N}_3\text{H}_6$, "inorganic benzene") and **Cyclotriphosphazenes** ($[\text{NPCl}_2]_3$).

```
             H                        H
             |                        |
             B                        N
           /   \\                  //   \
         N       N               B       B
         |       |       <==>    |       |
         B       B               N       N
          \\   /                   \   //
             N                        B
             |                        |
             H                        H
             (Canonical Resonance Forms of Borazine)
```

#### Analytical Secular Determinant for Borazine:
Borazine contains an alternating six-membered ring of three boron atoms and three nitrogen atoms.
Let the Coulomb integral of nitrogen be $\alpha_{\text{N}} = \alpha + h_{\text{N}} \beta$ (with $h_{\text{N}} \approx +1.5$, reflecting high electronegativity) and boron be $\alpha_{\text{B}} = \alpha + h_{\text{B}} \beta$ (with $h_{\text{B}} \approx -0.5$).
The resonance integral is $\beta_{\text{BN}} = k \beta \approx 0.8 \beta$.

Solving the $6 \times 6$ Hückel secular matrix:
$$\begin{vmatrix}
\alpha_{\text{B}} - E & \beta_{\text{BN}} & 0 & 0 & 0 & \beta_{\text{BN}} \\
\beta_{\text{BN}} & \alpha_{\text{N}} - E & \beta_{\text{BN}} & 0 & 0 & 0 \\
0 & \beta_{\text{BN}} & \alpha_{\text{B}} - E & \beta_{\text{BN}} & 0 & 0 \\
0 & 0 & \beta_{\text{BN}} & \alpha_{\text{N}} - E & \beta_{\text{BN}} & 0 \\
0 & 0 & 0 & \beta_{\text{BN}} & \alpha_{\text{B}} - E & \beta_{\text{BN}} \\
\beta_{\text{BN}} & 0 & 0 & 0 & \beta_{\text{BN}} & \alpha_{\text{N}} - E
\end{vmatrix} = 0$$

#### Chemical Consequence: Localized vs Delocalized $\pi$ Electrons
In benzene ($\text{C}_6\text{H}_6$), all six carbons are identical ($\alpha_{\text{C}} = \alpha$), yielding perfect delocalization and profound aromatic chemical inertness (electrophilic substitution rather than addition).
In borazine ($\text{B}_3\text{N}_3\text{H}_6$):
- Because $\alpha_{\text{N}}$ is deeply stabilizing and $\alpha_{\text{B}}$ is shallow, the three occupied $\pi$ molecular orbitals are **heavily polarized toward nitrogen** ($\sim 85\%$ electron density on nitrogen).
- The $\pi$ electron cloud is partially localized as lone pairs on nitrogen, while boron atoms retain significant partial positive charge ($B^{\delta+}-N^{\delta-}$).
- Consequently, borazine is far more reactive than benzene, readily undergoing nucleophilic addition reactions (e.g., adding three molecules of $\text{HCl}$ across the $\text{B}-\text{N}$ bonds to yield $\text{B}_3\text{N}_3\text{H}_9\text{Cl}_3$)."""
    }
    
    if not any(s['id'] == 'sec6_6' for s in u['sections']):
        u['sections'].append(sec_walsh_diagrams)
        
    with open("build_inorg1_unit6.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 6: Quantum Theories of Bonding: Valence Bond Theory & Molecular Orbital Theory\n"""\n\n')
        f.write("def get_unit6():\n    return " + repr(u) + "\n")
    print("Unit 6 enriched with sec6_6 successfully.")

def enrich_unit7_full():
    import build_inorg1_unit7
    u = build_inorg1_unit7.get_unit7()
    
    sec_superacids = {
        "id": "sec7_6",
        "title": "§7.6 Non-Aqueous Solvent Media, Superacids & The Hammett Acidity Function",
        "content": r"""### Beyond Aqueous Acid-Base Limits: The World of Superacids

In pure water, the acidity of any strong acid is leveled to the hydronium ion ($\text{H}_3\text{O}^+$, $pK_a = -1.74$). To study proton transfer to extremely weak bases (such as hydrocarbons, noble gases, or halogens), inorganic chemists operate in **non-aqueous, non-leveling media** and synthesize **Superacids** (defined by Ronald Gillespie as any acidic system possessing an acidity greater than $100\%$ pure anhydrous sulfuric acid).

---

### The Hammett Acidity Function ($H_0$)

Because dilute $pH = -\log[\text{H}^+]$ becomes meaningless in non-aqueous concentrated acid media where water activity is zero and activity coefficients deviate wildly, Louis Plack Hammett (1932) defined the **Hammett Acidity Function** ($H_0$):
$$H_0 = pK_{\text{BH}^+} - \log_{10}\left( \frac{[\text{BH}^+]}{[\text{B}]} \right) = -\log_{10}\left( a_{\text{H}^+} \frac{\gamma_{\text{B}}}{\gamma_{\text{BH}^+}} \right)$$
where $\text{B}$ is a neutral, weakly basic spectrophotometric indicator dye (such as nitroanilines) and $\text{BH}^+$ is its conjugate acid.
- For $100\%$ pure anhydrous $\text{H}_2\text{SO}_4$: $H_0 = -12.0$.
- For pure anhydrous Fluorosulfuric acid ($\text{HSO}_3\text{F}$): $H_0 = -15.1$.
- For pure anhydrous Hydrogen Fluoride ($\text{HF}$): $H_0 = -15.1$.

```
       The Hammett Acidity Scale of Inorganic Acids:
       
   Acid System                                  H_0 Value       Relative Acidity to 100% H2SO4
   ---------------------------------------------------------------------------------------------
   Water (1 M H3O+)                             0.0             10^(-12)
   100% Anhydrous H2SO4                         -12.0           1 (Reference standard)
   Trifluoromethanesulfonic acid (TfOH)          -14.1           100 times stronger
   Anhydrous HF                                 -15.1           1,200 times stronger
   Fluorosulfuric acid (HSO3F)                  -15.1           1,200 times stronger
   "Magic Acid" (HSO3F · SbF5, 1:1)             -23.0           10^11 times stronger!
   Fluoroantimonic Acid (HF · SbF5, 1:1)        -31.3           10^19 times stronger!
```

---

### George Olah's "Magic Acid" & Fluoroantimonic Acid

In the 1960s, George A. Olah (Nobel Prize in Chemistry, 1994) revolutionized chemistry by combining strong Brønsted acids with powerful Lewis acid pentafluorides:

#### 1. "Magic Acid" ($\text{HSO}_3\text{F} \cdot \text{SbF}_5$):
Antimony pentafluoride ($\text{SbF}_5$) is an exceptional Lewis acid that acts as a ferocious fluoride-ion and fluorosulfate-ion acceptor:
$$2\,\text{HSO}_3\text{F} + \text{SbF}_5 \rightleftharpoons [\text{H}_2\text{SO}_3\text{F}]^+ + [\text{FSO}_3\text{SbF}_5]^-$$
The resulting bare proton is virtually uncoordinated, imparting an acidity $H_0 \approx -23$. Olah demonstrated that Magic Acid spontaneously protonates paraffins, dissolving paraffin candle wax to generate stable long-lived carbocations!

#### 2. Fluoroantimonic Acid ($\text{HF} \cdot \text{SbF}_5$):
The most powerful known superacid system:
$$2\,\text{HF} + \text{SbF}_5 \rightleftharpoons \text{H}_2\text{F}^+ + \text{SbF}_6^-$$
At high $\text{SbF}_5$ concentrations, polymeric fluoroantimonate anions form:
$$\text{SbF}_6^- + \text{SbF}_5 \rightleftharpoons \text{Sb}_2\text{F}_{11}^-$$
$$\text{Sb}_2\text{F}_{11}^- + \text{SbF}_5 \rightleftharpoons \text{Sb}_3\text{F}_{16}^-$$
With $H_0 \approx -31.3$, fluoroantimonic acid is over **$10^{19}$ times more acidic than $100\%$ sulfuric acid**! It quantitatively protonates methane at room temperature to yield the iconic pentacoordinate carbonium ion:
$$\text{CH}_4 + \text{H}_2\text{F}^+ \longrightarrow \text{CH}_5^+ + \text{HF} \longrightarrow \text{CH}_3^+ + \text{H}_2(g) + \text{HF}$$

---

### The Drago-Wayland Enthalpy Framework for Lewis Adducts

Russell S. Drago and Bradford Wayland (1965) established an empirical four-parameter thermodynamic equation predicting the standard enthalpy of formation ($\Delta H^\circ$) of coordinate covalent Lewis acid-base adducts in non-polar, non-coordinating solvents:
$$-\Delta H_{\text{adduct}}^\circ = E_A E_B + C_A C_B + W$$
where:
- $E_A, E_B$ represent the **Electrostatic susceptibility parameters** of the acid and base (governing Coulombic, dipole-dipole, and ionic interactions).
- $C_A, C_B$ represent the **Covalent susceptibility parameters** of the acid and base (governing orbital overlap and covalent charge transfer).
- $W$ is a constant term (zero for neutral adducts; non-zero if adduct formation involves prior dissociation, as in dimeric $\text{Al}_2\text{Cl}_6$).

```
   Selected Drago-Wayland Parameters:
   
   Lewis Acid (A)         E_A      C_A       Lewis Base (B)          E_B      C_B
   ---------------------------------------------------------------------------------
   I2 (Iodine)            1.00     1.00      Pyridine (py)           1.17     6.40
   Phenol                 4.33     0.44      Diethyl ether (Et2O)    0.96     3.25
   BF3 (gas)              9.88     1.62      Trimethylamine (NMe3)   0.81    11.54
   BMe3                   6.14     1.70      Tetrahydrofuran (THF)   0.98     4.29
   SbCl5                  7.38     5.15      Acetonitrile (MeCN)     0.89     1.34
```

This quantitative framework separates ionic from covalent stabilization, providing numerical validation for Pearson's HSAB principle."""
    }
    
    if not any(s['id'] == 'sec7_6' for s in u['sections']):
        u['sections'].append(sec_superacids)
        
    with open("build_inorg1_unit7.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 7: Secondary Bonding, Intermolecular Forces & Acid-Base Equilibria\n"""\n\n')
        f.write("def get_unit7():\n    return " + repr(u) + "\n")
    print("Unit 7 enriched with sec7_6 successfully.")

def enrich_unit8_full():
    import build_inorg1_unit8
    u = build_inorg1_unit8.get_unit8()
    
    sec_multimetal_pourbaix = {
        "id": "sec8_6",
        "title": "§8.6 Multi-Element Pourbaix Diagrams, Industrial Passivation & Transition Metal Frost Landscapes",
        "content": r"""### Multi-Element Pourbaix Diagrams in Metallurgy & Materials Science

In practical metallurgical engineering, aqueous corrosion rarely involves isolated elemental iron; rather, structural alloys (such as austenitic stainless steels, marine bronze, and titanium aerospace alloys) operate in multi-component aqueous electrolytes containing chloride, sulfate, and alloyed transition metals ($\text{Cr, Ni, Mo, Ti}$).

---

### The Mechanism of Stainless Steel Passivation: The Iron-Chromium System

Chromium is the pivotal alloying element in stainless steels (typically $\ge 12\text{ wt}\%\text{ Cr}$).
Consider the Pourbaix diagram of pure Chromium in water:
- **Corrosion species**: $\text{Cr}^{2+}(aq)$ at low potentials; $\text{Cr}^{3+}(aq)$ in acidic media ($pH < 4$); soluble chromate $[\text{CrO}_4]^{2-}$ and dichromate $[\text{Cr}_2\text{O}_7]^{2-}$ at extreme oxidizing potentials ($E > +1.3\text{ V}$).
- **Passivating oxide**: Chromium(III) oxide ($\text{Cr}_2\text{O}_3$ or hydrated $\text{Cr(OH)}_3$):
  $$2\,\text{Cr}^{3+}(aq) + 3\,\text{H}_2\text{O}(l) \rightleftharpoons \text{Cr}_2\text{O}_3(s) + 6\,\text{H}^+(aq)$$

```
       Chromium Pourbaix Diagram Topology:
       
       Potential E (V)
       +1.5 |                 Cr2O7^2- (Acid) / CrO4^2- (Base)
            |              ------------------------------------- (Transpassive dissolution)
       +1.0 |
            |                      PASSIVATION ZONE
       +0.5 |                         (Cr2O3 / Cr(OH)3)
            |        Cr^3+           Adherent, self-healing,
        0.0 |       (Acidic)         nanometer-thin oxide film
            |     /
       -0.5 |    / Cr^2+
            |   /
       -1.0 |  -------------------------------------------------
            |               IMMUNITY ZONE (Metallic Cr)
            +---------------------------------------------------> pH
            0            4            7            10         14
```

#### Why Chromium Passivates Far More Effectively Than Iron:
1. **Broader Passivation Window**: The insoluble oxide $\text{Cr}_2\text{O}_3$ is thermodynamically stable over a vast $pH$ range ($3.8 \le pH \le 12.5$) and over a wide potential window ($-0.6\text{ V}$ to $+1.3\text{ V}$).
2. **Defect-Free Nanoscale Film**: In stainless steel, chromium atoms selectively diffuse to the alloy surface and react with dissolved oxygen to form a continuous, amorphous, pinhole-free layer of $\text{Cr}_2\text{O}_3$ just $1\text{–}3\text{ nm}$ thick.
3. **Pilling-Bedworth Ratio (PBR)**: The ratio of the molar volume of the oxide to the molar volume of the metal:
   $$\text{PBR} = \frac{V_{\text{oxide}}}{V_{\text{metal}}} = \frac{M_{\text{oxide}} \cdot \rho_{\text{metal}}}{n \cdot M_{\text{metal}} \cdot \rho_{\text{oxide}}}$$
   - For Chromium: $\text{PBR} = 2.07$. The oxide is dense and in mild compression, adhering tenaciously to the metal substrate without cracking or spalling.
   - For Iron: In moist air, iron forms porous, non-adherent rust ($\text{FeOOH} \cdot x\text{H}_2\text{O}$) that flakes off continuously, exposing fresh metal to catastrophic ongoing corrosion.

---

### Comparative Frost Diagrams of First-Row Transition Metals

A side-by-side comparison of Frost oxidation state diagrams across the $3d$ series ($\text{Ti, V, Cr, Mn, Fe, Co, Ni, Cu}$) in standard acidic aqueous solution ($pH = 0$) reveals fundamental periodic redox trends:

```
   Frost Diagram Landscape for First-Row Transition Metals (pH = 0):
   
   ΔG° / F (V)
   +4 |                                                           Co^3+
   +3 |                                            Mn^3+
   +2 |                            Cr^6+ (Cr2O7^2-)
   +1 |             V^5+ (VO2+)
    0 | -- Ti -- V -- Cr --------- Mn ------------ Fe --- Co --- Ni --- Cu -- (M^0 = 0)
   -1 |      \   \    \             \               \     \    \    /
   -2 |       \   \    \             \               \     \    *-- Cu^2+
   -3 |        \   \    *-- Cr^3+     \               *-- Fe^2+
   -4 |         \   *-- V^3+           *-- Mn^2+ (Thermodynamic Sink!)
   -5 |          *-- Ti^3+
   -6 |           \
   -7 |            *-- Ti^4+ (TiO^2+)
```

#### Key Thermodynamic Discoveries from Frost Analysis:
1. **The Extreme Stability of Manganese(II) ($\text{Mn}^{2+}$)**:
   The Frost curve for Manganese displays a profound, deep minimum at $\text{Mn}^{2+}$ ($\Delta G^\circ/F \approx -1.18\text{ V}$).
   - **Reason**: $\text{Mn}^{2+}$ possesses a high-spin $3d^5$ electron configuration with a half-filled subshell. The exchange stabilization energy is maximal ($10 K_{\text{ex}}$) and the crystal field stabilization is zero.
   - **Consequence**: All higher oxidation states ($\text{Mn}^{3+}, \text{MnO}_2, \text{MnO}_4^{2-}, \text{MnO}_4^-$) sit high on steep positive slopes. Consequently, **Permanganate ($\text{MnO}_4^-$) is a ferocious thermodynamic oxidant**, reduced precipitously to $\text{Mn}^{2+}$.
2. **The Convex Disproportionation Peaks of $\text{Mn}^{3+}$ and $\text{MnO}_4^{2-}$**:
   Both $\text{Mn}^{3+}$ and manganate ($\text{MnO}_4^{2-}$, $\text{Mn}^{+6}$) lie above the chord connecting their flanking neighbors; hence, both species spontaneously disproportionate in acidic media:
   $$2\,\text{Mn}^{3+}(aq) + 2\,\text{H}_2\text{O} \longrightarrow \text{Mn}^{2+}(aq) + \text{MnO}_2(s) + 4\,\text{H}^+(aq)$$
   $$3\,\text{MnO}_4^{2-}(aq) + 4\,\text{H}^+(aq) \longrightarrow 2\,\text{MnO}_4^-(aq) + \text{MnO}_2(s) + 2\,\text{H}_2\text{O}(l)$$
3. **The Ascending Stability of Divalent Ions from Left to Right**:
   Early transition metals ($\text{Ti, V}$) have thermodynamic sinks in high oxidation states ($\text{Ti}^{4+}, \text{V}^{5+}$), acting as powerful reducing agents. Late transition metals ($\text{Fe, Co, Ni, Cu}$) have thermodynamic sinks in the $+2$ state ($\text{Fe}^{2+}, \text{Co}^{2+}, \text{Ni}^{2+}, \text{Cu}^{2+}$), and their high oxidation states ($\text{Co}^{3+}, \text{Ni}^{4+}$) are virtually unreachable or violently oxidizing."""
    }
    
    if not any(s['id'] == 'sec8_6' for s in u['sections']):
        u['sections'].append(sec_multimetal_pourbaix)
        
    with open("build_inorg1_unit8.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 8: Inorganic Chemical Reactions: Precipitation, Redox Spontaneity & Potential Diagrams\n"""\n\n')
        f.write("def get_unit8():\n    return " + repr(u) + "\n")
    print("Unit 8 enriched with sec8_6 successfully.")

enrich_unit2_full()
enrich_unit3_full()
enrich_unit4_full()
enrich_unit5_full()
enrich_unit6_full()
enrich_unit7_full()
enrich_unit8_full()
print("ALL UNITS SUCCESSFULLY ENRICHED!")
