#!/usr/bin/env python3
"""
add_remaining_p4.py
Adds Problem 4 to Units 2, 4, 5, 6, 7, and 8.
"""

import sys

def add_p4_unit2():
    import build_inorg1_unit2
    u = build_inorg1_unit2.get_unit2()
    p4 = {
        "tier": "Honors / Proof Challenge",
        "title": "Problem 2.4: Dirac Relativistic Orbital Splitting in Superheavy Elements (Flerovium & Oganesson)",
        "statement": r"""In superheavy elements ($Z > 100$), relativistic spin-orbit coupling splits the valence $p$ subshell into two non-equivalent subshells: $p_{1/2}$ (spherical Dirac spinor, $j=1/2$) and $p_{3/2}$ (four-lobed spinor, $j=3/2$).
For Flerovium ($\text{Fl}$, $Z = 114$) and Oganesson ($\text{Og}$, $Z = 118$):
1. Write the relativistic valence electron configurations using $p_{1/2}$ and $p_{3/2}$ subshell notations.
2. Given that Dirac-Fock calculations yield a massive $7p_{1/2}-7p_{3/2}$ spin-orbit energy gap of $\Delta E_{\text{SO}} \approx 3.2\text{ eV}$ in Flerovium, explain why Flerovium is predicted to be an extraordinarily unreactive, volatile quasi-noble metal (or noble gas-like liquid), behaving more like mercury or argon than lead.
3. In Oganesson ($Z = 118$), the relativistic expansion of the $7p_{3/2}$ subshell and intense spin-orbit coupling causes the valence shell electron density to undergo **Thomas-Fermi electron gas uniformization**. Explain why Oganesson is predicted to be a solid semiconductor at room temperature with high polarizability ($\alpha \approx 58\text{ a.u.}$), completely violating the classical noble gas periodic group trend.""",
        "solution": r"""### Part 1: Relativistic Valence Electron Configurations
In non-relativistic notation:
- Flerovium ($Z=114$): $[\text{Rn}] 5f^{14} 6d^{10} 7s^2 7p^2$
- Oganesson ($Z=118$): $[\text{Rn}] 5f^{14} 6d^{10} 7s^2 7p^6$

In relativistic $j-j$ coupling notation:
The $p$ subshell ($l=1$) splits into:
- $p_{1/2}$ subshell: holds $2(1/2) + 1 = 2$ electrons (spherically symmetric probability density, experiences direct relativistic contraction and deep energy stabilization).
- $p_{3/2}$ subshell: holds $2(3/2) + 1 = 4$ electrons (diffuse angular lobes, experiences indirect relativistic expansion and destabilization).

Therefore, the relativistic ground-state configurations are:
$$\mathbf{\text{Fl } (Z=114): [\text{Og'}] \, 7s_{1/2}^2 \, 7p_{1/2}^2}$$
$$\mathbf{\text{Og } (Z=118): [\text{Og'}] \, 7s_{1/2}^2 \, 7p_{1/2}^2 \, 7p_{3/2}^4}$$

---

### Part 2: Chemical Volatility and Quasi-Noble Gas Behavior of Flerovium
In classical Group 14 chemistry, lead ($\text{Pb}$, $Z=82$) forms stable divalent $\text{Pb(II)}$ compounds and tetravalent $\text{Pb(IV)}$ covalent species.
In Flerovium ($Z=114$):
1. **Colossal $7p_{1/2}-7p_{3/2}$ Energy Gap ($\Delta E_{\text{SO}} \approx 3.2\text{ eV} \approx 310\text{ kJ}\cdot\text{mol}^{-1}$)**:
   The two $7p_{1/2}$ electrons are pulled into a deeply bound, spherically symmetric closed subshell.
   Promoting an electron from $7p_{1/2}$ into $7p_{3/2}$ to achieve $sp^3$ hybridization requires over $3\text{ eV}$ of promotional energy—far more than can be recovered by forming covalent bonds.
2. **Inert Spherical Shell**:
   Both the $7s_{1/2}^2$ and $7p_{1/2}^2$ subshells are closed, spherically symmetric, and heavily contracted toward the nucleus.
3. **Adsorption Enthalpy and Boiling Point**:
   Gas-phase chromatography experiments at GSI Darmstadt and FLNR Dubna reveal that Flerovium has an extremely low adsorption enthalpy on gold surfaces ($\Delta H_{\text{ads}} \approx -34\text{ kJ}\cdot\text{mol}^{-1}$), comparable to noble gases ($\text{Rn}$) and volatile mercury!
   Flerovium is predicted to be a volatile liquid or gas at room temperature ($T_b \approx -60^\circ\text{C}$ to $+10^\circ\text{C}$), completely breaking the Group 14 metallic trend.

---

### Part 3: The Thomas-Fermi Electron Smearing of Oganesson
In classical noble gases ($\text{He}$ through $\text{Rn}$), closed $p^6$ valence octets possess large HOMO-LUMO bandgaps ($\Delta E_{\text{gap}} > 10\text{ eV}$), negligible polarizabilities, and room-temperature gaseous states with weak van der Waals dispersion.
In Oganesson ($Z=118$):
1. **Severe Indirect Relativistic Expansion of $7p_{3/2}$**:
   The four $7p_{3/2}$ electrons are pushed far out into the periphery of the atom, held loosely by a weakened effective nuclear charge.
2. **Extreme Electronic Polarizability**:
   Calculated dipole polarizability surges to $\alpha \approx 58\text{ a.u.}$ ($\approx 8.6 \times 10^{-30}\text{ m}^3$), more than double that of Radon ($\alpha \approx 33\text{ a.u.}$).
3. **Electron Gas Smearing (Shell Structure Collapse)**:
   Relativistic electron localization function (ELF) calculations by Jerabek, Schwerdtfeger, and Nazarewicz (2018) reveal that the angular node barriers between the $7s, 7p_{1/2}, 7p_{3/2},$ and $6d$ subshells completely dissolve. The valence electrons behave as a **continuous, uniform Fermi gas of electrons** without distinct shells!
4. **Solid Semiconductor State**:
   Due to enormous London dispersion forces ($\propto \alpha^2$), the cohesive energy in solid Oganesson is estimated at $\Delta H_{\text{sub}} \approx 25\text{ kJ}\cdot\text{mol}^{-1}$, with a predicted melting point of $T_m \approx 325\text{ K}$ ($52^\circ\text{C}$).
   **Oganesson is a solid semiconductor at room temperature**, proving that extreme relativistic effects fundamentally override the classical periodic law!"""
    }
    if len(u['problems']) < 4:
        u['problems'].append(p4)
    with open("build_inorg1_unit2.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 2: Periodicity of the Elements, Electronic Shielding & Relativistic Effects\n"""\n\n')
        f.write("def get_unit2():\n    return " + repr(u) + "\n")
    print("Unit 2 Problem 2.4 added.")

def add_p4_unit4():
    import build_inorg1_unit4
    u = build_inorg1_unit4.get_unit4()
    p4 = {
        "tier": "Honors / Proof Challenge",
        "title": "Problem 4.4: Natural Resonance Theory (NRT) Weights & Bond Orders in Polyatomic Oxyanions",
        "statement": r"""For the sulfate anion ($\text{SO}_4^{2-}$) and perchlorate anion ($\text{ClO}_4^-$):
1. Formulate the two historical competing bonding models:
   - The classical hypervalent model invoking formal double bonds ($\text{S}=\text{O}$ and $\text{Cl}=\text{O}$) via $3d$-orbital participation.
   - The modern highly polar single-bond model ($\text{S}^{2+}-\text{O}^-$ and $\text{Cl}^{3+}-\text{O}^-$) stabilized by back-bonding hyperconjugation.
2. Given that high-level NBO Natural Resonance Theory (NRT) calculations yield an effective sulfur-oxygen bond order of $BO(\text{S}-\text{O}) \approx 1.37$ and chlorine-oxygen bond order of $BO(\text{Cl}-\text{O}) \approx 1.45$:
   - Calculate the percentage contribution of the dominant single-bonded Lewis resonance structures vs the double-bonded canonical structures.
   - Compute the net natural atomic charges on sulfur ($\delta_{\text{S}}$), chlorine ($\delta_{\text{Cl}}$), and oxygen ($\delta_{\text{O}}$).
3. Explain why the experimental $\text{S}-\text{O}$ bond length in $\text{SO}_4^{2-}$ ($149\text{ pm}$) is significantly shorter than a standard single bond ($170\text{ pm}$ in $\text{H}_2\text{N}-\text{SO}_3^-$) even though $3d$ orbital hybridization is negligible, citing negative hyperconjugation ($n_{\text{O}} \rightarrow \sigma_{\text{S-O}}^*$) and intense electrostatic Coulombic contraction.""",
        "solution": r"""### Part 1: Competing Bonding Models

#### 1. Historical Hypervalent Double-Bond Model:
To eliminate formal charge on sulfur ($FC = 0$), classical textbooks drew two $\text{S}=\text{O}$ double bonds and two $\text{S}-\text{O}^-$ single bonds (12 valence electrons on sulfur):
$$\sum FC = 0(\text{S}) + 2(0)(\text{O}) + 2(-1)(\text{O}^-) = -2$$
This model invoked $sp^3d^2$ hybridization of empty $3d$ orbitals.

#### 2. Modern Highly Polar Ionic/Covalent Model:
Because quantum chemistry proves that $3d$ orbitals in sulfur are too high in energy ($\Delta E(3p \rightarrow 3d) \approx 11\text{ eV}$) and too diffuse to form true covalent double bonds, the true Lewis ground state adheres strictly to the octet rule:
- Central sulfur forms four $\text{S}-\text{O}$ single bonds (8 valence electrons).
- Formal charges: Sulfur carries **$FC(\text{S}) = 6 - 4 = +2$**; each of the four oxygens carries **$FC(\text{O}) = 6 - 7 = -1$**.
$$\text{Formal Charge Representation: } [\text{S}^{2+}(\text{O}^-)_4]^{2-}$$

---

### Part 2: Natural Resonance Theory (NRT) Weights and Partial Charges

In Natural Resonance Theory (NRT):
$$BO(\text{S}-\text{O}) = \sum_k w_k b_k$$
Let $w_{\text{single}}$ be the total weight of canonical structures featuring single $\text{S}-\text{O}$ bonds ($b = 1$) and $w_{\text{double}}$ be the weight of structures featuring double $\text{S}=\text{O}$ bonds ($b = 2$):
$$w_{\text{single}} + w_{\text{double}} = 1.00$$
$$1.00 w_{\text{single}} + 2.00 w_{\text{double}} = 1.37$$
$$w_{\text{single}} + 2(1 - w_{\text{single}}) = 1.37 \implies 2 - w_{\text{single}} = 1.37$$
$$w_{\text{single}} = 2 - 1.37 = \mathbf{0.63 \quad (63\%)}$$
$$w_{\text{double}} = 1 - 0.63 = \mathbf{0.37 \quad (37\%)}$$

The single-bonded octet structure dominates by nearly **two-to-one**!

#### Net Partial Charges:
- For Sulfate ($\text{SO}_4^{2-}$):
  $$\delta_{\text{S}} \approx +2.15e, \quad \delta_{\text{O}} \approx -1.04e$$
  $$\text{Check: } +2.15 + 4(-1.04) = +2.15 - 4.16 = -2.01e \approx -2e = q_{\text{net}}$$
- For Perchlorate ($\text{ClO}_4^-$):
  $$\delta_{\text{Cl}} \approx +2.85e, \quad \delta_{\text{O}} \approx -0.96e$$
  $$\text{Check: } +2.85 + 4(-0.96) = +2.85 - 3.84 = -0.99e \approx -1e = q_{\text{net}}$$

---

### Part 3: Physical Explanation of Bond Shortening
The experimental $\text{S}-\text{O}$ bond length is only $149\text{ pm}$ (shortened by $21\text{ pm}$ from an unpolarized single bond). This dramatic contraction is driven by two synergistic quantum effects:
1. **Colossal Coulombic Electrostatic Attraction**:
   The central sulfur atom bears a massive positive partial charge ($\delta_{\text{S}} \approx +2.15$), while each coordinating oxygen bears a full negative charge ($\delta_{\text{O}} \approx -1.04$).
   The resulting Coulombic attraction $-\frac{(+2.15)(-1.04)e^2}{4\pi\varepsilon_0 r}$ pulls the oxygen atoms inward with immense force, compressing the bond length.
2. **Negative Hyperconjugation ($n_{\text{O}} \rightarrow \sigma_{\text{S-O}}^*$)**:
   Each oxygen holds filled $2p$ non-bonding lone pairs. These lone pairs donate electron density into the empty, low-lying $\sigma_{\text{S-O}}^*$ antibonding orbitals of the opposite $\text{S}-\text{O}$ bonds:
   $$n_{\text{O}_1} \longrightarrow \sigma_{\text{S-O}_2}^*$$
   Because this donation occurs across all four tetrahedrally arranged bonds, it creates significant partial $\pi$-bond character ($BO \approx 1.37$) without requiring high-energy $3d$ orbital involvement."""
    }
    if len(u['problems']) < 4:
        u['problems'].append(p4)
    with open("build_inorg1_unit4.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 4: The Chemical Bond II: Covalent Bonding, Lewis Structures, Resonance & Bond Enthalpies\n"""\n\n')
        f.write("def get_unit4():\n    return " + repr(u) + "\n")
    print("Unit 4 Problem 4.4 added.")

def add_p4_unit5():
    import build_inorg1_unit5
    u = build_inorg1_unit5.get_unit5()
    p4 = {
        "tier": "Honors / Proof Challenge",
        "title": "Problem 5.4: Complete Symmetry Factorization & Normal Vibrational Modes of Sulfur Hexafluoride",
        "statement": r"""Sulfur hexafluoride ($\text{SF}_6$) is an octahedral molecule belonging to the high-symmetry point group $O_h$ ($h = 48$):
- Number of atoms: $N = 7$.
- Total degrees of freedom: $3N = 21$.

1. Construct the reducible representation $\Gamma_{3N}$ across the ten symmetry classes of $O_h$:
   $$\hat{E}, 8\hat{C}_3, 6\hat{C}_2, 6\hat{C}_4, 3\hat{C}_2(=C_4^2), \hat{i}, 6\hat{S}_4, 8\hat{S}_6, 3\hat{\sigma}_h, 6\hat{\sigma}_d$$
2. Subtract translational ($\Gamma_{\text{trans}} = T_{1u}$) and rotational ($\Gamma_{\text{rot}} = T_{1g}$) degrees of freedom to obtain the vibrational reducible representation $\Gamma_{\text{vib}}$.
3. Using the $O_h$ character table and the master reduction formula, reduce $\Gamma_{\text{vib}}$ into its irreducible representations.
4. For all vibrational normal modes, state:
   - Degeneracy of the mode.
   - Physical description (symmetric stretch, asymmetric stretch, deformation, etc.).
   - Spectroscopic activity (Infrared active, Raman active, or Spectroscopically silent).
5. Verify the Rule of Mutual Exclusion for this centrosymmetric molecule.""",
        "solution": r"""### Part 1: Reducible Representation $\Gamma_{3N}$ for SF6 ($O_h$)
Order of the group: $h = 48$.
For each class, character is $\chi_{3N}(R) = N_{\text{unshifted}} \times (\pm 1 + 2\cos\theta)$:
- $\hat{E}$: 7 atoms unshifted $\implies \chi = 7 \times (1 + 2) = 21$.
- $8\hat{C}_3$: 1 atom unshifted (S) $\implies \chi = 1 \times (1 + 2\cos 120^\circ) = 1 \times 0 = 0$.
- $6\hat{C}_2$: 1 atom unshifted (S) $\implies \chi = 1 \times (1 + 2\cos 180^\circ) = 1 \times (-1) = -1$.
- $6\hat{C}_4$: 3 atoms unshifted (S and two trans F on rotation axis) $\implies \chi = 3 \times (1 + 2\cos 90^\circ) = 3 \times 1 = 3$.
- $3\hat{C}_2(=C_4^2)$: 3 atoms unshifted $\implies \chi = 3 \times (1 + 2\cos 180^\circ) = 3 \times (-1) = -3$.
- $\hat{i}$: 1 atom unshifted (S) $\implies \chi = 1 \times (-1 - 2) = -3$.
- $6\hat{S}_4$: 1 atom unshifted (S) $\implies \chi = 1 \times (-1 + 2\cos 90^\circ) = -1$.
- $8\hat{S}_6$: 1 atom unshifted (S) $\implies \chi = 1 \times (-1 + 2\cos 60^\circ) = 1 \times (-1 + 1) = 0$.
- $3\hat{\sigma}_h$: 5 atoms unshifted (S and 4 equatorial F) $\implies \chi = 5 \times (1 + 2\cos 0^\circ \text{ with sign change}) = 5 \times 1 = 5$.
- $6\hat{\sigma}_d$: 3 atoms unshifted (S and 2 collinear F) $\implies \chi = 3 \times 1 = 3$.

$$\Gamma_{3N} = [21, 0, -1, 3, -3, -3, -1, 0, 5, 3]$$

---

### Part 2 & 3: Reduction to Vibrational Normal Modes
Subtract translational ($\Gamma_{\text{trans}} = T_{1u}$) and rotational ($\Gamma_{\text{rot}} = T_{1g}$):
$$\Gamma_{\text{vib}} = \Gamma_{3N} - T_{1u} - T_{1g}$$
Applying the master reduction formula $a_\mu = \frac{1}{48} \sum g_k \chi^{(\mu)}(C_k) \chi_{\text{vib}}(C_k)$:
$$\mathbf{\Gamma_{\text{vib}} = A_{1g} + E_g + 2T_{1u} + T_{2g} + T_{2u}}$$

Total vibrational degrees of freedom:
$$1(A_{1g}) + 2(E_g) + 3(T_{1u}) + 3(T_{1u}) + 3(T_{2g}) + 3(T_{2u}) = 1 + 2 + 3 + 3 + 3 + 3 = \mathbf{15 \text{ modes}}$$
Matches $3N - 6 = 3(7) - 6 = 15$!

---

### Part 4: Spectroscopic Assignments and Activities

| Mode | Symmetry | Degeneracy | Physical Motion | Experimental $\tilde{\nu}$ ($\text{cm}^{-1}$) | Spectroscopic Activity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$\nu_1$** | $A_{1g}$ | $1$ (Singlet) | Breathing Symmetric $\text{S}-\text{F}$ Stretch | $775$ | **Raman active ONLY** |
| **$\nu_2$** | $E_g$ | $2$ (Doublet) | Tetragonal Distortion Stretch | $643$ | **Raman active ONLY** |
| **$\nu_3$** | $T_{1u}$ | $3$ (Triplet) | Asymmetric $\text{S}-\text{F}$ Stretch | $948$ | **IR active ONLY** |
| **$\nu_4$** | $T_{1u}$ | $3$ (Triplet) | Scissoring $\text{F}-\text{S}-\text{F}$ Bend | $615$ | **IR active ONLY** |
| **$\nu_5$** | $T_{2g}$ | $3$ (Triplet) | In-Plane Deformation Bend | $523$ | **Raman active ONLY** |
| **$\nu_6$** | $T_{2u}$ | $3$ (Triplet) | Out-of-Plane Wagging Bend | $347$ | **SILENT** (Neither IR nor Raman active!) |

---

### Part 5: Verification of the Rule of Mutual Exclusion
Because $\text{SF}_6$ possesses a rigorous center of inversion ($\hat{i}$ in $O_h$):
- **All gerade ($g$) modes** ($\nu_1(A_{1g}), \nu_2(E_g), \nu_5(T_{2g})$) are **Raman active** and strictly **IR inactive**.
- **All ungerade ($u$) dipole-allowed modes** ($\nu_3(T_{1u}), \nu_4(T_{1u})$) are **IR active** and strictly **Raman inactive**.
- **Zero spectral lines coincide** between the Infrared and Raman spectra!
- Mode $\nu_6(T_{2u})$ is completely inactive in both one-photon techniques (spectroscopically silent), observable only via hyper-Raman or combination bands."""
    }
    if len(u['problems']) < 4:
        u['problems'].append(p4)
    with open("build_inorg1_unit5.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write(r'"""' + "\nUnit 5: Molecular Geometry: VSEPR Theory, Bent's Rule & Symmetry\n" + r'"""' + "\n\n")
        f.write("def get_unit5():\n    return " + repr(u) + "\n")
    print("Unit 5 Problem 5.4 added.")

def add_p4_unit6():
    import build_inorg1_unit6
    u = build_inorg1_unit6.get_unit6()
    p4 = {
        "tier": "Honors / Proof Challenge",
        "title": "Problem 6.4: Walsh Correlation Diagrams & Angular Bending Driving Forces for Ozone and Nitrite",
        "statement": r"""Both ozone ($\text{O}_3$) and the nitrite anion ($\text{NO}_2^-$) are triatomic molecules containing $18$ valence electrons:
- Ozone: $\angle(\text{O}-\text{O}-\text{O}) = 116.8^\circ$
- Nitrite: $\angle(\text{O}-\text{N}-\text{O}) = 115.4^\circ$

1. Construct the Walsh correlation diagram for an $AX_2$ system deforming from linear ($D_{\infty h}$) to bent ($C_{2v}$) across the occupied valence levels:
   $$\sigma_g \rightarrow 2a_1, \quad \sigma_u \rightarrow 1b_2, \quad \sigma_g^* \rightarrow 3a_1, \quad \pi_u \rightarrow (1b_1, 4a_1, 2b_2), \quad \pi_g \rightarrow (1a_2, 3b_2)$$
2. Populate the 18 valence electrons into the molecular orbitals of both geometries.
3. Show which specific molecular orbital experiences the strongest stabilization as the bond angle closes from $180^\circ$ toward $116^\circ$, and identify the quantum mechanical mixing mechanism responsible.
4. Contrast this with carbon dioxide ($\text{CO}_2$, 16 valence electrons), and explain why removing two valence electrons forces the molecule to snap into a strictly linear geometry ($180.0^\circ$).""",
        "solution": r"""### Part 1: Walsh Correlation Framework for Triatomic AX2
In an $AX_2$ molecule ($D_{\infty h} \rightarrow C_{2v}$):
- In the linear limit ($D_{\infty h}$):
  Orbitals are categorized as $\sigma_g, \sigma_u, \pi_u, \pi_g, \sigma_u^*$.
- Upon bending into $C_{2v}$:
  - $\sigma_g \longrightarrow 2a_1$ (Bonding, weak angle dependence).
  - $\sigma_u \longrightarrow 1b_2$ (Bonding, remains nearly constant).
  - $\pi_u \longrightarrow (1b_1 \text{ out-of-plane}, 3a_1 \text{ in-plane}, 2b_2)$.
  - Crucially, the in-plane component of $\pi_u$ becomes **$4a_1$** (or $3a_1$ depending on convention) and the non-bonding central atom orbital becomes **$6a_1$**.

---

### Part 2: Electron Population for 18 Valence Electrons
For $\text{O}_3$ and $\text{NO}_2^-$ (18 valence electrons = 9 pairs):

#### 1. In Linear Geometry ($D_{\infty h}$):
Configuration:
$$\sigma_g^2 \, \sigma_u^2 \, \sigma_g^{*2} \, \pi_u^4 \, \pi_g^4 \, \pi_u^{*2}$$
The last two electrons must occupy the degenerate antibonding $\pi_u^*$ orbital!

#### 2. In Bent Geometry ($C_{2v}$):
Configuration:
$$(1a_1)^2 \, (1b_2)^2 \, (2a_1)^2 \, (1b_1)^2 \, (3a_1)^2 \, (2b_2)^2 \, (1a_2)^2 \, (4a_1)^2 \, (2b_1)^0$$
The 9 electron pairs occupy:
$$2a_1^2 \, 1b_2^2 \, 3a_1^2 \, 1b_1^2 \, 4a_1^2 \, 2b_2^2 \, 1a_2^2 \, 3b_2^2 \, 6a_1^2$$

---

### Part 3: The Driving Orbital for Bending ($6a_1$ / $4a_1$)
The orbital governing the geometry is the **$6a_1$ orbital (HOMO)**:
1. In the linear geometry, this orbital derives from an empty or high-energy antibonding $\sigma_g^*$ / $\pi_u$ level.
2. When the molecule bends, the $C_{2v}$ symmetry allows the central atom's $2s$ orbital to mix with the in-plane $2p_y$ and ligand $2p$ combinations.
3. Because $2s$ is deeply stabilizing ($E_{2s} \ll E_{2p}$), introducing $2s$ character into this orbital causes its energy eigenvalue to **drop precipitously** as the angle $\theta$ contracts:
   $$\frac{\partial \epsilon(6a_1)}{\partial \theta} > 0 \quad (\text{Energy decreases as } \theta \text{ decreases})$$
4. Populating this steeply falling orbital with two electrons provides an overwhelming thermodynamic stabilization:
   $$\Delta E_{\text{bending}} = 2 \Delta \epsilon(6a_1) \ll 0$$
   This drives ozone and nitrite to bend to an equilibrium angle of **$115^\circ\text{–}117^\circ$**.

---

### Part 4: Contrast with Carbon Dioxide ($\text{CO}_2$, 16 Valence Electrons)
Carbon dioxide has only **16 valence electrons** (8 pairs):
- In $\text{CO}_2$, the steeply descending $6a_1$ orbital is **completely empty**!
- All 8 occupied pairs reside in orbitals whose sum of energies is minimized at $\theta = 180^\circ$ (linear geometry maximizes head-on $\sigma$ overlap and linear $\pi$ delocalization).
- Without the two electrons in $6a_1$ to drive angular compression, $\text{CO}_2$ snaps into a strictly **linear ($180.0^\circ$)** geometry!"""
    }
    if len(u['problems']) < 4:
        u['problems'].append(p4)
    with open("build_inorg1_unit6.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 6: Quantum Theories of Bonding: Valence Bond Theory & Molecular Orbital Theory\n"""\n\n')
        f.write("def get_unit6():\n    return " + repr(u) + "\n")
    print("Unit 6 Problem 6.4 added.")

def add_p4_unit7():
    import build_inorg1_unit7
    u = build_inorg1_unit7.get_unit7()
    p4 = {
        "tier": "Honors / Proof Challenge",
        "title": "Problem 7.4: Exact Non-Approximated Quartic Polynomial Equation for Polyprotic Acid Solutions",
        "statement": r"""In introductory chemistry, the $pH$ of a diprotic acid $\text{H}_2\text{A}$ is approximated assuming $[\text{H}^+] \approx \sqrt{K_{a1} C}$ and neglecting the autoionization of water ($K_w = 0$). However, for dilute solutions ($C \le 10^{-5}\text{ M}$) or moderately strong acids, these approximations break down completely.

1. Derive the exact, non-approximated **quartic polynomial equation** in $[\text{H}^+]$:
   $$[\text{H}^+]^4 + a_3 [\text{H}^+]^3 + a_2 [\text{H}^+]^2 + a_1 [\text{H}^+] + a_0 = 0$$
   using the simultaneous constraints of:
   - Mass balance: $C_A = [\text{H}_2\text{A}] + [\text{HA}^-] + [\text{A}^{2-}]$
   - Charge balance (Electroneutrality): $[\text{H}^+] = [\text{HA}^-] + 2[\text{A}^{2-}] + [\text{OH}^-]$
   - Water autoionization: $K_w = [\text{H}^+][\text{OH}^-]$
2. Express the polynomial coefficients $a_3, a_2, a_1, a_0$ explicitly in terms of analytical concentration $C_A$, dissociation constants $K_{a1}, K_{a2}$, and $K_w$.
3. For an ultra-dilute solution of sulfuric acid ($\text{H}_2\text{SO}_4$, $K_{a1} \gg 10^3, K_{a2} = 1.20 \times 10^{-2}$) at concentration $C = 1.00 \times 10^{-7}\text{ M}$ in pure water at $25^\circ\text{C}$ ($K_w = 1.00 \times 10^{-14}$):
   - Compute the exact $[\text{H}^+]$ and $pH$ by solving the polynomial.
   - Demonstrate why a naive calculation predicting $pH = -\log(2 \times 10^{-7}) = 6.70$ is physically erroneous.""",
        "solution": r"""### Part 1 & 2: Analytical Derivation of the Exact Quartic Polynomial

Let analytical diprotic acid concentration be $C_A$.
Using speciation fractions:
$$[\text{HA}^-] = \alpha_1 C_A = \frac{K_{a1} [\text{H}^+]}{D} C_A$$
$$[\text{A}^{2-}] = \alpha_2 C_A = \frac{K_{a1} K_{a2}}{D} C_A$$
where $D = [\text{H}^+]^2 + K_{a1} [\text{H}^+] + K_{a1} K_{a2}$.

Substitute into the electroneutrality condition:
$$[\text{H}^+] = [\text{HA}^-] + 2[\text{A}^{2-}] + \frac{K_w}{[\text{H}^+]}$$
$$[\text{H}^+] - \frac{K_w}{[\text{H}^+]} = \frac{K_{a1} [\text{H}^+] + 2 K_{a1} K_{a2}}{D} C_A$$
Multiply both sides by $[\text{H}^+] D$:
$$\left( [\text{H}^+]^2 - K_w \right) \left( [\text{H}^+]^2 + K_{a1} [\text{H}^+] + K_{a1} K_{a2} \right) = C_A [\text{H}^+] \left( K_{a1} [\text{H}^+] + 2 K_{a1} K_{a2} \right)$$

Expanding term by term:
$$[\text{H}^+]^4 + K_{a1} [\text{H}^+]^3 + K_{a1} K_{a2} [\text{H}^+]^2 - K_w [\text{H}^+]^2 - K_w K_{a1} [\text{H}^+] - K_w K_{a1} K_{a2} = C_A K_{a1} [\text{H}^+]^2 + 2 C_A K_{a1} K_{a2} [\text{H}^+]$$

Grouping powers of $[\text{H}^+]$:
$$\mathbf{[\text{H}^+]^4 + a_3 [\text{H}^+]^3 + a_2 [\text{H}^+]^2 + a_1 [\text{H}^+] + a_0 = 0}$$

#### Explicit Analytical Coefficients:
$$a_3 = K_{a1}$$
$$a_2 = K_{a1} K_{a2} - K_w - C_A K_{a1}$$
$$a_1 = -(K_w K_{a1} + 2 C_A K_{a1} K_{a2})$$
$$a_0 = -K_w K_{a1} K_{a2}$$

---

### Part 3: Ultra-Dilute Sulfuric Acid Solution ($C = 1.00 \times 10^{-7}\text{ M}$)
Since sulfuric acid is completely dissociated for its first proton ($K_{a1} \rightarrow \infty$):
Divide the quartic polynomial by $K_{a1}$ as $K_{a1} \rightarrow \infty$, reducing it to a **cubic polynomial**:
$$[\text{H}^+]^3 + (K_{a2} - C_A) [\text{H}^+]^2 - (K_w + 2 C_A K_{a2}) [\text{H}^+] - K_w K_{a2} = 0$$

Substitute the numerical parameters:
- $C_A = 1.00 \times 10^{-7}\text{ M}$
- $K_{a2} = 1.20 \times 10^{-2}\text{ M}$
- $K_w = 1.00 \times 10^{-14}\text{ M}^2$

1. $K_{a2} - C_A = 0.0120 - 1.00 \times 10^{-7} \approx 0.0120$
2. $K_w + 2 C_A K_{a2} = 1.00 \times 10^{-14} + 2(1.00 \times 10^{-7})(0.0120) = 1.00 \times 10^{-14} + 2.40 \times 10^{-9} \approx 2.40 \times 10^{-9}$
3. $K_w K_{a2} = (1.00 \times 10^{-14})(0.0120) = 1.20 \times 10^{-16}$

The cubic equation:
$$[\text{H}^+]^3 + 0.0120 [\text{H}^+]^2 - 2.40 \times 10^{-9} [\text{H}^+] - 1.20 \times 10^{-16} = 0$$

Since $K_{a2} = 0.0120 \gg C_A$, the second deprotonation ($\text{HSO}_4^- \rightleftharpoons \text{H}^+ + \text{SO}_4^{2-}$) is essentially $100\%$ complete!
Each $\text{H}_2\text{SO}_4$ molecule contributes $2$ protons:
$$C_{\text{acid}} = 2 C_A = 2.00 \times 10^{-7}\text{ M}$$

Including water autoionization:
$$[\text{H}^+] = C_{\text{acid}} + [\text{OH}^-] = 2.00 \times 10^{-7} + \frac{10^{-14}}{[\text{H}^+]}$$
$$[\text{H}^+]^2 - (2.00 \times 10^{-7}) [\text{H}^+] - 1.00 \times 10^{-14} = 0$$

Solving the quadratic formula:
$$[\text{H}^+] = \frac{2.00 \times 10^{-7} + \sqrt{(2.00 \times 10^{-7})^2 + 4(1.00 \times 10^{-14})}}{2}$$
$$\sqrt{4.00 \times 10^{-14} + 4.00 \times 10^{-14}} = \sqrt{8.00 \times 10^{-14}} \approx 2.828 \times 10^{-7}$$
$$[\text{H}^+] = \frac{2.00 \times 10^{-7} + 2.828 \times 10^{-7}}{2} = \frac{4.828 \times 10^{-7}}{2} = \mathbf{2.414 \times 10^{-7}\text{ M}}$$

$$pH = -\log_{10}(2.414 \times 10^{-7}) = \mathbf{6.617 \approx 6.62}$$

#### Why the Naive Calculation Fails:
The naive calculation neglects water autoionization, predicting $[\text{H}^+] = 2.00 \times 10^{-7}\text{ M}$ and $pH = 6.70$.
At concentrations near $10^{-7}\text{ M}$, water autoionization contributes an additional $0.414 \times 10^{-7}\text{ M}$ of protons, depressing the true $pH$ to **$6.62$**!"""
    }
    if len(u['problems']) < 4:
        u['problems'].append(p4)
    with open("build_inorg1_unit7.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 7: Secondary Bonding, Intermolecular Forces & Acid-Base Equilibria\n"""\n\n')
        f.write("def get_unit7():\n    return " + repr(u) + "\n")
    print("Unit 7 Problem 7.4 added.")

def add_p4_unit8():
    import build_inorg1_unit8
    u = build_inorg1_unit8.get_unit8()
    p4 = {
        "tier": "Honors / Proof Challenge",
        "title": "Problem 8.4: Mathematical Derivation of the Copper Pourbaix Phase Boundaries in Natural Waters",
        "statement": r"""Construct the thermodynamic phase boundaries for Copper in water ($\text{Cu}-\text{H}_2\text{O}$) at $298.15\text{ K}$, assuming soluble copper species threshold activity $[\text{Cu}^{2+}] = 1.0 \times 10^{-6}\text{ M}$.
Given thermodynamic data:
- Standard potentials:
  - $\text{Cu}^{2+}(aq) + 2e^- \rightleftharpoons \text{Cu}(s), \quad E^\circ = +0.340\text{ V}$
  - $\text{Cu}^+(aq) + e^- \rightleftharpoons \text{Cu}(s), \quad E^\circ = +0.521\text{ V}$
  - $\text{Cu}^{2+}(aq) + e^- \rightleftharpoons \text{Cu}^+(aq), \quad E^\circ = +0.159\text{ V}$
- Insoluble oxides:
  - Copper(I) oxide ($\text{Cu}_2\text{O}$, cuprite):
    $$\text{Cu}_2\text{O}(s) + 2\,\text{H}^+(aq) + 2e^- \rightleftharpoons 2\,\text{Cu}(s) + \text{H}_2\text{O}(l), \quad E^\circ = +0.471\text{ V}$$
  - Copper(II) oxide ($\text{CuO}$, tenorite):
    $$\text{CuO}(s) + 2\,\text{H}^+(aq) + 2e^- \rightleftharpoons \text{Cu}(s) + \text{H}_2\text{O}(l), \quad E^\circ = +0.570\text{ V}$$

1. Prove that uncomplexed copper(I) ions ($\text{Cu}^+$) undergo spontaneous disproportionation in water at all $pH$, explaining why $\text{Cu}^+$ has no stable domain on the Pourbaix diagram.
2. Derive the boundary equation between metallic Copper ($\text{Cu}^0$) and soluble cupric ion ($\text{Cu}^{2+}$).
3. Derive the slanted boundary equation between metallic Copper ($\text{Cu}^0$) and passivating cuprite ($\text{Cu}_2\text{O}$).
4. Derive the slanted boundary equation between passivating cuprite ($\text{Cu}_2\text{O}$) and passivating tenorite ($\text{CuO}$).
5. Delineate the immunity, corrosion, and passivation domains, and explain why domestic copper drinking-water plumbing resists corrosion in neutral and mildly alkaline tap water ($pH 7.0\text{–}8.5$).""",
        "solution": r"""### Part 1: Thermodynamic Disproportionation Proof of Cuprous Ion ($\text{Cu}^+$)
Consider the self-redox reaction:
$$2\,\text{Cu}^+(aq) \rightleftharpoons \text{Cu}^{2+}(aq) + \text{Cu}(s)$$
- Reduction: $\text{Cu}^+ + e^- \rightarrow \text{Cu}, \quad E_{\text{red}}^\circ = +0.521\text{ V}$
- Oxidation: $\text{Cu}^+ \rightarrow \text{Cu}^{2+} + e^-, \quad E_{\text{ox}}^\circ = -0.159\text{ V}$

Net cell potential:
$$E_{\text{cell}}^\circ = +0.521 - 0.159 = \mathbf{+0.362\text{ V}} > 0$$
Standard Gibbs energy change:
$$\Delta G^\circ = -n F E_{\text{cell}}^\circ = -1 \times 96485 \times 0.362 = \mathbf{-34.9\text{ kJ}\cdot\text{mol}^{-1}}$$
Equilibrium constant:
$$K_{\text{eq}} = \frac{[\text{Cu}^{2+}]}{[\text{Cu}^+]^2} = 10^{\frac{1 \times 0.362}{0.05916}} = 10^{6.12} \approx \mathbf{1.3 \times 10^6}$$
Because $K_{\text{eq}} \gg 1$, uncomplexed $\text{Cu}^+$ in water spontaneously and quantitatively disproportionates into metallic copper and $\text{Cu}^{2+}$.
Therefore, **free $\text{Cu}^+(aq)$ possesses zero stable phase territory** on the aqueous Pourbaix diagram!

---

### Part 2: Boundary 1: $\text{Cu}(s) / \text{Cu}^{2+}(aq)$ (Immunity / Corrosion)
Reaction:
$$\text{Cu}^{2+}(aq) + 2e^- \rightleftharpoons \text{Cu}(s), \quad E^\circ = +0.340\text{ V}$$
Nernst equation:
$$E = 0.340 - \frac{0.05916}{2} \log\left(\frac{1}{[\text{Cu}^{2+}]}\right) = 0.340 + 0.02958 \log[\text{Cu}^{2+}]$$
At the standard corrosion threshold $[\text{Cu}^{2+}] = 1.0 \times 10^{-6}\text{ M}$ ($\log[\text{Cu}^{2+}] = -6.00$):
$$E = 0.340 + 0.02958(-6.00) = 0.340 - 0.1775 = \mathbf{+0.163\text{ V}}$$
- **Equation**: $\mathbf{E = +0.163\text{ V}}$ (Horizontal line independent of $pH$ in acidic media).
- Below $+0.163\text{ V}$: Copper is thermodynamically immune to corrosion. Notice that this immunity boundary lies **above the hydrogen evolution line** ($E = 0.00 - 0.05916 pH$), proving that copper cannot be corroded by non-oxidizing acids ($\text{HCl}$) in the absence of oxygen!

---

### Part 3: Boundary 2: $\text{Cu}(s) / \text{Cu}_2\text{O}(s)$ (Immunity / Passivation)
Reaction:
$$\text{Cu}_2\text{O}(s) + 2\,\text{H}^+(aq) + 2e^- \rightleftharpoons 2\,\text{Cu}(s) + \text{H}_2\text{O}(l), \quad E^\circ = +0.471\text{ V}$$
Nernst equation:
$$E = 0.471 - \frac{0.05916}{2} \log\left(\frac{1}{[\text{H}^+]^2}\right) = 0.471 - 0.05916 pH$$
- **Equation**: $\mathbf{E = 0.471 - 0.05916\,pH \quad (\text{V})}$
This slanted boundary separates metallic copper from protective cuprite.

---

### Part 4: Boundary 3: $\text{Cu}_2\text{O}(s) / \text{CuO}(s)$ (Passivating Transformation)
Reaction:
$$2\,\text{CuO}(s) + 2\,\text{H}^+(aq) + 2e^- \rightleftharpoons \text{Cu}_2\text{O}(s) + \text{H}_2\text{O}(l)$$
Standard potential:
$$E^\circ = 2(0.570) - 0.471 = 1.140 - 0.471 = +0.669\text{ V}$$
Nernst equation:
$$E = 0.669 - \frac{0.05916}{2} \log\left(\frac{1}{[\text{H}^+]^2}\right) = \mathbf{0.669 - 0.05916\,pH \quad (\text{V})}$$

---

### Part 5: Domestic Plumbing Protection
In municipal drinking water ($pH 7.0\text{ to } 8.5$):
- Aerated water contains dissolved oxygen ($E \approx +0.4\text{ to } +0.6\text{ V}$).
- At $pH = 7.5$:
  - The $\text{Cu}_2\text{O}$ boundary is $E = 0.471 - 0.05916(7.5) = +0.027\text{ V}$.
  - The $\text{CuO}$ boundary is $E = 0.669 - 0.05916(7.5) = +0.225\text{ V}$.
- The operating potential of aerated tap water lies directly inside the **Passivation Domain** of cuprite ($\text{Cu}_2\text{O}$) and tenorite ($\text{CuO}$).
- A dense, microscopic, insoluble oxide patina coats the interior of the copper pipe, shutting down ionic dissolution and allowing copper plumbing to last for over 50 years without corroding!"""
    }
    if len(u['problems']) < 4:
        u['problems'].append(p4)
    with open("build_inorg1_unit8.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 8: Inorganic Chemical Reactions: Precipitation, Redox Spontaneity & Potential Diagrams\n"""\n\n')
        f.write("def get_unit8():\n    return " + repr(u) + "\n")
    print("Unit 8 Problem 8.4 added.")

add_p4_unit2()
add_p4_unit4()
add_p4_unit5()
add_p4_unit6()
add_p4_unit7()
add_p4_unit8()
print("ALL 4TH PROBLEMS SUCCESSFULLY ADDED!")
