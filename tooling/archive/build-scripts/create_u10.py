import json

def get_unit_10():
    u10 = {
        "id": "unit-10",
        "number": 10,
        "title": "Solid-State Transport, Fast-Ion Conductors & Superconductivity",
        "leadSummary": "Microscopic mechanisms of mass and thermal transport: ionic jump kinetics, Nernst-Einstein relations, fast-ion conductors (alpha-AgI, beta-alumina, LLZO, LGPS), phonon thermal conduction, Wiedemann-Franz law, low-temperature BCS superconductivity, Meissner effect, London electrodynamics, Type I/II classification, and high-Tc cuprates.",
        "simulations": ["sim_ssc_superconductor_meissner_transport"],
        "sections": [
            {
                "secNumber": "10.1",
                "title": "Microscopic Ionic Transport: Random Walk Diffusion & Nernst-Einstein",
                "content": r"""Ionic motion in crystalline solids proceeds via discrete, thermally activated hops of ions between adjacent crystallographic equilibrium sites (vacancies or interstitial voids).

### Random Walk Diffusion Model
Consider an ion jumping between lattice sites separated by jump distance $a$ with successful jump frequency $\\Gamma$.
By transition-state theory, the jump frequency is:
\\[
\\Gamma = z \\nu_0 \\exp\\left(-\\frac{\\Delta G_m}{k_B T}\\right) = z \\nu_0 \\exp\\left(\\frac{\\Delta S_m}{k_B}\\right) \\exp\\left(-\\frac{\\Delta H_m}{k_B T}\\right)
\\]
where $z$ is the number of nearest-neighbor jump directions, $\\nu_0 \\sim 10^{12} - 10^{13}\\text{ s}^{-1}$ is the fundamental attempt frequency (optical phonon vibration), and $\\Delta G_m = \\Delta H_m - T\\Delta S_m$ is the migration Gibbs free energy barrier.
In three dimensions, the random-walk diffusion coefficient $D$ is:
\\[
D = \\frac{1}{6} \\Gamma a^2 = \\frac{1}{6} z a^2 \\nu_0 \\exp\\left(\\frac{\\Delta S_m}{k_B}\\right) \\exp\\left(-\\frac{\\Delta H_m}{k_B T}\\right) = D_0 \\exp\\left(-\\frac{\\Delta H_m}{k_B T}\\right)
\\]

### The Nernst-Einstein Relation
When an external electric field $\\mathbf{E}$ is applied, the potential energy landscape tilts, biasing hops in the direction of the electrostatic force. The ionic drift mobility $u_{\\text{ion}}$ is related to the self-diffusion coefficient by the **Nernst-Einstein equation**:
\\[
\\frac{u_{\\text{ion}}}{D} = \\frac{q}{k_B T}
\\]
The macroscopic ionic conductivity $\\sigma_i$ of mobile ions with charge $q = z_i e$ and concentration $n_i$ is:
\\[
\\sigma_i = n_i q u_{\\text{ion}} = \\frac{n_i q^2 D}{k_B T} = \\frac{n_i (z_i e)^2 D_0}{k_B T} \\exp\\left(-\\frac{E_a}{k_B T}\\right)
\\]
Rearranging into standard Arrhenius form gives the **temperature-dependent ionic conductivity**:
\\[
\\sigma_i T = \\sigma_0 \\exp\\left(-\\frac{E_a}{k_B T}\\right)
\\]
A plot of $\\ln(\\sigma_i T)$ versus $1/T$ yields a straight line with slope $-E_a / k_B$, where the total activation energy $E_a$ is:
- In the intrinsic regime: $E_a = \\frac{1}{2}\\Delta H_{\\text{formation}} + \\Delta H_{\\text{migration}}$.
- In the extrinsic (doped) regime: $E_a = \\Delta H_{\\text{migration}}$ (since defect concentration is fixed by dopants).r"""
            },
            {
                "secNumber": "10.2",
                "title": "Fast-Ion Conductors (Superionic Solids): Liquid-like Sublattices & alpha-AgI",
                "content": r"""In normal ionic solids (e.g., $\\text{NaCl}$), ionic conductivity at ambient temperature is negligible ($\\sigma < 10^{-12}\\text{ S/cm}$) because mobile defects must be thermally generated. In contrast, **fast-ion conductors** (superionic conductors) exhibit liquid-like ionic conductivities ($\\sigma > 10^{-2} - 10^0\\text{ S/cm}$) in the solid state.

### The Molten Sublattice Concept: $\alpha$-AgI
Silver iodide provides the historical prototype:
- At ambient temperature, $\\beta\\text{-AgI}$ (wurtzite) is a conventional low-conductivity solid.
- At $T = 146.5^\\circ\\text{C}$, $\\text{AgI}$ undergoes a first-order phase transformation to **$\\alpha\\text{-AgI}$**:
  - The iodide anions ($\\text{I}^-$) form a rigid, crystalline body-centered cubic (BCC) framework.
  - The two $\\text{Ag}^+$ cations per unit cell are distributed statistically over **42 available interstitial sites** (6 octahedral, 12 tetrahedral, and 24 trigonal sites).
  - The silver sublattice is essentially "molten", allowing $\\text{Ag}^+$ ions to flow continuously through a liquid-like 3D percolation network of interconnected channels, giving $\\sigma = 1.3\\text{ S/cm}$ at $150^\\circ\\text{C}$.

### Sodium $\beta$''-Alumina ($\text{Na}_{1+x}\text{Al}_{11}\text{O}_{17+x/2}$)
Sodium $\\beta''$-alumina is the solid electrolyte used in sodium-sulfur (Na-S) and ZEBRA batteries:
- Consists of dense, insulating 4-layer spinel blocks of $[\\text{Al}_{11}\\text{O}_{16}]$ separated by open 2D **conduction planes** spaced by $11.3\\text{ Å}$.
- The conduction planes contain loosely bound $\\text{Na}^+$ ions and bridging column oxygens.
- Sodium ions migrate with near-zero activation barriers ($E_a \\approx 0.15\\text{ eV}$) within the 2D plane via an interstitialcy (knock-on) mechanism, yielding $\\sigma_{\\text{Na}^+} \\approx 0.2\\text{ S/cm}$ at $300^\\circ\\text{C}$.r"""
            },
            {
                "secNumber": "10.3",
                "title": "Solid Electrolytes for Modern Batteries: YSZ, NASICON & Garnet LLZO",
                "content": r"""The development of all-solid-state lithium metal batteries and high-temperature solid oxide fuel cells (SOFCs) hinges on solid electrolytes combining high ionic conductivity with negligible electronic conductivity (ionic transference number $t_{\\text{ion}} = \\sigma_{\\text{ion}}/\\sigma_{\\text{total}} > 0.999$) and broad electrochemical stability windows.

### Archetypal Solid Electrolyte Systems
1. **Yttria-Stabilized Zirconia (YSZ, SOFC Electrolyte)**:
   - Doping pure $\\text{ZrO}_2$ with $8\\text{ mol}\\%$ $\\text{Y}_2\\text{O}_3$ stabilizes the cubic fluorite phase down to room temperature and introduces a massive concentration ($4\\%$) of oxygen vacancies:
   \\[
   \\text{Y}_2\\text{O}_3 \\xrightarrow{\\text{ZrO}_2} 2\\text{Y}_{\\text{Zr}}' + 3\\text{O}_O^\\times + \\text{V}_O^{\\bullet\\bullet}
   \\]
   At $800^\\circ\\text{C}$, $\\text{O}^{2-}$ conductivity reaches $\\sigma \\approx 0.1\\text{ S/cm}$ ($E_a \\approx 0.9\\text{ eV}$).

2. **Garnet-Type LLZO ($\text{Li}_7\text{La}_3\text{Zr}_2\text{O}_{12}$)**:
   - Cubic garnet framework where $\\text{La}^{3+}$ and $\\text{Zr}^{4+}$ occupy dodecahedral and octahedral sites.
   - $\\text{Li}^+$ ions partially occupy tetrahedral $24d$ and octahedral $96h$ sites. When stabilized with dopants ($\\text{Al}^{3+}$ or $\\text{Ta}^{5+}$), cubic LLZO exhibits room-temperature lithium conductivity $\\sigma_{\\text{Li}^+} \\approx 1.0\\text{ mS/cm}$ and thermodynamic stability against metallic lithium ($0 - 4.5\\text{ V}$ vs $\\text{Li/Li}^+$).

3. **Sulfide Superionic Conductors: LGPS ($\text{Li}_{10}\text{GeP}_2\text{S}_{12}$)**:
   - Kamaya and Kanno (2011) discovered that replacing polarizable oxide frameworks with highly polarizable sulfur anions ($\\text{S}^{2-}$) flattens the interstitial electrostatic energy landscape.
   - $\\text{Li}_{10}\\text{GeP}_2\\text{S}_{12}$ achieves record room-temperature lithium conductivity:
   \\[
   \\sigma_{\\text{Li}^+} = 12\\text{ mS/cm} \\quad (1.2 \\times 10^{-2}\\text{ S/cm})
   \\]
   which surpasses conventional liquid organic carbonate electrolytes.r"""
            },
            {
                "secNumber": "10.4",
                "title": "Thermal Conductivity in Solids: Phonons, Mean Free Path & Wiedemann-Franz",
                "content": r"""Heat conduction in solids is carried by two fundamental energy carriers: quantized lattice vibrational waves (**phonons**) and mobile conduction **electrons**:
\\[
\\kappa = \\kappa_{\\text{ph}} + \\kappa_e
\\]

### Phonon Thermal Transport in Dielectrics
In electrical insulators, thermal conduction is mediated exclusively by phonons. Treating the phonon gas within kinetic theory:
\\[
\\kappa_{\\text{ph}} = \\frac{1}{3} C_V v_s \\ell_{\\text{ph}}
\\]
where $C_V$ is the volumetric lattice heat capacity, $v_s$ is the average sound velocity, and $\\ell_{\\text{ph}}$ is the phonon mean free path:
- **Low Temperatures ($T \\ll \\Theta_D$)**: Phonon-phonon scattering is frozen. $\\ell_{\\text{ph}}$ is limited by crystal boundaries ($D$), so $\\ell_{\\text{ph}} \\approx \\text{constant}$. Since $C_V \\propto T^3$ (Debye $T^3$ law):
\\[
\\kappa_{\\text{ph}} \\propto T^3
\\]
- **Intermediate Temperatures**: $\\kappa_{\\text{ph}}$ reaches a peak.
- **High Temperatures ($T > \\Theta_D$)**: $C_V \\approx 3Nk_B = \\text{constant}$ (Dulong-Petit law). Anharmonic three-phonon **Umklapp processes** (where $\\mathbf{q}_1 + \\mathbf{q}_2 = \\mathbf{q}_3 + \\mathbf{G}$, transferring momentum back to the lattice) dominate, causing $\\ell_{\\text{ph}} \\propto 1/T$:
\\[
\\kappa_{\\text{ph}} \\propto \\frac{1}{T}
\\]

### Electronic Thermal Transport & The Wiedemann-Franz Law
In metals, electrons dominate heat conduction ($\\kappa_e \\gg \\kappa_{\\text{ph}}$). Gustav Wiedemann and Rudolf Franz (1853), modernized by Sommerfeld (1928), showed that the ratio of electronic thermal conductivity to electrical conductivity is strictly proportional to absolute temperature:
\\[
\\frac{\\kappa_e}{\\sigma} = L T
\\]
where the theoretical **Lorenz number** $L$ is a universal quantum constant:
\\[
L = \\frac{\\pi^2}{3} \\left(\\frac{k_B}{e}\\right)^2 = 2.443 \\times 10^{-8}\\text{ W}\\cdot\\Omega/\\text{K}^2
\\]
This law holds with extraordinary precision ($< 5\\%$ error) for simple metals at room temperature.r"""
            },
            {
                "secNumber": "10.5",
                "title": "Superconductivity: Zero Resistance & Critical Parameters (Tc, Hc, Jc)",
                "content": r"""Discovered by Heike Kamerlingh Onnes in 1911 upon liquefying helium, **superconductivity** is a macroscopic quantum phenomenon characterized by two independent, fundamental properties:
1. **Zero Electrical Resistance** ($R = 0$) below a critical temperature $T_c$.
2. **Perfect Diamagnetism** (The Meissner Effect, $\\mathbf{B} = \\mathbf{0}$) in external magnetic fields below a critical threshold.

### The Three Critical Parameters
Superconductivity exists only within a bounded thermodynamic volume defined by three mutually interdependent critical limits:
1. **Critical Temperature ($T_c$)**:
   The transition temperature below which the material enters the superconducting state in zero magnetic field and zero transport current (e.g., $\\text{Hg}$: $4.15\\text{ K}$, $\\text{Pb}$: $7.2\\text{ K}$, $\\text{Nb}$: $9.25\\text{ K}$, $\\text{YBa}_2\\text{Cu}_3\\text{O}_7$: $93\\text{ K}$).
2. **Thermodynamic Critical Magnetic Field ($H_c$)**:
   An applied magnetic field above which superconductivity is destroyed. The temperature dependence obeys the empirical parabolic law:
   \\[
   H_c(T) = H_c(0) \\left[ 1 - \\left(\\frac{T}{T_c}\\right)^2 \\right]
   \\]
3. **Critical Current Density ($J_c$)**:
   By Silsbee's rule, the maximum electrical current density that can flow through the superconductor before the self-induced magnetic field exceeds $H_c(T)$:
   \\[
   J_c(T) \\propto H_c(T)
   \\]

### Condensation Energy
The transition to the superconducting state at $T < T_c$ stabilizes the material by the **superconducting condensation energy** $\\Delta F_{\\text{cond}}$:
\\[
\\Delta F_{\\text{cond}} = F_n(T) - F_s(T) = \\frac{\\mu_0 H_c^2(T)}{2}
\\]
When the magnetic energy penalty of expelling the external field ($\frac{1}{2}\\mu_0 H^2$) exceeds $\\Delta F_{\\text{cond}}$, the normal state is restored via a first-order phase transition.r"""
            },
            {
                "secNumber": "10.6",
                "title": "The Meissner-Ochsenfeld Effect & London Electrodynamics",
                "content": r"""In 1933, Walther Meissner and Robert Ochsenfeld demonstrated that a superconductor is not simply a hypothetical "perfect conductor" with $\\sigma \\to \\infty$, but an active thermodynamic diamagnet.

### The Meissner Effect vs Perfect Conductor
- In a hypothetical perfect conductor ($R = 0$), Faraday's law of induction $\\nabla \\times \\mathbf{E} = -\\partial \\mathbf{B}/\\partial t$ with $\\mathbf{E} = \\mathbf{0}$ implies:
\\[
\\frac{\\partial \\mathbf{B}}{\\partial t} = \\mathbf{0} \\implies \\mathbf{B} = \\text{constant in time}
\\]
If cooled in a magnetic field, a perfect conductor would trap the flux inside forever.
- In a **true superconductor**, when cooled below $T_c$ inside an external field, magnetic flux is **expelled spontaneously**:
\\[
\\mathbf{B} = \\mathbf{0} \\quad \\text{everywhere inside the bulk}
\\]
The magnetic susceptibility is that of a perfect diamagnet: $\\chi = -1$ (in SI units).

### The Phenomenological London Equations
Fritz and Heinz London (1935) formulated two equations governing the electrodynamics of the superconducting carrier density $n_s$:
1. **First London Equation** (Zero Resistance):
   Accelerating the superconducting electron fluid with electric field $\mathbf{E}$:
   \\[
   m \\frac{d\\mathbf{v}_s}{dt} = -e \\mathbf{E} \\implies \\frac{\\partial \\mathbf{J}_s}{\\partial t} = \\frac{n_s e^2}{m} \\mathbf{E}
   \\]
2. **Second London Equation** (Meissner Effect):
   Taking the curl and combining with Maxwell's equation $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$:
   \\[
   \\nabla \\times \\mathbf{J}_s = -\\frac{n_s e^2}{m} \\mathbf{B}
   \\]

### London Penetration Depth ($\lambda_L$)
Combining the Second London Equation with Ampère's law $\\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J}_s$ (using $\\nabla \\times (\\nabla \\times \\mathbf{B}) = \\nabla(\\nabla \\cdot \\mathbf{B}) - \\nabla^2 \\mathbf{B} = -\\nabla^2 \\mathbf{B}$):
\\[
\\nabla^2 \\mathbf{B} = \\frac{\\mu_0 n_s e^2}{m} \\mathbf{B} = \\frac{1}{\\lambda_L^2} \\mathbf{B}
\\]
where the **London penetration depth** $\\lambda_L$ is:
\\[
\\lambda_L = \\sqrt{\\frac{m}{\\mu_0 n_s e^2}}
\\]
At a planar surface $x = 0$, the magnetic field decays exponentially into the bulk:
\\[
B(x) = B_0 e^{-x / \\lambda_L}
\\]
Magnetic fields penetrate only a microscopic skin layer of thickness $\\lambda_L \\approx 20 - 200\\text{ nm}$, screened by persistent dissipationless surface currents.r"""
            },
            {
                "secNumber": "10.7",
                "title": "Type I vs Type II Superconductors: Ginzburg-Landau Parameter & Vortices",
                "content": r"""Vitaly Ginzburg and Lev Landau (1950) introduced a macroscopic quantum order parameter $\\psi(\\mathbf{r}) = |\\psi| e^{i\\theta}$ (where $n_s = |\\psi|^2$).

### The Two Characteristic Length Scales
1. **London Penetration Depth ($\lambda_L$)**: The distance over which magnetic fields decay exponentially into the superconductor.
2. **Ginzburg-Landau Coherence Length ($\\xi$)**: The minimum distance over which the superconducting order parameter $|\psi|$ can change without prohibitive kinetic energy cost:
\\[
\\xi(T) = \\frac{\\hbar}{\\sqrt{2m |\\alpha(T)|}} \\approx 0.18 \\frac{\\hbar v_F}{k_B T_c}
\\]

### The Ginzburg-Landau Parameter ($\kappa$) & Surface Energy
The ratio of these two lengths defines the dimensionless **Ginzburg-Landau parameter**:
\\[
\\kappa = \\frac{\\lambda_L}{\\xi}
\\]
The interfacial surface energy $\\sigma_{\\text{ns}}$ between a normal and superconducting domain depends directly on $\\kappa$:
- **Type I Superconductors** ($\\kappa < 1/\\sqrt{2} \\approx 0.707$):
  - Coherence length dominates ($\\xi > \\sqrt{2}\\lambda_L$).
  - The surface energy is **positive** ($\\sigma_{\\text{ns}} > 0$).
  - Domain boundaries are energetically penalized. The material exhibits a sharp, complete Meissner effect up to $H_c$, where it transitions abruptly to the normal state.
  - Examples: Pure elemental metals ($\\text{Pb}, \\text{Sn}, \\text{Al}, \\text{Hg}$).

- **Type II Superconductors** ($\\kappa > 1/\\sqrt{2} \\approx 0.707$):
  - Penetration depth dominates ($\lambda_L > \\sqrt{2}\\xi$).
  - The surface energy is **negative** ($\\sigma_{\\text{ns}} < 0$).
  - Formation of normal-superconducting interfaces is energetically favorable!
  - Exhibits two critical fields:
    - **Lower Critical Field ($H_{c1}$)**: Complete Meissner expulsion for $H < H_{c1}$.
    - **Vortex (Mixed / Shubnikov) State** ($H_{c1} < H < H_{c2}$): Magnetic flux penetrates the material in the form of quantized flux filaments (**Abrikosov vortices**), each carrying one flux quantum $\\Phi_0 = h/(2e) = 2.0678 \\times 10^{-15}\\text{ Wb}$.
    - **Upper Critical Field ($H_{c2}$)**: Superconductivity is extinguished when vortex cores overlap at $H_{c2} = \\frac{\\Phi_0}{2\\pi \\xi^2}$.
  - Examples: Transition metal alloys ($\\text{NbTi}, \\text{Nb}_3\\text{Sn}$) and cuprates (YBCO, BSCCO) with $H_{c2} > 20 - 100\\text{ T}$, enabling powerful MRI and particle accelerator magnets.r"""
            },
            {
                "secNumber": "10.8",
                "title": "Microscopic BCS Theory, High-Tc Cuprates & Modern Technologies",
                "content": r"""The microscopic mechanism of conventional superconductivity was solved in 1957 by John Bardeen, Leon Cooper, and J. Robert Schrieffer (**BCS theory**).

### BCS Theory and Cooper Pairs
1. **Cooper Pairing**: An electron moving through the lattice polarizes the positively charged ionic cores, creating a localized trailing region of positive charge density. A second electron is attracted to this phonon-mediated polarization wake.
2. At $T < T_c$, this attractive electron-phonon interaction overcomes the screened Coulomb repulsion, binding pairs of electrons with opposite momenta and spins into a composite spin-singlet boson:
\\[
(\\mathbf{k} \\uparrow, -\\mathbf{k} \\downarrow) \\quad (S = 0)
\\]
3. Cooper pairs condense into a phase-coherent, macroscopic quantum ground state protected by an energy gap:
\\[
\\Delta(0) = 1.764 k_B T_c
\\]
Because an energy $2\\Delta$ is required to break a Cooper pair, electrons cannot be scattered elastically by single phonons or impurities, resulting in strictly zero electrical resistance.

### High-Temperature Superconductors (HTS)
- In 1986, Georg Bednorz and K. Alex Müller discovered superconductivity at $35\\text{ K}$ in $\\text{La}_{2-x}\\text{Ba}_x\\text{CuO}_4$, sparking the cuprate revolution.
- In 1987, $\\text{YBa}_2\\text{Cu}_3\\text{O}_{7-\\delta}$ (YBCO) broke the liquid nitrogen barrier ($77\\text{ K}$) with $T_c = 93\\text{ K}$, later extended to $135\\text{ K}$ in $\\text{HgBa}_2\\text{Ca}_2\\text{Cu}_3\\text{O}_8$ ($164\\text{ K}$ under high pressure).
- Cuprates are characterized by quasi-2D $[\\text{CuO}_2]$ planes, unconventional $d_{x^2 - y^2}$ orbital pairing symmetry, and strong electron correlation effects driven by antiferromagnetic spin fluctuations rather than simple acoustic phonons.
- In 2008, Hideo Hosono discovered iron-based superconductors (e.g., $\\text{LaFeAsO}_{1-x}\\text{F}_x, T_c = 26 - 56\\text{ K}$) with $s_{\\pm}$ pairing.

### Superconducting Quantum Technologies
- **SQUIDs (Superconducting Quantum Interference Devices)**: Measure minute magnetic fields down to $10^{-15}\\text{ T}$ via Josephson junction flux quantization.
- **Superconducting Qubits (Transmons)**: Form the hardware foundation for modern quantum computers (e.g., Google Sycamore, IBM Quantum).r"""
            }
        ],
        "problems": [
            {
                "probNumber": "10.1",
                "title": "Ionic Conductivity and Diffusion in Sodium beta-Alumina via Nernst-Einstein",
                "difficulty": "Foundational",
                "statement": "In a crystal of sodium $\\beta''$-alumina, the mobile $\\text{Na}^+$ ion concentration is $n = 4.20 \\times 10^{21}\\text{ cm}^{-3}$. The measured tracer diffusion coefficient at $T = 300^\\circ\\text{C}$ ($573.15\\text{ K}$) is $D^* = 1.65 \\times 10^{-6}\\text{ cm}^2/\\text{s}$ with Haven ratio $H_R = 0.60$.\\n(a) Compute the charge carrier diffusion coefficient $D_{\\sigma} = D^* / H_R$.\\n(b) Using the Nernst-Einstein equation, calculate the ionic drift mobility $\\mu_{\\text{ion}}$ in $\\text{cm}^2/(\\text{V}\\cdot\\text{s})$.\\n(c) Determine the electrical ionic conductivity $\\sigma_{\\text{ion}}$ in $\\text{S/cm}$ at $300^\\circ\\text{C}$.",
                "solution": r"""### Step 1: Charge Carrier Diffusion Coefficient
The Haven ratio relates the tracer diffusion coefficient $D^*$ to the conductivity diffusion coefficient $D_\\sigma$:
\\[
H_R = \\frac{D^*}{D_\\sigma} \\implies D_\\sigma = \\frac{D^*}{H_R}
\\]
With $D^* = 1.65 \\times 10^{-6}\\text{ cm}^2/\\text{s}$ and $H_R = 0.60$:
\\[
D_\\sigma = \\frac{1.65 \\times 10^{-6}\\text{ cm}^2/\\text{s}}{0.60} = 2.75 \\times 10^{-6}\\text{ cm}^2/\\text{s} = 2.75 \\times 10^{-10}\\text{ m}^2/\\text{s}
\\]

### Step 2: Ionic Drift Mobility
By the Nernst-Einstein equation:
\\[
\\mu_{\\text{ion}} = \\frac{e D_\\sigma}{k_B T}
\\]
At $T = 573.15\\text{ K}$:
\\[
k_B T = (1.38065 \\times 10^{-23}\\text{ J/K})(573.15\\text{ K}) = 7.9132 \\times 10^{-21}\\text{ J}
\\]
In electron-volts:
\\[
\\frac{k_B T}{e} = 0.04939\\text{ V} = 49.39\\text{ mV}
\\]
Ionic mobility:
\\[
\\mu_{\\text{ion}} = \\frac{D_\\sigma}{k_B T / e} = \\frac{2.75 \\times 10^{-6}\\text{ cm}^2/\\text{s}}{0.04939\\text{ V}} = 5.568 \\times 10^{-5}\\text{ cm}^2/(\\text{V}\\cdot\\text{s})
\\]

### Step 3: Ionic Conductivity
The macroscopic ionic conductivity is:
\\[
\\sigma_{\\text{ion}} = n e \\mu_{\\text{ion}}
\\]
Given $n = 4.20 \\times 10^{21}\\text{ cm}^{-3}$:
\\[
\\sigma_{\\text{ion}} = (4.20 \\times 10^{21}\\text{ cm}^{-3})(1.60218 \\times 10^{-19}\\text{ C})(5.568 \\times 10^{-5}\\text{ cm}^2/(\\text{V}\\cdot\\text{s}))
\\]
\\[
\\sigma_{\\text{ion}} = (672.92\\text{ C/cm}^3)(5.568 \\times 10^{-5}\\text{ cm}^2/(\\text{V}\\cdot\\text{s})) = 0.03747\\text{ S/cm} \\approx 0.0375\\text{ S/cm} = 3.75\\text{ S/m}
\\]
(Matches experimental Na-beta'' alumina conductivity benchmarks at $300^\circ\text{C}$).r"""
            },
            {
                "probNumber": "10.2",
                "title": "Haven Ratio and Tracer Diffusion Correlation Factor in Rock Salt",
                "difficulty": "Intermediate",
                "statement": "In vacancy-mediated cation self-diffusion in an FCC rock-salt lattice ($\\text{NaCl}$), successive jumps of a radioactive tracer ion ($^{22}\\text{Na}^+$) are geometrically correlated.\\n(a) Explain why the direction of a tracer jump is negatively correlated with its immediately preceding jump ($\\langle \\cos\\theta_1 \\rangle < 0$).\\n(b) Using the Bardeen-Herring formula $f = \\frac{1 + \\langle \\cos\\theta \\rangle}{1 - \\langle \\cos\\theta \\rangle}$, calculate the correlation factor $f$ for an FCC lattice given $\\langle \\cos\\theta \\rangle = -1/11 = -0.09091$.\\n(c) For a pure monovacancy mechanism with neutral vacancies, express the Haven ratio $H_R$ in terms of $f$ and deduce its numerical value.",
                "solution": r"""### Step 1: Physical Origin of Jump Correlation
Consider a radioactive tracer atom $^{22}\\text{Na}^+$ that has just jumped into a neighboring vacancy:
- Immediately after the jump, the vacancy resides directly behind the tracer ion (at the site the tracer just vacated).
- For its next jump, the tracer ion has $z = 12$ nearest-neighbor sites in the FCC lattice. However, $11$ of these sites are occupied by regular sodium ions, while $1$ site is the very vacancy it just exchanged with!
- Therefore, the tracer has a significantly higher probability of jumping straight back to its original site than in any other direction.
- Consequently, the angle $\\theta_1$ between two successive jump vectors satisfies $\\langle \\cos\\theta_1 \\rangle < 0$, making the tracer walk less efficient than a truly random walk.

### Step 2: Calculation of the Correlation Factor
John Bardeen and Conyers Herring (1951) derived the correlation factor $f$:
\\[
f = \\lim_{N \\to \\infty} \\frac{\\langle R^2 \\rangle}{N a^2} = \\frac{1 + \\langle \\cos\\theta \\rangle}{1 - \\langle \\cos\\theta \\rangle}
\\]
Given $\\langle \\cos\\theta \\rangle = -\\frac{1}{11} = -0.09091$:
Numerator:
\\[
1 + \\left(-\\frac{1}{11}\\right) = \\frac{10}{11}
\\]
Denominator:
\\[
1 - \\left(-\\frac{1}{11}\\right) = \\frac{12}{11}
\\]
Correlation factor:
\\[
f = \\frac{10/11}{12/11} = \\frac{10}{12} = \\frac{5}{6} = 0.7815 \\approx 0.781
\\]
(The rigorous infinite-pathway summation yields $f_{\\text{FCC}} = 0.78146$).

### Step 3: The Haven Ratio
The Haven ratio is defined as:
\\[
H_R = \\frac{D^*}{D_\\sigma}
\\]
- In electrical conductivity, charge transport is measured by the motion of the **vacancy**: every time a vacancy jumps, it carries effective charge $-e$ regardless of whether the jumping ion was a tracer or normal ion. Vacancy motion is completely uncorrelated ($f_v = 1.0$).
- Tracer diffusion tracks the motion of the **specific tracer ion**, which is subject to correlation factor $f$:
\\[
D^* = f D_{\\text{ion}}
\\]
- Therefore, for a single monovacancy hopping mechanism without neutral pairs:
\\[
H_R = f = 0.781
\\]
Measuring $H_R = 0.78$ in an experimental crystal provides conclusive proof of a vacancy-mediated diffusion mechanism.r"""
            },
            {
                "probNumber": "10.3",
                "title": "Temperature-Dependent Ionic Conductivity and Arrhenius Activation Energy for LGPS",
                "difficulty": "Intermediate",
                "statement": "The superionic conductor $\\text{Li}_{10}\\text{GeP}_2\\text{S}_{12}$ (LGPS) displays the following ionic conductivity data:\\n- At $T = -20.0^\\circ\\text{C}$ ($253.15\\text{ K}$): $\\sigma = 2.45 \\times 10^{-3}\\text{ S/cm}$\\n- At $T = 25.0^\\circ\\text{C}$ ($298.15\\text{ K}$): $\\sigma = 1.20 \\times 10^{-2}\\text{ S/cm}$\\n- At $T = 100.0^\\circ\\text{C}$ ($373.15\\text{ K}$): $\\sigma = 4.85 \\times 10^{-2}\\text{ S/cm}$\\n(a) Formulate the Arrhenius relation for ionic conductivity $\\sigma T = \\sigma_0 \\exp(-E_a/k_B T)$.\\n(b) Using the data points at $253.15\\text{ K}$ and $373.15\\text{ K}$, compute the activation energy $E_a$ in $\\text{eV}$ and $\\text{kJ/mol}$.\\n(c) Predict the conductivity $\\sigma$ at $T = 60.0^\\circ\\text{C}$ ($333.15\\text{ K}$) and compare with experiment.",
                "solution": r"""### Step 1: Arrhenius Equation Formulation
The temperature dependence of ionic conductivity obeys:
\\[
\\sigma T = \\sigma_0 \\exp\\left(-\\frac{E_a}{k_B T}\\right) \\implies \\ln(\\sigma T) = \\ln\\sigma_0 - \\frac{E_a}{k_B} \\frac{1}{T}
\\]

### Step 2: Activation Energy Calculation
Compute $\\sigma T$ values:
1. At $T_1 = 253.15\\text{ K}$:
\\[
\\sigma_1 T_1 = (2.45 \\times 10^{-3}\\text{ S/cm})(253.15\\text{ K}) = 0.62022\\text{ S}\\cdot\\text{K/cm}
\\]
\\[
\\ln(\\sigma_1 T_1) = \\ln(0.62022) = -0.4777
\\]
\\[
\\frac{1}{T_1} = \\frac{1}{253.15} = 0.0039502\\text{ K}^{-1}
\\]

2. At $T_2 = 373.15\\text{ K}$:
\\[
\\sigma_2 T_2 = (4.85 \\times 10^{-2}\\text{ S/cm})(373.15\\text{ K}) = 18.0978\\text{ S}\\cdot\\text{K/cm}
\\]
\\[
\\ln(\\sigma_2 T_2) = \\ln(18.0978) = 2.8958
\\]
\\[
\\frac{1}{T_2} = \\frac{1}{373.15} = 0.0026799\\text{ K}^{-1}
\\]

Differences:
\\[
\\Delta \\ln(\\sigma T) = 2.8958 - (-0.4777) = 3.3735
\\]
\\[
\\Delta\\left(\\frac{1}{T}\\right) = 0.0026799 - 0.0039502 = -0.0012703\\text{ K}^{-1}
\\]
Slope:
\\[
-\\frac{E_a}{k_B} = \\frac{3.3735}{-0.0012703} = -2655.7\\text{ K} \\implies \\frac{E_a}{k_B} = 2655.7\\text{ K}
\\]
Activation energy:
\\[
E_a = (2655.7\\text{ K})(8.6173 \\times 10^{-5}\\text{ eV/K}) = 0.2288\\text{ eV} \\approx 0.23\\text{ eV}
\\]
In $\\text{kJ/mol}$:
\\[
E_a = (2655.7\\text{ K})(8.3145\\text{ J/(mol}\\cdot\\text{K)}) = 22,\\!081\\text{ J/mol} = 22.1\\text{ kJ/mol}
\\]
(This ultra-low activation energy $0.23\\text{ eV}$ explains the exceptional room-temperature conduction).

### Step 3: Prediction at $60^\circ\text{C}$ ($333.15\text{ K}$)
Using $T_3 = 333.15\\text{ K}$:
\\[
\\frac{1}{T_3} = \\frac{1}{333.15} = 0.0030017\\text{ K}^{-1}
\\]
\\[
\\ln(\\sigma_3 T_3) = \\ln(\\sigma_2 T_2) - \\frac{E_a}{k_B} \\left(\\frac{1}{T_3} - \\frac{1}{T_2}\\right)
\\]
\\[
\\frac{1}{T_3} - \\frac{1}{T_2} = 0.0030017 - 0.0026799 = +0.0003218\\text{ K}^{-1}
\\]
\\[
\\ln(\\sigma_3 T_3) = 2.8958 - (2655.7)(0.0003218) = 2.8958 - 0.8546 = 2.0412
\\]
\\[
\\sigma_3 T_3 = \\exp(2.0412) = 7.6998\\text{ S}\\cdot\\text{K/cm}
\\]
Conductivity:
\\[
\\sigma_3 = \\frac{7.6998}{333.15} = 0.02311\\text{ S/cm} = 2.31 \\times 10^{-2}\\text{ S/cm}
\\]
(Matches experimental measurements $2.3 \\times 10^{-2}\\text{ S/cm}$ to within $0.5\\%$).r"""
            },
            {
                "probNumber": "10.4",
                "title": "Lattice Thermal Conductivity Calculation using Debye Phonon Gas Formulation",
                "difficulty": "Intermediate",
                "statement": "In crystalline silicon at room temperature ($T = 300\\text{ K}$), the volumetric heat capacity is $C_V = 1.66 \\times 10^6\\text{ J/(m}^3\\cdot\\text{K)}$, average acoustic phonon velocity is $v_s = 5800\\text{ m/s}$, and measured thermal conductivity is $\\kappa = 148\\text{ W/(m}\\cdot\\text{K)}$.\\n(a) Using kinetic theory $\\kappa = \\frac{1}{3} C_V v_s \\ell$, calculate the effective phonon mean free path $\\ell_{\\text{ph}}$ in $\\text{nm}$.\\n(b) Compute the average phonon relaxation time $\\tau_{\\text{ph}}$.\\n(c) In a silicon nanowire of diameter $d = 20\\text{ nm}$, boundary scattering reduces the mean free path to $\\ell' \\approx d$. Calculate the predicted thermal conductivity of the nanowire and compute the percentage reduction.",
                "solution": r"""### Step 1: Phonon Mean Free Path in Bulk Silicon
The kinetic theory formulation for phonon thermal conductivity is:
\\[
\\kappa = \\frac{1}{3} C_V v_s \\ell_{\\text{ph}}
\\]
Rearranging for $\\ell_{\\text{ph}}$:
\\[
\\ell_{\\text{ph}} = \\frac{3 \\kappa}{C_V v_s}
\\]
Given:
- $\\kappa = 148\\text{ W/(m}\\cdot\\text{K)}$
- $C_V = 1.66 \\times 10^6\\text{ J/(m}^3\\cdot\\text{K)}$
- $v_s = 5800\\text{ m/s}$

\\[
C_V v_s = (1.66 \\times 10^6)(5800) = 9.628 \\times 10^9\\text{ W/(m}^2\\cdot\\text{K)}
\\]
\\[
\\ell_{\\text{ph}} = \\frac{3 \\times 148}{9.628 \\times 10^9} = \\frac{444}{9.628 \\times 10^9} = 4.612 \\times 10^{-8}\\text{ m} = 46.1\\text{ nm}
\\]
The average distance between phonon-phonon Umklapp scattering events in bulk silicon is $46.1\\text{ nm}$.

### Step 2: Phonon Relaxation Time
The average relaxation time between scattering events is:
\\[
\\tau_{\\text{ph}} = \\frac{\\ell_{\\text{ph}}}{v_s} = \\frac{4.612 \\times 10^{-8}\\text{ m}}{5800\\text{ m/s}} = 7.95 \\times 10^{-12}\\text{ s} = 7.95\\text{ ps}
\\]

### Step 3: Nanowire Thermal Conductivity
In a $20\\text{ nm}$ nanowire, diffusive phonon scattering from the wire surfaces limits the mean free path to $\\ell' = 20.0\\text{ nm} = 2.0 \\times 10^{-8}\\text{ m}$.
The new thermal conductivity is:
\\[
\\kappa_{\\text{nano}} = \\frac{1}{3} C_V v_s \\ell' = \\frac{1}{3}(9.628 \\times 10^9\\text{ W/(m}^2\\cdot\\text{K)})(2.0 \\times 10^{-8}\\text{ m}) = 64.19\\text{ W/(m}\\cdot\\text{K)}
\\]
Percentage reduction:
\\[
\\frac{\\Delta \\kappa}{\\kappa_{\\text{bulk}}} = \\frac{64.19 - 148}{148} \\times 100\\% = \\frac{-83.81}{148} \\times 100\\% = -56.6\\%
\\]
Nanostructuring suppresses thermal conductivity by over $56\\%$ without substantially altering electronic band structure, which is the foundational strategy for thermoelectric efficiency enhancement.r"""
            },
            {
                "probNumber": "10.5",
                "title": "Wiedemann-Franz Law Verification and Transport Separation in Aluminium",
                "difficulty": "Foundational",
                "statement": "At $T = 300.0\\text{ K}$, metallic aluminium has electrical conductivity $\\sigma = 3.65 \\times 10^7\\text{ S/m}$ and measured total thermal conductivity $\\kappa = 237.0\\text{ W/(m}\\cdot\\text{K)}$.\\n(a) Using the theoretical Sommerfeld Lorenz number $L_0 = 2.443 \\times 10^{-8}\\text{ W}\\cdot\\Omega/\\text{K}^2$, calculate the theoretical electronic thermal conductivity $\\kappa_e$.\\n(b) Separate the total thermal conductivity into electronic ($\\kappa_e$) and lattice phonon ($\\kappa_{\\text{ph}}$) contributions.\\n(c) Calculate the experimental Lorenz number $L_{\\text{exp}} = \\kappa / (\\sigma T)$ and determine the percentage error relative to $L_0$.",
                "solution": r"""### Step 1: Electronic Thermal Conductivity
By the Wiedemann-Franz law:
\\[
\\kappa_e = L_0 \\sigma T
\\]
With $\\sigma = 3.65 \\times 10^7\\text{ S/m}$ and $T = 300.0\\text{ K}$:
\\[
\\kappa_e = (2.443 \\times 10^{-8}\\text{ W}\\cdot\\Omega/\\text{K}^2)(3.65 \\times 10^7\\text{ S/m})(300.0\\text{ K})
\\]
\\[
\\kappa_e = (2.443 \\times 10^{-8}) \\times (1.095 \\times 10^{10}) = 267.5\\text{ W/(m}\\cdot\\text{K)}
\\]
*(Note: At room temperature, inelastic electron-phonon scattering reduces effective $L$ slightly below $L_0$ to $\\sim 2.15 \\times 10^{-8}$).*

Using standard room-temperature transport data for aluminum ($L_{\\text{eff}} \\approx 2.14 \\times 10^{-8}\\text{ W}\\cdot\\Omega/\\text{K}^2$):
\\[
\\kappa_e = (2.14 \\times 10^{-8})(3.65 \\times 10^7)(300) = 234.3\\text{ W/(m}\\cdot\\text{K)}
\\]

### Step 2: Lattice Phonon Contribution
Using the total measured thermal conductivity $\\kappa = 237.0\\text{ W/(m}\\cdot\\text{K)}$:
\\[
\\kappa_{\\text{ph}} = \\kappa - \\kappa_e = 237.0 - 234.3 = 2.7\\text{ W/(m}\\cdot\\text{K)}
\\]
Phonons contribute only:
\\[
\\frac{\\kappa_{\\text{ph}}}{\\kappa} = \\frac{2.7}{237.0} = 1.14\\%
\\]
Over $98.8\\%$ of heat transport in aluminum is carried by conduction electrons!

### Step 3: Experimental Lorenz Number
\\[
L_{\\text{exp}} = \\frac{\\kappa}{\\sigma T} = \\frac{237.0\\text{ W/(m}\\cdot\\text{K)}}{(3.65 \\times 10^7\\text{ S/m})(300.0\\text{ K})} = \\frac{237.0}{1.095 \\times 10^{10}} = 2.164 \\times 10^{-8}\\text{ W}\\cdot\\Omega/\\text{K}^2
\\]
Percentage deviation from Sommerfeld value $L_0 = 2.443 \\times 10^{-8}$:
\\[
\\frac{2.164 - 2.443}{2.443} \\times 100\\% = \\frac{-0.279}{2.443} \\times 100\\% = -11.4\\%
\\]
This small deviation arises because at room temperature ($T < \\Theta_D = 428\\text{ K}$), small-angle electron-phonon scattering relaxes thermal transport more rapidly than electrical momentum.r"""
            },
            {
                "probNumber": "10.6",
                "title": "London Penetration Depth and Screening Current Density Derivation",
                "difficulty": "Intermediate",
                "statement": "Superconducting lead ($\\text{Pb}$, $T_c = 7.19\\text{ K}$) has a superconducting electron density of $n_s = 3.50 \\times 10^{28}\\text{ m}^{-3}$ at $T = 0\\text{ K}$.\\n(a) Derive the London penetration depth expression $\\lambda_L = \\sqrt{\\frac{m_e}{\\mu_0 n_s e^2}}$ and compute $\\lambda_L(0)$ in $\\text{nm}$.\\n(b) Using the empirical two-fluid relation $n_s(T) = n_s(0)[1 - (T/T_c)^4]$, compute $\\lambda_L$ at $T = 4.20\\text{ K}$ (liquid helium).\\n(c) In an external parallel magnetic field $B_0 = 0.050\\text{ T}$, calculate the surface screening current density $J_s(0)$ at the specimen boundary.",
                "solution": r"""### Step 1: London Penetration Depth at $T = 0\\text{ K}$
The second London equation combined with Ampère's law gives:
\\[
\\nabla^2 \\mathbf{B} = \\frac{\\mu_0 n_s e^2}{m_e} \\mathbf{B} = \\frac{1}{\\lambda_L^2} \\mathbf{B} \\implies \\lambda_L = \\sqrt{\\frac{m_e}{\\mu_0 n_s e^2}}
\\]
Given:
- $m_e = 9.10938 \\times 10^{-31}\\text{ kg}$
- $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ N/A}^2 = 1.25664 \\times 10^{-6}\\text{ H/m}$
- $e = 1.60218 \\times 10^{-19}\\text{ C} \\implies e^2 = 2.5670 \\times 10^{-38}\\text{ C}^2$
- $n_s = 3.50 \\times 10^{28}\\text{ m}^{-3}$

Denominator:
\\[
\\mu_0 n_s e^2 = (1.25664 \\times 10^{-6})(3.50 \\times 10^{28})(2.5670 \\times 10^{-38}) = 1.12905 \\times 10^{-15}\\text{ kg}/(\\text{m}^3\\cdot\\text{s}^2)
\\]
\\[
\\lambda_L^2 = \\frac{9.10938 \\times 10^{-31}}{1.12905 \\times 10^{-15}} = 8.0682 \\times 10^{-16}\\text{ m}^2
\\]
\\[
\\lambda_L(0) = \\sqrt{8.0682 \\times 10^{-16}} = 2.840 \\times 10^{-8}\\text{ m} = 28.4\\text{ nm}
\\]
(Experimental value: $\\lambda_{L,\\text{exp}} \\approx 37\\text{ nm}$, difference due to effective mass $m^*/m_0 \\approx 1.7$).

### Step 2: Temperature-Dependent Penetration Depth at $4.2\\text{ K}$
According to the two-fluid model:
\\[
\\lambda_L(T) = \\frac{\\lambda_L(0)}{\\sqrt{1 - (T/T_c)^4}}
\\]
With $T = 4.20\\text{ K}$ and $T_c = 7.19\\text{ K}$:
\\[
\\frac{T}{T_c} = \\frac{4.20}{7.19} = 0.5841
\\]
\\[
\\left(\\frac{T}{T_c}\\right)^4 = (0.5841)^4 = 0.1164
\\]
\\[
\\sqrt{1 - 0.1164} = \\sqrt{0.8836} = 0.9400
\\]
\\[
\\lambda_L(4.2\\text{ K}) = \\frac{28.4\\text{ nm}}{0.9400} = 30.2\\text{ nm}
\\]

### Step 3: Surface Screening Current Density
Inside the superconductor, $B(x) = B_0 e^{-x/\\lambda_L}$.
By Ampère's law ($\\mathbf{J}_s = \\frac{1}{\\mu_0} \\nabla \\times \\mathbf{B}$):
\\[
J_s(x) = -\\frac{1}{\\mu_0} \\frac{dB}{dx} = \\frac{B_0}{\\mu_0 \\lambda_L} e^{-x/\\lambda_L}
\\]
At the surface $x = 0$:
\\[
J_s(0) = \\frac{B_0}{\\mu_0 \\lambda_L} = \\frac{0.050\\text{ T}}{(1.25664 \\times 10^{-6}\\text{ H/m})(30.2 \\times 10^{-9}\\text{ m})} = \\frac{0.050}{3.795 \\times 10^{-14}} = 1.317 \\times 10^{12}\\text{ A/m}^2
\\]
The surface screening current density is $1.32 \\times 10^8\\text{ A/cm}^2$, flowing continuously without resistive dissipation.r"""
            },
            {
                "probNumber": "10.7",
                "title": "Ginzburg-Landau Parameter and Critical Fields in Niobium-Titanium",
                "difficulty": "Intermediate",
                "statement": r"A technical superconducting niobium-titanium alloy ($\text{Nb-47wt}\\%\\text{Ti}$, $T_c = 9.30\\text{ K}$) has coherence length $\\xi = 5.50\\text{ nm}$ and London penetration depth $\\lambda_L = 240.0\\text{ nm}$ at $T = 4.20\\text{ K}$.\\n(a) Compute the Ginzburg-Landau parameter $\\kappa = \\lambda_L/\\xi$ and confirm whether NbTi is Type I or Type II.\\n(b) Using flux quantum $\\Phi_0 = 2.0678 \\times 10^{-15}\\text{ Wb}$, calculate the upper critical magnetic field $B_{c2} = \\mu_0 H_{c2} = \\frac{\\Phi_0}{2\\pi \\xi^2}$.\\n(c) Compute the lower critical magnetic field $B_{c1} = \\frac{\\Phi_0}{4\\pi \\lambda_L^2} \\ln\\kappa$ and the thermodynamic critical field $B_c = \\frac{B_{c2}}{\\sqrt{2}\\kappa}$.",
                "solution": r"""### Step 1: Ginzburg-Landau Parameter
\\[
\\kappa = \\frac{\\lambda_L}{\\xi} = \\frac{240.0\\text{ nm}}{5.50\\text{ nm}} = 43.636 \\approx 43.6
\\]
Because $\\kappa = 43.6 \\gg 1/\\sqrt{2} \\approx 0.707$, $\\text{NbTi}$ is an **extreme Type II superconductor**.

### Step 2: Upper Critical Magnetic Field $B_{c2}$
The upper critical field is dictated by the coherence length $\\xi$:
\\[
B_{c2} = \\frac{\\Phi_0}{2\\pi \\xi^2}
\\]
Given $\\xi = 5.50 \\times 10^{-9}\\text{ m}$:
\\[
\\xi^2 = (5.50 \\times 10^{-9}\\text{ m})^2 = 3.025 \\times 10^{-17}\\text{ m}^2
\\]
\\[
2\\pi \\xi^2 = 2\\pi (3.025 \\times 10^{-17}) = 1.9007 \\times 10^{-16}\\text{ m}^2
\\]
Upper critical field:
\\[
B_{c2} = \\frac{2.0678 \\times 10^{-15}\\text{ Wb}}{1.9007 \\times 10^{-16}\\text{ m}^2} = 10.88\\text{ T}
\\]
(Matches the upper critical field of commercial MRI superconducting wire, $B_{c2} \\approx 11\\text{ T}$ at $4.2\\text{ K}$).

### Step 3: Lower Critical Field and Thermodynamic Critical Field
1. **Lower Critical Field $B_{c1}$**:
\\[
B_{c1} = \\frac{\\Phi_0}{4\\pi \\lambda_L^2} \\ln\\kappa
\\]
With $\\lambda_L = 2.40 \\times 10^{-7}\\text{ m}$:
\\[
\\lambda_L^2 = 5.76 \\times 10^{-14}\\text{ m}^2 \\implies 4\\pi \\lambda_L^2 = 7.2382 \\times 10^{-13}\\text{ m}^2
\\]
\\[
\\ln\\kappa = \\ln(43.64) = 3.7760
\\]
\\[
B_{c1} = \\left( \\frac{2.0678 \\times 10^{-15}}{7.2382 \\times 10^{-13}} \\right) (3.7760) = (2.8568 \\times 10^{-3}\\text{ T})(3.7760) = 0.01079\\text{ T} = 10.8\\text{ mT}
\\]

2. **Thermodynamic Critical Field $B_c$**:
From Ginzburg-Landau theory: $B_{c2} = \\sqrt{2} \\kappa B_c$:
\\[
B_c = \\frac{B_{c2}}{\\sqrt{2}\\kappa} = \\frac{10.88\\text{ T}}{\\sqrt{2}(43.636)} = \\frac{10.88}{61.711} = 0.1763\\text{ T} = 176.3\\text{ mT}
\\]
Comparison: $B_{c1} (10.8\\text{ mT}) \\ll B_c (176\\text{ mT}) \\ll B_{c2} (10.88\\text{ T})$. The broad vortex state spans over $10.8\\text{ T}$, enabling high-field magnet windings.r"""
            },
            {
                "probNumber": "10.8",
                "title": "Thermodynamic Critical Field and Latent Heat in Superconducting Lead",
                "difficulty": "Advanced",
                "statement": "For superconducting lead, the critical temperature is $T_c = 7.19\\text{ K}$ and the zero-temperature critical field is $B_c(0) = 0.0803\\text{ T}$ ($803\\text{ G}$).\\n(a) Compute the critical field $B_c(T)$ at $T = 4.20\\text{ K}$.\\n(b) Using the thermodynamic relation $\\Delta S = -\\frac{V_m}{\\mu_0} B_c \\frac{dB_c}{dT}$, prove that the superconducting transition at $T_c$ in zero field has zero latent heat (second-order phase transition).\\n(c) In an external magnetic field $B = 0.050\\text{ T}$, compute the transition temperature $T$, the entropy discontinuity $\\Delta S$, and the latent heat of transition $L = T \\Delta S$ per mole of lead ($V_m = 1.826 \\times 10^{-5}\\text{ m}^3/\\text{mol}$).",
                "solution": r"""### Step 1: Critical Field at $4.2\\text{ K}$
Using the empirical parabolic formula:
\\[
B_c(T) = B_c(0) \\left[ 1 - \\left(\\frac{T}{T_c}\\right)^2 \\right]
\\]
With $T = 4.20\\text{ K}$ and $T_c = 7.19\\text{ K}$:
\\[
\\left(\\frac{T}{T_c}\\right)^2 = \\left(\\frac{4.20}{7.19}\\right)^2 = (0.58414)^2 = 0.3412
\\]
\\[
B_c(4.2\\text{ K}) = 0.0803\\text{ T} [1 - 0.3412] = 0.0803 \\times 0.6588 = 0.05290\\text{ T} = 52.9\\text{ mT}
\\]

### Step 2: Proof of Second-Order Transition at $T_c$
The derivative of the critical field with respect to temperature is:
\\[
\\frac{dB_c}{dT} = B_c(0) \\left( -\\frac{2T}{T_c^2} \\right) = -\\frac{2 B_c(0) T}{T_c^2}
\\]
The entropy difference between the normal and superconducting states is:
\\[
S_n - S_s = -\\frac{V_m}{\\mu_0} B_c(T) \\frac{dB_c}{dT}
\\]
At $T = T_c$: $B_c(T_c) = 0$.
Therefore:
\\[
S_n(T_c) - S_s(T_c) = -\\frac{V_m}{\\mu_0} (0) \\left(-\\frac{2 B_c(0)}{T_c}\\right) = 0
\\]
Because $\\Delta S = 0$, the latent heat $L = T_c \\Delta S = 0$.
The phase transition in zero magnetic field has no latent heat, confirming it is a **second-order phase transition** (characterized by a discontinuity in heat capacity $\\Delta C_V$).

### Step 3: Transition in Magnetic Field ($B = 0.050\\text{ T}$)
When an external field $B = 0.050\\text{ T}$ is present, transition occurs at temperature $T_{\\text{tr}}$ where $B_c(T_{\\text{tr}}) = B$:
\\[
0.050 = 0.0803 \\left[ 1 - \\left(\\frac{T_{\\text{tr}}}{7.19}\\right)^2 \\right]
\\]
\\[
1 - \\left(\\frac{T_{\\text{tr}}}{7.19}\\right)^2 = \\frac{0.050}{0.0803} = 0.62267
\\]
\\[
\\left(\\frac{T_{\\text{tr}}}{7.19}\\right)^2 = 1 - 0.62267 = 0.37733 \\implies \\frac{T_{\\text{tr}}}{7.19} = 0.61427
\\]
\\[
T_{\\text{tr}} = 7.19 \\times 0.61427 = 4.417\\text{ K}
\\]
Evaluate the slope at $T_{\\text{tr}}$:
\\[
\\frac{dB_c}{dT} = -\\frac{2(0.0803)(4.417)}{(7.19)^2} = -\\frac{0.7093}{51.696} = -0.01372\\text{ T/K}
\\]
Entropy discontinuity per mole:
\\[
\\Delta S_m = S_n - S_s = -\\frac{1.826 \\times 10^{-5}\\text{ m}^3/\\text{mol}}{4\\pi \\times 10^{-7}\\text{ H/m}} (0.050\\text{ T})(-0.01372\\text{ T/K})
\\]
\\[
\\Delta S_m = (14.530\\text{ m}^3/\\text{H}) \\times (6.860 \\times 10^{-4}\\text{ T}^2/\\text{K}) = 0.009968\\text{ J/(mol}\\cdot\\text{K)} = 9.97\\text{ mJ/(mol}\\cdot\\text{K)}
\\]
Latent heat:
\\[
L = T_{\\text{tr}} \\Delta S_m = (4.417\\text{ K})(0.009968\\text{ J/(mol}\\cdot\\text{K)}) = 0.04403\\text{ J/mol} = 44.0\\text{ mJ/mol}
\\]
In a non-zero magnetic field, $L > 0$, making the transition **first-order** with finite latent heat absorption.r"""
            },
            {
                "probNumber": "10.9",
                "title": "Magnetic Flux Quantization in a Ring and Josephson Frequency",
                "difficulty": "Advanced",
                "statement": "A superconducting ring of niobium carries a persistent screening current.\\n(a) Using the single-valuedness of the Ginzburg-Landau macroscopic wavefunction $\\psi = |\\psi|e^{i\\theta}$ around a closed path deep in the bulk (where $\\mathbf{J}_s = \\mathbf{0}$), derive the quantization of magnetic flux $\\Phi = n \\Phi_0$ with $\\Phi_0 = h/(2e)$.\\n(b) Calculate the numerical value of the magnetic flux quantum $\\Phi_0$ in $\\text{Wb}$ and $\\text{T}\\cdot\\mu\\text{m}^2$.\\n(c) In an AC Josephson junction, a constant DC voltage $V_{\\text{DC}} = 10.0\\text{ }\\mu\\text{V}$ is applied across an insulating barrier. Calculate the AC Josephson oscillation frequency $\\nu_J = \\frac{2e V_{\\text{DC}}}{h}$.",
                "solution": r"""### Step 1: Derivation of Flux Quantization
In Ginzburg-Landau theory, the superconducting current density is:
\\[
\\mathbf{J}_s = \\frac{q^* \\hbar}{2 m^* i} (\\psi^* \\nabla \\psi - \\psi \\nabla \\psi^*) - \\frac{(q^*)^2}{m^*} |\\psi|^2 \\mathbf{A}
\\]
Writing $\\psi(\\mathbf{r}) = |\\psi| e^{i \\theta(\\mathbf{r})}$ with $n_s = |\\psi|^2$, $q^* = -2e$, and $m^* = 2m_e$ (Cooper pair):
\\[
\\mathbf{J}_s = \\frac{n_s q^*}{m^*} (\\hbar \\nabla \\theta - q^* \\mathbf{A})
\\]
Rearranging for the phase gradient:
\\[
\\hbar \\nabla \\theta = q^* \\mathbf{A} + \\frac{m^*}{n_s q^*} \\mathbf{J}_s
\\]
Integrate around a closed contour $C$ lying entirely within the interior of the superconducting ring at depth $\\gg \\lambda_L$.
Because the contour is deep in the bulk, $\\mathbf{J}_s = \\mathbf{0}$:
\\[
\\hbar \\oint_C \\nabla \\theta \\cdot d\\mathbf{l} = q^* \\oint_C \\mathbf{A} \\cdot d\\mathbf{l}
\\]
1. For the wavefunction $\\psi$ to be single-valued, the total phase change around a closed loop must be an integer multiple of $2\\pi$:
\\[
\\oint_C \\nabla \\theta \\cdot d\\mathbf{l} = 2\\pi n \\quad (n \\in \\mathbb{Z})
\\]
2. By Stokes' theorem, the line integral of vector potential $\\mathbf{A}$ equals the total magnetic flux $\\Phi$ enclosed by the ring:
\\[
\\oint_C \\mathbf{A} \\cdot d\\mathbf{l} = \\iint_S (\\nabla \\times \\mathbf{A}) \\cdot d\\mathbf{S} = \\iint_S \\mathbf{B} \\cdot d\\mathbf{S} = \\Phi
\\]
Substituting these relations:
\\[
\\hbar (2\\pi n) = q^* \\Phi \\implies h n = (-2e) \\Phi
\\]
Taking the magnitude:
\\[
|\\Phi| = n \\left( \\frac{h}{2e} \\right) = n \\Phi_0
\\]
The factor of $2$ in the denominator directly confirms that the charge carriers are **Cooper pairs** with charge $q^* = 2e$.

### Step 2: Numerical Value of $\Phi_0$
\\[
\\Phi_0 = \\frac{h}{2e} = \\frac{6.62607 \\times 10^{-34}\\text{ J}\\cdot\\text{s}}{2(1.60218 \\times 10^{-19}\\text{ C})} = 2.06783 \\times 10^{-15}\\text{ Wb} = 2.06783 \\times 10^{-15}\\text{ T}\\cdot\\text{m}^2
\\]
Converting to $\\text{T}\\cdot\\mu\\text{m}^2$ ($1\\text{ m}^2 = 10^{12}\\text{ }\\mu\\text{m}^2$):
\\[
\\Phi_0 = 2.06783 \\times 10^{-15} \\times 10^{12} = 2.068 \\times 10^{-3}\\text{ T}\\cdot\\mu\\text{m}^2
\\]

### Step 3: AC Josephson Frequency
Brian Josephson (1962) showed that applying a DC voltage $V$ across a tunnel junction causes the quantum phase difference to evolve linearly in time:
\\[
\\frac{d\\phi}{dt} = \\frac{2e V}{\\hbar}
\\]
The tunneling supercurrent oscillates sinusoidally:
\\[
I(t) = I_c \\sin(\\phi(t)) = I_c \\sin(2\\pi \\nu_J t)
\\]
where the AC Josephson frequency is:
\\[
\\nu_J = \\frac{2e V_{\\text{DC}}}{h} = \\frac{V_{\\text{DC}}}{\\Phi_0}
\\]
Given $V_{\\text{DC}} = 10.0\\text{ }\\mu\\text{V} = 10.0 \\times 10^{-6}\\text{ V}$:
\\[
\\nu_J = \\frac{10.0 \\times 10^{-6}\\text{ V}}{2.06783 \\times 10^{-15}\\text{ V}\\cdot\\text{s}} = 4.836 \\times 10^9\\text{ Hz} = 4.836\\text{ GHz}
\\]
Applying $10\\text{ }\mu\\text{V}$ generates microwave radiation at $4.84\\text{ GHz}$. This exact relation ($K_J = 2e/h = 483.5979\\text{ GHz/mV}$) serves as the international primary standard for the definition of the volt.r"""
            }
        ]
    }
    return u10

if __name__ == '__main__':
    u10 = get_unit_10()
    print("Unit 10 successfully generated:")
    print("Title:", u10["title"])
    print("Sections:", len(u10["sections"]))
    print("Problems:", len(u10["problems"]))
