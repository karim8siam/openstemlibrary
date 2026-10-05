import json

# ==========================================
# UNIT 3: Lattice Vibrations, Phonons & Thermal Properties
# ==========================================
u3 = {
    "unitNumber": 3,
    "unitId": "unit3-lattice-vibrations",
    "title": "Lattice Vibrations, Phonons & Thermal Properties",
    "description": "Rigorous classical and quantum theory of lattice dynamics: monatomic and diatomic 1D chain dispersion relations, acoustic and optical phonon branches, Brillouin zone boundaries, normal modes, inelastic neutron scattering, Einstein and Debye specific heat models, anharmonic lattice expansion, thermal conductivity, and Normal vs Umklapp phonon scattering processes.",
    "sections": [
        {
            "id": "ssp-3-1",
            "title": "Vibrations of a Monatomic 1D Lattice & Acoustic Dispersion",
            "simulation": "ssp-phonon-dispersion-sim",
            "content": r"""<h4>1. Equation of Motion for a Linear Monatomic Chain</h4>
<p>Consider an infinite one-dimensional lattice of identical atoms, each of mass $M$, separated at equilibrium by lattice spacing $a$. Let $u_n(t)$ denote the displacement of the $n$-th atom from its equilibrium position $x_n = n a$. Under the <em>harmonic approximation</em>, the restoring force on atom $n$ arises from Hooke's law interactions with its nearest neighbors $n-1$ and $n+1$ with spring constant $C$:</p>
<div class="math-display">
$$M \frac{d^2 u_n}{dt^2} = C (u_{n+1} - u_n) - C (u_n - u_{n-1}) = C (u_{n+1} + u_{n-1} - 2u_n)$$
</div>

<h4>2. Derivation of the Phonon Dispersion Relation $\omega(k)$</h4>
<p>Seeking traveling plane-wave normal-mode solutions of the form $u_n(t) = A e^{i(k n a - \omega t)}$, where $k$ is the wavevector and $\omega$ is the angular frequency:</p>
<div class="math-display">
$$- M \omega^2 A e^{i(k n a - \omega t)} = C A e^{i(k n a - \omega t)} \left[ e^{i k a} + e^{- i k a} - 2 \right]$$
</div>
<p>Dividing through by $A e^{i(k n a - \omega t)}$ and recalling Euler's identity $e^{i k a} + e^{-i k a} = 2\cos(k a)$:</p>
<div class="math-display">
$$- M \omega^2 = 2C [\cos(k a) - 1] = - 4C \sin^2\left(\frac{k a}{2}\right)$$
</div>
<p>Taking the positive square root yields the <strong>acoustic dispersion relation</strong> for the monatomic chain:</p>
<div class="math-display">
$$\omega(k) = 2 \sqrt{\frac{C}{M}} \left| \sin\left(\frac{k a}{2}\right) \right|$$
</div>

<h4>3. Long-Wavelength Limit and Brillouin Zone Boundary</h4>
<ul>
<li><strong>Long-Wavelength (Continuum / Acoustic) Limit ($k a \ll 1$):</strong>
<p>As $k \to 0$, $\sin(k a / 2) \approx k a / 2$, which gives a linear dispersion relation:</p>
<div class="math-display">
$$\omega \approx 2 \sqrt{\frac{C}{M}} \left(\frac{k a}{2}\right) = a \sqrt{\frac{C}{M}} k = v_s k$$
</div>
<p>where $v_s = a \sqrt{C/M}$ is the macroscopic <strong>sound velocity</strong> in the crystal. In this limit, the group velocity equals the phase velocity: $v_g = d\omega/dk = v_s = v_p = \omega/k$.</p></li>
<li><strong>First Brillouin Zone Boundary ($k = \pm \pi / a$):</strong>
<p>At the edge of the first Brillouin zone, $\sin(\pi / 2) = 1$, yielding the maximum cut-off angular frequency:</p>
<div class="math-display">
$$\omega_{\text{max}} = 2 \sqrt{\frac{C}{M}}$$
</div>
<p>The group velocity vanishes at the zone boundary: $\left. v_g \right|_{k = \pi/a} = \left. \frac{d\omega}{dk} \right|_{\pi/a} = a \sqrt{\frac{C}{M}} \cos\left(\frac{\pi}{2}\right) = 0$. The wave becomes a <em>standing wave</em> with adjacent atoms oscillating in exact antiphase: $u_{n+1}/u_n = e^{i\pi} = -1$.</p></li>
</ul>"""
        },
        {
            "id": "ssp-3-2",
            "title": "Vibrations of a Diatomic 1D Lattice: Acoustic & Optical Branches",
            "content": r"""<h4>1. Coupled Equations of Motion for a Diatomic Chain</h4>
<p>Consider a 1D lattice with a two-atom basis: alternating masses $M_1$ and $M_2$ ($M_1 > M_2$) connected by identical nearest-neighbor springs of force constant $C$ with unit cell dimension $a$ (interatomic separation $a/2$). Let $u_n(t)$ denote the displacement of mass $M_1$ in unit cell $n$, and $v_n(t)$ denote the displacement of mass $M_2$ in unit cell $n$:</p>
<div class="math-display">
$$M_1 \frac{d^2 u_n}{dt^2} = C (v_n + v_{n-1} - 2 u_n), \quad M_2 \frac{d^2 v_n}{dt^2} = C (u_{n+1} + u_n - 2 v_n)$$
</div>

<h4>2. Secular Determinant & Two Frequency Branches</h4>
<p>Substituting harmonic normal-mode trial solutions $u_n = A e^{i(k n a - \omega t)}$ and $v_n = B e^{i(k n a - \omega t)}$ yields the linear algebraic system:</p>
<div class="math-display">
$$\begin{pmatrix} 2C - M_1 \omega^2 & - C (1 + e^{-i k a}) \\ - C (1 + e^{i k a}) & 2C - M_2 \omega^2 \end{pmatrix} \begin{pmatrix} A \\ B \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
</div>
<p>For non-trivial solutions, the secular determinant must vanish:</p>
<div class="math-display">
$$(2C - M_1 \omega^2)(2C - M_2 \omega^2) - C^2 |1 + e^{i k a}|^2 = 0 \implies M_1 M_2 \omega^4 - 2C(M_1 + M_2)\omega^2 + 4C^2 \sin^2\left(\frac{k a}{2}\right) = 0$$
</div>
<p>Solving the quadratic equation in $\omega^2$ yields two distinct branches:</p>
<div class="math-display">
$$\omega^2(k) = C \left( \frac{1}{M_1} + \frac{1}{M_2} \right) \pm C \sqrt{\left(\frac{1}{M_1} + \frac{1}{M_2}\right)^2 - \frac{4 \sin^2(k a / 2)}{M_1 M_2}}$$
</div>

<h4>3. Physical Significance of Acoustic and Optical Branches</h4>
<ul>
<li><strong>Acoustic Branch (Minus Sign):</strong>
<p>As $k \to 0$, $\omega_{\text{ac}} \to 0$. In this limit, $A/B \to +1$: both masses in each unit cell oscillate in phase with identical amplitudes and directions, representing long-wavelength sound waves.</p></li>
<li><strong>Optical Branch (Plus Sign):</strong>
<p>At $k = 0$, $\omega_{\text{opt}}(0) = \sqrt{2C \left(\frac{1}{M_1} + \frac{1}{M_2}\right)} = \sqrt{\frac{2C}{\mu}}$, where $\mu$ is the reduced mass. In this limit, $M_1 A + M_2 B = 0 \implies A/B = - M_2 / M_1$: the center of mass of the unit cell remains stationary while adjacent opposite ions oscillate in antiphase against each other. In ionic crystals, this creates an oscillating electric dipole moment that couples strongly to electromagnetic light waves (infrared absorption), hence the name <em>optical branch</em>.</p></li>
<li><strong>Forbidden Band Gap at Brillouin Zone Boundary ($k = \pm \pi / a$):</strong>
<p>At $k = \pi / a$, $\sin^2(k a / 2) = 1$, yielding two discrete frequencies:</p>
<div class="math-display">
$$\omega_{\text{opt}}\left(\frac{\pi}{a}\right) = \sqrt{\frac{2C}{M_2}}, \quad \omega_{\text{ac}}\left(\frac{\pi}{a}\right) = \sqrt{\frac{2C}{M_1}}$$
</div>
<p>Between $\sqrt{2C/M_1}$ and $\sqrt{2C/M_2}$, no real solution for $k$ exists. This frequency interval is a <strong>forbidden phononic band gap</strong> where lattice waves cannot propagate and are exponentially attenuated.</p></li>
</ul>"""
        },
        {
            "id": "ssp-3-3",
            "title": "The Phonon Concept, Normal Modes & Inelastic Neutron Scattering",
            "content": r"""<h4>1. Quantum Mechanics of Lattice Vibrations: Phonons</h4>
<p>When the classical harmonic Hamiltonian of $N$ coupled lattice oscillators is transformed into normal coordinates $q_{\vec{k}, s}$ and canonically quantized, it decouples into a sum of $3N$ independent quantum harmonic oscillators:</p>
<div class="math-display">
$$\hat{H} = \sum_{\vec{k}, s} \hbar \omega_s(\vec{k}) \left( \hat{a}_{\vec{k},s}^\dagger \hat{a}_{\vec{k},s} + \frac{1}{2} \right)$$
</div>
<p>where $\hat{a}_{\vec{k},s}^\dagger$ and $\hat{a}_{\vec{k},s}$ are creation and annihilation operators. A quantum of lattice vibrational energy is called a <strong>phonon</strong>, carrying energy $\hbar \omega_s(\vec{k})$.</p>
<p>Because phonons are indistinguishable bosons with zero chemical potential ($\mu = 0$), their thermal equilibrium occupation number at temperature $T$ is governed strictly by the <strong>Planck distribution</strong>:</p>
<div class="math-display">
$$\langle n_{\vec{k},s} \rangle = \frac{1}{e^{\hbar \omega_s(\vec{k}) / k_B T} - 1}$$
</div>

<h4>2. Phonon Crystal Momentum $\hbar \vec{q}$</h4>
<p>A phonon carries wavevector $\vec{q}$ and a quantity $\hbar \vec{q}$ known as <strong>crystal momentum</strong>. Unlike physical momentum (the center of mass of the whole crystal does not move during internal vibrations), crystal momentum is conserved only modulo a reciprocal lattice vector $\vec{G}$:</p>
<div class="math-display">
$$\sum \vec{k}_{\text{initial}} = \sum \vec{k}_{\text{final}} + \vec{G}$$
</div>

<h4>3. Inelastic Neutron Scattering</h4>
<p>The experimental dispersion relation $\omega(\vec{q})$ across the entire Brillouin zone is determined by <strong>Inelastic Neutron Scattering (INS)</strong>. Thermal neutrons with mass $M_n \approx 1.675 \times 10^{-27}\text{ kg}$ have de Broglie wavelengths comparable to lattice spacings ($\lambda \sim 1 - 2\text{ \AA}$) and kinetic energies comparable to phonon energies ($E \sim 10 - 100\text{ meV}$):</p>
<ul>
<li><strong>Energy Conservation:</strong> $E' - E = \frac{\hbar^2 k'^2}{2M_n} - \frac{\hbar^2 k^2}{2M_n} = \pm \hbar \omega(\vec{q})$ ($+$ for phonon emission, $-$ for phonon absorption).</li>
<li><strong>Crystal Momentum Conservation:</strong> $\vec{k}' - \vec{k} = \mp \vec{q} + \vec{G}$.</li>
</ul>
<p>By measuring the scattered neutron angle and energy, both $\omega$ and $\vec{q}$ are mapped simultaneously.</p>"""
        },
        {
            "id": "ssp-3-4",
            "title": "Theories of Lattice Specific Heat: Einstein & Debye Models",
            "simulation": "ssp-debye-specific-heat-sim",
            "content": r"""<h4>1. Classical Dulong-Petit Law & Quantum Failure</h4>
<p>By the classical equipartition theorem, each of the $3N$ vibrational degrees of freedom in a 3D crystal of $N$ atoms possesses an average thermal energy of $k_B T$, yielding total internal energy $U = 3 N k_B T$. The molar lattice heat capacity at constant volume is the constant <strong>Dulong-Petit value</strong>:</p>
<div class="math-display">
$$C_V = \left(\frac{\partial U}{\partial T}\right)_V = 3 N_A k_B = 3 R \approx 24.94\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$$
</div>
<p>Experimentally, as $T \to 0\text{ K}$, $C_V$ vanishes rapidly, violating classical theory.</p>

<h4>2. The Einstein Specific Heat Model</h4>
<p>Einstein (1907) assumed that all $3N$ normal modes oscillate independently with the <em>same identical frequency</em> $\omega_E$ (characteristic Einstein temperature $\Theta_E = \hbar\omega_E / k_B$):</p>
<div class="math-display">
$$U = 3N \left( \frac{\hbar\omega_E}{e^{\hbar\omega_E / k_B T} - 1} + \frac{1}{2}\hbar\omega_E \right) \implies C_V = 3 N k_B \left(\frac{\Theta_E}{T}\right)^2 \frac{e^{\Theta_E / T}}{\left(e^{\Theta_E / T} - 1\right)^2}$$
</div>
<ul>
<li><strong>High-Temperature Limit ($T \gg \Theta_E$):</strong> $C_V \to 3 N k_B$ (recovers Dulong-Petit).</li>
<li><strong>Low-Temperature Limit ($T \ll \Theta_E$):</strong> $C_V \approx 3 N k_B (\Theta_E / T)^2 e^{-\Theta_E / T}$. While this vanishes at $T = 0$, the exponential drop is much steeper than experimental data, which follows a power law.</li>
</ul>

<h4>3. The Debye Model & The $T^3$ Law</h4>
<p>Debye (1912) treated the crystal as an elastic isotropic continuum with linear acoustic dispersion $\omega = v_s k$ across all three acoustic polarizations ($1$ longitudinal, $2$ transverse). The phonon density of states in 3D is:</p>
<div class="math-display">
$$g(\omega) d\omega = \frac{V}{2\pi^2} \left( \frac{1}{v_L^3} + \frac{2}{v_T^3} \right) \omega^2 d\omega = \frac{3V}{2\pi^2 v_s^3} \omega^2 d\omega$$
</div>
<p>Debye imposed a high-frequency cut-off, the <strong>Debye cut-off frequency</strong> $\omega_D$, to ensure the total number of modes equals $3N$:</p>
<div class="math-display">
$$\int_0^{\omega_D} g(\omega) d\omega = 3N \implies \omega_D = v_s \left( \frac{6\pi^2 N}{V} \right)^{1/3}, \quad \Theta_D = \frac{\hbar \omega_D}{k_B}$$
</div>
<p>The total thermal vibrational internal energy is:</p>
<div class="math-display">
$$U = \int_0^{\omega_D} \frac{\hbar\omega}{e^{\hbar\omega/k_BT} - 1} g(\omega) d\omega = 9 N k_B T \left(\frac{T}{\Theta_D}\right)^3 \int_0^{\Theta_D/T} \frac{x^3}{e^x - 1} dx \quad \left(x = \frac{\hbar\omega}{k_BT}\right)$$
</div>
<p>Differentiating with respect to $T$ in the low-temperature limit ($T \ll \Theta_D$), the upper limit goes to infinity: $\int_0^\infty \frac{x^3}{e^x - 1} dx = \frac{\pi^4}{15}$. This yields the celebrated <strong>Debye $T^3$ Law</strong>:</p>
<div class="math-display">
$$C_V = \frac{12\pi^4}{5} N k_B \left( \frac{T}{\Theta_D} \right)^3 \propto T^3 \quad (T \to 0\text{ K})$$
</div>
<p>This matches experimental specific heat measurements for all non-magnetic insulating solids.</p>"""
        },
        {
            "id": "ssp-3-5",
            "title": "Anharmonicity, Thermal Expansion & Normal vs Umklapp Processes",
            "content": r"""<h4>1. Anharmonic Effects & Thermal Expansion</h4>
<p>In a purely harmonic potential $V(x) = \frac{1}{2} c x^2$, the potential well is symmetric about $x = 0$. The thermal average displacement vanishes at all temperatures: $\langle x \rangle = \frac{\int x e^{-V(x)/k_BT} dx}{\int e^{-V(x)/k_BT} dx} = 0$, implying zero thermal expansion. Thermal expansion is an intrinsically <em>anharmonic</em> phenomenon.</p>
<p>Expanding the interatomic potential including cubic ($g x^3$) and quartic ($f x^4$) anharmonic perturbations:</p>
<div class="math-display">
$$V(x) = c x^2 - g x^3 - f x^4$$
</div>
<p>Calculating the thermal average position using the Boltzmann distribution yields:</p>
<div class="math-display">
$$\langle x \rangle = \frac{\int_{-\infty}^{\infty} x e^{-\beta(cx^2 - gx^3 - fx^4)} dx}{\int_{-\infty}^{\infty} e^{-\beta(cx^2 - gx^3 - fx^4)} dx} \approx \frac{3g}{4c^2} k_B T$$
</div>
<p>The linear thermal expansion coefficient $\alpha_{\text{th}} = \frac{1}{a} \frac{d\langle x \rangle}{dT} = \frac{3g k_B}{4c^2 a}$ is directly proportional to the cubic anharmonic coefficient $g$.</p>

<h4>2. Lattice Thermal Conductivity $\kappa$</h4>
<p>Heat conduction by phonons is described by the kinetic theory formula:</p>
<div class="math-display">
$$\kappa = \frac{1}{3} C_V v_s \ell_{\text{ph}}$$
</div>
<p>where $C_V$ is the phonon heat capacity per unit volume, $v_s$ is the mean sound velocity, and $\ell_{\text{ph}} = v_s \tau_{\text{ph}}$ is the phonon mean free path.</p>

<h4>3. Normal ($N$) vs. Umklapp ($U$) Phonon Scattering Processes</h4>
<p>In three-phonon scattering collisions ($\vec{q}_1 + \vec{q}_2 = \vec{q}_3 + \vec{G}$):</p>
<ul>
<li><strong>Normal ($N$) Processes ($\vec{G} = 0$):</strong> $\vec{q}_1 + \vec{q}_2 = \vec{q}_3$. Total phonon crystal momentum is conserved. $N$-processes redistribute energy among phonon modes but do not produce thermal resistance (they cannot decay a net heat current).</li>
<li><strong>Umklapp ($U$) Processes ($\vec{G} \neq 0$):</strong> $\vec{q}_1 + \vec{q}_2 = \vec{q}_3 + \vec{G}$. When two high-energy phonons collide such that $\vec{q}_1 + \vec{q}_2$ falls outside the First Brillouin Zone, it is Bragg-reflected back into the zone by subtracting a reciprocal lattice vector $\vec{G}$. This <em>reverses</em> the direction of the resultant energy flow, destroying net crystal momentum and creating intrinsic <strong>lattice thermal resistivity</strong>.</li>
</ul>
<p>At high temperatures ($T \gg \Theta_D$), the number of excited high-energy phonons scales as $n_{\text{ph}} \propto T$, so $\ell_{\text{ph}} \propto 1/T$, yielding $\kappa \propto 1/T$. At very low temperatures, $U$-processes freeze out as $e^{-\Theta_D / 2T}$, and $\ell_{\text{ph}}$ is limited only by sample boundary scattering ($\ell_{\text{ph}} \approx \text{const}$), so $\kappa \propto C_V \propto T^3$.</p>"""
        }
    ],
    "problems": [
        {
            "id": "ssp-p-3-1",
            "title": "Acoustic Cut-Off Frequency and Sound Velocity of Monatomic Aluminum",
            "statement": "Monatomic aluminum crystallizes in a 1D linear model with atomic mass $M = 26.98 \\text{ u} = 4.480 \\times 10^{-26} \\text{ kg}$, interatomic spacing $a = 2.86 \\text{ \u00c5}$, and interatomic spring constant $C = 25.0 \\text{ N/m}$. (a) Calculate the longitudinal sound velocity $v_s$. (b) Determine the maximum acoustic cut-off angular frequency $\\omega_{\\text{max}}$ and corresponding cyclical frequency $\\nu_{\\text{max}}$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Sound Velocity v_s",
                    "math": r"v_s = a \sqrt{\frac{C}{M}} = (2.86 \times 10^{-10}\text{ m}) \sqrt{\frac{25.0\text{ N/m}}{4.480 \times 10^{-26}\text{ kg}}} = (2.86 \times 10^{-10}) \sqrt{5.580 \times 10^{26}} \approx (2.86 \times 10^{-10}) \times (2.362 \times 10^{13}) \approx 6756\text{ m/s}",
                    "explanation": "Evaluate the continuum limit sound velocity v_s = a * sqrt(C / M)."
                },
                {
                    "stepName": "Step 2: Calculate the Maximum Cut-Off Angular Frequency",
                    "math": r"\omega_{\text{max}} = 2 \sqrt{\frac{C}{M}} = 2 \times (2.362 \times 10^{13}\text{ rad/s}) \approx 4.724 \times 10^{13}\text{ rad/s}",
                    "explanation": "At the Brillouin zone boundary k = pi / a, omega_max = 2 * sqrt(C / M)."
                },
                {
                    "stepName": "Step 3: Calculate the Cyclical Frequency nu_max",
                    "math": r"\nu_{\text{max}} = \frac{\omega_{\text{max}}}{2\pi} = \frac{4.724 \times 10^{13}\text{ rad/s}}{2\pi} \approx 7.519 \times 10^{12}\text{ Hz} = 7.52\text{ THz}",
                    "explanation": "Convert angular frequency to cyclical frequency in Terahertz (THz)."
                }
            ],
            "answer": "v_s = 6756 \\text{ m/s}, \\quad \\omega_{\\text{max}} = 4.72 \\times 10^{13} \\text{ rad/s}, \\quad \\nu_{\\text{max}} = 7.52 \\text{ THz}"
        },
        {
            "id": "ssp-p-3-2",
            "title": "Diatomic Chain Phonon Branches and Band Gap for Sodium Chloride",
            "statement": "Model a 1D chain of rock-salt $\\text{NaCl}$ with alternating sodium ions ($M_1 = 22.99 \\text{ u} = 3.818 \\times 10^{-26} \\text{ kg}$) and chlorine ions ($M_2 = 35.45 \\text{ u} = 5.887 \\times 10^{-26} \\text{ kg}$) connected by springs with constant $C = 15.0 \\text{ N/m}$. (a) Calculate the optical phonon frequency $\\omega_{\\text{opt}}$ at $k = 0$. (b) Calculate the optical and acoustic frequencies at the zone boundary $k = \\pi/a$, and determine the width of the forbidden phononic band gap $\\Delta \\omega$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Reduced Mass mu of the Ion Pair",
                    "math": r"\mu = \frac{M_1 M_2}{M_1 + M_2} = \frac{(3.818 \times 10^{-26})(5.887 \times 10^{-26})}{3.818 \times 10^{-26} + 5.887 \times 10^{-26}}\text{ kg} = \frac{2.2477 \times 10^{-51}}{9.705 \times 10^{-26}} \approx 2.316 \times 10^{-26}\text{ kg}",
                    "explanation": "Compute the reduced mass mu = M1 * M2 / (M1 + M2)."
                },
                {
                    "stepName": "Step 2: Calculate the Optical Frequency at k = 0",
                    "math": r"\omega_{\text{opt}}(0) = \sqrt{\frac{2C}{\mu}} = \sqrt{\frac{2 \times 15.0\text{ N/m}}{2.316 \times 10^{-26}\text{ kg}}} = \sqrt{1.295 \times 10^{27}} \approx 3.599 \times 10^{13}\text{ rad/s} \implies \nu_{\text{opt}}(0) = 5.73\text{ THz}",
                    "explanation": "At the zone center, the optical frequency is governed by the relative oscillation of both masses."
                },
                {
                    "stepName": "Step 3: Calculate Zone Boundary Frequencies at k = pi / a",
                    "math": r"\omega_1 = \sqrt{\frac{2C}{M_2}} = \sqrt{\frac{30.0}{5.887 \times 10^{-26}}} \approx 2.258 \times 10^{13}\text{ rad/s}, \quad \omega_2 = \sqrt{\frac{2C}{M_1}} = \sqrt{\frac{30.0}{3.818 \times 10^{-26}}} \approx 2.803 \times 10^{13}\text{ rad/s}",
                    "explanation": "At k = pi / a, the acoustic branch terminates at sqrt(2C / M_heavy) and the optical branch terminates at sqrt(2C / M_light)."
                },
                {
                    "stepName": "Step 4: Compute the Forbidden Phononic Band Gap Delta omega",
                    "math": r"\Delta \omega = \omega_2 - \omega_1 = (2.803 - 2.258) \times 10^{13}\text{ rad/s} = 0.545 \times 10^{13}\text{ rad/s} \implies \Delta \nu \approx 0.867\text{ THz}",
                    "explanation": "The gap between the top of the acoustic branch and the bottom of the optical branch."
                }
            ],
            "answer": "\\omega_{\\text{opt}}(0) = 3.60 \\times 10^{13} \\text{ rad/s}, \\quad \\Delta \\omega = 5.45 \\times 10^{12} \\text{ rad/s} \\quad (\\Delta \\nu = 0.87 \\text{ THz})"
        },
        {
            "id": "ssp-p-3-3",
            "title": "Debye Temperature and Low-Temperature Heat Capacity of Diamond",
            "statement": "Diamond has a density of $\\rho = 3.515 \\text{ g/cm}^3$ and atomic molar mass $M = 12.011 \\text{ g/mol}$. Its average sound velocity is $v_s = 1.20 \\times 10^4 \\text{ m/s}$. (a) Calculate the atomic number density $N/V$. (b) Determine the Debye cut-off frequency $\\omega_D$ and the Debye temperature $\\Theta_D$. (c) Evaluate the molar lattice heat capacity $C_V$ of diamond at $T = 30 \\text{ K}$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Atomic Number Density N / V",
                    "math": r"\frac{N}{V} = \frac{\rho N_A}{M} = \frac{(3.515 \times 10^6\text{ g/m}^3)(6.022 \times 10^{23}\text{ mol}^{-1})}{12.011\text{ g/mol}} \approx 1.762 \times 10^{29}\text{ atoms/m}^3",
                    "explanation": "Compute atomic number density from mass density and molar mass."
                },
                {
                    "stepName": "Step 2: Calculate the Debye Cut-Off Frequency omega_D",
                    "math": r"\omega_D = v_s \left( 6\pi^2 \frac{N}{V} \right)^{1/3} = (1.20 \times 10^4\text{ m/s}) \left[ 6\pi^2 (1.762 \times 10^{29}) \right]^{1/3} = (1.20 \times 10^4) (1.043 \times 10^{31})^{1/3} \approx (1.20 \times 10^4)(2.185 \times 10^{10}) \approx 2.622 \times 10^{14}\text{ rad/s}",
                    "explanation": "Evaluate the 3D Debye frequency formula."
                },
                {
                    "stepName": "Step 3: Calculate the Debye Temperature Theta_D",
                    "math": r"\Theta_D = \frac{\hbar \omega_D}{k_B} = \frac{(1.0546 \times 10^{-34}\text{ J}\cdot\text{s})(2.622 \times 10^{14}\text{ rad/s})}{1.3806 \times 10^{-23}\text{ J/K}} \approx \frac{2.765 \times 10^{-20}}{1.3806 \times 10^{-23}} \approx 2003\text{ K}",
                    "explanation": "Convert Debye frequency to Debye temperature."
                },
                {
                    "stepName": "Step 4: Calculate Molar Heat Capacity at T = 30 K using the T^3 Law",
                    "math": r"C_V = \frac{12\pi^4}{5} R \left(\frac{T}{\Theta_D}\right)^3 = \frac{12\pi^4}{5} (8.314\text{ J/mol}\cdot\text{K}) \left(\frac{30\text{ K}}{2003\text{ K}}\right)^3 \approx 1943.8 \times (1.498 \times 10^{-2})^3 \approx 1943.8 \times 3.361 \times 10^{-6} \approx 6.53 \times 10^{-3}\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}",
                    "explanation": "Apply the low-temperature Debye T^3 formula since T = 30 K is far below Theta_D = 2003 K."
                }
            ],
            "answer": "\\Theta_D \\approx 2003 \\text{ K}, \\quad C_V(30\\text{ K}) = 6.53 \\times 10^{-3} \\text{ J}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1}"
        }
    ]
}

# ==========================================
# UNIT 4: Multi-Electron Atoms & Molecular Bonding in Solids
# ==========================================
u4 = {
    "unitNumber": 4,
    "unitId": "unit4-multielectron-atoms",
    "title": "Multi-Electron Atoms & Chemical Bonding in Solids",
    "description": "Quantum mechanics of many-electron systems: identical particles, exchange symmetry, Pauli exclusion principle, para- and ortho-helium, Hartree and Hartree-Fock self-consistent field methods, atomic multiplets, Hund's rules, characteristic X-ray spectra, and LCAO molecular orbital theory of covalent bonds.",
    "sections": [
        {
            "id": "ssp-4-1",
            "title": "Identical Particles, Permutation Symmetry & Pauli Principle",
            "content": r"""<h4>1. Indistinguishability & The Permutation Operator</h4>
<p>In quantum mechanics, identical particles (such as electrons) are fundamentally indistinguishable. Consider a system of two identical particles described by coordinate vectors $\xi_1 = (\vec{r}_1, \sigma_1)$ and $\xi_2 = (\vec{r}_2, \sigma_2)$ combining spatial and spin coordinates. The permutation operator $\hat{P}_{12}$ exchanges the particles:</p>
<div class="math-display">
$$\hat{P}_{12} \Psi(\xi_1, \xi_2) = \Psi(\xi_2, \xi_1)$$
</div>
<p>Because $\hat{P}_{12}^2 = \hat{I}$, its eigenvalues are $\lambda = \pm 1$. The <strong>Symmetrization Postulate</strong> partitions all physical particles in nature into two disjoint classes:</p>
<ul>
<li><strong>Bosons (Integer Spin $S = 0, 1, 2, \dots$):</strong> Symmetric wavefunctions under exchange:
<div class="math-display">
$$\Psi(\xi_2, \xi_1) = + \Psi(\xi_1, \xi_2)$$
</div></li>
<li><strong>Fermions (Half-Integer Spin $S = 1/2, 3/2, \dots$):</strong> Antisymmetric wavefunctions under exchange:
<div class="math-display">
$$\Psi(\xi_2, \xi_1) = - \Psi(\xi_1, \xi_2)$$
</div></li>
</ul>

<h4>2. The Pauli Exclusion Principle & Slater Determinants</h4>
<p>Electrons are spin-$1/2$ fermions, so the total wavefunction of an $N$-electron system must be completely antisymmetric under the exchange of any pair of electrons $i$ and $j$. If the electrons occupy single-particle spin-orbitals $\chi_{\alpha}(\xi) = \phi_a(\vec{r}) \chi_s(\sigma)$, the total antisymmetric wavefunction is represented by a <strong>Slater Determinant</strong>:</p>
<div class="math-display">
$$\Psi(\xi_1, \xi_2, \dots, \xi_N) = \frac{1}{\sqrt{N!}} \begin{vmatrix} \chi_{\alpha_1}(\xi_1) & \chi_{\alpha_2}(\xi_1) & \dots & \chi_{\alpha_N}(\xi_1) \\ \chi_{\alpha_1}(\xi_2) & \chi_{\alpha_2}(\xi_2) & \dots & \chi_{\alpha_N}(\xi_2) \\ \vdots & \vdots & \ddots & \vdots \\ \chi_{\alpha_1}(\xi_N) & \chi_{\alpha_2}(\xi_N) & \dots & \chi_{\alpha_N}(\xi_N) \end{vmatrix}$$
</div>
<p>If two electrons occupy the identical quantum state ($\alpha_1 = \alpha_2$), two columns of the determinant are identical, causing $\Psi \equiv 0$. This establishes the <strong>Pauli Exclusion Principle</strong>: <em>no two electrons can occupy the same quantum state simultaneously</em>.</p>"""
        },
        {
            "id": "ssp-4-2",
            "title": "The Helium Atom: Exchange Symmetry, Para- & Ortho-Helium",
            "content": r"""<h4>1. Helium Hamiltonian & Electron-Electron Repulsion</h4>
<p>The non-relativistic Hamiltonian of the neutral Helium atom ($Z = 2$) with nucleus at the origin is:</p>
<div class="math-display">
$$\hat{H} = \left( - \frac{\hbar^2}{2m} \nabla_1^2 - \frac{2e^2}{4\pi\varepsilon_0 r_1} \right) + \left( - \frac{\hbar^2}{2m} \nabla_2^2 - \frac{2e^2}{4\pi\varepsilon_0 r_2} \right) + \frac{e^2}{4\pi\varepsilon_0 |\vec{r}_1 - \vec{r}_2|} = \hat{H}_1 + \hat{H}_2 + \hat{V}_{ee}$$
</div>
<p>The total two-electron wavefunction factors into spatial and spin parts: $\Psi(\xi_1, \xi_2) = \psi(\vec{r}_1, \vec{r}_2) \chi_{\text{spin}}(1, 2)$. Total antisymmetry requires:</p>
<ul>
<li><strong>Singlet State ($S = 0$, Para-Helium):</strong> Antisymmetric spin $\chi_{0,0} = \frac{1}{\sqrt{2}}(\alpha_1 \beta_2 - \beta_1 \alpha_2)$ coupled to a <strong>symmetric spatial wavefunction</strong>:
<div class="math-display">
$$\psi_+(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}} [\phi_a(\vec{r}_1)\phi_b(\vec{r}_2) + \phi_b(\vec{r}_1)\phi_a(\vec{r}_2)]$$
</div></li>
<li><strong>Triplet State ($S = 1$, Ortho-Helium):</strong> Symmetric spin ($M_S = +1, 0, -1$) coupled to an <strong>antisymmetric spatial wavefunction</strong>:
<div class="math-display">
$$\psi_-(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}} [\phi_a(\vec{r}_1)\phi_b(\vec{r}_2) - \phi_b(\vec{r}_1)\phi_a(\vec{r}_2)]$$
</div></li>
</ul>

<h4>2. Direct and Exchange Integrals</h4>
<p>Evaluating the expectation value of the electron-electron Coulomb repulsion $\hat{V}_{ee}$ in first-order perturbation theory:</p>
<div class="math-display">
$$\langle \hat{V}_{ee} \rangle_{\pm} = \iint |\psi_{\pm}(\vec{r}_1, \vec{r}_2)|^2 \frac{e^2}{4\pi\varepsilon_0 r_{12}} d^3r_1 d^3r_2 = J \pm K$$
</div>
<p>where:</p>
<ul>
<li><strong>Direct Coulomb Integral $J$:</strong> Classical electrostatic repulsion between the two electron charge clouds:
<div class="math-display">
$$J = \iint |\phi_a(\vec{r}_1)|^2 \frac{e^2}{4\pi\varepsilon_0 r_{12}} |\phi_b(\vec{r}_2)|^2 d^3r_1 d^3r_2 > 0$$
</div></li>
<li><strong>Exchange Integral $K$:</strong> Purely quantum mechanical energy shift arising from the overlap of the two single-particle orbitals:
<div class="math-display">
$$K = \iint \phi_a^*(\vec{r}_1) \phi_b^*(\vec{r}_2) \frac{e^2}{4\pi\varepsilon_0 r_{12}} \phi_b(\vec{r}_1) \phi_a(\vec{r}_2) d^3r_1 d^3r_2 > 0$$
</div></li>
</ul>
<p>The total energy eigenvalues are: $E_{\text{singlet}} = E_0 + J + K$ and $E_{\text{triplet}} = E_0 + J - K$. The triplet state (ortho-helium) lies lower in energy than the singlet state (para-helium) by the <strong>exchange splitting</strong> $\Delta E = 2K$. In the triplet state, $\psi_-(\vec{r}, \vec{r}) = 0$, meaning electrons avoid each other in space, reducing Coulomb repulsion.</p>"""
        },
        {
            "id": "ssp-4-3",
            "title": "Hartree & Hartree-Fock Self-Consistent Field (SCF) Methods",
            "simulation": "ssp-hartree-scf-sim",
            "content": r"""<h4>1. The Central Field Approximation</h4>
<p>In multi-electron atoms and solids with $N$ electrons, the exact many-body Schrödinger equation cannot be solved analytically. In the <strong>central field approximation</strong>, each electron moves independently in an effective spherically symmetric potential $V_{\text{eff}}(r)$ created by the nucleus plus the spherically averaged charge distribution of all other $N-1$ electrons:</p>
<div class="math-display">
$$\hat{H}_i \phi_i(\vec{r}_i) = \left( - \frac{\hbar^2}{2m}\nabla_i^2 + V_{\text{eff}}(r_i) \right) \phi_i(\vec{r}_i) = \varepsilon_i \phi_i(\vec{r}_i)$$
</div>

<h4>2. The Hartree Self-Consistent Field (SCF) Method</h4>
<p>Douglas Hartree (1928) formulated an iterative variational procedure. Assuming a trial product wavefunction $\Psi = \phi_1(\vec{r}_1)\phi_2(\vec{r}_2)\dots\phi_N(\vec{r}_N)$, electron $i$ experiences an electrostatic potential produced by the charge density $\rho_j(\vec{r}') = -e |\phi_j(\vec{r}')|^2$ of all other electrons:</p>
<div class="math-display">
$$V_i^{\text{Hartree}}(\vec{r}) = - \frac{Ze^2}{4\pi\varepsilon_0 r} + \sum_{j \neq i} \int \frac{e^2 |\phi_j(\vec{r}')|^2}{4\pi\varepsilon_0 |\vec{r} - \vec{r}'|} d^3r'$$
</div>
<p>The self-consistent iteration cycle proceeds as follows:</p>
<ol>
<li>Guess an initial set of radial wavefunctions $\{\phi_j^{(0)}\}$.</li>
<li>Compute the electronic charge density $\rho^{(0)}(\vec{r})$ and the Hartree potential $V_i^{(0)}(\vec{r})$.</li>
<li>Solve the single-particle Schrödinger equations to obtain a new set of wavefunctions $\{\phi_j^{(1)}\}$.</li>
<li>Repeat steps 2–3 iteratively until the input and output potentials converge within a numerical tolerance: $|V^{(k+1)} - V^{(k)}| < \delta$.</li>
</ol>

<h4>3. The Hartree-Fock Method & Non-Local Exchange Potential</h4>
<p>The simple Hartree product fails to satisfy the Pauli principle. Fock (1930) replaced the product with a fully antisymmetric Slater determinant, introducing an additional non-local <strong>exchange potential</strong> $V_{\text{ex}}$:</p>
<div class="math-display">
$$\left( - \frac{\hbar^2}{2m}\nabla^2 + V_{\text{nuc}}(\vec{r}) + V_{\text{Coulomb}}(\vec{r}) \right) \phi_i(\vec{r}) - \sum_{j} \left[ \int \frac{e^2 \phi_j^*(\vec{r}') \phi_i(\vec{r}')}{4\pi\varepsilon_0 |\vec{r} - \vec{r}'|} d^3r' \right] \phi_j(\vec{r}) = \varepsilon_i \phi_i(\vec{r})$$
</div>
<p>The exchange operator acts only between electrons with parallel spins, creating a surrounding depletion zone known as the <strong>Fermi hole</strong> (or exchange hole).</p>"""
        },
        {
            "id": "ssp-4-4",
            "title": "Hund's Rules, Characteristic X-Rays & Molecular LCAO Bonding",
            "simulation": "ssp-lcao-molecular-orbital-sim",
            "content": r"""<h4>1. Hund's Rules for Atomic Ground States</h4>
<p>For multi-electron open subshells ($p^n, d^n, f^n$), electrostatic repulsion and spin-orbit coupling determine the energetic ordering of spectroscopic term symbols $^{2S+1}L_J$ via <strong>Hund's three empirical rules</strong>:</p>
<ol>
<li><strong>Rule 1 (Maximize Spin Multiplicity $S$):</strong> The ground state term has the maximum total spin $S$ permitted by the Pauli exclusion principle (minimizes Coulomb repulsion by maximizing exchange stabilization).</li>
<li><strong>Rule 2 (Maximize Total Orbital Angular Momentum $L$):</strong> For a given $S$, the ground state has the maximum total orbital angular momentum $L$ (electrons orbit in the same sense, minimizing spatial close encounters).</li>
<li><strong>Rule 3 (Spin-Orbit Coupling $J$):</strong>
<ul>
<li>If the subshell is <em>less than half full</em>, the lowest energy level has minimum total angular momentum: $J = |L - S|$.</li>
<li>If the subshell is <em>more than half full</em>, the lowest energy level has maximum total angular momentum: $J = L + S$.</li>
</ul></li>
</ol>

<h4>2. Characteristic X-Ray Spectra & Moseley's Law</h4>
<p>When high-energy electrons eject an inner-core atomic electron, vacancies are filled by radiative transitions from outer shells, producing sharp characteristic X-ray lines:</p>
<ul>
<li>$K_\alpha$ line: transition from $n = 2$ ($L$-shell) to $n = 1$ ($K$-shell).</li>
<li>$K_\beta$ line: transition from $n = 3$ ($M$-shell) to $n = 1$ ($K$-shell).</li>
<li>$L_\alpha$ line: transition from $n = 3$ ($M$-shell) to $n = 2$ ($L$-shell).</li>
</ul>
<p>Henry Moseley (1913) discovered that the frequency $\nu$ of characteristic X-rays is related linearly to the atomic number $Z$:</p>
<div class="math-display">
$$\sqrt{\nu} = a (Z - b)$$
</div>
<p>For the $K_\alpha$ line, $b = 1$ (the remaining $1s$ electron screens one unit of nuclear charge), yielding:</p>
<div class="math-display">
$$\nu_{K_\alpha} = R_c c (Z - 1)^2 \left( \frac{1}{1^2} - \frac{1}{2^2} \right) = \frac{3}{4} R_c c (Z - 1)^2$$
</div>

<h4>3. Molecular Orbital Theory & LCAO Covalent Bonding</h4>
<p>In solids, atomic orbitals overlap to form extended molecular orbitals. In the simplest diatomic system ($\text{H}_2^+$ and $\text{H}_2$), Linear Combination of Atomic Orbitals (LCAO) yields two molecular orbitals from atomic hydrogen $1s$ states $\phi_A$ and $\phi_B$:</p>
<ul>
<li><strong>Bonding Orbital ($\sigma_g$):</strong> $\psi_+ = \frac{1}{\sqrt{2(1+S)}} (\phi_A + \phi_B)$. Large electron probability density $|\psi_+|^2$ builds up between the two positively charged nuclei, screening their Coulomb repulsion and lowering the total electronic energy.</li>
<li><strong>Antibonding Orbital ($\sigma_u^*$):</strong> $\psi_- = \frac{1}{\sqrt{2(1-S)}} (\phi_A - \phi_B)$. Nodal plane ($\psi = 0$) midway between the nuclei pushes electron density away, increasing nuclear repulsion and raising the energy.</li>
</ul>"""
        }
    ],
    "problems": [
        {
            "id": "ssp-p-4-1",
            "title": "Exchange Splitting in the Helium (1s)(2s) Excited Configuration",
            "statement": "In the excited $(1s)(2s)$ configuration of the Helium atom, the direct Coulomb integral is $J = 8.78 \\text{ eV}$ and the exchange integral is $K = 1.19 \\text{ eV}$. The unperturbed two-electron energy level is $E_0 = -59.38 \\text{ eV}$. (a) Calculate the total energies of the singlet state ($1^1S_0$, para-helium) and the triplet state ($2^3S_1$, ortho-helium). (b) Determine the exchange splitting energy $\\Delta E$ and explain physically why the triplet state lies lower in energy.",
            "steps": [
                {
                    "stepName": "Step 1: Formulate Energy Expressions for Singlet and Triplet States",
                    "math": r"E_{\text{singlet}} = E_0 + J + K, \quad E_{\text{triplet}} = E_0 + J - K",
                    "explanation": "In the singlet state, the spatial wavefunction is symmetric (J + K), while in the triplet state it is antisymmetric (J - K)."
                },
                {
                    "stepName": "Step 2: Calculate Numerical Energy of the Singlet State (Para-Helium)",
                    "math": r"E_{\text{singlet}} = -59.38\text{ eV} + 8.78\text{ eV} + 1.19\text{ eV} = -49.41\text{ eV}",
                    "explanation": "Evaluate E_singlet."
                },
                {
                    "stepName": "Step 3: Calculate Numerical Energy of the Triplet State (Ortho-Helium)",
                    "math": r"E_{\text{triplet}} = -59.38\text{ eV} + 8.78\text{ eV} - 1.19\text{ eV} = -51.79\text{ eV}",
                    "explanation": "Evaluate E_triplet."
                },
                {
                    "stepName": "Step 4: Compute the Exchange Splitting Delta E",
                    "math": r"\Delta E = E_{\text{singlet}} - E_{\text{triplet}} = 2K = 2 \times 1.19\text{ eV} = 2.38\text{ eV}",
                    "explanation": "The exchange splitting equals twice the exchange integral."
                }
            ],
            "answer": "E_{\\text{singlet}} = -49.41 \\text{ eV}, \\quad E_{\\text{triplet}} = -51.79 \\text{ eV}, \\quad \\Delta E = 2.38 \\text{ eV}"
        },
        {
            "id": "ssp-p-4-2",
            "title": "Ground State Spectroscopic Term Symbols for Carbon and Iron",
            "statement": "Use Hund's rules to determine the ground state spectroscopic term symbol $^{2S+1}L_J$ for: (a) Carbon (neutral atom, valence subshell $2p^2$). (b) Iron ($\text{Fe}^{2+}$ ion, valence subshell $3d^6$).",
            "steps": [
                {
                    "stepName": "Step 1: Carbon 2p^2 Configuration (l = 1, 2 electrons)",
                    "math": r"S = \frac{1}{2} + \frac{1}{2} = 1 \implies 2S+1 = 3 \quad (\text{Triplet})",
                    "explanation": "Rule 1: Maximize S. Place both electrons with parallel spins in different m_l orbitals: m_s = +1/2, +1/2."
                },
                {
                    "stepName": "Step 2: Maximize L for Carbon and Determine J",
                    "math": r"L = m_{l,1} + m_{l,2} = 1 + 0 = 1 \implies P \text{ state}",
                    "explanation": "Rule 2: Maximize L using available m_l in {+1, 0, -1}. Placing electrons in m_l = +1 and m_l = 0 gives L = 1."
                },
                {
                    "stepName": "Step 3: Determine J for Carbon (Less than Half Full)",
                    "math": r"J = |L - S| = |1 - 1| = 0 \implies {^3P_0}",
                    "explanation": "Rule 3: The 2p subshell is less than half full (2 of 6 electrons), so J = |L - S| = 0. The ground state is ^3P_0."
                },
                {
                    "stepName": "Step 4: Iron Fe^2+ 3d^6 Configuration (l = 2, 6 electrons)",
                    "math": r"S = 5 \times \left(\frac{1}{2}\right) - 1 \times \left(\frac{1}{2}\right) = 2 \implies 2S+1 = 5 \quad (\text{Quintet})",
                    "explanation": "Rule 1: Place 5 electrons spin-up in m_l = +2, +1, 0, -1, -2 and the 6th electron spin-down in m_l = +2. S = 2."
                },
                {
                    "stepName": "Step 5: Maximize L and Determine J for Fe^2+ (More than Half Full)",
                    "math": r"L = (+2) + (+1) + (0) + (-1) + (-2) + (+2) = 2 \implies D \text{ state}, \quad J = L + S = 2 + 2 = 4 \implies {^5D_4}",
                    "explanation": "Rule 2: L = 2 (D state). Rule 3: The 3d subshell is more than half full (6 of 10 electrons), so J = L + S = 4. The ground state is ^5D_4."
                }
            ],
            "answer": "\\text{Carbon: } {^3P_0}, \\quad \\text{Iron (Fe}^{2+}\\text{): } {^5D_4}"
        },
        {
            "id": "ssp-p-4-3",
            "title": "Moseley's Law and Characteristic K_alpha X-Ray Wavelength for Copper",
            "statement": "Copper has atomic number $Z = 29$. The Rydberg constant is $R_\infty = 1.09737 \times 10^7 \\text{ m}^{-1}$. Using Moseley's law with screening constant $b = 1.0$ for the $K_\\alpha$ transition: (a) Calculate the cyclical frequency $\\nu_{K_\\alpha}$ of the emitted X-ray photon. (b) Determine the wavelength $\\lambda_{K_\\alpha}$ in Angstroms and the photon energy in $\\text{keV}$.",
            "steps": [
                {
                    "stepName": "Step 1: Formulate Moseley's Equation for the K_alpha Line",
                    "math": r"\nu_{K_\alpha} = \frac{3}{4} c R_\infty (Z - 1)^2",
                    "explanation": "The K_alpha transition originates from n=2 to n=1 with screening factor b=1."
                },
                {
                    "stepName": "Step 2: Calculate the Cyclical Frequency nu",
                    "math": r"\nu_{K_\alpha} = \frac{3}{4} \times (2.9979 \times 10^8\text{ m/s}) \times (1.09737 \times 10^7\text{ m}^{-1}) \times (29 - 1)^2 = (2.4673 \times 10^{15}) \times (28)^2 \approx (2.4673 \times 10^{15}) \times 784 \approx 1.9344 \times 10^{18}\text{ Hz}",
                    "explanation": "Substitute c, R_infinity, and Z=29 into the formula."
                },
                {
                    "stepName": "Step 3: Calculate the Wavelength lambda",
                    "math": r"\lambda_{K_\alpha} = \frac{c}{\nu_{K_\alpha}} = \frac{2.9979 \times 10^8\text{ m/s}}{1.9344 \times 10^{18}\text{ s}^{-1}} \approx 1.5498 \times 10^{-10}\text{ m} = 1.550\text{ \AA}",
                    "explanation": "Compute lambda = c / nu. This closely matches the experimental Cu K_alpha value of 1.541 Angstroms."
                },
                {
                    "stepName": "Step 4: Calculate the Photon Energy in keV",
                    "math": r"E = h \nu = \frac{12398.4\text{ eV}\cdot\text{\AA}}{1.5498\text{ \AA}} \approx 8000\text{ eV} = 8.00\text{ keV}",
                    "explanation": "Convert wavelength to energy in keV."
                }
            ],
            "answer": "\\nu_{K_\\alpha} = 1.934 \\times 10^{18} \\text{ Hz}, \\quad \\lambda_{K_\\alpha} = 1.550 \\text{ \u00c5}, \\quad E = 8.00 \\text{ keV}"
        }
    ]
}

with open("ssp_u3.json", "w") as f:
    json.dump(u3, f, indent=2)
print("ssp_u3.json created successfully!")

with open("ssp_u4.json", "w") as f:
    json.dump(u4, f, indent=2)
print("ssp_u4.json created successfully!")
