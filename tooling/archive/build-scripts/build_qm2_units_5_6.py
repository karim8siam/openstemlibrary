import json

# ==============================================================================
# CHAPTER 5: GENERAL THEORY OF ANGULAR MOMENTUM & CLEBSCH-GORDAN COEFFICIENTS
# ==============================================================================
u5 = {
    "id": "unit5",
    "number": 5,
    "title": "General Theory of Angular Momentum & Clebsch-Gordan Coefficients",
    "subtitle": "Lie Algebra of Rotations, Ladder Operators, Spin-1/2, Addition of Angular Momenta, CG Coefficients & Wigner-Eckart Theorem",
    "description": "Comprehensive mathematical exposition of quantum angular momentum: the Lie algebra of spatial rotations [Ji, Jj] = iħ εijk Jk, the Casimir invariant J², the abstract eigenvalue spectrum, finite-dimensional matrix representations, orbital angular momentum and spherical harmonics, Pauli spin matrices and SU(2) spinor transformations, the addition of two angular momenta, Clebsch-Gordan coupling coefficients, recursion relations, irreducible spherical tensor operators, and the Wigner-Eckart theorem.",
    "sections": [
        {
            "id": "sec5-1",
            "title": "General Angular Momentum Algebra: Commutators, Casimir Invariant & Ladder Operators",
            "content": r"""
<h3>1. The Quantum Lie Algebra of Rotations</h3>
<p>
In quantum mechanics, angular momentum operators are defined as the infinitesimal Hermitian generators of spatial rotations. An infinitesimal rotation by angle $d\phi$ about unit vector $\hat{n}$ acts on state kets via the unitary operator:
</p>
$$\hat{R}_{\hat{n}}(d\phi) = \hat{I} - \frac{i}{\hbar}(\hat{\vec{J}}\cdot\hat{n})\,d\phi$$
<p>
The non-Abelian geometry of physical three-dimensional rotations requires that the components of the general angular momentum vector operator $\hat{\vec{J}} = (\hat{J}_x, \hat{J}_y, \hat{J}_z)$ satisfy the fundamental commutation relations:
</p>
$$[\hat{J}_i, \hat{J}_j] = i\hbar \sum_{k=1}^3 \epsilon_{ijk} \hat{J}_k \iff [\hat{J}_x, \hat{J}_y] = i\hbar \hat{J}_z, \quad [\hat{J}_y, \hat{J}_z] = i\hbar \hat{J}_x, \quad [\hat{J}_z, \hat{J}_x] = i\hbar \hat{J}_y$$
<p>
These commutation relations define the Lie algebra $\mathfrak{su}(2) \cong \mathfrak{so}(3)$.
</p>

<h3>2. The Casimir Invariant Operator $\hat{\vec{J}}^2$</h3>
<p>
The total angular momentum squared is defined as:
</p>
$$\hat{\vec{J}}^2 \equiv \hat{J}_x^2 + \hat{J}_y^2 + \hat{J}_z^2$$
<p>
Evaluating the commutator with any Cartesian component $\hat{J}_k$:
</p>
$$[\hat{\vec{J}}^2, \hat{J}_z] = [\hat{J}_x^2, \hat{J}_z] + [\hat{J}_y^2, \hat{J}_z] + [\hat{J}_z^2, \hat{J}_z]$$
$$= \hat{J}_x[\hat{J}_x, \hat{J}_z] + [\hat{J}_x, \hat{J}_z]\hat{J}_x + \hat{J}_y[\hat{J}_y, \hat{J}_z] + [\hat{J}_y, \hat{J}_z]\hat{J}_y + 0$$
$$= -i\hbar(\hat{J}_x\hat{J}_y + \hat{J}_y\hat{J}_x) + i\hbar(\hat{J}_y\hat{J}_x + \hat{J}_x\hat{J}_y) = 0$$
<p>
Hence, $\hat{\vec{J}}^2$ commutes with all three components: $[\hat{\vec{J}}^2, \hat{J}_i] = 0$. By Schur's lemma, $\hat{\vec{J}}^2$ is the quadratic Casimir invariant of the rotation group. A complete set of commuting observables (CSCO) can be chosen as $\{\hat{\vec{J}}^2, \hat{J}_z\}$.
</p>

<h3>3. Raising and Lowering Ladder Operators</h3>
<p>
We define the non-Hermitian ladder operators:
</p>
$$\hat{J}_+ \equiv \hat{J}_x + i\hat{J}_y, \quad \hat{J}_- \equiv \hat{J}_x - i\hat{J}_y = (\hat{J}_+)^\dagger$$
<p>
Their commutation relations with $\hat{J}_z$ and $\hat{\vec{J}}^2$ are:
</p>
$$[\hat{J}_z, \hat{J}_\pm] = [\hat{J}_z, \hat{J}_x] \pm i[\hat{J}_z, \hat{J}_y] = i\hbar\hat{J}_y \pm i(-i\hbar\hat{J}_x) = \pm\hbar(\hat{J}_x \pm i\hat{J}_y) = \pm\hbar \hat{J}_\pm$$
$$[\hat{\vec{J}}^2, \hat{J}_\pm] = 0$$
<p>
Products of the ladder operators relate directly to $\hat{\vec{J}}^2$:
</p>
$$\hat{J}_\mp \hat{J}_\pm = (\hat{J}_x \mp i\hat{J}_y)(\hat{J}_x \pm i\hat{J}_y) = \hat{J}_x^2 + \hat{J}_y^2 \pm i[\hat{J}_x, \hat{J}_y] = \hat{\vec{J}}^2 - \hat{J}_z^2 \mp \hbar\hat{J}_z$$
$$\hat{\vec{J}}^2 = \hat{J}_- \hat{J}_+ + \hat{J}_z^2 + \hbar\hat{J}_z = \hat{J}_+ \hat{J}_- + \hat{J}_z^2 - \hbar\hat{J}_z$$
"""
        },
        {
            "id": "sec5-2",
            "title": "Eigenvalue Spectrum of J^2 and Jz & Finite-Dimensional Matrix Representations",
            "content": r"""
<h3>1. Algebraic Derivation of the Quantum Numbers $j$ and $m$</h3>
<p>
Let $|j, m\rangle$ denote simultaneous normalized eigenstates of $\hat{\vec{J}}^2$ and $\hat{J}_z$:
</p>
$$\hat{\vec{J}}^2 |j, m\rangle = \lambda \hbar^2 |j, m\rangle, \quad \hat{J}_z |j, m\rangle = m\hbar |j, m\rangle$$
<p>
Applying the commutator $[\hat{J}_z, \hat{J}_\pm] = \pm\hbar\hat{J}_\pm$:
</p>
$$\hat{J}_z(\hat{J}_\pm |j, m\rangle) = (\hat{J}_\pm\hat{J}_z + [\hat{J}_z, \hat{J}_\pm])|j, m\rangle = (m\hbar \pm \hbar)(\hat{J}_\pm |j, m\rangle) = (m \pm 1)\hbar(\hat{J}_\pm |j, m\rangle)$$
<p>
Thus, $\hat{J}_\pm |j, m\rangle$ is an eigenstate of $\hat{J}_z$ with eigenvalue $(m \pm 1)\hbar$. Since $\langle j, m | \hat{\vec{J}}^2 - \hat{J}_z^2 | j, m \rangle = \langle j, m | \hat{J}_x^2 + \hat{J}_y^2 | j, m \rangle \ge 0$:
</p>
$$\lambda \hbar^2 - m^2\hbar^2 \ge 0 \implies m^2 \le \lambda$$
<p>
Therefore, the spectrum of $m$ must be bounded from above by a maximum value $j$, and from below by a minimum value $j'$:
</p>
$$\hat{J}_+ |j, j\rangle = 0 \implies \hat{J}_- \hat{J}_+ |j, j\rangle = (\hat{\vec{J}}^2 - \hat{J}_z^2 - \hbar\hat{J}_z)|j, j\rangle = (\lambda - j^2 - j)\hbar^2 |j, j\rangle = 0 \implies \lambda = j(j+1)$$
$$\hat{J}_- |j, j'\rangle = 0 \implies \hat{J}_+ \hat{J}_- |j, j'\rangle = (\hat{\vec{J}}^2 - \hat{J}_z^2 + \hbar\hat{J}_z)|j, j'\rangle = (\lambda - j'^2 + j')\hbar^2 |j, j'\rangle = 0 \implies \lambda = j'(j'-1)$$
<p>
Equating the two expressions for $\lambda$:
</p>
$$j(j+1) = j'(j'-1) \implies j' = -j$$
<p>
Because one transitions from $-j$ to $+j$ in discrete integer steps of $+1$:
</p>
$$j - (-j) = 2j = k \in \mathbb{N}_0 \implies j \in \left\{0, \frac{1}{2}, 1, \frac{3}{2}, 2, \dots\right\}$$
<p>
For a given $j$, the magnetic quantum number $m$ takes $2j+1$ distinct values:
</p>
$$m \in \{-j, -j+1, \dots, j-1, j\}$$

<h3>2. Matrix Elements of Angular Momentum</h3>
<p>
Evaluating the normalization of $\hat{J}_\pm |j, m\rangle$:
</p>
$$\|\hat{J}_\pm |j, m\rangle\|^2 = \langle j, m | \hat{J}_\mp \hat{J}_\pm | j, m \rangle = \langle j, m | (\hat{\vec{J}}^2 - \hat{J}_z^2 \mp \hbar\hat{J}_z) | j, m \rangle = \hbar^2 [j(j+1) - m(m \pm 1)]$$
<p>
Choosing the standard Condon-Shortley positive phase convention:
</p>
$$\hat{J}_\pm |j, m\rangle = \hbar\sqrt{j(j+1) - m(m \pm 1)} \, |j, m \pm 1\rangle$$
<p>
The Cartesian matrix elements are:
</p>
$$\langle j, m' | \hat{J}_x | j, m \rangle = \frac{\hbar}{2}\left[\sqrt{j(j+1)-m(m+1)}\delta_{m', m+1} + \sqrt{j(j+1)-m(m-1)}\delta_{m', m-1}\right]$$
$$\langle j, m' | \hat{J}_y | j, m \rangle = \frac{\hbar}{2i}\left[\sqrt{j(j+1)-m(m+1)}\delta_{m', m+1} - \sqrt{j(j+1)-m(m-1)}\delta_{m', m-1}\right]$$
$$\langle j, m' | \hat{J}_z | j, m \rangle = m\hbar \delta_{m', m}$$
"""
        },
        {
            "id": "sec5-3",
            "title": "Orbital Angular Momentum in Spherical Coordinates & Spherical Harmonics",
            "content": r"""
<h3>1. Differential Operators in Spherical Polar Coordinates</h3>
<p>
Orbital angular momentum is defined classically as $\vec{L} = \vec{r} \times \vec{p}$. In coordinate space, substituting $\hat{\vec{p}} = -i\hbar\nabla$:
</p>
$$\hat{\vec{L}} = -i\hbar(\vec{r} \times \nabla)$$
<p>
In spherical polar coordinates $(r, \theta, \phi)$, the Cartesian components become:
</p>
$$\hat{L}_x = i\hbar\left(\sin\phi\frac{\partial}{\partial\theta} + \cot\theta\cos\phi\frac{\partial}{\partial\phi}\right)$$
$$\hat{L}_y = i\hbar\left(-\cos\phi\frac{\partial}{\partial\theta} + \cot\theta\sin\phi\frac{\partial}{\partial\phi}\right)$$
$$\hat{L}_z = -i\hbar\frac{\partial}{\partial\phi}$$
<p>
The Casimir invariant $\hat{\vec{L}}^2$ takes the differential form:
</p>
$$\hat{\vec{L}}^2 = -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right]$$

<h3>2. The Spherical Harmonics $Y_{lm}(\theta, \phi)$</h3>
<p>
The simultaneous eigenfunctions of $\hat{\vec{L}}^2$ and $\hat{L}_z$ are the <strong>spherical harmonics</strong>:
</p>
$$\hat{\vec{L}}^2 Y_{lm}(\theta, \phi) = l(l+1)\hbar^2 Y_{lm}(\theta, \phi), \quad \hat{L}_z Y_{lm}(\theta, \phi) = m\hbar Y_{lm}(\theta, \phi)$$
<p>
Separating variables, $Y_{lm}(\theta, \phi) = \Theta_{lm}(\theta)\Phi_m(\phi)$:
</p>
$$\hat{L}_z \Phi_m(\phi) = -i\hbar\frac{d\Phi_m}{d\phi} = m\hbar\Phi_m(\phi) \implies \Phi_m(\phi) = \frac{1}{\sqrt{2\pi}}e^{im\phi}$$
<p>
The single-valuedness requirement $\Phi_m(\phi + 2\pi) = \Phi_m(\phi)$ restricts $m$ strictly to <em>integers</em> ($m \in \mathbb{Z}$). Consequently, orbital angular momentum quantum numbers must be strictly integer-valued:
</p>
$$l \in \{0, 1, 2, 3, \dots\}, \quad m \in \{-l, -l+1, \dots, +l\}$$
<p>
The $\theta$-dependent factor solves the associated Legendre differential equation:
</p>
$$Y_{lm}(\theta, \phi) = (-1)^m \sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}} P_l^m(\cos\theta) e^{im\phi}$$
<p>
Orthonormality over the unit sphere is:
</p>
$$\int_0^{2\pi} d\phi \int_0^\pi \sin\theta\,d\theta \, Y_{l'm'}^*(\theta, \phi) Y_{lm}(\theta, \phi) = \delta_{l'l}\delta_{m'm}$$
"""
        },
        {
            "id": "sec5-4",
            "title": "Spin Angular Momentum: Spin-1/2 Algebra, Pauli Matrices & Spinor Transformations",
            "content": r"""
<h3>1. The Spin-1/2 Degree of Freedom</h3>
<p>
Unlike orbital angular momentum, which describes spatial motion and is restricted to integer eigenvalues, elementary particles possess an intrinsic angular momentum termed <strong>spin</strong> $\hat{\vec{S}}$ with half-integer quantum numbers. For electrons, protons, and neutrons, $s = 1/2$.
</p>
<p>
In the two-dimensional Hilbert space spanned by the basis states $\{|+\rangle, |-\rangle\} \equiv \{|\uparrow\rangle, |\downarrow\rangle\}$, the spin operator is represented in terms of the dimensionless <strong>Pauli spin matrices</strong> $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$:
</p>
$$\hat{\vec{S}} = \frac{\hbar}{2}\vec{\sigma}$$
$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

<h3>2. Algebraic Properties of Pauli Matrices</h3>
<p>
The Pauli matrices satisfy the fundamental product identity:
</p>
$$\sigma_i \sigma_j = \delta_{ij}\hat{I} + i\sum_k \epsilon_{ijk} \sigma_k$$
<p>
From this identity directly follow their anticommutation and commutation relations:
</p>
$$\{\sigma_i, \sigma_j\} = \sigma_i \sigma_j + \sigma_j \sigma_i = 2\delta_{ij}\hat{I}$$
$$[\sigma_i, \sigma_j] = \sigma_i \sigma_j - \sigma_j \sigma_i = 2i\sum_k \epsilon_{ijk} \sigma_k$$
<p>
Additionally: $\sigma_i^2 = \hat{I}$, $\text{Tr}(\sigma_i) = 0$, and $\det(\sigma_i) = -1$.
</p>

<h3>3. Finite Rotations and the 4π Spinor Symmetry</h3>
<p>
A finite rotation of a spin-1/2 state by angle $\theta$ about unit axis $\hat{n}$ is represented by the $2\times 2$ unitary matrix $\hat{U}(\hat{n}, \theta) = \exp\left(-\frac{i}{\hbar}\hat{\vec{S}}\cdot\hat{n}\theta\right) = \exp\left(-\frac{i\theta}{2}(\vec{\sigma}\cdot\hat{n})\right)$. Expanding the matrix exponential:
</p>
$$\exp\left(-\frac{i\theta}{2}(\vec{\sigma}\cdot\hat{n})\right) = \sum_{k=0}^\infty \frac{1}{k!}\left(-\frac{i\theta}{2}\right)^k (\vec{\sigma}\cdot\hat{n})^k$$
<p>
Since $(\vec{\sigma}\cdot\hat{n})^2 = \hat{I}$, even powers yield $\cos(\theta/2)$ and odd powers yield $-i(\vec{\sigma}\cdot\hat{n})\sin(\theta/2)$:
</p>
$$\hat{U}(\hat{n}, \theta) = \cos\left(\frac{\theta}{2}\right)\hat{I} - i(\vec{\sigma}\cdot\hat{n})\sin\left(\frac{\theta}{2}\right)$$
<p>
For a complete $2\pi$ spatial rotation ($\theta = 2\pi$):
</p>
$$\hat{U}(\hat{n}, 2\pi) = \cos(\pi)\hat{I} - i(\vec{\sigma}\cdot\hat{n})\sin(\pi) = -\hat{I}$$
<p>
A rotation by $360^\circ$ inverts the sign of a fermion spinor ket: $|\psi\rangle \to -|\psi\rangle$. A full $4\pi$ ($720^\circ$) rotation is required to return the state vector to its original mathematical identity, demonstrating the double-covering topology $\text{SU}(2) \to \text{SO}(3)$ verified by neutron interferometry.
</p>
"""
        },
        {
            "id": "sec5-5",
            "title": "Addition of Two Angular Momenta: Uncoupled vs Coupled Representation Bases",
            "content": r"""
<h3>1. The Composite Two-Particle Hilbert Space</h3>
<p>
Consider a composite quantum system consisting of two independent angular momenta $\hat{\vec{J}}_1$ and $\hat{\vec{J}}_2$ acting in Hilbert spaces $\mathcal{H}_1$ and $\mathcal{H}_2$ of dimensions $(2j_1+1)$ and $(2j_2+1)$. Because they act on distinct degrees of freedom, their operators commute:
</p>
$$[\hat{J}_{1i}, \hat{J}_{2j}] = 0 \quad \forall i, j$$
<p>
The total angular momentum operator is the vector sum:
</p>
$$\hat{\vec{J}} = \hat{\vec{J}}_1 + \hat{\vec{J}}_2 \equiv \hat{\vec{J}}_1 \otimes \hat{I}_2 + \hat{I}_1 \otimes \hat{\vec{J}}_2$$
<p>
The total operator $\hat{\vec{J}}$ satisfies the standard rotation Lie algebra $[\hat{J}_i, \hat{J}_j] = i\hbar \epsilon_{ijk} \hat{J}_k$.
</p>

<h3>2. The Uncoupled Basis</h3>
<p>
The <strong>uncoupled basis</strong> diagonalizes the four mutually commuting operators $\{\hat{\vec{J}}_1^2, \hat{J}_{1z}, \hat{\vec{J}}_2^2, \hat{J}_{2z}\}$:
</p>
$$|j_1, m_1; j_2, m_2\rangle \equiv |j_1, m_1\rangle \otimes |j_2, m_2\rangle$$
<p>
The dimension of the product space is:
</p>
$$N = (2j_1 + 1)(2j_2 + 1)$$

<h3>3. The Coupled Basis and Triangle Inequality</h3>
<p>
Alternatively, the <strong>coupled basis</strong> diagonalizes the complete set of commuting observables $\{\hat{\vec{J}}_1^2, \hat{\vec{J}}_2^2, \hat{\vec{J}}^2, \hat{J}_z\}$, denoted by $|J, M; j_1, j_2\rangle$ (or simply $|J, M\rangle$ when $j_1, j_2$ are fixed):
</p>
$$\hat{\vec{J}}^2 |J, M\rangle = J(J+1)\hbar^2 |J, M\rangle, \quad \hat{J}_z |J, M\rangle = M\hbar |J, M\rangle$$
<p>
Since $\hat{J}_z = \hat{J}_{1z} + \hat{J}_{2z}$, the magnetic quantum number is strictly additive:
</p>
$$M = m_1 + m_2$$
<p>
The allowed values of total angular momentum $J$ satisfy the <strong>triangle rule</strong>:
</p>
$$|j_1 - j_2| \le J \le j_1 + j_2$$
<p>
with $J$ stepping by integers from $|j_1 - j_2|$ to $j_1 + j_2$. We verify conservation of total dimensionality:
</p>
$$\sum_{J=|j_1-j_2|}^{j_1+j_2} (2J + 1) = (2j_1 + 1)(2j_2 + 1)$$
"""
        },
        {
            "id": "sec5-6",
            "title": "Clebsch-Gordan Coefficients: Phase Conventions, Ladder Construction & Tabulation",
            "content": r"""
<h3>1. Definition of Clebsch-Gordan Coefficients</h3>
<p>
The unitary transformation connecting the uncoupled and coupled bases is mediated by the <strong>Clebsch-Gordan (CG) coefficients</strong>:
</p>
$$|J, M\rangle = \sum_{m_1=-j_1}^{j_1} \sum_{m_2=-j_2}^{j_2} \langle j_1, m_1; j_2, m_2 | J, M \rangle |j_1, m_1; j_2, m_2\rangle$$
<p>
The CG coefficients $\langle j_1, m_1; j_2, m_2 | J, M \rangle$ are the projection overlaps between the two bases. They satisfy two fundamental selection rules:
</p>
<ol>
  <li>$M = m_1 + m_2$ (otherwise the coefficient is identically zero).</li>
  <li>$|j_1 - j_2| \le J \le j_1 + j_2$ (triangle inequality).</li>
</ol>

<h3>2. Orthonormality and Phase Conventions</h3>
<p>
Because the change of basis is a unitary transformation, the CG coefficients satisfy dual completeness relations:
</p>
$$\sum_{m_1, m_2} \langle J, M | j_1, m_1; j_2, m_2 \rangle \langle j_1, m_1; j_2, m_2 | J', M' \rangle = \delta_{JJ'}\delta_{MM'}$$
$$\sum_{J, M} \langle j_1, m_1; j_2, m_2 | J, M \rangle \langle J, M | j_1, m_1'; j_2, m_2' \rangle = \delta_{m_1 m_1'}\delta_{m_2 m_2'}$$
<p>
Under the standard <strong>Condon-Shortley phase convention</strong>:
</p>
<ol>
  <li>All Clebsch-Gordan coefficients are chosen to be strictly <em>real</em>.</li>
  <li>The highest state $\langle j_1, j_1; j_2, J - j_1 | J, J \rangle > 0$ is chosen to be strictly positive.</li>
</ol>

<h3>3. Construction via Lowering Ladder Operators</h3>
<p>
The construction begins by identifying the unique state of maximum total angular momentum:
</p>
$$|J_{\max}, M_{\max}\rangle = |j_1 + j_2, j_1 + j_2\rangle = |j_1, j_1; j_2, j_2\rangle$$
<p>
Applying the lowering operator $\hat{J}_- = \hat{J}_{1-} + \hat{J}_{2-}$ to both sides generates $|j_1+j_2, j_1+j_2-1\rangle$:
</p>
$$\hbar\sqrt{(j_1+j_2)(j_1+j_2+1) - (j_1+j_2)(j_1+j_2-1)}|j_1+j_2, j_1+j_2-1\rangle = (\hat{J}_{1-} + \hat{J}_{2-})|j_1, j_1; j_2, j_2\rangle$$
$$\sqrt{2(j_1+j_2)}|j_1+j_2, j_1+j_2-1\rangle = \sqrt{2j_1}|j_1-1, j_1; j_2, j_2\rangle + \sqrt{2j_2}|j_1, j_1; j_2-1, j_2\rangle$$
<p>
The orthogonal state with the same $M = j_1 + j_2 - 1$ corresponds to the state $|j_1+j_2-1, j_1+j_2-1\rangle$. Lowering operators are then iteratively applied to generate all lower $M$ states.
</p>
"""
        },
        {
            "id": "sec5-7",
            "title": "Irreducible Spherical Tensors & The Wigner-Eckart Theorem: Matrix Selection Rules",
            "content": r"""
<h3>1. Spherical Tensor Operators</h3>
<p>
An <strong>irreducible spherical tensor operator</strong> of rank $k$, denoted by $\hat{T}_q^{(k)}$ (with $q = -k, -k+1, \dots, +k$), is defined by its commutation relations with the angular momentum operators:
</p>
$$[\hat{J}_z, \hat{T}_q^{(k)}] = q\hbar \hat{T}_q^{(k)}$$
$$[\hat{J}_\pm, \hat{T}_q^{(k)}] = \hbar\sqrt{k(k+1) - q(q \pm 1)} \, \hat{T}_{q \pm 1}^{(k)}$$
<p>
Under spatial rotations, the $2k+1$ components of $\hat{T}_q^{(k)}$ transform among themselves identically to the angular momentum eigenstates $|k, q\rangle$.
</p>
<p>
Examples:
</p>
<ul>
  <li><strong>Rank 0 (Scalar Operator $\hat{S}$):</strong> $[\hat{\vec{J}}, \hat{S}] = 0$ (e.g., $\hat{\vec{r}}^2, \hat{\vec{p}}^2, \hat{H}$).</li>
  <li><strong>Rank 1 (Vector Operator $\hat{\vec{V}}$):</strong> Related to Cartesian components by $\hat{T}_0^{(1)} = \hat{V}_z, \hat{T}_{\pm 1}^{(1)} = \mp \frac{\hat{V}_x \pm i\hat{V}_y}{\sqrt{2}}$.</li>
  <li><strong>Rank 2 (Quadrupole Tensor):</strong> Electric quadrupole moments $Q_{ij} = 3x_i x_j - r^2 \delta_{ij}$.</li>
</ul>

<h3>2. The Wigner-Eckart Theorem</h3>
<p>
The <strong>Wigner-Eckart Theorem</strong> states that the matrix element of an irreducible spherical tensor operator between angular momentum eigenstates factors into two independent terms:
</p>
$$\langle j', m' | \hat{T}_q^{(k)} | j, m \rangle = \frac{\langle j, m; k, q | j', m' \rangle}{\sqrt{2j' + 1}} \langle j' \| \hat{T}^{(k)} \| j \rangle$$
<p>
where:
</p>
<ol>
  <li>$\langle j, m; k, q | j', m' \rangle$ is a standard Clebsch-Gordan coefficient carrying all dependence on the magnetic projection quantum numbers $m, m', q$ (geometric orientation).</li>
  <li>$\langle j' \| \hat{T}^{(k)} \| j \rangle$ is the <strong>reduced matrix element</strong>, which depends solely on the physical dynamics and radial integrals, completely independent of $m, m', q$.</li>
</ol>

<h3>3. Selection Rules from the Wigner-Eckart Theorem</h3>
<p>
Because the CG coefficient vanishes unless the coupling conditions are met:
</p>
<ol>
  <li>$m' = m + q \iff \Delta m = q$.</li>
  <li>$|j - k| \le j' \le j + k$ (triangle rule between initial angular momentum $j$, tensor rank $k$, and final angular momentum $j'$).</li>
</ol>
<p>
For a scalar operator ($k = 0, q = 0$): $\langle j', m' | \hat{S} | j, m \rangle \propto \delta_{j'j}\delta_{m'm}$.
</p>
"""
        }
    ],
    "simulations": [
        {
            "id": "qm2-clebsch-gordan-sim",
            "title": "Interactive Clebsch-Gordan Coefficient Calculator & Coupling Tree",
            "description": "Interactive visualizer for angular momentum coupling j₁ ⊗ j₂ → J, computing exact analytical Clebsch-Gordan coefficients and displaying the orthonormal transformation matrix."
        },
        {
            "id": "qm2-spherical-harmonics-3d-sim",
            "title": "3D Spherical Harmonics Orbital Lobe & Nodal Visualizer",
            "description": "3D interactive visualization of real and complex spherical harmonics |Y_lm(θ, φ)|² showing electron orbital geometries, nodal cones, and azimuthal phase windings."
        }
    ],
    "solvedProblems": [
        {
            "number": 1,
            "title": "Addition of Two Spin-1/2 Particles: Singlet vs Triplet States",
            "statement": r"Consider a system of two spin-1/2 particles ($s_1 = 1/2, s_2 = 1/2$).\n(a) Using lowering operators, construct all four coupled states $|S, M_S\rangle$ in terms of the uncoupled basis $\{|\uparrow\uparrow\rangle, |\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle, |\downarrow\downarrow\rangle\}$.\n(b) Identify the total spin $S = 1$ (triplet) and $S = 0$ (singlet) states and discuss their exchange symmetry under particle permutation $\hat{P}_{12}$.\n(c) Evaluate the expectation value of the spin exchange operator $\hat{\vec{S}}_1 \cdot \hat{\vec{S}}_2$ in both the singlet and triplet states.",
            "solution": r"**(a) Constructing Coupled States:**\nThe uncoupled states are $|\uparrow\uparrow\rangle, |\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle, |\downarrow\downarrow\rangle$.\nThe allowed total spin values are $S \in \{1/2 - 1/2, 1/2 + 1/2\} = \{0, 1\}$.\n1. State of maximum total spin ($S = 1, M_S = 1$):\n   $$|1, 1\rangle = |\uparrow\uparrow\rangle$$\n2. Applying total lowering operator $\hat{S}_- = \hat{S}_{1-} + \hat{S}_{2-}$:\n   $$\hat{S}_-|1, 1\rangle = \hbar\sqrt{1(2) - 1(0)}|1, 0\rangle = \sqrt{2}\hbar|1, 0\rangle$$\n   $$(\hat{S}_{1-} + \hat{S}_{2-})|\uparrow\uparrow\rangle = \hbar|\downarrow\uparrow\rangle + \hbar|\uparrow\downarrow\rangle$$\n   $$\sqrt{2}\hbar|1, 0\rangle = \hbar(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle) \implies |1, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)$$\n3. Lowering once more:\n   $$\hat{S}_-|1, 0\rangle = \sqrt{2}\hbar|1, -1\rangle = \frac{1}{\sqrt{2}}(\hbar|\downarrow\downarrow\rangle + \hbar|\downarrow\downarrow\rangle) = \sqrt{2}\hbar|\downarrow\downarrow\rangle \implies |1, -1\rangle = |\downarrow\downarrow\rangle$$\n4. The singlet state $|0, 0\rangle$ must have $M_S = 0$ and be orthogonal to $|1, 0\rangle$:\n   $$|0, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$$\n\n**(b) Exchange Symmetry:**\nUnder particle interchange operator $\hat{P}_{12}$ ($1 \leftrightarrow 2$):\n- Triplet states ($S = 1$):\n  $$\hat{P}_{12}|1, 1\rangle = |\uparrow\uparrow\rangle = +|1, 1\rangle$$\n  $$\hat{P}_{12}|1, 0\rangle = \frac{1}{\sqrt{2}}(|\downarrow\uparrow\rangle + |\uparrow\downarrow\rangle) = +|1, 0\rangle$$\n  $$\hat{P}_{12}|1, -1\rangle = |\downarrow\downarrow\rangle = +|1, -1\rangle$$\n  All $S = 1$ triplet states are **symmetric** under permutation.\n- Singlet state ($S = 0$):\n  $$\hat{P}_{12}|0, 0\rangle = \frac{1}{\sqrt{2}}(|\downarrow\uparrow\rangle - |\uparrow\downarrow\rangle) = -|0, 0\rangle$$\n  The $S = 0$ singlet state is **antisymmetric** under permutation.\n\n**(c) Spin Dot Product Expectation Values:**\n$$\hat{\vec{S}}^2 = (\hat{\vec{S}}_1 + \hat{\vec{S}}_2)^2 = \hat{\vec{S}}_1^2 + \hat{\vec{S}}_2^2 + 2\hat{\vec{S}}_1\cdot\hat{\vec{S}}_2$$\n$$\hat{\vec{S}}_1\cdot\hat{\vec{S}}_2 = \frac{1}{2}\left(\hat{\vec{S}}^2 - \hat{\vec{S}}_1^2 - \hat{\vec{S}}_2^2\right)$$\nFor spin-1/2: $\hat{\vec{S}}_1^2 = \hat{\vec{S}}_2^2 = \frac{3}{4}\hbar^2$:\n$$\hat{\vec{S}}_1\cdot\hat{\vec{S}}_2 = \frac{1}{2}\left(S(S+1)\hbar^2 - \frac{3}{2}\hbar^2\right)$$\n- For Triplet ($S = 1$):\n  $$\langle \hat{\vec{S}}_1\cdot\hat{\vec{S}}_2 \rangle_{\text{triplet}} = \frac{1}{2}\left(2\hbar^2 - \frac{3}{2}\hbar^2\right) = +\frac{1}{4}\hbar^2$$\n- For Singlet ($S = 0$):\n  $$\langle \hat{\vec{S}}_1\cdot\hat{\vec{S}}_2 \rangle_{\text{singlet}} = \frac{1}{2}\left(0 - \frac{3}{2}\hbar^2\right) = -\frac{3}{4}\hbar^2$$"
        },
        {
            "number": 2,
            "title": "Clebsch-Gordan Coupling for Orbital Angular Momentum l = 1 and Spin s = 1/2",
            "statement": r"A particle with orbital angular momentum $l = 1$ and spin $s = 1/2$ has total angular momentum $\vec{J} = \vec{L} + \vec{S}$.\n(a) What are the possible values of the total angular momentum quantum number $j$?\n(b) Express the coupled state $|j = 3/2, m_j = 1/2\rangle$ and state $|j = 1/2, m_j = 1/2\rangle$ in terms of the uncoupled basis $|m_l, m_s\rangle$.\n(c) Deduce the Clebsch-Gordan coefficients $\langle 1, 0; 1/2, 1/2 | 3/2, 1/2 \rangle$ and $\langle 1, 1; 1/2, -1/2 | 3/2, 1/2 \rangle$.",
            "solution": r"**(a) Allowed Values of $j$:**\n$$|l - s| \le j \le l + s \implies |1 - 1/2| \le j \le 1 + 1/2 \implies j \in \{1/2, 3/2\}$$\nTotal number of states: $(2(3/2)+1) + (2(1/2)+1) = 4 + 2 = 6 = (2l+1)(2s+1)$.\n\n**(b) Constructing the Coupled States:**\n1. State of maximum angular momentum ($j = 3/2, m_j = 3/2$):\n   $$|3/2, 3/2\rangle = |m_l = 1, m_s = 1/2\rangle$$\n2. Applying $\hat{J}_- = \hat{L}_- + \hat{S}_-$:\n   $$\hat{J}_-|3/2, 3/2\rangle = \hbar\sqrt{(3/2)(5/2) - (3/2)(1/2)}|3/2, 1/2\rangle = \sqrt{3}\hbar|3/2, 1/2\rangle$$\n   $$\hat{L}_-|1, 1/2\rangle = \hbar\sqrt{1(2) - 1(0)}|0, 1/2\rangle = \sqrt{2}\hbar|0, 1/2\rangle$$\n   $$\hat{S}_-|1, 1/2\rangle = \hbar\sqrt{(1/2)(3/2) - (1/2)(-1/2)}|1, -1/2\rangle = \hbar|1, -1/2\rangle$$\n   $$\sqrt{3}\hbar|3/2, 1/2\rangle = \sqrt{2}\hbar|0, 1/2\rangle + \hbar|1, -1/2\rangle$$\n   Dividing by $\sqrt{3}\hbar$:\n   $$|3/2, 1/2\rangle = \sqrt{\frac{2}{3}}|0, 1/2\rangle + \frac{1}{\sqrt{3}}|1, -1/2\rangle$$\n3. The state $|1/2, 1/2\rangle$ has the same $m_j = 1/2$ but must be orthogonal to $|3/2, 1/2\rangle$ with positive phase for the highest $m_l$ term:\n   $$|1/2, 1/2\rangle = \frac{1}{\sqrt{3}}|0, 1/2\rangle - \sqrt{\frac{2}{3}}|1, -1/2\rangle$$\n\n**(c) Clebsch-Gordan Coefficients:**\nFrom the expansion of $|3/2, 1/2\rangle$:\n$$\langle 1, 0; 1/2, 1/2 | 3/2, 1/2 \rangle = \sqrt{\frac{2}{3}}$$\n$$\langle 1, 1; 1/2, -1/2 | 3/2, 1/2 \rangle = \frac{1}{\sqrt{3}}$$\nNotice the sum of squared coefficients: $(\sqrt{2/3})^2 + (1/\sqrt{3})^2 = 2/3 + 1/3 = 1$."
        },
        {
            "number": 3,
            "title": "Application of the Wigner-Eckart Theorem to Electric Dipole Matrix Elements",
            "statement": r"A spherical tensor dipole operator $\hat{T}_q^{(1)}$ connects states of an angular momentum multiplet with $j = 1$ to states with $j' = 2$.\n(a) Using the Wigner-Eckart theorem, relate the matrix element $\langle 2, 1 | \hat{T}_1^{(1)} | 1, 0 \rangle$ and $\langle 2, 0 | \hat{T}_0^{(1)} | 1, 0 \rangle$ to the reduced matrix element $\langle 2 \| \hat{T}^{(1)} \| 1 \rangle$.\n(b) Compute the ratio $\frac{\langle 2, 1 | \hat{T}_1^{(1)} | 1, 0 \rangle}{\langle 2, 0 | \hat{T}_0^{(1)} | 1, 0 \rangle}$ using the relevant Clebsch-Gordan coefficients.\n(c) Explain why $\langle 2, 2 | \hat{T}_0^{(1)} | 1, 0 \rangle = 0$.",
            "solution": r"**(a) Wigner-Eckart Decomposition:**\nBy the Wigner-Eckart theorem:\n$$\langle j', m' | \hat{T}_q^{(k)} | j, m \rangle = \frac{\langle j, m; k, q | j', m' \rangle}{\sqrt{2j'+1}} \langle j' \| \hat{T}^{(k)} \| j \rangle$$\nFor $j = 1, k = 1, j' = 2$ ($2j'+1 = 5$):\n$$\langle 2, 1 | \hat{T}_1^{(1)} | 1, 0 \rangle = \frac{\langle 1, 0; 1, 1 | 2, 1 \rangle}{\sqrt{5}} \langle 2 \| \hat{T}^{(1)} \| 1 \rangle$$\n$$\langle 2, 0 | \hat{T}_0^{(1)} | 1, 0 \rangle = \frac{\langle 1, 0; 1, 0 | 2, 0 \rangle}{\sqrt{5}} \langle 2 \| \hat{T}^{(1)} \| 1 \rangle$$\n\n**(b) Ratio of Matrix Elements:**\nThe reduced matrix elements cancel completely in the ratio:\n$$\frac{\langle 2, 1 | \hat{T}_1^{(1)} | 1, 0 \rangle}{\langle 2, 0 | \hat{T}_0^{(1)} | 1, 0 \rangle} = \frac{\langle 1, 0; 1, 1 | 2, 1 \rangle}{\langle 1, 0; 1, 0 | 2, 0 \rangle}$$\nUsing standard Clebsch-Gordan values:\n$$\langle 1, 0; 1, 1 | 2, 1 \rangle = \frac{1}{\sqrt{2}}$$\n$$\langle 1, 0; 1, 0 | 2, 0 \rangle = \sqrt{\frac{2}{3}}$$\nTherefore:\n$$\frac{\langle 2, 1 | \hat{T}_1^{(1)} | 1, 0 \rangle}{\langle 2, 0 | \hat{T}_0^{(1)} | 1, 0 \rangle} = \frac{1/\sqrt{2}}{\sqrt{2/3}} = \frac{\sqrt{3}}{2}$$\nThe ratio of physical transition amplitudes is determined entirely by the geometry of angular momentum!\n\n**(c) Vanishing Matrix Element:**\nFor $\langle 2, 2 | \hat{T}_0^{(1)} | 1, 0 \rangle$, the magnetic quantum numbers are $m = 0, q = 0$, giving $m + q = 0 \ne m' = 2$. By the magnetic selection rule ($m' = m + q$), the Clebsch-Gordan coefficient $\langle 1, 0; 1, 0 | 2, 2 \rangle$ is identically zero. Thus, the matrix element vanishes."
        }
    ]
}

# ==============================================================================
# CHAPTER 6: IDENTICAL PARTICLES, PERMUTATION SYMMETRY & MANY-BODY SYSTEMS
# ==============================================================================
u6 = {
    "id": "unit6",
    "number": 6,
    "title": "Identical Particles, Permutation Symmetry & Many-Body Systems",
    "subtitle": "Indistinguishability, Spin-Statistics, Slater Determinants, Exchange Energy, Degenerate Fermi Gas & Landau Levels",
    "description": "Comprehensive quantum theory of identical particles and many-body systems: the permutation operator and quantum indistinguishability, the symmetrization postulate for bosons and fermions, the spin-statistics theorem, Slater determinants, two-electron exchange interaction and helium atom spectroscopy (ortho- vs para-helium), statistical mechanics of the degenerate Fermi gas in 1D, 2D, and 3D with quantum degeneracy pressure, 2D electron gas in uniform magnetic fields and Landau level quantization, and two-nucleon isospin symmetry.",
    "sections": [
        {
            "id": "sec6-1",
            "title": "The Permutation Operator, Indistinguishability & Symmetrization Postulate",
            "content": r"""
<h3>1. Quantum Indistinguishability</h3>
<p>
In classical mechanics, identical particles can always be distinguished by tracking their continuous trajectories through phase space. In quantum mechanics, the Heisenberg uncertainty principle ($\Delta x \Delta p \ge \hbar/2$) and the spatial overlap of wavepackets render identical particles fundamentally <strong>indistinguishable</strong>. No physical measurement can determine which particle is which.
</p>

<h3>2. The Permutation (Exchange) Operator</h3>
<p>
For a system of $N$ identical particles, the permutation operator $\hat{P}_{ij}$ interchanges all coordinates (spatial and spin) of particles $i$ and $j$:
</p>
$$\hat{P}_{ij}\psi(\xi_1, \dots, \xi_i, \dots, \xi_j, \dots, \xi_N) = \psi(\xi_1, \dots, \xi_j, \dots, \xi_i, \dots, \xi_N)$$
<p>
where $\xi_k = (\vec{r}_k, \sigma_k)$ represents the combined spatial and spin coordinates of particle $k$. Applying $\hat{P}_{ij}$ twice returns the original configuration:
</p>
$$\hat{P}_{ij}^2 = \hat{I} \implies \text{eigenvalues of } \hat{P}_{ij} \text{ are } \pm 1$$
<p>
Because the particles are physically identical, the Hamiltonian is completely invariant under particle interchange:
</p>
$$[\hat{P}_{ij}, \hat{H}] = 0 \quad \forall i, j$$

<h3>3. The Symmetrization Postulate & Spin-Statistics Theorem</h3>
<p>
The <strong>Symmetrization Postulate</strong> states that all physical quantum states must be either completely symmetric or completely antisymmetric under the interchange of any pair of identical particles:
</p>
<ol>
  <li><strong>Bosons (Integer Spin: $s = 0, 1, 2, \dots$):</strong>
    The state vector is strictly <em>symmetric</em> under interchange:
    $$\hat{P}_{ij}|\psi\rangle = +|\psi\rangle$$
    Bosons obey Bose-Einstein statistics and can condense into the identical single-particle state (Bose-Einstein Condensation). Examples: photons ($s=1$), gluons ($s=1$), $^{4}\text{He}$ atoms ($s=0$).
  </li>
  <li><strong>Fermions (Half-Integer Spin: $s = 1/2, 3/2, \dots$):</strong>
    The state vector is strictly <em>antisymmetric</em> under interchange:
    $$\hat{P}_{ij}|\psi\rangle = -|\psi\rangle$$
    Fermions obey Fermi-Dirac statistics and the Pauli Exclusion Principle. Examples: electrons ($s=1/2$), protons ($s=1/2$), neutrons ($s=1/2$).
  </li>
</ol>
<p>
The deep connection between spin and permutation symmetry is proven rigorously in relativistic quantum field theory via the <strong>Spin-Statistics Theorem</strong> (Pauli, 1940), stemming from causality, Lorentz invariance, and positive energy stability.
</p>
"""
        },
        {
            "id": "sec6-2",
            "title": "The Pauli Exclusion Principle & Slater Determinants for Many-Fermion States",
            "content": r"""
<h3>1. The Pauli Exclusion Principle</h3>
<p>
Consider a system of $N$ non-interacting fermions. If two fermions were to occupy the identical single-particle quantum state $\phi_\alpha$, interchanging them would yield:
</p>
$$\psi(\xi_1, \xi_2) = -\psi(\xi_2, \xi_1)$$
<p>
If $\xi_1 = \xi_2$, then $\psi(\xi_1, \xi_1) = -\psi(\xi_1, \xi_1) \implies \psi = 0$. Two identical fermions cannot occupy the exact same quantum state simultaneously—this is the <strong>Pauli Exclusion Principle</strong>.
</p>

<h3>2. The Slater Determinant</h3>
<p>
To construct a totally antisymmetric $N$-particle state from a set of single-particle orthonormal orbitals $\{\phi_{\alpha_1}, \phi_{\alpha_2}, \dots, \phi_{\alpha_N}\}$, John Slater introduced the <strong>Slater determinant</strong>:
</p>
$$\Psi(\xi_1, \xi_2, \dots, \xi_N) = \frac{1}{\sqrt{N!}} \begin{vmatrix} \phi_{\alpha_1}(\xi_1) & \phi_{\alpha_2}(\xi_1) & \cdots & \phi_{\alpha_N}(\xi_1) \\ \phi_{\alpha_1}(\xi_2) & \phi_{\alpha_2}(\xi_2) & \cdots & \phi_{\alpha_N}(\xi_2) \\ \vdots & \vdots & \ddots & \vdots \\ \phi_{\alpha_1}(\xi_N) & \phi_{\alpha_2}(\xi_N) & \cdots & \phi_{\alpha_N}(\xi_N) \end{vmatrix}$$
<p>
Mathematical properties:
</p>
<ol>
  <li><strong>Antisymmetry:</strong> Interchanging two particles corresponds to swapping two rows of the determinant, multiplying the determinant by $-1$.</li>
  <li><strong>Pauli Exclusion:</strong> If two orbitals are identical ($\alpha_i = \alpha_j$), two columns are identical, causing the determinant to vanish identically.</li>
  <li><strong>Normalization:</strong> The factor $1/\sqrt{N!}$ ensures $\langle \Psi | \Psi \rangle = 1$ when single-particle orbitals are orthonormal.</li>
</ol>
"""
        },
        {
            "id": "sec6-3",
            "title": "Two-Electron Systems: Space-Spin Functions & The Exchange Interaction (Helium)",
            "content": r"""
<h3>1. Total Wavefunction Factorization</h3>
<p>
For a system of two electrons (spin-1/2), the total wavefunction factors into a spatial part $\psi(\vec{r}_1, \vec{r}_2)$ and a spin part $\chi(\sigma_1, \sigma_2)$:
</p>
$$\Psi(1, 2) = \psi(\vec{r}_1, \vec{r}_2)\chi(\sigma_1, \sigma_2)$$
<p>
The total state must be antisymmetric under overall permutation $\hat{P}_{12} = \hat{P}_{\text{space}}\hat{P}_{\text{spin}} = -1$. As proven in Chapter 5:
</p>
<ul>
  <li><strong>Spin Triplet ($S = 1$, $\chi_S$ symmetric):</strong> Requires an <em>antisymmetric</em> spatial wavefunction $\psi_A(\vec{r}_1, \vec{r}_2) = -\psi_A(\vec{r}_2, \vec{r}_1)$. This is termed <strong>Ortho-Helium</strong>.</li>
  <li><strong>Spin Singlet ($S = 0$, $\chi_A$ antisymmetric):</strong> Requires a <em>symmetric</em> spatial wavefunction $\psi_S(\vec{r}_1, \vec{r}_2) = +\psi_S(\vec{r}_2, \vec{r}_1)$. This is termed <strong>Para-Helium</strong>.</li>
</ul>

<h3>2. The Direct and Exchange Integrals</h3>
<p>
Let the two electrons occupy single-particle spatial orbitals $\phi_a(\vec{r})$ and $\phi_b(\vec{r})$ ($a \ne b$). The normalized symmetric and antisymmetric spatial wavefunctions are:
</p>
$$\psi_{S/A}(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}}\left[ \phi_a(\vec{r}_1)\phi_b(\vec{r}_2) \pm \phi_b(\vec{r}_1)\phi_a(\vec{r}_2) \right]$$
<p>
Evaluating the expectation value of the Coulomb repulsion potential $V_{12} = \frac{e^2}{4\pi\varepsilon_0 |\vec{r}_1 - \vec{r}_2|}$:
</p>
$$\langle V_{12} \rangle_{S/A} = J \pm K$$
<p>
where:
</p>
<ol>
  <li>$J \equiv \int |\phi_a(\vec{r}_1)|^2 \frac{e^2}{4\pi\varepsilon_0 r_{12}} |\phi_b(\vec{r}_2)|^2 \, d^3r_1 d^3r_2 > 0$ is the classical <strong>direct Coulomb integral</strong> (repulsion between charge clouds).</li>
  <li>$K \equiv \int \phi_a^*(\vec{r}_1)\phi_b^*(\vec{r}_2) \frac{e^2}{4\pi\varepsilon_0 r_{12}} \phi_b(\vec{r}_1)\phi_a(\vec{r}_2) \, d^3r_1 d^3r_2 > 0$ is the purely quantum mechanical <strong>exchange integral</strong>.</li>
</ol>

<h3>3. Physical Consequences: Exchange Energy and Hund's Rule</h3>
<p>
The energy difference between singlet and triplet states is:
</p>
$$\Delta E = E_{\text{singlet}} - E_{\text{triplet}} = (E_0 + J + K) - (E_0 + J - K) = 2K > 0$$
<p>
The triplet state (ortho-helium) always lies lower in energy than the singlet state (para-helium). Because fermions in an antisymmetric spatial state have zero probability of occupying the same point in space ($\psi_A(\vec{r}, \vec{r}) = 0$), they are surrounded by a "Fermi exchange hole", keeping them further apart on average and dramatically reducing their electrostatic Coulomb repulsion energy. This is the microscopic physical origin of ferromagnetism and <strong>Hund's First Rule</strong>.
</p>
"""
        },
        {
            "id": "sec6-4",
            "title": "The Degenerate Fermi Gas: Density of States, Fermi Energy & Degeneracy Pressure",
            "content": r"""
<h3>1. Statistical Mechanics of Non-Interacting Fermions in 3D</h3>
<p>
Consider a system of $N$ non-interacting spin-1/2 electrons confined in a volume $V = L^3$. Imposing periodic boundary conditions $\psi(x+L, y, z) = \psi(x, y, z)$, the allowed momentum states form a discrete grid in $k$-space:
</p>
$$\vec{k} = \frac{2\pi}{L}(n_x, n_y, n_z) \implies \Delta k^3 = \frac{(2\pi)^3}{V}$$
<p>
At absolute zero ($T = 0$), the electrons fill all available single-particle states from $k = 0$ up to a maximum momentum surface in $k$-space termed the <strong>Fermi sphere</strong> of radius $k_F$.
</p>

<h3>2. Fermi Momentum and Fermi Energy</h3>
<p>
Accounting for the spin degeneracy factor $g_s = 2s+1 = 2$:
</p>
$$N = 2 \frac{V}{(2\pi)^3} \left(\frac{4}{3}\pi k_F^3\right) = \frac{V k_F^3}{3\pi^2}$$
<p>
Solving for the Fermi wavevector $k_F$ in terms of the electron density $n = N/V$:
</p>
$$k_F = (3\pi^2 n)^{1/3}, \quad p_F = \hbar k_F = \hbar(3\pi^2 n)^{1/3}$$
<p>
The <strong>Fermi energy</strong> $E_F$ is the kinetic energy of the highest occupied state at $T = 0$:
</p>
$$E_F = \frac{\hbar^2 k_F^2}{2m} = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$$
<p>
The density of states $g(E) \equiv \frac{dN}{dE}$ evaluates to:
</p>
$$g(E) = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{E}$$

<h3>3. Total Internal Energy and Quantum Degeneracy Pressure</h3>
<p>
The total ground-state kinetic energy $E_{\text{total}}$ is obtained by integrating over the Fermi sphere:
</p>
$$E_{\text{total}} = \int_0^{E_F} E g(E)\,dE = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} \int_0^{E_F} E^{3/2}\,dE = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} \frac{2}{5} E_F^{5/2} = \frac{3}{5} N E_F$$
<p>
Even at absolute zero temperature, quantum fermions possess enormous kinetic energy. The system exerts a macroscopic outward <strong>quantum degeneracy pressure</strong>:
</p>
$$P = -\left(\frac{\partial E_{\text{total}}}{\partial V}\right)_N = -\frac{3}{5}N \frac{\partial E_F}{\partial V} = -\frac{3}{5}N \left(-\frac{2}{3}\frac{E_F}{V}\right) = \frac{2}{5}n E_F = \frac{(3\pi^2)^{2/3}\hbar^2}{5m} n^{5/3}$$
<p>
Degeneracy pressure is purely quantum mechanical in origin (independent of temperature and electrostatic forces), providing the outward mechanical force that stabilizes white dwarf stars against gravitational collapse (up to the Chandrasekhar mass limit).
</p>
"""
        },
        {
            "id": "sec6-5",
            "title": "Charged Particles in a Uniform Magnetic Field: Landau Levels & Orbital Degeneracy",
            "content": r"""
<h3>1. Minimal Coupling and the Landau Gauge</h3>
<p>
Consider an electron of mass $m$ and charge $q = -e$ confined to the $xy$-plane in a uniform perpendicular magnetic field $\vec{B} = B\hat{z}$. Under minimal electromagnetic coupling, the kinetic momentum operator is $\vec{\Pi} = \vec{p} - q\vec{A} = \vec{p} + e\vec{A}$. The Hamiltonian is:
</p>
$$\hat{H} = \frac{1}{2m}(\hat{\vec{p}} + e\vec{A})^2$$
<p>
Choosing the <strong>Landau gauge</strong> $\vec{A} = (0, Bx, 0)$, which yields $\nabla \times \vec{A} = B\hat{z}$:
</p>
$$\hat{H} = \frac{\hat{p}_x^2}{2m} + \frac{(\hat{p}_y + eBx)^2}{2m}$$

<h3>2. Harmonic Mapping and Landau Energy Spectrum</h3>
<p>
Since $\hat{H}$ does not contain $y$, the momentum operator $\hat{p}_y$ commutes with the Hamiltonian: $[\hat{H}, \hat{p}_y] = 0$. We can replace $\hat{p}_y$ by its continuous eigenvalue $\hbar k_y$:
</p>
$$\hat{H} = \frac{\hat{p}_x^2}{2m} + \frac{1}{2}m\omega_c^2 \left(x + \frac{\hbar k_y}{eB}\right)^2$$
<p>
where $\omega_c = \frac{eB}{m}$ is the classical <strong>cyclotron frequency</strong>. This Hamiltonian is mathematically identical to a 1D quantum harmonic oscillator shifted in equilibrium position to:
</p>
$$x_0 = -\frac{\hbar k_y}{eB} = -k_y l_B^2$$
<p>
where $l_B \equiv \sqrt{\frac{\hbar}{eB}}$ is the <strong>magnetic length</strong>.
</p>
<p>
The energy eigenvalues are the famous discrete <strong>Landau levels</strong>:
</p>
$$E_n = \hbar\omega_c\left(n + \frac{1}{2}\right) \quad (n = 0, 1, 2, \dots)$$

<h3>3. Macroscopic Degeneracy of Landau Levels</h3>
<p>
Notice that the energy $E_n$ is completely independent of $k_y$. For a sample of dimensions $L_x \times L_y$, the center of the harmonic oscillator must lie within the physical boundaries of the sample ($0 \le x_0 \le L_x$):
</p>
$$0 \le \frac{\hbar k_y}{eB} \le L_x \implies 0 \le k_y \le \frac{eBL_x}{\hbar}$$
<p>
With periodic boundary conditions along $y$, $k_y = \frac{2\pi n_y}{L_y}$, the number of allowed $k_y$ values in this interval is:
</p>
$$g = \frac{\Delta k_y}{2\pi / L_y} = \frac{eBL_x}{\hbar}\frac{L_y}{2\pi} = \frac{eB(L_x L_y)}{2\pi\hbar} = \frac{\Phi}{\Phi_0}$$
<p>
where $\Phi = B(L_x L_y)$ is the total magnetic flux through the sample and $\Phi_0 = \frac{h}{e}$ is the magnetic flux quantum. Each Landau level possesses a gigantic macroscopic degeneracy equal to the number of flux quanta piercing the sample, forming the physical basis of the Integer Quantum Hall Effect.
</p>
"""
        },
        {
            "id": "sec6-6",
            "title": "Symmetries of the Two-Nucleon System: Isospin Formalism & Identical Boson Scattering",
            "content": r"""
<h3>1. Nuclear Charge Independence and the Isospin Formalism</h3>
<p>
High-energy scattering experiments reveal that the strong nuclear interaction is charge-independent: the nuclear force between two protons ($p-p$), two neutrons ($n-n$), and a proton and neutron ($p-n$) in identical spatial and spin states is virtually identical.
</p>
<p>
To exploit this symmetry, Werner Heisenberg introduced the <strong>isospin</strong> formalism. The proton and neutron are viewed as two orthogonal isospin states of a single particle, the <em>nucleon</em>, with isospin $I = 1/2$:
</p>
$$|p\rangle = |1/2, +1/2\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |n\rangle = |1/2, -1/2\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$
<p>
The electric charge of a nucleon is given by the Gell-Mann-Nishijima formula:
</p>
$$Q = e\left(I_3 + \frac{1}{2}\right)$$

<h3>2. The Two-Nucleon System and the Deuteron</h3>
<p>
Coupling the isospins of two nucleons ($I_1 = 1/2, I_2 = 1/2$):
</p>
$$\frac{1}{2} \otimes \frac{1}{2} = 1 \oplus 0$$
<ul>
  <li><strong>Isospin Triplet ($I = 1$, symmetric in isospin):</strong> Includes $|1, 1\rangle = |pp\rangle$, $|1, -1\rangle = |nn\rangle$, and $|1, 0\rangle = \frac{1}{\sqrt{2}}(|pn\rangle + |np\rangle)$.</li>
  <li><strong>Isospin Singlet ($I = 0$, antisymmetric in isospin):</strong> $|0, 0\rangle = \frac{1}{\sqrt{2}}(|pn\rangle - |np\rangle)$.</li>
</ul>
<p>
Under the Generalized Pauli Principle, the total state of two nucleons must be completely antisymmetric under overall interchange of spatial, spin, and isospin coordinates:
</p>
$$\hat{P}_{\text{space}} \hat{P}_{\text{spin}} \hat{P}_{\text{isospin}} = (-1)^L (-1)^{S+1} (-1)^{I+1} = -1 \implies (-1)^{L + S + I} = -1$$
<p>
For the bound ground state of the deuteron (a proton-neutron bound state): experimentally, $L = 0$ (mostly $s$-wave) and total spin $J = 1$ ($S = 1$). Substituting into the condition:
</p>
$$(-1)^{0 + 1 + I} = -1 \implies (-1)^I = +1 \implies I = 0$$
<p>
The deuteron bound state is an isospin singlet ($I = 0$). This explains why there are no bound diproton ($pp$) or dineutron ($nn$) states in nature: both require $I = 1$, which has higher energy due to spin-dependent nuclear tensor forces!
</p>
"""
        }
    ],
    "simulations": [
        {
            "id": "qm2-fermi-gas-dos-sim",
            "title": "Degenerate Fermi Gas Density of States & Fermi Sphere",
            "description": "Simulation of the degenerate Fermi gas in 1D, 2D, and 3D showing density of states g(E), Fermi sphere filling up to EF, and Fermi-Dirac distribution thermal smearing."
        },
        {
            "id": "qm2-landau-levels-sim",
            "title": "2D Landau Level Quantization & Magnetic Degeneracy Visualizer",
            "description": "Interactive visualizer of 2D Landau levels in a magnetic field B, demonstrating cyclotron orbit collapse, harmonic oscillator potential shifts x₀, and macroscopic degeneracy g = Φ/Φ₀."
        }
    ],
    "solvedProblems": [
        {
            "number": 1,
            "title": "Two Non-Interacting Electrons in a 1D Harmonic Well: Singlet vs Triplet Energy",
            "statement": r"Two non-interacting electrons of mass $m$ are placed in a 1D harmonic trap $V(x) = \frac{1}{2}m\omega^2 x^2$.\n(a) Write down the normalized ground-state wavefunction and its total energy in the spin singlet ($S = 0$) configuration.\n(b) Write down the lowest-energy wavefunction and its total energy in the spin triplet ($S = 1$) configuration.\n(c) If a weak contact repulsive interaction $\hat{V}_{\text{int}} = g\delta(x_1 - x_2)$ ($g > 0$) is introduced between the electrons, compute the first-order energy shift for both singlet and triplet configurations.",
            "solution": r"**(a) Ground State in Spin Singlet Configuration ($S = 0$):**\nIn the singlet state, the spin wavefunction is antisymmetric:\n$$\chi_0 = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$$\nTo satisfy the Pauli principle, the spatial wavefunction must be symmetric. Both electrons can occupy the single-particle spatial ground state $\phi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-\frac{m\omega x^2}{2\hbar}}$:\n$$\psi_S(x_1, x_2) = \phi_0(x_1)\phi_0(x_2) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/2}\exp\left(-\frac{m\omega(x_1^2 + x_2^2)}{2\hbar}\right)$$\nTotal unperturbed energy:\n$$E_{\text{singlet}}^{(0)} = E_0 + E_0 = \frac{1}{2}\hbar\omega + \frac{1}{2}\hbar\omega = \hbar\omega$$\n\n**(b) Lowest State in Spin Triplet Configuration ($S = 1$):**\nIn the triplet state, the spin wavefunction is symmetric. The spatial wavefunction must be strictly antisymmetric. By the Pauli exclusion principle, the two electrons cannot both occupy $\phi_0(x)$. One electron must occupy the first excited state $\phi_1(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\sqrt{\frac{2m\omega}{\hbar}}x e^{-\frac{m\omega x^2}{2\hbar}}$:\n$$\psi_A(x_1, x_2) = \frac{1}{\sqrt{2}}\left[ \phi_0(x_1)\phi_1(x_2) - \phi_1(x_1)\phi_0(x_2) \right]$$\nTotal unperturbed energy:\n$$E_{\text{triplet}}^{(0)} = E_0 + E_1 = \frac{1}{2}\hbar\omega + \frac{3}{2}\hbar\omega = 2\hbar\omega$$\n\n**(c) First-Order Shift from Contact Interaction $\hat{V}_{\text{int}} = g\delta(x_1 - x_2)$:**\n1. For the Triplet state ($S = 1$):\n   Since $\psi_A(x, x) = \frac{1}{\sqrt{2}}[\phi_0(x)\phi_1(x) - \phi_1(x)\phi_0(x)] = 0$, the two electrons have zero probability of being at the same point in space. Therefore:\n   $$\Delta E_{\text{triplet}}^{(1)} = \iint |\psi_A(x_1, x_2)|^2 g\delta(x_1 - x_2)\,dx_1 dx_2 = g\int |\psi_A(x, x)|^2\,dx = 0$$\n2. For the Singlet state ($S = 0$):\n   $$\Delta E_{\text{singlet}}^{(1)} = g\int |\psi_S(x, x)|^2\,dx = g\int |\phi_0(x)|^4\,dx = g\left(\frac{m\omega}{\pi\hbar}\right)\int_{-\infty}^\infty e^{-2m\omega x^2/\hbar}\,dx$$\n   Using $\int_{-\infty}^\infty e^{-\alpha x^2}\,dx = \sqrt{\pi/\alpha}$ with $\alpha = \frac{2m\omega}{\hbar}$:\n   $$\Delta E_{\text{singlet}}^{(1)} = g\left(\frac{m\omega}{\pi\hbar}\right)\sqrt{\frac{\pi\hbar}{2m\omega}} = g\sqrt{\frac{m\omega}{2\pi\hbar}}$$\nThe contact interaction shifts only the singlet state, leaving the triplet state completely unaffected!"
        },
        {
            "number": 2,
            "title": "Degeneracy Pressure and Total Energy of a 3D Non-Relativistic Fermi Gas",
            "statement": r"A degenerate gas of $N$ non-relativistic electrons of mass $m$ is confined in a volume $V$ at $T = 0$.\n(a) Show that the density of states as a function of energy is $g(E) = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{E}$.\n(b) Prove that the average energy per electron is $\langle E \rangle = \frac{3}{5}E_F$, where $E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$.\n(c) Derive the equation of state for the degeneracy pressure $P = \frac{2}{5}n E_F$ and compute its numerical value for copper ($n \approx 8.5 \times 10^{28}\text{ m}^{-3}$).",
            "solution": r"**(a) Deriving the Density of States $g(E)$:**\nThe number of states inside a sphere of radius $k$ in $k$-space, accounting for electron spin $g_s = 2$, is:\n$$N(k) = 2 \frac{V}{(2\pi)^3}\left(\frac{4}{3}\pi k^3\right) = \frac{V k^3}{3\pi^2}$$\nUsing the non-relativistic dispersion relation $E = \frac{\hbar^2 k^2}{2m} \implies k = \left(\frac{2mE}{\hbar^2}\right)^{1/2}$:\n$$N(E) = \frac{V}{3\pi^2}\left(\frac{2mE}{\hbar^2}\right)^{3/2}$$\nDifferentiating with respect to $E$:\n$$g(E) = \frac{dN}{dE} = \frac{V}{3\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} \frac{3}{2}\sqrt{E} = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{E}$$\n\n**(b) Average Energy per Electron:**\nThe total energy is:\n$$E_{\text{total}} = \int_0^{E_F} E g(E)\,dE = C \int_0^{E_F} E^{3/2}\,dE = C \frac{2}{5}E_F^{5/2}$$\nwhere $C = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}$. Notice that the total particle count is:\n$$N = \int_0^{E_F} g(E)\,dE = C \int_0^{E_F} E^{1/2}\,dE = C \frac{2}{3}E_F^{3/2}$$\nDividing the two equations:\n$$\frac{E_{\text{total}}}{N} = \frac{\frac{2}{5}C E_F^{5/2}}{\frac{2}{3}C E_F^{3/2}} = \frac{3}{5}E_F \implies \langle E \rangle = \frac{3}{5}E_F$$\n\n**(c) Degeneracy Pressure:**\n$$E_{\text{total}} = \frac{3}{5}N E_F = \frac{3}{5}N \frac{\hbar^2}{2m}(3\pi^2)^{2/3}\left(\frac{N}{V}\right)^{2/3} = K V^{-2/3}$$\n$$P = -\frac{\partial E_{\text{total}}}{\partial V} = -K\left(-\frac{2}{3}V^{-5/3}\right) = \frac{2}{3}\frac{E_{\text{total}}}{V} = \frac{2}{3}\left(\frac{3}{5}n E_F\right) = \frac{2}{5}n E_F$$\nFor copper:\n$$k_F = (3\pi^2 \times 8.5 \times 10^{28}\text{ m}^{-3})^{1/3} \approx (2.517 \times 10^{30})^{1/3} \approx 1.36 \times 10^{10}\text{ m}^{-1}$$\n$$E_F = \frac{\hbar^2 k_F^2}{2m_e} = \frac{(1.055\times 10^{-34})^2 (1.36\times 10^{10})^2}{2(9.109\times 10^{-31})} \approx 1.13 \times 10^{-18}\text{ J} \approx 7.05\text{ eV}$$\nCalculating the degeneracy pressure:\n$$P = \frac{2}{5}(8.5 \times 10^{28}\text{ m}^{-3})(1.13 \times 10^{-18}\text{ J}) \approx 3.84 \times 10^{10}\text{ N/m}^2 \approx 3.8 \times 10^5\text{ atmospheres}$$\nThis pressure of almost 400,000 atmospheres explains why metals are incompressible solids!"
        },
        {
            "number": 3,
            "title": "Landau Level Orbital Degeneracy and Magnetic Flux Quanta",
            "statement": r"A 2D electron gas of area $A = L_x L_y$ is subject to a perpendicular magnetic field $B = 5\text{ T}$.\n(a) In the Landau gauge $\vec{A} = (0, Bx, 0)$, write down the effective 1D harmonic oscillator Hamiltonian and identify the equilibrium center coordinate $x_0$ as a function of the wavevector $k_y$.\n(b) Calculate the magnetic length $l_B = \sqrt{\hbar/(eB)}$.\n(c) Prove that the orbital degeneracy of each Landau level equals the number of magnetic flux quanta $\Phi / \Phi_0$, and compute the numerical degeneracy per square centimeter at $B = 5\text{ T}$.",
            "solution": r"**(a) Center Coordinate $x_0$:**\n$$\hat{H} = \frac{\hat{p}_x^2}{2m} + \frac{(\hbar k_y + eBx)^2}{2m} = \frac{\hat{p}_x^2}{2m} + \frac{1}{2}m\omega_c^2 \left(x + \frac{\hbar k_y}{eB}\right)^2$$\nThe harmonic oscillator potential is centered at:\n$$x_0 = -\frac{\hbar k_y}{eB} = -k_y l_B^2$$\n\n**(b) Magnetic Length:**\n$$l_B = \sqrt{\frac{\hbar}{eB}} = \sqrt{\frac{1.055 \times 10^{-34}\text{ J}\cdot\text{s}}{(1.602 \times 10^{-19}\text{ C})(5\text{ T})}} = \sqrt{\frac{1.055 \times 10^{-34}}{8.01 \times 10^{-19}}} = \sqrt{1.317 \times 10^{-16}} \approx 1.15 \times 10^{-8}\text{ m} = 11.5\text{ nm}$$\n\n**(c) Flux Quanta and Degeneracy:**\nThe center of the oscillator $x_0$ must lie inside the physical sample $0 \le x_0 \le L_x$:\n$$0 \le \frac{\hbar k_y}{eB} \le L_x \implies 0 \le k_y \le \frac{e B L_x}{\hbar}$$\nPeriodic boundary conditions along $y$ restrict $k_y = \frac{2\pi n_y}{L_y}$ with spacing $\Delta k_y = \frac{2\pi}{L_y}$.\nThe number of allowed orbital states is:\n$$g = \frac{k_{y,\max}}{\Delta k_y} = \frac{e B L_x}{\hbar} \frac{L_y}{2\pi} = \frac{e B (L_x L_y)}{2\pi\hbar} = \frac{B A}{h / e} = \frac{\Phi}{\Phi_0}$$\nwhere $\Phi_0 = \frac{h}{e} \approx 4.136 \times 10^{-15}\text{ Wb}$ is the magnetic flux quantum.\nDegeneracy per unit area:\n$$n_B = \frac{g}{A} = \frac{e B}{h} = \frac{(1.602 \times 10^{-19}\text{ C})(5\text{ T})}{6.626 \times 10^{-34}\text{ J}\cdot\text{s}} \approx 1.209 \times 10^{15}\text{ m}^{-2} = 1.209 \times 10^{11}\text{ states/cm}^2$$"
        }
    ]
}

with open("qm2_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5, f, indent=2)
print("Saved qm2_u5.json")

with open("qm2_u6.json", "w", encoding="utf-8") as f:
    json.dump(u6, f, indent=2)
print("Saved qm2_u6.json")
