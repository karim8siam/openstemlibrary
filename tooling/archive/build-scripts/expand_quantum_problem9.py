"""
expand_quantum_problem9.py
Provides Problem 9 for all 10 units of Quantum Chemistry and Statistical Thermodynamics.
Strictly zero prohibited tokens (no course numbers, no marks, no grades, no exams).
"""

def get_problem9_dict():
    return {
        "unit-1": {
            "id": "prob-1-9",
            "title": "Wavepacket Dispersion and Group Velocity of Free Matter Waves",
            "problem": r"""A free electron of mass \(m\) is described at \(t = 0\) by a normalized one-dimensional Gaussian wavepacket of initial spatial width \(\sigma_0\):
\[
\psi(x, 0) = \left( \frac{1}{2\pi \sigma_0^2} \right)^{1/4} \exp\left( -\frac{x^2}{4\sigma_0^2} + \frac{i p_0 x}{\hbar} \right)
\]
1. Calculate the initial momentum expectation value \(\langle p \rangle\), momentum uncertainty \(\sigma_p\), and verify that \(\sigma_x \sigma_p = \hbar / 2\).
2. By solving the time-dependent Schrödinger equation, express the width of the wavepacket \(\sigma(t)\) as a function of time \(t\).
3. If an electron has initial localization \(\sigma_0 = 1.00\text{ \AA}\) (\(10^{-10}\text{ m}\)), calculate the time \(\tau\) required for the wavepacket's spatial width to double.""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Initial Expectation Values and Minimum Uncertainty
The initial probability density is:
\[
|\psi(x, 0)|^2 = \left( \frac{1}{2\pi \sigma_0^2} \right)^{1/2} \exp\left( -\frac{x^2}{2\sigma_0^2} \right)
\]
By symmetry:
\[
\langle x \rangle = 0, \quad \langle x^2 \rangle = \sigma_0^2 \implies \sigma_x = \sigma_0
\]
The momentum expectation value is:
\[
\langle p \rangle = \int_{-\infty}^\infty \psi^* \left( -i\hbar \frac{\partial}{\partial x} \right) \psi \, dx = p_0
\]
For a Gaussian wavefunction, the momentum variance is:
\[
\langle p^2 \rangle = p_0^2 + \frac{\hbar^2}{4\sigma_0^2} \implies \sigma_p^2 = \langle p^2 \rangle - \langle p \rangle^2 = \frac{\hbar^2}{4\sigma_0^2} \implies \sigma_p = \frac{\hbar}{2\sigma_0}
\]
The uncertainty product is:
\[
\sigma_x \sigma_p = \sigma_0 \left( \frac{\hbar}{2\sigma_0} \right) = \frac{\hbar}{2}
\]
The Gaussian wavepacket is an exact minimum-uncertainty state.

---

#### Step 2: Time Evolution and Wavepacket Dispersion
The free-particle propagator is \(K(x, t; x', 0) = \sqrt{\frac{m}{2\pi i \hbar t}} \exp\left[ \frac{i m (x - x')^2}{2\hbar t} \right]\).
Performing the Gaussian convolution integral yields the time-dependent wavefunction:
\[
\psi(x, t) = \left( \frac{1}{2\pi \sigma_0^2} \right)^{1/4} \frac{1}{\sqrt{1 + i \hbar t / 2 m \sigma_0^2}} \exp\left[ -\frac{(x - p_0 t / m)^2}{4\sigma_0^2 (1 + i \hbar t / 2 m \sigma_0^2)} + \frac{i p_0 x}{\hbar} - \frac{i p_0^2 t}{2 m \hbar} \right]
\]
The probability density remains Gaussian, with its center moving at the classical group velocity \(v_g = p_0 / m\):
\[
|\psi(x, t)|^2 = \frac{1}{\sqrt{2\pi [\sigma(t)]^2}} \exp\left[ -\frac{(x - v_g t)^2}{2 [\sigma(t)]^2} \right]
\]
where the time-dependent spatial width is:
\[
\sigma(t) = \sigma_0 \sqrt{1 + \left( \frac{\hbar t}{2 m \sigma_0^2} \right)^2}
\]

---

#### Step 3: Doubling Time Calculation for an Electron
We require \(\sigma(\tau) = 2 \sigma_0\):
\[
\sqrt{1 + \left( \frac{\hbar \tau}{2 m \sigma_0^2} \right)^2} = 2 \implies 1 + \left( \frac{\hbar \tau}{2 m \sigma_0^2} \right)^2 = 4 \implies \left( \frac{\hbar \tau}{2 m \sigma_0^2} \right)^2 = 3
\]
\[
\frac{\hbar \tau}{2 m \sigma_0^2} = \sqrt{3} \implies \tau = \frac{2\sqrt{3} m \sigma_0^2}{\hbar}
\]
Substitute \(m = 9.10938 \times 10^{-31}\text{ kg}\), \(\sigma_0 = 1.00 \times 10^{-10}\text{ m}\), and \(\hbar = 1.05457 \times 10^{-34}\text{ J}\cdot\text{s}\):
\[
\tau = \frac{2 \sqrt{3} (9.10938 \times 10^{-31}\text{ kg})(1.00 \times 10^{-20}\text{ m}^2)}{1.05457 \times 10^{-34}\text{ J}\cdot\text{s}}
\]
\[
\tau = \frac{3.1556 \times 10^{-50}}{1.05457 \times 10^{-34}} \approx 2.99 \times 10^{-16}\text{ seconds} \approx 0.30\text{ femtoseconds}
\]
An electron localized within an atomic dimension (\(1\text{ \AA}\)) doubles its spatial spread in just 0.3 femtoseconds, illustrating how extreme quantum dispersion is for microscopic particles."""
        },
        "unit-2": {
            "id": "prob-2-9",
            "title": "Two-Dimensional Circular Quantum Billiard and Bessel Functions",
            "problem": r"""Consider a particle of mass \(m\) confined within a 2D circular billiard (quantum disk) of radius \(R\) with hard walls: \(V(r) = 0\) for \(r < R\) and \(\infty\) for \(r \ge R\).
1. Set up the Schrödinger equation in polar coordinates \((r, \phi)\) and separate variables \(\psi(r, \phi) = R(r) \Phi(\phi)\).
2. Show that the radial equation is Bessel's differential equation and state the boundary conditions.
3. Express the quantized energy eigenvalues in terms of the zeros of Bessel functions \(\alpha_{m, n}\), and calculate the ground-state energy for an electron in a quantum corral of radius \(R = 5.0\text{ nm}\).""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Separation of Variables in Polar Coordinates
In polar coordinates \((r, \phi)\), the Laplacian is:
\[
\nabla^2 = \frac{\partial^2}{\partial r^2} + \frac{1}{r} \frac{\partial}{\partial r} + \frac{1}{r^2} \frac{\partial^2}{\partial \phi^2}
\]
The time-independent Schrödinger equation for \(r < R\) is:
\[
-\frac{\hbar^2}{2m} \left( \frac{\partial^2 \psi}{\partial r^2} + \frac{1}{r} \frac{\partial \psi}{\partial r} + \frac{1}{r^2} \frac{\partial^2 \psi}{\partial \phi^2} \right) = E \psi
\]
Let \(k = \sqrt{2m E}/\hbar\) and substitute \(\psi(r, \phi) = R(r) \Phi(\phi)\):
\[
\frac{r^2}{R(r)} \left( \frac{d^2 R}{dr^2} + \frac{1}{r} \frac{dR}{dr} \right) + k^2 r^2 = -\frac{1}{\Phi(\phi)} \frac{d^2 \Phi}{d\phi^2} = m_l^2
\]
The angular equation \(\frac{d^2 \Phi}{d\phi^2} = -m_l^2 \Phi\) with cyclic boundary condition \(\Phi(\phi + 2\pi) = \Phi(\phi)\) requires:
\[
m_l \in \{0, \pm 1, \pm 2, \dots\}, \quad \Phi(\phi) = \frac{1}{\sqrt{2\pi}} e^{i m_l \phi}
\]

---

#### Step 2: Radial Equation and Bessel Functions
The radial equation becomes:
\[
r^2 \frac{d^2 R}{dr^2} + r \frac{dR}{dr} + (k^2 r^2 - m_l^2) R = 0
\]
Let \(\rho = k r\):
\[
\rho^2 \frac{d^2 R}{d\rho^2} + \rho \frac{dR}{d\rho} + (\rho^2 - m_l^2) R = 0
\]
This is Bessel's differential equation of order \(m_l\). The general solution is a linear combination of Bessel functions of the first kind \(J_{m_l}(\rho)\) and Neumann functions (Bessel functions of the second kind) \(Y_{m_l}(\rho)\):
\[
R(r) = C_1 J_{m_l}(k r) + C_2 Y_{m_l}(k r)
\]
Because \(Y_{m_l}(k r) \rightarrow -\infty\) as \(r \rightarrow 0\), physical wavefunctions must have \(C_2 = 0\):
\[
R(r) = C J_{m_l}(k r)
\]
Boundary condition at the wall \(r = R\):
\[
R(R) = 0 \implies J_{m_l}(k R) = 0
\]

---

#### Step 3: Quantized Energy Spectrum and Numerical Calculation
Let \(\alpha_{m_l, n}\) denote the \(n\)-th positive root (zero) of the Bessel function \(J_{m_l}(x)\):
\[
k R = \alpha_{m_l, n} \implies k = \frac{\alpha_{m_l, n}}{R}
\]
The quantized energy eigenvalues are:
\[
E_{m_l, n} = \frac{\hbar^2 k^2}{2m} = \frac{\hbar^2 \alpha_{m_l, n}^2}{2 m R^2} \quad (m_l = 0, 1, 2, \dots; \; n = 1, 2, 3, \dots)
\]
The absolute ground state occurs for \(m_l = 0\) (zero angular momentum) and the first root \(n = 1\).
The first zero of \(J_0(x)\) is:
\[
\alpha_{0, 1} \approx 2.4048
\]
For an electron (\(m_e = 9.10938 \times 10^{-31}\text{ kg}\)) in a corral of radius \(R = 5.0\text{ nm} = 5.0 \times 10^{-9}\text{ m}\):
\[
E_{0, 1} = \frac{(1.05457 \times 10^{-34}\text{ J}\cdot\text{s})^2 (2.4048)^2}{2(9.10938 \times 10^{-31}\text{ kg})(5.0 \times 10^{-9}\text{ m})^2} = \frac{(1.1121 \times 10^{-68})(5.7832)}{(1.8219 \times 10^{-30})(2.5 \times 10^{-17})}
\]
\[
E_{0, 1} = \frac{6.4315 \times 10^{-68}}{4.5547 \times 10^{-47}} \approx 1.412 \times 10^{-21}\text{ J}
\]
Converting to electron volts:
\[
E_{0, 1} = \frac{1.412 \times 10^{-21}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} \approx 0.00881\text{ eV} = 8.81\text{ meV}
\]
This describes the standing de Broglie electron wave patterns observed with scanning tunneling microscopes (STM) in artificial atomic quantum corrals."""
        },
        "unit-3": {
            "id": "prob-3-9",
            "title": "Spherical Harmonics and Rigid Rotor Transition Dipole Moment",
            "problem": r"""Consider a rigid rotor molecule with permanent electric dipole moment \(\mu_0\) oriented along its internuclear axis \(\mathbf{r}/r\).
1. Write the electric dipole moment component \(\hat{\mu}_z = \mu_0 \cos\theta\) in terms of the Spherical Harmonic \(Y_1^0(\theta, \phi)\).
2. Evaluate the transition dipole matrix element \(\langle J', M' | \hat{\mu}_z | J, M \rangle\) between rotational states \(|J, M\rangle\) and \(|J', M'\rangle\).
3. Prove mathematically that rotational transitions require \(\Delta J = \pm 1\) and \(\Delta M = 0\) for \(z\)-polarized radiation.""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Dipole Moment in Spherical Harmonics
The \(z\)-component of the dipole moment is:
\[
\hat{\mu}_z = \mu_0 \cos\theta
\]
Recall that the Spherical Harmonic for \(l = 1, m = 0\) is:
\[
Y_1^0(\theta, \phi) = \sqrt{\frac{3}{4\pi}} \cos\theta \implies \cos\theta = \sqrt{\frac{4\pi}{3}} Y_1^0(\theta, \phi)
\]
Therefore:
\[
\hat{\mu}_z = \mu_0 \sqrt{\frac{4\pi}{3}} Y_1^0(\theta, \phi)
\]

---

#### Step 2: Evaluation of the Transition Dipole Matrix Element
The transition dipole integral is:
\[
\langle J', M' | \hat{\mu}_z | J, M \rangle = \mu_0 \sqrt{\frac{4\pi}{3}} \int_0^{2\pi} d\phi \int_0^\pi \sin\theta \, d\theta \, [Y_{J'}^{M'}(\theta, \phi)]^* Y_1^0(\theta, \phi) Y_J^M(\theta, \phi)
\]
The integral over three Spherical Harmonics evaluates via Clebsch-Gordan coefficients / Wigner \(3j\)-symbols:
\[
\int Y_{J'}^{M'*} Y_{J_2}^{M_2} Y_J^M d\Omega = (-1)^{M'} \sqrt{\frac{(2J'+1)(2J_2+1)(2J+1)}{4\pi}} \begin{pmatrix} J' & J_2 & J \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} J' & J_2 & J \\ -M' & M_2 & M \end{pmatrix}
\]
Here \(J_2 = 1\) and \(M_2 = 0\):
1. **Selection rule for \(M\):**
   The second \(3j\)-symbol requires \(-M' + 0 + M = 0 \implies M' = M \implies \Delta M = 0\).
2. **Selection rule for \(J\):**
   By angular momentum addition triangle rules for coupling \(J\) and \(1\):
   \[
   |J - 1| \le J' \le J + 1 \implies J' \in \{J - 1, J, J + 1\}
   \]
   Furthermore, the parity condition embodied in \(\begin{pmatrix} J' & 1 & J \\ 0 & 0 & 0 \end{pmatrix}\) requires that \(J' + 1 + J\) must be an **even integer**.
   - If \(J' = J\): \(J + 1 + J = 2J + 1\) is odd, so the \(3j\)-symbol is strictly zero!
   - Therefore, \(J' = J\) is forbidden: \(\Delta J \ne 0\).
   - Only \(J' = J + 1\) and \(J' = J - 1\) survive.

---

#### Step 3: Selection Rule Proof
The explicit analytical result for the transition \(J \rightarrow J + 1\) with \(\Delta M = 0\) is:
\[
|\langle J + 1, M | \hat{\mu}_z | J, M \rangle|^2 = \mu_0^2 \frac{(J + 1)^2 - M^2}{(2J + 1)(2J + 3)}
\]
- When \(J' = J \pm 1\), the transition dipole moment is non-zero (allowed electric dipole transition).
- When \(J' = J\) or \(|J' - J| > 1\), the integral vanishes identically by parity and angular momentum orthogonality.
Thus, pure rotational absorption in linear molecules requires:
\[
\Delta J = \pm 1, \quad \Delta M = 0 \quad (\text{for } z\text{-polarized radiation})
\]
and \(\Delta M = \pm 1\) for circularly polarized radiation. This fundamental selection rule gives rise to the classic microwave spectra with lines evenly spaced by \(2B\)."""
        },
        "unit-4": {
            "id": "prob-4-9",
            "title": "Quadrupole Coupling and Electric Field Gradients in Hydrogenic Ions",
            "problem": r"""For a nucleus with non-spherical charge distribution and electric quadrupole moment \(Q\) interacting with an atomic electron:
1. Define the electric field gradient (EFG) tensor component \(q_{z z} = \frac{\partial^2 V}{\partial z^2}\) at the nucleus.
2. Given that for a hydrogenic orbital with quantum numbers \(n, l\):
   \[
   q_{z z} = -e \langle r^{-3} \rangle_{n l} \frac{l(l + 1) - 3 m_l^2}{(2l - 1)(2l + 3)}
   \]
   Show that \(q_{z z} = 0\) for all \(s\)-orbitals (\(l = 0\)).
3. For a \(2p_z\) electron in a hydrogenic ion of charge \(Z\), where \(\langle r^{-3} \rangle_{2p} = \frac{Z^3}{24 a_0^3}\), calculate \(q_{z z}\) in terms of fundamental constants.""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Definition of Electric Field Gradient (EFG)
The electrostatic potential produced at the nucleus (\(\mathbf{r} = 0\)) by an electron at position \(\mathbf{r}\) is:
\[
V(\mathbf{r}) = -\frac{e}{4\pi\varepsilon_0 r}
\]
The Electric Field Gradient (EFG) tensor \(V_{i j}\) is the second spatial derivative of the electrostatic potential:
\[
V_{i j} = \frac{\partial^2 V}{\partial x_i \partial x_j} = -\frac{e}{4\pi\varepsilon_0} \left( \frac{3 x_i x_j - r^2 \delta_{i j}}{r^5} \right)
\]
In traceless principal axis form, the principal EFG component is:
\[
e q_{z z} = V_{z z} = -\frac{e}{4\pi\varepsilon_0} \int \psi^* \left( \frac{3 z^2 - r^2}{r^5} \right) \psi \, d\tau = -\frac{e}{4\pi\varepsilon_0} \int \psi^* \left( \frac{3\cos^2\theta - 1}{r^3} \right) \psi \, d\tau
\]

---

#### Step 2: Vanishing of EFG for \(s\)-Orbitals (\(l = 0\))
For any \(s\)-orbital, the angular wavefunction is spherically symmetric:
\[
Y_0^0 = \frac{1}{\sqrt{4\pi}} \implies |\psi|^2 = \frac{1}{4\pi} [R_{n0}(r)]^2
\]
The angular integration over the sphere is:
\[
\int_0^\pi (3\cos^2\theta - 1) \sin\theta \, d\theta \int_0^{2\pi} d\phi = 2\pi \int_{-1}^1 (3 u^2 - 1) du
\]
Evaluate the integral:
\[
\int_{-1}^1 (3 u^2 - 1) du = \left[ u^3 - u \right]_{-1}^1 = (1 - 1) - (-1 - (-1)) = 0 - 0 = 0
\]
Because the angular factor \(3\cos^2\theta - 1 = 2 P_2(\cos\theta)\) is orthogonal to \(P_0(\cos\theta) = 1\), the integral vanishes identically:
\[
q_{z z}(s\text{-orbitals}) \equiv 0
\]
All \(s\)-electrons produce exactly zero electric field gradient at the nucleus, meaning they cannot induce nuclear quadrupole splitting!

---

#### Step 3: EFG for \(2p_z\) Electron (\(l = 1, m_l = 0\))
For a \(2p_z\) orbital, \(l = 1\) and \(m_l = 0\):
Evaluate the angular prefactor:
\[
\frac{l(l + 1) - 3 m_l^2}{(2l - 1)(2l + 3)} = \frac{1(2) - 3(0)^2}{(2 - 1)(2 + 3)} = \frac{2}{(1)(5)} = \frac{2}{5}
\]
Substitute into the formula with \(\langle r^{-3} \rangle_{2p} = \frac{Z^3}{24 a_0^3}\):
\[
q_{z z} = -e \left( \frac{Z^3}{24 a_0^3} \right) \left( \frac{2}{5} \right) = -e \frac{2 Z^3}{120 a_0^3} = -\frac{e Z^3}{60 a_0^3}
\]
Including the electrostatic constant \(\frac{1}{4\pi\varepsilon_0}\):
\[
V_{z z}(2p_z) = -\frac{e Z^3}{240 \pi \varepsilon_0 a_0^3}
\]
This non-zero electric field gradient couples to the nuclear electric quadrupole moment \(e Q\), generating nuclear quadrupole resonance (NQR) and hyperfine quadrupole splittings in high-resolution NMR and microwave spectra."""
        },
        "unit-5": {
            "id": "prob-5-9",
            "title": "Hellmann-Feynman Theorem for Harmonic and Coulomb Potentials",
            "problem": r"""The Hellmann-Feynman theorem states that for an exact normalized eigenstate \(\psi_\lambda\) with energy \(E(\lambda)\) governed by Hamiltonian \(\hat{H}(\lambda)\):
\[
\frac{d E}{d\lambda} = \left\langle \psi_\lambda \left| \frac{\partial \hat{H}}{\partial \lambda} \right| \psi_\lambda \right\rangle
\]
1. Prove the Hellmann-Feynman theorem using the hermiticity of \(\hat{H}\).
2. For the 1D harmonic oscillator with \(\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + \frac{1}{2} k x^2\) and \(E_n = \left(n + \frac{1}{2}\right)\hbar \sqrt{k/m}\), use the theorem with \(\lambda = k\) to find \(\langle x^2 \rangle_n\).
3. For the hydrogen atom with \(\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 - \frac{Z e^2}{4\pi\varepsilon_0 r}\) and \(E_n = -\frac{m Z^2 e^4}{32\pi^2\varepsilon_0^2\hbar^2 n^2}\), use the theorem with \(\lambda = Z\) to evaluate \(\langle r^{-1} \rangle_{n l}\).""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Proof of the Hellmann-Feynman Theorem
By definition:
\[
E(\lambda) = \langle \psi(\lambda) | \hat{H}(\lambda) | \psi(\lambda) \rangle
\]
Differentiate both sides with respect to \(\lambda\) using the product rule:
\[
\frac{d E}{d\lambda} = \left\langle \frac{\partial \psi}{\partial \lambda} \middle| \hat{H} \middle| \psi \right\rangle + \left\langle \psi \middle| \frac{\partial \hat{H}}{\partial \lambda} \middle| \psi \right\rangle + \left\langle \psi \middle| \hat{H} \middle| \frac{\partial \psi}{\partial \lambda} \right\rangle
\]
Because \(\hat{H}\) is Hermitian and \(\hat{H}|\psi\rangle = E|\psi\rangle\):
\[
\left\langle \frac{\partial \psi}{\partial \lambda} \middle| \hat{H} \middle| \psi \right\rangle = E \left\langle \frac{\partial \psi}{\partial \lambda} \middle| \psi \right\rangle
\]
\[
\left\langle \psi \middle| \hat{H} \middle| \frac{\partial \psi}{\partial \lambda} \right\rangle = E \left\langle \psi \middle| \frac{\partial \psi}{\partial \lambda} \right\rangle
\]
Summing both terms:
\[
E \left[ \left\langle \frac{\partial \psi}{\partial \lambda} \middle| \psi \right\rangle + \left\langle \psi \middle| \frac{\partial \psi}{\partial \lambda} \right\rangle \right] = E \frac{d}{d\lambda} \langle \psi | \psi \rangle
\]
Since the wavefunction is normalized for all \(\lambda\) (\(\langle \psi | \psi \rangle = 1\)), \(\frac{d}{d\lambda}(1) = 0\).
Therefore, the boundary derivative terms vanish identically, leaving:
\[
\frac{d E}{d\lambda} = \left\langle \psi \left| \frac{\partial \hat{H}}{\partial \lambda} \right| \psi \right\rangle \quad \text{Q.E.D.}
\]

---

#### Step 2: Evaluation of \(\langle x^2 \rangle\) for the Harmonic Oscillator
Set \(\lambda = k\) (spring constant).
1. Differentiate the Hamiltonian:
   \[
   \frac{\partial \hat{H}}{\partial k} = \frac{\partial}{\partial k} \left( -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + \frac{1}{2} k x^2 \right) = \frac{1}{2} x^2
   \]
2. Differentiate the exact energy \(E_n = \left(n + \frac{1}{2}\right)\hbar \sqrt{\frac{k}{m}}\):
   \[
   \frac{d E_n}{dk} = \left(n + \frac{1}{2}\right)\frac{\hbar}{\sqrt{m}} \frac{1}{2\sqrt{k}} = \frac{1}{2k} \left(n + \frac{1}{2}\right)\hbar\omega = \frac{E_n}{2k}
   \]
3. Equating by the Hellmann-Feynman theorem:
   \[
   \left\langle \frac{1}{2} x^2 \right\rangle = \frac{d E_n}{dk} = \frac{E_n}{2k} \implies \langle x^2 \rangle_n = \frac{E_n}{k} = \left(n + \frac{1}{2}\right) \frac{\hbar}{m\omega}
   \]
Notice that \(\langle V \rangle = \frac{1}{2} k \langle x^2 \rangle = \frac{1}{2} E_n\), automatically verifying the virial theorem!

---

#### Step 3: Evaluation of \(\langle r^{-1} \rangle\) for the Hydrogen Atom
Set \(\lambda = Z\) (nuclear charge).
1. Differentiate the Hamiltonian:
   \[
   \frac{\partial \hat{H}}{\partial Z} = \frac{\partial}{\partial Z} \left( -\frac{\hbar^2}{2m}\nabla^2 - \frac{Z e^2}{4\pi\varepsilon_0 r} \right) = -\frac{e^2}{4\pi\varepsilon_0 r}
   \]
2. Differentiate the energy \(E_n = -Z^2 \frac{m e^4}{32\pi^2\varepsilon_0^2\hbar^2 n^2}\):
   \[
   \frac{d E_n}{d Z} = -2 Z \frac{m e^4}{32\pi^2\varepsilon_0^2\hbar^2 n^2} = \frac{2 E_n}{Z}
   \]
3. Apply Hellmann-Feynman:
   \[
   \left\langle -\frac{e^2}{4\pi\varepsilon_0 r} \right\rangle = \frac{2 E_n}{Z}
   \]
   Recall \(a_0 = \frac{4\pi\varepsilon_0\hbar^2}{m e^2}\) and \(E_n = -\frac{Z^2 e^2}{8\pi\varepsilon_0 a_0 n^2}\):
   \[
   -\frac{e^2}{4\pi\varepsilon_0} \langle r^{-1} \rangle = 2 \left( -\frac{Z e^2}{8\pi\varepsilon_0 a_0 n^2} \right) = -\frac{Z e^2}{4\pi\varepsilon_0 a_0 n^2}
   \]
   Dividing both sides by \(-\frac{e^2}{4\pi\varepsilon_0}\):
   \[
   \langle r^{-1} \rangle_{n l} = \frac{Z}{a_0 n^2}
   \]
The Hellmann-Feynman theorem evaluates complex quantum expectation values in a single line of calculus."""
        },
        "unit-6": {
            "id": "prob-6-9",
            "title": "Walsh Diagrams and Molecular Geometry Prediction for AH2 Molecules",
            "problem": r"""Walsh diagrams correlate molecular orbital energies as a function of bond angle \(\theta = \angle\text{H-A-H}\) (from linear \(180^\circ\) to bent \(90^\circ\)):
For triatomic dihydrides \(\text{AH}_2\):
The valence molecular orbitals in \(C_{2v}\) symmetry (bent) correlate with \(D_{\infty h}\) symmetry (linear) as follows:
- \(2a_1\) correlates with \(2\sigma_g^+\) (predominantly \(\text{A}(s)\) character, stabilizes slightly on bending)
- \(1b_2\) correlates with \(1\sigma_u^+\) (antisymmetric \(\text{A}(p_y) - \text{H}(1s)\), destabilizes on bending)
- \(3a_1\) correlates with \(1\pi_u\) (pure non-bonding \(p_z\) orbital that gains substantial \(s\)-character on bending, causing a steep drop in energy)
- \(1b_1\) correlates with \(1\pi_u\) (pure non-bonding \(p_x\) out-of-plane, energy remains constant)
1. Determine the valence electron count for:
   - Water (\(\text{H}_2\text{O}\))
   - Methylene radical (\(\text{CH}_2\))
   - Beryllium hydride (\(\text{BeH}_2\))
2. Using the Walsh diagram orbital ordering, assign the ground-state valence electron configuration for each molecule.
3. Explain why \(\text{BeH}_2\) is strictly linear while \(\text{H}_2\text{O}\) is strongly bent (\(\theta \approx 104.5^\circ\)).""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Valence Electron Counts
1. **\(\text{BeH}_2\):** Be (\(2\) valence) + 2 \(\times\) H (\(1\)) = **4 valence electrons**.
2. **\(\text{CH}_2\):** C (\(4\) valence) + 2 \(\times\) H (\(1\)) = **6 valence electrons**.
3. **\(\text{H}_2\text{O}\):** O (\(6\) valence) + 2 \(\times\) H (\(1\)) = **8 valence electrons**.

---

#### Step 2: Ground-State Valence Electron Configurations
1. **For \(\text{BeH}_2\) (4 valence electrons):**
   - Fills the lowest two molecular orbitals:
     - In linear \(D_{\infty h}\): \((2\sigma_g)^2 (1\sigma_u)^2\)
     - In bent \(C_{2v}\): \((2a_1)^2 (1b_2)^2\)
2. **For \(\text{CH}_2\) (6 valence electrons):**
   - Fills the lowest three molecular orbitals:
     - In linear \(D_{\infty h}\): \((2\sigma_g)^2 (1\sigma_u)^2 (1\pi_u)^2\)
     - In bent \(C_{2v}\): \((2a_1)^2 (1b_2)^2 (3a_1)^2\) (singlet) or \((2a_1)^2 (1b_2)^2 (3a_1)^1 (1b_1)^1\) (triplet ground state)
3. **For \(\text{H}_2\text{O}\) (8 valence electrons):**
   - Fills the lowest four molecular orbitals:
     - In linear \(D_{\infty h}\): \((2\sigma_g)^2 (1\sigma_u)^2 (1\pi_u)^4\)
     - In bent \(C_{2v}\): \((2a_1)^2 (1b_2)^2 (3a_1)^2 (1b_1)^2\)

---

#### Step 3: Geometry Predictions from Walsh's Rules
1. **\(\text{BeH}_2\) (4 electrons):**
   - Occupies \((2a_1)^2\) and \((1b_2)^2\).
   - As the bond angle bends from \(180^\circ\) toward \(90^\circ\), the \(2a_1\) orbital stabilizes slightly, but the \(1b_2\) orbital rises steeply in energy due to destructive overlap of hydrogen \(1s\) orbitals.
   - The total energy is minimized at \(\theta = 180^\circ\).
   - Therefore, \(\mathbf{BeH_2}\) is strictly **linear**.

2. **\(\text{H}_2\text{O}\) (8 electrons):**
   - In addition to \(2a_1\) and \(1b_2\), water occupies the \(3a_1\) and \(1b_1\) orbitals.
   - The crucial orbital is **\(3a_1\)**: in the linear geometry, it is an unhybridized \(p_z\) orbital with relatively high energy. As the molecule bends, the central oxygen atom mixes in substantial \(2s\) character (\(s-p\) hybridization), causing the \(3a_1\) orbital energy to plunge dramatically downward.
   - Because \(3a_1\) is doubly occupied (\(3a_1^2\)), this steep energetic drop overwhelms the slight destabilization of \(1b_2\).
   - The total electronic energy reaches a deep minimum at a bent angle.
   - Including hydrogen-hydrogen core repulsion, the equilibrium bond angle settles at \(\theta \approx 104.5^\circ\).
   - Therefore, \(\mathbf{H_2O}\) is strongly **bent**.

Walsh diagrams provide a universal orbital-based explanation of molecular stereochemistry, correctly predicting the shapes of all \(AH_2, AH_3, AB_2\), and \(HAB\) molecules."""
        },
        "unit-7": {
            "id": "prob-7-9",
            "title": "Grand Canonical Particle Fluctuations and Isothermal Compressibility",
            "problem": r"""In the grand canonical ensemble with grand partition function \(\Xi(\mu, V, T)\):
1. Derive the expression for the average particle number \(\langle N \rangle\) and particle number variance \(\sigma_N^2 = \langle N^2 \rangle - \langle N \rangle^2\) in terms of derivatives of \(\ln\Xi\).
2. Prove the fluctuation theorem connecting particle number fluctuations to the isothermal compressibility \(\kappa_T = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_T\):
   \[
   \frac{\sigma_N^2}{\langle N \rangle} = \rho k_B T \kappa_T
   \]
   where \(\rho = \langle N \rangle / V\) is number density.
3. For an ideal gas (\(\kappa_T = 1/P\)), calculate \(\sigma_N^2 / \langle N \rangle\) and explain the physical significance of critical opalescence near liquid-gas critical points.""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Particle Number and Variance Derivatives
The grand canonical partition function is:
\[
\Xi = \sum_N \sum_i e^{-\beta (E_{N, i} - \mu N)}
\]
The average particle number is:
\[
\langle N \rangle = \frac{1}{\Xi} \sum_N \sum_i N e^{-\beta (E_{N, i} - \mu N)} = \frac{1}{\beta} \left( \frac{\partial \ln \Xi}{\partial \mu} \right)_{T, V} = k_B T \left( \frac{\partial \ln \Xi}{\partial \mu} \right)_{T, V}
\]
Differentiating \(\langle N \rangle\) with respect to \(\mu\):
\[
\left( \frac{\partial \langle N \rangle}{\partial \mu} \right)_{T, V} = \frac{\partial}{\partial \mu} \left( \frac{1}{\Xi} \sum_N N e^{-\beta(E - \mu N)} \right) = \frac{\beta}{\Xi} \sum_N N^2 e^{-\beta(E - \mu N)} - \frac{\beta}{\Xi^2} \left( \frac{\partial \Xi}{\partial \mu} \right) \sum_N N e^{-\beta(E - \mu N)}
\]
\[
\left( \frac{\partial \langle N \rangle}{\partial \mu} \right)_{T, V} = \beta \langle N^2 \rangle - \beta \langle N \rangle^2 = \beta \sigma_N^2
\]
Therefore:
\[
\sigma_N^2 = \langle N^2 \rangle - \langle N \rangle^2 = k_B T \left( \frac{\partial \langle N \rangle}{\partial \mu} \right)_{T, V}
\]

---

#### Step 2: Relation to Isothermal Compressibility \(\kappa_T\)
From the Gibbs-Duhem equation at constant temperature:
\[
N d\mu = V dP \implies d\mu = \frac{V}{N} dP = \frac{1}{\rho} dP
\]
Therefore:
\[
\left( \frac{\partial N}{\partial \mu} \right)_{T, V} = \left( \frac{\partial N}{\partial P} \right)_{T, V} \left( \frac{\partial P}{\partial \mu} \right)_T = \left( \frac{\partial N}{\partial P} \right)_{T, V} \rho
\]
Now use the thermodynamic relation for intensive density \(\rho = N/V\):
\[
\left( \frac{\partial N}{\partial P} \right)_{T, V} = -\frac{N^2}{V^2} \left( \frac{\partial V}{\partial P} \right)_{T, N} = \rho^2 V \kappa_T
\]
where \(\kappa_T = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_T\) is the isothermal compressibility.
Substituting into the variance:
\[
\sigma_N^2 = k_B T \left( \frac{\partial N}{\partial \mu} \right) = k_B T \rho \left( \rho^2 V \kappa_T \frac{1}{\rho} \right) = k_B T \rho^2 V \kappa_T = N \rho k_B T \kappa_T
\]
Dividing by \(\langle N \rangle\):
\[
\frac{\sigma_N^2}{\langle N \rangle} = \rho k_B T \kappa_T
\]

---

#### Step 3: Ideal Gas and Critical Opalescence
1. **For an Ideal Gas:**
   The equation of state is \(P = \rho k_B T\).
   The isothermal compressibility is:
   \[
   \kappa_T = -\frac{1}{V} \left( -\frac{n R T}{P^2} \right) = \frac{1}{P} = \frac{1}{\rho k_B T}
   \]
   Substitute into the fluctuation ratio:
   \[
   \frac{\sigma_N^2}{\langle N \rangle} = \rho k_B T \left( \frac{1}{\rho k_B T} \right) = 1
   \]
   For an ideal gas, \(\sigma_N^2 = \langle N \rangle\). The particle number follows a **Poisson distribution**, with relative fluctuation \(\frac{\sigma_N}{N} = \frac{1}{\sqrt{N}}\).
2. **Critical Opalescence:**
   Near a liquid-gas critical point (e.g., \(\text{CO}_2\) at \(31.0^\circ\text{C}, 73.8\text{ bar}\)), the slope of the isotherm flattens: \(\left(\frac{\partial P}{\partial V}\right)_T \rightarrow 0\).
   Consequently, the isothermal compressibility diverges:
   \[
   \kappa_T \rightarrow \infty \implies \sigma_N^2 \rightarrow \infty
   \]
   Density fluctuations grow to macroscopic length scales comparable to the wavelength of visible light (\(\sim 500\text{ nm}\)). The fluid scatters light violently in all directions, turning completely milky-white and opaque: **Critical Opalescence**."""
        },
        "unit-8": {
            "id": "prob-8-9",
            "title": "Rotational Relaxation and Ortho-to-Para Conversion Rates",
            "problem": r"""Consider a cryogenic sample of molecular hydrogen \(\text{H}_2\) cooled from \(300\text{ K}\) to \(20.0\text{ K}\).
1. State the fraction of ortho-\(\text{H}_2\) and para-\(\text{H}_2\) at \(300\text{ K}\) (normal hydrogen) and at \(20.0\text{ K}\) at true thermal equilibrium.
2. In the absence of a catalyst, ortho-to-para conversion follows second-order kinetics driven by nuclear dipole-dipole interactions between colliding molecules:
   \[
   -\frac{d x_{\text{ortho}}}{dt} = k_{\text{conv}} x_{\text{ortho}}^2
   \]
   with rate constant \(k_{\text{conv}} = 0.019\text{ hr}^{-1}\) in the liquid phase.
   Calculate the time required for the ortho fraction to drop from \(0.75\) to \(0.50\).
3. If the enthalpy of ortho-to-para conversion is \(\Delta H_{\text{conv}} = 1.42\text{ kJ/mol}\) and the heat of vaporization of liquid \(\text{H}_2\) is \(\Delta H_{\text{vap}} = 0.904\text{ kJ/mol}\), calculate the mass of liquid hydrogen boiled off per mole of unconverted ortho-hydrogen that undergoes spontaneous relaxation in an unvented storage dewar.""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Equilibrium Ortho and Para Fractions
- At \(T = 300\text{ K}\) (high temperature limit):
  \[
  x_{\text{ortho}} = \frac{3}{3 + 1} = 0.75 = 75\%, \quad x_{\text{para}} = \frac{1}{3 + 1} = 0.25 = 25\%
  \]
- At \(T = 20.0\text{ K}\) (\(\theta_{\text{rot}} = 85.3\text{ K} \implies \theta / T = 4.265\)):
  \[
  q_{\text{para}} \approx 1.000, \quad q_{\text{ortho}} = 3(3) e^{-2(4.265)} = 9 e^{-8.53} \approx 9(0.000197) \approx 0.00177
  \]
  Equilibrium fractions:
  \[
  x_{\text{ortho}} \approx \frac{0.00177}{1.00177} \approx 0.18\%, \quad x_{\text{para}} \approx 99.82\%
  \]
  True equilibrium liquid hydrogen is virtually 100% pure para-\(\text{H}_2\).

---

#### Step 2: Uncatalyzed Conversion Kinetics
The rate law is:
\[
-\frac{d x}{dt} = k_{\text{conv}} x^2 \implies \int_{x_0}^{x_t} \frac{dx}{x^2} = -k_{\text{conv}} \int_0^t dt
\]
\[
\frac{1}{x_t} - \frac{1}{x_0} = k_{\text{conv}} t \implies t = \frac{1}{k_{\text{conv}}} \left( \frac{1}{x_t} - \frac{1}{x_0} \right)
\]
Substitute \(x_0 = 0.75\), \(x_t = 0.50\), and \(k_{\text{conv}} = 0.019\text{ hr}^{-1}\):
\[
\frac{1}{0.50} - \frac{1}{0.75} = 2.000 - 1.333 = 0.667
\]
\[
t = \frac{0.667}{0.019\text{ hr}^{-1}} \approx 35.1\text{ hours}
\]
Without a catalyst, it takes over 35 hours for the ortho concentration to decrease from 75% to 50%.

---

#### Step 3: Liquid Boil-Off Calculation
Relaxation of 1 mole of ortho-\(\text{H}_2\) to para-\(\text{H}_2\) releases:
\[
Q_{\text{released}} = \Delta H_{\text{conv}} = 1.42\text{ kJ/mol}
\]
Each mole of liquid hydrogen vaporized absorbs:
\[
\Delta H_{\text{vap}} = 0.904\text{ kJ/mol}
\]
The moles of liquid hydrogen boiled off per mole of relaxing ortho-\(\text{H}_2\) is:
\[
n_{\text{boiled}} = \frac{Q_{\text{released}}}{\Delta H_{\text{vap}}} = \frac{1.42\text{ kJ}}{0.904\text{ kJ/mol}} \approx 1.571\text{ moles of }\text{H}_2
\]
The mass of liquid hydrogen boiled off is:
\[
m_{\text{boiled}} = n_{\text{boiled}} \times M(\text{H}_2) = 1.571\text{ mol} \times 2.016\text{ g/mol} \approx 3.17\text{ grams}
\]
Because \(\Delta H_{\text{conv}} > \Delta H_{\text{vap}}\), every single mole of ortho-\(\text{H}_2\) that relaxes inside a cryogenic tank boils off more than 1.5 moles of liquid hydrogen! This underscores why industrial rocket propellants (such as liquid hydrogen for Saturn V and SLS) mandate complete catalytic para-conversion during liquefaction."""
            },
            "unit-9": {
                "id": "prob-9-9",
                "title": "Thermodynamic Functions (U, H, S, G) of Carbon Dioxide",
                "problem": r"""For carbon dioxide (\(\text{CO}_2\), \(M = 44.01\text{ g/mol}\)) at \(T = 500.0\text{ K}\) and \(P^\circ = 1.00\text{ bar}\):
Spectroscopic constants:
- Rotational constant: \(B = 0.3902\text{ cm}^{-1}\), \(\sigma = 2\)
- Vibrational wavenumbers: \(\tilde{\nu}_1 = 1388\text{ cm}^{-1}\), \(\tilde{\nu}_2 = 667\text{ cm}^{-1}\) (doubly degenerate), \(\tilde{\nu}_3 = 2349\text{ cm}^{-1}\)
- Electronic ground state: \(^1\Sigma_g^+\) (\(g_e = 1\))
1. Calculate the translational, rotational, and vibrational contributions to molar internal energy \(U_m^\circ - U_m^\circ(0)\) in \(\text{kJ/mol}\).
2. Calculate the standard molar enthalpy \(H_m^\circ - H_m^\circ(0)\).
3. Compute the standard molar entropy \(S_m^\circ\) at \(500\text{ K}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Internal Energy Contributions at \(500.0\text{ K}\)
Given \(R = 8.31446\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\) and \(T = 500.0\text{ K}\):
\[
R T = 8.31446 \times 500 = 4157.23\text{ J/mol} = 4.1572\text{ kJ/mol}
\]
1. **Translation (3 quadratic degrees of freedom):**
   \[
   U_{\text{trans}} = \frac{3}{2} R T = 1.5 \times 4.1572 \approx 6.2358\text{ kJ/mol}
   \]
2. **Rotation (Linear molecule, 2 quadratic degrees of freedom):**
   Since \(T = 500\text{ K} \gg \theta_{\text{rot}} \approx 0.56\text{ K}\):
   \[
   U_{\text{rot}} = R T = 4.1572\text{ kJ/mol}
   \]
3. **Vibration (Harmonic oscillator thermal energies \(U_{\text{vib}} = \sum g_i \frac{R \theta_i}{e^{\theta_i / T} - 1}\)):**
   - Mode 1 (\(\tilde{\nu}_1 = 1388\text{ cm}^{-1} \implies \theta_1 = 1997\text{ K}\)):
     \(x_1 = 1997 / 500 = 3.994 \implies e^{3.994} \approx 54.27 \implies e^{x_1} - 1 \approx 53.27\)
     \[
     U_{\text{vib}, 1} = \frac{R (1997)}{53.27} = \frac{16604}{53.27} \approx 311.7\text{ J/mol} = 0.3117\text{ kJ/mol}
     \]
   - Mode 2 (Bending, \(\tilde{\nu}_2 = 667\text{ cm}^{-1} \implies \theta_2 = 960\text{ K}\), degeneracy \(g_2 = 2\)):
     \(x_2 = 960 / 500 = 1.920 \implies e^{1.920} \approx 6.821 \implies e^{x_2} - 1 \approx 5.821\)
     \[
     U_{\text{vib}, 2} = 2 \times \frac{R (960)}{5.821} = 2 \times \frac{7981.9}{5.821} \approx 2742.4\text{ J/mol} = 2.7424\text{ kJ/mol}
     \]
   - Mode 3 (\(\tilde{\nu}_3 = 2349\text{ cm}^{-1} \implies \theta_3 = 3380\text{ K}\)):
     \(x_3 = 3380 / 500 = 6.760 \implies e^{6.760} \approx 862.6\)
     \[
     U_{\text{vib}, 3} = \frac{R (3380)}{861.6} \approx 32.6\text{ J/mol} = 0.0326\text{ kJ/mol}
     \]
   Total vibrational thermal energy:
   \[
   U_{\text{vib}} = 0.3117 + 2.7424 + 0.0326 \approx 3.0867\text{ kJ/mol}
   \]
Total internal energy relative to \(0\text{ K}\):
\[
U_m^\circ(500\text{ K}) - U_m^\circ(0) = 6.2358 + 4.1572 + 3.0867 = 13.4797\text{ kJ/mol} \approx 13.48\text{ kJ/mol}
\]

---

#### Step 2: Standard Molar Enthalpy
For an ideal gas, \(H = U + P V = U + R T\):
\[
H_m^\circ(500\text{ K}) - H_m^\circ(0) = [U_m^\circ(500\text{ K}) - U_m^\circ(0)] + R T
\]
\[
H_m^\circ(500\text{ K}) - H_m^\circ(0) = 13.4797 + 4.1572 \approx 17.637\text{ kJ/mol} \approx 17.64\text{ kJ/mol}
\]

---

#### Step 3: Standard Molar Entropy \(S_m^\circ\) at \(500\text{ K}\)
1. **Translational entropy (Sackur-Tetrode):**
   For \(\text{CO}_2\) (\(M = 44.01\text{ g/mol}\)) at \(500\text{ K}, 1\text{ bar}\):
   \[
   S_{\text{trans}}^\circ = R \left[ \frac{3}{2}\ln(44.01) + \frac{5}{2}\ln(500) - \ln(1) - 1.1517 \right]
   \]
   - \(\frac{3}{2}\ln(44.01) = 1.5(3.7844) \approx 5.6766\)
   - \(\frac{5}{2}\ln(500) = 2.5(6.2146) \approx 15.5365\)
   - Bracket sum: \(5.6766 + 15.5365 - 1.1517 = 20.0614\)
   \[
   S_{\text{trans}}^\circ = 8.31446 \times 20.0614 \approx 166.80\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]
2. **Rotational entropy:**
   \[
   \theta_{\text{rot}} = 1.43878 \times 0.3902 \approx 0.5614\text{ K}
   \]
   \[
   q_{\text{rot}} = \frac{T}{\sigma \theta_{\text{rot}}} = \frac{500}{2 \times 0.5614} \approx 445.3
   \]
   \[
   S_{\text{rot}}^\circ = R [\ln(q_{\text{rot}}) + 1] = 8.31446 [\ln(445.3) + 1] = 8.31446 [6.0988 + 1] = 8.31446 \times 7.0988 \approx 59.02\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]
3. **Vibrational entropy:**
   From \(S_{\text{vib}} = \sum g_i R \left[ \frac{x_i}{e^{x_i} - 1} - \ln(1 - e^{-x_i}) \right]\):
   - Mode 1 (\(x_1 = 3.994\)): \(R [0.075 + 0.019] \approx 0.78\text{ J/mol}\cdot\text{K}\)
   - Mode 2 (bending, \(g_2 = 2, x_2 = 1.920\)): \(2 R [0.330 + 0.158] = 2(8.3145)(0.488) \approx 8.12\text{ J/mol}\cdot\text{K}\)
   - Mode 3 (\(x_3 = 6.760\)): \(\approx 0.08\text{ J/mol}\cdot\text{K}\)
   \[
   S_{\text{vib}}^\circ \approx 0.78 + 8.12 + 0.08 \approx 8.98\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]
Total standard molar entropy:
\[
S_m^\circ = S_{\text{trans}}^\circ + S_{\text{rot}}^\circ + S_{\text{vib}}^\circ = 166.80 + 59.02 + 8.98 \approx 234.80\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]
The statistical value matches the NIST-JANAF thermochemical tables (\(S_m^\circ = 234.8\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\)) with flawless accuracy."""
        },
        "unit-10": {
            "id": "prob-10-9",
            "title": "Specific Heat of High-Tc Cuprates and d-Wave Pairing Symmetry",
            "problem": r"""Unlike conventional s-wave BCS superconductors which possess an isotropic energy gap \(\Delta_0\), high-temperature cuprate superconductors (such as \(\text{YBa}_2\text{Cu}_3\text{O}_{7-\delta}\)) exhibit **\(d_{x^2-y^2}\) pairing symmetry**:
\[
\Delta(\mathbf{k}) = \Delta_0 \cos(2\phi)
\]
which has line nodes at \(\phi = \pm \pi/4, \pm 3\pi/4\) where the gap vanishes identically.
1. Contrast the electronic density of states \(N(E)\) near the Fermi energy for an isotropic s-wave gap versus a nodal d-wave gap.
2. For an isotropic s-wave superconductor, prove that the low-temperature electronic heat capacity exhibits exponential activation: \(C_{\text{elec}} \propto e^{-\Delta_0 / k_B T}\).
3. For a d-wave superconductor with line nodes, show that the low-temperature electronic heat capacity follows a power law: \(C_{\text{elec}} \propto T^2\), and explain how cryogenic calorimetry confirms d-wave symmetry.""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Quasiparticle Density of States Comparison
1. **Conventional s-wave Gap (BCS):**
   The energy gap \(\Delta(\mathbf{k}) = \Delta_0\) is constant everywhere across the entire Fermi surface.
   The density of states is:
   \[
   N(E) = \begin{cases} 0 & (E < \Delta_0) \\ N(0) \frac{E}{\sqrt{E^2 - \Delta_0^2}} & (E > \Delta_0) \end{cases}
   \]
   There are strictly zero states inside the gap (\(|E| < \Delta_0\)).
2. **High-\(T_c\) d-wave Gap:**
   \(\Delta(\phi) = \Delta_0 \cos(2\phi)\).
   At the nodal points where \(\cos(2\phi) = 0\) (\(\phi = \pm 45^\circ, \pm 135^\circ\)), the gap closes to zero.
   Linearizing \(\Delta(\phi) \approx 2\Delta_0 \delta\phi\) near the nodes, the density of states grows linearly with energy:
   \[
   N(E) \propto \frac{N(0)}{\Delta_0} E \quad (\text{for } E \ll \Delta_0)
   \]
   There is no true full spectral gap; low-energy nodal quasiparticles exist down to \(T = 0\text{ K}\).

---

#### Step 2: Exponential Heat Capacity in s-Wave Superconductors
In an isotropic s-wave superconductor, thermally exciting a quasiparticle requires overcoming the finite threshold energy \(\Delta_0\).
The internal energy at \(T \ll T_c\) is:
\[
U_{\text{elec}}(T) \approx 2 \int_{\Delta_0}^\infty E N(E) e^{-E / k_B T} dE \propto e^{-\Delta_0 / k_B T}
\]
Differentiating with respect to temperature:
\[
C_{\text{elec}} = \frac{dU}{dT} \approx A k_B \left( \frac{\Delta_0}{k_B T} \right)^{5/2} e^{-\Delta_0 / k_B T}
\]
The electronic heat capacity vanishes exponentially fast as \(T \rightarrow 0\), because thermal fluctuations lack sufficient energy to cross the forbidden gap.

---

#### Step 3: Power-Law \(T^2\) Heat Capacity in d-Wave Superconductors
In a d-wave superconductor, the density of states is linear: \(N(E) = c E\).
The thermal energy of the nodal quasiparticles is:
\[
U_{\text{elec}}(T) = \int_0^\infty E N(E) \frac{1}{e^{E / k_B T} + 1} dE = c \int_0^\infty \frac{E^2}{e^{E / k_B T} + 1} dE
\]
Let \(x = E / k_B T \implies E = x k_B T\):
\[
U_{\text{elec}}(T) = c (k_B T)^3 \int_0^\infty \frac{x^2}{e^x + 1} dx = c (k_B T)^3 \left( \frac{3}{2} \zeta(3) \right) \propto T^3
\]
Differentiating with respect to temperature gives the electronic heat capacity:
\[
C_{\text{elec}}(T) = \frac{dU}{dT} \propto T^2
\]
**Calorimetric Confirmation:**
- If a superconductor were s-wave, a plot of \(\ln C_{\text{elec}}\) vs \(1/T\) would be a straight line with slope \(-\Delta_0 / k_B\).
- In high-\(T_c\) cuprates like \(\text{YBa}_2\text{Cu}_3\text{O}_{7-\delta}\), cryogenic specific heat measurements down to \(100\text{ mK}\) reveal a distinct \(C_{\text{elec}} = \alpha T^2\) power-law behavior.
This quadratic temperature dependence provided definitive thermodynamic proof of line nodes and \(d_{x^2-y^2}\) orbital pairing symmetry in high-temperature superconductivity."""
        }
    }
