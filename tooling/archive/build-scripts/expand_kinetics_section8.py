# -*- coding: utf-8 -*-
"""
expand_kinetics_section8.py
Injects Section 8 across all 10 units of Molecular Motion and Reaction Kinetics.
Brings total sections from 70 to 80 (exactly 8 per unit).
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def inject_section_8(units):
    sec8_dict = {
        "unit-1": {
            "id": "sec-1-8",
            "secNumber": "1.8",
            "title": "Knudsen Effusion Mass Spectrometry & Supersonic Molecular Beam Aerodynamics",
            "content": r"""Effusion phenomena and free-jet gas expansions provide the experimental foundation for modern gas-phase reaction dynamics, molecular beam spectroscopy, and high-temperature vaporization thermodynamics.

### 1. Knudsen Effusion Mass Spectrometry (KEMS)
Knudsen Effusion Mass Spectrometry (developed by Inghram, Chupka, and Drowart) is the primary metrological method for measuring vapor pressures of refractory materials and determining dissociation energies of high-temperature gaseous species ($D_0^\circ$).

A sample is placed inside a sealed Knudsen cell (made of chemically inert tungsten, molybdenum, or alumina) maintained at temperature $T$ inside an ultra-high vacuum chamber ($P_{\text{chamber}} < 10^{-7}\text{ Torr}$). Vapor molecules escape through an ideal circular orifice of area $A_0$ having knife-edge walls ($L_w \ll d_{\text{hole}}$). The Knudsen number satisfies:
$$\text{Kn} = \frac{\lambda}{d_{\text{hole}}} > 10$$
ensuring that molecular collisions within the orifice are negligible and thermodynamic vapor-liquid/solid equilibrium inside the cell is undisturbed.

The molecular effusion beam is ionized by an electron impact source ($e^- + M \longrightarrow M^{+\bullet} + 2 e^-$) or tunable synchrotron VUV radiation, and ion intensities $I_i^+$ are measured by a quadrupole or time-of-flight mass spectrometer. The partial vapor pressure $P_i$ inside the cell is related to ion intensity by the fundamental KEMS formula:
$$P_i = \frac{k_{\text{cal}} \cdot I_i^+ \cdot T}{\sigma_i \cdot \gamma_i}$$
where $k_{\text{cal}}$ is an instrumental calibration constant (determined from silver or gold vapor standards), $\sigma_i$ is the electron impact ionization cross-section, and $\gamma_i$ is detector multiplier gain.

By recording $P_i(T)$ over temperature, the standard enthalpy of vaporization $\Delta_{\text{vap}} H^\circ$ is extracted from the Clausius-Clapeyron relation:
$$\frac{d \ln P_i}{d (1/T)} = -\frac{\Delta_{\text{vap}} H^\circ}{R}$$

### 2. Supersonic Free-Jet Aerodynamic Expansion
In contrast to effusive beams where particles exit independently without collisions, a **supersonic free jet** is created by expanding a high-pressure carrier gas ($P_0 = 1 - 50\text{ bar}$, typically He or Ar) through a tiny pinhole nozzle ($d = 50 - 200\;\mu\text{m}$) into high vacuum.

Within the first few nozzle diameters downstream of the orifice, molecules undergo tens of thousands of binary collisions. In this continuum hydrodynamic expansion zone:
- Random thermal kinetic energy is converted into directed, uniform forward velocity $u$.
- The local Mach number exceeds unity ($M = u / a > 1$).
- The velocity distribution narrows dramatically, collapsing the translational temperature $T_{\text{trans}}$ to cryogenic values ($T_{\text{trans}} < 1 - 5\text{ K}$).

#### Cooling Dynamics & Non-Equilibrium Freezing
Because collision rates scale with density ($Z \propto n$), the collision frequency drops precipitously as the gas expands, causing different molecular degrees of freedom to decouple at distinct downstream locations ("freezing"):
$$T_{\text{trans}} < T_{\text{rot}} \ll T_{\text{vib}} \ll T_0$$
1. **Translational Cooling**: Energy transfer between translational modes occurs in $1 - 2$ collisions; temperatures drop to $0.5 - 2\text{ K}$.
2. **Rotational Cooling**: Rotational-translational ($R-T$) relaxation requires $\sim 10 - 20$ collisions; rotational temperatures reach $2 - 10\text{ K}$, simplifying complex rovibrational spectra into isolated ground-state lines.
3. **Vibrational Freezing**: Vibrational-translational ($V-T$) relaxation requires $10^4 - 10^6$ collisions. Because density drops before sufficient collisions occur, vibrational cooling freezes early at $T_{\text{vib}} \approx 50 - 150\text{ K}$.

A conical skimmer extracts the central core of the supersonic jet, forming a pristine, collision-free molecular beam with narrow velocity dispersion ($\Delta v / v < 1\%$)."""
        },

        "unit-2": {
            "id": "sec-2-8",
            "secNumber": "2.8",
            "title": "Electrochemical Impedance Spectroscopy, Walden Rule & Superionic Glass Conductance",
            "content": r"""Understanding ionic transport in advanced electrolyte systems—ranging from lithium-ion battery non-aqueous solvents to room-temperature ionic liquids (RTILs) and solid superionic conductors—requires sophisticated electrodynamic relaxation techniques and generalized transport laws.

### 1. Electrochemical Impedance Spectroscopy (EIS) of Electrolytic Cells
When a small sinusoidal AC potential perturbation $\tilde{V}(\omega) = V_0 \sin(\omega t)$ is applied across an electrolytic conductance cell, the resulting AC current response exhibits a frequency-dependent amplitude and phase shift: $\tilde{I}(\omega) = I_0 \sin(\omega t + \phi)$. The complex impedance is:
$$Z(\omega) = \frac{\tilde{V}(\omega)}{\tilde{I}(\omega)} = Z'(\omega) + i Z''(\omega) = |Z| e^{i \phi}$$

#### Equivalent Circuit Modeling (Randles Circuit)
An electrolytic cell is modeled by equivalent electrical circuit networks:
1. **High-Frequency Intercept ($\omega \to \infty$)**: The capacitive double layer at the electrode-electrolyte interface shorts out ($Z_{C_{\text{dl}}} \to 0$). The real axis intercept on the Nyquist plot ($-Z''$ vs $Z'$) yields pure bulk electrolyte solution resistance:
   $$Z'(\infty) = R_{\text{sol}} = \frac{1}{\kappa} \frac{l}{A}$$
   from which absolute electrolytic conductivity $\kappa$ is measured without electrode polarization artifacts.
2. **Intermediate Frequencies**: Charge transfer resistance $R_{\text{ct}}$ in parallel with double-layer capacitance $C_{\text{dl}}$ produces a characteristic semicircular relaxation arc with peak frequency:
   $$\omega_{\text{max}} = \frac{1}{R_{\text{ct}} C_{\text{dl}}}$$
3. **Low-Frequency Warburg Tail ($\omega \to 0$)**: Semi-infinite linear diffusion of ions to electrode surfaces creates the Warburg impedance with $45^\circ$ slope:
   $$Z_W(\omega) = \sigma_W \omega^{-1/2} (1 - i)$$

### 2. The Walden Rule & Ionicity in Room-Temperature Ionic Liquids
Walden (1906) observed an empirical inverse relationship between equivalent conductivity $\Lambda$ and solvent macroscopic dynamic viscosity $\eta$:
$$\Lambda \cdot \eta = \text{constant} \quad (\text{Walden Product})$$

From Stokes' law for ionic hydrodynamic mobility:
$$u_i = \frac{z_i e}{6 \pi \eta r_{\text{hyd}, i}} \implies \lambda_i = F u_i = \frac{z_i e F}{6 \pi \eta r_{\text{hyd}, i}}$$
Summing over cations and anions gives:
$$\Lambda_0 \eta = \frac{F^2 e}{6 \pi} \left( \frac{z_+}{r_{\text{hyd}, +}} + \frac{z_-}{r_{\text{hyd}, -}} \right)$$
If hydrodynamic solvation radii are independent of solvent viscosity, the product $\Lambda_0 \eta$ remains constant across varied solvents and temperatures.

#### Walden Plot Classification of RTILs
Plotting $\log_{10} \Lambda$ vs $\log_{10}(1/\eta)$ establishes an "ideal line" corresponding to fully dissociated dilute aqueous potassium chloride ($KCl$).
- **"Good" Ionic Liquids**: Fall close to or directly on the ideal Walden line, indicating complete ion dissociation into independent charge-carrying mobile cations and anions ($[\text{BMIM}]^+[\text{PF}_6]^-$).
- **"Poor" Ionic Liquids**: Fall significantly below the ideal line (by $1 - 2$ logarithmic units), revealing severe ion pairing, neutral dipolar clustering ($[A^+ B^-]^0$), and reduced molar ionicity.

### 3. Solid Superionic Conductors (Fast Ion Conductors)
Certain crystalline solids (e.g., $\alpha\text{-AgI}$, $\text{Li}_{10}\text{GeP}_2\text{S}_{12}$, $\text{Na}_3\text{Zr}_2\text{Si}_2\text{PO}_{12}$ NASICON) exhibit liquid-like ionic conductivities ($\kappa > 10^{-2}\text{ S/cm}$) at room temperature, while remaining electronic insulators.
- **Structural Basis**: An open, rigid sublattice of polarizable framework anions ($I^-$, $S^{2-}$) contains interconnected interstitial polyhedral voids through which mobile cations ($\text{Ag}^+$, $\text{Li}^+$) hop with activation energy $E_a < 0.2\text{ eV}$.
- **Nernst-Einstein hopping conductivity**:
  $$\kappa = \frac{n q^2 a^2 \nu_0}{6 k_B T} \exp\left(-\frac{E_a}{k_B T}\right)$$
  where $a$ is jump distance and $\nu_0$ is the attempt phonon frequency."""
        },

        "unit-3": {
            "id": "sec-3-8",
            "secNumber": "3.8",
            "title": "Pulsed-Field-Gradient NMR Diffusion Metrology & Dynamic Light Scattering",
            "content": r"""Measuring self-diffusion coefficients $D$ non-invasively at molecular and macromolecular length scales is accomplished using nuclear spin-phase tagging via Pulsed-Field-Gradient NMR (PFG-NMR) and intensity autocorrelation analysis via Dynamic Light Scattering (DLS).

### 1. Pulsed-Field-Gradient NMR (Stejskal-Tanner Diffusion Metrology)
Pulsed-Field-Gradient Spin-Echo (PGSE) NMR, introduced by E.O. Stejskal and J.E. Tanner (1965), measures self-diffusion by applying pulsed spatial magnetic field gradients $g(z)$ along the static magnetic field axis $B_0$.

#### The PGSE Pulse Sequence
1. A $90^\circ$ radiofrequency pulse flips macroscopic magnetization into the transverse $x-y$ plane.
2. A pulsed gradient of amplitude $g$ and duration $\delta$ is applied. Nuclei at spatial position $z_1$ precess at local Larmor frequency $\omega(z_1) = \gamma (B_0 + g z_1)$, acquiring a spatially dependent phase angle:
   $$\phi_1 = \gamma B_0 t_1 + \gamma g z_1 \delta$$
3. A $180^\circ$ inversion pulse at time $\tau$ inverts spin phases: $\phi \to -\phi$.
4. After a diffusion delay $\Delta$, a second gradient pulse of identical magnitude $g$ and duration $\delta$ is applied. If molecules moved to new position $z_2$ via Brownian diffusion during interval $\Delta$, the re-phasing is incomplete:
   $$\Delta \phi = \gamma g \delta (z_2 - z_1)$$

#### The Stejskal-Tanner Attenuation Formula
Averaging over the 1D Gaussian displacement probability distribution $P(z_2 - z_1, \Delta) = \frac{1}{\sqrt{4 \pi D \Delta}} \exp\left(-\frac{(z_2 - z_1)^2}{4 D \Delta}\right)$, the attenuated NMR echo intensity $I(g)$ is:
$$\ln\left(\frac{I(g)}{I_0}\right) = -\gamma^2 g^2 \delta^2 \left(\Delta - \frac{\delta}{3}\right) D$$
where:
- $\gamma$ is the nuclear gyromagnetic ratio ($2.675 \times 10^8\text{ rad}/(\text{s}\cdot\text{T})$ for $^1H$).
- The correction $-\delta/3$ accounts for Brownian diffusion occurring during the finite duration of the gradient pulses.
Plotting $\ln(I/I_0)$ against the Stejskal-Tanner parameter $b = \gamma^2 g^2 \delta^2 (\Delta - \delta/3)$ produces a linear slope equal to $-D$. PFG-NMR measures diffusion coefficients from $10^{-9}\text{ m}^2/\text{s}$ (small molecules) down to $10^{-14}\text{ m}^2/\text{s}$ (polymers, lipid bilayers, confined porous media).

### 2. Dynamic Light Scattering (Photon Correlation Spectroscopy)
Dynamic Light Scattering (DLS) measures the Brownian translational diffusion coefficient of colloidal nanoparticles, micelles, and globular proteins suspended in liquid.

#### Temporal Intensity Autocorrelation
A monochromatic laser beam ($\lambda_0$) illuminates a dilute colloidal suspension. The scattered light intensity $I(t)$ collected at angle $\theta$ fluctuates randomly due to constructive and destructive interference caused by Brownian motion of scattering centers.
The normalized second-order temporal intensity autocorrelation function $g^{(2)}(\tau)$ is:
$$g^{(2)}(\tau) = \frac{\langle I(t) I(t + \tau) \rangle}{\langle I(t) \rangle^2}$$

By the Siegert relation for Gaussian optical fields:
$$g^{(2)}(\tau) = 1 + \beta |g^{(1)}(\tau)|^2$$
where $\beta \le 1$ is an optical coherence factor, and $g^{(1)}(\tau)$ is the normalized electric field autocorrelation function. For monodisperse spheres:
$$g^{(1)}(\tau) = \exp(-\Gamma \tau)$$
where the decay rate $\Gamma$ is directly proportional to the translational diffusion coefficient $D$:
$$\Gamma = D q^2$$
and $q$ is the magnitude of the scattering wave vector:
$$q = \frac{4 \pi n}{\lambda_0} \sin\left(\frac{\theta}{2}\right)$$

#### Hydrodynamic Size Extraction
Measuring $\Gamma$ as a function of $q^2$ yields the mutual diffusion coefficient $D = \Gamma / q^2$. Using the Stokes-Einstein equation, the hydrodynamic radius $R_h$ is directly obtained:
$$R_h = \frac{k_B T}{6 \pi \eta D}$$"""
        },

        "unit-4": {
            "id": "sec-4-8",
            "secNumber": "4.8",
            "title": "Operando Reaction Calorimetry & Online Flow-Spectroscopy for Real-Time Rate Tracking",
            "content": r"""Determining multi-step kinetic rate laws in modern organic synthesis and industrial process development relies on continuous, in situ physical property tracking using operando reaction calorimetry and continuous-flow spectroscopy.

### 1. In Situ Heat-Flow Reaction Calorimetry
Because virtually all chemical transformations exhibit a non-zero enthalpy of reaction ($\Delta_r H \ne 0$), the instantaneous rate of heat generation $q_r(t)$ in a closed or flow reactor is directly proportional to the instantaneous chemical reaction rate $r(t) = -d[A]/dt$:
$$q_r(t) = V_{\text{rxn}} \cdot (-\Delta_r H) \cdot r(t)$$

#### Dynamic Heat Balance in a Controlled Reactor
In an automated heat-flow reaction calorimeter (such as an RC1 or Omnical system), a thermostat jacket maintains reactor temperature $T_r$ under isothermal control. The heat balance equation is:
$$q_{\text{flow}}(t) = U A (T_r(t) - T_j(t)) = q_r(t) + q_{\text{stir}} + q_{\text{loss}} - C_p \frac{dT_r}{dt}$$
where:
- $U$ is overall heat transfer coefficient ($\text{W}/(\text{m}^2\cdot\text{K})$).
- $A$ is wetted heat exchange area ($\text{m}^2$).
- $T_j$ is cooling/heating jacket temperature.
- $q_{\text{stir}}$ is mechanical agitator power dissipation.
- $C_p$ is total heat capacity of the reactor assembly and liquid contents.

Under true isothermal steady conditions ($dT_r/dt = 0$), calibration pulses determine the instantaneous heat transfer product $U A$. Subtracting baseline power yields direct, millisecond-resolved chemical heat release rates $q_r(t)$ without withdrawing samples or perturbing chemical equilibria.

#### Reaction Progress Kinetic Analysis (RPKA) via Calorimetry
Integrating heat release from time $t = 0$ to completion ($t = \infty$) yields total chemical enthalpy release:
$$Q_{\text{tot}} = \int_0^\infty q_r(t) dt = V_{\text{rxn}} \cdot (-\Delta_r H) \cdot [A]_0$$
The instantaneous fractional conversion $\chi(t)$ and reactant concentration $[A](t)$ are given by:
$$\chi(t) = \frac{\int_0^t q_r(t') dt'}{Q_{\text{tot}}} \implies [A](t) = [A]_0 (1 - \chi(t))$$
Plotting instantaneous reaction rate $r(t) = q_r(t) / (V (-\Delta_r H))$ directly against concentration $[A](t)$ generates "graphical rate equations" that reveal reaction orders, catalyst deactivation, and product inhibition in a single experiment.

### 2. Online UV-Vis / FTIR Attenuated Total Reflectance (ATR) Spectroscopy
In situ ATR-FTIR utilizes a zinc selenide ($\text{ZnSe}$) or diamond internal reflection element placed inside the reaction medium. An infrared beam undergoes multiple total internal reflections at the crystal-solution interface, generating an evanescent wave that penetrates $1 - 3\;\mu\text{m}$ into the solution.

By Beer-Lambert's law for evanescent absorption:
$$A_i(\nu, t) = \epsilon_i(\nu) \cdot d_p(\nu) \cdot N_{\text{refl}} \cdot [C_i](t)$$
where $d_p = \frac{\lambda}{2 \pi \sqrt{n_{\text{crystal}}^2 \sin^2 \theta - n_{\text{sol}}^2}}$ is penetration depth.
Fourier transform deconvolution generates complete concentration profiles $[C_i](t)$ for reactants, transient reactive intermediates, and products with sub-second temporal resolution."""
        },

        "unit-5": {
            "id": "sec-5-8",
            "secNumber": "5.8",
            "title": "High-Pressure Arrhenius Activation Volumes & Isokinetic Enthalpy-Entropy Compensation",
            "content": r"""Investigating reaction dynamics under extreme hydrostatic pressures and across broad temperature ranges allows dissection of Transition State volumes, solvation rearrangements, and the physical reality of isokinetic relationships.

### 1. High-Pressure Chemical Kinetics & Activation Volume ($\Delta V^\ddagger$)
Hydrostatic pressure $P$ alters chemical equilibrium and reaction rate constants through mechanical work terms $P \Delta V$. From transition state thermodynamics:
$$\left(\frac{\partial \ln k}{\partial P}\right)_T = -\frac{\Delta V^\ddagger}{R T}$$
where $\Delta V^\ddagger = V^\ddagger - V_R$ is the **volume of activation**, representing the difference in partial molar volume between the Transition State and the reactant state.

#### Structural and Solvational Components of $\Delta V^\ddagger$
The activation volume decomposes into two distinct physical contributions:
$$\Delta V^\ddagger = \Delta V_{\text{intr}}^\ddagger + \Delta V_{\text{solv}}^\ddagger$$
1. **Intrinsic Volume Change ($\Delta V_{\text{intr}}^\ddagger$)**:
   - For bond cleavage (dissociative mechanisms, unimolecular homolysis, $S_N1$): Bonds stretch to form the transition state, resulting in a volume expansion: $\Delta V_{\text{intr}}^\ddagger > 0$ ($+5 \text{ to } +20\text{ cm}^3/\text{mol}$).
   - For bond formation (associative mechanisms, cycloadditions, $S_N2$): Molecules come together to form new covalent bonds, resulting in volume contraction: $\Delta V_{\text{intr}}^\ddagger < 0$ ($-10 \text{ to } -35\text{ cm}^3/\text{mol}$). In Diels-Alder reactions, $\Delta V^\ddagger \approx -30 \text{ to } -45\text{ cm}^3/\text{mol}$, causing dramatic rate accelerations ($> 1000\times$) at $P = 10\text{ kbar}$ ($1\text{ GPa}$).
2. **Solvational Volume Change ($\Delta V_{\text{solv}}^\ddagger$, Electrostriction)**:
   - When neutral reactants develop charge in the transition state (e.g., Menshutkin reaction: $R_3N + R'X \longrightarrow [R_3N^{\delta+}\cdots R'\cdots X^{\delta-}]^\ddagger$): Intense electric fields orient and pack dipolar solvent molecules tightly around developing charges. This electrostriction effect causes huge contraction: $\Delta V_{\text{solv}}^\ddagger \approx -20 \text{ to } -50\text{ cm}^3/\text{mol}$, accelerating the reaction under pressure.

### 2. Enthalpy-Entropy Compensation & The Isokinetic Temperature
When kinetic parameters are measured across a series of homologous reactions (varying catalyst ligands, substituents, or solvent mixtures), a linear correlation between activation enthalpy $\Delta H^\ddagger$ and activation entropy $\Delta S^\ddagger$ is frequently observed:
$$\Delta H^\ddagger = \beta \cdot \Delta S^\ddagger + \Delta G_0^\ddagger$$
where $\beta$ is known as the **isokinetic temperature** (or isoequilibrium temperature).

#### Physical Reality vs. Statistical Artifact (Exner Analysis)
At $T = \beta$:
$$\Delta G^\ddagger = \Delta H^\ddagger - \beta \Delta S^\ddagger = \Delta G_0^\ddagger = \text{constant}$$
All reactions in the series are predicted to proceed at precisely identical rates at temperature $\beta$.
However, because $\Delta H^\ddagger$ and $\Delta S^\ddagger$ are mathematically derived from the slope and intercept of the same Arrhenius/Eyring plot ($\ln(k/T)$ vs $1/T$), experimental errors in the slope propagate directly into the intercept, generating an apparent linear compensation artifact:
$$\delta(\Delta S^\ddagger) = \frac{\delta(\Delta H^\ddagger)}{T_{\text{mean}}}$$
O. Exner demonstrated that genuine physical isokinetic behavior must be verified by plotting rate constants measured at two distinct temperatures directly against each other:
$$\ln k(T_2) = a + b \ln k(T_1)$$
If the slope $b \ne 1$ and $b \ne T_1/T_2$ with statistical significance, a true common transition-state mechanism with identical solvation reorganization coordinates exists, and the true isokinetic temperature is calculated from:
$$\beta = T_1 T_2 \frac{b - 1}{b T_1 - T_2}$$"""
        },

        "unit-6": {
            "id": "sec-6-8",
            "secNumber": "6.8",
            "title": "Femtosecond Coherent Anti-Stokes Raman Scattering (CARS) & Ultra-Fast KIE Metrology",
            "content": r"""Probing transient reaction intermediates with lifetimes spanning picoseconds to femtoseconds requires non-linear optical four-wave mixing and ultra-fast kinetic isotope spectroscopy.

### 1. Coherent Anti-Stokes Raman Scattering (CARS) Metrology
Conventional spontaneous Raman scattering suffers from weak scattering cross-sections ($\sim 10^{-30}\text{ cm}^2/\text{sr}$) and overwhelming background fluorescence interference. Coherent Anti-Stokes Raman Scattering (CARS) is a non-linear third-order optical process ($\chi^{(3)}$) that produces high-intensity, coherent, laser-like anti-Stokes emission.

#### Principle of Four-Wave Mixing
Three synchronized laser beams interact within the reactive chemical sample:
1. A pump beam at frequency $\omega_p$.
2. A Stokes beam at frequency $\omega_s$.
3. A probe beam at frequency $\omega_{pr}$ (often $\omega_{pr} = \omega_p$).

When the frequency difference $\omega_p - \omega_s$ matches a vibrational Raman transition $\Omega_{\text{vib}}$ of a specific molecular bond in a reaction intermediate:
$$\omega_p - \omega_s = \Omega_{\text{vib}}$$
molecular vibrations throughout the focal volume are coherently driven in phase. The probe beam scatters off this coherent vibrational macroscopic polarization, emitting a blue-shifted anti-Stokes signal at frequency:
$$\omega_{aS} = \omega_p - \omega_s + \omega_{pr} = 2 \omega_p - \omega_s$$

#### Advantages in Fast Reaction Kinetics
- **Directional Coherent Emission**: The anti-Stokes beam exits in a narrow forward cone determined by the phase-matching wavevector condition $\vec{k}_{aS} = 2\vec{k}_p - \vec{k}_s$, allowing spatial isolation from isotropic background fluorescence.
- **Sub-Picosecond Time Resolution**: Femtosecond CARS tracks structural evolution of reactive intermediates during bond rupture, solvent cage recombination, and cis-trans photoisomerization with vibrational bond selectivity.

### 2. Time-Resolved and Competitive Kinetic Isotope Effects
Kinetic isotope effects (KIE) provide quantitative information regarding transition-state bond geometry. Modern instrumentation utilizes two primary experimental strategies:

#### Internal Competitive Multi-Isotope Ratios via IRMS
In competitive KIE experiments, an unlabelled substrate ($R\text{-H}$) and an isotopically labelled substrate ($R\text{-D}$ or $^{13}C$-labelled) are mixed in a single reaction vessel:
- Fractionation of isotopes in remaining reactant or forming product is monitored as a function of fractional conversion $F$ using High-Precision Isotope Ratio Mass Spectrometry (IRMS) or Multi-Nuclear Quantitative NMR.
- The KIE is calculated via the Bigeleisen-Goering formula:
  $$\text{KIE} = \frac{k_L}{k_H} = \frac{\ln(1 - F)}{\ln\left(1 - F \frac{R_p}{R_0}\right)}$$
  where $R_0$ is initial isotope ratio and $R_p$ is product isotope ratio. This eliminates experimental errors arising from temperature drifts, pipetting variations, or catalyst weighing.

#### Tunneling Signatures in Temperature-Dependent KIE
Measuring KIE over extended temperature ranges ($150 - 350\text{ K}$) distinguishes semiclassical zero-point energy shifts from quantum mechanical nuclear tunneling:
1. **Semiclassical Regime**:
   $$\frac{A_H}{A_D} \approx 0.7 - 1.2, \quad \Delta E_a = E_{a, D} - E_{a, H} \le 5.0\text{ kJ/mol}$$
2. **Extensive Tunneling Regime (Bell/Marcus Model)**:
   $$\frac{A_H}{A_D} \ll 0.1 \quad (\text{often } 10^{-2} - 10^{-4}), \quad \Delta E_a > 10 - 25\text{ kJ/mol}$$
   The rate of hydrogen transfer becomes nearly temperature-independent at cryogenic temperatures, confirming deep quantum under-barrier passage."""
        },

        "unit-7": {
            "id": "sec-7-8",
            "secNumber": "7.8",
            "title": "Cavity Ring-Down Spectroscopy (CRDS) & Fluorescence Correlation Spectroscopy",
            "content": r"""Measuring trace reactive free radicals in the gas phase and single-molecule unimolecular folding conformational kinetics in liquid environments requires extreme optical sensitivities.

### 1. Cavity Ring-Down Spectroscopy (CRDS) for Gas-Phase Kinetics
Conventional absorption spectroscopy governed by the Beer-Lambert law ($I = I_0 e^{-\alpha l}$) is limited to absorbance changes $\Delta A > 10^{-3}$ due to laser amplitude noise. Cavity Ring-Down Spectroscopy (CRDS), invented by Anthony O'Keefe and David Deacon (1988), converts absorption measurements from intensity attenuation into **photon decay time** in high-finesse optical resonators.

#### Principle of Ring-Down Decay
A high-finesse optical cavity consists of two ultra-high reflectivity mirrors ($R > 0.99995$) separated by distance $L$ (typically $0.5 - 1.0\text{ m}$).
1. A pulsed laser fires into the cavity through the front mirror. Light bounces back and forth thousands of times, creating an effective optical path length:
   $$l_{\text{eff}} = \frac{L}{1 - R} = \frac{0.5\text{ m}}{1 - 0.99995} = 10,000\text{ m} = 10\text{ km}$$
2. A fast photodetector behind the rear mirror measures exponential leakage of stored optical power. In an empty cavity (no absorbing analyte):
   $$I(t) = I_0 \exp\left(-\frac{t}{\tau_0}\right), \quad \tau_0 = \frac{L}{c (1 - R)}$$
3. When reactive transient radicals (e.g., $OH$, $CH_3$, $HO_2$, $NO_3$) are generated inside the cavity by laser photolysis, the ring-down time shortens to $\tau$:
   $$I(t) = I_0 \exp\left(-\frac{t}{\tau}\right), \quad \tau = \frac{L}{c \left[ (1 - R) + \sigma(\nu) N L \right]}$$

#### Extraction of Absolute Radical Concentrations
Subtracting the reciprocal ring-down times yields absolute per-pass absorbance without calibration standards:
$$\alpha(\nu) = \sigma(\nu) N = \frac{1}{c} \left( \frac{1}{\tau} - \frac{1}{\tau_0} \right)$$
Because $\tau$ is measured in the time domain, fluctuations in laser pulse energy do not introduce noise. Sensitivities reach absorption coefficients $\alpha_{\text{min}} < 10^{-11}\text{ cm}^{-1}$, detecting radical intermediates at sub-picomolar concentrations.

### 2. Fluorescence Correlation Spectroscopy (FCS)
Fluorescence Correlation Spectroscopy (FCS), introduced by Magde, Elson, and Webb (1972), measures spontaneous thermodynamic equilibrium fluctuations of single fluorescent molecules diffusing into and out of an open diffraction-limited confocal observation volume ($V_0 \approx 0.2 - 1.0\text{ fL} = 10^{-15}\text{ L}$).

#### Temporal Autocorrelation of Fluorescence Fluctuations
A high numerical aperture microscope objective focuses laser light to a sub-micron diffraction spot. The fluorescence intensity fluctuation is $\delta F(t) = F(t) - \langle F \rangle$.
The normalized temporal autocorrelation function is:
$$G(\tau) = \frac{\langle \delta F(t) \cdot \delta F(t + \tau) \rangle}{\langle F \rangle^2}$$

For a molecule undergoing 3D Brownian diffusion coupled to unimolecular two-state conformational switching ($A \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} B$, e.g., protein folding or fluorophore blinking between bright state $A$ and dark state $B$):
$$G(\tau) = \frac{1}{\langle N \rangle} \left( 1 + \frac{\tau}{\tau_D} \right)^{-1} \left( 1 + \frac{\tau}{S^2 \tau_D} \right)^{-1/2} \left[ 1 + K_{\text{conf}} \exp\left(-\frac{\tau}{\tau_{\text{conf}}}\right) \right]$$
where:
- $\langle N \rangle$ is the average number of fluorescent molecules within the confocal volume ($\langle N \rangle = C V_0 N_A$). At $\tau = 0$, $G(0) = 1 / \langle N \rangle$, directly measuring absolute concentration.
- $\tau_D = \frac{w_{xy}^2}{4 D}$ is the characteristic translational diffusion transit time across beam waist $w_{xy}$.
- $\tau_{\text{conf}} = \frac{1}{k_1 + k_{-1}}$ is the unimolecular conformational relaxation time.
FCS resolves both diffusion coefficients and unimolecular conformational kinetic rate constants in real time at nanomolar concentrations."""
        },

        "unit-8": {
            "id": "sec-8-8",
            "secNumber": "8.8",
            "title": "Synchrotron VUV Photoionization Mass Spectrometry (SVUV-PIMS) in Combustion",
            "content": r"""Elucidating the intricate multi-step branching radical networks of hydrocarbon combustion and atmospheric ozone depletion requires isomeric identification of transient radicals and reactive peroxide intermediates.

### 1. The Challenge of Isomer Differentiation in Complex Radical Chains
In high-temperature oxidation of hydrocarbons ($RH + O_2$), dozens of isomeric radical intermediates with identical molecular weights coexist (e.g., resonance-stabilized propenyl vs. allyl radicals, $C_3H_5$, $m/z = 41$; cyclic QOOH vs. peroxy radicals). Conventional electron impact mass spectrometry ($70\text{ eV}$) causes extensive fragmentation, obscuring parent ion identities and destroying fragile organic peroxides ($ROOH$, $OOQOOH$).

### 2. Synchrotron Vacuum Ultraviolet Photoionization Mass Spectrometry (SVUV-PIMS)
Synchrotron Vacuum Ultraviolet Photoionization Mass Spectrometry couples laminar flow reactors, low-pressure flat-flame burners, or shock tubes to a tunable synchrotron radiation beamline ($7 - 15\text{ eV}$) with an orthogonal time-of-flight mass spectrometer.

#### Principle of Threshold Photoionization
Synchrotron VUV radiation provides continuously tunable photon energies with narrow bandwidth ($\Delta E \approx 0.01\text{ eV}$). When photon energy $h\nu$ exceeds the adiabatic ionization potential of a molecule ($h\nu \ge AIE$), single-photon "soft" ionization occurs:
$$M + h\nu \longrightarrow M^{+\bullet} + e^-$$
Because the excess energy ($h\nu - AIE$) is negligible, **zero dissociative fragmentation** occurs, preserving fragile radical cations intact as parent molecular ions.

#### Photoionization Efficiency (PIE) Curves
By scanning photon energy across an energy interval and recording ion intensity at a fixed mass-to-charge ratio $m/z$, a **Photoionization Efficiency (PIE) curve** is measured:
$$\text{PIE}(E) = \frac{S_{\text{ion}}(E)}{\Phi_{\text{photon}}(E)}$$
Each chemical isomer has a distinct ionization threshold (AIE) and Franck-Condon structural overlap spectrum:
- Allyl radical ($\text{H}_2\text{C=CH-CH}_2^\bullet$): $AIE = 8.13\text{ eV}$.
- 2-Propenyl radical ($\text{H}_2\text{C=C}^\bullet\text{-CH}_3$): $AIE = 8.68\text{ eV}$.
- 1-Propenyl radical ($\text{CH}_3\text{-CH=CH}^\bullet$): $AIE = 7.70\text{ eV}$.
Fitting experimental PIE curves to absolute calibrated photoionization cross-sections deconvolutes isomeric mole fraction profiles $[X_i](T, z)$ through flame fronts with sub-millimeter spatial resolution.

### 3. Direct Discovery of the Elusive Hydroperoxyalkyl ($QOOH$) Intermediates
The low-temperature oxidation regime ($500 - 800\text{ K}$) that governs automotive knock and autoignition relies on the central chain-branching pathway:
$$R^\bullet + O_2 \rightleftharpoons RO_2^\bullet \rightleftharpoons ^\bullet QOOH \xrightarrow{+O_2} ^\bullet OOQOOH \longrightarrow \text{Keto-hydroperoxide} + OH^\bullet \longrightarrow 2 OH^\bullet + \text{radicals}$$
For decades, $^\bullet QOOH$ radicals eluded detection because the isomerization barrier is high and subsequent reaction is rapid. In 2012, Taatjes, Welz, Osborn, and co-workers used SVUV-PIMS at the Advanced Light Source to directly detect the simplest $QOOH$ radical ($\cdot CH_2CH_2OOH$) in photolysis flow reactors, confirming the mechanistic core of combustion chemical modeling."""
        },

        "unit-9": {
            "id": "sec-9-8",
            "secNumber": "9.8",
            "title": "Rapid-Freeze-Quench EPR Spectroscopy & Microfluidic Enzyme Kinetics",
            "content": r"""Capturing fleeting metalloenzyme catalytic intermediates and analyzing rapid enzyme inhibition mechanisms requires cryogenic spin trapping and microfluidic laminar flow kinetics.

### 1. Rapid-Freeze-Quench (RFQ) Electron Paramagnetic Resonance (EPR)
Many enzymatic oxidation-reduction reactions (catalase, cytochrome P450, ribonucleotide reductase, methane monooxygenase) proceed via transient paramagnetic metal centers ($\text{Fe(IV)=O}^{\bullet+}$, $\text{Cu(II)}$, $\text{Mo(V)}$) and radical amino acid intermediates ($\text{Tyr}^\bullet$, $\text{Trp}^\bullet$) with lifetimes of $5 - 100\text{ ms}$.

#### RFQ Operating Sequence
1. Enzyme and substrate solutions are rapidly propelled by motor-driven syringes into an impingement mixing chamber ($t_{\text{mix}} < 1\text{ ms}$).
2. The reacting fluid flows down a calibrated aging tube of variable length $L$ and velocity $u$, establishing an exact reaction time:
   $$t_{\text{aging}} = \frac{L}{u} \quad (5\text{ ms to } 2\text{ seconds})$$
3. At the exit nozzle, the reacting jet is atomized into an aerosol of microdroplets ($d \approx 10 - 20\;\mu\text{m}$) sprayed directly into a cryogenic liquid bath (isopentane at $-140^\circ\text{C}$ or liquid nitrogen at $-196^\circ\text{C}$).
4. Due to high surface-to-volume ratios, droplet freezing occurs in $\tau_{\text{quench}} \approx 2 - 5\text{ ms}$, permanently arresting chemical reactions.
5. The frozen microcrystals are packed into an EPR quartz tube under liquid nitrogen. Low-temperature X-band or Q-band EPR spectroscopy ($T = 4 - 20\text{ K}$) resolves g-tensors, hyperfine couplings ($A$), and electron spin states ($S = 1/2, 5/2$) of frozen intermediates.

### 2. Droplet-Based Microfluidic Enzyme Screening
Traditional multi-well microplate assays consume substantial enzyme volumes and are limited to mixing times $> 1\text{ second}$. Droplet microfluidics partitions aqueous enzyme reactions into picoliter water-in-oil emulsion droplets flowing inside fluoropolymer microchannels.

#### Physics of Microfluidic Droplet Formation
Using flow-focusing geometries with fluorinated oil (containing perfluoropolyether surfactant):
- Aqueous enzyme, substrate, and inhibitor streams meet at an orifice of width $w \approx 20 - 50\;\mu\text{m}$.
- Viscous shear forces overcome interfacial tension ($\gamma \approx 10 - 30\text{ mN/m}$), breaking the stream into monodisperse water-in-oil droplets at kilohertz frequencies ($> 5,000\text{ droplets/s}$, droplet volume $V_d \approx 10 - 50\text{ pL}$).

#### Rapid Chaotic Advection & In-Line Optical Tracking
Inside winding microchannels, recirculating internal vortex pairs generate **chaotic advection**, reducing mixing dead times to $\tau_{\text{mix}} < 2\text{ ms}$.
As droplets translate along the channel with velocity $u$, downstream distance $x$ corresponds strictly to reaction time:
$$t = \frac{x}{u}$$
Laser-induced fluorescence detection along the channel tracks Michaelis-Menten initial velocities across hundreds of substrate concentrations in minutes, using microgram quantities of recombinant enzyme."""
        },

        "unit-10": {
            "id": "sec-10-8",
            "secNumber": "10.8",
            "title": "Velocity Map Imaging (VMI) & Femtosecond Transition State Spectroscopy",
            "content": r"""Observing chemical reactions at the most fundamental quantum mechanical level requires measuring 3D product velocity vectors using ion imaging and observing transient Transition States in real time using femtosecond pump-probe laser pulses.

### 1. Velocity Map Imaging (VMI) in Crossed Molecular Beams
Velocity Map Imaging, introduced by David Parker and André Eppink (1997), revolutionized experimental reaction dynamics by measuring full 3D differential cross-sections $\frac{d^2\sigma}{d\Omega dE}$ with 100% collection efficiency.

#### Principle of Electrostatic Immersion Lens Focusing
In a crossed molecular beam experiment:
1. Two collimated supersonic molecular beams (e.g., $F + H_2$ or $O(^1D) + CH_4$) intersect at $90^\circ$ inside an ultra-high vacuum scattering chamber ($P < 10^{-10}\text{ Torr}$).
2. Products formed in specific quantum states are selectively ionized by Resonance-Enhanced Multi-Photon Ionization (REMPI).
3. The resulting ion cloud expands according to product recoil velocities. An open electrostatic immersion lens system (repeller, extractor, and ground electrodes with smooth curved potentials) accelerates ions toward a 2D position-sensitive microchannel plate (MCP) detector backed by a phosphor screen and CCD camera.
4. Crucially, the inhomogeneous electric field configuration functions as an **ion telescope**: All ions having identical initial velocity vectors $(v_x, v_y, v_z)$ are mapped onto the exact same spatial coordinate $(X, Y)$ on the detector, regardless of where they were formed within the finite spatial laser ionization volume.

#### Image Reconstruction via Abel Inversion
The 2D CCD image represents a cylindrical projection of the true 3D cylindrically symmetric scattering distribution around the relative velocity vector $\vec{v}_{\text{rel}}$.
Applying the mathematical Inverse Abel Transform:
$$F(r, \theta) = -\frac{1}{\pi} \int_r^\infty \frac{d P(x, y)/dx}{\sqrt{x^2 - r^2}} dx$$
reconstructs the true 3D velocity slice, revealing product scattering angle $\theta_{\text{c.m.}}$ (forward vs. backward rebound) and kinetic energy disposal $E_{\text{trans}}'$, proving the microscopic collision mechanism.

### 2. Femtosecond Transition State Spectroscopy (Ahmed Zewail)
Prior to femtosecond laser spectroscopy (Nobel Prize in Chemistry 1999 to Ahmed Zewail), the Transition State was regarded as an unobservable theoretical abstraction lasting only $\tau \approx 10 - 100\text{ fs}$ ($10^{-14} - 10^{-13}\text{ s}$).

#### The Pump-Probe Ultrafast Paradigm
1. **Pump Pulse ($t = 0$)**: An ultra-short laser pulse ($\tau_{\text{pulse}} \approx 20 - 50\text{ fs}$) promotes a stable reactant molecule ($ICN$ or $NaI$) from its ground potential energy surface $V_0(R)$ onto an excited repulsive surface $V_1(R)$, launching a coherent nuclear wavepacket:
   $$ICN + h\nu_{\text{pump}} \longrightarrow [I\cdots CN]^{\ddagger *}$$
2. **Dynamic Evolution**: The wavepacket slides down the repulsive potential curve as the bond stretches ($R = R_0 \to R^\ddagger \to \infty$).
3. **Probe Pulse ($t = \Delta t$)**: After an adjustable optical delay time $\Delta t$ (varied by moving a computer-controlled translation stage by $\Delta x = c \Delta t$, where $1\;\mu\text{m} \leftrightarrow 6.67\text{ fs}$):
   - Tuning the probe laser to frequency $\lambda_{\text{free}}$ monitors the appearance of free dissociated products ($CN^\bullet$).
   - Tuning the probe laser to a shifted frequency $\lambda_{\text{TS}}$ excites the transient complex $[I\cdots CN]^{\ddagger *}$ while the atoms are at intermediate separation $R^\ddagger$, emitting characteristic fluorescence.

By recording fluorescence as a function of optical delay $\Delta t$, the birth of a chemical molecule is watched in real time, clocking the transition state lifetime at precisely $200\text{ femtoseconds}$."""
        }
    }

    for u in units:
        uid = u["id"]
        if uid in sec8_dict:
            u["sections"].append(sec8_dict[uid])

    return units

if __name__ == "__main__":
    from build_kinetics_units_1_2_3 import get_units_1_2_3
    from build_kinetics_units_4_5_6 import get_units_4_5_6
    from build_kinetics_units_7_8_9_10 import get_units_7_8_9_10

    all_u = get_units_1_2_3() + get_units_4_5_6() + get_units_7_8_9_10()
    all_u = inject_section_8(all_u)
    print("Injected Section 8 across all units successfully!")
    for u in all_u:
        print(f"  {u['id']}: {len(u['sections'])} sections (latest: {u['sections'][-1]['secNumber']} {u['sections'][-1]['title'][:40]}...)")
