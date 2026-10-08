# expand_org1_part1.py
# Deep academic enrichment for Unit 1 and Unit 2 of Organic Chemistry I
# Adds graduate/honors depth, mathematical derivations, and detailed mechanistic treatments

def expand_unit1(u1):
    # Deepen Section 1: Electronic Structure & Quantum Orbitals
    u1["sections"][0]["content"] += r"""

### Radial and Angular Distribution Functions of Carbon Atomic Orbitals

To understand the spatial extent and reactivity of carbon's valence electrons, we must analyze the radial distribution functions $P(r) = r^2 |R_{nl}(r)|^2$ derived from hydrogenic wavefunctions with screening corrections:

$$R_{2s}(r) = \frac{1}{\sqrt{2}} \left(\frac{Z_{\text{eff}}}{a_0}\right)^{3/2} \left(1 - \frac{Z_{\text{eff}} r}{2 a_0}\right) \exp\left(-\frac{Z_{\text{eff}} r}{2 a_0}\right) \tag{1.1a}$$
$$R_{2p}(r) = \frac{1}{2\sqrt{6}} \left(\frac{Z_{\text{eff}}}{a_0}\right)^{5/2} r \exp\left(-\frac{Z_{\text{eff}} r}{2 a_0}\right) \tag{1.1b}$$

#### The Penetration Effect & $2s$-$2p$ Energy Splitting:
- The $2s$ radial wavefunction possesses a **radial node** at $r_{\text{node}} = 2 a_0 / Z_{\text{eff}}$. 
- Inside this node ($r < r_{\text{node}}$), a small but critical inner lobe penetrates close to the nucleus, feeling an unscreened nuclear charge approaching $Z = +6$.
- In contrast, the $2p$ radial wavefunction has zero amplitude at the nucleus ($R_{2p}(0) = 0$) due to the centrifugal potential barrier $l(l+1)\hbar^2 / (2\mu r^2)$.
- Consequently, the $2s$ electrons penetrate deeper into the core than $2p$ electrons:
  $$\langle V_{2s} \rangle < \langle V_{2p} \rangle \implies E_{2s} \approx -19.4\text{ eV}, \quad E_{2p} \approx -10.7\text{ eV} \tag{1.1c}$$
- The promotion energy required to excite an electron from the ground state configuration $1s^2 2s^2 2p^2$ ($^3P_0$) to the valence reactive state $1s^2 2s^1 2p^3$ ($^5S_2$) is approximately $+402\text{ kJ/mol}$ ($4.17\text{ eV}$). This investment of energy is repaid more than threefold by the formation of four strong covalent bonds rather than two weak ones, yielding an overall stabilization of over $1200\text{ kJ/mol}$.

#### Slater-Type Orbitals (STOs) vs Gaussian-Type Orbitals (GTOs):
In modern computational chemistry (Hartree-Fock and Density Functional Theory):
1. **STOs** exhibit the correct exponential decay $\exp(-\zeta r)$ at long range and the correct Kato cusp condition $\left.\frac{\partial \psi}{\partial r}\right|_{r=0} = -Z \psi(0)$ at the nucleus.
2. **GTOs** use Gaussian functions $\exp(-\alpha r^2)$, which have zero slope at the nucleus and decay too rapidly at large $r$, but allow analytical evaluation of two-electron four-center repulsion integrals using the Boys function. In basis sets like **6-31G(d,p)**, six primitive Gaussians contract to form the core $1s$ STO, while the valence shell is split into three inner and one outer primitive Gaussian augmented with polarization $d$-functions on carbon and $p$-functions on hydrogen."""

    # Deepen Section 2: Lewis Structures, Formal Charges & Electronegativity
    u1["sections"][1]["content"] += r"""

### Pauling, Mulliken, and Allen Electronegativity Formulations

The concept of electronegativity ($\chi$), which dictates bond dipoles and reaction site electrophilicity, is defined across three distinct theoretical foundations:

1. **Pauling Scale (Thermochemical Bond Dissociation Energies)**:
   Pauling defined electronegativity differences by comparing the heteronuclear bond dissociation energy $D(A-B)$ with the geometric mean of the homonuclear bond energies $D(A-A)$ and $D(B-B)$:
   $$\Delta_{AB} = D(A-B) - \sqrt{D(A-A) \cdot D(B-B)} \tag{1.6c}$$
   $$|\chi_A - \chi_B| = 0.102 \sqrt{\Delta_{AB} \text{ (in kJ/mol)}} \tag{1.6d}$$
   On this scale, Fluorine is defined as $\chi_{\text{Pauling}}(\text{F}) = 3.98$, Oxygen is $3.44$, Nitrogen is $3.04$, Carbon is $2.55$, and Hydrogen is $2.20$.

2. **Mulliken Scale (Absolute Spectroscopic Formulation)**:
   Robert Mulliken recognized that an atom's tendency to attract electrons in a molecule is the average of its ionization energy ($IE$) and electron affinity ($EA$):
   $$\chi_{\text{Mulliken}} = \frac{IE_v + EA_v}{2} \tag{1.6e}$$
   Converting to the Pauling scale: $\chi_{\text{Pauling}} \approx 0.336 (\chi_{\text{Mulliken}} - 0.615)\text{ eV}^{-1}$.

3. **Allen Spectroscopic Scale**:
   Leland Allen defined electronegativity as the configuration energy ($CE$), the average one-electron energy of the valence-shell electrons in ground-state free atoms:
   $$\chi_{\text{Allen}} = \frac{n_s \varepsilon_s + n_p \varepsilon_p}{n_s + n_p} \tag{1.6f}$$
   where $\varepsilon_s$ and $\varepsilon_p$ are experimentally determined valence orbital ionization energies. Because it relies directly on atomic spectroscopic data without empirical fitting, Allen's scale is considered the most fundamental quantum formulation of electronegativity."""

    # Deepen Section 3: Valence Bond & Coulson's Theorem
    u1["sections"][2]["content"] += r"""

### Rigorous Mathematical Derivation of Coulson's Theorem

In non-equivalent hybridization, an atom's hybrid orbitals do not possess equal fractions of $s$ and $p$ character. Let two hybrid orbitals $\phi_a$ and $\phi_b$ centered on carbon be defined as:
$$\phi_a = \frac{s + \lambda_a p_a}{\sqrt{1 + \lambda_a^2}}, \quad \phi_b = \frac{s + \lambda_b p_b}{\sqrt{1 + \lambda_b^2}} \tag{1.11a}$$
where $\lambda_i$ is the mixing coefficient. The fraction of $s$-character in orbital $\phi_i$ is $f_s = \frac{1}{1 + \lambda_i^2}$, and the fraction of $p$-character is $f_p = \frac{\lambda_i^2}{1 + \lambda_i^2}$, satisfying $f_s + f_p = 1$.

#### Quantum Orthogonality Condition:
Because the atomic basis orbitals $s, p_x, p_y, p_z$ are mutually orthogonal:
$$\langle s | s \rangle = 1, \quad \langle p_a | p_b \rangle = \cos \theta_{ab}, \quad \langle s | p_a \rangle = 0 \tag{1.11b}$$
Setting the overlap integral between the two hybrid orbitals $\langle \phi_a | \phi_b \rangle = 0$:
$$\langle \phi_a | \phi_b \rangle = \frac{\langle s + \lambda_a p_a | s + \lambda_b p_b \rangle}{\sqrt{1 + \lambda_a^2}\sqrt{1 + \lambda_b^2}} = \frac{\langle s | s \rangle + \lambda_a \lambda_b \langle p_a | p_b \rangle}{\sqrt{1 + \lambda_a^2}\sqrt{1 + \lambda_b^2}} = 0 \tag{1.11c}$$
$$1 + \lambda_a \lambda_b \cos \theta_{ab} = 0 \implies \mathbf{\cos \theta_{ab} = -\frac{1}{\lambda_a \lambda_b}} \tag{1.11d}$$
This fundamental relationship is **Coulson's Theorem**.

#### Special Symmetric Case ($\lambda_a = \lambda_b = \lambda$):
When two identical bonds subtend an inter-orbital angle $\theta$:
$$\cos \theta = -\frac{1}{\lambda^2} \implies \lambda^2 = -\frac{1}{\cos \theta} \tag{1.11e}$$
1. **Tetrahedral ($sp^3$)**: $\lambda^2 = 3 \implies \cos \theta = -1/3 \implies \theta = 109.47^\circ$.
2. **Trigonal Planar ($sp^2$)**: $\lambda^2 = 2 \implies \cos \theta = -1/2 \implies \theta = 120.0^\circ$.
3. **Linear ($sp$)**: $\lambda^2 = 1 \implies \cos \theta = -1 \implies \theta = 180.0^\circ$.

#### Bent Bonds in Strained Rings (Banana Bonds / Coulson-Moffitt Model):
In cyclopropane, the equilateral carbon triangle forces a nuclear internuclear angle of $\theta_{\text{geom}} = 60^\circ$.
Carbon cannot form hybrid orbitals with an inter-orbital angle of $60^\circ$ because that would require $\cos 60^\circ = +0.5 \implies \lambda^2 = -2$, which is mathematically impossible for real orbitals!
Instead, carbon utilizes **$sp^5$ hybridized orbitals** ($\lambda^2 \approx 5$) pointing along directions that make an angle of $\theta_{\text{hyb}} \approx 104^\circ$ with each other.
- The hybrid orbital maxima point **outward from the internuclear axis** by $\delta = (104^\circ - 60^\circ)/2 = 22^\circ$!
- This off-axis bonding ("bent bonds" or "banana bonds") drastically reduces orbital overlap, explaining why the $\text{C}-\text{C}$ bonds in cyclopropane have an unusually low dissociation energy ($D \approx 272\text{ kJ/mol}$ vs $368\text{ kJ/mol}$ in ethane) and exhibit alkene-like reactivity!
- By conservation of $s$-character, the remaining $\text{C}-\text{H}$ bonds have higher $s$-character ($sp^2$ hybridized, $f_s \approx 0.33$), resulting in unusually short $\text{C}-\text{H}$ bonds ($1.089\text{ \AA}$), higher acidity ($pK_a \approx 46$), and very large NMR coupling constants ($^1J_{\text{C-H}} = 161\text{ Hz}$)."""

    # Deepen Section 4: LCAO Molecular Orbital Theory
    u1["sections"][3]["content"] += r"""

### Secular Determinant & Two-Center Molecular Orbital Energy Derivation

To calculate the molecular orbital energies of a two-center system (e.g., $\text{C}-\text{C}$ or $\text{C}-\text{O}$), we apply the Rayleigh-Ritz variational method.
A trial molecular orbital is constructed as a linear combination of atomic orbitals:
$$\psi = c_1 \phi_1 + c_2 \phi_2 \tag{1.18a}$$
The expectation value of the electronic Hamiltonian $\hat{H}$ is:
$$E = \frac{\langle \psi | \hat{H} | \psi \rangle}{\langle \psi | \psi \rangle} = \frac{c_1^2 H_{11} + 2 c_1 c_2 H_{12} + c_2^2 H_{22}}{c_1^2 S_{11} + 2 c_1 c_2 S_{12} + c_2^2 S_{22}} \tag{1.18b}$$
where $H_{ii} = \alpha_i$ are the Coulomb integrals, $H_{12} = H_{21} = \beta$ is the resonance (transfer) integral, $S_{ii} = 1$ are normalization integrals, and $S_{12} = S_{21} = S$ is the overlap integral.
Minimizing $E$ with respect to the coefficients ($\partial E / \partial c_1 = 0$ and $\partial E / \partial c_2 = 0$) yields the secular equations:
$$\begin{pmatrix} \alpha_1 - E & \beta - E S \\ \beta - E S & \alpha_2 - E \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \tag{1.18c}$$
Nontrivial solutions require the secular determinant to vanish:
$$(\alpha_1 - E)(\alpha_2 - E) - (\beta - E S)^2 = 0 \tag{1.18d}$$

#### Case 1: Homonuclear $\sigma$ and $\pi$ Bonds ($\alpha_1 = \alpha_2 = \alpha$):
Setting overlap $S \approx 0$ for simplicity:
$$(\alpha - E)^2 = \beta^2 \implies \mathbf{E_{\pm} = \alpha \pm \beta} \tag{1.18e}$$
- **Bonding MO ($\sigma$ or $\pi$)**: $E_{\text{bond}} = \alpha + \beta$ (with $\beta < 0$, stabilized by $|\beta|$).
- **Antibonding MO ($\sigma^*$ or $\pi^*$)**: $E_{\text{anti}} = \alpha - \beta$ (destabilized by $|\beta|$).

#### Inclusion of Overlap ($S > 0$) & Antibonding Destabilization:
When the overlap integral $S$ is included rigorously ($S \approx 0.25$ for $\text{C}-\text{C}$ $\sigma$ bonds):
$$E_{\text{bond}} = \frac{\alpha + \beta}{1 + S}, \quad E_{\text{anti}} = \frac{\alpha - \beta}{1 - S} \tag{1.18f}$$
Because $\frac{1}{1 - S} > \frac{1}{1 + S}$, the destabilization of the antibonding orbital **always exceeds the stabilization of the bonding orbital**:
$$\Delta E_{\text{anti}} > \Delta E_{\text{bond}} \tag{1.18g}$$
This universal quantum principle proves why four-electron two-orbital interactions (such as the overlap of two filled lone pairs or closed shells) are strictly repulsive (Pauli repulsion / exchange steric repulsion)."""

    # Deepen Section 5: VSEPR, Bond Geometry & Bent's Rule
    u1["sections"][4]["content"] += r"""

### Bent's Rule: Physical Organic Foundations & Spectroscopic Evidence

Formulated by Henry Bent in 1961, **Bent's Rule** states:
> *Central atomic orbitals direct hybrid orbitals with more $p$-character toward more electronegative substituents, and hybrid orbitals with more $s$-character toward more electropositive substituents.*

#### Quantum Mechanical Basis of Bent's Rule:
1. An $s$-orbital has no directional node, penetrates closer to the nucleus, and has significantly lower energy than a $p$-orbital ($E_{2s} \ll E_{2p}$).
2. When carbon forms a bond to a highly electronegative atom (e.g., Fluorine, $\chi = 3.98$), electron density is drawn away from carbon toward fluorine.
3. Because the electron density in the $\text{C}-\text{F}$ bond resides primarily near fluorine, carbon derives little energetic stabilization from concentrating its lower-energy $s$-character in that bond.
4. Carbon therefore diverts its low-energy $s$-character toward bonds where electron density is held close to the carbon nucleus—specifically $\text{C}-\text{H}$ or $\text{C}-\text{C}$ bonds.

#### Spectroscopic Proof via NMR Spin-Spin Coupling Constants ($^1J_{\text{C-H}}$):
The Fermi contact term in nuclear spin-spin coupling dictates that the one-bond carbon-hydrogen coupling constant $^1J_{\text{C-H}}$ is directly proportional to the fractional $s$-character ($f_s$) of the carbon hybrid orbital:
$$^1J_{\text{C-H}} \approx 500 \cdot f_s \text{ (Hz)} \tag{1.24a}$$
Consider the series of fluoromethanes:

| Molecule | $\angle \text{H}-\text{C}-\text{H}$ Angle | Carbon Hybridization to H | Carbon Hybridization to F | $^1J_{\text{C-H}}$ Coupling Constant |
| :---: | :---: | :---: | :---: | :---: |
| **Methane ($\text{CH}_4$)** | $109.5^\circ$ | $sp^3.00$ ($25.0\% s$) | — | **$125\text{ Hz}$** |
| **Fluoromethyl ($\text{CH}_3\text{F}$)** | $110.2^\circ$ | $sp^2.80$ ($26.3\% s$) | $sp^3.80$ ($20.8\% s$) | **$149\text{ Hz}$** |
| **Difluoromethane ($\text{CH}_2\text{F}_2$)** | $111.9^\circ$ | $sp^2.50$ ($28.6\% s$) | $sp^4.50$ ($18.2\% s$) | **$184\text{ Hz}$** |
| **Fluoroform ($\text{CHF}_3$)** | — | $sp^2.00$ ($33.3\% s$) | $sp^5.00$ ($16.7\% s$) | **$239\text{ Hz}$** |

Notice that as electronegative fluorines are added:
- The carbon hybrid directed toward the remaining hydrogen transitions from pure $sp^3$ ($25\% s$, $125\text{ Hz}$) to pure $sp^2$ ($33.3\% s$, $239\text{ Hz}$)!
- The $\text{C}-\text{H}$ bond length progressively contracts from $1.091\text{ \AA}$ in $\text{CH}_4$ to $1.082\text{ \AA}$ in $\text{CHF}_3$.
- The $\text{C}-\text{F}$ bonds lengthen and acquire higher $p$-character ($sp^5$). Bent's rule provides a seamless, predictive bridge connecting electronegativity, orbital geometry, and molecular spectroscopy!"""

    # Deepen Section 6: Resonance & Hyperconjugation
    u1["sections"][5]["content"] += r"""

### Hyperconjugation vs Resonance: Second-Order Perturbation Theory

While resonance delocalization involves overlap between $\pi$ systems or lone pairs and empty $p$ orbitals, **hyperconjugation** involves the interaction between filled $\sigma$ bonding orbitals and adjacent empty or partially filled orbitals ($\sigma \to p$ or $\sigma \to \pi^*$).

In Natural Bond Orbital (NBO) analysis, the stabilization energy associated with donor orbital $i$ and acceptor orbital $j$ is calculated via second-order perturbation theory:
$$\Delta E_{i \to j}^{(2)} = -2 \frac{|\langle \phi_i | \hat{F} | \phi_j \rangle|^2}{\varepsilon_j - \varepsilon_i} \tag{1.32a}$$
where $\hat{F}$ is the Fock operator, $\langle \phi_i | \hat{F} | \phi_j \rangle = F_{ij}$ is the off-diagonal Fock matrix element representing orbital overlap, and $\varepsilon_j - \varepsilon_i$ is the energy gap between donor and acceptor.

#### 1. Carbocation Stabilization by Hyperconjugation ($\sigma_{\text{C-H}} \to p$):
- In the ethyl cation ($\text{CH}_3\text{CH}_2^+$), the vacant $2p_z$ orbital on the carbocation center overlaps with the coplanar $\sigma_{\text{C-H}}$ bonding orbitals of the adjacent methyl group.
- The three $\sigma_{\text{C-H}}$ bonds provide $\sim 25\text{ kJ/mol}$ of stabilizing delocalization energy each.
- In the tert-butyl cation ($(\text{CH}_3)_3\text{C}^+$), nine adjacent $\sigma_{\text{C-H}}$ and $\sigma_{\text{C-C}}$ bonds donate into the empty $p$ orbital, lowering the gas-phase heat of formation by over $130\text{ kJ/mol}$ relative to the primary propyl cation!

#### 2. The Anomeric Effect in Heterocycles:
In pyranose sugars and 2-halotetrahydropyrans, an electronegative substituent at C2 preferentially adopts the **axial position**, contradicting classical steric considerations.
- This stereoelectronic phenomenon, the **Anomeric Effect**, arises because the non-bonding lone pair ($n_O$) of the ring oxygen is perfectly anti-periplanar to the axial $\sigma^*_{\text{C-X}}$ antibonding orbital.
- Overlap between $n_O$ and $\sigma^*_{\text{C-X}}$ transfers electron density, lowering total energy by $6-12\text{ kJ/mol}$:
  $$\Delta E^{(2)}_{n_O \to \sigma^*_{\text{C-X}}} = -2 \frac{|F_{n,\sigma^*}|^2}{\varepsilon_{\sigma^*} - \varepsilon_n} \tag{1.32b}$$
- In the equatorial conformer, the oxygen lone pairs are oriented at dihedral angles of $60^\circ$ relative to $\sigma^*_{\text{C-X}}$, precluding efficient overlap and eliminating this hyperconjugative stabilization."""
    return u1


def expand_unit2(u2):
    # Deepen Section 1: Alkanes & Nomenclature
    u2["sections"][0]["content"] += r"""

### von Baeyer Systematic Nomenclature for Polycyclic & Spiro Hydrocarbons

Complex bicyclic, polycyclic, and spiroalkanes cannot be named using simple acyclic alkane rules and must follow the von Baeyer IUPAC nomenclature rules:

1. **Bicyclic Hydrocarbons ($\text{bicyclo}[a.b.c]\text{alkane}$)**:
   - Identify the two **bridgehead carbons** (atoms sharing three ring paths).
   - Count the number of carbons in each of the three connecting paths between the bridgeheads, listing them in descending order: $[a.b.c]$ where $a \ge b \ge c$.
   - Number the system starting at one bridgehead, proceeding along the longest path ($a$) to the second bridgehead, continuing along the second longest path ($b$) back to the first bridgehead, and finishing along the shortest bridge ($c$).
   - *Example*: Bicyclo[2.2.1]heptane (Norbornane), Bicyclo[4.4.0]decane (Decalin), Bicyclo[2.2.2]octane.

2. **Spiro Hydrocarbons ($\text{spiro}[a.b]\text{alkane}$)**:
   - Spiro compounds possess a single quaternary carbon atom shared between two rings.
   - Numbering begins in the smaller ring adjacent to the spiro carbon, circles around the smaller ring, crosses through the spiro carbon, and circles around the larger ring.
   - Bracketed numbers reflect ring sizes in ascending order: $[a.b]$ where $a \le b$.
   - *Example*: Spiro[4.5]decane."""

    # Deepen Section 3: Free-Radical Halogenation Kinetics
    u2["sections"][2]["content"] += r"""

### Derivation of Free-Radical Halogenation Steady-State Rate Laws

The gas-phase photochemical chlorination of an alkane proceeds via the classical Rice-Herzfeld free-radical chain mechanism:

$$\text{Cl}_2 + h\nu \xrightarrow{k_1} 2\,\text{Cl}^\bullet \quad (\text{Initiation}) \tag{2.5a}$$
$$\text{Cl}^\bullet + \text{R}-\text{H} \xrightarrow{k_2} \text{R}^\bullet + \text{HCl} \quad (\text{Propagation 1}) \tag{2.5b}$$
$$\text{R}^\bullet + \text{Cl}_2 \xrightarrow{k_3} \text{R}-\text{Cl} + \text{Cl}^\bullet \quad (\text{Propagation 2}) \tag{2.5c}$$
$$2\,\text{R}^\bullet \xrightarrow{k_4} \text{R}-\text{R} \quad (\text{Termination 1}) \tag{2.5d}$$
$$\text{R}^\bullet + \text{Cl}^\bullet \xrightarrow{k_5} \text{R}-\text{Cl} \quad (\text{Termination 2}) \tag{2.5e}$$
$$2\,\text{Cl}^\bullet \xrightarrow{k_6} \text{Cl}_2 \quad (\text{Termination 3}) \tag{2.5f}$$

#### Applying the Pseudo-Steady-State Approximation (PSSA):
Under long chain-length conditions (quantum yield $\Phi \gg 1$), the rates of generation and destruction of active radicals are balanced.
At low radical concentrations, termination predominantly occurs via radical recombination ($2\,\text{Cl}^\bullet \to \text{Cl}_2$ or $2\,\text{R}^\bullet \to \text{R}_2$ depending on the slow propagation step).
For chlorination, where Propagation 1 is fast and exothermic ($\Delta H^\circ \approx -17\text{ kJ/mol}$), the concentration of $\text{Cl}^\bullet$ is held in steady state:
$$\frac{d[\text{Cl}^\bullet]}{dt} = 2 k_1 I_a - k_2 [\text{Cl}^\bullet][\text{R-H}] + k_3 [\text{R}^\bullet][\text{Cl}_2] - 2 k_6 [\text{Cl}^\bullet]^2 \approx 0 \tag{2.5g}$$
The net rate of alkyl chloride formation is:
$$v = \frac{d[\text{R-Cl}]}{dt} = k_3 [\text{R}^\bullet][\text{Cl}_2] = k_2 [\text{Cl}^\bullet][\text{R-H}] \tag{2.5h}$$

#### Energetics and Radical Selectivity via Hammond's Postulate:
The contrast between chlorination and bromination illustrates **Hammond's Postulate**:
- **Chlorination**: The hydrogen abstraction step $\text{Cl}^\bullet + \text{R-H} \to \text{HCl} + \text{R}^\bullet$ is exothermic ($\Delta H^\circ = -17\text{ kJ/mol}$, $E_a \approx 4\text{ kJ/mol}$). The transition state is **early** (reactant-like); the $\text{C}-\text{H}$ bond is barely stretched ($\sim 10\%$), so the radical character on carbon is negligible. Consequently, the stability differences between $1^\circ, 2^\circ$, and $3^\circ$ radicals have little effect on the transition state energy (relative reactivity at $25^\circ\text{C}$ is $1 : 3.8 : 5.0$).
- **Bromination**: The abstraction step $\text{Br}^\bullet + \text{R-H} \to \text{HBr} + \text{R}^\bullet$ is strongly endothermic ($\Delta H^\circ = +42\text{ kJ/mol}$, $E_a \approx 54\text{ kJ/mol}$). The transition state is **late** (product-like); the $\text{C}-\text{H}$ bond is largely broken ($\sim 70\%$), and substantial radical character develops on carbon. The transition state energy directly mirrors the thermodynamic stability of the forming radical (relative reactivity at $127^\circ\text{C}$ is $1 : 82 : 1600$). Bromination is therefore an exceptionally clean, regiospecific synthetic tool."""

    # Deepen Section 4: Carbenes
    u2["sections"][3]["content"] += r"""

### Skell's Hypothesis & Electronic Spin Multiplicity of Carbenes

Carbenes ($:\text{CR}_2$) possess a neutral divalent carbon atom with two non-bonding electrons. Their chemical reactivity is fundamentally governed by their **spin multiplicity**:

1. **Singlet Carbene ($^1A_1$)**:
   - Both non-bonding electrons are paired in a single $sp^2$ hybrid orbital, while the $p_z$ orbital remains completely vacant:
     $$\text{Configuration}: (sp^2)^2 (p_z)^0, \quad S = 0, \quad 2S + 1 = 1 \tag{2.7a}$$
   - The bond angle is compressed ($\angle \text{H}-\text{C}-\text{H} \approx 102^\circ$) due to lone-pair repulsion.
   - **Reactivity (Skell Hypothesis)**: Proceeds through a **concerted, single-step addition** across an alkene $\pi$ bond. Because bond formation occurs simultaneously at both ends without generating an intermediate diradical, **the stereochemistry of the alkene is strictly preserved**:
     $$\text{cis-Alkene} + {}^1[:\text{CR}_2] \longrightarrow \text{cis-Cyclopropane exclusively} \tag{2.7b}$$

2. **Triplet Carbene ($^3B_1$)**:
   - The two non-bonding electrons reside in separate degenerate or nearly degenerate orbitals with parallel spins according to Hund's rule:
     $$\text{Configuration}: (sp)^1 (p_y)^1 (p_z)^0 \text{ or } (sp^2)^1 (p_z)^1, \quad S = 1, \quad 2S + 1 = 3 \tag{2.7c}$$
   - The bond angle is wide ($\angle \text{H}-\text{C}-\text{H} \approx 136^\circ$).
   - For methylene ($:\text{CH}_2$), the triplet state is the thermodynamic ground state, lying $\sim 38\text{ kJ/mol}$ lower in energy than the singlet state.
   - **Reactivity (Skell Hypothesis)**: Because spin inversion is quantum mechanically forbidden on the timescale of bond rotations ($10^{-10}\text{ s}$), addition to an alkene occurs via a **two-step radical pathway** forming a triplet 1,3-diradical intermediate:
     $$\text{Alkene} + {}^3[:\text{CR}_2] \longrightarrow [^\bullet\text{C}-\text{C}-\text{C}^\bullet \text{ (Triplet Diradical)}] \tag{2.7d}$$
     Free rotation around the single bond occurs before spin inversion, yielding a **mixture of cis and trans cyclopropanes** regardless of initial alkene geometry!"""

    # Deepen Section 6: Cyclohexane Dynamics
    u2["sections"][5]["content"] += r"""

### Complete Energy Profile & Dynamic NMR of Cyclohexane Chair Flip

The interconversion between the two degenerate chair conformations of cyclohexane proceeds along a well-defined multi-step potential energy surface:

$$\text{Chair}_1 \xrightleftharpoons[\Delta G^\ddagger = 45\text{ kJ/mol}]{} \left[\text{Half-Chair}\right]^\ddagger \rightleftharpoons \text{Twist-Boat} \rightleftharpoons \left[\text{Boat}\right]^\ddagger \rightleftharpoons \text{Twist-Boat}' \rightleftharpoons \left[\text{Half-Chair}'\right]^\ddagger \rightleftharpoons \text{Chair}_2 \tag{2.12a}$$

#### Thermodynamic & Kinetic Free Energies at $298\text{ K}$:
1. **Chair ($D_{3d}$ symmetry)**: Potential energy minimum defined as reference ($0.0\text{ kJ/mol}$). Possesses staggered bonds throughout, zero angle strain, and zero torsional strain.
2. **Half-Chair ($C_2$ symmetry)**: Transition state for chair-to-twist-boat conversion. Four carbons are coplanar, introducing intense angle and torsional strain:
   $$\Delta G^\ddagger = +45.2\text{ kJ/mol} \quad (10.8\text{ kcal/mol}) \tag{2.12b}$$
3. **Twist-Boat ($D_2$ symmetry)**: Local energy minimum (intermediate). Twisting relieves flagpole eclipsing:
   $$\Delta G^\circ = +23.0\text{ kJ/mol} \quad (5.5\text{ kcal/mol}) \tag{2.12c}$$
4. **Boat ($C_{2v}$ symmetry)**: Transition state for twist-boat to twist-boat pseudorotation. Exhibits complete eclipsing of four $\text{C}-\text{H}$ bonds along the sides and severe flagpole-flagpole van der Waals steric clash between C1 and C4 ($r_{\text{H}\cdots\text{H}} \approx 1.83\text{ \AA}$):
   $$\Delta G^\circ = +29.0\text{ kJ/mol} \quad (6.9\text{ kcal/mol}) \tag{2.12d}$$

#### Dynamic $^1\text{H}$ NMR Coalescence Spectroscopy:
At room temperature ($25^\circ\text{C}$), the chair flip occurs at a frequency of $k \approx 10^5\text{ s}^{-1}$.
Because this rate far exceeds the NMR chemical shift frequency difference between equatorial and axial protons ($\Delta \nu \approx 0.5\text{ ppm} \times 500\text{ MHz} = 250\text{ Hz}$), a single time-averaged sharp singlet is observed at $\delta = 1.44\text{ ppm}$.
- Upon cooling to the **coalescence temperature** ($T_c = 206\text{ K} = -67^\circ\text{C}$), the peak broadens and splits into two distinct, equal-intensity multiplets:
  - Axial protons ($\text{H}_{\text{ax}}$): $\delta = 1.19\text{ ppm}$ (shielded by $\text{C}-\text{C}$ diamagnetic anisotropy)
  - Equatorial protons ($\text{H}_{\text{eq}}$): $\delta = 1.68\text{ ppm}$ (deshielded)
- Applying the Gutowsky-Holm equation at coalescence:
  $$k_c = \frac{\pi \Delta \nu}{\sqrt{2}} = \frac{\pi (250)}{\sqrt{2}} \approx 555\text{ s}^{-1} \tag{2.12e}$$
- Applying the Eyring equation yields the experimental activation free energy:
  $$\Delta G^\ddagger = -R T_c \ln\left(\frac{h k_c}{k_B T_c}\right) = 43.1\text{ kJ/mol} \tag{2.12f}$$
  in exact alignment with computational force-field predictions!"""

    # Deepen Section 7: Bicycloalkanes & Bredt's Rule
    u2["sections"][6]["content"] += r"""

### Bredt's Rule & The Fawcett $S$-Number Geometric Limit

Formulated by Julius Bredt in 1924, **Bredt's Rule** establishes that:
> *A double bond cannot be located at the bridgehead carbon of a bridged bicyclic ring system unless the rings are sufficiently large to accommodate the necessary trans-cycloalkene geometry without prohibitive ring strain.*

#### Fawcett's Quantitative $S$-Number Formulation:
In 1950, Frank Fawcett parameterized Bredt's rule using the ring-size index $S$:
$$S = x + y + z \tag{2.15a}$$
where $x, y, z$ are the number of carbon atoms in the three bridges of the $\text{bicyclo}[x.y.z]$ system:
1. **$S < 7$**: Bridgehead alkenes are completely unstable, non-existent even as transient reaction intermediates.
2. **$S = 7 \text{ or } 8$**: Highly reactive, transient intermediates that can only be trapped in low-temperature matrices or via *in situ* Diels-Alder cycloadditions (e.g., bicyclo[2.2.1]hept-1-ene).
3. **$S \ge 9$**: Isolable, thermodynamically stable compounds at room temperature (e.g., bicyclo[3.3.1]non-1-ene, $S = 3 + 3 + 1 = 7$, is isolable but very strained; bicyclo[4.4.1]undec-1-ene, $S = 9$, is completely stable).

#### Geometric and Orbital Origin of Strain:
A bridgehead double bond in a bridged bicyclic system forces the $p$-orbitals of the alkene into a non-parallel, twisted orientation.
- The $\pi$-bond dihedral angle $\tau$ deviates from $0^\circ$:
  $$E_{\text{twist}} = V_\pi (1 - \cos 2\tau) \tag{2.15b}$$
- In norbornene derivatives ($S=5$), accommodating a bridgehead double bond requires a twist angle $\tau > 45^\circ$, reducing orbital overlap by more than $50\%$ and creating strain energies exceeding $180\text{ kJ/mol}$!
- Furthermore, one of the two rings containing the double bond must incorporate the double bond as a **trans-cycloalkene**. Because the smallest isolable trans-cycloalkene is trans-cyclooctene (which itself possesses $71\text{ kJ/mol}$ of strain), any bicyclic ring system containing a bridgehead double bond must incorporate at least an eight-membered ring across the active bridge to achieve room-temperature stability!"""
    return u2
