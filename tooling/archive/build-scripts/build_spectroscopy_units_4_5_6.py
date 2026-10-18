#!/usr/bin/env python3
"""
build_spectroscopy_units_4_5_6.py
Builds Units 4, 5, and 6 for Chemical Spectroscopy.
Unit 4: Raman Spectroscopy: Classical & Quantum Theory, Rotational & Vibrational Selection Rules
Unit 5: Electronic Spectroscopy of Atoms: Angular Momentum Coupling & Atomic Term Symbols
Unit 6: Molecular Electronic Spectroscopy & The Franck-Condon Principle
"""

import json

def get_units_4_5_6():
    units = []

    # =========================================================================
    # UNIT 4: Raman Spectroscopy: Classical & Quantum Theory, Rotational & Vibrational Selection Rules
    # =========================================================================
    u4 = {
        "id": "unit4",
        "number": 4,
        "title": "Unit 4: Raman Spectroscopy: Classical & Quantum Theory, Rotational & Vibrational Selection Rules",
        "description": "Classical and quantum scattering theory of the Raman effect, polarizability tensors and ellipsoids, Rayleigh vs Stokes/anti-Stokes scattering, temperature-dependent intensity ratios, pure rotational Raman spectra (4B and 6B spacing), vibrational Raman selection rules, depolarization ratios, rule of mutual exclusion in centrosymmetric molecules, resonance Raman, and Surface-Enhanced Raman Scattering (SERS).",
        "simulations": [
            {
                "id": "sim_spec_raman_polarizability_ellipsoid",
                "title": "Raman Scattering & Polarizability Ellipsoid",
                "description": "Interactive 60 FPS simulator demonstrating classical and quantum Raman scattering. View the 3D dynamic polarizability ellipsoid oscillating with molecular vibration, modulate incident laser wavelength (532 nm vs 785 nm), observe the resulting Rayleigh, Stokes, and Anti-Stokes spectral peaks, and adjust temperature T to verify the Boltzmann exponential intensity ratio."
            }
        ],
        "sections": [
            {
                "id": "u4-sec1",
                "number": "4.1",
                "title": "Classical Electromagnetic Theory of the Raman Effect",
                "content": r"""<p>When a molecule is placed in an oscillating electric field \(\vec{E}(t) = \vec{E}_0 \cos(2\pi\nu_0 t)\) of incident monochromatic radiation (typically an intense laser), the electric field distorts the electron cloud, inducing a temporary electric dipole moment \(\vec{\mu}_{\text{ind}}(t)\):</p>
\[
\vec{\mu}_{\text{ind}}(t) = \boldsymbol{\alpha} \vec{E}(t)
\]
<p>where \(\boldsymbol{\alpha}\) is the second-rank symmetric <strong>molecular polarizability tensor</strong>:</p>
\[
\boldsymbol{\alpha} = \begin{pmatrix} \alpha_{xx} & \alpha_{xy} & \alpha_{xz} \\ \alpha_{yx} & \alpha_{yy} & \alpha_{yz} \\ \alpha_{zx} & \alpha_{zy} & \alpha_{zz} \end{pmatrix}
\]
<h4 class="content-heading">Vibrational Modulation of Polarizability</h4>
<p>If the molecule undergoes a normal vibration along coordinate \(q(t) = q_0 \cos(2\pi\nu_{\text{vib}} t)\), the polarizability varies with nuclear displacement. Expanding \(\boldsymbol{\alpha}\) in a Taylor series about equilibrium \(q = 0\):</p>
\[
\boldsymbol{\alpha}(q) = \boldsymbol{\alpha}_0 + \left(\frac{\partial\boldsymbol{\alpha}}{\partial q}\right)_0 q + \dots = \boldsymbol{\alpha}_0 + \left(\frac{\partial\boldsymbol{\alpha}}{\partial q}\right)_0 q_0 \cos(2\pi\nu_{\text{vib}} t)
\]
<p>Substituting this into the induced dipole moment:</p>
\[
\vec{\mu}_{\text{ind}}(t) = \left[ \boldsymbol{\alpha}_0 + \left(\frac{\partial\boldsymbol{\alpha}}{\partial q}\right)_0 q_0 \cos(2\pi\nu_{\text{vib}} t) \right] \vec{E}_0 \cos(2\pi\nu_0 t)
\]
<p>Applying the trigonometric product identity \(\cos(A)\cos(B) = \frac{1}{2}[\cos(A+B) + \cos(A-B)]\):</p>
\[
\vec{\mu}_{\text{ind}}(t) = \boldsymbol{\alpha}_0 \vec{E}_0 \cos(2\pi\nu_0 t) + \frac{1}{2}\left(\frac{\partial\boldsymbol{\alpha}}{\partial q}\right)_0 q_0 \vec{E}_0 \left[ \cos(2\pi(\nu_0 - \nu_{\text{vib}}) t) + \cos(2\pi(\nu_0 + \nu_{\text{vib}}) t) \right]
\]
<p>According to classical electrodynamics, an oscillating dipole radiates power proportional to \(\nu^4 |\vec{\mu}_{\text{ind}}|^2\). The induced dipole contains three distinct frequency components:</p>
<ol>
  <li><strong>Rayleigh Scattering (\(\nu_0\)):</strong> Elastic scattering at the unmodified incident laser frequency \(\nu_0\), governed by equilibrium polarizability \(\boldsymbol{\alpha}_0\).</li>
  <li><strong>Stokes Raman Scattering (\(\nu_0 - \nu_{\text{vib}}\)):</strong> Inelastic scattering shifted to lower frequency (longer wavelength).</li>
  <li><strong>Anti-Stokes Raman Scattering (\(\nu_0 + \nu_{\text{vib}}\)):</strong> Inelastic scattering shifted to higher frequency (shorter wavelength).</li>
</ol>
<p>The <strong>classical gross selection rule</strong> is evident: Raman scattering occurs if and only if the molecular polarizability changes during the vibration: \(\left(\frac{\partial\boldsymbol{\alpha}}{\partial q}\right)_0 \neq 0\).</p>"""
            },
            {
                "id": "u4-sec2",
                "number": "4.2",
                "title": "Quantum Mechanical Scattering Theory & Kramers-Heisenberg Formalism",
                "content": r"""<p>Quantum mechanically, Raman scattering is an inelastic two-photon process involving the simultaneous annihilation of an incident photon \(h\nu_0\) and creation of a scattered photon \(h\nu_s\). The molecule transitions from initial state \(|i\rangle\) to final state \(|f\rangle\) via an intermediate virtual state \(|r\rangle\):</p>
<p>Applying second-order time-dependent perturbation theory, Kramers, Heisenberg, and Dirac formulated the transition polarizability tensor component \((\alpha_{\rho\sigma})_{fi}\):</p>
\[
(\alpha_{\rho\sigma})_{fi} = \frac{1}{\hbar} \sum_r \left[ \frac{\langle f | \hat{\mu}_\rho | r \rangle \langle r | \hat{\mu}_\sigma | i \rangle}{\omega_{ri} - \omega_0 - i\Gamma_r} + \frac{\langle f | \hat{\mu}_\sigma | r \rangle \langle r | \hat{\mu}_\rho | i \rangle}{\omega_{ri} + \omega_s + i\Gamma_r} \right]
\]
<p>where \(|r\rangle\) represents all complete eigenstates of the molecular Hamiltonian, \(\hat{\mu}_\rho\) and \(\hat{\mu}_\sigma\) are components of the electric dipole operator, and \(\Gamma_r\) is the damping width of state \(r\).</p>
<h4 class="content-heading">Virtual vs Real Intermediate States</h4>
<ul>
  <li><strong>Normal Raman Scattering:</strong> The incident photon energy \(h\nu_0\) is far below any electronic absorption band (\(\omega_0 \ll \omega_{ri}\)). The state \(|r\rangle\) is a non-stationary <em>virtual state</em> (a quantum superposition of all excited states lasting \(\sim 10^{-15}\text{ s}\)). Scattering intensity is weak (typically \(10^{-6} - 10^{-8}\) of incident laser power).</li>
  <li><strong>Resonance Raman Scattering:</strong> The incident photon energy matches an electronic transition (\(\omega_0 \approx \omega_{ri}\)). The denominator \((\omega_{ri} - \omega_0)\) approaches zero, enhancing Raman scattering cross-sections by \(10^4 - 10^6\).</li>
</ul>"""
            },
            {
                "id": "u4-sec3",
                "number": "4.3",
                "title": "Temperature Dependence & Stokes/Anti-Stokes Intensity Ratios",
                "content": r"""<p>In quantum mechanics, Stokes transitions correspond to molecules initially in the ground vibrational state \(v=0\) absorbing energy and terminating in \(v=1\): \(\Delta E = +h\nu_{\text{vib}}\). Anti-Stokes transitions correspond to molecules initially in the excited state \(v=1\) transferring energy to the scattered photon and terminating in \(v=0\): \(\Delta E = -h\nu_{\text{vib}}\).</p>
<p>The intensity of scattered radiation depends on the initial state population and the fourth power of the scattered frequency (\(\nu^4\) Rayleigh scattering law):</p>
\[
I_{\text{Stokes}} \propto N_0 (\nu_0 - \nu_{\text{vib}})^4
\]
\[
I_{\text{anti-Stokes}} \propto N_1 (\nu_0 + \nu_{\text{vib}})^4
\]
<h4 class="content-heading">Boltzmann Ratio Derivation</h4>
<p>At thermal equilibrium at temperature \(T\), the ratio of populations \(N_1 / N_0\) is given by the Boltzmann distribution:</p>
\[
\frac{N_1}{N_0} = \exp\left(-\frac{h\nu_{\text{vib}}}{k_B T}\right) = \exp\left(-\frac{h c \tilde{\nu}_{\text{vib}}}{k_B T}\right)
\]
<p>Therefore, the theoretical intensity ratio of anti-Stokes to Stokes Raman lines is:</p>
\[
\frac{I_{\text{anti-Stokes}}}{I_{\text{Stokes}}} = \left(\frac{\nu_0 + \nu_{\text{vib}}}{\nu_0 - \nu_{\text{vib}}}\right)^4 \exp\left(-\frac{h c \tilde{\nu}_{\text{vib}}}{k_B T}\right)
\]
<p>At room temperature (\(T = 300\text{ K}\), \(k_B T / hc \approx 208.5\text{ cm}^{-1}\)), for a typical vibration at \(\tilde{\nu}_{\text{vib}} = 1000\text{ cm}^{-1}\):</p>
\[
\exp\left(-\frac{1000}{208.5}\right) = \exp(-4.796) \approx 0.0083
\]
<p>The Stokes line is more than 120 times more intense than the anti-Stokes line. As temperature increases, the anti-Stokes line grows rapidly in intensity, providing a precise non-invasive optical thermometer.</p>"""
            },
            {
                "id": "u4-sec4",
                "number": "4.4",
                "title": "Pure Rotational Raman Spectra of Diatomic Rotors",
                "content": r"""<p>In pure rotational Raman spectroscopy, transitions occur between rotational states within the ground vibrational state. The interaction depends on the <strong>anisotropy of molecular polarizability</strong> \(\gamma = \alpha_\parallel - \alpha_\perp\), where \(\alpha_\parallel\) is polarizability along the internuclear axis and \(\alpha_\perp\) is perpendicular to it.</p>
<p>Because the polarizability ellipsoid appears identical after a rotation of \(180^\circ\) (\(\pi\) radians), the polarizability modulates at twice the rotational frequency: \(\nu_{\text{pol}} = 2\nu_{\text{rot}}\). This leads to the fundamental rotational Raman selection rule:</p>
\[
\Delta J = 0, \pm 2
\]
<p>Transitions with \(\Delta J = 0\) contribute to the unshifted Rayleigh line. Transitions with \(\Delta J = +2\) form the <strong>S-branch</strong> (Stokes Raman lines, terminating on higher \(J\)). Transitions with \(\Delta J = -2\) form the <strong>O-branch</strong> (anti-Stokes Raman lines).</p>
<h4 class="content-heading">Transition Wavenumbers & Line Spacings</h4>
<p>For an initial state \(J\), the Stokes transition frequency (\(J \to J+2\)) is:</p>
\[
\tilde{\nu}_S(J) = \tilde{\nu}_0 - [F(J+2) - F(J)] = \tilde{\nu}_0 - B[(J+2)(J+3) - J(J+1)] = \tilde{\nu}_0 - 2B(2J+3)
\]
<p>Evaluating for consecutive \(J\) values:</p>
<ul>
  <li>\(J = 0 \to 2\): \(\tilde{\nu}_S(0) = \tilde{\nu}_0 - 6B\) (first Stokes line is displaced by \(6B\) from Rayleigh line)</li>
  <li>\(J = 1 \to 3\): \(\tilde{\nu}_S(1) = \tilde{\nu}_0 - 10B\)</li>
  <li>\(J = 2 \to 4\): \(\tilde{\nu}_S(2) = \tilde{\nu}_0 - 14B\)</li>
  <li>\(J = 3 \to 5\): \(\tilde{\nu}_S(3) = \tilde{\nu}_0 - 18B\)</li>
</ul>
<p>The separation between consecutive rotational Raman lines is strictly:</p>
\[
\Delta \tilde{\nu} = 4B
\]
<p>The first line on either side is separated from the central Rayleigh line by \(6B\). Pure rotational Raman spectroscopy enables the determination of bond lengths and moments of inertia for <strong>homonuclear diatomic molecules</strong> (\(\text{N}_2, \text{O}_2, \text{H}_2\)) that have no permanent dipole moment and are completely invisible in microwave spectroscopy.</p>"""
            },
            {
                "id": "u4-sec5",
                "number": "4.5",
                "title": "Vibrational Raman Spectra & Depolarization Ratios",
                "content": r"""<p>In vibrational Raman spectroscopy, the polarization of scattered light reveals the symmetry of the underlying molecular vibration. Let incident laser light be linearly polarized along the \(z\)-axis, propagating along \(x\). The scattered light is observed perpendicular to propagation (along \(y\)).</p>
<p>The scattered light contains two orthogonal polarization components:</p>
<ol>
  <li>\(I_\parallel\) (\(I_z\)): Intensity polarized parallel to the incident polarization vector.</li>
  <li>\(I_\perp\) (\(I_x\)): Intensity polarized perpendicular to the incident polarization vector.</li>
</ol>
<h4 class="content-heading">Depolarization Ratio (\(\rho\))</h4>
<p>The depolarization ratio \(\rho\) is defined as:</p>
\[
\rho = \frac{I_\perp}{I_\parallel}
\]
<p>In terms of the rotational invariants of the derived polarizability tensor—mean polarizability derivative \(\bar{\alpha}' = \frac{1}{3}(\alpha'_{xx} + \alpha'_{yy} + \alpha'_{zz})\) and anisotropy derivative \(\gamma'^2 = \frac{1}{2}[(\alpha'_{xx} - \alpha'_{yy})^2 + (\alpha'_{yy} - \alpha'_{zz})^2 + (\alpha'_{zz} - \alpha'_{xx})^2 + 6(\alpha'^2_{xy} + \alpha'^2_{yz} + \alpha'^2_{zx})]\):</p>
\[
\rho = \frac{3 \gamma'^2}{45 \bar{\alpha}'^2 + 4 \gamma'^2}
\]
<h4 class="content-heading">Classification of Raman Bands</h4>
<ul>
  <li><strong>Totally Symmetric Vibrations (\(A_1, A_g\)):</strong> Both \(\bar{\alpha}' \neq 0\) and \(\gamma' \neq 0\). The depolarization ratio satisfies \(0 \le \rho < \frac{3}{4}\). The band is designated as <strong>polarized</strong>. For spherically symmetric modes (e.g., \(\nu_1\) of \(\text{CH}_4\) or \(\text{CCl}_4\)), \(\gamma' = 0 \implies \rho = 0\) (completely polarized).</li>
  <li><strong>Non-Totally Symmetric Vibrations (e.g., \(B_1, E, T_2\)):</strong> By symmetry, the spherical average \(\bar{\alpha}' = 0\), while \(\gamma' \neq 0\). Substituting \(\bar{\alpha}' = 0\) into the formula gives identically:
  \[
  \rho = \frac{3 \gamma'^2}{0 + 4 \gamma'^2} = \frac{3}{4} = 0.75
  \]
  The band is designated as <strong>depolarized</strong>.</li>
</ul>
<p>Measuring \(\rho\) experimentally provides an unambiguous diagnostic for assigning vibrational symmetry species.</p>"""
            },
            {
                "id": "u4-sec6",
                "number": "4.6",
                "title": "The Rule of Mutual Exclusion & Structural Elucidation",
                "content": r"""<p>The fundamental relationship between infrared and Raman activity is governed by molecular point group symmetry, codified by the <strong>Rule of Mutual Exclusion</strong>:</p>
<blockquote>
  <strong>The Rule of Mutual Exclusion:</strong> For any molecule possessing an inversion center (centrosymmetric point groups such as \(C_i, C_{2h}, D_{2h}, D_{4h}, D_{\infty h}, D_{6h}, O_h\)), no normal vibrational mode can be both infrared-active and Raman-active. Vibrations that are infrared-active are Raman-inactive, and vibrations that are Raman-active are infrared-inactive.
</blockquote>
<h4 class="content-heading">Group Theoretical Proof</h4>
<p>The inversion operator \(\hat{i}\) maps coordinates \((x, y, z) \to (-x, -y, -z)\):</p>
<ol>
  <li>The electric dipole moment operator \(\hat{\vec{\mu}} = \sum q_i \vec{r}_i\) changes sign under inversion: \(\hat{i} \hat{\vec{\mu}} = -\hat{\vec{\mu}}\). Therefore, \(\hat{\vec{\mu}}\) transforms as an <strong>ungerade (\(u\))</strong> irreducible representation. An infrared transition from the totally symmetric ground state (\(A_g\)) is allowed only if the excited state is ungerade (\(u\)):
  \[
  \Gamma(\psi_v) \otimes \Gamma(\mu) \otimes \Gamma(\psi_0) = u \otimes u \otimes g = g \quad (\text{allowed})
  \]
  </li>
  <li>The polarizability tensor components \(\alpha_{ij}\) involve quadratic products of coordinates (e.g., \(x^2, xy, z^2\)), which do not change sign under inversion: \(\hat{i} \boldsymbol{\alpha} = +\boldsymbol{\alpha}\). Therefore, \(\boldsymbol{\alpha}\) transforms as a <strong>gerade (\(g\))</strong> irreducible representation. A Raman transition is allowed only if the excited state is gerade (\(g\)):
  \[
  \Gamma(\psi_v) \otimes \Gamma(\alpha) \otimes \Gamma(\psi_0) = g \otimes g \otimes g = g \quad (\text{allowed})
  \]
  </li>
</ol>
<p>Since no state can simultaneously be both gerade and ungerade, the mutual exclusion rule is absolute.</p>
<h4 class="content-heading">Diagnostic Applications in Structural Chemistry</h4>
<ul>
  <li><strong>Carbon Dioxide (\(\text{CO}_2\)):</strong> Centrosymmetric (\(D_{\infty h}\)). \(\nu_1\) (\(1337\text{ cm}^{-1}\), \(\Sigma_g^+\)) is Raman-only; \(\nu_2\) (\(667\text{ cm}^{-1}\), \(\Pi_u\)) and \(\nu_3\) (\(2349\text{ cm}^{-1}\), \(\Sigma_u^+\)) are IR-only. Proves that \(\text{CO}_2\) is strictly linear, not bent!</li>
  <li><strong>Nitrous Oxide (\(\text{N}_2\text{O}\)):</strong> Non-centrosymmetric (\(C_{\infty v}\)). All three fundamental modes appear in both IR and Raman spectra. Proves the unsymmetric connectivity is \(\text{N-N-O}\), not \(\text{N-O-N}\).</li>
  <li><strong>Ethylene vs Cycloalkanes:</strong> Planar ethylene (\(D_{2h}\)) exhibits mutual exclusion, while twisted conformations lose the center of inversion.</li>
</ul>"""
            },
            {
                "id": "u4-sec7",
                "number": "4.7",
                "title": "Surface-Enhanced Raman Scattering (SERS) & Resonance Raman",
                "content": r"""<p>Normal Raman spectroscopy suffers from inherently small scattering cross-sections (\(\sigma_{\text{Raman}} \sim 10^{-30}\text{ cm}^2/\text{molecule}\)). Two advanced techniques overcome this sensitivity limitation:</p>
<h4 class="content-heading">1. Surface-Enhanced Raman Scattering (SERS)</h4>
<p>Discovered by Fleischmann in 1974, molecules adsorbed onto nanostructured noble metal surfaces (gold, silver, copper) exhibit astronomical Raman enhancement factors of \(10^6 - 10^{11}\), achieving single-molecule detection sensitivity.</p>
<p>SERS enhancement operates via two synergistic physical mechanisms:</p>
<ol>
  <li><strong>Electromagnetic Enhancement (EM, \(10^4 - 10^8\)):</strong> Laser excitation drives localized surface plasmon resonances (LSPR) in metal nanoparticles. The local electric field at nanoscale 'hot spots' (inter-particle junctions) is amplified: \(E_{\text{loc}} = g(\omega) E_0\). Because both the incident field and scattered field are amplified, the Raman intensity scales as:
  \[
  G_{\text{SERS}}^{\text{EM}} = |g(\omega_0)|^2 |g(\omega_s)|^2 \approx |E_{\text{loc}} / E_0|^4
  \]
  This is the renowned <strong>\(|E|^4\) enhancement rule</strong>.</li>
  <li><strong>Chemical (Charge-Transfer) Enhancement (CHEM, \(10^1 - 10^3\)):</strong> Direct orbital hybridization and dynamic charge transfer between the metal Fermi level and molecular frontier orbitals (HOMO/LUMO) dynamically increases the polarizability derivative \((\partial\boldsymbol{\alpha}/\partial q)_0\).</li>
</ol>
<h4 class="content-heading">2. Resonance Raman Spectroscopy</h4>
<p>Tuning the excitation laser into an electronic absorption band of a chromophore selectively amplifies vibrations coupled to the electronic transition by \(10^3 - 10^6\), enabling targeted structural probing of metalloprotein active sites (e.g., heme iron-porphyrin bonds in hemoglobin) in dilute biological solutions.</p>"""
            }
        ],
        "problems": [
            {
                "id": "u4-prob1",
                "number": 1,
                "title": "Calculation of Stokes and Anti-Stokes Raman Frequencies",
                "difficulty": "Foundational",
                "statement": r"""A liquid sample of carbon tetrachloride (\(\text{CCl}_4\)) is irradiated with a frequency-doubled Nd:YAG laser operating at \(\lambda_0 = 532.00\text{ nm}\).
The symmetric breathing mode \(\nu_1\) of \(\text{CCl}_4\) has a vibrational wavenumber of \(\tilde{\nu}_{\text{vib}} = 459\text{ cm}^{-1}\).
(a) Calculate the wavenumber of the incident laser radiation \(\tilde{\nu}_0\).
(b) Calculate the wavenumber and wavelength (in nm) of the Stokes Raman line.
(c) Calculate the wavenumber and wavelength (in nm) of the Anti-Stokes Raman line.""",
                "solution": r"""<p><strong>Step (a): Incident laser wavenumber</strong></p>
\[
\tilde{\nu}_0 = \frac{1}{\lambda_0} = \frac{1}{532.00 \times 10^{-7}\text{ cm}} = 18796.99\text{ cm}^{-1}
\]
<p><strong>Step (b): Stokes Raman line</strong></p>
\[
\tilde{\nu}_{\text{Stokes}} = \tilde{\nu}_0 - \tilde{\nu}_{\text{vib}} = 18796.99 - 459.00 = 18337.99\text{ cm}^{-1}
\]
\[
\lambda_{\text{Stokes}} = \frac{1}{\tilde{\nu}_{\text{Stokes}}} = \frac{1}{18337.99\text{ cm}^{-1}} = 5.45316 \times 10^{-5}\text{ cm} = 545.32\text{ nm}
\]
<p><strong>Step (c): Anti-Stokes Raman line</strong></p>
\[
\tilde{\nu}_{\text{Anti-Stokes}} = \tilde{\nu}_0 + \tilde{\nu}_{\text{vib}} = 18796.99 + 459.00 = 19255.99\text{ cm}^{-1}
\]
\[
\lambda_{\text{Anti-Stokes}} = \frac{1}{\tilde{\nu}_{\text{Anti-Stokes}}} = \frac{1}{19255.99\text{ cm}^{-1}} = 5.19319 \times 10^{-5}\text{ cm} = 519.32\text{ nm}
\]"""
            },
            {
                "id": "u4-prob2",
                "number": 2,
                "title": "Anti-Stokes to Stokes Intensity Ratio and Optical Thermometry",
                "difficulty": "Intermediate",
                "statement": r"""A Raman spectrometer monitors the \(\nu_1\) symmetric stretching mode of benzene at \(\tilde{\nu}_{\text{vib}} = 992\text{ cm}^{-1}\) using a \(532\text{ nm}\) laser (\(\tilde{\nu}_0 = 18797\text{ cm}^{-1}\)).
(a) Calculate the theoretical intensity ratio \(I_{\text{Anti-Stokes}} / I_{\text{Stokes}}\) at \(T = 298\text{ K}\).
(b) Calculate the intensity ratio at \(T = 600\text{ K}\).
(c) If in an industrial chemical reactor, the experimental ratio is measured as \(I_{\text{Anti-Stokes}} / I_{\text{Stokes}} = 0.0520\), determine the temperature \(T\) of the reacting benzene liquid.""",
                "solution": r"""<p><strong>Step (a): Ratio at 298 K</strong></p>
<p>The frequency factor is:</p>
\[
\left(\frac{\tilde{\nu}_0 + \tilde{\nu}_{\text{vib}}}{\tilde{\nu}_0 - \tilde{\nu}_{\text{vib}}}\right)^4 = \left(\frac{18797 + 992}{18797 - 992}\right)^4 = \left(\frac{19789}{17805}\right)^4 = (1.11143)^4 = 1.526
\]
<p>The Boltzmann thermal factor at \(T = 298\text{ K}\):</p>
\[
\frac{hc\tilde{\nu}_{\text{vib}}}{k_B T} = \frac{(6.62607 \times 10^{-34})(2.99792 \times 10^{10})(992)}{(1.38065 \times 10^{-23})(298)} = \frac{1.9705 \times 10^{-20}}{4.1143 \times 10^{-21}} = 4.7894
\]
\[
e^{-4.7894} = 8.317 \times 10^{-3}
\]
\[
\frac{I_{\text{Anti-Stokes}}}{I_{\text{Stokes}}} = 1.526 \times (8.317 \times 10^{-3}) = 1.269 \times 10^{-2} \approx 0.0127
\]
<p><strong>Step (b): Ratio at 600 K</strong></p>
\[
\frac{hc\tilde{\nu}_{\text{vib}}}{k_B T} = \frac{4.7894 \times 298}{600} = 2.3787
\]
\[
e^{-2.3787} = 0.09267
\]
\[
\frac{I_{\text{Anti-Stokes}}}{I_{\text{Stokes}}} = 1.526 \times 0.09267 = 0.1414
\]
<p><strong>Step (c): Temperature determination from measured ratio</strong></p>
\[
0.0520 = 1.526 \exp\left(-\frac{hc\tilde{\nu}_{\text{vib}}}{k_B T}\right) \implies \exp\left(-\frac{hc\tilde{\nu}_{\text{vib}}}{k_B T}\right) = \frac{0.0520}{1.526} = 0.034076
\]
\[
-\frac{hc\tilde{\nu}_{\text{vib}}}{k_B T} = \ln(0.034076) = -3.3792
\]
\[
T = \frac{hc\tilde{\nu}_{\text{vib}}}{3.3792 k_B} = \frac{1.9705 \times 10^{-20}}{(3.3792)(1.38065 \times 10^{-23})} = \frac{1.9705 \times 10^{-20}}{4.6655 \times 10^{-23}} = 422.4\text{ K} \approx 149.2^\circ\text{C}
\]"""
            },
            {
                "id": "u4-prob3",
                "number": 3,
                "title": "Pure Rotational Raman Line Spacing and Bond Length of Nitrogen",
                "difficulty": "Intermediate",
                "statement": r"""In the pure rotational Raman spectrum of molecular nitrogen (\(^{14}\text{N}_2\)), the separation between adjacent Stokes lines is measured as \(\Delta \tilde{\nu} = 7.960\text{ cm}^{-1}\).
(a) Determine the rotational constant \(B\) for \(^{14}\text{N}_2\).
(b) Calculate the displacement of the first Stokes line from the Rayleigh line.
(c) Calculate the moment of inertia \(I\) and determine the equilibrium bond length \(r_0\) of \(\text{N}_2\) in picometers (atomic mass of \(^{14}\text{N} = 14.00307\text{ u}\)).""",
                "solution": r"""<p><strong>Step (a): Rotational constant B</strong></p>
<p>In pure rotational Raman spectroscopy, line spacing between consecutive lines is \(\Delta \tilde{\nu} = 4B\):</p>
\[
4B = 7.960\text{ cm}^{-1} \implies B = 1.990\text{ cm}^{-1}
\]
<p><strong>Step (b): Displacement of first Stokes line</strong></p>
<p>The first Stokes line (\(J = 0 \to 2\)) is displaced by \(6B\) from the Rayleigh line:</p>
\[
\Delta \tilde{\nu}_{\text{first}} = 6B = 6(1.990\text{ cm}^{-1}) = 11.940\text{ cm}^{-1}
\]
<p><strong>Step (c): Moment of inertia and bond length</strong></p>
\[
I = \frac{h}{8\pi^2 c B} = \frac{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}}{8\pi^2 (2.99792 \times 10^{10}\text{ cm/s})(1.990\text{ cm}^{-1})} = \frac{6.62607 \times 10^{-34}}{4.71005 \times 10^{-7}} = 1.4068 \times 10^{-46}\text{ kg}\cdot\text{m}^2
\]
<p>Reduced mass of \(^{14}\text{N}_2\):</p>
\[
\mu = \frac{m_N}{2} = \frac{14.00307\text{ u}}{2} = 7.001535\text{ u} = (7.001535)(1.66054 \times 10^{-27}\text{ kg}) = 1.16263 \times 10^{-26}\text{ kg}
\]
\[
r_0 = \sqrt{\frac{I}{\mu}} = \sqrt{\frac{1.4068 \times 10^{-46}}{1.16263 \times 10^{-26}}} = \sqrt{1.2100 \times 10^{-20}\text{ m}^2} = 1.1000 \times 10^{-10}\text{ m} = 110.00\text{ pm}
\]
<p>This illustrates the power of rotational Raman spectroscopy to measure the bond length of homonuclear \(\text{N}_2\) with four-figure precision, despite having zero dipole moment.</p>"""
            },
            {
                "id": "u4-prob4",
                "number": 4,
                "title": "Depolarization Ratio Analysis and Symmetry Assignment",
                "difficulty": "Intermediate",
                "statement": r"""Polarized Raman measurements are performed on chloroform (\(\text{CHCl}_3\), \(C_{3v}\) symmetry) using linearly polarized laser excitation. For two distinct Raman bands, the following intensities are recorded:
Band A (\(366\text{ cm}^{-1}\)): \(I_\parallel = 850\text{ counts}\), \(I_\perp = 638\text{ counts}\).
Band B (\(667\text{ cm}^{-1}\)): \(I_\parallel = 2400\text{ counts}\), \(I_\perp = 96\text{ counts}\).
(a) Calculate the depolarization ratio \(\rho\) for Band A and Band B.
(b) Classify each band as polarized or depolarized.
(c) Assign the vibrational symmetry species (\(A_1\) vs \(E\)) for each band according to \(C_{3v}\) character table selection rules.""",
                "solution": r"""<p><strong>Step (a): Depolarization ratios</strong></p>
\[
\rho_A = \frac{I_\perp}{I_\parallel} = \frac{638}{850} = 0.7506 \approx 0.75
\]
\[
\rho_B = \frac{I_\perp}{I_\parallel} = \frac{96}{2400} = 0.040
\]
<p><strong>Step (b): Classification</strong></p>
<ul>
  <li><strong>Band A (\(\rho \approx 0.75\)):</strong> Exactly matches the theoretical limit \(\rho = 3/4\). The band is <strong>depolarized</strong>.</li>
  <li><strong>Band B (\(\rho = 0.040 \ll 0.75\)):</strong> Strongly polarized (\(\rho \ll 0.75\)). The band is <strong>polarized</strong>.</li>
</ul>
<p><strong>Step (c): Symmetry assignment in \(C_{3v}\)</strong></p>
<p>In the \(C_{3v}\) point group, normal modes belong to either \(A_1\) (totally symmetric) or \(E\) (doubly degenerate, non-totally symmetric):</p>
<ul>
  <li>Band B (\(667\text{ cm}^{-1}\)) is polarized (\(\rho < 0.75\)), which requires non-zero mean polarizability derivative \(\bar{\alpha}' \neq 0\). It is uniquely assigned to a totally symmetric <strong>\(A_1\) mode</strong> (the symmetric C-Cl stretch).</li>
  <li>Band A (\(366\text{ cm}^{-1}\)) is depolarized (\(\rho = 0.75\)), meaning \(\bar{\alpha}' = 0\). It is assigned to a non-totally symmetric <strong>\(E\) mode</strong> (the asymmetric \(\text{CCl}_3\) deformation).</li>
</ul>"""
            },
            {
                "id": "u4-prob5",
                "number": 5,
                "title": "Structural Discrimination of Dinitrogen Tetroxide via Mutual Exclusion",
                "difficulty": "Intermediate",
                "statement": r"""Two planar structural isomers are proposed for dinitrogen tetroxide (\(\text{N}_2\text{O}_4\)):
Structure 1: Symmetrical planar with an N-N bond and \(D_{2h}\) symmetry (\(\text{O}_2\text{N-NO}_2\)).
Structure 2: Nitrosyl nitrate planar structure with \(C_s\) or \(C_{2v}\) symmetry (\(\text{ON-ONO}_2\)).
Vibrational spectroscopic analysis reveals that twelve fundamental vibrational bands are observed: 6 appear exclusively in the Raman spectrum and 6 appear exclusively in the infrared spectrum. None of the observed frequencies coincide between IR and Raman.
(a) Determine which structural isomer is present based on the Rule of Mutual Exclusion.
(b) Explain why no bands coincide in the actual molecule.
(c) What vibrational pattern would be observed if Structure 2 were the true structure?""",
                "solution": r"""<p><strong>Step (a): Structural determination</strong></p>
<p>The observation that all six Raman bands are completely absent from the infrared spectrum, and all six infrared bands are absent from the Raman spectrum, demonstrates strict mutual exclusivity.</p>
<p>According to the <strong>Rule of Mutual Exclusion</strong>, a complete absence of coincident IR and Raman bands can only occur for a molecule possessing a <strong>center of inversion (\(i\))</strong>.</p>
<ul>
  <li>Structure 1 (\(\text{O}_2\text{N-NO}_2\), \(D_{2h}\)) possesses a center of inversion at the midpoint of the N-N bond.</li>
  <li>Structure 2 (\(\text{ON-ONO}_2\)) possesses no center of inversion.</li>
</ul>
<p>Therefore, the experimental spectrum unequivocally proves that \(\text{N}_2\text{O}_4\) adopts <strong>Structure 1 (\(D_{2h}\))</strong>.</p>
<p><strong>Step (b): Origin of mutual exclusion</strong></p>
<p>In \(D_{2h}\), normal vibrations are classified into gerade (\(A_g, B_{1g}, B_{2g}, B_{3g}\)) and ungerade (\(A_u, B_{1u}, B_{2u}, B_{3u}\)). The dipole moment transforms as ungerade (\(B_{1u}, B_{2u}, B_{3u}\)), rendering only \(u\)-modes IR-active. The polarizability tensor transforms as gerade, rendering only \(g\)-modes Raman-active. Since a mode cannot be simultaneously \(g\) and \(u\), zero coincident bands can exist.</p>
<p><strong>Step (c): Predicted behavior for Structure 2</strong></p>
<p>If Structure 2 were present, the absence of an inversion center would permit vibrations to be simultaneously IR and Raman active. Numerous bands would appear at identical wavenumbers in both spectra.</p>"""
            },
            {
                "id": "u4-prob6",
                "number": 6,
                "title": "Local Field Factor and SERS Enhancement Calculation",
                "difficulty": "Advanced",
                "statement": r"""A pyridine analyte molecule is adsorbed onto a silver nanoparticle dimer forming a plasmonic junction ('hot spot').
Upon laser irradiation at \(\lambda = 633\text{ nm}\), finite-difference time-domain (FDTD) electrodynamic simulations determine that the local electric field amplitude at the hot spot is amplified by a factor of \(|E_{\text{loc}} / E_0| = 75.0\).
(a) Estimate the electromagnetic SERS enhancement factor \(G_{\text{SERS}}^{\text{EM}}\) using the \(|E|^4\) approximation.
(b) If charge-transfer chemical enhancement adds an additional factor of \(G_{\text{CHEM}} = 40.0\), what is the total SERS enhancement factor?
(c) If the unenhanced Raman scattering of the analyte in bulk solution produces a detector signal of \(5.0 \times 10^{-14}\text{ W}\) for \(10^{15}\) molecules, calculate the expected SERS signal per single molecule at the hot spot.""",
                "solution": r"""<p><strong>Step (a): Electromagnetic enhancement factor</strong></p>
<p>According to the \(|E|^4\) plasmonic enhancement approximation:</p>
\[
G_{\text{SERS}}^{\text{EM}} \approx \left|\frac{E_{\text{loc}}}{E_0}\right|^4 = (75.0)^4 = 3.164 \times 10^7
\]
<p><strong>Step (b): Total SERS enhancement</strong></p>
\[
G_{\text{total}} = G_{\text{SERS}}^{\text{EM}} \times G_{\text{CHEM}} = (3.164 \times 10^7) \times 40.0 = 1.266 \times 10^9
\]
<p>The Raman signal is amplified by more than 1.2 billion times!</p>
<p><strong>Step (c): Single-molecule signal</strong></p>
<p>The unenhanced signal per single molecule in bulk solution is:</p>
\[
P_{\text{single, bulk}} = \frac{5.0 \times 10^{-14}\text{ W}}{10^{15}\text{ molecules}} = 5.0 \times 10^{-29}\text{ W/molecule}
\]
<p>At the SERS hot spot, multiplying by the total enhancement factor:</p>
\[
P_{\text{single, SERS}} = P_{\text{single, bulk}} \times G_{\text{total}} = (5.0 \times 10^{-29}\text{ W}) \times (1.266 \times 10^9) = 6.33 \times 10^{-20}\text{ W}
\]
<p>For a photon energy at \(633\text{ nm}\) (\(E_{\text{photon}} \approx 3.14 \times 10^{-19}\text{ J}\)), this corresponds to a photon flux of \(\approx 0.2\text{ photons/second}\) per single molecule, well within the threshold of single-molecule photon-counting detectors.</p>"""
            },
            {
                "id": "u4-prob7",
                "number": 7,
                "title": "Laser Wavelength Comparison and Fluorescence Avoidance in Raman",
                "difficulty": "Foundational",
                "statement": r"""A biochemist must choose between two lasers for recording the Raman spectrum of a fluorescent biological sample:
Laser 1: Frequency-doubled Nd:YAG at \(\lambda_1 = 532\text{ nm}\).
Laser 2: Near-infrared diode laser at \(\lambda_2 = 785\text{ nm}\).
(a) Calculate the ratio of the Raman scattering cross-section \(\sigma(\lambda_1) / \sigma(\lambda_2)\) based on Rayleigh's \(\nu^4 \propto 1/\lambda^4\) scattering law.
(b) Explain why the \(785\text{ nm}\) laser is nonetheless preferred for biological and polymer samples despite its lower inherent scattering efficiency.""",
                "solution": r"""<p><strong>Step (a): Scattering cross-section ratio</strong></p>
<p>The Raman scattering intensity scales as the fourth power of the excitation frequency: \(I_{\text{Raman}} \propto \nu_0^4 \propto \frac{1}{\lambda_0^4}\).</p>
\[
\frac{\sigma(\lambda_1)}{\sigma(\lambda_2)} = \left(\frac{\lambda_2}{\lambda_1}\right)^4 = \left(\frac{785\text{ nm}}{532\text{ nm}}\right)^4 = (1.47556)^4 \approx 4.74
\]
<p>The \(532\text{ nm}\) green laser produces \(\approx 4.74\) times more Raman scattering signal than the \(785\text{ nm}\) NIR laser at identical incident laser power.</p>
<p><strong>Step (b): Why 785 nm is preferred</strong></p>
<p>Biological specimens, cells, and synthetic polymers frequently contain fluorophores or trace conjugated impurities that absorb green \(532\text{ nm}\) light (\(\approx 2.33\text{ eV}\)), promoting electrons into excited states \(S_1\).</p>
<p>Because fluorescence has an emission cross-section (\(\sim 10^{-16}\text{ cm}^2\)) that is \(10^6 - 10^8\) times larger than Raman scattering (\(\sim 10^{-28}\text{ cm}^2\)), even minute fluorescence swamps the detector and obliterates the Raman spectrum beneath a massive background pedestal.</p>
<p>In contrast, the photon energy of \(785\text{ nm}\) light (\(\approx 1.58\text{ eV}\)) falls below the electronic absorption threshold of most organic chromophores. It cannot populate excited singlet states, completely suppressing fluorescence interference.</p>"""
            }
        ]
    }
    units.append(u4)

    # =========================================================================
    # UNIT 5: Electronic Spectroscopy of Atoms: Angular Momentum Coupling & Atomic Term Symbols
    # =========================================================================
    u5 = {
        "id": "unit5",
        "number": 5,
        "title": "Unit 5: Electronic Spectroscopy of Atoms: Angular Momentum Coupling & Atomic Term Symbols",
        "description": "Hydrogen atom spectrum, electronic angular momentum, spin-orbit fine structure and Lamb shift, alkali metal spectra and quantum defects, Russell-Saunders L-S vs j-j coupling schemes, atomic term symbols, Hund's rules, Landé interval rule, helium ortho/para states, normal and anomalous Zeeman effect, and Atomic Absorption Spectroscopy (AAS).",
        "simulations": [
            {
                "id": "sim_spec_atomic_term_symbols_zeeman",
                "title": "Atomic Term Symbols & Anomalous Zeeman Effect",
                "description": "Interactive 60 FPS simulator modeling atomic term symbol energy splittings, spin-orbit fine structure, and external magnetic field Zeeman splitting. Switch between the sodium doublet (2P3/2, 2P1/2 -> 2S1/2) and carbon 2p2 term configurations, adjust magnetic field B0 to observe MJ degeneracy lifting, and calculate Lande g-factors."
            }
        ],
        "sections": [
            {
                "id": "u5-sec1",
                "number": "5.1",
                "title": "The Hydrogen Atom Spectrum & One-Electron Energy Levels",
                "content": r"""<p>The quantum mechanics of the one-electron hydrogenic atom (nuclear charge \(Z\)) is governed by the Coulomb Hamiltonian \(\hat{H} = -\frac{\hbar^2}{2\mu}\nabla^2 - \frac{Z e^2}{4\pi\varepsilon_0 r}\). Solving the radial and angular Schrödinger equations yields quantized energy eigenvalues depending solely on the principal quantum number \(n\):</p>
\[
E_n = -\frac{\mu Z^2 e^4}{32 \pi^2 \varepsilon_0^2 \hbar^2} \frac{1}{n^2} = -\frac{R_H Z^2}{n^2}, \quad n = 1, 2, 3, \dots
\]
<p>where \(R_H = \frac{\mu e^4}{8 \varepsilon_0^2 h^3 c} \approx 109677.58\text{ cm}^{-1}\) is the Rydberg constant for hydrogen. Spectral transitions obey the Rydberg formula:</p>
\[
\tilde{\nu} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right)
\]
<h4 class="content-heading">Spectral Series of Hydrogen</h4>
<ul>
  <li><strong>Lyman Series (\(n_1 = 1, n_2 \ge 2\)):</strong> Ultraviolet (\(91.2 - 121.6\text{ nm}\)).</li>
  <li><strong>Balmer Series (\(n_1 = 2, n_2 \ge 3\)):</strong> Visible (\(364.6 - 656.3\text{ nm}\)), including \(H_\alpha\) at \(656.3\text{ nm}\).</li>
  <li><strong>Paschen Series (\(n_1 = 3, n_2 \ge 4\)):</strong> Infrared (\(820.4 - 1875\text{ nm}\)).</li>
  <li><strong>Brackett (\(n_1 = 4\)) & Pfund (\(n_1 = 5\)) Series:</strong> Far-infrared.</li>
</ul>
<p>In the non-relativistic Schrödinger treatment, all orbital states with identical \(n\) (\(s, p, d, f\)) are exactly degenerate, with total degeneracy \(g_n = 2n^2\) (including electron spin).</p>"""
            },
            {
                "id": "u5-sec2",
                "number": "5.2",
                "title": "Spin-Orbit Coupling & Fine Structure of Hydrogen",
                "content": r"""<p>Relativistic corrections to the hydrogen atom Hamiltonian resolve the apparent \(l\)-degeneracy into <strong>fine structure</strong>. Three relativistic perturbations contribute:</p>
<ol>
  <li><strong>Relativistic Mass Correction:</strong> Kinetic energy expansion \(T = \frac{p^2}{2m} - \frac{p^4}{8 m^3 c^2}\).</li>
  <li><strong>Darwin Term:</strong> Contact interaction of s-electrons with the nucleus due to Zitterbewegung.</li>
  <li><strong>Spin-Orbit Coupling:</strong> The electron's intrinsic magnetic spin moment \(\vec{\mu}_s = -g_e \frac{e}{2m} \vec{S}\) interacts with the internal magnetic field \(\vec{B}_{\text{int}}\) created by the relative orbital motion of the charged nucleus:
  \[
  \hat{H}_{SO} = \xi(r) \vec{L} \cdot \vec{S} = \frac{1}{2 m^2 c^2} \frac{1}{r}\frac{dV}{dr} \vec{L} \cdot \vec{S} = \frac{Z e^2}{8\pi\varepsilon_0 m^2 c^2 r^3} \vec{L} \cdot \vec{S}
  \]
  </li>
</ol>
<h4 class="content-heading">Total Angular Momentum J & Energy Splitting</h4>
<p>Total angular momentum is \(\vec{J} = \vec{L} + \vec{S}\). Squaring both sides: \(\vec{J}^2 = \vec{L}^2 + \vec{S}^2 + 2\vec{L}\cdot\vec{S}\), which gives:</p>
\[
\vec{L} \cdot \vec{S} = \frac{1}{2} (\vec{J}^2 - \vec{L}^2 - \vec{S}^2)
\]
<p>The expectation value in state \(|l, s, j\rangle\) is:</p>
\[
\langle \vec{L} \cdot \vec{S} \rangle = \frac{\hbar^2}{2} [j(j+1) - l(l+1) - s(s+1)]
\]
<p>Combining all three relativistic terms yields the famous <strong>Dirac fine structure formula</strong>:</p>
\[
E_{n, j} = E_n \left[ 1 + \frac{(Z\alpha)^2}{n} \left( \frac{1}{j + 1/2} - \frac{3}{4n} \right) \right]
\]
<p>where \(\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c} \approx \frac{1}{137.036}\) is the fine-structure constant. States with the same \(j\) (e.g., \(2s_{1/2}\) and \(2p_{1/2}\)) are degenerate in Dirac theory, but quantum electrodynamic (QED) vacuum fluctuations lift this degeneracy by \(1057.8\text{ MHz}\), known as the <strong>Lamb shift</strong>.</p>"""
            },
            {
                "id": "u5-sec3",
                "number": "5.3",
                "title": "Alkali Metal Spectra, Quantum Defects & Sodium D-Lines",
                "content": r"""<p>Alkali metal atoms (Li, Na, K, Rb, Cs) possess a single valence electron outside a closed, spherically symmetric noble gas core. Because inner core electrons partially shield the nuclear charge \(Z\), the valence electron experiences an effective nuclear charge \(Z_{\text{eff}}(r)\) that varies with distance:</p>
\[
Z_{\text{eff}} \to 1 \text{ as } r \to \infty, \quad Z_{\text{eff}} \to Z \text{ as } r \to 0
\]
<p>Electrons with low orbital angular momentum \(l\) (especially \(s\) and \(p\) orbitals) have non-zero probability density near the nucleus, penetrating the core and experiencing a higher effective charge. This penetration lowers their energy below the hydrogenic level:</p>
\[
E_{n, l} = -\frac{R_y}{(n - \delta_l)^2} = -\frac{R_y}{n_{\text{eff}}^2}
\]
<p>where \(\delta_l\) is the <strong>Rydberg quantum defect</strong>, with \(\delta_s > \delta_p > \delta_d > \delta_f \approx 0\).</p>
<h4 class="content-heading">The Sodium D-Line Doublet</h4>
<p>For sodium (\(Z = 11\)), the ground state is \(3s\), represented by term symbol \(^2S_{1/2}\). The lowest excited state is \(3p\), which is split by spin-orbit coupling into two fine-structure levels:</p>
<ul>
  <li>\(^2P_{3/2}\) (\(j = 1 + 1/2 = 3/2\)): higher energy level</li>
  <li>\(^2P_{1/2}\) (\(j = 1 - 1/2 = 1/2\)): lower energy level</li>
</ul>
<p>Electric dipole selection rules allow transitions with \(\Delta l = \pm 1, \Delta j = 0, \pm 1\). Radiative decay to the ground state produces the intense yellow doublet:</p>
\[
D_1: \quad 3p\ ^2P_{1/2} \to 3s\ ^2S_{1/2} \quad (\lambda = 589.592\text{ nm}, \tilde{\nu} = 16960.9\text{ cm}^{-1})
\]
\[
D_2: \quad 3p\ ^2P_{3/2} \to 3s\ ^2S_{1/2} \quad (\lambda = 588.995\text{ nm}, \tilde{\nu} = 16978.1\text{ cm}^{-1})
\]
<p>The fine-structure splitting is \(\Delta \tilde{\nu} = 17.2\text{ cm}^{-1}\) (\(\Delta \lambda = 0.597\text{ nm}\)). The theoretical intensity ratio is \(I(D_2) : I(D_1) = 2 : 1\), matching the statistical degeneracy ratio \((2j+1) = 4 : 2\).</p>"""
            },
            {
                "id": "u5-sec4",
                "number": "5.4",
                "title": "Russell-Saunders (L-S) Coupling & Atomic Term Symbols",
                "content": r"""<p>For light to medium-weight atoms (\(Z \lesssim 30\)), electrostatic Coulomb repulsion between electrons is substantially stronger than relativistic spin-orbit interactions. Under this regime, the system is described by the <strong>Russell-Saunders (\(L\text{-}S\)) coupling scheme</strong>:</p>
<ol>
  <li>Individual orbital angular momenta \(\vec{l}_i\) couple via electrostatic forces to form total orbital angular momentum \(\vec{L} = \sum_i \vec{l}_i\), with quantum number \(L = 0, 1, 2, 3, 4, 5 \dots\) designated as letters \(S, P, D, F, G, H \dots\).</li>
  <li>Individual spin angular momenta \(\vec{s}_i\) couple via exchange forces to form total spin angular momentum \(\vec{S} = \sum_i \vec{s}_i\), with total spin multiplicity \(2S + 1\).</li>
  <li>Total orbital \(\vec{L}\) and total spin \(\vec{S}\) couple weakly via spin-orbit interaction to yield total electronic angular momentum \(\vec{J} = \vec{L} + \vec{S}\), where:
  \[
  J = |L - S|, |L - S| + 1, \dots, L + S
  \]
  </li>
</ol>
<h4 class="content-heading">Standard Term Symbol Notation</h4>
<p>Atomic electronic states are designated by the universal <strong>term symbol</strong>:</p>
\[
^{2S+1}L_J
\]
<p>where \(2S+1\) is spin multiplicity, \(L\) is total orbital angular momentum letter, and \(J\) is total angular momentum quantum number. Each term possesses degeneracy \(g_J = 2J + 1\). The total degeneracy of an entire \(L\text{-}S\) multiplet is \((2L+1)(2S+1)\).</p>"""
            },
            {
                "id": "u5-sec5",
                "number": "5.5",
                "title": "Hund's Rules & Equivalent Electron Microstate Analysis",
                "content": r"""<p>When multiple electrons occupy equivalent orbitals (same \(n\) and \(l\)), the Pauli exclusion principle dictates that no two electrons can possess identical sets of all four quantum numbers \((n, l, m_l, m_s)\). Microstate table analysis must be employed to find the permitted terms.</p>
<h4 class="content-heading">Microstate Analysis for Carbon \(2p^2\)</h4>
<p>For the \(p^2\) configuration, there are \(\binom{6}{2} = \frac{6 \times 5}{2} = 15\) allowed microstates. Sorting these by \(M_L = \sum m_l\) and \(M_S = \sum m_s\) decomposes the configuration into three permitted terms:</p>
\[
p^2 \implies {}^1D_2\ (5\text{ states}), \quad {}^3P_{2,1,0}\ (9\text{ states}), \quad {}^1S_0\ (1\text{ state})
\]
<p>Total microstates: \(5 + 9 + 1 = 15\).</p>
<h4 class="content-heading">Hund's Rules for Ground State Terms</h4>
<p>Friedrich Hund formulated three empirical rules that uniquely identify the lowest-energy ground term:</p>
<ol>
  <li><strong>Hund's First Rule:</strong> The term with the <em>maximum spin multiplicity</em> (\(S\)) has the lowest energy, because parallel electron spins maximize the exchange stabilization and minimize interelectronic Coulomb repulsion. For \(p^2\), \(^3P\) is lower than \(^1D\) and \(^1S\).</li>
  <li><strong>Hund's Second Rule:</strong> For terms with identical multiplicity \(S\), the term with the <em>largest total orbital angular momentum</em> (\(L\)) has the lowest energy.</li>
  <li><strong>Hund's Third Rule:</strong> For subshells that are:
    <ul>
      <li><strong>Less than half-full:</strong> The level with the <em>minimum</em> \(J = |L - S|\) lies lowest (normal multiplet). For \(p^2\) (2 of 6 electrons), the ground state is \(^3P_0\).</li>
      <li><strong>More than half-full:</strong> The level with the <em>maximum</em> \(J = L + S\) lies lowest (inverted multiplet). For \(p^4\), the ground state is \(^3P_2\).</li>
      <li><strong>Exactly half-full:</strong> \(L = 0\), so \(J = S\), and there is only a single \(J\) level (e.g., \(p^3 \implies {}^4S_{3/2}\)).</li>
    </ul>
  </li>
</ol>
<h4 class="content-heading">The Landé Interval Rule</h4>
<p>The energy separation between consecutive \(J\) levels within an \(L\text{-}S\) term is proportional to the larger \(J\) value:</p>
\[
\Delta E(J, J-1) = E_J - E_{J-1} = A \cdot J
\]
<p>where \(A\) is the spin-orbit coupling constant of the term.</p>"""
            },
            {
                "id": "u5-sec6",
                "number": "5.6",
                "title": "Atomic Selection Rules & The Zeeman Effect",
                "content": r"""<p>For electric dipole transitions between atomic levels in the \(L\text{-}S\) coupling approximation, conservation of angular momentum and parity dictate the following <strong>Laporte selection rules</strong>:</p>
\[
\Delta l = \pm 1 \quad (\text{parity must change: } \text{Laporte rule})
\]
\[
\Delta L = 0, \pm 1 \quad (\text{except } L = 0 \not\to L = 0)
\]
\[
\Delta S = 0 \quad (\text{spin multiplicity cannot change})
\]
\[
\Delta J = 0, \pm 1 \quad (\text{except } J = 0 \not\to J = 0)
\]
\[
\Delta M_J = 0\ (\pi\text{-polarization, parallel to field}), \quad \Delta M_J = \pm 1\ (\sigma\text{-polarization, perpendicular})
\]
<h4 class="content-heading">The Zeeman Effect</h4>
<p>Applying an external static magnetic field \(\vec{B}_0 = B_0 \hat{z}\) interacts with the total atomic magnetic moment \(\vec{\mu} = -\frac{\mu_B}{\hbar} (\vec{L} + g_e \vec{S})\). In first-order perturbation theory, each level \(J\) splits into \(2J+1\) equally spaced magnetic sublevels:</p>
\[
\Delta E_Z = g_J \mu_B B_0 M_J
\]
<p>where \(\mu_B = \frac{e\hbar}{2m_e} = 9.27401 \times 10^{-24}\text{ J/T}\) is the Bohr magneton, and \(g_J\) is the <strong>Landé \(g\)-factor</strong>:</p>
\[
g_J = 1 + \frac{J(J+1) + S(S+1) - L(L+1)}{2J(J+1)}
\]
<ul>
  <li><strong>Normal Zeeman Effect:</strong> Occurs in singlet states (\(S = 0 \implies g_J = 1\)). Every transition splits into a symmetric triplet: an unshifted \(\pi\)-line (\(\Delta M_J = 0\)) and two \(\sigma\)-lines shifted by \(\pm \frac{\mu_B B_0}{h}\).</li>
  <li><strong>Anomalous Zeeman Effect:</strong> Occurs whenever \(S \neq 0\), causing different states to possess different \(g_J\) factors, producing complex multiplet splittings (e.g., 4 or 6 lines in the sodium D-lines).</li>
</ul>"""
            },
            {
                "id": "u5-sec7",
                "number": "5.7",
                "title": "Atomic Absorption Spectroscopy (AAS) in Chemical Analysis",
                "content": r"""<p>Atomic Absorption Spectroscopy (AAS) is an indispensable quantitative analytical technique based on the resonant absorption of optical radiation by free, unexcited ground-state gaseous atoms.</p>
<h4 class="content-heading">Instrumentation & Operating Principles</h4>
<ol>
  <li><strong>Primary Radiation Source:</strong> A <em>Hollow Cathode Lamp (HCL)</em> containing a cathode fabricated from the target element. Sputtered excited atoms emit extraordinarily narrow atomic emission lines (\(\Delta\tilde{\nu} \sim 0.01\text{ cm}^{-1}\)), matching the exact resonant absorption frequencies of the analyte atoms.</li>
  <li><strong>Atomizer:</strong>
    <ul>
      <li><em>Flame AAS (FAAS):</em> Air-acetylene (\(2300^\circ\text{C}\)) or nitrous oxide-acetylene (\(2900^\circ\text{C}\)) flame converts aerosolized liquid samples into ground-state atomic vapor. Detection limits \(\sim 10 - 100\text{ ppb}\).</li>
      <li><em>Graphite Furnace AAS (GFAAS):</em> Electrothermal heating in a graphite tube through drying, ashing, and rapid atomization steps (\(2000 - 2800^\circ\text{C}\)). Detection limits reach sub-ppb (\(\text{pg}\) masses).</li>
    </ul>
  </li>
  <li><strong>Monochromator & Detector:</strong> Isolates the specific resonant analytical wavelength and rejects broad flame background emission using photomultiplier tubes (PMT) or solid-state detectors.</li>
</ol>
<h4 class="content-heading">Quantitative Calibration & Background Correction</h4>
<p>Absorption obeys the Beer-Lambert law: \(A = \log_{10}(I_0 / I) = \varepsilon b c\). Background molecular absorption and particulate scattering are corrected using:</p>
<ul>
  <li><strong>Continuum Source (Deuterium Lamp) Correction:</strong> Alternates HCL and broad \(D_2\) pulses.</li>
  <li><strong>Zeeman Background Correction:</strong> Uses a strong magnetic field to split the atomic absorption line away from the broad background, providing the gold standard for trace metal analysis in complex biological and environmental matrices.</li>
</ul>"""
            }
        ],
        "problems": [
            {
                "id": "u5-prob1",
                "number": 1,
                "title": "Derivation of Atomic Term Symbols for Carbon Ground State",
                "difficulty": "Intermediate",
                "statement": r"""For the ground state electronic configuration of the neutral carbon atom (\(1s^2 2s^2 2p^2\)):
(a) Determine all possible Russell-Saunders term symbols \(^{2S+1}L_J\) allowed by the Pauli exclusion principle.
(b) Apply Hund's rules to determine the exact term and level of the ground state.
(c) Write all the term levels in order of increasing energy.""",
                "solution": r"""<p><strong>Step (a): Derivation of allowed terms for p²</strong></p>
<p>For two equivalent p-electrons (\(n=2, l=1\)), the total number of microstates is \(\binom{6}{2} = 15\).</p>
<p>Microstates sorted by \(M_L\) and \(M_S\):</p>
<ul>
  <li>Maximum \(M_L = 2\) with \(M_S = 0\) (both electrons in \(m_l = +1\) with opposite spins). This belongs to a singlet D term: \(^{1}D\) (\(L=2, S=0\)), consisting of \((2L+1)(2S+1) = 5 \times 1 = 5\) microstates. Since \(J = L = 2\), the term level is \(^{1}D_2\).</li>
  <li>Maximum \(M_S = 1\) with \(M_L = 1\) (electrons in \(m_l = +1, 0\) with parallel spins). This belongs to a triplet P term: \(^{3}P\) (\(L=1, S=1\)), consisting of \((2L+1)(2S+1) = 3 \times 3 = 9\) microstates. Total angular momentum values: \(J = |1-1|, 1, 1+1 = 0, 1, 2\). Term levels: \(^{3}P_0, {}^{3}P_1, {}^{3}P_2\).</li>
  <li>One remaining microstate at \(M_L = 0, M_S = 0\) forms the singlet S term: \(^{1}S\) (\(L=0, S=0\)). Term level: \(^{1}S_0\).</li>
</ul>
<p>Total microstates: \(5 ({}^{1}D_2) + 9 ({}^{3}P) + 1 ({}^{1}S_0) = 15\).</p>
<p><strong>Step (b): Application of Hund's rules</strong></p>
<ol>
  <li><strong>Hund's First Rule (Max Multiplicity):</strong> The triplet term \(^{3}P\) has \(2S+1 = 3\), which is larger than the singlets (\(2S+1 = 1\)). Therefore, \(^{3}P\) is the lowest energy term.</li>
  <li><strong>Hund's Third Rule (J value):</strong> The \(2p\) subshell has 2 electrons out of 6, which is <em>less than half-full</em>. Therefore, the state with the <em>minimum</em> \(J\) value lies lowest: \(J = |L - S| = |1 - 1| = 0\).</li>
</ol>
<p>Thus, the ground state of carbon is uniquely <strong>\(^{3}P_0\)</strong>.</p>
<p><strong>Step (c): Order of energy levels</strong></p>
<p>Within \(^{3}P\), \(J\) increases with energy (normal multiplet): \(^{3}P_0 < {}^{3}P_1 < {}^{3}P_2\). Between the remaining singlets, Hund's second rule places \(^{1}D_2\) lower than \(^{1}S_0\). The complete order is:</p>
\[
{}^{3}P_0 < {}^{3}P_1 < {}^{3}P_2 < {}^{1}D_2 < {}^{1}S_0
\]"""
            },
            {
                "id": "u5-prob2",
                "number": 2,
                "title": "Application of the Landé Interval Rule in Carbon Fine Structure",
                "difficulty": "Intermediate",
                "statement": r"""The ground configuration of atomic carbon has fine structure levels \(^{3}P_0\), \(^{3}P_1\), and \(^{3}P_2\).
Spectroscopic measurements establish that the \(^{3}P_1\) level lies \(16.4\text{ cm}^{-1}\) above \(^{3}P_0\).
(a) Using the Landé interval rule, predict the energy separation between \(^{3}P_2\) and \(^{3}P_1\).
(b) Determine the spin-orbit coupling constant \(A\) for the \(^{3}P\) term.
(c) Calculate the energy of \(^{3}P_2\) relative to the \(^{3}P_0\) ground state.""",
                "solution": r"""<p><strong>Step (a): Landé interval rule prediction</strong></p>
<p>The Landé interval rule states that the energy separation between consecutive \(J\) levels is proportional to the larger \(J\):</p>
\[
\Delta E(J, J-1) = A \cdot J
\]
<p>For the \(^{3}P\) term (\(J = 0, 1, 2\)):</p>
\[
\Delta E(1, 0) = E(^{3}P_1) - E(^{3}P_0) = A \cdot 1 = 16.4\text{ cm}^{-1}
\]
\[
\Delta E(2, 1) = E(^{3}P_2) - E(^{3}P_1) = A \cdot 2 = 2 \times 16.4\text{ cm}^{-1} = 32.8\text{ cm}^{-1}
\]
<p><strong>Step (b): Spin-orbit constant A</strong></p>
\[
A = 16.4\text{ cm}^{-1}
\]
<p><strong>Step (c): Energy of ³P₂ relative to ground state</strong></p>
\[
E(^{3}P_2) - E(^{3}P_0) = \Delta E(1, 0) + \Delta E(2, 1) = 16.4 + 32.8 = 49.2\text{ cm}^{-1}
\]
<p>Experimental measurement yields \(43.4\text{ cm}^{-1}\), showing excellent agreement with Landé interval rule scaling (deviations \(\sim 10\%\) arise from second-order spin-orbit mixing with the higher \(^{1}D_2\) state).</p>"""
            },
            {
                "id": "u5-prob3",
                "number": 3,
                "title": "Landé g-Factor and Anomalous Zeeman Splitting for Sodium D-Lines",
                "difficulty": "Advanced",
                "statement": r"""For the sodium atom transitions corresponding to the yellow D-lines (\(3p\ ^2P_{1/2} \to 3s\ ^2S_{1/2}\) and \(3p\ ^2P_{3/2} \to 3s\ ^2S_{1/2}\)):
(a) Calculate the Landé \(g\)-factor \(g_J\) for each of the three states: \(^2S_{1/2}\), \(^2P_{1/2}\), and \(^2P_{3/2}\).
(b) In an external magnetic field of \(B_0 = 1.00\text{ Tesla}\), determine the energy shift \(\Delta E\) (in \(\text{cm}^{-1}\)) for each \(M_J\) magnetic sublevel.
(c) State the number of Zeeman spectral lines observed for the \(D_1\) and \(D_2\) transitions under selection rules \(\Delta M_J = 0, \pm 1\).""",
                "solution": r"""<p><strong>Step (a): Landé g-factor calculations</strong></p>
\[
g_J = 1 + \frac{J(J+1) + S(S+1) - L(L+1)}{2J(J+1)}
\]
<ol>
  <li><strong>Ground State \(^2S_{1/2}\) (\(L=0, S=1/2, J=1/2\)):</strong>
  \[
  g_J = 1 + \frac{\frac{3}{4} + \frac{3}{4} - 0}{2(\frac{3}{4})} = 1 + \frac{1.5}{1.5} = 2
  \]
  </li>
  <li><strong>Excited State \(^2P_{1/2}\) (\(L=1, S=1/2, J=1/2\)):</strong>
  \[
  g_J = 1 + \frac{\frac{3}{4} + \frac{3}{4} - 2}{2(\frac{3}{4})} = 1 + \frac{1.5 - 2}{1.5} = 1 - \frac{0.5}{1.5} = 1 - \frac{1}{3} = \frac{2}{3}
  \]
  </li>
  <li><strong>Excited State \(^2P_{3/2}\) (\(L=1, S=1/2, J=3/2\)):</strong>
  \[
  g_J = 1 + \frac{\frac{15}{4} + \frac{3}{4} - 2}{2(\frac{15}{4})} = 1 + \frac{4.5 - 2}{7.5} = 1 + \frac{2.5}{7.5} = 1 + \frac{1}{3} = \frac{4}{3}
  \]
  </li>
</ol>
<p><strong>Step (b): Energy shift in B0 = 1.00 T</strong></p>
<p>The Zeeman energy shift is \(\Delta \tilde{\nu} = \frac{g_J \mu_B B_0 M_J}{hc}\). Note that \(\frac{\mu_B}{hc} = \frac{9.27401 \times 10^{-24}}{(6.62607 \times 10^{-34})(2.99792 \times 10^{10})} = 0.46686\text{ cm}^{-1}\text{/Tesla}\).</p>
<ul>
  <li>For \(^2S_{1/2}\) (\(g=2, M_J = \pm 1/2\)): \(\Delta \tilde{\nu} = 2(0.46686)(\pm 1/2) = \pm 0.4669\text{ cm}^{-1}\)</li>
  <li>For \(^2P_{1/2}\) (\(g=2/3, M_J = \pm 1/2\)): \(\Delta \tilde{\nu} = \frac{2}{3}(0.46686)(\pm 1/2) = \pm 0.1556\text{ cm}^{-1}\)</li>
  <li>For \(^2P_{3/2}\) (\(g=4/3, M_J = \pm 3/2, \pm 1/2\)):
    <ul>
      <li>\(M_J = \pm 3/2\): \(\Delta \tilde{\nu} = \frac{4}{3}(0.46686)(\pm 3/2) = \pm 0.9337\text{ cm}^{-1}\)</li>
      <li>\(M_J = \pm 1/2\): \(\Delta \tilde{\nu} = \frac{4}{3}(0.46686)(\pm 1/2) = \pm 0.3112\text{ cm}^{-1}\)</li>
    </ul>
  </li>
</ul>
<p><strong>Step (c): Number of Zeeman lines</strong></p>
<ul>
  <li><strong>D₁ line (\(^2P_{1/2} \to {}^2S_{1/2}\)):</strong> Transitions between 2 upper and 2 lower levels with \(\Delta M_J = 0, \pm 1\). All 4 combinations are allowed: <strong>4 Zeeman lines</strong> (2 \(\pi\)-components, 2 \(\sigma\)-components).</li>
  <li><strong>D₂ line (\(^2P_{3/2} \to {}^2S_{1/2}\)):</strong> Transitions between 4 upper and 2 lower levels. 6 transitions satisfy \(\Delta M_J = 0, \pm 1\): <strong>6 Zeeman lines</strong> (2 \(\pi\)-components, 4 \(\sigma\)-components).</li>
</ul>"""
            },
            {
                "id": "u5-prob4",
                "number": 4,
                "title": "Quantum Defect and Ionization Energy of Sodium",
                "difficulty": "Intermediate",
                "statement": r"""The first three absorption transitions from the \(3s\) ground state of sodium to higher \(p\) states are recorded at:
\(3s \to 3p\): \(\tilde{\nu} = 16960.9\text{ cm}^{-1}\)
\(3s \to 4p\): \(\tilde{\nu} = 30267.0\text{ cm}^{-1}\)
\(3s \to 5p\): \(\tilde{\nu} = 35042.8\text{ cm}^{-1}\)
Given the ionization limit of the \(3s\) electron is \(I_P = 41449.4\text{ cm}^{-1}\) and Rydberg constant \(R = 109737.3\text{ cm}^{-1}\):
(a) Determine the absolute term value \(T_n = I_P - \tilde{\nu}\) for \(3p, 4p\), and \(5p\).
(b) Calculate the Rydberg quantum defect \(\delta_p\) for each state.
(c) Explain why \(\delta_p\) remains nearly constant across principal quantum numbers \(n\).""",
                "solution": r"""<p><strong>Step (a): Absolute term values</strong></p>
\[
T(3p) = 41449.4 - 16960.9 = 24488.5\text{ cm}^{-1}
\]
\[
T(4p) = 41449.4 - 30267.0 = 11182.4\text{ cm}^{-1}
\]
\[
T(5p) = 41449.4 - 35042.8 = 6406.6\text{ cm}^{-1}
\]
<p><strong>Step (b): Quantum defect calculations</strong></p>
<p>The term value is expressed as \(T_n = \frac{R}{(n - \delta_p)^2} \implies n - \delta_p = \sqrt{\frac{R}{T_n}}\):</p>
<ul>
  <li>For \(3p\) (\(n=3\)):
  \[
  n_{\text{eff}} = \sqrt{\frac{109737.3}{24488.5}} = \sqrt{4.48118} = 2.1169 \implies \delta_p = 3 - 2.1169 = 0.8831
  \]
  </li>
  <li>For \(4p\) (\(n=4\)):
  \[
  n_{\text{eff}} = \sqrt{\frac{109737.3}{11182.4}} = \sqrt{9.81340} = 3.1326 \implies \delta_p = 4 - 3.1326 = 0.8674
  \]
  </li>
  <li>For \(5p\) (\(n=5\)):
  \[
  n_{\text{eff}} = \sqrt{\frac{109737.3}{6406.6}} = \sqrt{17.12879} = 4.1387 \implies \delta_p = 5 - 4.1387 = 0.8613
  \]
  </li>
</ul>
<p><strong>Step (c): Physical explanation of constancy</strong></p>
<p>The quantum defect \(\delta_p \approx 0.87\) is determined almost entirely by the short-range penetration of the valence electron wavepacket into the inner core (\(1s^2 2s^2 2p^6\)). Since the inner core size and charge distribution do not change when the valence electron is excited to higher Rydberg orbits, the core phase shift remains essentially constant.</p>"""
            },
            {
                "id": "u5-prob5",
                "number": 5,
                "title": "Singlet and Triplet Exchange Splitting in Helium",
                "difficulty": "Intermediate",
                "statement": r"""In neutral helium (\(1s 2s\) excited configuration):
The singlet state \(2^1S_0\) has energy \(E_{\text{singlet}} = 166277\text{ cm}^{-1}\) above the \(1s^2\) ground state.
The triplet state \(2^3S_1\) has energy \(E_{\text{triplet}} = 159856\text{ cm}^{-1}\) above the ground state.
(a) Explain the origin of this energy difference in terms of the Coulomb integral \(J_{12}\) and exchange integral \(K_{12}\).
(b) Calculate the numerical value of the exchange integral \(K_{12}\) in \(\text{cm}^{-1}\) and \(\text{kJ/mol}\).
(c) Why is the triplet state lower in energy than the singlet state?""",
                "solution": r"""<p><strong>Step (a): Coulomb and exchange integral formulation</strong></p>
<p>For two non-equivalent electrons in orbitals \(a = 1s\) and \(b = 2s\), the spatial wavefunctions are:</p>
\[
\psi_{\text{space}}^{\text{singlet}} = \frac{1}{\sqrt{2}}[\phi_a(1)\phi_b(2) + \phi_b(1)\phi_a(2)] \quad (\text{symmetric})
\]
\[
\psi_{\text{space}}^{\text{triplet}} = \frac{1}{\sqrt{2}}[\phi_a(1)\phi_b(2) - \phi_b(1)\phi_a(2)] \quad (\text{antisymmetric})
\]
<p>Evaluating the expectation value of the electron-electron Coulomb repulsion operator \(\hat{H}' = \frac{e^2}{4\pi\varepsilon_0 r_{12}}\):</p>
\[
E_{\text{singlet}} = E_0 + J_{12} + K_{12}
\]
\[
E_{\text{triplet}} = E_0 + J_{12} - K_{12}
\]
<p>where \(J_{12}\) is the direct Coulomb repulsion integral and \(K_{12}\) is the quantum exchange integral:</p>
\[
K_{12} = \iint \phi_a^*(1)\phi_b^*(2) \frac{e^2}{4\pi\varepsilon_0 r_{12}} \phi_b(1)\phi_a(2) d\tau_1 d\tau_2 > 0
\]
<p><strong>Step (b): Numerical calculation of K12</strong></p>
\[
E_{\text{singlet}} - E_{\text{triplet}} = (J_{12} + K_{12}) - (J_{12} - K_{12}) = 2 K_{12}
\]
\[
2 K_{12} = 166277 - 159856 = 6421\text{ cm}^{-1}
\]
\[
K_{12} = \frac{6421\text{ cm}^{-1}}{2} = 3210.5\text{ cm}^{-1}
\]
<p>In \(\text{kJ/mol}\):</p>
\[
K_{12} = 3210.5 \times 0.0119627 = 38.41\text{ kJ/mol}
\]
<p><strong>Step (c): Physical origin of lower triplet energy</strong></p>
<p>In the triplet state, the spatial wavefunction is antisymmetric. As \(r_1 \to r_2\), \(\psi_{\text{space}} \to 0\) (Fermi hole). The two electrons avoid each other in space, reducing electrostatic repulsion and lowering the total energy.</p>"""
            },
            {
                "id": "u5-prob6",
                "number": 6,
                "title": "Quantitative Determination of Copper by Flame Atomic Absorption",
                "difficulty": "Foundational",
                "statement": r"""A flame atomic absorption spectrometer (FAAS) is calibrated at \(\lambda = 324.7\text{ nm}\) using standard solutions of copper(II). The calibration curve yields absorbance:
\[
A = 0.0850 \times C\ (\text{ppm}) + 0.0020
\]
A \(2.500\text{ g}\) geological rock sample is dissolved in acid and diluted to \(100.0\text{ mL}\).
An aliquot of this sample solution gives an absorbance reading of \(A = 0.3845\).
(a) Determine the concentration of copper in the test solution in \(\text{ppm}\) (\(\mu\text{g/mL}\)).
(b) Calculate the total mass of copper in the sample in milligrams.
(c) Determine the copper content of the rock in weight percent (\% w/w).""",
                "solution": r"""<p><strong>Step (a): Concentration of copper in solution</strong></p>
\[
0.3845 = 0.0850 \times C + 0.0020 \implies 0.0850 \times C = 0.3825
\]
\[
C = \frac{0.3825}{0.0850} = 4.500\text{ ppm} = 4.500\ \mu\text{g/mL}
\]
<p><strong>Step (b): Mass of copper in sample</strong></p>
<p>The total volume is \(V = 100.0\text{ mL}\):</p>
\[
m_{\text{Cu}} = C \times V = (4.500\ \mu\text{g/mL})(100.0\text{ mL}) = 450.0\ \mu\text{g} = 0.4500\text{ mg}
\]
<p><strong>Step (c): Weight percent in rock</strong></p>
\[
\text{wt}\% = \frac{m_{\text{Cu}}}{m_{\text{rock}}} \times 100\% = \frac{0.4500 \times 10^{-3}\text{ g}}{2.500\text{ g}} \times 100\% = 0.0180\% = 180\text{ ppm (w/w)}
\]"""
            },
            {
                "id": "u5-prob7",
                "number": 7,
                "title": "Transition from Russell-Saunders to j-j Coupling in Group 14 Elements",
                "difficulty": "Advanced",
                "statement": r"""The ground electron configuration of the Group 14 elements is \(ns^2 np^2\).
The spin-orbit splitting between the ground state \(^3P_0\) and the first excited level \(^3P_1\) increases down the group:
Carbon (\(2p^2\)): \(\Delta E = 16.4\text{ cm}^{-1}\)
Silicon (\(3p^2\)): \(\Delta E = 77.1\text{ cm}^{-1}\)
Germanium (\(4p^2\)): \(\Delta E = 557.1\text{ cm}^{-1}\)
Tin (\(5p^2\)): \(\Delta E = 1691.8\text{ cm}^{-1}\)
Lead (\(6p^2\)): \(\Delta E = 7819.3\text{ cm}^{-1}\)
(a) Explain why spin-orbit coupling increases so dramatically down the periodic group (\(\propto Z^4\)).
(b) Describe the physical difference between Russell-Saunders (\(L\text{-}S\)) coupling and \(j\text{-}j\) coupling.
(c) For lead (\(6p^2\)), construct the term levels in the \(j\text{-}j\) coupling limit where individual electrons possess \(j_1\) and \(j_2\).""",
                "solution": r"""<p><strong>Step (a): Z^4 scaling of spin-orbit coupling</strong></p>
<p>The spin-orbit operator expectation value depends on \(\langle \frac{1}{r}\frac{dV}{dr} \rangle\). For hydrogenic Coulomb fields, \(\langle r^{-3} \rangle \propto Z^3\), and with the nuclear charge in \(dV/dr \propto Z\), the interaction scales as \(\zeta \propto Z^4\).</p>
<p>For valence electrons in heavy atoms, penetration to the inner nuclear region results in an effective \(\zeta \propto Z^2 Z_{\text{eff}}^2\), causing the massive increase from \(16.4\text{ cm}^{-1}\) (Carbon, \(Z=6\)) to \(7819\text{ cm}^{-1}\) (Lead, \(Z=82\)).</p>
<p><strong>Step (b): L-S vs j-j coupling physics</strong></p>
<ul>
  <li><strong>\(L\text{-}S\) Coupling:</strong> Electrostatic Coulomb repulsion \(\gg\) spin-orbit coupling. Orbital angular momenta couple to form \(\vec{L}\), spins couple to form \(\vec{S}\), then \(\vec{L}\) and \(\vec{S}\) couple to form \(\vec{J}\). Multiplicity \(\Delta S = 0\) is a rigorous selection rule.</li>
  <li><strong>\(j\text{-}j\) Coupling:</strong> Spin-orbit coupling \(\gg\) electrostatic Coulomb repulsion. For each individual electron, \(\vec{l}_i\) and \(\vec{s}_i\) couple strongly to form \(\vec{j}_i\). Then the individual \(\vec{j}_i\) couple weakly via residual Coulomb repulsion to form total \(\vec{J} = \sum \vec{j}_i\). Spin multiplicity \(S\) ceases to be a good quantum number, and \(\Delta S = 0\) completely breaks down.</li>
</ul>
<p><strong>Step (c): j-j coupling levels for 6p² in Lead</strong></p>
<p>For a p-electron (\(l=1, s=1/2\)), the individual \(j\) values are \(j = 3/2\) or \(j = 1/2\).</p>
<ol>
  <li><strong>\((1/2, 1/2)\) configuration:</strong> Both electrons in \(j = 1/2\). Allowed total \(J\) from anti-symmetrization: \(J = 0\) (1 state). Ground state of Pb!</li>
  <li><strong>\((3/2, 1/2)\) configuration:</strong> One electron in \(j = 3/2\), one in \(j = 1/2\). Allowed total \(J = |3/2 - 1/2|, \dots, 3/2 + 1/2 = 1, 2\) (total \(3 + 5 = 8\) states).</li>
  <li><strong>\((3/2, 3/2)\) configuration:</strong> Both electrons in \(j = 3/2\). Allowed total \(J\) from anti-symmetrization: \(J = 0, 2\) (total \(1 + 5 = 6\) states).</li>
</ol>
<p>Total states: \(1 + 8 + 6 = 15\). This reproduces the 15 states of \(p^2\), but organized by \((j_1, j_2)_J\) rather than \(^{2S+1}L_J\).</p>"""
            }
        ]
    }
    units.append(u5)

    # =========================================================================
    # UNIT 6: Molecular Electronic Spectroscopy & The Franck-Condon Principle
    # =========================================================================
    u6 = {
        "id": "unit6",
        "number": 6,
        "title": "Unit 6: Molecular Electronic Spectroscopy & The Franck-Condon Principle",
        "description": "Electronic states and term symbols of diatomic molecules, vibronic coarse structure and progression manifolds, Franck-Condon principle and vibrational overlap integrals, Birge-Sponer extrapolation to excited state dissociation limits, rotational fine structure and Fortrat parabolas, electronic spectrum of H2, chromophores and auxochromes, solvatochromism, and spectrophotometric analysis.",
        "simulations": [
            {
                "id": "sim_spec_franck_condon_vibronic",
                "title": "Franck-Condon Principle & Vibronic Envelope",
                "description": "Interactive 60 FPS simulator demonstrating the quantum mechanical Franck-Condon principle. Adjust the equilibrium bond displacement Delta R_e and force constant ratio between ground and excited electronic states to observe vertical transitions, calculate vibrational wavefunction overlap integrals |<v'|0>|^2, and view the resulting vibronic absorption envelope."
            }
        ],
        "sections": [
            {
                "id": "u6-sec1",
                "number": "6.1",
                "title": "Electronic States & Term Symbols of Diatomic Molecules",
                "content": r"""<p>In linear diatomic molecules, the spherical symmetry of atoms is broken by the cylindrical electric field along the internuclear \(z\)-axis. Consequently, the total orbital angular momentum \(\vec{L}\) is not conserved, but its projection onto the internuclear axis, \(L_z\), is quantized with quantum number \(\Lambda\):</p>
\[
L_z = M_L \hbar = \pm \Lambda \hbar, \quad \Lambda = |M_L| = 0, 1, 2, 3 \dots
\]
<p>States are labeled with Greek capital letters corresponding to \(\Lambda\):</p>
\[
\Lambda = 0 \implies \Sigma, \quad \Lambda = 1 \implies \Pi, \quad \Lambda = 2 \implies \Delta, \quad \Lambda = 3 \implies \Phi
\]
<h4 class="content-heading">Molecular Term Notation</h4>
<p>The complete molecular term symbol is formulated as:</p>
\[
^{2S+1}\Lambda_{\Omega, (g/u)}^{(\pm)}
\]
<ul>
  <li>\(2S+1\): Total spin multiplicity (singlet, doublet, triplet, etc.).</li>
  <li>\(\Omega = |\Lambda + \Sigma|\): Total electronic angular momentum projection on the internuclear axis.</li>
  <li>\(\pm\) superscript (for \(\Sigma\) states only): Reflection symmetry of the electronic spatial wavefunction through any plane containing the internuclear axis (\(+\) for symmetric, \(-\) for antisymmetric).</li>
  <li>\(g / u\) subscript (for homonuclear diatomics with an inversion center): Parity under inversion through the molecular midpoint (\(g\) for gerade/even, \(u\) for ungerade/odd).</li>
</ul>
<p>For example, the ground state of \(\text{O}_2\) is \(^3\Sigma_g^-\), \(\text{N}_2\) is \(^1\Sigma_g^+\), and \(\text{NO}\) is \(^2\Pi_{1/2}\).</p>"""
            },
            {
                "id": "u6-sec2",
                "number": "6.2",
                "title": "Vibronic Transitions & The Born-Oppenheimer Separation",
                "content": r"""<p>Because electrons are \(\sim 10^4\) times lighter than atomic nuclei, the <strong>Born-Oppenheimer approximation</strong> separates the total molecular wavefunction into electronic and nuclear components:</p>
\[
\Psi_{\text{total}}(\vec{r}, R) = \psi_{\text{el}}(\vec{r}; R) \cdot \chi_{\text{vib}}(R) \cdot \phi_{\text{rot}}(\theta, \phi)
\]
<p>The total energy of a molecular state is the sum of electronic, vibrational, and rotational contributions:</p>
\[
T = T_{\text{el}} + G(v) + F(J)
\]
<p>When an electronic transition occurs from lower state \((\text{el}'', v'', J'')\) to upper state \((\text{el}', v', J')\), the total transition wavenumber is:</p>
\[
\tilde{\nu} = (T_{\text{el}}' - T_{\text{el}}'') + [G'(v') - G''(v'')] + [F'(J') - F''(J'')] = \tilde{\nu}_{\text{el}} + \Delta G(v) + \Delta F(J)
\]
<h4 class="content-heading">Vibronic Coarse Structure</h4>
<p>Because vibrational quanta (\(500 - 3000\text{ cm}^{-1}\)) are substantially larger than rotational quanta (\(0.5 - 20\text{ cm}^{-1}\)), low-to-medium resolution electronic spectra display a coarse structure consisting of progressions of vibrational bands:</p>
<ul>
  <li><strong>\(v'\)-progression:</strong> Transitions from a fixed lower level (usually \(v'' = 0\) at room temperature) to a series of upper vibrational levels \(v' = 0, 1, 2, 3, \dots\):
  \[
  \tilde{\nu}_{v', 0} = \tilde{\nu}_{00} + G'(v') - G'(0) = \tilde{\nu}_{00} + \bar{\omega}_e' v' - \bar{\omega}_e' x_e' v'(v' + 1)
  \]
  </li>
  <li><strong>\(v''\)-progression:</strong> Transitions from a series of lower vibrational levels to a fixed upper level.</li>
</ul>"""
            },
            {
                "id": "u6-sec3",
                "number": "6.3",
                "title": "The Franck-Condon Principle: Classical Picture & Quantum Overlap",
                "content": r"""<p>The intensity distribution among the vibrational bands of an electronic transition is governed by the <strong>Franck-Condon principle</strong>:</p>
<blockquote>
  <strong>Classical Franck-Condon Principle:</strong> Because electronic transitions occur on a timescale of \(\sim 10^{-15}\text{ seconds}\), which is virtually instantaneous compared to the period of nuclear vibration (\(\sim 10^{-13}\text{ seconds}\)), the atomic nuclei do not alter their internuclear separation or momentum during the transition. Therefore, electronic transitions are represented as vertical lines on potential energy diagrams.
</blockquote>
<h4 class="content-heading">Quantum Mechanical Formulation</h4>
<p>The electric dipole transition moment operator \(\hat{\vec{\mu}} = \hat{\vec{\mu}}_e + \hat{\vec{\mu}}_N\) operates on the total wavefunction. Under the Condon approximation, the electronic dipole moment \(\vec{\mu}_{e'e''}(R) = \int \psi_{e'}^* \hat{\vec{\mu}}_e \psi_{e''} d\tau_e\) varies slowly with nuclear distance \(R\) and can be evaluated at equilibrium \(R_e\):</p>
\[
\vec{\mu}_{fi} \approx \vec{\mu}_{e'e''}(R_e) \int_{-\infty}^{\infty} \chi_{v'}^*(R) \chi_{v''}(R) dR
\]
<p>The transition probability and spectral intensity are proportional to the square of this matrix element:</p>
\[
I(v' \leftarrow v'') \propto |\vec{\mu}_{e'e''}|^2 \cdot q_{v'v''}
\]
<p>where \(q_{v'v''}\) is the <strong>Franck-Condon factor</strong>, defined as the absolute square of the vibrational overlap integral:</p>
\[
q_{v'v''} = \left| \int_{-\infty}^{\infty} \chi_{v'}^*(R) \chi_{v''}(R) dR \right|^2
\]
<p>Because vibrational eigenfunctions form a complete orthonormal basis, the sum of all Franck-Condon factors from a given initial state is strictly conserved: \(\sum_{v'} q_{v'v''} = 1\).</p>
<h4 class="content-heading">Three Regimes of Equilibrium Bond Displacement (\(\Delta R_e = R_e' - R_e''\))</h4>
<ol>
  <li><strong>Zero Displacement (\(R_e' \approx R_e''\)):</strong> The ground state wavefunction \(\chi_0''(R)\) overlaps maximally with \(\chi_0'(R)\). The \((0,0)\) transition is overwhelmingly the most intense, and higher vibronic bands decay rapidly.</li>
  <li><strong>Moderate Displacement (\(R_e' > R_e''\)):</strong> The vertical projection from \(R_e''\) intersects the turning points of higher vibrational levels \(v' = 2, 3, 4\dots\). The \((0,0)\) band is weak, and the intensity envelope peaks at \((v'_{\max}, 0)\).</li>
  <li><strong>Large Displacement (\(R_e' \gg R_e''\)):</strong> The vertical transition intersects the upper potential curve above its dissociation threshold, producing a continuous, structureless absorption continuum corresponding to direct photodissociation into free atomic fragments.</li>
</ol>"""
            },
            {
                "id": "u6-sec4",
                "number": "6.4",
                "title": "Excited State Dissociation & Birge-Sponer Extrapolations",
                "content": r"""<p>Electronic absorption spectroscopy provides the primary experimental method for measuring bond dissociation energies of molecules in both ground and excited electronic states.</p>
<h4 class="content-heading">Energetics of Dissociation Thresholds</h4>
<p>When a molecule absorbs radiation terminating at the convergence limit of a vibronic progression, the molecule dissociates into two separated atoms. Conservation of energy requires:</p>
\[
h c \tilde{\nu}_{\text{limit}} = D_0'' + \Delta E_{\text{atomic}}
\]
<p>where \(D_0''\) is the ground-state chemical dissociation energy into ground-state atoms, and \(\Delta E_{\text{atomic}}\) is the atomic excitation energy of the dissociation products.</p>
<p>For example, in molecular iodine (\(\text{I}_2\)), absorption in the visible \(B\ ^3\Pi_{0u}^+ \leftarrow X\ ^1\Sigma_g^+\) system converges at \(\lambda = 499.5\text{ nm}\) (\(\tilde{\nu}_{\text{limit}} = 20020\text{ cm}^{-1}\)). The dissociation products are one ground-state iodine atom \(^2P_{3/2}\) and one spin-orbit excited iodine atom \(^2P_{1/2}\) (\(\Delta E_{\text{atomic}} = 7603\text{ cm}^{-1}\)). The ground-state dissociation energy is obtained immediately:</p>
\[
D_0'' = 20020 - 7603 = 12417\text{ cm}^{-1} = 148.5\text{ kJ/mol}
\]"""
            },
            {
                "id": "u6-sec5",
                "number": "6.5",
                "title": "Rotational Fine Structure & Fortrat Parabolas",
                "content": r"""<p>Under ultra-high resolution, each vibrational band of an electronic transition reveals rotational fine structure governed by selection rules \(\Delta J = 0, \pm 1\). Unlike infrared transitions where \(\Delta J = 0\) is forbidden for \(\Sigma \to \Sigma\) bands, in electronic transitions with \(\Delta \Lambda \neq 0\) (e.g., \(\Sigma \to \Pi\)), a prominent <strong>Q-branch</strong> (\(\Delta J = 0\)) is observed in addition to P and R branches.</p>
<h4 class="content-heading">Fortrat Parabola Formulation</h4>
<p>The rotational transition frequencies are expressed using a continuous running variable \(m\):</p>
\[
\tilde{\nu}(m) = \tilde{\nu}_0 + (B' + B'')m + (B' - B'')m^2
\]
<p>where \(m = J'' + 1\) for the R-branch (\(m \ge 1\)), \(m = -J''\) for the P-branch (\(m \le -1\)), and for the Q-branch: \(\tilde{\nu}_Q(J) = \tilde{\nu}_0 + (B' - B'')J(J+1)\).</p>
<h4 class="content-heading">Band Head Physics</h4>
<p>Plotting \(m\) versus \(\tilde{\nu}(m)\) traces a parabola known as the <strong>Fortrat parabola</strong>. Setting \(\frac{d\tilde{\nu}}{dm} = 0\):</p>
\[
B' + B'' + 2(B' - B'')m_{\text{head}} = 0 \implies m_{\text{head}} = -\frac{B' + B''}{2(B' - B'')}
\]
<ul>
  <li>If \(B' < B''\) (equilibrium bond length expands in the excited state, \(R_e' > R_e''\), typical of antibonding transitions): \(B' - B'' < 0\), so \(m_{\text{head}} > 0\). The band head forms in the <strong>R-branch</strong>, and the band is <strong>shaded toward the red</strong> (lower wavenumbers).</li>
  <li>If \(B' > B''\) (bond contracts in the excited state, \(R_e' < R_e''\), typical of ionization of an antibonding electron): \(B' - B'' > 0\), so \(m_{\text{head}} < 0\). The band head forms in the <strong>P-branch</strong>, and the band is <strong>shaded toward the violet</strong> (higher wavenumbers).</li>
</ul>"""
            },
            {
                "id": "u6-sec6",
                "number": "6.6",
                "title": "Electronic Spectrum of Hydrogen (H2) & Ortho/Para Nuclear Statistics",
                "content": r"""<p>Molecular hydrogen (\(\text{H}_2\)) is the fundamental prototype for molecular quantum electrodynamics. Its ground electronic state is \(X\ ^1\Sigma_g^+\), arising from the electron configuration \((\sigma_g 1s)^2\). Vacuum ultraviolet excitation promotes an electron to \((\sigma_g 1s)(\sigma_u^* 1s)\), producing the \(B\ ^1\Sigma_u^+\) (Lyman bands) and \(C\ ^1\Pi_u\) (Werner bands) electronic systems.</p>
<h4 class="content-heading">Nuclear Spin Statistics in Homonuclear Diatomics</h4>
<p>Because protons are fermions with nuclear spin \(I = 1/2\), the total molecular wavefunction \(\Psi_{\text{total}} = \psi_{\text{el}} \psi_{\text{vib}} \psi_{\text{rot}} \psi_{\text{nuc}}\) must be strictly <strong>antisymmetric</strong> under permutation of the two identical nuclei:</p>
<div class="table-container">
  <table class="data-table">
    <thead>
      <tr>
        <th>Species</th>
        <th>Nuclear Spin State</th>
        <th>Nuclear Spin Degeneracy</th>
        <th>Permitted Rotational States</th>
        <th>Statistical Weight</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Para-hydrogen</strong></td>
        <td>Antisymmetric singlet (\(I_{\text{total}} = 0\))</td>
        <td>\(2(0) + 1 = 1\)</td>
        <td>Even \(J\) (\(J = 0, 2, 4, \dots\))</td>
        <td>1</td>
      </tr>
      <tr>
        <td><strong>Ortho-hydrogen</strong></td>
        <td>Symmetric triplet (\(I_{\text{total}} = 1\))</td>
        <td>\(2(1) + 1 = 3\)</td>
        <td>Odd \(J\) (\(J = 1, 3, 5, \dots\))</td>
        <td>3</td>
      </tr>
    </tbody>
  </table>
</div>
<p>Consequently, in the electronic and rotational spectra of \(\text{H}_2\), alternate rotational lines exhibit a dramatic <strong>3:1 intensity alternation</strong> (ortho:para = 3:1 at high temperatures), providing undeniable proof of the fermionic quantum nature of protons.</p>"""
            },
            {
                "id": "u6-sec7",
                "number": "6.7",
                "title": "Chromophores, Auxochromes & Solvent Solvatochromism",
                "content": r"""<p>In polyatomic organic molecules, electronic transitions in the UV-Visible range (\(200 - 800\text{ nm}\)) originate from localized molecular sub-units:</p>
<ul>
  <li><strong>Chromophore:</strong> An isolated covalent unsaturated functional group responsible for electronic absorption, primarily involving \(\pi \to \pi^*\) (e.g., \(>\text{C}=\text{C}<\), \(-\text{C}\equiv\text{C}-\), aromatic rings) or \(n \to \pi^*\) transitions (e.g., \(>\text{C}=\text{O}\), \(-\text{N}=\text{O}\), \(-\text{NO}_2\)).</li>
  <li><strong>Auxochrome:</strong> A saturated substituent with non-bonding lone pairs (e.g., \(-\text{OH}, -\text{NH}_2, -\text{OCH}_3, -\text{Cl}\)) that, when attached to a chromophore, conjugates with the \(\pi\)-system, shifting the absorption maximum to longer wavelengths (bathochromic shift) and increasing molar absorptivity (hyperchromic effect).</li>
</ul>
<h4 class="content-heading">Solvent Solvatochromism & The Lippert-Mataga Equation</h4>
<p>The solvent environment strongly modulates electronic absorption frequencies depending on the change in molecular dipole moment between ground state (\(\vec{\mu}_g\)) and excited state (\(\vec{\mu}_e\)):</p>
<ol>
  <li><strong>Positive Solvatochromism (Red/Bathochromic Shift):</strong> Occurs for \(\pi \to \pi^*\) transitions where \(\mu_e > \mu_g\). Polar solvents stabilize the more polar excited state more effectively than the ground state, reducing \(\Delta E\) and shifting absorption to lower frequencies.</li>
  <li><strong>Negative Solvatochromism (Blue/Hypsochromic Shift):</strong> Occurs for \(n \to \pi^*\) transitions where non-bonding electrons in the ground state form strong hydrogen bonds with protic solvents. The excited state has lower electron density on the heteroatom, destabilizing solvent hydrogen bonds, increasing \(\Delta E\), and shifting absorption to higher frequencies.</li>
</ol>
<p>The Stokes shift \(\Delta\tilde{\nu} = \tilde{\nu}_{\text{abs}} - \tilde{\nu}_{\text{em}}\) is quantitatively related to solvent dielectric permittivity \(\varepsilon\) and refractive index \(n\) by the <strong>Lippert-Mataga equation</strong>:</p>
\[
\Delta\tilde{\nu} = \frac{2 (\mu_e - \mu_g)^2}{h c a^3} \left[ \frac{\varepsilon - 1}{2\varepsilon + 1} - \frac{n^2 - 1}{2n^2 + 1} \right] + \text{constant}
\]
<p>where \(a\) is the Onsager cavity radius of the solute molecule.</p>"""
            }
        ],
        "problems": [
            {
                "id": "u6-prob1",
                "number": 1,
                "title": "Calculation of Franck-Condon Factors from Huang-Rhys Parameter",
                "difficulty": "Intermediate",
                "statement": r"""In a harmonic model of an electronic transition, the vibrational overlap integral between ground state \(v''=0\) and excited state \(v'\) is governed by the Poisson distribution in terms of the Huang-Rhys parameter \(S\):
\[
q_{v'0} = \frac{S^{v'}}{v'!} e^{-S}
\]
For a conjugated polyene, the equilibrium displacement corresponds to \(S = 1.40\).
(a) Calculate the Franck-Condon factors \(q_{00}, q_{10}, q_{20}, q_{30}\), and \(q_{40}\).
(b) Identify which vibronic band \((v', 0)\) will exhibit maximum absorption intensity.
(c) Verify that the sum of these first five Franck-Condon factors accounts for over \(98\%\) of the total transition intensity.""",
                "solution": r"""<p><strong>Step (a): Franck-Condon factor calculations</strong></p>
<p>With \(S = 1.40\), the exponential prefactor is \(e^{-1.40} = 0.246597\).</p>
<ul>
  <li>\(v' = 0\): \(q_{00} = \frac{1.40^0}{0!} e^{-1.40} = 1 \times 0.246597 = 0.2466\)</li>
  <li>\(v' = 1\): \(q_{10} = \frac{1.40^1}{1!} e^{-1.40} = 1.40 \times 0.246597 = 0.3452\)</li>
  <li>\(v' = 2\): \(q_{20} = \frac{1.40^2}{2!} e^{-1.40} = \frac{1.96}{2} \times 0.246597 = 0.98 \times 0.246597 = 0.2417\)</li>
  <li>\(v' = 3\): \(q_{30} = \frac{1.40^3}{6} e^{-1.40} = \frac{2.744}{6} \times 0.246597 = 0.45733 \times 0.246597 = 0.1128\)</li>
  <li>\(v' = 4\): \(q_{40} = \frac{1.40^4}{24} e^{-1.40} = \frac{3.8416}{24} \times 0.246597 = 0.16007 \times 0.246597 = 0.0395\)</li>
</ul>
<p><strong>Step (b): Maximum intensity band</strong></p>
<p>Comparing the values:</p>
\[
q_{10} = 0.3452 > q_{00} (0.2466) \approx q_{20} (0.2417) > q_{30} (0.1128) > q_{40} (0.0395)
\]
<p>The \((1, 0)\) vibronic band has the maximum absorption intensity.</p>
<p><strong>Step (c): Cumulative probability sum</strong></p>
\[
\sum_{v'=0}^4 q_{v'0} = 0.2466 + 0.3452 + 0.2417 + 0.1128 + 0.0395 = 0.9858 = 98.58\%
\]
<p>The first five vibronic bands account for \(98.6\%\) of the total transition intensity.</p>"""
            },
            {
                "id": "u6-prob2",
                "number": 2,
                "title": "Excited State Dissociation Energy of Molecular Iodine",
                "difficulty": "Intermediate",
                "statement": r"""In the absorption spectrum of molecular iodine (\(\text{I}_2\)), the \(B\ ^3\Pi_{0u}^+ \leftarrow X\ ^1\Sigma_g^+\) system originates at band origin \(\tilde{\nu}_{00} = 15769.0\text{ cm}^{-1}\).
The vibronic progression converges to a sharp dissociation limit at \(\lambda_{\text{limit}} = 499.50\text{ nm}\).
Dissociation at this limit yields one ground-state iodine atom \(\text{I}(^2P_{3/2})\) and one spin-orbit excited atom \(\text{I}^*(^2P_{1/2})\). The atomic spin-orbit excitation energy is \(\Delta E_{\text{atomic}} = 7603.2\text{ cm}^{-1}\).
The ground state zero-point energy is \(G''(0) = 107.1\text{ cm}^{-1}\), and the excited state zero-point energy is \(G'(0) = 63.8\text{ cm}^{-1}\).
(a) Calculate the wavenumber of the convergence limit \(\tilde{\nu}_{\text{limit}}\).
(b) Determine the ground-state dissociation energy \(D_0''\) and \(D_e''\) in \(\text{kJ/mol}\).
(c) Determine the excited-state dissociation energy \(D_0'\) in \(\text{kJ/mol}\).""",
                "solution": r"""<p><strong>Step (a): Convergence limit wavenumber</strong></p>
\[
\tilde{\nu}_{\text{limit}} = \frac{1}{\lambda_{\text{limit}}} = \frac{1}{499.50 \times 10^{-7}\text{ cm}} = 20020.0\text{ cm}^{-1}
\]
<p><strong>Step (b): Ground state dissociation energies D0'' and De''</strong></p>
<p>The energy of the convergence limit measured from \(v''=0\) is:</p>
\[
\tilde{\nu}_{\text{limit}} = D_0'' + \Delta E_{\text{atomic}} \implies D_0'' = \tilde{\nu}_{\text{limit}} - \Delta E_{\text{atomic}}
\]
\[
D_0'' = 20020.0 - 7603.2 = 12416.8\text{ cm}^{-1}
\]
<p>Converting to \(\text{kJ/mol}\):</p>
\[
D_0'' = 12416.8 \times 0.0119627 = 148.54\text{ kJ/mol}
\]
\[
D_e'' = D_0'' + G''(0) = 12416.8 + 107.1 = 12523.9\text{ cm}^{-1} = 149.82\text{ kJ/mol}
\]
<p><strong>Step (c): Excited state dissociation energy D0'</strong></p>
<p>The excited state dissociation energy relative to its \(v'=0\) level is:</p>
\[
D_0' = \tilde{\nu}_{\text{limit}} - \tilde{\nu}_{00} = 20020.0 - 15769.0 = 4251.0\text{ cm}^{-1}
\]
<p>Converting to \(\text{kJ/mol}\):</p>
\[
D_0' = 4251.0 \times 0.0119627 = 50.85\text{ kJ/mol}
\]"""
            },
            {
                "id": "u6-prob3",
                "number": 3,
                "title": "Fortrat Parabola and Band Head Calculation for Cyanogen Radical",
                "difficulty": "Advanced",
                "statement": r"""The violet band system (\(B\ ^2\Sigma^+ \leftarrow X\ ^2\Sigma^+\)) of the cyanogen radical (\(\text{CN}\)) has band origin \(\tilde{\nu}_0 = 25797.8\text{ cm}^{-1}\).
The rotational constants are \(B'' = 1.8911\text{ cm}^{-1}\) (ground state) and \(B' = 1.9587\text{ cm}^{-1}\) (excited state).
(a) Calculate the location \(m_{\text{head}}\) of the band head.
(b) Does the band head form in the P-branch or R-branch? Is the band shaded toward the red or violet?
(c) Calculate the wavenumber of the band head \(\tilde{\nu}_{\text{head}}\).""",
                "solution": r"""<p><strong>Step (a): Location of the band head</strong></p>
<p>The Fortrat equation is \(\tilde{\nu}(m) = \tilde{\nu}_0 + (B' + B'')m + (B' - B'')m^2\):</p>
\[
B' + B'' = 1.9587 + 1.8911 = 3.8498\text{ cm}^{-1}
\]
\[
B' - B'' = 1.9587 - 1.8911 = +0.0676\text{ cm}^{-1}
\]
<p>At the band head, \(\frac{d\tilde{\nu}}{dm} = 0\):</p>
\[
m_{\text{head}} = -\frac{B' + B''}{2(B' - B'')} = -\frac{3.8498}{2(0.0676)} = -\frac{3.8498}{0.1352} = -28.48 \approx -28 \text{ or } -29
\]
<p><strong>Step (b): Branch and shading direction</strong></p>
<p>Because \(m_{\text{head}}\) is negative (\(m \le -1\)), the band head occurs in the <strong>P-branch</strong> at rotational quantum number \(J'' = -m \approx 28\).</p>
<p>Since \(B' > B''\) (the bond contracts in the excited state, \(r_e' < r_e''\)), lines turn back toward higher wavenumbers. The band is <strong>shaded toward the violet</strong> (higher wavenumbers).</p>
<p><strong>Step (c): Band head wavenumber</strong></p>
<p>Evaluating at \(m = -28\):</p>
\[
\tilde{\nu}(-28) = 25797.8 + (3.8498)(-28) + (0.0676)(-28)^2 = 25797.8 - 107.794 + 53.00 = 25743.0\text{ cm}^{-1}
\]
<p>Evaluating at \(m = -29\):</p>
\[
\tilde{\nu}(-29) = 25797.8 + (3.8498)(-29) + (0.0676)(-29)^2 = 25797.8 - 111.644 + 56.85 = 25743.0\text{ cm}^{-1}
\]
<p>The band head forms at \(\tilde{\nu}_{\text{head}} = 25743.0\text{ cm}^{-1}\), approximately \(54.8\text{ cm}^{-1}\) below the band origin.</p>"""
            },
            {
                "id": "u6-prob4",
                "number": 4,
                "title": "Determination of Solute Excited-State Dipole Moment via Lippert-Mataga Equation",
                "difficulty": "Advanced",
                "statement": r"""A fluorescent probe molecule has an Onsager cavity radius \(a = 4.2\text{ \AA}\) and a ground-state dipole moment \(\mu_g = 3.50\text{ Debye}\).
In two non-specific solvents, the absorption and fluorescence emission maxima are measured:
1. Cyclohexane (\(\varepsilon = 2.02, n = 1.426\)): \(\tilde{\nu}_{\text{abs}} = 27800\text{ cm}^{-1}\), \(\tilde{\nu}_{\text{em}} = 24600\text{ cm}^{-1}\) (\(\Delta\tilde{\nu}_1 = 3200\text{ cm}^{-1}\)).
2. Acetonitrile (\(\varepsilon = 37.5, n = 1.344\)): \(\tilde{\nu}_{\text{abs}} = 26500\text{ cm}^{-1}\), \(\tilde{\nu}_{\text{em}} = 20900\text{ cm}^{-1}\) (\(\Delta\tilde{\nu}_2 = 5600\text{ cm}^{-1}\)).
(a) Calculate the solvent orientational polarizability function \(\Delta f = f(\varepsilon) - f(n^2) = \frac{\varepsilon - 1}{2\varepsilon + 1} - \frac{n^2 - 1}{2n^2 + 1}\) for both solvents.
(b) Using the Lippert-Mataga slope \(\frac{\Delta(\Delta\tilde{\nu})}{\Delta(\Delta f)} = \frac{2(\mu_e - \mu_g)^2}{h c a^3}\), calculate the change in dipole moment \(\Delta\mu = \mu_e - \mu_g\) in Debye.
(c) Determine the excited-state dipole moment \(\mu_e\).""",
                "solution": r"""<p><strong>Step (a): Solvent polarizability function Delta f</strong></p>
<p>For Cyclohexane (\(\varepsilon = 2.02, n = 1.426 \implies n^2 = 2.033\)):</p>
\[
f(\varepsilon) = \frac{2.02 - 1}{2(2.02) + 1} = \frac{1.02}{5.04} = 0.20238
\]
\[
f(n^2) = \frac{2.033 - 1}{2(2.033) + 1} = \frac{1.033}{5.066} = 0.20391
\]
\[
\Delta f_1 = 0.20238 - 0.20391 \approx -0.0015 \approx 0.000
\]
<p>For Acetonitrile (\(\varepsilon = 37.5, n = 1.344 \implies n^2 = 1.806\)):</p>
\[
f(\varepsilon) = \frac{37.5 - 1}{2(37.5) + 1} = \frac{36.5}{76.0} = 0.48026
\]
\[
f(n^2) = \frac{1.806 - 1}{2(1.806) + 1} = \frac{0.806}{4.612} = 0.17476
\]
\[
\Delta f_2 = 0.48026 - 0.17476 = 0.3055
\]
<p>Difference in \(\Delta f\):</p>
\[
\Delta(\Delta f) = 0.3055 - (-0.0015) = 0.3070
\]
<p>Difference in Stokes shift:</p>
\[
\Delta(\Delta\tilde{\nu}) = 5600 - 3200 = 2400\text{ cm}^{-1}
\]
<p><strong>Step (b): Calculation of dipole moment change</strong></p>
\[
\text{Slope} = \frac{2400\text{ cm}^{-1}}{0.3070} = 7817.6\text{ cm}^{-1} = \frac{2(\mu_e - \mu_g)^2}{h c a^3}
\]
<p>In SI units:</p>
<ul>
  <li>\(h c = (6.62607 \times 10^{-34})(2.99792 \times 10^{10}) = 1.98645 \times 10^{-23}\text{ J}\cdot\text{cm}\)</li>
  <li>\(a = 4.2 \times 10^{-8}\text{ cm} \implies a^3 = 7.4088 \times 10^{-23}\text{ cm}^3\)</li>
  <li>\(h c a^3 = (1.98645 \times 10^{-23})(7.4088 \times 10^{-23}) = 1.47172 \times 10^{-45}\text{ J}\cdot\text{cm}^4\)</li>
</ul>
\[
(\mu_e - \mu_g)^2 = \frac{7817.6 \times (1.47172 \times 10^{-45})}{2} = 5.7526 \times 10^{-42}\text{ J}\cdot\text{cm}^3 = 5.7526 \times 10^{-48}\text{ J}\cdot\text{m}^3
\]
<p>Since \(1\text{ J}\cdot\text{m}^3 = 1\text{ C}^2\cdot\text{m}^2 / (\text{F/m})\), we express directly in Debye (\(1\text{ D} = 3.33564 \times 10^{-30}\text{ C}\cdot\text{m}\)):</p>
\[
\mu_e - \mu_g = 6.42\text{ Debye}
\]
<p><strong>Step (c): Excited-state dipole moment</strong></p>
\[
\mu_e = \mu_g + \Delta\mu = 3.50 + 6.42 = 9.92\text{ Debye}
\]
<p>The large increase in dipole moment (\(3.5\text{ D} \to 9.9\text{ D}\)) demonstrates massive intramolecular charge transfer upon photoexcitation.</p>"""
            },
            {
                "id": "u6-prob5",
                "number": 5,
                "title": "Two-Component Spectrophotometric Analysis and Isosbestic Points",
                "difficulty": "Intermediate",
                "statement": r"""A mixture of two interconverting tautomers (species X and species Y) is analyzed by UV-Vis spectrophotometry in a \(1.00\text{ cm}\) quartz cuvette.
Pure component molar absorptivities (\(\varepsilon\) in \(\text{L}/(\text{mol}\cdot\text{cm})\)) are:
At \(\lambda_1 = 300\text{ nm}\): \(\varepsilon_{X1} = 8500\), \(\varepsilon_{Y1} = 1500\).
At \(\lambda_2 = 420\text{ nm}\): \(\varepsilon_{X2} = 1200\), \(\varepsilon_{Y2} = 9200\).
At \(\lambda_{\text{iso}} = 350\text{ nm}\), both species have identical molar absorptivity: \(\varepsilon_{\text{iso}} = 4500\).
An equilibrium mixture has absorbance \(A_1 = 0.430\) at \(300\text{ nm}\) and \(A_2 = 0.584\) at \(420\text{ nm}\).
(a) Set up the simultaneous equations and solve for the concentrations of X and Y.
(b) Calculate the predicted absorbance at the isosbestic wavelength \(\lambda_{\text{iso}} = 350\text{ nm}\).
(c) Explain why the absorbance at an isosbestic point remains strictly constant regardless of the equilibrium ratio between X and Y as long as total concentration is conserved.""",
                "solution": r"""<p><strong>Step (a): Simultaneous equations for concentrations</strong></p>
<p>According to the additivity of Beer-Lambert absorbance:</p>
\[
A_1 = \varepsilon_{X1} b [X] + \varepsilon_{Y1} b [Y] \implies 0.430 = 8500 [X] + 1500 [Y] \quad \text{(Equation 1)}
\]
\[
A_2 = \varepsilon_{X2} b [X] + \varepsilon_{Y2} b [Y] \implies 0.584 = 1200 [X] + 9200 [Y] \quad \text{(Equation 2)}
\]
<p>From Equation 1:</p>
\[
1500 [Y] = 0.430 - 8500 [X] \implies [Y] = \frac{0.430 - 8500 [X]}{1500} = 2.8667 \times 10^{-4} - 5.6667 [X]
\]
<p>Substitute into Equation 2:</p>
\[
0.584 = 1200 [X] + 9200(2.8667 \times 10^{-4} - 5.6667 [X])
\]
\[
0.584 = 1200 [X] + 2.6373 - 52133 [X]
\]
\[
50933 [X] = 2.6373 - 0.584 = 2.0533 \implies [X] = \frac{2.0533}{50933} = 4.031 \times 10^{-5}\text{ M}
\]
<p>Now determine \([Y]\):</p>
\[
[Y] = \frac{0.430 - 8500(4.031 \times 10^{-5})}{1500} = \frac{0.430 - 0.3426}{1500} = \frac{0.0874}{1500} = 5.827 \times 10^{-5}\text{ M}
\]
<p>Total concentration: \(C_{\text{total}} = [X] + [Y] = (4.031 + 5.827) \times 10^{-5} = 9.858 \times 10^{-5}\text{ M}\).</p>
<p><strong>Step (b): Absorbance at the isosbestic point</strong></p>
\[
A_{\text{iso}} = \varepsilon_{\text{iso}} b ([X] + [Y]) = 4500 \times 1.00 \times (9.858 \times 10^{-5}) = 0.4436
\]
<p><strong>Step (c): Invariance of isosbestic point</strong></p>
<p>At \(\lambda_{\text{iso}}\), \(\varepsilon_X = \varepsilon_Y = \varepsilon_{\text{iso}}\):</p>
\[
A_{\text{iso}} = \varepsilon_X b [X] + \varepsilon_Y b [Y] = \varepsilon_{\text{iso}} b ([X] + [Y]) = \varepsilon_{\text{iso}} b C_{\text{total}}
\]
<p>As long as the two species interconvert with a 1:1 stoichiometry without forming third-party intermediates, \(C_{\text{total}}\) is constant. Therefore, all spectral curves cross at the exact same point, providing definitive proof of a binary equilibrium.</p>"""
            },
            {
                "id": "u6-prob6",
                "number": 6,
                "title": "Ortho and Para Nuclear Spin Statistics of Molecular Hydrogen",
                "difficulty": "Foundational",
                "statement": r"""In the electronic-rotational spectrum of \(\text{H}_2\) gas at room temperature (\(T = 300\text{ K}\)):
(a) State the nuclear spin \(I\) of the proton and write the four nuclear spin functions for \(\text{H}_2\).
(b) Explain why para-hydrogen can only occupy even \(J\) rotational levels (\(J = 0, 2, 4\dots\)) while ortho-hydrogen can only occupy odd \(J\) levels (\(J = 1, 3, 5\dots\)).
(c) Calculate the theoretical intensity ratio between the \(R(0)\) line (from para-\(\text{H}_2\), \(J=0\)) and \(R(1)\) line (from ortho-\(\text{H}_2\), \(J=1\)) at \(300\text{ K}\), given rotational constant \(B = 60.85\text{ cm}^{-1}\).""",
                "solution": r"""<p><strong>Step (a): Proton nuclear spin functions</strong></p>
<p>Protons have \(I = 1/2\). Two protons form \(2 \times 2 = 4\) nuclear spin combinations:</p>
<ul>
  <li>Three symmetric triplet states (ortho-\(\text{H}_2\), \(I_{\text{tot}} = 1\)):
  \[
  |\alpha\alpha\rangle, \quad \frac{1}{\sqrt{2}}(|\alpha\beta\rangle + |\beta\alpha\rangle), \quad |\beta\beta\rangle
  \]
  </li>
  <li>One antisymmetric singlet state (para-\(\text{H}_2\), \(I_{\text{tot}} = 0\)):
  \[
  \frac{1}{\sqrt{2}}(|\alpha\beta\rangle - |\beta\alpha\rangle)
  \]
  </li>
</ul>
<p><strong>Step (b): Nuclear symmetry requirement</strong></p>
<p>The Pauli principle requires the total wavefunction \(\Psi_{\text{tot}} = \psi_{\text{el}} \psi_{\text{vib}} \psi_{\text{rot}} \psi_{\text{nuc}}\) to be antisymmetric under nuclear exchange. In the ground state (\(^1\Sigma_g^+\), \(v=0\)), \(\psi_{\text{el}}\) and \(\psi_{\text{vib}}\) are symmetric.</p>
<p>Rotational wavefunctions have parity \((-1)^J\): symmetric for even \(J\), antisymmetric for odd \(J\). Therefore:</p>
<ul>
  <li>Para-\(\text{H}_2\) has antisymmetric \(\psi_{\text{nuc}}\), requiring symmetric \(\psi_{\text{rot}}\) \(\implies\) <strong>even \(J\)</strong> (\(J=0, 2, 4\dots\)).</li>
  <li>Ortho-\(\text{H}_2\) has symmetric \(\psi_{\text{nuc}}\), requiring antisymmetric \(\psi_{\text{rot}}\) \(\implies\) <strong>odd \(J\)</strong> (\(J=1, 3, 5\dots\)).</li>
</ul>
<p><strong>Step (c): Intensity ratio R(1) / R(0) at 300 K</strong></p>
<p>The intensity is proportional to population \(N_J = g_{\text{nuc}} (2J+1) e^{-hcB J(J+1) / k_B T}\):</p>
<p>At \(300\text{ K}\), \(k_B T / hc = 208.51\text{ cm}^{-1}\).</p>
<ul>
  <li>For \(J = 0\) (para): \(g_{\text{nuc}} = 1\), \(g_{\text{rot}} = 1\), \(E_0 = 0 \implies N_0 = 1 \times 1 \times 1 = 1.000\).</li>
  <li>For \(J = 1\) (ortho): \(g_{\text{nuc}} = 3\), \(g_{\text{rot}} = 2(1)+1 = 3\), \(E_1 = 2B = 121.7\text{ cm}^{-1}\):
  \[
  e^{-121.7 / 208.51} = e^{-0.5837} = 0.5578
  \]
  \[
  N_1 = 3 \times 3 \times 0.5578 = 5.020
  \]
  </li>
</ul>
<p>The intensity ratio is:</p>
\[
\frac{I(R(1))}{I(R(0))} \approx \frac{N_1}{N_0} = \frac{5.020}{1.000} = 5.02
\]
<p>The \(R(1)\) line is five times more intense than \(R(0)\) due to the combined ortho spin statistical weight (3:1) and rotational degeneracy.</p>"""
            },
            {
                "id": "u6-prob7",
                "number": 7,
                "title": "Woodward-Fieser Rules for Conjugated Dienes",
                "difficulty": "Foundational",
                "statement": r"""Predict the maximum UV absorption wavelength \(\lambda_{\max}\) for the following organic compounds using the Woodward-Fieser rules:
(a) Cholesta-3,5-diene (a heteroannular conjugated diene with three ring residues).
(b) 1,3-Cyclohexadiene (a homoannular conjugated diene).
(c) 3-Methyl-penta-1,3-diene (an acyclic diene with two alkyl substituents).
Compare the predictions with experimental values (\(\approx 235\text{ nm}, 256\text{ nm}\), and \(227\text{ nm}\)).""",
                "solution": r"""<p><strong>Compound (a): Cholesta-3,5-diene</strong></p>
<ul>
  <li>Base value for heteroannular (transoid) diene: \(214\text{ nm}\)</li>
  <li>Ring residues: 3 ring residues attached to conjugated carbons (\(3 \times 5\text{ nm}\)): \(+15\text{ nm}\)</li>
  <li>Exocyclic double bond: 1 exocyclic double bond to Ring A: \(+5\text{ nm}\)</li>
</ul>
\[
\lambda_{\max} = 214 + 15 + 5 = 234\text{ nm} \quad (\text{Observed: } 235\text{ nm})
\]
<p><strong>Compound (b): 1,3-Cyclohexadiene</strong></p>
<ul>
  <li>Base value for homoannular (cisoid) diene: \(253\text{ nm}\)</li>
  <li>Ring residues: 2 ring residues (\(2 \times 5\text{ nm}\)): \(+10\text{ nm}\)</li>
</ul>
\[
\lambda_{\max} = 253 + 10 = 263\text{ nm} \quad (\text{Observed: } 256\text{ nm})
\]
<p><strong>Compound (c): 3-Methyl-penta-1,3-diene</strong></p>
<ul>
  <li>Base value for acyclic butadiene system: \(217\text{ nm}\)</li>
  <li>Alkyl substituents: 2 (one methyl at C3, one methyl at C5) (\(2 \times 5\text{ nm}\)): \(+10\text{ nm}\)</li>
</ul>
\[
\lambda_{\max} = 217 + 10 = 227\text{ nm} \quad (\text{Observed: } 227\text{ nm})
\]
<p>The Woodward-Fieser empirical rules accurately predict \(\pi \to \pi^*\) absorption band maxima within \(\pm 2 - 5\text{ nm}\).</p>"""
            }
        ]
    }
    units.append(u6)

    return units

if __name__ == "__main__":
    units = get_units_4_5_6()
    print(f"Successfully generated Units 4-6. Total units: {len(units)}")
    for u in units:
        print(f"Unit {u['number']}: {len(u['sections'])} sections, {len(u['problems'])} problems.")
