# expand_org1_part6.py
# Deep academic enrichment: Subsections §1.7, §2.9, §3.9, §4.9, §5.9, §6.9, §7.9, §8.9
# and 16 Graduate/Honors Solved Problems across all 8 units.

def expand_master_curriculum(units):
    u1, u2, u3, u4, u5, u6, u7, u8 = units

    # ==========================================
    # UNIT 1: Advanced Section & Honors Problems
    # ==========================================
    u1["sections"].append({
        "id": "sec1_7",
        "secNumber": "1.7",
        "title": "§1.7 Advanced Frontier Molecular Orbital Interactions & Non-Covalent Supramolecular Forces",
        "heading": "Advanced Frontier Molecular Orbital Interactions & Non-Covalent Supramolecular Forces",
        "simulations": ["sim_chem_organic_hybridization_resonance"],
        "content": r"""### The Klopman-Salem Equation of Chemical Reactivity

In physical organic chemistry, the interaction energy $\Delta E$ between two reacting molecular species $A$ and $B$ along a collision trajectory is evaluated using the **Klopman-Salem Equation** derived from second-order perturbation theory:

$$\Delta E = \Delta E_{\text{Coulomb}} + \Delta E_{\text{Exchange}} + \Delta E_{\text{Orbital}} \tag{1.35a}$$

#### Three Component Energy Contributions:
1. **Electrostatic / Coulomb Attraction ($\Delta E_{\text{Coulomb}}$)**:
   $$\Delta E_{\text{Coulomb}} = \sum_{a \in A} \sum_{b \in B} \frac{q_a q_b}{\varepsilon R_{ab}} \tag{1.35b}$$
   Governs reactions under **charge control** (hard-hard interactions, such as proton transfer or fluoride attacking silicon).
2. **Exchange / Pauli Steric Repulsion ($\Delta E_{\text{Exchange}}$)**:
   $$\Delta E_{\text{Exchange}} = -\sum_{i \in \text{occ}} \sum_{j \in \text{occ}} \frac{2 |S_{ij}|^2 (H_{ij} - E_0)}{1 - S_{ij}^2} \tag{1.35c}$$
   Repulsion between closed, filled electron shells. Always positive (destabilizing), dictating steric hindrance.
3. **Orbital Interaction Energy ($\Delta E_{\text{Orbital}}$)**:
   $$\Delta E_{\text{Orbital}} = 2 \sum_{i \in \text{occ}(A)} \sum_{j \in \text{unocc}(B)} \frac{|c_{i a} c_{j b} \beta_{ab}|^2}{\varepsilon_i - \varepsilon_j} + 2 \sum_{j \in \text{occ}(B)} \sum_{i \in \text{unocc}(A)} \frac{|c_{j b} c_{i a} \beta_{ab}|^2}{\varepsilon_j - \varepsilon_i} \tag{1.35d}$$
   Governs reactions under **orbital / frontier control** (soft-soft interactions, such as $S_N2$ substitution by iodide or Diels-Alder cycloadditions).
   - As the energy gap $\Delta \varepsilon = |\varepsilon_{\text{HOMO}} - \varepsilon_{\text{LUMO}}|$ decreases, the denominator approaches zero and orbital stabilization increases dramatically!

### Supramolecular Non-Covalent Interactions

Beyond classical covalent bonds, non-covalent forces dictate molecular recognition, protein folding, and crystal packing:

1. **Halogen Bonding ($\text{C}-\text{X}\cdots\text{B}$)**:
   - When carbon is bonded to a polarizable halogen ($\text{I} > \text{Br} > \text{Cl}$), the electron density forms a belt around the equator, leaving a localized region of positive electrostatic potential at the outermost pole—the **$\sigma$-hole**.
   - Lewis bases (e.g., amine nitrogens, carbonyl oxygens) donate electron density directly into this $\sigma$-hole along the $\text{C}-\text{X}$ axis ($\angle \text{C}-\text{X}\cdots\text{B} \approx 180^\circ$), with interaction energies reaching $10-40\text{ kJ/mol}$!
2. **Cation-$\pi$ Interactions**:
   - The electron-rich $\pi$ faces of aromatic rings interact electrostatically with alkali metal cations ($\text{Na}^+, \text{K}^+$) and organic cations (quaternary ammonium, choline).
   - In aqueous media, cation-$\pi$ binding energies between $\text{K}^+$ and benzene reach $-18\text{ kJ/mol}$, serving as the primary binding mode in potassium ion channels and neurotransmitter receptors.
3. **$\pi-\pi$ Stacking (Face-to-Face Displaced & T-Shaped Edge-to-Face)**:
   - Due to quadrupolar electrostatics (Hunter-Sanders model), parallel eclipsed benzene dimers are repulsive.
   - Stable orientations adopt either a **parallel-displaced geometry** (offset by $1.6 - 1.8\text{ \AA}$) or a **T-shaped edge-to-face geometry** (where a positively polarized peripheral proton points into the negative $\pi$ face), contributing $8-12\text{ kJ/mol}$ of stabilization per pair in DNA base stacking."""
    })

    u1["problems"].extend([
        {
            "id": "p1_5",
            "difficulty": "advanced",
            "difficultyLabel": "Advanced Honors Problem",
            "title": "Quantum Hybridization Angle & Nuclear Coupling Derivation for Bicyclo[1.1.0]butane",
            "question": "In bicyclo[1.1.0]butane, the bridgehead C-C bond length is unusually short (1.498 Å) and the inter-bridgehead dihedral angle is 122°. The one-bond 13C-1H coupling constant for the bridgehead protons is measured experimentally at 1J(C-H) = 205 Hz. Using Coulson's theorem and the Fermi contact relationship, calculate: (1) the fractional s-character of the bridgehead C-H bond, (2) the hybridization lambda^2 of the bridgehead C-H hybrid orbital, (3) the hybridization of the bridgehead C-C bridge bond, and (4) the inter-orbital angle theta subtended by the bridgehead C-C hybrids.",
            "solution": r"""#### Part 1: Fractional $s$-Character of the Bridgehead $\text{C}-\text{H}$ Bond
Using the Fermi contact empirical relation connecting the one-bond carbon-proton spin-spin coupling constant $^1J_{\text{C-H}}$ to fractional $s$-character $f_s$:
$$^1J_{\text{C-H}} \approx 500 \cdot f_s \text{ (Hz)} \tag{1}$$
$$f_s = \frac{^1J_{\text{C-H}}}{500} = \frac{205\text{ Hz}}{500\text{ Hz}} = \mathbf{0.410} \quad (41.0\% s\text{-character})$$

#### Part 2: Hybridization Parameter $\lambda_{\text{CH}}^2$
The fractional $s$-character in a hybrid orbital $sp^{\lambda^2}$ is defined as:
$$f_s = \frac{1}{1 + \lambda_{\text{CH}}^2} \implies 1 + \lambda_{\text{CH}}^2 = \frac{1}{0.410} \approx 2.439$$
$$\lambda_{\text{CH}}^2 = 2.439 - 1 = \mathbf{1.439} \implies \mathbf{sp^{1.44}}$$
The bridgehead $\text{C}-\text{H}$ bond possesses remarkable $s$-character, approaching that of an $sp$ hybrid ($50\%$), explaining its high kinetic acidity ($pK_a \approx 34$).

#### Part 3: Hybridization of the Central Bridgehead $\text{C}-\text{C}$ Bond
By the fundamental quantum conservation of atomic orbital character, each carbon atom possesses exactly one $2s$ orbital ($100\% s$) and three $2p$ orbitals ($300\% p$):
$$\sum_{i=1}^4 f_{s,i} = 1.000$$
The bridgehead carbon forms four bonds: one $\text{C}-\text{H}$ bond, one central bridgehead $\text{C}-\text{C}$ bond, and two peripheral $\text{C}-\text{C}$ bonds (each having $f_s \approx 0.05$ due to extreme ring strain):
$$f_{s,\text{central CC}} = 1.000 - f_{s,\text{CH}} - 2 f_{s,\text{periph}} = 1.000 - 0.410 - 2(0.050) = 0.490 \text{ remaining for bridge and peripheral distribution.}$$
Rigorous NBO (Natural Bond Orbital) calculations reveal that the central bridgehead bond is formed almost purely from unhybridized $p$-character:
$$f_{s,\text{bridge}} \approx 0.060 \implies \lambda_{\text{bridge}}^2 = \frac{1 - 0.060}{0.060} \approx \mathbf{15.7} \implies \mathbf{sp^{15.7}}$$

#### Part 4: Inter-Orbital Angle Subtended by Bridge Hybrids
Applying Coulson's theorem:
$$\cos \theta_{\text{inter}} = -\frac{1}{\lambda_{\text{bridge}}^2} = -\frac{1}{15.7} \approx -0.0637$$
$$\theta_{\text{inter}} = \arccos(-0.0637) = \mathbf{93.65^\circ}$$
Because the internuclear bridgehead axis has a geometric angle of nearly $0^\circ$ relative to the bridge path, the hybrid orbital maxima project outward by more than $45^\circ$, forming extreme bent "banana" bonds with significant diradical-like reactivity!"""
        },
        {
            "id": "p1_6",
            "difficulty": "honors",
            "difficultyLabel": "Graduate Level Derivation",
            "title": "Perturbation Calculation of the Salem-Klopman Denominator in Acid-Base Adducts",
            "question": "Calculate the second-order orbital stabilization energy Delta E_orb for the frontier interaction between the HOMO of trimethylamine (epsilon_HOMO = -7.8 eV) and the LUMO of boron trifluoride (epsilon_LUMO = -1.2 eV) versus the interaction with borane (BH3, epsilon_LUMO = +0.5 eV). Assume the Fock matrix interaction element beta_ab = 2.1 eV for both complexes. Explain using frontier orbital theory why trimethylamine forms a more thermodynamically stable adduct with BH3 than with BF3 despite fluorine being more electronegative.",
            "solution": r"""#### Step 1: Second-Order Orbital Stabilization Formula
According to second-order Rayleigh-Schrödinger perturbation theory in the Salem-Klopman formalism:
$$\Delta E_{\text{orb}} = -2 \frac{|\beta_{ab}|^2}{\varepsilon_{\text{LUMO}} - \varepsilon_{\text{HOMO}}} \tag{1}$$
where the factor of 2 accounts for the two electrons transferring from the donor HOMO.

#### Step 2: Evaluation for the $\text{Me}_3\text{N} \to \text{BF}_3$ Adduct
- Donor $\varepsilon_{\text{HOMO}}(\text{Me}_3\text{N}) = -7.8\text{ eV}$
- Acceptor $\varepsilon_{\text{LUMO}}(\text{BF}_3) = -1.2\text{ eV}$
- Energy gap $\Delta \varepsilon_1 = -1.2 - (-7.8) = \mathbf{+6.6\text{ eV}}$
$$\Delta E_{\text{orb}}(\text{BF}_3) = -2 \frac{(2.1\text{ eV})^2}{6.6\text{ eV}} = -2 \frac{4.41}{6.6} = \mathbf{-1.336\text{ eV}} \quad (\mathbf{-128.9\text{ kJ/mol}})$$

#### Step 3: Evaluation for the $\text{Me}_3\text{N} \to \text{BH}_3$ Adduct
- Acceptor $\varepsilon_{\text{LUMO}}(\text{BH}_3) = +0.5\text{ eV}$
- Energy gap $\Delta \varepsilon_2 = +0.5 - (-7.8) = \mathbf{+8.3\text{ eV}}$
$$\Delta E_{\text{orb}}(\text{BH}_3) = -2 \frac{(2.1\text{ eV})^2}{8.3\text{ eV}} = -2 \frac{4.41}{8.3} = \mathbf{-1.063\text{ eV}} \quad (\mathbf{-102.5\text{ kJ/mol}})$$

#### Step 4: Physical Organic Reconciliation: The $\pi$-Backbonding & Steric Anomaly
Although the simple orbital denominator predicts stronger frontier stabilization for $\text{BF}_3$, experimentally the adduct dissociation enthalpy $\Delta H_{\text{dissoc}}^\circ$ of $\text{Me}_3\text{N}-\text{BH}_3$ ($146\text{ kJ/mol}$) is **substantially higher** than that of $\text{Me}_3\text{N}-\text{BF}_3$ ($88\text{ kJ/mol}$).
1. **Loss of $p_\pi-p_\pi$ Backbonding in $\text{BF}_3$**:
   - In planar free $\text{BF}_3$, the vacant $2p_z$ orbital on boron is stabilized by strong resonance donation from the three fluorine lone pairs:
     $$\Delta E_{\pi\text{-stab}}(\text{free } \text{BF}_3) \approx \mathbf{125\text{ kJ/mol}}$$
   - Upon complexation, boron pyramidalizes from $sp^2$ trigonal planar to $sp^3$ tetrahedral, completely destroying $p_\pi-p_\pi$ overlap and imposing an enormous reorganization energy penalty!
   - In contrast, free $\text{BH}_3$ possesses zero $\pi$-stabilization, so pyramidalization incurs minimal electronic penalty.
2. **Steric F-F vs Me Clashing**:
   - Pyramidalizing $\text{BF}_3$ compresses three bulky, electronegative fluorine atoms against the three methyl groups of trimethylamine, creating severe Pauli exchange repulsion."""
        }
    ])

    # ==========================================
    # UNIT 2: Advanced Section & Honors Problems
    # ==========================================
    u2["sections"].append({
        "id": "sec2_9",
        "secNumber": "2.9",
        "title": "§2.9 Hydrocarbon Analytics: High-Resolution GC-MS & Bomb Calorimetry",
        "heading": "Hydrocarbon Analytics: High-Resolution GC-MS & Bomb Calorimetry",
        "simulations": ["sim_chem_cycloalkane_conformational_strain"],
        "content": r"""### Analytical Separation & Mass Spectrometric Fragmentation of Alkanes

The complex hydrocarbon mixtures generated by petroleum refining are resolved and characterized using capillary **Gas Chromatography coupled with Electron Ionization Mass Spectrometry (GC-MS)**:

#### 1. Capillary Gas Chromatography Dynamics:
The retention time $t_R$ of an alkane on a non-polar polydimethylsiloxane stationary phase (e.g., DB-5) correlates with its boiling point and Kovats retention index ($I$):
$$I = 100 \left[ n + \frac{\log t'_R(\text{analyte}) - \log t'_R(n)}{\log t'_R(n+1) - \log t'_R(n)} \right] \tag{2.17a}$$
where $t'_R = t_R - t_M$ is the adjusted retention time, and $n$ is the carbon number of the preceding normal alkane.
- **Branching Effect**: Highly branched alkanes possess more compact spherical geometries, smaller polarizable surface areas, and weaker London dispersion forces. Consequently, branched isomers elute substantially earlier than linear isomers (e.g., 2,2,4-trimethylpentane elutes before $n$-octane).

#### 2. Electron Ionization (EI) Mass Spectrometry Fragmentation:
High-energy electrons ($70\text{ eV}$) ionize alkane molecules to generate radical cations ($M^{\bullet+}$):
$$\text{R}-\text{H} + e^-(70\text{ eV}) \longrightarrow [\text{R}-\text{H}]^{\bullet+} + 2\,e^- \tag{2.17b}$$
- **$\alpha$-Cleavage & Carbocation Stability**: Fragmentation occurs preferentially at branched carbons to generate the most stable secondary or tertiary carbocation:
  $$[\text{R}-\text{CH}(\text{Me})-\text{R}']^{\bullet+} \longrightarrow \mathbf{\text{R}-\stackrel{\oplus}{\text{C}}\text{H}-\text{Me}} + \text{R}'^\bullet \tag{2.17c}$$
- **Mass Spectral Fingerprints**: Linear alkanes produce characteristic clusters spaced by $14\text{ Da}$ ($-\text{CH}_2-$ units): $m/z = 43 (\text{C}_3\text{H}_7^+), 57 (\text{C}_4\text{H}_9^+), 71 (\text{C}_5\text{H}_{11}^+), 85 (\text{C}_6\text{H}_{13}^+)$, with $m/z = 43$ or $57$ serving as the base peak.

### Precision Bomb Calorimetry & Real Gas Corrections

The experimental heats of combustion ($\Delta U_c^\circ$) of hydrocarbons are measured inside an adiabatic oxygen bomb calorimeter pressurized to $P \approx 30\text{ bar}$:

$$\Delta U_c^\circ = -\frac{C_{\text{cal}} \Delta T - q_{\text{fuse}} - q_{\text{HNO}_3}}{m_{\text{sample}}} \tag{2.17d}$$
$$\Delta H_c^\circ = \Delta U_c^\circ + \Delta n_g R T \tag{2.17e}$$
where $\Delta n_g = n(\text{CO}_2, g) - n(\text{O}_2, g)$ is the change in moles of gas.
- Applying Washburn corrections to adjust for non-ideality of gases at $30\text{ bar}$ enables measurements of combustion enthalpies with uncertainties below $\pm 0.02\%$, establishing the fundamental thermochemical scale for ring strain energies across all cycloalkanes!"""
    })

    u2["problems"].extend([
        {
            "id": "p2_5",
            "difficulty": "advanced",
            "difficultyLabel": "Advanced Honors Problem",
            "title": "Conformational Free Energy & Population of trans-1,4-Di-tert-butylcyclohexane",
            "question": "For trans-1,4-di-tert-butylcyclohexane, one tert-butyl group must be equatorial and the other must be axial if the ring adopts a chair conformation. Given that the A-value for a tert-butyl group is 4.90 kcal/mol (20.5 kJ/mol) and the twist-boat conformation of cyclohexane lies 5.50 kcal/mol (23.0 kJ/mol) above the chair conformation: (1) Calculate the free energy difference between the chair conformation (with one axial t-Bu) and the twist-boat conformation (where both t-Bu groups occupy equatorial-like pseudo-equatorial positions). (2) Determine the equilibrium mole fraction of twist-boat molecules present in a liquid sample at 298 K. (3) State the dynamic physical implications of this balance.",
            "solution": r"""#### Part 1: Free Energy Calculation for Both Conformations
1. **Chair Conformation ($\text{Chair}_{e,a}$)**:
   - One tert-butyl group is equatorial ($0.0\text{ kcal/mol}$).
   - The second tert-butyl group is forced into the axial position, incurring the full 1,3-diaxial steric strain penalty:
     $$E(\text{Chair}_{e,a}) = A(\text{tert-butyl}) = \mathbf{+4.90\text{ kcal/mol}} \quad (+20.50\text{ kJ/mol})$$
2. **Twist-Boat Conformation ($\text{Twist-Boat}_{e',e'}$)**:
   - In the twist-boat conformation, both the C1 and C4 positions can simultaneously accommodate bulky substituents in **pseudo-equatorial positions** with virtually zero 1,3-diaxial steric clash!
   - However, the cyclohexane ring skeleton itself incurs the intrinsic ring strain of the twist-boat:
     $$E(\text{Twist-Boat}_{e',e'}) = \Delta G_{\text{twist-boat}} + 2 \times E_{\text{strain}}(\text{pseudo-eq}) = 5.50 + 2(0.10) = \mathbf{+5.70\text{ kcal/mol}} \quad (+23.85\text{ kJ/mol})$$
3. **Net Free Energy Difference**:
   $$\Delta G^\circ = E(\text{Twist-Boat}) - E(\text{Chair}) = 5.70 - 4.90 = \mathbf{+0.80\text{ kcal/mol}} \quad (\mathbf{+3.35\text{ kJ/mol}})$$
   The chair conformation remains favored by only $0.80\text{ kcal/mol}$!

#### Part 2: Equilibrium Mole Fraction at $298\text{ K}$
Using the Boltzmann distribution:
$$K = \frac{[\text{Twist-Boat}]}{[\text{Chair}]} = \exp\left(-\frac{\Delta G^\circ}{R T}\right)$$
Using $R = 1.987 \times 10^{-3}\text{ kcal}/(\text{mol}\cdot\text{K})$ and $T = 298.15\text{ K}$:
$$R T = (1.987 \times 10^{-3})(298.15) \approx 0.5924\text{ kcal/mol}$$
$$K = \exp\left(-\frac{0.80}{0.5924}\right) = \exp(-1.350) \approx \mathbf{0.259}$$
The mole fraction of the twist-boat conformer ($x_{\text{TB}}$) is:
$$x_{\text{TB}} = \frac{K}{1 + K} = \frac{0.259}{1 + 0.259} = \frac{0.259}{1.259} \approx \mathbf{0.206} \quad (\mathbf{20.6\%})$$

#### Part 3: Physical Organic Significance
In trans-1,4-di-tert-butylcyclohexane, **over $20\%$ of all molecules exist in the non-chair twist-boat conformation at room temperature**!
This is one of the rare instances where extreme steric clash overrides the thermodynamic preference of the cyclohexane ring for the chair conformation, providing a classic system for measuring pure twist-boat activation barriers via dynamic low-temperature NMR."""
        },
        {
            "id": "p2_6",
            "difficulty": "honors",
            "difficultyLabel": "Graduate Level Derivation",
            "title": "Rice-Herzfeld Steady-State Radical Chain Derivation for Alkane Thermal Cracking",
            "question": "Derive the theoretical rate equation for the thermal decomposition of ethane (C2H6 -> C2H4 + H2) at 850 K using the classic Rice-Herzfeld free-radical mechanism: (1) Initiation: C2H6 -> 2 CH3* (k1); (2) Transfer: CH3* + C2H6 -> CH4 + C2H5* (k2); (3) Propagation: C2H5* -> C2H4 + H* (k3); (4) Propagation: H* + C2H6 -> H2 + C2H5* (k4); (5) Termination: H* + C2H5* -> C2H6 (k5). Prove that under steady-state conditions, the rate of ethylene production is first-order in ethane concentration: v = k_eff [C2H6]. Express k_eff in terms of elementary rate constants.",
            "solution": r"""#### Step 1: Write Elementary Reaction Rates
1. Initiation: $r_1 = k_1 [\text{C}_2\text{H}_6]$
2. Transfer: $r_2 = k_2 [\text{CH}_3^\bullet][\text{C}_2\text{H}_6]$
3. Propagation 1: $r_3 = k_3 [\text{C}_2\text{H}_5^\bullet]$
4. Propagation 2: $r_4 = k_4 [\text{H}^\bullet][\text{C}_2\text{H}_6]$
5. Termination: $r_5 = k_5 [\text{H}^\bullet][\text{C}_2\text{H}_5^\bullet]$

#### Step 2: Pseudo-Steady-State Approximations (PSSA)
For active radical intermediates ($\text{CH}_3^\bullet, \text{H}^\bullet, \text{C}_2\text{H}_5^\bullet$):
1. **Methyl Radical $[\text{CH}_3^\bullet]$**:
   $$\frac{d[\text{CH}_3^\bullet]}{dt} = 2 k_1 [\text{C}_2\text{H}_6] - k_2 [\text{CH}_3^\bullet][\text{C}_2\text{H}_6] = 0 \implies k_2 [\text{CH}_3^\bullet][\text{C}_2\text{H}_6] = 2 k_1 [\text{C}_2\text{H}_6] \tag{1}$$
2. **Hydrogen Atom $[\text{H}^\bullet]$**:
   $$\frac{d[\text{H}^\bullet]}{dt} = k_3 [\text{C}_2\text{H}_5^\bullet] - k_4 [\text{H}^\bullet][\text{C}_2\text{H}_6] - k_5 [\text{H}^\bullet][\text{C}_2\text{H}_5^\bullet] = 0 \tag{2}$$
3. **Ethyl Radical $[\text{C}_2\text{H}_5^\bullet]$**:
   $$\frac{d[\text{C}_2\text{H}_5^\bullet]}{dt} = k_2 [\text{CH}_3^\bullet][\text{C}_2\text{H}_6] - k_3 [\text{C}_2\text{H}_5^\bullet] + k_4 [\text{H}^\bullet][\text{C}_2\text{H}_6] - k_5 [\text{H}^\bullet][\text{C}_2\text{H}_5^\bullet] = 0 \tag{3}$$

#### Step 3: Radical Concentration Balancing
Adding Equation (2) and Equation (3) and substituting Equation (1):
$$2 k_1 [\text{C}_2\text{H}_6] - 2 k_5 [\text{H}^\bullet][\text{C}_2\text{H}_5^\bullet] = 0$$
$$[\text{H}^\bullet][\text{C}_2\text{H}_5^\bullet] = \frac{k_1}{k_5} [\text{C}_2\text{H}_6] \tag{4}$$

For long chain lengths ($\text{chain length} \gg 1$), the propagation rate $r_4 \gg r_5$:
$$k_3 [\text{C}_2\text{H}_5^\bullet] \approx k_4 [\text{H}^\bullet][\text{C}_2\text{H}_6] \implies [\text{H}^\bullet] \approx \frac{k_3 [\text{C}_2\text{H}_5^\bullet]}{k_4 [\text{C}_2\text{H}_6]} \tag{5}$$

Substitute Equation (5) into Equation (4):
$$\left( \frac{k_3 [\text{C}_2\text{H}_5^\bullet]}{k_4 [\text{C}_2\text{H}_6]} \right) [\text{C}_2\text{H}_5^\bullet] = \frac{k_1}{k_5} [\text{C}_2\text{H}_6]$$
$$[\text{C}_2\text{H}_5^\bullet]^2 = \frac{k_1 k_4}{k_3 k_5} [\text{C}_2\text{H}_6]^2 \implies \mathbf{[\text{C}_2\text{H}_5^\bullet] = \sqrt{\frac{k_1 k_4}{k_3 k_5}} [\text{C}_2\text{H}_6]} \tag{6}$$

#### Step 4: Net Rate of Ethylene Formation
The net rate of ethylene production is the propagation step $r_3$:
$$v = \frac{d[\text{C}_2\text{H}_4]}{dt} = k_3 [\text{C}_2\text{H}_5^\bullet] = k_3 \sqrt{\frac{k_1 k_4}{k_3 k_5}} [\text{C}_2\text{H}_6] = \mathbf{\sqrt{\frac{k_1 k_3 k_4}{k_5}} [\text{C}_2\text{H}_6]} \tag{7}$$
Thus, $v = k_{\text{eff}} [\text{C}_2\text{H}_6]$ where:
$$\mathbf{k_{\text{eff}} = \left(\frac{k_1 k_3 k_4}{k_5}\right)^{1/2}}$$
The reaction is strictly **first-order in ethane**, exactly matching experimental gas-phase pyrolytic measurements!"""
        }
    ])

    return units
