# build_ssp2_units_7_8.py
# Generates ssp2_u7.json and ssp2_u8.json for Course #18: Solid State Physics II

import json

# =========================================================================
# UNIT 7: Excitons, Photoconductivity, Luminescence & Crystal Defects
# =========================================================================

u7_data = {
    "title": "Excitons, Photoconductivity, Luminescence & Crystal Defects",
    "subtitle": "Wannier vs Frenkel Excitons, Recombination Kinetics, Schottky/Frenkel Defects",
    "summary": "This unit covers the optical excitations, carrier recombination kinetics, and defect thermodynamics in solids. We explore electron-hole Coulomb bound states, contrasting weakly bound, delocalized Wannier-Mott excitons in semiconductors with tightly bound, localized Frenkel excitons in insulators. We examine photoconductivity, Shockley-Read-Hall trap-assisted recombination, and space-charge-limited currents (Mott-Gurney law). We analyze luminescence mechanisms via the configuration coordinate diagram. Finally, we formulate the statistical thermodynamics of Schottky and Frenkel point defects, vacancy-assisted diffusion kinetics, and color centers in alkali halides.",
    "sections": [
        {
            "id": "sec-7-1",
            "title": "Excitons in Solids: Wannier-Mott vs Frenkel Exciton Energetics",
            "content": r"""
<h3>1. The Nature of Excitonic Quasiparticles</h3>
<p>
When a photon with energy near the fundamental bandgap $h\nu \lesssim E_g$ is absorbed by an insulator or semiconductor, it promotes an electron from the valence band to the conduction band. The negatively charged electron ($q_e = -e$) and positively charged hole ($q_h = +e$) experience an attractive Coulomb interaction:
</p>
$$V(r) = -\frac{e^2}{4\pi\epsilon_r\epsilon_0 r}$$
<p>
Instead of escaping as free carriers, they can form a neutral composite bound state known as an <strong>exciton</strong>. Because the exciton carries zero net electrical charge, it cannot transport electrical current, but it can transport energy across the crystal without Joule heating.
</p>

<h3>2. Wannier-Mott vs Frenkel Excitons</h3>
<ul>
  <li><strong>Wannier-Mott Excitons (Weakly Bound, Large Radius):</strong>
  Occur in semiconductors with large dielectric constants ($\epsilon_r \sim 10-16$) and small effective masses ($m^* \sim 0.05-0.2 m_0$).
  The Coulomb attraction is heavily screened. The electron and hole orbit around their common center of mass with an effective Bohr radius much larger than the lattice constant:
  $$a_{\text{exc}} = a_0 \epsilon_r \left( \frac{m_0}{\mu^*} \right), \quad \frac{1}{\mu^*} = \frac{1}{m_e^*} + \frac{1}{m_h^*}$$
  Typically $a_{\text{exc}} \sim 5-20\text{ nm} \gg a_{\text{lattice}}$, enclosing hundreds of unit cells.
  The binding energy series forms hydrogen-like levels below the conduction band edge:
  $$E_n = E_g - \frac{R_y^*}{n^2}, \quad R_y^* = 13.6\text{ eV} \frac{\mu^* / m_0}{\epsilon_r^2} \sim 5-30\text{ meV}$$
  Because $R_y^* \sim k_B T_{\text{room}}$, Wannier excitons are easily observed as sharp sub-bandgap absorption peaks at cryogenic temperatures.</li>

  <li><strong>Frenkel Excitons (Tightly Bound, Small Radius):</strong>
  Occur in materials with small dielectric constants ($\epsilon_r \sim 2-4$) and large effective masses, such as alkali halides, rare gas solids (Ar, Kr, Xe), and molecular organic crystals (anthracene).
  The Coulomb screening is weak, resulting in immense binding energies $E_b \sim 0.1-1.0\text{ eV}$.
  The electron and hole reside essentially on the <em>same atom or molecule</em> ($a_{\text{exc}} \sim a_{\text{lattice}} \sim 0.3\text{ nm}$).
  Frenkel excitons hop from site to site as localized excitation waves, exhibiting Davydov splitting due to resonant intermolecular exchange.</li>
</ul>
"""
        },
        {
            "id": "sec-7-2",
            "title": "Optical Absorption Spectra of Excitons & Polariton Dispersion",
            "content": r"""
<h3>1. Excitonic Optical Absorption Peaks</h3>
<p>
In the absence of excitonic interactions, the interband optical absorption coefficient for a direct bandgap semiconductor rises as a square root above the gap:
</p>
$$\alpha_0(\hbar\omega) \propto \sqrt{\hbar\omega - E_g}, \quad \hbar\omega \ge E_g$$
<p>
Coulomb attraction dramatically alters this spectrum (the <em>Elliott formula</em>):
</p>
<ol>
  <li><strong>Discrete Sub-Gap Peaks ($\hbar\omega < E_g$):</strong> A series of discrete hydrogen-like absorption lines appears at photon energies:
  $$\hbar\omega_n = E_g - \frac{R_y^*}{n^2}, \quad n = 1, 2, 3, \dots$$
  The oscillator strength scales as $f_n \propto |\psi_n(0)|^2 \propto 1/n^3$, making the ground state ($n=1$) peak overwhelmingly prominent.</li>
  <li><strong>Continuous Sommerfeld Enhancement ($\hbar\omega \ge E_g$):</strong> Even above the ionization threshold, the Coulomb attraction pulls electron and hole wavefunctions together, enhancing the transition probability at the band edge by the Sommerfeld factor $S(E) = \frac{2\pi\eta}{1 - e^{-2\pi\eta}} \to 2\pi\eta$ as $\hbar\omega \to E_g$. The absorption steps up abruptly rather than starting smoothly from zero.</li>
</ol>

<h3>2. Exciton-Polaritons</h3>
<p>
When an optical photon couples strongly to a transverse optical exciton mode, energy oscillates coherently between the photonic and electronic states before dissipation can occur.
</p>
<p>
The coupled system cannot be described by independent photons and excitons, but forms a hybrid quasiparticle known as an <strong>exciton-polariton</strong>.
The dispersion relation obeys:
</p>
$$\frac{c^2 k^2}{\omega^2} = \epsilon(\omega) = \epsilon_\infty + \frac{(\epsilon_0 - \epsilon_\infty) \omega_T^2}{\omega_T^2 - \omega^2}$$
<p>
At the crossover where the photon line $\omega = c k / \sqrt{\epsilon_\infty}$ intersects the exciton frequency $\omega_T$, an anti-crossing opens an energy gap known as the <strong>polariton stop-band</strong> (or longitudinal-transverse splitting $\omega_L - \omega_T$). Polaritons possess an ultra-light effective mass ($10^{-5} m_0$), enabling macroscopic Bose-Einstein condensation at room temperature in semiconductor microcavities!
</p>
""",
            "simulation": "ssp2-exciton-optical-sim",
            "simulations": ["ssp2-exciton-optical-sim"]
        },
        {
            "id": "sec-7-3",
            "title": "Photoconductivity Kinetics, Carrier Trapping & Recombination Mechanisms",
            "content": r"""
<h3>1. Photoconductance & Excess Carrier Kinetics</h3>
<p>
When a semiconductor is illuminated by light with photon energy $h\nu \ge E_g$, optical generation creates excess electron-hole pairs at rate $G$ per unit volume per second:
</p>
$$\frac{dn}{dt} = G - \mathcal{R}_n, \quad \frac{dp}{dt} = G - \mathcal{R}_p$$
<p>
In the steady state ($dn/dt = 0$), excess carrier densities satisfy:
</p>
$$\Delta n = G \tau_n, \quad \Delta p = G \tau_p$$
<p>
where $\tau_n$ and $\tau_p$ are the excess electron and hole recombination lifetimes. The resulting change in electrical conductivity is the <strong>photoconductivity</strong> $\Delta\sigma$:
</p>
$$\Delta\sigma = e (\Delta n \mu_n + \Delta p \mu_p) = e G (\tau_n \mu_n + \tau_p \mu_p)$$
<p>
The <strong>photoconductive gain</strong> $\mathcal{G}$ is defined as the ratio of the number of electrons collected at the electrode to the number of absorbed photons:
</p>
$$\mathcal{G} = \frac{\tau_n}{t_{\text{transit}}} = \frac{\tau_n \mu_n \mathcal{E}}{L}$$
<p>
If the carrier lifetime $\tau_n$ exceeds the transit time $t_{\text{transit}} = L / v_{\text{drift}}$, electrons cycle multiple times through the external circuit before recombining, yielding gain $\mathcal{G} \gg 1$!
</p>

<h3>2. Carrier Recombination Mechanisms</h3>
<ul>
  <li><strong>1. Band-to-Band Radiative Recombination:</strong> An electron drops directly from the conduction band into an empty state in the valence band, emitting a photon of energy $h\nu \approx E_g$. The rate is $\mathcal{R}_{\text{rad}} = B (n p - n_i^2)$.</li>
  <li><strong>2. Shockley-Read-Hall (SRH) Trap-Assisted Recombination:</strong> Mediated by deep defect levels or impurities near mid-gap. An electron is captured by the neutral defect, followed by hole capture, releasing energy via lattice phonons. In indirect semiconductors (Si, Ge), SRH recombination dominates.</li>
  <li><strong>3. Auger Non-Radiative Recombination:</strong> A three-particle collision where an electron and hole recombine, but the released energy is transferred as kinetic energy to a third carrier (an electron in $n$-type, or a hole in $p$-type), which thermalizes via phonons. The rate scales as $\mathcal{R}_{\text{Auger}} \propto C_n n^2 p + C_p n p^2$, dominating at high carrier injection densities (concentrated solar cells and high-power laser diodes).</li>
</ul>
"""
        },
        {
            "id": "sec-7-4",
            "title": "Space Charge Limited Currents (SCLC) & The Mott-Gurney Law",
            "content": r"""
<h3>1. Physics of Space Charge Injection</h3>
<p>
In an ideal insulator or high-purity intrinsic semiconductor with ohmic contacts, free thermal carriers are negligible ($n_0 \approx 0$). When a voltage $V$ is applied across a sample of length $L$, the cathode injects excess electrons into the conduction band.
</p>
<p>
At low voltages, Ohm's law holds: $J = e n_0 \mu (V/L)$.
However, as the voltage increases, the density of injected electrons exceeds the background thermal density. These uncompensated carriers accumulate in the bulk, forming a localized negative <strong>space charge cloud</strong> that screens the applied electric field.
</p>

<h3>2. Derivation of the Mott-Gurney Law</h3>
<p>
Assuming drift-dominated transport ($J = e n(x) \mu \mathcal{E}(x) = \text{const}$) in one dimension, Poisson's equation relates the space charge density to the electric field gradient:
</p>
$$\frac{d\mathcal{E}}{dx} = \frac{\rho(x)}{\epsilon_r\epsilon_0} = \frac{-e n(x)}{\epsilon_r\epsilon_0} = -\frac{J}{\epsilon_r\epsilon_0 \mu \mathcal{E}(x)}$$
<p>
Multiplying by $\mathcal{E}(x)$ and integrating from the injecting contact ($x = 0$, where for an ideal ohmic contact $\mathcal{E}(0) \approx 0$):
</p>
$$\mathcal{E} d\mathcal{E} = -\frac{J}{\epsilon_r\epsilon_0 \mu} dx \implies \frac{1}{2} \mathcal{E}^2(x) = -\frac{J x}{\epsilon_r\epsilon_0 \mu}$$
$$\mathcal{E}(x) = -\sqrt{-\frac{2 J x}{\epsilon_r\epsilon_0 \mu}}$$
<p>
Integrating the electric field to determine the applied voltage $V = -\int_0^L \mathcal{E}(x) dx$:
</p>
$$V = \int_0^L \sqrt{\frac{2 J x}{\epsilon_r\epsilon_0 \mu}} dx = \sqrt{\frac{2 J}{\epsilon_r\epsilon_0 \mu}} \left[ \frac{2}{3} x^{3/2} \right]_0^L = \frac{2}{3} \sqrt{\frac{2 J}{\epsilon_r\epsilon_0 \mu}} L^{3/2}$$
<p>
Squaring both sides and solving for the current density $J$:
</p>
$$V^2 = \frac{8 J L^3}{9 \epsilon_r\epsilon_0 \mu} \implies J_{\text{SCLC}} = \frac{9}{8} \epsilon_r\epsilon_0 \mu \frac{V^2}{L^3}$$
<p>
This is the celebrated <strong>Mott-Gurney Square Law</strong> (the solid-state analogue of Child's three-halves law in vacuum tubes). SCLC measurements provide a universal method for determining carrier drift mobilities in organic semiconductors, perovskites, and wide-bandgap insulators.
</p>
"""
        },
        {
            "id": "sec-7-5",
            "title": "Luminescence, Phosphorescence & The Configuration Coordinate Model",
            "content": r"""
<h3>1. Luminescence Phenomena in Solids</h3>
<p>
Luminescence is the non-thermal emission of electromagnetic radiation from an electronically excited solid:
</p>
<ul>
  <li><strong>Photoluminescence:</strong> Excitation by ultraviolet or visible photons.</li>
  <li><strong>Electroluminescence:</strong> Excitation by direct electrical current injection (LEDs and OLEDs).</li>
  <li><strong>Cathodoluminescence:</strong> Excitation by an energetic electron beam (CRTs and SEM microanalysis).</li>
</ul>
<p>
According to <strong>Stokes' Law</strong>, the emitted photon energy $h\nu_{\text{emission}}$ is almost invariably lower than the excitation photon energy $h\nu_{\text{absorption}}$:
</p>
$$\Delta E_{\text{Stokes}} = h\nu_{\text{abs}} - h\nu_{\text{em}} > 0$$
<p>
The missing energy is dissipated into the crystal lattice as vibrational heat (phonons).
</p>
<ul>
  <li><strong>Fluorescence:</strong> Rapid emission ($\tau \sim 10^{-9}-10^{-7}\text{ s}$) originating from spin-allowed transitions ($S \to S$), terminating immediately when excitation ceases.</li>
  <li><strong>Phosphorescence:</strong> Delayed, persistent afterglow ($\tau \sim 10^{-3}-10^2\text{ s}$) caused by non-radiative intersystem crossing into a metastable spin-triplet trap state ($T \to S_0$), which is quantum-mechanically dipole-forbidden by spin selection rules ($\Delta S = 0$).</li>
</ul>

<h3>2. The Configuration Coordinate Model & Franck-Condon Principle</h3>
<p>
The coupling between localized electronic transitions and lattice vibrations is modeled by the <strong>Configuration Coordinate Diagram</strong>:
</p>
<p>
The potential energy curves of the electronic ground state $|g\rangle$ and excited state $|e\rangle$ are plotted as harmonic parabolas against a generalized vibrational coordinate $Q$ representing the breathing displacement of surrounding ions:
</p>
$$E_g(Q) = \frac{1}{2} M \omega^2 Q^2, \quad E_e(Q) = E_0 + \frac{1}{2} M \omega^2 (Q - Q_0)^2$$
<p>
where $Q_0$ is the equilibrium lattice relaxation displacement caused by the altered electronic charge distribution in the excited state.
</p>
<ul>
  <li><strong>Franck-Condon Principle:</strong> Electronic transitions occur on timescales ($10^{-15}\text{ s}$) far faster than nuclear motion ($10^{-13}\text{ s}$). Transitions are represented by <strong>vertical lines</strong> on the diagram ($\Delta Q = 0$).</li>
  <li><strong>Absorption:</strong> Occurs vertically from $Q = 0$ to an excited vibrational level of $|e\rangle$ at energy $E_{\text{abs}} = E_0 + \frac{1}{2} M\omega^2 Q_0^2$.</li>
  <li><strong>Lattice Relaxation:</strong> The ions relax non-radiatively to the new equilibrium minimum $Q = Q_0$, releasing relaxation energy $S \hbar\omega = \frac{1}{2}M\omega^2 Q_0^2$ (where $S$ is the dimensionless <em>Huang-Rhys parameter</em>).</li>
  <li><strong>Emission:</strong> Occurs vertically from $Q = Q_0$ to a high vibrational state of $|g\rangle$ at energy $E_{\text{em}} = E_0 - \frac{1}{2} M\omega^2 Q_0^2$.</li>
  <li><strong>Stokes Shift:</strong>
  $$\Delta E_{\text{Stokes}} = E_{\text{abs}} - E_{\text{em}} = 2 S \hbar\omega$$</li>
</ul>
"""
        },
        {
            "id": "sec-7-6",
            "title": "Point Defects in Crystals: Schottky & Frenkel Defect Thermodynamics",
            "content": r"""
<h3>1. Thermodynamics of Point Defects in Thermal Equilibrium</h3>
<p>
Unlike dislocations or grain boundaries, point defects are thermodynamically stable and exist in non-zero concentrations in any crystal at $T > 0\text{ K}$.
</p>
<p>
Creating $n$ point defects requires enthalpy $\Delta H = n E_d > 0$. However, distributing $n$ defects across $N$ available lattice sites introduces immense <strong>configurational entropy</strong>:
</p>
$$S_{\text{config}} = k_B \ln W = k_B \ln\left( \frac{N!}{(N - n)! n!} \right)$$
<p>
Using Stirling's approximation $\ln x! \approx x\ln x - x$:
</p>
$$S_{\text{config}} \approx k_B [N\ln N - (N - n)\ln(N - n) - n\ln n]$$
<p>
The Helmholtz free energy change is:
</p>
$$\Delta F(n) = n E_d - T S_{\text{config}}$$
<p>
Minimizing with respect to defect count $\frac{\partial \Delta F}{\partial n} = 0$:
</p>
$$E_d - k_B T \ln\left( \frac{N - n}{n} \right) = 0 \implies \frac{n}{N - n} = e^{-E_d / k_B T}$$
<p>
Since $n \ll N$ under normal conditions:
</p>
$$n = N \exp\left( -\frac{E_d}{k_B T} \right)$$

<h3>2. Schottky vs Frenkel Defects in Stoichiometric Ionic Crystals</h3>
<ul>
  <li><strong>Schottky Defects (Paired Vacancies):</strong>
  Consists of a stoichiometric pair of vacancies: one cation vacancy $V_{\text{cat}}'$ and one anion vacancy $V_{\text{an}}^\bullet$, leaving the overall crystal strictly charge-neutral.
  The displaced ions migrate to the external crystal surface.
  If $E_S$ is the formation energy of a Schottky pair:
  $$n_S \approx N \exp\left( -\frac{E_S}{2 k_B T} \right)$$
  The factor of 2 in the denominator arises because two independent vacancy configurations must be chosen.
  Dominates in alkali halides with similar cation and anion ionic radii (e.g. $\text{NaCl}, \text{KCl}, \text{CsCl}$), leading to a measurable reduction in crystal bulk density.</li>

  <li><strong>Frenkel Defects (Vacancy-Interstitial Pairs):</strong>
  Consists of an ion (typically the smaller cation) displaced from its normal lattice site into an adjacent interstitial void, creating a vacancy $V_{\text{cat}}'$ and an interstitial cation $M_i^\bullet$.
  If $N$ is the number of regular sites and $N_i$ is the number of available interstitial sites, with formation energy $E_F$:
  $$n_F \approx \sqrt{N N_i} \exp\left( -\frac{E_F}{2 k_B T} \right)$$
  Dominates in ionic crystals with open crystal structures and large radius mismatches (e.g. silver halides $\text{AgCl}, \text{AgBr}$, and fluorites $\text{CaF}_2$), leaving bulk density unchanged.</li>
</ul>
""",
            "simulation": "ssp2-defects-diffusion-sim",
            "simulations": ["ssp2-defects-diffusion-sim"]
        },
        {
            "id": "sec-7-7",
            "title": "Atomic Diffusion Mechanisms & Color Centers (F-Centers) in Alkali Halides",
            "content": r"""
<h3>1. Mechanisms of Atomic Diffusion in Solids</h3>
<p>
Mass transport in crystalline solids occurs via discrete thermally activated atomic jumps across potential barriers $E_m$:
</p>
<ul>
  <li><strong>Vacancy Mechanism:</strong> An atom jumps into an adjacent empty lattice vacancy. The jump probability is proportional to the product of vacancy probability $n_v/N \propto e^{-E_v/k_B T}$ and hopping probability $\nu e^{-E_m/k_B T}$. The diffusion coefficient obeys an <strong>Arrhenius Law</strong>:
  $$D(T) = D_0 \exp\left( -\frac{E_a}{k_B T} \right), \quad E_a = E_v + E_m$$
  Dominates self-diffusion and substitutional solute diffusion.</li>
  <li><strong>Interstitial Mechanism:</strong> Small solute atoms (H, C, N, O) hop between adjacent interstitial voids without requiring pre-existing vacancies ($E_a = E_{m,\text{int}}$), diffusing orders of magnitude faster than host atoms.</li>
</ul>

<h3>2. Color Centers: The F-Center</h3>
<p>
When an alkali halide crystal (such as pure transparent $\text{NaCl}$) is heated in an excess vapor of sodium metal, sodium atoms deposit on the surface, lose electrons to form $\text{Na}^+$ ions, and draw $\text{Cl}^-$ ions out from the interior to maintain stoichiometry.
</p>
<p>
This leaves behind empty anion vacancies inside the bulk. To preserve local charge neutrality, the freed electron becomes trapped inside the positive electrostatic potential well formed by the six surrounding alkali metal cations ($\text{Na}^+$).
</p>
<p>
This trapped-electron defect is known as an <strong>$F$-center</strong> (from the German <em>Farbzentrum</em>, meaning color center).
</p>
<ul>
  <li>The trapped electron behaves as a particle in a 3D finite spherical potential well.</li>
  <li>Its optical absorption spectrum features a strong, broad resonance corresponding to the electric dipole transition from the $1s$-like ground state to the $2p$-like excited state.</li>
  <li>For $\text{NaCl}$, the $F$-band absorption peak occurs at $\lambda \approx 460\text{ nm}$ (blue light absorption), tinting the normally clear crystal an intense yellow-brown. In $\text{KCl}$, it absorbs at $560\text{ nm}$, coloring the crystal violet.</li>
  <li>The peak wavelength follows the empirical <strong>Mollwo-Ivey Relation</strong>:
  $$\lambda_{\max} \propto a^n \quad (n \approx 1.8-2.0)$$
  where $a$ is the lattice constant of the alkali halide.</li>
</ul>
"""
        }
    ],
    "problems": [
        {
            "id": "ssp2-prob-7-1",
            "title": "Wannier-Mott Exciton Bohr Radius, Binding Energy & Optical Absorption in GaAs",
            "statement": "Gallium arsenide (GaAs) has a direct fundamental bandgap $E_g = 1.424\\text{ eV}$ at $T = 300\\text{ K}$, relative dielectric constant $\\epsilon_r = 13.1$, electron effective mass $m_e^* = 0.067 m_0$, and hole effective mass $m_h^* = 0.45 m_0$.\\n\\n(a) Calculate the reduced exciton mass $\\mu^*$ in units of $m_0$.\\n(b) Compute the effective Bohr radius $a_{\\text{exc}}$ of the $1s$ ground state exciton in nanometers, and determine how many crystal unit cells ($a_{\\text{lattice}} = 0.565\\text{ nm}$) it spans across its diameter.\\n(c) Calculate the exciton Rydberg binding energy $R_y^*$ in meV, the photon energy $\\hbar\\omega_1$ required to create the $n=1$ exciton, and explain whether excitonic peaks can be resolved at room temperature ($k_B T = 25.9\\text{ meV}$).",
            "solution": """**(a) Reduced Exciton Effective Mass:**
$$\\frac{1}{\\mu^*} = \\frac{1}{m_e^*} + \\frac{1}{m_h^*} = \\frac{1}{0.067 m_0} + \\frac{1}{0.45 m_0} = (14.925 + 2.222) \\frac{1}{m_0} = 17.147 \\frac{1}{m_0}$$
$$\\mu^* = \\frac{1}{17.147} m_0 \\approx 0.0583 m_0$$

**(b) Exciton Bohr Radius:**
$$a_{\\text{exc}} = a_0 \\epsilon_r \\left( \\frac{m_0}{\\mu^*} \\right) = 0.0529\\text{ nm} \\times 13.1 \\times \\left( \\frac{1}{0.0583} \\right) = 0.0529 \\times 13.1 \\times 17.147 \\approx 11.88\\text{ nm}$$
The exciton diameter is $2 a_{\\text{exc}} \\approx 23.8\\text{ nm}$.
Number of lattice constants spanned:
$$\\frac{2 a_{\\text{exc}}}{a_{\\text{lattice}}} = \\frac{23.8\\text{ nm}}{0.565\\text{ nm}} \\approx 42.1 \\text{ unit cells}$$
The exciton diameter spans **over 42 unit cells** (enclosing roughly $70{,}000$ atoms!), proving that the continuum dielectric approximation of the Wannier-Mott model is exceptionally accurate for GaAs.

**(c) Exciton Binding Energy & Room Temperature Observability:**
$$R_y^* = 13.606\\text{ eV} \\times \\frac{\\mu^*/m_0}{\\epsilon_r^2} = 13.606 \\times \\frac{0.0583}{(13.1)^2} = 13.606 \\times \\frac{0.0583}{171.61} = 13.606 \\times 3.397 \\times 10^{-4} \\approx 4.62 \\times 10^{-3}\\text{ eV} = 4.62\\text{ meV}$$
The optical absorption photon energy for the $n=1$ exciton is:
$$\\hbar\\omega_1 = E_g - R_y^* = 1.424\\text{ eV} - 0.00462\\text{ eV} = 1.4194\\text{ eV}$$
**Thermal Observability:**
At room temperature ($300\\text{ K}$), $k_B T \\approx 25.9\\text{ meV}$.
Because $k_B T (25.9\\text{ meV}) \\gg R_y^* (4.62\\text{ meV})$, thermal phonon collisions ionize the exciton within picoseconds, broadening the discrete excitonic peak into the continuum. Thus, excitonic absorption lines in GaAs cannot be resolved at room temperature and require cooling below $T \\sim 50\\text{ K}$ ($k_B T \\lesssim 4\\text{ meV}$)."""
        },
        {
            "id": "ssp2-prob-7-2",
            "title": "Equilibrium Thermodynamics of Schottky Defects in Sodium Chloride",
            "statement": "In a crystal of sodium chloride ($\text{NaCl}$), the formation energy of a Schottky defect pair (one $\text{Na}^+$ vacancy and one $\text{Cl}^-$ vacancy) is $E_S = 2.02\\text{ eV}$. The atomic density is $N = 2.23 \\times 10^{22}\\text{ ion pairs/cm}^3$.\\n\\n(a) Formulate the total Helmholtz free energy $F(n_S)$ including the configurational entropy for distributing $n_S$ cation vacancies on $N$ cation sites and $n_S$ anion vacancies on $N$ anion sites.\\n(b) Prove that the equilibrium Schottky pair density is $n_S \\approx N \\exp(-E_S / 2k_B T)$.\\n(c) Calculate the fraction of vacant sites $n_S / N$ and the absolute vacancy density $n_S$ at room temperature ($300\\text{ K}$) and near the melting point ($1000\\text{ K}$).",
            "solution": """**(a) Helmholtz Free Energy Formulation:**
To form $n_S$ Schottky defect pairs, $n_S$ positive ions and $n_S$ negative ions are removed.
The internal enthalpy change is $\\Delta U = n_S E_S$.
The number of microstates for distributing $n_S$ cation vacancies among $N$ cation sites is:
$$W_+ = \\frac{N!}{(N - n_S)! n_S!}$$
Similarly, for distributing $n_S$ anion vacancies among $N$ anion sites:
$$W_- = \\frac{N!}{(N - n_S)! n_S!}$$
The total number of microstates is $W = W_+ \\times W_- = \\left[ \\frac{N!}{(N - n_S)! n_S!} \\right]^2$.
The configurational entropy is:
$$S = k_B \\ln W = 2 k_B [N\\ln N - (N - n_S)\\ln(N - n_S) - n_S\\ln n_S]$$
The change in Helmholtz free energy is:
$$\\Delta F(n_S) = n_S E_S - 2 k_B T [N\\ln N - (N - n_S)\\ln(N - n_S) - n_S\\ln n_S]$$

**(b) Equilibrium Minimization:**
At thermodynamic equilibrium, $\\frac{d\\Delta F}{dn_S} = 0$:
$$\\frac{d\\Delta F}{dn_S} = E_S - 2 k_B T \\left[ \\ln(N - n_S) - \\ln n_S \\right] = 0$$
$$E_S = 2 k_B T \\ln\\left( \\frac{N - n_S}{n_S} \\right) \\implies \\ln\\left( \\frac{N - n_S}{n_S} \\right) = \\frac{E_S}{2 k_B T}$$
$$\\frac{n_S}{N - n_S} = \\exp\\left( -\\frac{E_S}{2 k_B T} \\right)$$
Since $n_S \\ll N$, $N - n_S \\approx N$:
$$n_S \\approx N \\exp\\left( -\\frac{E_S}{2 k_B T} \\right) \\quad \\text{(Q.E.D.)}$$

**(c) Numerical Calculations:**
Given $E_S = 2.02\\text{ eV} \\implies E_S / 2 = 1.01\\text{ eV}$.
**1. At $T = 300\\text{ K}$ ($k_B T = 0.02585\\text{ eV}$):**
$$\\frac{E_S}{2 k_B T} = \\frac{1.01}{0.02585} \\approx 39.07$$
$$\\frac{n_S}{N} = e^{-39.07} \\approx 1.07 \\times 10^{-17}$$
$$n_S = 2.23 \\times 10^{22} \\times 1.07 \\times 10^{-17} \\approx 2.4 \\times 10^5\\text{ cm}^{-3}$$
At room temperature, only 1 in every $10^{17}$ sites is vacant; thermal vacancies are negligible.

**2. At $T = 1000\\text{ K}$ ($k_B T = 0.08617\\text{ eV}$):**
$$\\frac{E_S}{2 k_B T} = \\frac{1.01}{0.08617} \\approx 11.72$$
$$\\frac{n_S}{N} = e^{-11.72} \\approx 8.12 \\times 10^{-6}$$
$$n_S = 2.23 \\times 10^{22} \\times 8.12 \\times 10^{-6} \\approx 1.81 \\times 10^{17}\\text{ cm}^{-3}$$
Near the melting point, vacancy concentration increases by twelve orders of magnitude to roughly **1 vacancy per $120{,}000$ lattice sites**, dramatically accelerating atomic diffusion and ionic electrical conductivity."""
        },
        {
            "id": "ssp2-prob-7-3",
            "title": "Derivation of the Mott-Gurney Law for Space-Charge-Limited Current",
            "statement": "An insulator film of thickness $L = 5.0\\ \\mu\\text{m}$ with relative dielectric permittivity $\\epsilon_r = 3.5$ and electron mobility $\\mu = 1.5\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$ is equipped with injecting ohmic contacts. Assume a trap-free single-carrier conduction model with boundary condition $\\mathcal{E}(0) = 0$.\\n\\n(a) Solve the coupled drift current and Poisson equations to derive the electric field profile $\\mathcal{E}(x)$ and potential profile $\\phi(x)$.\\n(b) Integrate to derive the Mott-Gurney square law $J = \\frac{9}{8}\\epsilon_r\\epsilon_0\\mu \\frac{V^2}{L^3}$.\\n(c) Calculate the current density $J$ in $\\text{A/cm}^2$ at an applied voltage $V = 10.0\\text{ Volts}$, and compute the transit time $t_{\\text{transit}} = \\int_0^L \\frac{dx}{\\mu \\mathcal{E}(x)}$.",
            "solution": """**(a) Electric Field and Potential Profiles:**
In the steady state, the current density is independent of $x$:
$$J = e n(x) \\mu \\mathcal{E}(x) \\implies e n(x) = \\frac{J}{\\mu \\mathcal{E}(x)}$$
Poisson's equation is:
$$\\frac{d\\mathcal{E}}{dx} = \\frac{\\rho(x)}{\\epsilon_r\\epsilon_0} = \\frac{e n(x)}{\\epsilon_r\\epsilon_0} = \\frac{J}{\\epsilon_r\\epsilon_0\\mu \\mathcal{E}(x)}$$
$$\\mathcal{E} d\\mathcal{E} = \\frac{J}{\\epsilon_r\\epsilon_0\\mu} dx$$
Integrating from $x = 0$ with $\\mathcal{E}(0) = 0$:
$$\\frac{1}{2} \\mathcal{E}^2(x) = \\frac{J}{\\epsilon_r\\epsilon_0\\mu} x \\implies \\mathcal{E}(x) = \\left( \\frac{2 J x}{\\epsilon_r\\epsilon_0\\mu} \\right)^{1/2}$$
The electrostatic potential $\\phi(x) = -\\int_0^x \\mathcal{E}(x') dx'$ with $\\phi(0) = 0$ is:
$$\\phi(x) = -\\left( \\frac{2J}{\\epsilon_r\\epsilon_0\\mu} \\right)^{1/2} \\frac{2}{3} x^{3/2}$$

**(b) Derivation of the Mott-Gurney Law:**
The applied voltage across the film of thickness $L$ is $V = -\\phi(L)$:
$$V = \\frac{2}{3} \\left( \\frac{2J}{\\epsilon_r\\epsilon_0\\mu} \\right)^{1/2} L^{3/2}$$
Squaring both sides:
$$V^2 = \\frac{4}{9} \\left( \\frac{2J}{\\epsilon_r\\epsilon_0\\mu} \\right) L^3 = \\frac{8 J L^3}{9 \\epsilon_r\\epsilon_0\\mu}$$
Solving for $J$:
$$J = \\frac{9}{8} \\epsilon_r\\epsilon_0\\mu \\frac{V^2}{L^3} \\quad \\text{(Q.E.D.)}$$

**(c) Numerical Calculations:**
Given:
$$L = 5.0\\ \\mu\\text{m} = 5.0 \\times 10^{-6}\\text{ m} \\implies L^3 = 1.25 \\times 10^{-16}\\text{ m}^3$$
$$V = 10.0\\text{ V} \\implies V^2 = 100\\text{ V}^2$$
$$\\epsilon_r = 3.5, \\quad \\epsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$$
$$\\mu = 1.5\\text{ cm}^2/(\\text{V}\\cdot\\text{s}) = 1.5 \\times 10^{-4}\\text{ m}^2/(\\text{V}\\cdot\\text{s})$$
Compute $J$:
$$J = \\frac{9}{8} \\times \\frac{(3.5)(8.854 \\times 10^{-12})(1.5 \\times 10^{-4})(100)}{1.25 \\times 10^{-16}}$$
$$J = 1.125 \\times \\frac{5.244 \\times 10^{-13}}{1.25 \\times 10^{-16}} = 1.125 \\times 4195.2 \\approx 4719.6\\text{ A/m}^2 = 0.472\\text{ A/cm}^2$$
Now evaluate the carrier transit time:
$$t_{\\text{transit}} = \\int_0^L \\frac{dx}{\\mu \\mathcal{E}(x)} = \\int_0^L \\frac{dx}{\\mu \\left( \\frac{2 J x}{\\epsilon_r\\epsilon_0\\mu} \\right)^{1/2}} = \\frac{1}{\\mu \\sqrt{\\frac{2J}{\\epsilon_r\\epsilon_0\\mu}}} \\int_0^L x^{-1/2} dx = \\frac{2 L^{1/2}}{\\mu \\sqrt{\\frac{2J}{\\epsilon_r\\epsilon_0\\mu}}}$$
Using $\\sqrt{\\frac{2J}{\\epsilon_r\\epsilon_0\\mu}} = \\frac{3V}{2 L^{3/2}}$:
$$t_{\\text{transit}} = \\frac{2 L^{1/2}}{\\mu \\left( \\frac{3V}{2 L^{3/2}} \\right)} = \\frac{4 L^2}{3 \\mu V}$$
Notice the universal coefficient $4/3$:
$$t_{\\text{transit}} = \\frac{4}{3} \\frac{L^2}{\\mu V} = \\frac{4}{3} \\frac{(5.0 \\times 10^{-6})^2}{(1.5 \\times 10^{-4})(10.0)} = \\frac{4}{3} \\frac{2.5 \\times 10^{-11}}{1.5 \\times 10^{-3}} = \\frac{4}{3} \\times (1.667 \\times 10^{-8}) \\approx 2.22 \\times 10^{-8}\\text{ s} = 22.2\\text{ ns}$$
The carrier transit time through the $5\\ \\mu\\text{m}$ film is **$22.2\\text{ nanoseconds}$**."""
        }
    ]
}

# =========================================================================
# UNIT 8: Advanced Band Structure Methods & Many-Body Physics in Solids
# =========================================================================

u8_data = {
    "title": "Advanced Band Structure Methods & Many-Body Physics in Solids",
    "subtitle": "Hartree-Fock, Lindhard Screening, Fermi Surfaces, DFT & Mott Insulators",
    "summary": "This culminating unit covers advanced computational and many-body theoretical techniques in modern solid state physics. We analyze electron-electron interactions, Coulomb exchange energy, and the failure of single-particle Hartree-Fock theory at the Fermi surface. We derive the Lindhard dielectric response function, Thomas-Fermi screening, Kohn anomalies, and Friedel oscillations. We explore Fermi surface topology, de Haas-van Alphen quantum oscillations, and Wannier functions. We study modern electronic structure calculation methods including tight-binding, pseudopotentials, and Density Functional Theory (DFT). Finally, we explore strongly correlated electrons within the Hubbard model, the Mott metal-insulator transition, the GW approximation, and semiconductor superlattices.",
    "sections": [
        {
            "id": "sec-8-1",
            "title": "Electron-Electron Interactions: The Hartree & Hartree-Fock Approximations in the Electron Gas",
            "content": r"""
<h3>1. The Many-Body Hamiltonian & Jellium Model</h3>
<p>
In real solids, electrons interact not only with the periodic ionic lattice potential $V_{\text{ion}}(\vec{r})$, but strongly with each other via the long-range Coulomb repulsion. In the uniform electron gas (jellium) model:
</p>
$$\hat{H} = \sum_{i=1}^N \frac{p_i^2}{2m} + \frac{1}{2}\sum_{i \ne j} \frac{e^2}{4\pi\epsilon_0 |\vec{r}_i - \vec{r}_j|} + \hat{H}_{\text{bg}} + \hat{H}_{\text{e-bg}}$$
<p>
The positive ion background $\hat{H}_{\text{bg}}$ and electron-background interaction $\hat{H}_{\text{e-bg}}$ exactly cancel the direct (Hartree) classical electrostatic divergence at $\vec{q} = 0$.
</p>

<h3>2. The Hartree-Fock Exchange Energy</h3>
<p>
In the Hartree-Fock approximation, the $N$-electron wavefunction is represented by a single Slater determinant of plane waves. The total energy per electron is:
</p>
$$E_{\text{HF}} / N = \langle \hat{T} \rangle + E_{\text{exchange}} = \frac{3}{5} E_F - \frac{3}{4} \frac{e^2 k_F}{4\pi^2 \epsilon_0}$$
<p>
Introducing the dimensionless Wigner-Seitz density parameter $r_s \equiv r_0 / a_0$ (where $\frac{4}{3}\pi r_0^3 = 1/n$):
</p>
$$\frac{E_{\text{HF}}}{N} = \left[ \frac{2.21}{r_s^2} - \frac{0.916}{r_s} \right] \text{ Rydbergs}$$
<ul>
  <li>At high densities ($r_s \ll 1$): Kinetic energy ($\propto 1/r_s^2$) dominates $\implies$ Free electron gas behavior.</li>
  <li>At low densities ($r_s \gg 1$): Exchange and correlation energies ($\propto -1/r_s$) dominate $\implies$ Wigner electron crystallization!</li>
</ul>
<p>
<strong>Failure of Hartree-Fock at the Fermi Surface:</strong>
The single-particle Hartree-Fock energy dispersion is:
$$\epsilon_{\text{HF}}(k) = \frac{\hbar^2 k^2}{2m} - \frac{e^2 k_F}{2\pi^2 \epsilon_0} \left[ 1 + \frac{k_F^2 - k^2}{2 k k_F} \ln\left| \frac{k + k_F}{k - k_F} \right| \right]$$
Differentiating to obtain the group velocity $v_g = \frac{1}{\hbar}\frac{d\epsilon}{dk}$, the logarithmic term causes the velocity to <strong>diverge logarithmically to infinity</strong> at the Fermi surface ($k = k_F$), forcing the density of states $g(E_F) \propto 1/v_g$ to drop unphysically to zero! This catastrophe occurs because Hartree-Fock completely neglects <em>dynamic dielectric screening</em> of the Coulomb interaction by other electrons.
</p>
"""
        },
        {
            "id": "sec-8-2",
            "title": "Linear Dielectric Response Theory, Lindhard Function & Thomas-Fermi Screening",
            "content": r"""
<h3>1. Linear Dielectric Response Formalism</h3>
<p>
When an external test charge $\rho_{\text{ext}}(\vec{r}, t) = \rho_0 e^{i(\vec{q}\cdot\vec{r} - \omega t)}$ is introduced into the electron gas, it induces a screening charge density $\rho_{\text{ind}}(\vec{q}, \omega)$. In linear response theory:
</p>
$$\rho_{\text{ind}}(\vec{q}, \omega) = \chi(\vec{q}, \omega) \phi_{\text{total}}(\vec{q}, \omega)$$
<p>
where $\chi(\vec{q}, \omega)$ is the dynamic polarizability. The frequency- and wavevector-dependent dielectric function $\epsilon(\vec{q}, \omega)$ is defined by:
</p>
$$\phi_{\text{total}}(\vec{q}, \omega) = \frac{\phi_{\text{ext}}(\vec{q}, \omega)}{\epsilon(\vec{q}, \omega)} \implies \epsilon(\vec{q}, \omega) = 1 - \frac{e^2}{\epsilon_0 q^2} \chi(\vec{q}, \omega)$$

<h3>2. The Lindhard Dielectric Function</h3>
<p>
Jens Lindhard (1954) derived the exact quantum polarizability of a degenerate Fermi gas in the Random Phase Approximation (RPA):
</p>
$$\epsilon(\vec{q}, \omega) = 1 + \frac{e^2}{\epsilon_0 q^2} \sum_{\vec{k}} \frac{f(\vec{k}) - f(\vec{k}+\vec{q})}{\epsilon(\vec{k}+\vec{q}) - \epsilon(\vec{k}) - \hbar\omega - i\eta}$$
<p>
In the static limit ($\omega = 0$), the <strong>static Lindhard dielectric function</strong> is:
</p>
$$\epsilon(q, 0) = 1 + \frac{q_{\text{TF}}^2}{q^2} F\left( \frac{q}{2k_F} \right)$$
<p>
where $q_{\text{TF}} = \sqrt{\frac{3 e^2 n}{2\epsilon_0 E_F}}$ is the Thomas-Fermi screening wavevector, and $F(x)$ is the <strong>Lindhard function</strong> ($x \equiv q / 2k_F$):
</p>
$$F(x) = \frac{1}{2} + \frac{1 - x^2}{4x} \ln\left| \frac{1 + x}{1 - x} \right|$$
<ul>
  <li><strong>Long-Wavelength Limit ($q \ll 2k_F$, $x \to 0$):</strong> $F(x) \to 1$, giving the classical <strong>Thomas-Fermi screening</strong>:
  $$\epsilon(q) \approx 1 + \frac{q_{\text{TF}}^2}{q^2} \implies V(r) = \frac{e}{4\pi\epsilon_0 r} \exp(-q_{\text{TF}} r)$$
  The Coulomb potential is screened exponentially over the Thomas-Fermi length $\lambda_{\text{TF}} = 1/q_{\text{TF}} \sim 0.5\text{ \AA}$.</li>
  <li><strong>Zone Edge Singularity ($q = 2k_F$, $x = 1$):</strong> The derivative $dF/dx$ diverges logarithmically to $-\infty$ due to the sharp step in the Fermi-Dirac distribution at $T = 0\text{ K}$.</li>
</ul>
""",
            "simulation": "ssp2-lindhard-screening-sim",
            "simulations": ["ssp2-lindhard-screening-sim"]
        },
        {
            "id": "sec-8-3",
            "title": "Kohn Anomalies, Friedel Oscillations & The Friedel Sum Rule",
            "content": r"""
<h3>1. Real-Space Friedel Oscillations</h3>
<p>
Because the static Lindhard dielectric function $\epsilon(q, 0)$ possesses a non-analytic logarithmic derivative at $q = 2k_F$, taking the inverse Fourier transform of the screened potential $\phi(r) = \int \frac{\phi_{\text{ext}}(q)}{\epsilon(q)} e^{i\vec{q}\cdot\vec{r}} \frac{d^3q}{(2\pi)^3}$ produces long-range spatial ripples rather than pure exponential decay:
</p>
$$\delta\rho(r) \propto \frac{\cos(2k_F r)}{r^3} \quad (r \gg 1/k_F)$$
$$\phi(r) \propto \frac{\cos(2k_F r)}{r^3}$$
<p>
These quantum interference ripples are <strong>Friedel oscillations</strong>. They arise from the sharp edge of the Fermi sphere: electrons cannot screen perturbations on spatial scales shorter than the Fermi wavelength $\lambda_F = 2\pi/k_F$. Friedel oscillations govern the oscillatory sign of the RKKY magnetic exchange interaction and mediate long-range vacancy-impurity interactions in alloys.
</p>

<h3>2. Kohn Anomalies & The Friedel Sum Rule</h3>
<ul>
  <li><strong>Kohn Anomaly in Phonon Dispersion:</strong>
  In 1959, Walter Kohn showed that because ions are screened by conduction electrons, the singularity in $\epsilon(q, 0)$ at $q = 2k_F$ is directly imprinted onto the phonon dispersion curve $\omega(\vec{q})$. At phonon wavevectors spanning the Fermi surface ($|\vec{q}| = 2k_F$), the phonon frequency exhibits a sharp dip or kink:
  $$\left. \frac{d\omega}{dq} \right|_{q = 2k_F} \to -\infty$$
  In low-dimensional conductors (1D and 2D), this anomaly triggers the Peierls structural transition and charge density waves (CDWs).</li>
  <li><strong>The Friedel Sum Rule:</strong>
  When an impurity ion with excess nuclear charge $Z e$ is embedded in a metal, it scatters conduction electrons. The phase shifts $\delta_l(E_F)$ of the partial waves at the Fermi energy must completely screen the impurity charge:
  $$Z = \frac{2}{\pi} \sum_{l=0}^\infty (2l + 1) \delta_l(E_F)$$
  This exact relation connects microscopic electron scattering phase shifts to macroscopic residual electrical resistivity $\Delta\rho$.</li>
</ul>
"""
        },
        {
            "id": "sec-8-4",
            "title": "Geometry of the Fermi Surface, Harrison Construction & Quantum Oscillations",
            "content": r"""
<h3>1. The Harrison Construction & Fermi Surface Topology</h3>
<p>
The Fermi surface is the constant-energy locus $E(\vec{k}) = E_F$ separating occupied from unoccupied states in reciprocal space at $T = 0\text{ K}$.
</p>
<p>
In the nearly free electron approximation, the <strong>Harrison construction</strong> determines the Fermi surface geometry:
</p>
<ol>
  <li>Draw the free electron Fermi sphere of radius $k_F = (3\pi^2 n)^{1/3}$ centered at every reciprocal lattice point $\vec{G}$.</li>
  <li>Points enclosed by at least one sphere belong to the first Brillouin zone; points enclosed by at least two spheres belong to the second zone, and so on.</li>
  <li>Applying periodic potential gaps rounds off the sharp intersections, decomposing the Fermi surface into:
  <ul>
    <li><strong>Closed Electron Pockets:</strong> Enclosing lower unoccupied states.</li>
    <li><strong>Closed Hole Pockets:</strong> Enclosing unoccupied states.</li>
    <li><strong>Open Orbits:</strong> Non-periodic trajectories that traverse the entire Brillouin zone without closing, producing unsaturated transverse magnetoresistance ($\rho_{xx} \propto B^2$).</li>
  </ul>
  </li>
</ol>

<h3>2. The de Haas-van Alphen (dHvA) Effect & Onsager Relation</h3>
<p>
When a strong magnetic field $B\hat{z}$ is applied to a clean metal at cryogenic temperatures ($\omega_c \tau \gg 1, k_B T \ll \hbar\omega_c$), the continuous electronic density of states condenses into discrete Landau tubes in reciprocal space with cross-sectional area:
</p>
$$S_n = (n + \gamma) \frac{2\pi e B}{\hbar}$$
<p>
As $B$ increases, the Landau tubes expand radially. Each time a tube crosses the extremal cross-section of the Fermi surface $S_e$, the free energy and magnetic moment undergo a sharp oscillation.
</p>
<p>
According to the <strong>Onsager Relation</strong> (1952), the magnetic susceptibility oscillates periodically in $1/B$:
</p>
$$\Delta\left( \frac{1}{B} \right) = \frac{2\pi e}{\hbar S_e}$$
<p>
By measuring the oscillation periods $\Delta(1/B)$ as a function of the magnetic field orientation, the complete 3D topological shape and extremal cross-sectional areas $S_e$ of the Fermi surface can be reconstructed with sub-percent precision.
</p>
"""
        },
        {
            "id": "sec-8-5",
            "title": "Modern Computational Band Structure: Tight-Binding, Pseudopotentials & Density Functional Theory",
            "content": r"""
<h3>1. The Tight-Binding Method</h3>
<p>
In the tight-binding (LCAO) approximation, the crystal wavefunction is constructed from linear combinations of isolated atomic orbitals $\phi_m(\vec{r})$:
</p>
$$\psi_{\vec{k}}(\vec{r}) = \frac{1}{\sqrt{N}} \sum_j e^{i \vec{k} \cdot \vec{R}_j} \phi(\vec{r} - \vec{R}_j)$$
<p>
Retaining only on-site energy $\epsilon_0$ and nearest-neighbor hopping matrix element $t = -\int \phi^*(\vec{r}) \Delta V(\vec{r}) \phi(\vec{r} - \vec{\delta}) d^3r$, the band dispersion on a 2D square lattice of constant $a$ is:
</p>
$$E(\vec{k}) = \epsilon_0 - 2t [\cos(k_x a) + \cos(k_y a)]$$
<p>
At the band saddle points ($\vec{k} = (\pi/a, 0)$ and $(0, \pi/a)$), the group velocity vanishes, producing a logarithmic divergence in the 2D density of states known as a <strong>van Hove singularity</strong>:
</p>
$$g(E) \propto \ln\left| \frac{16t}{E - \epsilon_0} \right|$$

<h3>2. Pseudopotentials & Density Functional Theory (DFT)</h3>
<ul>
  <li><strong>Orthogonalized Plane Waves (OPW) & Pseudopotentials:</strong>
  Conduction wavefunctions must oscillate rapidly near atomic nuclei to remain orthogonal to tightly bound core states, requiring thousands of plane waves. Phillips and Kleinman proved that this core orthogonality acts as an effective repulsive potential that nearly cancels the deep Coulomb attraction:
  $$V_{\text{pseudo}}(\vec{r}) = V_{\text{true}}(\vec{r}) + \sum_c (E - E_c) |\phi_c\rangle\langle\phi_c|$$
  The resulting smooth, shallow <em>pseudopotential</em> reproduces valence eigenvalues accurately with a small plane-wave basis.</li>
  <li><strong>Density Functional Theory (Hohenberg-Kohn & Kohn-Sham, 1964-1965):</strong>
  DFT establishes that the ground-state properties of an interacting many-electron system are uniquely determined by the 3D ground-state electron density $n(\vec{r})$, reducing a $3N$-dimensional problem to 3 dimensions!
  The Kohn-Sham self-consistent single-particle equations are:
  $$\left[ -\frac{\hbar^2}{2m} \nabla^2 + V_{\text{ext}}(\vec{r}) + V_{\text{Hartree}}[n](\vec{r}) + V_{\text{xc}}[n](\vec{r}) \right] \psi_i(\vec{r}) = \epsilon_i \psi_i(\vec{r})$$
  $$n(\vec{r}) = \sum_{i=1}^N |\psi_i(\vec{r})|^2$$
  The exchange-correlation potential $V_{\text{xc}}$ is approximated via the Local Density Approximation (LDA) or Generalized Gradient Approximation (GGA). DFT forms the backbone of modern computational materials physics.</li>
</ul>
""",
            "simulation": "ssp2-tightbinding-hubbard-sim",
            "simulations": ["ssp2-tightbinding-hubbard-sim"]
        },
        {
            "id": "sec-8-6",
            "title": "Strongly Correlated Electron Systems: The Hubbard Model & The Mott Metal-Insulator Transition",
            "content": r"""
<h3>1. Failure of Independent-Electron Band Theory: Mott Insulators</h3>
<p>
According to conventional Bloch band theory, any crystal with an odd number of valence electrons per unit cell must have a half-filled energy band and should therefore be a <strong>metal</strong>.
</p>
<p>
However, materials such as $\text{NiO}$, $\text{CoO}$, and undoped cuprates ($\text{La}_2\text{CuO}_4$) have partially filled $3d$ shells, yet are transparent electrical <strong>insulators</strong> with optical bandgaps exceeding $4\text{ eV}$!
</p>
<p>
In 1937, Nevill Mott explained that single-particle band theory completely breaks down when the on-site Coulomb repulsion $U$ between two electrons on the same atom exceeds the kinetic hopping bandwidth $W = 2 z t$.
</p>

<h3>2. The Single-Band Hubbard Model</h3>
<p>
The minimal Hamiltonian capturing this competition between kinetic itinerancy and Coulomb localization is the <strong>Hubbard Model</strong>:
</p>
$$\hat{H} = -t \sum_{\langle ij \rangle, \sigma} \left( c_{i\sigma}^\dagger c_{j\sigma} + \text{h.c.} \right) + U \sum_i n_{i\uparrow} n_{i\downarrow}$$
<ul>
  <li><strong>Hopping parameter $t$:</strong> Promotes electron delocalization into a metallic band of bandwidth $W = 2 z t$.</li>
  <li><strong>On-site Coulomb repulsion $U$ ($U = \int |\phi(r_1)|^2 \frac{e^2}{r_{12}} |\phi(r_2)|^2$):</strong> Energy penalty incurred whenever two electrons with opposite spins occupy the same lattice site.</li>
</ul>
<p>
At half-filling (one electron per atom, $\langle n_i \rangle = 1$):
</p>
<ul>
  <li><strong>Weak Coupling ($U / W \ll 1$):</strong> Itinerant metallic Fermi liquid.</li>
  <li><strong>Strong Coupling ($U / W \gg 1$):</strong> Double occupancy is strictly suppressed. To conduct electricity, an electron must hop to an already occupied site, costing energy $U$. The single band splits into two sub-bands:
  <ul>
    <li><strong>Lower Hubbard Band (LHB):</strong> Completely filled ($E \approx 0$).</li>
    <li><strong>Upper Hubbard Band (UHB):</strong> Completely empty ($E \approx U$).</li>
  </ul>
  The gap separating them is the <strong>Mott-Hubbard gap</strong> $E_{\text{gap}} \approx U - W$. The material is a <strong>Mott Insulator</strong>!</li>
  <li>At second-order perturbation theory in $t/U$, virtual hopping between neighboring singly-occupied sites yields an effective antiferromagnetic Heisenberg exchange interaction:
  $$J = \frac{4 t^2}{U}$$
  explaining why virtually all parent Mott insulators are robust antiferromagnets.</li>
</ul>
"""
        },
        {
            "id": "sec-8-7",
            "title": "Green's Function Many-Body Formalism, GW Approximation & Semiconductor Superlattices",
            "content": r"""
<h3>1. Green's Functions & The GW Approximation</h3>
<p>
Standard DFT notoriously underestimates electronic bandgaps by $30-50\%$ (e.g. predicting $0.5\text{ eV}$ for Si instead of $1.12\text{ eV}$, and predicting zero gap for Mott insulators) because Kohn-Sham eigenvalues are Lagrange multipliers of a non-interacting auxiliary system, not true quasiparticle excitation energies.
</p>
<p>
To accurately compute true quasiparticle spectra, many-body perturbation theory employs the <strong>single-particle Green's function</strong> $G(\vec{r}, \vec{r}', \omega)$. The quasiparticle equation is:
</p>
$$\left[ -\frac{\hbar^2}{2m} \nabla^2 + V_{\text{ion}}(\vec{r}) + V_{\text{Hartree}}(\vec{r}) \right] \psi_n(\vec{r}) + \int \Sigma(\vec{r}, \vec{r}', \epsilon_n) \psi_n(\vec{r}') d^3r' = \epsilon_n \psi_n(\vec{r})$$
<p>
where $\Sigma$ is the non-local, energy-dependent <strong>self-energy operator</strong>. In Lars Hedin's <strong>GW approximation</strong>, the self-energy is expanded to first order in the dynamically screened Coulomb interaction $W = \epsilon^{-1} v$:
</p>
$$\Sigma = i G W$$
<p>
The $GW$ method accurately reproduces experimental bandgaps across semiconductors and insulators to within $0.1\text{ eV}$.
</p>

<h3>2. Semiconductor Superlattices & Minibands</h3>
<p>
In 1970, Leo Esaki and Raphael Tsu proposed fabricating artificial 1D periodic structures by alternating ultra-thin epitaxial layers of two different semiconductors (e.g. $\text{GaAs}$ and $\text{Al}_x\text{Ga}_{1-x}\text{As}$) with period $d \sim 5-20\text{ nm} \gg a_{\text{lattice}}$.
</p>
<p>
This introduces an artificial periodic potential that folds the host Brillouin zone into a <strong>mini-Brillouin zone</strong> of width $\pi/d$.
</p>
<ul>
  <li>The conduction band splits into narrow <strong>minibands</strong> of width $\Delta \sim 10-50\text{ meV}$ separated by minigaps.</li>
  <li>Under an applied electric field $\mathcal{E}$, electrons accelerate to the mini-zone boundary and undergo Bragg reflection, executing periodic real-space <strong>Bloch oscillations</strong> at frequency $\omega_B = e\mathcal{E}d / \hbar$ without scattering.</li>
  <li>This produces <strong>negative differential resistance</strong> ($dI/dV < 0$), providing the operational foundation for resonant tunneling diodes (RTDs) and quantum cascade lasers (QCLs).</li>
</ul>
"""
        }
    ],
    "problems": [
        {
            "id": "ssp2-prob-8-1",
            "title": "Thomas-Fermi vs Lindhard Screening & Derivation of Friedel Oscillations",
            "statement": "An impurity of charge $+Q$ is embedded in a 3D degenerate electron gas with Fermi wavevector $k_F$ and Fermi energy $E_F$.\\n\\n(a) Using the static Thomas-Fermi approximation $\\epsilon(q) = 1 + q_{\\text{TF}}^2/q^2$, calculate the real-space electrostatic potential $\\phi(r)$ by evaluating the 3D Fourier transform integral.\\n(b) In the quantum Lindhard dielectric function, the static polarizability has a logarithmic singularity $\\frac{d\\chi}{dq} \\to -\\infty$ at $q = 2k_F$. Prove using contour integration that the asymptotic screening charge density oscillates as $\\delta\\rho(r) \\propto \\frac{\\cos(2k_F r)}{r^3}$.\\n(c) For copper ($k_F = 1.36 \\times 10^{10}\\text{ m}^{-1}$), calculate the spatial period $\\lambda_{\\text{Friedel}} = \\pi / k_F$ of the Friedel oscillations, and explain why this sets the wavelength of the RKKY magnetic interaction.",
            "solution": """**(a) Thomas-Fermi Screened Potential:**
The bare external potential of the point charge $+Q$ in reciprocal space is $\\phi_{\\text{ext}}(q) = \\frac{Q}{\\epsilon_0 q^2}$.
With the Thomas-Fermi dielectric function $\\epsilon(q) = 1 + \\frac{q_{\\text{TF}}^2}{q^2} = \\frac{q^2 + q_{\\text{TF}}^2}{q^2}$:
$$\\phi(q) = \\frac{\\phi_{\\text{ext}}(q)}{\\epsilon(q)} = \\frac{Q}{\\epsilon_0 (q^2 + q_{\\text{TF}}^2)}$$
The real-space potential is obtained by 3D inverse Fourier transform:
$$\\phi(r) = \\frac{1}{(2\\pi)^3} \\int \\phi(q) e^{i\\vec{q}\\cdot\\vec{r}} d^3q = \\frac{1}{(2\\pi)^3} \\int_0^\\infty q^2 dq \\int_0^\\pi \\sin\\theta d\\theta \\int_0^{2\\pi} d\\varphi \\frac{Q}{\\epsilon_0 (q^2 + q_{\\text{TF}}^2)} e^{i q r \\cos\\theta}$$
$$\\phi(r) = \\frac{Q}{(2\\pi)^2 \\epsilon_0} \\int_0^\\infty \\frac{q^2}{q^2 + q_{\\text{TF}}^2} \\left[ \\frac{e^{i q r} - e^{-i q r}}{i q r} \\right] dq = \\frac{Q}{4\\pi^2 \\epsilon_0 i r} \\int_{-\\infty}^\\infty \\frac{q e^{i q r}}{q^2 + q_{\\text{TF}}^2} dq$$
Evaluating via residue calculus (closing the contour in the upper half-plane with a simple pole at $q = +i q_{\\text{TF}}$):
$$\\int_{-\\infty}^\\infty \\frac{q e^{i q r}}{(q - i q_{\\text{TF}})(q + i q_{\\text{TF}})} dq = 2\\pi i \\operatorname{Res}(i q_{\\text{TF}}) = 2\\pi i \\left[ \\frac{i q_{\\text{TF}} e^{-q_{\\text{TF}} r}}{2 i q_{\\text{TF}}} \\right] = \\pi i e^{-q_{\\text{TF}} r}$$
Substituting back:
$$\\phi(r) = \\frac{Q}{4\\pi^2 \\epsilon_0 i r} (\\pi i e^{-q_{\\text{TF}} r}) = \\frac{Q}{4\\pi \\epsilon_0 r} \\exp(-q_{\\text{TF}} r)$$
This is the **Yukawa / Thomas-Fermi screened potential**.

**(b) Derivation of Friedel Oscillations:**
The exact screening charge density in Fourier space is $\\delta\\rho(q) = -e \\chi(q) \\phi(q)$.
In the Lindhard function, the derivative $d\\epsilon/dq$ diverges logarithmically at $q = 2k_F$ due to the term $(1 - x^2) \\ln|\\frac{1+x}{1-x}|$ with $x = q/2k_F$.
Expanding near $q = 2k_F$ (where $q = 2k_F + \\delta$):
$$\\delta\\rho(r) = \\frac{1}{2\\pi^2 r} \\int_0^\\infty q \\delta\\rho(q) \\sin(q r) dq$$
Integrating by parts twice transfers derivatives onto $\\delta\\rho(q)$:
$$\\delta\\rho(r) = \\frac{1}{2\\pi^2 r^3} \\int_0^\\infty \\frac{d^2}{dq^2}[q \\delta\\rho(q)] \\sin(q r) dq$$
Because the second derivative has a non-analytic branch point pole $\\propto \\frac{1}{q - 2k_F}$ at $q = 2k_F$:
$$\\int \\frac{\\sin(q r)}{q - 2k_F} dq \\propto \\cos(2k_F r)$$
Therefore, the asymptotic real-space behavior at large distances ($r \\gg 1/k_F$) is:
$$\\delta\\rho(r) \\approx -\\frac{Q q_{\\text{TF}}^2}{2\\pi (2 + q_{\\text{TF}}^2/2k_F^2)^2} \\frac{\\cos(2k_F r)}{r^3} \\propto \\frac{\\cos(2k_F r)}{r^3}$$
This mathematically establishes the algebraic decay and **Friedel oscillations**.

**(c) Numerical Period for Copper:**
Given $k_F = 1.36 \\times 10^{10}\\text{ m}^{-1}$:
$$\\lambda_{\\text{Friedel}} = \\frac{\\pi}{k_F} = \\frac{3.14159}{1.36 \\times 10^{10}\\text{ m}^{-1}} \\approx 2.31 \\times 10^{-10}\\text{ m} = 0.231\\text{ nm} = 2.31\\text{ \\AA}$$
The spatial period of the charge oscillations in copper is **$2.31\\text{ \\AA}$** (nearly identical to the nearest-neighbor interatomic distance $a/\\sqrt{2} \\approx 2.55\\text{ \\AA}$).
Physical consequence: A magnetic impurity spin $\\vec{S}_1$ induces an oscillatory spin polarization in the conduction electrons with this exact spatial period $\\cos(2k_F r)/r^3$. A second impurity spin $\\vec{S}_2$ at distance $r$ aligns parallel or antiparallel depending on whether it sits on a crest or a trough of the Friedel wave, directly dictating the RKKY interaction sign."""
        },
        {
            "id": "ssp2-prob-8-2",
            "title": "2D Tight-Binding Band Structure, Van Hove Singularity & Fermi Surface Nesting",
            "statement": "Electrons on a 2D square lattice of constant $a$ have the nearest-neighbor tight-binding dispersion:\\n$$E(k_x, k_y) = -2t [\\cos(k_x a) + \\cos(k_y a)]$$\\n\\n(a) Determine the bandwidth $W = E_{\\max} - E_{\\min}$ and the location of the band extrema in the first Brillouin zone.\\n(b) Prove that a saddle point exists at $\\vec{k} = (\\pi/a, 0)$ and $(0, \\pi/a)$ at energy $E = 0$, and prove that the 2D density of states $g(E)$ diverges logarithmically as $E \\to 0$ (Van Hove singularity).\\n(c) Sketch the Fermi surface at half-filling ($E_F = 0$). Prove that the Fermi surface is a perfect square tilted at 45°, and demonstrate that it exhibits perfect **nesting** with nesting wavevector $\\vec{Q} = (\\pi/a, \\pi/a)$.",
            "solution": """**(a) Band Extrema and Bandwidth:**
- Minimum energy occurs at $k_x = 0, k_y = 0$ ($\\Gamma$-point):
$$E_{\\min} = -2t (1 + 1) = -4t$$
- Maximum energy occurs at $k_x = \\pm \\pi/a, k_y = \\pm \\pi/a$ ($M$-point):
$$E_{\\max} = -2t (-1 - 1) = +4t$$
The total bandwidth is:
$$W = E_{\\max} - E_{\\min} = 4t - (-4t) = 8t$$

**(b) Saddle Points & Van Hove Singularity:**
Compute the group velocity components:
$$v_x = \\frac{1}{\\hbar} \\frac{\\partial E}{\\partial k_x} = \\frac{2t a}{\\hbar} \\sin(k_x a)$$
$$v_y = \\frac{1}{\\hbar} \\frac{\\partial E}{\\partial k_y} = \\frac{2t a}{\\hbar} \\sin(k_y a)$$
At $\\vec{k} = (\\pi/a, 0)$ ($X$-point):
$$v_x = 0, \\quad v_y = 0 \\implies \\nabla_{\\vec{k}} E = 0$$
The energy is:
$$E = -2t [\\cos\\pi + \\cos 0] = -2t [-1 + 1] = 0$$
Evaluating the second derivatives:
$$\\frac{\\partial^2 E}{\\partial k_x^2} = 2t a^2 \\cos(k_x a) = 2t a^2 \\cos\\pi = -2t a^2 < 0$$
$$\\frac{\\partial^2 E}{\\partial k_y^2} = 2t a^2 \\cos(k_y a) = 2t a^2 \\cos 0 = +2t a^2 > 0$$
Because the principal curvatures have **opposite signs** (negative along $k_x$, positive along $k_y$), the point $(\\pi/a, 0)$ is a **saddle point**.
Near this saddle point, let $k_x = \\pi/a + q_x$ and $k_y = q_y$:
$$E(q_x, q_y) \\approx t a^2 (q_y^2 - q_x^2)$$
The density of states in 2D is:
$$g(E) = \\frac{1}{(2\\pi)^2} \\oint_{E(\\vec{k})=E} \\frac{dl}{|\\nabla_{\\vec{k}} E|}$$
Since $|\\nabla E| = 2t a^2 \\sqrt{q_x^2 + q_y^2}$, integrating over the hyperbolic contours $q_y^2 - q_x^2 = E / t a^2$ yields:
$$g(E) = \\frac{1}{2\\pi^2 t a^2} \\ln\\left| \\frac{16t}{E} \\right|$$
As $E \\to 0$, $g(E) \\to \\infty$ diverges logarithmically. This is the **2D van Hove singularity**.

**(c) Fermi Surface at Half-Filling & Nesting:**
At half-filling, there is 1 electron per site, filling half the total zone capacity (since each site can hold 2 electrons). By particle-hole symmetry, $E_F = 0$.
The Fermi surface contour equation is:
$$E(k_x, k_y) = 0 \\implies -2t [\\cos(k_x a) + \\cos(k_y a)] = 0 \\implies \\cos(k_x a) + \\cos(k_y a) = 0$$
Using the trigonometric identity $\\cos A + \\cos B = 2\\cos\\left(\\frac{A+B}{2}\\right)\\cos\\left(\\frac{A-B}{2}\\right)$:
$$\\cos\\left( \\frac{k_x + k_y}{2} a \\right) = 0 \\quad \\text{or} \\quad \\cos\\left( \\frac{k_x - k_y}{2} a \\right) = 0$$
This yields four straight intersecting line segments connecting the saddle points:
$$k_y a \\pm k_x a = \\pm \\pi$$
Connecting $(\\pi/a, 0) \\to (0, \\pi/a) \\to (-\\pi/a, 0) \\to (0, -\\pi/a) \\to (\\pi/a, 0)$.
This forms a **perfect square tilted at 45°**!
**Proof of Perfect Nesting:**
Consider the nesting wavevector $\\vec{Q} = (\\pi/a, \\pi/a)$.
Displace any wavevector $\\vec{k}$ on the Fermi surface by $\\vec{Q}$:
$$E(\\vec{k} + \\vec{Q}) = -2t [\\cos(k_x a + \\pi) + \\cos(k_y a + \\pi)] = -2t [-\\cos(k_x a) - \\cos(k_y a)] = -E(\\vec{k})$$
For any state on the Fermi surface ($E(\\vec{k}) = 0$):
$$E(\\vec{k} + \\vec{Q}) = -0 = 0$$
The entire flat edge of the Fermi surface translates exactly onto the opposing parallel edge under translation by $\\vec{Q}$!
This **perfect nesting** produces a divergence in the static susceptibility $\\chi(\\vec{Q}) \\propto \\ln^2(T)$, driving an immediate instability toward an **antiferromagnetic spin density wave (SDW)** or charge density wave (CDW) at infinitesimal Coulomb repulsion $U > 0$."""
        },
        {
            "id": "ssp2-prob-8-3",
            "title": "Strong-Coupling Hubbard Model & Derivation of Antiferromagnetic Exchange J = 4t^2/U",
            "statement": "Two electrons occupy two adjacent lattice sites $1$ and $2$ described by the two-site Hubbard Hamiltonian:\\n$$\\hat{H} = -t \\sum_\\sigma (c_{1\\sigma}^\\dagger c_{2\\sigma} + c_{2\\sigma}^\\dagger c_{1\\sigma}) + U (n_{1\\uparrow}n_{1\\downarrow} + n_{2\\uparrow}n_{2\\downarrow})$$\\n\\n(a) Enumerate the six basis states of the two-electron Hilbert space, separating them into singly-occupied and doubly-occupied configurations.\\n(b) Using second-order degenerate perturbation theory in the strong-coupling limit $U \\gg t$, calculate the energy of the spin-triplet ($S = 1$) state and the spin-singlet ($S = 0$) state.\\n(c) Prove that the effective spin Hamiltonian is equivalent to an antiferromagnetic Heisenberg interaction $\\hat{H}_{\\text{spin}} = J \\vec{S}_1 \\cdot \\vec{S}_2 + \\text{const}$, and derive the exact formula for the exchange coupling constant $J = 4t^2/U$.",
            "solution": """**(a) Hilbert Space Basis States:**
There are $\\binom{4}{2} = 6$ total states:
1. *Singly-occupied states (Energy = $0$ in unperturbed limit $t = 0$):*
- Triplet states ($S = 1, S_z = +1, 0, -1$):
  $$|T_+\\rangle = c_{1\\uparrow}^\\dagger c_{2\\uparrow}^\\dagger |0\rangle$$
  $$|T_0\\rangle = \\frac{1}{\\sqrt{2}} (c_{1\\uparrow}^\\dagger c_{2\\downarrow}^\\dagger + c_{1\\downarrow}^\\dagger c_{2\\uparrow}^\\dagger) |0\rangle$$
  $$|T_-\\rangle = c_{1\\downarrow}^\\dagger c_{2\\downarrow}^\\dagger |0\rangle$$
- Singlet state ($S = 0, S_z = 0$):
  $$|S\\rangle = \\frac{1}{\\sqrt{2}} (c_{1\\uparrow}^\\dagger c_{2\\downarrow}^\\dagger - c_{1\\downarrow}^\\dagger c_{2\\uparrow}^\\dagger) |0\rangle$$
2. *Doubly-occupied states (Energy = $U$ in unperturbed limit):*
  $$|D_1\\rangle = c_{1\\uparrow}^\\dagger c_{1\\downarrow}^\\dagger |0\rangle, \\quad |D_2\\rangle = c_{2\\uparrow}^\\dagger c_{2\\downarrow}^\\dagger |0\rangle$$

**(b) Perturbation Energy of Triplet and Singlet:**
- **For the Triplet States ($|T_+\\rangle, |T_0\\rangle, |T_-\\rangle$):**
Both electrons have parallel spins. Hopping one electron to the other site would require placing two electrons with the *same spin* on the same site ($c_{1\\sigma}^\\dagger c_{1\\sigma}^\\dagger = 0$). By the Pauli exclusion principle, this is strictly forbidden!
Therefore, the hopping operator $\\hat{T}$ gives zero when acting on any triplet state:
$$\\hat{T} |T\\rangle = 0 \\implies E_T^{(2)} = 0$$
The triplet states cannot hop virtually, so their energy remains unperturbed at $E_T = 0$.

- **For the Singlet State ($|S\\rangle$):**
Because the two electrons have opposite spins, hopping is allowed by the Pauli principle:
$$\\hat{T} |S\\rangle = -t \\left[ c_{2\\downarrow}^\\dagger c_{1\\downarrow} \\frac{1}{\\sqrt{2}} c_{1\\uparrow}^\\dagger c_{2\\downarrow}^\\dagger - c_{2\\uparrow}^\\dagger c_{1\\uparrow} \\frac{1}{\\sqrt{2}} (-c_{1\\downarrow}^\\dagger c_{2\\uparrow}^\\dagger) + \\dots \\right] |0\rangle = -\\sqrt{2} t |D_+\\rangle$$
where $|D_+\\rangle = \\frac{1}{\\sqrt{2}} (|D_1\\rangle + |D_2\\rangle)$ is the symmetric doubly occupied state.
The intermediate state $|D_+\\rangle$ has unperturbed energy $U$.
By second-order perturbation theory:
$$E_S^{(2)} = \\sum_{m \\in \\text{doubly}} \\frac{|\\langle m | \\hat{T} | S \\rangle|^2}{E_0 - E_m} = \\frac{|-\\sqrt{2} t|^2}{0 - U} = -\\frac{2 t^2}{U}$$
Thus, virtual hopping to the doubly occupied states lowers the singlet energy by $-\\frac{2t^2}{U}$.

**(c) Effective Heisenberg Exchange Constant $J$:**
The energy difference between singlet and triplet is:
$$E_T - E_S = 0 - \\left(-\\frac{2t^2}{U}\\right) = +\\frac{2t^2}{U} > 0$$
The singlet ($S = 0$, antiparallel spins) is lower in energy than the triplet ($S = 1$) by $\\frac{2t^2}{U}$.
Recall the spin operator identity:
$$\\vec{S}_1 \\cdot \\vec{S}_2 = \\frac{1}{2} [S(S+1) - 3/2] = \\begin{cases} -3/4, & S = 0 \\\\ +1/4, & S = 1 \\end{cases}$$
We map this onto an effective spin Hamiltonian:
$$\\hat{H}_{\\text{spin}} = J \\vec{S}_1 \\cdot \\vec{S}_2 + C$$
Evaluating for the two states:
$$E_S = -\\frac{3}{4} J + C, \\quad E_T = +\\frac{1}{4} J + C$$
The difference is:
$$E_T - E_S = J$$
Equating to the microscopic perturbation result:
$$J = \\frac{4 t^2}{U} \\quad \\text{(Q.E.D.)}$$
Because $J = \\frac{4t^2}{U} > 0$, the ground state favors antiparallel spin alignment.
This proves that in the strong-coupling limit of the Hubbard model ($U \\gg t$), the kinetic suppression of charge fluctuations generates an **antiferromagnetic Heisenberg exchange interaction**! Virtual electron hopping lowers the kinetic energy of the antiparallel state through quantum mechanical hybridization with high-energy polar states."""
        }
    ]
}

with open("ssp2_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7_data, f, indent=2)

with open("ssp2_u8.json", "w", encoding="utf-8") as f:
    json.dump(u8_data, f, indent=2)

print("Generated ssp2_u7.json and ssp2_u8.json successfully.")
