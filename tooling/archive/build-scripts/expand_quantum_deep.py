"""
expand_quantum_deep.py
Provides deep mathematical operator formalisms for all 10 units.
Strictly zero prohibited tokens (no course numbers, no marks, no grades, no exams).
"""

def get_deep_dict():
    return {
        "unit-1": {
            "title_append": "Advanced Mathematical Supplement: Spectral Theorem & Rigged Hilbert Spaces",
            "content": r"""
### Mathematical Rigor: The Spectral Theorem for Unbounded Self-Adjoint Operators
In standard elementary quantum mechanics, physical operators such as position \(\hat{x}\) and momentum \(\hat{p}\) are often treated as simple linear matrices. However, in functional analysis, \(\hat{x}\) and \(\hat{p}\) are unbounded self-adjoint operators acting on the infinite-dimensional Hilbert space \(\mathcal{L}^2(\mathbb{R})\).

#### Domain Issues and Self-Adjointness vs Hermiticity
A linear operator \(\hat{A}\) with domain \(D(\hat{A}) \subset \mathcal{H}\) is symmetric (Hermitian) if:
\[
\langle \phi | \hat{A} \psi \rangle = \langle \hat{A} \phi | \psi \rangle \quad \forall \phi, \psi \in D(\hat{A})
\]
However, the adjoint operator \(\hat{A}^\dagger\) has domain:
\[
D(\hat{A}^\dagger) = \{ \phi \in \mathcal{H} : \exists \eta \in \mathcal{H} \text{ such that } \langle \phi | \hat{A} \psi \rangle = \langle \eta | \psi \rangle \; \forall \psi \in D(\hat{A}) \}
\]
An operator is truly **self-adjoint** if and only if:
\[
\hat{A} = \hat{A}^\dagger \quad \text{and} \quad D(\hat{A}) = D(\hat{A}^\dagger)
\]
By Stone's theorem, only strictly self-adjoint operators can generate strongly continuous one-parameter unitary groups representing physical time evolution:
\[
\hat{U}(t) = \exp\left( -\frac{i \hat{H} t}{\hbar} \right)
\]

#### The Spectral Decomposition
According to the Spectral Theorem for unbounded self-adjoint operators, there exists a unique projection-valued measure \(E(\lambda)\) on the Borel \(\sigma\)-algebra of \(\mathbb{R}\) such that:
\[
\hat{A} = \int_{\sigma(\hat{A})} \lambda \, dE(\lambda)
\]
where the spectrum \(\sigma(\hat{A}) = \sigma_{\text{point}}(\hat{A}) \cup \sigma_{\text{cont}}(\hat{A})\) decomposes into:
1. **Point Spectrum \(\sigma_{\text{point}}\)**: Discrete eigenvalues with normalizable eigenfunctions in \(\mathcal{L}^2(\mathbb{R})\) (bound states).
2. **Continuous Spectrum \(\sigma_{\text{cont}}\)**: Continuous eigenvalues whose generalized eigenfunctions lie outside \(\mathcal{L}^2(\mathbb{R})\) (scattering states).

#### The Rigged Hilbert Space (Gel'fand Triplet)
To place plane waves \(\psi_p(x) = \frac{1}{\sqrt{2\pi\hbar}} e^{i p x / \hbar}\) and Dirac delta functions \(\delta(x - x_0)\) on rigorous mathematical footing, quantum mechanics employs the **Gel'fand Triplet**:
\[
\Phi \subset \mathcal{H} \subset \Phi^\times
\]
- \(\Phi\): The nuclear space of rapidly decreasing test functions (Schwartz space \(\mathcal{S}(\mathbb{R})\)).
- \(\mathcal{H}\): The conventional Hilbert space of square-integrable functions \(\mathcal{L}^2(\mathbb{R})\).
- \(\Phi^\times\): The dual space of tempered distributions (\(\mathcal{S}'(\mathbb{R})\)), containing plane waves and delta distributions.
In this rigged Hilbert space, Dirac's bra-ket formalism is mathematically rigorous, and the completeness relation holds identically:
\[
\hat{I} = \int_{-\infty}^\infty |p\rangle\langle p| \, dp
\]
"""
        },
        "unit-2": {
            "title_append": "Advanced Mathematical Supplement: Feynman Path Integral Formulation",
            "content": r"""
### The Feynman Path Integral Representation of Solvable Wells
In 1948, Richard Feynman reformulated quantum mechanics by replacing the operator differential equation with a sum over all possible classical trajectories connecting spacetime points \((x_a, t_a)\) and \((x_b, t_b)\).

#### The Quantum Propagator
The transition amplitude (quantum propagator) is:
\[
K(x_b, t_b; x_a, t_a) = \langle x_b | e^{-i \hat{H} (t_b - t_a) / \hbar} | x_a \rangle
\]
In Feynman's functional path integral formulation:
\[
K(x_b, t_b; x_a, t_a) = \int \mathcal{D}[x(t)] \exp\left( \frac{i}{\hbar} S[x(t)] \right)
\]
where the classical action functional is:
\[
S[x(t)] = \int_{t_a}^{t_b} \left[ \frac{1}{2} m \dot{x}(t)^2 - V(x(t)) \right] dt
\]

#### Method of Images for the Infinite Potential Well
For a particle in an infinite potential well of width \(L\) (\(V(x) = 0\) for \(0 < x < L\)), every path must remain confined strictly within the boundaries \(0 < x < L\).
Using the method of images, the path integral over the box equals the sum over all classical trajectories of a free particle in an infinite periodic lattice with alternating mirror reflections at \(x = 0\) and \(x = L\):
\[
K(x_b, t_b; x_a, 0) = \sum_{n=-\infty}^\infty \left[ K_{\text{free}}(x_b - x_a + 2nL, t) - K_{\text{free}}(-x_b - x_a + 2nL, t) \right]
\]
where \(K_{\text{free}}(x, t) = \sqrt{\frac{m}{2\pi i \hbar t}} \exp\left( \frac{i m x^2}{2\hbar t} \right)\).
By applying the Poisson summation formula \(\sum_{n=-\infty}^\infty e^{2\pi i n k} = \sum_{m=-\infty}^\infty \delta(k - m)\), this sum over topological winding numbers converts identically into the eigenfunction expansion:
\[
K(x_b, t; x_a, 0) = \sum_{n=1}^\infty \frac{2}{L} \sin\left(\frac{n\pi x_b}{L}\right) \sin\left(\frac{n\pi x_a}{L}\right) \exp\left( -\frac{i E_n t}{\hbar} \right)
\]
with \(E_n = \frac{n^2 \pi^2 \hbar^2}{2 m L^2}\).
The path integral establishes that the discrete quantum energy spectrum arises from the constructive interference of an infinite family of virtual classical trajectories reflecting between the boundaries."""
        },
        "unit-3": {
            "title_append": "Advanced Mathematical Supplement: Lie Algebra SU(2) & Wigner D-Matrices",
            "content": r"""
### Lie Algebraic Formulation of Angular Momentum & SU(2) Representations
Orbital and spin angular momentum operators are the infinitesimal generators of spatial rotations, forming the Lie algebra \(\mathfrak{su}(2) \cong \mathfrak{so}(3)\).

#### The Lie Algebra Commutation Relations
The components satisfy the Lie bracket relations:
\[
[\hat{J}_i, \hat{J}_j] = i\hbar \sum_{k} \epsilon_{i j k} \hat{J}_k
\]
Defining ladder operators \(\hat{J}_\pm = \hat{J}_x \pm i \hat{J}_y\):
\[
[\hat{J}_z, \hat{J}_\pm] = \pm \hbar \hat{J}_\pm, \quad [\hat{J}_+, \hat{J}_-] = 2\hbar \hat{J}_z
\]
The Casimir operator of the algebra is \(\hat{J}^2 = \hat{J}_x^2 + \hat{J}_y^2 + \hat{J}_z^2\), which commutes with all generators: \([\hat{J}^2, \hat{J}_k] = 0\).

#### Finite Rotations and Wigner D-Matrices
A finite rotation of a quantum state by Euler angles \((\alpha, \beta, \gamma)\) in the \(z\)-\(y'\)-\(z''\) convention is represented by the unitary rotation operator:
\[
\hat{\mathcal{D}}(\alpha, \beta, \gamma) = \exp\left( -\frac{i \alpha \hat{J}_z}{\hbar} \right) \exp\left( -\frac{i \beta \hat{J}_y}{\hbar} \right) \exp\left( -\frac{i \gamma \hat{J}_z}{\hbar} \right)
\]
In the orthonormal angular momentum basis \(|j, m\rangle\), the matrix elements are the **Wigner D-matrices**:
\[
D_{m' m}^j(\alpha, \beta, \gamma) = \langle j, m' | \hat{\mathcal{D}}(\alpha, \beta, \gamma) | j, m \rangle = e^{-i m' \alpha} d_{m' m}^j(\beta) e^{-i m \gamma}
\]
where Wigner's small \(d\)-matrix is given by the Jacobi polynomial formula:
\[
d_{m' m}^j(\beta) = \sqrt{\frac{(j+m')!(j-m')!}{(j+m)!(j-m)!}} \left(\sin\frac{\beta}{2}\right)^{m'-m} \left(\cos\frac{\beta}{2}\right)^{m'+m} P_{j-m'}^{(m'-m, m'+m)}(\cos\beta)
\]

#### The Wigner-Eckart Theorem
For any irreducible spherical tensor operator \(\hat{T}_q^{(k)}\) of rank \(k\), all spatial matrix elements factor into a geometric Clebsch-Gordan coefficient and a physical reduced matrix element:
\[
\langle j', m' | \hat{T}_q^{(k)} | j, m \rangle = (-1)^{j' - m'} \begin{pmatrix} j' & k & j \\ -m' & q & m \end{pmatrix} \langle j' || \hat{\mathbf{T}}^{(k)} || j \rangle
\]
The Wigner-Eckart theorem proves that all spectroscopic selection rules (\(\Delta J, \Delta M\)) are governed strictly by the rotational symmetry of the transition operator, independent of the internal radial Hamiltonian."""
        },
        "unit-4": {
            "title_append": "Advanced Mathematical Supplement: SO(4) Symmetry & Runge-Lenz Invariant",
            "content": r"""
### Dynamical SO(4) Symmetry of the Hydrogen Atom & The Laplace-Runge-Lenz Vector
The accidental degeneracy of hydrogenic energy levels with respect to orbital angular momentum \(l\) (where \(E_n\) depends strictly on \(n\)) is not an accident. It is the direct consequence of an underlying four-dimensional rotational symmetry \(\mathbf{SO}(4)\).

#### The Quantum Laplace-Runge-Lenz Operator
In classical Keplerian planetary orbits, the Laplace-Runge-Lenz vector points from the focus along the major axis toward perihelion, remaining strictly constant in time.
In quantum mechanics, the Hermitian Laplace-Runge-Lenz operator is:
\[
\hat{\mathbf{M}} = \frac{1}{2\mu} (\hat{\mathbf{p}} \times \hat{\mathbf{L}} - \hat{\mathbf{L}} \times \hat{\mathbf{p}}) - \frac{Z e^2}{4\pi\varepsilon_0} \frac{\mathbf{r}}{r}
\]
Evaluating the commutator with the Coulomb Hamiltonian \(\hat{H} = \frac{\hat{\mathbf{p}}^2}{2\mu} - \frac{Z e^2}{4\pi\varepsilon_0 r}\):
\[
[\hat{H}, \hat{\mathbf{M}}] = 0
\]
Because both \(\hat{\mathbf{L}}\) and \(\hat{\mathbf{M}}\) commute with \(\hat{H}\), the hydrogen atom possesses six independent conserved continuous generators.

#### The SO(4) Lie Algebra
For bound states (\(E < 0\)), define the scaled vector:
\[
\hat{\mathbf{K}} = \sqrt{-\frac{\mu}{2 E}} \hat{\mathbf{M}}
\]
The commutation relations between \(\hat{\mathbf{L}}\) and \(\hat{\mathbf{K}}\) are:
\[
[\hat{L}_i, \hat{L}_j] = i\hbar \epsilon_{i j k} \hat{L}_k, \quad [\hat{L}_i, \hat{K}_j] = i\hbar \epsilon_{i j k} \hat{K}_k, \quad [\hat{K}_i, \hat{K}_j] = i\hbar \epsilon_{i j k} \hat{L}_k
\]
This is precisely the Lie algebra of the four-dimensional orthogonal rotation group \(\mathbf{SO}(4)\).
By defining two decoupled commuting angular momentum vectors:
\[
\hat{\mathbf{I}}_1 = \frac{1}{2} (\hat{\mathbf{L}} + \hat{\mathbf{K}}), \quad \hat{\mathbf{I}}_2 = \frac{1}{2} (\hat{\mathbf{L}} - \hat{\mathbf{K}})
\]
they satisfy two independent \(\mathfrak{su}(2)\) algebras:
\[
[\hat{I}_{1i}, \hat{I}_{1j}] = i\hbar \epsilon_{i j k} \hat{I}_{1k}, \quad [\hat{I}_{2i}, \hat{I}_{2j}] = i\hbar \epsilon_{i j k} \hat{I}_{2k}, \quad [\hat{\mathbf{I}}_1, \hat{\mathbf{I}}_2] = 0
\]
Because \(\hat{\mathbf{L}} \cdot \hat{\mathbf{K}} = 0\), the Casimirs are equal: \(\hat{\mathbf{I}}_1^2 = \hat{\mathbf{I}}_2^2 = j(j + 1)\hbar^2\).
The total Casimir relates directly to the Hamiltonian:
\[
\hat{\mathbf{I}}_1^2 + \hat{\mathbf{I}}_2^2 = \frac{1}{2} (\hat{\mathbf{L}}^2 + \hat{\mathbf{K}}^2) = -\frac{\mu Z^2 e^4}{32\pi^2\varepsilon_0^2 \hat{H}} - \hbar^2
\]
Setting \(2j + 1 = n\), the bound-state energy eigenvalues are obtained algebraically without ever solving differential equations:
\[
E_n = -\frac{\mu Z^2 e^4}{32\pi^2\varepsilon_0^2 \hbar^2 n^2}
\]
The state degeneracy is \((2j + 1)^2 = n^2\), matching the observed spatial orbital degeneracy."""
        },
        "unit-5": {
            "title_append": "Advanced Mathematical Supplement: Dalgarno-Lewis & Hylleraas Variational Bounds",
            "content": r"""
### The Dalgarno-Lewis Formalism & Dual Variational Bounds in Perturbation Theory
Standard second-order perturbation theory requires evaluating an infinite sum over all bound and continuum states of the unperturbed system:
\[
E_0^{(2)} = \sum_{k \ne 0} \frac{|\langle \psi_k^{(0)} | \hat{H}' | \psi_0^{(0)} \rangle|^2}{E_0^{(0)} - E_k^{(0)}}
\]
In practice, evaluating the continuum integral is often mathematically intractable.

#### The Dalgarno-Lewis Equation
In 1955, Alexander Dalgarno and John T. Lewis proved that the infinite summation can be converted into an equivalent first-order inhomogeneous differential equation.
Define a function \(F(\mathbf{r})\) such that the first-order wavefunction is:
\[
\psi_0^{(1)}(\mathbf{r}) = F(\mathbf{r}) \psi_0^{(0)}(\mathbf{r})
\]
Substituting into the first-order perturbation equation \((\hat{H}^{(0)} - E_0^{(0)}) \psi_0^{(1)} = -( \hat{H}' - E_0^{(1)} ) \psi_0^{(0)}\) yields the **Dalgarno-Lewis differential equation**:
\[
-\frac{\hbar^2}{2m} \left[ \psi_0^{(0)} \nabla^2 F + 2 \nabla\psi_0^{(0)} \cdot \nabla F \right] = -( \hat{H}' - E_0^{(1)} ) \psi_0^{(0)}
\]
Once \(F(\mathbf{r})\) is found, the second-order energy is given directly by a simple single integral:
\[
E_0^{(2)} = \langle \psi_0^{(0)} | \hat{H}' | \psi_0^{(1)} \rangle = \int |\psi_0^{(0)}(\mathbf{r})|^2 F(\mathbf{r}) [ \hat{H}'(\mathbf{r}) - E_0^{(1)} ] d\mathbf{r}
\]
no infinite sum or continuum integration required!

#### The Hylleraas Variational Principle for Second-Order Energy
Egil Hylleraas formulated a variational principle that provides a rigorous upper bound on the second-order perturbation energy.
Define the Hylleraas functional for a trial first-order correction \(\chi\):
\[
J[\chi] = \langle \chi | \hat{H}^{(0)} - E_0^{(0)} | \chi \rangle + 2 \text{Re} \langle \chi | \hat{H}' - E_0^{(1)} | \psi_0^{(0)} \rangle
\]
**Theorem**: For any trial function \(\chi\), the functional \(J[\chi]\) satisfies:
\[
J[\chi] \ge E_0^{(2)}
\]
The exact second-order energy \(E_0^{(2)}\) is the global minimum of \(J[\chi]\), achieved if and only if \(\chi = \psi_0^{(1)}\).
This allows variational parameters to be optimized directly to compute second-order polarizabilities and dispersion coefficients without summing over unperturbed states."""
        },
        "unit-6": {
            "title_append": "Advanced Mathematical Supplement: Second Quantization Algebra",
            "content": r"""
### Second Quantization Algebra: Creation, Annihilation & Field Operators
In many-body quantum chemistry, tracking explicit coordinate labels \((\mathbf{r}_1, \dots, \mathbf{r}_N)\) and Slater determinants becomes unwieldy. The formalism of **Second Quantization** replaces coordinate wavefunctions with an algebraic representation on **Fock Space**:
\[
\mathcal{F} = \bigoplus_{N=0}^\infty \mathcal{H}_N
\]

#### Fermionic Creation and Annihilation Operators
Let \(\{ |\phi_p\rangle \}\) be a complete orthonormal basis of single-particle spin-orbitals.
We define the creation operator \(a_p^\dagger\) and annihilation operator \(a_p\):
- \(a_p^\dagger |0\rangle = |\phi_p\rangle\) (creates an electron in spin-orbital \(p\))
- \(a_p |\phi_p\rangle = |0\rangle\) (annihilates the electron in spin-orbital \(p\))
- \(a_p |0\rangle = 0\) (annihilation on the vacuum state yields zero)

The Pauli exclusion principle and antisymmetry are enforced identically by the **Canonical Anticommutation Relations (CAR)**:
\[
\{ a_p, a_q^\dagger \} \equiv a_p a_q^\dagger + a_q^\dagger a_p = \delta_{p q}
\]
\[
\{ a_p, a_q \} = 0, \quad \{ a_p^\dagger, a_q^\dagger \} = 0
\]
Notice that \(\{ a_p^\dagger, a_p^\dagger \} = 2 (a_p^\dagger)^2 = 0 \implies (a_p^\dagger)^2 = 0\): attempting to create two electrons in the exact same spin-orbital gives zero, encoding the Pauli exclusion principle into the operator algebra!

#### Second Quantized Hamiltonian
The full non-relativistic molecular electronic Hamiltonian transforms into:
\[
\hat{H} = \sum_{p, q} h_{p q} a_p^\dagger a_q + \frac{1}{2} \sum_{p, q, r, s} g_{p q r s} a_p^\dagger a_q^\dagger a_s a_r
\]
where the one-electron core integrals are:
\[
h_{p q} = \int \phi_p^*(\mathbf{r}) \hat{h}(\mathbf{r}) \phi_q(\mathbf{r}) \, d\mathbf{r}
\]
and the two-electron repulsion integrals (in physicist's notation) are:
\[
g_{p q r s} = \iint \frac{\phi_p^*(\mathbf{r}_1) \phi_q^*(\mathbf{r}_2) \phi_r(\mathbf{r}_1) \phi_s(\mathbf{r}_2)}{r_{12}} \, d\mathbf{r}_1 d\mathbf{r}_2
\]
All many-electron Slater determinants are written as operator strings acting on vacuum:
\[
|\Phi\rangle = a_1^\dagger a_2^\dagger \dots a_N^\dagger |0\rangle
\]
Wick's theorem then evaluates all matrix elements purely through algebraic contractions, forming the mathematical backbone of modern coupled cluster and quantum computing algorithms."""
        },
        "unit-7": {
            "title_append": "Advanced Mathematical Supplement: Jaynes MaxEnt & von Neumann Entropy",
            "content": r"""
### Information Theoretic MaxEnt Formulation & The von Neumann Density Matrix
In 1957, Edwin Jaynes re-founded statistical mechanics on Claude Shannon's Information Theory: statistical distributions are not physical assumptions, but rather the unique mathematically unbiased inference consistent with incomplete macroscopic information (**Maximum Entropy Principle, MaxEnt**).

#### The von Neumann Density Operator
In quantum statistical mechanics, a mixed quantum state is described by a Hermitian, positive-semidefinite **density operator** \(\hat{\rho}\):
\[
\hat{\rho} = \sum_i P_i |\psi_i\rangle\langle \psi_i|, \quad \text{Tr}(\hat{\rho}) = 1, \quad \hat{\rho} \ge 0
\]
The expectation value of any physical observable \(\hat{A}\) is:
\[
\langle A \rangle = \text{Tr}(\hat{\rho} \hat{A})
\]
For a pure state, \(\hat{\rho}^2 = \hat{\rho}\) (\(\text{Tr}(\hat{\rho}^2) = 1\)); for a mixed state, \(\text{Tr}(\hat{\rho}^2) < 1\).

#### The von Neumann Quantum Entropy
The quantum mechanical extension of Gibbs and Shannon entropy is:
\[
S_{\text{vN}}[\hat{\rho}] = -k_B \text{Tr}(\hat{\rho} \ln \hat{\rho})
\]
Properties:
1. \(S_{\text{vN}} \ge 0\), with \(S_{\text{vN}} = 0\) if and only if the state is pure.
2. Invariant under unitary transformations: \(S_{\text{vN}}[\hat{U}\hat{\rho}\hat{U}^\dagger] = S_{\text{vN}}[\hat{\rho}]\).
3. Subadditive: For a composite bipartite system \(A B\), \(S(A B) \le S(A) + S(B)\).

#### Derivation of the Canonical Density Matrix via MaxEnt
We maximize \(S_{\text{vN}}\) subject to two physical constraints:
1. Normalization: \(\text{Tr}(\hat{\rho}) = 1\) (multiplier \(\lambda_0\))
2. Average internal energy: \(\text{Tr}(\hat{\rho} \hat{H}) = U\) (multiplier \(\beta\))

Construct the variational functional:
\[
\mathcal{L}[\hat{\rho}] = -k_B \text{Tr}(\hat{\rho} \ln \hat{\rho}) - \lambda_0 (\text{Tr}(\hat{\rho}) - 1) - \beta (\text{Tr}(\hat{\rho}\hat{H}) - U)
\]
Setting the functional derivative to zero:
\[
\frac{\delta \mathcal{L}}{\delta \hat{\rho}} = -k_B (\ln \hat{\rho} + \hat{I}) - \lambda_0 \hat{I} - \beta \hat{H} = 0 \implies \ln \hat{\rho} = -(1 + \lambda_0 / k_B)\hat{I} - \frac{\beta}{k_B} \hat{H}
\]
Exponentiating:
\[
\hat{\rho} = \frac{e^{-\beta \hat{H}}}{\text{Tr}(e^{-\beta \hat{H}})} = \frac{e^{-\beta \hat{H}}}{Q}
\]
where the canonical partition function is \(Q = \text{Tr}(e^{-\beta \hat{H}})\).
Thermal equilibrium emerges as the state of maximal missing information given knowledge only of the average internal energy."""
        },
        "unit-8": {
            "title_append": "Advanced Mathematical Supplement: Dunham Coefficients & High-T Asymptotics",
            "content": r"""
### Dunham Expansions & High-Temperature Partition Function Asymptotics
In high-precision thermochemistry, idealized harmonic oscillator and rigid rotor models are insufficient. J. L. Dunham expanded the rovibrational energy levels in a bivariate double power series in \((v + 1/2)\) and \(J(J + 1)\):
\[
E(v, J) = \sum_{l=0}^\infty \sum_{j=0}^\infty Y_{l, j} \left( v + \frac{1}{2} \right)^l [J(J + 1)]^j
\]
where \(Y_{l, j}\) are the **Dunham Coefficients**:
- \(Y_{1, 0} \approx \tilde{\omega}_e\) (fundamental harmonic frequency)
- \(Y_{2, 0} \approx -\tilde{\omega}_e x_e\) (anharmonicity constant)
- \(Y_{0, 1} \approx B_e\) (equilibrium rotational constant)
- \(Y_{1, 1} \approx -\alpha_e\) (vibration-rotation coupling)
- \(Y_{0, 2} \approx -D_e\) (centrifugal distortion)

#### High-Temperature Asymptotics via the Euler-Maclaurin Summation
To evaluate the partition function without truncation error, we apply the Euler-Maclaurin formula:
\[
\sum_{k=a}^b f(k) = \int_a^b f(x) dx + \frac{f(a) + f(b)}{2} + \sum_{k=1}^m \frac{B_{2k}}{(2k)!} [f^{(2k-1)}(b) - f^{(2k-1)}(a)]
\]
where \(B_{2k}\) are the Bernoulli numbers (\(B_2 = 1/6, B_4 = -1/30\)).
For the rotational partition function of a linear rotor:
\[
q_{\text{rot}}(T) = \sum_{J=0}^\infty (2J + 1) e^{-J(J+1) \theta_{\text{rot}} / T} = \frac{T}{\sigma \theta_{\text{rot}}} \left[ 1 + \frac{1}{3}\left(\frac{\theta_{\text{rot}}}{T}\right) + \frac{1}{15}\left(\frac{\theta_{\text{rot}}}{T}\right)^2 + \frac{4}{315}\left(\frac{\theta_{\text{rot}}}{T}\right)^3 + \dots \right]
\]
- The leading term \(\frac{T}{\sigma \theta_{\text{rot}}}\) is the classical integral.
- The term \(+\frac{1}{3}\) is the first quantum correction.
- Higher-order terms ensure six-figure accuracy down to cryogenic temperatures without explicit summation."""
        },
        "unit-9": {
            "title_append": "Advanced Mathematical Supplement: Quantum Tunneling Rate Corrections in TST",
            "content": r"""
### Non-Classical Reaction Coordinates: Quantum Tunneling Corrections in TST
Classical Transition State Theory assumes that all reacting trajectories pass over the potential energy barrier. For light atoms (particularly protons \(\text{H}^+\), hydrogen atoms \(\text{H}^\bullet\), and hydride ions \(\text{H}^-\)), quantum mechanical tunneling through the barrier significantly accelerates reaction rates at ambient and sub-ambient temperatures.

#### The Wigner Semiclassical Tunneling Correction
In 1932, Eugene Wigner expanded the quantum transmission coefficient in powers of Planck's constant \(\hbar\).
For an inverted parabolic barrier of imaginary barrier frequency \(\nu^\ddagger = \frac{1}{2\pi}\sqrt{\frac{k^\ddagger}{\mu^\ddagger}}\):
\[
\kappa(T) = \frac{k_{\text{quantum}}(T)}{k_{\text{classical}}(T)} = 1 + \frac{1}{24} \left( \frac{h \nu^\ddagger}{k_B T} \right)^2 - \frac{1}{2880} \left( \frac{h \nu^\ddagger}{k_B T} \right)^4 + \dots
\]
When \(\frac{h \nu^\ddagger}{k_B T} < 1\), the Wigner formula provides a rapid, accurate tunneling correction:
\[
\kappa_{\text{Wigner}}(T) \approx 1 + \frac{1}{24} \left( \frac{h \nu^\ddagger}{k_B T} \right)^2
\]

#### The Eckart Barrier Model for Deep Tunneling
For high, narrow barriers where \(h \nu^\ddagger > k_B T\), tunneling from levels below the barrier apex dominates.
Carl Eckart modeled the reaction profile with an asymmetric continuous potential:
\[
V(x) = \frac{A y}{1 + y} + \frac{B y}{(1 + y)^2}, \quad \text{where } y = e^{2\pi x / L}
\]
The quantum transmission probability \(P(E)\) has an exact analytical solution in terms of hypergeometric functions:
\[
P(E) = \frac{\cosh[2\pi(\alpha + \beta)] - \cosh[2\pi(\alpha - \beta)]}{\cosh[2\pi(\alpha + \beta)] + \cosh[2\pi \delta]}
\]
where \(\alpha = \frac{1}{2}\sqrt{E/C}\), \(\beta = \frac{1}{2}\sqrt{(E - A)/C}\), and \(\delta = \frac{1}{2}\sqrt{(B - C)/C}\) with \(C = \frac{h^2}{8 m L^2}\).
The thermally averaged transmission coefficient is:
\[
\kappa_{\text{Eckart}}(T) = \frac{\int_0^\infty P(E) e^{-E / k_B T} dE}{\int_{V_{\text{barrier}}}^\infty e^{-E / k_B T} dE} = e^{V_{\text{barrier}} / k_B T} \frac{1}{k_B T} \int_0^\infty P(E) e^{-E / k_B T} dE
\]
In enzyme-catalyzed hydrogen transfer reactions, \(\kappa_{\text{Eckart}}\) can exceed \(100\), explaining immense kinetic isotope effects (\(k_H / k_D \sim 10 - 80\)) that classical Arrhenius kinetics fails to capture."""
        },
        "unit-10": {
            "title_append": "Advanced Mathematical Supplement: Bogoliubov Canonical Transformations",
            "content": r"""
### Bogoliubov Canonical Transformations & The Landau Criterion for Superfluidity
To diagonalize interacting many-body Hamiltonians for weakly interacting Bose gases and BCS superconductors, Nikolay Bogoliubov introduced unitary transformations mixing creation and annihilation operators.

#### The Bogoliubov Transformation for Bosons
Consider a weakly interacting Bose gas with macroscopic condensate \(N_0 \approx N\).
Replacing zero-momentum operators with numbers \(a_0, a_0^\dagger \rightarrow \sqrt{N_0}\), the effective Hamiltonian for non-zero momentum excitations \(\mathbf{k} \ne 0\) is quadratic:
\[
\hat{H}_{\text{eff}} = \sum_{\mathbf{k} \ne 0} \left( \frac{\hbar^2 k^2}{2m} + n_0 V_0 \right) a_\mathbf{k}^\dagger a_\mathbf{k} + \frac{1}{2} n_0 V_0 \sum_{\mathbf{k} \ne 0} (a_\mathbf{k}^\dagger a_{-\mathbf{k}}^\dagger + a_\mathbf{k} a_{-\mathbf{k}})
\]
We define new quasiparticle operators \(b_\mathbf{k}, b_\mathbf{k}^\dagger\) via the **Bogoliubov Canonical Transformation**:
\[
b_\mathbf{k} = u_k a_\mathbf{k} + v_k a_{-\mathbf{k}}^\dagger, \quad b_\mathbf{k}^\dagger = u_k a_\mathbf{k}^\dagger + v_k a_{-\mathbf{k}}
\]
Preserving bosonic commutation relations \([b_\mathbf{k}, b_{\mathbf{k}'}^\dagger] = \delta_{\mathbf{k} \mathbf{k}'}\) requires:
\[
u_k^2 - v_k^2 = 1
\]
Choosing \(u_k, v_k\) to eliminate the off-diagonal pairing terms diagonalizes the Hamiltonian:
\[
\hat{H}_{\text{eff}} = E_0 + \sum_{\mathbf{k} \ne 0} \varepsilon(k) b_\mathbf{k}^\dagger b_\mathbf{k}
\]
where the **Bogoliubov Quasiparticle Dispersion Relation** is:
\[
\varepsilon(k) = \sqrt{\left(\frac{\hbar^2 k^2}{2m}\right)^2 + 2 n_0 V_0 \left(\frac{\hbar^2 k^2}{2m}\right)} = \sqrt{\left(\frac{\hbar^2 k^2}{2m}\right)^2 + (\hbar c_s k)^2}
\]
where \(c_s = \sqrt{n_0 V_0 / m}\) is the speed of sound.
- At low momentum (\(k \rightarrow 0\)): \(\varepsilon(k) \approx \hbar c_s k\) (linear acoustic phonon dispersion).
- At high momentum (\(k \rightarrow \infty\)): \(\varepsilon(k) \approx \frac{\hbar^2 k^2}{2m} + n_0 V_0\) (free particle parabolic dispersion).

#### The Landau Criterion for Superfluidity
Lev Landau analyzed an object moving with velocity \(\mathbf{v}\) through a fluid. Creating an excitation of momentum \(\hbar \mathbf{k}\) and energy \(\varepsilon(k)\) is kinematically forbidden unless:
\[
v \ge \min_k \left( \frac{\varepsilon(k)}{\hbar k} \right) \equiv v_c
\]
- For an ideal non-interacting Bose gas: \(\varepsilon(k) = \frac{\hbar^2 k^2}{2m} \implies \frac{\varepsilon(k)}{\hbar k} = \frac{\hbar k}{2m} \rightarrow 0\) as \(k \rightarrow 0\). The critical velocity is \(v_c = 0\); an ideal Bose gas is NOT superfluid!
- For an interacting Bose gas with Bogoliubov dispersion:
  \[
  v_c = \min_k \left( \frac{\sqrt{(\hbar^2 k^2 / 2m)^2 + (\hbar c_s k)^2}}{\hbar k} \right) = c_s > 0
  \]
Because \(v_c = c_s > 0\), particles moving slower than the speed of sound cannot dissipate energy into the fluid, giving rise to frictionless macroscopic **superfluidity**."""
        }
    }
