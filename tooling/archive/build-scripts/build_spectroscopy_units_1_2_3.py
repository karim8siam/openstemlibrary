#!/usr/bin/env python3
"""
build_spectroscopy_units_1_2_3.py
Builds Units 1, 2, and 3 for Chemical Spectroscopy.
Unit 1: Foundations of Electromagnetic Radiation, Transition Moments & Spectral Linewidths
Unit 2: Rotational & Microwave Spectroscopy of Diatomic & Polyatomic Rotors
Unit 3: Infrared & Vibrational Spectroscopy of Diatomic & Polyatomic Molecules
"""

import json

def get_units_1_2_3():
    units = []

    # =========================================================================
    # UNIT 1: Foundations of Electromagnetic Radiation, Transition Moments & Spectral Linewidths
    # =========================================================================
    u1 = {
        "id": "unit1",
        "number": 1,
        "title": "Unit 1: Foundations of Electromagnetic Radiation, Transition Moments & Spectral Linewidths",
        "description": "Fundamental principles of electromagnetic radiation and molecular transitions: wave-particle duality, quantization of energy, Einstein coefficients of absorption and emission, transition dipole moment operator, lifetime and Doppler broadening mechanisms, Fourier transform interferometry, and signal-to-noise optimization.",
        "simulations": [
            {
                "id": "sim_spec_electromagnetic_wave_fourier",
                "title": "EM Wave Superposition & Michelson Interferogram FFT",
                "description": "Interactive 60 FPS real-time simulator tracing electromagnetic wave interference in a Michelson interferometer. Adjust optical retardation velocity, superimpose dual-frequency radiation waves, observe the time-domain interferogram, and perform live Fast Fourier Transform (FFT) recovery into the frequency domain power spectrum."
            }
        ],
        "sections": [
            {
                "id": "u1-sec1",
                "number": "1.1",
                "title": "The Electromagnetic Spectrum & Wave-Particle Quantization",
                "content": r"""<p>Electromagnetic radiation constitutes propagating oscillating electric and magnetic fields governed by Maxwell's equations. In a vacuum, radiation propagates at speed \(c = 2.99792458 \times 10^8\text{ m/s}\). The relationship between frequency \(\nu\) (Hz), wavelength \(\lambda\) (m), and spectroscopic wavenumber \(\tilde{\nu}\) (\(\text{cm}^{-1}\)) is given by:</p>
\[
c = \nu \lambda, \quad \tilde{\nu} = \frac{1}{\lambda} = \frac{\nu}{c} = \frac{\omega}{2\pi c}
\]
<p>Energy quantization formalizes radiation as discrete energy packets (photons) carrying energy \(E = h\nu = \hbar\omega = hc\tilde{\nu}\), where Planck's constant \(h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}\) and \(\hbar = h / (2\pi) = 1.0545718 \times 10^{-34}\text{ J}\cdot\text{s}\).</p>
<h4 class="content-heading">Spectroscopic Regions of the Electromagnetic Spectrum</h4>
<p>The electromagnetic spectrum spans diverse physical domains, each probing distinct quantum mechanical transitions within molecular systems:</p>
<div class="table-container">
  <table class="data-table">
    <thead>
      <tr>
        <th>Spectral Region</th>
        <th>Typical Wavelength (\(\lambda\))</th>
        <th>Wavenumber (\(\tilde{\nu}\))</th>
        <th>Energy (\(\text{kJ/mol}\))</th>
        <th>Primary Molecular Quantum Transition</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Radiofrequency</td>
        <td>\(1\text{ m} - 10\text{ cm}\)</td>
        <td>\(0.01 - 0.1\text{ cm}^{-1}\)</td>
        <td>\(10^{-4} - 10^{-2}\)</td>
        <td>Nuclear spin state reorientation in magnetic fields (NMR)</td>
      </tr>
      <tr>
        <td>Microwave</td>
        <td>\(10\text{ cm} - 1\text{ mm}\)</td>
        <td>\(0.1 - 10\text{ cm}^{-1}\)</td>
        <td>\(0.01 - 1.2\)</td>
        <td>Molecular rotational transitions; electron spin flips (EPR/ESR)</td>
      </tr>
      <tr>
        <td>Far-Infrared</td>
        <td>\(1000 - 50\ \mu\text{m}\)</td>
        <td>\(10 - 200\text{ cm}^{-1}\)</td>
        <td>\(1.2 - 24\)</td>
        <td>Low-frequency skeletal vibrations and torsional modes</td>
      </tr>
      <tr>
        <td>Mid-Infrared</td>
        <td>\(50 - 2.5\ \mu\text{m}\)</td>
        <td>\(200 - 4000\text{ cm}^{-1}\)</td>
        <td>\(24 - 480\)</td>
        <td>Fundamental molecular vibrational and rovibrational modes</td>
      </tr>
      <tr>
        <td>Near-Infrared</td>
        <td>\(2.5\ \mu\text{m} - 800\text{ nm}\)</td>
        <td>\(4000 - 12500\text{ cm}^{-1}\)</td>
        <td>\(48 - 150\)</td>
        <td>Vibrational overtones and combination bands</td>
      </tr>
      <tr>
        <td>Visible & UV</td>
        <td>\(800 - 200\text{ nm}\)</td>
        <td>\(12500 - 50000\text{ cm}^{-1}\)</td>
        <td>\(150 - 600\)</td>
        <td>Outer valence electronic transitions (\(\pi \to \pi^*, n \to \pi^*\))</td>
      </tr>
      <tr>
        <td>Vacuum UV / X-Ray</td>
        <td>\(200 - 0.01\text{ nm}\)</td>
        <td>\(> 50000\text{ cm}^{-1}\)</td>
        <td>\(> 600\)</td>
        <td>Core electron ionization and inner shell electronic promotions</td>
      </tr>
      <tr>
        <td>\(\gamma\)-Rays</td>
        <td>\(< 0.01\text{ nm}\)</td>
        <td>\(> 10^7\text{ cm}^{-1}\)</td>
        <td>\(> 10^5\)</td>
        <td>Nuclear isomeric state transitions (Mössbauer spectroscopy)</td>
      </tr>
    </tbody>
  </table>
</div>
<p>Understanding these distinct energetic regimes establishes the foundation for assigning spectral lines to microscopic quantum Hamiltonians.</p>"""
            },
            {
                "id": "u1-sec2",
                "number": "1.2",
                "title": "Einstein Coefficients & Radiation Equilibrium",
                "content": r"""<p>In 1917, Albert Einstein formulated the thermodynamic and kinetic equilibrium between matter and radiation fields by defining three transition rate coefficients for a two-level quantum system with lower state \(|1\rangle\) (energy \(E_1\)) and upper state \(|2\rangle\) (energy \(E_2\)), where \(\nu_{12} = (E_2 - E_1)/h\):</p>
<ol>
  <li><strong>Induced (Stimulated) Absorption:</strong> Transition rate from state 1 to 2 stimulated by spectral energy density \(\rho(\nu)\):
  \[
  \left(\frac{dN_{1\to 2}}{dt}\right)_{\text{abs}} = B_{12} N_1 \rho(\nu)
  \]
  </li>
  <li><strong>Spontaneous Emission:</strong> Transition rate from state 2 to 1 occurring spontaneously without external radiation:
  \[
  \left(\frac{dN_{2\to 1}}{dt}\right)_{\text{spont}} = A_{21} N_2
  \]
  </li>
  <li><strong>Stimulated Emission:</strong> Transition rate from state 2 to 1 driven by the external field \(\rho(\nu)\):
  \[
  \left(\frac{dN_{2\to 1}}{dt}\right)_{\text{stim}} = B_{21} N_2 \rho(\nu)
  \]
  </li>
</ol>
<h4 class="content-heading">Derivation of Einstein Relations</h4>
<p>At thermal equilibrium at temperature \(T\), the principle of detailed balance requires that the total rate of upward transitions matches the total rate of downward transitions:</p>
\[
B_{12} N_1 \rho(\nu) = A_{21} N_2 + B_{21} N_2 \rho(\nu)
\]
<p>Solving for the radiation energy density \(\rho(\nu)\) yields:</p>
\[
\rho(\nu) = \frac{A_{21}}{B_{12}\frac{N_1}{N_2} - B_{21}}
\]
<p>According to the Maxwell-Boltzmann distribution, the ratio of populations of states with degeneracies \(g_1\) and \(g_2\) is:</p>
\[
\frac{N_1}{N_2} = \frac{g_1}{g_2} \exp\left(\frac{h\nu}{k_B T}\right)
\]
<p>Substituting into the expression for \(\rho(\nu)\):</p>
\[
\rho(\nu) = \frac{A_{21}}{B_{12}\frac{g_1}{g_2} e^{h\nu / k_B T} - B_{21}}
\]
<p>Comparing this directly with Planck's blackbody radiation law:</p>
\[
\rho(\nu) = \frac{8\pi h \nu^3}{c^3} \frac{1}{e^{h\nu / k_B T} - 1}
\]
<p>Equating coefficients requires two rigorous equalities:</p>
\[
g_1 B_{12} = g_2 B_{21} \implies B_{12} = \frac{g_2}{g_1} B_{21}
\]
\[
\frac{A_{21}}{B_{21}} = \frac{8\pi h \nu^3}{c^3} = \frac{8\pi h}{\lambda^3}
\]
<p>The \(\nu^3\) dependence reveals why spontaneous emission is negligible in the microwave and radiofrequency regimes (\(A_{21} \ll B_{21}\rho\)), whereas in visible and UV spectroscopy, spontaneous emission dominates radiative relaxation.</p>"""
            },
            {
                "id": "u1-sec3",
                "number": "1.3",
                "title": "Quantum Transition Dipole Moments & Selection Rules",
                "content": r"""<p>The interaction Hamiltonian between an electromagnetic plane wave polarized along \(\hat{e}\) and molecular charges is formulated in the electric dipole approximation as \(\hat{H}'(t) = -\hat{\vec{\mu}} \cdot \vec{E}(t)\), where \(\hat{\vec{\mu}} = \sum_i q_i \vec{r}_i\) is the electric dipole operator.</p>
<p>Using time-dependent perturbation theory, Fermi's Golden Rule defines the transition probability per unit time \(W_{fi}\) between initial state \(|\psi_i\rangle\) and final state \(|\psi_f\rangle\):</p>
\[
W_{fi} = \frac{2\pi}{\hbar} |\langle \psi_f | \hat{H}' | \psi_i \rangle|^2 \rho(E_f) = \frac{2\pi}{\hbar} |\vec{\mu}_{fi}|^2 |\vec{E}_0|^2 \delta(E_f - E_i - \hbar\omega)
\]
<h4 class="content-heading">Transition Dipole Moment Integral</h4>
<p>The transition dipole moment vector \(\vec{\mu}_{fi}\) is defined explicitly as:</p>
\[
\vec{\mu}_{fi} = \int \psi_f^*(\vec{r}) \hat{\vec{\mu}} \psi_i(\vec{r}) d\tau = \langle \psi_f | \hat{\vec{\mu}} | \psi_i \rangle
\]
<p>Spectral intensity is proportional to the square of the transition moment, \(I_{fi} \propto |\vec{\mu}_{fi}|^2\). A transition is defined as <em>electric dipole allowed</em> if and only if:</p>
\[
\vec{\mu}_{fi} \neq 0
\]
<p>If \(\vec{\mu}_{fi} = 0\), the transition is <em>forbidden</em> in the electric dipole approximation, though it may occur weakly through higher-order interactions such as magnetic dipole or electric quadrupole moments.</p>
<h4 class="content-heading">Einstein B-Coefficient from Quantum Mechanics</h4>
<p>Averaging over all isotropic molecular orientations in space, the quantum mechanical expression for the Einstein absorption coefficient is:</p>
\[
B_{12} = \frac{2\pi}{3\hbar^2} |\vec{\mu}_{12}|^2 = \frac{8\pi^3}{3h^2} |\vec{\mu}_{12}|^2
\]
<p>The dimensionless oscillator strength \(f_{12}\), characterizing the classical electron oscillator equivalent of the quantum transition, is defined as:</p>
\[
f_{12} = \frac{8\pi^2 m_e \nu_{12}}{3 h e^2} |\vec{\mu}_{12}|^2 = \frac{4\pi m_e \nu_{12}}{3 \hbar e^2} |\vec{\mu}_{12}|^2
\]
<p>The Thomas-Reiche-Kuhn sum rule states that for an \(N\)-electron system, \(\sum_f f_{fi} = N\).</p>"""
            },
            {
                "id": "u1-sec4",
                "number": "1.4",
                "title": "Spectral Linewidths & Broadening Mechanisms",
                "content": r"""<p>An ideal spectroscopic transition between two perfectly sharp quantum states would produce an infinitely sharp Dirac delta function line. In real physical systems, every spectral transition possesses finite width described by a line shape function \(g(\nu)\), normalized such that \(\int_0^\infty g(\nu)d\nu = 1\).</p>
<h4 class="content-heading">1. Natural (Lifetime) Broadening</h4>
<p>According to the Heisenberg energy-time uncertainty principle, a state with finite lifetime \(\tau\) has an uncertainty in energy \(\Delta E\):</p>
\[
\Delta E \Delta t \ge \frac{\hbar}{2} \implies \Delta \nu_{\text{nat}} \ge \frac{1}{2\pi \tau}
\]
<p>If state 2 has lifetime \(\tau_2\) and state 1 has lifetime \(\tau_1\), the total damping rate is \(\gamma = \frac{1}{\tau_1} + \frac{1}{\tau_2}\). The resulting spectral profile is a <strong>Lorentzian</strong> line shape:</p>
\[
g_L(\nu) = \frac{1}{\pi} \frac{\frac{\Gamma}{2}}{(\nu - \nu_0)^2 + \left(\frac{\Gamma}{2}\right)^2}
\]
<p>The Full Width at Half Maximum (FWHM) of a Lorentzian line is \(\Delta \nu_{\text{FWHM}} = \Gamma = \frac{\gamma}{2\pi}\). For an excited electronic state with spontaneous radiative lifetime \(\tau \sim 10\text{ ns}\), \(\Delta \nu_{\text{nat}} \approx 16\text{ MHz}\) (\(5 \times 10^{-4}\text{ cm}^{-1}\)).</p>
<h4 class="content-heading">2. Collisional (Pressure) Broadening</h4>
<p>In gases, collisions between molecules interrupt the phase of the emitted or absorbed radiation wave train. If the mean time between collisions is \(\tau_{\text{coll}}\), the effective lifetime decreases:</p>
\[
\frac{1}{\tau_{\text{eff}}} = \frac{1}{\tau_{\text{nat}}} + \frac{1}{\tau_{\text{coll}}} = \frac{1}{\tau_{\text{nat}}} + 2 z_{\text{coll}}
\]
<p>Kinetic theory gives the collision frequency \(z_{\text{coll}} = \sqrt{2} \pi d^2 \bar{v} n\), where \(d\) is the collision diameter, \(\bar{v} = \sqrt{\frac{8 k_B T}{\pi m}}\) is the average molecular speed, and \(n = P / (k_B T)\) is number density. Collisional broadening also yields a Lorentzian profile with FWHM proportional to pressure \(P\): \(\Delta \nu_{\text{coll}} \propto P\).</p>"""
            },
            {
                "id": "u1-sec5",
                "number": "1.5",
                "title": "Doppler Broadening & Voigt Line Profiles",
                "content": r"""<p>In gas-phase spectroscopy, molecules move randomly with a Maxwell-Boltzmann velocity distribution. A molecule moving with velocity component \(v_z\) along the line of sight of radiation of frequency \(\nu_0\) experiences a Doppler shift:</p>
\[
\nu = \nu_0 \left(1 + \frac{v_z}{c}\right)
\]
<p>The one-dimensional Maxwell-Boltzmann velocity distribution is given by:</p>
\[
P(v_z) dv_z = \sqrt{\frac{m}{2\pi k_B T}} \exp\left(-\frac{m v_z^2}{2 k_B T}\right) dv_z
\]
<h4 class="content-heading">Gaussian Doppler Line Shape</h4>
<p>Substituting \(v_z = c(\nu - \nu_0)/\nu_0\) into the velocity distribution yields the <strong>Gaussian</strong> Doppler line shape function:</p>
\[
g_D(\nu) = \sqrt{\frac{m c^2}{2\pi k_B T \nu_0^2}} \exp\left(-\frac{m c^2 (\nu - \nu_0)^2}{2 k_B T \nu_0^2}\right)
\]
<p>The peak height occurs at \(\nu = \nu_0\). The Full Width at Half Maximum (FWHM) \(\Delta \nu_D\) is obtained where \(g_D(\nu) = \frac{1}{2} g_D(\nu_0)\):</p>
\[
\exp\left(-\frac{m c^2 (\Delta \nu_D / 2)^2}{2 k_B T \nu_0^2}\right) = \frac{1}{2} \implies \Delta \nu_D = 2\nu_0 \sqrt{\frac{2 k_B T \ln 2}{m c^2}} = \sqrt{\frac{8 k_B T \ln 2}{m c^2}} \nu_0
\]
<p>Expressed in terms of molar mass \(M = N_A m\) and gas constant \(R = N_A k_B\):</p>
\[
\frac{\Delta \nu_D}{\nu_0} = 7.16 \times 10^{-7} \sqrt{\frac{T}{M\ (\text{g/mol})}}
\]
<h4 class="content-heading">The Voigt Profile</h4>
<p>When both homogeneous (Lorentzian, FWHM \(\Gamma\)) and inhomogeneous (Gaussian, FWHM \(\Delta\nu_D\)) broadening mechanisms are significant, the observed spectral line is the convolution of both distributions, known as the <strong>Voigt profile</strong>:</p>
\[
g_V(\nu) = \int_{-\infty}^{\infty} g_L(\nu - \nu') g_D(\nu') d\nu'
\]
<p>The Voigt profile exhibits a Gaussian core near the line center with extended Lorentzian wings (tails) decaying as \((\nu - \nu_0)^{-2}\).</p>"""
            },
            {
                "id": "u1-sec6",
                "number": "1.6",
                "title": "Sub-Doppler Techniques: Lamb Dip & Two-Photon Spectroscopy",
                "content": r"""<p>Because Doppler broadening frequently obscures fine and hyperfine structures in gas-phase spectroscopy, specialized non-linear laser techniques have been developed to eliminate Doppler broadening entirely.</p>
<h4 class="content-heading">1. Saturated Absorption & The Lamb Dip</h4>
<p>Consider two counter-propagating laser beams (a strong 'pump' beam and a weak 'probe' beam) traversing a gas cell at frequency \(\nu\):</p>
<ul>
  <li>If \(\nu \neq \nu_0\), the pump beam interacts only with molecules having velocity \(v_z = c(\nu - \nu_0)/\nu_0\), burning a 'hole' in the ground state velocity distribution. The probe beam travels in the opposite direction and interacts with molecules having velocity \(-v_z\), thus seeing an unperturbed population.</li>
  <li>If \(\nu = \nu_0\), both beams interact simultaneously with the same velocity group: molecules with \(v_z = 0\) (zero longitudinal velocity). The intense pump beam bleaches/saturates the absorption for these stationary molecules. Consequently, the probe beam experiences sharply reduced absorption, producing a transmission spike at \(\nu = \nu_0\) known as the <strong>Lamb dip</strong>.</li>
</ul>
<p>The linewidth of the Lamb dip is governed solely by the homogeneous Lorentzian width \(\Gamma_{\text{hom}} \ll \Delta\nu_D\), enabling ultra-high resolution frequency standards.</p>
<h4 class="content-heading">2. Doppler-Free Two-Photon Spectroscopy</h4>
<p>When an atomic or molecular transition occurs via the simultaneous absorption of two photons from counter-propagating laser beams with identical frequency \(\omega\):</p>
\[
E_f - E_i = \hbar \omega_1 + \hbar \omega_2 = \hbar \omega\left(1 + \frac{v_z}{c}\right) + \hbar \omega\left(1 - \frac{v_z}{c}\right) = 2\hbar\omega
\]
<p>The linear Doppler shifts identically cancel for all velocity classes \(v_z\)! Every molecule in the gas cell absorbs at exactly \(2\omega = (E_f - E_i)/\hbar\), producing a Doppler-free absorption resonance whose resolution is limited only by the natural radiative lifetime.</p>"""
            },
            {
                "id": "u1-sec7",
                "number": "1.7",
                "title": "Signal-to-Noise Ratio, Resolving Power & Detection Thresholds",
                "content": r"""<p>The fidelity and quantitative accuracy of any spectroscopic measurement depend fundamentally on the Signal-to-Noise ratio (\(S/N\)) and the instrumental resolving power \(R\).</p>
<h4 class="content-heading">Signal-to-Noise Ratio (S/N) & Averaging</h4>
<p>In repeated experimental measurements consisting of \(N\) independent co-added spectral scans, the signal accumulates coherently while random (uncorrelated) noise accumulates in quadrature:</p>
\[
S_N = N \cdot S_1, \quad \sigma_N = \sqrt{N} \cdot \sigma_1 \implies \left(\frac{S}{N}\right)_N = \frac{N \cdot S_1}{\sqrt{N} \cdot \sigma_1} = \sqrt{N} \left(\frac{S}{N}\right)_1
\]
<p>Thus, improving the \(S/N\) ratio by a factor of 10 requires averaging \(N = 100\) scans.</p>
<h4 class="content-heading">Noise Sources in Practical Spectroscopy</h4>
<ol>
  <li><strong>Johnson-Nyquist (Thermal) Noise:</strong> Voltage fluctuations in resistive detector circuits: \(\sigma_V = \sqrt{4 k_B T R \Delta f}\), where \(\Delta f\) is the measurement bandwidth.</li>
  <li><strong>Shot Noise:</strong> Quantum fluctuations in discrete photon arrival: \(\sigma_{\text{shot}} = \sqrt{2 e I \Delta f}\). Shot-noise-limited detection obeys Poisson statistics: \(S/N = \sqrt{N_{\text{photons}}}\).</li>
  <li><strong>Flicker (\(1/f\)) Noise:</strong> Low-frequency instrumental drift, eliminated using lock-in amplification and high-frequency phase modulation.</li>
</ol>
<h4 class="content-heading">Chromatic Resolving Power</h4>
<p>The resolving power \(R\) of a spectrometer characterizes its ability to distinguish two adjacent spectral lines separated by \(\Delta \lambda\):</p>
\[
R = \frac{\lambda}{\Delta \lambda} = \frac{\nu}{\Delta \nu} = \frac{\tilde{\nu}}{\Delta \tilde{\nu}}
\]
<p>For a diffraction grating of width \(W\) and groove density \(N_{\text{total}}\) operated in diffraction order \(m\), the theoretical resolving power is \(R = m N_{\text{total}}\). For a prism of base length \(b\), \(R = b \left|\frac{dn}{d\lambda}\right|\).</p>"""
            }
        ],
        "problems": [
            {
                "id": "u1-prob1",
                "number": 1,
                "title": "Calculation of Photon Wavenumber, Frequency and Molar Energy",
                "difficulty": "Foundational",
                "statement": r"""A spectroscopic transition is observed at wavelength \(\lambda = 589.0\text{ nm}\) (the sodium D₂ line). Calculate:
(a) The frequency \(\nu\) in Hz.
(b) The spectroscopic wavenumber \(\tilde{\nu}\) in \(\text{cm}^{-1}\).
(c) The energy of a single photon in Joules and electron-volts (\(\text{eV}\)).
(d) The molar energy of the transition in \(\text{kJ/mol}\).""",
                "solution": r"""<p><strong>Step (a): Frequency calculation</strong></p>
\[
\nu = \frac{c}{\lambda} = \frac{2.99792 \times 10^8\text{ m/s}}{589.0 \times 10^{-9}\text{ m}} = 5.08985 \times 10^{14}\text{ Hz}
\]
<p><strong>Step (b): Wavenumber calculation</strong></p>
\[
\tilde{\nu} = \frac{1}{\lambda} = \frac{1}{589.0 \times 10^{-7}\text{ cm}} = 16977.9\text{ cm}^{-1}
\]
<p><strong>Step (c): Energy per photon</strong></p>
\[
E = h\nu = (6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(5.08985 \times 10^{14}\text{ s}^{-1}) = 3.37257 \times 10^{-19}\text{ J}
\]
<p>In electron-volts (\(1\text{ eV} = 1.60217663 \times 10^{-19}\text{ J}\)):</p>
\[
E = \frac{3.37257 \times 10^{-19}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} = 2.1050\text{ eV}
\]
<p><strong>Step (d): Molar energy</strong></p>
\[
E_{\text{molar}} = N_A \cdot E = (6.02214 \times 10^{23}\text{ mol}^{-1})(3.37257 \times 10^{-19}\text{ J}) = 203.099\text{ kJ/mol}
\]"""
            },
            {
                "id": "u1-prob2",
                "number": 2,
                "title": "Ratio of Spontaneous to Stimulated Emission in Microwave vs Optical Regimes",
                "difficulty": "Intermediate",
                "statement": r"""Compare the ratio of the spontaneous emission rate to the stimulated emission rate \(\frac{A_{21}}{B_{21}\rho(\nu)}\) for a system at thermal equilibrium at \(T = 300\text{ K}\) in:
(a) The microwave regime at \(\nu = 10\text{ GHz}\) (\(\lambda = 3.0\text{ cm}\)).
(b) The visible optical regime at \(\lambda = 500\text{ nm}\) (\(\nu = 6.0 \times 10^{14}\text{ Hz}\)).
Discuss the physical implications for laser action and microwave amplification.""",
                "solution": r"""<p><strong>Derivation of the rate ratio:</strong></p>
<p>From the Einstein detailed balance equation, the ratio of spontaneous to stimulated emission rates at equilibrium is:</p>
\[
\frac{R_{\text{spont}}}{R_{\text{stim}}} = \frac{A_{21} N_2}{B_{21} N_2 \rho(\nu)} = \frac{A_{21}}{B_{21}\rho(\nu)} = e^{h\nu / k_B T} - 1
\]
<p>At \(T = 300\text{ K}\), the thermal energy parameter is:</p>
\[
k_B T = (1.38065 \times 10^{-23}\text{ J/K})(300\text{ K}) = 4.14195 \times 10^{-21}\text{ J}
\]
<p><strong>Case (a): Microwave regime (\(\nu = 10^{10}\text{ Hz}\))</strong></p>
\[
h\nu = (6.62607 \times 10^{-34})(10^{10}) = 6.62607 \times 10^{-24}\text{ J}
\]
\[
\frac{h\nu}{k_B T} = \frac{6.62607 \times 10^{-24}}{4.14195 \times 10^{-21}} = 1.60 \times 10^{-3}
\]
<p>Since \(h\nu \ll k_B T\), we expand the exponential: \(e^x - 1 \approx x\):</p>
\[
\frac{A_{21}}{B_{21}\rho(\nu)} \approx 1.60 \times 10^{-3}
\]
<p>In the microwave regime, stimulated emission vastly dominates over spontaneous emission by a factor of \(\sim 625\). Spontaneous noise is minimal, enabling maser amplification.</p>
<p><strong>Case (b): Optical regime (\(\nu = 6.0 \times 10^{14}\text{ Hz}\))</strong></p>
\[
h\nu = (6.62607 \times 10^{-34})(6.0 \times 10^{14}) = 3.9756 \times 10^{-19}\text{ J}
\]
\[
\frac{h\nu}{k_B T} = \frac{3.9756 \times 10^{-19}}{4.14195 \times 10^{-21}} = 95.98
\]
\[
\frac{A_{21}}{B_{21}\rho(\nu)} = e^{95.98} - 1 \approx 4.8 \times 10^{41}
\]
<p>In the visible domain at room temperature, spontaneous emission dominates over stimulated thermal emission by over 41 orders of magnitude! Achieving laser action requires an intense non-equilibrium population inversion (\(N_2 > N_1\)).</p>"""
            },
            {
                "id": "u1-prob3",
                "number": 3,
                "title": "Evaluation of Doppler FWHM Linewidth for Hydrogen vs Iodine Gas",
                "difficulty": "Intermediate",
                "statement": r"""Calculate the Doppler broadening FWHM \(\Delta \nu_D\) (in MHz and \(\text{cm}^{-1}\)) at \(T = 300\text{ K}\) for:
(a) The atomic hydrogen Lyman-\(\alpha\) line at \(\lambda = 121.6\text{ nm}\) (\(M = 1.008\text{ g/mol}\)).
(b) The molecular iodine (\(\text{I}_2\)) absorption line at \(\lambda = 514.5\text{ nm}\) (\(M = 253.8\text{ g/mol}\)).
Explain how atomic mass and transition frequency govern the Doppler width.""",
                "solution": r"""<p><strong>General Doppler FWHM Formula:</strong></p>
\[
\Delta \nu_D = \nu_0 \sqrt{\frac{8 k_B T \ln 2}{m c^2}} = \frac{c}{\lambda} \sqrt{\frac{8 R T \ln 2}{M c^2}} = \frac{1}{\lambda} \sqrt{\frac{8 R T \ln 2}{M}}
\]
<p>Here \(\sqrt{8 R T \ln 2} = \sqrt{8(8.31446)(300)(0.69315)} = \sqrt{13837.7} = 117.634\text{ m/s}\cdot(\text{kg/mol})^{1/2}\).</p>
<p><strong>Case (a): Hydrogen atom (\(M = 1.008 \times 10^{-3}\text{ kg/mol}\), \(\lambda = 121.6 \times 10^{-9}\text{ m}\))</strong></p>
\[
\Delta \nu_D = \frac{1}{121.6 \times 10^{-9}\text{ m}} \frac{117.634}{\sqrt{1.008 \times 10^{-3}}} = (8.2237 \times 10^6)(3705.5) = 3.047 \times 10^{10}\text{ Hz} = 30470\text{ MHz}
\]
<p>In wavenumbers:</p>
\[
\Delta \tilde{\nu}_D = \frac{\Delta \nu_D}{c} = \frac{3.047 \times 10^{10}}{2.99792 \times 10^{10}\text{ cm/s}} = 1.016\text{ cm}^{-1}
\]
<p><strong>Case (b): Iodine molecule (\(M = 0.2538\text{ kg/mol}\), \(\lambda = 514.5 \times 10^{-9}\text{ m}\))</strong></p>
\[
\Delta \nu_D = \frac{1}{514.5 \times 10^{-9}\text{ m}} \frac{117.634}{\sqrt{0.2538}} = (1.9436 \times 10^6)(233.5) = 4.538 \times 10^8\text{ Hz} = 453.8\text{ MHz}
\]
<p>In wavenumbers:</p>
\[
\Delta \tilde{\nu}_D = \frac{4.538 \times 10^8}{2.99792 \times 10^{10}} = 0.0151\text{ cm}^{-1}
\]
<p><strong>Comparison:</strong> Hydrogen has a Doppler width nearly 67 times larger than iodine because Doppler broadening scales inversely with the square root of mass (\(\propto M^{-1/2}\)) and directly with transition frequency (\(\propto \nu_0\)).</p>"""
            },
            {
                "id": "u1-prob4",
                "number": 4,
                "title": "Lifetime Broadening and Einstein A-Coefficient Derivation",
                "difficulty": "Advanced",
                "statement": r"""An excited electronic state of a molecule has a transition dipole moment \(|\mu_{12}| = 1.50\text{ Debye}\) (\(1\text{ D} = 3.33564 \times 10^{-30}\text{ C}\cdot\text{m}\)) to the ground state at transition wavelength \(\lambda = 400.0\text{ nm}\).
(a) Calculate the Einstein spontaneous emission coefficient \(A_{21}\) in \(\text{s}^{-1}\).
(b) Determine the natural radiative lifetime \(\tau\) of the excited state.
(c) Calculate the natural Lorentzian linewidth FWHM \(\Delta \nu_{\text{nat}}\) in MHz and in \(\text{cm}^{-1}\).""",
                "solution": r"""<p><strong>Step (a): Einstein A-coefficient</strong></p>
<p>The relation between Einstein \(A_{21}\) and transition dipole moment \(|\mu_{12}|\) in SI units is:</p>
\[
A_{21} = \frac{16 \pi^3 \nu^3}{3 \varepsilon_0 h c^3} |\mu_{12}|^2 = \frac{16 \pi^3}{3 \varepsilon_0 h \lambda^3} |\mu_{12}|^2
\]
<p>Given parameters:</p>
<ul>
  <li>\(\lambda = 4.00 \times 10^{-7}\text{ m} \implies \lambda^3 = 6.40 \times 10^{-20}\text{ m}^3\)</li>
  <li>\(|\mu_{12}| = 1.50 \times 3.33564 \times 10^{-30} = 5.00346 \times 10^{-30}\text{ C}\cdot\text{m}\)</li>
  <li>\(|\mu_{12}|^2 = 2.50346 \times 10^{-59}\text{ C}^2\cdot\text{m}^2\)</li>
  <li>\(\varepsilon_0 = 8.85419 \times 10^{-12}\text{ F/m}\), \(h = 6.62607 \times 10^{-34}\text{ J}\cdot\text{s}\)</li>
</ul>
<p>Denominator:</p>
\[
3 \varepsilon_0 h \lambda^3 = 3(8.85419 \times 10^{-12})(6.62607 \times 10^{-34})(6.40 \times 10^{-20}) = 1.1259 \times 10^{-63}
\]
<p>Numerator:</p>
\[
16 \pi^3 |\mu_{12}|^2 = 16(31.0063)(2.50346 \times 10^{-59}) = 1.24197 \times 10^{-57}
\]
\[
A_{21} = \frac{1.24197 \times 10^{-57}}{1.1259 \times 10^{-63}} = 1.103 \times 10^6\text{ s}^{-1}
\]
<p><strong>Step (b): Natural radiative lifetime</strong></p>
\[
\tau = \frac{1}{A_{21}} = \frac{1}{1.103 \times 10^6\text{ s}^{-1}} = 9.066 \times 10^{-7}\text{ s} \approx 907\text{ ns}
\]
<p><strong>Step (c): Natural linewidth FWHM</strong></p>
\[
\Delta \nu_{\text{nat}} = \frac{A_{21}}{2\pi} = \frac{1.103 \times 10^6}{2\pi} = 1.756 \times 10^5\text{ Hz} = 0.176\text{ MHz}
\]
<p>In wavenumbers:</p>
\[
\Delta \tilde{\nu}_{\text{nat}} = \frac{\Delta \nu_{\text{nat}}}{c} = \frac{1.756 \times 10^5\text{ s}^{-1}}{2.99792 \times 10^{10}\text{ cm/s}} = 5.86 \times 10^{-6}\text{ cm}^{-1}
\]"""
            },
            {
                "id": "u1-prob5",
                "number": 5,
                "title": "Signal-to-Noise Improvement Factor and Scan Co-addition",
                "difficulty": "Foundational",
                "statement": r"""A single scan of an infrared spectrum yields an absorption peak with signal amplitude \(S = 0.45\text{ V}\) and root-mean-square noise \(\sigma = 0.15\text{ V}\).
(a) Determine the initial signal-to-noise ratio \((S/N)_1\).
(b) How many scans \(N\) must be co-added to achieve a target \(S/N \ge 60\)?
(c) If each scan requires \(2.5\text{ seconds}\), how long will the total data acquisition take?""",
                "solution": r"""<p><strong>Step (a): Initial S/N ratio</strong></p>
\[
\left(\frac{S}{N}\right)_1 = \frac{S_1}{\sigma_1} = \frac{0.45\text{ V}}{0.15\text{ V}} = 3.0
\]
<p><strong>Step (b): Number of co-added scans</strong></p>
<p>Using the square-root scaling law for uncorrelated white noise:</p>
\[
\left(\frac{S}{N}\right)_N = \sqrt{N} \left(\frac{S}{N}\right)_1
\]
\[
60 = \sqrt{N} \times 3.0 \implies \sqrt{N} = 20 \implies N = 20^2 = 400\text{ scans}
\]
<p><strong>Step (c): Total acquisition time</strong></p>
\[
t_{\text{total}} = N \times t_{\text{scan}} = 400 \times 2.5\text{ s} = 1000\text{ seconds} = 16\text{ minutes and } 40\text{ seconds}
\]"""
            },
            {
                "id": "u1-prob6",
                "number": 6,
                "title": "Resolving Power and Grating Specifications for Sodium Doublet",
                "difficulty": "Intermediate",
                "statement": r"""The sodium doublet consists of two yellow lines at \(\lambda_1 = 589.592\text{ nm}\) (\(D_1\)) and \(\lambda_2 = 588.995\text{ nm}\) (\(D_2\)).
(a) Calculate the minimum resolving power \(R\) required to resolve this doublet according to Rayleigh's criterion.
(b) If a diffraction grating with groove density \(600\text{ lines/mm}\) is used in the first diffraction order (\(m=1\)), what is the minimum illuminated grating width \(W\) needed?
(c) What minimum grating width would be required if the second order (\(m=2\)) is used?""",
                "solution": r"""<p><strong>Step (a): Required resolving power</strong></p>
\[
\bar{\lambda} = \frac{589.592 + 588.995}{2} = 589.2935\text{ nm}
\]
\[
\Delta \lambda = 589.592 - 588.995 = 0.597\text{ nm}
\]
\[
R = \frac{\bar{\lambda}}{\Delta \lambda} = \frac{589.2935}{0.597} \approx 987.1 \implies R_{\min} \approx 988
\]
<p><strong>Step (b): Grating width in first order (\(m=1\))</strong></p>
<p>The resolving power of a grating is \(R = m N_{\text{total}}\), where \(N_{\text{total}} = W \cdot d_{\text{lines}}\):</p>
\[
N_{\text{total}} = \frac{R}{m} = \frac{987.1}{1} \approx 988\text{ total rulings}
\]
\[
W = \frac{N_{\text{total}}}{600\text{ lines/mm}} = \frac{987.1}{600} = 1.645\text{ mm}
\]
<p><strong>Step (c): Grating width in second order (\(m=2\))</strong></p>
\[
N_{\text{total}} = \frac{R}{2} = \frac{987.1}{2} = 493.6\text{ rulings}
\]
\[
W = \frac{493.6}{600\text{ lines/mm}} = 0.823\text{ mm}
\]"""
            },
            {
                "id": "u1-prob7",
                "number": 7,
                "title": "Nyquist Sampling Theorem and Fourier Transform Retardation",
                "difficulty": "Advanced",
                "statement": r"""In a Fourier Transform Infrared (FTIR) spectrometer, the mirror of the Michelson interferometer moves with constant velocity \(v = 1.25\text{ mm/s}\).
(a) If the spectrometer acquires spectra up to \(\tilde{\nu}_{\max} = 4000\text{ cm}^{-1}\), what is the maximum optical retardation sampling interval \(\Delta \delta\) required by the Nyquist sampling theorem?
(b) Calculate the modulation frequency \(f = 2 v \tilde{\nu}\) for radiation at \(\tilde{\nu} = 4000\text{ cm}^{-1}\) and \(\tilde{\nu} = 400\text{ cm}^{-1}\).
(c) To achieve an instrumental spectral resolution of \(\Delta \tilde{\nu} = 0.5\text{ cm}^{-1}\), what total optical retardation \(\delta_{\max}\) and mirror physical displacement \(L\) are required?""",
                "solution": r"""<p><strong>Step (a): Nyquist sampling interval</strong></p>
<p>According to the Nyquist-Shannon sampling theorem, the sampling interval in optical retardation \(\Delta \delta\) must be at least twice per cycle of the highest frequency present:</p>
\[
\Delta \delta \le \frac{1}{2 \tilde{\nu}_{\max}} = \frac{1}{2(4000\text{ cm}^{-1})} = \frac{1}{8000}\text{ cm} = 1.25 \times 10^{-4}\text{ cm} = 1.25\ \mu\text{m}
\]
<p>Standard FTIR spectrometers use a He-Ne laser reference (\(\lambda_{\text{HeNe}} = 632.8\text{ nm}\)), sampling at zero-crossings (\(\Delta \delta = \lambda / 2 = 316.4\text{ nm}\)), which comfortably exceeds this threshold.</p>
<p><strong>Step (b): Modulation frequency calculation</strong></p>
<p>The optical retardation changes at rate \(\frac{d\delta}{dt} = 2v = 2(0.125\text{ cm/s}) = 0.25\text{ cm/s}\). The audio modulation frequency is:</p>
\[
f = 2 v \tilde{\nu}
\]
<p>For \(\tilde{\nu} = 4000\text{ cm}^{-1}\):</p>
\[
f_1 = (0.25\text{ cm/s})(4000\text{ cm}^{-1}) = 1000\text{ Hz} = 1.0\text{ kHz}
\]
<p>For \(\tilde{\nu} = 400\text{ cm}^{-1}\):</p>
\[
f_2 = (0.25\text{ cm/s})(400\text{ cm}^{-1}) = 100\text{ Hz}
\]
<p>The entire mid-IR spectrum is transformed into the convenient audio frequency range (100 Hz – 1 kHz).</p>
<p><strong>Step (c): Required optical retardation and mirror displacement</strong></p>
<p>The spectral resolution \(\Delta \tilde{\nu}\) is inversely related to maximum retardation:</p>
\[
\Delta \tilde{\nu} \approx \frac{1}{\delta_{\max}} \implies \delta_{\max} = \frac{1}{0.5\text{ cm}^{-1}} = 2.0\text{ cm}
\]
<p>Since optical retardation \(\delta = 2 L\) (double pass of the moving mirror):</p>
\[
L = \frac{\delta_{\max}}{2} = \frac{2.0\text{ cm}}{2} = 1.0\text{ cm}
\]"""
            }
        ]
    }
    units.append(u1)

    # =========================================================================
    # UNIT 2: Rotational & Microwave Spectroscopy of Diatomic & Polyatomic Rotors
    # =========================================================================
    u2 = {
        "id": "unit2",
        "number": 2,
        "title": "Unit 2: Rotational & Microwave Spectroscopy of Diatomic & Polyatomic Rotors",
        "description": "Rigid and non-rigid rotor mechanics, moment of inertia tensors, rotational constant B, bond length determination from isotopic substitution, centrifugal distortion constant D, classification of polyatomic rotors, Stark effect and electric dipole moments, microwave instrumentation and dielectric loss mechanisms.",
        "simulations": [
            {
                "id": "sim_spec_rotational_microwave_rotor",
                "title": "Rigid/Non-Rigid Rotor & Stark Splitting",
                "description": "Interactive 60 FPS Canvas simulation of a rotating diatomic molecule with centrifugal distortion and electric-field-induced Stark splitting. Modify the rotational constant B, temperature T, and applied electric field to observe the splitting of rotational energy states into MJ components and monitor the resulting microwave stick spectrum."
            }
        ],
        "sections": [
            {
                "id": "u2-sec1",
                "number": "2.1",
                "title": "Classical & Quantum Mechanics of Free Rigid Rotators",
                "content": r"""<p>A rigid diatomic rotator consists of two point masses \(m_1\) and \(m_2\) held at fixed bond length \(r_0\). In center-of-mass coordinates, this two-body problem reduces to the motion of a single fictitious particle with reduced mass \(\mu\) at distance \(r_0\) from the origin:</p>
\[
\mu = \frac{m_1 m_2}{m_1 + m_2}, \quad I = \mu r_0^2
\]
<p>where \(I\) is the moment of inertia. Classically, the kinetic energy of rotation with angular velocity \(\omega\) is \(E_{\text{rot}} = \frac{1}{2} I \omega^2 = \frac{J^2}{2I}\), where \(J = I\omega\) is the magnitude of the angular momentum vector.</p>
<h4 class="content-heading">Schrödinger Equation & Spherical Harmonics</h4>
<p>Quantum mechanically, the Hamiltonian for a free rigid rotor is:</p>
\[
\hat{H} = \frac{\hat{J}^2}{2I} = -\frac{\hbar^2}{2I} \left[ \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2} \right]
\]
<p>The eigenfunctions of \(\hat{J}^2\) are the spherical harmonics \(Y_{J, M_J}(\theta, \phi)\), with eigenvalues:</p>
\[
\hat{J}^2 Y_{J, M_J} = \hbar^2 J(J+1) Y_{J, M_J}, \quad \hat{J}_z Y_{J, M_J} = \hbar M_J Y_{J, M_J}
\]
<p>where \(J = 0, 1, 2, \dots\) is the rotational quantum number, and \(M_J = -J, -J+1, \dots, +J\) is the magnetic quantum number. The energy eigenvalues are:</p>
\[
E_J = \frac{\hbar^2}{2I} J(J+1)
\]
<p>Each rotational energy level \(E_J\) is \((2J+1)\)-fold degenerate in the absence of external fields.</p>"""
            },
            {
                "id": "u2-sec2",
                "number": "2.2",
                "title": "Rotational Term Values, Constant B & Selection Rules",
                "content": r"""<p>In spectroscopy, rotational energy levels are universally expressed in wavenumber units (\(\text{cm}^{-1}\)) as rotational term values \(F(J) = E_J / (hc)\):</p>
\[
F(J) = B J(J+1)
\]
<p>where \(B\) is the <strong>rotational constant</strong>:</p>
\[
B = \frac{h}{8\pi^2 c I} = \frac{\hbar}{4\pi c \mu r_0^2}
\]
<h4 class="content-heading">Gross & Specific Selection Rules</h4>
<p>The interaction between the rotating molecule and microwave radiation requires the dipole matrix element to be non-zero:</p>
<ol>
  <li><strong>Gross Selection Rule:</strong> The molecule must possess a <em>permanent electric dipole moment</em>: \(\mu_0 \neq 0\). Heteronuclear diatomic molecules (e.g., \(\text{CO}, \text{HCl}, \text{NO}\)) exhibit pure rotational microwave spectra, whereas homonuclear diatomics (e.g., \(\text{N}_2, \text{O}_2, \text{H}_2\)) have zero permanent dipole moment and are completely microwave-inactive.</li>
  <li><strong>Specific Selection Rule:</strong> For transitions within an electric dipole permitted manifold:
  \[
  \Delta J = \pm 1, \quad \Delta M_J = 0, \pm 1
  \]
  </li>
</ol>
<h4 class="content-heading">Rotational Transition Frequencies</h4>
<p>For an absorption transition from level \(J\) to \(J+1\):</p>
\[
\tilde{\nu}_{J \to J+1} = F(J+1) - F(J) = B(J+1)(J+2) - BJ(J+1) = 2B(J+1)
\]
<p>This yields a sequence of equally spaced lines in the microwave spectrum:</p>
\[
\tilde{\nu}_{0\to 1} = 2B, \quad \tilde{\nu}_{1\to 2} = 4B, \quad \tilde{\nu}_{2\to 3} = 6B, \quad \tilde{\nu}_{3\to 4} = 8B, \dots
\]
<p>The separation between any two adjacent rotational absorption lines is strictly constant and equal to \(2B\):</p>
\[
\Delta \tilde{\nu} = \tilde{\nu}_{J+1\to J+2} - \tilde{\nu}_{J\to J+1} = 2B
\]
<p>Measuring \(\Delta \tilde{\nu}\) allows immediate calculation of \(B\), \(I\), and the equilibrium bond length \(r_0\) with extraordinary sub-picometer precision.</p>"""
            },
            {
                "id": "u2-sec3",
                "number": "2.3",
                "title": "Isotopic Substitution & Determination of Bond Lengths",
                "content": r"""<p>Because isotopic substitution changes the nuclear mass without altering the electronic potential energy surface, the equilibrium internuclear distance \(r_0\) remains identical between isotopologues to a very high approximation.</p>
<p>Consider two isotopologues with reduced masses \(\mu\) and \(\mu'\) (where \(\mu' > \mu\)):</p>
\[
I = \mu r_0^2, \quad I' = \mu' r_0^2 \implies \frac{B}{B'} = \frac{I'}{I} = \frac{\mu'}{\mu}
\]
<p>Since \(\mu' > \mu\), \(B' < B\). The heavier isotopologue exhibits smaller rotational line spacing. For carbon monoxide:</p>
<ul>
  <li>\(^{12}\text{C}^{16}\text{O}\): \(\mu = \frac{12.0000 \times 15.9949}{12.0000 + 15.9949} = 6.8562\text{ u} \implies B \approx 1.92118\text{ cm}^{-1}\)</li>
  <li>\(^{13}\text{C}^{16}\text{O}\): \(\mu' = \frac{13.0034 \times 15.9949}{13.0034 + 15.9949} = 7.1699\text{ u} \implies B' \approx 1.83797\text{ cm}^{-1}\)</li>
</ul>
<h4 class="content-heading">Kraitchman's Equations for Polyatomics</h4>
<p>For polyatomic molecules with multiple unknown bond lengths and angles, isotopic substitution at atom \(i\) shifts the center of mass. Kraitchman derived exact expressions determining the coordinate \(|z_i|\) of the substituted atom relative to the principal axes of the parent molecule:</p>
\[
|z_i| = \sqrt{\frac{\Delta I_x}{\mu_s}}, \quad \mu_s = \frac{M \Delta m}{M + \Delta m}
\]
<p>where \(M\) is the total molecular mass and \(\Delta m\) is the mass increase. By systematically substituting each atomic site, the complete 3D structure is elucidated without assuming bond angles.</p>"""
            },
            {
                "id": "u2-sec4",
                "number": "2.4",
                "title": "Centrifugal Distortion & Non-Rigid Rotors",
                "content": r"""<p>In real molecules, the chemical bond is not a rigid rod but an elastic spring with force constant \(k\). As the rotational quantum number \(J\) increases, the centrifugal force \(\mu \omega^2 r\) stretches the bond, increasing the moment of inertia \(I\) and slightly lowering the rotational energy levels below the rigid rotor expectation.</p>
<p>Treating centrifugal distortion with perturbation theory gives the modified rotational term formula:</p>
\[
F(J) = B J(J+1) - D J^2(J+1)^2
\]
<p>where \(D\) is the <strong>centrifugal distortion constant</strong>. For a harmonic bond with vibrational frequency \(\bar{\omega}\) (\(\text{cm}^{-1}\)), Kratzer's relation connects \(D\) directly to \(B\) and \(\bar{\omega}\):</p>
\[
D = \frac{4 B^3}{\bar{\omega}^2}
\]
<h4 class="content-heading">Transition Frequencies for Non-Rigid Rotors</h4>
<p>The absorption transition frequency becomes:</p>
\[
\tilde{\nu}_{J \to J+1} = F(J+1) - F(J) = 2B(J+1) - 4D(J+1)^3
\]
<p>The separation between consecutive lines is no longer strictly constant:</p>
\[
\Delta \tilde{\nu} = \tilde{\nu}_{J+1\to J+2} - \tilde{\nu}_{J\to J+1} = 2B - 4D[ (J+2)^3 - (J+1)^3 ] = 2B - 6D(J+1)^2 - 6D(J+1) - 4D
\]
<p>Because \(D \ll B\) (typically \(D / B \sim 10^{-4} - 10^{-5}\)), centrifugal distortion is small at low \(J\) but becomes increasingly prominent at high rotational quantum numbers.</p>"""
            },
            {
                "id": "u2-sec5",
                "number": "2.5",
                "title": "Rotational State Populations & Spectral Intensity Distribution",
                "content": r"""<p>The intensity of a rotational absorption line \(J \to J+1\) is governed by the thermal population \(N_J\) of the initial state \(J\). According to the Maxwell-Boltzmann distribution:</p>
\[
N_J \propto g_J \exp\left(-\frac{E_J}{k_B T}\right) = (2J+1) \exp\left(-\frac{h c B J(J+1)}{k_B T}\right)
\]
<p>Two opposing mathematical factors govern \(N_J\) as \(J\) increases:</p>
<ol>
  <li>The degeneracy factor \(g_J = (2J+1)\) increases linearly with \(J\), promoting population in higher states.</li>
  <li>The Boltzmann exponential factor \(\exp\left(-\frac{hcBJ(J+1)}{k_B T}\right)\) decreases exponentially with \(J(J+1)\).</li>
</ol>
<h4 class="content-heading">Finding the Most Populated State (\(J_{\max}\))</h4>
<p>To find the value of \(J\) corresponding to maximum population, we treat \(J\) as a continuous variable and set \(\frac{d N_J}{d J} = 0\):</p>
\[
\frac{d}{dJ}\left[ (2J+1) e^{-\frac{hcB J(J+1)}{k_B T}} \right] = 2 e^{-\frac{hcB J(J+1)}{k_B T}} - (2J+1) \left(\frac{hcB (2J+1)}{k_B T}\right) e^{-\frac{hcB J(J+1)}{k_B T}} = 0
\]
<p>Factoring out the non-zero exponential term:</p>
\[
2 - \frac{hcB}{k_B T} (2J+1)^2 = 0 \implies (2J+1)^2 = \frac{2 k_B T}{hcB}
\]
\[
2J+1 = \sqrt{\frac{2 k_B T}{hcB}} \implies J_{\max} = \sqrt{\frac{k_B T}{2 hcB}} - \frac{1}{2}
\]
<p>This explains why microwave spectra display a characteristic intensity envelope: spectral line intensities initially rise with \(J\), reach a smooth maximum at \(J \approx J_{\max}\), and then decay asymptotically to zero at large \(J\).</p>"""
            },
            {
                "id": "u2-sec6",
                "number": "2.6",
                "title": "Classification of Polyatomic Rotors: Spherical, Symmetric & Asymmetric Tops",
                "content": r"""<p>Polyatomic molecules possess three principal moments of inertia \(I_A \le I_B \le I_C\) along mutually orthogonal principal axes of inertia \(a, b, c\). Rotational constants are defined as:</p>
\[
A = \frac{h}{8\pi^2 c I_A}, \quad B = \frac{h}{8\pi^2 c I_B}, \quad C = \frac{h}{8\pi^2 c I_C} \quad (A \ge B \ge C)
\]
<h4 class="content-heading">Taxonomy of Molecular Rotors</h4>
<div class="table-container">
  <table class="data-table">
    <thead>
      <tr>
        <th>Rotor Class</th>
        <th>Moments of Inertia</th>
        <th>Rotational Constants</th>
        <th>Representative Examples</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Linear Rotors</td>
        <td>\(I_A = 0, I_B = I_C\)</td>
        <td>\(B = C, A = \infty\)</td>
        <td>\(\text{CO}_2, \text{HCN}, \text{OCS}, \text{C}_2\text{H}_2\)</td>
      </tr>
      <tr>
        <td>Spherical Tops</td>
        <td>\(I_A = I_B = I_C\)</td>
        <td>\(A = B = C\)</td>
        <td>\(\text{CH}_4, \text{SF}_6, \text{CCl}_4\)</td>
      </tr>
      <tr>
        <td>Prolate Symmetric Tops</td>
        <td>\(I_A < I_B = I_C\)</td>
        <td>\(A > B = C\)</td>
        <td>\(\text{CH}_3\text{Cl}, \text{CH}_3\text{C}\equiv\text{CH}, \text{NH}_3\)</td>
      </tr>
      <tr>
        <td>Oblate Symmetric Tops</td>
        <td>\(I_A = I_B < I_C\)</td>
        <td>\(A = B > C\)</td>
        <td>\(\text{BF}_3, \text{C}_6\text{H}_6, \text{CHCl}_3\)</td>
      </tr>
      <tr>
        <td>Asymmetric Tops</td>
        <td>\(I_A \neq I_B \neq I_C\)</td>
        <td>\(A > B > C\)</td>
        <td>\(\text{H}_2\text{O}, \text{SO}_2, \text{CH}_2=\text{CH}_2\)</td>
      </tr>
    </tbody>
  </table>
</div>
<h4 class="content-heading">Symmetric Top Quantum Term Formula</h4>
<p>For a prolate symmetric top, the projection of total angular momentum \(\vec{J}\) onto the principal molecular symmetry axis is quantized with quantum number \(K = -J, \dots, +J\):</p>
\[
F(J, K) = B J(J+1) + (A - B) K^2
\]
<p>The electric dipole selection rules for a prolate top with dipole along the symmetry axis are \(\Delta J = \pm 1, \Delta K = 0\). Consequently, the transition frequencies are \(\tilde{\nu} = 2B(J+1)\), identical to a linear rotor, meaning \(K\)-splittings are absent in rigid symmetric tops unless centrifugal distortion or the Stark effect is introduced.</p>"""
            },
            {
                "id": "u2-sec7",
                "number": "2.7",
                "title": "The Stark Effect & Electric Dipole Moment Determination",
                "content": r"""<p>When an external static electric field \(\vec{\mathcal{E}}\) is applied to a rotating polar molecule, the interaction between the field and the permanent dipole moment \(\vec{\mu}_0\) lifts the \((2J+1)\)-fold \(M_J\) degeneracy. This field-induced splitting is the <strong>Stark effect</strong>.</p>
<h4 class="content-heading">Linear Rotors: Second-Order Stark Shift</h4>
<p>For a linear rotor in state \(J\), the first-order Stark energy perturbation vanishes by parity: \(\langle J, M_J | \hat{\vec{\mu}} \cdot \vec{\mathcal{E}} | J, M_J \rangle = 0\). The energy shifts arise from second-order perturbation theory:</p>
\[
\Delta E_{\text{Stark}}^{(2)}(J, M_J) = \frac{\mu_0^2 \mathcal{E}^2}{2hcB} \left[ \frac{J(J+1) - 3 M_J^2}{J(J+1)(2J-1)(2J+3)} \right] \quad (J > 0)
\]
<p>For \(J = 0\), the second-order shift is \(\Delta E^{(2)}(0, 0) = -\frac{\mu_0^2 \mathcal{E}^2}{6 hc B}\). Notice that the shift depends on \(M_J^2\), splitting each \(J\) level into \(J+1\) distinct components (\(|M_J| = 0, 1, \dots, J\)).</p>
<h4 class="content-heading">Symmetric Tops: First-Order Stark Shift</h4>
<p>In symmetric tops with \(K \neq 0\), the molecule possesses an average projection of dipole moment along the space-fixed \(Z\)-axis, producing a dramatic <strong>first-order Stark effect</strong> linear in electric field:</p>
\[
\Delta E_{\text{Stark}}^{(1)}(J, K, M_J) = -\frac{\mu_0 \mathcal{E} K M_J}{J(J+1)}
\]
<p>Because the shift is proportional to \(\mu_0 \mathcal{E}\), measuring the frequency separation between Stark components as a function of calibrated field \(\mathcal{E}\) provides the most precise experimental method for determining permanent molecular electric dipole moments in the gas phase.</p>"""
            }
        ],
        "problems": [
            {
                "id": "u2-prob1",
                "number": 1,
                "title": "Calculation of Rotational Constant B and Bond Length for HCl",
                "difficulty": "Foundational",
                "statement": r"""The first rotational absorption line of \(^{1}\text{H}^{35}\text{Cl}\) is observed at \(\tilde{\nu} = 20.68\text{ cm}^{-1}\).
(a) Determine the rotational constant \(B\) of \(^{1}\text{H}^{35}\text{Cl}\).
(b) Calculate the moment of inertia \(I\) in \(\text{kg}\cdot\text{m}^2\).
(c) Given atomic masses \(m(^{1}\text{H}) = 1.007825\text{ u}\) and \(m(^{35}\text{Cl}) = 34.96885\text{ u}\), calculate the reduced mass \(\mu\) and determine the equilibrium bond length \(r_0\) in picometers (\(\text{pm}\)).""",
                "solution": r"""<p><strong>Step (a): Rotational constant B</strong></p>
<p>The \(J = 0 \to 1\) transition occurs at \(\tilde{\nu}_{0\to 1} = 2B\):</p>
\[
2B = 20.68\text{ cm}^{-1} \implies B = 10.34\text{ cm}^{-1}
\]
<p><strong>Step (b): Moment of inertia I</strong></p>
\[
B = \frac{h}{8\pi^2 c I} \implies I = \frac{h}{8\pi^2 c B}
\]
\[
I = \frac{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}}{8\pi^2 (2.99792 \times 10^{10}\text{ cm/s})(10.34\text{ cm}^{-1})} = \frac{6.62607 \times 10^{-34}}{2.4475 \times 10^{-7}} = 2.7073 \times 10^{-47}\text{ kg}\cdot\text{m}^2
\]
<p><strong>Step (c): Reduced mass and bond length</strong></p>
\[
\mu = \frac{m_H m_{Cl}}{m_H + m_{Cl}} = \frac{(1.007825)(34.96885)}{1.007825 + 34.96885}\text{ u} = \frac{35.2424}{35.9767}\text{ u} = 0.97959\text{ u}
\]
\[
\mu = (0.97959)(1.66054 \times 10^{-27}\text{ kg}) = 1.6266 \times 10^{-27}\text{ kg}
\]
<p>Now determine \(r_0\) from \(I = \mu r_0^2\):</p>
\[
r_0 = \sqrt{\frac{I}{\mu}} = \sqrt{\frac{2.7073 \times 10^{-47}\text{ kg}\cdot\text{m}^2}{1.6266 \times 10^{-27}\text{ kg}}} = \sqrt{1.6644 \times 10^{-20}\text{ m}^2} = 1.2901 \times 10^{-10}\text{ m} = 129.01\text{ pm}
\]"""
            },
            {
                "id": "u2-prob2",
                "number": 2,
                "title": "Isotopic Frequency Shift of Carbon Monoxide Isotopologues",
                "difficulty": "Intermediate",
                "statement": r"""The \(J = 0 \to 1\) rotational transition of \(^{12}\text{C}^{16}\text{O}\) occurs at frequency \(\nu = 115.2712\text{ GHz}\).
(a) Calculate the rotational constant \(B\) for \(^{12}\text{C}^{16}\text{O}\) in GHz and \(\text{cm}^{-1}\).
(b) Assuming the equilibrium bond length \(r_0\) is unchanged by isotopic substitution, predict the frequency of the \(J = 0 \to 1\) transition in \(^{13}\text{C}^{16}\text{O}\).
(Atomic masses: \(^{12}\text{C} = 12.00000\text{ u}\), \(^{13}\text{C} = 13.00335\text{ u}\), \(^{16}\text{O} = 15.99491\text{ u}\)).""",
                "solution": r"""<p><strong>Step (a): B for ¹²C¹⁶O</strong></p>
\[
\nu_{0\to 1} = 2B \implies B = \frac{115.2712\text{ GHz}}{2} = 57.6356\text{ GHz}
\]
<p>In wavenumbers:</p>
\[
B = \frac{57.6356 \times 10^9\text{ s}^{-1}}{2.99792458 \times 10^{10}\text{ cm/s}} = 1.92252\text{ cm}^{-1}
\]
<p><strong>Step (b): Frequency for ¹³C¹⁶O</strong></p>
<p>Calculate reduced masses:</p>
\[
\mu(^{12}\text{C}^{16}\text{O}) = \frac{12.00000 \times 15.99491}{12.00000 + 15.99491} = \frac{191.93892}{27.99491} = 6.85621\text{ u}
\]
\[
\mu(^{13}\text{C}^{16}\text{O}) = \frac{13.00335 \times 15.99491}{13.00335 + 15.99491} = \frac{207.98741}{28.99826} = 7.17241\text{ u}
\]
<p>Since \(I \propto \mu\) and \(B \propto 1/\mu\):</p>
\[
\frac{B'}{B} = \frac{\mu}{\mu'} = \frac{6.85621}{7.17241} = 0.955914
\]
\[
\nu'_{0\to 1} = 2B' = 2B \times \frac{\mu}{\mu'} = 115.2712\text{ GHz} \times 0.955914 = 110.1894\text{ GHz}
\]
<p>The isotopic shift is \(\Delta \nu = 115.2712 - 110.1894 = 5.0818\text{ GHz}\).</p>"""
            },
            {
                "id": "u2-prob3",
                "number": 3,
                "title": "Centrifugal Distortion and High-J Line Displacement in CO",
                "difficulty": "Intermediate",
                "statement": r"""For carbon monoxide \(^{12}\text{C}^{16}\text{O}\), the rotational constant is \(B = 1.92118\text{ cm}^{-1}\) and the fundamental vibrational wavenumber is \(\bar{\omega} = 2143.2\text{ cm}^{-1}\).
(a) Estimate the centrifugal distortion constant \(D\) using Kratzer's relation.
(b) Calculate the transition wavenumber for \(J = 9 \to 10\) with and without centrifugal distortion.
(c) Determine the fractional frequency error incurred if centrifugal distortion is neglected at \(J = 9\).""",
                "solution": r"""<p><strong>Step (a): Centrifugal distortion constant via Kratzer relation</strong></p>
\[
D = \frac{4 B^3}{\bar{\omega}^2} = \frac{4 (1.92118)^3}{(2143.2)^2} = \frac{4(7.09104)}{4593306.24} = 6.1747 \times 10^{-6}\text{ cm}^{-1}
\]
<p><strong>Step (b): Transition wavenumber for J = 9 -> 10</strong></p>
<p>Rigid rotor model (\(D = 0\)):</p>
\[
\tilde{\nu}_{\text{rigid}} = 2B(J+1) = 2(1.92118)(10) = 38.4236\text{ cm}^{-1}
\]
<p>Non-rigid rotor model:</p>
\[
\tilde{\nu}_{\text{non-rigid}} = 2B(J+1) - 4D(J+1)^3
\]
\[
4D(J+1)^3 = 4(6.1747 \times 10^{-6})(10^3) = 4(6.1747 \times 10^{-6})(1000) = 0.0247\text{ cm}^{-1}
\]
\[
\tilde{\nu}_{\text{non-rigid}} = 38.4236 - 0.0247 = 38.3989\text{ cm}^{-1}
\]
<p><strong>Step (c): Fractional error</strong></p>
\[
\text{Fractional error} = \frac{0.0247}{38.3989} \approx 6.43 \times 10^{-4} \approx 0.064\%
\]
<p>While small in percentage terms, a displacement of \(0.0247\text{ cm}^{-1}\) (\(740\text{ MHz}\)) is enormous compared to typical microwave spectrometer linewidths (\(< 0.1\text{ MHz}\)).</p>"""
            },
            {
                "id": "u2-prob4",
                "number": 4,
                "title": "Most Populated Rotational State and Spectral Intensity Envelope",
                "difficulty": "Foundational",
                "statement": r"""For the \(^{14}\text{N}_2\text{O}\) linear molecule, the rotational constant is \(B = 0.419\text{ cm}^{-1}\).
(a) Determine the most populated rotational energy level \(J_{\max}\) at \(T = 300\text{ K}\).
(b) Determine \(J_{\max}\) at low temperature \(T = 10\text{ K}\) (interstellar conditions).
(c) Calculate the ratio of the population of the \(J = 15\) state to the \(J = 0\) ground state at \(300\text{ K}\).""",
                "solution": r"""<p><strong>Step (a): J_max at 300 K</strong></p>
<p>The thermal energy factor in wavenumber units is:</p>
\[
\frac{k_B T}{h c} = \frac{(1.38065 \times 10^{-23})(300)}{(6.62607 \times 10^{-34})(2.99792 \times 10^{10})} = 208.51\text{ cm}^{-1}
\]
\[
J_{\max} = \sqrt{\frac{k_B T}{2 hc B}} - \frac{1}{2} = \sqrt{\frac{208.51}{2 \times 0.419}} - 0.5 = \sqrt{248.82} - 0.5 = 15.77 - 0.5 = 15.27
\]
<p>Thus, the state with the maximum population is \(J = 15\).</p>
<p><strong>Step (b): J_max at 10 K</strong></p>
\[
\frac{k_B T}{hc} = \frac{208.51}{30} = 6.95\text{ cm}^{-1}
\]
\[
J_{\max} = \sqrt{\frac{6.95}{2 \times 0.419}} - 0.5 = \sqrt{8.294} - 0.5 = 2.88 - 0.5 = 2.38 \implies J_{\max} = 2
\]
<p><strong>Step (c): Population ratio N(15) / N(0) at 300 K</strong></p>
\[
E_J = hcB J(J+1) \implies \frac{E_J}{k_B T} = \frac{B J(J+1)}{k_B T / hc} = \frac{0.419 \times 15 \times 16}{208.51} = \frac{100.56}{208.51} = 0.4823
\]
\[
\frac{N_{15}}{N_0} = \frac{g_{15}}{g_0} e^{-0.4823} = \frac{2(15) + 1}{1} e^{-0.4823} = 31 \times 0.6174 = 19.14
\]
<p>The \(J = 15\) level is more than 19 times as populated as the \(J = 0\) ground state!</p>"""
            },
            {
                "id": "u2-prob5",
                "number": 5,
                "title": "Prolate Symmetric Top Energy Levels of Methyl Chloride",
                "difficulty": "Intermediate",
                "statement": r"""For methyl chloride (\(\text{CH}_3^{35}\text{Cl}\)), a prolate symmetric top, the rotational constants are \(A = 5.097\text{ cm}^{-1}\) and \(B = 0.4434\text{ cm}^{-1}\).
(a) Write the rotational term value formula \(F(J, K)\).
(b) Calculate the energy (in \(\text{cm}^{-1}\)) of the following rotational states: \((J=1, K=0)\), \((J=1, K=1)\), \((J=2, K=1)\), and \((J=2, K=2)\).
(c) State the allowed electric dipole transitions for microwave absorption and calculate their transition wavenumbers.""",
                "solution": r"""<p><strong>Step (a): Prolate symmetric top term formula</strong></p>
\[
F(J, K) = B J(J+1) + (A - B) K^2
\]
<p>Here \(A - B = 5.097 - 0.4434 = 4.6536\text{ cm}^{-1}\).</p>
<p><strong>Step (b): State energy calculations</strong></p>
<ul>
  <li>\((J=1, K=0)\): \(F(1, 0) = 0.4434(1)(2) + 4.6536(0)^2 = 0.8868\text{ cm}^{-1}\)</li>
  <li>\((J=1, K=1)\): \(F(1, 1) = 0.4434(1)(2) + 4.6536(1)^2 = 0.8868 + 4.6536 = 5.5404\text{ cm}^{-1}\)</li>
  <li>\((J=2, K=1)\): \(F(2, 1) = 0.4434(2)(3) + 4.6536(1)^2 = 2.6604 + 4.6536 = 7.3140\text{ cm}^{-1}\)</li>
  <li>\((J=2, K=2)\): \(F(2, 2) = 0.4434(2)(3) + 4.6536(2)^2 = 2.6604 + 18.6144 = 21.2748\text{ cm}^{-1}\)</li>
</ul>
<p><strong>Step (c): Microwave absorption transitions</strong></p>
<p>The selection rules for a rigid symmetric top with dipole along the symmetry axis are \(\Delta J = +1, \Delta K = 0\):</p>
\[
\tilde{\nu} = F(J+1, K) - F(J, K) = 2B(J+1)
\]
<p>For \(J = 1 \to 2\):</p>
\[
\tilde{\nu}_{1\to 2} = 2(0.4434)(2) = 1.7736\text{ cm}^{-1}
\]
<p>Notice that the \(K^2\) terms identically cancel: the \(J=1 \to 2\) transition frequency is exactly \(1.7736\text{ cm}^{-1}\) for both \(K=0\) and \(K=1\).</p>"""
            },
            {
                "id": "u2-prob6",
                "number": 6,
                "title": "Stark Effect Splitting and Electric Dipole Moment of OCS",
                "difficulty": "Advanced",
                "statement": r"""In a Stark-modulated microwave spectrometer, carbonyl sulfide (\(^{16}\text{O}^{12}\text{C}^{32}\text{S}\)) has rotational constant \(B = 6081.49\text{ MHz}\).
A static electric field \(\mathcal{E} = 1500\text{ V/cm}\) is applied.
(a) Calculate the second-order Stark shift \(\Delta \nu\) for the \(J = 0 \to 1, M_J = 0 \to 0\) transition.
(b) If the measured frequency shift is \(\Delta \nu = -0.320\text{ MHz}\), calculate the permanent electric dipole moment \(\mu_0\) of \(\text{OCS}\) in Debye.""",
                "solution": r"""<p><strong>Step (a): Formula for Stark shift of J = 0 -> 1 line</strong></p>
<p>The second-order Stark energies are:</p>
\[
E^{(2)}(J=0, M=0) = -\frac{\mu_0^2 \mathcal{E}^2}{6 h B}
\]
\[
E^{(2)}(J=1, M=0) = \frac{\mu_0^2 \mathcal{E}^2}{2 h B} \left[ \frac{(1)(2) - 0}{(1)(2)(1)(5)} \right] = \frac{\mu_0^2 \mathcal{E}^2}{2 h B} \left(\frac{2}{10}\right) = \frac{\mu_0^2 \mathcal{E}^2}{10 h B}
\]
<p>The frequency shift of the \(J=0 \to 1, M=0 \to 0\) transition is:</p>
\[
h \Delta \nu = E^{(2)}(1, 0) - E^{(2)}(0, 0) = \frac{\mu_0^2 \mathcal{E}^2}{h B} \left( \frac{1}{10} - \left(-\frac{1}{6}\right) \right) = \frac{\mu_0^2 \mathcal{E}^2}{h B} \left(\frac{3 + 5}{30}\right) = \frac{4 \mu_0^2 \mathcal{E}^2}{15 h B}
\]
\[
\Delta \nu = \frac{4 \mu_0^2 \mathcal{E}^2}{15 h^2 B}
\]
<p><strong>Step (b): Dipole moment calculation</strong></p>
<p>Convert \(\mathcal{E}\) to SI units: \(\mathcal{E} = 1500\text{ V/cm} = 1.50 \times 10^5\text{ V/m}\).</p>
\[
\mu_0^2 = \frac{15 h^2 B |\Delta \nu|}{4 \mathcal{E}^2}
\]
<p>With \(h = 6.62607 \times 10^{-34}\text{ J}\cdot\text{s}\), \(B = 6.08149 \times 10^9\text{ Hz}\), \(|\Delta \nu| = 3.20 \times 10^5\text{ Hz}\):</p>
\[
\mu_0^2 = \frac{15 (6.62607 \times 10^{-34})^2 (6.08149 \times 10^9)(3.20 \times 10^5)}{4 (1.50 \times 10^5)^2}
\]
\[
\mu_0^2 = \frac{15 (4.39048 \times 10^{-67}) (1.94608 \times 10^{15})}{9.00 \times 10^{10}} = \frac{1.28169 \times 10^{-50}}{9.00 \times 10^{10}} = 1.4241 \times 10^{-61}\text{ C}^2\cdot\text{m}^2
\]
\[
\mu_0 = \sqrt{1.4241 \times 10^{-61}} = 2.3867 \times 10^{-30}\text{ C}\cdot\text{m}
\]
<p>Convert to Debye (\(1\text{ D} = 3.33564 \times 10^{-30}\text{ C}\cdot\text{m}\)):</p>
\[
\mu_0 = \frac{2.3867 \times 10^{-30}}{3.33564 \times 10^{-30}} = 0.7155\text{ Debye}
\]
<p>The experimental dipole moment of OCS is \(0.715\text{ D}\).</p>"""
            },
            {
                "id": "u2-prob7",
                "number": 7,
                "title": "Dielectric Heating Mechanism in Microwave Cavities",
                "difficulty": "Advanced",
                "statement": r"""A domestic microwave oven operates at frequency \(f = 2.45\text{ GHz}\) with microwave power \(P = 900\text{ W}\).
At this frequency, liquid water at \(25^\circ\text{C}\) has relative dielectric permittivity \(\varepsilon' = 78.0\) and dielectric loss factor \(\varepsilon'' = 12.0\).
(a) Calculate the loss tangent \(\tan\delta = \varepsilon'' / \varepsilon'\) of water.
(b) The volumetric heating rate is given by \(Q_v = 2\pi f \varepsilon_0 \varepsilon'' |\vec{\mathcal{E}}|^2\). If an electric field amplitude of \(|\vec{\mathcal{E}}| = 4.0\text{ kV/m}\) penetrates the food matrix, calculate \(Q_v\) in \(\text{kW/m}^3\).
(c) Assuming no heat loss, calculate the initial temperature rise rate \(dT/dt\) for \(100\text{ g}\) of liquid water (\(c_p = 4184\text{ J}/(\text{kg}\cdot\text{K})\), \(\rho = 1000\text{ kg/m}^3\)).""",
                "solution": r"""<p><strong>Step (a): Loss tangent calculation</strong></p>
\[
\tan\delta = \frac{\varepsilon''}{\varepsilon'} = \frac{12.0}{78.0} = 0.1538
\]
<p><strong>Step (b): Volumetric power dissipation</strong></p>
\[
Q_v = 2\pi f \varepsilon_0 \varepsilon'' |\vec{\mathcal{E}}|^2
\]
<p>Parameters in SI units:</p>
<ul>
  <li>\(f = 2.45 \times 10^9\text{ Hz}\)</li>
  <li>\(\varepsilon_0 = 8.85419 \times 10^{-12}\text{ F/m}\)</li>
  <li>\(\varepsilon'' = 12.0\)</li>
  <li>\(|\vec{\mathcal{E}}| = 4000\text{ V/m} \implies |\vec{\mathcal{E}}|^2 = 1.60 \times 10^7\text{ V}^2/\text{m}^2\)</li>
</ul>
\[
Q_v = 2\pi (2.45 \times 10^9)(8.85419 \times 10^{-12})(12.0)(1.60 \times 10^7)
\]
\[
Q_v = (15.3938)(8.85419 \times 10^{-3})(1.92 \times 10^8) = 2.617 \times 10^7\text{ W/m}^3 = 26170\text{ kW/m}^3
\]
<p><strong>Step (c): Initial rate of temperature increase</strong></p>
<p>The volumetric thermal capacity is \(C_v = \rho c_p = (1000\text{ kg/m}^3)(4184\text{ J/kg}\cdot\text{K}) = 4.184 \times 10^6\text{ J}/(\text{m}^3\cdot\text{K})\).</p>
\[
\frac{dT}{dt} = \frac{Q_v}{\rho c_p} = \frac{2.617 \times 10^7\text{ W/m}^3}{4.184 \times 10^6\text{ J}/(\text{m}^3\cdot\text{K})} = 6.255\text{ K/s} \approx 6.26^\circ\text{C/s}
\]
<p>This demonstrates the exceptional efficiency of dipolar dielectric relaxation heating at 2.45 GHz compared to conventional thermal conduction.</p>"""
            }
        ]
    }
    units.append(u2)

    # =========================================================================
    # UNIT 3: Infrared & Vibrational Spectroscopy of Diatomic & Polyatomic Molecules
    # =========================================================================
    u3 = {
        "id": "unit3",
        "number": 3,
        "title": "Unit 3: Infrared & Vibrational Spectroscopy of Diatomic & Polyatomic Molecules",
        "description": "Harmonic oscillator model, Morse potential and anharmonicity, vibrational term values, Birge-Sponer extrapolation to bond dissociation, diatomic vibrating rotators, rovibrational P and R branches, vibration-rotation interaction constant alpha_e, high-resolution CO spectrum, Fermi resonance, and polyatomic normal modes.",
        "simulations": [
            {
                "id": "sim_spec_rovibrational_co_spectrum",
                "title": "CO Rovibrational Spectrum (P & R Branches)",
                "description": "Interactive 60 FPS simulator modeling the high-resolution rovibrational infrared absorption spectrum of carbon monoxide (12C16O). Adjust temperature T, vibration-rotation coupling constant alpha_e, and band origin to observe line spacing narrowing in the R-branch and spreading in the P-branch, with explicit visualization of the forbidden Q-branch."
            }
        ],
        "sections": [
            {
                "id": "u3-sec1",
                "number": "3.1",
                "title": "The Quantum Harmonic Oscillator & Force Constants",
                "content": r"""<p>For small displacements \(q = r - r_e\) around equilibrium bond length \(r_e\), the molecular potential energy can be expanded in a Taylor series: \(V(q) = V(0) + \left(\frac{dV}{dq}\right)_0 q + \frac{1}{2}\left(\frac{d^2V}{dq^2}\right)_0 q^2 + \dots\). Taking \(V(0) = 0\) and noting that \((dV/dq)_0 = 0\) at equilibrium, the harmonic approximation retains only the quadratic term: \(V(q) = \frac{1}{2} k q^2\), where \(k = \left(\frac{d^2V}{dq^2}\right)_0\) is the <strong>bond force constant</strong>.</p>
<p>The time-independent Schrödinger equation for the harmonic oscillator is:</p>
\[
-\frac{\hbar^2}{2\mu}\frac{d^2\psi_v}{dq^2} + \frac{1}{2} k q^2 \psi_v = E_v \psi_v
\]
<p>The normalized eigenfunctions are expressed in terms of Hermite polynomials \(H_v(\xi)\):</p>
\[
\psi_v(q) = \left(\frac{\alpha}{\pi}\right)^{1/4} \frac{1}{\sqrt{2^v v!}} H_v(\sqrt{\alpha} q) e^{-\alpha q^2 / 2}, \quad \alpha = \frac{\sqrt{\mu k}}{\hbar} = \frac{\mu \omega}{\hbar}
\]
<p>The quantized energy eigenvalues are:</p>
\[
E_v = \hbar \omega \left(v + \frac{1}{2}\right) = h c \bar{\omega}_e \left(v + \frac{1}{2}\right), \quad v = 0, 1, 2, \dots
\]
<p>where the harmonic vibrational wavenumber is \(\bar{\omega}_e = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}\). Even at absolute zero (\(T = 0\text{ K}\)), the molecule possesses <strong>zero-point energy (ZPE)</strong>: \(E_0 = \frac{1}{2}\hbar\omega = \frac{1}{2}hc\bar{\omega}_e\), a direct consequence of the Heisenberg uncertainty principle.</p>"""
            },
            {
                "id": "u3-sec2",
                "number": "3.2",
                "title": "Vibrational Selection Rules & Dipole Derivatives",
                "content": r"""<p>The transition dipole moment integral between vibrational states \(|v\rangle\) and \(|v'\rangle\) is \(\mu_{v'v} = \langle \psi_{v'} | \hat{\mu}(q) | \psi_v \rangle\). Expanding the molecular dipole moment as a Taylor series about equilibrium:</p>
\[
\hat{\mu}(q) = \mu_0 + \left(\frac{d\mu}{dq}\right)_0 q + \frac{1}{2}\left(\frac{d^2\mu}{dq^2}\right)_0 q^2 + \dots
\]
<p>Substituting this into the transition moment:</p>
\[
\mu_{v'v} = \mu_0 \langle \psi_{v'} | \psi_v \rangle + \left(\frac{d\mu}{dq}\right)_0 \langle \psi_{v'} | q | \psi_v \rangle + \dots
\]
<p>By orthogonality of Hermite functions, \(\langle \psi_{v'} | \psi_v \rangle = 0\) for \(v' \neq v\). Therefore:</p>
<ol>
  <li><strong>Gross Selection Rule:</strong> The dipole moment must vary with bond displacement: \(\left(\frac{d\mu}{dq}\right)_0 \neq 0\). Homonuclear diatomics have zero dipole derivative at all distances and are strictly infrared inactive. Heteronuclear diatomics (\(\text{HCl}, \text{CO}, \text{NO}\)) have non-zero dipole derivatives and are infrared active.</li>
  <li><strong>Specific Selection Rule:</strong> Using the Hermite polynomial recurrence relation \(q |v\rangle = \sqrt{\frac{\hbar}{2\mu\omega}} (\sqrt{v+1}|v+1\rangle + \sqrt{v}|v-1\rangle)\), the transition moment is non-zero only when:
  \[
  \Delta v = v' - v = \pm 1
  \]
  </li>
</ol>
<p>In the harmonic approximation, all transitions occur at the exact same wavenumber \(\tilde{\nu} = \bar{\omega}_e\).</p>"""
            },
            {
                "id": "u3-sec3",
                "number": "3.3",
                "title": "Anharmonicity, Morse Potential & Overtones",
                "content": r"""<p>Real chemical bonds deviate significantly from harmonic behavior at larger displacements: the potential energy steepens at short distances due to core electron repulsion and flattens asymptotically to the bond dissociation limit at large internuclear separations. The <strong>Morse potential</strong> accurately models this physical behavior:</p>
\[
V(r) = D_e \left[ 1 - e^{-a(r - r_e)} \right]^2
\]
<p>where \(D_e\) is the spectroscopic dissociation energy relative to the potential minimum, and \(a = \sqrt{\frac{k_e}{2 D_e}}\) governs the curvature of the well.</p>
<h4 class="content-heading">Anharmonic Vibrational Term Values</h4>
<p>Solving the Schrödinger equation with the Morse potential yields the vibrational term values:</p>
\[
G(v) = \bar{\omega}_e \left(v + \frac{1}{2}\right) - \bar{\omega}_e x_e \left(v + \frac{1}{2}\right)^2 + \bar{\omega}_e y_e \left(v + \frac{1}{2}\right)^3 + \dots
\]
<p>where \(x_e = \frac{h c \bar{\omega}_e}{4 D_e}\) is the dimensionless <strong>anharmonicity constant</strong>. Anharmonicity has profound physical consequences:</p>
<ul>
  <li>Energy level spacing contracts with increasing \(v\): \(\Delta G_{v+1/2} = G(v+1) - G(v) = \bar{\omega}_e - 2\bar{\omega}_e x_e(v + 1)\).</li>
  <li>The harmonic selection rule \(\Delta v = \pm 1\) breaks down: weak <strong>overtone transitions</strong> become allowed:
    <ul>
      <li>Fundamental (\(v = 0 \to 1\)): \(\tilde{\nu}_1 = G(1) - G(0) = \bar{\omega}_e(1 - 2x_e)\)</li>
      <li>First Overtone (\(v = 0 \to 2\)): \(\tilde{\nu}_2 = G(2) - G(0) = 2\bar{\omega}_e(1 - 3x_e)\)</li>
      <li>Second Overtone (\(v = 0 \to 3\)): \(\tilde{\nu}_3 = G(3) - G(0) = 3\bar{\omega}_e(1 - 4x_e)\)</li>
    </ul>
  </li>
  <li><strong>Hot bands</strong> (\(v = 1 \to 2\)) appear at elevated temperatures at slightly lower frequencies: \(\tilde{\nu}_{\text{hot}} = \bar{\omega}_e(1 - 4x_e)\).</li>
</ul>"""
            },
            {
                "id": "u3-sec4",
                "number": "3.4",
                "title": "Birge-Sponer Extrapolation & Dissociation Limits",
                "content": r"""<p>The Birge-Sponer extrapolation provides an elegant experimental methodology for determining the bond dissociation energy \(D_e\) directly from observed vibrational line spacings.</p>
<h4 class="content-heading">Linear Birge-Sponer Formulation</h4>
<p>The separation between consecutive vibrational levels is:</p>
\[
\Delta G_{v+1/2} = G(v+1) - G(v) = \bar{\omega}_e - 2\bar{\omega}_e x_e (v + 1)
\]
<p>Plotting \(\Delta G_{v+1/2}\) linearly against \((v+1)\) produces a straight line with intercept \(\bar{\omega}_e\) and negative slope \(-2\bar{\omega}_e x_e\). The dissociation limit occurs at maximum quantum number \(v_{\max}\) where the energy difference reaches zero: \(\Delta G_{v_{\max}+1/2} = 0\):</p>
\[
v_{\max} + 1 = \frac{\bar{\omega}_e}{2\bar{\omega}_e x_e} = \frac{1}{2x_e}
\]
<p>The total dissociation energy \(D_e\) is the area under the Birge-Sponer curve:</p>
\[
D_e = \sum_{v=0}^{v_{\max}} \Delta G_{v+1/2} \approx \int_0^{v_{\max}+1} [\bar{\omega}_e - 2\bar{\omega}_e x_e (v+1)] d(v+1) = \frac{\bar{\omega}_e^2}{4\bar{\omega}_e x_e}
\]
<p>The ground state chemical dissociation energy \(D_0\) accounts for zero-point energy:</p>
\[
D_0 = D_e - G(0) = D_e - \left(\frac{1}{2}\bar{\omega}_e - \frac{1}{4}\bar{\omega}_e x_e\right)
\]"""
            },
            {
                "id": "u3-sec5",
                "number": "3.5",
                "title": "The Diatomic Vibrating Rotator & Rovibrational Transitions",
                "content": r"""<p>In the gas phase, molecules undergo simultaneous vibration and rotation. In the Born-Oppenheimer approximation, the total rovibrational term value is the sum of vibrational and rotational energies:</p>
\[
T(v, J) = G(v) + F(J) = \left[\bar{\omega}_e\left(v + \frac{1}{2}\right) - \bar{\omega}_e x_e\left(v + \frac{1}{2}\right)^2\right] + B_v J(J+1)
\]
<p>For a heteronuclear diatomic molecule in a \(^1\Sigma\) electronic ground state (zero electronic orbital angular momentum), the selection rules are:</p>
\[
\Delta v = \pm 1, \quad \Delta J = \pm 1 \quad (\Delta J = 0 \text{ is forbidden!})
\]
<h4 class="content-heading">R-Branch and P-Branch Manifolds</h4>
<p>Consider the fundamental absorption transition from \(v = 0\) to \(v = 1\), with band origin \(\tilde{\nu}_0 = G(1) - G(0)\):</p>
<ol>
  <li><strong>R-Branch (\(\Delta J = +1\), \(J' = J'' + 1\)):</strong>
  \[
  \tilde{\nu}_R(J'') = \tilde{\nu}_0 + F_1(J''+1) - F_0(J'') = \tilde{\nu}_0 + 2B_1 + (3B_1 - B_0)J'' + (B_1 - B_0)J''^2
  \]
  If \(B_1 \approx B_0 = B\), this simplifies to: \(\tilde{\nu}_R(J'') = \tilde{\nu}_0 + 2B(J''+1)\) for \(J'' = 0, 1, 2, \dots\). Lines appear at \(\tilde{\nu}_0 + 2B, \tilde{\nu}_0 + 4B, \tilde{\nu}_0 + 6B, \dots\).</li>
  <li><strong>P-Branch (\(\Delta J = -1\), \(J' = J'' - 1\)):</strong>
  \[
  \tilde{\nu}_P(J'') = \tilde{\nu}_0 + F_1(J''-1) - F_0(J'') = \tilde{\nu}_0 - (B_1 + B_0)J'' + (B_1 - B_0)J''^2
  \]
  If \(B_1 \approx B_0 = B\), this simplifies to: \(\tilde{\nu}_P(J'') = \tilde{\nu}_0 - 2B J''\) for \(J'' = 1, 2, 3, \dots\). Lines appear at \(\tilde{\nu}_0 - 2B, \tilde{\nu}_0 - 4B, \tilde{\nu}_0 - 6B, \dots\).</li>
</ol>
<p>Because \(\Delta J = 0\) is forbidden, no absorption line appears at the exact band origin \(\tilde{\nu}_0\). The separation between the first R-line (\(R(0) = \tilde{\nu}_0 + 2B\)) and the first P-line (\(P(1) = \tilde{\nu}_0 - 2B\)) is \(4B\), leaving a prominent <strong>zero-gap</strong> in the center of the band.</p>"""
            },
            {
                "id": "u3-sec6",
                "number": "3.6",
                "title": "Vibration-Rotation Interaction Constant α_e & Band Heads",
                "content": r"""<p>In real molecules, the average bond length in the excited vibrational state \(v=1\) is slightly larger than in the ground state \(v=0\) due to anharmonicity of the Morse potential: \(\langle r \rangle_{v=1} > \langle r \rangle_{v=0}\). Consequently, the moment of inertia increases and the rotational constant decreases in the upper vibrational state:</p>
\[
B_v = B_e - \alpha_e \left(v + \frac{1}{2}\right)
\]
<p>where \(B_e\) is the equilibrium rotational constant and \(\alpha_e\) is the <strong>vibration-rotation coupling constant</strong> (\(\alpha_e > 0\)). Therefore, \(B_1 < B_0\), and \(B_1 - B_0 = -\alpha_e\).</p>
<h4 class="content-heading">Line Spacing Asymmetry & Band Head Formation</h4>
<p>Incorporating \(\alpha_e\), the rovibrational transition frequencies become:</p>
\[
\tilde{\nu}_R(J) = \tilde{\nu}_0 + (2B_e - 3\alpha_e) + (2B_e - 4\alpha_e)J - \alpha_e J^2
\]
\[
\tilde{\nu}_P(J) = \tilde{\nu}_0 - (2B_e - 2\alpha_e)J - \alpha_e J^2
\]
<p>Notice the quadratic term \(-\alpha_e J^2\):</p>
<ul>
  <li>In the <strong>R-branch</strong>, the quadratic term opposes the linear term. As \(J\) increases, the spacing between consecutive R-lines progressively contracts, eventually converging to a reversal point known as a <strong>band head</strong> where \(\frac{d\tilde{\nu}_R}{dJ} = 0\).</li>
  <li>In the <strong>P-branch</strong>, the quadratic term adds to the linear term in the negative direction, causing the spacing between consecutive P-lines to steadily widen with increasing \(J\).</li>
</ul>"""
            },
            {
                "id": "u3-sec7",
                "number": "3.7",
                "title": "Carbon Monoxide (CO) Rovibrational Spectrum & Combination Differences",
                "content": r"""<p>The fundamental infrared absorption band of carbon monoxide (\(^{12}\text{C}^{16}\text{O}\)) centered at \(\tilde{\nu}_0 = 2143.27\text{ cm}^{-1}\) serves as the quintessential benchmark for high-resolution rovibrational spectroscopy.</p>
<h4 class="content-heading">Method of Combination Differences</h4>
<p>To extract \(B_0\) and \(B_1\) independently without relying on assumptions about the band origin \(\tilde{\nu}_0\), spectroscopists use <strong>combination differences</strong>:</p>
<ol>
  <li><strong>Common Lower State Combination Differences (\(\Delta_2 F''(J)\)):</strong>
  Consider transitions starting from the same lower state \(J''\) and terminating at \(J'+1\) (via R-branch) and \(J'-1\) (via P-branch):
  \[
  \Delta_2 F'(J) = R(J) - P(J) = F_1(J+1) - F_1(J-1) = 4B_1\left(J + \frac{1}{2}\right)
  \]
  Plotting \(R(J) - P(J)\) against \((J + 1/2)\) gives a straight line with slope \(4B_1\).</li>
  <li><strong>Common Upper State Combination Differences (\(\Delta_2 F''(J)\)):</strong>
  Consider transitions terminating on the same upper state \(J'\) originating from \(J''-1\) and \(J''+1\):
  \[
  \Delta_2 F''(J) = R(J-1) - P(J+1) = F_0(J+1) - F_0(J-1) = 4B_0\left(J + \frac{1}{2}\right)
  \]
  Plotting \(R(J-1) - P(J+1)\) against \((J + 1/2)\) gives a straight line with slope \(4B_0\).</li>
</ol>
<p>For \(^{12}\text{C}^{16}\text{O}\), this analysis yields \(B_0 = 1.9225\text{ cm}^{-1}\), \(B_1 = 1.9050\text{ cm}^{-1}\), \(\alpha_e = 0.0175\text{ cm}^{-1}\), and equilibrium bond length \(r_e = 112.83\text{ pm}\).</p>"""
            }
        ],
        "problems": [
            {
                "id": "u3-prob1",
                "number": 1,
                "title": "Force Constant and Zero-Point Energy of Carbon Monoxide",
                "difficulty": "Foundational",
                "statement": r"""The fundamental vibrational wavenumber of \(^{12}\text{C}^{16}\text{O}\) is \(\bar{\omega}_e = 2169.8\text{ cm}^{-1}\).
(a) Calculate the bond force constant \(k\) in \(\text{N/m}\).
(b) Determine the zero-point vibrational energy (ZPE) in \(\text{kJ/mol}\) and in \(\text{eV}\).
(c) Predict the harmonic vibrational wavenumber for \(^{13}\text{C}^{16}\text{O}\) assuming the force constant is unaffected by isotopic substitution.""",
                "solution": r"""<p><strong>Step (a): Force constant calculation</strong></p>
<p>The reduced mass of \(^{12}\text{C}^{16}\text{O}\) is \(\mu = 6.85621\text{ u} = 1.13850 \times 10^{-26}\text{ kg}\).</p>
\[
\bar{\omega}_e = \frac{1}{2\pi c} \sqrt{\frac{k}{\mu}} \implies k = 4\pi^2 c^2 \bar{\omega}_e^2 \mu
\]
\[
k = 4\pi^2 (2.99792 \times 10^{10}\text{ cm/s})^2 (2169.8\text{ cm}^{-1})^2 (1.13850 \times 10^{-26}\text{ kg})
\]
\[
k = 4\pi^2 (8.98755 \times 10^{20})(4.70803 \times 10^6)(1.13850 \times 10^{-26}) = 1901.9\text{ N/m}
\]
<p>This exceptionally large force constant (\(\sim 1902\text{ N/m}\)) reflects the formidable triple bond in carbon monoxide.</p>
<p><strong>Step (b): Zero-point energy</strong></p>
\[
E_0 = \frac{1}{2} hc \bar{\omega}_e = \frac{1}{2}(6.62607 \times 10^{-34})(2.99792 \times 10^{10})(2169.8) = 2.155 \times 10^{-20}\text{ J}
\]
<p>Per mole:</p>
\[
E_{0, \text{molar}} = N_A E_0 = (6.02214 \times 10^{23})(2.155 \times 10^{-20}\text{ J}) = 12.978\text{ kJ/mol}
\]
<p>In electron-volts:</p>
\[
E_0 = \frac{2.155 \times 10^{-20}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} = 0.1345\text{ eV}
\]
<p><strong>Step (c): Vibrational wavenumber for ¹³C¹⁶O</strong></p>
<p>The reduced mass of \(^{13}\text{C}^{16}\text{O}\) is \(\mu' = 7.17241\text{ u}\).</p>
\[
\bar{\omega}_e' = \bar{\omega}_e \sqrt{\frac{\mu}{\mu'}} = 2169.8 \sqrt{\frac{6.85621}{7.17241}} = 2169.8 \times 0.977708 = 2121.4\text{ cm}^{-1}
\]"""
            },
            {
                "id": "u3-prob2",
                "number": 2,
                "title": "Anharmonicity Constants and Morse Dissociation Energy of HCl",
                "difficulty": "Intermediate",
                "statement": r"""For \(^{1}\text{H}^{35}\text{Cl}\), the fundamental absorption band appears at \(\tilde{\nu}_1 = 2885.9\text{ cm}^{-1}\) and the first overtone band appears at \(\tilde{\nu}_2 = 5668.0\text{ cm}^{-1}\).
(a) Determine the harmonic wavenumber \(\bar{\omega}_e\) and the anharmonicity constant \(x_e\).
(b) Calculate the predicted wavenumber of the second overtone (\(v = 0 \to 3\)).
(c) Estimate the spectroscopic dissociation energy \(D_e\) and ground state chemical dissociation energy \(D_0\) in \(\text{kJ/mol}\).""",
                "solution": r"""<p><strong>Step (a): Calculation of \(\bar{\omega}_e\) and \(x_e\)</strong></p>
<p>The transition wavenumbers are related to term values by:</p>
\[
\tilde{\nu}_1 = G(1) - G(0) = \bar{\omega}_e(1 - 2x_e) = 2885.9\text{ cm}^{-1}
\]
\[
\tilde{\nu}_2 = G(2) - G(0) = 2\bar{\omega}_e(1 - 3x_e) = 5668.0\text{ cm}^{-1}
\]
<p>Dividing the second equation by 2:</p>
\[
\bar{\omega}_e(1 - 3x_e) = 2834.0\text{ cm}^{-1}
\]
<p>Subtracting this from the fundamental:</p>
\[
\bar{\omega}_e(1 - 2x_e) - \bar{\omega}_e(1 - 3x_e) = \bar{\omega}_e x_e = 2885.9 - 2834.0 = 51.9\text{ cm}^{-1}
\]
<p>Now substitute \(\bar{\omega}_e x_e\) back into \(\bar{\omega}_e(1 - 2x_e) = \bar{\omega}_e - 2\bar{\omega}_e x_e\):</p>
\[
\bar{\omega}_e = 2885.9 + 2(51.9) = 2885.9 + 103.8 = 2989.7\text{ cm}^{-1}
\]
\[
x_e = \frac{\bar{\omega}_e x_e}{\bar{\omega}_e} = \frac{51.9}{2989.7} = 0.01736
\]
<p><strong>Step (b): Second overtone wavenumber (\(v = 0 \to 3\))</strong></p>
\[
\tilde{\nu}_3 = G(3) - G(0) = 3\bar{\omega}_e(1 - 4x_e) = 3(2989.7)(1 - 4 \times 0.01736) = 8969.1(1 - 0.06944) = 8346.3\text{ cm}^{-1}
\]
<p><strong>Step (c): Dissociation energies \(D_e\) and \(D_0\)</strong></p>
\[
D_e = \frac{\bar{\omega}_e^2}{4\bar{\omega}_e x_e} = \frac{(2989.7)^2}{4(51.9)} = \frac{8938306}{207.6} = 43055\text{ cm}^{-1}
\]
<p>Converting to \(\text{kJ/mol}\) (\(1\text{ cm}^{-1} = 0.0119627\text{ kJ/mol}\)):</p>
\[
D_e = 43055 \times 0.0119627 = 515.1\text{ kJ/mol}
\]
\[
D_0 = D_e - G(0) = D_e - \left(\frac{1}{2}\bar{\omega}_e - \frac{1}{4}\bar{\omega}_e x_e\right) = 43055 - (1494.85 - 12.98) = 43055 - 1481.87 = 41573\text{ cm}^{-1}
\]
\[
D_0 = 41573 \times 0.0119627 = 497.3\text{ kJ/mol}
\]"""
            },
            {
                "id": "u3-prob3",
                "number": 3,
                "title": "Birge-Sponer Linear Extrapolation for Iodine Molecule",
                "difficulty": "Intermediate",
                "statement": r"""Vibrational level separations \(\Delta G_{v+1/2}\) for the ground electronic state of \(^{127}\text{I}_2\) yield a linear Birge-Sponer regression:
\[
\Delta G_{v+1/2} = 214.50 - 1.22(v+1)\ \text{cm}^{-1}
\]
(a) Identify \(\bar{\omega}_e\) and \(\bar{\omega}_e x_e\).
(b) Calculate the maximum bound vibrational quantum number \(v_{\max}\).
(c) Calculate the total dissociation energy \(D_e\) in \(\text{cm}^{-1}\) and \(\text{kJ/mol}\).""",
                "solution": r"""<p><strong>Step (a): Identify parameters</strong></p>
<p>Comparing with \(\Delta G_{v+1/2} = \bar{\omega}_e - 2\bar{\omega}_e x_e(v+1)\):</p>
\[
\bar{\omega}_e = 214.50\text{ cm}^{-1}
\]
\[
2\bar{\omega}_e x_e = 1.22\text{ cm}^{-1} \implies \bar{\omega}_e x_e = 0.61\text{ cm}^{-1} \implies x_e = \frac{0.61}{214.50} = 0.00284
\]
<p><strong>Step (b): Maximum bound vibrational state</strong></p>
\[
\Delta G_{v_{\max}+1/2} = 0 \implies 214.50 - 1.22(v_{\max} + 1) = 0 \implies v_{\max} + 1 = \frac{214.50}{1.22} = 175.8
\]
\[
v_{\max} = 174\text{ bound states}
\]
<p><strong>Step (c): Total dissociation energy De</strong></p>
\[
D_e = \frac{\bar{\omega}_e^2}{4\bar{\omega}_e x_e} = \frac{(214.50)^2}{2(1.22)} = \frac{46010.25}{2.44} = 18856.7\text{ cm}^{-1}
\]
<p>Converting to \(\text{kJ/mol}\):</p>
\[
D_e = 18856.7\text{ cm}^{-1} \times 0.0119627\text{ kJ/mol per cm}^{-1} = 225.58\text{ kJ/mol}
\]"""
            },
            {
                "id": "u3-prob4",
                "number": 4,
                "title": "Assignment and Analysis of Rovibrational P and R Branch Lines",
                "difficulty": "Intermediate",
                "statement": r"""In the fundamental infrared absorption band of \(^{1}\text{H}^{35}\text{Cl}\), four consecutive lines are recorded at:
\(\tilde{\nu}_A = 2865.1\text{ cm}^{-1}\), \(\tilde{\nu}_B = 2906.2\text{ cm}^{-1}\), \(\tilde{\nu}_C = 2925.8\text{ cm}^{-1}\), \(\tilde{\nu}_D = 2944.9\text{ cm}^{-1}\).
Notice the gap between lines A and B is \(\approx 41.1\text{ cm}^{-1}\), while between B and C is \(\approx 19.6\text{ cm}^{-1}\).
(a) Identify the band origin \(\tilde{\nu}_0\) and assign lines A, B, C, D to specific transitions (\(P(J)\) or \(R(J)\)).
(b) Estimate the average rotational constant \(B\).
(c) Explain the origin of the \(\approx 41\text{ cm}^{-1}\) gap between lines A and B.""",
                "solution": r"""<p><strong>Step (a): Identification of band origin and line assignments</strong></p>
<p>In a rovibrational spectrum with \(\Delta J = \pm 1\), the separation between consecutive lines within a branch is \(\approx 2B\), whereas the gap across the missing Q-branch (\(P(1)\) to \(R(0)\)) is \(\approx 4B\).</p>
<p>The gap between \(\tilde{\nu}_A = 2865.1\text{ cm}^{-1}\) and \(\tilde{\nu}_B = 2906.2\text{ cm}^{-1}\) is \(41.1\text{ cm}^{-1} \approx 4B\). Therefore:</p>
<ul>
  <li>Line A is the first line of the P-branch: \(P(1)\) (\(v=0, J=1 \to v=1, J=0\))</li>
  <li>Line B is the first line of the R-branch: \(R(0)\) (\(v=0, J=0 \to v=1, J=1\))</li>
  <li>Line C is the second line of the R-branch: \(R(1)\) (\(v=0, J=1 \to v=1, J=2\))</li>
  <li>Line D is the third line of the R-branch: \(R(2)\) (\(v=0, J=2 \to v=1, J=3\))</li>
</ul>
<p>The band origin \(\tilde{\nu}_0\) lies midway between \(P(1)\) and \(R(0)\):</p>
\[
\tilde{\nu}_0 \approx \frac{2865.1 + 2906.2}{2} = 2885.65\text{ cm}^{-1}
\]
<p><strong>Step (b): Rotational constant B</strong></p>
\[
4B \approx 41.1\text{ cm}^{-1} \implies B \approx 10.28\text{ cm}^{-1}
\]
<p>Checking R-branch spacing:</p>
\[
R(1) - R(0) = 2925.8 - 2906.2 = 19.6\text{ cm}^{-1} \approx 2B \implies B \approx 9.8\text{ cm}^{-1}
\]
<p><strong>Step (c): Physical origin of the 4B gap</strong></p>
<p>Because \(\Delta J = 0\) is strictly forbidden for \(\Sigma \to \Sigma\) transitions, there is no Q-branch. The transition from \(J=0 \to 0\) cannot occur, leaving a vacant window of width \((R(0) - P(1)) = (\tilde{\nu}_0 + 2B) - (\tilde{\nu}_0 - 2B) = 4B\).</p>"""
            },
            {
                "id": "u3-prob5",
                "number": 5,
                "title": "Extraction of B0 and B1 via Method of Combination Differences",
                "difficulty": "Advanced",
                "statement": r"""High-resolution FTIR data for the \(^{12}\text{C}^{16}\text{O}\) fundamental band yields the following lines:
\(R(0) = 2147.08\text{ cm}^{-1}\), \(R(1) = 2150.86\text{ cm}^{-1}\), \(R(2) = 2154.60\text{ cm}^{-1}\),
\(P(1) = 2139.43\text{ cm}^{-1}\), \(P(2) = 2135.55\text{ cm}^{-1}\), \(P(3) = 2131.63\text{ cm}^{-1}\).
(a) Use the combination difference \(\Delta_2 F'(1) = R(1) - P(1)\) to calculate \(B_1\).
(b) Use the combination difference \(\Delta_2 F''(1) = R(0) - P(2)\) to calculate \(B_0\).
(c) Determine the vibration-rotation coupling constant \(\alpha_e = B_0 - B_1\).""",
                "solution": r"""<p><strong>Step (a): Upper state B1 calculation</strong></p>
<p>The combination difference for the upper state with \(J = 1\) is:</p>
\[
\Delta_2 F'(1) = R(1) - P(1) = 4B_1\left(1 + \frac{1}{2}\right) = 6 B_1
\]
\[
R(1) - P(1) = 2150.86 - 2139.43 = 11.43\text{ cm}^{-1}
\]
\[
B_1 = \frac{11.43\text{ cm}^{-1}}{6} = 1.9050\text{ cm}^{-1}
\]
<p><strong>Step (b): Lower state B0 calculation</strong></p>
<p>The combination difference for the lower state with \(J = 1\) is:</p>
\[
\Delta_2 F''(1) = R(0) - P(2) = 4B_0\left(1 + \frac{1}{2}\right) = 6 B_0
\]
\[
R(0) - P(2) = 2147.08 - 2135.55 = 11.53\text{ cm}^{-1}
\]
\[
B_0 = \frac{11.53\text{ cm}^{-1}}{6} = 1.9217\text{ cm}^{-1}
\]
<p><strong>Step (c): Vibration-rotation interaction constant \(\alpha_e\)</strong></p>
\[
\alpha_e = B_0 - B_1 = 1.9217 - 1.9050 = 0.0167\text{ cm}^{-1}
\]
<p>The equilibrium rotational constant is \(B_e = B_0 + \frac{1}{2}\alpha_e = 1.9217 + 0.00835 = 1.9300\text{ cm}^{-1}\).</p>"""
            },
            {
                "id": "u3-prob6",
                "number": 6,
                "title": "Band Head Formation in the R-Branch",
                "difficulty": "Advanced",
                "statement": r"""A diatomic molecule has band origin \(\tilde{\nu}_0 = 2000.0\text{ cm}^{-1}\), lower state rotational constant \(B_0 = 1.800\text{ cm}^{-1}\), and vibration-rotation coupling constant \(\alpha_e = 0.025\text{ cm}^{-1}\).
(a) Express \(\tilde{\nu}_R(J)\) as a function of \(J\).
(b) Calculate the rotational quantum number \(J_{\text{head}}\) at which the R-branch forms a band head.
(c) Calculate the wavenumber of the band head \(\tilde{\nu}_{\text{head}}\).""",
                "solution": r"""<p><strong>Step (a): R-branch wavenumber function</strong></p>
<p>With \(B_1 = B_0 - \alpha_e = 1.800 - 0.025 = 1.775\text{ cm}^{-1}\):</p>
\[
\tilde{\nu}_R(J) = \tilde{\nu}_0 + 2B_1 + (3B_1 - B_0)J + (B_1 - B_0)J^2
\]
\[
2B_1 = 2(1.775) = 3.550\text{ cm}^{-1}
\]
\[
3B_1 - B_0 = 3(1.775) - 1.800 = 5.325 - 1.800 = 3.525\text{ cm}^{-1}
\]
\[
B_1 - B_0 = -\alpha_e = -0.025\text{ cm}^{-1}
\]
\[
\tilde{\nu}_R(J) = 2000.0 + 3.550 + 3.525 J - 0.025 J^2 = 2003.55 + 3.525 J - 0.025 J^2
\]
<p><strong>Step (b): Band head location J_head</strong></p>
<p>At the band head, the wavenumber reaches an extremum: \(\frac{d\tilde{\nu}_R}{dJ} = 0\):</p>
\[
\frac{d\tilde{\nu}_R}{dJ} = 3.525 - 0.050 J = 0 \implies J_{\text{head}} = \frac{3.525}{0.050} = 70.5 \approx 70 \text{ or } 71
\]
<p><strong>Step (c): Wavenumber of the band head</strong></p>
<p>Evaluating at \(J = 70\):</p>
\[
\tilde{\nu}_R(70) = 2003.55 + 3.525(70) - 0.025(70)^2 = 2003.55 + 246.75 - 122.50 = 2127.80\text{ cm}^{-1}
\]
<p>Evaluating at \(J = 71\):</p>
\[
\tilde{\nu}_R(71) = 2003.55 + 3.525(71) - 0.025(71)^2 = 2003.55 + 250.275 - 126.025 = 2127.80\text{ cm}^{-1}
\]
<p>Beyond \(J = 70\), lines turn back toward lower wavenumbers, creating an intense pile-up (band head) shaded toward the red.</p>"""
            },
            {
                "id": "u3-prob7",
                "number": 7,
                "title": "Normal Modes and Fermi Resonance in Carbon Dioxide",
                "difficulty": "Intermediate",
                "statement": r"""Carbon dioxide (\(\text{CO}_2\)) is a linear triatomic molecule.
(a) Determine the number of normal vibrational modes.
(b) Classify each normal mode by symmetry (\(\Sigma_g^+, \Pi_u, \Sigma_u^+\)), state whether it is infrared active or inactive, and give approximate wavenumbers.
(c) Explain the phenomenon of Fermi resonance between the symmetric stretch \(\nu_1\) and the first overtone of the bend \(2\nu_2\). Why does the Raman spectrum show a doublet at \(1285\text{ cm}^{-1}\) and \(1388\text{ cm}^{-1}\)?""",
                "solution": r"""<p><strong>Step (a): Degrees of vibrational freedom</strong></p>
<p>For a linear molecule with \(N = 3\) atoms:</p>
\[
3N - 5 = 3(3) - 5 = 4\text{ normal vibrational modes}
\]
<p><strong>Step (b): Classification of normal modes</strong></p>
<ol>
  <li><strong>Symmetric Stretch (\(\nu_1\), \(\Sigma_g^+\)):</strong> \(\sim 1337\text{ cm}^{-1}\). The two C=O bonds stretch symmetrically. The dipole moment remains strictly zero throughout the vibration (\((d\mu/dq)_0 = 0\)). <strong>IR inactive</strong>, Raman active.</li>
  <li><strong>Bending Mode (\(\nu_2\), \(\Pi_u\)):</strong> \(\sim 667\text{ cm}^{-1}\). Doubly degenerate (bending in xz and yz planes). The linear geometry bends, creating an oscillating perpendicular dipole moment. <strong>IR active</strong>, Raman inactive.</li>
  <li><strong>Asymmetric Stretch (\(\nu_3\), \(\Sigma_u^+\)):</strong> \(\sim 2349\text{ cm}^{-1}\). One C=O bond contracts while the other stretches, producing an oscillating parallel dipole moment. <strong>IR active</strong>, Raman inactive.</li>
</ol>
<p><strong>Step (c): Fermi resonance mechanism</strong></p>
<p>The fundamental symmetric stretch \(\nu_1\) has unperturbed wavenumber \(\approx 1337\text{ cm}^{-1}\) with \(\Sigma_g^+\) symmetry. The bending overtone \(2\nu_2\) has unperturbed wavenumber \(2 \times 667 \approx 1334\text{ cm}^{-1}\) and also contains a \(\Sigma_g^+\) component.</p>
<p>Because these two states have:</p>
<ul>
  <li>Nearly identical unperturbed energies (\(\Delta E_0 \approx 3\text{ cm}^{-1}\))</li>
  <li>Identical irreducible representation (\(\Sigma_g^+\))</li>
</ul>
<p>They are coupled by cubic anharmonic terms in the molecular potential (\(k_{122} q_1 q_2^2\)). Quantum mechanical perturbation theory mixes the wavefunctions:</p>
\[
\psi_{\pm} = \frac{1}{\sqrt{2}}(\psi_{\nu_1} \pm \psi_{2\nu_2})
\]
<p>This quantum mechanical mixing repels the energy levels apart, producing a Fermi doublet at \(1285\text{ cm}^{-1}\) and \(1388\text{ cm}^{-1}\) with shared Raman scattering intensity.</p>"""
            }
        ]
    }
    units.append(u3)

    return units

if __name__ == "__main__":
    units = get_units_1_2_3()
    print(f"Successfully generated Units 1-3. Total units: {len(units)}")
    for u in units:
        print(f"Unit {u['number']}: {len(u['sections'])} sections, {len(u['problems'])} problems.")
