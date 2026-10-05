import json

# ==========================================
# UNIT 5: Radiation Interaction with Matter & Detection Systems
# ==========================================
u5 = {
    "unitNumber": 5,
    "unitId": "unit5-radiation-interactions-detectors",
    "title": "Radiation Interaction with Matter & Detection Systems",
    "description": "Comprehensive physical principles of radiation interactions and nuclear detection instrumentation: Bethe-Bloch relativistic stopping power formula for heavy charged particles, Bragg peak, range straggling; electron radiative and collisional losses, Bremsstrahlung, critical energy; neutron elastic scattering, logarithmic energy decrement, slowing-down length, and diffusion; gas ionization chambers, proportional counters, Townsend avalanche, and Geiger-Muller regimes; scintillation mechanisms (NaI:Tl, plastics) and photomultiplier tube gain; semiconductor detectors (HPGe, Si surface barrier), Fano factor, energy resolution, and pulse processing electronics.",
    "sections": [
        {
            "id": "nuc-5-1",
            "title": "Charged Particle Stopping Power: Bethe-Bloch & Bragg Peak",
            "simulation": "nuc-bragg-peak-sim",
            "content": r"""<h4>1. Linear Stopping Power & The Relativistic Bethe-Bloch Formula</h4>
<p>As a fast heavy charged particle (proton, alpha, fission fragment) traverses matter, it interacts primarily via the long-range Coulomb force with atomic electrons, transferring energy through excitation and ionization. The average linear rate of energy loss per unit path length, $-dE/dx$, is governed by the quantum mechanical <strong>Bethe-Bloch formula</strong>:</p>
<div class="math-display">
$$-\frac{dE}{dx} = 2\pi N_A r_e^2 m_e c^2 \rho \frac{Z}{A} \frac{z^2}{\beta^2} \left[ \ln\left( \frac{2 m_e c^2 \beta^2 \gamma^2 T_{\text{max}}}{I^2} \right) - 2\beta^2 - \delta(\beta) - \frac{2C}{Z} \right]$$
</div>
<p>where:</p>
<ul>
<li>$z e$ and $v = \beta c$ are the charge and velocity of the incident projectile ($\gamma = 1 / \sqrt{1 - \beta^2}$).</li>
<li>$Z, A, \rho$ are the atomic number, mass number, and mass density of the absorbing medium.</li>
<li>$r_e = \frac{e^2}{4\pi\varepsilon_0 m_e c^2} \approx 2.818\text{ fm}$ is the classical electron radius.</li>
<li>$I \approx 10 Z\text{ eV}$ is the mean excitation energy of the absorber atoms.</li>
<li>$T_{\text{max}} = \frac{2 m_e c^2 \beta^2 \gamma^2}{1 + 2\gamma (m_e / M) + (m_e / M)^2} \approx 2 m_e c^2 \beta^2 \gamma^2$ is the maximum kinetic energy transferable to an atomic electron in a single head-on collision.</li>
<li>$\delta(\beta)$ is the high-velocity density effect correction (dielectric polarization of the medium).</li>
<li>$C/Z$ is the inner-shell correction (for projectile velocities comparable to inner orbital electron speeds).</li>
</ul>

<h4>2. Physical Regimes & The Bragg Peak</h4>
<p>The Bethe-Bloch formula reveals essential physical properties of charged particle stopping:</p>
<ol>
<li><strong>Low Velocity Regime ($v \ll c$):</strong> Stopping power varies inversely with the square of velocity:
<div class="math-display">
$$-\frac{dE}{dx} \propto \frac{z^2}{v^2} \propto \frac{z^2}{E}$$
</div>
As the charged particle penetrates matter and slows down, its rate of energy loss does not decrease—it <strong>increases dramatically</strong>, reaching a sharp maximum immediately prior to coming to rest. This pronounced ionization spike at the end of the particle range is the <strong>Bragg Peak</strong>.</li>
<li><strong>Hadron Cancer Therapy:</strong> Protons ($150 - 250\text{ MeV}$) and Carbon ions ($400\text{ MeV/u}$) deposit minimal radiation dose in healthy surface tissue, concentrating their massive destructive Bragg peak precisely within deep-seated tumors.</li>
<li><strong>Minimum Ionizing Particles (MIP):</strong> At $\beta\gamma \approx 3 - 4$ ($\beta \approx 0.96$), $-dE/dx$ reaches a broad global minimum of approximately $1 - 2\text{ MeV}\cdot\text{cm}^2/\text{g}$ for all singly charged particles ($z=1$).</li>
</ol>

<h4>3. Particle Range & Range Straggling</h4>
<p>The total mean path length or <strong>range</strong> $R$ of a charged particle of initial kinetic energy $E_0$ is evaluated under the Continuous Slowing Down Approximation (CSDA):</p>
<div class="math-display">
$$R(E_0) = \int_0^{E_0} \left( -\frac{dE}{dx} \right)^{-1} dE$$
</div>
<p>Because energy loss arises from a large number of discrete statistical collisions, individual particle ranges fluctuate around the mean $R_0$ with a Gaussian distribution characterized by the <strong>range straggling parameter</strong> $\sigma_R / R_0 \approx 1 - 2\%$.</p>"""
        },
        {
            "id": "nuc-5-2",
            "title": "Fast Electron Energy Loss: Collisional vs Bremsstrahlung",
            "content": r"""<h4>1. Collisional Energy Loss of Fast Electrons</h4>
<p>Electrons ($e^-$) and positrons ($e^+$) differ fundamentally from heavy ions due to their minuscule mass ($m_e$ equals target electron mass) and quantum mechanical indistinguishability. The collisional stopping power is given by the relativistic <strong>Bethe-Møller formula</strong>:</p>
<div class="math-display">
$$\left( -\frac{dE}{dx} \right)_{\text{coll}} = 2\pi N_A r_e^2 m_e c^2 \rho \frac{Z}{A} \frac{1}{\beta^2} \left[ \ln\left(\frac{T^2 (T + 2 m_e c^2)}{2 I^2 m_e c^2}\right) + F^\pm(\beta) - \delta \right]$$
</div>
<p>Because $M_{\text{proj}} = M_{\text{target}}$, electrons undergo catastrophic wide-angle Coulomb scatterings, following tortuous, zigzag trajectories through the absorber. Consequently, the actual penetration depth (projected range) is typically $30 - 50\%$ shorter than the total integrated path length.</p>

<h4>2. Radiative Energy Loss: Bremsstrahlung</h4>
<p>When a fast electron experiences intense transverse acceleration in the strong electric field of an atomic nucleus, classical and quantum electrodynamics dictate that it radiates electromagnetic energy as <strong>Bremsstrahlung</strong> ("braking radiation"):</p>
<div class="math-display">
$$\left( -\frac{dE}{dx} \right)_{\text{rad}} \approx \frac{E}{X_0}$$
</div>
<p>where $X_0$ is the <strong>radiation length</strong> of the absorbing material (in $\text{g/cm}^2$):</p>
<div class="math-display">
$$\frac{1}{X_0} \approx 4 \alpha r_e^2 \frac{N_A}{A} Z(Z + 1) \ln\left( \frac{183}{Z^{1/3}} \right)$$
</div>
<p>Bremsstrahlung losses scale proportional to the square of the target atomic number $Z^2$ and linearly with electron energy $E$.</p>

<h4>3. The Critical Energy ($E_c$)</h4>
<p>The total stopping power of electrons is the sum of collisional and radiative components:</p>
<div class="math-display">
$$\left(-\frac{dE}{dx}\right)_{\text{total}} = \left(-\frac{dE}{dx}\right)_{\text{coll}} + \left(-\frac{dE}{dx}\right)_{\text{rad}}$$
</div>
<p>The ratio of radiative to collisional losses is parameterized empirically as:</p>
<div class="math-display">
$$\frac{(-dE/dx)_{\text{rad}}}{(-dE/dx)_{\text{coll}}} \approx \frac{E \cdot Z}{800\text{ MeV}}$$
</div>
<p>The energy at which radiative and collisional losses are exactly equal is the <strong>Critical Energy</strong> $E_c$:</p>
<div class="math-display">
$$E_c \approx \frac{800\text{ MeV}}{Z + 1.2}$$
</div>
<ul>
<li>In <strong>Lead ($Z = 82$)</strong>: $E_c \approx 9.5\text{ MeV}$. For $E > 10\text{ MeV}$, Bremsstrahlung completely dominates.</li>
<li>In <strong>Air / Water ($Z_{\text{eff}} \approx 7.5$)</strong>: $E_c \approx 85\text{ MeV}$. Collisional ionization dominates up to very high energies.</li>
<li><strong>Shielding Precaution:</strong> Energetic beta sources ($^{90}\text{Sr}$-$^{90}\text{Y}$) must never be shielded directly with Lead, as intense secondary Bremsstrahlung X-rays would be generated. Instead, low-$Z$ materials (Lucite, aluminum) are employed first to slow the electrons with minimal radiation, followed by high-$Z$ lead to attenuate residual gammas.</li>
</ul>"""
        },
        {
            "id": "nuc-5-3",
            "title": "Neutron Moderation, Logarithmic Decrement & Diffusion",
            "content": r"""<h4>1. Neutron Interactions and Kinematics of Elastic Scattering</h4>
<p>Because the neutron carries zero electric charge, it experiences no Coulomb forces and interacts exclusively with atomic nuclei via the strong force (or magnetic dipole interaction). In an elastic collision of a neutron of mass $m \approx 1$ and laboratory kinetic energy $E$ with a target nucleus of mass number $A$ initially at rest, the ratio of scattered neutron energy $E'$ to initial energy $E$ as a function of the center-of-mass scattering angle $\theta_{\text{cm}}$ is:</p>
<div class="math-display">
$$\frac{E'}{E} = \frac{(A - 1)^2 + 2 A (1 + \cos\theta_{\text{cm}})}{(A + 1)^2} = \frac{1 + \alpha}{2} + \frac{1 - \alpha}{2} \cos\theta_{\text{cm}}$$
</div>
<p>where the collision collision parameter $\alpha$ is:</p>
<div class="math-display">
$$\alpha = \left( \frac{A - 1}{A + 1} \right)^2$$
</div>
<p>The minimum energy after a single head-on collision ($\theta_{\text{cm}} = 180^\circ$) is $E'_{\text{min}} = \alpha E$:</p>
<ul>
<li>For <strong>Hydrogen ($A = 1$):</strong> $\alpha = 0$. In a head-on collision with a proton, the neutron can transfer $100\%$ of its kinetic energy in a single collision ($E'_{\text{min}} = 0$). Light water ($H_2O$) is therefore an extraordinarily compact moderator.</li>
<li>For <strong>Carbon ($A = 12$):</strong> $\alpha = (11/13)^2 \approx 0.716$. The maximum energy loss per collision is only $28.4\%$.</li>
<li>For <strong>Uranium ($A = 238$):</strong> $\alpha \approx 0.983$. The neutron loses at most $1.7\%$ of its energy per collision, making heavy nuclei useless as moderators.</li>
</ul>

<h4>2. Average Logarithmic Energy Decrement ($\xi$)</h4>
<p>Assuming isotropic scattering in the center-of-mass frame (valid for s-wave scattering at $E_n < 10\text{ MeV}$), the probability distribution of $E'$ is uniform between $\alpha E$ and $E$. The mean loss of the logarithm of energy per collision, denoted $\xi$, is an invariant constant independent of initial neutron energy:</p>
<div class="math-display">
$$\xi \equiv \left\langle \ln\left( \frac{E}{E'} \right) \right\rangle = 1 + \frac{\alpha}{1 - \alpha} \ln\alpha = 1 - \frac{(A - 1)^2}{2 A} \ln\left( \frac{A + 1}{A - 1} \right)$$
</div>
<p>For $A > 1$, a highly accurate Taylor series approximation is $\xi \approx \frac{2}{A + 2/3}$.</p>
<ul>
<li>For Hydrogen ($A=1$): $\xi = 1.000$.</li>
<li>For Deuterium ($A=2$): $\xi = 0.725$.</li>
<li>For Carbon ($A=12$): $\xi \approx 0.158$.</li>
</ul>
<p>The average number of collisions $N$ required to slow down a fast fission neutron from $E_0 = 2\text{ MeV}$ to thermal energy $E_{\text{th}} = 0.025\text{ eV}$ is:</p>
<div class="math-display">
$$N = \frac{\ln(E_0 / E_{\text{th}})}{\xi} = \frac{\ln(2 \times 10^6 / 0.025)}{\xi} = \frac{\ln(8 \times 10^7)}{\xi} = \frac{18.2}{\xi}$$
</div>
<p>In Hydrogen, $N \approx 18$ collisions; in Deuterium, $N \approx 25$; in Graphite, $N \approx 115$ collisions.</p>

<h4>3. Moderating Ratio</h4>
<p>An ideal moderator must possess not only high slowing-down power $\xi \Sigma_s$, but also an extremely small thermal neutron absorption cross-section $\Sigma_a$. The overall figure of merit is the <strong>Moderating Ratio</strong>:</p>
<div class="math-display">
$$\text{MR} = \frac{\xi \Sigma_s}{\Sigma_a}$$
</div>
<p>Heavy water ($D_2O$) boasts the world's highest moderating ratio ($\text{MR} \approx 5800$) due to the near-zero neutron absorption of deuterium, enabling CANDU reactors to achieve criticality using unenriched natural uranium.</p>"""
        },
        {
            "id": "nuc-5-4",
            "title": "Gas Detectors: Ion Chambers, Proportional & GM Counters",
            "simulation": "nuc-geiger-counter-sim",
            "content": r"""<h4>1. Gas Ionization Regimes vs Applied Voltage</h4>
<p>Gas-filled detectors consist of a cylindrical conductive chamber filled with gas (e.g., Argon + quench gas) with a central thin anode wire maintained at positive potential $V$. Ionizing radiation creates electron-ion pairs along its track (average energy required to produce one ion pair in gas is $W \approx 30 - 35\text{ eV}$). Plotting the collected pulse charge $Q$ against applied cathode-to-anode voltage reveals five characteristic operational regimes:</p>
<ol>
<li><strong>Recombination Region:</strong> Low electric field; positive ions and electrons recombine before reaching the electrodes. No steady signal.</li>
<li><strong>Ionization Chamber Region (Regime II):</strong> Electric field is sufficient to sweep all primary ion pairs to electrodes with zero recombination. Gas multiplication factor $M = 1$. Pulse amplitude is directly proportional to deposited energy, but signals are minuscule ($10^{-15}\text{ C}$), requiring ultra-low-noise electrometers. Used for beam monitoring and gamma dosimeters.</li>
<li><strong>Proportional Counter Region (Regime III):</strong> Near the thin anode wire ($r_a \sim 25\text{ \mu m}$), the radial electric field $E(r) = \frac{V}{r \ln(b/a)}$ exceeds $10^6\text{ V/m}$. Primary electrons gain sufficient kinetic energy between collisions to ionize gas atoms, triggering a localized <strong>Townsend avalanche</strong>. Gas gain is linear: $M \approx 10^3 - 10^5$. Pulse height is strictly proportional to initial particle energy, allowing energy spectroscopy of alpha and beta particles.</li>
<li><strong>Limited Proportionality (Regime IV):</strong> Positive ion space charge shields the anode wire, causing non-linear saturation.</li>
<li><strong>Geiger-Müller (GM) Region (Regime V):</strong> High electric field causes UV photons emitted in the avalanche to induce secondary avalanches throughout the entire length of the anode wire. The discharge terminates only when a sheath of slow positive ions encompasses the wire, collapsing the electric field. Gas gain reaches $M \sim 10^8$. Every ionizing event produces an identical, massive pulse ($\sim 1\text{ V}$), destroying all energy information but enabling sensitive count detection.</li>
</ol>

<h4>2. Geiger Tube Quenching & Dead Time</h4>
<p>As the positive ion sheath drifts to the cathode wall, neutralizing ions could extract secondary electrons and trigger spurious repeat discharges. To prevent this, a <strong>quench gas</strong> is added:</p>
<ul>
<li><strong>Organic Quenching:</strong> Ethanol or ethyl formate ($10\%$). Quench molecules have lower ionization potential than Argon, absorbing positive charges and dissipating energy via harmless molecular dissociation (tubes have a finite lifespan of $\sim 10^9$ counts).</li>
<li><strong>Halogen Quenching:</strong> Bromine ($Br_2$) or Chlorine ($Cl_2$). Dissociated halogen atoms spontaneously recombine, providing infinite tube operational lifetime.</li>
</ul>
<p>The <strong>dead time $\tau$</strong> of a GM tube is the time window ($\sim 50 - 200\text{ \mu s}$) during which a subsequent incoming particle cannot produce a pulse. For a measured count rate $R_m$, the true count rate $R_{\text{true}}$ in the non-paralyzable model is:</p>
<div class="math-display">
$$R_{\text{true}} = \frac{R_m}{1 - R_m \tau}$$
</div>"""
        },
        {
            "id": "nuc-5-5",
            "title": "Scintillation Detectors & Photomultiplier Tubes (PMTs)",
            "content": r"""<h4>1. Mechanism of Inorganic and Organic Scintillators</h4>
<p>Scintillation detectors convert the energy deposited by ionizing radiation into a burst of visible or ultraviolet fluorescence photons:</p>
<ul>
<li><strong>Inorganic Scintillators (e.g., $\text{NaI(Tl)}$, $\text{CsI(Tl)}$, $\text{BGO}$, $\text{LaBr}_3\text{:Ce}$):</strong> Crystalline insulators doped with activator impurities (Thallium). Ionizing radiation excites electrons into the conduction band, creating electron-hole pairs that migrate to activator luminescence centers $\text{Tl}^+$. Transition to the ground state emits optical photons ($\lambda \approx 415\text{ nm}$ for NaI:Tl) with high light yield ($\sim 38,000\text{ photons/MeV}$) and high density ($\rho = 3.67\text{ g/cm}^3$) / high atomic number ($Z=53$), making NaI(Tl) the premier standard for gamma-ray detection.</li>
<li><strong>Organic Scintillators (Anthracene, Stilbene, Plastic Scintillators):</strong> Fluorescence arises from transitions between $\pi$-electron molecular energy levels. Possess sub-nanosecond decay times ($\tau \sim 1 - 3\text{ ns}$), making them ideal for high-speed coincidence timing and neutron detection.</li>
</ul>

<h4>2. The Photomultiplier Tube (PMT) Operation</h4>
<p>The scintillation crystal is optically coupled to a Photomultiplier Tube (PMT) that converts the weak optical burst into a measurable electrical charge pulse:</p>
<ol>
<li><strong>Photocathode:</strong> Optical photons strike a thin photosensitive layer (e.g., bialkali Sb-K-Cs), releasing photoelectrons via the external photoelectric effect with quantum efficiency $\eta \approx 20 - 30\%$.</li>
<li><strong>Electron Focusing:</strong> Electrostatic focusing electrodes direct photoelectrons toward the first dynode.</li>
<li><strong>Dynode Multiplication Chain:</strong> A sequence of $N \approx 10 - 14$ dynodes at escalating positive potentials ($\Delta V \approx 100\text{ V}$ per stage). Each incoming electron releases $\delta \approx 3 - 5$ secondary electrons upon striking a dynode surface. Total electron multiplication gain is:
<div class="math-display">
$$G = \delta^N \approx (4)^{10} \approx 10^6 - 10^7$$
</div></li>
<li><strong>Anode Collection:</strong> The resulting packet of $\sim 10^7$ electrons is collected at the anode, producing a voltage pulse across load resistor $R_L$:
<div class="math-display">
$$V(t) = \frac{Q}{C} e^{-t / RC} = \frac{N_{pe} e G}{C} e^{-t / RC}$$
</div>
The peak voltage amplitude is strictly proportional to the energy deposited by the incident gamma ray in the crystal.</li>
</ol>"""
        },
        {
            "id": "nuc-5-6",
            "title": "Semiconductor Detectors (HPGe, Si) & Counting Statistics",
            "simulation": "nuc-gamma-spectroscopy-hpge-sim",
            "content": r"""<h4>1. Semiconductor Diode Principles (HPGe & Si Surface Barrier)</h4>
<p>Semiconductor radiation detectors function as solid-state ionization chambers. An incoming charged particle or photon creates electron-hole pairs across the semiconductor band gap $E_g$ ($E_g = 1.12\text{ eV}$ for Silicon, $E_g = 0.67\text{ eV}$ for Germanium). The average ionization energy required to create one electron-hole pair is:</p>
<div class="math-display">
$$w_{\text{Si}} \approx 3.62\text{ eV}, \quad w_{\text{Ge}} \approx 2.96\text{ eV}$$
</div>
<p>Because $w$ in semiconductors is an order of magnitude smaller than in gas ($W \approx 30\text{ eV}$) and two orders smaller than in scintillators ($W_{\text{scint}} \approx 100 - 300\text{ eV}$ per photoelectron), a given energy deposition $E$ creates a vastly larger number of charge carriers $N = E / w$, yielding unparalleled <strong>energy resolution</strong>.</p>
<ul>
<li><strong>High-Purity Germanium (HPGe):</strong> Germanium crystals purified to residual impurity densities $< 10^{10}\text{ atoms/cm}^3$ enable planar and coaxial depletion depths of several centimeters. Due to small band gap ($0.67\text{ eV}$), HPGe must be operated at liquid nitrogen temperatures ($77\text{ K}$) to suppress thermal leakage currents. HPGe is the absolute gold standard for high-resolution gamma spectroscopy (FWHM $< 0.15\%$ at $1.33\text{ MeV}$).</li>
<li><strong>Silicon Detectors (Passivated Implanted Planar Silicon - PIPS):</strong> Silicon has a larger band gap, allowing room temperature operation. Used for charged particle spectroscopy (alpha, proton) and X-ray fluorescence (SDD).</li>
</ul>

<h4>2. Energy Resolution & The Fano Factor</h4>
<p>The theoretical statistical variance in the number of created charge carriers $N$ is reduced below Poisson statistics because carrier generation events are not mutually independent (constrained by total energy conservation). This reduction is quantified by the <strong>Fano Factor ($F \approx 0.10 - 0.12$ for HPGe/Si)</strong>:</p>
<div class="math-display">
$$\sigma_N^2 = F \cdot N = F \left( \frac{E}{w} \right)$$
</div>
<p>The statistical Full Width at Half Maximum (FWHM) of an energy peak is:</p>
<div class="math-display">
$$\Delta E_{\text{FWHM}} = 2.355 \sigma_E = 2.355 \sqrt{F \cdot w \cdot E}$$
</div>
<p>For a $1.332\text{ MeV}$ gamma ray in HPGe ($F = 0.11, w = 2.96\text{ eV}$):</p>
<div class="math-display">
$$\Delta E_{\text{FWHM}} = 2.355 \sqrt{0.11 \times (2.96\text{ eV}) \times (1.332 \times 10^6\text{ eV})} \approx 2.355 \times 658\text{ eV} \approx 1.55\text{ keV} \quad (0.12\%)$$
</div>
<p>In contrast, an $\text{NaI(Tl)}$ scintillator achieves an FWHM of $\approx 80\text{ keV}$ ($6\%$) at the same energy—making HPGe over 50 times sharper.</p>

<h4>3. Counting Statistics and Error Propagation</h4>
<p>Radioactive disintegrations obey the <strong>Poisson distribution</strong>. For a total observed count $N$ recorded over duration $t$, the standard deviation is $\sigma_N = \sqrt{N}$, and the relative fractional uncertainty is:</p>
<div class="math-display">
$$\frac{\sigma_N}{N} = \frac{1}{\sqrt{N}}$$
</div>
<p>When subtracting a background count $N_b$ (measured over $t_b$) from a gross sample count $N_g$ (measured over $t_g$), the net count rate $R_{\text{net}} = \frac{N_g}{t_g} - \frac{N_b}{t_b}$ has an uncertainty:</p>
<div class="math-display">
$$\sigma_{R_{\text{net}}} = \sqrt{\frac{R_g}{t_g} + \frac{R_b}{t_b}}$$
</div>"""
        }
    ],
    "problems": [
        {
            "id": "nuc-p-5-1",
            "title": "Alpha Particle Range and Stopping Power in Air and Biological Tissue",
            "statement": "An alpha particle emitted from $^{241}_{95}\\text{Am}$ has a kinetic energy of $E_\\alpha = 5.486 \\text{ MeV}$. (a) Using the Bragg-Kleeman empirical range formula in air at standard temperature and pressure ($R_{\\text{air}} \\approx 0.318 E^{3/2} \\text{ cm}$ with $E$ in MeV), calculate the range of this alpha particle in air. (b) Using the density scaling relationship $R_1 \\rho_1 / \\sqrt{A_1} \\approx R_2 \\rho_2 / \\sqrt{A_2}$, estimate the range of this alpha particle in human biological tissue (density $\\rho = 1.05 \\text{ g/cm}^3$, effective atomic weight $A \\approx 14.6$, compared to air with $\\rho_{\\text{air}} = 0.001225 \\text{ g/cm}^3$ and $A_{\\text{air}} \\approx 14.6$). (c) Discuss the biological hazard of external versus internal contamination with $^{241}\\text{Am}$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Alpha Range in Air",
                    "math": r"R_{\text{air}} \approx 0.318 \times (5.486)^{3/2}\text{ cm} = 0.318 \times (12.850)\text{ cm} \approx 4.086\text{ cm}",
                    "explanation": "Evaluate Bragg-Kleeman formula: range in air is approximately 4.09 cm."
                },
                {
                    "stepName": "Step 2: Calculate Range in Biological Tissue",
                    "math": r"R_{\text{tissue}} \approx R_{\text{air}} \left( \frac{\rho_{\text{air}}}{\rho_{\text{tissue}}} \right) \sqrt{\frac{A_{\text{tissue}}}{A_{\text{air}}}} = 4.086\text{ cm} \times \left( \frac{0.001225\text{ g/cm}^3}{1.05\text{ g/cm}^3} \right) \times 1.0 = 4.086 \times (1.167 \times 10^{-3})\text{ cm} \approx 4.77 \times 10^{-3}\text{ cm} = 47.7\text{ \mu m}",
                    "explanation": "Compute range in tissue using density scaling: approx 48 micrometers."
                },
                {
                    "stepName": "Step 3: Biological Radiation Hazard Assessment",
                    "math": r"R_{\text{tissue}} \approx 48\text{ \mu m} < \text{Stratum Corneum Thickness } (\sim 70\text{ \mu m})",
                    "explanation": "Externally, the dead stratum corneum layer of human skin completely stops the 5.5 MeV alphas, posing zero external hazard. Internally (ingestion or inhalation), 48 um penetrates living cell nuclei, depositing the entire 5.5 MeV Bragg peak directly into DNA, yielding high linear energy transfer (LET) and severe double-strand chromosomal breaks."
                }
            ],
            "answer": "R_{\\text{air}} = 4.09 \\text{ cm}, \\quad R_{\\text{tissue}} = 47.7 \\text{ \\mu m} \\quad (\\text{Zero External Hazard, Lethal Internal Hazard})"
        },
        {
            "id": "nuc-p-5-2",
            "title": "Neutron Moderation: Collisions and Moderating Ratio in Water vs Graphite",
            "statement": "Fast fission neutrons are generated with an average kinetic energy of $E_0 = 2.00 \\text{ MeV}$ and must be slowed down to thermal energy $E_{\\text{th}} = 0.025 \\text{ eV}$. (a) Calculate the total logarithmic energy reduction $\\ln(E_0 / E_{\\text{th}})$. (b) For a light water moderator (Hydrogen, $A=1$, $\\xi = 1.000$) and a nuclear-grade graphite moderator (Carbon, $A=12$, $\\xi = 0.1578$), calculate the average number of collisions $N$ required to achieve thermalization. (c) If the microscopic scattering and absorption cross-sections for thermal neutrons are $\\sigma_s = 4.8 \\text{ b}, \\sigma_a = 0.0035 \\text{ b}$ for Carbon, and $\\sigma_s = 49 \\text{ b}, \\sigma_a = 0.66 \\text{ b}$ for Light Water molecules ($H_2O$), calculate the Moderating Ratio for each material.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Total Logarithmic Reduction",
                    "math": r"\ln\left(\frac{E_0}{E_{\text{th}}}\right) = \ln\left( \frac{2.00 \times 10^6\text{ eV}}{0.025\text{ eV}} \right) = \ln(8.00 \times 10^7) \approx 18.197",
                    "explanation": "Compute total logarithmic decrement from 2 MeV to 0.025 eV."
                },
                {
                    "stepName": "Step 2: Calculate Collisions in Hydrogen and Carbon",
                    "math": r"N_{\text{H}} = \frac{18.197}{1.000} \approx 18.2 \ (\approx 18\text{ collisions}), \quad N_{\text{C}} = \frac{18.197}{0.1578} \approx 115.3 \ (\approx 115\text{ collisions})",
                    "explanation": "Divide logarithmic decrement by xi for each element."
                },
                {
                    "stepName": "Step 3: Calculate Moderating Ratio for Graphite",
                    "math": r"\text{MR}_{\text{C}} = \frac{\xi \sigma_s}{\sigma_a} = \frac{0.1578 \times 4.8\text{ b}}{0.0035\text{ b}} = \frac{0.7574}{0.0035} \approx 216",
                    "explanation": "Evaluate moderating ratio for Carbon."
                },
                {
                    "stepName": "Step 4: Calculate Moderating Ratio for Light Water",
                    "math": r"\text{MR}_{H_2O} = \frac{\xi \Sigma_s}{\Sigma_a} = \frac{(0.925)(49\text{ b})}{0.66\text{ b}} = \frac{45.32}{0.66} \approx 68.7",
                    "explanation": "Evaluate moderating ratio for light water: ~69 (Graphite is 216; Heavy water is ~5800)."
                }
            ],
            "answer": "N_{\\text{H}} \\approx 18 \\text{ collisions}, \\quad N_{\\text{C}} \\approx 115 \\text{ collisions}, \\quad \\text{MR}_{\\text{C}} \\approx 216, \\quad \\text{MR}_{H_2O} \\approx 68.7"
        },
        {
            "id": "nuc-p-5-3",
            "title": "Energy Resolution and FWHM of HPGe Detector vs NaI(Tl) Scintillator",
            "statement": "A High-Purity Germanium (HPGe) detector is used to record the $E_\\gamma = 1332.5 \\text{ keV}$ gamma ray of $^{60}\\text{Co}$. For Germanium at $77\\text{ K}$, the average ionization energy per electron-hole pair is $w = 2.96 \\text{ eV}$ and the Fano factor is $F = 0.110$. (a) Calculate the average number of electron-hole pairs $N$ produced by complete photoelectric absorption of the photon. (b) Calculate the theoretical statistical energy resolution $\\Delta E_{\\text{FWHM}}$ in $\\text{keV}$ and the percentage resolution. (c) A typical $\\text{NaI(Tl)}$ scintillator achieves an energy resolution of $5.8\\%$ FWHM at $1332\\text{ keV}$. By what factor is the HPGe detector resolution superior to the scintillator?",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Mean Number of Charge Carriers",
                    "math": r"N = \frac{E_\gamma}{w} = \frac{1332.5 \times 10^3\text{ eV}}{2.96\text{ eV}} \approx 4.5017 \times 10^5\text{ electron-hole pairs}",
                    "explanation": "Divide total photon energy by electron-hole pair energy."
                },
                {
                    "stepName": "Step 2: Calculate Statistical Variance and Standard Deviation",
                    "math": r"\sigma_N = \sqrt{F \cdot N} = \sqrt{0.110 \times 4.5017 \times 10^5} = \sqrt{49519} \approx 222.5\text{ carriers}",
                    "explanation": "Apply Fano-corrected standard deviation."
                },
                {
                    "stepName": "Step 3: Calculate Theoretical Statistical FWHM",
                    "math": r"\Delta E_{\text{FWHM}} = 2.355 \sigma_E = 2.355 (\sigma_N \cdot w) = 2.355 (222.5 \times 2.96\text{ eV}) = 2.355 \times 658.7\text{ eV} \approx 1551\text{ eV} = 1.551\text{ keV}",
                    "explanation": "Calculate FWHM in keV."
                },
                {
                    "stepName": "Step 4: Percentage Resolution and Comparison with NaI(Tl)",
                    "math": r"\%R_{\text{HPGe}} = \frac{1.551\text{ keV}}{1332.5\text{ keV}} \times 100\% \approx 0.116\%. \quad \Delta E_{\text{NaI}} = 0.058 \times 1332.5\text{ keV} \approx 77.3\text{ keV}",
                    "explanation": "Compute percentage resolution."
                },
                {
                    "stepName": "Step 5: Resolution Advantage Ratio",
                    "math": r"\frac{\Delta E_{\text{NaI}}}{\Delta E_{\text{HPGe}}} = \frac{77.3\text{ keV}}{1.551\text{ keV}} \approx 49.8 \approx 50 \times",
                    "explanation": "The HPGe detector is ~50 times sharper, resolving closely spaced gamma lines that merge into a single broad blob in NaI(Tl)."
                }
            ],
            "answer": "N = 4.50 \\times 10^5, \\quad \\Delta E_{\\text{FWHM}} = 1.55 \\text{ keV} \\quad (0.116\\%), \\quad \\text{Resolution Advantage: } 49.8\\times \\text{ sharper than NaI(Tl)}"
        }
    ]
}

# ==========================================
# UNIT 6: Particle Accelerators & The Standard Model of Particle Physics
# ==========================================
u6 = {
    "unitNumber": 6,
    "unitId": "unit6-accelerators-standard-model",
    "title": "Particle Accelerators & The Standard Model of Particle Physics",
    "description": "State-of-the-art subatomic instrumentation and theoretical framework of particle physics: Van de Graaff, Tandem, linear accelerators (Linacs), and RF cavities; cyclic accelerators, cyclotron resonance frequency, relativistic mass limits, Betatron flux condition, and synchrocyclotron; phase stability principle, alternating gradient strong focusing, and colliding-beam synchrotrons; four fundamental interactions and exchange gauge bosons; leptons, quarks, baryon and meson spectroscopy, Gell-Mann-Nishijima formula, and color charge SU(3); weak isospin SU(2) x U(1), CKM quark mixing matrix, CP violation, and the Higgs mechanism.",
    "sections": [
        {
            "id": "nuc-6-1",
            "title": "Electrostatic & Linear Accelerators: Van de Graaff, Tandem & Linacs",
            "content": r"""<h4>1. Electrostatic Accelerators: The Van de Graaff & Tandem Principle</h4>
<p>Electrostatic accelerators exploit high static potential differences to accelerate charged ions in a single or dual stage:</p>
<ol>
<li><strong>Van de Graaff Accelerator:</strong> A continuous moving insulating belt mechanically transports electric charge from a ground corona source onto a high-voltage hollow metal dome, establishing terminal voltages up to $V \approx 5 - 10\text{ MV}$. The energy gained by an ion of charge $q = z e$ is $T = q V$.</li>
<li><strong>Tandem Van de Graaff Accelerator:</strong> Multiplies kinetic energy by reversing ion charge midway. Negative ions ($X^-$) are accelerated from ground to the positive high-voltage terminal ($+V$). Inside the terminal, the ion traverses a thin carbon foil or gas stripper, stripping off electrons to become a positive ion ($X^{z+}$). The positive ion is subsequently repelled away from the terminal back to ground, gaining additional energy $z e V$:</p>
<div class="math-display">
$$T_{\text{total}} = e V + z e V = (z + 1) e V$$
</div>
<p>For a terminal voltage of $15\text{ MV}$, accelerating Gold ions stripped to $z = +10$ achieves kinetic energies exceeding $(1 + 10) \times 15 = 165\text{ MeV}$ with extraordinary energy precision ($\Delta E / E \sim 10^{-4}$).</li>
</ol>

<h4>2. Radio-Frequency Linear Accelerators (Linacs)</h4>
<p>Rolf Wideröe (1928) bypassed electrostatic voltage breakdown by utilizing a series of collinear cylindrical drift tubes connected to an alternating RF oscillator of frequency $f_{\text{RF}}$. Inside each drift tube, the electric field is zero (Faraday cage shielding); acceleration occurs exclusively across the gaps when the oscillating voltage has the correct accelerating polarity.</p>
<p>To ensure synchronous acceleration as the ion accelerates to speed $v_n$ in drift tube $n$, the particle must transit the tube in exactly half an RF period ($T_{\text{RF}} / 2 = 1 / 2 f_{\text{RF}}$). The required length of drift tube $n$ is:</p>
<div class="math-display">
$$L_n = v_n \frac{T_{\text{RF}}}{2} = \frac{v_n}{2 f_{\text{RF}}} = \frac{1}{2 f_{\text{RF}}} \sqrt{\frac{2 n q V_0}{m}}$$
</div>
<p>Tube lengths increase proportionally to $\sqrt{n}$ at non-relativistic velocities, approaching a constant length $L \approx c / 2 f_{\text{RF}}$ as particles approach the speed of light.</p>"""
        },
        {
            "id": "nuc-6-2",
            "title": "Cyclic Accelerators: Cyclotron Resonance, Relativistic Limits & Betatrons",
            "simulation": "nuc-cyclotron-trajectory-sim",
            "content": r"""<h4>1. Ernest Lawrence's Cyclotron & The Resonance Condition</h4>
<p>Ernest Lawrence (1930) invented the <strong>cyclotron</strong>, bending ions into circular orbits using a uniform perpendicular magnetic field $B$ while accelerating them across the gap between two hollow semi-circular electrodes ("Dees") powered by an alternating RF voltage $V_0 \cos(\omega_{\text{RF}} t)$.</p>
<p>Equating magnetic Lorentz force to centripetal acceleration:</p>
<div class="math-display">
$$q v B = \frac{m v^2}{r} \implies r = \frac{m v}{q B} = \frac{p}{q B}$$
</div>
<p>The orbital angular frequency is independent of radius and speed:</p>
<div class="math-display">
$$\omega_c = \frac{v}{r} = \frac{q B}{m}, \quad f_c = \frac{\omega_c}{2\pi} = \frac{q B}{2\pi m}$$
</div>
<p>This constancy—the <strong>cyclotron resonance condition</strong>—means slow particles on inner orbits and fast particles on outer orbits complete half-revolutions in exactly the same time $t = \pi / \omega_c$. At each Dee crossing, the particle gains energy $\Delta T = 2 q V_0$. At the extraction radius $R_{\text{max}}$, the maximum kinetic energy is:</p>
<div class="math-display">
$$T_{\text{max}} = \frac{q^2 B^2 R_{\text{max}}^2}{2 m}$$
</div>

<h4>2. The Relativistic Limit & The Synchrocyclotron</h4>
<p>As the ion energy approaches relativistic levels ($T \sim 10 - 20\text{ MeV}$ for protons), the particle's relativistic mass increases: $m(v) = \gamma m_0$. The true orbital frequency decreases:</p>
<div class="math-display">
$$\omega_{\text{rel}} = \frac{q B}{\gamma m_0} = \omega_c \sqrt{1 - \frac{v^2}{c^2}} < \omega_c$$
</div>
<p>The accelerating ion falls progressively behind the fixed RF phase, eventually entering a decelerating phase and stopping further acceleration. In a <strong>classical cyclotron</strong>, protons are limited to $T_{\text{max}} \sim 25\text{ MeV}$.</p>
<p>Edwin McMillan and Vladimir Veksler solved this in the <strong>Synchrocyclotron</strong> by dynamically sweeping the applied RF frequency downward in synchronization with relativistic mass growth ($f_{\text{RF}}(t) \propto 1 / \gamma(t)$), enabling proton energies up to $700\text{ MeV}$.</p>

<h4>3. Donald Kerst's Betatron & The 2:1 Flux Condition</h4>
<p>The <strong>Betatron</strong> accelerates electrons in a toroidal vacuum donut via the electric field induced by a time-varying magnetic flux $\Phi(t)$ (Faraday's law of induction). To maintain a constant orbital equilibrium radius $R_0$, the magnetic field at the orbit $B(R_0)$ must equal exactly half the average magnetic field $\bar{B}$ enclosed within the orbit:</p>
<div class="math-display">
$$B(R_0, t) = \frac{1}{2} \bar{B}(t) = \frac{1}{2} \left[ \frac{\Phi(t)}{\pi R_0^2} \right] \quad (\text{Wideröe-Kerst 2:1 Condition})$$
</div>"""
        },
        {
            "id": "nuc-6-3",
            "title": "Synchrotrons: Phase Stability & Alternating Gradient Focusing",
            "content": r"""<h4>1. Principle of Phase Stability</h4>
<p>Discovered independently by Edwin McMillan (1945) and Vladimir Veksler (1944), the <strong>principle of phase stability</strong> is the foundational governing mechanism of all modern high-energy accelerators. Consider a particle crossing an accelerating RF gap at synchronous phase $\phi_s$ with nominal energy $E_s$:</p>
<ul>
<li><strong>Energy Deviation ($\Delta E > 0$):</strong> A particle with excess energy travels faster ($\beta$ higher), but in a relativistic synchrotron its trajectory bends less in dipole magnets, forcing it into a larger circumference orbit ($C \propto p^\alpha$). Above the transition energy ($\gamma > \gamma_t$), the increase in orbital path length dominates over velocity increase, causing the particle to take <em>longer</em> to complete a revolution. It arrives at the next RF cavity <em>later</em> in phase ($\phi > \phi_s$), encountering a smaller accelerating voltage and shedding its energy excess!</li>
<li><strong>Negative Feedback:</strong> Non-synchronous particles perform stable harmonic phase and energy oscillations (<strong>synchrotron oscillations</strong>) around the synchronous particle, forming stable, self-correcting particle bunches.</li>
</ul>

<h4>2. Alternating Gradient (Strong) Focusing</h4>
<p>In 1952, Ernest Courant, Stanley Livingston, and Hartland Snyder revolutionized accelerator design with <strong>Alternating Gradient (AG) focusing</strong>. In earlier weak-focusing synchrotrons, guiding magnetic fields had a slight gradient ($n = - \frac{r}{B} \frac{dB}{dr} \in (0, 1)$), requiring colossal magnet cross-sections weighing thousands of tons (e.g., the Dubna synchrophasotron used a $36,000\text{-ton}$ magnet ring).</p>
<p>Strong focusing utilizes alternating quadrupole magnets:</p>
<ul>
<li>A quadrupole magnet that focuses horizontally ($F$) defocuses vertically ($D$).</li>
<li>Arranging quadrupoles in a periodic $F-D-F-D$ lattice produces net <strong>focusing in both transverse planes simultaneously</strong>, directly analogous to the optical theorem where two thin lenses of focal lengths $+f$ and $-f$ separated by distance $d$ have an overall positive net focal length:
<div class="math-display">
$$\frac{1}{F_{\text{net}}} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2} = \frac{1}{f} - \frac{1}{f} + \frac{d}{f^2} = \frac{d}{f^2} > 0$$
</div></li>
</ul>
<p>Strong focusing compresses beam diameters from dozens of centimeters down to fractions of a millimeter, enabling immense modern rings like CERN's $27\text{-km}$ Large Hadron Collider (LHC) operating at $13.6\text{ TeV}$.</p>"""
        },
        {
            "id": "nuc-6-4",
            "title": "Fundamental Interactions, Gauge Bosons & Three Fermion Generations",
            "content": r"""<h4>1. The Four Fundamental Interactions of Nature</h4>
<p>All physical phenomena in the universe are mediated by four fundamental interactions described by local gauge quantum field theories:</p>
<div class="table-responsive">
<table class="table table-bordered">
<thead>
<tr><th>Interaction</th><th>Gauge Symmetry</th><th>Exchange Gauge Boson</th><th>Mass ($m c^2$)</th><th>Spin</th><th>Relative Strength</th><th>Range</th></tr>
</thead>
<tbody>
<tr><td><strong>Strong</strong></td><td>$SU(3)_C$</td><td>8 Gluons ($g$)</td><td>$0$</td><td>$1$</td><td>$1$</td><td>$\sim 10^{-15}\text{ m}$ (Confinement)</td></tr>
<tr><td><strong>Electromagnetic</strong></td><td>$U(1)_{\text{EM}}$</td><td>Photon ($\gamma$)</td><td>$0$</td><td>$1$</td><td>$10^{-2}$ ($\alpha \approx 1/137$)</td><td>$\infty$ ($1/r^2$)</td></tr>
<tr><td><strong>Weak</strong></td><td>$SU(2)_L$</td><td>$W^\pm, Z^0$</td><td>$80.38\text{ GeV}, 91.19\text{ GeV}$</td><td>$1$</td><td>$10^{-7}$</td><td>$\sim 10^{-18}\text{ m}$ ($\hbar / M_W c$)</td></tr>
<tr><td><strong>Gravitational</strong></td><td>General Relativity</td><td>Graviton ($G$, hypothesized)</td><td>$0$</td><td>$2$</td><td>$10^{-39}$</td><td>$\infty$ ($1/r^2$)</td></tr>
</tbody>
</table>
</div>

<h4>2. Three Generations of Fundamental Matter (Fermions)</h4>
<p>All matter is composed of twelve elementary spin-$1/2$ fermions organized into three sequential generations of increasing mass:</p>
<ul>
<li><strong>Six Leptons (No Color Charge, Immune to Strong Interaction):</strong>
<ul>
<li>Generation 1: Electron ($e^-, 0.511\text{ MeV}$, $Q=-1$) and Electron Neutrino ($\nu_e, < 0.45\text{ eV}$, $Q=0$).</li>
<li>Generation 2: Muon ($\mu^-, 105.66\text{ MeV}$, $Q=-1$) and Muon Neutrino ($\nu_\mu, < 0.17\text{ MeV}$, $Q=0$).</li>
<li>Generation 3: Tau ($\tau^-, 1776.86\text{ MeV}$, $Q=-1$) and Tau Neutrino ($\nu_\tau, < 18.2\text{ MeV}$, $Q=0$).</li>
</ul></li>
<li><strong>Six Quarks (Carry Color Charge: Red, Green, Blue; Feel All Forces):</strong>
<ul>
<li>Generation 1: Up ($u, \approx 2.2\text{ MeV}$, $Q = +2/3 e$) and Down ($d, \approx 4.7\text{ MeV}$, $Q = -1/3 e$).</li>
<li>Generation 2: Charm ($c, \approx 1.28\text{ GeV}$, $Q = +2/3 e$) and Strange ($s, \approx 96\text{ MeV}$, $Q = -1/3 e$).</li>
<li>Generation 3: Top ($t, \approx 173.1\text{ GeV}$, $Q = +2/3 e$) and Bottom ($b, \approx 4.18\text{ GeV}$, $Q = -1/3 e$).</li>
</ul></li>
</ul>
<p>Ordinary matter in the universe is constructed entirely from Generation 1 ($u, d, e^-$); heavier generations are unstable and decay rapidly to the first generation via the weak interaction.</p>"""
        },
        {
            "id": "nuc-6-5",
            "title": "The Quark Model, Gell-Mann-Nishijima Formula & Color Charge",
            "content": r"""<h4>1. The Quark Model of Hadrons</h4>
<p>In 1964, Murray Gell-Mann and George Zweig proposed that all strongly interacting particles (<strong>hadrons</strong>) are bound states of fractional-charge valence quarks:</p>
<ol>
<li><strong>Baryons (Fermions, Half-Integer Spin):</strong> Composed of three valence quarks ($qqq$).
<ul>
<li>Proton: $p = uud \implies Q = \frac{2}{3} + \frac{2}{3} - \frac{1}{3} = +1$.</li>
<li>Neutron: $n = udd \implies Q = \frac{2}{3} - \frac{1}{3} - \frac{1}{3} = 0$.</li>
<li>$\Lambda^0$ hyperon: $uds \implies Q = \frac{2}{3} - \frac{1}{3} - \frac{1}{3} = 0$, Strangeness $S = -1$.</li>
<li>$\Omega^-$ hyperon: $sss \implies Q = 3(-1/3) = -1$, Strangeness $S = -3$, Spin $J = 3/2^+$.</li>
</ul></li>
<li><strong>Mesons (Bosons, Integer Spin):</strong> Composed of a quark and an antiquark ($q\bar{q}'$).
<ul>
<li>Pions: $\pi^+ = u\bar{d}$ ($Q=+1$), $\pi^0 = \frac{u\bar{u} - d\bar{d}}{\sqrt{2}}$ ($Q=0$), $\pi^- = \bar{u}d$ ($Q=-1$).</li>
<li>Kaons: $K^+ = u\bar{s}$ ($S=+1$), $K^0 = d\bar{s}$ ($S=+1$).</li>
</ul></li>
</ol>

<h4>2. The Gell-Mann-Nishijima Formula</h4>
<p>The electric charge $Q$ of any hadron is related to its isospin third component $I_3$, baryon number $B$, and flavor quantum numbers (Strangeness $S$, Charm $C$, Bottomness $B'$, Topness $T$) by the generalized <strong>Gell-Mann-Nishijima formula</strong>:</p>
<div class="math-display">
$$Q = I_3 + \frac{Y}{2} = I_3 + \frac{B + S + C + B' + T}{2}$$
</div>
<p>where $Y = B + S + C + B' + T$ is the <strong>hypercharge</strong>. All strong and electromagnetic interactions strictly conserve $I_3, B, S, C, B', T$, while weak interactions can violate flavor quantum numbers ($\Delta S = \pm 1$).</p>

<h4>3. Color Charge & Quantum Chromodynamics (QCD)</h4>
<p>The discovery of the $\Delta^{++} = uuu$ and $\Omega^- = sss$ baryons in a symmetric ground state ($L=0$, all three spins aligned parallel $J_z = 3/2$) posed a serious paradox: it appeared to violate Fermi-Dirac statistics for three identical fermions. Oscar Greenberg (1964) resolved this by introducing an internal degree of freedom: <strong>Color Charge</strong> (Red, Green, Blue).</p>
<p>The total wave function is antisymmetrized by a color singlet determinant:</p>
<div class="math-display">
$$\psi_{\text{color}} = \frac{1}{\sqrt{6}} (RGB - RBG + GBR - GRB + BRG - BGR)$$
</div>
<p>Quantum Chromodynamics (QCD) is the non-Abelian $SU(3)_C$ gauge theory of color. Because gluons themselves carry color charges, the strong force exhibits two extraordinary phenomena:</p>
<ul>
<li><strong>Asymptotic Freedom:</strong> At extremely short distances / high energies ($q^2 \to \infty$), the effective coupling $\alpha_s(q^2) \to 0$; quarks behave as free, non-interacting particles.</li>
<li><strong>Color Confinement:</strong> The inter-quark potential grows linearly with distance ($V(r) \approx \kappa r$, $\kappa \approx 1\text{ GeV/fm} \approx 160,000\text{ N}$). Quarks and gluons can never be isolated as free particles; separating them creates a flux tube that snaps, creating new quark-antiquark pairs (hadronization).</li>
</ul>"""
        },
        {
            "id": "nuc-6-6",
            "title": "Flavor Mixing, CKM Matrix, CP Violation & The Higgs Mechanism",
            "simulation": "nuc-standard-model-table-sim",
            "content": r"""<h4>1. Weak Flavor Mixing & The Cabibbo-Kobayashi-Maskawa (CKM) Matrix</h4>
<p>In the Standard Model, the quark eigenstates that participate in the weak charged current ($W^\pm$ interactions) are not identical to the mass eigenstates ($d, s, b$), but are quantum linear superpositions parameterized by the unitary $3 \times 3$ <strong>CKM Matrix</strong>:</p>
<div class="math-display">
$$\begin{pmatrix} d' \\ s' \\ b' \end{pmatrix} = \begin{pmatrix} V_{ud} & V_{us} & V_{ub} \\ V_{cd} & V_{cs} & V_{cb} \\ V_{td} & V_{ts} & V_{tb} \end{pmatrix} \begin{pmatrix} d \\ s \\ b \end{pmatrix}$$
</div>
<p>In the standard Wolfenstein parameterization ($\lambda = \sin\theta_C \approx 0.225$):</p>
<div class="math-display">
$$V_{\text{CKM}} \approx \begin{pmatrix} 1 - \frac{\lambda^2}{2} & \lambda & A \lambda^3 (\rho - i\eta) \\ -\lambda & 1 - \frac{\lambda^2}{2} & A \lambda^2 \\ A \lambda^3 (1 - \rho - i\eta) & -A \lambda^2 & 1 \end{pmatrix}$$
</div>
<p>Unitarity of the matrix requires $\sum_k V_{ik} V_{jk}^* = \delta_{ij}$. For the first row:</p>
<div class="math-display">
$$|V_{ud}|^2 + |V_{us}|^2 + |V_{ub}|^2 = 1$$
</div>
<p>Empirical measurements yield $|V_{ud}| \approx 0.9737$, $|V_{us}| \approx 0.2245$, and $|V_{ub}| \approx 0.0038$, verifying unitarity to within $0.05\%$.</p>

<h4>2. CP Violation & The Unitarity Triangle</h4>
<p>The presence of an irreducible complex phase $\eta \ne 0$ in the CKM matrix introduces an asymmetry between matter and antimatter, known as <strong>$CP$ violation</strong> (discovered in neutral Kaon decay by James Cronin and Val Fitch in 1964, and subsequently in $B$ mesons). The orthogonality condition between the first and third columns yields the Unitarity Triangle in the complex plane:</p>
<div class="math-display">
$$V_{ud} V_{ub}^* + V_{cd} V_{cb}^* + V_{td} V_{tb}^* = 0$$
</div>
<p>$CP$ violation in the Standard Model explains how particle decays can favor matter over antimatter, providing a crucial piece of Andrei Sakharov's conditions for the cosmological baryon asymmetry of the universe.</p>

<h4>3. The Brout-Englert-Higgs Mechanism</h4>
<p>Unbroken electroweak $SU(2)_L \times U(1)_Y$ gauge symmetry requires all gauge bosons and fermions to be strictly massless. Peter Higgs, François Englert, and Robert Brout (1964) proposed <strong>spontaneous electroweak symmetry breaking</strong> via a complex scalar doublet field $\Phi$ with a "Mexican hat" potential:</p>
<div class="math-display">
$$V(\Phi) = \mu^2 (\Phi^\dagger \Phi) + \lambda (\Phi^\dagger \Phi)^2 \quad (\mu^2 < 0, \lambda > 0)$$
</div>
<p>The ground state acquires a non-zero vacuum expectation value (VEV):</p>
<div class="math-display">
$$v = \sqrt{\frac{-\mu^2}{\lambda}} \approx 246\text{ GeV}$$
</div>
<p>Three of the four scalar degrees of freedom are "eaten" by the $W^\pm$ and $Z^0$ gauge bosons, providing their longitudinal polarization states and generating their massive rest masses:</p>
<div class="math-display">
$$M_W = \frac{1}{2} g v \approx 80.4\text{ GeV}/c^2, \quad M_Z = \frac{1}{2} \sqrt{g^2 + g'^2} v = \frac{M_W}{\cos\theta_W} \approx 91.2\text{ GeV}/c^2$$
</div>
<p>while the photon remains massless ($M_\gamma = 0$). Quarks and charged leptons acquire their masses through <strong>Yukawa couplings</strong> to the Higgs field ($m_f = \frac{y_f v}{\sqrt{2}}$). The physical excitation of the vacuum field is the <strong>Higgs boson ($H^0$)</strong>, discovered at CERN's Large Hadron Collider in 2012 with a mass $m_H \approx 125.1\text{ GeV}/c^2$.</p>"""
        }
    ],
    "problems": [
        {
            "id": "nuc-p-6-1",
            "title": "Relativistic Limit of Proton Kinetic Energy in a Classical Cyclotron",
            "statement": "A classical Lawrence cyclotron has an extraction pole diameter of $D = 1.60 \\text{ m}$ (radius $R = 0.80 \\text{ m}$) and a uniform magnetic field $B = 1.50 \\text{ T}$. (a) Calculate the non-relativistic cyclotron resonance frequency $f_c$ for protons ($q = 1.602 \\times 10^{-19} \\text{ C}$, $m_0 = 1.673 \\times 10^{-27} \\text{ kg}$). (b) Calculate the nominal proton kinetic energy $T$ at the outer radius in $\\text{MeV}$. (c) In a classical cyclotron, phase slip causes acceleration failure when the relativistic frequency shift $\\Delta f / f$ exceeds approximately $1.5\\%$. Calculate the maximum allowable relativistic kinetic energy $T_{\\text{max}}$ before synchronization is lost.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Cyclotron Resonance Frequency",
                    "math": r"f_c = \frac{q B}{2\pi m_0} = \frac{(1.6022 \times 10^{-19}\text{ C})(1.50\text{ T})}{2\pi (1.6726 \times 10^{-27}\text{ kg})} \approx \frac{2.4033 \times 10^{-19}}{1.0509 \times 10^{-26}}\text{ Hz} \approx 2.287 \times 10^7\text{ Hz} = 22.87\text{ MHz}",
                    "explanation": "Evaluate cyclotron resonance frequency for protons: 22.87 MHz."
                },
                {
                    "stepName": "Step 2: Nominal Extraction Kinetic Energy",
                    "math": r"p = q B R = (1.6022 \times 10^{-19})(1.50)(0.80)\text{ N}\cdot\text{s} = 1.9226 \times 10^{-19}\text{ kg}\cdot\text{m/s} = 360\text{ MeV}/c",
                    "explanation": "Compute relativistic momentum at maximum radius."
                },
                {
                    "stepName": "Step 3: Evaluate Kinetic Energy",
                    "math": r"E = \sqrt{p^2 c^2 + m_0^2 c^4} = \sqrt{(360)^2 + (938.3)^2}\text{ MeV} = \sqrt{1.296 \times 10^5 + 8.804 \times 10^5}\text{ MeV} = \sqrt{1.010 \times 10^6}\text{ MeV} \approx 1005\text{ MeV} \implies T = E - m_0 c^2 \approx 66.7\text{ MeV}",
                    "explanation": "Calculate relativistic kinetic energy: ~66.7 MeV."
                },
                {
                    "stepName": "Step 4: Relativistic Phase Slip Limit",
                    "math": r"\frac{\Delta f}{f_c} = \frac{f_c - f_{\text{rel}}}{f_c} = 1 - \frac{1}{\gamma} \approx 0.015 \implies \gamma \approx \frac{1}{0.985} \approx 1.0152 \implies T_{\text{max}} = (\gamma - 1) m_0 c^2 \approx 0.0152 \times 938.3\text{ MeV} \approx 14.3\text{ MeV}",
                    "explanation": "Calculate kinetic energy limit: without synchrocyclotron frequency modulation, protons de-synchronize at ~14.3 MeV."
                }
            ],
            "answer": "f_c = 22.87 \\text{ MHz}, \\quad T_{\\text{nom}} = 66.7 \\text{ MeV}, \\quad T_{\\text{max}} \\approx 14.3 \\text{ MeV} \\quad (\\text{Relativistic Desynchronization Limit})"
        },
        {
            "id": "nuc-p-6-2",
            "title": "Gell-Mann-Nishijima Formula and Quantum Numbers of Hadrons",
            "statement": "Using the quark model and the Gell-Mann-Nishijima formula $Q = I_3 + \\frac{B + S + C + B' + T}{2}$: (a) For the $\\Delta^{++}$ resonance ($uuu$), determine the baryon number $B$, strangeness $S$, charm $C$, isospin third component $I_3$, and verify its electric charge $Q$. (b) For the $\\Omega^-$ hyperon ($sss$), evaluate $B, S, C, I_3$, and verify $Q$. (c) For the charmed meson $D^0$ ($c\\bar{u}$), evaluate its quark flavor contents, hypercharge $Y$, and net charge $Q$.",
            "steps": [
                {
                    "stepName": "Step 1: Quantum Numbers of Delta++ (uuu)",
                    "math": r"q_u: B=1/3, I_3=+1/2, S=0. \implies B = 3(1/3) = 1, \quad I_3 = 3(+1/2) = +3/2, \quad S=0. \implies Q = 3/2 + \frac{1 + 0}{2} = 3/2 + 1/2 = +2e",
                    "explanation": "Compute Delta++ quantum numbers: B=1, I_3=+3/2, S=0, Q=+2."
                },
                {
                    "stepName": "Step 2: Quantum Numbers of Omega- (sss)",
                    "math": r"q_s: B=1/3, I_3=0, S=-1. \implies B = 3(1/3) = 1, \quad I_3 = 0, \quad S = 3(-1) = -3. \implies Q = 0 + \frac{1 - 3}{2} = -1e",
                    "explanation": "Compute Omega- quantum numbers: B=1, I_3=0, S=-3, Q=-1."
                },
                {
                    "stepName": "Step 3: Quantum Numbers of D0 Meson (c anti-u)",
                    "math": r"c: B=1/3, C=+1, I_3=0; \quad \bar{u}: B=-1/3, C=0, I_3=-1/2. \implies B = 0, \quad C = +1, \quad I_3 = -1/2. \implies Q = -1/2 + \frac{0 + 1}{2} = 0",
                    "explanation": "Compute D0 meson quantum numbers: B=0, C=+1, I_3=-1/2, Q=0."
                }
            ],
            "answer": "\\Delta^{++}: B=1, I_3=+3/2, S=0, Q=+2; \\quad \\Omega^-: B=1, I_3=0, S=-3, Q=-1; \\quad D^0: B=0, C=+1, I_3=-1/2, Q=0"
        },
        {
            "id": "nuc-p-6-3",
            "title": "CKM Matrix Unitarity and Weak Decay Coupling Evaluation",
            "statement": "High-precision experimental values for the first row elements of the Cabibbo-Kobayashi-Maskawa (CKM) matrix are: $|V_{ud}| = 0.97370 \\pm 0.00014$ (from superallowed $0^+ \\to 0^+$ nuclear beta decays), $|V_{us}| = 0.22450 \\pm 0.00080$ (from semileptonic kaon decays $K_{e3}$), and $|V_{ub}| = (3.82 \\pm 0.24) \\times 10^{-3}$ (from charmless semileptonic $B$ meson decays). (a) Test the unitarity relation $|V_{ud}|^2 + |V_{us}|^2 + |V_{ub}|^2 = 1$ and determine the deviation from unity. (b) Calculate the Cabibbo angle $\\theta_C = \\arcsin(|V_{us}|)$ in degrees. (c) Explain why this precise test sets strict constraints on hypothetical 4th generation quarks.",
            "steps": [
                {
                    "stepName": "Step 1: Compute Squares of Matrix Elements",
                    "math": r"|V_{ud}|^2 = (0.97370)^2 \approx 0.948092, \quad |V_{us}|^2 = (0.22450)^2 \approx 0.050400, \quad |V_{ub}|^2 = (0.00382)^2 \approx 0.000015",
                    "explanation": "Square each first-row matrix element."
                },
                {
                    "stepName": "Step 2: Evaluate Sum and Deviation from Unitarity",
                    "math": r"\sum_{q=d,s,b} |V_{uq}|^2 = 0.948092 + 0.050400 + 0.000015 = 0.998507 \implies 1 - \sum |V_{uq}|^2 \approx 0.00149 \pm 0.0007",
                    "explanation": "Sum of squares is 0.9985, consistent with 1 within ~2 standard deviations (0.15% agreement!)."
                },
                {
                    "stepName": "Step 3: Calculate Cabibbo Angle",
                    "math": r"\theta_C = \arcsin(0.22450) \approx 0.22644\text{ rad} \approx 12.97^\circ",
                    "explanation": "Compute Cabibbo mixing angle: approx 13.0 degrees."
                },
                {
                    "stepName": "Step 4: Constraint on 4th Generation Quarks",
                    "math": r"|V_{ub'}|^2 = 1 - (|V_{ud}|^2 + |V_{us}|^2 + |V_{ub}|^2) \le 0.002 \implies |V_{ub'}| < 0.045",
                    "explanation": "If a fourth generation up-type quark b' existed, unitarity of a 4x4 matrix would require |V_ud|^2 + |V_us|^2 + |V_ub|^2 + |V_ub'|^2 = 1. The fact that the first three terms sum to 0.9985 severely constrains any fourth generation coupling to |V_ub'| < 0.045."
                }
            ],
            "answer": "\\sum |V_{uq}|^2 = 0.9985 \\pm 0.0007 \\quad (\\text{Unitarity Verified to } 0.15\\%), \\quad \\theta_C = 12.97^\\circ, \\quad |V_{ub'}| < 0.045"
        }
    ]
}

with open("nuc_u5.json", "w") as f:
    json.dump(u5, f, indent=2)
print("nuc_u5.json created successfully!")

with open("nuc_u6.json", "w") as f:
    json.dump(u6, f, indent=2)
print("nuc_u6.json created successfully!")
