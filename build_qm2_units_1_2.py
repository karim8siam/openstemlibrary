import json

# ==============================================================================
# CHAPTER 1: MATRIX MECHANICS, HILBERT SPACE & OPERATOR REPRESENTATIONS
# ==============================================================================
u1 = {
    "id": "unit1",
    "number": 1,
    "title": "Matrix Mechanics, Hilbert Space & Operator Representations",
    "subtitle": "State Vectors, Dirac Bra-Ket Algebra, Unitary Transformations, Density Operators & Algebraic Oscillator",
    "description": "Comprehensive mathematical and physical foundations of modern quantum state space: the physical significance of two-slit interference, state vectors in abstract complex Hilbert space, Dirac notation, adjoints, projection operators, continuous coordinate and momentum representations, transformation theory, spatial inversion and parity, pure versus mixed state ensembles with the density matrix formalism, and the complete algebraic ladder operator matrix mechanics of the quantum harmonic oscillator.",
    "sections": [
        {
            "id": "sec1-1",
            "title": "Foundations of Quantum State Space: Slit Experiments, Superposition & Dirac Bra-Ket Algebra",
            "content": r"""
<h3>1. Physical Impetus: The Double-Slit Experiment & Quantum Probability Amplitudes</h3>
<p>
The conceptual foundation of quantum mechanics rests upon the breakdown of classical probability theory, most dramatically demonstrated by electron diffraction through two closely spaced slits. In classical statistical mechanics, if an event can occur via two mutually exclusive classical alternatives (passing through slit 1 or slit 2), the resultant probability distribution on a detection screen is the direct sum of the individual probabilities:
</p>
$$\mathcal{P}_{\text{classical}}(x) = \mathcal{P}_1(x) + \mathcal{P}_2(x)$$
<p>
In quantum mechanics, when no measurement is made to determine the specific path traversed by the electron, the detector records an interference pattern characteristic of wave phenomena. Quantum kinematics resolves this paradox by associating with every physical event a complex-valued <em>probability amplitude</em> $\psi(x) \in \mathbb{C}$, such that the total state is a coherent linear superposition of the two path alternatives:
</p>
$$\psi(x) = \psi_1(x) + \psi_2(x)$$
<p>
The observable probability density $\mathcal{P}(x)$ is the modulus squared of the total amplitude:
</p>
$$\mathcal{P}(x) = |\psi(x)|^2 = |\psi_1(x) + \psi_2(x)|^2 = |\psi_1(x)|^2 + |\psi_2(x)|^2 + 2\,\text{Re}\left[\psi_1^*(x)\,\psi_2(x)\right]$$
<p>
The final term, $2\sqrt{\mathcal{P}_1\mathcal{P}_2}\cos(\phi_1 - \phi_2)$, is the quantum interference cross-term. If a non-destructive measurement is introduced to register which slit the particle traversed, the relative phase coherence is irrevocably destroyed by quantum backaction (decoherence), collapsing the interference pattern into the classical additive distribution $\mathcal{P}_1 + \mathcal{P}_2$.
</p>

<h3>2. The Dirac Bra and Ket Formalism</h3>
<p>
Paul Dirac synthesized the wave mechanics of Schrödinger and the matrix mechanics of Heisenberg into an abstract vector space representation. A physical state of an isolated quantum system is represented by a ray in a complex vector space $\mathcal{H}$, termed a <strong>ket vector</strong> and denoted by $|\psi\rangle$.
</p>
<p>
Associated with the vector space $\mathcal{H}$ is its dual space $\mathcal{H}^*$, consisting of all continuous linear functionals mapping $\mathcal{H} \to \mathbb{C}$. Dirac denoted elements of the dual space as <strong>bra vectors</strong>, $\langle \phi| \in \mathcal{H}^*$. By the Riesz representation theorem, for every ket $|\psi\rangle \in \mathcal{H}$, there exists a unique conjugate dual bra $\langle \psi| \in \mathcal{H}^*$ under an anti-linear bijective map termed the Hermitian adjoint:
</p>
$$(c_1|\psi_1\rangle + c_2|\psi_2\rangle)^\dagger = c_1^*\langle \psi_1| + c_2^*\langle \psi_2|$$
<p>
The action of a functional $\langle \phi|$ on a state ket $|\psi\rangle$ forms the Dirac <em>bracket</em>, representing the inner product:
</p>
$$\langle \phi | \psi \rangle = \int_{\Omega} \phi^*(x)\,\psi(x)\,dx \in \mathbb{C}$$
<p>
The inner product satisfies three defining axioms:
</p>
<ol>
  <li><strong>Skew-symmetry (Hermitian conjugate property):</strong> $\langle \phi | \psi \rangle = \langle \psi | \phi \rangle^*$</li>
  <li><strong>Linearity in the ket argument:</strong> $\langle \phi | (c_1 |\psi_1\rangle + c_2 |\psi_2\rangle) = c_1 \langle \phi | \psi_1\rangle + c_2 \langle \phi | \psi_2\rangle$</li>
  <li><strong>Positive-definiteness:</strong> $\langle \psi | \psi \rangle \ge 0$, with equality holding if and only if $|\psi\rangle = 0$.</li>
</ol>
"""
        },
        {
            "id": "sec1-2",
            "title": "Hilbert Space Geometry: Inner Products, Norms, Cauchy-Schwarz Inequality & Bases",
            "content": r"""
<h3>1. Definition of Complex Hilbert Space</h3>
<p>
An abstract Hilbert space $\mathcal{H}$ is a complete complex inner product space. Completeness ensures that every Cauchy sequence of state vectors $\{|\psi_n\rangle\}_{n=1}^\infty$ converges to an element within $\mathcal{H}$ with respect to the induced norm:
</p>
$$\|\psi\| = \sqrt{\langle \psi | \psi \rangle}$$
$$\lim_{n,m\to\infty} \|\psi_n - \psi_m\| = 0 \implies \exists |\psi\rangle \in \mathcal{H} \text{ such that } \lim_{n\to\infty} \|\psi_n - \psi\| = 0$$

<h3>2. The Cauchy-Schwarz and Triangle Inequalities</h3>
<p>
For any two state kets $|\psi\rangle, |\phi\rangle \in \mathcal{H}$, consider the arbitrary real or complex parameter $\lambda$. Since the norm of the vector $|\chi\rangle = |\psi\rangle + \lambda |\phi\rangle$ is strictly non-negative:
</p>
$$\langle \chi | \chi \rangle = \langle \psi | \psi \rangle + \lambda \langle \psi | \phi \rangle + \lambda^* \langle \phi | \psi \rangle + |\lambda|^2 \langle \phi | \phi \rangle \ge 0$$
<p>
Choosing the specific variation $\lambda = -\frac{\langle \phi | \psi \rangle}{\langle \phi | \phi \rangle}$ (assuming $\langle \phi | \phi \rangle \ne 0$) yields:
</p>
$$\langle \psi | \psi \rangle - \frac{|\langle \phi | \psi \rangle|^2}{\langle \phi | \phi \rangle} \ge 0 \implies |\langle \phi | \psi \rangle|^2 \le \langle \psi | \psi \rangle \langle \phi | \phi \rangle$$
<p>
This is the foundational <strong>Cauchy-Schwarz inequality</strong>:
</p>
$$|\langle \phi | \psi \rangle| \le \|\phi\| \, \|\psi\|$$
<p>
Equality holds if and only if the kets are linearly dependent: $|\psi\rangle = c|\phi\rangle$. Using this result, the Minkowski (triangle) inequality directly follows:
</p>
$$\| |\psi\rangle + |\phi\rangle \| \le \|\psi\| + \|\phi\|$$

<h3>3. Orthonormal Bases and Completeness (Closure) Relations</h3>
<p>
Let $\{|u_n\rangle\}_{n=1}^N$ (where $N$ may be finite or countably infinite) be an orthonormal set spanning $\mathcal{H}$, satisfying the orthonormality condition:
</p>
$$\langle u_n | u_m \rangle = \delta_{nm}$$
<p>
Any arbitrary state $|\psi\rangle \in \mathcal{H}$ can be expanded uniquely as:
</p>
$$|\psi\rangle = \sum_{n} c_n |u_n\rangle, \quad c_n = \langle u_n | \psi \rangle$$
<p>
Substituting $c_n$ into the expansion reveals the identity operator $\hat{I}$:
</p>
$$|\psi\rangle = \sum_{n} |u_n\rangle \langle u_n | \psi \rangle = \left( \sum_{n} |u_n\rangle \langle u_n| \right) |\psi\rangle \implies \sum_{n} |u_n\rangle \langle u_n| = \hat{I}$$
<p>
This equation is the <strong>completeness relation</strong> (or resolution of the identity). The norm of $|\psi\rangle$ expressed through basis coordinates gives Parseval's identity:
</p>
$$\langle \psi | \psi \rangle = \sum_{n} |c_n|^2 = \sum_n |\langle u_n | \psi \rangle|^2 = 1$$
"""
        },
        {
            "id": "sec1-3",
            "title": "Linear Operators, Matrix Representations, Adjoints & Spectral Decomposition",
            "content": r"""
<h3>1. Linear Operators and Dyadic Outer Products</h3>
<p>
A linear operator $\hat{A}: \mathcal{H} \to \mathcal{H}$ maps kets to kets while preserving linear combinations:
</p>
$$\hat{A}\left(c_1|\psi_1\rangle + c_2|\psi_2\rangle\right) = c_1 \hat{A}|\psi_1\rangle + c_2 \hat{A}|\psi_2\rangle$$
<p>
The outer product between a ket $|\phi\rangle$ and a bra $\langle \chi|$ forms a rank-1 linear operator (a dyad):
</p>
$$\hat{M} = |\phi\rangle \langle \chi| \implies \hat{M}|\psi\rangle = |\phi\rangle \langle \chi | \psi \rangle = (\langle \chi | \psi \rangle) |\phi\rangle$$

<h3>2. Matrix Representation in a Discrete Basis</h3>
<p>
By inserting the completeness relation on both sides of an operator $\hat{A}$, we express $\hat{A}$ in terms of its matrix elements:
</p>
$$\hat{A} = \hat{I} \hat{A} \hat{I} = \sum_{n} \sum_{m} |u_n\rangle \langle u_n | \hat{A} | u_m \rangle \langle u_m|$$
<p>
Defining the matrix element $A_{nm} \equiv \langle u_n | \hat{A} | u_m \rangle$, the operator acts as a matrix acting upon coordinate column vectors:
</p>
$$\hat{A} \doteq \begin{pmatrix} A_{11} & A_{12} & \cdots \\ A_{21} & A_{22} & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}, \quad |\psi\rangle \doteq \begin{pmatrix} c_1 \\ c_2 \\ \vdots \end{pmatrix}$$

<h3>3. Hermitian Adjoint and Observable Operators</h3>
<p>
The Hermitian adjoint $\hat{A}^\dagger$ of an operator $\hat{A}$ is defined by the condition:
</p>
$$\langle \phi | \hat{A} | \psi \rangle^* = \langle \psi | \hat{A}^\dagger | \phi \rangle \quad \forall |\psi\rangle, |\phi\rangle \in \mathcal{H}$$
<p>
In matrix terms, $(A^\dagger)_{nm} = (A_{mn})^*$, representing the conjugate transpose. An operator represents a physical observable if and only if it is self-adjoint (Hermitian):
</p>
$$\hat{A}^\dagger = \hat{A} \iff \langle u_n | \hat{A} | u_m \rangle = \langle u_m | \hat{A} | u_n \rangle^*$$
<p>
Hermitian operators possess two vital physical properties:
</p>
<ol>
  <li><strong>Real Eigenvalues:</strong> If $\hat{A}|a_n\rangle = a_n |a_n\rangle$, then $a_n = a_n^* \in \mathbb{R}$.</li>
  <li><strong>Orthogonality of Eigenvectors:</strong> If $\hat{A}|a_n\rangle = a_n|a_n\rangle$ and $\hat{A}|a_m\rangle = a_m|a_m\rangle$ with $a_n \ne a_m$, then $\langle a_n | a_m \rangle = 0$.</li>
</ol>

<h3>4. Projection Operators and the Spectral Decomposition Theorem</h3>
<p>
A projection operator $\hat{P}_n$ onto the one-dimensional subspace spanned by the normalized ket $|u_n\rangle$ is defined as:
</p>
$$\hat{P}_n \equiv |u_n\rangle \langle u_n|$$
<p>
Projection operators satisfy the algebraic properties of idempotency and Hermiticity:
</p>
$$\hat{P}_n^2 = (|u_n\rangle \langle u_n|)(|u_n\rangle \langle u_n|) = |u_n\rangle \langle u_n | u_n \rangle \langle u_n| = |u_n\rangle \langle u_n| = \hat{P}_n$$
$$\hat{P}_n^\dagger = \hat{P}_n, \quad \hat{P}_n \hat{P}_m = \delta_{nm}\hat{P}_n$$
<p>
According to the <strong>Spectral Decomposition Theorem</strong>, any Hermitian observable $\hat{A}$ with a non-degenerate discrete spectrum can be represented as a weighted sum of its projection operators:
</p>
$$\hat{A} = \sum_n a_n |a_n\rangle \langle a_n| = \sum_n a_n \hat{P}_n$$
<p>
For any analytic function $f(\hat{A})$, the spectral representation evaluates directly to:
</p>
$$f(\hat{A}) = \sum_n f(a_n) |a_n\rangle \langle a_n|$$
"""
        },
        {
            "id": "sec1-4",
            "title": "Unitary Transformation Theory, Change of Basis & Continuous Representations",
            "content": r"""
<h3>1. Change of Basis and Unitary Operators</h3>
<p>
Consider two distinct complete orthonormal bases $\{|u_n\rangle\}$ and $\{|v_k\rangle\}$ spanning the same Hilbert space $\mathcal{H}$. The transformation connecting the two bases is mediated by a linear operator $\hat{U}$:
</p>
$$|v_k\rangle = \sum_n |u_n\rangle \langle u_n | v_k\rangle \equiv \hat{U} |u_k\rangle$$
$$\hat{U} = \sum_k |v_k\rangle \langle u_k|$$
<p>
Evaluating the adjoint operator:
</p>
$$\hat{U}^\dagger = \sum_j |u_j\rangle \langle v_j| \implies \hat{U} \hat{U}^\dagger = \sum_{k,j} |v_k\rangle \langle u_k | u_j\rangle \langle v_j| = \sum_k |v_k\rangle \langle v_k| = \hat{I}$$
$$\hat{U}^\dagger \hat{U} = \sum_{j,k} |u_j\rangle \langle v_j | v_k\rangle \langle u_k| = \sum_k |u_k\rangle \langle u_k| = \hat{I}$$
<p>
Thus, $\hat{U}^\dagger = \hat{U}^{-1}$, meaning $\hat{U}$ is a <strong>unitary operator</strong>. Unitary transformations preserve inner products, vector norms, and the algebraic spectra of operators:
</p>
$$\langle \phi' | \psi' \rangle = \langle \phi | \hat{U}^\dagger \hat{U} | \psi \rangle = \langle \phi | \psi \rangle$$
$$\hat{A}' = \hat{U}^\dagger \hat{A} \hat{U}$$

<h3>2. Continuous Spectra: Position and Momentum Representations</h3>
<p>
When an observable exhibits a continuous spectrum, such as position $\hat{x}$ or momentum $\hat{p}$, the Kronecker delta is replaced by the Dirac delta distribution:
</p>
$$\hat{x}|x\rangle = x|x\rangle, \quad \langle x | x' \rangle = \delta(x - x'), \quad \int_{-\infty}^\infty |x\rangle \langle x| \, dx = \hat{I}$$
$$\hat{p}|p\rangle = p|p\rangle, \quad \langle p | p' \rangle = \delta(p - p'), \quad \int_{-\infty}^\infty |p\rangle \langle p| \, dp = \hat{I}$$
<p>
The Schrödinger wave function $\psi(x)$ is the coordinate-basis projection of the state ket $|\psi\rangle$:
</p>
$$\psi(x) = \langle x | \psi \rangle, \quad \phi(p) = \langle p | \psi \rangle$$
<p>
The transformation kernel connecting coordinate and momentum space is the overlap bracket $\langle x | p \rangle$. Using the fundamental commutator $[\hat{x}, \hat{p}] = i\hbar\hat{I}$ and the differential representation $\langle x | \hat{p} | \psi \rangle = -i\hbar \frac{\partial}{\partial x}\psi(x)$:
</p>
$$\langle x | \hat{p} | p \rangle = p \langle x | p \rangle = -i\hbar \frac{\partial}{\partial x} \langle x | p \rangle$$
$$\implies \langle x | p \rangle = \frac{1}{\sqrt{2\pi\hbar}} \exp\left(\frac{i p x}{\hbar}\right)$$
<p>
Consequently, transforming from coordinate to momentum wavefunctions is mathematically identical to a continuous Fourier transformation:
</p>
$$\phi(p) = \langle p | \psi \rangle = \int_{-\infty}^\infty \langle p | x \rangle \langle x | \psi \rangle \, dx = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^\infty e^{-ipx/\hbar} \psi(x) \, dx$$
"""
        },
        {
            "id": "sec1-5",
            "title": "Parity and Symmetry Operators: Spatial Inversion, Selection Rules & Invariance",
            "content": r"""
<h3>1. The Spatial Inversion (Parity) Operator</h3>
<p>
The parity operator $\hat{\Pi}$ acts on spatial coordinate eigenkets by inverting all Cartesian axes through the origin:
</p>
$$\hat{\Pi} |x, y, z\rangle = |-x, -y, -z\rangle$$
<p>
Acting twice upon any arbitrary state returns the original spatial coordinates:
</p>
$$\hat{\Pi}^2 |x\rangle = \hat{\Pi} |-x\rangle = |x\rangle \implies \hat{\Pi}^2 = \hat{I}$$
<p>
Since $\hat{\Pi}$ is also unitary ($\hat{\Pi}^\dagger \hat{\Pi} = \hat{I}$), it is simultaneously Hermitian:
</p>
$$\hat{\Pi}^\dagger = \hat{\Pi}^{-1} = \hat{\Pi}$$
<p>
The eigenvalues $\pi_k$ of the parity operator must satisfy:
</p>
$$\hat{\Pi}|\psi\rangle = \pi_k |\psi\rangle \implies \hat{\Pi}^2|\psi\rangle = \pi_k^2 |\psi\rangle = |\psi\rangle \implies \pi_k = \pm 1$$
<p>
States with eigenvalue $+1$ are termed <em>even parity</em> states ($\psi(-x) = +\psi(x)$), while states with eigenvalue $-1$ are termed <em>odd parity</em> states ($\psi(-x) = -\psi(x)$).
</p>

<h3>2. Transformation of Dynamical Observables Under Parity</h3>
<p>
Under coordinate inversion, the position and momentum operators change sign:
</p>
$$\hat{\Pi}^\dagger \hat{x} \hat{\Pi} = -\hat{x} \iff \{\hat{\Pi}, \hat{x}\} = \hat{\Pi}\hat{x} + \hat{x}\hat{\Pi} = 0$$
$$\hat{\Pi}^\dagger \hat{p} \hat{\Pi} = -\hat{p} \iff \{\hat{\Pi}, \hat{p}\} = 0$$
<p>
Conversely, the orbital angular momentum operator $\hat{\vec{L}} = \hat{\vec{r}} \times \hat{\vec{p}}$ is an axial vector (pseudovector) and commutes with parity:
</p>
$$\hat{\Pi}^\dagger \hat{\vec{L}} \hat{\Pi} = (\hat{\Pi}^\dagger \hat{\vec{r}} \hat{\Pi}) \times (\hat{\Pi}^\dagger \hat{\vec{p}} \hat{\Pi}) = (-\hat{\vec{r}}) \times (-\hat{\vec{p}}) = \hat{\vec{r}} \times \hat{\vec{p}} = \hat{\vec{L}} \implies [\hat{\Pi}, \hat{\vec{L}}] = 0$$

<h3>3. Parity Conservation and Laporte's Selection Rule</h3>
<p>
If the Hamiltonian of a system is invariant under spatial inversion, $V(-\vec{r}) = V(\vec{r})$, then:
</p>
$$[\hat{\Pi}, \hat{H}] = 0$$
<p>
Consequently, stationary states can be chosen as simultaneous eigenstates of $\hat{H}$ and $\hat{\Pi}$. Furthermore, parity is a constant of motion:
</p>
$$\frac{d}{dt}\langle \hat{\Pi} \rangle = \frac{1}{i\hbar}\langle [\hat{\Pi}, \hat{H}] \rangle = 0$$
<p>
For electric dipole transitions mediated by the vector dipole operator $\hat{\vec{d}} = q\hat{\vec{r}}$, the transition matrix element between states $|\psi_i\rangle$ and $|\psi_f\rangle$ with definite parities $\pi_i$ and $\pi_f$ satisfies:
</p>
$$\langle \psi_f | \hat{\vec{r}} | \psi_i \rangle = \langle \psi_f | \hat{\Pi}^\dagger \hat{\Pi} \hat{\vec{r}} \hat{\Pi}^\dagger \hat{\Pi} | \psi_i \rangle = \pi_f \pi_i \langle \psi_f | (-\hat{\vec{r}}) | \psi_i \rangle = -\pi_f \pi_i \langle \psi_f | \hat{\vec{r}} | \psi_i \rangle$$
<p>
Thus, the matrix element is identically zero unless $\pi_f \pi_i = -1$. This establishes <strong>Laporte's selection rule</strong>: electric dipole transitions can only occur between states of opposite parity ($\Delta l = \pm 1$).
</p>
"""
        },
        {
            "id": "sec1-6",
            "title": "The Density Matrix Formalism: Pure vs Mixed States, Ensembles & von Neumann Entropy",
            "content": r"""
<h3>1. Limitations of Pure State Vectors and Statistical Ensembles</h3>
<p>
A single state ket $|\psi\rangle$ describes a <strong>pure state</strong>, in which complete maximal knowledge about the quantum preparation is available. However, in realistic experimental scenarios (such as an unpolarized thermal beam of particles, or a subsystem entangled with an unobserved environment), the system is described by a statistical ensemble: it has classical probability $p_k \ge 0$ of being in state $|\psi_k\rangle$, where $\sum_k p_k = 1$. Note that the kets $\{|\psi_k\rangle\}$ need not be mutually orthogonal.
</p>

<h3>2. The Density Operator</h3>
<p>
To describe such a statistical mixture, John von Neumann introduced the <strong>density operator</strong> (or density matrix) $\hat{\rho}$:
</p>
$$\hat{\rho} \equiv \sum_k p_k |\psi_k\rangle \langle \psi_k|$$
<p>
The ensemble average expectation value of any physical observable $\hat{A}$ is given by:
</p>
$$\langle \hat{A} \rangle = \sum_k p_k \langle \psi_k | \hat{A} | \psi_k \rangle = \sum_k p_k \sum_n \langle \psi_k | u_n \rangle \langle u_n | \hat{A} | \psi_k \rangle = \sum_n \langle u_n | \hat{A} \left( \sum_k p_k |\psi_k\rangle \langle \psi_k| \right) | u_n \rangle$$
$$\langle \hat{A} \rangle = \text{Tr}(\hat{\rho}\hat{A})$$

<h3>3. Mathematical Properties of the Density Operator</h3>
<ol>
  <li><strong>Hermiticity:</strong> $\hat{\rho}^\dagger = \sum_k p_k (|\psi_k\rangle \langle \psi_k|)^\dagger = \hat{\rho}$</li>
  <li><strong>Unit Trace (Conservation of Total Probability):</strong> $\text{Tr}(\hat{\rho}) = \sum_k p_k \langle \psi_k | \psi_k \rangle = \sum_k p_k = 1$</li>
  <li><strong>Positive Semi-Definiteness:</strong> For any ket $|\phi\rangle$, $\langle \phi | \hat{\rho} | \phi \rangle = \sum_k p_k |\langle \phi | \psi_k \rangle|^2 \ge 0$</li>
  <li><strong>Purity Criterion:</strong>
    $$\text{Tr}(\hat{\rho}^2) \le 1$$
    Equality $\text{Tr}(\hat{\rho}^2) = 1 \iff \hat{\rho}^2 = \hat{\rho}$ holds if and only if the state is pure ($\hat{\rho} = |\psi\rangle \langle \psi|$). For a strictly mixed state in an $N$-dimensional Hilbert space, $\frac{1}{N} \le \text{Tr}(\hat{\rho}^2) < 1$.
  </li>
</ol>

<h3>4. von Neumann Entropy and Thermal Density Operators</h3>
<p>
The quantum mechanical generalization of Gibbs-Shannon entropy is the <strong>von Neumann entropy</strong>:
</p>
$$S(\hat{\rho}) = -k_B \text{Tr}(\hat{\rho} \ln \hat{\rho}) = -k_B \sum_j \lambda_j \ln \lambda_j$$
<p>
where $\{\lambda_j\}$ are the eigenvalues of $\hat{\rho}$. For any pure state, $S(\hat{\rho}) = 0$. For a maximally mixed state in $N$ dimensions ($\hat{\rho} = \frac{1}{N}\hat{I}$), $S = k_B \ln N$.
</p>
<p>
For a system in canonical thermal equilibrium at temperature $T = (k_B \beta)^{-1}$, the thermal density operator is:
</p>
$$\hat{\rho}_{\text{th}} = \frac{e^{-\beta \hat{H}}}{\mathcal{Z}}, \quad \mathcal{Z} = \text{Tr}\left(e^{-\beta \hat{H}}\right)$$
"""
        },
        {
            "id": "sec1-7",
            "title": "Algebraic Solution of the Harmonic Oscillator: Ladder Operators & Matrix Mechanics",
            "content": r"""
<h3>1. Factorization of the Harmonic Oscillator Hamiltonian</h3>
<p>
Consider the one-dimensional quantum harmonic oscillator Hamiltonian:
</p>
$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2 \hat{x}^2$$
<p>
We define the dimensionless non-Hermitian creation (raising) operator $\hat{a}^\dagger$ and annihilation (lowering) operator $\hat{a}$:
</p>
$$\hat{a} = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} + \frac{i}{m\omega}\hat{p}\right), \quad \hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} - \frac{i}{m\omega}\hat{p}\right)$$
<p>
Evaluating the commutator of $\hat{a}$ and $\hat{a}^\dagger$ using $[\hat{x}, \hat{p}] = i\hbar$:
</p>
$$[\hat{a}, \hat{a}^\dagger] = \frac{m\omega}{2\hbar}\left[\hat{x} + \frac{i}{m\omega}\hat{p}, \hat{x} - \frac{i}{m\omega}\hat{p}\right] = \frac{m\omega}{2\hbar}\left(-\frac{i}{m\omega}[\hat{x}, \hat{p}] + \frac{i}{m\omega}[\hat{p}, \hat{x}]\right) = \frac{m\omega}{2\hbar}\left(2\frac{\hbar}{m\omega}\right) = 1$$
$$[\hat{a}, \hat{a}^\dagger] = \hat{I}$$
<p>
Multiplying $\hat{a}^\dagger \hat{a}$:
</p>
$$\hat{a}^\dagger \hat{a} = \frac{m\omega}{2\hbar}\left(\hat{x}^2 + \frac{\hat{p}^2}{m^2\omega^2} - \frac{i}{m\omega}[\hat{x}, \hat{p}]\right) = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}$$
<p>
Defining the Hermitian <strong>number operator</strong> $\hat{N} \equiv \hat{a}^\dagger \hat{a}$, the Hamiltonian takes the canonical diagonal form:
</p>
$$\hat{H} = \hbar\omega\left(\hat{N} + \frac{1}{2}\right)$$

<h3>2. The Fock State Eigenvalue Spectrum</h3>
<p>
The commutators of $\hat{N}$ with $\hat{a}$ and $\hat{a}^\dagger$ are:
</p>
$$[\hat{N}, \hat{a}] = [\hat{a}^\dagger \hat{a}, \hat{a}] = [\hat{a}^\dagger, \hat{a}]\hat{a} = -\hat{a}$$
$$[\hat{N}, \hat{a}^\dagger] = [\hat{a}^\dagger \hat{a}, \hat{a}^\dagger] = \hat{a}^\dagger[\hat{a}, \hat{a}^\dagger] = +\hat{a}^\dagger$$
<p>
Let $|n\rangle$ denote an eigenstate of $\hat{N}$ with eigenvalue $n$: $\hat{N}|n\rangle = n|n\rangle$. Then:
</p>
$$\hat{N}(\hat{a}|n\rangle) = (\hat{a}\hat{N} + [\hat{N}, \hat{a}])|n\rangle = (\hat{a}n - \hat{a})|n\rangle = (n - 1)(\hat{a}|n\rangle)$$
$$\hat{N}(\hat{a}^\dagger|n\rangle) = (\hat{a}^\dagger\hat{N} + [\hat{N}, \hat{a}^\dagger])|n\rangle = (\hat{a}^\dagger n + \hat{a}^\dagger)|n\rangle = (n + 1)(\hat{a}^\dagger|n\rangle)$$
<p>
Thus, $\hat{a}$ decreases $n$ by 1, and $\hat{a}^\dagger$ increases $n$ by 1. Since $\langle n | \hat{N} | n \rangle = \|\hat{a}|n\rangle\|^2 \ge 0$, the spectrum must be bounded from below. There must exist a unique ground state $|0\rangle$ such that:
</p>
$$\hat{a}|0\rangle = 0 \implies n = 0$$
<p>
Repeated application of $\hat{a}^\dagger$ generates the complete discrete spectrum:
</p>
$$E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n \in \{0, 1, 2, 3, \dots\}$$
$$|n\rangle = \frac{(\hat{a}^\dagger)^n}{\sqrt{n!}}|0\rangle, \quad \hat{a}|n\rangle = \sqrt{n}|n-1\rangle, \quad \hat{a}^\dagger|n\rangle = \sqrt{n+1}|n+1\rangle$$

<h3>3. Exact Matrix Representation of Operators</h3>
<p>
In the Fock basis $\{|0\rangle, |1\rangle, |2\rangle, \dots\}$, the operators have the infinite-dimensional matrix representations:
</p>
$$\hat{a} \doteq \begin{pmatrix} 0 & \sqrt{1} & 0 & 0 & \dots \\ 0 & 0 & \sqrt{2} & 0 & \dots \\ 0 & 0 & 0 & \sqrt{3} & \dots \\ 0 & 0 & 0 & 0 & \ddots \end{pmatrix}, \quad \hat{a}^\dagger \doteq \begin{pmatrix} 0 & 0 & 0 & 0 & \dots \\ \sqrt{1} & 0 & 0 & 0 & \dots \\ 0 & \sqrt{2} & 0 & 0 & \dots \\ 0 & 0 & \sqrt{3} & 0 & \ddots \end{pmatrix}$$
<p>
Inverting the definitions of $\hat{a}$ and $\hat{a}^\dagger$ expresses the coordinate and momentum operators purely in terms of ladder operators:
</p>
$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a} + \hat{a}^\dagger), \quad \hat{p} = -i\sqrt{\frac{m\hbar\omega}{2}}(\hat{a} - \hat{a}^\dagger)$$
<p>
This yields the off-diagonal Heisenberg matrix mechanics:
</p>
$$\langle n' | \hat{x} | n \rangle = \sqrt{\frac{\hbar}{2m\omega}}\left(\sqrt{n}\delta_{n', n-1} + \sqrt{n+1}\delta_{n', n+1}\right)$$
$$\langle n' | \hat{p} | n \rangle = -i\sqrt{\frac{m\hbar\omega}{2}}\left(\sqrt{n}\delta_{n', n-1} - \sqrt{n+1}\delta_{n', n+1}\right)$$
"""
        }
    ],
    "simulations": [
        {
            "id": "qm2-hilbert-state-sim",
            "title": "Interactive Hilbert State Space & Unitary Basis Rotation",
            "description": "Visualize quantum state kets |ψ⟩, projection onto orthonormal bases |u₁⟩ and |u₂⟩, and continuous unitary SU(2) rotations on the Bloch/state sphere."
        },
        {
            "id": "qm2-ladder-operator-sim",
            "title": "Harmonic Oscillator Fock State Matrix Elements & Ladder Transitions",
            "description": "Interactive matrix element visualizer and ladder transition animator showing â|n⟩ and â†|n⟩ operations, energy levels, and ⟨n|x|m⟩ off-diagonal couplings."
        }
    ],
    "solvedProblems": [
        {
            "number": 1,
            "title": "Spectral Decomposition and Projector Analysis of a 3-Level Hamiltonian",
            "statement": r"A three-level quantum system is governed by the Hamiltonian matrix in an orthonormal basis $\{|1\rangle, |2\rangle, |3\rangle\}$ given by:\n$$\hat{H} = \hbar\omega \begin{pmatrix} 2 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$$\n(a) Find the eigenvalues and normalized eigenvectors of $\hat{H}$.\n(b) Construct the projection operators $\hat{P}_k$ for each energy level and explicitly verify completeness $\sum_k \hat{P}_k = \hat{I}$ and the spectral decomposition $\hat{H} = \sum_k E_k \hat{P}_k$.\n(c) If the system is initially prepared in state $|\psi(0)\rangle = \frac{1}{\sqrt{3}}(|1\rangle + |2\rangle + |3\rangle)$, calculate the probability of measuring the system in energy state $E = 0$ at time $t > 0$.",
            "solution": r"**(a) Eigenvalue Spectrum and Eigenvectors:**\nThe characteristic polynomial is:\n$$\det(\hat{H} - \lambda \hat{I}) = \det\begin{pmatrix} 2\hbar\omega - \lambda & 0 & 0 \\ 0 & -\lambda & \hbar\omega \\ 0 & \hbar\omega & -\lambda \end{pmatrix} = (2\hbar\omega - \lambda)(\lambda^2 - (\hbar\omega)^2) = 0$$\nThe eigenvalues are:\n$$E_1 = 2\hbar\omega, \quad E_2 = +\hbar\omega, \quad E_3 = -\hbar\omega$$\nFinding normalized eigenvectors:\n- For $E_1 = 2\hbar\omega$:\n  $$\hat{H}|E_1\rangle = 2\hbar\omega|E_1\rangle \implies |E_1\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = |1\rangle$$\n- For $E_2 = +\hbar\omega$:\n  $$\begin{pmatrix} 0 & -\hbar\omega & \hbar\omega \\ 0 & \hbar\omega & -\hbar\omega \end{pmatrix} \begin{pmatrix} c_2 \\ c_3 \end{pmatrix} = 0 \implies c_2 = c_3 \implies |E_2\rangle = \frac{1}{\sqrt{2}}(|2\rangle + |3\rangle)$$\n- For $E_3 = -\hbar\omega$:\n  $$\begin{pmatrix} 0 & \hbar\omega & \hbar\omega \\ 0 & \hbar\omega & \hbar\omega \end{pmatrix} \begin{pmatrix} c_2 \\ c_3 \end{pmatrix} = 0 \implies c_2 = -c_3 \implies |E_3\rangle = \frac{1}{\sqrt{2}}(|2\rangle - |3\rangle)$$\n\n**(b) Projection Operators and Spectral Decomposition:**\n$$\hat{P}_1 = |E_1\rangle\langle E_1| = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$\n$$\hat{P}_2 = |E_2\rangle\langle E_2| = \frac{1}{2}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \begin{pmatrix} 0 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1/2 & 1/2 \\ 0 & 1/2 & 1/2 \end{pmatrix}$$\n$$\hat{P}_3 = |E_3\rangle\langle E_3| = \frac{1}{2}\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} \begin{pmatrix} 0 & 1 & -1 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1/2 & -1/2 \\ 0 & -1/2 & 1/2 \end{pmatrix}$$\nSumming the projectors:\n$$\hat{P}_1 + \hat{P}_2 + \hat{P}_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \hat{I}$$\nEvaluating the spectral decomposition:\n$$E_1\hat{P}_1 + E_2\hat{P}_2 + E_3\hat{P}_3 = 2\hbar\omega\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} + \hbar\omega\begin{pmatrix} 0 & 0 & 0 \\ 0 & 1/2 & 1/2 \\ 0 & 1/2 & 1/2 \end{pmatrix} - \hbar\omega\begin{pmatrix} 0 & 0 & 0 \\ 0 & 1/2 & -1/2 \\ 0 & -1/2 & 1/2 \end{pmatrix} = \hbar\omega\begin{pmatrix} 2 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} = \hat{H}$$\n\n**(c) Measurement Probability:**\nThe allowed energy eigenvalues are $2\hbar\omega, \hbar\omega, -\hbar\omega$. An eigenvalue of $0$ is **not** present in the spectrum of $\hat{H}$. Therefore, the probability of measuring energy $E = 0$ is strictly **zero**: $\mathcal{P}(E=0) = 0$."
        },
        {
            "number": 2,
            "title": "Density Matrix Purity, von Neumann Entropy & Spin Measurement Ensemble",
            "statement": r"A statistical ensemble of spin-1/2 particles consists of a 75% fraction of particles prepared in the spin-up state along the $z$-axis, $|+z\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, and a 25% fraction prepared in the spin-down state along the $x$-axis, $|-x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$.\n(a) Write down the density matrix $\hat{\rho}$ of the ensemble in the standard $S_z$ basis.\n(b) Compute $\text{Tr}(\hat{\rho}^2)$ and determine whether the state is pure or mixed.\n(c) Calculate the expectation value $\langle S_x \rangle$ and $\langle S_z \rangle$.\n(d) Calculate the von Neumann entropy $S(\hat{\rho})$.",
            "solution": r"**(a) Constructing the Density Matrix:**\nThe statistical mixture has probabilities $p_1 = 3/4$ and $p_2 = 1/4$:\n$$\hat{\rho} = \frac{3}{4}|+z\rangle\langle +z| + \frac{1}{4}|-x\rangle\langle -x|$$\n$$|+z\rangle\langle +z| = \begin{pmatrix} 1 \\ 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$$\n$$|-x\rangle\langle -x| = \frac{1}{2}\begin{pmatrix} 1 \\ -1 \end{pmatrix}\begin{pmatrix} 1 & -1 \end{pmatrix} = \begin{pmatrix} 1/2 & -1/2 \\ -1/2 & 1/2 \end{pmatrix}$$\nCombining both contributions:\n$$\hat{\rho} = \frac{3}{4}\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \frac{1}{4}\begin{pmatrix} 1/2 & -1/2 \\ -1/2 & 1/2 \end{pmatrix} = \begin{pmatrix} 3/4 + 1/8 & -1/8 \\ -1/8 & 1/8 \end{pmatrix} = \begin{pmatrix} 7/8 & -1/8 \\ -1/8 & 1/8 \end{pmatrix}$$\nNotice that $\text{Tr}(\hat{\rho}) = 7/8 + 1/8 = 1$ and $\hat{\rho}^\dagger = \hat{\rho}$.\n\n**(b) Purity Check:**\n$$\hat{\rho}^2 = \begin{pmatrix} 7/8 & -1/8 \\ -1/8 & 1/8 \end{pmatrix} \begin{pmatrix} 7/8 & -1/8 \\ -1/8 & 1/8 \end{pmatrix} = \begin{pmatrix} 49/64 + 1/64 & -7/64 - 1/64 \\ -7/64 - 1/64 & 1/64 + 1/64 \end{pmatrix} = \begin{pmatrix} 50/64 & -8/64 \\ -8/64 & 2/64 \end{pmatrix}$$\n$$\text{Tr}(\hat{\rho}^2) = \frac{50}{64} + \frac{2}{64} = \frac{52}{64} = \frac{13}{16} = 0.8125$$\nSince $\text{Tr}(\hat{\rho}^2) = 13/16 < 1$, the ensemble is a **mixed state**.\n\n**(c) Expectation Values:**\n$$\hat{S}_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \hat{S}_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$\n$$\langle S_x \rangle = \text{Tr}(\hat{\rho}\hat{S}_x) = \frac{\hbar}{2}\text{Tr}\begin{pmatrix} -1/8 & 7/8 \\ 1/8 & -1/8 \end{pmatrix} = \frac{\hbar}{2}\left(-\frac{1}{8} - \frac{1}{8}\right) = -\frac{\hbar}{8}$$\n$$\langle S_z \rangle = \text{Tr}(\hat{\rho}\hat{S}_z) = \frac{\hbar}{2}\text{Tr}\begin{pmatrix} 7/8 & 1/8 \\ -1/8 & -1/8 \end{pmatrix} = \frac{\hbar}{2}\left(\frac{7}{8} - \frac{1}{8}\right) = \frac{3\hbar}{8}$$\n\n**(d) von Neumann Entropy:**\nThe eigenvalues of $\hat{\rho}$ satisfy $\det(\hat{\rho} - \lambda\hat{I}) = 0$:\n$$\left(\frac{7}{8}-\lambda\right)\left(\frac{1}{8}-\lambda\right) - \left(-\frac{1}{8}\right)^2 = \lambda^2 - \lambda + \frac{7}{64} - \frac{1}{64} = \lambda^2 - \lambda + \frac{6}{64} = 0$$\n$$\lambda = \frac{1 \pm \sqrt{1 - 24/64}}{2} = \frac{1 \pm \sqrt{40/64}}{2} = \frac{1 \pm \frac{\sqrt{10}}{4}}{2} = \frac{4 \pm \sqrt{10}}{8}$$\n$$\lambda_1 \approx 0.8953, \quad \lambda_2 \approx 0.1047$$\n$$S(\hat{\rho}) = -k_B(\lambda_1 \ln\lambda_1 + \lambda_2 \ln\lambda_2) \approx -k_B(0.8953(-0.1106) + 0.1047(-2.257)) = 0.335\,k_B$$"
        },
        {
            "number": 3,
            "title": "Matrix Mechanics Evaluation of Higher-Order Coordinate Moments Using Ladder Operators",
            "statement": r"Using the algebraic ladder operator definitions $\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a} + \hat{a}^\dagger)$ and $[\hat{a}, \hat{a}^\dagger] = 1$:\n(a) Evaluate the expectation value $\langle n | \hat{x}^4 | n \rangle$ for any arbitrary Fock eigenstate $|n\rangle$ of the 1D harmonic oscillator.\n(b) Deduce the quantum ground state ($n=0$) expectation value $\langle 0 | \hat{x}^4 | 0 \rangle$ and verify the quantum uncertainty relationship $\langle x^4 \rangle > (\langle x^2 \rangle)^2$.",
            "solution": r"**(a) Expanding the Fourth Power of Position:**\n$$\hat{x}^4 = \left(\frac{\hbar}{2m\omega}\right)^2 (\hat{a} + \hat{a}^\dagger)^4$$\nLet $\hat{B} \equiv (\hat{a} + \hat{a}^\dagger)^2 = \hat{a}^2 + \hat{a}\hat{a}^\dagger + \hat{a}^\dagger\hat{a} + (\hat{a}^\dagger)^2$.\nUsing $\hat{a}\hat{a}^\dagger = \hat{a}^\dagger\hat{a} + 1 = \hat{N} + 1$:\n$$\hat{B} = \hat{a}^2 + (\hat{a}^\dagger)^2 + 2\hat{N} + 1$$\nNow squaring $\hat{B}$ to obtain $(\hat{a} + \hat{a}^\dagger)^4$:\n$$(\hat{a} + \hat{a}^\dagger)^4 = \hat{B}^2 = [\hat{a}^2 + (\hat{a}^\dagger)^2 + (2\hat{N}+1)]^2$$\nWhen evaluating the diagonal expectation value $\langle n | \dots | n \rangle$, only terms with an equal number of creation and annihilation operators have non-vanishing expectation values. The contributing terms are:\n1. $(2\hat{N} + 1)^2$: $\langle n | (2\hat{N}+1)^2 | n \rangle = (2n + 1)^2$\n2. $\hat{a}^2 (\hat{a}^\dagger)^2$: \n   $$\hat{a}^2(\hat{a}^\dagger)^2|n\rangle = \hat{a}^2 \sqrt{n+1}\sqrt{n+2}|n+2\rangle = \sqrt{n+1}\sqrt{n+2}\sqrt{n+2}\sqrt{n+1}|n\rangle = (n+1)(n+2)|n\rangle$$\n3. $(\hat{a}^\dagger)^2 \hat{a}^2$:\n   $$(\hat{a}^\dagger)^2 \hat{a}^2|n\rangle = (\hat{a}^\dagger)^2 \sqrt{n}\sqrt{n-1}|n-2\rangle = n(n-1)|n\rangle$$\nSumming these three matrix contributions:\n$$\langle n | (\hat{a} + \hat{a}^\dagger)^4 | n \rangle = (2n + 1)^2 + (n+1)(n+2) + n(n-1)$$\nExpanding algebraically:\n$$= (4n^2 + 4n + 1) + (n^2 + 3n + 2) + (n^2 - n) = 6n^2 + 6n + 3 = 3(2n^2 + 2n + 1)$$\nTherefore, the exact coordinate fourth moment is:\n$$\langle n | \hat{x}^4 | n \rangle = \frac{3\hbar^2}{4m^2\omega^2}(2n^2 + 2n + 1)$$\n\n**(b) Ground State Evaluation:**\nSetting $n = 0$:\n$$\langle 0 | \hat{x}^4 | 0 \rangle = \frac{3\hbar^2}{4m^2\omega^2}$$\nComparing with the second moment $\langle 0 | \hat{x}^2 | 0 \rangle = \frac{\hbar}{2m\omega}$:\n$$(\langle 0 | \hat{x}^2 | 0 \rangle)^2 = \left(\frac{\hbar}{2m\omega}\right)^2 = \frac{\hbar^2}{4m^2\omega^2}$$\n$$\frac{\langle 0 | \hat{x}^4 | 0 \rangle}{(\langle 0 | \hat{x}^2 | 0 \rangle)^2} = \frac{\frac{3\hbar^2}{4m^2\omega^2}}{\frac{\hbar^2}{4m^2\omega^2}} = 3 > 1$$\nThis factor of 3 precisely matches the fourth moment of a Gaussian distribution ($\mathbb{E}[x^4] = 3\sigma^4$), confirming that the quantum harmonic oscillator ground state is an exact Gaussian wavepacket."
        }
    ]
}

# ==============================================================================
# CHAPTER 2: QUANTUM DYNAMICS, TIME EVOLUTION & ALTERNATIVE PICTURES
# ==============================================================================
u2 = {
    "id": "unit2",
    "number": 2,
    "title": "Quantum Dynamics, Time Evolution & Alternative Pictures",
    "subtitle": "Time Evolution Operators, Schrödinger, Heisenberg & Dirac Pictures, Heisenberg Oscillator & Rabi Dynamics",
    "description": "Rigorous investigation of quantum dynamical evolution: the unitary time-evolution operator U(t, t0), Dyson series expansions, the fundamental differential equations of motion across the Schrödinger, Heisenberg, and Dirac (interaction) pictures, the operator mechanics of the linear harmonic oscillator in the Heisenberg picture, and the exact dynamics of two-level systems undergoing resonant Rabi flopping.",
    "sections": [
        {
            "id": "sec2-1",
            "title": "The Time-Evolution Operator U(t, t0), Infinitesimal Generators & Unitary Propagators",
            "content": r"""
<h3>1. Postulate of Unitary Time Evolution</h3>
<p>
In quantum mechanics, if a system is prepared in state $|\psi(t_0)\rangle$ at initial time $t_0$, its subsequent state $|\psi(t)\rangle$ at any time $t > t_0$ is generated by a linear time-evolution operator $\hat{U}(t, t_0)$:
</p>
$$|\psi(t)\rangle = \hat{U}(t, t_0)|\psi(t_0)\rangle$$
<p>
Conservation of total probability requires that the norm of the state vector be invariant under temporal evolution:
</p>
$$\langle \psi(t) | \psi(t) \rangle = \langle \psi(t_0) | \hat{U}^\dagger(t, t_0) \hat{U}(t, t_0) | \psi(t_0) \rangle = \langle \psi(t_0) | \psi(t_0) \rangle = 1$$
<p>
This holds for all initial states if and only if $\hat{U}(t, t_0)$ is strictly <strong>unitary</strong>:
</p>
$$\hat{U}^\dagger(t, t_0) \hat{U}(t, t_0) = \hat{U}(t, t_0) \hat{U}^\dagger(t, t_0) = \hat{I}$$
<p>
Additionally, the evolution operator satisfies the group composition property:
</p>
$$\hat{U}(t, t_1)\hat{U}(t_1, t_0) = \hat{U}(t, t_0), \quad \hat{U}(t_0, t_0) = \hat{I}, \quad \hat{U}^{-1}(t, t_0) = \hat{U}(t_0, t)$$

<h3>2. Infinitesimal Time Evolution and the Hamiltonian Generator</h3>
<p>
Consider an infinitesimal time step $dt$. Since $\hat{U}(t_0, t_0) = \hat{I}$, $\hat{U}(t_0 + dt, t_0)$ can be expanded to first order in $dt$:
</p>
$$\hat{U}(t_0 + dt, t_0) = \hat{I} - \frac{i}{\hbar}\hat{\Omega} \, dt$$
<p>
The unitarity condition $(\hat{I} + \frac{i}{\hbar}\hat{\Omega}^\dagger dt)(\hat{I} - \frac{i}{\hbar}\hat{\Omega} dt) = \hat{I} + \frac{i}{\hbar}(\hat{\Omega}^\dagger - \hat{\Omega})dt + \mathcal{O}(dt^2) = \hat{I}$ demands that $\hat{\Omega}^\dagger = \hat{\Omega}$. By Planck's quantum hypothesis, the Hermitian generator of time translations is the energy observable, the Hamiltonian $\hat{H}$:
</p>
$$\hat{\Omega} = \hat{H}$$
<p>
Forming the difference quotient:
</p>
$$\frac{\partial}{\partial t}\hat{U}(t, t_0) = \lim_{dt \to 0} \frac{\hat{U}(t+dt, t_0) - \hat{U}(t, t_0)}{dt} = \lim_{dt \to 0} \frac{(\hat{I} - \frac{i}{\hbar}\hat{H}(t)dt - \hat{I})\hat{U}(t, t_0)}{dt}$$
$$i\hbar \frac{\partial}{\partial t}\hat{U}(t, t_0) = \hat{H}(t)\hat{U}(t, t_0)$$

<h3>3. Integration Cases: From Conservative Systems to the Dyson Series</h3>
<p>
Three cases govern the explicit mathematical form of $\hat{U}(t, t_0)$:
</p>
<ol>
  <li><strong>Time-Independent Hamiltonian ($\hat{H} \ne f(t)$):</strong>
    $$\hat{U}(t, t_0) = \exp\left(-\frac{i}{\hbar}\hat{H}(t - t_0)\right) = \sum_{n=0}^\infty \frac{1}{n!} \left(-\frac{i}{\hbar}\hat{H}(t - t_0)\right)^n$$
  </li>
  <li><strong>Commuting Time-Dependent Hamiltonian ($[\hat{H}(t_1), \hat{H}(t_2)] = 0$):</strong>
    $$\hat{U}(t, t_0) = \exp\left(-\frac{i}{\hbar}\int_{t_0}^t \hat{H}(t')\,dt'\right)$$
  </li>
  <li><strong>General Non-Commuting Time-Dependent Hamiltonian:</strong>
    Direct integration leads to the integral equation:
    $$\hat{U}(t, t_0) = \hat{I} - \frac{i}{\hbar}\int_{t_0}^t \hat{H}(t_1)\hat{U}(t_1, t_0)\,dt_1$$
    Iterative substitution generates the famous <strong>Dyson series</strong>:
    $$\hat{U}(t, t_0) = \hat{I} + \sum_{n=1}^\infty \left(-\frac{i}{\hbar}\right)^n \int_{t_0}^t dt_1 \int_{t_0}^{t_1} dt_2 \cdots \int_{t_0}^{t_{n-1}} dt_n \hat{H}(t_1)\hat{H}(t_2)\cdots \hat{H}(t_n)$$
    Using the time-ordering meta-operator $\mathcal{T}$, which rearranges operators in descending chronological order:
    $$\hat{U}(t, t_0) = \mathcal{T}\exp\left(-\frac{i}{\hbar}\int_{t_0}^t \hat{H}(t')\,dt'\right)$$
  </li>
</ol>
"""
        },
        {
            "id": "sec2-2",
            "title": "Schrödinger Picture: Dynamics of State Kets & Stationary States",
            "content": r"""
<h3>1. The Schrödinger Equation of Motion</h3>
<p>
In the <strong>Schrödinger picture</strong>, all time dependence resides within the state vectors $|\psi_S(t)\rangle$, while observable operators $\hat{A}_S$ remain constant in time (unless they possess explicit parametric time dependence, such as a time-varying external electric field).
</p>
<p>
Applying the time evolution operator equation to $|\psi_S(t)\rangle = \hat{U}(t, 0)|\psi_S(0)\rangle$:
</p>
$$i\hbar \frac{\partial}{\partial t}|\psi_S(t)\rangle = i\hbar \frac{\partial \hat{U}(t, 0)}{\partial t}|\psi_S(0)\rangle = \hat{H}\hat{U}(t, 0)|\psi_S(0)\rangle$$
$$i\hbar \frac{\partial}{\partial t}|\psi_S(t)\rangle = \hat{H}|\psi_S(t)\rangle$$
<p>
Projecting this abstract ket equation onto continuous coordinate eigenstates $\langle x|$ yields the familiar partial differential Schrödinger wave equation:
</p>
$$i\hbar \frac{\partial \psi(x, t)}{\partial t} = \left(-\frac{\hbar^2}{2m}\nabla^2 + V(x)\right)\psi(x, t)$$

<h3>2. Stationary States and Constant Expectation Values</h3>
<p>
If the Hamiltonian is time-independent, its energy eigenstates satisfy $\hat{H}|E_n\rangle = E_n |E_n\rangle$. Expanding the initial state in the energy basis:
</p>
$$|\psi_S(0)\rangle = \sum_n c_n |E_n\rangle \implies |\psi_S(t)\rangle = e^{-i\hat{H}t/\hbar}\sum_n c_n |E_n\rangle = \sum_n c_n e^{-i E_n t/\hbar} |E_n\rangle$$
<p>
If the system is prepared in a pure energy eigenstate $|\psi_S(0)\rangle = |E_k\rangle$, its state vector evolves solely by an overall global phase factor:
</p>
$$|\psi_S(t)\rangle = e^{-i E_k t/\hbar}|E_k\rangle$$
<p>
The expectation value of any time-independent observable $\hat{A}_S$ in this state is strictly constant:
</p>
$$\langle \hat{A}_S \rangle(t) = \langle \psi_S(t) | \hat{A}_S | \psi_S(t) \rangle = e^{iE_k t/\hbar} \langle E_k | \hat{A}_S | E_k \rangle e^{-iE_k t/\hbar} = \langle E_k | \hat{A}_S | E_k \rangle$$
<p>
Hence, energy eigenstates are termed <strong>stationary states</strong>: neither probability densities nor physical expectation values depend on time.
</p>
"""
        },
        {
            "id": "sec2-3",
            "title": "Heisenberg Picture: Time-Dependent Operators & Heisenberg Equations of Motion",
            "content": r"""
<h3>1. Formulation of the Heisenberg Picture</h3>
<p>
Werner Heisenberg formulated quantum dynamics by holding state vectors fixed at their initial values while transferring the entire temporal evolution onto the operators. By definition, expectation values must be identical in both pictures:
</p>
$$\langle \hat{A} \rangle(t) = \langle \psi_S(t) | \hat{A}_S | \psi_S(t) \rangle = \langle \psi_S(0) | \hat{U}^\dagger(t, 0) \hat{A}_S \hat{U}(t, 0) | \psi_S(0) \rangle \equiv \langle \psi_H | \hat{A}_H(t) | \psi_H \rangle$$
<p>
This establishes the unitary transformation between Schrödinger and Heisenberg pictures:
</p>
$$|\psi_H\rangle \equiv |\psi_S(0)\rangle, \quad \frac{\partial}{\partial t}|\psi_H\rangle = 0$$
$$\hat{A}_H(t) \equiv \hat{U}^\dagger(t, 0) \hat{A}_S \hat{U}(t, 0)$$

<h3>2. The Heisenberg Equation of Motion</h3>
<p>
Differentiating the Heisenberg operator $\hat{A}_H(t)$ with respect to time:
</p>
$$\frac{d\hat{A}_H}{dt} = \frac{\partial \hat{U}^\dagger}{\partial t} \hat{A}_S \hat{U} + \hat{U}^\dagger \hat{A}_S \frac{\partial \hat{U}}{\partial t} + \hat{U}^\dagger \left(\frac{\partial \hat{A}_S}{\partial t}\right) \hat{U}$$
<p>
Since $i\hbar \frac{\partial \hat{U}}{\partial t} = \hat{H}\hat{U} \implies \frac{\partial \hat{U}}{\partial t} = -\frac{i}{\hbar}\hat{H}\hat{U}$, and taking the Hermitian adjoint yields $\frac{\partial \hat{U}^\dagger}{\partial t} = \frac{i}{\hbar}\hat{U}^\dagger \hat{H}$:
</p>
$$\frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}\hat{U}^\dagger \hat{H} \hat{A}_S \hat{U} - \frac{i}{\hbar}\hat{U}^\dagger \hat{A}_S \hat{H} \hat{U} + \left(\frac{\partial \hat{A}_S}{\partial t}\right)_H$$
<p>
Noting that $\hat{U}^\dagger \hat{H} \hat{U} = \hat{H}_H$, we arrive at the celebrated <strong>Heisenberg Equation of Motion</strong>:
</p>
$$\frac{d\hat{A}_H}{dt} = \frac{1}{i\hbar}[\hat{A}_H, \hat{H}_H] + \left(\frac{\partial \hat{A}}{\partial t}\right)_H$$

<h3>3. Connection to Classical Mechanics: Poisson Brackets & Ehrenfest's Theorem</h3>
<p>
The Heisenberg equation of motion displays a profound isomorphism with the classical Hamilton-Jacobi equation:
</p>
$$\frac{df}{dt} = \{f, H\}_{\text{classical}} + \frac{\partial f}{\partial t}$$
<p>
Dirac established the canonical quantization postulate by mapping classical Poisson brackets to quantum commutators:
</p>
$$\{\cdot, \cdot\}_{\text{classical}} \longleftrightarrow \frac{1}{i\hbar}[\cdot, \cdot]$$
<p>
Taking the expectation value of the Heisenberg equation yields <strong>Ehrenfest's Theorem</strong>:
</p>
$$\frac{d}{dt}\langle \hat{A} \rangle = \frac{1}{i\hbar}\langle [\hat{A}, \hat{H}] \rangle + \left\langle \frac{\partial \hat{A}}{\partial t} \right\rangle$$
<p>
Specifically, for a particle in a potential $V(\hat{x})$:
</p>
$$\frac{d}{dt}\langle \hat{x} \rangle = \frac{\langle \hat{p} \rangle}{m}, \quad \frac{d}{dt}\langle \hat{p} \rangle = -\left\langle \frac{\partial V(\hat{x})}{\partial \hat{x}} \right\rangle$$
<p>
Quantum expectation values follow classical Newtonian equations of motion, provided the spatial spread of the wavepacket is small compared to the scale of spatial variation of the potential.
</p>
"""
        },
        {
            "id": "sec2-4",
            "title": "Dirac (Interaction) Picture: Partitioning the Hamiltonian H = H0 + V(t)",
            "content": r"""
<h3>1. Motivation and Partitioning of the Hamiltonian</h3>
<p>
In many advanced quantum systems, the total Hamiltonian can be split into an unperturbed exactly solvable part $\hat{H}_0$ and a small or time-dependent perturbation $\hat{V}(t)$:
</p>
$$\hat{H}(t) = \hat{H}_0 + \hat{V}(t)$$
<p>
The <strong>Dirac (interaction) picture</strong> provides an intermediate representation where the fast trivial evolution governed by $\hat{H}_0$ is factored into the operators, while the slow non-trivial transition dynamics governed by $\hat{V}(t)$ is transferred to the state vectors.
</p>

<h3>2. State Vectors and Operators in the Interaction Picture</h3>
<p>
The state vector in the interaction picture is defined by stripping off the unperturbed evolution:
</p>
$$|\psi_I(t)\rangle \equiv e^{i\hat{H}_0 t/\hbar}|\psi_S(t)\rangle$$
<p>
For observables to yield identical expectation values, $\langle \psi_S(t) | \hat{A}_S | \psi_S(t) \rangle = \langle \psi_I(t) | \hat{A}_I(t) | \psi_I(t) \rangle$:
</p>
$$\hat{A}_I(t) \equiv e^{i\hat{H}_0 t/\hbar}\hat{A}_S e^{-i\hat{H}_0 t/\hbar}$$

<h3>3. Dual Equations of Motion</h3>
<p>
Differentiating the interaction state ket $|\psi_I(t)\rangle$:
</p>
$$i\hbar \frac{\partial}{\partial t}|\psi_I(t)\rangle = i\hbar\left(\frac{i\hat{H}_0}{\hbar}e^{i\hat{H}_0 t/\hbar}|\psi_S(t)\rangle + e^{i\hat{H}_0 t/\hbar}\frac{\partial |\psi_S(t)\rangle}{\partial t}\right)$$
$$= -\hat{H}_0|\psi_I(t)\rangle + e^{i\hat{H}_0 t/\hbar}(\hat{H}_0 + \hat{V}(t))|\psi_S(t)\rangle$$
$$= -\hat{H}_0|\psi_I(t)\rangle + \hat{H}_0|\psi_I(t)\rangle + e^{i\hat{H}_0 t/\hbar}\hat{V}(t)e^{-i\hat{H}_0 t/\hbar}|\psi_I(t)\rangle$$
$$i\hbar \frac{\partial}{\partial t}|\psi_I(t)\rangle = \hat{V}_I(t)|\psi_I(t)\rangle$$
<p>
State vectors evolve solely under the interaction potential $\hat{V}_I(t)$. Conversely, differentiating the operator $\hat{A}_I(t)$ yields:
</p>
$$\frac{d\hat{A}_I}{dt} = \frac{1}{i\hbar}[\hat{A}_I, \hat{H}_0] + \left(\frac{\partial \hat{A}}{\partial t}\right)_I$$
<p>
Operators evolve strictly under the unperturbed Hamiltonian $\hat{H}_0$. The interaction picture is the foundational framework for time-dependent perturbation theory, S-matrix scattering, and relativistic quantum field theory.
</p>
"""
        },
        {
            "id": "sec2-5",
            "title": "Dynamical Evolution of the Linear Harmonic Oscillator in the Heisenberg Picture",
            "content": r"""
<h3>1. Heisenberg Equations of Motion for Coordinate and Momentum</h3>
<p>
Consider the one-dimensional harmonic oscillator with time-independent Hamiltonian:
</p>
$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2 \hat{x}^2$$
<p>
Applying the Heisenberg equation of motion to the position operator $\hat{x}_H(t)$:
</p>
$$\frac{d\hat{x}_H}{dt} = \frac{1}{i\hbar}[\hat{x}_H, \hat{H}] = \frac{1}{i\hbar}\left[\hat{x}_H, \frac{\hat{p}_H^2}{2m}\right] = \frac{1}{i\hbar}\frac{1}{2m}(2i\hbar\hat{p}_H) = \frac{\hat{p}_H(t)}{m}$$
<p>
Applying it to the momentum operator $\hat{p}_H(t)$:
</p>
$$\frac{d\hat{p}_H}{dt} = \frac{1}{i\hbar}[\hat{p}_H, \hat{H}] = \frac{1}{i\hbar}\left[\hat{p}_H, \frac{1}{2}m\omega^2\hat{x}_H^2\right] = \frac{1}{i\hbar}\frac{1}{2}m\omega^2(-2i\hbar\hat{x}_H) = -m\omega^2\hat{x}_H(t)$$

<h3>2. Exact Operator Solutions</h3>
<p>
Differentiating $\frac{d\hat{x}_H}{dt}$ once more with respect to time:
</p>
$$\frac{d^2\hat{x}_H}{dt^2} = \frac{1}{m}\frac{d\hat{p}_H}{dt} = -\omega^2 \hat{x}_H(t)$$
<p>
This is an operator second-order linear differential equation, with the exact operator solution:
</p>
$$\hat{x}_H(t) = \hat{x}_H(0)\cos(\omega t) + \frac{\hat{p}_H(0)}{m\omega}\sin(\omega t)$$
$$\hat{p}_H(t) = m\frac{d\hat{x}_H}{dt} = \hat{p}_H(0)\cos(\omega t) - m\omega \hat{x}_H(0)\sin(\omega t)$$
<p>
Notice that the equal-time commutator remains invariant for all time $t$:
</p>
$$[\hat{x}_H(t), \hat{p}_H(t)] = [\hat{x}(0)\cos\omega t + \frac{\hat{p}(0)}{m\omega}\sin\omega t, \hat{p}(0)\cos\omega t - m\omega\hat{x}(0)\sin\omega t]$$
$$= \cos^2(\omega t)[\hat{x}(0), \hat{p}(0)] - \sin^2(\omega t)[\frac{\hat{p}(0)}{m\omega}, m\omega\hat{x}(0)] = (\cos^2\omega t + \sin^2\omega t)[\hat{x}(0), \hat{p}(0)] = i\hbar\hat{I}$$

<h3>3. Evolution of Ladder Operators</h3>
<p>
In terms of the creation and annihilation operators:
</p>
$$\frac{d\hat{a}_H}{dt} = \frac{1}{i\hbar}[\hat{a}_H, \hbar\omega(\hat{a}_H^\dagger\hat{a}_H + 1/2)] = \frac{\hbar\omega}{i\hbar}[\hat{a}_H, \hat{a}_H^\dagger\hat{a}_H] = -i\omega\hat{a}_H(t)$$
$$\implies \hat{a}_H(t) = \hat{a}_H(0)e^{-i\omega t}, \quad \hat{a}_H^\dagger(t) = \hat{a}_H^\dagger(0)e^{+i\omega t}$$
<p>
This illustrates that in the Heisenberg picture, the ladder operators rotate in the complex phase plane at the classical frequency $\omega$.
</p>
"""
        },
        {
            "id": "sec2-6",
            "title": "Two-Level Systems and Precession Dynamics: Magnetic Dipoles & Rabi Oscillations",
            "content": r"""
<h3>1. Two-Level State Space Hamiltonian</h3>
<p>
Consider a quantum two-level system with unperturbed basis states $\{|1\rangle, |2\rangle\}$, energies $E_1 = \hbar\omega_1$ and $E_2 = \hbar\omega_2$, coupled by an oscillating classical driving field of angular frequency $\omega$:
</p>
$$\hat{H}(t) = \begin{pmatrix} E_1 & V_{12} e^{i\omega t} \\ V_{21} e^{-i\omega t} & E_2 \end{pmatrix}, \quad V_{21} = V_{12}^* \equiv \frac{\hbar\Omega_R}{2}$$
<p>
where $\Omega_R = \frac{2|V_{12}|}{\hbar}$ is the on-resonance <strong>Rabi frequency</strong>. Expanding the general state vector $|\psi(t)\rangle = c_1(t)|1\rangle + c_2(t)|2\rangle$, the time-dependent Schrödinger equation $i\hbar \frac{d}{dt}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \hat{H}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$ yields the coupled system:
</p>
$$i\dot{c}_1 = \omega_1 c_1 + \frac{\Omega_R}{2} e^{i\omega t} c_2$$
$$i\dot{c}_2 = \omega_2 c_2 + \frac{\Omega_R}{2} e^{-i\omega t} c_1$$

<h3>2. Rotating Wave Transformation & Exact Rabi Solution</h3>
<p>
Defining the transition frequency $\omega_0 \equiv \omega_2 - \omega_1$ and the detuning $\Delta \equiv \omega - \omega_0$, we transform amplitudes to remove high-frequency oscillations:
</p>
$$c_1(t) = a_1(t) e^{-i\omega_1 t}, \quad c_2(t) = a_2(t) e^{-i(\omega_2 - \Delta)t}$$
<p>
Assuming the system is initially prepared in state $|1\rangle$, so $a_1(0) = 1$ and $a_2(0) = 0$, solving the coupled differential equations yields the probability of finding the system in excited state $|2\rangle$ at time $t$:
</p>
$$\mathcal{P}_{1\to 2}(t) = |c_2(t)|^2 = \frac{\Omega_R^2}{\Omega_{\text{eff}}^2} \sin^2\left(\frac{\Omega_{\text{eff}} t}{2}\right)$$
<p>
where the generalized effective Rabi frequency $\Omega_{\text{eff}}$ is defined by:
</p>
$$\Omega_{\text{eff}} \equiv \sqrt{\Omega_R^2 + \Delta^2}$$

<h3>3. Physical Interpretation: Resonance, Power Broadening & Flopping</h3>
<p>
Two key physical consequences emerge:
</p>
<ol>
  <li><strong>Complete Inversion at Resonance ($\Delta = 0$):</strong>
    When the driving frequency exactly matches the Bohr transition frequency ($\omega = \omega_0$), the transition probability simplifies to:
    $$\mathcal{P}_{1\to 2}(t) = \sin^2\left(\frac{\Omega_R t}{2}\right)$$
    At time $t = \pi / \Omega_R$ (termed a <strong>$\pi$-pulse</strong>), the population is completely inverted into state $|2\rangle$ with 100% probability. A pulse of duration $t = \pi / (2\Omega_R)$ (a <strong>$\pi/2$-pulse</strong>) creates an equal coherent superposition $\frac{1}{\sqrt{2}}(|1\rangle - i|2\rangle)$.
  </li>
  <li><strong>Detuning Suppression:</strong>
    As the detuning $|\Delta|$ increases, the maximum possible transition probability drops to $\left(\frac{\Omega_R}{\Omega_{\text{eff}}}\right)^2 = \frac{\Omega_R^2}{\Omega_R^2 + \Delta^2} < 1$, while the oscillation frequency increases to $\Omega_{\text{eff}} > \Omega_R$.
  </li>
</ol>
"""
        }
    ],
    "simulations": [
        {
            "id": "qm2-heisenberg-dynamics-sim",
            "title": "Heisenberg Operator Dynamics & Phase Space Trajectories",
            "description": "Real-time simulation of operator expectation values ⟨x(t)⟩ and ⟨p(t)⟩ in the Heisenberg picture, showing classical trajectory correspondence and quantum phase-plane orbits."
        },
        {
            "id": "qm2-rabi-oscillations-sim",
            "title": "Interactive Two-Level Rabi Flopping & Detuning Resonance",
            "description": "Interactive two-level driven atom simulator with adjustable driving frequency, detuning Δ, and Rabi frequency ΩR, displaying population inversion and Bloch sphere nutation."
        }
    ],
    "solvedProblems": [
        {
            "number": 1,
            "title": "Driven Quantum Harmonic Oscillator in the Heisenberg Picture",
            "statement": r"A 1D quantum harmonic oscillator is perturbed by an external time-dependent driving force $F(t)$, described by the Hamiltonian:\n$$\hat{H}(t) = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2 \hat{x}^2 - F(t)\hat{x}$$\n(a) Derive the Heisenberg equations of motion for the operators $\hat{x}_H(t)$ and $\hat{p}_H(t)$.\n(b) Solve for $\hat{x}_H(t)$ in terms of the initial operators $\hat{x}(0)$, $\hat{p}(0)$, and the driving force $F(t)$.\n(c) Assuming the oscillator is in its ground state $|0\rangle$ at $t = 0$, evaluate the expectation value $\langle 0 | \hat{x}_H(t) | 0 \rangle$.",
            "solution": r"**(a) Heisenberg Equations of Motion:**\nUsing $\frac{d\hat{A}_H}{dt} = \frac{1}{i\hbar}[\hat{A}_H, \hat{H}]$:\n$$\frac{d\hat{x}_H}{dt} = \frac{1}{i\hbar}\left[\hat{x}_H, \frac{\hat{p}_H^2}{2m}\right] = \frac{\hat{p}_H(t)}{m}$$\n$$\frac{d\hat{p}_H}{dt} = \frac{1}{i\hbar}\left[\hat{p}_H, \frac{1}{2}m\omega^2\hat{x}_H^2 - F(t)\hat{x}_H\right] = -m\omega^2\hat{x}_H(t) + F(t)\hat{I}$$\n\n**(b) Explicit Operator Solution:**\nDifferentiating $\frac{d\hat{x}_H}{dt}$ yields the inhomogeneous harmonic equation:\n$$\frac{d^2\hat{x}_H}{dt^2} + \omega^2\hat{x}_H(t) = \frac{F(t)}{m}\hat{I}$$\nThe general solution is the homogeneous solution plus the particular integral found via Green's function:\n$$\hat{x}_H(t) = \hat{x}(0)\cos(\omega t) + \frac{\hat{p}(0)}{m\omega}\sin(\omega t) + \frac{\hat{I}}{m\omega}\int_0^t F(t')\sin[\omega(t - t')]\,dt'$$\n\n**(c) Ground State Expectation Value:**\nTaking the expectation value with respect to the initial ground state $|0\rangle$:\n$$\langle 0 | \hat{x}(0) | 0 \rangle = 0, \quad \langle 0 | \hat{p}(0) | 0 \rangle = 0$$\nTherefore, the homogeneous operator terms vanish identically:\n$$\langle 0 | \hat{x}_H(t) | 0 \rangle = \frac{1}{m\omega}\int_0^t F(t')\sin[\omega(t - t')]\,dt'$$\nThis demonstrates that the center of the quantum wavepacket exactly follows the classical trajectory $x_{\text{classical}}(t)$ of a driven oscillator starting from rest at the origin."
        },
        {
            "number": 2,
            "title": "Quantum Propagator for a Particle in a Uniform Gravitational/Electric Field",
            "statement": r"A particle of mass $m$ moves in a uniform potential $V(x) = -Fx$, where $F$ is a constant force (e.g. gravitational $mg$ or electric $q\mathcal{E}$).\n(a) Using the Heisenberg equation of motion, find exact closed expressions for $\hat{x}_H(t)$ and $\hat{p}_H(t)$.\n(b) Express the unitary time-evolution operator $\hat{U}(t, 0) = \exp\left(-\frac{i}{\hbar}\hat{H}t\right)$ as a product of single-variable exponential operators using the Baker-Campbell-Hausdorff formula.\n(c) Compute the quantum expectation value $\langle x(t) \rangle$ if the initial state is a localized wavepacket with $\langle x(0) \rangle = x_0$ and $\langle p(0) \rangle = p_0$.",
            "solution": r"**(a) Heisenberg Equations:**\n$$\hat{H} = \frac{\hat{p}^2}{2m} - F\hat{x}$$\n$$\frac{d\hat{x}_H}{dt} = \frac{1}{i\hbar}[\hat{x}_H, \hat{H}] = \frac{\hat{p}_H}{m}$$\n$$\frac{d\hat{p}_H}{dt} = \frac{1}{i\hbar}[\hat{p}_H, -F\hat{x}_H] = F\hat{I}$$\nIntegrating $\frac{d\hat{p}_H}{dt}$ directly:\n$$\hat{p}_H(t) = \hat{p}(0) + F t \hat{I}$$\nSubstituting $\hat{p}_H(t)$ into $\frac{d\hat{x}_H}{dt}$ and integrating:\n$$\hat{x}_H(t) = \hat{x}(0) + \frac{\hat{p}(0)}{m}t + \frac{1}{2}\frac{F}{m}t^2 \hat{I}$$\n\n**(b) Operator Factorization:**\nLet $\hat{A} = -\frac{it}{\hbar}\frac{\hat{p}^2}{2m}$ and $\hat{B} = \frac{it}{\hbar}F\hat{x}$.\nEvaluating their commutator:\n$$[\hat{A}, \hat{B}] = \left(-\frac{it}{\hbar}\frac{1}{2m}\right)\left(\frac{itF}{\hbar}\right)[\hat{p}^2, \hat{x}] = \frac{t^2 F}{2m\hbar^2}(-2i\hbar\hat{p}) = -\frac{it^2 F}{m\hbar}\hat{p}$$\nNotice that $[[\hat{A}, \hat{B}], \hat{A}] = 0$, but $[[\hat{A}, \hat{B}], \hat{B}] = -\frac{it^2 F}{m\hbar}\left(\frac{itF}{\hbar}\right)[\hat{p}, \hat{x}] = -\frac{t^3 F^2}{m\hbar^2}\hat{I}$, which is a c-number commuting with all operators. By the Zassenhaus/BCH formula:\n$$e^{\hat{A} + \hat{B}} = e^{\hat{A}} e^{\hat{B}} e^{-\frac{1}{2}[\hat{A}, \hat{B}]} e^{\frac{1}{6}(2[\hat{B},[\hat{A},\hat{B}]] + [\hat{A},[\hat{A},\hat{B}]])} = \exp\left(-\frac{it\hat{p}^2}{2m\hbar}\right)\exp\left(\frac{itF\hat{x}}{\hbar}\right)\exp\left(\frac{it^2 F\hat{p}}{2m\hbar}\right)\exp\left(-\frac{it^3 F^2}{6m\hbar}\right)$$\n\n**(c) Expectation Values:**\nTaking the expectation values of the exact operator equations found in part (a):\n$$\langle \hat{x}(t) \rangle = \langle \hat{x}(0) \rangle + \frac{\langle \hat{p}(0) \rangle}{m}t + \frac{F}{2m}t^2 = x_0 + \frac{p_0}{m}t + \frac{1}{2}a t^2$$\nwhere $a = F/m$. The quantum wavepacket accelerates identically to a classical Galilean particle."
        },
        {
            "number": 3,
            "title": "Exact Two-Level Rabi Inversion and Resonant Population Transfer",
            "statement": r"A two-level atomic system with ground state $|g\rangle$ and excited state $|e\rangle$ separated by energy $\hbar\omega_0$ is illuminated by a monochromatic laser field of frequency $\omega$ with dipole coupling $V(t) = \hbar\Omega_R \cos(\omega t)(|e\rangle\langle g| + |g\rangle\langle e|)$.\n(a) In the rotating wave approximation (RWA), write down the interaction Hamiltonian $\hat{V}_I(t)$ and the equations of motion for the probability amplitudes $c_g(t)$ and $c_e(t)$.\n(b) If the atom is initially in state $|g\rangle$ and the laser is precisely on resonance ($\omega = \omega_0$), determine the shortest laser pulse duration $\tau_{\pi}$ required to achieve 100% excitation to state $|e\rangle$ (a $\pi$-pulse).\n(c) For a detuned laser with $\Delta = \omega - \omega_0 = \sqrt{3}\Omega_R$, compute the maximum transition probability and the period of population oscillation.",
            "solution": r"**(a) Equations of Motion under RWA:**\nIn the interaction picture, $\hat{V}_I(t) = e^{i\hat{H}_0 t/\hbar}\hat{V}(t)e^{-i\hat{H}_0 t/\hbar}$:\n$$\hat{V}_I(t) = \hbar\Omega_R \frac{e^{i\omega t} + e^{-i\omega t}}{2}\left( e^{i\omega_0 t}|e\rangle\langle g| + e^{-i\omega_0 t}|g\rangle\langle e| \right)$$\nNeglecting the rapidly oscillating terms $e^{\pm i(\omega + \omega_0)t}$ (RWA):\n$$\hat{V}_I(t) \approx \frac{\hbar\Omega_R}{2}\left( e^{i(\omega_0 - \omega)t}|e\rangle\langle g| + e^{-i(\omega_0 - \omega)t}|g\rangle\langle e| \right) = \frac{\hbar\Omega_R}{2}\left( e^{-i\Delta t}|e\rangle\langle g| + e^{i\Delta t}|g\rangle\langle e| \right)$$\nThe amplitude equations $i\hbar \dot{c}_j = \sum_k \langle j | \hat{V}_I | k \rangle c_k$ become:\n$$i\dot{c}_g(t) = \frac{\Omega_R}{2}e^{i\Delta t} c_e(t), \quad i\dot{c}_e(t) = \frac{\Omega_R}{2}e^{-i\Delta t} c_g(t)$$\n\n**(b) Resonant Transition and $\pi$-Pulse Duration:**\nOn resonance ($\Delta = 0$):\n$$\ddot{c}_e(t) = -\frac{i\Omega_R}{2}\dot{c}_g(t) = -\frac{\Omega_R^2}{4}c_e(t)$$\nWith initial conditions $c_g(0) = 1, c_e(0) = 0$:\n$$c_e(t) = -i\sin\left(\frac{\Omega_R t}{2}\right) \implies \mathcal{P}_e(t) = |c_e(t)|^2 = \sin^2\left(\frac{\Omega_R t}{2}\right)$$\nComplete excitation occurs when $\mathcal{P}_e(t) = 1$, requiring $\frac{\Omega_R t}{2} = \frac{\pi}{2}$:\n$$\tau_{\pi} = \frac{\pi}{\Omega_R}$$\n\n**(c) Detuned Case ($\Delta = \sqrt{3}\Omega_R$):**\nThe effective generalized Rabi frequency is:\n$$\Omega_{\text{eff}} = \sqrt{\Omega_R^2 + \Delta^2} = \sqrt{\Omega_R^2 + 3\Omega_R^2} = \sqrt{4\Omega_R^2} = 2\Omega_R$$\nThe transition probability is:\n$$\mathcal{P}_e(t) = \frac{\Omega_R^2}{\Omega_{\text{eff}}^2}\sin^2\left(\frac{\Omega_{\text{eff}}t}{2}\right) = \frac{\Omega_R^2}{4\Omega_R^2}\sin^2(\Omega_R t) = \frac{1}{4}\sin^2(\Omega_R t)$$\n- Maximum transition probability: $\mathcal{P}_{\max} = \frac{1}{4} = 25\\%$\n- Period of population oscillation: $T = \frac{2\pi}{\Omega_{\text{eff}}} = \frac{2\pi}{2\Omega_R} = \frac{\pi}{\Omega_R}$."
        }
    ]
}

with open("qm2_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1, f, indent=2)
print("Saved qm2_u1.json")

with open("qm2_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2, f, indent=2)
print("Saved qm2_u2.json")
