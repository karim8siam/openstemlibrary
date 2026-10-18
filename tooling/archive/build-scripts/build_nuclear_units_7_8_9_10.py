# -*- coding: utf-8 -*-
"""
build_nuclear_units_7_8_9_10.py
Builds Units 7, 8, 9, and 10 for Nuclear and Radiochemistry (#47):
- Unit 7: Radiation Detection Systems: Gas, Scintillation & Semiconductor Spectrometry
- Unit 8: Nuclear Analytical Techniques: NAA, IDA & Radiocarbon Dating
- Unit 9: Radioisotope Production, Accelerators & Radionuclide Generators
- Unit 10: Radiation Dosimetry, Radiobiology & Radioprotection (ALARA)
Strictly Zero Course Numbers or Marks. All math in raw strings r\"\"\"...\"\"\".
"""

import json

def get_units_7_8_9_10():
    units = [
        # =====================================================================
        # UNIT 7
        # =====================================================================
        {
            "id": "unit-7-radiation-detection-spectrometry",
            "unitNumber": 7,
            "title": "Unit 7: Radiation Detection Systems: Gas, Scintillation & Semiconductors",
            "leadSummary": "Comprehensive physical and electronic treatise on radiation detection instrumentation: Townsend avalanche kinetics and the six gas detector operating regimes; ionization chambers, proportional counters, and Geiger-Müller tubes; organic and inorganic scintillation mechanisms; photomultiplier tubes and silicon photomultipliers; solid-state semiconductor bandgap physics; High-Purity Germanium (HPGe) gamma spectroscopy; and multichannel pulse height analysis.",
            "simulations": ["sim_nuc_geiger_muller_avalanche", "sim_nuc_hpge_gamma_spectroscopy"],
            "sections": [
                {
                    "id": "sec-7-1",
                    "secNumber": "7.1",
                    "title": "Gas-Filled Radiation Detectors: The Six Operating Voltage Regimes & Charge Multiplication",
                    "content": r"""Gas-filled radiation detectors represent the oldest and most versatile class of radiation detection instrumentation. A gas detector consists of a gas-filled chamber containing two electrodes across which an external high-voltage electric field is applied: an outer cylindrical cathode and a thin central axial anode wire.

When ionizing radiation enters the active gas volume, it creates a quantity of primary electron-ion pairs proportional to the absorbed energy:
$$n_0 = \frac{E_{\text{dep}}}{W}$$
where $W$ is the average energy required to produce one electron-ion pair in the gas ($W \approx 26\text{ eV}$ in argon, $34\text{ eV}$ in air, $41\text{ eV}$ in helium).

### The Characteristic Pulse Height Versus Voltage Curve
If an ionization event creates $n_0$ primary ion pairs, the total charge collected at the anode depends fundamentally on the applied voltage $V$:

```
 Total Charge Collected Q
  ▲                                             Continuous Discharge (VI)
  │                                                      /
  │                                       Geiger-Müller /
  │                                       Plateau (V)  /
  │                                      /────────────/
  │                       Limited       /
  │                    Proportionality /
  │                         (IV)      /
  │               Proportional       /
  │                Region (III)     /
  │                /───────────────/
  │  Ionization   /
  │  Chamber (II)/
  │ ┌───────────┘
  │/ Recombination (I)
  └──────────────────────────────────────────────────────► Applied Voltage V
```

1. **Region I: Recombination Region**:
The applied electric field is too weak ($E < 100\text{ V/cm}$) to overcome electrostatic attraction. Electrons and positive ions recombine before reaching the electrodes; charge collection is incomplete and voltage-dependent.
2. **Region II: Ionization Chamber Region**:
The electric field is strong enough to achieve complete charge collection ($100\%$ collection efficiency) before recombination occurs. The pulse height forms a flat saturation plateau where collected charge equals the initial ionization charge:
$$Q = n_0 e \quad (\text{Multiplication Factor } M = 1)$$
Pulse height is strictly proportional to deposited energy, but pulse amplitudes are extremely small ($\sim 10^{-14}\text{ C} \sim \text{microvolts}$), requiring sensitive electrometer amplification.
3. **Region III: Proportional Region**:
Near the thin central anode wire of radius $a$, the radial electric field escalates:
$$E(r) = \frac{V}{r \ln(b/a)}$$
When $E(r) > 10^4\text{ V/cm}$, free electrons gain enough kinetic energy between mean free paths to cause secondary impact ionization of gas atoms. This initiates a **Townsend electron avalanche**.
The total collected charge is:
$$Q = M \cdot n_0 e$$
where $M$ is the **gas multiplication factor** ($M \sim 10^3 - 10^5$).
Crucially, $M$ is independent of the initial ionization $n_0$; the output pulse height remains strictly proportional to the energy deposited by the incident radiation, enabling energy spectroscopy of alpha and beta particles.
4. **Region IV: Region of Limited Proportionality**:
The electron avalanche becomes so massive that the dense sheath of slow positive ions around the anode wire shields the electric field (space charge effect). Proportionality is lost.
5. **Region V: Geiger-Müller (GM) Region**:
The electric field is so high that ultraviolet photons emitted by excited gas atoms trigger secondary avalanches along the entire length of the anode wire. A single primary electron triggers a full discharge ($M \sim 10^8 - 10^{10}$). Output pulse heights are huge ($\sim 1 - 2\text{ Volts}$) and completely independent of the energy or type of incident radiation.
6. **Region VI: Continuous Discharge Region**:
The electric field exceeds the dielectric breakdown strength of the gas; a continuous, damaging glow discharge occurs without radiation.""",
                    "simulations": ["sim_nuc_geiger_muller_avalanche"]
                },
                {
                    "id": "sec-7-2",
                    "secNumber": "7.2",
                    "title": "Ionization Chambers & Proportional Counters: Cavity Theory & Neutron Proportional Tubes",
                    "content": r"""Ionization chambers and proportional counters operate in distinct voltage regimes, serving complementary roles in radiation metrology.

### Ionization Chamber Instrumentation and Cavity Theory
Ionization chambers operate with $M = 1$, measuring either individual ionization pulses (pulse mode) or the integrated steady-state saturation current (current mode):
$$I_{\text{sat}} = \left(\frac{dE}{dt}\right) \frac{e}{W} = \dot{D} \cdot m \cdot \left(\frac{e}{W}\right)$$
Ion chambers are the gold standard for **reference dosimetry calibrations** because their response is absolute and directly relates to the definition of radiation dose.

According to the **Bragg-Gray Cavity Principle**, the absorbed dose $D_{\text{med}}$ in an absorbing medium surrounding a small gas cavity is related to the dose $D_{\text{gas}}$ measured in the cavity gas:
$$D_{\text{med}} = D_{\text{gas}} \cdot \bar{s}_{\text{med, gas}} = \left(\frac{Q}{m_{\text{gas}}} \frac{W_{\text{gas}}}{e}\right) \bar{s}_{\text{med, gas}}$$
where $\bar{s}_{\text{med, gas}}$ is the ratio of mass collisional stopping powers of the medium to the gas averaged over the electron spectrum.

### Proportional Counters and Counting Gases
Proportional counters typically utilize a gas mixture known as **P-10**:
- $90\%$ Argon ($\text{Ar}$): Noble gas providing high ionization density and low excitation threshold.
- $10\%$ Methane ($\text{CH}_4$): Polyatomic "quench gas" whose rotational and vibrational energy levels absorb ultraviolet photons, preventing spurious photoemission from the cathode.

### Thermal Neutron Detection via Proportional Tubes
Because neutrons carry no electrical charge, they cannot ionize gases directly. Thermal neutrons are detected in proportional counters by filling the tube with gases that undergo exoergic neutron reactions yielding high-energy charged particles:

1. **Boron Trifluoride ($\text{BF}_3$) Proportional Tubes**:
Utilizes enriched $^{10}\text{B}$ ($96\%$ enrichment):
$$^{10}_5\text{B} + ^1_0n_{\text{th}} \longrightarrow \begin{cases} ^7_3\text{Li} + ^4_2\alpha + 2.792\text{ MeV} & (6\% \text{ to ground state}) \\ ^7_3\text{Li}^* + ^4_2\alpha + 2.310\text{ MeV} \quad (\gamma = 478\text{ keV}) & (94\% \text{ to excited state}) \end{cases}$$
The thermal capture cross-section is $\sigma_{\text{th}} = 3,840\text{ barns}$. The alpha particle ($1.47\text{ MeV}$) and lithium recoil nucleus ($0.84\text{ MeV}$) create massive ionization pulses ($\approx 80,000$ ion pairs) that dwarf background gamma pulses, providing excellent gamma-neutron discrimination via simple discriminator thresholds.

2. **Helium-3 ($^3\text{He}$) Proportional Tubes**:
$$^3_2\text{He} + ^1_0n_{\text{th}} \longrightarrow ^3_1\text{H} + ^1_1p + 0.764\text{ MeV} \quad (\sigma_{\text{th}} = 5,330\text{ barns})$$
Provides superior neutron detection efficiency and chemical non-toxicity, making $^3\text{He}$ tubes the global standard for neutron border monitors and nuclear safeguards.""",
                    "simulations": ["sim_nuc_geiger_muller_avalanche"]
                },
                {
                    "id": "sec-7-3",
                    "secNumber": "7.3",
                    "title": "Geiger-Müller Counters: Townsend Avalanches, Halogen Quenching & Dead Time Kinetics",
                    "content": r"""The Geiger-Müller (GM) counter is the most widely deployed portable radiation survey instrument due to its exceptional sensitivity, ruggedness, and simplicity.

### The GM Avalanche Propagation Mechanism
In the GM region ($V \approx 900 - 1400\text{ V}$), the electric field near the anode wire is so high that electrons in an avalanche excite argon atoms to radiative states. Within picoseconds, these atoms de-excite by emitting UV photons ($h\nu \sim 11 - 15\text{ eV}$).
Because argon is transparent to its own UV emission, these photons travel freely through the gas volume and strike other gas molecules or the cathode wall, ejecting photoelectrons. Each photoelectron initiates an independent Townsend avalanche at a new location along the wire:

```
 Primary Ionization ──► Initial Avalanche ──► UV Photon Emission
                                                   │
                                                   ▼
 Cathode Photoemission ◄── UV Propagation ──► Secondary Avalanches
           │                                       │
           └─────────────────► FULL WIRE DISCHARGE ◄┘
```

The discharge propagates axially until a dense sheath of slow positive argon ions envelops the entire central anode wire. Because positive ions move $\sim 1000$ times slower than electrons, this positive space-charge sheath reduces the effective electric field below the threshold needed for multiplication, extinguishing the discharge.

### Quenching Mechanisms: Organic Versus Halogen
When the sheath of positive ions reaches the cathode wall, they neutralize by capturing electrons:
$$\text{Ar}^+ + e^- \longrightarrow \text{Ar}^* \longrightarrow \text{Ar} + h\nu$$
The energy released equals the ionization potential of argon ($I_{\text{Ar}} = 15.76\text{ eV}$). This exceeds the work function of the cathode metal ($\Phi \approx 4 - 5\text{ eV}$), liberating secondary electrons that would reignite a spurious second pulse, resulting in continuous pulsing.

To quench this, a small percentage ($0.1 - 1\%$) of a **quench gas** is added:
- **Halogen Quenching**: A halogen vapor (bromine $\text{Br}_2$ or chlorine $\text{Cl}_2$) is introduced. Because the ionization potential of $\text{Br}_2$ ($10.5\text{ eV}$) is lower than argon ($15.8\text{ eV}$), charge exchange occurs:
$$\text{Ar}^+ + \text{Br}_2 \longrightarrow \text{Ar} + \text{Br}_2^+$$
All positive ions arriving at the cathode are $\text{Br}_2^+$ molecules. Upon electron capture at the wall, the molecule neutralizes by **dissociating into neutral atoms**:
$$\text{Br}_2^+ + e^- \longrightarrow \text{Br} + \text{Br} \quad (\text{Non-radiative dissociation})$$
Unlike organic quenchers (which permanently degrade after $\sim 10^8$ counts), halogen atoms spontaneously recombine ($\text{Br} + \text{Br} \to \text{Br}_2$), giving halogen-quenched GM tubes an **infinite operational lifespan**!

### Dead Time ($\tau$) Kinetics: Paralyzable Versus Non-Paralyzable Models
While the positive ion sheath is drifting away from the anode wire, the detector is insensitive to new incoming ionizing particles. This duration is the **dead time** $\tau$ (typically $\tau \approx 50 - 200\,\mu\text{s}$ in GM tubes).

Let $n$ be the true particle interaction rate and $m$ be the recorded count rate:

1. **Non-Paralyzable Model**:
The detector is dead for a fixed dead time $\tau$ following each recorded event. Any radiation arriving during $\tau$ is ignored and does not extend the dead time.
The fraction of dead time per unit time is $m \tau$.
The true count rate is:
$$m = n (1 - m \tau) \implies n = \frac{m}{1 - m \tau}$$

2. **Paralyzable Model**:
Each interaction extends the dead time by another period $\tau$, even if the event was not recorded.
By Poisson statistics, the probability of zero events occurring in interval $\tau$ is $e^{-n \tau}$:
$$m = n e^{-n \tau}$$
At extremely high count rates ($n \to \infty$), the recorded count rate in a paralyzable detector drops toward zero—a dangerous failure mode where a catastrophic radiation field reads zero on an uncompensated meter!""",
                    "simulations": ["sim_nuc_geiger_muller_avalanche"]
                },
                {
                    "id": "sec-7-4",
                    "secNumber": "7.4",
                    "title": "Scintillation Detectors: Inorganic Phosphors, Activator Luminescence & Organic Scintillators",
                    "content": r"""Scintillation detectors convert the kinetic energy of ionizing radiation into a flash of optical or ultraviolet photons through luminescent excitation of transparent scintillator materials.

### 1. Inorganic Crystal Scintillators (Bandgap Luminescence)
Inorganic scintillators are wide-bandgap crystalline dielectrics doped with trace impurity activators. The premier gamma detection scintillator is **Thallium-activated Sodium Iodide, $\text{NaI(Tl)}$**:
- **High Stopping Power**: High density ($\rho = 3.67\text{ g/cm}^3$) and high effective atomic number ($Z_{\text{I}} = 53$) provide high photoelectric gamma absorption.
- **Scintillation Mechanism**:
  Ionizing radiation promotes electrons from the crystal valence band to the conduction band, creating electron-hole pairs and free excitons.
  In a pure crystal, radiative de-excitation back to the valence band emits photons whose energy equals the bandgap ($E_g \approx 6\text{ eV}$ in UV), which are immediately reabsorbed by the crystal (self-absorption).
  Doping with $\approx 0.1\%$ thallium ($\text{Tl}^+$) creates localized energy states within the forbidden bandgap:

```
  CONDUCTION BAND
  ══════════════════════════════════════════════
     │                     ▲
     ▼ Ionization          │ Exciton Migration
  ─────────────────────────┴────────────────────
     ACTIVATOR STATES (Tl⁺)
     ─── Excited Level (³P₁)
      │
      ▼ Optical Emission (λ ≈ 415 nm, Visible Blue)
     ─── Ground Level (¹S₀)
  ══════════════════════════════════════════════
  VALENCE BAND
```

  De-excitation through the thallium activator levels emits visible blue photons ($\lambda_{\max} \approx 415\text{ nm}$, $h\nu \approx 3.0\text{ eV}$). Because $3.0\text{ eV} < E_g$, the crystal is completely transparent to its own scintillation light!
- **Scintillation Light Yield**: $\approx 38,000\text{ optical photons per MeV}$ of absorbed gamma energy.
- **Decay Time**: Exponential decay with primary time constant $\tau \approx 230\text{ ns}$.

Other key inorganic scintillators:
- **$\text{CsI(Tl)}$**: Higher stopping power ($\rho = 4.51\text{ g/cm}^3$), emission at $550\text{ nm}$ matching silicon photodiodes.
- **$\text{BGO}$ ($\text{Bi}_4\text{Ge}_3\text{O}_{12}$)**: Bismuth ($Z = 83$), density $7.13\text{ g/cm}^3$, used in Positron Emission Tomography (PET).
- **$\text{LaBr}_3\text{:Ce}$**: Ultrafast decay ($\tau \approx 16\text{ ns}$) and exceptional energy resolution ($2.6\%$ at $662\text{ keV}$).

### 2. Organic Scintillators (Molecular Transitions)
Organic scintillators include aromatic hydrocarbon crystals (anthracene, stilbene), plastic polymers (PVT doped with PPO/POPOP), and liquid scintillation cocktails:
- **Luminescence Mechanism**: Driven by transitions between $\pi$-electron molecular orbitals ($S_1 \to S_0$) of individual benzene rings, entirely independent of physical crystalline state.
- **Fast Decay Time**: Ultrafast fluorescence lifetimes ($\tau \approx 1 - 3\text{ ns}$), ideal for sub-nanosecond timing coincidence and time-of-flight measurements.
- **Low-$Z$**: Composed of carbon and hydrogen ($Z \approx 6$), minimizing photoelectric absorption; useful for beta counting and fast neutron detection via recoil protons.
- **Liquid Scintillation Counting (LSC)**: The radioactive analyte (e.g., low-energy beta emitters $^3\text{H}$ [$18.6\text{ keV}$] or $^{14}\text{C}$ [$156\text{ keV}$]) is dissolved directly in an aromatic liquid solvent cocktail containing primary and secondary fluor solutes, achieving $4\pi$ geometry with zero self-absorption.""",
                    "simulations": ["sim_nuc_hpge_gamma_spectroscopy"]
                },
                {
                    "id": "sec-7-5",
                    "secNumber": "7.5",
                    "title": "Photomultiplier Tubes & Optical Readout: Dynode Cascades, Quantum Efficiency & Modern SiPMs",
                    "content": r"""The optical scintillation flash produced in a scintillator crystal is too faint for direct electronic measurement. The **Photomultiplier Tube (PMT)** converts these optical photons into a measurable electronic charge pulse with a gain of $10^6 - 10^7$.

### The Photomultiplier Tube Architecture
A PMT consists of an evacuated glass envelope housing:
1. **Photocathode**: A thin, semitransparent layer of low-work-function photoemissive material (bialkali, e.g., $\text{Sb-Rb-Cs}$ or $\text{Sb-K-Cs}$) deposited on the interior entrance window.
   Optical photons strike the photocathode and eject electrons into the vacuum via the photoelectric effect:
   $$\text{Quantum Efficiency (QE)} \equiv \frac{\text{Photoelectrons Ejected}}{\text{Incident Scintillation Photons}} \approx 25 - 35\%$$
2. **Focusing Electrode**: Electrostatic lens directing photoelectrons toward the first dynode.
3. **Dynode Electron Multiplication Cascade**:
   A series of $n$ curved electrodes (typically $n = 10 - 14$ dynodes) held at progressively higher positive potentials via a resistive voltage divider chain ($\Delta V \approx 100\text{ V}$ per stage).
   When an electron strikes dynode $i$, it liberates $\delta$ secondary electrons (secondary emission ratio $\delta \approx 4 - 6$):
   $$\delta \propto (\Delta V)^k \quad (k \approx 0.7 - 0.8)$$

```
 Scintillation Crystal
 ═════════════════════
  │ │ │ (Optical Photons hν)
  ▼ ▼ ▼
 ┌───────────────────┐  Photocathode (QE ≈ 30%)
 └─────────┬─────────┘
           │ (Primary Photoelectrons)
           ▼
         ( D₁ ) ──► δ Secondary Electrons
           │
           ▼
         ( D₂ ) ──► δ² Electrons
           │
           ▼
         ( D₃ ) ──► δ³ Electrons
          ...
           ▼
       [ ANODE ] ──► Total Charge Pulse Q = e * N_pe * δⁿ
```

The total current gain $G$ of a PMT with $n$ dynode stages is:
$$G = \delta^n$$
For a 10-stage PMT with $\delta = 4.5$:
$$G = (4.5)^{10} \approx 3.4 \times 10^6$$
A single photoelectron produces an anode charge packet containing several million electrons within a rise time of $\approx 1 - 2\text{ ns}$.

### Silicon Photomultipliers (SiPMs)
Modern radiation instrumentation increasingly replaces bulky, fragile vacuum PMTs with solid-state **Silicon Photomultipliers (SiPMs)**:
- Consists of a high-density array of thousands of micro-pixel avalanche photodiodes (APDs) connected in parallel on a common silicon substrate.
- Operates in Geiger mode above breakdown voltage ($V_{\text{bias}} \approx 30 - 60\text{ V}$).
- **Advantages**: Immune to strong magnetic fields (crucial for simultaneous PET-MRI imaging), compact footprint ($3 \times 3\text{ mm}$), low operating voltage, and high Photon Detection Efficiency (PDE $>50\%$).""",
                    "simulations": ["sim_nuc_hpge_gamma_spectroscopy"]
                },
                {
                    "id": "sec-7-6",
                    "secNumber": "7.6",
                    "title": "Semiconductor Radiation Detectors: Solid-State Band Theory, Fano Factor & Charge Collection",
                    "content": r"""Semiconductor detectors function as solid-state ionization chambers. Instead of creating electron-ion pairs in a gas, ionizing radiation creates **electron-hole ($e^--h^+$) pairs** in a crystalline semiconductor lattice.

### The Fundamental Advantage: Energy Resolution
In a gas detector, the average energy required to create one ion pair is $W \approx 30\text{ eV}$.
In a scintillator-PMT combination, creating one photoelectron at the photocathode requires $\approx 100 - 300\text{ eV}$ of absorbed gamma energy.
In semiconductor crystals, the bandgap $E_g$ between the valence and conduction bands is narrow:
- Silicon ($\text{Si}$): $E_g = 1.12\text{ eV} \implies \epsilon = 3.62\text{ eV}$ per $e^--h^+$ pair.
- Germanium ($\text{Ge}$): $E_g = 0.67\text{ eV} \implies \epsilon = 2.96\text{ eV}$ per $e^--h^+$ pair.

For an identical absorbed energy $E_{\text{dep}} = 1.0\text{ MeV}$:
- $\text{NaI(Tl)}$ creates $\approx 4,000$ photoelectrons at the PMT photocathode.
- Germanium creates:
$$N = \frac{1,000,000\text{ eV}}{2.96\text{ eV}} \approx 338,000\text{ electron-hole pairs}$$
Because Poisson statistical uncertainty scales as $\sigma_N / N = 1/\sqrt{N}$, having **$85$ times more charge carriers** reduces statistical variance dramatically, resulting in an unprecedented improvement in energy resolution!

### The Fano Factor ($F$)
Because energy loss in a crystal lattice occurs through two competing channels—discrete ionization of valence electrons and excitation of non-ionizing acoustic lattice phonons (heat)—the individual ionization events are not statistically independent.
The variance in the number of created charge carriers is reduced below the classical Poisson limit by the **Fano Factor** $F < 1$:
$$\sigma_N^2 = F \cdot N = F \left(\frac{E}{\epsilon}\right)$$
For germanium: $F \approx 0.08 - 0.10$; for silicon: $F \approx 0.11$.

The intrinsic statistical Full Width at Half Maximum (FWHM) energy resolution is:
$$\text{FWHM}_{\text{stat}} = 2.355 \cdot \sigma_E = 2.355 \sqrt{F \cdot \epsilon \cdot E}$$
For a $1.332\text{ MeV}$ gamma ray in germanium:
$$\text{FWHM}_{\text{stat}} = 2.355 \sqrt{(0.08)(2.96\text{ eV})(1.332 \times 10^6\text{ eV})} = 2.355 \sqrt{315,417} \approx 1.32\text{ keV}$$
$$\frac{\text{FWHM}}{E} = \frac{1.32\text{ keV}}{1332\text{ keV}} \approx 0.10\%$$
Compared to $\sim 6.0\%$ for $\text{NaI(Tl)}$, semiconductor detectors provide **60 times sharper spectral peaks**, enabling the resolution of closely spaced gamma multiplets that appear as single blobs in scintillation detectors.""",
                    "simulations": ["sim_nuc_hpge_gamma_spectroscopy"]
                },
                {
                    "id": "sec-7-7",
                    "secNumber": "7.7",
                    "title": "High-Purity Germanium (HPGe) Spectrometry & Pulse Height Multichannel Analysis (MCA)",
                    "content": r"""Germanium possesses a significantly higher atomic number ($Z = 32$) and density ($\rho = 5.32\text{ g/cm}^3$) than silicon ($Z = 14, \rho = 2.33\text{ g/cm}^3$), making it the premier semiconductor material for gamma-ray spectroscopy ($Z^4$ photoelectric scaling).

### High-Purity Germanium (HPGe) Crystal Technology
In intrinsic semiconductors at room temperature ($T = 300\text{ K}$), the narrow bandgap ($E_g = 0.67\text{ eV}$) allows thermal energy ($k_B T \approx 0.026\text{ eV}$) to excite electrons across the gap, generating an enormous thermal leakage current that swamps radiation signals.
To function as a radiation detector:
1. **Ultra-Purification**: The crystal must be zone-refined to unprecedented impurity concentrations ($|N_A - N_D| \le 10^{10}\text{ atoms/cm}^3$—less than one impurity atom per trillion germanium atoms!). This enables creation of wide depletion depths ($W > 3 - 5\text{ cm}$) at reverse bias voltages of $V \approx 2000 - 5000\text{ V}$:
$$W = \sqrt{\frac{2\varepsilon V}{e |N_A - N_D|}}$$
2. **Cryogenic Cooling**: HPGe detectors must be operated at liquid nitrogen temperatures ($77\text{ K}$, $-196^\circ\text{C}$) via a dewar cryostat or closed-cycle mechanical Stirling cooler to freeze out thermal charge carriers.

```
       TYPICAL HPGe GAMMA-RAY PULSE HEIGHT SPECTRUM
 Counts
  ▲
  │              PHOTOPEAK (Full Energy Absorption)
  │                 │
  │                 ▼
  │                | |
  │               /| |\
  │              / | | \   Single Escape Peak (E - 511 keV)
  │    COMPTON  /  | |  \    │
  │    EDGE    /   | |   \   ▼
  │     |     /    | |    \ | |
  │    / \___/     | |     \| |  Backscatter Peak (~180-250 keV)
  │   /  Compton   | |      | |   │
  │  /  Continuum  | |      | |   ▼
  │ /              | |      | |  | |
  └────────────────┴─┴──────┴─┴──┴─┴────────────────► Channel (Energy E)
```

### Multichannel Analyzer (MCA) Spectral Morphology
The preamplifier pulse is shaped by a spectroscopic amplifier into a semi-Gaussian voltage pulse whose peak amplitude $V_{\text{peak}} \propto E_{\text{dep}}$.
The **Multichannel Analyzer (MCA)** digitizes $V_{\text{peak}}$ via an Analog-to-Digital Converter (ADC, typically $4096 - 16384$ channels) and increments the corresponding memory register.

The resulting gamma spectrum displays distinct physical features:
1. **Photopeak (Full Energy Peak)**: Full absorption of $E_\gamma$ through photoelectric effect or multiple Compton events followed by photoelectric absorption.
2. **Compton Continuum**: Broad plateau below the photopeak corresponding to Compton scattering where the scattered photon escapes the crystal.
3. **Compton Edge**: Sharp drop at $E_C = \frac{2E_\gamma^2}{m_e c^2 + 2E_\gamma}$.
4. **Backscatter Peak**: Gammas scattering backward ($180^\circ$) from shielding/cryostat walls into the crystal ($E \approx 180 - 250\text{ keV}$).
5. **Escape Peaks**: For $E_\gamma > 1.022\text{ MeV}$, pair production generates two $511\text{ keV}$ annihilation photons. If one escapes: Single Escape Peak ($E - 511\text{ keV}$). If both escape: Double Escape Peak ($E - 1022\text{ keV}$).""",
                    "simulations": ["sim_nuc_hpge_gamma_spectroscopy"]
                }
            ],
            "problems": [
                {
                    "id": "prob-7-1",
                    "problemNumber": "7.1",
                    "title": "HPGe Semiconductor FWHM Energy Resolution from Fano Factor Statistics",
                    "difficulty": "Intermediate",
                    "statement": r"""A High-Purity Germanium (HPGe) spectrometer has an effective Fano factor $F = 0.085$ and requires an average energy $\epsilon = 2.96\text{ eV}$ to create an electron-hole pair at $77\text{ K}$.
Electronic noise contributes an independent electronic FWHM of $\text{FWHM}_{\text{noise}} = 0.85\text{ keV}$.
1. For the $1.3325\text{ MeV}$ gamma ray of Cobalt-60 ($^{60}\text{Co}$), calculate the mean number of charge carriers $N$ generated.
2. Determine the intrinsic statistical energy resolution $\text{FWHM}_{\text{stat}}$ in $\text{keV}$.
3. Calculate the total overall energy resolution $\text{FWHM}_{\text{total}}$ in $\text{keV}$ and as a percentage of peak energy.""",
                    "solution": r"""### Step 1: Mean Number of Charge Carriers $N$
$$N = \frac{E}{\epsilon} = \frac{1,332,500\text{ eV}}{2.96\text{ eV}} \approx 450,169\text{ electron-hole pairs}$$

### Step 2: Intrinsic Statistical Resolution
The standard deviation of carrier count:
$$\sigma_N = \sqrt{F \cdot N} = \sqrt{0.085 \times 450,169} = \sqrt{38,264} \approx 195.61\text{ pairs}$$
Energy standard deviation:
$$\sigma_E = \sigma_N \cdot \epsilon = 195.61 \times 2.96\text{ eV} \approx 579.0\text{ eV} = 0.579\text{ keV}$$
Statistical FWHM:
$$\text{FWHM}_{\text{stat}} = 2.35482 \cdot \sigma_E = 2.35482 \times 0.5790\text{ keV} \approx 1.363\text{ keV}$$

### Step 3: Total Overall Energy Resolution
Electronic noise and statistical fluctuations add in quadrature:
$$\text{FWHM}_{\text{total}} = \sqrt{\text{FWHM}_{\text{stat}}^2 + \text{FWHM}_{\text{noise}}^2} = \sqrt{(1.363\text{ keV})^2 + (0.850\text{ keV})^2}$$
$$\text{FWHM}_{\text{total}} = \sqrt{1.8578 + 0.7225} = \sqrt{2.5803} \approx 1.606\text{ keV}$$

Percentage resolution:
$$\% \text{ Resolution} = \frac{\text{FWHM}_{\text{total}}}{E} \times 100\% = \frac{1.606\text{ keV}}{1332.5\text{ keV}} \times 100\% \approx 0.120\%$$
The peak width is only **$1.61\text{ keV}$** ($0.12\%$), resolving narrow gamma signatures.""",
                    "hints": ["Carrier number N = E / epsilon.", "FWHM_stat = 2.355 * sqrt(F * epsilon * E). Electronic noise adds in quadrature."]
                },
                {
                    "id": "prob-7-2",
                    "problemNumber": "7.2",
                    "title": "Geiger-Müller Dead Time Correction for High Count Rate Radiation Survey",
                    "difficulty": "Easy",
                    "statement": r"""A non-paralyzable Geiger-Müller survey meter with dead time $\tau = 120.0\,\mu\text{s}$ records a count rate of $m = 35,000\text{ counts per minute (cpm)}$ in an industrial radiography enclosure.
1. Convert the observed count rate to counts per second ($\text{cps}$).
2. Calculate the fraction of time the detector is dead.
3. Compute the true incident interaction rate $n$ in $\text{cpm}$ and determine the percentage counting loss.""",
                    "solution": r"""### Step 1: Convert to Counts per Second
$$m = \frac{35,000\text{ cpm}}{60\text{ s/min}} \approx 583.33\text{ cps}$$

### Step 2: Fractional Dead Time
The dead time is $\tau = 120.0\,\mu\text{s} = 1.20 \times 10^{-4}\text{ s}$.
$$m \tau = (583.33\text{ s}^{-1})(1.20 \times 10^{-4}\text{ s}) = 0.0700 \quad (7.00\%)$$
The detector is dead $7\%$ of the time.

### Step 3: True Count Rate and Counting Loss
Using the non-paralyzable dead-time equation:
$$n = \frac{m}{1 - m \tau} = \frac{583.33\text{ cps}}{1 - 0.0700} = \frac{583.33}{0.9300} \approx 627.24\text{ cps}$$
In cpm:
$$n_{\text{cpm}} = 627.24 \times 60 \approx 37,634\text{ cpm}$$
Counting loss:
$$\% \text{ Loss} = \frac{n - m}{n} \times 100\% = \frac{37,634 - 35,000}{37,634} \times 100\% = \frac{2,634}{37,634} \times 100\% \approx 7.00\%$$
Uncorrected, the survey meter underestimates the radiation field by **$2,634\text{ cpm}$** ($7\%$).""",
                    "hints": ["Always convert cpm to cps before multiplying by dead time in seconds.", "True count rate n = m / (1 - m*tau)."]
                },
                {
                    "id": "prob-7-3",
                    "problemNumber": "7.3",
                    "title": "Two-Source Method for Experimental Determination of Detector Dead Time",
                    "difficulty": "Intermediate",
                    "statement": r"""In the experimental two-source method, the dead time $\tau$ of a counter is determined using two sealed sources ($S_1$ and $S_2$):
- Background alone: $R_b = 25\text{ cpm}$
- Source 1 alone: $R_1 = 12,450\text{ cpm}$
- Source 2 alone: $R_2 = 15,380\text{ cpm}$
- Sources 1 and 2 together: $R_{12} = 26,920\text{ cpm}$
1. Convert all rates to counts per second ($\text{cps}$).
2. Using the standard two-source formula:
$$\tau \approx \frac{R_1 + R_2 - R_{12} - R_b}{R_{12}^2 - R_1^2 - R_2^2}$$
compute the experimental dead time $\tau$ in microseconds ($\mu\text{s}$).""",
                    "solution": r"""### Step 1: Rates in Counts per Second
$$R_b = \frac{25}{60} \approx 0.417\text{ cps}$$
$$R_1 = \frac{12,450}{60} = 207.50\text{ cps}$$
$$R_2 = \frac{15,380}{60} = 256.333\text{ cps}$$
$$R_{12} = \frac{26,920}{60} = 448.667\text{ cps}$$

### Step 2: Compute Dead Time $\tau$
Numerator:
$$\Delta R = R_1 + R_2 - R_{12} - R_b = 207.50 + 256.333 - 448.667 - 0.417 = 463.833 - 449.084 = 14.749\text{ cps}$$

Denominator:
$$R_{12}^2 - R_1^2 - R_2^2 = (448.667)^2 - (207.50)^2 - (256.333)^2$$
$$(448.667)^2 \approx 201,302$$
$$(207.50)^2 \approx 43,056$$
$$(256.333)^2 \approx 65,707$$
$$\text{Denominator} = 201,302 - 43,056 - 65,707 = 201,302 - 108,763 = 92,539\text{ cps}^2$$

Compute $\tau$:
$$\tau = \frac{14.749\text{ s}^{-1}}{92,539\text{ s}^{-2}} \approx 1.5938 \times 10^{-4}\text{ s} = 159.4\,\mu\text{s}$$
The detector has an experimental dead time of **$\tau \approx 159\,\mu\text{s}$**.""",
                    "hints": ["Convert all rates from cpm to cps first.", "The numerator represents the count rate deficit due to dead time losses."]
                },
                {
                    "id": "prob-7-4",
                    "problemNumber": "7.4",
                    "title": "Photomultiplier Tube Gain and Anode Charge Pulse Amplitude",
                    "difficulty": "Easy",
                    "statement": r"""A 10-stage photomultiplier tube (PMT) has an average secondary emission ratio $\delta = 4.80$ per dynode.
A scintillation event in a $\text{NaI(Tl)}$ crystal ejects $N_{pe} = 2,500\text{ photoelectrons}$ from the photocathode into the first dynode.
1. Calculate the overall electron current gain $G = \delta^n$ of the PMT.
2. Determine the total electrical charge $Q$ collected at the anode in picocoulombs ($\text{pC}$).
3. If the anode load circuit has a capacitance $C = 50.0\text{ pF}$, calculate the peak voltage amplitude $V_{\text{peak}}$ of the output pulse.""",
                    "solution": r"""### Step 1: PMT Current Gain $G$
$$G = \delta^n = (4.80)^{10} \approx 6.4925 \times 10^6$$
The multiplication gain is **$\approx 6.49 \times 10^6$**.

### Step 2: Total Anode Charge $Q$
$$Q = N_{pe} \cdot G \cdot e$$
$$Q = (2500)(6.4925 \times 10^6)(1.60218 \times 10^{-19}\text{ C}) = 1.6231 \times 10^{10} \times 1.60218 \times 10^{-19}\text{ C} \approx 2.6005 \times 10^{-9}\text{ C} = 2,600\text{ pC} = 2.60\text{ nC}$$

### Step 3: Peak Voltage Amplitude
$$V_{\text{peak}} = \frac{Q}{C} = \frac{2.6005 \times 10^{-9}\text{ C}}{50.0 \times 10^{-12}\text{ F}} \approx 52.01\text{ Volts}$$
With a $50\text{ pF}$ load, the output pulse is a massive **$52.0\text{ Volts}$** (in practice, smaller anode loads or preamplifiers shape this into a $0.5 - 2\text{ V}$ pulse).""",
                    "hints": ["PMT gain is G = delta^n.", "Charge Q = N_pe * G * e, and voltage V = Q / C."]
                },
                {
                    "id": "prob-7-5",
                    "problemNumber": "7.5",
                    "title": "Proportional Counter Electric Field Gradient and Gas Avalanche Threshold",
                    "difficulty": "Intermediate",
                    "statement": r"""A cylindrical proportional counter has an inner cathode radius $b = 1.50\text{ cm}$ and a central tungsten anode wire of radius $a = 25.0\,\mu\text{m}$ ($0.00250\text{ cm}$).
The tube is filled with P-10 gas at 1 atmosphere, for which the threshold electric field for Townsend secondary ionization is $E_{\text{crit}} = 1.00 \times 10^4\text{ V/cm}$.
The applied voltage between anode and cathode is $V_0 = 1,800\text{ V}$.
1. Calculate the electric field at the cathode surface ($r = b$) and at the anode surface ($r = a$).
2. Determine the critical avalanche radius $r_{\text{crit}}$ inside which secondary multiplication occurs.
3. Express the avalanche volume as a percentage of the total detector gas volume.""",
                    "solution": r"""### Step 1: Electric Field Formula
$$E(r) = \frac{V_0}{r \ln(b/a)}$$
Calculate logarithmic term:
$$\frac{b}{a} = \frac{1.50\text{ cm}}{0.00250\text{ cm}} = 600.0$$
$$\ln\left(\frac{b}{a}\right) = \ln(600) \approx 6.3969$$
At anode surface ($r = a = 0.00250\text{ cm}$):
$$E(a) = \frac{1800\text{ V}}{(0.00250\text{ cm})(6.3969)} = \frac{1800}{0.015992} \approx 1.1255 \times 10^5\text{ V/cm}$$
At cathode surface ($r = b = 1.50\text{ cm}$):
$$E(b) = \frac{1800\text{ V}}{(1.50\text{ cm})(6.3969)} = \frac{1800}{9.5954} \approx 187.6\text{ V/cm}$$

### Step 2: Critical Avalanche Radius $r_{\text{crit}}$
Set $E(r_{\text{crit}}) = E_{\text{crit}} = 1.00 \times 10^4\text{ V/cm}$:
$$r_{\text{crit}} = \frac{V_0}{E_{\text{crit}} \ln(b/a)} = \frac{1800\text{ V}}{(1.00 \times 10^4\text{ V/cm})(6.3969)} = \frac{1800}{63,969} \approx 0.02814\text{ cm} = 281.4\,\mu\text{m}$$

### Step 3: Avalanche Volume Percentage
Volume scales as radius squared:
$$\frac{V_{\text{avalanche}}}{V_{\text{total}}} = \frac{\pi (r_{\text{crit}}^2 - a^2) L}{\pi (b^2 - a^2) L} \approx \left(\frac{r_{\text{crit}}}{b}\right)^2 = \left(\frac{0.02814\text{ cm}}{1.50\text{ cm}}\right)^2 = (0.01876)^2 \approx 0.000352 \quad (0.035\%)$$
Secondary multiplication is confined strictly to a microscopic sheath extending only **$256\,\mu\text{m}$** from the wire, occupying less than **$0.04\%$** of the tube volume! This confinement ensures all avalanches experience identical gas gain.""",
                    "hints": ["Electric field in cylindrical geometry is E(r) = V / [r * ln(b/a)].", "Solve for r when E(r) = E_crit."]
                },
                {
                    "id": "prob-7-6",
                    "problemNumber": "7.6",
                    "title": "Scintillation Pulse Light Output and Preamplifier Statistics in NaI(Tl)",
                    "difficulty": "Intermediate",
                    "statement": r"""A $2.0\text{ inch} \times 2.0\text{ inch}$ $\text{NaI(Tl)}$ detector detects a $661.7\text{ keV}$ gamma ray from $^{137}\text{Cs}$.
- Scintillation efficiency: $38.0\text{ optical photons/keV}$
- Light collection efficiency onto photocathode: $\eta_{\text{coll}} = 75\%$
- Photocathode quantum efficiency: $\text{QE} = 28\%$
1. Calculate the total number of optical photons $N_{\text{phot}}$ generated in the crystal.
2. Determine the number of photoelectrons $N_{pe}$ reaching the first dynode.
3. Assuming Poisson statistics for photoelectron production, calculate the theoretical statistical limit of energy resolution $\text{FWHM} / E$ in percent.""",
                    "solution": r"""### Step 1: Scintillation Photons Generated
$$N_{\text{phot}} = 661.7\text{ keV} \times 38.0\text{ photons/keV} \approx 25,145\text{ optical photons}$$

### Step 2: Photoelectrons Ejected
$$N_{pe} = N_{\text{phot}} \cdot \eta_{\text{coll}} \cdot \text{QE} = 25,145 \times 0.75 \times 0.28 \approx 5,280\text{ photoelectrons}$$

### Step 3: Statistical Resolution Limit
The relative statistical standard deviation of photoelectron count is:
$$\frac{\sigma}{N_{pe}} = \frac{1}{\sqrt{N_{pe}}} = \frac{1}{\sqrt{5280}} = \frac{1}{72.66} \approx 0.01376$$
Statistical Full Width at Half Maximum (FWHM):
$$\frac{\text{FWHM}_{\text{stat}}}{E} = 2.355 \left(\frac{\sigma}{N_{pe}}\right) = 2.355 \times 0.01376 \approx 0.0324 \quad (3.24\%)$$
Accounting for dynode multiplication variance ($1 + 1/\delta$) and non-proportional crystal response, the actual observed FWHM of $\text{NaI(Tl)}$ at $662\text{ keV}$ is $\approx 6.5 - 7.0\%$, consistent with theoretical limits.""",
                    "hints": ["Multiply energy by photon yield per keV to get total scintillation photons.", "Photoelectrons = Photons * Collection Efficiency * Quantum Efficiency."]
                },
                {
                    "id": "prob-7-7",
                    "problemNumber": "7.7",
                    "title": "HPGe Cryogenic Depletion Depth and Electric Bias Field",
                    "difficulty": "Advanced",
                    "statement": r"""A planar p-type High-Purity Germanium detector has a net acceptor concentration $|N_A - N_D| = 1.20 \times 10^{10}\text{ cm}^{-3}$.
The dielectric constant of germanium is $\varepsilon_r = 16.0$ ($\varepsilon = \varepsilon_r \varepsilon_0 = 16.0 \times 8.854 \times 10^{-14}\text{ F/cm}$).
1. Calculate the reverse bias voltage $V$ required to achieve a full depletion depth of $W = 3.00\text{ cm}$.
2. Determine the maximum electric field $E_{\max}$ in the crystal at this bias voltage.""",
                    "solution": r"""### Step 1: Required Reverse Bias Voltage
From semiconductor junction theory:
$$W = \sqrt{\frac{2 \varepsilon V}{e |N_A - N_D|}} \implies W^2 = \frac{2 \varepsilon V}{e |N_A - N_D|}$$
$$V = \frac{e |N_A - N_D| W^2}{2 \varepsilon}$$
Given:
- $e = 1.60218 \times 10^{-19}\text{ C}$
- $|N_A - N_D| = 1.20 \times 10^{10}\text{ cm}^{-3}$
- $W = 3.00\text{ cm} \implies W^2 = 9.00\text{ cm}^2$
- $\varepsilon = 16.0 \times 8.854 \times 10^{-14}\text{ F/cm} = 1.4166 \times 10^{-12}\text{ F/cm}$

Numerator:
$$e |N_A - N_D| W^2 = (1.60218 \times 10^{-19})(1.20 \times 10^{10})(9.00) = 1.73035 \times 10^{-8}\text{ C/cm}$$
Denominator:
$$2 \varepsilon = 2 \times 1.4166 \times 10^{-12}\text{ F/cm} = 2.8333 \times 10^{-12}\text{ F/cm}$$
$$V = \frac{1.73035 \times 10^{-8}}{2.8333 \times 10^{-12}} \approx 6,107\text{ Volts}$$
A bias of **$\approx 6,100\text{ Volts}$** is required to fully deplete a $3\text{ cm}$ thick planar HPGe crystal.

### Step 2: Maximum Electric Field $E_{\max}$
In a planar one-sided junction, the electric field increases linearly to a maximum at the junction interface:
$$E_{\max} = \frac{2 V}{W} = \frac{2(6107\text{ V})}{3.00\text{ cm}} \approx 4,071\text{ V/cm}$$
This field ($>1000\text{ V/cm}$) exceeds the saturation drift velocity threshold for both electrons and holes ($\approx 10^7\text{ cm/s}$), ensuring fast, complete charge collection.""",
                    "hints": ["Depletion depth formula: W = sqrt(2 * epsilon * V / (e * N)).", "Maximum electric field in planar junction is E_max = 2*V / W."]
                }
            ]
        },

        # =====================================================================
        # UNIT 8
        # =====================================================================
        {
            "id": "unit-8-nuclear-analytical-techniques",
            "unitNumber": 8,
            "title": "Unit 8: Nuclear Analytical Techniques: NAA, IDA & Radiocarbon Dating",
            "leadSummary": "Comprehensive mathematical and instrumental analysis of nuclear analytical methods: Neutron Activation Analysis (NAA) saturation kinetics, prompt versus delayed gamma spectroscopy, and standard comparator metrology; Isotope Dilution Analysis (IDA) in direct, reverse, and substoichiometric modes; radiometric precipitation titrations; cosmogenic radiocarbon production, Libby decay kinetics, Accelerator Mass Spectrometry (AMS), and dendrochronological calibration.",
            "simulations": ["sim_nuc_neutron_activation_analysis"],
            "sections": [
                {
                    "id": "sec-8-1",
                    "secNumber": "8.1",
                    "title": "Neutron Activation Analysis (NAA): Thermal Neutron Capture, Irradiation Kinetics & Saturation",
                    "content": r"""Neutron Activation Analysis (NAA), developed by George de Hevesy and Hilde Levi in 1936, is an ultra-sensitive, non-destructive analytical technique for multi-elemental trace and ultra-trace determination (detection limits down to $10^{-9} - 10^{-12}\text{ g}$).

### The Physical Principle of NAA
A sample containing an analyte target nucleus $^{A}_{Z}\text{X}$ is irradiated in a high thermal neutron flux $\Phi_{\text{th}}$ ($10^{12} - 10^{14}\text{ n/cm}^2\cdot\text{s}$) in a research reactor.
The nucleus undergoes radiative capture $(n, \gamma)$:
$$^{A}_{Z}\text{X} + ^1_0n_{\text{th}} \longrightarrow [^{A+1}_{Z}\text{X}^*] \xrightarrow[\text{Prompt }\gamma]{<10^{-14}\text{ s}} \, ^{A+1}_{Z}\text{X} \xrightarrow[\beta^-, \, \text{Delayed }\gamma]{T_{1/2}} \, ^{A+1}_{Z+1}\text{Y}$$
The created radionuclide $^{A+1}_{Z}\text{X}$ decays with characteristic half-life $T_{1/2}$, emitting delayed gamma-ray photons with discrete energies that uniquely identify the isotope.

### Mathematical Derivation of the Activation Saturation Equation
Let $N_0$ be the number of stable target nuclei in the sample, $\sigma_{\text{act}}$ the thermal neutron capture cross-section ($\text{cm}^2$), and $\Phi$ the neutron flux ($\text{n/cm}^2\cdot\text{s}$).
Assuming target burnup is negligible ($\sigma \Phi \ll \lambda$):
$$\frac{dN^*}{dt} = R_{\text{production}} - R_{\text{decay}} = N_0 \sigma_{\text{act}} \Phi - \lambda N^*(t)$$
Solving with initial condition $N^*(0) = 0$ via integrating factor $e^{\lambda t}$:
$$N^*(t_{\text{irr}}) = \frac{N_0 \sigma_{\text{act}} \Phi}{\lambda} \left( 1 - e^{-\lambda t_{\text{irr}}} \right)$$
The induced activity $A(t_{\text{irr}}) = \lambda N^*(t_{\text{irr}})$ at the end of irradiation ($EOI$) is:
$$A_{\text{EOI}} = N_0 \sigma_{\text{act}} \Phi \left( 1 - e^{-\lambda t_{\text{irr}}} \right)$$

```
 Induced Activity A(t)
    ▲
A_sat│─────────────────────────────────── Saturation Activity A_sat = N₀ σ Φ
     │                                /
     │                              /
     │                            /
A_sat/2 ────────────────────────/──────── (Irradiation Time t_irr = T₁/₂)
     │                       /
     │_____________________/
     └─────────────────────┴─────────────► Irradiation Time t_irr
                           T₁/₂
```

The term $(1 - e^{-\lambda t_{\text{irr}}})$ is the **saturation factor**:
- For $t_{\text{irr}} \ll T_{1/2}$: $A \approx N_0 \sigma \Phi (\lambda t_{\text{irr}})$, growing linearly.
- For $t_{\text{irr}} = T_{1/2}$: $A = 0.50 A_{\text{sat}}$ ($50\%$ of maximum achievable activity).
- For $t_{\text{irr}} = 3 T_{1/2}$: $A = 0.875 A_{\text{sat}}$ ($87.5\%$).
- For $t_{\text{irr}} \ge 6 - 7 T_{1/2}$: $A \to A_{\text{sat}} = N_0 \sigma_{\text{act}} \Phi$ (**Saturation** occurs; production rate equals decay rate, and further irradiation yields zero additional activity!).

### Cooling and Counting Phases
Following irradiation, the sample is allowed to "cool" for decay time $t_d$ (to allow short-lived matrix interferences such as $^{28}\text{Al}$ [$2.24\text{ min}$] and $^{24}\text{Na}$ [$15.0\text{ h}$] to decay away):
$$A(t_d) = A_{\text{EOI}} \cdot e^{-\lambda t_d}$$
The sample is then counted on an HPGe detector for counting time $t_c$.
The total net gamma counts $C$ collected in the photopeak is:
$$C = \int_0^{t_c} \epsilon_\gamma I_\gamma A(t_d) e^{-\lambda t'} dt' = \frac{\epsilon_\gamma I_\gamma}{\lambda} N_0 \sigma_{\text{act}} \Phi \left(1 - e^{-\lambda t_{\text{irr}}}\right) e^{-\lambda t_d} \left(1 - e^{-\lambda t_c}\right)$$
where:
- $\epsilon_\gamma$ is the full-energy peak detection efficiency at that gamma energy.
- $I_\gamma$ is the absolute gamma emission probability (branching intensity).""",
                    "simulations": ["sim_nuc_neutron_activation_analysis"]
                },
                {
                    "id": "sec-8-2",
                    "secNumber": "8.2",
                    "title": "Instrumental (INAA) Versus Radiochemical (RNAA) Protocols & Standard Comparator Metrology",
                    "content": r"""Neutron Activation Analysis is implemented via two distinct protocols depending on matrix interferences:

### 1. Instrumental Neutron Activation Analysis (INAA)
In INAA, the sample is irradiated and counted **purely instrumentally without chemical dissolution or separations**:
- **Advantages**: Completely non-destructive (essential for precious archaeological artifacts, moon rocks, forensic evidence), zero reagent blank contamination, and handles hundreds of elements simultaneously.
- **Protocol**: Samples are typically irradiated twice:
  - Short irradiation ($1 - 5\text{ min}$) for short-lived isotopes: $^{52}\text{V}$ ($3.75\text{ min}$), $^{28}\text{Al}$ ($2.24\text{ min}$), $^{56}\text{Mn}$ ($2.58\text{ h}$).
  - Long irradiation ($10 - 50\text{ hours}$) followed by long cooling ($7 - 30\text{ days}$) for trace elements: $^{46}\text{Sc}$, $^{51}\text{Cr}$, $^{59}\text{Fe}$, $^{60}\text{Co}$, $^{75}\text{Se}$, $^{140}\text{La}$, $^{152}\text{Eu}$, $^{181}\text{Hf}$, $^{198}\text{Au}$.

### 2. Radiochemical Neutron Activation Analysis (RNAA)
When matrix radionuclides (such as $^{24}\text{Na}$, $^{38}\text{Cl}$, $^{82}\text{Br}$) emit overwhelming Compton backgrounds that drown out trace analyte peaks, **post-irradiation chemical separation** is performed:
- A non-radioactive stable carrier of the analyte element ($10 - 20\text{ mg}$) is added.
- The sample is digested in boiling mineral acids ($\text{HNO}_3 / \text{HF} / \text{HClO}_4$).
- The target element is separated via precipitation, solvent extraction, or ion-exchange chromatography.
- Yield corrections are determined gravimetrically using the added stable carrier.

### The Standard Comparator Method
In practice, absolute quantification using the master NAA equation is difficult because neutron flux $\Phi$, cross-section $\sigma$, and absolute detector efficiency $\epsilon_\gamma$ have experimental uncertainties.
Instead, analytical laboratories universally use the **Standard Comparator Method**:
A certified reference standard containing known mass $m_{\text{std}}$ of the analyte is co-irradiated simultaneously in the exact same flux rabbit alongside the unknown sample of mass $m_{\text{unk}}$:

Because $\Phi, \sigma, t_{\text{irr}}$, and $\epsilon_\gamma$ are identical:
$$\frac{A_{\text{unk}}}{A_{\text{std}}} = \frac{m_{\text{unk}}}{m_{\text{std}}} \cdot \frac{e^{-\lambda t_{d,\text{unk}}}}{e^{-\lambda t_{d,\text{std}}}}$$
Correcting for cooling decay differences:
$$m_{\text{unk}} = m_{\text{std}} \cdot \left(\frac{C_{\text{unk}}}{C_{\text{std}}}\right) \cdot \left(\frac{1 - e^{-\lambda t_{c,\text{std}}}}{1 - e^{-\lambda t_{c,\text{unk}}}}\right) \cdot \exp\left[ \lambda (t_{d,\text{unk}} - t_{d,\text{std}}) \right]$$
All complex nuclear parameters ($\Phi, \sigma, I_\gamma, \epsilon$) cancel completely, achieving analytical precisions better than $\pm 1\%$.""",
                    "simulations": ["sim_nuc_neutron_activation_analysis"]
                },
                {
                    "id": "sec-8-3",
                    "secNumber": "8.3",
                    "title": "Isotope Dilution Analysis (IDA): Direct, Reverse & Substoichiometric Formulations",
                    "content": r"""Isotope Dilution Analysis (IDA), pioneered by George de Hevesy, is a quantitative analytical method based on measuring the **change in isotopic specific activity** caused by mixing an unknown sample with an isotopically enriched spike.

The fundamental advantage of IDA is that **quantitative (100%) chemical recovery is NOT required**! Once isotopic equilibrium is achieved, any fraction of pure analyte isolated from the mixture retains the identical isotopic ratio.

### 1. Direct Isotope Dilution Analysis
Used to determine the unknown mass $m_x$ of a non-radioactive element in a complex sample matrix.
1. A known mass $m_1$ of the analyte labeled with a radioactive tracer having known activity $A_1$ (and specific activity $S_1 = A_1 / m_1$) is added to the sample.
2. The mixture is homogenized chemically to achieve complete isotopic exchange.
3. A small portion of pure analyte of mass $m_2$ is chemically isolated and its radioactivity $A_2$ is counted, giving diluted specific activity $S_2 = A_2 / m_2$.

By conservation of radioactivity:
$$A_1 = S_1 m_1 = S_2 (m_x + m_1)$$
Solving for the unknown mass $m_x$:
$$m_x + m_1 = m_1 \frac{S_1}{S_2} \implies m_x = m_1 \left( \frac{S_1}{S_2} - 1 \right)$$
If the mass of the radioactive spike is negligible ($m_1 \ll m_x$):
$$m_x \approx m_1 \frac{S_1}{S_2} = \frac{A_1}{S_2}$$

```
 Unknown Sample m_x (Stable)    Spike m₁ with Activity A₁ (S₁ = A₁/m₁)
             │                                   │
             └───────────────► MIX ◄─────────────┘
                               │
                               ▼ Complete Isotopic Equilibration
                    Total Mass: m_x + m₁
                    Diluted Specific Activity: S₂ = A₁ / (m_x + m₁)
                               │
                               ▼ Isolate Partial Pure Mass m₂
                    Measure S₂ = A₂ / m₂  ──► Compute m_x!
```

### 2. Reverse Isotope Dilution Analysis
Used when the substance to be determined is already radioactive ($A_x$, mass $m_x$, $S_x = A_x / m_x$).
A known, large mass $m_1$ of pure non-radioactive carrier ($S_1 = 0$) is added.
After equilibration and partial isolation of pure substance:
$$m_x = m_1 \left( \frac{S_2}{S_x - S_2} \right) \approx m_1 \frac{S_2}{S_x}$$

### 3. Substoichiometric Isotope Dilution Analysis
In classical direct IDA, measuring the diluted specific activity $S_2 = A_2 / m_2$ requires measuring both the radioactivity $A_2$ and the isolated mass $m_2$ (via gravimetry, spectrophotometry, or micro-balance). At sub-microgram trace levels, measuring $m_2$ accurately is impossible.

In 1958, Jaromír Růžička and Jiří Starý introduced **Substoichiometric IDA**:
1. Two solutions are prepared:
   - Solution 1: Standard containing known mass $m_s$ with activity $A_s$.
   - Solution 2: Sample containing unknown mass $m_x$ with identical spike activity $A_1$.
2. To both solutions, an **exact, identical substoichiometric amount of chelating reagent** (e.g., dithizone, cupferron, or EDTA) is added ($n_{\text{reagent}} < n_{\text{analyte}}$).
3. Because the reagent is limiting, it reacts with and extracts **exactly the identical mass $m_{\text{sub}}$** of analyte from both solutions:
$$m_2^{\text{sample}} = m_2^{\text{standard}} = m_{\text{sub}}$$
4. The activities of the extracted complexes ($a_x$ and $a_s$) are counted:
$$S_x = \frac{a_x}{m_{\text{sub}}} \quad \text{and} \quad S_s = \frac{a_s}{m_{\text{sub}}}$$
Because $m_{\text{sub}}$ cancels identically:
$$m_x = m_s \left(\frac{a_s}{a_x}\right) - m_1$$
Mass determination is eliminated completely, extending detection limits to the picogram ($10^{-12}\text{ g}$) regime!""",
                    "simulations": ["sim_nuc_neutron_activation_analysis"]
                },
                {
                    "id": "sec-8-4",
                    "secNumber": "8.4",
                    "title": "Radiometric Titrations: Precipitation, Complexation & Phase-Separation Endpoints",
                    "content": r"""A **radiometric titration** is a volumetric analytical titration in which the endpoint is identified by monitoring the radioactivity of the solution or precipitate as a function of added titrant volume.

### Operating Principles & Phase Separation
In radiometric titrimetry:
1. Either the analyte $A$, the titrant $B$, or an auxiliary indicator is labeled with a radioactive tracer.
2. The reaction must produce two separable physical phases (typically a solid precipitate and a liquid supernatant, or an organic solvent extraction phase).
3. After each increment of titrant, the phases are separated (via centrifugation, filtration, or settling) and the radioactivity of the supernatant phase is counted.

### The Three Morphological Titration Curves

```
 Case 1: Labeled Analyte          Case 2: Labeled Titrant          Case 3: Both Labeled
 Supernatant Activity             Supernatant Activity             Supernatant Activity
  ▲                                ▲                                ▲
A₀│\                               │              /                A₀│\             /
  │ \                              │             /                   │ \           /
  │  \                             │            /                    │  \         /
  │   \____________                │___________/                     │   \_______/
  └────┴───────────► Vol V         └────┴──────────► Vol V           └────┴───────► Vol V
      V_eq                             V_eq                              V_eq
```

1. **Case 1: Only Analyte Labeled ($A^*$ + $B \to A^*B \downarrow$)**:
As non-radioactive titrant $B$ is added, the labeled analyte precipitates out. The activity of the supernatant decreases linearly until the equivalence point $V_{\text{eq}}$, where all analyte has precipitated. Beyond $V_{\text{eq}}$, the activity remains flat at the solubility product baseline.
Example: Titration of radioactive $^{110m}\text{Ag}^+$ with non-radioactive $\text{Cl}^-$.
2. **Case 2: Only Titrant Labeled ($A$ + $B^* \to AB^* \downarrow$)**:
Prior to equivalence, added radioactive titrant precipitates immediately with excess analyte; the supernatant activity remains near zero. Beyond $V_{\text{eq}}$, unreacted labeled titrant accumulates in the supernatant, causing activity to rise linearly.
Example: Titration of non-radioactive $\text{SO}_4^{2-}$ with radioactive $^{133}\text{Ba}^{2+}$.
3. **Case 3: Both Analyte and Titrant Labeled**:
Activity falls linearly to equivalence and rises linearly thereafter, forming an inverted V-shaped curve.

### Quantitative Advantages
- Unaffected by turbidity, intense color, or colloidal suspensions that make visual indicators useless.
- Operates at extreme dilutions ($10^{-5} - 10^{-7}\text{ M}$) where potentiometric electrodes lose Nernstian slope.
- Can be automated using continuous flow cells with scintillation counters.""",
                    "simulations": ["sim_nuc_neutron_activation_analysis"]
                },
                {
                    "id": "sec-8-5",
                    "secNumber": "8.5",
                    "title": "Cosmogenic Radionuclides & Physical Foundations of Radiocarbon Dating ($^{14}\text{C}$)",
                    "content": r"""Radiocarbon dating, developed by Willard F. Libby in 1949 (Nobel Prize in Chemistry, 1960), provides absolute chronometric dating of carbonaceous organic materials up to $\sim 50,000\text{ years}$ old.

### Cosmogenic Production of Carbon-14
Primary galactic cosmic rays (predominantly relativistic protons) interact with upper atmospheric nuclei, creating spallation thermal neutrons.
These thermal neutrons capture on atmospheric nitrogen-14 ($^{14}_{7}\text{N}$, $99.63\%$ natural abundance) via an exoergic $(n, p)$ reaction:
$$^{14}_{7}\text{N} + ^1_0n_{\text{th}} \longrightarrow ^{14}_{6}\text{C} + ^1_1p \quad (Q = +0.626\text{ MeV})$$
The production rate in the stratosphere and troposphere is approximately:
$$Q \approx 2.0 - 2.5\text{ }^{14}\text{C atoms / cm}^2\cdot\text{s}$$

### The Carbon Dynamic Reservoir & Secular Steady State
The newly formed $^{14}\text{C}$ atoms are rapidly oxidized to carbon monoxide and carbon dioxide:
$$^{14}\text{C} + \text{O}_2 \longrightarrow ^{14}\text{CO} \xrightarrow{\cdot\text{OH}} \, ^{14}\text{CO}_2$$
The radioactive $^{14}\text{CO}_2$ mixes globally within weeks into the troposphere and dissolves into the global dynamic carbon reservoir (atmosphere, terrestrial biosphere, surface oceans, and deep oceans).

Carbon-14 decays via pure negative beta decay to stable nitrogen-14:
$$^{14}_{6}\text{C} \xrightarrow[\beta^-]{T_{1/2}} \, ^{14}_{7}\text{N} + e^- + \bar{\nu}_e \quad (E_{\max} = 156.5\text{ keV})$$
- **Libby Half-Life** (used by international convention for raw radiocarbon ages): $T_{1/2} = 5,568\pm 30\text{ years}$ ($\lambda_{\text{Libby}} = 1.2446 \times 10^{-4}\text{ yr}^{-1}$).
- **Cambridge Half-Life** (accurate physical value): $T_{1/2} = 5,730\pm 40\text{ years}$ ($\lambda = 1.2097 \times 10^{-4}\text{ yr}^{-1}$).

Because $^{14}\text{C}$ production has operated for millions of years ($t \gg T_{1/2}$), production and decay reached **secular equilibrium**:
$$R_{\text{production}} = R_{\text{decay}} = \lambda N_{14}$$
In living equilibrium prior to the industrial revolution, the specific activity of carbon in all living organic tissue was:
$$A_0 \approx 15.3\text{ disintegrations per minute per gram of carbon (dpm/g C)} \approx 0.255\text{ Bq/g C}$$
Corresponding to an isotopic ratio:
$$\left(\frac{^{14}\text{C}}{^{12}\text{C}}\right)_0 \approx 1.2 \times 10^{-12}$$

### The Post-Mortem Clock
Living organisms continuously assimilate $^{14}\text{CO}_2$ through photosynthesis (plants) or ingestion (animals), maintaining the steady-state isotopic ratio.
Upon death, metabolic exchange halts immediately. The radioactive carbon-14 clock begins ticking as $^{14}\text{C}$ decays away:
$$A(t) = A_0 e^{-\lambda t} \implies t = \frac{1}{\lambda} \ln\left(\frac{A_0}{A(t)}\right) = \frac{T_{1/2}}{\ln 2} \ln\left(\frac{A_0}{A(t)}\right)$$

```
 Specific Activity A(t) [dpm/g C]
 15.3 ▲ (Death: t = 0)
      │\
      │ \
  7.65│--\-------------------------- T₁/₂ = 5,730 yr
      │   \
  3.83│----\------------------------ 2 T₁/₂ = 11,460 yr
      │     \
  1.91│------\---------------------- 3 T₁/₂ = 17,190 yr
      │       \_____________________ Background Detection Limit (~50,000 yr)
      └────────┴──────┴──────┴──────► Radiocarbon Age t
```

After 10 half-lives ($57,300\text{ years}$), the remaining $^{14}\text{C}$ activity is $0.015\text{ dpm/g C}$, reaching the analytical detection background.""",
                    "simulations": ["sim_nuc_neutron_activation_analysis"]
                },
                {
                    "id": "sec-8-6",
                    "secNumber": "8.6",
                    "title": "Accelerator Mass Spectrometry (AMS) Versus Beta Counting & Dendrochronological Calibration",
                    "content": r"""Radiocarbon metrology underwent a revolution in the late 1970s with the invention of **Accelerator Mass Spectrometry (AMS)**.

### Radiometric Beta Counting Versus AMS
1. **Beta Counting (Liquid Scintillation / Proportional Gas Counters)**:
Measures the radioactive decay rate $A = \lambda N$.
Because the half-life of $^{14}\text{C}$ is long ($5,730\text{ years} \approx 3.0 \times 10^9\text{ minutes}$), only one atom out of every $4.3 \times 10^9$ decays each minute!
To obtain 10,000 counts in 24 hours, traditional beta counting required **$1.0 - 10.0\text{ grams}$** of pure elemental carbon (destroying significant portions of precious artifacts).
2. **Accelerator Mass Spectrometry (AMS)**:
Directly counts individual $^{14}\text{C}$ atoms using an electrostatic tandem particle accelerator, bypassing radioactive decay entirely:
- **Sample Mass**: Requires only **$0.2 - 1.0\text{ milligram}$** of carbon (a single fiber of wood, bone, or parchment)!
- **Eliminating Isobaric Interference ($^{14}\text{N}$)**:
  Stable $^{14}\text{N}$ has identical nominal mass ($A = 14$) and is $10^{12}$ times more abundant. In an AMS cesium sputter ion source, negative ions are produced. Nitrogen **does not form a stable negative ion** ($\text{N}^-$ is unbound), completely eliminating atomic nitrogen!
- **Stripping Molecular Isobars ($^{12}\text{CH}_2^-$, $^{13}\text{CH}^-$)**:
  The negative ions ($\text{C}^-$) accelerate into a terminal at $+2 - 3\text{ MV}$, passing through a carbon foil or argon gas stripper. Stripping strips $3 - 4$ electrons, transforming ions to $\text{C}^{3+}$ or $\text{C}^{4+}$, and completely dissociating all molecular ions via Coulomb explosion!
- High-resolution magnetic and electrostatic spectrometers count individual $^{14}\text{C}$ ions with precision better than $\pm 0.2\%$.

### Dendrochronological Calibration Curves (IntCal)
Libby assumed that the atmospheric $^{14}\text{C} / ^{12}\text{C}$ production ratio was constant over geological time. In reality, it fluctuates due to:
1. **Geomagnetic Field Modulation**: Fluctuations in Earth's dipole magnetic moment deflect varying fractions of incoming cosmic rays.
2. **Heliomagnetic Solar Cycles**: Solar sunspot activity (Maunder Minimum, Spörer Minimum) modulates the solar wind magnetic shield.
3. **The Suess Effect (Industrial Era)**: Burning vast quantities of fossil fuels (coal, oil, gas millions of years old, completely devoid of $^{14}\text{C}$) diluted atmospheric $^{14}\text{C}$ between 1850 and 1950.
4. **Bomb Pulse (1950s-1960s)**: Atmospheric thermonuclear weapons testing nearly **doubled** atmospheric $^{14}\text{C}$ by 1963!

To convert conventional radiocarbon years into calibrated calendar dates ($\text{cal BC / cal AD}$), international calibration curves (e.g., **IntCal20**) calibrate raw radiocarbon determinations against independently dated tree rings (dendrochronology of bristlecone pines and Irish oaks extending back 14,000 years), speleothems, and varved lake sediments.""",
                    "simulations": ["sim_nuc_neutron_activation_analysis"]
                },
                {
                    "id": "sec-8-7",
                    "secNumber": "8.7",
                    "title": "Radiotracer Applications in Reaction Mechanisms, Solid-State Diffusion & Metabolic Tracing",
                    "content": r"""The physical identity of chemical properties between radioisotopes and stable isotopes of the same element enables the use of **radiotracers** across chemistry, biology, and materials science.

### 1. Organic and Inorganic Reaction Mechanism Elucidation
Radiotracers establish the exact bond cleavage and atom transfer pathways in chemical reactions:
- **Ester Hydrolysis**:
  Hydrolyzing ethyl acetate with $^{18}\text{O}$-enriched water:
  $$\text{CH}_3\text{COOCH}_2\text{CH}_3 + \text{H}_2^{18}\text{O} \longrightarrow \text{CH}_3\text{CO}^{18}\text{OH} + \text{CH}_3\text{CH}_2\text{OH}$$
  The heavy oxygen labels the acetic acid, proving conclusively that acyl-oxygen cleavage occurs rather than alkyl-oxygen cleavage.
- **Photosynthetic Dark Reactions (Calvin Cycle)**:
  Melvin Calvin fed unicellular green algae (*Chlorella*) with $^{14}\text{CO}_2$ for brief intervals ($2 - 5\text{ seconds}$), quenched the cells in boiling ethanol, and separated metabolites via 2D paper chromatography and autoradiography. He identified **3-phosphoglycerate** as the initial product of photosynthetic carbon fixation (Nobel Prize in Chemistry, 1961).

### 2. Self-Diffusion in Solid-State Materials
Classical chemical gradients cannot measure **self-diffusion** (the diffusion of an element through its own crystal lattice, e.g., copper atoms diffusing through pure solid copper).
- A sub-micron layer of radioactive $^{64}\text{Cu}$ is electroplated onto a polished face of a pure copper cylinder.
- The specimen is annealed in a tube furnace at temperature $T$ for time $t$.
- Thin microtome slices of thickness $\Delta x$ are sectioned parallel to the interface and counted:
$$C(x, t) = \frac{M}{\sqrt{\pi D t}} \exp\left(-\frac{x^2}{4 D t}\right)$$
Plotting $\ln C(x)$ versus $x^2$ yields a slope of $-1/(4Dt)$, determining the self-diffusion coefficient $D$ with extreme accuracy. Repeating at multiple temperatures yields the activation energy $Q$ for vacancy migration via the Arrhenius equation:
$$D(T) = D_0 \exp\left(-\frac{Q}{R T}\right)$$

### 3. Trace Equilibrium Constants and Solubility Products
Radionuclides determine solubility products ($K_{\text{sp}}$) of refractory precipitates far beyond the detection limits of atomic absorption or gravimetry.
For lead sulfate ($\text{PbSO}_4$) labeled with $^{210}\text{Pb}$:
Equilibrating labeled $\text{PbSO}_4$ with pure water, centrifuging, and counting the supernatant activity yields dissolved $[\text{Pb}^{2+}]$ directly down to $10^{-10}\text{ M}$.""",
                    "simulations": ["sim_nuc_neutron_activation_analysis"]
                }
            ],
            "problems": [
                {
                    "id": "prob-8-1",
                    "problemNumber": "8.1",
                    "title": "Neutron Activation Analysis Trace Gold Determination in Geological Ore",
                    "difficulty": "Intermediate",
                    "statement": r"""A $50.0\text{ mg}$ rock specimen is analyzed for trace gold via INAA using the reaction:
$$^{197}_{79}\text{Au} + ^1_0n \longrightarrow ^{198}_{79}\text{Au} + \gamma \quad (\sigma_{\text{act}} = 98.7\text{ barns})$$
Gold-198 decays with half-life $T_{1/2} = 2.695\text{ days}$ ($64.68\text{ h}$), emitting a $411.8\text{ keV}$ gamma ray ($I_\gamma = 0.956$).
The sample is irradiated in a research reactor at thermal neutron flux $\Phi = 2.00 \times 10^{13}\text{ n/cm}^2\cdot\text{s}$ for $t_{\text{irr}} = 24.0\text{ hours}$.
Following a cooling time $t_d = 48.0\text{ hours}$, the sample is counted on an HPGe detector ($\epsilon_\gamma = 0.0450$) for $t_c = 3,600\text{ seconds}$, accumulating $C = 84,200\text{ net counts}$ in the $412\text{ keV}$ photopeak.
1. Calculate the decay constant $\lambda$ of $^{198}\text{Au}$ in $\text{s}^{-1}$ and $\text{h}^{-1}$.
2. Determine the saturation factor $(1 - e^{-\lambda t_{\text{irr}}})$, decay factor $e^{-\lambda t_d}$, and counting factor $(1 - e^{-\lambda t_c})$.
3. Calculate the mass of gold in the rock in nanograms ($\text{ng}$) and the gold concentration in parts per billion ($\text{ppb}$).""",
                    "solution": r"""### Step 1: Decay Constant $\lambda$
$$T_{1/2} = 2.695\text{ days} = 64.68\text{ h} = 232,848\text{ s}$$
$$\lambda = \frac{\ln 2}{232,848\text{ s}} \approx 2.9768 \times 10^{-6}\text{ s}^{-1}$$
$$\lambda_{\text{hour}} = \frac{\ln 2}{64.68\text{ h}} \approx 0.010716\text{ h}^{-1}$$

### Step 2: Kinetic Timing Factors
1. **Saturation Factor**:
$$\lambda t_{\text{irr}} = 0.010716\text{ h}^{-1} \times 24.0\text{ h} = 0.25719$$
$$S = 1 - e^{-\lambda t_{\text{irr}}} = 1 - e^{-0.25719} = 1 - 0.77322 = 0.22678$$

2. **Cooling Factor**:
$$\lambda t_d = 0.010716\text{ h}^{-1} \times 48.0\text{ h} = 0.51439$$
$$D = e^{-\lambda t_d} = e^{-0.51439} \approx 0.59787$$

3. **Counting Factor**:
$$\lambda t_c = (2.9768 \times 10^{-6}\text{ s}^{-1})(3600\text{ s}) = 0.010716$$
Because $\lambda t_c \ll 1$:
$$C_f = 1 - e^{-\lambda t_c} \approx \lambda t_c = 0.010659$$

### Step 3: Solve for Target Gold Mass
The net counts equation is:
$$C = N_{\text{Au}} \cdot \sigma \cdot \Phi \cdot S \cdot D \cdot \frac{C_f}{\lambda} \cdot \epsilon_\gamma \cdot I_\gamma = N_{\text{Au}} \cdot \sigma \cdot \Phi \cdot S \cdot D \cdot t_c \cdot \epsilon_\gamma \cdot I_\gamma$$
Given:
- $\sigma = 98.7\text{ b} = 9.87 \times 10^{-22}\text{ cm}^2$
- $\Phi = 2.00 \times 10^{13}\text{ cm}^{-2}\cdot\text{s}^{-1}$
- $\sigma \Phi = (9.87 \times 10^{-22})(2.00 \times 10^{13}) = 1.974 \times 10^{-8}\text{ s}^{-1}$
- $\epsilon_\gamma I_\gamma = (0.0450)(0.956) = 0.04302$

Multiply constants:
$$\text{Factor} = (1.974 \times 10^{-8})(0.22678)(0.59787)(3600)(0.04302) \approx 4.148 \times 10^{-7}\text{ counts/atom}$$
Number of gold atoms:
$$N_{\text{Au}} = \frac{C}{\text{Factor}} = \frac{84,200}{4.148 \times 10^{-7}} \approx 2.030 \times 10^{11}\text{ atoms}$$
Mass of gold:
$$m_{\text{Au}} = \frac{N_{\text{Au}}}{N_A} \times M_{\text{Au}} = \frac{2.030 \times 10^{11}}{6.022 \times 10^{23}} \times 196.97\text{ g/mol} \approx 6.640 \times 10^{-11}\text{ g} = 0.0664\text{ ng}$$
Concentration in $50.0\text{ mg}$ rock:
$$\text{Concentration} = \frac{6.640 \times 10^{-11}\text{ g}}{0.0500\text{ g}} \approx 1.328 \times 10^{-9} = 1.33\text{ ppb}$$
The rock contains **$1.33\text{ ppb}$** gold, detected with outstanding statistical significance!""",
                    "hints": ["Net counts formula: C = N_0 * sigma * Phi * (1 - exp(-lambda*t_irr)) * exp(-lambda*t_d) * (1 - exp(-lambda*t_c)) / lambda * epsilon * I_gamma.", "Convert cross-section from barns to cm^2 (1 b = 1e-24 cm^2)."]
                },
                {
                    "id": "prob-8-2",
                    "problemNumber": "8.2",
                    "title": "Direct Isotope Dilution Analysis of Cobalt in High-Purity Steel Alloy",
                    "difficulty": "Easy",
                    "statement": r"""The trace cobalt content in a high-purity nickel-base superalloy is determined via direct isotope dilution analysis.
1. A spike of $m_1 = 5.00\text{ mg}$ of cobalt labeled with $^{60}\text{Co}$ having specific activity $S_1 = 120.0\text{ kBq/mg}$ is added to a dissolved alloy sample.
2. After complete chemical equilibration, a small pure fraction of cobalt ($m_2 = 1.80\text{ mg}$) is isolated via anion-exchange chromatography and counted, yielding an activity $A_2 = 28.8\text{ kBq}$.
Calculate:
1. The diluted specific activity $S_2$ of the isolated cobalt in $\text{kBq/mg}$.
2. The mass of cobalt $m_x$ initially present in the alloy sample in milligrams.""",
                    "solution": r"""### Step 1: Diluted Specific Activity $S_2$
$$S_2 = \frac{A_2}{m_2} = \frac{28.8\text{ kBq}}{1.80\text{ mg}} = 16.00\text{ kBq/mg}$$

### Step 2: Unknown Mass $m_x$
Using the direct isotope dilution formula:
$$m_x = m_1 \left( \frac{S_1}{S_2} - 1 \right)$$
Given $m_1 = 5.00\text{ mg}$, $S_1 = 120.0\text{ kBq/mg}$, and $S_2 = 16.00\text{ kBq/mg}$:
$$\frac{S_1}{S_2} = \frac{120.0}{16.00} = 7.50$$
$$m_x = 5.00\text{ mg} \times (7.50 - 1) = 5.00\text{ mg} \times 6.50 = 32.50\text{ mg}$$
The alloy sample contained **$32.5\text{ milligrams}$** of cobalt.""",
                    "hints": ["Diluted specific activity is S_2 = A_2 / m_2.", "Use m_x = m_1 * (S_1 / S_2 - 1)."]
                },
                {
                    "id": "prob-8-3",
                    "problemNumber": "8.3",
                    "title": "Radiocarbon Dating of Dead Sea Scroll Parchment Fragment",
                    "difficulty": "Easy",
                    "statement": r"""A $25.0\text{ mg}$ parchment fragment from the Dead Sea Scrolls is analyzed by Accelerator Mass Spectrometry (AMS).
The measured specific activity of the carbon in the parchment is $A = 11.85\text{ dpm/g C}$.
The pre-industrial modern living reference specific activity is $A_0 = 15.30\text{ dpm/g C}$, and the Libby half-life is $T_{1/2} = 5,568\text{ years}$.
1. Calculate the decay constant $\lambda_{\text{Libby}}$ in $\text{yr}^{-1}$.
2. Determine the uncalibrated radiocarbon age of the parchment in years Before Present (BP).
3. If "Present" is defined as 1950 AD, calculate the historical calendar year of the parchment and verify its consistency with the Second Temple Period.""",
                    "solution": r"""### Step 1: Libby Decay Constant
$$\lambda = \frac{\ln 2}{5,568\text{ yr}} \approx 1.24488 \times 10^{-4}\text{ yr}^{-1}$$

### Step 2: Uncalibrated Radiocarbon Age
Using the radiocarbon age equation:
$$t = \frac{1}{\lambda} \ln\left(\frac{A_0}{A}\right)$$
Activity ratio:
$$\frac{A_0}{A} = \frac{15.30\text{ dpm/g}}{11.85\text{ dpm/g}} \approx 1.29114$$
$$\ln\left(\frac{A_0}{A}\right) = \ln(1.29114) \approx 0.25553$$
$$t = \frac{0.25553}{1.24488 \times 10^{-4}\text{ yr}^{-1}} \approx 2,052.6\text{ years BP}$$
The uncalibrated radiocarbon age is **$2,053\pm 30\text{ years BP}$**.

### Step 3: Historical Calendar Date
Using the 1950 AD baseline:
$$\text{Calendar Year} = 1950 - 2053 = -103 \implies 104\text{ BC}$$
The parchment dates to approximately **$104\text{ BC}$**, perfectly consistent with the historical floruit of the Qumran Essene community during the Hasmonean Period (2nd to 1st century BC)!""",
                    "hints": ["Use t = (T_half / ln(2)) * ln(A_0 / A).", "Calendar year = 1950 - Radiocarbon Age BP."]
                },
                {
                    "id": "prob-8-4",
                    "problemNumber": "8.4",
                    "title": "Substoichiometric Isotope Dilution Trace Zinc Analysis",
                    "difficulty": "Intermediate",
                    "statement": r"""Trace zinc in high-purity gallium arsenide semiconductor material is determined via substoichiometric IDA.
- A radioactive $^{65}\text{Zn}$ spike of mass $m_1 = 0.200\,\mu\text{g}$ with activity $A_1 = 15,000\text{ cpm}$ is added to an unknown solution.
- A standard solution containing $m_s = 5.00\,\mu\text{g}$ of zinc with identical $^{65}\text{Zn}$ activity ($A_1 = 15,000\text{ cpm}$) is prepared.
- To both solutions at $\text{pH } 7.5$, exactly $0.050\,\mu\text{mol}$ of dithizone is added, extracting an identical substoichiometric mass of zinc into carbon tetrachloride.
The measured organic phase activities are:
- Standard extract: $a_s = 1,250\text{ cpm}$
- Unknown extract: $a_x = 225\text{ cpm}$
Calculate the mass of zinc $m_x$ present in the semiconductor sample in micrograms ($\mu\text{g}$).""",
                    "solution": r"""### Step 1: Substoichiometric Derivation
Because identical substoichiometric amounts of zinc are extracted ($m_{\text{ext}}$ is identical):
$$a_s = S_s \cdot m_{\text{ext}} = \frac{A_1}{m_s + m_1} m_{\text{ext}}$$
$$a_x = S_x \cdot m_{\text{ext}} = \frac{A_1}{m_x + m_1} m_{\text{ext}}$$
Taking the ratio:
$$\frac{a_s}{a_x} = \frac{m_x + m_1}{m_s + m_1}$$
Solving for $m_x$:
$$m_x + m_1 = (m_s + m_1) \frac{a_s}{a_x} \implies m_x = (m_s + m_1) \left(\frac{a_s}{a_x}\right) - m_1$$

### Step 2: Numerical Calculation
Given:
- $m_s = 5.00\,\mu\text{g}$
- $m_1 = 0.200\,\mu\text{g} \implies m_s + m_1 = 5.200\,\mu\text{g}$
- $a_s / a_x = 1,250\text{ cpm} / 225\text{ cpm} \approx 5.5556$

$$m_x = (5.200\,\mu\text{g})(5.5556) - 0.200\,\mu\text{g} = 28.889\,\mu\text{g} - 0.200\,\mu\text{g} = 28.69\,\mu\text{g}$$
The semiconductor specimen contains **$28.7\,\mu\text{g}$** of zinc.""",
                    "hints": ["In substoichiometric IDA, identical masses are extracted from standard and unknown.", "Use m_x = (m_s + m_1) * (a_s / a_x) - m_1."]
                },
                {
                    "id": "prob-8-5",
                    "problemNumber": "8.5",
                    "title": "Radiometric Precipitation Titration of Chloride with Ag-110m",
                    "difficulty": "Easy",
                    "statement": r"""A $20.0\text{ mL}$ aliquot of a saline wastewater sample containing an unknown concentration of chloride ($\text{Cl}^-$) is titrated with $0.0500\text{ M}$ silver nitrate ($\text{AgNO}_3$) labeled with $^{110m}\text{Ag}$ ($T_{1/2} = 249.8\text{ days}$).
After each addition of titrant, the $\text{AgCl}$ precipitate is centrifuged and a $1.00\text{ mL}$ sample of clear supernatant is counted:
- At $V = 5.0\text{ mL}$: $R = 45\text{ cpm}$
- At $V = 10.0\text{ mL}$: $R = 52\text{ cpm}$
- At $V = 12.0\text{ mL}$: $R = 60\text{ cpm}$
- At $V = 15.0\text{ mL}$: $R = 1,840\text{ cpm}$
- At $V = 18.0\text{ mL}$: $R = 3,620\text{ cpm}$
1. Plotting supernatant activity versus titrant volume, determine the equivalence volume $V_{\text{eq}}$ by linear intersection.
2. Calculate the molarity of $\text{Cl}^-$ in the wastewater sample.
3. Determine the chloride concentration in $\text{mg/L}$ (ppm).""",
                    "solution": r"""### Step 1: Linear Extrapolation to Equivalence Point
1. **Pre-Equivalence Line**: Activity remains nearly zero ($R \approx 50\text{ cpm}$, governed by tiny $K_{\text{sp}}(\text{AgCl}) = 1.8 \times 10^{-10}$).
2. **Post-Equivalence Line**: Activity rises steeply as excess $^{110m}\text{Ag}^+$ accumulates.
Slope of post-equivalence line:
$$\text{Slope} = \frac{3620 - 1840}{18.0 - 15.0} = \frac{1780}{3.0} \approx 593.33\text{ cpm/mL}$$
Equation of line:
$$R - 1840 = 593.33(V - 15.0) \implies R = 593.33 V - 7060$$
Intersection with baseline $R \approx 50\text{ cpm}$:
$$50 = 593.33 V_{\text{eq}} - 7060 \implies 593.33 V_{\text{eq}} = 7110 \implies V_{\text{eq}} \approx 11.98\text{ mL} \approx 12.00\text{ mL}$$

### Step 2: Chloride Molarity
At equivalence:
$$M_{\text{Cl}} V_{\text{Cl}} = M_{\text{Ag}} V_{\text{eq}}$$
$$M_{\text{Cl}} = \frac{(0.0500\text{ M})(12.00\text{ mL})}{20.00\text{ mL}} = 0.0300\text{ M}$$

### Step 3: Concentration in mg/L
$$\text{Concentration} = 0.0300\text{ mol/L} \times 35.453\text{ g/mol} \times 1000\text{ mg/g} = 1,063.6\text{ mg/L} \approx 1,064\text{ ppm}$$
The chloride concentration is **$1,064\text{ mg/L}$**.""",
                    "hints": ["The endpoint is found by the sharp intersection where supernatant activity begins rising linearly.", "M_1 * V_1 = M_2 * V_2 at equivalence."]
                },
                {
                    "id": "prob-8-6",
                    "problemNumber": "8.6",
                    "title": "Radiotracer Self-Diffusion Coefficient in Solid Nickel",
                    "difficulty": "Intermediate",
                    "statement": r"""A thin layer of radioactive nickel-63 ($^{63}\text{Ni}$, pure $\beta^-$, $T_{1/2} = 100.1\text{ yr}$) is deposited on the end face of a pure nickel rod.
The rod is annealed in a vacuum furnace at $T = 1,100^\circ\text{C}$ ($1373\text{ K}$) for an annealing duration $t = 24.0\text{ hours}$ ($86,400\text{ s}$).
Serial sectioning reveals the following specific activity profile:
- At penetration depth $x_1 = 15.0\,\mu\text{m}$: $A_1 = 4,500\text{ cpm}$
- At penetration depth $x_2 = 35.0\,\mu\text{m}$: $A_2 = 1,120\text{ cpm}$
1. Using the thin-film Gaussian solution $A(x) = A_0 \exp(-x^2 / 4Dt)$, formulate the ratio $\ln(A_1 / A_2)$.
2. Calculate the self-diffusion coefficient $D$ of nickel in $\text{cm}^2/\text{s}$ at $1,100^\circ\text{C}$.""",
                    "solution": r"""### Step 1: Ratio Formulation
For thin-film boundary conditions:
$$\frac{A(x_1)}{A(x_2)} = \frac{A_0 \exp(-x_1^2 / 4Dt)}{A_0 \exp(-x_2^2 / 4Dt)} = \exp\left( \frac{x_2^2 - x_1^2}{4Dt} \right)$$
Taking the natural logarithm:
$$\ln\left(\frac{A_1}{A_2}\right) = \frac{x_2^2 - x_1^2}{4Dt} \implies D = \frac{x_2^2 - x_1^2}{4 t \ln(A_1 / A_2)}$$

### Step 2: Numerical Calculation
Convert micrometers to centimeters:
- $x_1 = 15.0\,\mu\text{m} = 1.50 \times 10^{-3}\text{ cm} \implies x_1^2 = 2.25 \times 10^{-6}\text{ cm}^2$
- $x_2 = 35.0\,\mu\text{m} = 3.50 \times 10^{-3}\text{ cm} \implies x_2^2 = 1.225 \times 10^{-5}\text{ cm}^2$
$$x_2^2 - x_1^2 = 12.25 \times 10^{-6} - 2.25 \times 10^{-6} = 1.00 \times 10^{-5}\text{ cm}^2$$

Logarithm of activity ratio:
$$\frac{A_1}{A_2} = \frac{4500}{1120} \approx 4.01786$$
$$\ln(4.01786) \approx 1.39075$$

Time: $t = 86,400\text{ s}$.
$$4 t \ln(A_1 / A_2) = 4(86400\text{ s})(1.39075) \approx 480,643\text{ s}$$
Compute $D$:
$$D = \frac{1.00 \times 10^{-5}\text{ cm}^2}{480,643\text{ s}} \approx 2.08 \times 10^{-11}\text{ cm}^2/\text{s}$$
The self-diffusion coefficient is **$2.08 \times 10^{-11}\text{ cm}^2/\text{s}$** (or $2.08 \times 10^{-15}\text{ m}^2/\text{s}$).""",
                    "hints": ["Gaussian diffusion profile: A(x) = A_0 * exp(-x^2 / (4*D*t)).", "Convert all distances to cm and time to seconds."]
                },
                {
                    "id": "prob-8-7",
                    "problemNumber": "8.7",
                    "title": "Cosmogenic Beryllium-10 and Aluminum-26 Exposure Dating",
                    "difficulty": "Advanced",
                    "statement": r"""In surface exposure geological dating, quartz rocks ($\text{SiO}_2$) exposed to cosmic ray showers accumulate cosmogenic $^{10}\text{Be}$ ($T_{1/2} = 1.387\text{ Ma}$, $\lambda_{10} = 4.997 \times 10^{-7}\text{ yr}^{-1}$) and $^{26}\text{Al}$ ($T_{1/2} = 0.705\text{ Ma}$, $\lambda_{26} = 9.832 \times 10^{-7}\text{ yr}^{-1}$).
The constant surface production ratio is $P_{26} / P_{10} = 6.75$.
An exposed glacial boulder has a measured atomic ratio $N_{26} / N_{10} = 4.10$.
1. Derive the time evolution equation for the ratio $N_{26}(t) / N_{10}(t)$ assuming zero erosion.
2. Determine the surface exposure age $t$ of the glacial moraine in thousands of years (ka).""",
                    "solution": r"""### Step 1: Ratio Formulation
For an initially unexposed rock ($N(0) = 0$), the accumulation of each isotope balances production and decay:
$$N_i(t) = \frac{P_i}{\lambda_i} (1 - e^{-\lambda_i t})$$
The atomic ratio at exposure time $t$ is:
$$\frac{N_{26}(t)}{N_{10}(t)} = \left(\frac{P_{26}}{P_{10}}\right) \left(\frac{\lambda_{10}}{\lambda_{26}}\right) \left[\frac{1 - e^{-\lambda_{26} t}}{1 - e^{-\lambda_{10} t}}\right]$$
For exposure ages much less than the half-lives ($t \ll 700\text{ ka}$), using $1 - e^{-\lambda t} \approx \lambda t - \frac{1}{2}\lambda^2 t^2$:
$$\frac{1 - e^{-\lambda_{26} t}}{1 - e^{-\lambda_{10} t}} \approx \frac{\lambda_{26} t (1 - \frac{1}{2}\lambda_{26} t)}{\lambda_{10} t (1 - \frac{1}{2}\lambda_{10} t)} = \left(\frac{\lambda_{26}}{\lambda_{10}}\right) \left[ 1 - \frac{1}{2}(\lambda_{26} - \lambda_{10}) t \right]$$
Substituting:
$$\frac{N_{26}}{N_{10}} \approx \left(\frac{P_{26}}{P_{10}}\right) \left[ 1 - \frac{1}{2}(\lambda_{26} - \lambda_{10}) t \right]$$

### Step 2: Numerical Age Calculation
Given $P_{26} / P_{10} = 6.75$ and observed ratio $N_{26} / N_{10} = 4.10$:
$$\frac{4.10}{6.75} \approx 0.60741$$
Using the exact equation:
$$0.60741 = \left(\frac{4.997 \times 10^{-7}}{9.832 \times 10^{-7}}\right) \left[ \frac{1 - e^{-\lambda_{26} t}}{1 - e^{-\lambda_{10} t}} \right] = 0.50824 \left[ \frac{1 - e^{-\lambda_{26} t}}{1 - e^{-\lambda_{10} t}} \right]$$
$$\frac{1 - e^{-\lambda_{26} t}}{1 - e^{-\lambda_{10} t}} = \frac{0.60741}{0.50824} \approx 1.1951$$
Solving numerically via Newton-Raphson or successive approximation yields:
$$t \approx 625,000\text{ years} = 625\text{ ka}$$
The glacial moraine was exposed to cosmic rays **$625,000\text{ years}$** ago.""",
                    "hints": ["Cosmogenic nuclide buildup: N(t) = (P / lambda) * (1 - exp(-lambda * t)).", "The ratio decreases over time because Al-26 decays faster than Be-10."]
                }
            ]
        },

        # =====================================================================
        # UNIT 9
        # =====================================================================
        {
            "id": "unit-9-radioisotope-production-generators",
            "unitNumber": 9,
            "title": "Unit 9: Radioisotope Production, Accelerators & Radionuclide Generators",
            "leadSummary": "Comprehensive technological and radiochemical treatise on radionuclide synthesis: high-flux thermal neutron irradiation in nuclear research reactors; carrier-free fission product harvesting; cyclotron kinematics, RF acceleration cavities, and target design; medical cyclotron production of short-lived PET radiotracers; the alumina-based Mo-99 / Tc-99m generator elution system; and advanced alpha-emitting and therapeutic sealed sources.",
            "simulations": ["sim_nuc_generator_99mo_99mtc"],
            "sections": [
                {
                    "id": "sec-9-1",
                    "secNumber": "9.1",
                    "title": "Nuclear Reactor Radioisotope Production: High-Flux Neutron Irradiation & Transmutation",
                    "content": r"""Over $80\%$ of all radioisotopes used worldwide in medicine and industry are produced in nuclear research reactors (e.g., BR2 in Belgium, HFR in the Netherlands, OPAL in Australia, MURR in the USA).

Reactors produce radionuclides via two primary pathways:
1. **Neutron Capture Reactions ($(n, \gamma)$)**:
A stable target isotope captures a thermal neutron:
$$^{A}_{Z}\text{X} + ^1_0n \longrightarrow ^{A+1}_{Z}\text{X} + \gamma$$
Because the product is an **isotope of the target element**, chemical separation is impossible! The product is inherently **carrier-added**; its specific activity is limited by target burnup:
$$SA = \frac{\lambda N^*}{m_{\text{target}} + m^*} \ll SA_{\text{theoretical}}$$
Examples:
- $^{59}_{27}\text{Co}(n, \gamma)^{60}_{27}\text{Co}$ ($T_{1/2} = 5.27\text{ yr}$) for industrial sterilization and cancer teletherapy.
- $^{191}_{77}\text{Ir}(n, \gamma)^{192}_{77}\text{Ir}$ ($T_{1/2} = 73.8\text{ days}$) for pipeline radiography and brachytherapy.

2. **Fast Neutron Transmutation Reactions ($(n, p)$ and $(n, \alpha)$)**:
Fast fission neutrons ($E_n > 1\text{ MeV}$) induce charge-changing transmutation reactions:
$$^{A}_{Z}\text{X} + ^1_0n \longrightarrow ^{A}_{Z-1}\text{Y} + ^1_1p \quad \text{or} \quad ^{A}_{Z}\text{X} + ^1_0n \longrightarrow ^{A-3}_{Z-2}\text{W} + ^4_2\alpha$$
Because the product is a **different chemical element**, it can be separated from the target matrix with $>99.99\%$ purity using ion-exchange chromatography or solvent extraction. The product is **carrier-free (No-Carrier-Added, NCA)**, achieving maximum theoretical specific activity!
Examples:
- $^{32}_{16}\text{S}(n, p)^{32}_{15}\text{P}$ ($T_{1/2} = 14.3\text{ days}$, pure beta emitter).
- $^{14}_{7}\text{N}(n, p)^{14}_{6}\text{C}$ ($T_{1/2} = 5,730\text{ yr}$).
- $^{6}_{3}\text{Li}(n, \alpha)^{3}_{1}\text{H}$ ($T_{1/2} = 12.32\text{ yr}$, tritium production).""",
                    "simulations": ["sim_nuc_generator_99mo_99mtc"]
                },
                {
                    "id": "sec-9-2",
                    "secNumber": "9.2",
                    "title": "Carrier-Free Radiochemistry: Fission Product Harvesting Versus Transmutation Pathways",
                    "content": r"""The highest specific activity radionuclides are obtained by harvesting fission products from irradiated uranium targets:
$$^{235}_{92}\text{U} + ^1_0n_{\text{th}} \longrightarrow \text{Fission Products} + 2.4 \, ^1_0n$$

### Production of Fission Molybdenum-99 ($^{99}\text{Mo}$)
Molybdenum-99 is the parent of technetium-99m, the workhorse of nuclear medicine ($>30\text{ million}$ scans annually).
- **Target**: Enriched uranium targets ($19.75\%$ Low-Enriched Uranium, LEU) electroplated as uranium metal or aluminide foil inside a target pin.
- **Irradiation**: Irradiated in a reactor core for $5 - 7\text{ days}$ at thermal flux $\Phi \sim 10^{14}\text{ n/cm}^2\cdot\text{s}$. Fission yield for mass chain 99 is exceptionally high: $\gamma(^{99}\text{Mo}) = 6.13\%$.
- **Chemical Extraction (Hot Cell Radiochemistry)**:
  Within hours of discharge, the target is dissolved in boiling sodium hydroxide ($\text{NaOH}$) or nitric acid ($\text{HNO}_3$) behind lead hot-cell shielding.
  Uranium and actinides precipitate as insoluble hydrous oxides.
  The dissolved molybdate ($^{99}\text{MoO}_4^{2-}$) is purified through successive alumina and anion-exchange chromatography columns, achieving carrier-free specific activities exceeding **$10,000\text{ Ci/gram}$** ($3.7 \times 10^{14}\text{ Bq/g}$).

Other critical carrier-free fission products:
- **Iodine-131 ($^{131}_{53}\text{I}$)**: Fission yield $2.89\%$, extracted via thermal dry distillation of irradiated uranium or via tellurium neutron capture:
$$^{130}_{52}\text{Te}(n, \gamma)^{131}_{52}\text{Te} \xrightarrow[\beta^-]{25.0\text{ min}} \, ^{131}_{53}\text{I} \quad (T_{1/2} = 8.02\text{ days})$$
- **Xenon-133 ($^{133}_{54}\text{Xe}$)**: Fission yield $6.70\%$, cryogenically trapped as a noble gas for lung ventilation imaging.""",
                    "simulations": ["sim_nuc_generator_99mo_99mtc"]
                },
                {
                    "id": "sec-9-3",
                    "secNumber": "9.3",
                    "title": "Charged Particle Accelerators: Cyclotron Resonance Kinematics, RF Cavities & Target Design",
                    "content": r"""Particle accelerators produce proton-rich radionuclides that decay via positron emission ($\beta^+$) or electron capture (EC)—isotopes that cannot be produced in nuclear reactors.

### Classical Cyclotron Kinematics (Lawrence, 1930)
A classical cyclotron accelerates charged ions (e.g., protons, deuterons) between two semicircular hollow D-shaped electrodes ("dees") housed in a high-vacuum chamber between the poles of an electromagnet.
A particle of mass $m$ and charge $q$ moving with velocity $v$ in a perpendicular magnetic field $B$ experiences a centripetal Lorentz force:
$$q v B = \frac{m v^2}{r} \implies r = \frac{m v}{q B} = \frac{p}{q B}$$
The orbital revolution frequency is:
$$\omega_{\text{cyc}} = \frac{v}{r} = \frac{q B}{m} \implies f_{\text{cyc}} = \frac{q B}{2\pi m}$$
Notice that **velocity $v$ and radius $r$ cancel out completely**!
As long as the particle remains non-relativistic ($m \approx m_0$), the revolution period is completely independent of its energy and orbital radius.

```
       TOP VIEW OF CYCLOTRON DEES
      ┌─────────────────┐ ┌─────────────────┐
      │  DEE 1 (-V)     │ │   DEE 2 (+V)    │
      │                 │ │                 │
      │       /───\     │ │                 │
      │      /  ●  \    │ │                 │  ● Ion Source
      │     (  / \  )   │ │                 │
      │      \     /    │ │                 │
      │       \───/     │ │                 │
      │                 │ │      DEFLECTOR  │
      │                 │ │          \      │
      └─────────────────┘ └───────────\─────┘
                                       \──► EXTRACTION TO TARGET
```

By applying an alternating radio-frequency (RF) voltage across the dee gap at resonance frequency $f_{\text{RF}} = f_{\text{cyc}}$, the particle receives an accelerating electrostatic kick $\Delta T = q V_{\text{dee}}$ twice per revolution, spiraling outward in expanding orbits.

### Relativistic Relativistic Breakdown & Isochronous Cyclotrons
At relativistic energies, mass increases with the Lorentz factor:
$$m(v) = \gamma m_0 = \frac{m_0}{\sqrt{1 - \beta^2}} \implies \omega_{\text{cyc}}(v) = \frac{q B}{\gamma m_0}$$
As the particle accelerates, $\omega_{\text{cyc}}$ drops; the particle falls out of phase with the fixed RF frequency.
Modern biomedical cyclotrons overcome this by using **Isochronous (Azimuthally Varying Field, AVF) Cyclotrons**:
The magnetic field is engineered to increase radially ($B(r) \propto \gamma(r)$) using spiral-shaped iron pole sectors to provide strong alternating-gradient focusing, keeping $B / \gamma$ strictly constant up to $30\text{ MeV}$.""",
                    "simulations": ["sim_nuc_generator_99mo_99mtc"]
                },
                {
                    "id": "sec-9-4",
                    "secNumber": "9.4",
                    "title": "Medical Cyclotron Production of Short-Lived PET Radionuclides ($^{18}\text{F}, ^{11}\text{C}, ^{13}\text{N}, ^{15}\text{O}$)",
                    "content": r"""Positron Emission Tomography (PET) requires ultra-short-lived, positron-emitting radionuclides of the fundamental biological elements: carbon, nitrogen, oxygen, and fluorine (a bio-isostere of hydrogen).
These radionuclides are synthesized on-site using compact, self-shielded hospital cyclotrons ($E_p \approx 11 - 18\text{ MeV}$):

| Radionuclide | Half-Life ($T_{1/2}$) | Nuclear Production Reaction | Target Chemical Matrix | Chemical Form Produced | Key Clinical Radiopharmaceutical |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Fluorine-18** | **$109.77\text{ min}$** | $^{18}\text{O}(p, n)^{18}\text{F}$ | Enriched Water ($\text{H}_2^{18}\text{O}, 98\%$) | $[^{18}\text{F}]\text{F}^-_{\text{aq}}$ (Fluoride) | $[^{18}\text{F}]\text{FDG}$ (2-Fluorodeoxyglucose, oncology) |
| **Carbon-11** | **$20.36\text{ min}$** | $^{14}\text{N}(p, \alpha)^{11}\text{C}$ | High-Pressure Gas ($\text{N}_2 + 0.5\% \text{O}_2$) | $[^{11}\text{C}]\text{CO}_2$ | $[^{11}\text{C}]\text{Choline}, [^{11}\text{C}]\text{Methionine}$ |
| **Nitrogen-13** | **$9.97\text{ min}$** | $^{16}\text{O}(p, \alpha)^{13}\text{N}$ | Natural Water ($\text{H}_2^{16}\text{O}$) + Ethanol | $[^{13}\text{N}]\text{NH}_3$ (Ammonia) | $[^{13}\text{N}]\text{NH}_3$ (Myocardial perfusion) |
| **Oxygen-15** | **$122.24\text{ s}$** | $^{14}\text{N}(d, n)^{15}\text{O}$ | High-Pressure Gas ($\text{N}_2 + 1\% \text{O}_2$) | $[^{15}\text{O}]\text{O}_2, [^{15}\text{O}]\text{H}_2\text{O}$ | Cerebral blood flow / oxygen utilization |

### Fluorine-18 Synthesis Chemistry
Fluorine-18 is the dominant PET isotope due to its optimal $110\text{ min}$ half-life, allowing commercial regional distribution:
1. Liquid target: $2.5\text{ mL}$ of enriched water ($\text{H}_2^{18}\text{O}$, costing $\sim \$50/\text{g}$) is irradiated with a $16.5\text{ MeV}$ proton beam at $40\,\mu\text{A}$ for $60 - 90\text{ minutes}$.
2. The aqueous $^{18}\text{F}^-$ is trapped on an anion-exchange cartridge (QMA Sep-Pak), while the expensive $\text{H}_2^{18}\text{O}$ is recovered for recycling.
3. The $^{18}\text{F}^-$ is eluted with potassium carbonate/Kryptofix 2.2.2 in acetonitrile.
4. Nucleophilic fluorination of mannose triflate followed by acid/base hydrolysis yields pure **$^{18}\text{F-FDG}$** in an automated synthesis module within $30\text{ minutes}$.""",
                    "simulations": ["sim_nuc_generator_99mo_99mtc"]
                },
                {
                    "id": "sec-9-5",
                    "secNumber": "9.5",
                    "title": "Radionuclide Generator Physics: The Alumina-Based $^{99}\text{Mo}/^{99m}\text{Tc}$ Generator System",
                    "content": r"""A **radionuclide generator** (historically termed a "cow") is an on-site radiochemical separation apparatus that houses a long-lived parent radionuclide that decays into a short-lived daughter radionuclide. It enables hospitals thousands of miles from a nuclear reactor to obtain short-lived isotopes on demand.

### The Physics of the $^{99}\text{Mo}/^{99m}\text{Tc}$ Couple
The generator exploits the parent-daughter decay relationship:
$$^{99}_{42}\text{Mo} \xrightarrow[\beta^- \text{ (87.5\%)}]{T_{1/2} = 66.0\text{ h}} \, ^{99m}_{43}\text{Tc} \xrightarrow[\text{IT } (\gamma = 140.5\text{ keV})]{T_{1/2} = 6.01\text{ h}} \, ^{99}_{43}\text{Tc} \xrightarrow[\beta^-]{T_{1/2} = 2.1 \times 10^5\text{ yr}} \, ^{99}_{44}\text{Ru} \text{ (Stable)}$$
Key physical features:
- Parent $^{99}\text{Mo}$ half-life ($66\text{ h}$) is long enough for shipping across continents.
- Daughter $^{99m}\text{Tc}$ half-life ($6.0\text{ h}$) matches patient imaging procedures while minimizing radiation dose.
- Gamma emission: Clean, monoenergetic $140.5\text{ keV}$ photon ($89\%$ abundance) with zero particulate beta emission, perfectly matched to gamma camera NaI(Tl) crystal thickness ($3/8\text{ inch}$).

```
   Activity on Generator Column (GBq)
100 ▲
    │\  Parent ⁹⁹Mo (T₁/₂ = 66.0 h)
    │ \                                    Daughter ⁹⁹ᵐTc (Post-Milking In-growth)
 80 │  \                                  /──────────────\
    │   \                                /                \
 60 │    \                              /                  \
    │     \                            /                    \
 40 │      \__________________________/                      \_____
    │       Milked (t = 0)            Peak Activity (t_max ≈ 22.9 h)
    └─────────────────────────────────┴─────────────────────────────► Time t (Hours)
```

### Chemical Architecture of the Alumina Column
The generator utilizes an acid-washed chromatographic column packed with high-purity **acidic aluminum oxide ($\text{Al}_2\text{O}_3$)**:
1. At acidic $\text{pH} \approx 4 - 5$, the alumina surface acquires positive charges ($-\text{AlOH}_2^+$).
2. Carrier-free parent $^{99}\text{Mo}$ is loaded as divalent molybdate anions ($^{99}\text{MoO}_4^{2-}$). The high charge density ($-2$) binds firmly to the alumina surface:
$$2 [-\text{AlOH}_2^+] + [^{99}\text{MoO}_4]^{2-} \rightleftharpoons [-\text{AlOH}_2^+]_2 [^{99}\text{MoO}_4]^{2-}$$
3. As $^{99}\text{Mo}$ decays, it transmutes into technetium-99m, forming the monovalent pertechnetate anion ($^{99m}\text{TcO}_4^-$).
4. Because pertechnetate has only a single negative charge ($-1$) and a large ionic radius, its binding affinity for alumina is extremely weak.
5. **Elution ("Milking")**: Passing $5 - 10\text{ mL}$ of sterile, pyrogen-free $0.9\%\text{ NaCl}$ saline solution through the column selectively elutes the daughter as sodium pertechnetate ($\text{Na}^{99m}\text{TcO}_4$), while $99.999\%$ of the $^{99}\text{Mo}$ remains bound to the alumina!""",
                    "simulations": ["sim_nuc_generator_99mo_99mtc"]
                },
                {
                    "id": "sec-9-6",
                    "secNumber": "9.6",
                    "title": "Generator Milking Chemistry, Elution Dynamics & Metrological Quality Assurance",
                    "content": r"""Following elution of a $^{99}\text{Mo}/^{99m}\text{Tc}$ generator, the technetium activity on the column regenerates according to the Bateman transient growth formula:
$$A_{\text{Tc}}(t) = BR \cdot \frac{\lambda_{\text{Tc}}}{\lambda_{\text{Tc}} - \lambda_{\text{Mo}}} A_{\text{Mo}}(0) \left( e^{-\lambda_{\text{Mo}} t} - e^{-\lambda_{\text{Tc}} t} \right)$$
Maximum activity is reached at:
$$t_{\max} = \frac{\ln(\lambda_{\text{Tc}} / \lambda_{\text{Mo}})}{\lambda_{\text{Tc}} - \lambda_{\text{Mo}}} \approx 22.85\text{ hours}$$
At $t = 24\text{ hours}$, the daughter activity reaches **$95\%$** of its theoretical maximum, establishing the universal clinical rhythm of daily morning milking.

### Metrological Quality Assurance Standards
Before eluate can be administered to patients, strict pharmacopeial quality criteria must be satisfied:

1. **Radionuclidic Purity (Molybdenum Breakthrough)**:
Contamination with parent $^{99}\text{Mo}$ ($T_{1/2} = 66\text{ h}$, energetic beta emitter) delivers unnecessary radiation dose to patient bone marrow.
- **Assay**: Eluate is placed inside a calibrated lead canister ($6\text{ mm}$ wall thickness). The $140\text{ keV}$ gammas of $^{99m}\text{Tc}$ are absorbed completely, while energetic $740\text{ keV}$ and $778\text{ keV}$ photons of $^{99}\text{Mo}$ penetrate the shield and are counted.
- **US Pharmacopeia (USP) Regulatory Limit**:
$$\frac{\text{Activity of }^{99}\text{Mo}}{\text{Activity of }^{99m}\text{Tc}} \le 0.15\,\mu\text{Ci } ^{99}\text{Mo} / \text{mCi } ^{99m}\text{Tc} \quad (0.15\text{ kBq / MBq}) \quad \text{at time of administration}$$

2. **Chemical Purity (Aluminum Ion Breakthrough)**:
Alumina breakdown can release colloidal $\text{Al}^{3+}$ ions, which precipitate radiopharmaceutical complexes (e.g., flocculating sulfur colloid).
- **Assay**: Colorimetric spot test using aurintricarboxylic acid (aluminon) test strips.
- **USP Limit**: $[\text{Al}^{3+}] < 10\,\mu\text{g/mL}$ of eluate.

3. **Radiochemical Purity**:
Percentage of technetium existing in the correct chemical oxidation state (pertechnetate $\text{TcO}_4^-, \text{Tc(VII)}$ vs reduced hydrolyzed species $\text{TcO}_2$).
- **Assay**: Instant Thin-Layer Chromatography (ITLC).
- **Limit**: $>95\%$ pure pertechnetate.""",
                    "simulations": ["sim_nuc_generator_99mo_99mtc"]
                },
                {
                    "id": "sec-9-7",
                    "secNumber": "9.7",
                    "title": "Advanced Biomedical & Industrial Radionuclides: $^{68}\text{Ge}/^{68}\text{Ga}$, Alpha Emitters & Sealed Sources",
                    "content": r"""Beyond technetium-99m, radiochemistry has developed specialized generator systems and industrial sealed sources:

### 1. The $^{68}\text{Ge}/^{68}\text{Ga}$ PET Generator System
The modern PET counterpart to the technetium generator:
$$^{68}_{32}\text{Ge} \xrightarrow[\text{EC}]{T_{1/2} = 270.95\text{ days}} \, ^{68}_{31}\text{Ga} \xrightarrow[\beta^+ \text{ (89\%)}]{T_{1/2} = 67.71\text{ min}} \, ^{68}_{30}\text{Zn} \text{ (Stable)}$$
- **Column**: Titanium dioxide ($\text{TiO}_2$) or tin dioxide ($\text{SnO}_2$).
- **Elution**: Eluted with dilute hydrochloric acid ($0.1\text{ M HCl}$) as gallium chloride ($[^{68}\text{Ga}]\text{Ga}^{3+}$).
- **Advantage**: A parent half-life of **9 months** allows a single generator to supply a PET imaging center with positron-emitting $^{68}\text{Ga}$ (for prostate cancer PSMA imaging and neuroendocrine DOTATOC scans) without an on-site cyclotron!

### 2. Targeted Alpha Therapy (TAT) Radionuclides
Alpha particles deposit extreme localized ionization ($\text{LET} \sim 100\text{ keV}/\mu\text{m}$) over a $40 - 80\,\mu\text{m}$ path length, delivering lethal double-strand DNA breaks to tumor cells while sparing neighboring normal tissues:
- **Actinium-225 ($^{225}\text{Ac}$)**: $T_{1/2} = 9.92\text{ days}$, emits a cascade of 4 alpha particles ($^{225}\text{Ac} \to ^{221}\text{Fr} \to ^{217}\text{At} \to ^{213}\text{Bi} \to ^{209}\text{Pb}$). Conjugated to PSMA-617 for metastatic castration-resistant prostate cancer.
- **Radium-223 ($^{223}\text{Ra}$ dichloride, Xofigo)**: $T_{1/2} = 11.43\text{ days}$, a natural calcium mimetic that targets osteoblastic bone metastases directly.

### 3. Industrial Sealed Radiation Sources
- **Cobalt-60 ($^{60}\text{Co}$)**: Sealed double-encapsulated stainless steel pencils (activity up to $100\text{ kCi} \approx 3.7\text{ PBq}$) used for food irradiation, medical device sterilization, and industrial gamma radiography.
- **Cesium-137 ($^{137}\text{Cs}$)**: Sealed ceramic pellets used for borehole geophysical well-logging and industrial level gauges.
- **Americium-241 / Beryllium ($^{241}\text{Am}-\text{Be}$)**: Alpha-neutron source ($(\alpha, n)$ reaction on $^9\text{Be}$, emitting $\sim 2.2 \times 10^6\text{ n/s per Ci}$) for moisture gauges and neutron activation.""",
                    "simulations": ["sim_nuc_generator_99mo_99mtc"]
                }
            ],
            "problems": [
                {
                    "id": "prob-9-1",
                    "problemNumber": "9.1",
                    "title": "Cyclotron Resonant Frequency and Relativistic Kinetic Energy Limit",
                    "difficulty": "Easy",
                    "statement": r"""A medical cyclotron used for fluorine-18 production has a uniform magnetic field $B = 1.65\text{ Tesla}$ and an extraction radius $R = 0.520\text{ m}$.
1. Calculate the non-relativistic cyclotron resonance frequency $f_{\text{cyc}}$ in $\text{MHz}$ for protons ($q = 1.602 \times 10^{-19}\text{ C}, m_p = 1.673 \times 10^{-27}\text{ kg}$).
2. Determine the maximum momentum $p_{\max}$ and kinetic energy $T_{\max}$ of extracted protons in $\text{MeV}$.
3. Calculate the relativistic factor $\gamma$ and assess whether isochronous magnetic field profiling is required.""",
                    "solution": r"""### Step 1: Cyclotron Resonance Frequency
$$\omega_{\text{cyc}} = \frac{q B}{m_p} = \frac{(1.60218 \times 10^{-19}\text{ C})(1.65\text{ T})}{1.67262 \times 10^{-27}\text{ kg}} \approx 1.5799 \times 10^8\text{ rad/s}$$
$$f_{\text{cyc}} = \frac{\omega_{\text{cyc}}}{2\pi} = \frac{1.5799 \times 10^8}{6.283185} \approx 25.145\text{ MHz}$$
The RF oscillator must operate at **$25.15\text{ MHz}$**.

### Step 2: Maximum Extracted Kinetic Energy
At extraction radius $R = 0.520\text{ m}$:
$$p = q B R = (1.60218 \times 10^{-19}\text{ C})(1.65\text{ T})(0.520\text{ m}) \approx 1.37467 \times 10^{-19}\text{ kg}\cdot\text{m/s}$$
In energy units:
$$p c = (1.37467 \times 10^{-19}\text{ kg}\cdot\text{m/s})(2.99792 \times 10^8\text{ m/s}) \approx 4.1211 \times 10^{-11}\text{ J}$$
Convert to $\text{MeV}$:
$$p c = \frac{4.1211 \times 10^{-11}\text{ J}}{1.60218 \times 10^{-13}\text{ J/MeV}} \approx 257.22\text{ MeV}$$
Using relativistic energy relation ($E^2 = p^2 c^2 + m_0^2 c^4$ with $m_0 c^2 = 938.272\text{ MeV}$):
$$E = \sqrt{(257.22)^2 + (938.272)^2} = \sqrt{66,162 + 880,354} = \sqrt{946,516} \approx 972.89\text{ MeV}$$
Kinetic energy:
$$T = E - m_0 c^2 = 972.89 - 938.27 = 34.62\text{ MeV}$$

### Step 3: Relativistic Factor $\gamma$
$$\gamma = \frac{E}{m_0 c^2} = \frac{972.89}{938.27} \approx 1.0369$$
Because $\gamma = 1.037$, the relativistic mass increases by **$3.7\%$**. Without isochronous field profiling ($B(r)$ increasing by $3.7\%$ toward the periphery), the protons would slip out of RF phase within a few dozen turns. Isochronous flutter sectors are required!""",
                    "hints": ["Resonance frequency is f = q*B / (2*pi*m).", "Relativistic momentum is p = q*B*R, and kinetic energy is T = sqrt(p^2*c^2 + m_0^2*c^4) - m_0*c^2."]
                },
                {
                    "id": "prob-9-2",
                    "problemNumber": "9.2",
                    "title": "Theoretical Carrier-Free Specific Activity of Technetium-99m and Cobalt-60",
                    "difficulty": "Easy",
                    "statement": r"""1. Derive the general formula for carrier-free specific activity $SA_{\text{CF}}$ in $\text{Ci/g}$ as a function of molar mass $M$ ($\text{g/mol}$) and half-life $T_{1/2}$ ($\text{hours}$).
2. Calculate the theoretical carrier-free specific activity for:
   (a) Technetium-99m ($M = 98.91\text{ g/mol}$, $T_{1/2} = 6.007\text{ hours}$)
   (b) Cobalt-60 ($M = 59.93\text{ g/mol}$, $T_{1/2} = 5.271\text{ years} \approx 46,174\text{ hours}$)""",
                    "solution": r"""### Step 1: General Formula Derivation
Number of atoms per gram of pure radionuclide:
$$N = \frac{N_A}{M} = \frac{6.02214 \times 10^{23}}{M}$$
Activity in Becquerels:
$$A = \lambda N = \frac{\ln 2}{T_{1/2 (\text{sec})}} \frac{N_A}{M} = \frac{0.693147 \times 6.02214 \times 10^{23}}{M \cdot (3600 \cdot T_{1/2 (\text{hours})})} = \frac{1.1595 \times 10^{20}}{M \cdot T_{1/2 (\text{hours})}}\text{ Bq/g}$$
Convert to Curies ($1\text{ Ci} = 3.700 \times 10^{10}\text{ Bq}$):
$$SA_{\text{CF}}\text{ (Ci/g)} = \frac{1.1595 \times 10^{20}}{3.700 \times 10^{10} \cdot M \cdot T_{1/2 (\text{hours})}} \approx \frac{3.134 \times 10^9}{M \cdot T_{1/2 (\text{hours})}}$$

### Step 2: Numerical Calculations
1. **For Technetium-99m**:
$$M = 98.91\text{ g/mol}, \quad T_{1/2} = 6.007\text{ hours}$$
$$SA_{\text{CF}}(^{99m}\text{Tc}) = \frac{3.134 \times 10^9}{(98.91)(6.007)} = \frac{3.134 \times 10^9}{594.15} \approx 5.275 \times 10^6\text{ Ci/g} = 5,275,000\text{ Ci/g}$$
In SI: $5.275 \times 10^6 \times 37\text{ GBq/Ci} \approx 1.95 \times 10^{17}\text{ Bq/g} = 195\text{ PBq/g}$.

2. **For Cobalt-60**:
$$M = 59.93\text{ g/mol}, \quad T_{1/2} = 46,174\text{ hours}$$
$$SA_{\text{CF}}(^{60}\text{Co}) = \frac{3.134 \times 10^9}{(59.93)(46,174)} = \frac{3.134 \times 10^9}{2.7672 \times 10^6} \approx 1,132.5\text{ Ci/g}$$
Carrier-free $^{99m}\text{Tc}$ is nearly **$5,000$ times more active per gram** than $^{60}\text{Co}$ due to its short 6-hour half-life!""",
                    "hints": ["Specific activity SA = lambda * N_A / M.", "1 Ci = 3.7e10 Bq."]
                },
                {
                    "id": "prob-9-3",
                    "problemNumber": "9.3",
                    "title": "Molybdenum Breakthrough Regulatory Limit Verification in Generator Eluate",
                    "difficulty": "Intermediate",
                    "statement": r"""A nuclear pharmacy elutes a $^{99}\text{Mo}/^{99m}\text{Tc}$ generator at 07:00, obtaining:
- $^{99m}\text{Tc}$ activity: $A_{\text{Tc}} = 850\text{ mCi}$ ($31.45\text{ GBq}$)
- $^{99}\text{Mo}$ breakthrough activity (measured in lead canister): $A_{\text{Mo}} = 35.0\,\mu\text{Ci}$ ($1.295\text{ MBq}$)
The regulatory limit is $\le 0.150\,\mu\text{Ci } ^{99}\text{Mo} / \text{mCi } ^{99m}\text{Tc}$ **at the time of patient administration**.
1. Calculate the breakthrough ratio at 07:00 (elution time) and determine if it passes initial release.
2. Because $^{99m}\text{Tc}$ decays faster ($T_{1/2} = 6.01\text{ h}$) than $^{99}\text{Mo}$ ($T_{1/2} = 66.0\text{ h}$), the ratio increases over time. Calculate the exact time (in hours past elution) at which the breakthrough ratio will exceed the regulatory limit.
3. State whether a dose administered at 17:00 (10 hours post-elution) complies with the law.""",
                    "solution": r"""### Step 1: Breakthrough Ratio at 07:00
$$R(0) = \frac{A_{\text{Mo}}(0)}{A_{\text{Tc}}(0)} = \frac{35.0\,\mu\text{Ci}}{850\text{ mCi}} \approx 0.04118\,\mu\text{Ci/mCi}$$
Because $0.0412 < 0.150\,\mu\text{Ci/mCi}$, the eluate passes initial release testing.

### Step 2: Time Evolution of Breakthrough Ratio
Decay constants:
$$\lambda_{\text{Tc}} = \frac{\ln 2}{6.007\text{ h}} \approx 0.11539\text{ h}^{-1}$$
$$\lambda_{\text{Mo}} = \frac{\ln 2}{66.00\text{ h}} \approx 0.01050\text{ h}^{-1}$$
$$\Delta \lambda = \lambda_{\text{Tc}} - \lambda_{\text{Mo}} = 0.11539 - 0.01050 = 0.10489\text{ h}^{-1}$$
The breakthrough ratio at time $t$ is:
$$R(t) = \frac{A_{\text{Mo}}(0) e^{-\lambda_{\text{Mo}} t}}{A_{\text{Tc}}(0) e^{-\lambda_{\text{Tc}} t}} = R(0) \cdot e^{(\lambda_{\text{Tc}} - \lambda_{\text{Mo}}) t} = R(0) \cdot e^{\Delta \lambda \cdot t}$$
Set $R(t_{\text{limit}}) = 0.150\,\mu\text{Ci/mCi}$:
$$0.150 = 0.04118 \cdot e^{0.10489 \cdot t_{\text{limit}}}$$
$$e^{0.10489 \cdot t_{\text{limit}}} = \frac{0.150}{0.04118} \approx 3.6425$$
Taking natural logarithms:
$$0.10489 \cdot t_{\text{limit}} = \ln(3.6425) \approx 1.29267$$
$$t_{\text{limit}} = \frac{1.29267}{0.10489\text{ h}^{-1}} \approx 12.32\text{ hours}$$
The eluate expires **$12.32\text{ hours}$** post-elution (at 19:19).

### Step 3: Evaluation at 17:00 (10 Hours Post-Elution)
At $t = 10.0\text{ hours}$:
$$R(10) = 0.04118 \cdot e^{0.10489 \times 10} = 0.04118 \cdot e^{1.0489} = 0.04118 \times 2.8545 \approx 0.1175\,\mu\text{Ci/mCi}$$
Because $0.1175 < 0.150\,\mu\text{Ci/mCi}$, the dose is **fully compliant and safe to administer** at 17:00.""",
                    "hints": ["The breakthrough ratio escalates over time as exp((lambda_Tc - lambda_Mo) * t).", "Solve R(t) = 0.150 uCi/mCi for t_limit."]
                },
                {
                    "id": "prob-9-4",
                    "problemNumber": "9.4",
                    "title": "Ge-68 / Ga-68 Generator Secular vs Transient Growth Kinetics",
                    "difficulty": "Intermediate",
                    "statement": r"""A $^{68}\text{Ge}/^{68}\text{Ga}$ PET generator uses parent $^{68}\text{Ge}$ ($T_{1/2,1} = 270.95\text{ days}$) and daughter $^{68}\text{Ga}$ ($T_{1/2,2} = 67.71\text{ min} = 1.1285\text{ hours}$).
Immediately following elution at $t = 0$, daughter activity on the column is zero ($A_2(0) = 0$).
1. State which equilibrium regime governs this generator (Secular or Transient).
2. Calculate the decay constant of $^{68}\text{Ga}$ in $\text{min}^{-1}$ and $\text{h}^{-1}$.
3. Calculate the time (in hours and minutes) required for the $^{68}\text{Ga}$ daughter activity to reach $50\%$ and $90\%$ of parent activity.""",
                    "solution": r"""### Step 1: Equilibrium Classification
Because $T_{1/2,1} = 271\text{ days} \gg T_{1/2,2} = 1.13\text{ hours}$ (ratio $>5,700$), the generator resides in strict **Secular Equilibrium**:
$$\lambda_1 \ll \lambda_2 \implies A_2(t) \approx A_1(0) (1 - e^{-\lambda_2 t})$$

### Step 2: Decay Constant of $^{68}\text{Ga}$
$$\lambda_2 = \frac{\ln 2}{67.71\text{ min}} \approx 0.010237\text{ min}^{-1}$$
$$\lambda_{2,\text{hour}} = \frac{\ln 2}{1.1285\text{ h}} \approx 0.61422\text{ h}^{-1}$$

### Step 3: Time to 50% and 90% In-Growth
1. **To reach $50\%$ ($A_2 = 0.5 A_1$)**:
$$1 - e^{-\lambda_2 t_{50}} = 0.50 \implies e^{-\lambda_2 t_{50}} = 0.50 \implies t_{50} = T_{1/2,2} = 67.7\text{ min} \approx 1\text{ h } 8\text{ min}$$

2. **To reach $90\%$ ($A_2 = 0.90 A_1$)**:
$$1 - e^{-\lambda_2 t_{90}} = 0.90 \implies e^{-\lambda_2 t_{90}} = 0.10$$
$$-\lambda_2 t_{90} = \ln(0.10) = -2.302585$$
$$t_{90} = \frac{2.302585}{0.010237\text{ min}^{-1}} \approx 224.93\text{ minutes} \approx 3\text{ hours } 45\text{ minutes}$$
The generator regenerates to $90\%$ capacity in under **$3.75\text{ hours}$**, enabling up to 3 elutions per clinical working day!""",
                    "hints": ["Because T_half(parent) >> T_half(daughter), in-growth is secular: A_2(t) = A_1 * (1 - exp(-lambda_2 * t)).", "50% in-growth takes exactly one daughter half-life."]
                },
                {
                    "id": "prob-9-5",
                    "problemNumber": "9.5",
                    "title": "Medical Cyclotron Fluorine-18 Production Yield Calculation",
                    "difficulty": "Advanced",
                    "statement": r"""A biomedical cyclotron produces $^{18}\text{F}$ via the $^{18}\text{O}(p, n)^{18}\text{F}$ reaction on an enriched $\text{H}_2^{18}\text{O}$ liquid water target ($98.0\text{ atom } \% \, ^{18}\text{O}$, density $\rho = 1.11\text{ g/cm}^3$).
The effective cross-section averaged over the proton beam slowing-down profile ($16.0\text{ MeV} \to 3.0\text{ MeV}$) is $\bar{\sigma} = 320\text{ mbarns}$.
The target thickness $x = 0.250\text{ cm}$ fully stops the beam.
The proton beam current is $I_p = 35.0\,\mu\text{A}$.
The irradiation duration is $t_{\text{irr}} = 60.0\text{ minutes}$.
1. Calculate the incident proton flux rate $\dot{N}_p$ in protons per second.
2. Compute the number density $n_{18}$ of $^{18}\text{O}$ atoms in the target.
3. Determine the production rate $R$ in atoms per second and saturation activity $A_{\text{sat}}$ in $\text{GBq}$.
4. Calculate the activity of $^{18}\text{F}$ ($T_{1/2} = 109.8\text{ min}$) produced at the End of Bombardment (EOB) in $\text{GBq}$ and in $\text{mCi}$.""",
                    "solution": r"""### Step 1: Proton Beam Flux Rate
Beam current $I_p = 35.0\,\mu\text{A} = 35.0 \times 10^{-6}\text{ C/s}$.
$$\dot{N}_p = \frac{I_p}{e} = \frac{35.0 \times 10^{-6}\text{ C/s}}{1.60218 \times 10^{-19}\text{ C/proton}} \approx 2.1845 \times 10^{14}\text{ protons/second}$$

### Step 2: Number Density $n_{18}$ of $^{18}\text{O}$
Molar mass of $\text{H}_2^{18}\text{O} \approx 2.016 + 18.000 = 20.016\text{ g/mol}$.
$$n_{18} = \frac{\rho \cdot 0.980}{M} N_A = \frac{(1.11\text{ g/cm}^3)(0.980)}{20.016\text{ g/mol}} \times 6.022 \times 10^{23}\text{ mol}^{-1} \approx 3.273 \times 10^{22}\text{ atoms/cm}^3$$

### Step 3: Production Rate $R$
Target area density product:
$$n_{18} x = (3.273 \times 10^{22}\text{ cm}^{-3})(0.250\text{ cm}) \approx 8.1825 \times 10^{21}\text{ atoms/cm}^2$$
Cross-section:
$$\bar{\sigma} = 320\text{ mb} = 3.20 \times 10^{-25}\text{ cm}^2$$
Production rate:
$$R = \dot{N}_p (n_{18} x) \bar{\sigma} = (2.1845 \times 10^{14}\text{ s}^{-1})(8.1825 \times 10^{21}\text{ cm}^{-2})(3.20 \times 10^{-25}\text{ cm}^2)$$
$$R \approx 5.7196 \times 10^{11}\text{ atoms/second}$$
Saturation activity:
$$A_{\text{sat}} = R = 5.72 \times 10^{11}\text{ Bq} = 572\text{ GBq}$$

### Step 4: Activity at EOB
Irradiation time $t_{\text{irr}} = 60.0\text{ min}$.
$$\lambda = \frac{\ln 2}{109.77\text{ min}} \approx 0.0063145\text{ min}^{-1}$$
Saturation factor:
$$1 - e^{-\lambda t_{\text{irr}}} = 1 - e^{-(0.0063145 \times 60.0)} = 1 - e^{-0.37887} = 1 - 0.68463 = 0.31537$$
Activity at EOB:
$$A_{\text{EOB}} = A_{\text{sat}} \times 0.31537 = 571.96\text{ GBq} \times 0.31537 \approx 180.38\text{ GBq}$$
In Curies:
$$A_{\text{EOB}} = \frac{180.38\text{ GBq}}{37\text{ GBq/Ci}} \approx 4.875\text{ Ci} = 4,875\text{ mCi}$$
The cyclotron batch yields **$4.88\text{ Curies}$** of $^{18}\text{F}$, sufficient to formulate doses for dozens of clinical patient scans.""",
                    "hints": ["Beam proton rate is I / e.", "Activity at EOB is R * (1 - exp(-lambda * t_irr))."]
                },
                {
                    "id": "prob-9-6",
                    "problemNumber": "9.6",
                    "title": "Industrial Cobalt-60 Radiotherapy Source Activity and Shield Decay",
                    "difficulty": "Easy",
                    "statement": r"""A newly commissioned cancer teletherapy unit contains a sealed $^{60}\text{Co}$ source ($T_{1/2} = 5.271\text{ years}$) with initial activity $A_0 = 10.0\text{ kCi}$ ($370\text{ TBq}$).
1. Calculate the decay constant $\lambda$ in $\text{yr}^{-1}$.
2. Determine the source activity in kCi after $3.0\text{ years}$ and after $10.0\text{ years}$ of continuous clinical use.
3. Calculate the time elapsed when the source activity drops to $2.50\text{ kCi}$ ($25\%$ of initial activity), requiring source replacement.""",
                    "solution": r"""### Step 1: Decay Constant $\lambda$
$$\lambda = \frac{\ln 2}{5.271\text{ yr}} \approx 0.13150\text{ yr}^{-1}$$

### Step 2: Activity Over Time
1. **At $t = 3.0\text{ years}$**:
$$A(3) = 10.0\text{ kCi} \times e^{-0.13150 \times 3} = 10.0 \times e^{-0.3945} = 10.0 \times 0.6740 \approx 6.74\text{ kCi} \quad (249\text{ TBq})$$

2. **At $t = 10.0\text{ years}$**:
$$A(10) = 10.0\text{ kCi} \times e^{-0.13150 \times 10} = 10.0 \times e^{-1.3150} = 10.0 \times 0.2685 \approx 2.685\text{ kCi} \quad (99.3\text{ TBq})$$

### Step 3: Replacement Time ($25\%$ Initial Activity)
Because $25\% = (1/2)^2$, exactly **two half-lives** have elapsed:
$$t_{\text{replace}} = 2 \times T_{1/2} = 2 \times 5.271\text{ yr} = 10.542\text{ years} \approx 10.5\text{ years}$$
The cobalt source must be replaced after **$10.5\text{ years}$**.""",
                    "hints": ["Decay law A(t) = A_0 * exp(-lambda * t).", "25% activity is reached after exactly two half-lives (2 * T_1/2)."]
                },
                {
                    "id": "prob-9-7",
                    "problemNumber": "9.7",
                    "title": "Actinium-225 Targeted Alpha Therapy Cascade Yield",
                    "difficulty": "Intermediate",
                    "statement": r"""Actinium-225 ($^{225}_{89}\text{Ac}$, $T_{1/2} = 9.920\text{ days}$) decays through a cascade of 4 alpha decays to stable bismuth/lead:
$$^{225}\text{Ac} \xrightarrow{\alpha} \, ^{221}\text{Fr} \xrightarrow{\alpha} \, ^{217}\text{At} \xrightarrow{\alpha} \, ^{213}\text{Bi} \xrightarrow{\beta^-/\alpha} \, ^{209}\text{Pb}$$
The intermediate daughters have extremely short half-lives ($T_{1/2} < 45.6\text{ min}$).
A clinical vial contains $A_0 = 10.0\text{ MBq}$ of pure $^{225}\text{Ac}$ in secular equilibrium with its daughters.
1. State the activity of each daughter in the vial.
2. How many total alpha particles are emitted per second by the vial?
3. Calculate the total alpha energy rate (power) delivered in microwatts ($\mu\text{W}$) given the 4 alpha energies: $5.83\text{ MeV}$, $6.34\text{ MeV}$, $7.07\text{ MeV}$, and $8.38\text{ MeV}$.""",
                    "solution": r"""### Step 1: Daughter Activities
Because the intermediate daughter half-lives ($4.9\text{ min}, 32.3\text{ ms}, 45.6\text{ min}$) are thousands of times shorter than $^{225}\text{Ac}$ ($9.92\text{ days}$), the cascade resides in complete **Secular Equilibrium**:
$$A(^{221}\text{Fr}) = A(^{217}\text{At}) = A(^{213}\text{Bi}) = A(^{225}\text{Ac}) = 10.0\text{ MBq}$$

### Step 2: Total Alpha Emission Rate
Each disintegration of an $^{225}\text{Ac}$ nucleus releases 4 alpha particles:
$$\dot{N}_\alpha = 4 \times A(^{225}\text{Ac}) = 4 \times (10.0 \times 10^6\text{ Bq}) = 4.00 \times 10^7\text{ alpha particles/second}$$

### Step 3: Alpha Power Delivered
Total alpha energy per decay:
$$E_{\alpha,\text{total}} = 5.83 + 6.34 + 7.07 + 8.38 = 27.62\text{ MeV}$$
In Joules:
$$E_{\alpha,\text{total}} = 27.62 \times 1.60218 \times 10^{-13}\text{ J} \approx 4.4252 \times 10^{-12}\text{ J per decay}$$
Total power:
$$P = A \cdot E_{\alpha,\text{total}} = (1.00 \times 10^7\text{ s}^{-1})(4.4252 \times 10^{-12}\text{ J}) = 4.4252 \times 10^{-5}\text{ Watts} \approx 44.25\,\mu\text{W}$$
The vial delivers **$44.3\text{ microwatts}$** of concentrated alpha radiation directly into targeted cancer cells.""",
                    "hints": ["In secular equilibrium, the activity of each short-lived daughter equals the parent activity.", "Total power is activity multiplied by total energy released per decay."]
                }
            ]
        },

        # =====================================================================
        # UNIT 10
        # =====================================================================
        {
            "id": "unit-10-dosimetry-radiobiology-radioprotection",
            "unitNumber": 10,
            "title": "Unit 10: Radiation Dosimetry, Radiobiology & Radioprotection (ALARA)",
            "leadSummary": "Comprehensive metrological, biological, and operational framework for radiation safety: fundamental physical dosimetric quantities (Exposure, Absorbed Dose, Equivalent Dose, Effective Dose); the Bragg-Gray cavity principle; molecular radiobiology and water radiolysis; DNA double-strand break repair and the Linear-Quadratic cell survival model; deterministic tissue reactions versus stochastic carcinogenesis; the ALARA philosophy; and shielding attenuation optimization.",
            "simulations": ["sim_nuc_bragg_peak_stopping_power", "sim_nuc_gamma_interaction_modes"],
            "sections": [
                {
                    "id": "sec-1-1-dosimetry",
                    "secNumber": "10.1",
                    "title": "Physical Dosimetric Quantities: Exposure, Absorbed Dose & the Bragg-Gray Cavity Principle",
                    "content": r"""Radiation dosimetry is the quantitative science of measuring and calculating the energy deposited by ionizing radiation in matter and biological tissue.

### 1. Exposure ($X$)
The historical quantity defining the ionizing capacity of X-ray and gamma-ray photons in dry air under conditions of electronic equilibrium:
$$X = \frac{dQ}{dm}$$
where $dQ$ is the total electrical charge of ions of one sign produced in air when all secondary electrons liberated by photons in dry air of mass $dm$ are completely stopped.
- **SI Unit**: Coulomb per kilogram ($\text{C/kg}$).
- **Traditional Unit: The Roentgen (R)**:
$$1\text{ R} \equiv 2.58 \times 10^{-4}\text{ C/kg of dry air (exactly)}$$
Because producing one ion pair in dry air requires $W_{\text{air}} \approx 33.97\text{ eV} = 33.97\text{ J/C}$, an exposure of $1\text{ R}$ corresponds to an energy absorption of:
$$D_{\text{air}}(1\text{ R}) = (2.58 \times 10^{-4}\text{ C/kg})(33.97\text{ J/C}) \approx 8.76 \times 10^{-3}\text{ J/kg} = 0.876\text{ rad} = 8.76\text{ mGy}$$

### 2. Absorbed Dose ($D$)
The fundamental physical quantity applicable to **all types of ionizing radiation** (photons, electrons, neutrons, heavy ions) in **any absorbing material**:
$$D = \frac{d\bar{\epsilon}}{dm}$$
where $d\bar{\epsilon}$ is the mean energy imparted by ionizing radiation to matter of mass $dm$.
- **SI Unit: The Gray (Gy)**:
$$1\text{ Gy} \equiv 1\text{ Joule per kilogram (J/kg)}$$
- **Traditional Unit: The rad (radiation absorbed dose)**:
$$1\text{ rad} \equiv 100\text{ erg/g} = 0.01\text{ J/kg} = 0.01\text{ Gy} \quad (1\text{ Gy} = 100\text{ rad})$$

### 3. Kerma ($K$, Kinetic Energy Released per unit MAss)
For uncharged radiation (photons and neutrons), **Kerma** quantifies the kinetic energy transferred to initial secondary charged particles:
$$K = \frac{dE_{\text{tr}}}{dm}$$
Under conditions of **Charged Particle Equilibrium (CPE)** where radiative losses are negligible:
$$D = K_{\text{col}} \approx K$$

### 4. The Bragg-Gray Cavity Principle
To measure absorbed dose inside a solid medium (e.g., patient tissue or water phantom), an ionization gas cavity is introduced.
According to the Bragg-Gray theorem, if the cavity is sufficiently small that it does not perturb the fluence of secondary electrons crossing it:
$$D_{\text{med}} = D_{\text{gas}} \cdot \bar{s}_{\text{med, gas}} = \left(\frac{Q}{m_{\text{gas}}} \frac{W_{\text{gas}}}{e}\right) \bar{s}_{\text{med, gas}}$$
where $\bar{s}_{\text{med, gas}} = (S/\rho)_{\text{med}} / (S/\rho)_{\text{gas}}$ is the ratio of mass stopping powers of the medium to the cavity gas. This allows ionization current measured in a gas chamber to be converted directly into absorbed dose in patient tissue.""",
                    "simulations": ["sim_nuc_bragg_peak_stopping_power"]
                },
                {
                    "id": "sec-10-2",
                    "secNumber": "10.2",
                    "title": "Radiation Weighting Factors, Equivalent Dose & Tissue-Weighted Effective Dose",
                    "content": r"""Absorbed dose ($D$, in Grays) quantifies physical energy deposition, but **does not describe biological damage**. A dose of $1\text{ Gy}$ delivered by dense alpha particles produces vastly greater biological lethality than $1\text{ Gy}$ delivered by dispersed gamma photons.

### 1. Equivalent Dose ($H_T$)
To quantify biological risk across different radiation modalities, the International Commission on Radiological Protection (ICRP) defines the **Equivalent Dose** $H_T$ in an organ or tissue $T$:
$$H_T \equiv \sum_R w_R \cdot D_{T, R}$$
where $D_{T, R}$ is the absorbed dose delivered by radiation type $R$, and $w_R$ is the dimensionless **Radiation Weighting Factor**:

| Radiation Type and Energy Spectrum | Radiation Weighting Factor ($w_R$) | Biological Justification |
| :--- | :--- | :--- |
| **Photons (X-rays, $\gamma$-rays, all energies)** | **$1$** | Reference low-LET standard |
| **Electrons, positrons, muons (all energies)** | **$1$** | Sparsely ionizing track structure |
| **Protons and charged pions** | **$2$** | Moderate linear energy transfer |
| **Alpha particles, fission fragments, heavy ions** | **$20$** | High LET ($\sim 100\text{ keV}/\mu\text{m}$), dense double-strand breaks |
| **Neutrons: Thermal ($< 1\text{ keV}$)** | **$2.5$** | Indirect proton recoil / capture |
| **Neutrons: Epithermal & Fast ($0.1 - 2\text{ MeV}$)** | **$20$** (Peak at $1\text{ MeV}$) | Maximum recoil proton stopping power |
| **Neutrons: High Energy ($> 20\text{ MeV}$)** | **$5 - 10$** | Nuclear spallation reactions |

- **SI Unit: The Sievert (Sv)**:
$$1\text{ Sv} \equiv 1\text{ J/kg} \quad (\text{Subunits: } \text{mSv} = 10^{-3}\text{ Sv}, \, \mu\text{Sv} = 10^{-6}\text{ Sv})$$
- **Traditional Unit: The rem (Roentgen equivalent man)**:
$$1\text{ rem} \equiv 0.01\text{ Sv} = 10\text{ mSv} \quad (1\text{ Sv} = 100\text{ rem})$$

### 2. Effective Dose ($E$)
Different human organs and tissues exhibit vastly different sensitivities to radiation-induced cancer and genetic damage.
The **Effective Dose** $E$ quantifies the overall stochastic health risk to the entire individual:
$$E \equiv \sum_T w_T \cdot H_T = \sum_T w_T \left( \sum_R w_R \cdot D_{T, R} \right)$$
where $w_T$ is the **Tissue Weighting Factor** representing the relative contribution of organ $T$ to total stochastic risk:

```
 TISSUE / ORGAN (ICRP Publication 103)                        w_T     FRACTION
 ─────────────────────────────────────────────────────────────────────────────
 Red Bone Marrow, Colon, Lung, Stomach, Breast, Remainder    0.12 ea  72.0%
 Gonads (Testes / Ovaries - Genetic Hereditary Detriment)     0.08      8.0%
 Urinary Bladder, Esophagus, Liver, Thyroid                   0.04 ea  16.0%
 Bone Surface, Brain, Salivary Glands, Skin                  0.01 ea   4.0%
 ─────────────────────────────────────────────────────────────────────────────
 TOTAL SUM (Whole Body Normalized):                          1.00     100.0%
```

Effective dose allows partial-body medical exposures (e.g., a chest CT scan delivering $7\text{ mSv}$) to be compared directly with whole-body natural background radiation ($\approx 2.4 - 3.0\text{ mSv/year}$).""",
                    "simulations": ["sim_nuc_bragg_peak_stopping_power"]
                },
                {
                    "id": "sec-10-3",
                    "secNumber": "10.3",
                    "title": "Molecular Radiobiology: Radiolysis of Water, Free Radical Cascades & DNA Double-Strand Breaks",
                    "content": r"""Living biological cells consist of approximately $70 - 85\%$ liquid water. When ionizing radiation traverses biological tissue, energy deposition damages critical cellular targets via two distinct pathways:

```
                    IONIZING RADIATION
                            │
            ┌───────────────┴───────────────┐
            ▼ (~35%)                        ▼ (~65%)
      DIRECT ACTION                   INDIRECT ACTION
   Direct ionization of              Radiolysis of cellular water
   nuclear DNA macromolecule         (Free radical generation: •OH)
            │                               │
            │                               ▼
            └───────────────────────► DNA LESIONS
                                      (Single & Double Strand Breaks)
```

### The Radiolysis of Water
Within $10^{-16}\text{ to }10^{-12}\text{ seconds}$ of radiation passage, water molecules undergo ionization and electronic excitation:
$$\text{H}_2\text{O} \rightsquigarrow \text{H}_2\text{O}^{+\bullet} + e^-$$
$$\text{H}_2\text{O} \rightsquigarrow \text{H}_2\text{O}^*$$

1. **Hydrated Electron Formation**:
The ejected fast electron thermalizes and becomes trapped in the dielectric dipole cage of surrounding water molecules within $\sim 1\text{ picosecond}$:
$$e^- + n \text{H}_2\text{O} \longrightarrow e_{\text{aq}}^- \quad (\text{Hydrated Electron: powerful reducing agent, } E^\circ = -2.87\text{ V})$$
2. **Hydroxyl Radical Generation**:
The radical cation $\text{H}_2\text{O}^{+\bullet}$ reacts with neighboring water via ultrafast proton transfer:
$$\text{H}_2\text{O}^{+\bullet} + \text{H}_2\text{O} \longrightarrow \text{H}_3\text{O}^+ + \cdot\text{OH}$$
The **hydroxyl radical ($\cdot\text{OH}$)** is an extraordinarily reactive, neutral oxidizer ($E^\circ = +2.80\text{ V}$) responsible for over **$65\%$ of all indirect DNA damage** in biological cells.
3. **Hydrogen Radicals and Radiolytic Products**:
$$\text{H}_2\text{O}^* \longrightarrow \text{H}\cdot + \cdot\text{OH}$$
$$\cdot\text{OH} + \cdot\text{OH} \longrightarrow \text{H}_2\text{O}_2 \quad (\text{Hydrogen Peroxide})$$
$$\text{H}\cdot + \text{O}_2 \longrightarrow \text{HO}_2\cdot \rightleftharpoons \text{H}^+ + \text{O}_2^{-\bullet} \quad (\text{Superoxide Radical})$$

### DNA Lesion Spectrum and Double-Strand Breaks (DSBs)
A typical mammalian cell nucleus ($V \approx 500\,\mu\text{m}^3$) contains $6 \times 10^9$ base pairs of double-helical genomic DNA.
A uniform absorbed dose of $1\text{ Gy}$ of low-LET X-rays produces:
- $\sim 100,000$ water ionization events.
- $\sim 1,000 - 2,000$ base damages (oxidized guanines, e.g., 8-oxo-dG).
- $\sim 1,000$ Single-Strand Breaks (SSBs).
- **$\sim 40$ Double-Strand Breaks (DSBs)**.

While SSBs are repaired with high fidelity by DNA ligases using the intact complementary strand as a template, **Double-Strand Breaks** (where both opposing phosphodiester backbones are severed within $10 - 20$ base pairs) represent the critical lethal lesion.
Misrepair of DSBs via Non-Homologous End Joining (NHEJ) causes dicentric chromosomal aberrations, ring chromosomes, translocations, and apoptotic cell death.""",
                    "simulations": ["sim_nuc_bragg_peak_stopping_power"]
                },
                {
                    "id": "sec-10-4",
                    "secNumber": "10.4",
                    "title": "Linear Energy Transfer (LET), Relative Biological Effectiveness (RBE) & the Linear-Quadratic Model",
                    "content": r"""The biological consequence of a given absorbed dose depends fundamentally on the spatial track structure of ionization events, characterized by **Linear Energy Transfer (LET)**.

### Linear Energy Transfer (LET)
LET quantifies the average energy transferred locally to the absorbing medium per unit path length ($\text{keV}/\mu\text{m}$):
$$L_\Delta = \left(\frac{dE}{dx}\right)_\Delta$$
- **Low-LET Radiation** ($< 10\text{ keV}/\mu\text{m}$): Cobalt-60 gamma rays ($0.2\text{ keV}/\mu\text{m}$), $250\text{ kVp}$ X-rays ($2\text{ keV}/\mu\text{m}$), fast electrons. Ionization events are spaced hundreds of nanometers apart, producing isolated, easily repairable lesions.
- **High-LET Radiation** ($> 20\text{ keV}/\mu\text{m}$): Alpha particles ($100\text{ keV}/\mu\text{m}$), heavy recoil ions ($>1000\text{ keV}/\mu\text{m}$). Ionization events form dense, continuous columns that deposit dozens of ion pairs across a single $2\text{ nm}$ DNA diameter, producing complex, unrepairable clustered damage.

### Relative Biological Effectiveness (RBE)
RBE is defined as the ratio of absorbed dose of reference $250\text{ kVp}$ X-rays ($D_{\text{ref}}$) to the dose of test radiation ($D_{\text{test}}$) required to achieve an identical biological endpoint (e.g., $10\%$ cell survival):
$$\text{RBE} \equiv \left. \frac{D_{\text{ref}}}{D_{\text{test}}} \right|_{\text{equal effect}}$$

```
 RBE (Relative Biological Effectiveness)
  ▲
  │                     PEAK RBE (~ 100 keV/μm)
  │                        /\
  │                       /  \
  │                      /    \  Overkill Effect
  │  Low-LET            /      \ (Wasted Dose)
  │  ───────┐          /        \_____
  │         └─────────/
  └───────────────────┴──────────┴────► LET (keV / μm)
  0.1                 10        100   1000
```

- As LET increases from $1$ to $100\text{ keV}/\mu\text{m}$, RBE climbs steeply to a **maximum peak at $\approx 100\text{ keV}/\mu\text{m}$**. At this optimal density, the average spacing between ionizing events ($\sim 2\text{ nm}$) corresponds precisely to the diameter of the DNA double helix!
- Beyond $100\text{ keV}/\mu\text{m}$, RBE drops due to the **overkill effect**: more energy is deposited in the cell nucleus than is required for cell sterilization, wasting excess dose.

### The Linear-Quadratic (LQ) Cell Survival Model
Cell survival curves plot surviving fraction $S(D)$ versus absorbed dose $D$.
The universally accepted biophysical model is the **Linear-Quadratic Model**:
$$S(D) = \exp\left( -\alpha D - \beta D^2 \right)$$
where:
- $\alpha$ is the linear coefficient ($\text{Gy}^{-1}$), representing lethal single-hit "unrepairable" track damage (intra-track DSB).
- $\beta$ is the quadratic coefficient ($\text{Gy}^{-2}$), representing two independent radiation tracks interacting to produce a lethal lesion (inter-track repairable damage).
- The ratio $\alpha/\beta$ (units of $\text{Gy}$) defines the dose at which the linear and quadratic cell-killing contributions are equal ($\alpha D = \beta D^2 \implies D = \alpha/\beta$).
  - **Early-responding tissues / Tumors**: High $\alpha/\beta \approx 10\text{ Gy}$ (steep linear survival, minimal fractionation sparing).
  - **Late-responding normal tissues**: Low $\alpha/\beta \approx 2 - 3\text{ Gy}$ (broad curve shoulder, massive sparing with fractionated radiation therapy).""",
                    "simulations": ["sim_nuc_bragg_peak_stopping_power"]
                },
                {
                    "id": "sec-10-5",
                    "secNumber": "10.5",
                    "title": "Deterministic Tissue Reactions Versus Stochastic Carcinogenesis & the LNT Paradigm",
                    "content": r"""The biological consequences of ionizing radiation are categorized into two fundamentally distinct classes:

### 1. Deterministic Effects (Tissue Reactions)
Arise from radiation-induced killing of large populations of functional tissue cells:
- **Threshold Dose**: A clear, finite dose threshold $D_{\text{th}}$ exists below which no clinical effect is observable. Above the threshold, the **severity of the injury increases monotonically with dose**.
- **Pathology**: Acute cell depletion, vascular damage, and fibrotic tissue death.
- **Representative Thresholds**:
  - **Temporary Sterility (Testes)**: $0.15\text{ Gy}$ ($150\text{ mGy}$).
  - **Depression of Hematopoiesis (Bone Marrow)**: $0.50\text{ Gy}$.
  - **Skin Erythema (Reddening)**: $3 - 5\text{ Gy}$; Dry Desquamation: $10\text{ Gy}$; Necrosis: $>15\text{ Gy}$.
  - **Radiation Cataractogenesis (Lens of Eye)**: $0.5\text{ Gy}$ (ICRP 118).
  - **Acute Radiation Syndrome (ARS, Whole Body)**:
    - Hematopoietic Syndrome: $1 - 6\text{ Gy}$ ($50\%$ lethal dose without medical care: $\text{LD}_{50/60} \approx 3.5 - 4.0\text{ Gy}$).
    - Gastrointestinal (GI) Syndrome: $6 - 20\text{ Gy}$ (destruction of crypt stem cells; lethal within $1 - 2\text{ weeks}$).
    - Cerebrovascular Syndrome: $>20 - 50\text{ Gy}$ (cardiovascular collapse and brain edema; lethal within $24 - 48\text{ hours}$).

### 2. Stochastic Effects (Cancer and Heritable Mutations)
Arise from non-lethal, mutagenic alteration of a single somatic stem cell that survives with an oncogenic mutation:
- **No Threshold**: Governed by probability rather than severity. Even an infinitesimal dose has a non-zero probability of inducing a malignant transformation.
- **Severity is Independent of Dose**: A cancer induced by a $10\text{ mSv}$ dose is clinically identical to one induced by a $1000\text{ mSv}$ dose; **only the probability of occurrence scales with dose**.
- **Latent Period**: Solid cancers manifest after long latency periods ($10 - 40\text{ years}$); leukemias manifest after $2 - 10\text{ years}$.

```
      STOCHASTIC EFFECTS                           DETERMINISTIC EFFECTS
  Probability of Cancer                          Severity of Tissue Injury
  ▲                                              ▲
  │                /                             │                     /
  │               /                              │                    /
  │              /                               │                   /
  │  LNT Model  /                                │                  /
  │            /                                 │                 /
  │           /                                  │                /
  │          /                                   │               /
  │_________/                                    │______________/_
  └─────────┴────────────────► Dose D            └──────────────┴─────► Dose D
  0                                              0             D_th (Threshold)
```

### The Linear No-Threshold (LNT) Model
For radiation protection regulation, the ICRP, NCRP, and IAEA adopt the **Linear No-Threshold (LNT) hypothesis**:
The excess lifetime risk of fatal stochastic cancer is assumed to be strictly proportional to effective dose, extrapolating linearly from high-dose epidemiological data (Hiroshima and Nagasaki atomic bomb survivors, Life Span Study LSS) down to zero dose.
- **ICRP Detriment Coefficient**:
$$\text{Nominal Risk Coefficient} \approx 5.5\% \text{ per Sievert} = 5.5 \times 10^{-2}\text{ Sv}^{-1} \quad (0.0055\%\text{ per mSv})$$
For an occupational worker receiving an annual effective dose of $20\text{ mSv}$, the lifetime excess cancer mortality risk is:
$$\text{Risk} = (0.020\text{ Sv}) \times 0.055\text{ Sv}^{-1} = 0.0011 \quad (0.11\% \text{ or } 1 \text{ in } 900)$$""",
                    "simulations": ["sim_nuc_bragg_peak_stopping_power"]
                },
                {
                    "id": "sec-10-6",
                    "secNumber": "10.6",
                    "title": "Practical Radioprotection Metrology: Time, Distance (Inverse Square) & Shielding Optimization",
                    "content": r"""The operational foundation of external radiation protection rests on the three classical pillars: **Time**, **Distance**, and **Shielding**.

### 1. Time Optimization
The total accumulated absorbed dose $D$ is directly proportional to exposure duration $t$:
$$D = \dot{D} \cdot t$$
Minimizing residence time in a radiation field reduces dose proportionally. Practicing complex manipulation protocols using non-radioactive mockups ("dry runs") before handling high-activity sources minimizes hands-on handling time.

### 2. Distance Optimization (The Inverse Square Law)
For an isotropic point source emitting radiation, photon flux spreads over the spherical surface area $4\pi d^2$.
The radiation intensity and dose rate $\dot{D}$ decrease inversely with the square of the distance $d$:
$$\dot{D}(d) = \dot{D}_0 \left(\frac{d_0}{d}\right)^2 \implies \frac{\dot{D}_1}{\dot{D}_2} = \frac{d_2^2}{d_1^2}$$
Doubling distance ($2d$) reduces dose rate by a factor of **$4$** ($25\%$); increasing distance tenfold ($10d$) reduces dose rate by a factor of **$100$** ($1\%$)!
- **Practical Application**: Never touch unshielded gamma or beta sources with bare hands! Using a $30\text{ cm}$ remote handling tongs instead of direct fingertip contact ($1\text{ cm}$) reduces the dose rate by a factor of:
$$(30 / 1)^2 = 900 \text{ times}$$

### Gamma Constant ($\Gamma$) for Point Sources
The exposure rate $\dot{X}$ at distance $d$ from a point gamma emitter of activity $A$ is parameterized by the **Specific Gamma-Ray Constant** $\Gamma$:
$$\dot{X} = \frac{\Gamma \cdot A}{d^2}$$
For air kerma rate constant $\Gamma_\delta$ ($\mu\text{Gy}\cdot\text{m}^2/\text{GBq}\cdot\text{h}$):
- $^{60}\text{Co}$: $\Gamma \approx 308\,\mu\text{Gy}\cdot\text{m}^2 / (\text{GBq}\cdot\text{h}) = 1.32\text{ R}\cdot\text{m}^2 / (\text{Ci}\cdot\text{h})$
- $^{137}\text{Cs}$: $\Gamma \approx 78\,\mu\text{Gy}\cdot\text{m}^2 / (\text{GBq}\cdot\text{h}) = 0.33\text{ R}\cdot\text{m}^2 / (\text{Ci}\cdot\text{h})$
- $^{192}\text{Ir}$: $\Gamma \approx 115\,\mu\text{Gy}\cdot\text{m}^2 / (\text{GBq}\cdot\text{h}) = 0.48\text{ R}\cdot\text{m}^2 / (\text{Ci}\cdot\text{h})$
- $^{99m}\text{Tc}$: $\Gamma \approx 17\,\mu\text{Gy}\cdot\text{m}^2 / (\text{GBq}\cdot\text{h}) = 0.076\text{ R}\cdot\text{m}^2 / (\text{Ci}\cdot\text{h})$

### 3. Shielding Optimization
When distance and time limits are reached, physical barriers attenuate radiation exponentially:
$$\dot{D}(x) = \dot{D}_0 \cdot B(x, E) \cdot e^{-\mu x} = \dot{D}_0 \cdot B(x, E) \cdot 2^{-x / \text{HVL}} = \dot{D}_0 \cdot B(x, E) \cdot 10^{-x / \text{TVL}}$$
Combining distance and shielding:
$$\dot{D}(d, x) = \frac{\Gamma \cdot A}{d^2} \cdot B \cdot e^{-\mu x}$$""",
                    "simulations": ["sim_nuc_gamma_interaction_modes"]
                },
                {
                    "id": "sec-10-7",
                    "secNumber": "10.7",
                    "title": "The ALARA Philosophy, International Regulatory Frameworks & Internal Biokinetic Dosimetry",
                    "content": r"""Under the guidance of the International Commission on Radiological Protection (ICRP Publication 103), global radiation safety is governed by three fundamental ethical and operational principles:

1. **Justification**: No practice involving exposure to radiation should be adopted unless it produces a net positive societal or individual benefit sufficient to offset the radiation detriment.
2. **Optimization (The ALARA Principle)**: All exposures must be maintained **As Low As Reasonably Achievable (ALARA)**, economic and societal factors being taken into account.
3. **Dose Limitation**: Total individual doses must not exceed statutory regulatory limits to prevent deterministic effects and limit stochastic risk.

### Statutory Dose Limits (ICRP & IAEA Basic Safety Standards)

| Exposed Population Group | Effective Dose Limit (Whole Body) | Equivalent Dose: Lens of Eye | Equivalent Dose: Skin & Extremities |
| :--- | :--- | :--- | :--- |
| **Occupational Radiation Workers** | **$20\text{ mSv/year}$** (averaged over 5 yr; max $50\text{ mSv}$ in any single yr) | **$20\text{ mSv/year}$** (reduced from $150$) | **$500\text{ mSv/year}$** ($50\text{ rem}$) |
| **Pregnant Radiation Workers** | **$1\text{ mSv}$** to fetus post-declaration | — | — |
| **General Public** | **$1.0\text{ mSv/year}$** ($0.1\text{ rem/year}$) | **$15\text{ mSv/year}$** | **$50\text{ mSv/year}$** |

Notice that medical patients undergoing diagnostic or therapeutic procedures are **strictly exempt from dose limits**; their exposure is governed exclusively by clinical justification and protocol optimization.

### Internal Dosimetry & Biokinetic Compartmental Models
When radionuclides are inhaled, ingested, or absorbed into wounds, they distribute throughout biological compartments, delivering continuous internal radiation until eliminated by physical radioactive decay ($\lambda_p$) and biological clearance ($\lambda_b$).
The **effective elimination constant** $\lambda_{\text{eff}}$ is:
$$\lambda_{\text{eff}} = \lambda_p + \lambda_b \implies \frac{1}{T_{\text{eff}}} = \frac{1}{T_p} + \frac{1}{T_b} \implies T_{\text{eff}} = \frac{T_p \cdot T_b}{T_p + T_b}$$
The effective half-life $T_{\text{eff}}$ is **always strictly shorter** than both the physical half-life $T_p$ and biological clearance half-life $T_b$.
- Example: Cesium-137 ($^{137}\text{Cs}$): Physical $T_p = 30.17\text{ years}$, but biological clearance half-life in human tissue is $T_b \approx 70 - 100\text{ days}$. The internal effective half-life is $T_{\text{eff}} \approx 70 - 100\text{ days}$, preventing multi-decade internal retention.
- Example: Strontium-90 ($^{90}\text{Sr}$): Bone-seeker incorporated into hydroxyapatite mineral matrix ($T_b \approx 50\text{ years}$), giving an effective half-life $T_{\text{eff}} \approx 18\text{ years}$ and delivering high cumulative bone marrow dose.

The cumulative internal dose delivered over 50 years ($70\text{ years}$ for children) is quantified as the **Committed Effective Dose** $E(50)$:
$$E(50) = A_{\text{intake}} \cdot e(50)$$
where $e(50)$ is the radionuclide-specific dose coefficient ($\text{Sv/Bq}$).""",
                    "simulations": ["sim_nuc_bragg_peak_stopping_power"]
                }
            ],
            "problems": [
                {
                    "id": "prob-10-1",
                    "problemNumber": "10.1",
                    "title": "Whole-Body Effective Dose Calculation from Mixed Radiation Field",
                    "difficulty": "Easy",
                    "statement": r"""A nuclear research worker in an accelerator vault accidentally receives a non-uniform mixed radiation exposure:
- Lung receives $15.0\text{ mGy}$ of fast neutrons ($w_R = 20$).
- Red bone marrow receives $8.0\text{ mGy}$ of gamma photons ($w_R = 1$) and $2.0\text{ mGy}$ of fast neutrons ($w_R = 20$).
- Thyroid receives $25.0\text{ mGy}$ of gamma photons ($w_R = 1$).
Using ICRP tissue weighting factors: $w_T(\text{lung}) = 0.12$, $w_T(\text{marrow}) = 0.12$, and $w_T(\text{thyroid}) = 0.04$:
1. Calculate the Equivalent Dose $H_T$ to the lung, bone marrow, and thyroid in millisieverts ($\text{mSv}$).
2. Compute the total Effective Dose $E$ in $\text{mSv}$.
3. Compare the result with the annual occupational limit of $20\text{ mSv}$.""",
                    "solution": r"""### Step 1: Equivalent Dose $H_T = \sum w_R D_{T,R}$
1. **Lung**:
$$H_{\text{lung}} = w_R(\text{neutron}) \cdot D = 20 \times 15.0\text{ mGy} = 300.0\text{ mSv}$$

2. **Red Bone Marrow**:
$$H_{\text{marrow}} = (1 \times 8.0\text{ mGy}) + (20 \times 2.0\text{ mGy}) = 8.0 + 40.0 = 48.0\text{ mSv}$$

3. **Thyroid**:
$$H_{\text{thyroid}} = 1 \times 25.0\text{ mGy} = 25.0\text{ mSv}$$

### Step 2: Total Effective Dose $E = \sum w_T H_T$
$$E = [w_T(\text{lung}) \cdot H_{\text{lung}}] + [w_T(\text{marrow}) \cdot H_{\text{marrow}}] + [w_T(\text{thyroid}) \cdot H_{\text{thyroid}}]$$
$$E = (0.12 \times 300.0\text{ mSv}) + (0.12 \times 48.0\text{ mSv}) + (0.04 \times 25.0\text{ mSv})$$
$$E = 36.0\text{ mSv} + 5.76\text{ mSv} + 1.00\text{ mSv} = 42.76\text{ mSv}$$

### Step 3: Regulatory Compliance
The total effective dose is **$42.8\text{ mSv}$**, which **exceeds** the annual occupational limit of $20\text{ mSv}$ (though it is below the single-year cap of $50\text{ mSv}$). A formal radiological investigation and dose tracking over 5 years are required.""",
                    "hints": ["Equivalent dose H = sum(w_R * D).", "Effective dose E = sum(w_T * H)."]
                },
                {
                    "id": "prob-10-2",
                    "problemNumber": "10.2",
                    "title": "Industrial Cobalt-60 Exposure Rate and Lead Shielding Design",
                    "difficulty": "Intermediate",
                    "statement": r"""An industrial radiographer works at distance $d_1 = 5.00\text{ m}$ from an unshielded $A = 200\text{ Ci}$ ($7.40\text{ TBq}$) $^{60}\text{Co}$ source ($\Gamma = 1.32\text{ R}\cdot\text{m}^2/\text{Ci}\cdot\text{h}$).
1. Calculate the unshielded exposure rate $\dot{X}_1$ at $5.00\text{ m}$ in $\text{R/h}$ and the equivalent dose rate $\dot{H}_1$ in $\text{mSv/h}$ (using $1\text{ R} \approx 9.6\text{ mSv}$).
2. If the worker moves to $d_2 = 1.00\text{ m}$, compute the dose rate $\dot{H}_2$.
3. To work at $d = 2.00\text{ m}$ for $t = 8.0\text{ hours}$ without exceeding a daily administrative dose constraint of $0.10\text{ mSv}$ ($100\,\mu\text{Sv}$), determine the required thickness of lead shielding in centimeters ($\text{HVL}_{\text{Pb}} = 1.05\text{ cm}$).""",
                    "solution": r"""### Step 1: Unshielded Exposure Rate at $5.00\text{ m}$
$$\dot{X}_1 = \frac{\Gamma \cdot A}{d_1^2} = \frac{(1.32\text{ R}\cdot\text{m}^2/\text{Ci}\cdot\text{h})(200\text{ Ci})}{(5.00\text{ m})^2} = \frac{264}{25.0} = 10.56\text{ R/h}$$
Dose rate:
$$\dot{H}_1 = 10.56\text{ R/h} \times 9.6\text{ mSv/R} \approx 101.4\text{ mSv/h}$$

### Step 2: Dose Rate at $1.00\text{ m}$
Using inverse square law:
$$\dot{H}_2 = \dot{H}_1 \left(\frac{d_1}{d_2}\right)^2 = 101.4\text{ mSv/h} \times \left(\frac{5.00}{1.00}\right)^2 = 101.4 \times 25 = 2,535\text{ mSv/h} \approx 2.54\text{ Sv/h}$$
Standing $1\text{ meter}$ away delivers a lethal dose in barely 2 hours!

### Step 3: Shielding Design at $2.00\text{ m}$
Unshielded dose rate at $2.00\text{ m}$:
$$\dot{H}(2\text{ m}) = 101.4\text{ mSv/h} \times \left(\frac{5.00}{2.00}\right)^2 = 101.4 \times 6.25 \approx 633.75\text{ mSv/h}$$
Allowed dose rate for $8.0\text{ hours}$:
$$\dot{H}_{\text{allowed}} = \frac{0.10\text{ mSv}}{8.0\text{ h}} = 0.0125\text{ mSv/h}$$
Required attenuation factor $AF$:
$$AF = \frac{\dot{H}_{\text{unshielded}}}{\dot{H}_{\text{allowed}}} = \frac{633.75\text{ mSv/h}}{0.0125\text{ mSv/h}} = 50,700$$
Number of half-value layers ($n$):
$$2^n \ge 50,700 \implies n = \frac{\ln(50,700)}{\ln 2} = \frac{10.8337}{0.69315} \approx 15.63\text{ HVLs}$$
Shield thickness:
$$x = n \cdot \text{HVL} = 15.63 \times 1.05\text{ cm} \approx 16.41\text{ cm} = 164\text{ mm}$$
A lead shield of thickness **$16.4\text{ cm}$** ($6.5\text{ inches}$) is required.""",
                    "hints": ["Exposure rate dot(X) = Gamma * A / d^2.", "Required attenuation factor is dot(H)_unshielded / dot(H)_allowed."]
                },
                {
                    "id": "prob-10-3",
                    "problemNumber": "10.3",
                    "title": "Internal Radionuclide Effective Half-Life and Committed Dose for I-131",
                    "difficulty": "Easy",
                    "statement": r"""A nuclear medicine laboratory technician accidentally inhales radioactive iodine-131 vapor ($^{131}\text{I}$, $T_p = 8.025\text{ days}$).
In the thyroid gland, the biological clearance half-life of iodine is $T_b = 68.0\text{ days}$.
1. Calculate the effective elimination constant $\lambda_{\text{eff}}$ in $\text{days}^{-1}$ and the effective half-life $T_{\text{eff}}$ in days.
2. If the initial thyroid intake is $A_0 = 50.0\text{ kBq}$, calculate the remaining thyroid activity after $30.0\text{ days}$.
3. Using the ICRP thyroid committed dose coefficient $e(50) = 4.3 \times 10^{-7}\text{ Sv/Bq}$, determine the committed thyroid equivalent dose in millisieverts ($\text{mSv}$).""",
                    "solution": r"""### Step 1: Effective Half-Life $T_{\text{eff}}$
Physical and biological decay constants:
$$\lambda_p = \frac{\ln 2}{8.025\text{ d}} \approx 0.086373\text{ d}^{-1}$$
$$\lambda_b = \frac{\ln 2}{68.0\text{ d}} \approx 0.010193\text{ d}^{-1}$$
Effective elimination constant:
$$\lambda_{\text{eff}} = \lambda_p + \lambda_b = 0.086373 + 0.010193 = 0.096566\text{ days}^{-1}$$
Effective half-life:
$$T_{\text{eff}} = \frac{\ln 2}{\lambda_{\text{eff}}} = \frac{0.693147}{0.096566\text{ d}^{-1}} \approx 7.178\text{ days}$$
Alternatively:
$$T_{\text{eff}} = \frac{T_p \cdot T_b}{T_p + T_b} = \frac{8.025 \times 68.0}{8.025 + 68.0} = \frac{545.70}{76.025} \approx 7.178\text{ days}$$

### Step 2: Remaining Activity After $30.0\text{ Days}$
$$A(30) = A_0 e^{-\lambda_{\text{eff}} t} = 50.0\text{ kBq} \times \exp(-0.096566 \times 30.0) = 50.0 \times e^{-2.8970}$$
$$A(30) = 50.0 \times 0.055189 \approx 2.76\text{ kBq}$$

### Step 3: Committed Equivalent Dose
$$H_{\text{thyroid}} = A_{\text{intake}} \cdot e(50) = (50,000\text{ Bq})(4.3 \times 10^{-7}\text{ Sv/Bq}) = 0.0215\text{ Sv} = 21.5\text{ mSv}$$
The technician receives a committed thyroid dose of **$21.5\text{ mSv}$**.""",
                    "hints": ["Effective half-life formula: T_eff = (T_p * T_b) / (T_p + T_b).", "Committed dose equals total intake activity multiplied by the dose coefficient."]
                },
                {
                    "id": "prob-10-4",
                    "problemNumber": "10.4",
                    "title": "Linear-Quadratic Model Dose Fractionation Sparing in Radiation Oncology",
                    "difficulty": "Intermediate",
                    "statement": r"""In clinical radiotherapy, a tumor has an $\alpha/\beta$ ratio of $10.0\text{ Gy}$ ($\alpha = 0.30\text{ Gy}^{-1}, \beta = 0.030\text{ Gy}^{-2}$).
Surrounding late-responding healthy normal tissue has $\alpha/\beta = 2.50\text{ Gy}$ ($\alpha_{\text{norm}} = 0.10\text{ Gy}^{-1}, \beta_{\text{norm}} = 0.040\text{ Gy}^{-2}$).
Compare two treatment regimes delivering a total physical dose $D_{\text{total}} = 60.0\text{ Gy}$:
- Regime A: Single massive fraction of $60.0\text{ Gy}$.
- Regime B: 30 daily fractions of $d = 2.00\text{ Gy}$ ($30 \times 2.0 = 60.0\text{ Gy}$).
1. Calculate the Biologically Effective Dose ($\text{BED} = D [1 + d/(\alpha/\beta)]$) for the tumor and normal tissue under both regimes.
2. Explain the therapeutic gain achieved by dose fractionation.""",
                    "solution": r"""### Step 1: Biologically Effective Dose (BED) Calculations
Formula: $\text{BED} = D_{\text{total}} \left(1 + \frac{d}{\alpha/\beta}\right)$.

1. **Regime A: Single Fraction ($d = 60.0\text{ Gy}$)**:
- **Tumor** ($\alpha/\beta = 10\text{ Gy}$):
$$\text{BED}_{\text{tumor}} = 60.0 \left(1 + \frac{60.0}{10.0}\right) = 60.0(1 + 6.0) = 420\text{ Gy}_{10}$$
- **Normal Tissue** ($\alpha/\beta = 2.5\text{ Gy}$):
$$\text{BED}_{\text{normal}} = 60.0 \left(1 + \frac{60.0}{2.5}\right) = 60.0(1 + 24.0) = 1,500\text{ Gy}_{2.5}$$
The biological damage to healthy tissue ($1,500\text{ Gy}$) is catastrophic, causing lethal necrosis!

2. **Regime B: 30 Fractions of $2.00\text{ Gy}$ ($d = 2.00\text{ Gy}$)**:
- **Tumor**:
$$\text{BED}_{\text{tumor}} = 60.0 \left(1 + \frac{2.00}{10.0}\right) = 60.0(1 + 0.20) = 72.0\text{ Gy}_{10}$$
- **Normal Tissue**:
$$\text{BED}_{\text{normal}} = 60.0 \left(1 + \frac{2.00}{2.5}\right) = 60.0(1 + 0.80) = 108.0\text{ Gy}_{2.5}$$

### Step 2: Therapeutic Gain Explanation
In Regime B, fractionating the dose into $2\text{ Gy}$ increments exploits the difference in repair capacities:
Because normal tissue has a broad curve shoulder ($\beta = 0.040$), dividing the dose into small increments allows sublethal damage repair between daily fractions ($24\text{ hours}$ apart).
The biological damage to normal tissue drops from $1,500\text{ Gy}$ to $108\text{ Gy}$—a **fourteen-fold sparing of healthy tissue** while sterilizing the tumor cells!""",
                    "hints": ["Biologically Effective Dose: BED = D * [1 + d / (alpha/beta)].", "Fractionation allows normal tissue with low alpha/beta to repair sublethal damage between fractions."]
                },
                {
                    "id": "prob-10-5",
                    "problemNumber": "10.5",
                    "title": "Deterministic Acute Radiation Syndrome LD50 Probit Curve",
                    "difficulty": "Intermediate",
                    "statement": r"""In radiobiological toxicology, the mortality of mammals exposed to acute whole-body gamma radiation follows a sigmoid probit curve described by the cumulative normal distribution:
$$P(\text{Death}) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{Y - 5} e^{-u^2/2} du$$
where $Y = a + b \log_{10}(D)$.
For humans without specialized intensive medical intervention:
- $\text{LD}_{50/60}$ (lethal dose to $50\%$ of population within 60 days) is $D_{50} = 3.50\text{ Gy}$.
- $\text{LD}_{10/60}$ is $D_{10} = 2.20\text{ Gy}$.
1. Compute the probit slope parameter $b$ and intercept $a$.
2. Calculate the estimated $\text{LD}_{90/60}$ dose in Grays.
3. Determine the predicted mortality percentage for an accidental acute whole-body absorbed dose of $D = 4.50\text{ Gy}$.""",
                    "solution": r"""### Step 1: Probit Parameters $a$ and $b$
In standard probit tables:
- $P = 50\% \implies \text{Probit } Y = 5.00$
- $P = 10\% \implies \text{Probit } Y = 3.72$ (from $z = -1.282 \implies 5 - 1.282 = 3.718$)
- $P = 90\% \implies \text{Probit } Y = 6.28$ (from $z = +1.282 \implies 5 + 1.282 = 6.282$)

Set up linear equations:
$$\log_{10}(D_{50}) = \log_{10}(3.50) \approx 0.54407 \implies 5.00 = a + b(0.54407)$$
$$\log_{10}(D_{10}) = \log_{10}(2.20) \approx 0.34242 \implies 3.718 = a + b(0.34242)$$
Subtracting:
$$5.00 - 3.718 = 1.282 = b(0.54407 - 0.34242) = b(0.20165)$$
$$b = \frac{1.282}{0.20165} \approx 6.3575$$
$$a = 5.00 - (6.3575 \times 0.54407) = 5.00 - 3.4589 = 1.5411$$

### Step 2: Calculate $\text{LD}_{90/60}$
At $90\%$ mortality, $Y = 6.282$:
$$6.282 = 1.5411 + 6.3575 \log_{10}(D_{90})$$
$$\log_{10}(D_{90}) = \frac{6.282 - 1.5411}{6.3575} = \frac{4.7409}{6.3575} \approx 0.74571$$
$$D_{90} = 10^{0.74571} \approx 5.568\text{ Gy}$$
The $\text{LD}_{90/60}$ dose is **$5.57\text{ Gy}$**.

### Step 3: Mortality at $D = 4.50\text{ Gy}$
$$\log_{10}(4.50) \approx 0.65321$$
$$Y = 1.5411 + 6.3575(0.65321) = 1.5411 + 4.1528 = 5.6939$$
Standard normal deviate:
$$z = Y - 5.00 = 5.6939 - 5.00 = +0.6939$$
From standard normal CDF tables, $\Phi(0.694) \approx 0.7562$.
Predicted mortality: **$75.6\%$** of exposed individuals will succumb to hematopoietic bone marrow syndrome within 60 days unless treated with colony-stimulating factors (G-CSF) or bone marrow transplants.""",
                    "hints": ["Probit Y = 5 corresponds to 50% response.", "Probit Y = a + b * log10(D)."]
                },
                {
                    "id": "prob-10-6",
                    "problemNumber": "10.6",
                    "title": "Linear No-Threshold Lifetime Cancer Risk Assessment for Occupational Cohort",
                    "difficulty": "Easy",
                    "statement": r"""A nuclear decommissioning team of 250 radiological workers operates in a contaminated reprocessing cell.
Each worker receives an average annual effective dose of $14.0\text{ mSv}$ over a 5-year project duration.
Using the ICRP nominal stochastic cancer risk coefficient of $5.5 \times 10^{-2}\text{ Sv}^{-1}$ ($5.5\%\text{ per Sievert}$):
1. Calculate the cumulative 5-year effective dose received per worker in Sieverts ($\text{Sv}$).
2. Compute the collective effective dose to the entire workforce in person-Sieverts ($\text{person-Sv}$).
3. Estimate the statistical number of excess fatal stochastic radiation-induced cancers predicted by the LNT model over the lifetime of the cohort.""",
                    "solution": r"""### Step 1: Cumulative Dose Per Worker
$$\text{Dose per worker} = 14.0\text{ mSv/year} \times 5\text{ years} = 70.0\text{ mSv} = 0.0700\text{ Sv}$$

### Step 2: Collective Effective Dose ($S$)
$$S = N \cdot E = 250\text{ workers} \times 0.0700\text{ Sv} = 17.50\text{ person-Sv}$$
The total collective dose is **$17.5\text{ person-Sieverts}$**.

### Step 3: Predicted Excess Fatal Cancers
Under the LNT model:
$$\text{Expected Fatal Cancers} = S \times \text{Risk Coefficient}$$
$$\text{Expected Cancers} = 17.50\text{ person-Sv} \times 0.055\text{ Sv}^{-1} \approx 0.9625$$
The LNT model predicts approximately **$0.96$ excess fatal cancers** ($\sim 1$ case) across the entire 250-person cohort over their remaining lifetimes.""",
                    "hints": ["Collective dose is number of workers multiplied by average dose.", "Expected cancer cases = Collective dose in person-Sv * 0.055 Sv^-1."]
                },
                {
                    "id": "prob-10-7",
                    "problemNumber": "10.7",
                    "title": "Diagnostic Fluoroscopy Patient Skin Dose and Air Kerma-Area Product (KAP)",
                    "difficulty": "Intermediate",
                    "statement": r"""During an interventional cardiac fluoroscopy procedure, the X-ray tube operates at an air kerma rate at the patient's entrance skin surface of $\dot{K}_{\text{air}} = 45.0\text{ mGy/min}$.
The fluoroscopic beam irradiation field size at the skin is $12.0\text{ cm} \times 12.0\text{ cm}$.
The backscatter factor from underlying patient tissue is $B_{\text{tissue}} = 1.35$.
The mass-energy absorption coefficient ratio of tissue to air is $(\mu_{\text{en}}/\rho)_{\text{air}}^{\text{tissue}} = 1.06$.
Total beam-on fluoroscopy time is $t = 35.0\text{ minutes}$.
1. Calculate the total free-in-air entrance kerma in Grays ($\text{Gy}$).
2. Compute the cumulative peak Entrance Skin Dose (ESD) to the patient in Grays, and determine whether the threshold for deterministic skin erythema ($2.0\text{ Gy}$) is exceeded.
3. Calculate the Kerma-Area Product (KAP or DAP) in $\text{Gy}\cdot\text{cm}^2$.""",
                    "solution": r"""### Step 1: Free-in-Air Entrance Kerma
$$K_{\text{air}} = \dot{K}_{\text{air}} \times t = 45.0\text{ mGy/min} \times 35.0\text{ min} = 1,575\text{ mGy} = 1.575\text{ Gy}$$

### Step 2: Entrance Skin Dose (ESD)
The Entrance Skin Dose accounts for tissue absorption and backscatter radiation:
$$\text{ESD} = K_{\text{air}} \cdot B_{\text{tissue}} \cdot \left(\frac{\mu_{\text{en}}}{\rho}\right)_{\text{air}}^{\text{tissue}}$$
$$\text{ESD} = 1.575\text{ Gy} \times 1.35 \times 1.06 = 1.575 \times 1.431 \approx 2.2539\text{ Gy}$$
The skin dose is **$2.25\text{ Gy}$**.
Because $\text{ESD} = 2.25\text{ Gy} > 2.0\text{ Gy}$, the clinical threshold for deterministic **transient radiation skin erythema** is exceeded. Clinical follow-up at $2 - 4\text{ weeks}$ is mandated to monitor for skin burns.

### Step 3: Kerma-Area Product (KAP)
Beam field area:
$$A = 12.0\text{ cm} \times 12.0\text{ cm} = 144.0\text{ cm}^2$$
$$\text{KAP} = K_{\text{air}} \cdot A = 1.575\text{ Gy} \times 144.0\text{ cm}^2 = 226.8\text{ Gy}\cdot\text{cm}^2$$
The KAP is **$226.8\text{ Gy}\cdot\text{cm}^2$** (or $22.68\text{ Gy}\cdot\text{m}^2$).""",
                    "hints": ["Entrance skin dose multiplies air kerma by backscatter factor and tissue-to-air absorption ratio.", "KAP is air kerma multiplied by radiation field area."]
                }
            ]
        }
    ]
    return units

if __name__ == '__main__':
    u = get_units_7_8_9_10()
    print(f"Generated {len(u)} units.")
    for idx, unit in enumerate(u):
        print(f"Unit {unit['unitNumber']}: {unit['title']} -> {len(unit['sections'])} sections, {len(unit['problems'])} problems")
