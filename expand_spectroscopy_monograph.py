"""
expand_spectroscopy_monograph.py
Provides advanced research monographs, state-of-the-art instrumentation case studies,
and modern spectroscopy applications for all 10 units of Chemical Spectroscopy.
Zero prohibited tokens (no course numbers, no marks, no grades, no exams).
"""

def get_monograph_enhancements():
    """
    Returns a dict mapping unit_idx (1..10) to a dict mapping section_idx (0..7)
    to supplementary monograph content that will be appended to that section.
    """
    monographs = {}

    # Unit 1: Synchrotron & XFEL Spectroscopy in Section 7 (index 6)
    monographs[1] = {
        6: r"""

### Advanced Research Monograph: Synchrotron Radiation and X-ray Free-Electron Lasers (XFEL)
While laboratory spectrometers utilize benchtop thermal filaments or hollow-cathode discharge lamps, modern frontier spectroscopy relies on accelerator-based relativistic light sources.

#### 1. Synchrotron Radiation Generation
When relativistic electrons with Lorentz factor \(\gamma = \frac{E_e}{m_e c^2} \gg 1\) are accelerated transversely along circular storage rings by magnetic bending dipoles or periodic undulator magnetic arrays (magnetic period \(\lambda_u\)), the emitted dipole radiation is compressed relativistically into a narrow forward cone of opening angle:
\[
\theta \approx \frac{1}{\gamma} \ll 1\text{ rad}
\]
The fundamental wavelength emitted on-axis by an undulator with deflection parameter \(K = \frac{e B_0 \lambda_u}{2\pi m_e c}\) is:
\[
\lambda = \frac{\lambda_u}{2\gamma^2} \left( 1 + \frac{K^2}{2} \right)
\]
Because \(\gamma \sim 10^3 - 10^4\) (GeV electron energies), centimeter-scale magnetic periods translate into vacuum ultraviolet (VUV) and hard X-ray radiation of unprecedented brilliance:
\[
\text{Brilliance} = \frac{\text{Photons / second}}{(\text{mrad})^2 \cdot (\text{mm}^2) \cdot (0.1\% \text{ bandwidth})} > 10^{20}
\]

#### 2. X-ray Free-Electron Lasers (XFEL) and SASE Lasing
In an X-ray Free-Electron Laser (such as the European XFEL or LCLS at SLAC), high-brightness electron bunches traverse hundreds of meters of undulators. Through the Self-Amplified Spontaneous Emission (SASE) mechanism, the interaction of the electrons with their own emitted radiation field induces longitudinal microbunching on the scale of the X-ray wavelength.
- This creates macroscopic coherent superposition where \(N\) electrons radiate in phase:
  \[
  I_{\text{SASE}} \propto N^2 \gg N
  \]
- Peak brilliance exceeds third-generation synchrotrons by nine orders of magnitude (\(10^{33}\)).
- Pulse durations shrink to femtosecond and attosecond regimes (\(10 - 100\text{ fs}\)), shorter than the timescale of nuclear vibrational motion (\(\sim 10 - 100\text{ fs}\)).

#### 3. "Diffraction Before Destruction" and Ultrafast Chemical Dynamics
XFEL spectroscopy enables serial femtosecond crystallography (SFX) and ultrafast time-resolved X-ray absorption spectroscopy (TR-XAS):
- By delivering pulses containing \(\sim 10^{12}\) coherent X-ray photons in a 20-fs burst, a complete diffraction and absorption pattern is recorded before Coulomb explosion disrupts the atomic coordinates.
- This allows researchers to capture real-time transition states during chemical bond breaking, such as the photolysis of iron pentacarbonyl and the oxygen-evolving catalytic cycle of Photosystem II at room temperature."""
    }

    # Unit 2: Chirped-Pulse Microwave Spectroscopy in Section 7 (index 6)
    monographs[2] = {
        6: r"""

### Advanced Research Monograph: Chirped-Pulse Fourier Transform Microwave (CP-FTMW) Astrochemistry
Historically, microwave spectroscopy was plagued by slow acquisition rates because cavity Fourier-transform spectrometers (Balle-Flygare design) could only sample bandwidths of \(\sim 1\text{ MHz}\) per cavity resonance tuning.

#### 1. Broadband Chirped-Pulse Revolution
Developed by B. H. Pate and coworkers, Chirped-Pulse Fourier Transform Microwave (CP-FTMW) spectroscopy utilizes high-speed arbitrary waveform generators (AWGs) to sweep microwave frequencies across an 11 GHz bandwidth (e.g., 7 to 18 GHz) in a single microsecond pulse (\(\Delta t = 1.0\text{ }\mu\text{s}\)):
\[
E_{\text{chirp}}(t) = E_0 \cos\left( \omega_0 t + \frac{1}{2} \alpha t^2 \right)
\]
where \(\alpha = \frac{2\pi \Delta \nu}{\Delta t}\) is the linear chirp rate.

#### 2. Macroscopic Polarization and Free Induction Decay (FID)
- The broadband pulse simultaneously polarizes all electric-dipole allowed rotational transitions across thousands of molecular species in a supersonic expansion jet.
- As the molecular ensemble macroscopically dephases, it radiates an 11-GHz broad Free Induction Decay (FID) lasting tens of microseconds.
- Real-time digitizers sampling at \(40\text{ GS/s}\) capture the complete FID, which yields the entire high-resolution microwave spectrum upon digital FFT with sub-kHz precision.

#### 3. Interstellar Astrochemistry and Prebiotic Molecule Discovery
Because pure rotational transitions are the unique fingerprint of gas-phase polar molecules in cold interstellar space (\(T \sim 10 - 50\text{ K}\)):
- CP-FTMW laboratory data directly calibrate ALMA (Atacama Large Millimeter/submillimeter Array) radio telescope observations.
- This has led to the definitive identification of complex organic molecules (COMs) in the Taurus Molecular Cloud (TMC-1) and Sagittarius B2, including chiral propylene oxide, benzonitrile (the first aromatic ring detected by radio astronomy), and cyano-polyynes."""
    }

    # Unit 3: 2D-IR Spectroscopy in Section 7 (index 6)
    monographs[3] = {
        6: r"""

### Advanced Research Monograph: Ultrafast Two-Dimensional Infrared (2D-IR) Spectroscopy
While linear FTIR measures time-averaged vibrational transitions, ultrafast 2D-IR spectroscopy provides structural correlations and sub-picosecond dynamical timescales analogous to 2D NMR, but with a \(10^9\times\) faster temporal window.

#### 1. Three-Pulse Coherent Infrared Photon Echo
2D-IR employs three femtosecond mid-IR laser pulses (\(\sim 100\text{ fs}\) duration) in a non-collinear boxcar geometry:
\[
\text{Pulse 1 } (t = 0) \xrightarrow{\tau} \text{Pulse 2 } (t = \tau) \xrightarrow{T_w} \text{Pulse 3 } (t = \tau + T_w) \xrightarrow{t} \text{Echo Detection}
\]
- **Coherence time (\(\tau\)):** Encodes the initial excitation frequency \(\omega_{\text{pump}}\).
- **Waiting time (\(T_w\)):** Population time during which structural evolution, vibrational energy transfer, and chemical exchange take place.
- **Detection time (\(t\)):** Radiates the four-wave mixing third-order nonlinear polarization \(\mathbf{P}^{(3)}(t)\), detected via spectral interferometry to yield the probe frequency \(\omega_{\text{probe}}\).

#### 2. Spectral Signatures in 2D-IR Contour Plots
At each waiting time \(T_w\), a 2D plot of \(\omega_{\text{probe}}\) versus \(\omega_{\text{pump}}\) displays two distinct features for each vibrational mode:
1. **Ground State Bleach / Stimulated Emission (Diagonal Peak, negative sign):**
   Located at \(\omega_{\text{pump}} = \omega_{01}\) and \(\omega_{\text{probe}} = \omega_{01}\).
2. **Excited-State Absorption (Off-diagonal / Anharmonic Shift, positive sign):**
   Corresponds to the \(v = 1 \rightarrow 2\) transition, shifted downwards along the probe axis by the vibrational mechanical anharmonicity:
   \[
   \Delta = \omega_{01} - \omega_{12} = 2 \omega_e x_e
   \]

#### 3. Spectral Diffusion and Hydrogen-Bond Dynamics
At \(T_w = 0\), solvent fluctuations cause inhomogeneous broadening, creating an elongated elliptical diagonal peak.
- As \(T_w\) increases, molecular reorientation and rapid hydrogen-bond breaking/re-forming randomize the local electrostatic field felt by the oscillator.
- This **spectral diffusion** causes the 2D contour to round into a symmetric circle.
- The decay rate of the peak ellipse eccentricity (Center Line Slope, CLS) directly quantifies the frequency-frequency correlation function (FFCF) \(\langle \delta\omega(t)\delta\omega(0)\rangle\), revealing that water hydrogen-bond networks rearrange on a blistering timescale of \(\sim 1.5\text{ ps}\)."""
    }

    # Unit 4: SERS and TERS in Section 7 (index 6)
    monographs[4] = {
        6: r"""

### Advanced Research Monograph: Surface-Enhanced Raman (SERS) and Tip-Enhanced Raman (TERS) Nanoscopy
Spontaneous Raman scattering has an extraordinarily small scattering cross-section (\(\sigma_R \approx 10^{-30}\text{ cm}^2/\text{molecule}\)), rendering single-molecule detection impossible under standard conditions. Plasmonic nano-optics overcomes this limitation by up to 14 orders of magnitude.

#### 1. Electromagnetic Enhancement Mechanism
When noble metal nanostructures (Au, Ag, Cu) are irradiated by laser light matching their localized surface plasmon resonance (LSPR), conduction electrons undergo collective dipolar oscillation.
- The local electric field in the vicinity of plasmonic "hot spots" (nanogaps and sharp tips) is dramatically amplified by a field enhancement factor \(g(\omega) = \frac{E_{\text{loc}}}{E_0}\).
- Because incident laser power is amplified by \(|g(\omega_L)|^2\) and the inelastically scattered Raman radiation is also amplified by the local plasmonic antenna by \(|g(\omega_S)|^2\), the total electromagnetic Raman intensity enhancement scales with the famous **fourth power of the local field**:
  \[
  G_{\text{SERS}}^{\text{EM}} = |g(\omega_L)|^2 |g(\omega_S)|^2 \approx |g(\omega)|^4 \sim 10^8 - 10^{10}
  \]

#### 2. Chemical (Charge-Transfer) Enhancement Mechanism
Molecules chemisorbed on the metal surface form coordinate bonds that facilitate photoinduced metal-to-molecule or molecule-to-metal charge transfer (CT):
\[
G_{\text{SERS}}^{\text{Chem}} = \left| \frac{\langle f | \hat{\mu} | \text{CT} \rangle \langle \text{CT} | \hat{\mu} | i \rangle}{\hbar\omega_{\text{CT}} - \hbar\omega_L - i\Gamma} \right|^2 \sim 10^2 - 10^4
\]
Combining \(G_{\text{SERS}}^{\text{EM}}\) and \(G_{\text{SERS}}^{\text{Chem}}\) yields overall enhancement factors reaching \(10^{11} - 10^{14}\), sufficient for single-molecule Raman identification.

#### 3. Tip-Enhanced Raman Spectroscopy (TERS): Nanoscale Chemical Imaging
By combining atomic force microscopy (AFM) or scanning tunneling microscopy (STM) with confocal Raman spectroscopy:
- An atomically sharp silver- or gold-coated tip acts as a single, mobile plasmonic hot spot.
- Confining the plasmonic near-field to the apex of the tip breaks the optical diffraction limit (\(\lambda / 2 \approx 250\text{ nm}\)), achieving chemical imaging with sub-nanometer spatial resolution (\(< 1\text{ nm}\)).
- In ultra-high vacuum low-temperature STM-TERS, researchers can now resolve intramolecular vibrational variations across individual chemical bonds within a single porphyrin or DNA base pair."""
    }

    # Unit 5: LIBS and XPS in Section 7 (index 6)
    monographs[5] = {
        6: r"""

### Advanced Research Monograph: Laser-Induced Breakdown Spectroscopy (LIBS) and X-ray Photoelectron Spectroscopy (XPS)
Modern multi-elemental and surface oxidation state characterization relies on high-energy atomic interactions.

#### 1. Laser-Induced Breakdown Spectroscopy (LIBS)
LIBS is an optical atomic emission technique utilizing high-power pulsed lasers:
- A nanosecond or picosecond laser pulse (\(1064\text{ nm}\), \(\sim 10 - 100\text{ mJ}\)) is focused onto a solid, liquid, or gas target, achieving power densities exceeding \(10^9\text{ W/cm}^2\).
- Multiphoton ionization and cascade electron avalanche ignite a high-temperature microplasma (\(T_{\text{plasma}} \sim 10000 - 20000\text{ K}\), electron densities \(n_e \sim 10^{17}\text{ cm}^{-3}\)).
- As the plasma cools over \(1 - 10\text{ }\mu\text{s}\), atomized and ionized elements emit characteristic atomic lines.
- **Planetary Exploration:** LIBS forms the core of the SuperCam instrument aboard the NASA Mars Perseverance rover and ChemCam on Curiosity, enabling stand-off elemental analysis of Martian rocks from distances of up to 7 meters without physical sampling.

#### 2. X-ray Photoelectron Spectroscopy (XPS / ESCA)
Developed by Kai Siegbahn, XPS is based on the photoelectric effect using monochromatic soft X-rays (\(\text{Al } K_\alpha = 1486.6\text{ eV}\) or \(\text{Mg } K_\alpha = 1253.6\text{ eV}\)):
\[
E_{\text{binding}} = h\nu - E_{\text{kinetic}} - \Phi_{\text{spectrometer}}
\]
where \(\Phi_{\text{spectrometer}}\) is the instrument work function.
- **Surface Sensitivity:** The inelastic mean free path (IMFP, \(\lambda_{\text{inelastic}}\)) of photoelectrons in solids follows the universal curve, ranging from \(0.5\) to \(2.0\text{ nm}\) for kinetic energies between \(50 - 1000\text{ eV}\). XPS samples strictly the top \(3 - 10\) atomic layers.
- **Chemical Shift and Oxidation State:** The binding energy of core electrons shifts by \(1 - 8\text{ eV}\) depending on the formal oxidation state and electronegativity of surrounding ligands (e.g., \(\text{C-C}\) at \(284.8\text{ eV}\), \(\text{C-O}\) at \(286.5\text{ eV}\), \(\text{C=O}\) at \(288.0\text{ eV}\), and \(-\text{COOH}\) at \(289.2\text{ eV}\)), providing unambiguous chemical state speciation for catalysts, battery electrodes, and semiconductor interfaces."""
    }

    # Unit 6: Ultrafast Transient Absorption in Section 7 (index 6)
    monographs[6] = {
        6: r"""

### Advanced Research Monograph: Ultrafast Transient Absorption (TA) Spectroscopy
To directly observe short-lived electronic excited states, exciton dynamics, and photochemical reaction intermediates, transient absorption uses femtosecond pump-probe spectroscopy.

#### 1. Experimental Pump-Probe Architecture
- **Pump Pulse:** A high-energy femtosecond laser pulse tuned to an absorption band excites a fraction (\(0.1 - 5\%\)) of sample molecules to an excited electronic state \(S_n\).
- **Probe Pulse:** A delayed supercontinuum white-light pulse (generated by focusing \(800\text{ nm}\) pulses into sapphire or \(\text{CaF}_2\)) probes the sample across a continuous UV-Vis-NIR bandwidth.
- The optical delay line with mechanical sub-micron motorized stages modulates delay time \(t\) with femtosecond resolution (\(1\text{ }\mu\text{m} \leftrightarrow 6.67\text{ fs}\)).

#### 2. Differential Absorption Signatures \(\Delta A(\lambda, t)\)
The recorded signal is the difference in optical density between pump-on and pump-off states:
\[
\Delta A(\lambda, t) = A_{\text{pump-on}}(\lambda, t) - A_{\text{pump-off}}(\lambda)
\]
Decomposing \(\Delta A\) yields four distinct physical components:
1. **Ground State Bleach (GSB, \(\Delta A < 0\)):**
   Depletion of the ground state population produces a negative differential absorbance that mirrors the steady-state absorption spectrum.
2. **Stimulated Emission (SE, \(\Delta A < 0\)):**
   The probe pulse induces downward transitions \(S_1 \rightarrow S_0\), amplifying probe light and appearing as a negative signal matching the steady-state fluorescence spectrum.
3. **Excited-State Absorption (ESA, \(\Delta A > 0\)):**
   Molecules in the excited state \(S_1\) absorb probe photons to higher states \(S_n \leftarrow S_1\), producing a positive differential signal.
4. **Photoproduct Absorption (PA, \(\Delta A > 0\)):**
   Triplet states, solvated electrons, isomerized intermediates, or radical pairs formed via photochemical reactions produce long-lived positive absorption bands.

#### 3. Global Target Analysis
Raw 2D datasets \(\Delta A(\lambda, t)\) containing thousands of time points are analyzed using global multi-exponential fitting:
\[
\Delta A(\lambda, t) = \sum_{k=1}^K \text{DADS}_k(\lambda) e^{-t / \tau_k}
\]
yielding Decay-Associated Difference Spectra (DADS) and Species-Associated Difference Spectra (SADS) that unravel complex multi-step kinetic schemes in artificial photosynthesis and organic solar cell charge separation."""
    }

    # Unit 7: smFRET and STED in Section 7 (index 6)
    monographs[7] = {
        6: r"""

### Advanced Research Monograph: Single-Molecule FRET and Super-Resolution STED Microscopy
Ensemble fluorescence measurements average over billions of unsynchronized molecules, obscuring rare conformational states and transient structural intermediates.

#### 1. Single-Molecule FRET (smFRET)
By immobilizing fluorophore-labeled biomolecules at sub-nanomolar concentrations in total internal reflection fluorescence (TIRF) flow cells:
- Individual photons from single donor and acceptor chromophores are detected using electron-multiplying charge-coupled devices (EMCCD) or single-photon avalanche diodes (SPAD).
- The trajectory of individual FRET efficiencies \(E(t) = \frac{I_A(t)}{I_A(t) + \gamma I_D(t)}\) displays discrete, stochastic jumps between conformational states.
- Hidden Markov Modeling (HMM) applied to single-molecule time series extracts microscopic rate constants \(k_{\text{open} \rightarrow \text{closed}}\) and detects transient folding intermediates invisible in ensemble spectrophotometry, resolving ribosome translocation mechanisms and CRISPR-Cas9 DNA target recognition.

#### 2. Stimulated Emission Depletion (STED) Nanoscopy
Invented by Stefan W. Hell, STED nanoscopy overcomes Ernst Abbe's diffraction limit (\(d = \frac{\lambda}{2 \text{NA}} \approx 200 - 300\text{ nm}\)) without post-processing:
- A diffraction-limited circular excitation laser spot (\(\sim 250\text{ nm}\)) excites fluorophores to \(S_1\).
- Simultaneously, a red-shifted high-intensity STED laser beam passed through a helical vortex phase plate produces a **doughnut-shaped focal pattern** with zero intensity at the exact center.
- The doughnut beam depresses fluorescence at the perimeter via instantaneous stimulated emission (\(S_1 \xrightarrow{h\nu_{\text{STED}}} S_0\)) to an uncollected long wavelength.
- Fluorescence emission is restricted to the sub-diffraction central null.
The effective focal spot diameter is governed by the saturation factor \(I_{\text{STED}} / I_s\):
\[
d_{\text{STED}} = \frac{\lambda}{2 \text{NA} \sqrt{1 + \frac{I_{\text{STED}}}{I_s}}}
\]
where \(I_s\) is the threshold saturation intensity.
By increasing \(I_{\text{STED}}\), spatial resolution reaches down to \(\sim 20\text{ nm}\) in live neural synapses, directly imaging vesicle trafficking and cytoskeletal actin rings."""
    }

    # Unit 8: DNP Surface-Enhanced NMR in Section 7 (index 6)
    monographs[8] = {
        6: r"""

### Advanced Research Monograph: Dynamic Nuclear Polarization (DNP) Surface-Enhanced NMR
The fundamental bottleneck of NMR spectroscopy is its intrinsically low sensitivity, caused by tiny nuclear Zeeman energy splittings relative to thermal energy (\(\Delta E_{\text{Zeeman}} \ll k_B T\)), which produces Boltzmann population differences of only \(\sim 10^{-5}\).

#### 1. Principle of Dynamic Nuclear Polarization (DNP)
Because the gyromagnetic ratio of the electron is much larger than that of nuclei (\(|\gamma_e| \approx 658 \times \gamma_{^1\text{H}}\)):
- Unpaired electron spins polarize almost completely (\(P_e \approx 100\%\)) at cryogenic temperatures (\(100\text{ K}\)) and high magnetic fields (\(9.4\text{ T}\)).
- By introducing stable bis-nitroxide biradicals (e.g., AMUPol, TEKPol) and irradiating the sample with continuous-wave high-power microwave radiation generated by a **gyrotron** (\(\sim 263\text{ GHz}\) at \(9.4\text{ T}\)), polarization is transferred from electron spins to nuclear spins via the Cross Effect (CE):
  \[
  \epsilon = \frac{P_{\text{DNP}}}{P_{\text{Boltzmann}}} \sim 100 - 400
  \]

#### 2. Signal Gain and Acquisition Speedup
Since experimental signal-to-noise ratio scales with \(\sqrt{N_{\text{scans}}}\), a DNP enhancement factor of \(\epsilon = 100\) reduces experimental acquisition time by a factor of:
\[
\text{Time Reduction Factor} = \epsilon^2 = (100)^2 = 10000
\]
An experiment requiring 3 years of continuous signal averaging on a conventional NMR spectrometer can be recorded in less than 3 hours under DNP conditions!

#### 3. DNP-SENS: Surface-Enhanced NMR Spectroscopy of Materials
In DNP Surface-Enhanced NMR Spectroscopy (DNP-SENS):
- Incipient wetness impregnation wets porous catalysts, metal-organic frameworks (MOFs), or functionalized nanoparticles with a biradical solution without penetrating dense inorganic bulk lattices.
- Hyperpolarization originates exclusively at the external liquid-solid interface and propagates into the material surface via \(^1\text{H}-^1\text{H}\) spin diffusion.
- This selectively amplifies surface species (\(^{13}\text{C}, ^{15}\text{N}, ^{29}\text{Si}, ^{17}\text{O}, ^{27}\text{Al}\)) by several orders of magnitude, allowing sub-monolayer active catalytic sites to be characterized with structural precision previously restricted to bulk solution NMR."""
    }

    # Unit 9: Solid-State MAS NMR in Section 7 (index 6)
    monographs[9] = {
        6: r"""

### Advanced Research Monograph: Solid-State Magic Angle Spinning (MAS) NMR of Biomolecules and Battery Materials
Unlike solution NMR where rapid isotropic Brownian tumbling averages anisotropic magnetic interactions to zero, solid-state NMR spectra of powders and membranes are severely broadened by Chemical Shift Anisotropy (CSA), direct Dipolar Couplings, and Nuclear Quadrupole Interactions.

#### 1. Fast and Ultra-Fast Magic Angle Spinning
By mechanically spinning the cylindrical zirconia rotor at an angle \(\theta = \arctan(\sqrt{2}) \approx 54.74^\circ\) relative to \(\mathbf{B}_0\):
- The geometric Legendre polynomial vanishes identically:
  \[
  P_2(\cos\theta) = \frac{3\cos^2\theta - 1}{2} = \frac{3(1/3) - 1}{2} = 0
  \]
- Spinning speeds have advanced from \(10\text{ kHz}\) (4 mm rotors) to over \(100 - 150\text{ kHz}\) (0.7 mm micro-rotors driven by compressed nitrogen gas).
- At \(\nu_R > 100\text{ kHz}\), massive \(^1\text{H}-^1\text{H}\) homonuclear dipolar couplings (\(\sim 50\text{ kHz}\)) are completely averaged out, yielding high-resolution \(^1\text{H}\) solid-state spectra with linewidths rivaling solution-state NMR.

#### 2. Atomic-Resolution Structure Determination of Insoluble Aggregates
Solid-state MAS NMR is uniquely suited for systems that cannot crystallize or be dissolved:
- **Amyloid Fibrils:** Elucidated the full 3D atomic structures of \(\beta\)-amyloid (A\(\beta_{40}\), A\(\beta_{42}\)) fibrils in Alzheimer's disease and \(\alpha\)-synuclein in Parkinson's pathology.
- **Membrane Proteins:** Resolved the active conformation and ion channels of GPCRs and light-driven pumps in native phospholipid bilayer environments without detergent extraction.

#### 3. Operando Battery Electrochemistry
Using specialized radiofrequency probe circuits with hermetically sealed battery pouch cells:
- In situ \(^7\text{Li}\) and \(^{23}\text{Na}\) MAS NMR monitors lithium metal dendrite formation in real time during charge/discharge cycling.
- Resolves the evolution of solid electrolyte interphase (SEI) layers, distinguishing reversible insertion from irreversible dead metal deposition at the electrode surface."""
    }

    # Unit 10: In Situ Operando ESR and Mössbauer in Section 7 (index 6)
    monographs[10] = {
        6: r"""

### Advanced Research Monograph: In Situ Operando ESR and Mössbauer Spectroscopy in Heterogeneous and Bio-Catalysis
To unravel catalytic reaction mechanisms, spectroscopic observation must be performed *operando*—under real working conditions (high temperature, pressure, reactive gas atmospheres, and electrochemical potentials).

#### 1. In Situ Operando ESR for Transient Radical Intermediates
- **Electrochemical ESR (EC-ESR):** An electrochemical cell integrated directly into an ESR microwave cavity enables simultaneous cyclic voltammetry and radical detection. Rapid single-electron transfer reactions at the electrode generate paramagnetic radical anions or cations that are monitored in real time.
- **Spin Trapping for Reactive Oxygen Species (ROS):** Extremely short-lived free radicals (\(\cdot\text{OH}, \text{O}_2^{\cdot-}, \text{HO}_2^\cdot\), lifetimes \(< 1\text{ }\mu\text{s}\)) in photocatalytic water oxidation are captured by nitrone spin traps (such as DMPO, DEPMPO) to form long-lived, stable nitroxide spin adducts with distinct multi-line hyperfine split fingerprints.
- **High-Pressure Catalytic Flow Cells:** Quartz capillary microreactors operating at \(100\text{ bar}\) and \(400^\circ\text{C}\) reveal the valence fluctuation of paramagnetic active centers (\(\text{Mo}^{5+}, \text{V}^{4+}, \text{Ti}^{3+}\)) during industrial olefin polymerization and selective oxidation of hydrocarbons.

#### 2. In Situ Operando \(^{57}\text{Fe}\) Mössbauer Spectroscopy
Because \(\gamma\)-rays (14.4 keV) penetrate deep through cell walls, reactor windows, and liquid electrolytes without attenuation:
- **Oxygen Evolution Catalysts:** In situ electrochemical Mössbauer spectroscopy of iron-doped nickel oxyhydroxide (\(\text{Ni}_{1-x}\text{Fe}_x\text{OOH}\)) electrocatalysts reveals the transient formation of high-valent \(\text{Fe}^{4+}\) species characterized by an isomer shift of \(\delta \approx -0.27\text{ mm/s}\), identifying the elusive active site responsible for rapid O-O bond formation.
- **Fischer-Tropsch Synthesis:** Tracking the conversion of \(\alpha\text{-Fe}_2\text{O}_3\) into active Hägg carbide (\(\chi\text{-Fe}_5\text{C}_2\)) and cementite (\(\theta\text{-Fe}_3\text{C}\)) under \(20\text{ bar}\) syngas at \(300^\circ\text{C}\) identifies deactivation by oxidation and coke encapsulation.
- **Iron-Sulfur Metalloclusters:** In bioinorganic chemistry, freeze-quenched Mössbauer spectroscopy captures the fleeting high-spin \(\text{Fe(IV)=O}\) intermediates in non-heme iron oxygenases and nitrogenase FeMo-cofactor during catalytic dinitrogen reduction."""
    }

    return monographs

if __name__ == "__main__":
    monographs = get_monograph_enhancements()
    print(f"Generated monographs for {len(monographs)} units.")
    for u, sects in sorted(monographs.items()):
        print(f"Unit {u}: enhanced sections {list(sects.keys())}")
