"""
expand_spectroscopy_deep.py
Provides deep quantum mechanical Hamiltonians, selection rule proofs, and mathematical
derivations for all 10 units of Chemical Spectroscopy.
Zero prohibited tokens (no course numbers, no marks, no grades, no exams).
"""

def get_deep_enhancements():
    """
    Returns a dict mapping unit_idx (1..10) to a dict mapping section_idx (0..7)
    to supplementary markdown content that will be appended to the corresponding section.
    """
    deep = {}

    # Unit 1: Second Quantization & Quantum Radiation Field in Section 1 (index 0)
    deep[1] = {
        0: r"""

### Advanced Quantum Theoretical Foundation: Second Quantization of the Radiation Field
To derive the spontaneous and stimulated transition rates from first principles without semi-classical approximations, the electromagnetic radiation field must be treated as a quantized dynamical system.

#### 1. Quantized Vector Potential
In the Coulomb gauge (\(\nabla \cdot \mathbf{A} = 0\)), the vector potential operator \(\hat{\mathbf{A}}(\mathbf{r}, t)\) expanded over plane-wave spatial modes with wavevector \(\mathbf{k}\) and polarization unit vectors \(\boldsymbol{\epsilon}_{\mathbf{k},\lambda}\) (\(\lambda \in \{1, 2\}\)) is expressed in second-quantized form as:
\[
\hat{\mathbf{A}}(\mathbf{r}) = \sum_{\mathbf{k}, \lambda} \sqrt{\frac{\hbar}{2 \epsilon_0 \omega_k V}} \left( \hat{a}_{\mathbf{k},\lambda} \boldsymbol{\epsilon}_{\mathbf{k},\lambda} e^{i \mathbf{k} \cdot \mathbf{r}} + \hat{a}_{\mathbf{k},\lambda}^\dagger \boldsymbol{\epsilon}_{\mathbf{k},\lambda}^* e^{-i \mathbf{k} \cdot \mathbf{r}} \right)
\]
where \(V\) is the quantization cavity volume, \(\omega_k = c|\mathbf{k}|\), and \(\hat{a}_{\mathbf{k},\lambda}\), \(\hat{a}_{\mathbf{k},\lambda}^\dagger\) are the bosonic annihilation and creation operators obeying canonical commutation relations:
\[
[\hat{a}_{\mathbf{k},\lambda}, \hat{a}_{\mathbf{k}',\lambda'}^\dagger] = \delta_{\mathbf{k},\mathbf{k}'} \delta_{\lambda,\lambda'}, \quad [\hat{a}_{\mathbf{k},\lambda}, \hat{a}_{\mathbf{k}',\lambda'}] = 0
\]

#### 2. Radiation Field Hamiltonian and Fock States
The free electromagnetic Hamiltonian corresponds to an infinite set of decoupled harmonic oscillators:
\[
\hat{H}_{\text{rad}} = \sum_{\mathbf{k},\lambda} \hbar \omega_k \left( \hat{a}_{\mathbf{k},\lambda}^\dagger \hat{a}_{\mathbf{k},\lambda} + \frac{1}{2} \right)
\]
Its eigenstates are Fock number states \(|n_{\mathbf{k},\lambda}\rangle\), with eigenvalues:
\[
E_{\text{rad}} = \sum_{\mathbf{k},\lambda} \hbar \omega_k \left( n_{\mathbf{k},\lambda} + \frac{1}{2} \right)
\]
Even in the vacuum state \(|0\rangle\) (\(n_{\mathbf{k},\lambda} = 0\)), the vacuum zero-point energy density \(\frac{1}{2}\hbar\omega_k\) induces vacuum fluctuations:
\[
\langle 0 | \hat{\mathbf{E}}^2 | 0 \rangle = \sum_{\mathbf{k},\lambda} \frac{\hbar \omega_k}{2 \epsilon_0 V} \neq 0
\]
These vacuum electromagnetic fluctuations are the physical driving force behind **spontaneous emission**.

#### 3. Interaction Hamiltonian and Fermi's Golden Rule
For a molecular system with charged particles \(q_j\) and momenta \(\hat{\mathbf{p}}_j\), the total minimal-coupling Hamiltonian is:
\[
\hat{H} = \sum_j \frac{1}{2m_j} [\hat{\mathbf{p}}_j - q_j \hat{\mathbf{A}}(\hat{\mathbf{r}}_j)]^2 + \hat{V}_{\text{Coulomb}} + \hat{H}_{\text{rad}} = \hat{H}_{\text{matter}} + \hat{H}_{\text{rad}} + \hat{H}_{\text{int}}
\]
To first order in \(\hat{\mathbf{A}}\):
\[
\hat{H}_{\text{int}} = -\sum_j \frac{q_j}{m_j} \hat{\mathbf{A}}(\hat{\mathbf{r}}_j) \cdot \hat{\mathbf{p}}_j
\]
In the electric dipole approximation (\(e^{i \mathbf{k}\cdot\mathbf{r}} \approx 1\)), this interaction reduces via the Heisenberg equation of motion \(\hat{\mathbf{p}} = \frac{m}{i\hbar}[\hat{\mathbf{r}}, \hat{H}_0]\) to the electric dipole interaction:
\[
\hat{H}_{\text{int}}^{\text{dipole}} = -\hat{\boldsymbol{\mu}} \cdot \hat{\mathbf{E}}
\]
Applying Fermi's Golden Rule for the transition from initial joint state \(|i\rangle = |\psi_e, n_{\mathbf{k},\lambda}\rangle\) to final state \(|f\rangle = |\psi_g, n_{\mathbf{k},\lambda} + 1\rangle\):
\[
W_{i \rightarrow f} = \frac{2\pi}{\hbar} |\langle f | \hat{H}_{\text{int}} | i \rangle|^2 \rho(E_f)
\]
Since \(\langle n+1 | \hat{a}^\dagger | n \rangle = \sqrt{n+1}\), the squared transition matrix element factors into:
\[
|\langle f | \hat{H}_{\text{int}} | i \rangle|^2 \propto |\langle \psi_g | \hat{\boldsymbol{\mu}} \cdot \boldsymbol{\epsilon} | \psi_e \rangle|^2 \times (n_{\mathbf{k},\lambda} + 1)
\]
- The term proportional to \(n_{\mathbf{k},\lambda}\) describes **stimulated emission** (rate strictly dependent on ambient photon density).
- The term proportional to \(1\) describes **spontaneous emission** (persisting even when \(n_{\mathbf{k},\lambda} = 0\)).
Integrating over the continuous density of vacuum radiation states in three dimensions:
\[
\rho(\omega) d\omega = \frac{V \omega^2}{\pi^2 c^3} d\omega
\]
directly produces Einstein's spontaneous emission rate:
\[
A_{eg} = \frac{\omega_{eg}^3 |\boldsymbol{\mu}_{ge}|^2}{3 \pi \epsilon_0 \hbar c^3}
\]
which proves Einstein's \(A\) and \(B\) coefficient relationship purely from quantum electrodynamic principles."""
    }

    # Unit 2: Watson's Effective Rotational Hamiltonian in Section 2 (index 1)
    deep[2] = {
        1: r"""

### Advanced Mathematical Formulation: Watson's Reduced Asymmetric Rotor Hamiltonians
For a general asymmetric top molecule (\(I_A \neq I_B \neq I_C\)), the centrifugal distortion cannot be described by simple scalar constants \(D_J\). Instead, centrifugal distortion couples angular momentum operators of higher even powers.

#### 1. The Quartic Centrifugal Distortion Hamiltonian
The unreduced effective rotational Hamiltonian up to fourth order in angular momentum is:
\[
\hat{H}_{\text{rot}} = X \hat{J}_x^2 + Y \hat{J}_y^2 + Z \hat{J}_z^2 + \frac{1}{4} \sum_{\alpha,\beta,\gamma,\delta} \tau_{\alpha\beta\gamma\delta} \hat{J}_\alpha \hat{J}_\beta \hat{J}_\gamma \hat{J}_\delta
\]
where \(\alpha, \beta, \gamma, \delta \in \{x, y, z\}\).
Because the components of total angular momentum do not commute (\([\hat{J}_x, \hat{J}_y] = -i\hbar \hat{J}_z\)), there exist linear dependencies among the 81 \(\tau\) coefficients. Symmetrization leaves nine independent quartic centrifugal distortion coefficients.

#### 2. Watson's Unitary Contact Transformation
To eliminate indeterminacy and produce a hermitian Hamiltonian with minimal parameters that can be unambiguously fitted to observed microwave spectra, J. K. G. Watson applied an operator unitary transformation:
\[
\tilde{H} = e^{i \hat{S}} \hat{H} e^{-i \hat{S}} = \hat{H} + i [\hat{S}, \hat{H}] - \frac{1}{2} [\hat{S}, [\hat{S}, \hat{H}]] + \dots
\]
where \(\hat{S}\) is an odd hermitian operator of third degree in \(\hat{J}_\alpha\). Depending on the molecular symmetry and prolate/oblate character, two standardized reductions are employed:

**Watson's \(A\)-Reduction (Asymmetric Reduction):**
\[
\hat{H}^{(A)} = \frac{1}{2}(B + C) \hat{\mathbf{J}}^2 + \left[A - \frac{1}{2}(B + C)\right] \hat{J}_z^2 + \frac{1}{2}(B - C) (\hat{J}_x^2 - \hat{J}_y^2)
\]
\[
- \Delta_J \hat{\mathbf{J}}^4 - \Delta_{JK} \hat{\mathbf{J}}^2 \hat{J}_z^2 - \Delta_K \hat{J}_z^4 - 2 \delta_J \hat{\mathbf{J}}^2 (\hat{J}_x^2 - \hat{J}_y^2) - \delta_K \left[ \hat{J}_z^2 (\hat{J}_x^2 - \hat{J}_y^2) + (\hat{J}_x^2 - \hat{J}_y^2) \hat{J}_z^2 \right]
\]
where the 5 Watson quartic constants \(\Delta_J, \Delta_{JK}, \Delta_K, \delta_J, \delta_K\) represent:
- \(\Delta_J\): Isotropic centrifugal stretching.
- \(\Delta_{JK}\): Cross-coupling between total rotation and axial rotation.
- \(\Delta_K\): Centrifugal expansion along the principal symmetry axis.
- \(\delta_J, \delta_K\): Asymmetry-splitting centrifugal modulations.

**Watson's \(S\)-Reduction (Symmetric Reduction):**
Preferred for near-spherical or accidental symmetric tops where \(\delta_K\) in the \(A\)-reduction becomes ill-conditioned:
\[
\hat{H}^{(S)} = \frac{1}{2}(B + C) \hat{\mathbf{J}}^2 + \left[A - \frac{1}{2}(B + C)\right] \hat{J}_z^2 + \frac{1}{2}(B - C) (\hat{J}_x^2 - \hat{J}_y^2)
\]
\[
- D_J \hat{\mathbf{J}}^4 - D_{JK} \hat{\mathbf{J}}^2 \hat{J}_z^2 - D_K \hat{J}_z^4 + d_1 \hat{\mathbf{J}}^2 (\hat{J}_+^2 + \hat{J}_-^2) + d_2 (\hat{J}_+^4 + \hat{J}_-^4)
\]

#### 3. Matrix Representation in the Symmetric Top Basis \(|J, K, M\rangle\)
The matrix elements are evaluated analytically:
\[
\langle J, K | \hat{\mathbf{J}}^2 | J, K \rangle = J(J+1)
\]
\[
\langle J, K | \hat{J}_z^2 | J, K \rangle = K^2
\]
\[
\langle J, K \pm 2 | (\hat{J}_x^2 - \hat{J}_y^2) | J, K \rangle = \frac{1}{2} \sqrt{ [J(J+1) - K(K \pm 1)] [J(J+1) - (K \pm 1)(K \pm 2)] }
\]
Diagonalization of this tridiagonal band matrix yields the exact rovibrational rotational energy eigenvalues with sub-kHz precision."""
    }

    # Unit 3: Dunham Expansion and Anharmonic Potential Inversion in Section 2 (index 1)
    deep[3] = {
        1: r"""

### Advanced Mathematical Formulation: Dunham Expansion and the RKR Potential Inversion
Beyond simple second-order Morse potential expansions, high-resolution rovibrational transitions spanning dozens of vibrational levels require Dunham's semiclassical representation of diatomic energy levels.

#### 1. The Dunham Series Expansion
J. L. Dunham expressed the rovibrational term values \(T(v, J)\) as a double power series in \((v + 1/2)\) and \(J(J+1)\):
\[
T(v, J) = \sum_{l=0}^\infty \sum_{j=0}^\infty Y_{lj} \left( v + \frac{1}{2} \right)^l [J(J+1)]^j
\]
where \(Y_{lj}\) are the Dunham coefficients.
The leading Dunham coefficients relate directly to standard spectroscopic constants:
\[
Y_{10} \approx \omega_e + \frac{B_e^3}{4\omega_e^2} (a_1^2 \dots) \approx \omega_e
\]
\[
Y_{20} \approx -\omega_e x_e
\]
\[
Y_{01} \approx B_e
\]
\[
Y_{11} \approx -\alpha_e
\]
\[
Y_{02} \approx -D_e = -\frac{4 B_e^3}{\omega_e^2}
\]

#### 2. The Dimensionless Born-Oppenheimer Potential
The internuclear potential is written in terms of the dimensionless reduced coordinate \(\xi = \frac{R - R_e}{R_e}\):
\[
V(\xi) = a_0 \xi^2 \left( 1 + a_1 \xi + a_2 \xi^2 + a_3 \xi^3 + \dots \right)
\]
where \(a_0 = \frac{\omega_e^2}{4 B_e}\). Dunham derived explicit analytical expressions connecting the potential coefficients \(a_k\) to the spectroscopic constants:
\[
a_1 = -1 - \frac{\alpha_e \omega_e}{6 B_e^2}
\]
\[
a_2 = \frac{5}{4} a_1^2 - \frac{2 \omega_e x_e}{3 B_e}
\]

#### 3. Semiclassical Rydberg-Klein-Rees (RKR) Inversion
The RKR method utilizes the Bohr-Sommerfeld WKB quantization condition to directly determine the classical turning points \(R_{\text{min}}(v)\) and \(R_{\text{max}}(v)\) from experimental \(G(v)\) and \(B_v\) data without assuming an analytical potential shape:
\[
R_{\text{max}}(v) - R_{\text{min}}(v) = 2 f(v) = 2 \sqrt{\frac{\hbar}{2\pi \mu c}} \int_{-1/2}^v \frac{dv'}{\sqrt{G(v) - G(v')}}
\]
\[
\frac{1}{R_{\text{min}}(v)} - \frac{1}{R_{\text{max}}(v)} = 2 g(v) = 2 \sqrt{\frac{2\pi \mu c}{\hbar}} \int_{-1/2}^v \frac{B_{v'}}{\sqrt{G(v) - G(v')}} dv'
\]
Solving these two simultaneous algebraic relations gives:
\[
R_{\text{min}}(v) = \sqrt{f(v)^2 + \frac{f(v)}{g(v)}} - f(v)
\]
\[
R_{\text{max}}(v) = \sqrt{f(v)^2 + \frac{f(v)}{g(v)}} + f(v)
\]
This inversion algorithm constructs the true quantum potential energy curve \(V(R)\) directly from high-resolution IR Fourier-transform spectra."""
    }

    # Unit 4: Kramers-Heisenberg-Dirac Raman Tensor in Section 1 (index 0)
    deep[4] = {
        0: r"""

### Advanced Quantum Formalism: Kramers-Heisenberg-Dirac (KHD) Raman Scattering Tensor
To understand Raman scattering beyond the classical polarizability derivative model, second-order time-dependent perturbation theory must be applied to the matter-field interaction.

#### 1. Derivation of the Transition Polarizability Tensor
When an incident photon of frequency \(\omega_L\) and polarization unit vector \(\mathbf{e}_i\) scatters inelastically into a scattered photon of frequency \(\omega_S\) and polarization \(\mathbf{e}_s\), the transition polarizability tensor \([\alpha_{\rho\sigma}]_{fi}\) between initial state \(|i\rangle\) and final state \(|f\rangle\) is given by the Kramers-Heisenberg-Dirac (KHD) dispersion formula:
\[
[\alpha_{\rho\sigma}]_{fi} = \frac{1}{\hbar} \sum_v \left[ \frac{\langle f | \hat{\mu}_\rho | v \rangle \langle v | \hat{\mu}_\sigma | i \rangle}{\omega_{vi} - \omega_L - i \Gamma_v} + \frac{\langle f | \hat{\mu}_\sigma | v \rangle \langle v | \hat{\mu}_\rho | i \rangle}{\omega_{vf} + \omega_L + i \Gamma_v} \right]
\]
where:
- \(|v\rangle\) represents all intermediate vibronic eigenstates of the molecule.
- \(\hbar \omega_{vi} = E_v - E_i\) is the transition energy from initial state to intermediate state.
- \(\Gamma_v\) is the homogeneous damping width (finite lifetime) of state \(|v\rangle\).
- \(\hat{\mu}_\rho, \hat{\mu}_\sigma\) are the Cartesian components of the electric dipole moment operator.

#### 2. The Albrecht A, B, and C Terms in Resonance Raman Spectroscopy
Applying the Born-Oppenheimer adiabatic approximation and expanding the electronic transition dipole moment \(\mathbf{M}_{eg}(Q)\) in a Taylor series along normal coordinate \(Q_k\) (Herzberg-Teller expansion):
\[
\mathbf{M}_{eg}(Q) = \mathbf{M}_{eg}^0 + \sum_k \left( \frac{\partial \mathbf{M}_{eg}}{\partial Q_k} \right)_0 Q_k + \dots
\]
The transition polarizability decomposes into three distinct mechanisms:
\[
[\alpha]_{fi} = A + B + C
\]

1. **Albrecht \(A\)-Term (Franck-Condon Scattering):**
   \[
   A = \frac{(\mathbf{M}_{eg}^0)^2}{\hbar} \sum_{v_e} \frac{\langle f_g | v_e \rangle \langle v_e | i_g \rangle}{\omega_{v_e, i_g} - \omega_L - i \Gamma_{v_e}}
   \]
   - Driven by the zero-order transition dipole moment and Franck-Condon vibrational overlap integrals.
   - Dominates when \(\omega_L\) approaches an electric-dipole allowed electronic transition (\(\mathbf{M}_{eg}^0 \neq 0\)).
   - Exclusively enhances **totally symmetric vibrations** that experience excited-state geometric displacement (\(\Delta \neq 0\)).

2. **Albrecht \(B\)-Term (Herzberg-Teller Vibronic Coupling):**
   \[
   B = \frac{\mathbf{M}_{eg}^0}{\hbar} \left( \frac{\partial \mathbf{M}_{es}^0}{\partial Q_k} \right)_0 \sum_{v_e} \frac{\langle f_g | Q_k | v_e \rangle \langle v_e | i_g \rangle + \langle f_g | v_e \rangle \langle v_e | Q_k | i_g \rangle}{\omega_{v_e, i_g} - \omega_L - i \Gamma_{v_e}}
   \]
   - Involves vibronic mixing between two excited electronic states \(|e\rangle\) and \(|s\rangle\) mediated by non-totally symmetric vibrational modes.
   - Activates non-totally symmetric modes (e.g., \(b_{1g}, b_{2g}, e_u\) in porphyrins and metalloproteins) under resonance conditions.

3. **Albrecht \(C\)-Term:**
   - Involves vibronic coupling in the ground state manifold; typically negligible compared to \(A\) and \(B\) terms.

This rigorous quantum framework underpins modern resonance Raman characterization of metalloenzyme active sites, chromophores, and 2D conjugated materials."""
    }

    # Unit 5: Wigner-Eckart Theorem and Breit-Rabi Equation in Section 2 (index 1)
    deep[5] = {
        1: r"""

### Advanced Quantum Formalism: Wigner-Eckart Theorem and the Breit-Rabi Equation
In atomic spectroscopy, calculating transition intensities and magnetic shifts across arbitrary coupling regimes requires angular momentum tensor algebra.

#### 1. The Wigner-Eckart Theorem for Electric Dipole Transitions
The electric dipole operator is an irreducible spherical tensor of rank 1: \(\hat{T}_q^{(1)} = \hat{\mu}_q\), where \(q \in \{0, \pm 1\}\).
The Wigner-Eckart theorem states that the matrix element of any spherical tensor operator factors cleanly into a geometrical Clebsch-Gordan coefficient (or Wigner 3-\(j\) symbol) and a dynamical **reduced matrix element**:
\[
\langle \gamma J M | \hat{T}_q^{(k)} | \gamma' J' M' \rangle = (-1)^{J - M} \begin{pmatrix} J & k & J' \\ -M & q & M' \end{pmatrix} \langle \gamma J || \hat{T}^{(k)} || \gamma' J' \rangle
\]
Consequences for spectroscopic transitions (\(k = 1\)):
- **Triangular condition:** \(|J - J'| \le 1 \le J + J' \implies \Delta J = 0, \pm 1\) (with \(J = 0 \not\rightarrow J' = 0\)).
- **Magnetic projection:** \(-M + q + M' = 0 \implies \Delta M = M - M' = q \in \{0, \pm 1\}\).
- All relative line intensities within a multiplet or Zeeman pattern are governed entirely by the geometric Wigner 3-\(j\) symbols, leaving the intrinsic electronic radial overlap locked inside \(\langle \gamma J || \hat{\mathbf{r}} || \gamma' J' \rangle\).

#### 2. The Breit-Rabi Equation: Intermediate Magnetic Field Splitting
When an external magnetic field \(B_0\) is neither strictly weak (Zeeman limit, \(g_F \mu_B B_0 \ll A_{\text{hfs}}\)) nor strictly strong (Paschen-Back limit, \(\mu_B B_0 \gg A_{\text{hfs}}\)), the hyperfine Hamiltonian:
\[
\hat{H} = A_{\text{hfs}} \hat{\mathbf{I}} \cdot \hat{\mathbf{J}} + g_J \mu_B B_0 \hat{J}_z + g_I \mu_N B_0 \hat{I}_z
\]
can be solved analytically for any atom with electronic angular momentum \(J = 1/2\) (such as alkali ground states \(^2S_{1/2}\)) using the **Breit-Rabi formula**:
\[
E(F, M_F) = -\frac{\Delta E_{\text{hfs}}}{2(2I + 1)} + g_I \mu_N B_0 M_F \pm \frac{\Delta E_{\text{hfs}}}{2} \sqrt{1 + \frac{4 M_F}{2I + 1} x + x^2}
\]
where:
- \(\Delta E_{\text{hfs}} = A_{\text{hfs}} \left( I + \frac{1}{2} \right)\) is the zero-field hyperfine splitting.
- \(x\) is the dimensionless magnetic field parameter:
  \[
  x = \frac{(g_J \mu_B - g_I \mu_N) B_0}{\Delta E_{\text{hfs}}} \approx \frac{g_J \mu_B B_0}{\Delta E_{\text{hfs}}}
  \]
- The plus sign applies to the upper hyperfine manifold \(F = I + 1/2\), and the minus sign applies to the lower manifold \(F = I - 1/2\).

**Limiting Behaviors:**
1. **Low-field limit (\(x \ll 1\)):**
   Expanding the square root via Taylor series:
   \[
   \sqrt{1 + \frac{4 M_F}{2I + 1} x + x^2} \approx 1 + \frac{2 M_F}{2I+1} x + \mathcal{O}(x^2)
   \]
   reproduces linear Zeeman splitting with \(g_F \approx \frac{g_J}{2I+1}\).
2. **High-field limit (\(x \gg 1\)):**
   The square root approaches \(x + \frac{2 M_F}{2I+1}\), decoupling \(\mathbf{I}\) and \(\mathbf{J}\) into linear Paschen-Back states with energies \(g_J \mu_B B_0 M_J + A_{\text{hfs}} M_I M_J\)."""
    }

    # Unit 6: Conical Intersections and Vibronic Hamiltonians in Section 3 (index 2)
    deep[6] = {
        2: r"""

### Advanced Quantum Formalism: Conical Intersections and Non-Adiabatic Derivative Coupling
The Breakdown of the Born-Oppenheimer approximation is paramount in modern photochemistry and molecular electronic spectroscopy.

#### 1. The Non-Adiabatic Coupling Vector
The total molecular wavefunction in the adiabatic electronic representation is:
\[
\Psi(\mathbf{r}, \mathbf{R}) = \sum_n \psi_n(\mathbf{r}; \mathbf{R}) \chi_n(\mathbf{R})
\]
Applying the nuclear kinetic energy operator \(\hat{T}_{\mathbf{N}} = -\sum_k \frac{\hbar^2}{2 M_k} \nabla_{\mathbf{R}_k}^2\) yields coupled differential equations for the nuclear wavefunctions \(\chi_n\):
\[
\left[ -\frac{\hbar^2}{2M} \nabla_{\mathbf{R}}^2 + E_n(\mathbf{R}) \right] \chi_n(\mathbf{R}) - \frac{\hbar^2}{2M} \sum_m \left[ 2 \mathbf{F}_{nm}(\mathbf{R}) \cdot \nabla_{\mathbf{R}} + G_{nm}(\mathbf{R}) \right] \chi_m(\mathbf{R}) = E \chi_n(\mathbf{R})
\]
where the **first-order non-adiabatic derivative coupling vector** is:
\[
\mathbf{F}_{nm}(\mathbf{R}) = \langle \psi_n | \nabla_{\mathbf{R}} | \psi_m \rangle_{\mathbf{r}} = \frac{\langle \psi_n | [\nabla_{\mathbf{R}} \hat{H}_{\text{elec}}] | \psi_m \rangle}{E_m(\mathbf{R}) - E_n(\mathbf{R})}
\]
Notice that as two adiabatic electronic surfaces approach degeneracy (\(E_m(\mathbf{R}) \rightarrow E_n(\mathbf{R})\)), the coupling \(\mathbf{F}_{nm}(\mathbf{R})\) diverges to infinity, rendering the Born-Oppenheimer approximation completely invalid.

#### 2. The Branching Space of a Conical Intersection
At a conical intersection (CoIn), two adiabatic potential energy surfaces become strictly degenerate in a subspace of the \(3N-6\) vibrational coordinates.
The degeneracy is lifted linearly in a 2-dimensional subspace termed the **branching space** spanned by:
1. **Tuning Vector (\(\mathbf{g}\)):**
   \[
   \mathbf{g} = \frac{1}{2} \nabla_{\mathbf{R}} \left( E_1(\mathbf{R}) - E_2(\mathbf{R}) \right)
   \]
   which tunes the energy difference between the two electronic states.
2. **Coupling Vector (\(\mathbf{h}\)):**
   \[
   \mathbf{h} = \langle \psi_1 | \nabla_{\mathbf{R}} \hat{H}_{\text{elec}} | \psi_2 \rangle
   \]
   which couples the two electronic states vibronically.

Expanding the diabatic \(2 \times 2\) Hamiltonian matrix in local coordinates \(x = \mathbf{g} \cdot \mathbf{R}\) and \(y = \mathbf{h} \cdot \mathbf{R}\):
\[
\mathbf{H}_{\text{diab}}(x, y) = \begin{pmatrix} \bar{E} + \kappa_x x & \lambda_y y \\ \lambda_y y & \bar{E} - \kappa_x x \end{pmatrix}
\]
The adiabatic eigenvalues are:
\[
E_\pm(x, y) = \bar{E} \pm \sqrt{\kappa_x^2 x^2 + \lambda_y^2 y^2}
\]
Plotting \(E_\pm\) versus \(x\) and \(y\) reveals a double cone touching at a single singular vertex: the **conical intersection**.

#### 3. Geometric Phase (Berry Phase)
When a nuclear wavepacket encircles the conical intersection along a closed path \(C\) in the branching space, the electronic adiabatic wavefunction accumulates a sign change:
\[
\psi_{\text{ad}}(\mathbf{r}; \mathbf{R}) \xrightarrow{\oint_C} -\psi_{\text{ad}}(\mathbf{r}; \mathbf{R}) = e^{i \pi} \psi_{\text{ad}}(\mathbf{r}; \mathbf{R})
\]
This topological Berry phase of \(\pi\) forces the nuclear wavefunction \(\chi(\mathbf{R})\) to also change sign to preserve single-valuedness of the total state, creating destructive quantum interference that dictates ultrafast, radiationless funneling in vision (rhodopsin isomerization in 200 fs) and DNA photoprotection."""
    }

    # Unit 7: Marcus Electron Transfer Theory in Section 2 (index 1)
    deep[7] = {
        1: r"""

### Advanced Photophysical Theory: Quantum and Semiclassical Marcus Theory of Photoinduced Electron Transfer
Photoinduced electron transfer (PET) is a ubiquitous deactivation pathway competing directly with fluorescence and phosphorescence in molecular triads and photocatalytic systems.

#### 1. Semiclassical Marcus Free Energy Expression
In the dielectric continuum framework developed by Rudolph A. Marcus, reactants and products are described by intersecting parabolic free energy surfaces:
\[
G_R(q) = \frac{1}{2} k q^2
\]
\[
G_P(q) = \frac{1}{2} k (q - q_0)^2 + \Delta G_{\text{ET}}^\circ
\]
The reorganization energy \(\lambda\) is the free energy required to distort the reactant nuclear coordinates to the equilibrium geometry of the product state without transferring the electron:
\[
\lambda = \frac{1}{2} k q_0^2 = \lambda_i + \lambda_o
\]
- \(\lambda_i\): Inner-sphere reorganization energy (bond length changes in donor and acceptor).
- \(\lambda_o\): Outer-sphere reorganization energy (solvent dipole reorientation), given in a dielectric continuum of optical dielectric constant \(\epsilon_{\text{op}} = n^2\) and static dielectric constant \(\epsilon_s\) by:
  \[
  \lambda_o = \frac{e^2}{4\pi \epsilon_0} \left( \frac{1}{2 r_D} + \frac{1}{2 r_A} - \frac{1}{R_{DA}} \right) \left( \frac{1}{\epsilon_{\text{op}}} - \frac{1}{\epsilon_s} \right)
  \]
Setting \(G_R(q^\ddagger) = G_P(q^\ddagger)\) yields the famous Marcus activation barrier:
\[
\Delta G^\ddagger = \frac{(\Delta G_{\text{ET}}^\circ + \lambda)^2}{4\lambda}
\]
The rate constant for non-adiabatic electron transfer is given by:
\[
k_{\text{ET}} = \frac{2\pi}{\hbar} |V_{\text{el}}|^2 \frac{1}{\sqrt{4\pi \lambda k_B T}} \exp\left[ -\frac{(\Delta G_{\text{ET}}^\circ + \lambda)^2}{4\lambda k_B T} \right]
\]
where \(V_{\text{el}}\) is the electronic donor-acceptor coupling matrix element.

#### 2. The Marcus Inverted Region
As the driving force \(-\Delta G_{\text{ET}}^\circ\) becomes increasingly exergonic:
1. **Normal Region (\(-\Delta G_{\text{ET}}^\circ < \lambda\)):**
   \(\Delta G^\ddagger > 0\). Increasing exergonicity lowers the barrier and increases \(k_{\text{ET}}\).
2. **Activationless Point (\(-\Delta G_{\text{ET}}^\circ = \lambda\)):**
   \(\Delta G^\ddagger = 0\). The rate constant reaches its maximum value \(k_{\text{ET}}^{\text{max}} = \frac{2\pi}{\hbar} \frac{|V_{\text{el}}|^2}{\sqrt{4\pi \lambda k_B T}}\).
3. **Inverted Region (\(-\Delta G_{\text{ET}}^\circ > \lambda\)):**
   The potential parabolic curves intersect on the left side of the minimum! Further increase in thermodynamic driving force **increases** the activation barrier \(\Delta G^\ddagger\) and dramatically **slows down** the electron transfer rate.

This counterintuitive Marcus inverted behavior is essential in natural photosynthesis: charge recombination from the special pair to quinone acceptors is situated deep in the inverted region, suppressing wasteful back-electron transfer and ensuring near-unity quantum efficiency."""
    }

    # Unit 8: Product Operator Formalism in Section 5 (index 4)
    deep[8] = {
        4: r"""

### Advanced Quantum Formalism: Product Operator Formalism for Two-Spin Systems
For multi-pulse and multidimensional NMR experiments, vector models fail whenever spin-spin scalar coupling \(J\) or quantum coherence transfer is involved. The rigorous description requires the density matrix and **product operator formalism**.

#### 1. Basis Operators for a Two-Spin System (\(I = 1/2, S = 1/2\))
The 16 orthogonal Cartesian product operators spanning Liouville space are:
\[
\frac{1}{2}\hat{E}, \quad \hat{I}_x, \hat{I}_y, \hat{I}_z, \quad \hat{S}_x, \hat{S}_y, \hat{S}_z, \quad 2\hat{I}_x\hat{S}_z, 2\hat{I}_y\hat{S}_z, 2\hat{I}_z\hat{S}_x, 2\hat{I}_z\hat{S}_y, \dots, 4\hat{I}_x\hat{S}_x\dots
\]
Physical significance:
- \(\hat{I}_z, \hat{S}_z\): Longitudinal polarization (Zeeman magnetization).
- \(\hat{I}_x, \hat{I}_y\): Single-quantum in-phase coherence (observable transverse magnetization).
- \(2\hat{I}_x\hat{S}_z, 2\hat{I}_y\hat{S}_z\): Single-quantum anti-phase coherence (multiplet components with opposite phase).
- \(2\hat{I}_x\hat{S}_x, 2\hat{I}_x\hat{S}_y\): Multiple-quantum coherences (zero-quantum and double-quantum coherences, strictly invisible to direct detection).

#### 2. The Three Fundamental Evolution Rotations
The time evolution of the density operator under any interaction Hamiltonian \(\hat{H}\) is governed by the Liouville-von Neumann equation:
\[
\hat{\sigma}(t) = \exp\left(-\frac{i \hat{H} t}{\hbar}\right) \hat{\sigma}(0) \exp\left(\frac{i \hat{H} t}{\hbar}\right)
\]

1. **Chemical Shift Evolution (\(\hat{H}_{\text{CS}} = \Omega_I \hat{I}_z\)):**
   \[
   \hat{I}_x \xrightarrow{\Omega_I t \hat{I}_z} \hat{I}_x \cos(\Omega_I t) + \hat{I}_y \sin(\Omega_I t)
   \]
   \[
   \hat{I}_y \xrightarrow{\Omega_I t \hat{I}_z} \hat{I}_y \cos(\Omega_I t) - \hat{I}_x \sin(\Omega_I t)
   \]

2. **Scalar Coupling Evolution (\(\hat{H}_J = 2\pi J \hat{I}_z \hat{S}_z\)):**
   \[
   \hat{I}_x \xrightarrow{\pi J t 2\hat{I}_z\hat{S}_z} \hat{I}_x \cos(\pi J t) + 2\hat{I}_y\hat{S}_z \sin(\pi J t)
   \]
   \[
   2\hat{I}_y\hat{S}_z \xrightarrow{\pi J t 2\hat{I}_z\hat{S}_z} 2\hat{I}_y\hat{S}_z \cos(\pi J t) + \hat{I}_x \sin(\pi J t)
   \]
   At \(t = \frac{1}{2J}\) (\(\pi J t = \pi/2\)), total conversion of in-phase into anti-phase coherence occurs:
   \[
   \hat{I}_x \rightarrow 2\hat{I}_y\hat{S}_z
   \]

3. **Radiofrequency Pulse Rotations (Flip angle \(\beta\) along axis \(x\) or \(y\)):**
   \[
   \hat{I}_z \xrightarrow{\beta \hat{I}_x} \hat{I}_z \cos\beta - \hat{I}_y \sin\beta
   \]
   \[
   2\hat{I}_y\hat{S}_z \xrightarrow{(\pi/2)\hat{S}_x} -2\hat{I}_y\hat{S}_y \quad (\text{double-quantum / zero-quantum coherence})
   \]

This algebra enables exact closed-form tracking of any arbitrary multi-dimensional NMR pulse sequence without numerical matrix integration."""
    }

    # Unit 9: Density Matrix Coherence Pathway in Section 2 (index 1)
    deep[9] = {
        1: r"""

### Advanced 2D NMR Theory: Complete Product Operator Tracking of the 2D COSY Experiment
To demonstrate how two-dimensional homonuclear correlation works at the quantum level, consider two scalar-coupled spins \(I\) and \(S\) with scalar coupling constant \(J\) in a Homonuclear Correlation Spectroscopy (COSY) sequence:
\[
\left(\frac{\pi}{2}\right)_x - t_1 - \left(\frac{\pi}{2}\right)_x - t_2\text{ (detection)}
\]

#### 1. Equilibrium to First Pulse
Thermal equilibrium density matrix:
\[
\hat{\sigma}_0 = \hat{I}_z + \hat{S}_z
\]
Applying the first non-selective \(90_x^\circ\) pulse:
\[
\hat{\sigma}_0 \xrightarrow{(\pi/2)(\hat{I}_x + \hat{S}_x)} -\hat{I}_y - \hat{S}_y
\]

#### 2. Evolution during Evolution Period \(t_1\)
Tracking the \(\hat{I}\) spin components under chemical shift \(\Omega_I\) and coupling \(\pi J t_1\):
\[
-\hat{I}_y \xrightarrow{\Omega_I t_1 \hat{I}_z} -\hat{I}_y \cos(\Omega_I t_1) + \hat{I}_x \sin(\Omega_I t_1)
\]
Now letting scalar coupling evolve:
\[
-\hat{I}_y \cos(\Omega_I t_1) \xrightarrow{\pi J t_1 2\hat{I}_z\hat{S}_z} -\hat{I}_y \cos(\pi J t_1) \cos(\Omega_I t_1) + 2\hat{I}_x\hat{S}_z \sin(\pi J t_1) \cos(\Omega_I t_1)
\]
\[
+\hat{I}_x \sin(\Omega_I t_1) \xrightarrow{\pi J t_1 2\hat{I}_z\hat{S}_z} +\hat{I}_x \cos(\pi J t_1) \sin(\Omega_I t_1) + 2\hat{I}_y\hat{S}_z \sin(\pi J t_1) \sin(\Omega_I t_1)
\]

#### 3. Action of the Second Mixing Pulse \((90_x^\circ)\)
The second \(90_x^\circ\) pulse transforms each operator:
- \(\hat{I}_x \rightarrow \hat{I}_x\)
- \(\hat{I}_y \rightarrow \hat{I}_z\) (longitudinal, unobservable during \(t_2\))
- \(2\hat{I}_x\hat{S}_z \xrightarrow{(\pi/2)(\hat{I}_x + \hat{S}_x)} -2\hat{I}_x\hat{S}_y\) (multiple quantum, unobservable)
- \(2\hat{I}_y\hat{S}_z \xrightarrow{(\pi/2)(\hat{I}_x + \hat{S}_x)} 2\hat{I}_z(-\hat{S}_y) = -2\hat{I}_z\hat{S}_y\)

#### 4. The Origin of Cross-Peaks and Diagonal Peaks
Observe the term \(-2\hat{I}_z\hat{S}_y\)!
The coherence initially labeled by the chemical shift of spin \(I\) (\(\sin(\Omega_I t_1)\)) has been transferred to **spin \(S\)**:
\[
\hat{\sigma}_{\text{transferred}} = -2\hat{I}_z\hat{S}_y \sin(\Omega_I t_1) \sin(\pi J t_1)
\]
During the detection period \(t_2\), this anti-phase coherence evolves under the chemical shift of **spin \(S\)** (\(\Omega_S\)):
\[
-2\hat{I}_z\hat{S}_y \xrightarrow{\pi J t_2 2\hat{I}_z\hat{S}_z} \hat{S}_x \sin(\pi J t_2)
\]
\[
\xrightarrow{\Omega_S t_2 \hat{S}_z} \hat{S}_x \cos(\Omega_S t_2) \sin(\pi J t_2) + \dots
\]
The 2D Fourier transform across \(t_1\) and \(t_2\) produces:
- **Diagonal peaks:** Modulated by \(\cos(\Omega_I t_1)\) and detected at \(\Omega_I\) (frequency \(\omega_1 = \Omega_I, \omega_2 = \Omega_I\)).
- **Cross-peaks:** Modulated by \(\sin(\Omega_I t_1)\) during \(t_1\) and detected at \(\Omega_S\) during \(t_2\) (frequency \(\omega_1 = \Omega_I, \omega_2 = \Omega_S\)) with an antiphase multiplet structure!
This algebraic derivation rigorously proves that cross-peaks can appear in a COSY spectrum if and only if the scalar coupling between the two spins is strictly non-zero (\(J \neq 0\))."""
    }

    # Unit 10: Zero-Field Splitting and Kramers Theorem in Section 1 (index 0)
    deep[10] = {
        0: r"""

### Advanced Quantum Formalism: Spin Hamiltonian Formalism, Zero-Field Splitting, and Kramers Theorem
For paramagnetic transition metal ions and actinide complexes with \(S \ge 1\), the electronic Zeeman interaction is strongly perturbed by spin-orbit coupling and ligand-field asymmetry.

#### 1. The Effective Spin Hamiltonian
By projecting the coupled orbital and spin states onto the lowest spin-multiplet manifold, the effective spin Hamiltonian is written:
\[
\hat{H}_S = \mu_B \mathbf{B}_0 \cdot \mathbf{g} \cdot \hat{\mathbf{S}} + \hat{\mathbf{S}} \cdot \mathbf{D} \cdot \hat{\mathbf{S}} + \sum_i \hat{\mathbf{S}} \cdot \mathbf{A}_i \cdot \hat{\mathbf{I}}_i + \sum_i \hat{\mathbf{I}}_i \cdot \mathbf{P}_i \cdot \hat{\mathbf{I}}_i - \sum_i g_{N,i} \mu_N \mathbf{B}_0 \cdot \hat{\mathbf{I}}_i
\]
where \(\mathbf{D}\) is the symmetric, traceless **Zero-Field Splitting (ZFS)** tensor.

#### 2. Canonical Parameterization of Zero-Field Splitting
In its principal axis coordinate system, \(\mathbf{D}\) is parameterized by two scalar parameters:
\[
D = \frac{3}{2} D_{zz}, \quad E = \frac{1}{2}(D_{xx} - D_{yy})
\]
yielding the standard ZFS Hamiltonian:
\[
\hat{H}_{\text{ZFS}} = D \left( \hat{S}_z^2 - \frac{1}{3} S(S+1) \right) + E (\hat{S}_x^2 - \hat{S}_y^2)
\]
- \(D\) represents the axial zero-field splitting parameter.
- \(E\) represents the rhombic (orthorhombic) distortion parameter, strictly constrained to \(0 \le |E/D| \le 1/3\).

#### 3. Kramers Degeneracy Theorem and Half-Integer Spins
H. A. Kramers proved that for any quantum system with an **odd number of electrons** (half-integer total spin \(S = 1/2, 3/2, 5/2, \dots\)), every energy level is at least doubly degenerate in the absence of an external magnetic field.
**Proof:**
The time-reversal operator \(\hat{\Theta}\) is anti-unitary:
\[
\hat{\Theta} = \hat{K} \exp\left(-\frac{i \pi \hat{S}_y}{\hbar}\right)
\]
For half-integer spin, \(\hat{\Theta}^2 = -1\).
If \(|\psi\rangle\) is an eigenstate of the field-free Hamiltonian \(\hat{H}_0\) with energy \(E\):
\[
\hat{H}_0 (\hat{\Theta} |\psi\rangle) = \hat{\Theta} \hat{H}_0 |\psi\rangle = E (\hat{\Theta} |\psi\rangle)
\]
Suppose \(|\psi\rangle\) and \(\hat{\Theta}|\psi\rangle\) were linearly dependent: \(\hat{\Theta}|\psi\rangle = c|\psi\rangle\).
Then:
\[
\hat{\Theta}^2 |\psi\rangle = \hat{\Theta}(c|\psi\rangle) = c^* \hat{\Theta}|\psi\rangle = c^* c |\psi\rangle = |c|^2 |\psi\rangle
\]
Since \(|c|^2 \ge 0\), this directly contradicts \(\hat{\Theta}^2 = -1\).
Therefore, \(|\psi\rangle\) and \(\hat{\Theta}|\psi\rangle\) must be strictly orthogonal and distinct:
\[
\langle \psi | \hat{\Theta} \psi \rangle = 0
\]
This guarantees that **Kramers doublets** cannot be split by any electric field or crystal field distortion of arbitrary low symmetry. An external magnetic field \(\mathbf{B}_0\) (which breaks time-reversal symmetry) is strictly required to lift the degeneracy, ensuring that half-integer spin systems (e.g., \(\text{Fe}^{3+}\) \(S=5/2\), \(\text{Cu}^{2+}\) \(S=1/2\), \(\text{Mn}^{2+}\) \(S=5/2\)) always yield observable ESR spectra even in amorphous frozen solutions."""
    }

    return deep

if __name__ == "__main__":
    deep = get_deep_enhancements()
    print(f"Generated deep enhancements for {len(deep)} units.")
    for u, sects in sorted(deep.items()):
        print(f"Unit {u}: enhanced sections {list(sects.keys())}")
