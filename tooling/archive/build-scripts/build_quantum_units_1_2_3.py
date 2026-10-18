"""
build_quantum_units_1_2_3.py
Builds Units 1, 2, and 3 for Quantum Chemistry and Statistical Thermodynamics (OpenSTEM Milestone #52).
Each unit contains 7 comprehensive sections and 7 multi-step solved problems.
Strictly zero prohibited tokens (no course numbers, no marks, no grades, no exams).
"""

def get_units_1_2_3():
    units = []

    # =========================================================================
    # UNIT 1: Foundations & Historical Development of Quantum Mechanics
    # =========================================================================
    unit1 = {
        "id": "unit-1",
        "unitNumber": 1,
        "title": "Unit 1: Foundations & Historical Development of Quantum Mechanics",
        "leadSummary": r"""Comprehensive foundational treatment of the breakdown of classical Newtonian and Maxwellian physics at microscopic scales: blackbody spectral radiance and ultraviolet divergence, Planck's quantized energy hypothesis, the photoelectric effect and Einstein's photon momentum, Compton scattering kinematics, de Broglie matter waves, the Heisenberg uncertainty principle, Schrödinger wave mechanics, Hermitian operator algebra, and the foundational postulates of quantum theory.""",
        "simulations": [
            "sim_qc_blackbody_compton_wavepacket"
        ],
        "sections": [
            {
                "id": "sec-1-1",
                "secNumber": "1.1",
                "title": "Failure of Classical Mechanics & The Ultraviolet Catastrophe",
                "content": r"""By the late nineteenth century, classical mechanics (Newtonian dynamics) and classical electrodynamics (Maxwell's field equations) successfully described macroscopic phenomena. However, applying classical equipartition of energy to electromagnetic cavity radiation led to a profound mathematical catastrophe.

### The Classical Rayleigh-Jeans Radiation Law
Consider an isothermal cavity (hohlraum) at absolute temperature \(T\) containing standing electromagnetic waves with perfectly conducting walls of volume \(V\). 
In classical physics, each spatial standing wave mode possesses two independent transverse polarization states. The number of electromagnetic cavity modes per unit volume in the frequency interval \([\nu, \nu + d\nu]\) is given by the three-dimensional density of states:
\[
g(\nu) d\nu = \frac{8\pi \nu^2}{c^3} d\nu
\]
According to the classical equipartition theorem of statistical mechanics, every quadratic degree of freedom in thermal equilibrium carries an average thermal energy of \(\frac{1}{2} k_B T\). Because each standing electromagnetic mode corresponds to an equivalent one-dimensional harmonic oscillator (possessing kinetic and potential energy quadratic terms), the classical average energy per mode is:
\[
\langle \epsilon \rangle_{\text{class}} = k_B T
\]
Multiplying the mode density by the classical average energy yields the Rayleigh-Jeans spectral energy density:
\[
\rho_{\text{RJ}}(\nu, T) d\nu = g(\nu) \langle \epsilon \rangle_{\text{class}} d\nu = \frac{8\pi \nu^2}{c^3} k_B T d\nu
\]
Expressed in terms of wavelength \(\lambda = c / \nu\):
\[
\rho_{\text{RJ}}(\lambda, T) d\lambda = \frac{8\pi k_B T}{\lambda^4} d\lambda
\]

### The Ultraviolet Catastrophe
While the Rayleigh-Jeans law agreed with infrared measurements at long wavelengths (\(\lambda \rightarrow \infty\)), it diverged catastrophically as \(\lambda \rightarrow 0\) (\(\nu \rightarrow \infty\)):
\[
\lim_{\nu \rightarrow \infty} \rho_{\text{RJ}}(\nu, T) = \infty
\]
Integrating the total radiant energy density across all frequencies yielded an impossible physical infinity:
\[
U_{\text{total}} = \int_0^\infty \rho_{\text{RJ}}(\nu, T) d\nu = \frac{8\pi k_B T}{c^3} \int_0^\infty \nu^2 d\nu = \infty
\]
This divergence, termed the **ultraviolet catastrophe** by Paul Ehrenfest, meant that any heated cavity should instantaneously radiate infinite energy into high-frequency ultraviolet, X-ray, and gamma-ray modes—a physical impossibility.

### Planck's Revolutionary Quantization Hypothesis
In December 1900, Max Planck resolved the catastrophe by proposing that the atomic resonators constituting the cavity walls cannot absorb or emit energy continuously. Instead, energy exchange occurs strictly in discrete, indivisible packets called *quanta*:
\[
\epsilon_n = n h \nu, \quad n \in \{0, 1, 2, 3, \dots\}
\]
where \(h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}\) is Planck's constant.

Applying Maxwell-Boltzmann statistics to the discrete energy states, the quantum statistical average energy of a cavity oscillator is:
\[
\langle \epsilon \rangle_{\text{quant}} = \frac{\sum_{n=0}^\infty (n h \nu) e^{-n h \nu / k_B T}}{\sum_{n=0}^\infty e^{-n h \nu / k_B T}}
\]
Letting \(x = e^{-h\nu / k_B T}\):
\[
\sum_{n=0}^\infty x^n = \frac{1}{1 - x}, \quad \sum_{n=0}^\infty n x^n = x \frac{d}{dx} \left( \frac{1}{1 - x} \right) = \frac{x}{(1 - x)^2}
\]
Hence:
\[
\langle \epsilon \rangle_{\text{quant}} = h\nu \frac{x}{1 - x} = \frac{h\nu}{e^{h\nu / k_B T} - 1}
\]
Multiplying by the mode density \(g(\nu)\) yields **Planck's radiation law**:
\[
\rho(\nu, T) d\nu = \frac{8\pi h \nu^3}{c^3} \frac{1}{e^{h\nu / k_B T} - 1} d\nu
\]
In wavelength coordinates:
\[
\rho(\lambda, T) d\lambda = \frac{8\pi h c}{\lambda^5} \frac{1}{e^{h c / \lambda k_B T} - 1} d\lambda
\]

### Asymptotic Limits and Wien's Displacement Law
1. **Low Frequency / Long Wavelength Limit (\(h\nu \ll k_B T\)):**
   Expanding the exponential \(e^{h\nu / k_B T} \approx 1 + \frac{h\nu}{k_B T}\):
   \[
   \langle \epsilon \rangle \approx \frac{h\nu}{1 + \frac{h\nu}{k_B T} - 1} = k_B T
   \]
   reproducing the classical Rayleigh-Jeans expression.
2. **High Frequency / Short Wavelength Limit (\(h\nu \gg k_B T\)):**
   \(e^{h\nu / k_B T} \gg 1\):
   \[
   \rho(\nu, T) \approx \frac{8\pi h \nu^3}{c^3} e^{-h\nu / k_B T}
   \]
   reproducing Wien's empirical exponential distribution and preventing the ultraviolet catastrophe.
3. **Wien's Displacement Law:**
   Differentiating \(\rho(\lambda, T)\) with respect to \(\lambda\) and setting \(\frac{\partial \rho}{\partial \lambda} = 0\) leads to the transcendental equation \(5(1 - e^{-y}) - y = 0\) where \(y = \frac{h c}{\lambda_{\text{max}} k_B T}\). Numerical solution gives \(y \approx 4.965114\), yielding:
   \[
   \lambda_{\text{max}} T = \frac{h c}{4.965114 k_B} = b \approx 2.89777 \times 10^{-3}\text{ m}\cdot\text{K}
   \]"""
            },
            {
                "id": "sec-1-2",
                "secNumber": "1.2",
                "title": "Photoelectric & Compton Effects: Particle Nature of Light",
                "content": r"""While Planck viewed quantization as a mathematical property of atomic cavity resonators, Albert Einstein (1905) established that electromagnetic radiation itself propagates as localized, corpuscular quanta—photons—each carrying discrete energy and momentum.

### The Photoelectric Effect
When monochromatic ultraviolet or visible light strikes a clean metallic surface, electrons (photoelectrons) are ejected. Classical wave theory predicted that:
1. Electron kinetic energy should increase with increasing light wave intensity (electric field amplitude squared).
2. Electron emission should occur after a measurable time lag at low light intensities while the continuous wavefront accumulates sufficient energy.
3. Photoelectrons should be ejected at any frequency provided the intensity is sufficiently large.

Experimental observations by Heinrich Hertz, Philipp Lenard, and Robert Millikan directly contradicted classical theory:
- Electron emission occurs instantaneously (time lag \(< 10^{-9}\text{ s}\)) even under ultra-weak illumination.
- A well-defined threshold frequency \(\nu_0\) exists below which zero photoelectrons are emitted regardless of beam intensity.
- The maximum kinetic energy \(K_{\text{max}}\) depends linearly on light frequency \(\nu\) and is completely independent of light intensity.
- Increasing light intensity increases the photocurrent (number of ejected electrons per second) without changing \(K_{\text{max}}\).

### Einstein's Photoelectric Equation
Einstein proposed that a single photon of energy \(h\nu\) collides with a single bound electron in the metal. Overcoming the surface electrostatic potential barrier requires a characteristic binding energy termed the **work function** \(\Phi\). The conservation of energy yields:
\[
h\nu = \Phi + K_{\text{max}} = \Phi + \frac{1}{2} m_e v_{\text{max}}^2
\]
Expressing \(K_{\text{max}}\) in terms of the stopping potential \(V_s\) required to reduce the photocurrent to zero (\(K_{\text{max}} = e V_s\)):
\[
e V_s = h\nu - \Phi \implies V_s = \left(\frac{h}{e}\right)\nu - \frac{\Phi}{e}
\]
The slope of \(V_s\) versus frequency \(\nu\) is universally equal to \(h/e\), providing an independent measurement of Planck's constant.

### The Compton Effect
In 1923, Arthur H. Compton directed monochromatic X-rays (\(\lambda \sim 0.07\text{ nm}\)) at a graphite target and observed that the scattered radiation contained both the incident wavelength \(\lambda\) and an unexpected shifted, longer wavelength \(\lambda'\).

Treating the collision between an X-ray photon and an initially stationary free electron (\(m_0\)) using relativistic mechanics:
- **Incident Photon:** Energy \(E = h\nu\), momentum \(\mathbf{p} = \frac{h\nu}{c} \hat{\mathbf{i}}\).
- **Target Electron (at rest):** Energy \(E_e = m_0 c^2\), momentum \(\mathbf{p}_e = 0\).
- **Scattered Photon (at angle \(\theta\)):** Energy \(E' = h\nu'\), momentum \(\mathbf{p}' = \frac{h\nu'}{c}\).
- **Recoil Electron (at angle \(\phi\)):** Relativistic energy \(E_e' = \sqrt{p_e^2 c^2 + m_0^2 c^4}\), momentum \(\mathbf{p}_e\).

From conservation of relativistic momentum:
\[
\mathbf{p} = \mathbf{p}' + \mathbf{p}_e \implies \mathbf{p}_e = \mathbf{p} - \mathbf{p}'
\]
Squaring both sides:
\[
p_e^2 = p^2 + p'^2 - 2 p p' \cos\theta = \left(\frac{h\nu}{c}\right)^2 + \left(\frac{h\nu'}{c}\right)^2 - 2 \left(\frac{h\nu}{c}\right)\left(\frac{h\nu'}{c}\right) \cos\theta
\]
From conservation of total relativistic energy:
\[
h\nu + m_0 c^2 = h\nu' + E_e' \implies E_e' = h(\nu - \nu') + m_0 c^2
\]
Equating \((E_e')^2 = p_e^2 c^2 + m_0^2 c^4\):
\[
[h(\nu - \nu') + m_0 c^2]^2 = p_e^2 c^2 + m_0^2 c^4
\]
Expanding and substituting \(p_e^2\):
\[
h^2(\nu - \nu')^2 + 2 h m_0 c^2 (\nu - \nu') + m_0^2 c^4 = h^2 \nu^2 + h^2 \nu'^2 - 2 h^2 \nu \nu' \cos\theta + m_0^2 c^4
\]
Subtracting common terms yields:
\[
-2 h^2 \nu \nu' + 2 h m_0 c^2 (\nu - \nu') = -2 h^2 \nu \nu' \cos\theta
\]
Dividing throughout by \(2 h m_0 c^2 \nu \nu'\):
\[
\frac{1}{\nu'} - \frac{1}{\nu} = \frac{h}{m_0 c^2} (1 - \cos\theta)
\]
Multiplying by \(c\) (\(\lambda = c/\nu\)) yields the **Compton shift equation**:
\[
\Delta\lambda = \lambda' - \lambda = \frac{h}{m_0 c} (1 - \cos\theta) = \lambda_C (1 - \cos\theta)
\]
where \(\lambda_C = \frac{h}{m_0 c} \approx 2.42631 \times 10^{-12}\text{ m} = 0.02426\text{ Å}\) is the Compton wavelength of the electron."""
            },
            {
                "id": "sec-1-3",
                "secNumber": "1.3",
                "title": "de Broglie Hypothesis & Matter Wave Diffraction",
                "content": r"""In 1924, Louis de Broglie extended the wave-particle duality of light to all material particles. If electromagnetic waves possess particle-like characteristics (photons with \(p = h/\lambda\)), then material particles (electrons, protons, neutrons) must possess intrinsic wave-like properties.

### The de Broglie Relations
For any particle with relativistic energy \(E\) and linear momentum \(p = m v\), de Broglie associated a matter wave of frequency \(\nu\) and wavelength \(\lambda\):
\[
\lambda = \frac{h}{p} = \frac{h}{m v}
\]
\[
\nu = \frac{E}{h}
\]
Expressed in terms of the reduced Planck constant \(\hbar = \frac{h}{2\pi}\), wavevector \(k = \frac{2\pi}{\lambda}\), and angular frequency \(\omega = 2\pi\nu\):
\[
\mathbf{p} = \hbar \mathbf{k}, \quad E = \hbar \omega
\]

### Thermal and Non-Relativistic Kinetic Scaling
For a non-relativistic particle of mass \(m\) accelerated through an electrostatic potential difference \(V\):
\[
K = \frac{p^2}{2m} = e V \implies p = \sqrt{2 m e V}
\]
The corresponding de Broglie wavelength is:
\[
\lambda = \frac{h}{\sqrt{2 m e V}}
\]
For an electron (\(m_e = 9.109 \times 10^{-31}\text{ kg}\), \(e = 1.602 \times 10^{-19}\text{ C}\)):
\[
\lambda_e = \frac{1.226}{\sqrt{V}}\text{ nm} = \sqrt{\frac{150}{V}}\text{ Å}
\]
For an accelerating voltage \(V = 100\text{ V}\), \(\lambda_e \approx 0.123\text{ nm}\) (1.23 Å), which is of the exact order of interatomic lattice spacings in crystalline solids (\(d \sim 1 - 3\text{ Å}\)).

### Experimental Verification: Davisson-Germer & Thomson Experiments
In 1927, Clinton Davisson and Lester Germer scattered slow electrons (\(54\text{ eV}\)) from a target nickel single crystal. They observed a pronounced peak in scattered electron intensity at an angle \(\phi = 50^\circ\).
Using Bragg's diffraction law for atomic lattice planes with spacing \(D = 0.215\text{ nm}\):
\[
n \lambda = 2 d \sin\theta = 2 (D \sin(\phi/2)) \sin\theta = D \sin\phi = 0.215\text{ nm} \times \sin(50^\circ) = 0.165\text{ nm}
\]
The theoretical de Broglie wavelength for a \(54\text{ eV}\) electron is:
\[
\lambda = \frac{h}{\sqrt{2 m_e (54\text{ eV})}} = 0.167\text{ nm}
\]
The extraordinary agreement (\(0.165\text{ nm}\) vs \(0.167\text{ nm}\)) definitively proved that electrons travel as coherent wave fields capable of constructive and destructive interference."""
            },
            {
                "id": "sec-1-4",
                "secNumber": "1.4",
                "title": "Heisenberg Uncertainty Principle & Wavepacket Dispersion",
                "content": r"""The wave nature of matter implies that a microscopic particle cannot be localized to an infinitesimal geometric point while possessing a sharply defined momentum. In 1927, Werner Heisenberg formulated this fundamental limitation.

### Mathematical Origin from Fourier Transform Pairs
A localized quantum particle is mathematically represented as a **wavepacket** formed by the continuous superposition of monochromatic plane waves:
\[
\psi(x, 0) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty \phi(k) e^{i k x} dk
\]
where \(\phi(k)\) is the momentum-space probability amplitude obtained via inverse Fourier transform:
\[
\phi(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty \psi(x, 0) e^{-i k x} dx
\]
For a standard Gaussian wavepacket:
\[
\psi(x, 0) = \left( \frac{1}{2\pi \sigma_x^2} \right)^{1/4} \exp\left( -\frac{x^2}{4\sigma_x^2} + i k_0 x \right)
\]
Its Fourier transform in wavenumber space is also Gaussian:
\[
\phi(k) = \left( \frac{2\sigma_x^2}{\pi} \right)^{1/4} \exp\left( -\sigma_x^2 (k - k_0)^2 \right)
\]
The standard deviation in spatial position is \(\Delta x = \sigma_x\), and the standard deviation in wavenumber is \(\Delta k = \frac{1}{2\sigma_x}\).
Using de Broglie's relation \(p = \hbar k \implies \Delta p = \hbar \Delta k\):
\[
\Delta x \cdot \Delta p = \sigma_x \cdot \left( \frac{\hbar}{2\sigma_x} \right) = \frac{\hbar}{2}
\]
For any arbitrary (non-Gaussian) normalized wavefunction, the product of standard deviations satisfies the general **Heisenberg uncertainty inequality**:
\[
\Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}
\]

### Generalized Robertson-Schrödinger Uncertainty Relation
In operator quantum mechanics, for any two Hermitian operators \(\hat{A}\) and \(\hat{B}\):
\[
\Delta A = \sqrt{\langle \hat{A}^2 \rangle - \langle \hat{A} \rangle^2}, \quad \Delta B = \sqrt{\langle \hat{B}^2 \rangle - \langle \hat{B} \rangle^2}
\]
The general uncertainty product is bounded by their commutator \([\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}\):
\[
\Delta A \cdot \Delta B \ge \frac{1}{2} |\langle [\hat{A}, \hat{B}] \rangle|
\]
For position \(\hat{x} = x\) and momentum \(\hat{p}_x = -i\hbar \frac{\partial}{\partial x}\):
\[
[\hat{x}, \hat{p}_x] f(x) = x \left(-i\hbar \frac{\partial f}{\partial x}\right) - \left(-i\hbar \frac{\partial (x f)}{\partial x}\right) = i\hbar f(x) \implies [\hat{x}, \hat{p}_x] = i\hbar \hat{I}
\]
Substituting into Robertson's theorem yields \(\Delta x \cdot \Delta p_x \ge \frac{1}{2} |i\hbar| = \frac{\hbar}{2}\).

### Time-Energy Uncertainty Relation
A complementary uncertainty relation connects the lifetime \(\Delta t\) of an excited quantum state to the uncertainty in its energy \(\Delta E\):
\[
\Delta E \cdot \Delta t \ge \frac{\hbar}{2}
\]
If an excited atomic or molecular state has a finite radiative lifetime \(\tau\), the emitted photon energy cannot be monochromatic. It possesses an intrinsic **natural linewidth** \(\Delta \nu = \frac{1}{2\pi \tau}\)."""
            },
            {
                "id": "sec-1-5",
                "secNumber": "1.5",
                "title": "Schrödinger Wave Equation: Time-Dependent & Stationary States",
                "content": r"""In 1926, Erwin Schrödinger developed wave mechanics, replacing classical trajectories \(\mathbf{r}(t)\) with a continuous, complex-valued probability amplitude wavefunction \(\Psi(\mathbf{r}, t)\).

### The Time-Dependent Schrödinger Equation (TDSE)
For a single non-relativistic particle of mass \(m\) moving in an external scalar potential field \(V(\mathbf{r}, t)\), the state vector evolves according to:
\[
i\hbar \frac{\partial \Psi(\mathbf{r}, t)}{\partial t} = \hat{H} \Psi(\mathbf{r}, t)
\]
where \(\hat{H}\) is the Hamiltonian operator:
\[
\hat{H} = \hat{T} + \hat{V} = -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r}, t)
\]
In one Cartesian dimension:
\[
i\hbar \frac{\partial \Psi(x, t)}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi(x, t)}{\partial x^2} + V(x, t) \Psi(x, t)
\]

### Separation of Variables & The Time-Independent Schrödinger Equation
When the potential energy is static (\(V(\mathbf{r}, t) = V(\mathbf{r})\)), we apply the separation of variables ansatz:
\[
\Psi(\mathbf{r}, t) = \psi(\mathbf{r}) \phi(t)
\]
Substituting into the TDSE:
\[
i\hbar \psi(\mathbf{r}) \frac{d\phi(t)}{dt} = \left[ -\frac{\hbar^2}{2m} \nabla^2 \psi(\mathbf{r}) + V(\mathbf{r}) \psi(\mathbf{r}) \right] \phi(t)
\]
Dividing throughout by \(\psi(\mathbf{r}) \phi(t)\):
\[
\frac{i\hbar}{\phi(t)} \frac{d\phi(t)}{dt} = \frac{1}{\psi(\mathbf{r})} \left[ -\frac{\hbar^2}{2m} \nabla^2 \psi(\mathbf{r}) + V(\mathbf{r}) \psi(\mathbf{r}) \right] = E
\]
Because the left side depends purely on time \(t\) while the right side depends purely on position \(\mathbf{r}\), both sides must equal a spatial-temporal constant \(E\) (the total energy).

Solving the temporal differential equation:
\[
\frac{d\phi}{dt} = -\frac{i E}{\hbar} \phi \implies \phi(t) = \exp\left(-\frac{i E t}{\hbar}\right)
\]
The spatial component satisfies the **Time-Independent Schrödinger Equation (TISE)**:
\[
\hat{H} \psi(\mathbf{r}) = E \psi(\mathbf{r})
\]
\[
\left[ -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r}) \right] \psi(\mathbf{r}) = E \psi(\mathbf{r})
\]

### Properties of Stationary States
A state described by a single energy eigenfunction \(\psi_n(\mathbf{r})\) with eigenvalue \(E_n\) has total wavefunction:
\[
\Psi_n(\mathbf{r}, t) = \psi_n(\mathbf{r}) e^{-i E_n t / \hbar}
\]
1. **Time-Invariant Probability Density:**
   \[
   |\Psi_n(\mathbf{r}, t)|^2 = \Psi_n^*(\mathbf{r}, t) \Psi_n(\mathbf{r}, t) = \psi_n^*(\mathbf{r}) e^{+i E_n t / \hbar} \psi_n(\mathbf{r}) e^{-i E_n t / \hbar} = |\psi_n(\mathbf{r})|^2
   \]
   The probability distribution is strictly static over time (hence *stationary state*).
2. **Stationary Expectation Values:**
   For any time-independent operator \(\hat{A}\):
   \[
   \langle \hat{A} \rangle(t) = \int \Psi_n^* \hat{A} \Psi_n d\tau = \int \psi_n^* \hat{A} \psi_n d\tau = \text{constant}
   \]
3. **Superposition and Non-Stationary Dynamics:**
   If a system is prepared in a linear combination of two or more distinct stationary states:
   \[
   \Psi(\mathbf{r}, t) = c_1 \psi_1(\mathbf{r}) e^{-i E_1 t / \hbar} + c_2 \psi_2(\mathbf{r}) e^{-i E_2 t / \hbar}
   \]
   the probability density beats at the Bohr transition frequency \(\omega_{21} = \frac{E_2 - E_1}{\hbar}\):
   \[
   |\Psi(\mathbf{r}, t)|^2 = |c_1|^2 |\psi_1|^2 + |c_2|^2 |\psi_2|^2 + 2 \text{Re}\left[ c_1^* c_2 \psi_1^* \psi_2 e^{-i (E_2 - E_1) t / \hbar} \right]
   \]"""
            },
            {
                "id": "sec-1-6",
                "secNumber": "1.6",
                "title": "Operators, Eigenvalues, Hermitian Adjoints & Commutation Rules",
                "content": r"""In quantum mechanics, physical observables are represented by linear operators acting on vectors in a complex Hilbert space \(\mathcal{H}\).

### Operator Algebra and Linearity
An operator \(\hat{A}\) is linear if for all wavefunctions \(\psi_1, \psi_2\) and complex scalars \(c_1, c_2\):
\[
\hat{A} (c_1 \psi_1 + c_2 \psi_2) = c_1 \hat{A}\psi_1 + c_2 \hat{A}\psi_2
\]
The eigenvalue equation for an operator \(\hat{A}\) is:
\[
\hat{A} \psi_n = a_n \psi_n
\]
where \(\psi_n\) is the eigenfunction and \(a_n\) is the corresponding scalar eigenvalue.

### Hermitian (Self-Adjoint) Operators
Because physical measurements yield real numbers, all physical observables must correspond to **Hermitian operators**.
The Hermitian adjoint (conjugate transpose) \(\hat{A}^\dagger\) of an operator \(\hat{A}\) is defined by the inner product relation:
\[
\langle \phi | \hat{A} \psi \rangle = \int \phi^* (\hat{A} \psi) d\tau = \int (\hat{A}^\dagger \phi)^* \psi d\tau = \langle \hat{A}^\dagger \phi | \psi \rangle
\]
An operator is **Hermitian** if \(\hat{A}^\dagger = \hat{A}\):
\[
\int \phi^* (\hat{A} \psi) d\tau = \int (\hat{A} \phi)^* \psi d\tau
\]

**Theorem 1: Real Eigenvalues**
Let \(\hat{A} \psi = a \psi\). Taking the inner product with \(\psi\):
\[
\langle \psi | \hat{A} \psi \rangle = a \langle \psi | \psi \rangle
\]
Since \(\hat{A}\) is Hermitian:
\[
\langle \psi | \hat{A} \psi \rangle = \langle \hat{A} \psi | \psi \rangle = a^* \langle \psi | \psi \rangle
\]
Therefore, \((a - a^*) \langle \psi | \psi \rangle = 0\). Since \(\langle \psi | \psi \rangle > 0\):
\[
a = a^* \implies a \in \mathbb{R}
\]

**Theorem 2: Orthogonality of Eigenfunctions**
Let \(\hat{A} \psi_1 = a_1 \psi_1\) and \(\hat{A} \psi_2 = a_2 \psi_2\) with distinct eigenvalues \(a_1 \neq a_2\):
\[
\langle \psi_1 | \hat{A} \psi_2 \rangle = a_2 \langle \psi_1 | \psi_2 \rangle
\]
\[
\langle \hat{A} \psi_1 | \psi_2 \rangle = a_1^* \langle \psi_1 | \psi_2 \rangle = a_1 \langle \psi_1 | \psi_2 \rangle
\]
Subtracting the two equations:
\[
(a_2 - a_1) \langle \psi_1 | \psi_2 \rangle = 0
\]
Since \(a_1 \neq a_2\):
\[
\langle \psi_1 | \psi_2 \rangle = \int \psi_1^* \psi_2 d\tau = 0
\]
Eigenfunctions belonging to distinct eigenvalues of a Hermitian operator are strictly orthogonal.

### Commutators and Simultaneous Observables
The commutator of two operators \(\hat{A}\) and \(\hat{B}\) is defined as:
\[
[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}
\]
- If \([\hat{A}, \hat{B}] = 0\), the operators **commute**. There exists a complete set of mutual simultaneous eigenfunctions \(\psi_{a,b}\) such that:
  \[
  \hat{A} \psi_{a,b} = a \psi_{a,b}, \quad \hat{B} \psi_{a,b} = b \psi_{a,b}
  \]
  Both observables can be measured simultaneously to arbitrary precision (\(\Delta A \cdot \Delta B = 0\)).
- If \([\hat{A}, \hat{B}] \neq 0\), the operators are **incompatible**. Measuring one observable inherently disrupts the state and creates fundamental uncertainty in the other."""
            },
            {
                "id": "sec-1-7",
                "secNumber": "1.7",
                "title": "Postulates of Quantum Mechanics & Dirac Bracket Formalism",
                "content": r"""The axiomatic mathematical foundation of modern non-relativistic quantum theory is codified in Dirac's bra-ket formalism.

### The Six Foundational Postulates

#### Postulate 1: The State Space
The physical state of a quantum system is completely specified by a state vector (ket) \(|\Psi(t)\rangle\) residing in a complex Hilbert space \(\mathcal{H}\). The state is normalized such that:
\[
\langle \Psi | \Psi \rangle = \int |\Psi(\mathbf{r}, t)|^2 d\tau = 1
\]
Max Born's statistical interpretation dictates that \(P(\mathbf{r}) d\tau = |\Psi(\mathbf{r}, t)|^2 d\tau\) represents the probability of finding the particle in differential volume \(d\tau\).

#### Postulate 2: Physical Observables
To every physically measurable dynamical observable \(A\) in classical mechanics, there corresponds a linear Hermitian operator \(\hat{A}\) acting in Hilbert space. Position and momentum operators obey the canonical commutation relation:
\[
[\hat{x}_j, \hat{p}_k] = i\hbar \delta_{jk} \hat{I}
\]

#### Postulate 3: Measurement Eigenvalues
The only possible outcomes of a single precise measurement of an observable \(A\) are the eigenvalues \(a_n\) of its associated Hermitian operator \(\hat{A}\):
\[
\hat{A} |a_n\rangle = a_n |a_n\rangle
\]

#### Postulate 4: Measurement Probabilities & State Collapse
Any normalized state \(|\Psi\rangle\) can be expanded in terms of the complete orthonormal eigenbasis \(\{|a_n\rangle\}\) of \(\hat{A}\):
\[
|\Psi\rangle = \sum_n c_n |a_n\rangle, \quad c_n = \langle a_n | \Psi\rangle
\]
The probability \(P(a_n)\) of measuring eigenvalue \(a_n\) is:
\[
P(a_n) = |\langle a_n | \Psi \rangle|^2 = |c_n|^2
\]
Immediately upon measuring the value \(a_n\), the state vector instantaneously collapses to the corresponding eigenstate \(|a_n\rangle\).

#### Postulate 5: Time Evolution
Between non-demolition measurements, the time evolution of the state vector is governed by the time-dependent Schrödinger equation:
\[
i\hbar \frac{d}{dt} |\Psi(t)\rangle = \hat{H} |\Psi(t)\rangle
\]

#### Postulate 6: Pauli Antisymmetry (Symmetrization Postulate)
The total state vector of a system of identical indistinguishable particles must be symmetric under particle permutation for bosons (integer spin \(S = 0, 1, 2\)) and antisymmetric for fermions (half-integer spin \(S = 1/2, 3/2\)):
\[
\hat{P}_{12} |\Psi(1, 2)\rangle = (-1)^{2S} |\Psi(1, 2)\rangle
\]"""
            }
        ],
        "problems": [
            {
                "id": "chem-qc-u1-p1",
                "title": "Problem 1: Blackbody Peak Radiance & Solar Surface Temperature from Wien's Law",
                "difficulty": "Foundational",
                "statement": r"""The solar emission spectrum measured outside Earth's atmosphere peaks at a maximum spectral wavelength \(\lambda_{\text{max}} = 502\text{ nm}\).
1. Calculate the effective surface blackbody temperature \(T_{\odot}\) of the Sun using Wien's displacement law constant \(b = 2.89777 \times 10^{-3}\text{ m}\cdot\text{K}\).
2. Derive the ratio of spectral energy densities predicted by the quantum Planck law versus the classical Rayleigh-Jeans formula at this peak wavelength \(\lambda_{\text{max}}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Effective Surface Temperature Calculation
From Wien's displacement law:
\[
\lambda_{\text{max}} T = b \implies T_{\odot} = \frac{b}{\lambda_{\text{max}}}
\]
Substitute \(\lambda_{\text{max}} = 502\text{ nm} = 5.02 \times 10^{-7}\text{ m}\):
\[
T_{\odot} = \frac{2.89777 \times 10^{-3}\text{ m}\cdot\text{K}}{5.02 \times 10^{-7}\text{ m}} \approx 5772.45\text{ K} \approx 5772\text{ K}
\]

---

#### Step 2: Planck to Rayleigh-Jeans Ratio at \(\lambda_{\text{max}}\)
The Planck spectral radiance is:
\[
\rho_{\text{Planck}}(\lambda) = \frac{8\pi h c}{\lambda^5} \frac{1}{e^{h c / \lambda k_B T} - 1}
\]
The Rayleigh-Jeans classical approximation is:
\[
\rho_{\text{RJ}}(\lambda) = \frac{8\pi k_B T}{\lambda^4}
\]
Taking the ratio:
\[
\frac{\rho_{\text{Planck}}(\lambda)}{\rho_{\text{RJ}}(\lambda)} = \frac{h c}{\lambda k_B T} \frac{1}{e^{h c / \lambda k_B T} - 1}
\]
Let \(y = \frac{h c}{\lambda k_B T}\). At the Wien peak \(\lambda_{\text{max}}\), \(y = 4.965114\).
Evaluate the ratio:
\[
\frac{\rho_{\text{Planck}}}{\rho_{\text{RJ}}} = \frac{y}{e^y - 1} = \frac{4.965114}{e^{4.965114} - 1} = \frac{4.965114}{143.324 - 1} = \frac{4.965114}{142.324} \approx 0.03488
\]
Thus, the classical Rayleigh-Jeans formula overestimates the actual cavity energy density at the solar peak by a factor of:
\[
\frac{\rho_{\text{RJ}}}{\rho_{\text{Planck}}} = \frac{1}{0.03488} \approx 28.67\text{ times}
\]
This demonstrates the complete breakdown of classical equipartition in the visible spectrum."""
            },
            {
                "id": "chem-qc-u1-p2",
                "title": "Problem 2: Photoelectric Stopping Potential & Maximum Kinetic Energy of Potassium",
                "difficulty": "Foundational",
                "statement": r"""Potassium metal has a work function \(\Phi = 2.29\text{ eV}\). Ultraviolet radiation of wavelength \(\lambda = 320\text{ nm}\) irradiates a clean potassium photocathode in high vacuum.
1. Determine the threshold frequency \(\nu_0\) and threshold wavelength \(\lambda_0\) for potassium.
2. Calculate the maximum kinetic energy \(K_{\text{max}}\) (in \(\text{eV}\) and Joules) of the emitted photoelectrons.
3. Calculate the stopping potential \(V_s\) required to bring the photocurrent to zero.
4. Calculate the maximum velocity \(v_{\text{max}}\) of the ejected electrons.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Threshold Frequency and Wavelength
The work function is:
\[
\Phi = 2.29\text{ eV} = 2.29 \times 1.60218 \times 10^{-19}\text{ J} = 3.6690 \times 10^{-19}\text{ J}
\]
The threshold frequency is:
\[
\nu_0 = \frac{\Phi}{h} = \frac{3.6690 \times 10^{-19}\text{ J}}{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}} = 5.537 \times 10^{14}\text{ Hz}
\]
The threshold wavelength is:
\[
\lambda_0 = \frac{c}{\nu_0} = \frac{2.99792 \times 10^8\text{ m/s}}{5.537 \times 10^{14}\text{ s}^{-1}} = 5.414 \times 10^{-7}\text{ m} = 541.4\text{ nm}
\]

---

#### Step 2: Incident Photon Energy and Maximum Kinetic Energy
Energy of incident photon:
\[
E_{\text{photon}} = \frac{h c}{\lambda} = \frac{(6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(2.99792 \times 10^8\text{ m/s})}{320 \times 10^{-9}\text{ m}} = 6.2075 \times 10^{-19}\text{ J}
\]
In electron-volts:
\[
E_{\text{photon}} = \frac{6.2075 \times 10^{-19}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} \approx 3.8744\text{ eV}
\]
Applying Einstein's photoelectric equation:
\[
K_{\text{max}} = E_{\text{photon}} - \Phi = 3.8744\text{ eV} - 2.2900\text{ eV} = 1.5844\text{ eV} \approx 1.584\text{ eV}
\]
In Joules:
\[
K_{\text{max}} = 1.5844 \times 1.60218 \times 10^{-19}\text{ J} = 2.5385 \times 10^{-19}\text{ J}
\]

---

#### Step 3: Stopping Potential
Since \(K_{\text{max}} = e V_s\):
\[
V_s = \frac{K_{\text{max}}}{e} = \frac{1.5844\text{ eV}}{e} = 1.5844\text{ V} \approx 1.58\text{ V}
\]

---

#### Step 4: Maximum Electron Velocity
Using the classical kinetic energy relation (valid since \(K_{\text{max}} \ll m_e c^2 \approx 511\text{ keV}\)):
\[
v_{\text{max}} = \sqrt{\frac{2 K_{\text{max}}}{m_e}} = \sqrt{\frac{2 \times 2.5385 \times 10^{-19}\text{ J}}{9.10938 \times 10^{-31}\text{ kg}}} = \sqrt{5.5734 \times 10^{11}} \approx 7.465 \times 10^5\text{ m/s}
\]"""
            },
            {
                "id": "chem-qc-u1-p3",
                "title": "Problem 3: Compton Scattering Angle, Electron Recoil Energy & Relativistic Kinematics",
                "difficulty": "Intermediate",
                "statement": r"""A beam of monochromatic X-rays with incident wavelength \(\lambda_0 = 0.0500\text{ nm}\) is scattered through an angle \(\theta = 120^\circ\) by quasi-free electrons in a beryllium target.
1. Calculate the wavelength \(\lambda'\) of the Compton scattered X-rays.
2. Determine the kinetic energy \(K_e\) transferred to the recoil electron (in \(\text{eV}\)).
3. Calculate the recoil angle \(\phi\) of the scattered electron relative to the incident photon trajectory.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Wavelength of Scattered X-ray
The Compton formula is:
\[
\lambda' - \lambda_0 = \lambda_C (1 - \cos\theta)
\]
where the electron Compton wavelength is \(\lambda_C = \frac{h}{m_e c} = 2.42631 \times 10^{-12}\text{ m} = 0.0024263\text{ nm}\).
For \(\theta = 120^\circ\):
\[
\cos(120^\circ) = -0.5 \implies 1 - \cos\theta = 1 - (-0.5) = 1.5
\]
The Compton shift is:
\[
\Delta\lambda = 0.0024263\text{ nm} \times 1.5 = 0.0036395\text{ nm}
\]
The scattered wavelength is:
\[
\lambda' = \lambda_0 + \Delta\lambda = 0.0500\text{ nm} + 0.0036395\text{ nm} = 0.05364\text{ nm} = 5.364 \times 10^{-11}\text{ m}
\]

---

#### Step 2: Recoil Electron Kinetic Energy
From conservation of energy:
\[
K_e = E_0 - E' = h c \left( \frac{1}{\lambda_0} - \frac{1}{\lambda'} \right) = h c \frac{\lambda' - \lambda_0}{\lambda_0 \lambda'}
\]
Using \(h c = 1239.84\text{ eV}\cdot\text{nm}\):
\[
E_0 = \frac{1239.84\text{ eV}\cdot\text{nm}}{0.0500\text{ nm}} = 24796.8\text{ eV} = 24.797\text{ keV}
\]
\[
E' = \frac{1239.84\text{ eV}\cdot\text{nm}}{0.0536395\text{ nm}} = 23114.3\text{ eV} = 23.114\text{ keV}
\]
The kinetic energy imparted to the electron is:
\[
K_e = 24796.8\text{ eV} - 23114.3\text{ eV} = 1682.5\text{ eV} \approx 1.683\text{ keV}
\]

---

#### Step 3: Recoil Angle of the Electron
From momentum conservation along the transversal axis (perpendicular to incident photon):
\[
0 = p' \sin\theta - p_e \sin\phi \implies p_e \sin\phi = \frac{h}{\lambda'} \sin\theta
\]
Along the longitudinal axis:
\[
p_0 = p' \cos\theta + p_e \cos\phi \implies p_e \cos\phi = \frac{h}{\lambda_0} - \frac{h}{\lambda'} \cos\theta
\]
Dividing the transverse by longitudinal equations:
\[
\tan\phi = \frac{\frac{1}{\lambda'} \sin\theta}{\frac{1}{\lambda_0} - \frac{1}{\lambda'} \cos\theta} = \frac{\sin\theta}{\left(\frac{\lambda'}{\lambda_0}\right) - \cos\theta}
\]
Substitute \(\sin(120^\circ) = \frac{\sqrt{3}}{2} \approx 0.86603\), \(\cos(120^\circ) = -0.5\), and \(\frac{\lambda'}{\lambda_0} = \frac{0.0536395}{0.0500} = 1.07279\):
\[
\tan\phi = \frac{0.86603}{1.07279 - (-0.5)} = \frac{0.86603}{1.57279} \approx 0.55063
\]
Taking the arctangent:
\[
\phi = \arctan(0.55063) \approx 28.84^\circ
\]"""
            },
            {
                "id": "chem-qc-u1-p4",
                "title": "Problem 4: de Broglie Wavelength of Thermal Neutrons & Macromolecular Crystallography",
                "difficulty": "Intermediate",
                "statement": r"""Thermal neutrons in a research nuclear reactor emerge in thermal equilibrium with heavy water at \(T = 300\text{ K}\).
1. Calculate the root-mean-square momentum \(p_{\text{rms}}\) and the corresponding thermal de Broglie wavelength \(\lambda_{\text{th}}\) of the neutrons (\(m_n = 1.67493 \times 10^{-27}\text{ kg}\)).
2. Compare this wavelength to the covalent bond length of a carbon-carbon single bond (\(d_{\text{C-C}} = 1.54\text{ Å}\)) and explain why thermal neutron diffraction is uniquely suited for locating hydrogen atoms in protein crystallography.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Thermal Root-Mean-Square Momentum & de Broglie Wavelength
From the equipartition theorem for a three-dimensional monoatomic gas:
\[
\langle K \rangle = \frac{p_{\text{rms}}^2}{2 m_n} = \frac{3}{2} k_B T \implies p_{\text{rms}} = \sqrt{3 m_n k_B T}
\]
Substitute \(m_n = 1.67493 \times 10^{-27}\text{ kg}\), \(k_B = 1.38065 \times 10^{-23}\text{ J/K}\), and \(T = 300\text{ K}\):
\[
p_{\text{rms}} = \sqrt{3 \times (1.67493 \times 10^{-27}\text{ kg}) \times (1.38065 \times 10^{-23}\text{ J/K}) \times (300\text{ K})}
\]
\[
p_{\text{rms}} = \sqrt{2.0825 \times 10^{-47}} \approx 4.5634 \times 10^{-24}\text{ kg}\cdot\text{m/s}
\]
The corresponding de Broglie wavelength is:
\[
\lambda_{\text{th}} = \frac{h}{p_{\text{rms}}} = \frac{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}}{4.5634 \times 10^{-24}\text{ kg}\cdot\text{m/s}} \approx 1.452 \times 10^{-10}\text{ m} = 1.452\text{ Å} = 0.1452\text{ nm}
\]

---

#### Step 2: Comparison with Covalent Bond Length and Structural Significance
The thermal neutron wavelength (\(1.452\text{ Å}\)) is remarkably close to the canonical \(\text{C-C}\) single bond length (\(1.54\text{ Å}\)).
- In X-ray crystallography, X-rays scatter off the electron cloud, meaning scattering power scales with atomic number squared (\(Z^2\)). Hydrogen (\(Z = 1\)) scatters X-rays exceptionally weakly compared to carbon (\(Z=6\)), nitrogen (\(Z=7\)), or oxygen (\(Z=8\)), making hydrogen positions notoriously difficult to resolve.
- In neutron diffraction, neutrons scatter off atomic nuclei via the strong nuclear force. The coherent neutron scattering length for hydrogen (\(b_H = -3.74\text{ fm}\)) and deuterium (\(b_D = +6.67\text{ fm}\)) is of the same order of magnitude as carbon (\(b_C = 6.65\text{ fm}\)) and oxygen (\(b_O = 5.80\text{ fm}\)).
- Combined with sub-angstrom thermal wavelengths that avoid radiation damage, thermal neutron diffraction enables precise three-dimensional localization of protonation states in enzyme active sites."""
            },
            {
                "id": "chem-qc-u1-p5",
                "title": "Problem 5: Minimum Uncertainty Product for a Gaussian Wavepacket",
                "difficulty": "Advanced",
                "statement": r"""A particle of mass \(m\) is described by the real normalized ground-state Gaussian wavepacket:
\[
\psi(x) = \left( \frac{2\alpha}{\pi} \right)^{1/4} \exp(-\alpha x^2)
\]
where \(\alpha > 0\) is a real constant.
1. Verify that \(\psi(x)\) is properly normalized on the interval \((-\infty, \infty)\).
2. Calculate the expectation values \(\langle x \rangle\), \(\langle x^2 \rangle\), and evaluate the position uncertainty \(\Delta x\).
3. Calculate the expectation values \(\langle p_x \rangle\), \(\langle p_x^2 \rangle\), and evaluate the momentum uncertainty \(\Delta p_x\).
4. Prove that the uncertainty product \(\Delta x \cdot \Delta p_x\) strictly achieves the minimum theoretical lower bound allowed by the Heisenberg uncertainty principle.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Verification of Normalization
Standard Gaussian integral identity:
\[
\int_{-\infty}^\infty e^{-a x^2} dx = \sqrt{\frac{\pi}{a}}
\]
Evaluate \(\langle \psi | \psi \rangle\):
\[
\int_{-\infty}^\infty |\psi(x)|^2 dx = \left( \frac{2\alpha}{\pi} \right)^{1/2} \int_{-\infty}^\infty e^{-2\alpha x^2} dx = \sqrt{\frac{2\alpha}{\pi}} \cdot \sqrt{\frac{\pi}{2\alpha}} = 1
\]
Hence \(\psi(x)\) is normalized.

---

#### Step 2: Evaluation of \(\Delta x\)
By symmetry, because \(|\psi(x)|^2\) is an even function of \(x\):
\[
\langle x \rangle = \int_{-\infty}^\infty x |\psi(x)|^2 dx = 0
\]
Using the standard Gaussian moment identity \(\int_{-\infty}^\infty x^2 e^{-a x^2} dx = \frac{1}{2a} \sqrt{\frac{\pi}{a}}\) with \(a = 2\alpha\):
\[
\langle x^2 \rangle = \sqrt{\frac{2\alpha}{\pi}} \int_{-\infty}^\infty x^2 e^{-2\alpha x^2} dx = \sqrt{\frac{2\alpha}{\pi}} \cdot \left( \frac{1}{4\alpha} \sqrt{\frac{\pi}{2\alpha}} \right) = \frac{1}{4\alpha}
\]
The spatial standard deviation is:
\[
\Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2} = \sqrt{\frac{1}{4\alpha}} = \frac{1}{2\sqrt{\alpha}}
\]

---

#### Step 3: Evaluation of \(\Delta p_x\)
The momentum operator is \(\hat{p}_x = -i\hbar \frac{d}{dx}\):
\[
\frac{d\psi}{dx} = -2\alpha x \psi(x)
\]
\[
\langle p_x \rangle = -i\hbar \int_{-\infty}^\infty \psi(x) \left( -2\alpha x \psi(x) \right) dx = 0 \quad (\text{integrand is odd})
\]
For \(\langle p_x^2 \rangle = -\hbar^2 \int_{-\infty}^\infty \psi(x) \frac{d^2\psi}{dx^2} dx\), integrating by parts:
\[
\langle p_x^2 \rangle = \hbar^2 \int_{-\infty}^\infty \left| \frac{d\psi}{dx} \right|^2 dx = \hbar^2 \int_{-\infty}^\infty (-2\alpha x \psi)^2 dx = 4 \alpha^2 \hbar^2 \langle x^2 \rangle
\]
Substituting \(\langle x^2 \rangle = \frac{1}{4\alpha}\):
\[
\langle p_x^2 \rangle = 4 \alpha^2 \hbar^2 \left( \frac{1}{4\alpha} \right) = \alpha \hbar^2
\]
The momentum standard deviation is:
\[
\Delta p_x = \sqrt{\langle p_x^2 \rangle - \langle p_x \rangle^2} = \sqrt{\alpha \hbar^2} = \hbar \sqrt{\alpha}
\]

---

#### Step 4: Heisenberg Uncertainty Product
Multiplying the two uncertainties:
\[
\Delta x \cdot \Delta p_x = \left( \frac{1}{2\sqrt{\alpha}} \right) \cdot (\hbar \sqrt{\alpha}) = \frac{\hbar}{2}
\]
The result exactly equals \(\frac{\hbar}{2}\). This proves that the Gaussian wavepacket is the unique state of minimum uncertainty."""
            },
            {
                "id": "chem-qc-u1-p6",
                "title": "Problem 6: Proof of Hermiticity and Commutator Relations for Position and Kinetic Energy",
                "difficulty": "Advanced",
                "statement": r"""1. Prove rigorously that the one-dimensional momentum operator \(\hat{p} = -i\hbar \frac{d}{dx}\) is Hermitian for square-integrable wavefunctions vanishing at infinity (\(\psi(\pm\infty) = 0\)).
2. Evaluate the commutator \([\hat{x}, \hat{T}]\) where \(\hat{T} = \frac{\hat{p}^2}{2m} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2}\) is the kinetic energy operator.
3. Use your result to derive the Ehrenfest theorem expression for the time evolution of the position expectation value \(\frac{d\langle x \rangle}{dt}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Proof of Hermiticity of \(\hat{p}\)
To be Hermitian, \(\hat{p}\) must satisfy:
\[
\langle \phi | \hat{p} \psi \rangle = \langle \hat{p} \phi | \psi \rangle \iff \int_{-\infty}^\infty \phi^* \left(-i\hbar \frac{d\psi}{dx}\right) dx = \int_{-\infty}^\infty \left(-i\hbar \frac{d\phi}{dx}\right)^* \psi dx
\]
Evaluate the left-hand integral using integration by parts:
\[
\int_{-\infty}^\infty \phi^* \left(-i\hbar \frac{d\psi}{dx}\right) dx = -i\hbar \left[ \phi^* \psi \right]_{-\infty}^\infty - (-i\hbar) \int_{-\infty}^\infty \frac{d\phi^*}{dx} \psi dx
\]
Because \(\phi, \psi \in L^2(\mathbb{R})\), the boundary term vanishes: \(\left[ \phi^* \psi \right]_{-\infty}^\infty = 0\).
Now rewrite the remaining integral:
\[
i\hbar \int_{-\infty}^\infty \frac{d\phi^*}{dx} \psi dx = \int_{-\infty}^\infty \left( -i\hbar \frac{d\phi}{dx} \right)^* \psi dx = \langle \hat{p}\phi | \psi \rangle
\]
Hence \(\hat{p}^\dagger = \hat{p}\), proving that the momentum operator is Hermitian.

---

#### Step 2: Evaluation of \([\hat{x}, \hat{T}]\)
The kinetic energy operator is \(\hat{T} = \frac{\hat{p}^2}{2m}\).
Using the commutator identity \([\hat{A}, \hat{B}\hat{C}] = [\hat{A}, \hat{B}]\hat{C} + \hat{B}[\hat{A}, \hat{C}]\):
\[
[\hat{x}, \hat{p}^2] = [\hat{x}, \hat{p}]\hat{p} + \hat{p}[\hat{x}, \hat{p}]
\]
Since the canonical commutator is \([\hat{x}, \hat{p}] = i\hbar \hat{I}\):
\[
[\hat{x}, \hat{p}^2] = (i\hbar)\hat{p} + \hat{p}(i\hbar) = 2i\hbar \hat{p}
\]
Therefore:
\[
[\hat{x}, \hat{T}] = \frac{1}{2m} [\hat{x}, \hat{p}^2] = \frac{1}{2m} (2i\hbar \hat{p}) = \frac{i\hbar}{m} \hat{p}
\]

---

#### Step 3: Ehrenfest's Theorem for \(\frac{d\langle x \rangle}{dt}\)
For any time-independent operator \(\hat{A}\), the general equation of motion for expectation values is:
\[
\frac{d\langle \hat{A} \rangle}{dt} = \frac{i}{\hbar} \langle [\hat{H}, \hat{A}] \rangle
\]
For position \(\hat{A} = \hat{x}\) in a local potential \(\hat{H} = \hat{T} + V(\hat{x})\):
Since \([\hat{x}, V(\hat{x})] = 0\):
\[
[\hat{H}, \hat{x}] = [\hat{T}, \hat{x}] = -[\hat{x}, \hat{T}] = -\frac{i\hbar}{m} \hat{p}
\]
Substitute into Ehrenfest's theorem:
\[
\frac{d\langle x \rangle}{dt} = \frac{i}{\hbar} \left\langle -\frac{i\hbar}{m} \hat{p} \right\rangle = \frac{\langle p \rangle}{m}
\]
This reproduces the classical kinematic velocity relation \(\frac{dx}{dt} = \frac{p}{m}\)."""
            },
            {
                "id": "chem-qc-u1-p7",
                "title": "Problem 7: Non-Stationary State Superposition Dynamics & Bohr Beat Frequency",
                "difficulty": "Advanced",
                "statement": r"""A quantum particle in a one-dimensional system is prepared at \(t = 0\) in a normalized non-stationary state consisting of an equal linear superposition of the ground state \(\psi_1(x)\) (energy \(E_1\)) and first excited state \(\psi_2(x)\) (energy \(E_2\)):
\[
\Psi(x, 0) = \frac{1}{\sqrt{2}} \psi_1(x) + \frac{1}{\sqrt{2}} \psi_2(x)
\]
1. Write the full time-dependent state \(\Psi(x, t)\).
2. Derive the time-dependent probability density \(P(x, t) = |\Psi(x, t)|^2\) and identify the oscillation frequency \(\omega_{21}\).
3. If \(E_1 = 2.0\text{ eV}\) and \(E_2 = 5.5\text{ eV}\), calculate the beat frequency \(\nu_{21}\) (in THz) and oscillation period \(T_{\text{osc}}\) (in fs).
4. Evaluate the expectation value of the Hamiltonian \(\langle \hat{H} \rangle\) as a function of time.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Time-Dependent Wavefunction
Each stationary eigenstate evolves with its phase factor \(\exp(-i E_n t / \hbar)\):
\[
\Psi(x, t) = \frac{1}{\sqrt{2}} \psi_1(x) e^{-i E_1 t / \hbar} + \frac{1}{\sqrt{2}} \psi_2(x) e^{-i E_2 t / \hbar}
\]

---

#### Step 2: Probability Density & Beat Frequency
Taking the squared modulus:
\[
P(x, t) = \Psi^*(x, t) \Psi(x, t)
\]
\[
P(x, t) = \left( \frac{1}{\sqrt{2}} \psi_1^* e^{i E_1 t / \hbar} + \frac{1}{\sqrt{2}} \psi_2^* e^{i E_2 t / \hbar} \right) \left( \frac{1}{\sqrt{2}} \psi_1 e^{-i E_1 t / \hbar} + \frac{1}{\sqrt{2}} \psi_2 e^{-i E_2 t / \hbar} \right)
\]
Assuming real spatial eigenfunctions \(\psi_1, \psi_2\):
\[
P(x, t) = \frac{1}{2} \psi_1^2(x) + \frac{1}{2} \psi_2^2(x) + \frac{1}{2} \psi_1(x) \psi_2(x) \left( e^{-i (E_2 - E_1) t / \hbar} + e^{i (E_2 - E_1) t / \hbar} \right)
\]
Using Euler's identity \(e^{i\theta} + e^{-i\theta} = 2\cos\theta\):
\[
P(x, t) = \frac{1}{2} \psi_1^2(x) + \frac{1}{2} \psi_2^2(x) + \psi_1(x) \psi_2(x) \cos(\omega_{21} t)
\]
where the Bohr transition angular frequency is:
\[
\omega_{21} = \frac{E_2 - E_1}{\hbar}
\]

---

#### Step 3: Numerical Beat Frequency and Period
Given:
\[
\Delta E = E_2 - E_1 = 5.5\text{ eV} - 2.0\text{ eV} = 3.5\text{ eV} = 3.5 \times 1.60218 \times 10^{-19}\text{ J} = 5.6076 \times 10^{-19}\text{ J}
\]
The linear oscillation frequency is:
\[
\nu_{21} = \frac{\Delta E}{h} = \frac{5.6076 \times 10^{-19}\text{ J}}{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}} \approx 8.463 \times 10^{14}\text{ Hz} = 846.3\text{ THz}
\]
The oscillation period is:
\[
T_{\text{osc}} = \frac{1}{\nu_{21}} = \frac{1}{8.463 \times 10^{14}\text{ s}^{-1}} \approx 1.182 \times 10^{-15}\text{ s} = 1.182\text{ fs}
\]

---

#### Step 4: Expectation Value of Energy
\[
\langle \hat{H} \rangle = \int \Psi^*(x, t) \hat{H} \Psi(x, t) dx
\]
Since \(\hat{H} \psi_n = E_n \psi_n\) and \(\langle \psi_m | \psi_n \rangle = \delta_{mn}\):
\[
\langle \hat{H} \rangle = |c_1|^2 E_1 + |c_2|^2 E_2 = \left(\frac{1}{\sqrt{2}}\right)^2 E_1 + \left(\frac{1}{\sqrt{2}}\right)^2 E_2 = \frac{E_1 + E_2}{2}
\]
\[
\langle \hat{H} \rangle = \frac{2.0\text{ eV} + 5.5\text{ eV}}{2} = 3.75\text{ eV}
\]
The energy expectation value is completely independent of time, demonstrating energy conservation in isolated quantum systems."""
            }
        ]
    }
    units.append(unit1)

    # =========================================================================
    # UNIT 2: Exact Quantum Models I: Particle in a Box & Ring
    # =========================================================================
    unit2 = {
        "id": "unit-2",
        "unitNumber": 2,
        "title": "Unit 2: Exact Quantum Models I: Particle in a Box & Ring",
        "leadSummary": r"""Rigorous quantum mechanical formulation of bounded particle models: the one-dimensional infinite potential well, Dirichlet boundary conditions, energy quantization, zero-point energy, symmetry-enforced parity, extension to 2D and 3D cuboidal and cubic boxes, spatial degeneracy, density of states, electron on a ring under periodic boundary conditions, angular momentum quantization, and the Free Electron Molecular Orbital (FEMO) model applied to conjugated polyenes and aromatic systems.""",
        "simulations": [
            "sim_qc_particle_box_ring_quantum"
        ],
        "sections": [
            {
                "id": "sec-2-1",
                "secNumber": "2.1",
                "title": "One-Dimensional Infinite Potential Well: Boundary Conditions & Quantization",
                "content": r"""The particle in a one-dimensional box represents the simplest exact solvable quantum system exhibiting boundary-condition-induced energy quantization.

### Mathematical Formulation
A point particle of mass \(m\) is constrained to move along the \(x\)-axis between rigid boundaries at \(x = 0\) and \(x = L\). The potential energy function is:
\[
V(x) = \begin{cases} 0 & 0 < x < L \\ \infty & x \le 0 \text{ or } x \ge L \end{cases}
\]
Inside the box (\(0 < x < L\)), the TISE is:
\[
-\frac{\hbar^2}{2m} \frac{d^2\psi(x)}{dx^2} = E \psi(x) \implies \frac{d^2\psi(x)}{dx^2} + k^2 \psi(x) = 0
\]
where the wavenumber is \(k = \frac{\sqrt{2mE}}{\hbar}\). The general solution is:
\[
\psi(x) = A \sin(kx) + B \cos(kx)
\]

### Application of Dirichlet Boundary Conditions
To prevent infinite potential energy, the wavefunction must vanish identically outside the well: \(\psi(x) = 0\) for \(x \le 0\) and \(x \ge L\). Continuity requires:
1. **At \(x = 0\):**
   \[
   \psi(0) = A \sin(0) + B \cos(0) = B = 0
   \]
   Thus, \(\psi(x) = A \sin(kx)\).
2. **At \(x = L\):**
   \[
   \psi(L) = A \sin(k L) = 0
   \]
   To avoid the trivial solution \(\psi(x) \equiv 0\) (no particle exists), we require:
   \[
   k L = n \pi, \quad n \in \{1, 2, 3, \dots\}
   \]
   The quantum number \(n = 0\) is disallowed because it yields \(\psi(x) \equiv 0\), violating normalization. Negative integers \(n < 0\) yield identical physical states up to an unobservable global phase factor (\(\sin(-x) = -\sin(x)\)).

### Quantized Energy Eigenvalues
Equating \(k = \frac{n\pi}{L} = \frac{\sqrt{2mE}}{\hbar}\) yields the quantized energy spectrum:
\[
E_n = \frac{n^2 \pi^2 \hbar^2}{2 m L^2} = \frac{n^2 h^2}{8 m L^2}, \quad n = 1, 2, 3, \dots
\]

### Normalization of Eigenfunctions
Integrating the probability density over the box:
\[
\int_0^L |\psi_n(x)|^2 dx = |A|^2 \int_0^L \sin^2\left(\frac{n\pi x}{L}\right) dx = |A|^2 \frac{L}{2} = 1 \implies A = \sqrt{\frac{2}{L}}
\]
Thus, the normalized stationary eigenfunctions are:
\[
\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)
\]

### Physical Hallmarks
- **Zero-Point Energy:** The ground state (\(n = 1\)) has non-zero energy \(E_1 = \frac{h^2}{8 m L^2} > 0\). A particle confined to a finite domain cannot be at rest (\(E = 0\)), as having zero energy would imply \(\Delta p = 0\) while \(\Delta x \le L\), violating \(\Delta x \cdot \Delta p \ge \hbar/2\).
- **Nodal Structure:** State \(\psi_n(x)\) has exactly \(n - 1\) internal nodes (zeros inside the box). Higher kinetic energy directly correlates with higher spatial curvature (\(d^2\psi/dx^2\)) and more nodes.
- **Classical Correspondence:** As \(n \rightarrow \infty\), the spacing between successive nodes becomes microscopic. The rapid spatial oscillation averages out such that \(\langle |\psi_n(x)|^2 \rangle \approx 1/L\), recovering the classical uniform probability distribution (Bohr's correspondence principle)."""
            },
            {
                "id": "sec-2-2",
                "secNumber": "2.2",
                "title": "Symmetry, Parity & The Symmetric Infinite Well",
                "content": r"""Choosing coordinate origins that exploit physical symmetries greatly simplifies matrix element evaluations and reveals conservation laws.

### The Center-Symmetric Box
Let the box be centered at the origin, spanning the interval \([-a, +a]\) with total width \(L = 2a\). The potential is:
\[
V(x) = \begin{cases} 0 & -a < x < a \\ \infty & |x| \ge a \end{cases}
\]
Notice that the Hamiltonian is invariant under spatial inversion (parity operator \(\hat{\Pi} x = -x\)):
\[
\hat{H}(-x) = \hat{H}(x) \implies [\hat{H}, \hat{\Pi}] = 0
\]
Because \(\hat{H}\) and \(\hat{\Pi}\) commute, the non-degenerate stationary states must be simultaneous eigenfunctions of parity with eigenvalues \(\pm 1\):
\[
\psi(-x) = \pm \psi(x)
\]

### Solving the Symmetric Well
The general solution inside the well is:
\[
\psi(x) = A \cos(kx) + B \sin(kx)
\]
1. **Even Parity Solutions (\(\psi(-x) = +\psi(x) \implies B = 0\)):**
   Boundary condition at \(x = \pm a\):
   \[
   \cos(k a) = 0 \implies k a = \frac{n \pi}{2}, \quad n = 1, 3, 5, \dots
   \]
   \[
   \psi_n(x) = \frac{1}{\sqrt{a}} \cos\left(\frac{n\pi x}{2a}\right), \quad n = 1, 3, 5, \dots
   \]
2. **Odd Parity Solutions (\(\psi(-x) = -\psi(x) \implies A = 0\)):**
   Boundary condition at \(x = \pm a\):
   \[
   \sin(k a) = 0 \implies k a = \frac{n \pi}{2}, \quad n = 2, 4, 6, \dots
   \]
   \[
   \psi_n(x) = \frac{1}{\sqrt{a}} \sin\left(\frac{n\pi x}{2a}\right), \quad n = 2, 4, 6, \dots
   \]
Combining both branches with \(L = 2a\):
\[
E_n = \frac{n^2 \pi^2 \hbar^2}{2 m (2a)^2} = \frac{n^2 h^2}{8 m L^2}, \quad n = 1, 2, 3, \dots
\]
The energy spectrum is identical, but the alternating even/odd parity character drastically simplifies dipole transition selection rules: \(\langle \psi_m | \hat{x} | \psi_n \rangle = 0\) whenever \(m\) and \(n\) possess identical parity."""
            },
            {
                "id": "sec-2-3",
                "secNumber": "2.3",
                "title": "Two- and Three-Dimensional Boxes: Separation of Variables & Degeneracy",
                "content": r"""Extending confinement to higher spatial dimensions introduces the concept of quantum degeneracy, where multiple distinct wavefunctions share identical energy eigenvalues.

### The Three-Dimensional Rectangular Box
Consider a particle of mass \(m\) confined within a 3D cuboidal cavity of dimensions \(L_x, L_y, L_z\):
\[
V(x, y, z) = \begin{cases} 0 & 0 < x < L_x, \ 0 < y < L_y, \ 0 < z < L_z \\ \infty & \text{otherwise} \end{cases}
\]
Inside the box, the TISE is:
\[
-\frac{\hbar^2}{2m} \left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} \right) \psi(x, y, z) = E \psi(x, y, z)
\]
Using separation of variables \(\psi(x, y, z) = X(x) Y(y) Z(z)\):
\[
-\frac{\hbar^2}{2m} \left( \frac{X''}{X} + \frac{Y''}{Y} + \frac{Z''}{Z} \right) = E
\]
Each independent coordinate satisfies an identical 1D equation:
\[
-\frac{\hbar^2}{2m} X''(x) = E_x X(x), \quad -\frac{\hbar^2}{2m} Y''(y) = E_y Y(y), \quad -\frac{\hbar^2}{2m} Z''(z) = E_z Z(z)
\]
with \(E = E_x + E_y + E_z\).

### Quantized Eigenvalues and Wavefunctions
Applying Dirichlet boundary conditions on each axis:
\[
\psi_{n_x, n_y, n_z}(x, y, z) = \sqrt{\frac{8}{L_x L_y L_z}} \sin\left(\frac{n_x \pi x}{L_x}\right) \sin\left(\frac{n_y \pi y}{L_y}\right) \sin\left(\frac{n_z \pi z}{L_z}\right)
\]
\[
E_{n_x, n_y, n_z} = \frac{h^2}{8m} \left( \frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2} \right), \quad n_x, n_y, n_z \in \{1, 2, 3, \dots\}
\]

### Symmetry and Systematic Degeneracy in a Cubic Box
When the box possesses cubic symmetry (\(L_x = L_y = L_z = L\)):
\[
E_{n_x, n_y, n_z} = \frac{h^2}{8 m L^2} (n_x^2 + n_y^2 + n_z^2)
\]
1. **Ground State (1, 1, 1):**
   \(E_{1,1,1} = 3 \frac{h^2}{8mL^2}\). Non-degenerate (degeneracy \(g = 1\)).
2. **First Excited State (2, 1, 1), (1, 2, 1), (1, 1, 2):**
   \(E = (4 + 1 + 1) \frac{h^2}{8mL^2} = 6 \frac{h^2}{8mL^2}\). Three distinct states share identical energy; **triply degenerate** (\(g = 3\)).
3. **Second Excited State (2, 2, 1), (2, 1, 2), (1, 2, 2):**
   \(E = (4 + 4 + 1) \frac{h^2}{8mL^2} = 9 \frac{h^2}{8mL^2}\). Triply degenerate (\(g = 3\)).
4. **Accidental Degeneracy:**
   Higher energy levels may exhibit degeneracies not dictated by cubic spatial symmetry alone. For example, \((3, 3, 3)\) with \(n_x^2 + n_y^2 + n_z^2 = 27\) can mix with different sums of three squares, termed *accidental degeneracy*."""
            },
            {
                "id": "sec-2-4",
                "secNumber": "2.4",
                "title": "Electron in a Ring: Periodic Boundary Conditions & Aromaticity",
                "content": r"""When a particle is constrained to move along a circular path of radius \(R\), the spatial domain is closed and continuous, replacing Dirichlet boundary conditions with **periodic boundary conditions**.

### The Schrödinger Equation in Polar Coordinates
Consider an electron of mass \(m\) moving on a planar circular ring of radius \(R\) (circumference \(L = 2\pi R\)) in the \(xy\)-plane with \(V(\phi) = 0\). The arc length coordinate is \(s = R \phi\).
The kinetic energy operator in angular coordinate \(\phi\) is:
\[
\hat{H} = -\frac{\hbar^2}{2m R^2} \frac{d^2}{d\phi^2} = -\frac{\hbar^2}{2 I} \frac{d^2}{d\phi^2}
\]
where \(I = m R^2\) is the moment of inertia. The TISE is:
\[
-\frac{\hbar^2}{2 I} \frac{d^2\psi(\phi)}{d\phi^2} = E \psi(\phi) \implies \frac{d^2\psi(\phi)}{d\phi^2} + m_l^2 \psi(\phi) = 0
\]
where \(m_l = \frac{\sqrt{2 I E}}{\hbar}\). The general solution is:
\[
\psi(\phi) = A e^{i m_l \phi} + B e^{-i m_l \phi}
\]

### Periodic Boundary Conditions
Because \(\phi\) and \(\phi + 2\pi\) represent the identical physical point in space:
\[
\psi(\phi + 2\pi) = \psi(\phi) \implies e^{i m_l (\phi + 2\pi)} = e^{i m_l \phi} \implies e^{i 2\pi m_l} = 1
\]
Euler's identity requires:
\[
m_l \in \{0, \pm 1, \pm 2, \pm 3, \dots\}
\]
Notice that \(m_l = 0\) is physically allowed here (unlike the 1D box) because \(e^0 = 1\) is non-zero and normalizable.

### Quantized Energy Levels & Degeneracy
The energy eigenvalues are:
\[
E_{m_l} = \frac{m_l^2 \hbar^2}{2 I} = \frac{m_l^2 \hbar^2}{2 m R^2}
\]
- Ground state (\(m_l = 0\)): \(E_0 = 0\). The electron has zero angular momentum and zero zero-point energy (non-degenerate, \(g = 1\)).
- Excited states (\(|m_l| \ge 1\)): Every energy level is **doubly degenerate** (\(g = 2\)) corresponding to clockwise (\(+m_l\)) and counter-clockwise (\(-m_l\)) circulating currents.

### Normalization
\[
\int_0^{2\pi} |\psi(\phi)|^2 d\phi = |A|^2 \int_0^{2\pi} d\phi = 2\pi |A|^2 = 1 \implies A = \frac{1}{\sqrt{2\pi}}
\]
Thus:
\[
\psi_{m_l}(\phi) = \frac{1}{\sqrt{2\pi}} e^{i m_l \phi}
\]
These functions are simultaneous eigenfunctions of the \(z\)-component of orbital angular momentum:
\[
\hat{L}_z = -i\hbar \frac{\partial}{\partial \phi} \implies \hat{L}_z \psi_{m_l}(\phi) = m_l \hbar \psi_{m_l}(\phi)
\]"""
            },
            {
                "id": "sec-2-5",
                "secNumber": "2.5",
                "title": "Free Electron Molecular Orbital (FEMO) Model for Conjugated Polyenes",
                "content": r"""The Free Electron Molecular Orbital (FEMO) model, developed by Hans Kuhn (1949), treats \(\pi\)-electrons in conjugated polyenes as independent particles in an effective one-dimensional box.

### Physical Model Assumptions
In a conjugated polyene \(\text{H}_2\text{C}=\text{CH}-(\text{CH}=\text{CH})_k-\text{CH}=\text{CH}_2\) containing \(N\) conjugated carbon atoms:
1. The \(\sigma\)-bonding skeleton provides a uniform, flat potential well of length \(L\).
2. The \(N\) \(\pi\)-electrons move freely along the carbon backbone without inter-electronic repulsion.
3. The box length \(L\) is approximated by the sum of carbon-carbon bond lengths plus boundary extensions \(\delta\) at the terminal carbons (accounting for \(\pi\)-cloud spill-over):
   \[
   L = (N - 1) d_{\text{C-C}} + 2 \delta \approx N d_{\text{avg}}
   \]
   where \(d_{\text{avg}} \approx 1.39 - 1.40\text{ Å}\) is the average resonant \(\text{C-C}\) bond distance.

### Aufbau Principle & HOMO-LUMO Transition
According to the Pauli exclusion principle, each spatial orbital \(\psi_n\) accommodates at most two electrons with antiparallel spins (\(m_s = \pm 1/2\)).
For an even number of \(\pi\)-electrons \(N\):
- The Highest Occupied Molecular Orbital (HOMO) corresponds to quantum number:
  \[
  n_{\text{HOMO}} = \frac{N}{2}
  \]
- The Lowest Unoccupied Molecular Orbital (LUMO) corresponds to quantum number:
  \[
  n_{\text{LUMO}} = \frac{N}{2} + 1
  \]
The lowest-energy electronic absorption transition is the \(\text{HOMO} \rightarrow \text{LUMO}\) excitation:
\[
\Delta E = E_{\text{LUMO}} - E_{\text{HOMO}} = \frac{h^2}{8 m_e L^2} \left[ \left(\frac{N}{2} + 1\right)^2 - \left(\frac{N}{2}\right)^2 \right] = \frac{h^2}{8 m_e L^2} (N + 1)
\]
Expressing the absorption wavelength \(\lambda\):
\[
\Delta E = \frac{h c}{\lambda} \implies \lambda = \frac{8 m_e c L^2}{h (N + 1)}
\]
Substituting \(L \approx N d\):
\[
\lambda \approx \frac{8 m_e c d^2}{h} \frac{N^2}{N + 1}
\]
As conjugation length \(N\) increases, \(\lambda\) shifts bathochromically into the visible spectrum, explaining the intense colors of carotenoids (\(\beta\)-carotene, \(N=22\), orange) and cyanine dyes."""
            },
            {
                "id": "sec-2-6",
                "secNumber": "2.6",
                "title": "Quantum Mechanical Tunneling: Finite Potential Wells & Barriers",
                "content": r"""When the potential walls have finite height \(V_0 < \infty\), quantum wavefunctions penetrate into classically forbidden regions where \(E < V(x)\), giving rise to quantum mechanical tunneling.

### The Finite One-Dimensional Square Well
Consider a particle of mass \(m\) in a finite well:
\[
V(x) = \begin{cases} 0 & -a \le x \le a \\ V_0 & |x| > a \end{cases}
\]
For bound states with \(0 < E < V_0\):
- **Inside the Well (\(|x| < a\)):**
  \[
  \frac{d^2\psi}{dx^2} + k^2 \psi = 0, \quad k = \frac{\sqrt{2mE}}{\hbar}
  \]
  Solutions are oscillatory: \(\cos(kx)\) (even) or \(\sin(kx)\) (odd).
- **Outside the Well (\(|x| > a\)):**
  \[
  \frac{d^2\psi}{dx^2} - \kappa^2 \psi = 0, \quad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}
  \]
  Solutions are exponentially decaying evanescent waves:
  \[
  \psi(x) = C e^{-\kappa x} \quad (x > a), \quad \psi(x) = C e^{+\kappa x} \quad (x < -a)
  \]

### Continuity Conditions and Penetration Depth
Matching \(\psi(x)\) and its first derivative \(\psi'(x)\) at the boundary \(x = a\) for even states yields:
\[
k \tan(k a) = \kappa
\]
The characteristic penetration depth \(\delta\) where the wavefunction decays to \(1/e\) of its boundary value is:
\[
\delta = \frac{1}{\kappa} = \frac{\hbar}{\sqrt{2m(V_0 - E)}}
\]
Because \(\psi(x) \neq 0\) outside the well, there is a finite probability of finding the particle in the classically forbidden zone.

### Rectangular Potential Barrier & Transmission Coefficient
For a barrier of width \(L\) and height \(V_0 > E\), the quantum transmission coefficient (tunneling probability) is:
\[
T = \frac{1}{1 + \frac{V_0^2}{4 E (V_0 - E)} \sinh^2(\kappa L)}
\]
In the thick/high barrier limit (\(\kappa L \gg 1\)):
\[
T \approx 16 \frac{E}{V_0} \left(1 - \frac{E}{V_0}\right) \exp(-2\kappa L)
\]
Tunneling probability decays exponentially with barrier width \(L\) and the square root of particle mass \(\sqrt{m}\). This explains why proton tunneling occurs readily in enzyme active sites and ammonia inversion, whereas deuteron tunneling is suppressed by an order of magnitude."""
            },
            {
                "id": "sec-2-7",
                "secNumber": "2.7",
                "title": "Density of States & Transition to the Classical Continuum",
                "content": r"""In macroscopic condensed matter and statistical mechanics, quantum systems contain billions of closely spaced energy levels, requiring a continuous **density of states** representation.

### Derivation of the Density of States in 3D
For a particle in a 3D cubic box of volume \(V = L^3\), the energy levels satisfy:
\[
E = \frac{h^2}{8 m L^2} (n_x^2 + n_y^2 + n_z^2) = \frac{\hbar^2 \pi^2}{2 m L^2} n^2
\]
where \(n^2 = n_x^2 + n_y^2 + n_z^2\).
In the three-dimensional quantum number space \((n_x, n_y, n_z)\), each quantum state occupies a unit volume of \(1 \times 1 \times 1 = 1\). Because \(n_x, n_y, n_z > 0\), the states are restricted to the positive octant (\(1/8\) of a sphere).
The total number of states with radius less than \(n\) is:
\[
N(E) = \frac{1}{8} \left( \frac{4}{3} \pi n^3 \right) = \frac{\pi}{6} n^3
\]
Expressing \(n\) in terms of energy \(E\):
\[
n = \frac{L}{\pi \hbar} \sqrt{2 m E} \implies N(E) = \frac{\pi}{6} \left( \frac{L}{\pi \hbar} \sqrt{2m E} \right)^3 = \frac{V}{6\pi^2 \hbar^3} (2m E)^{3/2}
\]
The **density of states** \(g(E) = \frac{dN}{dE}\) is the number of available quantum states per unit energy:
\[
g(E) = \frac{dN}{dE} = \frac{V}{4\pi^2 \hbar^3} (2m)^{3/2} E^{1/2} = \frac{2\pi V}{h^3} (2m)^{3/2} \sqrt{E}
\]

### Dimensionality and Density of States Scaling
The energy dependence of the density of states depends fundamentally on the spatial dimensionality \(d\) of confinement:
- **3D Bulk:** \(g(E) \propto E^{1/2}\) (continuous parabolic increase)
- **2D Quantum Well:** \(g(E) \propto E^0 = \text{constant}\) (step-like staircase)
- **1D Quantum Wire:** \(g(E) \propto E^{-1/2}\) (van Hove singularities)
- **0D Quantum Dot:** \(g(E) = \sum_i \delta(E - E_i)\) (discrete delta peaks)
This dimensional scaling underpins semiconductor quantum well lasers, carbon nanotubes, and colloidal nanocrystal quantum dots."""
            }
        ],
        "problems": [
            {
                "id": "chem-qc-u2-p1",
                "title": "Problem 1: Ground State & Excitation Energies for an Electron in a Nanoscale Well",
                "difficulty": "Foundational",
                "statement": r"""An electron is trapped in a one-dimensional infinite potential well of width \(L = 0.500\text{ nm}\).
1. Calculate the ground-state zero-point energy \(E_1\) in Joules and electron-volts (\(\text{eV}\)).
2. Determine the energy of the first two excited states (\(E_2\) and \(E_3\)).
3. Calculate the wavelength \(\lambda\) of the photon absorbed when the electron undergoes a transition from \(n = 1 \rightarrow n = 2\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Ground-State Zero-Point Energy
The energy levels for a 1D infinite well are:
\[
E_n = \frac{n^2 h^2}{8 m_e L^2}
\]
Substitute \(n = 1\), \(h = 6.62607 \times 10^{-34}\text{ J}\cdot\text{s}\), \(m_e = 9.10938 \times 10^{-31}\text{ kg}\), and \(L = 0.500 \times 10^{-9}\text{ m}\):
\[
E_1 = \frac{(1)^2 (6.62607 \times 10^{-34}\text{ J}\cdot\text{s})^2}{8 (9.10938 \times 10^{-31}\text{ kg})(0.500 \times 10^{-9}\text{ m})^2}
\]
\[
E_1 = \frac{4.39048 \times 10^{-67}}{1.82188 \times 10^{-48}} = 2.40986 \times 10^{-19}\text{ J}
\]
In electron-volts:
\[
E_1 = \frac{2.40986 \times 10^{-19}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} \approx 1.5041\text{ eV} \approx 1.504\text{ eV}
\]

---

#### Step 2: Excited State Energies
Since \(E_n = n^2 E_1\):
- For \(n = 2\):
  \[
  E_2 = 2^2 E_1 = 4 \times 1.5041\text{ eV} = 6.0164\text{ eV} \approx 6.016\text{ eV}
  \]
- For \(n = 3\):
  \[
  E_3 = 3^2 E_1 = 9 \times 1.5041\text{ eV} = 13.5369\text{ eV} \approx 13.537\text{ eV}
  \]

---

#### Step 3: Transition Wavelength for \(n = 1 \rightarrow 2\)
The transition energy is:
\[
\Delta E = E_2 - E_1 = 3 E_1 = 3 \times 2.40986 \times 10^{-19}\text{ J} = 7.22958 \times 10^{-19}\text{ J} = 4.5123\text{ eV}
\]
The absorbed photon wavelength is:
\[
\lambda = \frac{h c}{\Delta E} = \frac{(6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(2.99792 \times 10^8\text{ m/s})}{7.22958 \times 10^{-19}\text{ J}} \approx 2.7476 \times 10^{-7}\text{ m} = 274.8\text{ nm}
\]
This transition lies in the near-ultraviolet spectrum."""
            },
            {
                "id": "chem-qc-u2-p2",
                "title": "Problem 2: Spatial Probability Integration & Central Region Locality",
                "difficulty": "Foundational",
                "statement": r"""For a particle in a one-dimensional box of length \(L\) in its ground state \(\psi_1(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{\pi x}{L}\right)\):
1. Calculate the probability of finding the particle in the central third of the box, \(x \in [L/3, 2L/3]\).
2. Compare this result to the classical probability for a uniform distribution and explain the physical difference.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Quantum Probability Calculation
The probability is given by integrating \(|\psi_1(x)|^2\):
\[
P = \int_{L/3}^{2L/3} |\psi_1(x)|^2 dx = \frac{2}{L} \int_{L/3}^{2L/3} \sin^2\left(\frac{\pi x}{L}\right) dx
\]
Using the trigonometric identity \(\sin^2\theta = \frac{1 - \cos(2\theta)}{2}\):
\[
P = \frac{2}{L} \int_{L/3}^{2L/3} \frac{1 - \cos\left(\frac{2\pi x}{L}\right)}{2} dx = \frac{1}{L} \left[ x - \frac{L}{2\pi} \sin\left(\frac{2\pi x}{L}\right) \right]_{L/3}^{2L/3}
\]
Evaluate at the upper limit \(x = 2L/3\):
\[
\text{Upper} = \frac{2L}{3} - \frac{L}{2\pi} \sin\left(\frac{4\pi}{3}\right) = \frac{2L}{3} - \frac{L}{2\pi} \left(-\frac{\sqrt{3}}{2}\right) = \frac{2L}{3} + \frac{\sqrt{3} L}{4\pi}
\]
Evaluate at the lower limit \(x = L/3\):
\[
\text{Lower} = \frac{L}{3} - \frac{L}{2\pi} \sin\left(\frac{2\pi}{3}\right) = \frac{L}{3} - \frac{L}{2\pi} \left(\frac{\sqrt{3}}{2}\right) = \frac{L}{3} - \frac{\sqrt{3} L}{4\pi}
\]
Subtracting the lower limit from the upper limit:
\[
P = \frac{1}{L} \left[ \left(\frac{2L}{3} - \frac{L}{3}\right) + \frac{\sqrt{3} L}{2\pi} \right] = \frac{1}{L} \left[ \frac{L}{3} + \frac{\sqrt{3} L}{2\pi} \right] = \frac{1}{3} + \frac{\sqrt{3}}{2\pi}
\]
Evaluating numerically:
\[
P \approx 0.33333 + \frac{1.73205}{6.28318} = 0.33333 + 0.27566 = 0.60899 \approx 0.609\text{ (or } 60.9\%\text{)}
\]

---

#### Step 2: Classical Comparison
For a classical particle bouncing back and forth at constant speed:
\[
P_{\text{class}} = \frac{\Delta x}{L} = \frac{2L/3 - L/3}{L} = \frac{1}{3} \approx 0.333\text{ (or } 33.3\%\text{)}
\]
The quantum probability (\(60.9\%\)) is nearly double the classical expectation because the ground-state wavefunction forms a standing half-wave with maximum probability amplitude at the center of the well (\(x = L/2\))."""
            },
            {
                "id": "chem-qc-u2-p3",
                "title": "Problem 3: Degeneracy and Level Spectrum in a 2D Square Box",
                "difficulty": "Intermediate",
                "statement": r"""A particle of mass \(m\) is confined within a two-dimensional square box of length \(L\) along both \(x\) and \(y\).
1. Write the expression for the energy levels \(E_{n_x, n_y}\) in units of \(E_0 = \frac{h^2}{8 m L^2}\).
2. Determine the energies and degeneracies of the lowest six energy levels.
3. If the square well is deformed into a rectangle with \(L_x = L\) and \(L_y = 2L\), calculate the new energies of the states that were originally degenerate with \(n_x^2 + n_y^2 = 5\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Energy Level Expression for 2D Square Box
\[
E_{n_x, n_y} = \frac{h^2}{8 m L^2} (n_x^2 + n_y^2) = E_0 (n_x^2 + n_y^2), \quad n_x, n_y \in \{1, 2, 3, \dots\}
\]

---

#### Step 2: Lowest Six Energy Levels and Degeneracies
Listing states by increasing values of \(n_x^2 + n_y^2\):
1. **Level 1 (\(n_x=1, n_y=1\)):**
   \(n_x^2 + n_y^2 = 1 + 1 = 2 \implies E = 2 E_0\). Degeneracy \(g = 1\) (non-degenerate).
2. **Level 2 (\(n_x=1, n_y=2\) and \(n_x=2, n_y=1\)):**
   \(n_x^2 + n_y^2 = 1 + 4 = 5 \implies E = 5 E_0\). Degeneracy \(g = 2\) (doubly degenerate).
3. **Level 3 (\(n_x=2, n_y=2\)):**
   \(n_x^2 + n_y^2 = 4 + 4 = 8 \implies E = 8 E_0\). Degeneracy \(g = 1\).
4. **Level 4 (\(n_x=1, n_y=3\) and \(n_x=3, n_y=1\)):**
   \(n_x^2 + n_y^2 = 1 + 9 = 10 \implies E = 10 E_0\). Degeneracy \(g = 2\).
5. **Level 5 (\(n_x=2, n_y=3\) and \(n_x=3, n_y=2\)):**
   \(n_x^2 + n_y^2 = 4 + 9 = 13 \implies E = 13 E_0\). Degeneracy \(g = 2\).
6. **Level 6 (\(n_x=1, n_y=4\) and \(n_x=4, n_y=1\)):**
   \(n_x^2 + n_y^2 = 1 + 16 = 17 \implies E = 17 E_0\). Degeneracy \(g = 2\).

---

#### Step 3: Symmetry Breaking in Rectangular Box (\(L_x = L, L_y = 2L\))
For a rectangular box:
\[
E_{n_x, n_y} = \frac{h^2}{8m} \left( \frac{n_x^2}{L^2} + \frac{n_y^2}{(2L)^2} \right) = E_0 \left( n_x^2 + \frac{n_y^2}{4} \right)
\]
Evaluating the two states that were previously degenerate at \(5 E_0\):
- State \((1, 2)\):
  \[
  E_{1, 2} = E_0 \left( 1^2 + \frac{2^2}{4} \right) = E_0 (1 + 1) = 2.00 E_0
  \]
- State \((2, 1)\):
  \[
  E_{2, 1} = E_0 \left( 2^2 + \frac{1^2}{4} \right) = E_0 (4 + 0.25) = 4.25 E_0
  \]
Deforming the square into a rectangle breaks the spatial reflection symmetry across the diagonal (\(x \leftrightarrow y\)), completely lifting the degeneracy."""
            },
            {
                "id": "chem-qc-u2-p4",
                "title": "Problem 4: FEMO Model of Octatetraene Absorption Wavelength",
                "difficulty": "Intermediate",
                "statement": r"""1,3,5,7-Octatetraene has \(N = 8\) conjugated \(\pi\)-electrons.
1. Assuming an average \(\text{C-C}\) bond distance \(d_{\text{avg}} = 0.140\text{ nm}\) and a box length \(L = (N - 1) d_{\text{avg}} + 2 \delta\) with terminal extension \(\delta = 0.070\text{ nm}\) (total \(L = 8 \times 0.140\text{ nm} = 1.120\text{ nm}\)):
   - Identify the quantum numbers of the HOMO and LUMO.
   - Calculate the \(\text{HOMO} \rightarrow \text{LUMO}\) transition energy \(\Delta E\) in \(\text{eV}\).
   - Calculate the predicted absorption wavelength \(\lambda_{\text{abs}}\) (in \(\text{nm}\)).
2. Compare this prediction with the experimental maximum absorption of octatetraene (\(\lambda_{\text{exp}} \approx 304\text{ nm}\)).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Identification of Frontier Orbitals
With \(N = 8\) \(\pi\)-electrons, each spatial level holds 2 electrons:
\[
n_{\text{HOMO}} = \frac{N}{2} = \frac{8}{2} = 4
\]
\[
n_{\text{LUMO}} = n_{\text{HOMO}} + 1 = 5
\]

---

#### Step 2: Transition Energy Calculation
The energy difference is:
\[
\Delta E = E_5 - E_4 = \frac{h^2}{8 m_e L^2} (5^2 - 4^2) = \frac{h^2}{8 m_e L^2} (25 - 16) = 9 \frac{h^2}{8 m_e L^2}
\]
Given \(L = 1.120\text{ nm} = 1.120 \times 10^{-9}\text{ m}\):
\[
\frac{h^2}{8 m_e L^2} = \frac{(6.62607 \times 10^{-34}\text{ J}\cdot\text{s})^2}{8 (9.10938 \times 10^{-31}\text{ kg})(1.120 \times 10^{-9}\text{ m})^2} = \frac{4.39048 \times 10^{-67}}{9.1415 \times 10^{-48}} = 4.8028 \times 10^{-20}\text{ J}
\]
In electron-volts:
\[
\frac{h^2}{8 m_e L^2} = \frac{4.8028 \times 10^{-20}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} \approx 0.29977\text{ eV}
\]
Therefore:
\[
\Delta E = 9 \times 0.29977\text{ eV} \approx 2.6979\text{ eV} \approx 2.698\text{ eV}
\]
In Joules:
\[
\Delta E = 9 \times 4.8028 \times 10^{-20}\text{ J} = 4.3225 \times 10^{-19}\text{ J}
\]

---

#### Step 3: Absorption Wavelength & Comparison
The theoretical absorption wavelength is:
\[
\lambda_{\text{abs}} = \frac{h c}{\Delta E} = \frac{(6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(2.99792 \times 10^8\text{ m/s})}{4.3225 \times 10^{-19}\text{ J}} \approx 4.595 \times 10^{-7}\text{ m} = 459.5\text{ nm}
\]
Comparing with the experimental value \(\lambda_{\text{exp}} \approx 304\text{ nm}\):
The simple FEMO model overestimates the wavelength because it assumes completely zero electron-electron Coulomb repulsion and equal bond lengths. In real octatetraene, bond length alternation (alternating double and single bonds) creates a periodic potential modulation that opens a wider bandgap, shifting the absorption to \(304\text{ nm}\)."""
            },
            {
                "id": "chem-qc-u2-p5",
                "title": "Problem 5: Electron in a Benzene Ring & Aromatic Delocalization Energy",
                "difficulty": "Advanced",
                "statement": r"""Model the six \(\pi\)-electrons of a benzene ring (\(\text{C}_6\text{H}_6\)) as independent particles on a circular ring of radius \(R = 0.139\text{ nm}\).
1. Write the energy formula \(E_{m_l}\) in terms of \(\hbar, m_e, R\).
2. Populate the six \(\pi\)-electrons into the ring energy levels according to the Pauli principle and calculate the total \(\pi\)-electron ground-state energy \(E_{\text{total}}\) in \(\text{eV}\).
3. Determine the lowest electronic excitation energy \(\Delta E\) and predicted absorption wavelength \(\lambda\).
4. Explain how this circular model naturally rationalizes Hückel's \((4n + 2)\) aromatic stability rule.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Energy Expression on a Ring
The energy levels for an electron on a ring are:
\[
E_{m_l} = \frac{m_l^2 \hbar^2}{2 m_e R^2}, \quad m_l = 0, \pm 1, \pm 2, \dots
\]
Calculate the base energy unit \(\epsilon_0 = \frac{\hbar^2}{2 m_e R^2}\):
With \(\hbar = 1.05457 \times 10^{-34}\text{ J}\cdot\text{s}\), \(m_e = 9.10938 \times 10^{-31}\text{ kg}\), and \(R = 0.139 \times 10^{-9}\text{ m}\):
\[
\epsilon_0 = \frac{(1.05457 \times 10^{-34}\text{ J}\cdot\text{s})^2}{2 (9.10938 \times 10^{-31}\text{ kg})(0.139 \times 10^{-9}\text{ m})^2} = \frac{1.1121 \times 10^{-68}}{3.5209 \times 10^{-49}} = 3.1586 \times 10^{-20}\text{ J} \approx 0.19714\text{ eV}
\]

---

#### Step 2: Ground-State Electronic Configuration
Populating 6 \(\pi\)-electrons:
1. Ground level \(m_l = 0\) (degeneracy \(g = 1\)): Holds 2 electrons (spin up, spin down).
   \[
   E(m_l = 0) = 2 \times (0) = 0
   \]
2. First excited level \(m_l = \pm 1\) (degeneracy \(g = 2\)): Holds 4 electrons (2 in \(+1\), 2 in \(-1\)).
   \[
   E(m_l = \pm 1) = 4 \times (1^2 \epsilon_0) = 4 \epsilon_0
   \]
Total ground-state energy:
\[
E_{\text{total}} = 0 + 4 \epsilon_0 = 4 \times 0.19714\text{ eV} \approx 0.7886\text{ eV} \approx 1.263 \times 10^{-19}\text{ J}
\]

---

#### Step 3: Lowest Electronic Transition
The HOMO is \(m_l = \pm 1\), and the LUMO is \(m_l = \pm 2\).
The transition energy is:
\[
\Delta E = E(m_l = 2) - E(m_l = 1) = (2^2 - 1^2) \epsilon_0 = 3 \epsilon_0
\]
\[
\Delta E = 3 \times 0.19714\text{ eV} \approx 0.5914\text{ eV} = 9.476 \times 10^{-20}\text{ J}
\]
The transition wavelength is:
\[
\lambda = \frac{h c}{\Delta E} = \frac{(6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(2.99792 \times 10^8\text{ m/s})}{9.476 \times 10^{-20}\text{ J}} \approx 2.096 \times 10^{-6}\text{ m} = 2096\text{ nm}
\]

---

#### Step 4: Physical Rationale of Hückel's \((4n+2)\) Rule
In any circular potential:
- The lowest level (\(m_l = 0\)) is single-fold degenerate, accommodating exactly **2 electrons**.
- All subsequent energy levels (\(|m_l| = 1, 2, 3, \dots\)) are doubly degenerate (\(g = 2\)), each holding exactly **4 electrons** (2 pairs).
- To achieve a closed-shell electronic configuration with all occupied degenerate shells completely filled, the total number of \(\pi\)-electrons must be:
  \[
  N_\pi = 2 + 4n = 4n + 2, \quad n \in \{0, 1, 2, \dots\}
  \]
This provides a direct physical derivation of Hückel's aromaticity rule."""
            },
            {
                "id": "chem-qc-u2-p6",
                "title": "Problem 6: Quantum Tunneling Transmission Coefficient Through a Rectangular Barrier",
                "difficulty": "Advanced",
                "statement": r"""An electron with kinetic energy \(E = 2.00\text{ eV}\) approaches a rectangular potential energy barrier of height \(V_0 = 5.00\text{ eV}\) and width \(L = 0.200\text{ nm}\).
1. Calculate the decay constant \(\kappa\) inside the barrier (in \(\text{m}^{-1}\)) and the characteristic penetration depth \(\delta\).
2. Calculate the exact quantum transmission probability \(T\) through the barrier.
3. Determine how much the transmission probability drops if the barrier width is doubled to \(L = 0.400\text{ nm}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Decay Constant and Penetration Depth
The barrier height is \(V_0 - E = 5.00\text{ eV} - 2.00\text{ eV} = 3.00\text{ eV}\).
In Joules:
\[
V_0 - E = 3.00 \times 1.60218 \times 10^{-19}\text{ J} = 4.80654 \times 10^{-19}\text{ J}
\]
The decay wavevector \(\kappa\) is:
\[
\kappa = \frac{\sqrt{2 m_e (V_0 - E)}}{\hbar} = \frac{\sqrt{2 (9.10938 \times 10^{-31}\text{ kg})(4.80654 \times 10^{-19}\text{ J})}}{1.05457 \times 10^{-34}\text{ J}\cdot\text{s}}
\]
\[
\kappa = \frac{\sqrt{8.7569 \times 10^{-49}}}{1.05457 \times 10^{-34}} = \frac{9.3578 \times 10^{-25}}{1.05457 \times 10^{-34}} \approx 8.8736 \times 10^9\text{ m}^{-1}
\]
The penetration depth is:
\[
\delta = \frac{1}{\kappa} = \frac{1}{8.8736 \times 10^9\text{ m}^{-1}} \approx 1.127 \times 10^{-10}\text{ m} = 0.1127\text{ nm} = 1.127\text{ Å}
\]

---

#### Step 2: Transmission Probability for \(L = 0.200\text{ nm}\)
Evaluate \(\kappa L\):
\[
\kappa L = (8.8736 \times 10^9\text{ m}^{-1})(0.200 \times 10^{-9}\text{ m}) = 1.7747
\]
Evaluate \(\sinh(\kappa L)\):
\[
\sinh(1.7747) = \frac{e^{1.7747} - e^{-1.7747}}{2} = \frac{5.8985 - 0.1695}{2} = 2.8645
\]
\[
\sinh^2(\kappa L) = (2.8645)^2 \approx 8.2054
\]
Now evaluate the prefactor:
\[
\frac{V_0^2}{4 E (V_0 - E)} = \frac{(5.00)^2}{4 (2.00)(3.00)} = \frac{25.0}{24.0} \approx 1.04167
\]
The exact transmission coefficient is:
\[
T = \frac{1}{1 + \frac{V_0^2}{4 E (V_0 - E)} \sinh^2(\kappa L)} = \frac{1}{1 + (1.04167)(8.2054)} = \frac{1}{1 + 8.5473} = \frac{1}{9.5473} \approx 0.10474\text{ (or } 10.47\%\text{)}
\]

---

#### Step 3: Doubling the Barrier Width to \(L = 0.400\text{ nm}\)
For \(L = 0.400\text{ nm}\):
\[
\kappa L = 2 \times 1.7747 = 3.5494
\]
\[
\sinh(3.5494) = \frac{e^{3.5494} - e^{-3.5494}}{2} \approx \frac{34.793 - 0.0287}{2} \approx 17.382
\]
\[
\sinh^2(\kappa L) = (17.382)^2 \approx 302.13
\]
\[
T_{0.4} = \frac{1}{1 + (1.04167)(302.13)} = \frac{1}{1 + 314.72} = \frac{1}{315.72} \approx 3.167 \times 10^{-3}\text{ (or } 0.317\%\text{)}
\]
The transmission probability drops by a factor of:
\[
\frac{T_{0.2}}{T_{0.4}} = \frac{0.10474}{0.003167} \approx 33.1\text{ times}
\]
Doubling the barrier width attenuates the tunneling current by over 97%."""
            },
            {
                "id": "chem-qc-u2-p7",
                "title": "Problem 7: Complete Orthonormality Matrix and Momentum Expectation Value",
                "difficulty": "Advanced",
                "statement": r"""For a particle in a 1D box of length \(L\):
1. Prove by direct integration that the eigenfunctions \(\psi_m(x)\) and \(\psi_n(x)\) satisfy the orthonormality condition:
\[
\int_0^L \psi_m^*(x) \psi_n(x) dx = \delta_{mn}
\]
2. Calculate the expectation value of linear momentum \(\langle p \rangle\) in any arbitrary stationary state \(\psi_n(x)\).
3. Calculate the expectation value of kinetic energy \(\langle T \rangle\) and verify that \(\langle T \rangle = E_n\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Proof of Orthonormality
The eigenfunctions are \(\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)\).
Evaluate the inner product:
\[
I_{mn} = \int_0^L \psi_m^*(x) \psi_n(x) dx = \frac{2}{L} \int_0^L \sin\left(\frac{m\pi x}{L}\right) \sin\left(\frac{n\pi x}{L}\right) dx
\]
Using the product-to-sum identity \(\sin A \sin B = \frac{1}{2}[\cos(A - B) - \cos(A + B)]\):
\[
I_{mn} = \frac{1}{L} \int_0^L \left[ \cos\left(\frac{(m - n)\pi x}{L}\right) - \cos\left(\frac{(m + n)\pi x}{L}\right) \right] dx
\]
- **Case 1: \(m = n\):**
  \[
  I_{nn} = \frac{1}{L} \int_0^L \left[ \cos(0) - \cos\left(\frac{2n\pi x}{L}\right) \right] dx = \frac{1}{L} \left[ x - \frac{L}{2n\pi} \sin\left(\frac{2n\pi x}{L}\right) \right]_0^L = \frac{1}{L} [L - 0] = 1
  \]
- **Case 2: \(m \neq n\):**
  \[
  I_{mn} = \frac{1}{L} \left[ \frac{L}{(m - n)\pi} \sin\left(\frac{(m - n)\pi x}{L}\right) - \frac{L}{(m + n)\pi} \sin\left(\frac{(m + n)\pi x}{L}\right) \right]_0^L
  \]
  Because \(\sin(k\pi) = 0\) for all integers \(k\), both sine terms evaluate to zero at both limits:
  \[
  I_{mn} = 0 \quad (\text{for } m \neq n)
  \]
Combining both cases proves \(\langle \psi_m | \psi_n \rangle = \delta_{mn}\).

---

#### Step 2: Momentum Expectation Value \(\langle p \rangle\)
\[
\langle p \rangle = \int_0^L \psi_n^*(x) \left(-i\hbar \frac{d}{dx}\right) \psi_n(x) dx
\]
Substitute \(\psi_n(x)\):
\[
\frac{d\psi_n}{dx} = \sqrt{\frac{2}{L}} \left(\frac{n\pi}{L}\right) \cos\left(\frac{n\pi x}{L}\right)
\]
\[
\langle p \rangle = -i\hbar \left(\frac{2}{L}\right) \left(\frac{n\pi}{L}\right) \int_0^L \sin\left(\frac{n\pi x}{L}\right) \cos\left(\frac{n\pi x}{L}\right) dx
\]
Using \(\sin\theta \cos\theta = \frac{1}{2} \sin(2\theta)\):
\[
\int_0^L \sin\left(\frac{2n\pi x}{L}\right) dx = \left[ -\frac{L}{2n\pi} \cos\left(\frac{2n\pi x}{L}\right) \right]_0^L = -\frac{L}{2n\pi} [\cos(2n\pi) - \cos(0)] = -\frac{L}{2n\pi} [1 - 1] = 0
\]
Thus:
\[
\langle p \rangle = 0
\]
The average momentum is zero because the particle moves with equal probability in the \(+x\) and \(-x\) directions, forming a standing wave.

---

#### Step 3: Kinetic Energy Expectation Value
The kinetic energy operator is \(\hat{T} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2}\):
\[
\frac{d^2\psi_n}{dx^2} = -\left(\frac{n\pi}{L}\right)^2 \psi_n(x)
\]
Therefore:
\[
\hat{T} \psi_n(x) = \frac{\hbar^2}{2m} \left(\frac{n\pi}{L}\right)^2 \psi_n(x) = E_n \psi_n(x)
\]
Evaluating the expectation value:
\[
\langle T \rangle = \int_0^L \psi_n^* \hat{T} \psi_n dx = E_n \int_0^L |\psi_n|^2 dx = E_n \cdot 1 = E_n
\]
Since \(V(x) = 0\) inside the box, the total energy is purely kinetic: \(E_n = \langle T \rangle\)."""
            }
        ]
    }
    units.append(unit2)

    # =========================================================================
    # UNIT 3: Exact Quantum Models II: The Harmonic Oscillator & Rigid Rotor
    # =========================================================================
    unit3 = {
        "id": "unit-3",
        "unitNumber": 3,
        "title": "Unit 3: Exact Quantum Models II: The Harmonic Oscillator & Rigid Rotor",
        "leadSummary": r"""Rigorous quantum mechanical treatment of molecular vibrations and rotations: the quantum simple harmonic oscillator, power series solutions, Hermite polynomials, Gaussian ground states, ladder operator algebra (creation and annihilation operators), vibrational zero-point energy, quantum tunneling at classical turning points, the 3D rigid rotor, spherical harmonics, angular momentum operators, and space quantization.""",
        "simulations": [
            "sim_qc_harmonic_oscillator_ladder"
        ],
        "sections": [
            {
                "id": "sec-3-1",
                "secNumber": "3.1",
                "title": "The Quantum Harmonic Oscillator: Power Series & Dimensionless Formulation",
                "content": r"""The harmonic oscillator is the quintessential model for molecular vibrations, describing parabolic potential wells about equilibrium geometry.

### The Schrödinger Equation for a Harmonic Oscillator
A particle of mass \(m\) moving in a one-dimensional parabolic potential \(V(x) = \frac{1}{2} k x^2\) (where \(k\) is the force constant) obeys:
\[
-\frac{\hbar^2}{2m} \frac{d^2\psi(x)}{dx^2} + \frac{1}{2} k x^2 \psi(x) = E \psi(x)
\]
Introducing the classical harmonic oscillator frequency \(\omega = \sqrt{\frac{k}{m}}\):
\[
\frac{d^2\psi(x)}{dx^2} + \frac{2m}{\hbar^2} \left( E - \frac{1}{2} m \omega^2 x^2 \right) \psi(x) = 0
\]

### Dimensionless Coordinate Transformation
Define the dimensionless coordinate \(y\) and dimensionless energy eigenvalue \(\epsilon\):
\[
\alpha = \frac{m\omega}{\hbar}, \quad y = \sqrt{\alpha} x = \left(\frac{m\omega}{\hbar}\right)^{1/2} x
\]
\[
\epsilon = \frac{2E}{\hbar\omega}
\]
Transforming derivatives using the chain rule (\(\frac{d}{dx} = \sqrt{\alpha} \frac{d}{dy}\), \(\frac{d^2}{dx^2} = \alpha \frac{d^2}{dy^2}\)):
\[
\alpha \frac{d^2\psi}{dy^2} + \left( \alpha \epsilon - \alpha y^2 \right) \psi = 0
\]
Dividing throughout by \(\alpha\):
\[
\frac{d^2\psi(y)}{dy^2} + (\epsilon - y^2) \psi(y) = 0
\]

### Asymptotic Analysis at Large Distances
As \(y \rightarrow \pm\infty\), \(y^2 \gg \epsilon\):
\[
\frac{d^2\psi}{dy^2} - y^2 \psi \approx 0
\]
The asymptotic solution that remains square-integrable (\(\psi \rightarrow 0\) as \(|y| \rightarrow \infty\)) is:
\[
\psi_{\text{asympt}}(y) \sim e^{-y^2 / 2}
\]
We therefore introduce the ansatz:
\[
\psi(y) = H(y) e^{-y^2 / 2}
\]
Substituting this ansatz into the dimensionless differential equation:
\[
\frac{d\psi}{dy} = \left( H' - y H \right) e^{-y^2 / 2}
\]
\[
\frac{d^2\psi}{dy^2} = \left( H'' - 2y H' + (y^2 - 1) H \right) e^{-y^2 / 2}
\]
Substituting into \(\psi'' + (\epsilon - y^2)\psi = 0\) yields **Hermite's differential equation**:
\[
H''(y) - 2y H'(y) + (\epsilon - 1) H(y) = 0
\]

### Truncation of the Power Series & Energy Quantization
Seeking a power series solution \(H(y) = \sum_{j=0}^\infty c_j y^j\), substituting into Hermite's equation gives the recurrence relation:
\[
c_{j+2} = \frac{2j + 1 - \epsilon}{(j + 1)(j + 2)} c_j
\]
For the wavefunction to remain square-integrable as \(y \rightarrow \infty\), the infinite series must terminate into a finite polynomial of degree \(v\). Requiring the numerator to vanish at \(j = v\):
\[
2v + 1 - \epsilon = 0 \implies \epsilon = 2v + 1
\]
Substituting \(\epsilon = \frac{2E}{\hbar\omega}\):
\[
\frac{2E}{\hbar\omega} = 2v + 1 \implies E_v = \left( v + \frac{1}{2} \right) \hbar\omega = \left( v + \frac{1}{2} \right) h \nu_0, \quad v = 0, 1, 2, 3, \dots
\]
The energy levels are equally spaced by \(\hbar\omega\), with a ground-state zero-point energy of \(E_0 = \frac{1}{2}\hbar\omega\)."""
            },
            {
                "id": "sec-3-2",
                "secNumber": "3.2",
                "title": "Hermite Polynomials, Wavefunction Parity & Classical Turning Points",
                "content": r"""The solutions \(H_v(y)\) of Hermite's differential equation are the classical orthogonal Hermite polynomials.

### Rodrigues' Formula and Generating Function
The Hermite polynomials \(H_v(y)\) can be generated systematically via Rodrigues' formula:
\[
H_v(y) = (-1)^v e^{y^2} \frac{d^v}{dy^v} \left( e^{-y^2} \right)
\]
Alternatively, from the generating function \(G(y, s) = e^{2ys - s^2} = \sum_{v=0}^\infty \frac{H_v(y)}{v!} s^v\).

The first six Hermite polynomials are:
- \(H_0(y) = 1\)
- \(H_1(y) = 2y\)
- \(H_2(y) = 4y^2 - 2\)
- \(H_3(y) = 8y^3 - 12y\)
- \(H_4(y) = 16y^4 - 48y^2 + 12\)
- \(H_5(y) = 32y^5 - 160y^3 + 120y\)

### Normalized Vibrational Wavefunctions
The normalized harmonic oscillator wavefunctions are:
\[
\psi_v(x) = N_v H_v(\sqrt{\alpha} x) \exp\left( -\frac{\alpha x^2}{2} \right)
\]
where the normalization constant is derived from \(\int_{-\infty}^\infty H_v^2(y) e^{-y^2} dy = \sqrt{\pi} 2^v v!\):
\[
N_v = \left( \frac{\alpha}{\pi} \right)^{1/4} \frac{1}{\sqrt{2^v v!}} = \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^v v!}}
\]

### Symmetry and Nodal Properties
- **Wavefunction Parity:** Because \(V(-x) = V(x)\), the states possess definite parity:
  \[
  \psi_v(-x) = (-1)^v \psi_v(x)
  \]
  Even \(v\) states are even (symmetric); odd \(v\) states are odd (antisymmetric).
- **Nodes:** State \(\psi_v(x)\) possesses exactly \(v\) nodes (real roots of \(H_v\)).

### Classical Turning Points & Quantum Penetration
In classical mechanics, an oscillator with energy \(E_v\) cannot exceed the amplitude where potential energy equals total energy:
\[
E_v = \frac{1}{2} k x_c^2 \implies x_c = \pm \sqrt{\frac{2E_v}{k}} = \pm \sqrt{\frac{(2v + 1)\hbar\omega}{m\omega^2}} = \pm \sqrt{\frac{2v + 1}{\alpha}}
\]
In quantum mechanics:
- For \(|x| < x_c\), the kinetic energy is positive (\(E > V(x)\)), and the wavefunction is oscillatory.
- For \(|x| > x_c\), the kinetic energy is negative (\(E < V(x)\)). The Gaussian factor \(\exp(-\alpha x^2 / 2)\) decays exponentially into the classically forbidden barrier.
- For the ground state (\(v = 0\)), integrating \(|\psi_0(x)|^2\) beyond \(x_c = 1/\sqrt{\alpha}\) reveals that there is a **15.7% probability** of finding the quantum particle outside the classical turning points!"""
            },
            {
                "id": "sec-3-3",
                "secNumber": "3.3",
                "title": "Ladder Operator Formalism: Raising & Lowering Algebra",
                "content": r"""Paul Dirac introduced an elegant algebraic method to solve the harmonic oscillator without differential equations using non-Hermitian creation and annihilation operators.

### Definition of Ladder Operators
Define the dimensionless annihilation (lowering) operator \(\hat{a}\) and creation (raising) operator \(\hat{a}^\dagger\):
\[
\hat{a} = \sqrt{\frac{m\omega}{2\hbar}} \left( \hat{x} + \frac{i}{m\omega} \hat{p} \right) = \frac{1}{\sqrt{2}} \left( \hat{y} + i \hat{p}_y \right)
\]
\[
\hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}} \left( \hat{x} - \frac{i}{m\omega} \hat{p} \right) = \frac{1}{\sqrt{2}} \left( \hat{y} - i \hat{p}_y \right)
\]
Inverting for position and momentum operators:
\[
\hat{x} = \sqrt{\frac{\hbar}{2m\omega}} (\hat{a} + \hat{a}^\dagger)
\]
\[
\hat{p} = -i \sqrt{\frac{m\hbar\omega}{2}} (\hat{a} - \hat{a}^\dagger)
\]

### The Fundamental Commutation Relation
Using \([\hat{x}, \hat{p}] = i\hbar\):
\[
[\hat{a}, \hat{a}^\dagger] = \frac{m\omega}{2\hbar} \left[ \hat{x} + \frac{i}{m\omega}\hat{p}, \hat{x} - \frac{i}{m\omega}\hat{p} \right] = \frac{m\omega}{2\hbar} \left( -\frac{i}{m\omega}[\hat{x}, \hat{p}] + \frac{i}{m\omega}[\hat{p}, \hat{x}] \right)
\]
\[
[\hat{a}, \hat{a}^\dagger] = \frac{m\omega}{2\hbar} \left( -\frac{i}{m\omega}(i\hbar) - \frac{i}{m\omega}(i\hbar) \right) = \frac{m\omega}{2\hbar} \left( \frac{2\hbar}{m\omega} \right) = 1
\]
Thus:
\[
[\hat{a}, \hat{a}^\dagger] = \hat{I}
\]

### The Number Operator and Hamiltonian
The product \(\hat{a}^\dagger \hat{a}\) is the Hermitian **number operator** \(\hat{N}\):
\[
\hat{N} = \hat{a}^\dagger \hat{a}
\]
Expressing the Hamiltonian in terms of ladder operators:
\[
\hat{a}^\dagger \hat{a} = \frac{m\omega}{2\hbar} \left( \hat{x}^2 + \frac{\hat{p}^2}{m^2\omega^2} + \frac{i}{m\omega}(\hat{x}\hat{p} - \hat{p}\hat{x}) \right) = \frac{1}{\hbar\omega} \left( \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2\hat{x}^2 \right) - \frac{1}{2}
\]
Therefore:
\[
\hat{H} = \hbar\omega \left( \hat{a}^\dagger \hat{a} + \frac{1}{2} \right) = \hbar\omega \left( \hat{N} + \frac{1}{2} \right)
\]

### Action on Number Eigenstates \(|v\rangle\)
Let \(|v\rangle\) be an eigenstate of \(\hat{N}\) with eigenvalue \(v\): \(\hat{N}|v\rangle = v|v\rangle\).
From the commutator \([\hat{N}, \hat{a}] = [\hat{a}^\dagger \hat{a}, \hat{a}] = [\hat{a}^\dagger, \hat{a}]\hat{a} = -\hat{a}\):
\[
\hat{N} (\hat{a}|v\rangle) = (\hat{a}\hat{N} - \hat{a}) |v\rangle = (v - 1) (\hat{a}|v\rangle)
\]
Similarly, \([\hat{N}, \hat{a}^\dagger] = +\hat{a}^\dagger \implies \hat{N} (\hat{a}^\dagger|v\rangle) = (v + 1) (\hat{a}^\dagger|v\rangle)\).
Evaluating normalization:
\[
\hat{a}|v\rangle = \sqrt{v} |v - 1\rangle
\]
\[
\hat{a}^\dagger|v\rangle = \sqrt{v + 1} |v + 1\rangle
\]
Because the norm \(\langle v | \hat{a}^\dagger \hat{a} | v \rangle = v \ge 0\), the spectrum must terminate at \(v = 0\) via:
\[
\hat{a}|0\rangle = 0
\]
This algebraic condition directly yields the ground-state differential equation \(\left(x + \frac{\hbar}{m\omega}\frac{d}{dx}\right)\psi_0 = 0 \implies \psi_0(x) \propto e^{-\alpha x^2 / 2}\). Any state \(|v\rangle\) can be constructed by repeated application of the creation operator:
\[
|v\rangle = \frac{(\hat{a}^\dagger)^v}{\sqrt{v!}} |0\rangle
\]"""
            },
            {
                "id": "sec-3-4",
                "secNumber": "3.4",
                "title": "Three-Dimensional Rigid Rotor & Spherical Harmonics",
                "content": r"""The rigid rotor describes the rotational motion of diatomic and polyatomic molecules with fixed internuclear bond lengths.

### Hamiltonian in Spherical Polar Coordinates
Consider two masses \(m_1\) and \(m_2\) separated by a fixed bond distance \(R_0\). Reducing to a one-body problem of reduced mass \(\mu = \frac{m_1 m_2}{m_1 + m_2}\) with moment of inertia \(I = \mu R_0^2\):
\[
\hat{H}_{\text{rot}} = \frac{\hat{\mathbf{L}}^2}{2I}
\]
where \(\hat{\mathbf{L}}^2\) is the square of the orbital angular momentum operator:
\[
\hat{\mathbf{L}}^2 = -\hbar^2 \left[ \frac{1}{\sin\theta} \frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta} \frac{\partial^2}{\partial\phi^2} \right]
\]
The TISE is:
\[
\hat{\mathbf{L}}^2 Y(\theta, \phi) = 2 I E Y(\theta, \phi) = \hbar^2 l(l + 1) Y(\theta, \phi)
\]
with \(E_l = \frac{\hbar^2 l(l + 1)}{2I}\).

### Separation of Variables & Associated Legendre Polynomials
Using separation \(Y(\theta, \phi) = \Theta(\theta) \Phi(\phi)\):
1. **Azimuthal Equation:**
   \[
   \frac{d^2\Phi}{d\phi^2} = -m^2 \Phi \implies \Phi_m(\phi) = \frac{1}{\sqrt{2\pi}} e^{i m \phi}, \quad m \in \{0, \pm 1, \pm 2, \dots\}
   \]
2. **Polar Equation:**
   Substituting \(\Phi\) yields the Associated Legendre differential equation for \(\Theta(\theta)\). Solutions that remain finite at the poles (\(\theta = 0, \pi\)) require:
   \[
   l \in \{0, 1, 2, 3, \dots\}, \quad m \in \{-l, -l+1, \dots, +l\}
   \]
   giving the Associated Legendre functions \(P_l^{|m|}(\cos\theta)\).

### Orthonormal Spherical Harmonics
The joint angular eigenfunctions are the **spherical harmonics** \(Y_l^m(\theta, \phi)\):
\[
Y_l^m(\theta, \phi) = (-1)^m \sqrt{\frac{2l + 1}{4\pi} \frac{(l - m)!}{(l + m)!}} P_l^m(\cos\theta) e^{i m \phi}
\]
They satisfy simultaneous eigenvalue equations:
\[
\hat{\mathbf{L}}^2 Y_l^m(\theta, \phi) = l(l + 1) \hbar^2 Y_l^m(\theta, \phi)
\]
\[
\hat{L}_z Y_l^m(\theta, \phi) = m \hbar Y_l^m(\theta, \phi)
\]
and orthonormal integration:
\[
\int_0^{2\pi} d\phi \int_0^\pi d\theta \sin\theta Y_l^{m*}(\theta, \phi) Y_{l'}^{m'}(\theta, \phi) = \delta_{ll'} \delta_{mm'}
\]
Each rotational energy level \(E_l\) is \((2l + 1)\)-fold degenerate corresponding to the allowed orientations of \(m \in \{-l, \dots, +l\}\) in space (*space quantization*)."""
            },
            {
                "id": "sec-3-5",
                "secNumber": "3.5",
                "title": "Angular Momentum Commutation Algebra & Space Quantization",
                "content": r"""Angular momentum in quantum mechanics is defined fundamentally by its commutation relations rather than by classical cross products.

### Canonical Commutators
The Cartesian components of orbital angular momentum \(\hat{\mathbf{L}} = \hat{\mathbf{r}} \times \hat{\mathbf{p}}\) satisfy:
\[
[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z
\]
\[
[\hat{L}_y, \hat{L}_z] = i\hbar \hat{L}_x
\]
\[
[\hat{L}_z, \hat{L}_x] = i\hbar \hat{L}_y
\]
Compactly written using the Levi-Civita permutation symbol \(\epsilon_{ijk}\):
\[
[\hat{L}_i, \hat{L}_j] = i\hbar \sum_k \epsilon_{ijk} \hat{L}_k
\]
Because no two Cartesian components commute, they cannot be measured simultaneously. By the Robertson-Schrödinger uncertainty relation:
\[
\Delta L_x \cdot \Delta L_y \ge \frac{\hbar}{2} |\langle \hat{L}_z \rangle|
\]

### Commutation with the Total Angular Momentum Operator
The scalar operator \(\hat{\mathbf{L}}^2 = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2\) commutes with all three components:
\[
[\hat{\mathbf{L}}^2, \hat{L}_x] = [\hat{\mathbf{L}}^2, \hat{L}_y] = [\hat{\mathbf{L}}^2, \hat{L}_z] = 0
\]
Proof for \(\hat{L}_z\):
\[
[\hat{\mathbf{L}}^2, \hat{L}_z] = [\hat{L}_x^2, \hat{L}_z] + [\hat{L}_y^2, \hat{L}_z] + [\hat{L}_z^2, \hat{L}_z]
\]
\[
= \hat{L}_x [\hat{L}_x, \hat{L}_z] + [\hat{L}_x, \hat{L}_z]\hat{L}_x + \hat{L}_y [\hat{L}_y, \hat{L}_z] + [\hat{L}_y, \hat{L}_z]\hat{L}_y
\]
\[
= \hat{L}_x (-i\hbar \hat{L}_y) + (-i\hbar \hat{L}_y)\hat{L}_x + \hat{L}_y (i\hbar \hat{L}_x) + (i\hbar \hat{L}_x)\hat{L}_y = 0
\]
Therefore, \(\hat{\mathbf{L}}^2\) and exactly one Cartesian projection (conventionally \(\hat{L}_z\)) form a Complete Set of Commuting Observables (CSCO).

### Angular Momentum Ladder Operators \(\hat{L}_\pm\)
Define the ladder operators:
\[
\hat{L}_+ = \hat{L}_x + i \hat{L}_y, \quad \hat{L}_- = \hat{L}_x - i \hat{L}_y
\]
They satisfy:
\[
[\hat{L}_z, \hat{L}_\pm] = \pm \hbar \hat{L}_\pm
\]
\[
[\hat{L}_+, \hat{L}_-] = 2\hbar \hat{L}_z
\]
\[
\hat{\mathbf{L}}^2 = \hat{L}_- \hat{L}_+ + \hat{L}_z^2 + \hbar \hat{L}_z = \hat{L}_+ \hat{L}_- + \hat{L}_z^2 - \hbar \hat{L}_z
\]
Acting on mutual eigenstates \(|l, m\rangle\):
\[
\hat{L}_\pm |l, m\rangle = \hbar \sqrt{l(l + 1) - m(m \pm 1)} |l, m \pm 1\rangle
\]

### Vector Model & Precessional Cones of Space Quantization
In state \(|l, m\rangle\), the magnitude of the angular momentum vector is \(|\mathbf{L}| = \sqrt{l(l + 1)} \hbar\), while its projection along the \(z\)-axis is \(L_z = m\hbar\).
Because \(|m| \le l < \sqrt{l(l+1)}\), the vector \(\mathbf{L}\) can never align purely along the \(z\)-axis!
The angle \(\theta\) between \(\mathbf{L}\) and the quantization axis is:
\[
\cos\theta = \frac{L_z}{|\mathbf{L}|} = \frac{m}{\sqrt{l(l + 1)}}
\]
The perpendicular components \(L_x\) and \(L_y\) remain completely indeterminate, causing \(\mathbf{L}\) to precess on a cone of half-angle \(\theta\) around the \(z\)-axis."""
            },
            {
                "id": "sec-3-6",
                "secNumber": "3.6",
                "title": "Matrix Representations of Angular Momentum Operators",
                "content": r"""Using the orthonormal basis states \(\{|l, m\rangle\}\), angular momentum operators can be cast into explicit finite-dimensional matrix representations.

### General Matrix Elements in the \(|l, m\rangle\) Basis
For a fixed angular momentum quantum number \(l\), the Hilbert subspace has dimension \(2l + 1\).
1. **Matrix elements of \(\hat{L}_z\):**
   \[
   \langle l, m' | \hat{L}_z | l, m \rangle = m \hbar \delta_{m, m'}
   \]
   \(\hat{L}_z\) is represented by a diagonal matrix.
2. **Matrix elements of \(\hat{L}_+\) and \(\hat{L}_-\):**
   \[
   \langle l, m' | \hat{L}_+ | l, m \rangle = \hbar \sqrt{l(l + 1) - m(m + 1)} \delta_{m', m+1}
   \]
   \[
   \langle l, m' | \hat{L}_- | l, m \rangle = \hbar \sqrt{l(l + 1) - m(m - 1)} \delta_{m', m-1}
   \]
3. **Cartesian Components \(\hat{L}_x\) and \(\hat{L}_y\):**
   \[
   \hat{L}_x = \frac{1}{2}(\hat{L}_+ + \hat{L}_-), \quad \hat{L}_y = \frac{1}{2i}(\hat{L}_+ - \hat{L}_-)
   \]

### Explicit Matrices for \(l = 1\) (Three-Dimensional Representation)
In the basis ordered as \(\{|1, +1\rangle, |1, 0\rangle, |1, -1\rangle\}\):
\[
\mathbf{L}_z = \hbar \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix}
\]
Evaluating ladder operators:
\[
\hat{L}_+|1, 0\rangle = \hbar\sqrt{1(2) - 0(1)}|1, 1\rangle = \sqrt{2}\hbar |1, 1\rangle
\]
\[
\hat{L}_+|1, -1\rangle = \hbar\sqrt{1(2) - (-1)(0)}|1, 0\rangle = \sqrt{2}\hbar |1, 0\rangle
\]
\[
\mathbf{L}_+ = \sqrt{2}\hbar \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}, \quad \mathbf{L}_- = \mathbf{L}_+^\dagger = \sqrt{2}\hbar \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}
\]
Consequently:
\[
\mathbf{L}_x = \frac{\hbar}{\sqrt{2}} \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \quad \mathbf{L}_y = \frac{\hbar}{\sqrt{2}} \begin{pmatrix} 0 & -i & 0 \\ i & 0 & -i \\ 0 & i & 0 \end{pmatrix}
\]
Evaluating \(\mathbf{L}_x^2 + \mathbf{L}_y^2 + \mathbf{L}_z^2\):
\[
\mathbf{L}^2 = 2\hbar^2 \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = l(l+1)\hbar^2 \mathbf{I}
\]
which rigorously confirms the operator algebra."""
            },
            {
                "id": "sec-3-7",
                "secNumber": "3.7",
                "title": "Rotational Transitions & Microwave Absorption Selection Rules",
                "content": r"""The quantum rigid rotor model directly governs pure rotational transitions observed in microwave spectroscopy.

### Electric Dipole Transition Operator
The interaction between rotating molecules and electromagnetic radiation is mediated by the electric dipole transition moment operator \(\hat{\boldsymbol{\mu}} = \mu_0 \hat{\mathbf{u}}\), where \(\mu_0\) is the permanent molecular dipole moment:
\[
\mathbf{M}_{l'm', lm} = \langle l', m' | \hat{\boldsymbol{\mu}} | l, m \rangle = \mu_0 \int Y_{l'}^{m'*}(\theta, \phi) \mathbf{u} Y_l^m(\theta, \phi) d\Omega
\]

### The Gross Selection Rule
If a molecule possesses zero permanent electric dipole moment (\(\mu_0 = 0\), as in homonuclear diatomics \(\text{N}_2, \text{O}_2, \text{H}_2\) or spherical rotors \(\text{CH}_4, \text{SF}_6\)), the transition dipole matrix element vanishes identically for all states:
\[
\mu_0 = 0 \implies \mathbf{M}_{l'm', lm} = 0
\]
**Gross Selection Rule:** A molecule must possess a non-zero permanent electric dipole moment (\(\mu_0 \neq 0\)) to exhibit an electric-dipole allowed pure rotational microwave spectrum.

### The Specific Selection Rules
For linear rotors with \(\mu_0 \neq 0\), the dipole component along the space-fixed \(z\)-axis is \(\hat{\mu}_z = \mu_0 \cos\theta = \mu_0 \sqrt{\frac{4\pi}{3}} Y_1^0(\theta, \phi)\).
The transition matrix element is:
\[
\langle l', m' | \cos\theta | l, m \rangle \propto \int_0^{2\pi} e^{i (m - m')\phi} d\phi \int_0^\pi P_{l'}^{m'}(\cos\theta) \cos\theta P_l^m(\cos\theta) \sin\theta d\theta
\]
Using the recurrence relation \((2l + 1) x P_l^m(x) = (l - m + 1) P_{l+1}^m(x) + (l + m) P_{l-1}^m(x)\):
- The integral is strictly non-zero if and only if:
  \[
  \Delta l = l' - l = \pm 1
  \]
  \[
  \Delta m = m' - m = 0, \pm 1
  \]
For absorption transitions (\(\Delta l = +1\), denoted \(J \rightarrow J + 1\)):
\[
\tilde{\nu} = F(J + 1) - F(J) = 2 B (J + 1)
\]
where \(B = \frac{h}{8\pi^2 c I}\) is the rotational constant in \(\text{cm}^{-1}\). This yields equally spaced spectral absorption lines separated by \(2B\)."""
            }
        ],
        "problems": [
            {
                "id": "chem-qc-u3-p1",
                "title": "Problem 1: Carbon Monoxide Vibrational Zero-Point Energy & Classical Turning Point",
                "difficulty": "Foundational",
                "statement": r"""The fundamental vibrational wavenumber of carbon monoxide (\(^{12}\text{C}^{16}\text{O}\)) is \(\tilde{\nu}_0 = 2170\text{ cm}^{-1}\).
1. Calculate the effective force constant \(k\) of the \(\text{C}\equiv\text{O}\) triple bond (in \(\text{N/m}\)) using reduced mass \(\mu = \frac{m_{\text{C}} m_{\text{O}}}{m_{\text{C}} + m_{\text{O}}}\) with atomic masses \(m(^{12}\text{C}) = 12.000\text{ u}\) and \(m(^{16}\text{O}) = 15.995\text{ u}\).
2. Calculate the zero-point vibrational energy \(E_0\) in Joules and \(\text{kJ/mol}\).
3. Calculate the classical turning point amplitude \(x_c\) for the ground state (\(v = 0\)).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Reduced Mass and Force Constant Calculation
Calculate reduced mass \(\mu\):
\[
\mu = \frac{12.000 \times 15.995}{12.000 + 15.995}\text{ u} = \frac{191.94}{27.995}\text{ u} \approx 6.85622\text{ u}
\]
Convert to kilograms (\(1\text{ u} = 1.66054 \times 10^{-27}\text{ kg}\)):
\[
\mu = 6.85622 \times 1.66054 \times 10^{-27}\text{ kg} \approx 1.1385 \times 10^{-26}\text{ kg}
\]
The vibrational frequency is:
\[
\nu_0 = c \tilde{\nu}_0 = (2.99792 \times 10^{10}\text{ cm/s}) \times 2170\text{ cm}^{-1} \approx 6.5055 \times 10^{13}\text{ s}^{-1}
\]
The angular frequency is \(\omega = 2\pi \nu_0 = 2\pi (6.5055 \times 10^{13}) \approx 4.0875 \times 10^{14}\text{ rad/s}\).
The force constant is:
\[
k = \mu \omega^2 = (1.1385 \times 10^{-26}\text{ kg}) \times (4.0875 \times 10^{14}\text{ s}^{-1})^2 \approx 1902.1\text{ N/m}
\]
This large force constant (\(\sim 1902\text{ N/m}\)) reflects the strong carbon-oxygen triple bond.

---

#### Step 2: Zero-Point Energy Calculation
\[
E_0 = \frac{1}{2} h \nu_0 = \frac{1}{2} (6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(6.5055 \times 10^{13}\text{ s}^{-1}) \approx 2.1553 \times 10^{-20}\text{ J}
\]
Per mole:
\[
E_{0, \text{molar}} = E_0 N_A = (2.1553 \times 10^{-20}\text{ J}) \times (6.02214 \times 10^{23}\text{ mol}^{-1}) \approx 12979\text{ J/mol} \approx 12.98\text{ kJ/mol}
\]

---

#### Step 3: Classical Turning Point Amplitude \(x_c\)
At the turning point for \(v = 0\):
\[
\frac{1}{2} k x_c^2 = E_0 \implies x_c = \sqrt{\frac{2 E_0}{k}} = \sqrt{\frac{\hbar\omega}{k}} = \sqrt{\frac{\hbar}{\mu\omega}}
\]
\[
x_c = \sqrt{\frac{2 \times 2.1553 \times 10^{-20}\text{ J}}{1902.1\text{ N/m}}} = \sqrt{2.2662 \times 10^{-23}\text{ m}^2} \approx 4.76 \times 10^{-12}\text{ m} = 0.0476\text{ Å}
\]
The zero-point oscillation stretches or compresses the equilibrium bond length (\(R_e = 1.128\text{ Å}\)) by only \(\sim 4.2\%\)."""
            },
            {
                "id": "chem-qc-u3-p2",
                "title": "Problem 2: Matrix Elements of Position and Momentum using Ladder Operators",
                "difficulty": "Foundational",
                "statement": r"""Using the ladder operator definitions:
\[
\hat{x} = \sqrt{\frac{\hbar}{2m\omega}} (\hat{a} + \hat{a}^\dagger), \quad \hat{p} = -i\sqrt{\frac{m\hbar\omega}{2}} (\hat{a} - \hat{a}^\dagger)
\]
1. Calculate the matrix elements \(\langle v' | \hat{x} | v \rangle\) and \(\langle v' | \hat{p} | v \rangle\) between arbitrary vibrational states.
2. Derive the selection rule for electric dipole vibrational transitions.
3. Calculate \(\langle v | \hat{x}^2 | v \rangle\) and prove that the average potential energy \(\langle V \rangle\) equals the average kinetic energy \(\langle T \rangle = \frac{1}{2} E_v\) (Virial Theorem).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Matrix Elements of \(\hat{x}\) and \(\hat{p}\)
Recall that:
\[
\hat{a}|v\rangle = \sqrt{v}|v - 1\rangle, \quad \hat{a}^\dagger|v\rangle = \sqrt{v + 1}|v + 1\rangle
\]
For position \(\hat{x}\):
\[
\hat{x}|v\rangle = \sqrt{\frac{\hbar}{2m\omega}} \left( \sqrt{v}|v - 1\rangle + \sqrt{v + 1}|v + 1\rangle \right)
\]
Taking the inner product with \(\langle v'|\):
\[
\langle v' | \hat{x} | v \rangle = \sqrt{\frac{\hbar}{2m\omega}} \left( \sqrt{v} \delta_{v', v-1} + \sqrt{v+1} \delta_{v', v+1} \right)
\]
Similarly for momentum \(\hat{p}\):
\[
\langle v' | \hat{p} | v \rangle = -i\sqrt{\frac{m\hbar\omega}{2}} \left( \sqrt{v} \delta_{v', v-1} - \sqrt{v+1} \delta_{v', v+1} \right)
\]

---

#### Step 2: Vibrational Dipole Selection Rule
In the harmonic approximation, the molecular dipole moment is expanded to first order in displacement \(x\):
\[
\mu(x) = \mu_0 + \left(\frac{d\mu}{dx}\right)_0 x
\]
The transition matrix element is:
\[
\langle v' | \mu(x) | v \rangle = \left(\frac{d\mu}{dx}\right)_0 \langle v' | \hat{x} | v \rangle
\]
From Step 1, \(\langle v' | \hat{x} | v \rangle\) is non-zero only when:
\[
v' = v \pm 1 \iff \Delta v = \pm 1
\]
Transitions with \(\Delta v = \pm 2, \pm 3, \dots\) (overtones) are strictly forbidden in a pure harmonic oscillator.

---

#### Step 3: Evaluation of \(\langle x^2 \rangle\) and the Virial Theorem
Expand \(\hat{x}^2\):
\[
\hat{x}^2 = \frac{\hbar}{2m\omega} (\hat{a} + \hat{a}^\dagger)^2 = \frac{\hbar}{2m\omega} (\hat{a}^2 + \hat{a}\hat{a}^\dagger + \hat{a}^\dagger\hat{a} + (\hat{a}^\dagger)^2)
\]
Because \(\hat{a}^2\) and \((\hat{a}^\dagger)^2\) change the quantum number by \(\pm 2\), their expectation values in state \(|v\rangle\) vanish:
\[
\langle v | \hat{x}^2 | v \rangle = \frac{\hbar}{2m\omega} \langle v | (\hat{a}\hat{a}^\dagger + \hat{a}^\dagger\hat{a}) | v \rangle
\]
Using \(\hat{a}\hat{a}^\dagger = \hat{a}^\dagger\hat{a} + 1\):
\[
\hat{a}\hat{a}^\dagger + \hat{a}^\dagger\hat{a} = 2\hat{a}^\dagger\hat{a} + 1 = 2\hat{N} + 1
\]
Therefore:
\[
\langle x^2 \rangle_v = \frac{\hbar}{2m\omega} (2v + 1) = \left(v + \frac{1}{2}\right) \frac{\hbar}{m\omega}
\]
Now calculate the average potential energy:
\[
\langle V \rangle = \frac{1}{2} k \langle x^2 \rangle = \frac{1}{2} (m\omega^2) \left(v + \frac{1}{2}\right) \frac{\hbar}{m\omega} = \frac{1}{2} \left(v + \frac{1}{2}\right) \hbar\omega = \frac{1}{2} E_v
\]
Because \(\langle T \rangle + \langle V \rangle = E_v\):
\[
\langle T \rangle = E_v - \langle V \rangle = \frac{1}{2} E_v = \langle V \rangle
\]
This proves the Virial Theorem (\(\langle T \rangle = \langle V \rangle\)) for a harmonic potential."""
            },
            {
                "id": "chem-qc-u3-p3",
                "title": "Problem 3: Rotational Constant and Bond Length of Hydrogen Chloride from Microwave Transitions",
                "difficulty": "Intermediate",
                "statement": r"""The pure rotational spectrum of gaseous \(^1\text{H}^{35}\text{Cl}\) exhibits a series of equidistant absorption lines in the far-infrared region with an average adjacent spacing \(\Delta\tilde{\nu} = 20.68\text{ cm}^{-1}\).
Atomic masses: \(m(^1\text{H}) = 1.007825\text{ u}\), \(m(^{35}\text{Cl}) = 34.96885\text{ u}\).
1. Calculate the rotational constant \(B\) of \(^1\text{H}^{35}\text{Cl}\) in \(\text{cm}^{-1}\) and Joules.
2. Calculate the moment of inertia \(I\) (in \(\text{kg}\cdot\text{m}^2\)).
3. Calculate the equilibrium internuclear bond distance \(R_0\) (in Angstroms).
4. Predict the wavenumber of the \(J = 3 \rightarrow J = 4\) rotational transition.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Rotational Constant Calculation
For a rigid diatomic rotor, adjacent rotational lines are separated by:
\[
\Delta\tilde{\nu} = 2B \implies B = \frac{\Delta\tilde{\nu}}{2} = \frac{20.68\text{ cm}^{-1}}{2} = 10.34\text{ cm}^{-1}
\]
In energy units:
\[
B(\text{Joules}) = h c B(\text{cm}^{-1}) = (6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(2.99792 \times 10^{10}\text{ cm/s})(10.34\text{ cm}^{-1}) \approx 2.054 \times 10^{-22}\text{ J}
\]

---

#### Step 2: Moment of Inertia
From the definition of the rotational constant:
\[
B = \frac{h}{8\pi^2 c I} \implies I = \frac{h}{8\pi^2 c B}
\]
\[
I = \frac{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}}{8 \pi^2 (2.99792 \times 10^{10}\text{ cm/s})(10.34\text{ cm}^{-1})} = \frac{6.62607 \times 10^{-34}}{2.4475 \times 10^{-11}} \approx 2.7073 \times 10^{-47}\text{ kg}\cdot\text{m}^2
\]

---

#### Step 3: Internuclear Bond Length \(R_0\)
Calculate the reduced mass \(\mu\):
\[
\mu = \frac{1.007825 \times 34.96885}{1.007825 + 34.96885}\text{ u} = \frac{35.2424}{35.9767}\text{ u} \approx 0.97959\text{ u}
\]
In kilograms:
\[
\mu = 0.97959 \times 1.66054 \times 10^{-27}\text{ kg} \approx 1.6266 \times 10^{-27}\text{ kg}
\]
Since \(I = \mu R_0^2\):
\[
R_0 = \sqrt{\frac{I}{\mu}} = \sqrt{\frac{2.7073 \times 10^{-47}\text{ kg}\cdot\text{m}^2}{1.6266 \times 10^{-27}\text{ kg}}} = \sqrt{1.6644 \times 10^{-20}\text{ m}^2} \approx 1.290 \times 10^{-10}\text{ m} = 1.290\text{ Å}
\]
This precisely reproduces the experimental gas-phase bond length of \(\text{HCl}\) (\(1.275 - 1.29\text{ Å}\)).

---

#### Step 4: Wavenumber of \(J = 3 \rightarrow 4\) Transition
The transition wavenumber for \(J \rightarrow J + 1\) is:
\[
\tilde{\nu}(3 \rightarrow 4) = 2B (3 + 1) = 8B = 8 \times 10.34\text{ cm}^{-1} = 82.72\text{ cm}^{-1}
\]"""
            },
            {
                "id": "chem-qc-u3-p4",
                "title": "Problem 4: Most Populated Rotational Energy Level at Thermal Equilibrium",
                "difficulty": "Intermediate",
                "statement": r"""At thermal equilibrium at temperature \(T = 300\text{ K}\), molecules are distributed among rotational states according to Boltzmann statistics with degeneracy \(g_J = 2J + 1\):
\[
N_J \propto (2J + 1) \exp\left( -\frac{B h c J(J + 1)}{k_B T} \right)
\]
1. Derive the general formula for the rotational quantum number \(J_{\text{max}}\) corresponding to the most populated rotational level by treating \(J\) as a continuous variable.
2. For carbon monoxide (\(B = 1.931\text{ cm}^{-1}\)), calculate \(J_{\text{max}}\) at \(T = 300\text{ K}\).
3. Explain why the most intense spectral line in microwave absorption corresponds to transition from \(J_{\text{max}}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Derivation of \(J_{\text{max}}\)
Let the population function be:
\[
f(J) = (2J + 1) \exp(-\beta J(J + 1))
\]
where \(\beta = \frac{B h c}{k_B T}\).
To find the maximum, set the first derivative to zero:
\[
\frac{df}{dJ} = 2 \exp(-\beta J(J + 1)) + (2J + 1) [-\beta(2J + 1)] \exp(-\beta J(J + 1)) = 0
\]
Dividing by the non-zero exponential factor:
\[
2 - \beta (2J + 1)^2 = 0 \implies (2J + 1)^2 = \frac{2}{\beta} = \frac{2 k_B T}{B h c}
\]
Taking the positive square root:
\[
2J + 1 = \sqrt{\frac{2 k_B T}{B h c}} \implies J_{\text{max}} = \sqrt{\frac{k_B T}{2 B h c}} - \frac{1}{2}
\]

---

#### Step 2: Numerical Calculation for CO at \(300\text{ K}\)
First calculate the dimensionless ratio \(\frac{k_B T}{B h c}\):
\[
k_B T = (1.38065 \times 10^{-23}\text{ J/K})(300\text{ K}) = 4.14195 \times 10^{-21}\text{ J}
\]
\[
B h c = (1.931\text{ cm}^{-1})(6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(2.99792 \times 10^{10}\text{ cm/s}) = 3.8358 \times 10^{-23}\text{ J}
\]
\[
\frac{k_B T}{B h c} = \frac{4.14195 \times 10^{-21}}{3.8358 \times 10^{-23}} \approx 107.98
\]
Now evaluate \(J_{\text{max}}\):
\[
J_{\text{max}} = \sqrt{\frac{107.98}{2}} - 0.5 = \sqrt{53.99} - 0.5 \approx 7.348 - 0.5 = 6.85
\]
Rounding to the nearest integer:
\[
J_{\text{max}} = 7
\]
At \(300\text{ K}\), the rotational state \(J = 7\) is the most heavily populated state in gas-phase \(\text{CO}\).

---

#### Step 3: Connection to Spectral Intensity
Microwave absorption transition intensity is directly proportional to the population difference between states:
\[
I(J \rightarrow J + 1) \propto N_J - N_{J+1} \approx N_J \frac{\Delta E}{k_B T}
\]
Because \(N_J\) peaks at \(J = J_{\text{max}}\) while the transition energy \(2B(J+1)\) varies gently, the absorption spectrum envelope mirrors the rotational population distribution, displaying maximum absorption intensity around \(J = 7 \rightarrow 8\)."""
            },
            {
                "id": "chem-qc-u3-p5",
                "title": "Problem 5: Non-Commuting Angular Momentum and Uncertainty Products",
                "difficulty": "Advanced",
                "statement": r"""Consider an angular momentum eigenstate \(|l, m\rangle\) where \(\hat{\mathbf{L}}^2|l, m\rangle = l(l+1)\hbar^2|l, m\rangle\) and \(\hat{L}_z|l, m\rangle = m\hbar|l, m\rangle\).
1. Prove that \(\langle \hat{L}_x \rangle = 0\) and \(\langle \hat{L}_y \rangle = 0\).
2. Calculate the expectation values \(\langle \hat{L}_x^2 \rangle\) and \(\langle \hat{L}_y^2 \rangle\) in terms of \(l, m, \hbar\).
3. Evaluate the uncertainty product \(\Delta L_x \cdot \Delta L_y\) and show that it satisfies the Robertson-Schrödinger uncertainty inequality:
\[
\Delta L_x \cdot \Delta L_y \ge \frac{\hbar}{2} |\langle \hat{L}_z \rangle|
\]
4. Identify under what condition \(\Delta L_x \cdot \Delta L_y\) achieves its minimum value.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Expectation Values of \(\hat{L}_x\) and \(\hat{L}_y\)
Using ladder operators:
\[
\hat{L}_x = \frac{1}{2}(\hat{L}_+ + \hat{L}_-), \quad \hat{L}_y = \frac{1}{2i}(\hat{L}_+ - \hat{L}_-)
\]
Because \(\hat{L}_\pm |l, m\rangle \propto |l, m \pm 1\rangle\) and \(\langle l, m | l, m \pm 1 \rangle = 0\) by orthogonality:
\[
\langle \hat{L}_x \rangle = \frac{1}{2} (\langle l, m | \hat{L}_+ | l, m \rangle + \langle l, m | \hat{L}_- | l, m \rangle) = 0
\]
\[
\langle \hat{L}_y \rangle = \frac{1}{2i} (\langle l, m | \hat{L}_+ | l, m \rangle - \langle l, m | \hat{L}_- | l, m \rangle) = 0
\]

---

#### Step 2: Evaluation of \(\langle \hat{L}_x^2 \rangle\) and \(\langle \hat{L}_y^2 \rangle\)
By rotational symmetry about the \(z\)-axis:
\[
\langle \hat{L}_x^2 \rangle = \langle \hat{L}_y^2 \rangle
\]
Since \(\hat{\mathbf{L}}^2 = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2\):
\[
\langle \hat{L}_x^2 \rangle + \langle \hat{L}_y^2 \rangle = \langle \hat{\mathbf{L}}^2 \rangle - \langle \hat{L}_z^2 \rangle = l(l + 1)\hbar^2 - m^2 \hbar^2
\]
Equating the two equal transverse components:
\[
2 \langle \hat{L}_x^2 \rangle = \hbar^2 [l(l + 1) - m^2] \implies \langle \hat{L}_x^2 \rangle = \langle \hat{L}_y^2 \rangle = \frac{\hbar^2}{2} [l(l + 1) - m^2]
\]

---

#### Step 3: Uncertainty Product Evaluation
Since \(\langle \hat{L}_x \rangle = \langle \hat{L}_y \rangle = 0\):
\[
\Delta L_x = \sqrt{\langle \hat{L}_x^2 \rangle} = \hbar \sqrt{\frac{l(l + 1) - m^2}{2}}
\]
\[
\Delta L_y = \sqrt{\langle \hat{L}_y^2 \rangle} = \hbar \sqrt{\frac{l(l + 1) - m^2}{2}}
\]
The uncertainty product is:
\[
\Delta L_x \cdot \Delta L_y = \frac{\hbar^2}{2} [l(l + 1) - m^2]
\]
Testing against the uncertainty inequality:
\[
\Delta L_x \cdot \Delta L_y \ge \frac{\hbar}{2} |\langle \hat{L}_z \rangle| = \frac{\hbar^2}{2} |m|
\]
Subtracting the two expressions:
\[
\frac{\hbar^2}{2} [l(l + 1) - m^2 - |m|] = \frac{\hbar^2}{2} [l(l + 1) - |m|(|m| + 1)]
\]
Since \(|m| \le l\), \(l(l + 1) - |m|(|m| + 1) \ge 0\), proving the inequality holds universally.

---

#### Step 4: Minimum Uncertainty Condition
The minimum occurs when \(|m| = l\) (maximum alignment along \(z\)):
\[
l(l + 1) - l^2 = l
\]
\[
\Delta L_x \cdot \Delta L_y = \frac{\hbar^2}{2} l = \frac{\hbar}{2} |\langle \hat{L}_z \rangle|
\]
States with \(m = \pm l\) are minimum uncertainty states for angular momentum."""
            },
            {
                "id": "chem-qc-u3-p6",
                "title": "Problem 6: Anharmonic Morse Potential & Vibrational Dissociation Limit",
                "difficulty": "Advanced",
                "statement": r"""A real diatomic molecule is modeled by the Morse potential:
\[
V(x) = D_e [1 - e^{-a x}]^2
\]
where \(D_e\) is the equilibrium dissociation energy and \(x = R - R_e\).
The quantized energy levels are given by:
\[
E_v = \hbar\omega_e \left(v + \frac{1}{2}\right) - \hbar\omega_e x_e \left(v + \frac{1}{2}\right)^2
\]
where the anharmonicity constant is \(\omega_e x_e = \frac{\hbar\omega_e^2}{4 D_e}\).
1. For \(\text{HCl}\), \(\tilde{\omega}_e = 2990.9\text{ cm}^{-1}\) and \(\tilde{\omega}_e x_e = 52.8\text{ cm}^{-1}\). Calculate the depth \(D_e\) of the Morse potential well (in \(\text{eV}\)).
2. Calculate the fundamental transition wavenumber \(\tilde{\nu}_1 = E_1 - E_0\) and the first overtone \(\tilde{\nu}_2 = E_2 - E_0\).
3. Determine the maximum vibrational quantum number \(v_{\text{max}}\) before dissociation occurs.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Equilibrium Dissociation Energy \(D_e\)
From Morse theory:
\[
\tilde{\omega}_e x_e = \frac{\tilde{\omega}_e^2}{4 D_e} \implies D_e(\text{cm}^{-1}) = \frac{\tilde{\omega}_e^2}{4 \tilde{\omega}_e x_e}
\]
Substitute \(\tilde{\omega}_e = 2990.9\text{ cm}^{-1}\) and \(\tilde{\omega}_e x_e = 52.8\text{ cm}^{-1}\):
\[
D_e = \frac{(2990.9)^2}{4 \times 52.8} = \frac{8945482.8}{211.2} \approx 42355.5\text{ cm}^{-1}
\]
Convert to electron-volts (\(1\text{ eV} = 8065.54\text{ cm}^{-1}\)):
\[
D_e = \frac{42355.5\text{ cm}^{-1}}{8065.54\text{ cm}^{-1}/\text{eV}} \approx 5.2514\text{ eV} \approx 5.25\text{ eV}
\]
In \(\text{kJ/mol}\):
\[
D_e = 5.2514 \times 96.485\text{ kJ/mol} \approx 506.7\text{ kJ/mol}
\]

---

#### Step 2: Fundamental and First Overtone Transitions
Using \(E_v = \tilde{\omega}_e (v + 1/2) - \tilde{\omega}_e x_e (v + 1/2)^2\):
1. **Fundamental Transition (\(v = 0 \rightarrow 1\)):**
   \[
   \Delta E(0 \rightarrow 1) = \tilde{\omega}_e - 2 \tilde{\omega}_e x_e
   \]
   \[
   \tilde{\nu}_1 = 2990.9 - 2(52.8) = 2990.9 - 105.6 = 2885.3\text{ cm}^{-1}
   \]
2. **First Overtone Transition (\(v = 0 \rightarrow 2\)):**
   \[
   \Delta E(0 \rightarrow 2) = 2 \tilde{\omega}_e - 6 \tilde{\omega}_e x_e
   \]
   \[
   \tilde{\nu}_2 = 2(2990.9) - 6(52.8) = 5981.8 - 316.8 = 5665.0\text{ cm}^{-1}
   \]
Notice that \(\tilde{\nu}_2 < 2 \tilde{\nu}_1\) (\(5665.0\text{ cm}^{-1} < 5770.6\text{ cm}^{-1}\)) due to anharmonic level crowding.

---

#### Step 3: Maximum Vibrational Quantum Number \(v_{\text{max}}\)
Dissociation occurs when the spacing between adjacent levels vanishes:
\[
\Delta E_v = E_{v+1} - E_v = \tilde{\omega}_e - 2 \tilde{\omega}_e x_e (v + 1) = 0
\]
\[
v_{\text{max}} + 1 = \frac{\tilde{\omega}_e}{2 \tilde{\omega}_e x_e} = \frac{2990.9}{2 \times 52.8} = \frac{2990.9}{105.6} \approx 28.32
\]
\[
v_{\text{max}} = 28.32 - 1 = 27.32 \implies v_{\text{max}} = 27
\]
The \(\text{HCl}\) potential well supports 28 bound vibrational states (\(v = 0, 1, \dots, 27\)) before reaching the continuous dissociation continuum."""
            },
            {
                "id": "chem-qc-u3-p7",
                "title": "Problem 7: Centrifugal Distortion & Non-Rigid Rotor Correction",
                "difficulty": "Advanced",
                "statement": r"""A real diatomic molecule stretches as it rotates due to centrifugal force. The effective term values including the quartic centrifugal distortion constant \(D_J\) are:
\[
F(J) = B J(J + 1) - D_J [J(J + 1)]^2
\]
where \(D_J \approx \frac{4 B^3}{\tilde{\omega}_e^2}\).
1. For \(^{12}\text{C}^{16}\text{O}\), \(B = 1.93128\text{ cm}^{-1}\) and \(\tilde{\omega}_e = 2169.8\text{ cm}^{-1}\). Calculate \(D_J\) in \(\text{cm}^{-1}\).
2. Calculate the transition wavenumber for \(J = 9 \rightarrow 10\) with and without the centrifugal distortion correction.
3. Determine the percentage error incurred if the rigid rotor approximation is used for this high-\(J\) transition.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Centrifugal Distortion Constant \(D_J\)
Using the Kratzer relation:
\[
D_J = \frac{4 B^3}{\tilde{\omega}_e^2}
\]
Substitute \(B = 1.93128\text{ cm}^{-1}\) and \(\tilde{\omega}_e = 2169.8\text{ cm}^{-1}\):
\[
B^3 = (1.93128)^3 \approx 7.2033\text{ cm}^{-3}
\]
\[
\tilde{\omega}_e^2 = (2169.8)^2 \approx 4708032\text{ cm}^{-2}
\]
\[
D_J = \frac{4 \times 7.2033}{4708032} = \frac{28.8132}{4708032} \approx 6.120 \times 10^{-6}\text{ cm}^{-1}
\]

---

#### Step 2: Transition Wavenumber for \(J = 9 \rightarrow 10\)
For non-rigid rotor:
\[
\tilde{\nu}(J \rightarrow J + 1) = F(J + 1) - F(J) = 2 B (J + 1) - 4 D_J (J + 1)^3
\]
For \(J = 9 \implies J + 1 = 10\):
1. **Rigid Rotor Approximation (\(D_J = 0\)):**
   \[
   \tilde{\nu}_{\text{rigid}} = 2 B (10) = 20 B = 20 \times 1.93128\text{ cm}^{-1} = 38.6256\text{ cm}^{-1}
   \]
2. **Centrifugal Correction:**
   \[
   \Delta\tilde{\nu}_{\text{centrif}} = -4 D_J (10)^3 = -4000 D_J = -4000 \times (6.120 \times 10^{-6}\text{ cm}^{-1}) = -0.02448\text{ cm}^{-1}
   \]
3. **Corrected Transition Wavenumber:**
   \[
   \tilde{\nu}_{\text{actual}} = 38.6256 - 0.02448 = 38.6011\text{ cm}^{-1}
   \]

---

#### Step 3: Error Analysis
The absolute difference is \(0.0245\text{ cm}^{-1}\).
The relative percentage error is:
\[
\% \text{ Error} = \frac{0.02448\text{ cm}^{-1}}{38.6011\text{ cm}^{-1}} \times 100\% \approx 0.0634\%
\]
In high-resolution microwave and millimeter-wave Fourier-transform spectroscopy (measurement precision \(\sim 10^{-4}\text{ cm}^{-1}\)), an error of \(0.0245\text{ cm}^{-1}\) is massive (over 200 times the instrumental resolution), demonstrating that centrifugal distortion corrections are essential for high-accuracy molecular structure determination."""
            }
        ]
    }
    units.append(unit3)

    return units

if __name__ == "__main__":
    units = get_units_1_2_3()
    print(f"Generated {len(units)} units successfully.")
    for u in units:
        print(f" - {u['id']}: {u['title']} ({len(u['sections'])} sections, {len(u['problems'])} problems)")
