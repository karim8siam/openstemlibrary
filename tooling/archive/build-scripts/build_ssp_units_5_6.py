import json

# ==========================================
# UNIT 5: Free Electron Theory of Metals & Fermi Surfaces
# ==========================================
u5 = {
    "unitNumber": 5,
    "unitId": "unit5-free-electron-theory",
    "title": "Free Electron Theory of Metals & Fermi Surfaces",
    "description": "Comprehensive electronic transport in metals: classical Drude phenomenology, Sommerfeld quantum free Fermi gas, 1D/2D/3D density of states, Fermi-Dirac statistics, Fermi energy and velocity, linear electronic heat capacity, Pauli paramagnetism, Hall effect, Wiedemann-Franz law, and Matthiessen's rule.",
    "sections": [
        {
            "id": "ssp-5-1",
            "title": "Drude Classical Phenomenology of Electrical & Thermal Conduction",
            "content": r"""<h4>1. Postulates of the Drude Model (1900)</h4>
<p>Paul Drude treated valence electrons in a metal as an ideal classical gas of non-interacting point particles of mass $m$ and charge $-e$, moving through a static background of positive ion cores:</p>
<ol>
<li><strong>Independent & Free Electron Approximation:</strong> Electron-electron and electron-ion interactions are neglected between collisions.</li>
<li><strong>Relaxation-Time Approximation:</strong> Collisions are instantaneous, random events occurring with an average probability per unit time $1/\tau$, where $\tau$ is the <strong>relaxation time</strong> (mean free time between collisions).</li>
<li><strong>Thermal Equilibrium:</strong> Electrons emerge from each collision in thermal equilibrium with the local lattice temperature, with zero average drift velocity.</li>
</ol>

<h4>2. Derivation of Ohm's Law and DC Electrical Conductivity</h4>
<p>Under an applied macroscopic electric field $\vec{E}$, the equation of motion for the average drift velocity $\vec{v}_d$ of an electron is:</p>
<div class="math-display">
$$m \frac{d\vec{v}_d}{dt} = - e \vec{E} - \frac{m \vec{v}_d}{\tau}$$
</div>
<p>In steady state ($d\vec{v}_d/dt = 0$):</p>
<div class="math-display">
$$\vec{v}_d = - \frac{e \tau}{m} \vec{E}$$
</div>
<p>The macroscopic electric current density $\vec{J}$ carried by electron density $n$ is:</p>
<div class="math-display">
$$\vec{J} = - n e \vec{v}_d = \left( \frac{n e^2 \tau}{m} \right) \vec{E} = \sigma_0 \vec{E}$$
</div>
<p>This derives microscopic <strong>Ohm's Law</strong>, with DC electrical conductivity $\sigma_0$ given by the <strong>Drude formula</strong>:</p>
<div class="math-display">
$$\sigma_0 = \frac{n e^2 \tau}{m} = n e \mu$$
</div>
<p>where $\mu = e\tau/m$ is the electron drift mobility.</p>

<h4>3. The Classical Wiedemann-Franz Law & Failure of Drude Model</h4>
<p>Treating electrons as a classical Maxwell-Boltzmann gas with thermal conductivity $\kappa = \frac{1}{3} C_v v_{\text{th}} \ell$ and heat capacity $C_v = \frac{3}{2} n k_B$:</p>
<div class="math-display">
$$\frac{\kappa}{\sigma T} = \frac{3}{2} \left(\frac{k_B}{e}\right)^2 \approx 1.11 \times 10^{-8}\text{ W}\cdot\Omega\cdot\text{K}^{-2}$$
</div>
<p>While this qualitatively explained the empirical <strong>Wiedemann-Franz law</strong>, Drude's classical model suffered from a catastrophic failure: it predicted that the electronic heat capacity should contribute $\frac{3}{2} R$ per mole, which was completely absent in room-temperature measurements.</p>"""
        },
        {
            "id": "ssp-5-2",
            "title": "Sommerfeld Quantum Free Fermi Gas: Density of States in 1D, 2D & 3D",
            "simulation": "ssp-fermi-dirac-dos-sim",
            "content": r"""<h4>1. Schrödinger Equation in a 3D Potential Well</h4>
<p>Arnold Sommerfeld (1928) resolved the Drude paradox by applying quantum mechanics and Fermi-Dirac statistics to the valence electrons. Consider $N$ free electrons confined within a box of volume $V = L_x L_y L_z$ with periodic Born-von Kármán boundary conditions:</p>
<div class="math-display">
$$- \frac{\hbar^2}{2m} \nabla^2 \psi(\vec{r}) = E \psi(\vec{r}) \implies \psi_{\vec{k}}(\vec{r}) = \frac{1}{\sqrt{V}} e^{i \vec{k}\cdot\vec{r}}$$
</div>
<p>The energy eigenvalues are continuous parabolic free-particle dispersions:</p>
<div class="math-display">
$$E(\vec{k}) = \frac{\hbar^2 k^2}{2m} = \frac{\hbar^2}{2m}(k_x^2 + k_y^2 + k_z^2)$$
</div>
<p>where allowed wavevectors form a uniform grid in reciprocal $\vec{k}$-space: $k_i = \frac{2\pi n_i}{L_i}$ ($n_i \in \mathbb{Z}$). Each allowed state occupies a volume in $k$-space of $\Delta k^3 = \frac{(2\pi)^3}{V}$.</p>

<h4>2. Derivation of the Density of States $g(E)$ in 3D</h4>
<p>Taking into account electron spin degeneracy ($g_s = 2$):</p>
<div class="math-display">
$$N(k) = 2 \times \frac{\frac{4}{3}\pi k^3}{(2\pi)^3 / V} = \frac{V}{3\pi^2} k^3$$
</div>
<p>Substituting $k = \left(\frac{2mE}{\hbar^2}\right)^{1/2}$:</p>
<div class="math-display">
$$N(E) = \frac{V}{3\pi^2} \left( \frac{2mE}{\hbar^2} \right)^{3/2}$$
</div>
<p>The <strong>Density of States (DOS)</strong> $g(E) = \frac{dN}{dE}$ per unit volume in three dimensions is:</p>
<div class="math-display">
$$g_{\text{3D}}(E) = \frac{1}{V} \frac{dN}{dE} = \frac{1}{2\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} E^{1/2} \propto \sqrt{E}$$
</div>

<h4>3. Dimensionality Comparison of Density of States</h4>
<ul>
<li><strong>1D (Quantum Wire):</strong> $g_{\text{1D}}(E) = \frac{\sqrt{2m}}{\pi \hbar} E^{-1/2} \propto E^{-1/2}$ (Van Hove singularity).</li>
<li><strong>2D (Quantum Well):</strong> $g_{\text{2D}}(E) = \frac{m}{\pi \hbar^2} = \text{constant}$ (energy-independent step functions).</li>
<li><strong>3D (Bulk Metal):</strong> $g_{\text{3D}}(E) = \frac{m}{\pi^2 \hbar^3} \sqrt{2mE} \propto E^{1/2}$.</li>
</ul>"""
        },
        {
            "id": "ssp-5-3",
            "title": "Fermi-Dirac Statistics, Fermi Energy & Quantum Degeneracy",
            "content": r"""<h4>1. The Fermi-Dirac Distribution Function</h4>
<p>Because electrons are indistinguishable fermions obeying the Pauli exclusion principle, the probability of an electronic state of energy $E$ being occupied at absolute temperature $T$ is given by the <strong>Fermi-Dirac distribution</strong>:</p>
<div class="math-display">
$$f(E) = \frac{1}{e^{(E - \mu)/k_B T} + 1}$$
</div>
<p>where $\mu(T)$ is the chemical potential. At $T = 0\text{ K}$, the chemical potential is defined as the <strong>Fermi Energy</strong> $E_F \equiv \mu(0)$. The distribution becomes an exact step function:</p>
<div class="math-display">
$$f(E) = \begin{cases} 1, & E < E_F \\ 0, & E > E_F \end{cases}$$
</div>

<h4>2. Calculation of the Fermi Energy $E_F$ and Fermi Surface</h4>
<p>At $T = 0\text{ K}$, $N$ electrons fill all available states in $k$-space up to a maximum radius, the <strong>Fermi wavevector</strong> $k_F$, enclosing a sphere known as the <strong>Fermi Sphere</strong>:</p>
<div class="math-display">
$$n = \frac{N}{V} = \frac{1}{V} \int_0^{E_F} g(E) dE = \frac{k_F^3}{3\pi^2} \implies k_F = (3\pi^2 n)^{1/3}$$
</div>
<p>The fundamental ground-state parameters of the free Fermi gas are:</p>
<ul>
<li><strong>Fermi Energy:</strong>
<div class="math-display">
$$E_F = \frac{\hbar^2 k_F^2}{2m} = \frac{\hbar^2}{2m} (3\pi^2 n)^{2/3}$$
</div></li>
<li><strong>Fermi Velocity:</strong>
<div class="math-display">
$$v_F = \frac{\hbar k_F}{m} = \frac{\hbar}{m} (3\pi^2 n)^{1/3}$$
</div></li>
<li><strong>Fermi Temperature:</strong>
<div class="math-display">
$$T_F = \frac{E_F}{k_B} \sim 10^4 - 10^5\text{ K}$$
</div></li>
</ul>
<p>Because room temperature ($T \approx 300\text{ K}$) satisfies $T \ll T_F$, valence electrons in typical metals form a <strong>highly degenerate Fermi gas</strong>.</p>"""
        },
        {
            "id": "ssp-5-4",
            "title": "Electronic Heat Capacity & Pauli Paramagnetism",
            "content": r"""<h4>1. Quantum Suppression of Electronic Heat Capacity</h4>
<p>When a metal is heated from $T = 0\text{ K}$ to temperature $T$, the Pauli exclusion principle dictates that electrons with energies deep below the Fermi surface ($E < E_F - k_BT$) cannot absorb thermal energy, because all states within $\sim k_BT$ above them are already occupied. Only electrons within a narrow thermal layer of width $\sim k_BT$ around $E_F$ can undergo transitions.</p>
<p>The fraction of thermally active electrons is approximately $\frac{k_B T}{E_F} = \frac{T}{T_F} \sim 10^{-2}$. Each of these excited electrons acquires thermal energy $\sim k_B T$, yielding an excess internal energy:</p>
<div class="math-display">
$$\Delta U_{el} \approx \left( N \frac{T}{T_F} \right) (k_B T) = N k_B \frac{T^2}{T_F}$$
</div>
<p>Differentiating with respect to $T$ yields a heat capacity linear in temperature:</p>
<div class="math-display">
$$C_{el} = \frac{dU_{el}}{dT} \approx 2 N k_B \frac{T}{T_F} \propto T$$
</div>

<h4>2. Rigorous Sommerfeld Expansion for $C_{el}$</h4>
<p>Performing a rigorous Sommerfeld expansion of the internal energy integral $U(T) = \int_0^\infty E g(E) f(E) dE$ leads to the exact theoretical formula for the electronic heat capacity:</p>
<div class="math-display">
$$C_{el} = \frac{\pi^2}{3} g(E_F) k_B^2 T = \frac{\pi^2}{2} N k_B \left(\frac{T}{T_F}\right) = \gamma T$$
</div>
<p>where $\gamma = \frac{\pi^2}{3} g(E_F) k_B^2$ is the <strong>Sommerfeld coefficient</strong>.</p>
<p>At liquid helium temperatures ($T < 10\text{ K}$), the total heat capacity of a normal non-magnetic metal is the sum of electronic and phononic (Debye) contributions:</p>
<div class="math-display">
$$C_V = C_{el} + C_{\text{ph}} = \gamma T + A T^3 \implies \frac{C_V}{T} = \gamma + A T^2$$
</div>
<p>Plotting $C_V/T$ against $T^2$ yields a straight line whose $y$-intercept is $\gamma$ and whose slope determines the Debye temperature $\Theta_D$.</p>

<h4>3. Pauli Paramagnetism of Conduction Electrons</h4>
<p>In an external magnetic field $B$, electron spin magnetic moments $\mu_B$ align parallel or antiparallel to the field, shifting the up- and down-spin sub-bands by $\mp \mu_B B$. At $T = 0\text{ K}$, electrons near $E_F$ flip their spins into the lower energy sub-band until the Fermi levels equalize:</p>
<div class="math-display">
$$\Delta N = \frac{1}{2} g(E_F) (\mu_B B) - \left(-\frac{1}{2} g(E_F) \mu_B B\right) = g(E_F) \mu_B B$$
</div>
<p>The resulting net magnetic magnetization is $M = \Delta N \mu_B = g(E_F) \mu_B^2 B$. The <strong>Pauli paramagnetic susceptibility</strong> is:</p>
<div class="math-display">
$$\chi_{\text{Pauli}} = \frac{\mu_0 M}{B} = \mu_0 \mu_B^2 g(E_F) = \frac{3 \mu_0 n \mu_B^2}{2 E_F}$$
</div>
<p>Unlike classical Curie paramagnetism ($\chi \propto 1/T$), Pauli paramagnetism is completely temperature-independent, in perfect agreement with experimental data for alkali and noble metals.</p>"""
        },
        {
            "id": "ssp-5-5",
            "title": "The Hall Effect, Wiedemann-Franz Law & Matthiessen's Rule",
            "simulation": "ssp-hall-effect-sim",
            "content": r"""<h4>1. The Hall Effect & Hall Coefficient $R_H$</h4>
<p>When an electric current density $J_x$ flows along the $x$-direction of a conductor immersed in a transverse magnetic field $B_z$ in the $z$-direction, the magnetic Lorentz force $\vec{F}_B = q (\vec{v}_d \times \vec{B})$ deflects charge carriers along the $y$-direction:</p>
<div class="math-display">
$$F_{B,y} = q (v_{d,x} B_z) = - e v_{d,x} B_z$$
</div>
<p>Charge accumulates on the lateral boundaries, generating a transverse electrostatic <strong>Hall electric field</strong> $E_y$. In steady state, the transverse electrostatic force exactly balances the magnetic Lorentz force ($F_y = 0$):</p>
<div class="math-display">
$$q E_y + q v_{d,x} B_z = 0 \implies E_y = - v_{d,x} B_z$$
</div>
<p>Since $J_x = n q v_{d,x} \implies v_{d,x} = \frac{J_x}{n q}$:</p>
<div class="math-display">
$$E_y = - \frac{J_x B_z}{n q} = R_H J_x B_z$$
</div>
<p>where $R_H$ is the <strong>Hall Coefficient</strong>:</p>
<div class="math-display">
$$R_H = \frac{E_y}{J_x B_z} = \frac{1}{n q} = - \frac{1}{n e} \quad (\text{for electrons})$$
</div>
<p>The Hall effect provides an unambiguous experimental measurement of both the <strong>sign of the charge carriers</strong> (negative for electrons, positive for holes) and the <strong>carrier concentration</strong> $n$.</p>

<h4>2. Quantum Wiedemann-Franz Law & The Lorenz Number</h4>
<p>Applying Sommerfeld's degenerate Fermi gas theory to electronic thermal conduction ($\kappa = \frac{1}{3} C_{el} v_F^2 \tau$ with $C_{el} = \frac{\pi^2}{3} g(E_F) k_B^2 T$) and electrical conductivity ($\sigma = \frac{n e^2 \tau}{m}$) yields the <strong>quantum Wiedemann-Franz law</strong>:</p>
<div class="math-display">
$$\frac{\kappa}{\sigma T} = \frac{\pi^2}{3} \left(\frac{k_B}{e}\right)^2 = L \approx 2.443 \times 10^{-8}\text{ W}\cdot\Omega\cdot\text{K}^{-2}$$
</div>
<p>where $L = \frac{\pi^2}{3}(k_B/e)^2$ is the universal <strong>Lorenz number</strong>, completely independent of carrier density, mass, and material parameters.</p>

<h4>3. Matthiessen's Rule for Electrical Resistivity</h4>
<p>Electrons in a real metal are scattered by both static structural crystal defects/impurities and dynamic thermal lattice vibrations (phonons). By <strong>Matthiessen's Rule</strong>, independent scattering rates add linearly:</p>
<div class="math-display">
$$\frac{1}{\tau_{\text{tot}}} = \frac{1}{\tau_{\text{impurity}}} + \frac{1}{\tau_{\text{phonon}}(T)}$$
</div>
<p>Consequently, the total electrical resistivity $\rho = m / (ne^2\tau)$ separates into temperature-independent and temperature-dependent terms:</p>
<div class="math-display">
$$\rho(T) = \rho_{\text{residual}} + \rho_{\text{ideal}}(T)$$
</div>
<p>where $\rho_{\text{residual}}$ is determined by impurity concentration, and $\rho_{\text{ideal}}(T) \propto T^5$ at low temperatures (Bloch-Grüneisen law) and $\rho_{\text{ideal}}(T) \propto T$ at high temperatures ($T > \Theta_D$).</p>"""
        }
    ],
    "problems": [
        {
            "id": "ssp-p-5-1",
            "title": "Fermi Energy, Fermi Velocity and Fermi Temperature of Copper",
            "statement": "Copper is a monovalent metal (one conduction electron per atom) with atomic mass $M = 63.546 \\text{ g/mol}$, density $\\rho = 8.96 \\text{ g/cm}^3$, and electron mass $m = 9.109 \\times 10^{-31} \\text{ kg}$. (a) Calculate the conduction electron number density $n$. (b) Determine the Fermi wavevector $k_F$, the Fermi energy $E_F$ in $\\text{eV}$, the Fermi velocity $v_F$, and the Fermi temperature $T_F$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Electron Density n",
                    "math": r"n = \frac{\rho N_A}{M} = \frac{(8.96 \times 10^6\text{ g/m}^3)(6.022 \times 10^{23}\text{ mol}^{-1})}{63.546\text{ g/mol}} \approx 8.492 \times 10^{28}\text{ electrons/m}^3",
                    "explanation": "Compute conduction electron density from mass density and molar mass."
                },
                {
                    "stepName": "Step 2: Calculate the Fermi Wavevector k_F",
                    "math": r"k_F = (3\pi^2 n)^{1/3} = [3\pi^2 (8.492 \times 10^{28})]^{1/3} = (2.5144 \times 10^{30})^{1/3} \approx 1.360 \times 10^{10}\text{ m}^{-1} = 1.360\text{ \AA}^{-1}",
                    "explanation": "Evaluate the radius of the spherical Fermi surface in reciprocal space."
                },
                {
                    "stepName": "Step 3: Calculate the Fermi Energy E_F in eV",
                    "math": r"E_F = \frac{\hbar^2 k_F^2}{2m} = \frac{(1.0546 \times 10^{-34}\text{ J}\cdot\text{s})^2 (1.360 \times 10^{10}\text{ m}^{-1})^2}{2(9.109 \times 10^{-31}\text{ kg})} = \frac{2.056 \times 10^{-47}}{1.8218 \times 10^{-30}}\text{ J} \approx 1.1286 \times 10^{-18}\text{ J} \approx 7.04\text{ eV}",
                    "explanation": "Convert Joules to electron-volts by dividing by 1.6022 x 10^-19 J/eV."
                },
                {
                    "stepName": "Step 4: Calculate the Fermi Velocity v_F",
                    "math": r"v_F = \frac{\hbar k_F}{m} = \frac{(1.0546 \times 10^{-34}\text{ J}\cdot\text{s})(1.360 \times 10^{10}\text{ m}^{-1})}{9.109 \times 10^{-31}\text{ kg}} \approx 1.574 \times 10^6\text{ m/s}",
                    "explanation": "Compute the velocity of electrons at the Fermi surface."
                },
                {
                    "stepName": "Step 5: Calculate the Fermi Temperature T_F",
                    "math": r"T_F = \frac{E_F}{k_B} = \frac{1.1286 \times 10^{-18}\text{ J}}{1.3806 \times 10^{-23}\text{ J/K}} \approx 81750\text{ K} \approx 8.18 \times 10^4\text{ K}",
                    "explanation": "Compute the degeneracy temperature."
                }
            ],
            "answer": "n = 8.49 \\times 10^{28} \\text{ m}^{-3}, \\quad E_F = 7.04 \\text{ eV}, \\quad v_F = 1.57 \\times 10^6 \\text{ m/s}, \\quad T_F = 8.18 \\times 10^4 \\text{ K}"
        },
        {
            "id": "ssp-p-5-2",
            "title": "Sommerfeld Electronic Heat Capacity Coefficient for Silver",
            "statement": "Silver has a Fermi energy of $E_F = 5.49 \\text{ eV}$ and atomic molar mass $M = 107.87 \\text{ g/mol}$. (a) Calculate the theoretical Sommerfeld coefficient $\\gamma$ per mole of conduction electrons. (b) Calculate the molar electronic heat capacity $C_{el}$ at liquid helium temperature $T = 4.2 \\text{ K}$, and compare it with the classical value $3R/2$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Fermi Temperature of Silver",
                    "math": r"T_F = \frac{E_F}{k_B} = \frac{5.49\text{ eV} \times 1.6022 \times 10^{-19}\text{ J/eV}}{1.3806 \times 10^{-23}\text{ J/K}} = \frac{8.796 \times 10^{-19}\text{ J}}{1.3806 \times 10^{-23}\text{ J/K}} \approx 63710\text{ K}",
                    "explanation": "Convert Fermi energy to Fermi temperature."
                },
                {
                    "stepName": "Step 2: Calculate the Sommerfeld Coefficient gamma",
                    "math": r"\gamma = \frac{\pi^2}{2} R \frac{1}{T_F} = \frac{\pi^2}{2} \times (8.314\text{ J/mol}\cdot\text{K}) \times \frac{1}{63710\text{ K}} \approx \frac{41.028}{63710}\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-2} \approx 6.44 \times 10^{-4}\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-2} = 0.644\text{ mJ}\cdot\text{mol}^{-1}\cdot\text{K}^{-2}",
                    "explanation": "Evaluate the theoretical Sommerfeld constant per mole."
                },
                {
                    "stepName": "Step 3: Evaluate Electronic Heat Capacity at T = 4.2 K",
                    "math": r"C_{el}(4.2\text{ K}) = \gamma T = (6.44 \times 10^{-4}\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-2}) \times (4.2\text{ K}) \approx 2.705 \times 10^{-3}\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} = 2.71\text{ mJ}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}",
                    "explanation": "Multiply gamma by T = 4.2 K."
                },
                {
                    "stepName": "Step 4: Compare with Classical Prediction",
                    "math": r"\frac{C_{el}(4.2\text{ K})}{C_{\text{classical}}} = \frac{2.705 \times 10^{-3}\text{ J/mol}\cdot\text{K}}{\frac{3}{2}(8.314\text{ J/mol}\cdot\text{K})} = \frac{2.705 \times 10^{-3}}{12.471} \approx 2.17 \times 10^{-4}",
                    "explanation": "The quantum electronic heat capacity is suppressed by nearly four orders of magnitude compared to the classical prediction."
                }
            ],
            "answer": "\\gamma = 0.644 \\text{ mJ}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-2}, \\quad C_{el}(4.2\\text{ K}) = 2.71 \\text{ mJ}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1} \\quad (0.0217\\% \\text{ of classical } 3R/2)"
        },
        {
            "id": "ssp-p-5-3",
            "title": "Hall Coefficient, Carrier Density and Mobility in Sodium Metal",
            "statement": "A rectangular ribbon of sodium metal of thickness $t = 0.10 \\text{ mm}$ and width $w = 5.0 \\text{ mm}$ carries a longitudinal current $I_x = 10.0 \\text{ A}$ in a transverse magnetic field $B_z = 1.20 \\text{ T}$. A transverse Hall voltage of $V_H = -2.94 \\text{ }\u03bc\\text{V}$ is measured across its width. The electrical resistivity of sodium is $\\rho = 4.75 \\times 10^{-8} \\text{ }\u03a9\\cdot\\text{m}$. (a) Calculate the Hall coefficient $R_H$. (b) Determine the conduction electron density $n$. (c) Calculate the electron drift mobility $\\mu$ and relaxation time $\\tau$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Hall Coefficient R_H",
                    "math": r"V_H = \frac{R_H I_x B_z}{t} \implies R_H = \frac{V_H t}{I_x B_z} = \frac{(-2.94 \times 10^{-6}\text{ V})(1.0 \times 10^{-4}\text{ m})}{(10.0\text{ A})(1.20\text{ T})} = \frac{-2.94 \times 10^{-10}}{12.0} = - 2.45 \times 10^{-11}\text{ m}^3/\text{C}",
                    "explanation": "Solve for the Hall coefficient using the measured Hall voltage, sample thickness, current, and magnetic field."
                },
                {
                    "stepName": "Step 2: Determine the Conduction Electron Density n",
                    "math": r"n = - \frac{1}{e R_H} = \frac{1}{(1.6022 \times 10^{-19}\text{ C})(2.45 \times 10^{-11}\text{ m}^3/\text{C})} = \frac{1}{3.9254 \times 10^{-30}} \approx 2.548 \times 10^{28}\text{ electrons/m}^3",
                    "explanation": "Extract the carrier density from R_H = -1 / (n e)."
                },
                {
                    "stepName": "Step 3: Calculate the Electron Drift Mobility mu",
                    "math": r"\sigma = \frac{1}{\rho} = \frac{1}{4.75 \times 10^{-8}\text{ }\Omega\cdot\text{m}} \approx 2.105 \times 10^7\text{ }\Omega^{-1}\cdot\text{m}^{-1} \implies \mu = \sigma |R_H| = (2.105 \times 10^7)(2.45 \times 10^{-11})\text{ m}^2/\text{V}\cdot\text{s} \approx 5.158 \times 10^{-4}\text{ m}^2/\text{V}\cdot\text{s}",
                    "explanation": "Compute mobility using mu = sigma * |R_H|."
                },
                {
                    "stepName": "Step 4: Calculate the Relaxation Time tau",
                    "math": r"\tau = \frac{m \mu}{e} = \frac{(9.109 \times 10^{-31}\text{ kg})(5.158 \times 10^{-4}\text{ m}^2/\text{V}\cdot\text{s})}{1.6022 \times 10^{-19}\text{ C}} \approx 2.93 \times 10^{-14}\text{ s}",
                    "explanation": "Evaluate the electron collision relaxation time."
                }
            ],
            "answer": "R_H = -2.45 \\times 10^{-11} \\text{ m}^3/\\text{C}, \\quad n = 2.55 \\times 10^{28} \\text{ m}^{-3}, \\quad \\mu = 5.16 \\times 10^{-4} \\text{ m}^2/\\text{V}\\cdot\\text{s}, \\quad \\tau = 2.93 \\times 10^{-14} \\text{ s}"
        }
    ]
}

# ==========================================
# UNIT 6: Electronic Band Structure & Bloch Electron Dynamics
# ==========================================
u6 = {
    "unitNumber": 6,
    "unitId": "unit6-band-structure",
    "title": "Electronic Band Structure & Bloch Electron Dynamics",
    "description": "Comprehensive energy band theory in crystals: periodic potential, Bloch theorem, Kronig-Penney solvable model, origin of energy band gaps, reduced and extended zone schemes, nearly free electron approximation, tight-binding LCAO method, semiclassical electron dynamics, group velocity, effective mass tensor, concept of positive holes, and Fermi surfaces.",
    "sections": [
        {
            "id": "ssp-6-1",
            "title": "Periodic Crystal Potential & Bloch's Theorem",
            "content": r"""<h4>1. Electrons in a Periodic Crystal Potential</h4>
<p>An electron in a perfect crystalline solid experiences a potential energy $V(\vec{r})$ that possesses the full discrete translational periodicity of the Bravais lattice:</p>
<div class="math-display">
$$V(\vec{r} + \vec{R}) = V(\vec{r}) \quad \forall \vec{R} = n_1 \vec{a}_1 + n_2 \vec{a}_2 + n_3 \vec{a}_3$$
</div>
<p>The single-electron Schrödinger equation is:</p>
<div class="math-display">
$$\hat{H} \psi(\vec{r}) = \left[ - \frac{\hbar^2}{2m} \nabla^2 + V(\vec{r}) \right] \psi(\vec{r}) = E \psi(\vec{r})$$
</div>

<h4>2. Formal Statement & Proof of Bloch's Theorem</h4>
<p>Because the Hamiltonian commutes with all lattice translation operators $\hat{T}_{\vec{R}}$ ($[\hat{H}, \hat{T}_{\vec{R}}] = 0$), simultaneous eigenstates of $\hat{H}$ and $\hat{T}_{\vec{R}}$ can be constructed. <strong>Bloch's Theorem</strong> states that the eigenstates of an electron in a periodic potential can be chosen in the form of a plane wave modulated by a periodic function $u_{n,\vec{k}}(\vec{r})$ having the periodicity of the lattice:</p>
<div class="math-display">
$$\psi_{n,\vec{k}}(\vec{r}) = e^{i \vec{k} \cdot \vec{r}} u_{n,\vec{k}}(\vec{r})$$
</div>
<p>where $u_{n,\vec{k}}(\vec{r} + \vec{R}) = u_{n,\vec{k}}(\vec{r})$ for all lattice vectors $\vec{R}$. Equivalently, translating by any lattice vector $\vec{R}$ merely shifts the phase of the wavefunction:</p>
<div class="math-display">
$$\psi_{n,\vec{k}}(\vec{r} + \vec{R}) = e^{i \vec{k} \cdot \vec{R}} \psi_{n,\vec{k}}(\vec{r})$$
</div>
<p>The vector $\vec{k}$ is the <strong>crystal wavevector</strong>, and the integer $n = 1, 2, 3, \dots$ is the <strong>band index</strong>.</p>

<h4>3. Crystal Momentum vs. Physical Momentum</h4>
<p>The quantity $\hbar \vec{k}$ is known as <strong>crystal momentum</strong>. It is not the eigenvalue of the physical momentum operator $-i\hbar\nabla$ (since momentum is not conserved in the presence of the lattice potential). Instead, crystal momentum is conserved in electron-photon, electron-phonon, and electron-electron scattering events modulo an arbitrary reciprocal lattice vector $\vec{G}$:</p>
<div class="math-display">
$$\vec{k}' = \vec{k} + \vec{q} + \vec{G}$$
</div>"""
        },
        {
            "id": "ssp-6-2",
            "title": "The Kronig-Penney Model & Origin of Energy Band Gaps",
            "simulation": "ssp-kronig-penney-sim",
            "content": r"""<h4>1. The Kronig-Penney 1D Solvable Model</h4>
<p>R. de L. Kronig and W. G. Penney (1931) introduced an idealized one-dimensional periodic array of rectangular potential barriers of height $V_0$, barrier width $b$, and well width $a$ (lattice constant $d = a + b$):</p>
<div class="math-display">
$$V(x) = \begin{cases} 0, & 0 < x < a \\ V_0, & -b < x < 0 \end{cases}$$
</div>
<p>In Region I ($0 < x < a$), $\psi_1(x) = A e^{i K x} + B e^{-i K x}$, where $K = \sqrt{2mE/\hbar^2}$.</p>
<p>In Region II ($-b < x < 0$), for $E < V_0$, $\psi_2(x) = C e^{Q x} + D e^{-Q x}$, where $Q = \sqrt{2m(V_0 - E)/\hbar^2}$.</p>

<h4>2. The Dirac Delta-Function Barrier Limit</h4>
<p>Taking the limit where the barriers become infinitely thin and tall ($b \to 0, V_0 \to \infty$) while their barrier area $P = \lim \frac{m V_0 b a}{\hbar^2}$ remains constant, matching wavefunctions and their derivatives across the boundary using Bloch's theorem yields the famous <strong>Kronig-Penney dispersion relation</strong>:</p>
<div class="math-display">
$$P \frac{\sin(K a)}{K a} + \cos(K a) = \cos(k a)$$
</div>
<p>where $P$ is the dimensionless <strong>barrier strength</strong> (representing the strength of the periodic crystal potential).</p>

<h4>3. Origin of Energy Bands and Band Gaps</h4>
<p>Because the right-hand side is $\cos(k a)$, real solutions for crystal wavevector $k$ exist <em>if and only if</em> the left-hand side satisfies:</p>
<div class="math-display">
$$-1 \le P \frac{\sin(K a)}{K a} + \cos(K a) \le +1$$
</div>
<ul>
<li><strong>Allowed Energy Bands:</strong> Values of $E = \frac{\hbar^2 K^2}{2m}$ where the condition is satisfied represent allowed energy bands.</li>
<li><strong>Forbidden Band Gaps ($E_g$):</strong> Energy ranges where the magnitude of the left-hand side exceeds unity ($> +1$ or $< -1$). No traveling Bloch waves can propagate through the crystal at these energies; electron waves undergo destructive interference and total Bragg reflection.</li>
<li><strong>Limits:</strong>
<ul>
<li>$P \to 0$ (Free Electrons): $\cos(Ka) = \cos(ka) \implies K = k \implies E = \frac{\hbar^2 k^2}{2m}$ (continuous parabolic spectrum).</li>
<li>$P \to \infty$ (Isolated Atoms): $\sin(Ka) = 0 \implies Ka = n\pi \implies E_n = \frac{n^2 \pi^2 \hbar^2}{2m a^2}$ (discrete bound atomic levels).</li>
</ul></li>
</ul>"""
        },
        {
            "id": "ssp-6-3",
            "title": "Zone Schemes & Nearly Free Electron (NFE) Approximation",
            "content": r"""<h4>1. Representation of Energy Bands: Zone Schemes</h4>
<p>Because energy eigenvalues satisfy $E_n(k + G) = E_n(k)$, the band structure can be represented in three equivalent representations:</p>
<ol>
<li><strong>Extended Zone Scheme:</strong> Band $n$ is plotted in the $n$-th Brillouin zone: band 1 in $[-\pi/a, +\pi/a]$, band 2 in $[-2\pi/a, -\pi/a] \cup [+\pi/a, +2\pi/a]$, etc. Most closely resembles the free-electron parabola $E = \hbar^2 k^2/2m$.</li>
<li><strong>Reduced Zone Scheme:</strong> All energy bands are mapped back into the First Brillouin Zone ($-\pi/a \le k \le +\pi/a$) by translating by appropriate reciprocal lattice vectors $G = 2\pi n / a$. Standard representation used in modern solid-state physics.</li>
<li><strong>Periodic (Repeated) Zone Scheme:</strong> The First Brillouin Zone dispersion is repeated periodically across all $k$-space with period $2\pi/a$. Convenient for visualizing semiclassical electron trajectories.</li>
</ol>

<h4>2. The Nearly Free Electron (NFE) Approximation</h4>
<p>When the periodic crystal potential $V(x)$ is weak compared to electron kinetic energies, it can be treated as a perturbation. Expanding the potential in a Fourier series over reciprocal lattice vectors $G$:</p>
<div class="math-display">
$$V(x) = \sum_{G} V_G e^{i G x} \quad (V_0 = 0)$$
</div>
<p>Away from the Brillouin zone boundaries, standard non-degenerate perturbation theory shifts energies insignificantly. However, near the zone boundary $k = \pm G/2$, the two unperturbed plane-wave states $|k\rangle$ and $|k - G\rangle$ are degenerate ($E_0(k) \approx E_0(k - G)$).</p>
<p>Applying degenerate perturbation theory with trial state $\psi = c_1 |k\rangle + c_2 |k - G\rangle$ yields the $2 \times 2$ secular equation:</p>
<div class="math-display">
$$\begin{pmatrix} E_0(k) - E & V_G \\ V_G^* & E_0(k - G) - E \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = 0$$
</div>
<p>At the exact zone boundary $k = G/2$, $E_0(k) = E_0(k - G) = \frac{\hbar^2 (G/2)^2}{2m} = E_0$:</p>
<div class="math-display">
$$(E_0 - E)^2 - |V_G|^2 = 0 \implies E_{\pm} = E_0 \pm |V_G|$$
</div>
<p>A band gap of magnitude $\Delta E_g = 2 |V_G|$ opens up at every Brillouin zone boundary. The standing wave solutions $\psi_+ \sim \cos(Gx/2)$ and $\psi_- \sim \sin(Gx/2)$ pile up electronic charge density either at the ion cores (lowering energy by $-|V_G|$) or midway between the ion cores (raising energy by $+|V_G|$).</p>"""
        },
        {
            "id": "ssp-6-4",
            "title": "The Tight-Binding Approximation (LCAO for Crystals)",
            "content": r"""<h4>1. Physical Foundation of Tight-Binding</h4>
<p>In contrast to the nearly free electron model, the <strong>Tight-Binding Approximation</strong> assumes that electrons are tightly bound to individual atomic cores, spending most of their time in localized atomic orbitals $\phi(\vec{r} - \vec{R}_n)$. When atoms are brought together into a crystal lattice, the overlap between adjacent atomic wavefunctions broadens discrete atomic energy levels into continuous energy bands.</p>

<h4>2. Formulation of the Bloch Sum</h4>
<p>To satisfy Bloch's theorem, the trial crystal wavefunction is formed as a coherent linear combination of atomic orbitals (LCAO) summed over all $N$ lattice sites $\vec{R}_n$:</p>
<div class="math-display">
$$\psi_k(\vec{r}) = \frac{1}{\sqrt{N}} \sum_{n} e^{i \vec{k}\cdot\vec{R}_n} \phi(\vec{r} - \vec{R}_n)$$
</div>

<h4>3. Derivation of 1D and 3D Tight-Binding Dispersion</h4>
<p>Evaluating the expectation value of the crystal Hamiltonian $\hat{H} = \hat{H}_{\text{atom}} + \Delta U(\vec{r})$:</p>
<div class="math-display">
$$E(k) = \frac{\langle \psi_k | \hat{H} | \psi_k \rangle}{\langle \psi_k | \psi_k \rangle} \approx \frac{\sum_{n, m} e^{i \vec{k}\cdot(\vec{R}_m - \vec{R}_n)} \int \phi^*(\vec{r} - \vec{R}_n) \hat{H} \phi(\vec{r} - \vec{R}_m) d^3r}{N}$$
</div>
<p>Retaining only on-site and nearest-neighbor matrix elements:</p>
<ul>
<li><strong>On-site atomic energy:</strong> $\varepsilon_0 = \int \phi^*(\vec{r}) \hat{H} \phi(\vec{r}) d^3r \approx - E_0 - \alpha$.</li>
<li><strong>Nearest-neighbor transfer (hopping) integral:</strong> $t = - \int \phi^*(\vec{r}) \hat{H} \phi(\vec{r} - \vec{a}) d^3r > 0$.</li>
</ul>
<p>For a <strong>one-dimensional chain</strong> with nearest-neighbor distance $a$:</p>
<div class="math-display">
$$E(k) = \varepsilon_0 - 2 t \cos(k a)$$
</div>
<p>The total bandwidth of the tight-binding band is $W = E_{\text{max}} - E_{\text{min}} = (\varepsilon_0 + 2t) - (\varepsilon_0 - 2t) = 4t$.</p>
<p>For a <strong>3D Simple Cubic lattice</strong> with nearest-neighbor spacing $a$:</p>
<div class="math-display">
$$E(\vec{k}) = \varepsilon_0 - 2 t [\cos(k_x a) + \cos(k_y a) + \cos(k_z a)] \quad (\text{Bandwidth } W = 12 t)$$
</div>"""
        },
        {
            "id": "ssp-6-5",
            "title": "Semiclassical Electron Dynamics, Effective Mass & Positive Holes",
            "simulation": "ssp-effective-mass-sim",
            "content": r"""<h4>1. Semiclassical Equations of Motion for Bloch Electrons</h4>
<p>An electron in an energy band $E_n(\vec{k})$ is described by a localized wave packet centered at position $\vec{r}$ and mean wavevector $\vec{k}$. Its dynamical evolution under external electromagnetic fields $\vec{E}$ and $\vec{B}$ is governed by the <strong>semiclassical equations of motion</strong>:</p>
<ol>
<li><strong>Group Velocity:</strong>
<div class="math-display">
$$\vec{v}(\vec{k}) = \frac{1}{\hbar} \nabla_{\vec{k}} E(\vec{k})$$
</div></li>
<li><strong>Rate of Change of Crystal Momentum:</strong>
<div class="math-display">
$$\hbar \frac{d\vec{k}}{dt} = \vec{F}_{\text{ext}} = - e [\vec{E} + \vec{v}(\vec{k}) \times \vec{B}]$$
</div></li>
</ol>

<h4>2. Derivation of the Effective Mass Tensor $m^*$</h4>
<p>Differentiating the group velocity with respect to time:</p>
<div class="math-display">
$$\frac{d\vec{v}}{dt} = \frac{1}{\hbar} \frac{d}{dt} \nabla_{\vec{k}} E(\vec{k}) = \frac{1}{\hbar} \sum_{j} \left( \frac{\partial^2 E}{\partial k_i \partial k_j} \right) \frac{dk_j}{dt}$$
</div>
<p>Substituting $\hbar \frac{dk_j}{dt} = F_j$:</p>
<div class="math-display">
$$\frac{dv_i}{dt} = \sum_{j} \left( \frac{1}{\hbar^2} \frac{\partial^2 E}{\partial k_i \partial k_j} \right) F_j = \sum_{j} \left(\frac{1}{m^*}\right)_{ij} F_j$$
</div>
<p>Comparing with Newton's second law $\vec{a} = (m^*)^{-1} \vec{F}$ defines the <strong>Effective Mass Tensor</strong> $(m^*)_{ij}$:</p>
<div class="math-display">
$$\left(\frac{1}{m^*}\right)_{ij} = \frac{1}{\hbar^2} \frac{\partial^2 E(\vec{k})}{\partial k_i \partial k_j}$$
</div>
<p>In an isotropic 1D band: $m^* = \hbar^2 / \left(\frac{d^2E}{dk^2}\right)$.</p>
<ul>
<li>Near the <strong>bottom of a band</strong> ($\frac{d^2E}{dk^2} > 0$): $m^* > 0$. The electron accelerates in the direction of the applied electric force like a free electron.</li>
<li>Near the <strong>top of a band</strong> ($\frac{d^2E}{dk^2} < 0$): $m^* < 0$. The electron accelerates in the direction <em>opposite</em> to the external force because of Bragg reflections from the lattice potential.</li>
</ul>

<h4>3. The Concept of Positive Holes</h4>
<p>In a nearly filled band, the absence of an electron from a state with wavevector $\vec{k}_e$, energy $E_e$, and charge $-e$ is described as a quasiparticle called a <strong>hole</strong>:</p>
<ul>
<li><strong>Wavevector:</strong> $\vec{k}_h = - \vec{k}_e$</li>
<li><strong>Energy:</strong> $E_h(\vec{k}_h) = - E_e(\vec{k}_e)$</li>
<li><strong>Velocity:</strong> $\vec{v}_h = \vec{v}_e$</li>
<li><strong>Charge:</strong> $q_h = + e$ (positive charge)</li>
<li><strong>Effective Mass:</strong> $m_h^* = - m_e^* > 0$ (positive effective mass at the band top)</li>
</ul>
<p>Treating valence band transport in terms of positive holes simplifies the quantum statistical mechanics of semiconductors and metals.</p>"""
        }
    ],
    "problems": [
        {
            "id": "ssp-p-6-1",
            "title": "Energy Band Gap Opening in the Nearly Free Electron Model",
            "statement": "An electron moves in a 1D crystal with lattice spacing $a = 3.0 \\text{ \u00c5}$ under a weak periodic potential $V(x) = 2 V_1 \\cos(2\\pi x / a)$ with Fourier amplitude $V_1 = 0.75 \\text{ eV}$. (a) Calculate the unperturbed free-electron kinetic energy $E_0$ at the First Brillouin Zone boundary $k = \\pi / a$. (b) Determine the energy values $E_+$ and $E_-$ at the zone boundary and the magnitude of the band gap $\\Delta E_g$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Reciprocal Lattice Vector G",
                    "math": r"G = \frac{2\pi}{a} = \frac{2\pi}{3.0 \times 10^{-10}\text{ m}} \approx 2.094 \times 10^{10}\text{ m}^{-1} \implies k_{\text{edge}} = \frac{G}{2} = \frac{\pi}{a} \approx 1.047 \times 10^{10}\text{ m}^{-1}",
                    "explanation": "Compute the First Brillouin Zone boundary wavevector."
                },
                {
                    "stepName": "Step 2: Calculate the Unperturbed Free-Electron Energy E_0",
                    "math": r"E_0 = \frac{\hbar^2 k_{\text{edge}}^2}{2m} = \frac{(1.0546 \times 10^{-34}\text{ J}\cdot\text{s})^2 (1.047 \times 10^{10}\text{ m}^{-1})^2}{2(9.109 \times 10^{-31}\text{ kg})} = \frac{1.2185 \times 10^{-47}}{1.8218 \times 10^{-30}}\text{ J} \approx 6.688 \times 10^{-19}\text{ J} \approx 4.174\text{ eV}",
                    "explanation": "Compute unperturbed kinetic energy in electron-volts."
                },
                {
                    "stepName": "Step 3: Calculate the Band Gap Delta E_g",
                    "math": r"\Delta E_g = 2 |V_G| = 2 V_1 = 2 \times 0.75\text{ eV} = 1.50\text{ eV}",
                    "explanation": "In degenerate perturbation theory, the band gap equals twice the Fourier component of the potential."
                },
                {
                    "stepName": "Step 4: Determine the Band Edge Energies E_+ and E_-",
                    "math": r"E_- = E_0 - V_1 = 4.174\text{ eV} - 0.75\text{ eV} = 3.424\text{ eV}, \quad E_+ = E_0 + V_1 = 4.174\text{ eV} + 0.75\text{ eV} = 4.924\text{ eV}",
                    "explanation": "The lower band terminates at E_- and the upper band begins at E_+."
                }
            ],
            "answer": "E_0 = 4.17 \\text{ eV}, \\quad \\Delta E_g = 1.50 \\text{ eV}, \\quad E_- = 3.42 \\text{ eV}, \\quad E_+ = 4.92 \\text{ eV}"
        },
        {
            "id": "ssp-p-6-2",
            "title": "Effective Mass and Group Velocity in a 1D Tight-Binding Band",
            "statement": "The energy dispersion of a 1D tight-binding conduction band is given by $E(k) = - E_0 - 2t \\cos(ka)$, where $E_0 = 1.20 \\text{ eV}$, hopping integral $t = 0.85 \\text{ eV}$, and lattice spacing $a = 2.50 \\text{ \u00c5}$. (a) Calculate the total bandwidth $W$. (b) Derive the expression for effective mass $m^*(k)$ and evaluate its numerical value in units of free electron mass $m_0$ at the band bottom ($k = 0$) and band top ($k = \\pi/a$). (c) Find the wavevector $k$ at which the electron group velocity $v_g$ reaches its maximum value.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Total Bandwidth W",
                    "math": r"W = E_{\text{max}} - E_{\text{min}} = 4t = 4 \times 0.85\text{ eV} = 3.40\text{ eV}",
                    "explanation": "In a 1D tight-binding cosine band, the bandwidth equals 4 times the transfer integral t."
                },
                {
                    "stepName": "Step 2: Derive the Effective Mass Formula",
                    "math": r"\frac{dE}{dk} = 2 t a \sin(k a) \implies \frac{d^2E}{dk^2} = 2 t a^2 \cos(k a) \implies m^*(k) = \frac{\hbar^2}{2 t a^2 \cos(k a)}",
                    "explanation": "Differentiate E(k) twice with respect to wavevector k."
                },
                {
                    "stepName": "Step 3: Evaluate m* at k = 0 (Band Bottom)",
                    "math": r"m^*(0) = \frac{\hbar^2}{2 t a^2} = \frac{(1.0546 \times 10^{-34}\text{ J}\cdot\text{s})^2}{2 \times (0.85 \times 1.6022 \times 10^{-19}\text{ J}) \times (2.50 \times 10^{-10}\text{ m})^2} = \frac{1.1122 \times 10^{-68}}{2.7237 \times 10^{-19} \times 6.25 \times 10^{-20}} = \frac{1.1122 \times 10^{-68}}{1.7023 \times 10^{-38}}\text{ kg} \approx 6.533 \times 10^{-31}\text{ kg} \implies \frac{m^*(0)}{m_0} = \frac{6.533 \times 10^{-31}}{9.109 \times 10^{-31}} \approx 0.717",
                    "explanation": "Substitute numerical values to find the effective mass at k = 0."
                },
                {
                    "stepName": "Step 4: Evaluate m* at k = pi / a (Band Top)",
                    "math": r"m^*(\pi/a) = \frac{\hbar^2}{2 t a^2 \cos(\pi)} = - m^*(0) = - 0.717 m_0",
                    "explanation": "At the zone boundary, cos(pi) = -1, yielding a negative effective mass corresponding to a positive hole mass m_h* = +0.717 m_0."
                },
                {
                    "stepName": "Step 5: Determine Maximum Group Velocity",
                    "math": r"v_g(k) = \frac{1}{\hbar}\frac{dE}{dk} = \frac{2ta}{\hbar}\sin(ka) \implies \left. v_g \right|_{\text{max}} \text{ occurs when } \sin(ka) = 1 \implies ka = \frac{\pi}{2} \implies k = \frac{\pi}{2a}",
                    "explanation": "The maximum group velocity occurs at the inflection point k = pi / (2a) where effective mass diverges to infinity."
                }
            ],
            "answer": "W = 3.40 \\text{ eV}, \\quad m^*(0) = +0.717 m_0, \\quad m^*(\\pi/a) = -0.717 m_0, \\quad k_{\\text{max}} = \\pi / (2a)"
        },
        {
            "id": "ssp-p-6-3",
            "title": "Period of Bloch Oscillations in an External Electric Field",
            "statement": "An electron in a crystal with lattice constant $a = 3.50 \\text{ \u00c5}$ is subjected to a uniform external electric field $E_x = 1.50 \\times 10^5 \\text{ V/m}$. Assuming negligible scattering (mean free path exceeds the oscillation length): (a) Calculate the rate of change of crystal wavevector $dk/dt$. (b) Determine the time period $T_B$ and cyclical frequency $\\nu_B$ of the resulting Bloch oscillations.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Rate of Change of Wavevector dk / dt",
                    "math": r"\hbar \frac{dk}{dt} = - e E_x \implies \left|\frac{dk}{dt}\right| = \frac{e E_x}{\hbar} = \frac{(1.6022 \times 10^{-19}\text{ C})(1.50 \times 10^5\text{ V/m})}{1.0546 \times 10^{-34}\text{ J}\cdot\text{s}} \approx 2.279 \times 10^{20}\text{ m}^{-1}\cdot\text{s}^{-1}",
                    "explanation": "Apply the semiclassical equation of motion in an electric field."
                },
                {
                    "stepName": "Step 2: Determine the Wavevector Traversed in One Full Oscillation",
                    "math": r"\Delta k = \frac{2\pi}{a} = \frac{2\pi}{3.50 \times 10^{-10}\text{ m}} \approx 1.795 \times 10^{10}\text{ m}^{-1}",
                    "explanation": "One full cycle corresponds to traversing the entire First Brillouin Zone of width 2 pi / a."
                },
                {
                    "stepName": "Step 3: Calculate the Bloch Oscillation Period T_B",
                    "math": r"T_B = \frac{\Delta k}{|dk/dt|} = \frac{2\pi \hbar}{e E_x a} = \frac{h}{e E_x a} = \frac{6.626 \times 10^{-34}\text{ J}\cdot\text{s}}{(1.6022 \times 10^{-19}\text{ C})(1.50 \times 10^5\text{ V/m})(3.50 \times 10^{-10}\text{ m})} = \frac{6.626 \times 10^{-34}}{8.4116 \times 10^{-24}}\text{ s} \approx 7.877 \times 10^{-11}\text{ s} = 78.8\text{ ps}",
                    "explanation": "Evaluate the Bloch period T_B = h / (e E a)."
                },
                {
                    "stepName": "Step 4: Calculate the Bloch Oscillation Frequency nu_B",
                    "math": r"\nu_B = \frac{1}{T_B} = \frac{1}{7.877 \times 10^{-11}\text{ s}} \approx 1.269 \times 10^{10}\text{ Hz} = 12.7\text{ GHz}",
                    "explanation": "Inverted period gives the Bloch oscillation frequency in the microwave / terahertz regime."
                }
            ],
            "answer": "T_B = 78.8 \\text{ ps}, \\quad \\nu_B = 12.7 \\text{ GHz}"
        }
    ]
}

with open("ssp_u5.json", "w") as f:
    json.dump(u5, f, indent=2)
print("ssp_u5.json created successfully!")

with open("ssp_u6.json", "w") as f:
    json.dump(u6, f, indent=2)
print("ssp_u6.json created successfully!")
