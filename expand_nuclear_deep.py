# -*- coding: utf-8 -*-
"""
expand_nuclear_deep.py
Appends comprehensive reference tables, decay series data, cross sections,
and rigorous derivations to Units 1-10 for Nuclear and Radiochemistry (#47).
Strictly Zero Course Numbers or Marks.
"""

def append_deep_reference_data(units):
    deep_additions = {
        1: r"""
### Comprehensive Reference: The Four Primordial & Extinct Radioactive Decay Series
All natural heavy radioactive decay chains follow one of four series characterized by mass number $A$ modulo 4 ($A = 4n + k$, where $k \in \{0, 1, 2, 3\}$):

| Series Name | Classification | Parent Nuclide | Half-Life ($T_{1/2}$) | Stable Endpoint | Dominant Mode |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Thorium Series** ($4n$) | Natural Primordial | $^{232}_{90}\text{Th}$ | $1.405 \times 10^{10}\text{ yr}$ | $^{208}_{82}\text{Pb}$ | $6\alpha, 4\beta^-$ |
| **Neptunium Series** ($4n + 1$) | Extinct Cosmogenic / Artificial | $^{237}_{93}\text{Np}$ | $2.144 \times 10^6\text{ yr}$ | $^{209}_{83}\text{Bi}$ | $7\alpha, 4\beta^-$ |
| **Uranium-Radium Series** ($4n + 2$) | Natural Primordial | $^{238}_{92}\text{U}$ | $4.468 \times 10^9\text{ yr}$ | $^{206}_{82}\text{Pb}$ | $8\alpha, 6\beta^-$ |
| **Actinium Series** ($4n + 3$) | Natural Primordial | $^{235}_{92}\text{U}$ | $7.040 \times 10^8\text{ yr}$ | $^{207}_{82}\text{Pb}$ | $7\alpha, 4\beta^-$ |

The neptunium series ($4n + 1$) is extinct in nature because the half-life of its longest-lived parent ($^{237}\text{Np}$, $2.14\text{ Ma}$) is vastly shorter than the age of the Earth ($4.54\text{ Ga}$). It was first synthesized artificially by Seaborg, McMillan, and Wahl in 1940.""",

        2: r"""
### Comparative Systematics of Semi-Empirical Mass Formula (SEMF) Parameter Sets
Different empirical fits to experimental nuclear masses yield slightly varying coefficient sets (all in MeV):

| Parameter Set | Volume $a_v$ | Surface $a_s$ | Coulomb $a_c$ | Asymmetry $a_a$ | Pairing $a_p$ | RMS Mass Error |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **von Weizsäcker (1935)** | $15.75$ | $17.80$ | $0.711$ | $23.70$ | $11.18$ | $\sim 2.5\text{ MeV}$ |
| **Green (1954)** | $15.75$ | $17.80$ | $0.710$ | $23.69$ | $12.00$ | $\sim 2.1\text{ MeV}$ |
| **Myers & Swiatecki (1966)** | $15.68$ | $18.56$ | $0.717$ | $28.07$ | $11.00$ | $\sim 1.8\text{ MeV}$ |
| **Möller et al. (FRDM, 1995)** | $16.25$ | $19.00$ | $0.730$ | $32.00$ | $11.50$ | $\sim 0.67\text{ MeV}$ |

Modern Finite-Range Droplet Models (FRDM) incorporate microscopic Strutinsky shell corrections and macroscopic nuclear surface diffuseness, predicting nuclear binding energies for thousands of exotic isotopes out to the neutron and proton driplines.""",

        3: r"""
### Mathematical Taxonomy of Radioactive Decay Kinetics & Equilibrium Regimes

```
                      SUCCESSIVE DECAY KINETICS
                     N₁ ──(λ₁)──► N₂ ──(λ₂)──► N₃

     REGIME             CONDITION             ACTIVITY RATIO (Late Times)
  ─────────────   ───────────────────────   ───────────────────────────────
   Secular Eq       λ₁ ≪ λ₂ (T₁/₂ ≫ 10⁴×)      A₂(t) / A₁(t) ──► 1.000
   Transient Eq     λ₁ < λ₂ (T₁/₂ ≈ 10×)       A₂(t) / A₁(t) ──► λ₂ / (λ₂ - λ₁) > 1
   No Equilibrium   λ₁ > λ₂ (T₁/₂ < T₁/₂,₂)    A₂(t) / A₁(t) ──► ∞ (A₁ vanishes)
```

In the secular regime, the abundance of all intermediate daughters in an undisturbed rock is directly proportional to their half-lives:
$$\frac{N_1}{T_{1/2,1}} = \frac{N_2}{T_{1/2,2}} = \frac{N_3}{T_{1/2,3}} = \dots = \frac{N_n}{T_{1/2,n}}$$
This simple relation allows geochemists to determine the age of continents, meteorites, and lunar samples.""",

        4: r"""
### Giant Resonance Parameters of Slow-Neutron Absorber Isotopes

| Nuclide | Natural Abundance | Target Spin $I^\pi$ | Thermal Cross-Section $\sigma_{\text{th}}$ | Resonance Energy $E_0$ | Peak Cross-Section $\sigma_0$ | Primary Application |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$^{10}\text{B}$** | $19.9\%$ | $3^+$ | $3,840\text{ b}$ | $1/v$ up to $100\text{ keV}$ | — | Reactor control rods, neutron shielding |
| **$^{113}\text{Cd}$** | $12.22\%$ | $1/2^+$ | $20,600\text{ b}$ | $0.178\text{ eV}$ | $60,000\text{ b}$ | Thermal neutron cut-off filter ($E_{\text{Cd}} = 0.55\text{ eV}$) |
| **$^{115}\text{In}$** | $95.71\%$ | $9/2^+$ | $202\text{ b}$ | $1.457\text{ eV}$ | $35,100\text{ b}$ | Neutron flux activation foil |
| **$^{135}\text{Xe}$** | $0.0\%$ (Fission) | $3/2^+$ | **$2,650,000\text{ b}$** | $0.084\text{ eV}$ | **$3.5 \times 10^6\text{ b}$** | Strongest known reactor poison |
| **$^{149}\text{Sm}$** | $13.82\%$ | $7/2^-$ | $41,000\text{ b}$ | $0.097\text{ eV}$ | $120,000\text{ b}$ | Permanent non-decaying reactor poison |
| **$^{157}\text{Gd}$** | $15.65\%$ | $3/2^-$ | **$254,000\text{ b}$** | $0.031\text{ eV}$ | **$2.6 \times 10^5\text{ b}$** | Burnable poison in nuclear fuel assemblies |""",

        5: r"""
### Comprehensive Comparison of Global Commercial Nuclear Reactor Architectures

| Reactor System | Full Name | Moderator | Coolant | Core Pressure | Outlet Temp | Fuel Type & Enrichment | Worldwide Fleet Share |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **PWR** | Pressurized Water Reactor | $\text{H}_2\text{O}$ | $\text{H}_2\text{O}$ (liquid) | $15.5\text{ MPa}$ | $325^\circ\text{C}$ | $\text{UO}_2$ ($3.2 - 4.95\%$) | **$68\%$** |
| **BWR** | Boiling Water Reactor | $\text{H}_2\text{O}$ | Steam/Water | $7.2\text{ MPa}$ | $285^\circ\text{C}$ | $\text{UO}_2$ ($3.0 - 4.5\%$) | **$15\%$** |
| **PHWR / CANDU** | Pressurized Heavy Water | $\text{D}_2\text{O}$ | $\text{D}_2\text{O}$ | $10.0\text{ MPa}$ | $310^\circ\text{C}$ | **Natural Uranium** ($0.72\%$) | **$11\%$** |
| **AGR** | Advanced Gas-Cooled | Graphite | $\text{CO}_2$ gas | $4.2\text{ MPa}$ | $650^\circ\text{C}$ | $\text{UO}_2$ ($2.5 - 3.5\%$) in Stainless | **$2\%$** |
| **SFR / LMFBR** | Sodium Fast Reactor | **None** | Liquid Sodium | $0.1\text{ MPa}$ | $550^\circ\text{C}$ | $\text{MOX}$ ($15 - 20\% \, \text{Pu}$) | **$<1\%$** |
| **VHTR** | Very High Temperature Gas | Graphite | Helium gas | $7.0\text{ MPa}$ | $950 - 1000^\circ\text{C}$ | TRISO fuel particles ($10 - 15\%$) | Emerging Gen-IV |""",

        6: r"""
### Linear and Mass Attenuation Data for Photons Across Materials (0.01 to 10 MeV)

| Material | Density $\rho$ ($\text{g/cm}^3$) | $\mu/\rho$ at $0.05\text{ MeV}$ | $\mu/\rho$ at $0.10\text{ MeV}$ | $\mu/\rho$ at $0.50\text{ MeV}$ | $\mu/\rho$ at $1.00\text{ MeV}$ | $\mu/\rho$ at $5.00\text{ MeV}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Air (STP)** | $0.001205$ | $0.208\text{ cm}^2/\text{g}$ | $0.155\text{ cm}^2/\text{g}$ | $0.087\text{ cm}^2/\text{g}$ | $0.0636\text{ cm}^2/\text{g}$ | $0.0275\text{ cm}^2/\text{g}$ |
| **Water** | $1.000$ | $0.227$ | $0.171$ | $0.0969$ | $0.0707$ | $0.0303$ |
| **Aluminum ($Z=13$)** | $2.699$ | $0.368$ | $0.170$ | $0.0845$ | $0.0615$ | $0.0284$ |
| **Iron ($Z=26$)** | $7.874$ | $1.96$ | $0.372$ | $0.0841$ | $0.0599$ | $0.0314$ |
| **Lead ($Z=82$)** | $11.35$ | **$8.04$** | **$5.55$** | **$0.161$** | **$0.0710$** | **$0.0426$** |

At $50\text{ keV}$, lead is **35 times more attenuating per gram** than water due to the $Z^4 / E^{3.5}$ photoelectric effect. At $1\text{ MeV}$, Compton scattering dominates, and mass attenuation coefficients across all materials become virtually identical ($\sim 0.06 - 0.07\text{ cm}^2/\text{g}$) because electron density per gram ($Z/A \approx 0.4 - 0.5$) is nearly constant!""",

        7: r"""
### Comprehensive Performance Specifications of Radiation Detectors

| Detector Category | Active Material | Average Energy per Ion/Carrier | FWHM Resolution @ $662\text{ keV}$ | Operational Temperature | Key Advantages & Applications |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Gas Ion Chamber** | Air / Ar ($M=1$) | $34.0\text{ eV}$ | Not applicable | Room temp ($300\text{ K}$) | Absolute reference dosimetry |
| **Proportional Tube** | P-10 ($M=10^4$) | $26.0\text{ eV}$ | $\approx 12 - 15\%$ | Room temp | X-ray spectroscopy, neutron detection ($^3\text{He}$) |
| **GM Counter** | $\text{Ar} + \text{Br}_2$ ($M=10^9$) | Full discharge | No energy resolution | Room temp | High-sensitivity survey meters |
| **Inorganic Scintillator** | $\text{NaI(Tl)} + \text{PMT}$ | $\sim 100\text{ eV/pe}$ | **$6.5 - 7.5\%$** | Room temp | Field gamma spectrometry, borehole logging |
| **Ultra-Dense Scintillator** | $\text{BGO} (\text{Bi}_4\text{Ge}_3\text{O}_{12})$ | $\sim 300\text{ eV/pe}$ | $10 - 12\%$ | Room temp | Positron Emission Tomography (PET) |
| **Fast Lanthanide Scint** | $\text{LaBr}_3\text{:Ce}$ | $\sim 60\text{ eV/pe}$ | **$2.6 - 2.9\%$** | Room temp | Fast timing coincidence, homeland security |
| **HPGe Semiconductor** | High-Purity Ge | **$2.96\text{ eV}$** | **$0.15 - 0.20\%$** ($1.2\text{ keV}$) | **Cryogenic ($77\text{ K}$)** | Gold standard gamma spectroscopy |
| **CZT Semiconductor** | $\text{Cd}_{0.9}\text{Zn}_{0.1}\text{Te}$ | **$4.64\text{ eV}$** | **$1.5 - 2.5\%$** | Room temp | Handheld isotope identification devices |""",

        8: r"""
### Comparative Analytical Capabilities: Nuclear vs Atomic Spectrometric Techniques

| Technique | Analytical Principle | Detection Limit Range | Destructive? | Simultaneous Elements | Matrix Interferences |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **INAA** | Thermal neutron $(n,\gamma)$ + HPGe | $10^{-9} - 10^{-12}\text{ g}$ | **No (Non-destructive)** | $40 - 60$ | Low (except high Na/Br/Cl) |
| **RNAA** | Post-irradiation chemical separation | **$10^{-12} - 10^{-14}\text{ g}$** | Yes (Destructive) | $1 - 10$ | None (Carrier chemistry) |
| **Direct IDA** | Traced isotopic equilibration | $10^{-6} - 10^{-9}\text{ g}$ | Yes | Single element | None (Recovery independent) |
| **AMS** | Direct atom counting via accelerator | **$10^{-15} - 10^{-18}\text{ g}$** | Yes ($<1\text{ mg}$ sample) | Single isotope ($^{14}\text{C}, ^{10}\text{Be}$) | Zero isobaric background |
| **ICP-MS** | Inductively coupled plasma ionization | $10^{-9} - 10^{-12}\text{ g}$ | Yes (Liquid digestion) | $70+$ | Spectral polyatomic isobars |
| **XRF** | Inner-shell X-ray fluorescence | $10^{-3} - 10^{-6}\text{ g}$ | No | $30 - 40$ | Matrix absorption/enhancement |""",

        9: r"""
### Global Production Pathways of Major Medical and Industrial Radioisotopes

| Isotope | Half-Life | Primary Production Reaction | Production Facility | Carrier Status | Major Clinical / Industrial Use |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$^{99}\text{Mo} \to ^{99m}\text{Tc}$** | $66.0\text{ h} / 6.0\text{ h}$ | $^{235}\text{U}(n, f)^{99}\text{Mo}$ | Research Reactor | Carrier-free (NCA) | $>80\%$ of all diagnostic nuclear medicine |
| **$^{131}\text{I}$** | $8.025\text{ days}$ | $^{130}\text{Te}(n, \gamma)^{131}\text{Te} \xrightarrow{\beta^-} ^{131}\text{I}$ | Research Reactor | Carrier-free (NCA) | Thyroid cancer ablation & hyperthyroidism |
| **$^{18}\text{F}$** | $109.8\text{ min}$ | $^{18}\text{O}(p, n)^{18}\text{F}$ | Biomedical Cyclotron | Carrier-free (NCA) | PET oncology imaging ($^{18}\text{F-FDG}$) |
| **$^{68}\text{Ge} \to ^{68}\text{Ga}$** | $271\text{ d} / 67.7\text{ min}$ | $^{69}\text{Ga}(p, 2n)^{68}\text{Ge}$ | High-energy Cyclotron | Generator system | PET neuroendocrine and prostate imaging |
| **$^{60}\text{Co}$** | $5.271\text{ years}$ | $^{59}\text{Co}(n, \gamma)^{60}\text{Co}$ | Heavy-water Reactor | Carrier-added | Industrial sterilization, gamma knife |
| **$^{192}\text{Ir}$** | $73.8\text{ days}$ | $^{191}\text{Ir}(n, \gamma)^{192}\text{Ir}$ | High-flux Reactor | High specific activity | Pipeline non-destructive testing, brachytherapy |
| **$^{225}\text{Ac}$** | $9.92\text{ days}$ | $^{226}\text{Ra}(p, 2n)^{225}\text{Ac}$ or $^{229}\text{Th}$ cow | Cyclotron / Generator | Carrier-free | Targeted Alpha Therapy (PSMA-617) |""",

        10: r"""
### ICRP International System of Radiological Protection: Dose Limits & Detriment Metrics

```
                     ICRP DOSE LIMIT ARCHITECTURE
                              (ICRP 103)
                                  │
          ┌───────────────────────┴───────────────────────┐
          ▼                                               ▼
 OCCUPATIONAL WORKERS                              GENERAL PUBLIC
  • Effective Dose: 20 mSv/yr                      • Effective Dose: 1.0 mSv/yr
    (Averaged over 5 yr; max 50 mSv in any 1 yr)    (Higher in special circumstances)
  • Equivalent Dose Lens: 20 mSv/yr                • Equivalent Dose Lens: 15 mSv/yr
  • Equivalent Dose Skin: 500 mSv/yr               • Equivalent Dose Skin: 50 mSv/yr
  • Equivalent Dose Hands/Feet: 500 mSv/yr         • Pregnant Public: Unrestricted
```

### Major Radiological Accidents and Lessons Learned
1. **Chernobyl (1986, INES Level 7)**:
Prompt criticality power excursion driven by positive void coefficient ($+4.5\,\beta$) during low-power turbine test with control rods withdrawn, followed by xenon pit poisoning. Release of $1.8 \times 10^{18}\text{ Bq}$ of $^{131}\text{I}$ and $8.5 \times 10^{16}\text{ Bq}$ of $^{137}\text{Cs}$. Resulted in 28 acute radiation deaths and over 6,000 thyroid cancers among children who drank milk contaminated with $^{131}\text{I}$.
2. **Fukushima Daiichi (2011, INES Level 7)**:
Loss of all off-site power and on-site emergency diesel generators following a $14\text{-meter}$ tsunami. Loss of decay heat cooling caused core meltdowns in Units 1, 2, and 3. Zircaloy-water reaction ($Zr + 2\text{H}_2\text{O} \to \text{ZrO}_2 + 2\text{H}_2$) produced explosive hydrogen gas, blowing off reactor building roofs. Prompt evacuation and food bans prevented any acute radiation sickness or fatal deterministic exposures.
3. **Goiânia (1987, INES Level 5)**:
Scrap metal scavengers dismantled an abandoned teletherapy machine, breaching a sealed cesium-137 chloride source ($50.9\text{ TBq} \approx 1375\text{ Ci}$). Attracted by its glowing blue luminescence in the dark, individuals spread the soluble powder across family members and neighborhoods. 4 fatalities from acute bone marrow syndrome; over 112,000 individuals screened."""
    }

    for unit in units:
        un = unit["unitNumber"]
        if un in deep_additions:
            # append deep content to the last section of the unit
            unit["sections"][-1]["content"] += "\n\n" + deep_additions[un]
    return units
