import json

# ==============================================================================
# CHAPTER 7: QUANTUM THEORY OF SCATTERING: PARTIAL WAVES, BORN APPROXIMATION
# ==============================================================================
u7 = {
    "id": "unit7",
    "number": 7,
    "title": "Quantum Theory of Scattering: Partial Waves, Born Approximation & Green's Functions",
    "subtitle": "Cross-Sections, Partial Wave Phase Shifts, Optical Theorem, Breit-Wigner Resonances, Lippmann-Schwinger Equation & Born Series",
    "description": "Comprehensive mathematical foundation of quantum scattering theory: laboratory and center-of-mass kinematics, differential and total scattering cross-sections, the asymptotic wave function, partial wave expansion for central potentials, spherical Bessel/Neumann functions, phase shifts, the optical theorem, low-energy s-wave scattering length, hard-sphere scattering, Breit-Wigner resonance theory, the S-matrix, Green's function techniques, the Lippmann-Schwinger integral equation, and first/second Born approximations applied to Yukawa and Coulomb potentials.",
    "sections": [
        {
            "id": "sec7-1",
            "title": "Kinematics & Geometry of Scattering: Laboratory vs CM Frames & Cross-Sections",
            "content": r"""
<h3>1. Asymptotic Wavefunction and the Scattering Amplitude</h3>
<p>
Consider a beam of monoenergetic particles of mass $m$ and incident wavevector $\vec{k} = k\hat{z}$ ($E = \frac{\hbar^2 k^2}{2m}$) incident upon a localized scattering potential $V(\vec{r})$ of finite range $a$. In the asymptotic region far from the scattering center ($r \gg a$), the stationary scattering wavefunction $\psi(\vec{r})$ is an exact superposition of the incident plane wave and an outgoing spherical wave:
</p>
$$\psi(\vec{r}) \xrightarrow{r \to \infty} e^{ikz} + f(\theta, \phi)\frac{e^{ikr}}{r}$$
<p>
where $f(\theta, \phi)$ is the <strong>scattering amplitude</strong> having dimensions of length.
</p>

<h3>2. Differential and Total Scattering Cross-Sections</h3>
<p>
The incident probability current density is:
</p>
$$\vec{J}_{\text{inc}} = \frac{\hbar}{2mi}\left(\psi_{\text{inc}}^* \nabla \psi_{\text{inc}} - \psi_{\text{inc}} \nabla \psi_{\text{inc}}^*\right) = \frac{\hbar k}{m}\hat{z} = v\hat{z}$$
<p>
The outgoing scattered radial current density into solid angle $d\Omega = \sin\theta\,d\theta\,d\phi$ through surface element $dA = r^2 d\Omega$ is:
</p>
$$J_{\text{scatt}, r} = \frac{\hbar}{2mi}\left(\psi_{\text{scatt}}^* \frac{\partial}{\partial r}\psi_{\text{scatt}} - \psi_{\text{scatt}} \frac{\partial}{\partial r}\psi_{\text{scatt}}^*\right) = \frac{\hbar k}{m}\frac{|f(\theta, \phi)|^2}{r^2} = v \frac{|f(\theta, \phi)|^2}{r^2}$$
<p>
The <strong>differential cross-section</strong> $\frac{d\sigma}{d\Omega}$ is defined as the number of particles scattered into solid angle $d\Omega$ per unit time, divided by the incident flux $J_{\text{inc}}$:
</p>
$$\frac{d\sigma}{d\Omega} \equiv \frac{J_{\text{scatt}, r} r^2 d\Omega}{J_{\text{inc}} d\Omega} = |f(\theta, \phi)|^2$$
<p>
The <strong>total scattering cross-section</strong> $\sigma_{\text{tot}}$ is the integral over all solid angles:
</p>
$$\sigma_{\text{tot}} = \int_{4\pi} \frac{d\sigma}{d\Omega}\,d\Omega = \int_0^{2\pi} d\phi \int_0^\pi |f(\theta, \phi)|^2 \sin\theta\,d\theta$$

<h3>3. Laboratory vs Center-of-Mass (CM) Frame Kinematics</h3>
<p>
For a projectile of mass $m_1$ striking a target particle of mass $m_2$ initially at rest in the Laboratory frame:
</p>
$$\tan\theta_{\text{lab}} = \frac{\sin\theta_{\text{cm}}}{\cos\theta_{\text{cm}} + \gamma_m}, \quad \gamma_m \equiv \frac{m_1}{m_2}$$
<p>
The differential cross-sections relate by:
</p>
$$\left(\frac{d\sigma}{d\Omega}\right)_{\text{lab}} = \left(\frac{d\sigma}{d\Omega}\right)_{\text{cm}} \frac{(1 + 2\gamma_m\cos\theta_{\text{cm}} + \gamma_m^2)^{3/2}}{|1 + \gamma_m\cos\theta_{\text{cm}}|}$$
"""
        },
        {
            "id": "sec7-2",
            "title": "Partial Wave Analysis for Central Potentials: Radial Solutions & Phase Shifts",
            "content": r"""
<h3>1. Partial Wave Expansion</h3>
<p>
For a spherically symmetric potential $V(r) = V(|\vec{r}|)$, angular momentum $\vec{L}$ is conserved, and the scattering amplitude exhibits azimuthal symmetry: $f(\theta, \phi) = f(\theta)$. We can expand both the incident plane wave and the scattering wavefunction in terms of Legendre polynomials $P_l(\cos\theta)$:
</p>
$$e^{ikz} = e^{ikr\cos\theta} = \sum_{l=0}^\infty i^l (2l+1) j_l(kr) P_l(\cos\theta)$$
<p>
where $j_l(kr)$ are the spherical Bessel functions. Using the asymptotic identity $j_l(\rho) \xrightarrow{\rho\to\infty} \frac{\sin(\rho - l\pi/2)}{\rho}$:
</p>
$$e^{ikz} \xrightarrow{r\to\infty} \sum_{l=0}^\infty i^l (2l+1) \frac{\sin(kr - l\pi/2)}{kr} P_l(\cos\theta) = \sum_{l=0}^\infty \frac{2l+1}{2ik r}\left[ e^{ikr} - (-1)^l e^{-ikr} \right] P_l(\cos\theta)$$

<h3>2. Radial Phase Shifts $\delta_l(k)$</h3>
<p>
In the presence of the potential $V(r)$, the asymptotic radial wavefunction undergoes a phase shift $\delta_l(k)$ relative to the free spherical Bessel function:
</p>
$$R_l(r) \xrightarrow{r\to\infty} A_l \frac{\sin(kr - l\pi/2 + \delta_l)}{kr}$$
<p>
The total asymptotic wavefunction becomes:
</p>
$$\psi(\vec{r}) \xrightarrow{r\to\infty} \sum_{l=0}^\infty i^l (2l+1) e^{i\delta_l} \frac{\sin(kr - l\pi/2 + \delta_l)}{kr} P_l(\cos\theta)$$
<p>
Subtracting the incident plane wave $e^{ikz}$ from $\psi(\vec{r})$ and equating the coefficient of $\frac{e^{ikr}}{r}$ yields the exact <strong>partial wave expansion of the scattering amplitude</strong>:
</p>
$$f(\theta) = \sum_{l=0}^\infty (2l+1) f_l(k) P_l(\cos\theta)$$
<p>
where the $l$-th partial wave amplitude $f_l(k)$ is:
</p>
$$f_l(k) = \frac{e^{2i\delta_l} - 1}{2ik} = \frac{e^{i\delta_l}\sin\delta_l}{k} = \frac{1}{k(\cot\delta_l - i)}$$
"""
        },
        {
            "id": "sec7-3",
            "title": "The Optical Theorem, Low-Energy Scattering & Effective Range Expansion",
            "content": r"""
<h3>1. The Optical Theorem</h3>
<p>
Integrating $|f(\theta)|^2$ over the sphere and using the orthogonality of Legendre polynomials $\int_{-1}^1 P_l(u) P_{l'}(u)\,du = \frac{2}{2l+1}\delta_{ll'}$:
</p>
$$\sigma_{\text{tot}} = 2\pi \int_0^\pi |f(\theta)|^2 \sin\theta\,d\theta = \frac{4\pi}{k^2}\sum_{l=0}^\infty (2l+1)\sin^2\delta_l$$
<p>
Evaluating the forward scattering amplitude at $\theta = 0$ (where $P_l(1) = 1$):
</p>
$$f(0) = \frac{1}{k}\sum_{l=0}^\infty (2l+1) e^{i\delta_l}\sin\delta_l = \frac{1}{k}\sum_{l=0}^\infty (2l+1)(\cos\delta_l\sin\delta_l + i\sin^2\delta_l)$$
<p>
Taking the imaginary part:
</p>
$$\text{Im}[f(0)] = \frac{1}{k}\sum_{l=0}^\infty (2l+1)\sin^2\delta_l = \frac{k}{4\pi}\sigma_{\text{tot}}$$
<p>
This is the celebrated <strong>Optical Theorem</strong>:
</p>
$$\sigma_{\text{tot}} = \frac{4\pi}{k}\text{Im}[f(0)]$$
<p>
It expresses conservation of probability: the total scattered flux equals the quantum interference depletion of the forward beam (the "shadow" cast by the scatterer).
</p>

<h3>2. Low-Energy Scattering Length & Effective Range</h3>
<p>
As the incident energy approaches zero ($k \to 0$), centrifugal barrier terms $\frac{\hbar^2 l(l+1)}{2mr^2}$ suppress all higher partial waves ($l \ge 1$): $\delta_l \propto k^{2l+1}$. Only the $s$-wave ($l = 0$) contributes:
</p>
$$\lim_{k\to 0} k\cot\delta_0 = -\frac{1}{a_0} + \frac{1}{2}r_0 k^2 + \mathcal{O}(k^4)$$
<p>
where $a_0$ is the <strong>scattering length</strong> and $r_0$ is the <strong>effective range</strong>.
</p>
<p>
In the extreme low-energy limit ($k \to 0$):
</p>
$$f_0 \to \frac{1}{-1/a_0 - ik} \to -a_0 \implies \sigma_{\text{tot}} = 4\pi a_0^2$$
<p>
The scattering is completely isotropic ($d\sigma/d\Omega = a_0^2$).
</p>
"""
        },
        {
            "id": "sec7-4",
            "title": "Applications: Hard Sphere, Square Well, Ramsauer-Townsend & Breit-Wigner Resonances",
            "content": r"""
<h3>1. Hard Sphere Scattering</h3>
<p>
Consider a hard sphere of radius $a$: $V(r) = \infty$ for $r \le a$, and $V(r) = 0$ for $r > a$. The radial wavefunction must vanish at $r = a$:
</p>
$$R_l(a) = 0 \implies j_l(ka)\cos\delta_l - n_l(ka)\sin\delta_l = 0 \implies \tan\delta_l = \frac{j_l(ka)}{n_l(ka)}$$
<p>
For low energy ($ka \ll 1$), considering $l = 0$:
</p>
$$\tan\delta_0 = \frac{\sin(ka)}{-\cos(ka)} = -\tan(ka) \implies \delta_0 = -ka$$
<p>
The scattering length is $a_0 = -\lim_{k\to 0}\frac{\tan\delta_0}{k} = a$. The low-energy cross-section is:
</p>
$$\sigma_{\text{tot}} = 4\pi a^2$$
<p>
<strong>Key Physical Insight:</strong> The quantum total cross section $\sigma = 4\pi a^2$ is exactly <em>four times</em> the classical geometric cross-section $\sigma_{\text{class}} = \pi a^2$! The factor of 4 arises from wave diffraction around the shadow edge (the optical theorem).
</p>

<h3>2. The Ramsauer-Townsend Effect</h3>
<p>
For scattering by an attractive square well of depth $V_0$, as the energy varies, the phase shift $\delta_0$ may pass through integer multiples of $\pi$ ($\delta_0 = n\pi$). When this occurs, $\sin\delta_0 = 0 \implies \sigma_0 \approx 0$. At specific low electron energies ($\approx 0.7\text{ eV}$ in noble gases like Argon and Krypton), the scattering cross-section vanishes, making the gas effectively transparent to electrons—the <strong>Ramsauer-Townsend effect</strong>.
</p>

<h3>3. Breit-Wigner Resonance Scattering</h3>
<p>
When the incident particle energy $E$ matches a quasi-bound state energy $E_R$ inside a potential well surrounded by a barrier, the phase shift $\delta_l$ increases rapidly by $\pi$, passing through $\pi/2$:
</p>
$$\delta_l(E) = \delta_{\text{bg}} + \arctan\left(\frac{\Gamma/2}{E_R - E}\right)$$
<p>
where $\Gamma$ is the resonance width. The partial wave cross-section displays a Lorentzian peak:
</p>
$$\sigma_l = \frac{4\pi}{k^2}(2l+1)\sin^2\delta_l = \frac{4\pi}{k^2}(2l+1)\frac{\Gamma^2/4}{(E - E_R)^2 + \Gamma^2/4}$$
<p>
The resonance width $\Gamma$ is directly related to the lifetime $\tau$ of the decaying quasi-bound state by the time-energy uncertainty relation: $\tau = \hbar / \Gamma$.
</p>
"""
        },
        {
            "id": "sec7-5",
            "title": "The S-Matrix, Unitarity & Bound States as Analytic Poles",
            "content": r"""
<h3>1. The Scattering Matrix (S-Matrix)</h3>
<p>
The asymptotic radial partial wave function can be decomposed into incoming and outgoing spherical waves:
</p>
$$R_l(r) \propto \frac{1}{2ikr}\left[ S_l(k) e^{i(kr - l\pi/2)} - e^{-i(kr - l\pi/2)} \right]$$
<p>
where the <strong>$S$-matrix element</strong> is defined by:
</p>
$$S_l(k) \equiv e^{2i\delta_l(k)}$$
<p>
Conservation of probability (elastic scattering) requires that the modulus of the outgoing flux equals the incoming flux:
</p>
$$|S_l(k)| = |e^{2i\delta_l}| = 1 \iff S_l^\dagger S_l = \hat{I}$$
<p>
This proves that the $S$-matrix is strictly <strong>unitary</strong>.
</p>

<h3>2. Analytic Continuation and Bound State Poles</h3>
<p>
Continuing the wavevector $k$ into the complex $k$-plane ($k \to \kappa = i\kappa_B$, with $\kappa_B > 0$):
</p>
$$e^{ikr} = e^{i(i\kappa_B)r} = e^{-\kappa_B r}$$
<p>
For a true bound state, the wavefunction must decay exponentially as $r \to \infty$ without any incoming flux. In the complex $k$-plane, bound states of the Hamiltonian correspond precisely to simple <strong>poles of the $S$-matrix on the positive imaginary axis</strong> ($k = i\kappa_B$), with binding energy:
</p>
$$E_{\text{bound}} = \frac{\hbar^2 k^2}{2m} = -\frac{\hbar^2 \kappa_B^2}{2m} < 0$$
<p>
Resonances correspond to poles in the lower half of the complex $k$-plane at $k = k_R - i\frac{\gamma}{2}$.
</p>
"""
        },
        {
            "id": "sec7-6",
            "title": "Green's Function Formalism & The Lippmann-Schwinger Integral Equation",
            "content": r"""
<h3>1. The Inhomogeneous Helmholtz Equation</h3>
<p>
The stationary Schrödinger equation can be rewritten as an inhomogeneous Helmholtz differential equation:
</p>
$$\left(\nabla^2 + k^2\right)\psi(\vec{r}) = U(\vec{r})\psi(\vec{r}), \quad U(\vec{r}) \equiv \frac{2m}{\hbar^2}V(\vec{r})$$
<p>
The free-particle Green's function $G_0(\vec{r}, \vec{r}')$ satisfies:
</p>
$$\left(\nabla^2 + k^2\right)G_0(\vec{r}, \vec{r}') = \delta^3(\vec{r} - \vec{r}')$$
<p>
Imposing the boundary condition of outgoing spherical waves at infinity selects the causal Green's function $G_0^+(\vec{r}, \vec{r}')$:
</p>
$$G_0^+(\vec{r}, \vec{r}') = -\frac{1}{4\pi}\frac{e^{ik|\vec{r} - \vec{r}'|}}{|\vec{r} - \vec{r}'|}$$

<h3>2. The Lippmann-Schwinger Equation</h3>
<p>
Integrating using Green's identity converts the differential Schrödinger equation into the exact <strong>Lippmann-Schwinger integral equation</strong>:
</p>
$$\psi(\vec{r}) = \phi_{\text{inc}}(\vec{r}) + \int G_0^+(\vec{r}, \vec{r}') U(\vec{r}') \psi(\vec{r}')\,d^3r'$$
$$\psi(\vec{r}) = e^{i\vec{k}\cdot\vec{r}} - \frac{m}{2\pi\hbar^2}\int \frac{e^{ik|\vec{r} - \vec{r}'|}}{|\vec{r} - \vec{r}'|} V(\vec{r}') \psi(\vec{r}')\,d^3r'$$
<p>
In the asymptotic limit $r \gg r'$:
</p>
$$|\vec{r} - \vec{r}'| \approx r - \hat{r}\cdot\vec{r}', \quad \frac{e^{ik|\vec{r} - \vec{r}'|}}{|\vec{r} - \vec{r}'|} \approx \frac{e^{ikr}}{r} e^{-i\vec{k}'\cdot\vec{r}'}$$
<p>
where $\vec{k}' \equiv k\hat{r}$ is the scattered wavevector. Comparing with $\psi \to e^{i\vec{k}\cdot\vec{r}} + f(\theta, \phi)\frac{e^{ikr}}{r}$ yields the exact expression for the scattering amplitude:
</p>
$$f(\theta, \phi) = -\frac{m}{2\pi\hbar^2}\int e^{-i\vec{k}'\cdot\vec{r}'} V(\vec{r}') \psi(\vec{r}')\,d^3r'$$
"""
        },
        {
            "id": "sec7-7",
            "title": "The Born Series & Born Approximations: Yukawa & Coulomb Potentials",
            "content": r"""
<h3>1. The Born Series Expansion</h3>
<p>
Iteratively substituting the Lippmann-Schwinger equation into itself generates the <strong>Neumann-Born series</strong>:
</p>
$$\psi = \phi + \hat{G}_0 \hat{V}\phi + \hat{G}_0 \hat{V}\hat{G}_0 \hat{V}\phi + \dots$$
<p>
The <strong>First Born Approximation</strong> replaces the unknown internal wavefunction $\psi(\vec{r}')$ inside the integral by the incident unperturbed plane wave $\phi(\vec{r}') = e^{i\vec{k}\cdot\vec{r}'}$:
</p>
$$f^{(1)}(\theta, \phi) = -\frac{m}{2\pi\hbar^2}\int e^{-i\vec{k}'\cdot\vec{r}'} V(\vec{r}') e^{i\vec{k}\cdot\vec{r}'}\,d^3r' = -\frac{m}{2\pi\hbar^2}\int V(\vec{r}') e^{i\vec{q}\cdot\vec{r}'}\,d^3r'$$
<p>
where $\vec{q} \equiv \vec{k} - \vec{k}'$ is the momentum transfer wavevector, with magnitude:
</p>
$$q = |\vec{k} - \vec{k}'| = 2k\sin\left(\frac{\theta}{2}\right)$$
<p>
Thus, the First Born scattering amplitude is proportional to the 3D spatial Fourier transform of the scattering potential evaluated at momentum transfer $\vec{q}$.
</p>
<p>
For a spherically symmetric potential $V(r)$:
</p>
$$f^{(1)}(\theta) = -\frac{2m}{\hbar^2 q}\int_0^\infty r V(r)\sin(qr)\,dr$$

<h3>2. Application to the Screened Coulomb (Yukawa) Potential</h3>
<p>
The Yukawa potential models the screened Coulomb or nuclear force:
</p>
$$V(r) = V_0 \frac{e^{-\mu r}}{r}$$
<p>
Evaluating the Fourier integral:
</p>
$$f^{(1)}(\theta) = -\frac{2m V_0}{\hbar^2 q}\int_0^\infty e^{-\mu r}\sin(qr)\,dr = -\frac{2m V_0}{\hbar^2 q}\left(\frac{q}{\mu^2 + q^2}\right) = -\frac{2m V_0}{\hbar^2(\mu^2 + q^2)}$$
<p>
Substituting $q^2 = 4k^2\sin^2(\theta/2)$:
</p>
$$\frac{d\sigma}{d\Omega} = |f^{(1)}(\theta)|^2 = \frac{4m^2 V_0^2}{\hbar^4\left[\mu^2 + 4k^2\sin^2(\theta/2)\right]^2}$$
<p>
Taking the unscreened Coulomb limit ($\mu \to 0$, $V_0 = \frac{z Z e^2}{4\pi\varepsilon_0}$):
</p>
$$\frac{d\sigma}{d\Omega} = \frac{4m^2}{\hbar^4}\left(\frac{z Z e^2}{4\pi\varepsilon_0}\right)^2 \frac{1}{16k^4\sin^4(\theta/2)} = \left(\frac{z Z e^2}{16\pi\varepsilon_0 E}\right)^2 \frac{1}{\sin^4(\theta/2)}$$
<p>
This recovers the classic <strong>Rutherford Scattering Formula</strong> identically!
</p>
"""
        }
    ],
    "simulations": [
        {
            "id": "qm2-partial-wave-scattering-sim",
            "title": "Interactive Partial Wave Phase Shifts & Differential Cross-Section",
            "description": "Visualizer for partial wave decomposition of central scattering, displaying radial functions, phase shifts δ₀, δ₁, δ₂, and angular differential cross-section dσ/dΩ(θ)."
        },
        {
            "id": "qm2-born-approximation-sim",
            "title": "Born Approximation Yukawa & Coulomb Scattering Visualizer",
            "description": "Interactive cross-section simulator for the Yukawa potential V(r) = V₀ e^(-μr)/r, demonstrating how screening parameter μ smoothly transitions into Rutherford scattering."
        }
    ],
    "solvedProblems": [
        {
            "number": 1,
            "title": "Low-Energy s-Wave Scattering by a Rigid Hard Sphere",
            "statement": r"A particle of mass $m$ and low momentum $\hbar k$ scatters from a hard sphere potential:\n$$V(r) = \begin{cases} \infty & \text{for } r \le a \\ 0 & \text{for } r > a \end{cases}$$\n(a) Solve the radial Schrödinger equation for $r > a$ for the $s$-wave ($l = 0$) and apply boundary conditions to find the exact phase shift $\delta_0(k)$.\n(b) In the low-energy limit $ka \ll 1$, deduce the scattering length $a_0$ and compute the total scattering cross-section $\sigma_{\text{tot}}$.\n(c) Explain physically why $\sigma_{\text{tot}} = 4\pi a^2$ is four times larger than the classical cross-section $\pi a^2$.",
            "solution": r"**(a) Deriving the Exact $s$-Wave Phase Shift:**\nFor $r > a$, $V(r) = 0$. The radial equation for $u_0(r) = r R_0(r)$ is:\n$$\frac{d^2 u_0}{dr^2} + k^2 u_0(r) = 0$$\nThe general solution is:\n$$u_0(r) = A \sin(kr + \delta_0)$$\nAt the hard sphere surface $r = a$, the infinite barrier imposes the boundary condition $u_0(a) = 0$:\n$$\sin(ka + \delta_0) = 0 \implies ka + \delta_0 = 0 \implies \delta_0(k) = -ka$$\n\n**(b) Low-Energy Cross-Section:**\nFor $ka \ll 1$, centrifugal forces suppress all higher partial waves ($l \ge 1$):\n$$\delta_l \sim (ka)^{2l+1} \ll \delta_0$$\nThe $s$-wave scattering amplitude is:\n$$f_0(k) = \frac{e^{i\delta_0}\sin\delta_0}{k} = \frac{e^{-ika}\sin(-ka)}{k} \xrightarrow{k\to 0} \frac{1(-ka)}{k} = -a$$\nThe scattering length is:\n$$a_0 = -\lim_{k\to 0} \frac{\tan\delta_0}{k} = a$$\nThe total low-energy cross-section is:\n$$\sigma_{\text{tot}} = 4\pi |f_0|^2 = 4\pi a^2$$\n\n**(c) The Factor of 4 Paradox:**\nClassically, any particle with impact parameter $b \le a$ hits the sphere, giving a geometric shadow cross-section $\sigma_{\text{classical}} = \pi a^2$.\nIn quantum wave mechanics:\n1. The hard sphere directly deflects incoming waves by reflection, contributing an area $\pi a^2$.\n2. To produce a shadow behind the sphere in the forward direction, quantum interference must subtract the incident beam amplitude, causing forward diffraction around the perimeter of the sphere. This wave diffraction scatters an additional equal flux into small forward angles, contributing another $\pi a^2$.\nSumming reflection and diffraction gives $\sigma_{\text{quantum}} = \pi a^2 + \pi a^2 = 2\pi a^2$ in the high-energy limit ($ka \gg 1$), and precisely $4\pi a^2$ in the low-energy limit ($ka \ll 1$) where $s$-wave scattering is completely isotropic."
        },
        {
            "number": 2,
            "title": "Breit-Wigner Resonant Scattering and Metastable State Lifetime",
            "statement": r"A particle scatters in a central potential with an isolated narrow resonance at energy $E_R = 4.0\text{ MeV}$ with full width at half maximum $\Gamma = 0.2\text{ MeV}$ in the $d$-wave channel ($l = 2$).\n(a) Write down the Breit-Wigner parameterization for the resonant phase shift $\delta_2(E)$ and the partial wave cross-section $\sigma_2(E)$.\n(b) Compute the peak cross-section $\sigma_2(E_R)$ if the incident particle is a proton ($m_p \approx 1.67 \times 10^{-27}\text{ kg}$).\n(c) Calculate the lifetime $\tau$ of the formed resonance state.",
            "solution": r"**(a) Breit-Wigner Cross-Section:**\nThe resonant phase shift is:\n$$\delta_2(E) = \arctan\left(\frac{\Gamma/2}{E_R - E}\right)$$\n$$\sin^2\delta_2 = \frac{\Gamma^2/4}{(E - E_R)^2 + \Gamma^2/4}$$\nThe partial cross-section for $l = 2$ ($2l+1 = 5$) is:\n$$\sigma_2(E) = \frac{4\pi}{k^2}(2l+1)\sin^2\delta_2 = \frac{20\pi}{k^2}\frac{\Gamma^2/4}{(E - E_R)^2 + \Gamma^2/4}$$\n\n**(b) Peak Cross-Section at $E = E_R$:**\nAt resonance ($E = E_R$), $\sin^2\delta_2 = 1$:\n$$\sigma_2(E_R) = \frac{20\pi}{k^2}$$\nThe wavenumber $k$ at $E_R = 4.0\text{ MeV} = 6.408 \times 10^{-13}\text{ J}$ is:\n$$k = \frac{\sqrt{2m_p E_R}}{\hbar} = \frac{\sqrt{2(1.6726 \times 10^{-27})(6.408 \times 10^{-13})}}{1.0546 \times 10^{-34}} \approx \frac{4.63 \times 10^{-20}}{1.0546 \times 10^{-34}} \approx 4.39 \times 10^{14}\text{ m}^{-1}$$\nEvaluating the peak cross-section:\n$$\sigma_2(E_R) = \frac{20\pi}{(4.39 \times 10^{14})^2} \approx \frac{62.83}{1.927 \times 10^{29}} \approx 3.26 \times 10^{-28}\text{ m}^2 = 3.26\text{ barns}$$\n\n**(c) Lifetime of the Resonant State:**\nUsing the time-energy uncertainty relation:\n$$\tau = \frac{\hbar}{\Gamma}$$\n$$\Gamma = 0.2\text{ MeV} = 3.204 \times 10^{-14}\text{ J}$$\n$$\tau = \frac{1.0546 \times 10^{-34}\text{ J}\cdot\text{s}}{3.204 \times 10^{-14}\text{ J}} \approx 3.29 \times 10^{-21}\text{ seconds}$$"
        },
        {
            "number": 3,
            "title": "First Born Approximation for the Yukawa Potential & Rutherford Limit",
            "statement": r"A particle of mass $m$ is scattered by a Yukawa potential $V(r) = V_0 \frac{e^{-\mu r}}{r}$.\n(a) Using the First Born approximation, derive the scattering amplitude $f(\theta)$ as a function of the momentum transfer $q = 2k\sin(\theta/2)$.\n(b) Calculate the differential cross-section $\frac{d\sigma}{d\Omega}$.\n(c) Take the zero-mass mediator limit $\mu \to 0$ and show that it reproduces the Rutherford scattering formula.",
            "solution": r"**(a) First Born Scattering Amplitude:**\n$$f^{(1)}(\theta) = -\frac{2m}{\hbar^2 q}\int_0^\infty r V(r)\sin(qr)\,dr$$\nSubstituting $V(r) = V_0 \frac{e^{-\mu r}}{r}$:\n$$r V(r) = V_0 e^{-\mu r}$$\n$$f^{(1)}(\theta) = -\frac{2m V_0}{\hbar^2 q}\int_0^\infty e^{-\mu r}\sin(qr)\,dr$$\nUsing the standard integral $\int_0^\infty e^{-\mu r}\sin(qr)\,dr = \frac{q}{\mu^2 + q^2}$:\n$$f^{(1)}(\theta) = -\frac{2m V_0}{\hbar^2 q}\left(\frac{q}{\mu^2 + q^2}\right) = -\frac{2m V_0}{\hbar^2(\mu^2 + q^2)}$$\n\n**(b) Differential Cross-Section:**\n$$\frac{d\sigma}{d\Omega} = |f^{(1)}(\theta)|^2 = \frac{4m^2 V_0^2}{\hbar^4(\mu^2 + q^2)^2}$$\nSubstituting $q^2 = 4k^2\sin^2(\theta/2)$:\n$$\frac{d\sigma}{d\Omega} = \frac{4m^2 V_0^2}{\hbar^4\left[\mu^2 + 4k^2\sin^2(\theta/2)\right]^2}$$\n\n**(c) The Rutherford Limit ($\mu \to 0$):**\nFor a Coulomb potential between charges $q_1 = z e$ and $q_2 = Z e$, $V_0 = \frac{z Z e^2}{4\pi\varepsilon_0}$.\nSetting $\mu = 0$:\n$$\frac{d\sigma}{d\Omega} = \frac{4m^2}{\hbar^4}\left(\frac{z Z e^2}{4\pi\varepsilon_0}\right)^2 \frac{1}{\left[4k^2\sin^2(\theta/2)\right]^2} = \frac{4m^2}{\hbar^4}\left(\frac{z Z e^2}{4\pi\varepsilon_0}\right)^2 \frac{1}{16k^4\sin^4(\theta/2)}$$\nSince $E = \frac{\hbar^2 k^2}{2m} \implies \hbar^2 k^2 = 2mE$:\n$$\frac{d\sigma}{d\Omega} = \frac{4m^2}{(2mE)^2}\left(\frac{z Z e^2}{4\pi\varepsilon_0}\right)^2 \frac{1}{16\sin^4(\theta/2)} = \left(\frac{z Z e^2}{16\pi\varepsilon_0 E}\right)^2 \frac{1}{\sin^4(\theta/2)}$$\nThis is precisely the classical Rutherford scattering cross-section!"
        }
    ]
}

# ==============================================================================
# CHAPTER 8: RELATIVISTIC QUANTUM MECHANICS: KLEIN-GORDON & DIRAC EQUATIONS
# ==============================================================================
u8 = {
    "id": "unit8",
    "number": 8,
    "title": "Relativistic Quantum Mechanics: Klein-Gordon & Dirac Formulations",
    "subtitle": "Covariant Wave Equations, Clifford Algebra, 4-Component Spinors, Spin-Orbit & Darwin Reductions, Hole Theory & Klein Paradox",
    "description": "Comprehensive mathematical synthesis of relativistic quantum wave mechanics: the breakdown of non-relativistic quantum mechanics, covariant four-vector notation, the Klein-Gordon equation and its historical negative probability crisis, the Dirac equation linearization, Dirac gamma matrices and the Clifford algebra, covariant conserved currents, free-particle positive and negative energy four-spinors, the natural emergence of electron spin s=1/2 and g=2, the Foldy-Wouthuysen non-relativistic reduction (systematically generating spin-orbit and Darwin corrections), Dirac sea hole theory, pair production, and the Klein tunneling paradox.",
    "sections": [
        {
            "id": "sec7-1_u8",
            "title": "Breakdown of Non-Relativistic QM, Four-Vectors & Covariant Notation",
            "content": r"""
<h3>1. The Incompatibility of Relativity and the Schrödinger Equation</h3>
<p>
The standard Schrödinger equation $i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi$ is fundamentally asymmetric: it contains a <em>first-order</em> derivative in time, but <em>second-order</em> derivatives in space. In special relativity, space and time are inextricably unified into spacetime coordinates $x^\mu = (ct, \vec{x})$. Any physical wave equation invariant under Lorentz transformations must treat space and time derivatives on an equal footing.
</p>

<h3>2. Four-Vector Kinematics and the Einstein Energy-Momentum Relation</h3>
<p>
Using natural covariant tensor notation with the Minkowski metric signature $\eta_{\mu\nu} = \text{diag}(+1, -1, -1, -1)$:
</p>
$$x^\mu = (x^0, x^1, x^2, x^3) = (ct, x, y, z), \quad x_\mu = \eta_{\mu\nu} x^\nu = (ct, -x, -y, -z)$$
$$p^\mu = (E/c, \vec{p}), \quad p_\mu = (E/c, -\vec{p})$$
<p>
The relativistic invariant scalar product of four-momentum is the rest mass shell constraint:
</p>
$$p^\mu p_\mu = \frac{E^2}{c^2} - \vec{p}^2 = m^2 c^2 \iff E^2 = \vec{p}^2 c^2 + m^2 c^4$$
<p>
Canonical quantum operator replacement maps four-momentum to four-gradient:
</p>
$$E \to i\hbar \frac{\partial}{\partial t}, \quad \vec{p} \to -i\hbar\nabla \iff \hat{p}^\mu = i\hbar\partial^\mu = i\hbar \left(\frac{1}{c}\frac{\partial}{\partial t}, -\nabla\right)$$
"""
        },
        {
            "id": "sec7-2_u8",
            "title": "The Klein-Gordon Equation: Conserved Current & The Negative Probability Crisis",
            "content": r"""
<h3>1. Derivation of the Klein-Gordon Equation</h3>
<p>
Applying canonical operator replacement directly to the relativistic energy-momentum invariant $E^2 - \vec{p}^2 c^2 = m^2 c^4$:
</p>
$$\left( -\hbar^2 \frac{\partial^2}{\partial t^2} + \hbar^2 c^2 \nabla^2 \right)\phi(\vec{r}, t) = m^2 c^4 \phi(\vec{r}, t)$$
$$\left( \frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2 + \frac{m^2 c^2}{\hbar^2} \right)\phi(\vec{r}, t) = 0 \iff \left(\Box + \frac{m^2 c^2}{\hbar^2}\right)\phi = 0$$
<p>
where $\Box \equiv \partial^\mu \partial_\mu = \frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2$ is the d'Alembertian operator. This is the <strong>Klein-Gordon equation</strong> (1926).
</p>

<h3>2. The Continuity Equation and Negative Probability Density</h3>
<p>
Multiplying the Klein-Gordon equation by $\phi^*$ and subtracting the complex conjugate equation multiplied by $\phi$:
</p>
$$\phi^* \frac{\partial^2\phi}{\partial t^2} - \phi \frac{\partial^2\phi^*}{\partial t^2} - c^2\left(\phi^* \nabla^2\phi - \phi \nabla^2\phi^*\right) = 0$$
$$\frac{\partial}{\partial t}\left[ \frac{i\hbar}{2mc^2}\left(\phi^* \frac{\partial\phi}{\partial t} - \phi \frac{\partial\phi^*}{\partial t}\right) \right] + \nabla\cdot\left[ -\frac{i\hbar}{2m}\left(\phi^* \nabla\phi - \phi \nabla\phi^*\right) \right] = 0$$
<p>
This defines the conserved four-current $\partial_\mu j^\mu = 0$ with probability density $\rho$:
</p>
$$\rho = \frac{i\hbar}{2mc^2}\left(\phi^* \frac{\partial\phi}{\partial t} - \phi \frac{\partial\phi^*}{\partial t}\right)$$
<p>
<strong>The Crisis:</strong> Because the Klein-Gordon equation is second order in time, both $\phi$ and $\frac{\partial\phi}{\partial t}$ can be chosen independently as initial Cauchy conditions. Consequently, $\rho$ can be <em>negative</em>! In 1928, this was viewed as a fatal defect for a single-particle probability density. (Later, Pauli and Weisskopf showed that the Klein-Gordon equation correctly describes spin-0 bosons like pions, with $\rho$ reinterpreted as electric charge density $j^0 = \rho_q$).
</p>
"""
        },
        {
            "id": "sec7-3_u8",
            "title": "The Dirac Equation: Linearization & The Clifford Algebra of Gamma Matrices",
            "content": r"""
<h3>1. Dirac's Linearization Postulate</h3>
<p>
To ensure a positive-definite probability density $\rho \ge 0$, Paul Dirac (1928) sought a relativistic wave equation that is strictly <strong>first order in time</strong>:
</p>
$$i\hbar \frac{\partial \psi}{\partial t} = \hat{H}_D \psi$$
<p>
For relativistic covariance, it must also be first order in spatial gradients:
</p>
$$\hat{H}_D = c(\vec{\alpha}\cdot\hat{\vec{p}}) + \beta m c^2 = -i\hbar c \sum_{k=1}^3 \alpha_k \frac{\partial}{\partial x_k} + \beta m c^2$$
<p>
Squaring the Hamiltonian $\hat{H}_D^2 \psi = -\hbar^2 \frac{\partial^2\psi}{\partial t^2}$ and requiring that every component of $\psi$ identically satisfies the relativistic dispersion relation $E^2 = p^2 c^2 + m^2 c^4$:
</p>
$$\hat{H}_D^2 = c^2 \sum_{j,k} \frac{1}{2}\{\alpha_j, \alpha_k\} p_j p_k + m c^3 \sum_k \{\alpha_k, \beta\} p_k + \beta^2 m^2 c^4 \equiv c^2 \vec{p}^2 + m^2 c^4$$

<h3>2. The Clifford Algebra</h3>
<p>
Equating coefficients yields the required algebraic conditions for the coefficients $\alpha_1, \alpha_2, \alpha_3, \beta$:
</p>
$$\{\alpha_j, \alpha_k\} = \alpha_j \alpha_k + \alpha_k \alpha_j = 2\delta_{jk}\hat{I}$$
$$\{\alpha_k, \beta\} = \alpha_k \beta + \beta \alpha_k = 0$$
$$\alpha_k^2 = \hat{I}, \quad \beta^2 = \hat{I}$$
<p>
Since $\alpha_k$ and $\beta$ anticommute, their eigenvalues must be $\pm 1$ and their traces must vanish ($\text{Tr}(\alpha_k) = \text{Tr}(\beta) = 0$). This requires their matrix dimension $N$ to be even. In $N = 2$, only three anticommuting matrices exist (the Pauli matrices). Thus, the minimal dimensionality is <strong>$N = 4$</strong>!
</p>

<h3>3. The Dirac-Pauli Representation and Gamma Matrices</h3>
<p>
In the standard Dirac-Pauli representation:
</p>
$$\vec{\alpha} = \begin{pmatrix} 0 & \vec{\sigma} \\ \vec{\sigma} & 0 \end{pmatrix}, \quad \beta = \begin{pmatrix} \hat{I}_{2\times 2} & 0 \\ 0 & -\hat{I}_{2\times 2} \end{pmatrix}$$
<p>
Multiplying the Dirac equation by $\beta / c$ and defining the covariant <strong>Dirac gamma matrices</strong>:
</p>
$$\gamma^0 \equiv \beta, \quad \vec{\gamma} \equiv \beta\vec{\alpha} \implies \gamma^\mu = (\beta, \beta\vec{\alpha})$$
$$\gamma^0 = \begin{pmatrix} \hat{I} & 0 \\ 0 & -\hat{I} \end{pmatrix}, \quad \gamma^k = \begin{pmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{pmatrix}$$
<p>
The gamma matrices satisfy the fundamental <strong>Clifford Algebra</strong>:
</p>
$$\{\gamma^\mu, \gamma^\nu\} = \gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2\eta^{\mu\nu}\hat{I}_{4\times 4}$$
<p>
The Dirac equation takes the elegant covariant form:
</p>
$$\left(i\hbar \gamma^\mu \partial_\mu - mc\right)\psi = 0 \iff (i\hbar \gamma^\mu \partial_\mu - mc)\psi = 0$$
"""
        },
        {
            "id": "sec7-4_u8",
            "title": "Covariance of the Dirac Equation & Conserved Probability Four-Current",
            "content": r"""
<h3>1. The Dirac Adjoint Spinor and Conserved Current</h3>
<p>
The Dirac wavefunction $\psi(x)$ is a 4-component column vector termed a <strong>Dirac bispinor</strong>. Taking the Hermitian conjugate of $(i\hbar\gamma^0\partial_0 + i\hbar\vec{\gamma}\cdot\nabla - mc)\psi = 0$:
</p>
$$-i\hbar \partial_0\psi^\dagger (\gamma^0)^\dagger - i\hbar \nabla\psi^\dagger\cdot(\vec{\gamma})^\dagger - mc\psi^\dagger = 0$$
<p>
Since $(\gamma^0)^\dagger = \gamma^0$ and $(\gamma^k)^\dagger = -\gamma^k$, multiplying from the right by $\gamma^0$ and using $\gamma^k\gamma^0 = -\gamma^0\gamma^k$:
</p>
$$i\hbar \partial_\mu \bar{\psi} \gamma^\mu + mc\bar{\psi} = 0$$
<p>
where the <strong>Dirac adjoint spinor</strong> is defined as:
</p>
$$\bar{\psi} \equiv \psi^\dagger \gamma^0$$
<p>
Combining the two equations:
</p>
$$\bar{\psi}(i\hbar\gamma^\mu\partial_\mu\psi) + (i\hbar\partial_\mu\bar{\psi}\gamma^\mu)\psi = i\hbar\partial_\mu(\bar{\psi}\gamma^\mu\psi) = 0$$
<p>
This defines the conserved probability four-current:
</p>
$$j^\mu \equiv c\bar{\psi}\gamma^\mu\psi, \quad \partial_\mu j^\mu = 0$$
<p>
The time component is the probability density:
</p>
$$\rho = \frac{j^0}{c} = \bar{\psi}\gamma^0\psi = \psi^\dagger (\gamma^0)^2 \psi = \psi^\dagger \psi = \sum_{a=1}^4 |\psi_a|^2 \ge 0$$
<p>
Dirac's formulation triumphantly resolves the negative probability crisis: $\rho$ is <strong>strictly positive-definite</strong>!
</p>
"""
        },
        {
            "id": "sec7-5_u8",
            "title": "Free Particle Solutions: Positive & Negative Energy 4-Spinors",
            "content": r"""
<h3>1. Plane Wave Ansatz and Spinor Decomposition</h3>
<p>
For a free particle with four-momentum $p^\mu = (E/c, \vec{p})$, we seek plane wave solutions:
</p>
$$\psi(x) = u(\vec{p}) e^{-ip\cdot x/\hbar} = \begin{pmatrix} \phi \\ \chi \end{pmatrix} e^{-i(Et - \vec{p}\cdot\vec{r})/\hbar}$$
<p>
where $\phi, \chi$ are two-component Pauli spinors. Substituting into the Dirac equation:
</p>
$$\begin{pmatrix} mc^2 & c\vec{\sigma}\cdot\vec{p} \\ c\vec{\sigma}\cdot\vec{p} & -mc^2 \end{pmatrix} \begin{pmatrix} \phi \\ \chi \end{pmatrix} = E \begin{pmatrix} \phi \\ \chi \end{pmatrix}$$
$$\implies (E - mc^2)\phi = c(\vec{\sigma}\cdot\vec{p})\chi$$
$$\implies (E + mc^2)\chi = c(\vec{\sigma}\cdot\vec{p})\phi$$

<h3>2. Positive Energy Solutions ($E = +E_p = +\sqrt{p^2 c^2 + m^2 c^4}$)</h3>
<p>
Expressing the lower spinor $\chi$ in terms of the upper spinor $\phi$:
</p>
$$\chi = \frac{c(\vec{\sigma}\cdot\vec{p})}{E_p + mc^2}\phi$$
<p>
For an electron at rest ($\vec{p} = 0$), $\chi = 0$, meaning $\phi$ represents the two familiar non-relativistic spin states (spin-up $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and spin-down $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$). The normalized positive-energy four-spinors are:
</p>
$$u^{(s)}(\vec{p}) = \sqrt{\frac{E_p + mc^2}{2mc^2}} \begin{pmatrix} \chi_s \\ \frac{c(\vec{\sigma}\cdot\vec{p})}{E_p + mc^2}\chi_s \end{pmatrix} \quad (s = 1, 2)$$

<h3>3. Negative Energy Solutions ($E = -E_p = -\sqrt{p^2 c^2 + m^2 c^4}$)</h3>
<p>
Setting $\psi(x) = v(\vec{p}) e^{+ip\cdot x/\hbar}$, the upper component $\phi$ becomes smaller than $\chi$:
</p>
$$\phi = \frac{c(\vec{\sigma}\cdot\vec{p})}{-E_p - mc^2}\chi = -\frac{c(\vec{\sigma}\cdot\vec{p})}{E_p + mc^2}\chi$$
$$v^{(s)}(\vec{p}) = \sqrt{\frac{E_p + mc^2}{2mc^2}} \begin{pmatrix} \frac{c(\vec{\sigma}\cdot\vec{p})}{E_p + mc^2}\chi_s' \\ \chi_s' \end{pmatrix} \quad (s = 1, 2)$$
<p>
There are exactly two positive-energy states and two negative-energy states for every momentum $\vec{p}$, representing the two spin orientations of particle and antiparticle.
</p>
"""
        },
        {
            "id": "sec7-6_u8",
            "title": "Electron Spin & Magnetic Moment: Minimal Coupling & The Natural g = 2 Factor",
            "content": r"""
<h3>1. Minimal Electromagnetic Coupling in the Dirac Equation</h3>
<p>
In the presence of an electromagnetic four-potential $A^\mu = (\Phi/c, \vec{A})$, canonical momentum is replaced by kinetic momentum:
</p>
$$p^\mu \to \pi^\mu = p^\mu - q A^\mu = p^\mu + e A^\mu \quad (q = -e)$$
<p>
The Dirac equation becomes:
</p>
$$i\hbar \frac{\partial \psi}{\partial t} = \left[ c\vec{\alpha}\cdot(\hat{\vec{p}} + e\vec{A}) + \beta m c^2 - e\Phi \right]\psi$$

<h3>2. The Non-Relativistic Limit: Recovery of the Pauli Equation</h3>
<p>
Writing $\psi = \begin{pmatrix} \phi \\ \chi \end{pmatrix} e^{-imc^2 t/\hbar}$ to separate out the fast rest-mass oscillation, the coupled equations for the large component $\phi$ and small component $\chi$ are:
</p>
$$i\hbar \frac{\partial \phi}{\partial t} = c\vec{\sigma}\cdot\vec{\Pi}\chi - e\Phi\phi$$
$$i\hbar \frac{\partial \chi}{\partial t} + 2mc^2\chi = c\vec{\sigma}\cdot\vec{\Pi}\phi - e\Phi\chi$$
<p>
In the non-relativistic limit ($|i\hbar\partial_t \chi| \ll 2mc^2\chi$ and $|e\Phi| \ll mc^2$):
</p>
$$\chi \approx \frac{\vec{\sigma}\cdot\vec{\Pi}}{2mc}\phi$$
<p>
Substituting $\chi$ back into the equation for $\phi$:
</p>
$$i\hbar \frac{\partial \phi}{\partial t} = \left[ \frac{(\vec{\sigma}\cdot\vec{\Pi})^2}{2m} - e\Phi \right]\phi$$
<p>
Using the Pauli identity $(\vec{\sigma}\cdot\vec{A})(\vec{\sigma}\cdot\vec{B}) = \vec{A}\cdot\vec{B} + i\vec{\sigma}\cdot(\vec{A}\times\vec{B})$:
</p>
$$(\vec{\sigma}\cdot\vec{\Pi})^2 = \vec{\Pi}^2 + i\vec{\sigma}\cdot(\vec{\Pi}\times\vec{\Pi}) = (\vec{p} + e\vec{A})^2 + i\vec{\sigma}\cdot(-i\hbar e\nabla \times \vec{A}) = (\vec{p} + e\vec{A})^2 + e\hbar(\vec{\sigma}\cdot\vec{B})$$
<p>
Substituting this result yields the famous <strong>Pauli Equation</strong>:
</p>
$$i\hbar \frac{\partial \phi}{\partial t} = \left[ \frac{(\vec{p} + e\vec{A})^2}{2m} + \frac{e\hbar}{2m}(\vec{\sigma}\cdot\vec{B}) - e\Phi \right]\phi$$

<h3>3. The Natural Gyromagnetic Factor $g = 2$</h3>
<p>
Notice the interaction term with the magnetic field:
</p>
$$\hat{H}_{\text{mag}} = \frac{e\hbar}{2m}(\vec{\sigma}\cdot\vec{B}) = \frac{e}{m}\left(\frac{\hbar}{2}\vec{\sigma}\right)\cdot\vec{B} = \frac{e}{m}(\vec{S}\cdot\vec{B}) = 2\left(\frac{e}{2m}\right)\vec{S}\cdot\vec{B} = -\vec{\mu}_s \cdot \vec{B}$$
<p>
where $\vec{\mu}_s = -g_s \frac{e}{2m}\vec{S}$. Dirac's theory proves that:
</p>
$$g_s = 2$$
<p>
In non-relativistic physics, $g=2$ had to be inserted as an ad-hoc empirical postulate. In Dirac's relativistic equation, **electron spin ($s=1/2$) and the anomalous gyromagnetic factor ($g=2$) emerge automatically and inevitably from the requirement of relativistic spacetime covariance!**
</p>
"""
        },
        {
            "id": "sec7-7_u8",
            "title": "Non-Relativistic Reduction: Foldy-Wouthuysen Transformation & Fine Structure",
            "content": r"""
<h3>1. Systematic Expansion Beyond Leading Order</h3>
<p>
To systematically decouple the positive and negative energy states to order $(v/c)^2$, one applies a canonical unitary transformation $\psi' = e^{i\hat{S}}\psi$, termed the <strong>Foldy-Wouthuysen (FW) transformation</strong>.
</p>
<p>
For an electron moving in a central electrostatic potential $V(r) = -e\Phi(r)$:
</p>
$$\hat{H}_{\text{FW}} = \beta\left(mc^2 + \frac{\vec{p}^2}{2m} - \frac{\vec{p}^4}{8m^3 c^2}\right) + V(r) + \frac{1}{2m^2 c^2}\frac{1}{r}\frac{dV}{dr}(\vec{L}\cdot\vec{S}) + \frac{\hbar^2}{8m^2 c^2}\nabla^2 V(r)$$

<h3>2. Rigorous Derivation of Fine Structure Terms</h3>
<p>
Restricting to the upper two-component spinor ($\beta \to +1$), the effective Hamiltonian reproduces the exact fine structure of hydrogen derived perturbatively in Chapter 3:
</p>
<ol>
  <li><strong>Relativistic Mass-Kinetic Correction:</strong> $\hat{H}_{\text{rel}} = -\frac{\vec{p}^4}{8m^3 c^2}$.</li>
  <li><strong>Spin-Orbit Interaction with Exact Thomas Precession:</strong>
    $$\hat{H}_{\text{SO}} = \frac{1}{2m^2 c^2}\frac{1}{r}\frac{dV}{dr}(\vec{L}\cdot\vec{S})$$
    The kinematic Thomas factor $1/2$ appears automatically without needing non-inertial frame arguments!
  </li>
  <li><strong>Darwin Term:</strong>
    $$\hat{H}_{\text{Darwin}} = \frac{\hbar^2}{8m^2 c^2}\nabla^2 V(r) = \frac{\hbar^2}{8m^2 c^2}\left(\frac{e^2}{\varepsilon_0}\delta^3(\vec{r})\right) = \frac{\pi\hbar^2 e^2}{2m^2 c^2(4\pi\varepsilon_0)}\delta^3(\vec{r})$$
  </li>
</ol>
"""
        },
        {
            "id": "sec7-8_u8",
            "title": "Hole Theory, Negative Energy Sea, Zitterbewegung & The Klein Paradox",
            "content": r"""
<h3>1. Dirac's Hole Theory and the Prediction of the Positron</h3>
<p>
Because relativistic quantum mechanics permits negative energy eigenstates with $E \le -mc^2$, an unconstrained electron would cascade down into infinitely negative energies by radiative emission.
</p>
<p>
To resolve this instability, Dirac invoked the Pauli exclusion principle:
</p>
<blockquote>
  <em>"All negative-energy states in the universe with $E \le -mc^2$ are completely filled with an invisible, uniform sea of electrons—the <strong>Dirac Sea</strong>."</em>
</blockquote>
<p>
If a photon of energy $\hbar\omega \ge 2mc^2 \approx 1.022\text{ MeV}$ is absorbed by an electron in the negative-energy sea, the electron is kicked into a positive-energy state ($E \ge +mc^2$). It leaves behind a <em>vacancy</em> or <strong>hole</strong> in the sea.
</p>
<p>
A hole in a sea of charge $-e$ and energy $-E$ behaves physically as a particle of:
</p>
$$q_{\text{hole}} = -(-e) = +e, \quad E_{\text{hole}} = -(-E) = +E > 0$$
<p>
Dirac thus predicted the <strong>positron</strong> (the anti-electron), discovered experimentally by Carl Anderson in 1932.
</p>

<h3>2. The Klein Paradox: Relativistic Tunneling</h3>
<p>
Consider a relativistic electron of energy $E < V_0$ incident upon an electrostatic step potential of height $V_0$.
</p>
<p>
In non-relativistic physics, when $V_0 > E$, the wave is exponentially damped inside the barrier with zero transmission. In the Dirac equation, when the potential step exceeds the pair-creation threshold:
</p>
$$V_0 > E + mc^2$$
<p>
the incident positive-energy state couples directly to the continuum of negative-energy states inside the barrier! The transmission coefficient does not decay to zero; rather, particles penetrate through the barrier with substantial probability. Physically, the gigantic electric field $\mathcal{E} \sim V_0 / \lambda_c$ sparks the vacuum, creating electron-positron pairs: electrons are reflected, while positrons are transmitted into the barrier.
</p>
"""
        }
    ],
    "simulations": [
        {
            "id": "qm2-dirac-spinor-sim",
            "title": "Dirac 4-Component Spinor Dispersion & Helicity Visualizer",
            "description": "Interactive visualizer of Dirac 4-component spinors in momentum space, showing positive/negative energy branches E = ±√(p²c² + m²c⁴), upper/lower component ratios, and helicity projections."
        },
        {
            "id": "qm2-klein-paradox-sim",
            "title": "The Klein Paradox: Relativistic Barrier Tunneling & Pair Production",
            "description": "Simulation of Dirac wavepacket transmission at a supercritical step potential V₀ > E + mc², showing anti-matter phase oscillation and Klein transmission into the negative energy continuum."
        }
    ],
    "solvedProblems": [
        {
            "number": 1,
            "title": "Proof of the Clifford Algebra & Fundamental Dirac Gamma Trace Identities",
            "statement": r"The Dirac gamma matrices satisfy $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}\hat{I}_{4\times 4}$.\n(a) Prove that $\text{Tr}(\gamma^\mu) = 0$ for all $\mu \in \{0, 1, 2, 3\}$.\n(b) Prove that $\text{Tr}(\gamma^\mu \gamma^\nu) = 4\eta^{\mu\nu}$.\n(c) Prove the contraction identity $\gamma^\mu \gamma_\mu = 4\hat{I}_{4\times 4}$.",
            "solution": r"**(a) Trace of Single Gamma Matrix:**\nUsing the matrix $\gamma^5 \equiv i\gamma^0\gamma^1\gamma^2\gamma^3$, which anticommutes with all gamma matrices: $\{\gamma^\mu, \gamma^5\} = 0$, and $(\gamma^5)^2 = \hat{I}$.\n$$\text{Tr}(\gamma^\mu) = \text{Tr}(\gamma^\mu (\gamma^5)^2) = \text{Tr}(\gamma^5 \gamma^\mu \gamma^5)$$\nUsing the cyclic property of the trace $\text{Tr}(AB) = \text{Tr}(BA)$:\n$$\text{Tr}(\gamma^5 \gamma^\mu \gamma^5) = \text{Tr}((\gamma^5 \gamma^\mu)\gamma^5) = \text{Tr}(\gamma^5 (-\gamma^5 \gamma^\mu)) = -\text{Tr}((\gamma^5)^2 \gamma^\mu) = -\text{Tr}(\gamma^\mu)$$\n$$\text{Tr}(\gamma^\mu) = -\text{Tr}(\gamma^\mu) \implies 2\text{Tr}(\gamma^\mu) = 0 \implies \text{Tr}(\gamma^\mu) = 0$$\n\n**(b) Trace of Product of Two Gamma Matrices:**\nUsing the Clifford anticommutator $\{\gamma^\mu, \gamma^\nu\} = \gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2\eta^{\mu\nu}\hat{I}$:\n$$\text{Tr}(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu) = \text{Tr}(2\eta^{\mu\nu}\hat{I}) = 2\eta^{\mu\nu}\text{Tr}(\hat{I}) = 2\eta^{\mu\nu}(4) = 8\eta^{\mu\nu}$$\nBy cyclic invariance of the trace:\n$$\text{Tr}(\gamma^\nu\gamma^\mu) = \text{Tr}(\gamma^\mu\gamma^\nu)$$\nTherefore:\n$$\text{Tr}(\gamma^\mu\gamma^\nu) + \text{Tr}(\gamma^\mu\gamma^\nu) = 2\text{Tr}(\gamma^\mu\gamma^\nu) = 8\eta^{\mu\nu} \implies \text{Tr}(\gamma^\mu\gamma^\nu) = 4\eta^{\mu\nu}$$\n\n**(c) Contraction Identity $\gamma^\mu \gamma_\mu$:**\n$$\gamma^\mu \gamma_\mu = \eta_{\mu\nu}\gamma^\mu\gamma^\nu = \frac{1}{2}\eta_{\mu\nu}(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu) = \frac{1}{2}\eta_{\mu\nu}(2\eta^{\mu\nu}\hat{I}) = \eta_{\mu\nu}\eta^{\mu\nu}\hat{I}$$\nIn four spacetime dimensions:\n$$\eta_{\mu\nu}\eta^{\mu\nu} = \delta_\mu^\mu = 1 + 1 + 1 + 1 = 4$$\n$$\gamma^\mu \gamma_\mu = 4\hat{I}_{4\times 4}$$"
        },
        {
            "number": 2,
            "title": "Non-Relativistic Reduction of the Dirac Equation to the Pauli Equation",
            "statement": r"Starting from the minimally coupled Dirac equation for an electron in an electromagnetic field $(\Phi, \vec{A})$:\n$$i\hbar \frac{\partial}{\partial t}\begin{pmatrix} \phi \\ \chi \end{pmatrix} = \begin{pmatrix} mc^2 - e\Phi & c\vec{\sigma}\cdot\vec{\Pi} \\ c\vec{\sigma}\cdot\vec{\Pi} & -mc^2 - e\Phi \end{pmatrix} \begin{pmatrix} \phi \\ \chi \end{pmatrix}$$\n(a) Factor out the fast phase $e^{-imc^2 t/\hbar}$ and write the coupled differential equations for $\phi$ and $\chi$.\n(b) In the non-relativistic regime $v \ll c$, express the small component $\chi$ in terms of $\phi$ to order $\mathcal{O}(v/c)$.\n(c) Prove that the resulting equation for $\phi$ is the Pauli equation with gyromagnetic ratio $g = 2$.",
            "solution": r"**(a) Factoring the Rest-Mass Phase:**\nLet $\begin{pmatrix} \phi \\ \chi \end{pmatrix} = \begin{pmatrix} \tilde{\phi} \\ \tilde{\chi} \end{pmatrix}e^{-imc^2 t/\hbar}$.\nDifferentiating: $i\hbar \partial_t \phi = (i\hbar \partial_t \tilde{\phi} + mc^2 \tilde{\phi})e^{-imc^2 t/\hbar}$.\nSubstituting into the Dirac Hamiltonian:\n$$i\hbar \frac{\partial \tilde{\phi}}{\partial t} + mc^2 \tilde{\phi} = (mc^2 - e\Phi)\tilde{\phi} + c\vec{\sigma}\cdot\vec{\Pi}\tilde{\chi}$$\n$$i\hbar \frac{\partial \tilde{\chi}}{\partial t} + mc^2 \tilde{\chi} = c\vec{\sigma}\cdot\vec{\Pi}\tilde{\phi} - (mc^2 + e\Phi)\tilde{\chi}$$\nCanceling $mc^2$ from the first equation and rearranging the second:\n$$i\hbar \frac{\partial \tilde{\phi}}{\partial t} = -e\Phi\tilde{\phi} + c\vec{\sigma}\cdot\vec{\Pi}\tilde{\chi}$$\n$$i\hbar \frac{\partial \tilde{\chi}}{\partial t} + 2mc^2\tilde{\chi} = c\vec{\sigma}\cdot\vec{\Pi}\tilde{\phi} - e\Phi\tilde{\chi}$$\n\n**(b) Small Component Elimination:**\nIn the non-relativistic limit, the kinetic and potential energies are negligible compared to the rest mass energy $2mc^2$:\n$$|i\hbar \partial_t \tilde{\chi}| \ll 2mc^2|\tilde{\chi}|, \quad |e\Phi| \ll 2mc^2$$\nTherefore, the second equation simplifies to:\n$$2mc^2\tilde{\chi} \approx c\vec{\sigma}\cdot\vec{\Pi}\tilde{\phi} \implies \tilde{\chi} \approx \frac{\vec{\sigma}\cdot\vec{\Pi}}{2mc}\tilde{\phi}$$\nNotice that $\tilde{\chi} \sim \frac{v}{c}\tilde{\phi}$, confirming that $\tilde{\chi}$ is indeed the small component suppressed by $v/c$.\n\n**(c) Pauli Equation and $g = 2$:**\nSubstituting $\tilde{\chi}$ into the equation for $\tilde{\phi}$:\n$$i\hbar \frac{\partial \tilde{\phi}}{\partial t} = c(\vec{\sigma}\cdot\vec{\Pi})\left(\frac{\vec{\sigma}\cdot\vec{\Pi}}{2mc}\tilde{\phi}\right) - e\Phi\tilde{\phi} = \frac{(\vec{\sigma}\cdot\vec{\Pi})^2}{2m}\tilde{\phi} - e\Phi\tilde{\phi}$$\nUsing the Pauli vector identity:\n$$(\vec{\sigma}\cdot\vec{\Pi})^2 = \vec{\Pi}^2 + i\vec{\sigma}\cdot(\vec{\Pi} \times \vec{\Pi})$$\nEvaluating the cross product of kinetic momenta:\n$$(\vec{\Pi}\times\vec{\Pi})_k = \epsilon_{ijk}\Pi_i\Pi_j = \frac{1}{2}\epsilon_{ijk}[\Pi_i, \Pi_j]$$\n$$[\Pi_i, \Pi_j] = [p_i + eA_i, p_j + eA_j] = e[p_i, A_j] + e[A_i, p_j] = -i\hbar e(\partial_i A_j - \partial_j A_i) = -i\hbar e \epsilon_{ijk} B_k$$\n$$\implies \vec{\Pi}\times\vec{\Pi} = -i\hbar e \vec{B}$$\nSubstituting back:\n$$(\vec{\sigma}\cdot\vec{\Pi})^2 = \vec{\Pi}^2 + i\vec{\sigma}\cdot(-i\hbar e\vec{B}) = (\vec{p} + e\vec{A})^2 + e\hbar(\vec{\sigma}\cdot\vec{B})$$\nDividing by $2m$:\n$$i\hbar \frac{\partial \tilde{\phi}}{\partial t} = \left[ \frac{(\vec{p} + e\vec{A})^2}{2m} + \frac{e\hbar}{2m}(\vec{\sigma}\cdot\vec{B}) - e\Phi \right]\tilde{\phi}$$\nSince $\vec{S} = \frac{\hbar}{2}\vec{\sigma}$, the magnetic Zeeman coupling term is:\n$$\hat{H}_B = \frac{e\hbar}{2m}\vec{\sigma}\cdot\vec{B} = 2\left(\frac{e}{2m}\right)\vec{S}\cdot\vec{B} = -\vec{\mu}_s \cdot \vec{B} \implies g_s = 2$$\nThis completes the proof that $g = 2$ is an inescapable consequence of relativistic quantum mechanics."
        },
        {
            "number": 3,
            "title": "The Klein Paradox: Dirac Electron Transmission Across a Supercritical Step Barrier",
            "statement": r"A 1D relativistic electron of mass $m$ and positive energy $E > mc^2$ travels to the right and encounters an electrostatic step potential $V(x) = 0$ for $x < 0$ and $V(x) = V_0$ for $x > 0$, where $V_0 > E + mc^2$ (supercritical barrier).\n(a) Write down the Dirac wavefunction in Region I ($x < 0$) in terms of incident and reflected amplitudes.\n(b) Write down the transmitted wavefunction in Region II ($x > 0$), explaining why the transmitted wave corresponds to negative energy states.\n(c) Calculate the reflection coefficient $R$ and transmission coefficient $T$, and interpret the apparent paradox $R > 1$ in terms of pair creation and antiparticle current.",
            "solution": r"**(a) Region I ($x < 0$, $V = 0$):**\nThe wavevector is $p_1 = \sqrt{E^2 - m^2 c^4}/c > 0$.\nThe incident and reflected wavefunctions are:\n$$\psi_I(x) = a \begin{pmatrix} 1 \\ 0 \\ \frac{c p_1}{E + mc^2} \\ 0 \end{pmatrix}e^{i p_1 x/\hbar} + b \begin{pmatrix} 1 \\ 0 \\ -\frac{c p_1}{E + mc^2} \\ 0 \end{pmatrix}e^{-i p_1 x/\hbar}$$\n\n**(b) Region II ($x > 0$, $V = V_0$):**\nInside the barrier, the effective energy is $E' = E - V_0 < -mc^2$.\nThe momentum satisfies $p_2^2 c^2 = (E - V_0)^2 - m^2 c^4 > 0$, so $p_2$ is real!\n$$\psi_{II}(x) = d \begin{pmatrix} 1 \\ 0 \\ \frac{c p_2}{E - V_0 + mc^2} \\ 0 \end{pmatrix}e^{i p_2 x/\hbar}$$\nTo ensure that group velocity $v_g = \frac{\partial E}{\partial p_2} = \frac{c^2 p_2}{E - V_0}$ directs energy *away* from the interface (into $x > 0$), since $E - V_0 < 0$, the momentum $p_2$ must be chosen negative: $p_2 = -\frac{\sqrt{(V_0 - E)^2 - m^2 c^4}}{c}$.\n\n**(c) Boundary Conditions and Transmission Paradox:**\nMatching the wavefunctions at $x = 0$:\n$$a + b = d$$\n$$a - b = r d, \quad r \equiv \frac{p_2}{p_1}\frac{E + mc^2}{E - V_0 + mc^2}$$\nBecause $p_2 < 0$ and $E - V_0 + mc^2 < 0$, $r$ is positive:\n$$\frac{b}{a} = \frac{1 - r}{1 + r}, \quad \frac{d}{a} = \frac{2}{1 + r}$$\nThe conserved probability current is $J = c\psi^\dagger \alpha_x \psi$. Calculating the currents:\n$$J_{\text{inc}} = \frac{2c^2 p_1}{E + mc^2}|a|^2$$\n$$J_{\text{ref}} = \frac{2c^2 p_1}{E + mc^2}|b|^2$$\n$$J_{\text{trans}} = \frac{2c^2 p_2}{E - V_0 + mc^2}|d|^2$$\nSince $p_2 < 0$ and $E - V_0 + mc^2 < 0$, $J_{\text{trans}}$ is *negative*! Current conservation $J_{\text{inc}} = J_{\text{ref}} + J_{\text{trans}}$ implies:\n$$R = \frac{J_{\text{ref}}}{J_{\text{inc}}} = \left(\frac{1 - r}{1 + r}\right)^2$$\n$$T = \frac{J_{\text{trans}}}{J_{\text{inc}}} = \frac{4r}{(1 + r)^2}$$\nWhen $V_0 \gg E$, $r < 0$ can occur in other conventions, but in all consistent treatments, the reflected flux is augmented by transmitted positrons moving into the barrier: the strong field tears electron-positron pairs from the vacuum, sending positrons into the barrier ($x > 0$) and electrons back into Region I ($x < 0$), proving that a single-particle picture breaks down in relativistic strong fields in favor of quantum field theory."
        }
    ]
}

with open("qm2_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7, f, indent=2)
print("Saved qm2_u7.json")

with open("qm2_u8.json", "w", encoding="utf-8") as f:
    json.dump(u8, f, indent=2)
print("Saved qm2_u8.json")
