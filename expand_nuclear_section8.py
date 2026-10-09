# -*- coding: utf-8 -*-
"""
expand_nuclear_section8.py
Injects Section 8 across all 10 units for Nuclear and Radiochemistry (#47),
bringing total sections from 70 to 80.
Strictly Zero Course Numbers or Marks.
"""

def add_section_8_to_units(units):
    sec8_data = {
        1: {
            "id": "sec-1-8",
            "secNumber": "1.8",
            "title": "Historical Radiochemical Metrology & Discovery Anomalies: From Crookes' Spinthariscope to Early Transmutation",
            "content": r"""The initial decades of radioactivity research witnessed the invention of ingenious physical detection devices that revealed the discrete, particulate nature of subatomic phenomena long before electronic pulse amplifiers were conceived.

### William Crookes and the Spinthariscope (1903)
In 1903, Sir William Crookes discovered that when alpha particles from a radium preparation struck a screen coated with phosphorescent zinc sulfide ($\text{ZnS:Cu}$), the emission did not appear as a continuous luminous glow under optical magnification. Instead, viewing the screen through a high-power objective lens revealed thousands of distinct, instantaneous points of scintillating light.

Crookes mounted a needle tipped with a microscopic speck of radium bromide a few millimeters above a $\text{ZnS}$ screen inside a small brass viewing tube with an adjustable focus eyepiece, inventing the **spinthariscope** (from Greek *spintharis*, "spark"). For the first time in human history, scientists could directly observe the macroscopic optical consequence of an **individual single-atom nuclear disintegration**!

Rutherford and Geiger utilized visual scintillation counting on $\text{ZnS}$ screens to count alpha particles individually. Observers sat in pitch darkness for 30 minutes to achieve dark adaptation, then counted flashes through a microscope for intervals of 60 seconds with hand tally counters. Despite physiological eye fatigue, this visual metrology yielded the experimental scattering cross-sections that proved the existence of the atomic nucleus.

### Early Transmutation and the N-14 to O-17 Discovery (1919)
Prior to 1919, radioactivity was observed strictly as an immutable, spontaneous disintegration beyond human intervention. In 1919, Ernest Rutherford announced the first **artificial nuclear transmutation**:
Collimating intense alpha particles from a polonium or bismuth-214 source into a gas-tight chamber filled with pure dry nitrogen gas, Rutherford observed scintillations on a $\text{ZnS}$ detector placed beyond the maximum stopping range of alpha particles in nitrogen ($R_\alpha \approx 7\text{ cm}$). Magnetic deflection proved that these long-range penetrating particles were fast protons ($^1\text{H}$):
$$^{14}_{7}\text{N} + ^{4}_{2}\alpha \longrightarrow [^{18}_{9}\text{F}^*] \longrightarrow ^{17}_{8}\text{O} + ^{1}_{1}p$$
Patrick Blackett (1925) confirmed this historic discovery by photographing 400,000 alpha tracks in an automatic Wilson cloud chamber, capturing eight historic bifurcated "forked tracks" where an alpha track ended abruptly, yielding an ultra-thin long proton track and a short, thick oxygen-17 recoil track.""",
            "simulations": ["sim_nuc_decay_series_bateman"]
        },
        2: {
            "id": "sec-2-8",
            "secNumber": "2.8",
            "title": "Modern Nuclear Structure & Isospin Formalism: Charge Independence & Wigner Supermultiplets",
            "content": r"""In 1932, immediately following Chadwick's discovery of the neutron, Werner Heisenberg proposed that the proton and neutron are not fundamentally distinct particles, but two different charge states of a single underlying physical entity: the **nucleon**.

### The Isospin Vector Formalism
Heisenberg introduced the concept of **isotopic spin** (or **isospin**, denoted by vector $\vec{T}$ or $\vec{I}$), formulating a mathematical analogy with quantum mechanical spin-1/2:
The nucleon possesses total isospin $T = 1/2$. In an abstract three-dimensional "isospace":
- **Proton state**: Third component projection $T_3 = +1/2$ (or $-1/2$ by nuclear convention):
$$|p\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$
- **Neutron state**: Third component projection $T_3 = -1/2$ (or $+1/2$):
$$|n\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

For a nucleus composed of $Z$ protons and $N$ neutrons, the total third isospin component $T_3$ is strictly fixed by its composition:
$$T_3 = \frac{1}{2}(Z - N) = Z - \frac{A}{2}$$
The total isospin quantum number $T$ can take any integer or half-integer value satisfying:
$$|T_3| \le T \le \frac{A}{2}$$

### Charge Symmetry and Charge Independence
High-energy scattering experiments demonstrate that the strong nuclear force obeys two profound symmetries:
1. **Charge Symmetry**: The proton-proton ($p-p$) strong potential equals the neutron-neutron ($n-n$) strong potential in the identical spatial and spin state ($V_{pp} = V_{nn}$).
2. **Charge Independence**: The proton-neutron ($p-n$) strong interaction equals the $p-p$ and $n-n$ interactions in identical $T = 1$ states ($V_{pp} = V_{nn} = V_{pn}|_{T=1}$).

Mathematically, the nuclear Hamiltonian $\hat{H}_{\text{strong}}$ commutes with the total isospin operator:
$$[\hat{H}_{\text{strong}}, \vec{T}] = 0$$
Consequently, states with identical total isospin $T$ but differing projections $T_3$ form an **isobaric multiplet** (or **isospin analog states**) with nearly identical nuclear structure, differing in energy solely due to electromagnetic Coulomb perturbation:
$$\Delta E_{\text{Coulomb}} = \frac{3}{5}\frac{e^2}{4\pi\varepsilon_0 R} \left[ Z_1(Z_1 - 1) - Z_2(Z_2 - 1) \right]$$
Eugene Wigner expanded this into **Wigner Supermultiplet Theory**, classifying nuclear energy levels according to $SU(4)$ symmetry combining space, spin, and isospin degrees of freedom.""",
            "simulations": ["sim_nuc_binding_energy_curve"]
        },
        3: {
            "id": "sec-3-8",
            "secNumber": "3.8",
            "title": "Matrix Exponential & Laplace Transform Methods in Bateman Decay Networks",
            "content": r"""While the classical Bateman equations provide elegant solutions for simple linear chains ($N_1 \to N_2 \to N_3$), real-world nuclear fuel cycles and reactor transmutation networks involve branched, cyclic, and cross-feeding pathways (e.g., $(n, \gamma)$ activation competing with simultaneous beta and alpha decays). For such complex networks, modern nuclear inventory codes (e.g., ORIGEN, CINDER) formulate the problem via **matrix differential equations**.

### Matrix Formulation of Transmutation Chains
Let the column vector $\vec{N}(t) = [N_1(t), N_2(t), \dots, N_k(t)]^T$ denote the time-dependent population inventory of $k$ distinct nuclides. The governing system of coupled first-order differential equations is:
$$\frac{d\vec{N}(t)}{dt} = \mathbf{A} \vec{N}(t)$$
where $\mathbf{A}$ is the $k \times k$ **transition rate matrix** (or burnup matrix):
- Diagonal elements represent the total destruction rate (decay constant plus neutron absorption):
$$A_{ii} = -(\lambda_i + \sigma_{a,i} \Phi)$$
- Off-diagonal elements represent the production rate of nuclide $i$ from precursor $j$:
$$A_{ij} = \lambda_{j \to i} + \sigma_{j \to i} \Phi \quad (i \ne j)$$

### Formal Solution via the Matrix Exponential
The exact analytical solution of this autonomous linear system with initial inventory $\vec{N}(0)$ is:
$$\vec{N}(t) = \exp(\mathbf{A} t) \vec{N}(0)$$
where the matrix exponential is defined by the convergent Taylor series:
$$\exp(\mathbf{A} t) = \mathbf{I} + \mathbf{A} t + \frac{(\mathbf{A} t)^2}{2!} + \frac{(\mathbf{A} t)^3}{3!} + \dots = \sum_{m=0}^\infty \frac{(\mathbf{A} t)^m}{m!}$$

### Numerical Solution via the Chebyshev Rational Approximation Method (CRAM)
Direct Taylor summation of $\exp(\mathbf{A} t)$ suffers from numerical instability when the spectrum of eigenvalues $\lambda_i$ spans dozens of orders of magnitude (from fractions of a second to billions of years).
Modern reactor burnup solvers utilize the **Chebyshev Rational Approximation Method (CRAM)**, approximating $\exp(\mathbf{A} t)$ by a rational function $\hat{r}_k(z) = p_k(z) / q_k(z)$ on the negative real axis:
$$\exp(\mathbf{A} t) \approx \alpha_0 \mathbf{I} + 2 \text{Re}\left( \sum_{j=1}^{k/2} \alpha_j (\mathbf{A} t - \theta_j \mathbf{I})^{-1} \right)$$
where $\alpha_j$ and $\theta_j$ are pre-computed complex poles and residues. CRAM evaluates the complete isotopic inventory of thousands of isotopes across an entire nuclear reactor core in milliseconds with precision exceeding $10^{-14}$!""",
            "simulations": ["sim_nuc_decay_series_bateman"]
        },
        4: {
            "id": "sec-4-8",
            "secNumber": "4.8",
            "title": "Direct Reaction Mechanisms: Optical Model, DWBA & Transfer Spectroscopy",
            "content": r"""At incident projectile energies exceeding $10 - 20\text{ MeV}$, nuclear reactions bypass compound nucleus formation, proceeding via **direct reactions** where the projectile interacts with only one or two valence nucleons during a single transit time ($\tau \sim 10^{-22}\text{ s}$).

### The Optical Model of Elastic Nuclear Scattering
To describe direct elastic scattering and total reaction cross-sections, Herman Feshbach, Charles Porter, and Victor Weisskopf (1954) introduced the **Optical Model**.
The nucleus is treated as a partially transparent, refractive, and absorbing cloudy crystal sphere for projectile matter waves, modeled by a **complex phenomenological potential**:
$$U(r) = V(r) + i W(r)$$
- **Real Part $V(r)$**: Refracts the incoming matter wave, describing elastic scattering. Modeled using a Woods-Saxon volume potential:
$$V(r) = -V_0 f(r, R_v, a_v) \quad \text{where } f(r, R, a) = \frac{1}{1 + \exp\left(\frac{r - R}{a}\right)}$$
- **Imaginary Part $W(r)$**: Absorbs flux from the elastic channel, describing all non-elastic reaction processes (inelastic scattering, capture, transfer, fission):
$$W(r) = -W_v f(r, R_w, a_w) + 4 a_s W_s \frac{d}{dr}f(r, R_s, a_s)$$
- **Spin-Orbit Term $V_{so}(r)$**: Describes polarization and spin-flip scattering:
$$V_{so}(r) = V_{so} \left(\frac{\hbar}{m_\pi c}\right)^2 \frac{1}{r} \frac{df}{dr} (\vec{L} \cdot \vec{S})$$

### The Distorted Wave Born Approximation (DWBA) for Single-Nucleon Transfer
In a transfer reaction such as $(d, p)$ stripping:
$$d + X \longrightarrow p + Y \quad \text{where } Y = X + n$$
The deuteron breaks up; the neutron is captured into an unoccupied single-particle shell-model orbital with orbital angular momentum $l$ and total angular momentum $j$, while the proton escapes.

In the **Distorted Wave Born Approximation (DWBA)**, the transition matrix element is:
$$T_{fi} = \int d^3r_i \int d^3r_f \, \chi_f^{(-)*}(\vec{k}_f, \vec{r}_f) \langle \psi_Y \psi_p | V_{\text{trans}} | \psi_X \psi_d \rangle \chi_i^{(+)}(\vec{k}_i, \vec{r}_i)$$
where $\chi_i$ and $\chi_f$ are distorted waves calculated using Optical Model potentials.
The experimental differential cross-section factorizes into:
$$\left(\frac{d\sigma}{d\Omega}\right)_{\text{exp}} = S_{l j} \cdot \left(\frac{d\sigma}{d\Omega}\right)_{\text{DWBA}}$$
where $S_{l j}$ is the **Spectroscopic Factor**, quantifying the purity of the single-particle configuration in the residual nuclear state. DWBA transfer reactions serve as the primary experimental tool for mapping single-particle energy levels across the chart of nuclides.""",
            "simulations": ["sim_nuc_reaction_cross_section_q"]
        },
        5: {
            "id": "sec-5-8",
            "secNumber": "5.8",
            "title": "Advanced Fission Physics: Ternary Fission, Delayed Precursor Chemistry & Actinide Incineration",
            "content": r"""While binary fission splits a nucleus into two primary fragments, approximately **1 in every 500 thermal fissions** of $^{235}\text{U}$ is a **ternary fission** event in which a third light charged particle (LCP) is emitted simultaneously from the scission neck.

### Ternary Fission Mechanics
- Over $90\%$ of ternary particles are energetic **alpha particles** ($^{4}\text{He}^{2+}$ with kinetic energy $\bar{E} \approx 16\text{ MeV}$).
- Other light particles include tritons ($^3\text{H}$, $\sim 7\%$), deuterons ($^2\text{H}$), and trace lithium, beryllium, and carbon ions ($^8\text{Be}, ^{10}\text{Be}, ^{14}\text{C}$).
- The ternary particle is ejected nearly perpendicular to the fission axis ($90^\circ$) by the intense mutual Coulomb repulsion of the two receding heavy fragments. Ternary fission is the primary source of radioactive **tritium ($^3\text{H}$)** generated inside nuclear fuel rods.

### Precursor Chemistry of Delayed Neutron Emitters
Delayed neutron precursors reside in specific chemical groups within the fission fragment distribution:
1. **Halogen Precursors**: Bromine ($^{87}\text{Br}, ^{88}\text{Br}, ^{89}\text{Br}$) and Iodine ($^{137}\text{I}, ^{138}\text{I}, ^{139}\text{I}$). They possess high beta-decay energies ($Q_\beta \sim 6 - 8\text{ MeV}$) feeding states above the neutron separation energy $S_n$ of the noble gas daughters ($\text{Kr}$ and $\text{Xe}$).
2. **Alkali Precursors**: Rubidium ($^{92}\text{Rb}, ^{93}\text{Rb}$) and Cesium ($^{141}\text{Cs}, ^{142}\text{Cs}$).

### Minor Actinide Partitioning & Transmutation (Actinide Incineration)
In spent nuclear fuel, the dominant long-term radiotoxicity ($>1,000\text{ years}$) arises from **minor actinides**: neptunium ($^{237}\text{Np}$), americium ($^{241}\text{Am}, ^{243}\text{Am}$), and curium ($^{244}\text{Cm}$).
To eliminate multi-millennial geological repository hazards, advanced fuel cycles develop **Partitioning and Transmutation (P&T)**:
1. **Pyrochemical Pyroprocessing**: Spent oxide fuel is reduced to metal in molten lithium chloride-potassium chloride ($\text{LiCl-KCl}$) eutectic salt at $500^\circ\text{C}$ and electrorefined, separating actinides from fission products.
2. **Fast Reactor & Accelerator-Driven System (ADS) Incineration**:
In a fast neutron spectrum, the fission-to-capture cross-section ratio $\sigma_f / \sigma_c$ increases dramatically. Minor actinides are loaded into subcritical fast cores driven by spallation proton accelerators, where fast neutrons fission them into short-lived fission products, reducing waste storage lifespans from **300,000 years to under 300 years**!""",
            "simulations": ["sim_nuc_fission_chain_reactor"]
        },
        6: {
            "id": "sec-6-8",
            "secNumber": "6.8",
            "title": "Microdosimetric Track Structure & Stochastic Energy Deposition: Nanodosimetry of Clustered DNA Lesions",
            "content": r"""Macroscopic dosimetry defines absorbed dose as an average quantity: $D = \Delta E / \Delta m$. However, within microscopic cellular targets (cell nucleus diameter $\sim 5 - 10\,\mu\text{m}$, DNA chromatin fiber diameter $\sim 30\text{ nm}$, DNA double helix diameter $\approx 2.0\text{ nm}$), radiation deposits energy in discrete, highly localized stochastic clusters known as **track structures**.

### Formalism of ICRU Microdosimetry
In 1983, the International Commission on Radiation Units and Measurements (ICRU Report 36) established **microdosimetry** to describe stochastic energy deposition in sub-cellular volumes:
1. **Energy Imparted ($\epsilon$)**: The stochastic sum of all energy transfers within a microscopic volume $V$.
2. **Lineal Energy ($y$)**: The stochastic analogue of linear energy transfer (LET), defined as the energy imparted by a single tracking event divided by the mean chord length $\bar{l}$ of the volume:
$$y \equiv \frac{\epsilon}{\bar{l}} \quad (\text{dimensions: } \text{keV}/\mu\text{m})$$
3. **Specific Energy ($z$)**: The stochastic analogue of absorbed dose:
$$z \equiv \frac{\epsilon}{m} \quad (\text{dimensions: } \text{Gy})$$
As the target mass $m \to \infty$ or the number of independent tracks $n \to \infty$, the expectation value converges to macroscopic dose: $\langle z \rangle = D$.

```
 Low-LET Electron Track: Sparse Ionizations      High-LET Alpha Track: Dense Column
       ●                                                ●●●●●●●●●●●●●●●●●●●●●●●
                  ●                                     ●●●●●●●●●●●●●●●●●●●●●●●
                                                        ●●●●●●●●●●●●●●●●●●●●●●●
                              ●                         (Clustered Damage: >10 DSBs
 (Simple repairable SSB)                                 across single chromatin loop!)
```

### Nanodosimetry and Clustered DNA Lesions (Complex Damage)
Monte Carlo track structure simulations (e.g., GEANT4-DNA, PARTRAC) demonstrate that:
- For low-LET radiation ($0.2\text{ keV}/\mu\text{m}$), ionizations are isolated; over $85\%$ of DNA lesions are isolated single-strand breaks or base damages that cellular repair enzymes fix with $<0.1\%$ error.
- For high-LET radiation ($100\text{ keV}/\mu\text{m}$ alpha particles), a single track traversing a cell nucleus deposits hundreds of ionizations along a continuous cylinder, producing **Clustered DNA Lesions** (Multiple Damaged Sites, MDS): multiple double-strand breaks, base oxidations, and abasic sites all clustered within $1 - 2$ helical turns of DNA. Cellular repair machinery (NHEJ, HR) cannot resolve clustered breaks, resulting in chromosomal fragmentation, genomic instability, and mitotic death.""",
            "simulations": ["sim_nuc_bragg_peak_stopping_power"]
        },
        7: {
            "id": "sec-7-8",
            "secNumber": "7.8",
            "title": "Digital Signal Processing & Pulse Shape Discrimination in Radiation Spectrometry",
            "content": r"""Modern radiation spectroscopy has transitioned from analog shaping amplifiers to high-speed **Digital Signal Processing (DSP)** and digital pulse processors (DPPs).

### Flash ADC Digitization and Digital Trapezoidal Filtering
In digital spectrometers, the continuous exponential charge pulse emerging from a preamplifier ($V(t) = V_0 e^{-t/\tau}$) is digitized directly by a high-speed Flash ADC ($14 - 16\text{ bits}$ at $100 - 500\text{ MSamples/s}$).
The digitized waveform $x[n]$ is shaped in real time using a **Digital Trapezoidal Filter**:
$$y[n] = y[n-1] + (x[n] - x[n-k] - x[n-l] + x[n-k-l]) + M_c \sum_{i=n-k}^{n-1} x[i]$$
where $k$ is the peaking rise time, $l$ is the flat-top duration, and $M_c$ is the pole-zero cancellation constant.
The flat top eliminates pulse ballistic deficit (caused by variations in charge collection time across large HPGe crystals), while the sharp symmetric sides optimize signal-to-noise ratio at count rates exceeding $500,000\text{ cps}$ without peak shift or baseline distortion.

### Pulse Shape Discrimination (PSD) for Neutron-Gamma Separation
Certain scintillation detectors (e.g., stilbene, organic liquid scintillators BC-501A/EJ-301, and dual-mode CLYC) exhibit scintillation decay profiles that depend on the **ionization density of the particle**.
Scintillation light consists of two components:
- **Prompt Fluorescence** ($\tau \sim 2 - 5\text{ ns}$): Arises from radiative decay of excited singlet states ($S_1 \to S_0$).
- **Delayed Phosphorescence** ($\tau \sim 100 - 500\text{ ns}$): Arises from bimolecular annihilation of long-lived triplet states ($T_1 + T_1 \to S_1^* + S_0$).

High-LET particles (such as recoil protons from fast neutron elastic scattering) produce intense ionization density, promoting extensive triplet-triplet collisions and generating a much larger **delayed light component** than low-LET Compton electrons from gamma rays.

Digital spectrometers calculate the **Charge Comparison Discrimination Parameter**:
$$\text{PSD} = \frac{Q_{\text{tail}}}{Q_{\text{total}}} = \frac{\int_{t_{\text{gate}}}^{t_{\text{end}}} V(t) dt}{\int_0^{t_{\text{end}}} V(t) dt}$$
Plotting $\text{PSD}$ versus total energy yields two completely separated 2D branches, achieving real-time discrimination of fast neutrons from gamma backgrounds with Figures of Merit ($\text{FOM} = \Delta \text{Peak} / [\text{FWHM}_1 + \text{FWHM}_2]$) exceeding $2.5$.""",
            "simulations": ["sim_nuc_hpge_gamma_spectroscopy"]
        },
        8: {
            "id": "sec-8-8",
            "secNumber": "8.8",
            "title": "Advanced Radiometric Methods: Epithermal NAA (ENAA), k0-Standardization & Nuclear Forensics Attribution",
            "content": r"""Modern radiochemical analytical science has evolved advanced protocols that extend sensitivity and address national security metrology:

### 1. Epithermal Neutron Activation Analysis (ENAA)
In standard thermal NAA, high-abundance matrix elements with large thermal capture cross-sections (e.g., $^{23}\text{Na}, ^{45}\text{Sc}, ^{59}\text{Co}$) generate intense radioactivity that obscures trace elements.
In **ENAA**, the sample is encapsulated inside a cadmium ($\text{Cd}$, thickness $1.0\text{ mm}$) or boron shield prior to irradiation.
Cadmium possesses an enormous thermal capture cross-section ($\sigma_{\text{th}} \approx 20,000\text{ b}$ for $^{113}\text{Cd}$) that cuts off all neutrons below the **cadmium cutoff energy** ($E_{\text{Cd}} \approx 0.55\text{ eV}$), transmitting only epithermal and resonance neutrons.
The **Resonance Advantage Factor** is:
$$F_{\text{adv}} = \frac{(I_0 / \sigma_{\text{th}})_{\text{analyte}}}{(I_0 / \sigma_{\text{th}})_{\text{matrix}}}$$
where $I_0 = \int_{E_{\text{Cd}}}^\infty \sigma(E) \frac{dE}{E}$ is the resonance capture integral.
For elements with massive resonance capture integrals (e.g., $\text{Au, U, Th, In, As, Sb, Mo}$), ENAA improves signal-to-noise ratios by factors of **$50 - 500$**!

### 2. The $k_0$-Standardization Method
In 1975, Frans De Corte developed the **$k_0$-standardization method** to eliminate the need for multi-element comparative standard solutions.
Every reaction is calibrated relative to a single universal co-irradiated gold flux monitor ($^{197}\text{Au}$):
$$k_{0,\text{Au}}(x) \equiv \frac{M_{\text{Au}} \cdot \theta_x \cdot \sigma_{0,x} \cdot I_{\gamma,x}}{M_x \cdot \theta_{\text{Au}} \cdot \sigma_{0,\text{Au}} \cdot I_{\gamma,\text{Au}}}$$
Because $k_0$ is a composite fundamental nuclear constant independent of experimental reactor parameters, measuring the gold monitor determines the concentration of all 65 detectable elements simultaneously from first principles.

### 3. Nuclear Forensics & Illicit Material Attribution
Nuclear forensics investigates interdicted nuclear materials (e.g., smuggled enriched uranium or plutonium) to trace their origin, reactor type, enrichment technology, and time since purification.
Key signatures:
- **Radiochronometry (Model Age)**: Determining the purification date by measuring daughter-to-parent decay ratios via High-Resolution ICP-MS:
  - For Uranium: $^{230}\text{Th} / ^{234}\text{U}$ and $^{231}\text{Pa} / ^{235}\text{U}$.
  - For Plutonium: $^{241}\text{Am} / ^{241}\text{Pu}$.
- **Trace Elemental & Isotopic Fingerprinting**: Minor uranium isotopes ($^{236}\text{U}$ indicates recycled reprocessed reactor fuel; $^{234}\text{U}$ depletion indicates gaseous diffusion vs centrifuge enrichment) and rare earth element distribution patterns.""",
            "simulations": ["sim_nuc_neutron_activation_analysis"]
        },
        9: {
            "id": "sec-9-8",
            "secNumber": "9.8",
            "title": "Heavy Ion Accelerators & Superheavy Element Synthesis (Z >= 114): Oganesson & the Island of Stability",
            "content": r"""The synthesis of the heaviest transactinide elements ($Z \ge 104$, superheavy elements) tests the fundamental limits of nuclear existence and maps the predicted **Island of Stability** around spherical magic numbers $Z = 114, 120, 126$ and $N = 184$.

### Synthesis Strategies: Cold Versus Hot Fusion
Superheavy elements are synthesized by bombarding heavy targets with high-intensity heavy-ion beams in specialized accelerators (e.g., GSI Helmholtzzentrum in Germany, JINR Flerov Laboratory in Dubna, RIKEN in Japan):

1. **Cold Fusion Reactions (Peter Armbruster & Sigurd Hofmann, GSI)**:
- Target: Doubly magic lead-208 ($^{208}\text{Pb}$) or bismuth-209 ($^{209}\text{Bi}$).
- Projectiles: Medium-mass stable ions ($^{54}\text{Cr}, ^{58}\text{Fe}, ^{64}\text{Ni}, ^{70}\text{Zn}$).
- Characteristics: Low excitation energy of compound nucleus ($E^* \approx 10 - 15\text{ MeV}$). De-excites by boiling off only **one prompt neutron** ($1n$ channel).
- Synthesized elements $Z = 107 - 113$ (Bohrium through Nihonium).
- Limitation: Massive Coulomb barrier repulsion limits cross-sections for $Z \ge 114$ to the sub-picobarn regime ($<10^{-36}\text{ cm}^2$).

2. **Hot Fusion with Calcium-48 Beams (Yuri Oganessian, Dubna)**:
- Projectile: Rare, neutron-rich doubly magic **calcium-48** ($^{48}_{20}\text{Ca}_{28}$, $0.187\%$ natural abundance, cost $\sim \$250,000/\text{g}$).
- Targets: Transuranic actinide targets ($^{238}\text{U}, ^{244}\text{Pu}, ^{243}\text{Am}, ^{248}\text{Cm}, ^{249}\text{Bk}, ^{249}\text{Cf}$).
- Characteristics: The 8 neutron excess of $^{48}\text{Ca}$ forms compound nuclei closer to the predicted $N = 184$ neutron shell closure. Higher excitation energy ($E^* \approx 30 - 40\text{ MeV}$) de-excites via $3n$ and $4n$ evaporation channels.
- Synthesized elements $Z = 114 - 118$:
  - Flerovium ($Z = 114$): $^{244}\text{Pu}(^{48}\text{Ca}, 3n)^{289}\text{Fl}$
  - Moscovium ($Z = 115$): $^{243}\text{Am}(^{48}\text{Ca}, 3n)^{288}\text{Mc}$
  - Livermorium ($Z = 116$): $^{248}\text{Cm}(^{48}\text{Ca}, 4n)^{292}\text{Lv}$
  - Tennessine ($Z = 117$): $^{249}\text{Bk}(^{48}\text{Ca}, 3n)^{294}\text{Ts}$
  - **Oganesson ($Z = 118$)**: $^{249}\text{Cf}(^{48}\text{Ca}, 3n)^{294}\text{Og}$ ($\sigma \approx 0.5\text{ picobarn}$, barely 1 atom synthesized per month of continuous beam irradiation!).

### Chemistry at the Relativistic Limit
At $Z = 118$, intense nuclear charge pulls inner $1s$ electrons to speeds approaching $85\%$ the speed of light ($v/c \approx Z\alpha \approx 118/137 \approx 0.86$).
Relativistic mass increase contracts $s$ and $p_{1/2}$ orbitals while screening the nucleus and expanding $d$ and $f$ orbitals.
Oganesson ($Z = 118$) is predicted to have an electron shell structure so modified by spin-orbit splitting that its valence electrons form a uniform electron gas (Fermi gas), predicting that Oganesson behaves not as a noble gas, but as a **reactive semiconductor solid** at room temperature!""",
            "simulations": ["sim_nuc_generator_99mo_99mtc"]
        },
        10: {
            "id": "sec-10-8",
            "secNumber": "10.8",
            "title": "Operational Health Physics: Internal Bioassay Mathematical Modeling & ALARA Engineering",
            "content": r"""Operational radiation safety transforms fundamental physical principles into engineering practices designed to keep occupational and public doses As Low As Reasonably Achievable (ALARA).

### 1. ICRP Human Respiratory Tract Model (HRTM, ICRP Publication 66 & 130)
Inhaled radioactive aerosols are deposited in respiratory compartments according to aerodynamic diameter ($AMAD$, Activity Median Aerodynamic Diameter, typically $1 - 5\,\mu\text{m}$):
- Extrathoracic airways ($ET_1, ET_2$): Nose, pharynx, larynx.
- Bronchial ($BB$) and bronchiolar ($bb$) tree: Ciliated mucociliary escalator transports particles upward to the esophagus within hours.
- Alveolar-interstitial region ($AI$): Gas-exchange region lacking cilia; clearance is rate-limited by chemical solubility in alveolar macrophages.

Particles are classified by their chemical absorption rate into blood:
- **Type F (Fast)**: $100\%$ absorbed into systemic blood within minutes to hours (e.g., soluble nitrates, fluorides, pertechnetates).
- **Type M (Moderate)**: Half-times of days to weeks (e.g., oxides of uranium, carbonates, cobalt).
- **Type S (Slow)**: Highly insoluble refractory particulates (e.g., high-fired $\text{UO}_2, \text{PuO}_2$) retained in lung tissue and pulmonary lymph nodes for decades ($T_{\text{clearance}} > 7,000\text{ days}$).

### 2. In Vivo and In Vitro Bioassay Monitoring
To monitor occupational internal contamination:
- **In Vivo Whole-Body Counting (WBC)**: The worker sits in a heavily shielded low-background room (pre-WWII steel plate shielding) surrounded by large HPGe or $\text{NaI(Tl)}$ detectors to quantify high-energy gamma emitters ($^{60}\text{Co}, ^{137}\text{Cs}$). Specialized low-energy Germanium (LEGe) lung counters detect the faint $59.5\text{ keV}$ photons of $^{241}\text{Am}$ to assay insoluble plutonium contamination.
- **In Vitro Bioassay**: Radiochemical separation and alpha spectrometry of 24-hour urine and fecal samples to detect sub-picocurie levels of alpha-emitting actinides ($^{239}\text{Pu}, ^{238}\text{U}, ^{232}\text{Th}$).

### 3. ALARA Engineering Controls
In nuclear engineering facility design:
1. **Zoned Ventilation**: Air flows strictly from zones of lowest contamination potential to zones of highest contamination potential (Zone 1: Offices $\to$ Zone 2: Hallways $\to$ Zone 3: Radiation Laboratories $\to$ Zone 4: Hot Cells). Hot cells operate under permanent negative gauge pressure ($-250\text{ Pa}$) to prevent aerosol leakage.
2. **HEPA Filtration**: Exhaust air passes through redundant series of Nuclear-Grade High-Efficiency Particulate Air (HEPA) filters ($99.97\%$ capture efficiency for $0.3\,\mu\text{m}$ particles) and charcoal beds to trap radioiodine vapors.""",
            "simulations": ["sim_nuc_bragg_peak_stopping_power"]
        }
    }

    for unit in units:
        un = unit["unitNumber"]
        if un in sec8_data:
            sec8 = sec8_data[un]
            # check if not already present
            if not any(s["id"] == sec8["id"] for s in unit["sections"]):
                unit["sections"].append(sec8)
    return units
