import json

# ==========================================
# UNIT 7: Dielectric Properties, Plasmons & Optical Phenomena
# ==========================================
u7 = {
    "unitNumber": 7,
    "unitId": "unit7-dielectric-properties",
    "title": "Dielectric Properties, Plasmons & Optical Phenomena",
    "description": "Comprehensive macroscopic and microscopic electrodynamics of solids: macroscopic field vs local Lorentz field, polarizabilities, Clausius-Mossotti relation, AC complex permittivity, Debye dielectric relaxation, plasma oscillations, plasma frequency, Thomas-Fermi screening, ferroelectricity, piezoelectricity, and Kramers-Kronig optical relations.",
    "sections": [
        {
            "id": "ssp-7-1",
            "title": "Macroscopic Electric Field & The Microscopic Local Lorentz Field",
            "content": r"""<h4>1. Macroscopic Polarization $\vec{P}$ and Electric Displacement $\vec{D}$</h4>
<p>In a dielectric solid subjected to an external electrostatic field, bound charges undergo micro-displacements, creating a volume dipole moment density known as the <strong>polarization vector</strong> $\vec{P}$:</p>
<div class="math-display">
$$\vec{P} = \lim_{\Delta V \to 0} \frac{1}{\Delta V} \sum_{i \in \Delta V} \vec{p}_i$$
</div>
<p>The macroscopic electric displacement $\vec{D}$ and macroscopic electric field $\vec{E}$ are related in linear, isotropic media by:</p>
<div class="math-display">
$$\vec{D} = \varepsilon_0 \vec{E} + \vec{P} = \varepsilon_0 (1 + \chi_e) \vec{E} = \varepsilon_0 \varepsilon_r \vec{E}$$
</div>
<p>where $\chi_e$ is the electric susceptibility and $\varepsilon_r = 1 + \chi_e$ is the relative dielectric permittivity.</p>

<h4>2. Derivation of the Local Lorentz Field $\vec{E}_{\text{loc}}$</h4>
<p>The actual electric field acting on an individual atom inside a condensed solid—the <strong>local microscopic field</strong> $\vec{E}_{\text{loc}}$—is not equal to the macroscopic Maxwell average field $\vec{E}$, because the atom is surrounded by polarized atomic neighbors. Following H. A. Lorentz, we construct a spherical cavity of microscopic radius $R_{\text{cav}}$ centered at the target atom:</p>
<div class="math-display">
$$\vec{E}_{\text{loc}} = \vec{E}_0 + \vec{E}_1 + \vec{E}_2 + \vec{E}_3$$
</div>
<ol>
<li>$\vec{E}_0$: External field produced by fixed external charges.</li>
<li>$\vec{E}_1$: Depolarization field produced by the macroscopic polarization charges on the external outer boundaries of the dielectric specimen ($\vec{E}_0 + \vec{E}_1 = \vec{E}$, the macroscopic field).</li>
<li>$\vec{E}_2$: Surface polarization charge field on the spherical cavity boundary. Integrating the bound surface charge density $\sigma_b = - \vec{P} \cdot \hat{n} = P \cos\theta$ over the spherical surface yields:
<div class="math-display">
$$\vec{E}_2 = \frac{1}{4\pi\varepsilon_0} \int_0^\pi \frac{(P \cos\theta)(\cos\theta)}{R_{\text{cav}}^2} (2\pi R_{\text{cav}}^2 \sin\theta d\theta) \hat{z} = \frac{\vec{P}}{3\varepsilon_0}$$
</div></li>
<li>$\vec{E}_3$: Microscopic field produced by individual dipoles situated <em>inside</em> the cavity. For sites possessing cubic point-group symmetry (or random isotropic liquids), $\vec{E}_3 \equiv 0$.</li>
</ol>
<p>Summing these terms yields the celebrated <strong>Lorentz Local Field Relation</strong>:</p>
<div class="math-display">
$$\vec{E}_{\text{loc}} = \vec{E} + \frac{\vec{P}}{3\varepsilon_0}$$
</div>"""
        },
        {
            "id": "ssp-7-2",
            "title": "Atomic Polarizabilities & The Clausius-Mossotti Relation",
            "simulation": "ssp-clausius-mossotti-sim",
            "content": r"""<h4>1. Mechanisms of Microscopic Dielectric Polarization</h4>
<p>The total microscopic electric dipole moment $\vec{p}$ induced in an individual atom or molecule is directly proportional to the local field: $\vec{p} = \alpha \vec{E}_{\text{loc}}$, where $\alpha$ is the <strong>total polarizability</strong>, composed of three fundamental mechanisms:</p>
<ol>
<li><strong>Electronic Polarizability ($\alpha_e$):</strong> Displacement of the negative valence electron cloud relative to the positive nucleus ($\sim 10^{-40}\text{ C}\cdot\text{m}^2/\text{V}$). Resonant at optical frequencies ($\sim 10^{15}\text{ Hz}$).</li>
<li><strong>Ionic (Atomic) Polarizability ($\alpha_i$):</strong> Relative displacement of positive and negative ions in ionic crystals ($\sim 10^{-39}\text{ C}\cdot\text{m}^2/\text{V}$). Resonant at infrared phonon frequencies ($\sim 10^{13}\text{ Hz}$).</li>
<li><strong>Dipolar (Orientation) Polarizability ($\alpha_d$):</strong> Thermal realignment of permanent molecular electric dipoles $\vec{p}_0$ against thermal randomization. Described by the Langevin-Debye formula:
<div class="math-display">
$$\alpha_d = \frac{p_0^2}{3 k_B T}$$
</div>
<p>Active at radio and microwave frequencies ($\sim 10^9 - 10^{11}\text{ Hz}$), vanishing at higher frequencies.</p></li>
</ol>
<p>The total polarizability is: $\alpha = \alpha_e + \alpha_i + \frac{p_0^2}{3 k_B T}$.</p>

<h4>2. Derivation of the Clausius-Mossotti Relation</h4>
<p>For a non-polar dielectric with number density $N$ atoms per unit volume, the macroscopic polarization is $\vec{P} = N \vec{p} = N \alpha \vec{E}_{\text{loc}}$. Substituting the Lorentz local field $\vec{E}_{\text{loc}} = \vec{E} + \frac{\vec{P}}{3\varepsilon_0}$:</p>
<div class="math-display">
$$\vec{P} = N \alpha \left( \vec{E} + \frac{\vec{P}}{3\varepsilon_0} \right) \implies \vec{P} \left( 1 - \frac{N\alpha}{3\varepsilon_0} \right) = N \alpha \vec{E}$$
</div>
<p>Recalling the macroscopic definition $\vec{P} = \varepsilon_0 (\varepsilon_r - 1) \vec{E}$, we equate:</p>
<div class="math-display">
$$\varepsilon_0 (\varepsilon_r - 1) = \frac{N \alpha}{1 - \frac{N\alpha}{3\varepsilon_0}} \implies \frac{\varepsilon_r - 1}{\varepsilon_r + 2} = \frac{N \alpha}{3 \varepsilon_0}$$
</div>
<p>This is the <strong>Clausius-Mossotti Relation</strong>. It links a purely macroscopic, experimentally measurable property—the relative dielectric constant $\varepsilon_r$—directly to the microscopic atomic polarizability $\alpha$ and atomic density $N$. At optical frequencies where $\varepsilon_r = n^2$ ($n$ is the refractive index), it is called the <strong>Lorentz-Lorenz equation</strong>.</p>"""
        },
        {
            "id": "ssp-7-3",
            "title": "AC Dielectric Response, Debye Relaxation & Dielectric Loss",
            "content": r"""<h4>1. Complex Dielectric Function $\tilde{\varepsilon}(\omega)$</h4>
<p>Under an alternating sinusoidal electric field $\vec{E}(t) = \vec{E}_0 e^{-i\omega t}$, dipolar and ionic reorientations exhibit a phase lag relative to the driving field due to internal friction and damping. The dielectric response becomes a complex function of frequency:</p>
<div class="math-display">
$$\tilde{\varepsilon}(\omega) = \varepsilon_1(\omega) - i \varepsilon_2(\omega)$$
</div>
<ul>
<li><strong>Real Part $\varepsilon_1(\omega)$:</strong> Quantifies reversible electrostatic energy storage (capacitance).</li>
<li><strong>Imaginary Part $\varepsilon_2(\omega)$:</strong> Quantifies irreversible energy dissipation and dielectric heating loss.</li>
</ul>
<p>The <strong>Loss Tangent</strong> (or dissipation factor) is defined as:</p>
<div class="math-display">
$$\tan\delta = \frac{\varepsilon_2(\omega)}{\varepsilon_1(\omega)}$$
</div>

<h4>2. The Debye Relaxation Equations</h4>
<p>Peter Debye modeled the time-dependent relaxation of orientation polarization following the removal of a field as an exponential decay: $\frac{d\vec{P}_d}{dt} = - \frac{\vec{P}_d}{\tau_D}$, where $\tau_D$ is the <strong>Debye relaxation time</strong>. Solving under harmonic driving yields:</p>
<div class="math-display">
$$\tilde{\varepsilon}(\omega) = \varepsilon_\infty + \frac{\varepsilon_s - \varepsilon_\infty}{1 - i \omega \tau_D}$$
</div>
<p>Separating into real and imaginary components yields the <strong>Debye equations</strong>:</p>
<div class="math-display">
$$\varepsilon_1(\omega) = \varepsilon_\infty + \frac{\varepsilon_s - \varepsilon_\infty}{1 + \omega^2 \tau_D^2}, \quad \varepsilon_2(\omega) = \frac{(\varepsilon_s - \varepsilon_\infty) \omega \tau_D}{1 + \omega^2 \tau_D^2}$$
</div>
<p>where $\varepsilon_s$ is the static low-frequency dielectric constant ($\omega \tau_D \ll 1$) and $\varepsilon_\infty$ is the high-frequency electronic limit ($\omega \tau_D \gg 1$). The dielectric absorption loss $\varepsilon_2(\omega)$ reaches a sharp maximum at the resonance condition $\omega = 1/\tau_D$.</p>"""
        },
        {
            "id": "ssp-7-4",
            "title": "Plasmons, Plasma Frequency & Thomas-Fermi Screening",
            "simulation": "ssp-plasma-frequency-sim",
            "content": r"""<h4>1. Plasma Oscillations of the Free Electron Gas</h4>
<p>Consider a free electron gas of density $n$ in a metal. If the entire electron cloud is displaced collectively as a rigid slab by a distance $u$ along $x$ relative to the positive ion core background, a surface charge density $\sigma = \pm n e u$ accumulates on the opposing ends of the slab. This generates an internal restoring electric field:</p>
<div class="math-display">
$$E = \frac{\sigma}{\varepsilon_0} = \frac{n e u}{\varepsilon_0}$$
</div>
<p>The classical equation of motion for each electron in the displaced cloud is:</p>
<div class="math-display">
$$m \frac{d^2 u}{dt^2} = - e E = - \frac{n e^2}{\varepsilon_0} u \implies \frac{d^2 u}{dt^2} + \left(\frac{n e^2}{\varepsilon_0 m}\right) u = 0$$
</div>
<p>This is a simple harmonic oscillator. Collective longitudinal density oscillations of the electron gas occur at the <strong>Plasma Frequency</strong> $\omega_p$:</p>
<div class="math-display">
$$\omega_p = \sqrt{\frac{n e^2}{\varepsilon_0 m}}$$
</div>
<p>A quantum of plasma oscillation is a quasiparticle called a <strong>plasmon</strong>, carrying energy $\hbar \omega_p \sim 5 - 20\text{ eV}$ in typical metals.</p>

<h4>2. Dielectric Function of a Metal & Ultraviolet Transparency</h4>
<p>Neglecting damping at optical frequencies ($\omega \tau \gg 1$), the Drude dielectric function of a metal reduces to:</p>
<div class="math-display">
$$\varepsilon(\omega) = 1 - \frac{\omega_p^2}{\omega^2}$$
</div>
<ul>
<li><strong>For $\omega < \omega_p$:</strong> $\varepsilon(\omega) < 0$. The refractive index $n = \sqrt{\varepsilon}$ is purely imaginary ($n = i \kappa$), causing total reflection ($R \approx 100\%$). Metals act as mirrors for visible light.</li>
<li><strong>For $\omega > \omega_p$:</strong> $\varepsilon(\omega) > 0$. The refractive index is real and positive. Electromagnetic waves propagate freely through the metal without reflection: the metal undergoes an <strong>ultraviolet transparency transition</strong>.</li>
</ul>

<h4>3. Thomas-Fermi Electrostatic Screening</h4>
<p>When a static test charge $Q$ is embedded in a degenerate electron gas, conduction electrons rearrange to screen its Coulomb potential. In the <strong>Thomas-Fermi approximation</strong>, the bare Coulomb potential $V_0(r) = \frac{Q}{4\pi\varepsilon_0 r}$ is screened exponentially:</p>
<div class="math-display">
$$V(r) = \frac{Q}{4\pi\varepsilon_0 r} e^{- k_{TF} r} = \frac{Q}{4\pi\varepsilon_0 r} e^{- r / \lambda_{TF}}$$
</div>
<p>where the <strong>Thomas-Fermi screening wavevector</strong> $k_{TF}$ and screening length $\lambda_{TF}$ are given by:</p>
<div class="math-display">
$$k_{TF}^2 = \frac{e^2}{\varepsilon_0} g(E_F) = \frac{3 n e^2}{2 \varepsilon_0 E_F} \implies \lambda_{TF} = \frac{1}{k_{TF}} = \sqrt{\frac{2\varepsilon_0 E_F}{3 n e^2}} \sim 0.5 - 1.0\text{ \AA}$$
</div>
<p>In typical metals, Coulomb interactions are completely screened within an atomic radius, explaining why electron-electron repulsion can often be neglected.</p>"""
        },
        {
            "id": "ssp-7-5",
            "title": "Ferroelectricity, Piezoelectricity & Kramers-Kronig Relations",
            "content": r"""<h4>1. Ferroelectricity & The Soft Phonon Mode</h4>
<p>A <strong>ferroelectric crystal</strong> (e.g., Barium Titanate $\text{BaTiO}_3$, $\text{PbTiO}_3$) exhibits a spontaneous, reversible electric polarization $\vec{P}_s$ in the absence of an applied electric field below a critical <strong>Curie temperature</strong> $T_C$. Above $T_C$, the crystal undergoes a structural phase transition to a paraelectric phase governed by the <strong>Curie-Weiss law</strong>:</p>
<div class="math-display">
$$\varepsilon_r = \varepsilon_0 + \frac{C}{T - T_C} \quad (T > T_C)$$
</div>
<p>In the Lyddane-Sachs-Teller (LST) dynamical theory, the divergence of $\varepsilon_r(0)$ as $T \to T_C$ is driven by the condensation of a transverse optical phonon frequency, the <strong>soft mode</strong>:</p>
<div class="math-display">
$$\omega_{TO}^2(T) = \gamma (T - T_C) \to 0 \quad \text{as } T \to T_C^+$$
</div>

<h4>2. Piezoelectricity & Pyroelectricity</h4>
<ul>
<li><strong>Piezoelectric Effect:</strong> Induction of electric polarization $\vec{P}$ proportional to applied mechanical stress $\sigma$ ($P_i = d_{ijk} \sigma_{jk}$), and conversely mechanical strain upon application of an electric field. Occurs exclusively in non-centrosymmetric crystal classes ($20$ of the $32$ point groups). Canonical example: Quartz ($\text{SiO}_2$), PZT.</li>
<li><strong>Pyroelectric Effect:</strong> Spontaneous polarization changes as a function of temperature: $\Delta P_i = p_i \Delta T$. All pyroelectric materials are piezoelectric, but not all piezoelectrics are pyroelectric.</li>
</ul>

<h4>3. The Kramers-Kronig Dispersion Relations</h4>
<p>By the fundamental principle of <strong>causality</strong> (an electric displacement response $\vec{D}(t)$ cannot precede the applied electric field $\vec{E}(t)$), Cauchy's residue theorem applied in the complex frequency plane establishes the <strong>Kramers-Kronig relations</strong> connecting the real and imaginary parts of the dielectric function:</p>
<div class="math-display">
$$\varepsilon_1(\omega) - 1 = \frac{2}{\pi} \mathcal{P} \int_0^\infty \frac{\omega' \varepsilon_2(\omega')}{\omega'^2 - \omega^2} d\omega'$$
</div>
<div class="math-display">
$$\varepsilon_2(\omega) = - \frac{2\omega}{\pi} \mathcal{P} \int_0^\infty \frac{\varepsilon_1(\omega') - 1}{\omega'^2 - \omega^2} d\omega'$$
</div>
<p>where $\mathcal{P}$ denotes Cauchy's principal value. Measuring the optical absorption spectrum $\varepsilon_2(\omega)$ across all frequencies allows exact determination of the real dielectric permittivity $\varepsilon_1(\omega)$ and refractive index without adjustable parameters.</p>"""
        }
    ],
    "problems": [
        {
            "id": "ssp-p-7-1",
            "title": "Clausius-Mossotti Polarizability Calculation for Solid Germanium",
            "statement": "Solid Germanium crystallizes in the diamond structure with lattice constant $a = 5.658 \\text{ \u00c5}$ and measured static dielectric constant $\\varepsilon_r = 16.0$. (a) Calculate the atomic number density $N$ of Germanium in atoms per $\\text{m}^3$. (b) Using the Clausius-Mossotti relation, determine the electronic polarizability $\\alpha$ of a Germanium atom in SI units ($\\text{C}\\cdot\\text{m}^2/\\text{V}$) and in volume units ($\\text{\u00c5}^3$).",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Atomic Number Density N",
                    "math": r"N = \frac{8}{a^3} = \frac{8}{(5.658 \times 10^{-10}\text{ m})^3} = \frac{8}{1.8113 \times 10^{-28}\text{ m}^3} \approx 4.417 \times 10^{28}\text{ atoms/m}^3",
                    "explanation": "Diamond cubic conventional unit cell contains 8 atoms."
                },
                {
                    "stepName": "Step 2: Solve the Clausius-Mossotti Equation for Polarizability alpha",
                    "math": r"\frac{\varepsilon_r - 1}{\varepsilon_r + 2} = \frac{N \alpha}{3\varepsilon_0} \implies \alpha = \frac{3\varepsilon_0}{N} \left( \frac{\varepsilon_r - 1}{\varepsilon_r + 2} \right)",
                    "explanation": "Isolate the atomic polarizability alpha."
                },
                {
                    "stepName": "Step 3: Evaluate the Dimensionless Dielectric Factor",
                    "math": r"\frac{\varepsilon_r - 1}{\varepsilon_r + 2} = \frac{16.0 - 1}{16.0 + 2} = \frac{15.0}{18.0} = \frac{5}{6} \approx 0.8333",
                    "explanation": "Compute (epsilon_r - 1) / (epsilon_r + 2)."
                },
                {
                    "stepName": "Step 4: Compute Polarizability in SI Units",
                    "math": r"\alpha = \frac{3 \times (8.8542 \times 10^{-12}\text{ F/m})}{4.417 \times 10^{28}\text{ m}^{-3}} \times \left(\frac{5}{6}\right) = \frac{2.6563 \times 10^{-11} \times 0.8333}{4.417 \times 10^{28}} \approx 5.011 \times 10^{-40}\text{ C}\cdot\text{m}^2/\text{V}",
                    "explanation": "Evaluate the numerical value in SI units."
                },
                {
                    "stepName": "Step 5: Convert Polarizability to Polarizability Volume alpha'",
                    "math": r"\alpha' = \frac{\alpha}{4\pi\varepsilon_0} = \frac{5.011 \times 10^{-40}\text{ C}\cdot\text{m}^2/\text{V}}{4\pi \times (8.8542 \times 10^{-12}\text{ F/m})} \approx 4.504 \times 10^{-30}\text{ m}^3 = 4.504\text{ \AA}^3",
                    "explanation": "Compute the polarizability volume alpha' = alpha / (4 pi epsilon_0)."
                }
            ],
            "answer": "N = 4.42 \\times 10^{28} \\text{ m}^{-3}, \\quad \\alpha = 5.01 \\times 10^{-40} \\text{ C}\\cdot\\text{m}^2/\\text{V}, \\quad \\alpha' = 4.50 \\text{ \u00c5}^3"
        },
        {
            "id": "ssp-p-7-2",
            "title": "Plasma Frequency and Ultraviolet Transmission Edge of Aluminum",
            "statement": "Aluminum is a trivalent metal ($Z_{\\text{val}} = 3$) with atomic mass $M = 26.98 \\text{ g/mol}$ and density $\\rho = 2.70 \\text{ g/cm}^3$. (a) Calculate the free electron density $n$. (b) Determine the plasma frequency $\\omega_p$, the plasmon energy $\\hbar \\omega_p$ in $\\text{eV}$, and the critical ultraviolet transparency threshold wavelength $\\lambda_p$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Conduction Electron Density n",
                    "math": r"n = Z_{\text{val}} \frac{\rho N_A}{M} = 3 \times \frac{(2.70 \times 10^6\text{ g/m}^3)(6.022 \times 10^{23}\text{ mol}^{-1})}{26.98\text{ g/mol}} = 3 \times (6.026 \times 10^{28}) \approx 1.808 \times 10^{29}\text{ electrons/m}^3",
                    "explanation": "Each aluminum atom contributes 3 conduction electrons."
                },
                {
                    "stepName": "Step 2: Calculate the Angular Plasma Frequency omega_p",
                    "math": r"\omega_p = \sqrt{\frac{n e^2}{\varepsilon_0 m}} = \sqrt{\frac{(1.808 \times 10^{29})(1.6022 \times 10^{-19})^2}{(8.8542 \times 10^{-12})(9.109 \times 10^{-31})}} = \sqrt{\frac{4.641 \times 10^{-9}}{8.065 \times 10^{-42}}} = \sqrt{5.754 \times 10^{32}} \approx 2.399 \times 10^{16}\text{ rad/s}",
                    "explanation": "Evaluate the plasma frequency formula."
                },
                {
                    "stepName": "Step 3: Calculate the Plasmon Energy in eV",
                    "math": r"E_p = \hbar \omega_p = \frac{(1.0546 \times 10^{-34}\text{ J}\cdot\text{s})(2.399 \times 10^{16}\text{ rad/s})}{1.6022 \times 10^{-19}\text{ J/eV}} \approx \frac{2.530 \times 10^{-18}\text{ J}}{1.6022 \times 10^{-19}\text{ J/eV}} \approx 15.79\text{ eV}",
                    "explanation": "Convert plasmon energy to electron-volts."
                },
                {
                    "stepName": "Step 4: Calculate the Critical Transparency Wavelength lambda_p",
                    "math": r"\lambda_p = \frac{2\pi c}{\omega_p} = \frac{2\pi \times (2.9979 \times 10^8\text{ m/s})}{2.399 \times 10^{16}\text{ s}^{-1}} \approx 7.852 \times 10^{-8}\text{ m} = 78.5\text{ nm}",
                    "explanation": "Light with wavelength shorter than 78.5 nm (deep vacuum ultraviolet) passes freely through aluminum."
                }
            ],
            "answer": "\\omega_p = 2.40 \\times 10^{16} \\text{ rad/s}, \\quad \\hbar\\omega_p = 15.79 \\text{ eV}, \\quad \\lambda_p = 78.5 \\text{ nm}"
        },
        {
            "id": "ssp-p-7-3",
            "title": "Thomas-Fermi Screening Length for Conduction Electrons in Copper",
            "statement": "Copper has a conduction electron density $n = 8.49 \\times 10^{28} \\text{ m}^{-3}$ and Fermi energy $E_F = 7.04 \\text{ eV} = 1.128 \\times 10^{-18} \\text{ J}$. (a) Calculate the Thomas-Fermi screening wavevector $k_{\\text{TF}}$. (b) Determine the Thomas-Fermi screening length $\\lambda_{\\text{TF}}$ in Angstroms, and compare it with the interatomic spacing $a = 3.615 \\text{ \u00c5}$.",
            "steps": [
                {
                    "stepName": "Step 1: State the Thomas-Fermi Screening Formula",
                    "math": r"k_{\text{TF}} = \sqrt{\frac{3 n e^2}{2 \varepsilon_0 E_F}}",
                    "explanation": "Use the degenerate electron gas screening relation."
                },
                {
                    "stepName": "Step 2: Substitute Physical Constants and Material Parameters",
                    "math": r"k_{\text{TF}}^2 = \frac{3 \times (8.49 \times 10^{28}\text{ m}^{-3}) \times (1.6022 \times 10^{-19}\text{ C})^2}{2 \times (8.8542 \times 10^{-12}\text{ F/m}) \times (1.128 \times 10^{-18}\text{ J})} = \frac{6.538 \times 10^{-9}}{1.9975 \times 10^{-29}} \approx 3.273 \times 10^{20}\text{ m}^{-2}",
                    "explanation": "Compute the square of the screening wavevector."
                },
                {
                    "stepName": "Step 3: Calculate the Screening Wavevector k_TF",
                    "math": r"k_{\text{TF}} = \sqrt{3.273 \times 10^{20}\text{ m}^{-2}} \approx 1.809 \times 10^{10}\text{ m}^{-1} = 1.809\text{ \AA}^{-1}",
                    "explanation": "Take the square root."
                },
                {
                    "stepName": "Step 4: Determine the Screening Length lambda_TF",
                    "math": r"\lambda_{\text{TF}} = \frac{1}{k_{\text{TF}}} = \frac{1}{1.809 \times 10^{10}\text{ m}^{-1}} \approx 5.528 \times 10^{-11}\text{ m} = 0.553\text{ \AA}",
                    "explanation": "The screening distance is approximately half an Angstrom, much smaller than the 3.615 Angstrom lattice constant of copper."
                }
            ],
            "answer": "k_{\\text{TF}} = 1.81 \\times 10^{10} \\text{ m}^{-1}, \\quad \\lambda_{\\text{TF}} = 0.553 \\text{ \u00c5} \\quad (\\text{Screening occurs within } 15\\% \\text{ of the unit cell size})"
        }
    ]
}

# ==========================================
# UNIT 8: Semiconductors, Junction Devices & Quantum Dots
# ==========================================
u8 = {
    "unitNumber": 8,
    "unitId": "unit8-semiconductors",
    "title": "Semiconductors, Junction Devices & Quantum Dots",
    "description": "Comprehensive semiconductor physics and low-dimensional quantum transport: direct vs indirect bandgaps, intrinsic carrier statistics, shallow donor and acceptor doping, drift and diffusion transport, Einstein relation, p-n junction electrostatics, Shockley diode equation, LEDs, photovoltaics, and quantum confinement in 2D quantum wells, 1D wires, and 0D quantum dots.",
    "sections": [
        {
            "id": "ssp-8-1",
            "title": "Band Structures: Direct vs Indirect Semiconductors & Effective Masses",
            "content": r"""<h4>1. Direct vs. Indirect Band Gap Semiconductors</h4>
<p>In crystalline semiconductors, the electrical and optical properties are governed by the band gap $E_g$ separating the highest occupied <strong>Valence Band Maximum (VBM)</strong> from the lowest unoccupied <strong>Conduction Band Minimum (CBM)</strong>:</p>
<ul>
<li><strong>Direct Band Gap Semiconductors (e.g., $\text{GaAs}, \text{InP}, \text{GaN}$):</strong> Both the conduction band minimum and valence band maximum occur at the <em>same crystal wavevector</em> (typically the zone center $\Gamma$-point, $\vec{k} = 0$). Optical photon transitions ($\Delta \vec{k} \approx 0$) occur directly via vertical electric dipole absorption and rapid radiative electron-hole recombination ($h\nu = E_g$). Essential for efficient optoelectronics: LEDs, laser diodes.</li>
<li><strong>Indirect Band Gap Semiconductors (e.g., $\text{Si}, \text{Ge}, \text{GaP}$):</strong> The conduction band minimum and valence band maximum occur at <em>different wavevectors</em> (e.g., in Silicon, the VBM is at $\Gamma$ while the CBM is near $0.85$ of the zone edge along $[100]$). Conservation of crystal momentum forbids first-order radiative transitions: photon absorption or emission requires simultaneous absorption or emission of a lattice <strong>phonon</strong> ($\hbar\vec{q}$):
<div class="math-display">
$$h\nu = E_g \pm \hbar\omega_{\text{phonon}}, \quad \vec{k}_{\text{initial}} + \vec{k}_{\text{photon}} \approx \vec{k}_{\text{final}} \pm \vec{q}$$
</div>
<p>Because second-order phonon-assisted transitions are far less probable, indirect semiconductors exhibit long carrier radiative lifetimes, making them ideal for photovoltaic solar cells and CMOS microelectronics, but inefficient as light emitters.</p></li>
</ul>

<h4>2. Kane Non-Parabolicity & Anisotropic Effective Masses</h4>
<p>Near band extrema, expanding $E(\vec{k})$ to quadratic order yields anisotropic effective mass tensors:</p>
<div class="math-display">
$$E_c(\vec{k}) = E_c + \frac{\hbar^2}{2} \left( \frac{k_l^2}{m_l^*} + \frac{k_t^2 + k_t'^2}{m_t^*} \right)$$
</div>
<p>where $m_l^*$ is the longitudinal mass and $m_t^*$ is the transverse mass (e.g., in Silicon, $m_l^* = 0.98 m_0$, $m_t^* = 0.19 m_0$). The density-of-states effective mass is $m_d^* = (m_l^* m_t^{*2})^{1/3}$, while the conductivity effective mass is $m_c^* = 3\left(\frac{1}{m_l^*} + \frac{2}{m_t^*}\right)^{-1}$.</p>"""
        },
        {
            "id": "ssp-8-2",
            "title": "Intrinsic Carrier Statistics & The Law of Mass Action",
            "content": r"""<h4>1. Intrinsic Conduction Electron Density $n$ and Hole Density $p$</h4>
<p>In a non-degenerate semiconductor ($E_c - E_F \gg k_BT$ and $E_F - E_v \gg k_BT$), the Fermi-Dirac distribution is accurately approximated by the classical Maxwell-Boltzmann tail:</p>
<div class="math-display">
$$f(E) \approx e^{-(E - E_F)/k_B T}$$
</div>
<p>Integrating over the parabolic conduction band density of states yields the thermal equilibrium electron concentration:</p>
<div class="math-display">
$$n = \int_{E_c}^\infty g_c(E) f(E) dE = N_c e^{-(E_c - E_F)/k_B T}$$
</div>
<p>where $N_c$ is the <strong>effective density of states in the conduction band</strong>:</p>
<div class="math-display">
$$N_c = 2 \left( \frac{2\pi m_e^* k_B T}{h^2} \right)^{3/2}$$
</div>
<p>Similarly, the hole concentration in the valence band is:</p>
<div class="math-display">
$$p = \int_{-\infty}^{E_v} g_v(E) [1 - f(E)] dE = N_v e^{-(E_F - E_v)/k_B T}$$
</div>
<p>where $N_v = 2 \left( \frac{2\pi m_h^* k_B T}{h^2} \right)^{3/2}$ is the effective density of states in the valence band.</p>

<h4>2. The Law of Mass Action & Intrinsic Carrier Concentration $n_i$</h4>
<p>Multiplying $n$ and $p$ eliminates the Fermi energy $E_F$ entirely, establishing the fundamental <strong>Law of Mass Action</strong>:</p>
<div class="math-display">
$$n \cdot p = N_c N_v e^{-(E_c - E_v)/k_B T} = N_c N_v e^{-E_g / k_B T} = n_i^2$$
</div>
<p>where $n_i$ is the <strong>intrinsic carrier concentration</strong>:</p>
<div class="math-display">
$$n_i(T) = \sqrt{N_c N_v} e^{- E_g / 2 k_B T} \propto T^{3/2} e^{- E_g / 2 k_B T}$$
</div>
<p>This product $n \cdot p = n_i^2$ holds strictly for any semiconductor in thermal equilibrium, regardless of whether it is intrinsic or heavily doped.</p>

<h4>3. The Intrinsic Fermi Level $E_i$</h4>
<p>In an undoped intrinsic semiconductor, charge neutrality requires $n = p = n_i$. Equating $n$ and $p$ reveals the position of the intrinsic Fermi level:</p>
<div class="math-display">
$$E_i = \frac{E_c + E_v}{2} + \frac{3}{4} k_B T \ln\left( \frac{m_h^*}{m_e^*} \right)$$
</div>
<p>Because $\ln(m_h^*/m_e^*) \sim 0$, the intrinsic Fermi level lies virtually at the exact mid-gap ($E_g/2$).</p>"""
        },
        {
            "id": "ssp-8-3",
            "title": "Extrinsic Doping: Donors, Acceptors & Carrier Transport",
            "content": r"""<h4>1. Shallow Hydrogenic Donor and Acceptor Impurities</h4>
<p>Extrinsic semiconductors are created by intentionally introducing trace dopant atoms into the host lattice:</p>
<ul>
<li><strong>$n$-Type Doping (Group V in Group IV, e.g., P, As in Si):</strong> Donates an extra valence electron. The extra electron orbits the positively charged donor ion core ($+e$) in a hydrogen-like orbit screened by the large dielectric permittivity of the crystal ($\varepsilon_r \sim 12$):
<div class="math-display">
$$E_d = \frac{m_e^*}{m_0} \frac{1}{\varepsilon_r^2} E_H = \frac{m_e^*}{m_0} \frac{13.6\text{ eV}}{\varepsilon_r^2} \sim 10 - 50\text{ meV}$$
</div>
<p>The donor Bohr radius is expanded to $r_d = \varepsilon_r \frac{m_0}{m_e^*} a_0 \sim 30 - 80\text{ \AA}$. At room temperature ($k_BT \approx 26\text{ meV}$), virtually all donors are thermally ionized, so $n \approx N_D$.</p></li>
<li><strong>$p$-Type Doping (Group III in Group IV, e.g., B, Ga in Si):</strong> Lacks one valence electron, creating a bound acceptor state near the valence band edge that accepts an electron, generating mobile positive holes ($p \approx N_A$).</li>
</ul>

<h4>2. Drift and Diffusion Transport</h4>
<p>In the presence of an electric field $\vec{E}$ and carrier concentration gradients $\nabla n$ and $\nabla p$, total electron and hole current densities comprise both <strong>drift</strong> and <strong>diffusion</strong> components:</p>
<div class="math-display">
$$\vec{J}_n = n e \mu_n \vec{E} + e D_n \nabla n$$
</div>
<div class="math-display">
$$\vec{J}_p = p e \mu_p \vec{E} - e D_p \nabla p$$
</div>
<p>where $\mu_n, \mu_p$ are carrier mobilities and $D_n, D_p$ are diffusion coefficients. In thermal equilibrium ($\vec{J} = 0$), the drift and diffusion currents balance identically, deriving the universal <strong>Einstein Relation</strong>:</p>
<div class="math-display">
$$\frac{D_n}{\mu_n} = \frac{D_p}{\mu_p} = \frac{k_B T}{e}$$
</div>
<p>The total electrical conductivity is given by $\sigma = e (n \mu_n + p \mu_p)$.</p>"""
        },
        {
            "id": "ssp-8-4",
            "title": "The p-n Junction: Built-in Potential & Shockley Diode Equation",
            "simulation": "ssp-pn-junction-band-sim",
            "content": r"""<h4>1. Electrostatics of the Equilibrium p-n Junction</h4>
<p>When $p$-type and $n$-type semiconductor regions are brought into intimate metallurgical contact, the steep concentration gradient drives diffusion of majority electrons from $n$ to $p$ and holes from $p$ to $n$. This recombination uncovers fixed, ionized donor cores ($N_D^+$) on the $n$-side and ionized acceptor cores ($N_A^-$) on the $p$-side, creating a space-charge <strong>depletion region</strong> of width $W = x_p + x_n$.</p>
<p>The resulting internal electric field opposes further diffusion until equilibrium is established with a flat Fermi level ($dE_F/dx = 0$). The total electrostatic potential barrier across the junction is the <strong>built-in potential</strong> $V_{bi}$:</p>
<div class="math-display">
$$V_{bi} = \frac{k_B T}{e} \ln\left( \frac{N_A N_D}{n_i^2} \right)$$
</div>
<p>Solving Poisson's equation $\frac{d^2 V}{dx^2} = - \frac{\rho(x)}{\varepsilon_s}$ under the depletion approximation yields the total depletion layer width under applied voltage $V_a$:</p>
<div class="math-display">
$$W = \sqrt{\frac{2 \varepsilon_s (V_{bi} - V_a)}{e} \left( \frac{1}{N_A} + \frac{1}{N_D} \right)}$$
</div>

<h4>2. The Shockley Ideal Diode Equation</h4>
<p>Applying a forward bias voltage ($V_a > 0$) lowers the potential barrier to $V_{bi} - V_a$, exponentially increasing minority carrier injection across the depletion region edges. Integrating minority carrier diffusion currents yields the celebrated <strong>Shockley Diode Equation</strong>:</p>
<div class="math-display">
$$I(V_a) = I_0 \left( e^{e V_a / k_B T} - 1 \right)$$
</div>
<p>where $I_0 = e A \left( \frac{D_n n_{p0}}{L_n} + \frac{D_p p_{n0}}{L_p} \right)$ is the reverse saturation current.</p>

<h4>3. Optoelectronic Devices</h4>
<ul>
<li><strong>Light-Emitting Diodes (LEDs):</strong> Under forward bias, electrons and holes are injected across the junction and recombine radiatively, emitting photons with peak energy $h\nu \approx E_g$ ($\lambda \approx hc/E_g$).</li>
<li><strong>Photovoltaic Solar Cells:</strong> Photons with $h\nu > E_g$ generate electron-hole pairs within and near the depletion region. The built-in electric field sweeps electrons to the $n$-side and holes to the $p$-side, producing a photocurrent $I_{sc}$ and open-circuit photovoltage $V_{oc}$.</li>
</ul>"""
        },
        {
            "id": "ssp-8-5",
            "title": "Low-Dimensional Nanostructures: Quantum Wells, Wires & Quantum Dots",
            "simulation": "ssp-quantum-dot-confinement-sim",
            "content": r"""<h4>1. Quantum Confinement & Dimensionality Hierarchy</h4>
<p>When the spatial dimensions of a semiconductor crystal are reduced below the exciton Bohr radius $a_B = \varepsilon_r \frac{m_0}{\mu} a_0 \sim 2 - 10\text{ nm}$, continuous electronic energy bands quantize into discrete sub-bands due to <strong>quantum confinement</strong>:</p>
<ol>
<li><strong>3D (Bulk):</strong> Confinement in $0$ dimensions; $g(E) \propto \sqrt{E}$.</li>
<li><strong>2D (Quantum Well):</strong> Confinement along $1$ dimension ($L_z \sim \text{nm}$), free in $x, y$. Energy spectrum: $E(k_x, k_y, n_z) = E_{n_z} + \frac{\hbar^2(k_x^2 + k_y^2)}{2m^*}$. Density of states consists of discrete <strong>staircase steps</strong>: $g_{\text{2D}}(E) = \frac{m^*}{\pi\hbar^2} \sum_{n} \Theta(E - E_n)$.</li>
<li><strong>1D (Quantum Wire):</strong> Confinement along $2$ dimensions ($L_x, L_y \sim \text{nm}$), free along $z$. Energy spectrum: $E(k_z, n_x, n_y) = E_{n_x, n_y} + \frac{\hbar^2 k_z^2}{2m^*}$. Density of states exhibits sharp <strong>$E^{-1/2}$ Van Hove singularities</strong>: $g_{\text{1D}}(E) \propto \sum_n (E - E_n)^{-1/2}$.</li>
<li><strong>0D (Quantum Dot):</strong> Confinement along all $3$ spatial dimensions ($L_x, L_y, L_z \sim \text{nm}$). Completely discrete "artificial atom" spectrum: $E_{n_x, n_y, n_z} = \frac{\pi^2\hbar^2}{2m^*} \left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2}\right)$. Density of states is a collection of <strong>Dirac delta-functions</strong>: $g_{\text{0D}}(E) = 2 \sum_i \delta(E - E_i)$.</li>
</ol>

<h4>2. Size-Dependent Bandgap Tuning in Quantum Dots (Brus Formula)</h4>
<p>For a spherical semiconductor nanocrystal (quantum dot) of radius $R$, Louis Brus (1984) derived the quantum confinement energy shift using the effective mass approximation:</p>
<div class="math-display">
$$E_g(R) = E_{g,\text{bulk}} + \frac{\hbar^2 \pi^2}{2 \mu R^2} - \frac{1.786 e^2}{4\pi\varepsilon_0 \varepsilon_r R}$$
</div>
<p>where $\frac{1}{\mu} = \frac{1}{m_e^*} + \frac{1}{m_h^*}$ is the exciton reduced mass.</p>
<ul>
<li>The first correction term ($+ \hbar^2\pi^2 / 2\mu R^2 \propto 1/R^2$) represents kinetic quantum confinement energy, pushing the effective band gap upward.</li>
<li>The second correction term ($- 1.786 e^2 / 4\pi\varepsilon_0 \varepsilon_r R \propto -1/R$) represents screened Coulomb attraction between electron and hole.</li>
</ul>
<p>By simply tuning the nanocrystal radius $R$ from $1.5\text{ nm}$ to $6.0\text{ nm}$, the emission color of cadmium selenide ($\text{CdSe}$) quantum dots can be tuned continuously across the entire visible spectrum from vibrant blue to deep red.</p>"""
        }
    ],
    "problems": [
        {
            "id": "ssp-p-8-1",
            "title": "Intrinsic Carrier Concentration and Resistivity of Silicon at 300 K",
            "statement": "At $T = 300 \\text{ K}$, Silicon has a band gap $E_g = 1.12 \\text{ eV}$, effective conduction band density of states $N_c = 2.80 \\times 10^{19} \\text{ cm}^{-3}$, effective valence band density of states $N_v = 1.04 \\times 10^{19} \\text{ cm}^{-3}$, electron mobility $\\mu_n = 1450 \\text{ cm}^2/\\text{V}\\cdot\\text{s}$, and hole mobility $\\mu_p = 450 \\text{ cm}^2/\\text{V}\\cdot\\text{s}$. (a) Calculate the intrinsic carrier concentration $n_i$. (b) Determine the electrical conductivity $\\sigma$ and electrical resistivity $\\rho$ of pure intrinsic Silicon.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Product N_c N_v in SI Units",
                    "math": r"N_c N_v = (2.80 \times 10^{25}\text{ m}^{-3})(1.04 \times 10^{25}\text{ m}^{-3}) \approx 2.912 \times 10^{50}\text{ m}^{-6} \implies \sqrt{N_c N_v} \approx 1.7065 \times 10^{25}\text{ m}^{-3}",
                    "explanation": "Convert densities from cm^-3 to m^-3 and compute their geometric mean."
                },
                {
                    "stepName": "Step 2: Evaluate the Boltzmann Exponential Factor",
                    "math": r"\frac{E_g}{2 k_B T} = \frac{1.12\text{ eV}}{2 \times (0.02585\text{ eV})} \approx \frac{1.12}{0.0517} \approx 21.663 \implies e^{-E_g / 2k_BT} = e^{-21.663} \approx 3.907 \times 10^{-10}",
                    "explanation": "Evaluate the thermal excitation factor at 300 K."
                },
                {
                    "stepName": "Step 3: Calculate the Intrinsic Carrier Concentration n_i",
                    "math": r"n_i = \sqrt{N_c N_v} e^{-E_g/2k_BT} = (1.7065 \times 10^{25}\text{ m}^{-3}) \times (3.907 \times 10^{-10}) \approx 6.67 \times 10^{15}\text{ m}^{-3} = 6.67 \times 10^9\text{ cm}^{-3}",
                    "explanation": "Compute n_i at 300 K."
                },
                {
                    "stepName": "Step 4: Compute Intrinsic Electrical Conductivity and Resistivity",
                    "math": r"\sigma_i = e n_i (\mu_n + \mu_p) = (1.6022 \times 10^{-19}\text{ C}) \times (6.67 \times 10^{15}\text{ m}^{-3}) \times (0.1450 + 0.0450\text{ m}^2/\text{V}\cdot\text{s}) = (1.069 \times 10^{-3}) \times (0.190) \approx 2.03 \times 10^{-4}\text{ }\Omega^{-1}\cdot\text{m}^{-1}",
                    "explanation": "Convert mobilities to m^2/V*s and compute sigma_i."
                },
                {
                    "stepName": "Step 5: Determine Intrinsic Resistivity rho_i",
                    "math": r"\rho_i = \frac{1}{\sigma_i} = \frac{1}{2.03 \times 10^{-4}\text{ }\Omega^{-1}\cdot\text{m}^{-1}} \approx 4926\text{ }\Omega\cdot\text{m} \approx 4.93 \times 10^5\text{ }\Omega\cdot\text{cm}",
                    "explanation": "Take the reciprocal of conductivity."
                }
            ],
            "answer": "n_i = 6.67 \\times 10^9 \\text{ cm}^{-3} \\quad (6.67 \\times 10^{15} \\text{ m}^{-3}), \\quad \\sigma_i = 2.03 \\times 10^{-4} \\text{ }\u03a9^{-1}\\cdot\\text{m}^{-1}, \\quad \\rho_i = 4926 \\text{ }\u03a9\\cdot\\text{m}"
        },
        {
            "id": "ssp-p-8-2",
            "title": "Hydrogenic Donor Binding Energy and Bohr Radius in Silicon",
            "statement": "Phosphorus ($Z = 15$) is added as a donor impurity to Silicon, which has a relative dielectric permittivity $\\varepsilon_r = 11.7$ and an effective electron mass $m_e^* = 0.26 m_0$. Using the hydrogenic donor model: (a) Calculate the donor ionization energy $E_d$ in $\\text{meV}$. (b) Calculate the effective donor Bohr radius $r_d$ in Angstroms, and determine how many Silicon unit cells ($a = 5.43 \\text{ \u00c5}$) are enclosed within the donor electron orbit.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Donor Ionization Energy E_d",
                    "math": r"E_d = \left(\frac{m_e^*}{m_0}\right) \frac{1}{\varepsilon_r^2} E_H = 0.26 \times \frac{13.606\text{ eV}}{(11.7)^2} = \frac{3.5376\text{ eV}}{136.89} \approx 0.02584\text{ eV} = 25.84\text{ meV}",
                    "explanation": "Scale the hydrogen Rydberg energy (13.6 eV) by the effective mass and dielectric screening factor epsilon_r^2."
                },
                {
                    "stepName": "Step 2: Calculate the Effective Donor Bohr Radius r_d",
                    "math": r"r_d = \varepsilon_r \left(\frac{m_0}{m_e^*}\right) a_0 = 11.7 \times \left(\frac{1}{0.26}\right) \times (0.5292\text{ \AA}) \approx 11.7 \times 3.846 \times 0.5292\text{ \AA} \approx 23.81\text{ \AA}",
                    "explanation": "Scale the atomic Bohr radius a_0 by epsilon_r and m_0 / m_e*."
                },
                {
                    "stepName": "Step 3: Calculate the Number of Enclosed Unit Cells",
                    "math": r"V_{\text{orbit}} = \frac{4}{3}\pi r_d^3 = \frac{4}{3}\pi (23.81\text{ \AA})^3 \approx 5.653 \times 10^4\text{ \AA}^3, \quad V_{\text{cell}} = a^3 = (5.431\text{ \AA})^3 \approx 160.2\text{ \AA}^3 \implies N_{\text{cells}} = \frac{5.653 \times 10^4}{160.2} \approx 353\text{ unit cells}",
                    "explanation": "Divide the volume of the donor electron cloud by the unit cell volume of silicon."
                }
            ],
            "answer": "E_d = 25.8 \\text{ meV}, \\quad r_d = 23.8 \\text{ \u00c5}, \\quad N_{\\text{cells}} \\approx 353 \\text{ unit cells}"
        },
        {
            "id": "ssp-p-8-3",
            "title": "Quantum Dot Size-Dependent Emission Tuning for Cadmium Selenide",
            "statement": "Cadmium Selenide ($\\text{CdSe}$) has a bulk band gap $E_{g,\\text{bulk}} = 1.74 \\text{ eV}$, dielectric constant $\\varepsilon_r = 10.6$, electron effective mass $m_e^* = 0.13 m_0$, and hole effective mass $m_h^* = 0.45 m_0$. Using the Brus quantum confinement formula: (a) Calculate the reduced exciton mass $\\mu$. (b) Determine the effective emission bandgap $E_g(R)$ and emission wavelength $\\lambda$ for a spherical $\\text{CdSe}$ quantum dot of radius $R = 2.0 \\text{ nm}$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Reduced Exciton Mass mu",
                    "math": r"\frac{1}{\mu} = \frac{1}{m_e^*} + \frac{1}{m_h^*} = \frac{1}{0.13 m_0} + \frac{1}{0.45 m_0} = \frac{7.692 + 2.222}{m_0} = \frac{9.914}{m_0} \implies \mu \approx 0.1009 m_0 \approx 9.19 \times 10^{-32}\text{ kg}",
                    "explanation": "Compute the reduced mass of the electron-hole pair."
                },
                {
                    "stepName": "Step 2: Calculate the Kinetic Confinement Energy Shift Delta E_kin",
                    "math": r"\Delta E_{\text{kin}} = \frac{\hbar^2 \pi^2}{2 \mu R^2} = \frac{(1.0546 \times 10^{-34}\text{ J}\cdot\text{s})^2 \pi^2}{2 \times (9.19 \times 10^{-32}\text{ kg}) \times (2.0 \times 10^{-9}\text{ m})^2} = \frac{1.0978 \times 10^{-67}}{7.352 \times 10^{-49}}\text{ J} \approx 1.493 \times 10^{-19}\text{ J} \approx 0.932\text{ eV}",
                    "explanation": "Evaluate the particle-in-a-sphere kinetic confinement energy in electron-volts."
                },
                {
                    "stepName": "Step 3: Calculate the Screened Coulomb Attraction Energy Shift Delta E_Coul",
                    "math": r"\Delta E_{\text{Coul}} = \frac{1.786 e^2}{4\pi\varepsilon_0 \varepsilon_r R} = \frac{1.786 \times (1.440\text{ eV}\cdot\text{\AA})}{10.6 \times (20.0\text{ \AA})} = \frac{2.5718}{212.0}\text{ eV} \approx 0.012\text{ eV}",
                    "explanation": "Compute the electrostatic Coulomb correction term."
                },
                {
                    "stepName": "Step 4: Compute the Effective Quantum Dot Bandgap E_g(R)",
                    "math": r"E_g(R) = E_{g,\text{bulk}} + \Delta E_{\text{kin}} - \Delta E_{\text{Coul}} = 1.74\text{ eV} + 0.932\text{ eV} - 0.012\text{ eV} \approx 2.66\text{ eV}",
                    "explanation": "Sum the bulk gap and quantum corrections."
                },
                {
                    "stepName": "Step 5: Determine the Emission Wavelength lambda",
                    "math": r"\lambda = \frac{h c}{E_g(R)} = \frac{1239.84\text{ eV}\cdot\text{nm}}{2.66\text{ eV}} \approx 466\text{ nm} \quad (\text{Vibrant Blue Emission})",
                    "explanation": "Convert the band gap energy to emission wavelength. Note that while bulk CdSe emits in the deep red (713 nm), 2.0 nm quantum dots emit blue light at 466 nm."
                }
            ],
            "answer": "\\mu = 0.101 m_0, \\quad E_g(R=2\\text{ nm}) = 2.66 \\text{ eV}, \\quad \\lambda = 466 \\text{ nm} \\quad (\\text{Blue Light})"
        }
    ]
}

with open("ssp_u7.json", "w") as f:
    json.dump(u7, f, indent=2)
print("ssp_u7.json created successfully!")

with open("ssp_u8.json", "w") as f:
    json.dump(u8, f, indent=2)
print("ssp_u8.json created successfully!")
