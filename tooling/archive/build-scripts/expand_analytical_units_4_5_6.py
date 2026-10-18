# -*- coding: utf-8 -*-
"""
expand_analytical_units_4_5_6.py
Enrichment module expanding Units 4, 5, and 6 of Analytical Chemistry (#46) to honors depth.
Strict zero course numbers or marks.
Adds deep coordination thermodynamics, atomic spectral physics, ion-exchange resin kinetics,
and an 8th comprehensive multi-part solved problem to each unit.
"""

def enrich_units_4_5_6(u4, u5, u6):
    print("Enriching Units 4, 5, and 6 with advanced analytical and mathematical rigor...")

    # =========================================================================
    # UNIT 4 ENRICHMENT
    # =========================================================================
    # Section 4.1: Entropy of Multidentate Chelation & Ring Size Mechanics
    u4["sections"][0]["content"] += r"""

### Statistical and Conformational Factors in Chelate Ring Stabilities
The thermodynamic stability of chelate rings is strictly maximized for 5-membered and 6-membered chelate rings due to strain-free coordinate geometries:
1. **5-Membered Rings**: Optimal for large metal cations with coordination numbers 6 or 8 (e.g., $\text{Ca}^{2+}, \text{Pb}^{2+}, \text{Cd}^{2+}$). The $\text{M--N--C--C--N}$ bite angle of $\approx 85^\circ\text{ to }90^\circ$ perfectly accommodates octahedral and square antiprismatic coordination without angle strain.
2. **6-Membered Rings**: Favored when conjugated $\pi$-systems exist across the ring (e.g., acetylacetonate $\text{acac}^-$ or $\beta$-diketonates), where resonance delocalization stabilizes the quasi-aromatic chelate ring:
   $$\text{M}^{n+} + n\,\text{acac}^- \rightleftharpoons [\text{M(acac)}_n]$$
3. **Macrocyclic Effect**: Cyclam ($1,4,8,11$-tetraazacyclotetradecane) and crown ethers display formation constants up to $10^4$ times higher than their open-chain counterparts (e.g., tetren) because the macrocyclic ring is pre-organized in space, dramatically reducing the conformational entropy penalty ($\Delta S^\circ_{\text{conf}}$) required upon ligand wrapping."""

    # Problem 4.8: Complexometric Analysis of Seawater Hardness with Masking
    prob_4_8 = {
        "id": "prob-4-8",
        "title": "Problem 4.8: Differential Complexometric Titration of Calcium and Magnesium in High-Salinity Seawater",
        "statement": r"""A $25.00\text{ mL}$ aliquot of synthetic ocean water is diluted to $100.0\text{ mL}$ and analyzed for alkaline earth content using standard $0.0500\text{ M}$ EDTA.
1. **Titration 1 (Total Hardness)**: A $25.00\text{ mL}$ aliquot of the diluted seawater is buffered to $\text{pH } 10.0$ with an ammonia-ammonium chloride buffer. Eriochrome Black T indicator is added, requiring $34.20\text{ mL}$ of $0.0500\text{ M}$ EDTA to reach the pure sky-blue endpoint.
2. **Titration 2 (Calcium Alone)**: A second $25.00\text{ mL}$ aliquot of the diluted seawater is adjusted to $\text{pH } 12.5$ using $8.0\text{ M NaOH}$ (precipitating magnesium quantitatively as $\text{Mg(OH)}_2$). Hydroxynaphthol blue indicator is added, requiring $5.20\text{ mL}$ of $0.0500\text{ M}$ EDTA to reach the pure blue endpoint.

Calculate:
1. The molar concentration of calcium ($[\text{Ca}^{2+}]$) in the original undiluted seawater.
2. The molar concentration of magnesium ($[\text{Mg}^{2+}]$) in the original undiluted seawater.
3. The total hardness expressed in parts-per-million ($\text{ppm}$) of $\text{CaCO}_3$ equivalent ($M(\text{CaCO}_3) = 100.09\text{ g}\cdot\text{mol}^{-1}$).""",
        "solution": r"""### Part 1: Calcium Concentration
In Titration 2 at $\text{pH } 12.5$, only calcium reacts with EDTA because magnesium is precipitated as insoluble $\text{Mg(OH)}_2$:
$$n_{\text{Ca}} = C_{\text{EDTA}} \times V_2 = 0.0500\text{ M} \times 0.00520\text{ L} = 2.600 \times 10^{-4}\text{ mol}$$
In the $25.00\text{ mL}$ aliquot of diluted seawater:
$$[\text{Ca}^{2+}]_{\text{diluted}} = \frac{2.600 \times 10^{-4}\text{ mol}}{0.02500\text{ L}} = 0.01040\text{ M}$$
Because $25.00\text{ mL}$ of original seawater was diluted to $100.0\text{ mL}$ (a 4-fold dilution factor):
$$[\text{Ca}^{2+}]_{\text{seawater}} = 0.01040\text{ M} \times \left(\frac{100.0}{25.00}\right) = 0.04160\text{ M} = 41.60\text{ mM}$$

### Part 2: Magnesium Concentration
In Titration 1 at $\text{pH } 10.0$, both calcium and magnesium react stoichiometrically with EDTA:
$$n_{\text{total}} = n_{\text{Ca}} + n_{\text{Mg}} = C_{\text{EDTA}} \times V_1 = 0.0500\text{ M} \times 0.03420\text{ L} = 1.710 \times 10^{-3}\text{ mol}$$
The moles of magnesium in the aliquot are:
$$n_{\text{Mg}} = n_{\text{total}} - n_{\text{Ca}} = 1.710 \times 10^{-3} - 2.600 \times 10^{-4} = 1.450 \times 10^{-3}\text{ mol}$$
Concentration in the diluted aliquot:
$$[\text{Mg}^{2+}]_{\text{diluted}} = \frac{1.450 \times 10^{-3}\text{ mol}}{0.02500\text{ L}} = 0.05800\text{ M}$$
Concentration in the original seawater:
$$[\text{Mg}^{2+}]_{\text{seawater}} = 0.05800\text{ M} \times 4.00 = 0.2320\text{ M} = 232.0\text{ mM}$$

### Part 3: Total Hardness as CaCO3 Equivalent
Total alkaline earth concentration in original seawater:
$$C_{\text{hard}} = [\text{Ca}^{2+}] + [\text{Mg}^{2+}] = 0.04160\text{ M} + 0.2320\text{ M} = 0.2736\text{ M}$$
Mass of $\text{CaCO}_3$ per liter:
$$\text{Mass} = 0.2736\text{ mol}\cdot\text{L}^{-1} \times 100.09\text{ g}\cdot\text{mol}^{-1} = 27.385\text{ g}\cdot\text{L}^{-1}$$
Converting to $\text{ppm}$ ($\text{mg}\cdot\text{L}^{-1}$):
$$\text{Total Hardness} = 27,385\text{ mg}\cdot\text{L}^{-1} = 27,385\text{ ppm CaCO}_3$$"""
    }
    u4["problems"].append(prob_4_8)

    # =========================================================================
    # UNIT 5 ENRICHMENT
    # =========================================================================
    # Section 5.1: Voigt Spectral Line Profile Convolution
    u5["sections"][0]["content"] += r"""

### The Voigt Spectral Convolution Profile
Because natural, Doppler, and Lorentz broadening mechanisms operate simultaneously in flame and furnace atomizers, the overall atomic absorption profile is described by the mathematical convolution of a Gaussian profile (Doppler) and a Lorentzian profile (Lorentz/natural), yielding the **Voigt absorption profile** $k(\nu)$:

$$k(\nu) = k_0 \frac{a}{\pi} \int_{-\infty}^{+\infty} \frac{\exp(-y^2)}{a^2 + (v - y)^2} \, dy \tag{5.0a}$$

where:
- $v = \frac{2(\nu - \nu_0)}{\Delta \nu_D} \sqrt{\ln 2}$ is the normalized frequency displacement.
- $a = \frac{\Delta \nu_L}{\Delta \nu_D} \sqrt{\ln 2}$ is the Voigt damping parameter (ratio of collisional to Doppler width).
- $y$ is an integration variable representing atomic velocity components.
In typical analytical flames ($T \sim 2500\text{ K}$, $P = 1\text{ atm}$), the Voigt parameter is $a \approx 0.5\text{ to }1.5$, meaning that Lorentzian pressure broadening accounts for more than half of the total spectral linewidth, suppressing peak absorption cross-sections by $40\text{--}60\%$ compared to a pure Doppler profile."""

    # Problem 5.8: Zeeman Effect Splitting & Polarized Optics in Graphite Furnace AAS
    prob_5_8 = {
        "id": "prob-5-8",
        "title": "Problem 5.8: Longitudinal Zeeman Background Correction & Magnetic Polarized Optics in GFAAS",
        "statement": r"""A transverse-heated graphite furnace atomic absorption spectrometer employs a modulated longitudinal magnetic field ($B = 0.80\text{ Tesla}$) pulsed at $50\text{ Hz}$ across the graphite tube to eliminate severe structured background absorption from a urine matrix.
The analyte is cadmium, absorbing at the resonance line $\lambda_0 = 228.802\text{ nm}$ ($^1S_0 \to ^1P_1$ transition, normal Zeeman triplet).
1. Calculate the Zeeman frequency shift $\Delta \nu_Z$ and wavelength displacement $\Delta \lambda_Z$ of the $\sigma^+$ and $\sigma^-$ components in a magnetic field of $0.80\text{ T}$ ($\mu_B = 9.274 \times 10^{-24}\text{ J}\cdot\text{T}^{-1}, h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}, c = 2.998 \times 10^8\text{ m}\cdot\text{s}^{-1}$).
2. In longitudinal Zeeman geometry, the light beam propagates parallel to the magnetic field vector. State which Zeeman components ($\pi, \sigma^+, \sigma^-$) interact with the beam when the magnet is energized ($B > 0$).
3. During atomization of a $10.0\,\mu\text{L}$ urine sample, the detector records:
   - Magnet OFF ($B = 0$): $A_{\text{total}} = A_{\text{analyte}} + A_{\text{background}} = 0.645$
   - Magnet ON ($B = 0.80\text{ T}$): $A_{\text{background}} = 0.415$
   Calculate the net corrected analyte absorbance and the percent background contribution.""",
        "solution": r"""### Part 1: Zeeman Frequency Shift and Wavelength Displacement
For a normal Zeeman singlet-to-singlet transition ($^1S_0 \to ^1P_1$, Landé $g$-factor $g = 1$):
$$\Delta E = g \mu_B B = 1 \times (9.274 \times 10^{-24}\text{ J}\cdot\text{T}^{-1}) \times 0.80\text{ T} = 7.419 \times 10^{-24}\text{ J}$$
The frequency shift is:
$$\Delta \nu_Z = \frac{\Delta E}{h} = \frac{7.419 \times 10^{-24}\text{ J}}{6.626 \times 10^{-34}\text{ J}\cdot\text{s}} = 1.1197 \times 10^{10}\text{ Hz} = 11.20\text{ GHz}$$
The wavelength shift is:
$$\Delta \lambda_Z = \frac{\lambda_0^2}{c} \Delta \nu_Z = \frac{(2.288 \times 10^{-7}\text{ m})^2}{2.998 \times 10^8\text{ m}\cdot\text{s}^{-1}} \times (1.1197 \times 10^{10}\text{ s}^{-1}) = \frac{5.235 \times 10^{-14}}{2.998 \times 10^8} \times 1.1197 \times 10^{10} = 1.955 \times 10^{-12}\text{ m} = 0.001955\text{ nm} \approx 1.96\text{ pm}$$
This shifts the $\sigma$ components cleanly outside the narrow emission bandwidth of the hollow cathode lamp ($\Delta \lambda_{\text{HCL}} \approx 0.001\text{ nm}$).

### Part 2: Longitudinal Zeeman Optical Mechanics
When viewing longitudinally (parallel to the magnetic field vector $\mathbf{B}$):
- The central $\pi$ component ($\Delta M_J = 0$) is dipole-forbidden along the field direction and has **zero intensity** ($I_\pi = 0$).
- Only the circularly polarized $\sigma^+$ and $\sigma^-$ components exist, and because their absorption profiles are shifted away by $\Delta \lambda_Z$, atomic cadmium cannot absorb light at the lamp emission wavelength $\lambda_0$ when the magnet is energized!
- Broadband molecular background (smoke, salt matrix) consists of broad bands ($> 10\text{ nm}$ wide) that are unaffected by a picometer magnetic shift.
Thus:
- Magnet OFF: Measures $A_{\text{total}} = A_{\text{Cd}} + A_{\text{background}}$
- Magnet ON: Measures $A_{\text{background}}$ alone!

### Part 3: Net Analyte Absorbance
$$A_{\text{net}} = A_{\text{total}} - A_{\text{background}} = 0.645 - 0.415 = 0.230$$
The background contribution is:
$$\% \text{ Background} = \left(\frac{A_{\text{background}}}{A_{\text{total}}}\right) \times 100\% = \left(\frac{0.415}{0.645}\right) \times 100\% = 64.3\%$$
Zeeman background correction extracts a pristine analyte absorbance of $0.230$ out of an overwhelming background that accounts for nearly two-thirds of the total light attenuation."""
    }
    u5["problems"].append(prob_5_8)

    # =========================================================================
    # UNIT 6 ENRICHMENT
    # =========================================================================
    # Section 6.1: Donnan Potential and Electrolyte Exclusion
    u6["sections"][0]["content"] += r"""

### The Donnan Membrane Equilibrium in Ion-Exchange Resins
When an ion-exchange resin bead is immersed in an electrolyte solution, mobile co-ions (ions possessing the same sign of electrical charge as the fixed resin matrix) are thermodynamically excluded from entering the internal resin gel phase:

$$\left( \frac{a_{\text{cat},r}}{a_{\text{cat},s}} \right)^{1/z_{\text{cat}}} = \left( \frac{a_{\text{an},s}}{a_{\text{an},r}} \right)^{1/z_{\text{an}}} = \exp\left( -\frac{F \Phi_{\text{Donnan}}}{RT} \right) \tag{6.0a}$$

where subscript $r$ denotes the resin phase, $s$ the solution phase, and $\Phi_{\text{Donnan}}$ is the **Donnan electrical potential** established across the bead boundary.
Because the internal concentration of fixed ionic groups is immense ($3\text{ to }5\text{ equivalents}\cdot\text{L}^{-1}$), the Donnan potential strongly repels incoming co-ions. Consequently:
- In dilute external electrolytes ($< 0.1\text{ M}$), co-ion invasion is virtually zero ($\approx 99.9\%$ excluded), so the resin functions as an ideal semipermeable ion exchanger.
- In concentrated electrolytes ($> 3\text{--}6\text{ M HCl}$), the Donnan exclusion breaks down, allowing substantial electrolyte invasion. This breakdown enables neutral ion-pair sorption and metal chloro-complex formation inside the bead."""

    # Problem 6.8: Separation of Lanthanide Cations via Hydroxyisobutyrate Elution
    prob_6_8 = {
        "id": "prob-6-8",
        "title": "Problem 6.8: High-Resolution Cation-Exchange Separation of Trivalent Lanthanides via α-HIBA Elution",
        "statement": r"""A mixture of europium ($\text{Eu}^{3+}$, ionic radius $0.947\text{ Å}$) and neodymium ($\text{Nd}^{3+}$, ionic radius $0.983\text{ Å}$) is separated on a strong acid cation exchange resin (Dowex 50W-X8, $\text{NH}_4^+$ form) using ammonium $\alpha$-hydroxyisobutyrate ($\alpha\text{-HIBA}$) as an auxiliary complexing eluent.
The selectivity of the resin alone for uncomplexed ions is very close:
$$K_{\text{Eu}^{3+}/\text{NH}_4^+} = 4.25, \quad K_{\text{Nd}^{3+}/\text{NH}_4^+} = 3.90$$
However, $\alpha\text{-HIBA}$ forms successive soluble anionic complexes $[\text{Ln}(\text{HIBA})_4]^-$ whose overall stability constants differ markedly due to the lanthanide contraction:
- For $\text{Eu}^{3+}$: $\log \beta_4 = 10.40 \implies \beta_{4,\text{Eu}} = 2.51 \times 10^{10}$
- For $\text{Nd}^{3+}$: $\log \beta_4 = 8.80 \implies \beta_{4,\text{Nd}} = 6.31 \times 10^8$

1. Derive the conditional distribution ratio $D_{\text{Ln}}$ as a function of free ligand concentration $[\text{HIBA}^-]$.
2. Calculate the separation factor $\alpha_{\text{sep}} = D_{\text{Nd}} / D_{\text{Eu}}$ at $[\text{HIBA}^-] = 0.100\text{ M}$.
3. Deduce which lanthanide elutes first from the column and explain the physical origin of the separation.""",
        "solution": r"""### Part 1: Derivation of Conditional Distribution Ratio
The uncomplexed metal cation fraction in solution is:
$$\alpha_{\text{Ln}^{3+}} = \frac{1}{1 + \sum_{i=1}^4 \beta_i [\text{HIBA}^-]^i} \approx \frac{1}{\beta_4 [\text{HIBA}^-]^4}$$
Only the free trivalent cation $\text{Ln}^{3+}$ is retained by the sulfonic acid groups of the resin ($[\text{Ln}^{3+}]_{\text{resin}}$):
$$D_{\text{Ln}} = \frac{[\text{Ln}]_{\text{resin}}}{C_{\text{Ln},\text{aq}}} \approx \frac{K_{\text{ex}} [\text{Ln}^{3+}]_{\text{aq}}}{\beta_4 [\text{HIBA}^-]^4 [\text{Ln}^{3+}]_{\text{aq}}} = \frac{K_{\text{ex}}}{\beta_4 [\text{HIBA}^-]^4}$$

### Part 2: Calculation of Separation Factor
At $[\text{HIBA}^-] = 0.100\text{ M}$:
$$[\text{HIBA}^-]^4 = (0.100)^4 = 1.00 \times 10^{-4}\text{ M}^4$$
- For $\text{Eu}^{3+}$:
  $$D_{\text{Eu}} = \frac{4.25}{(2.51 \times 10^{10}) \times (1.00 \times 10^{-4})} = \frac{4.25}{2.51 \times 10^6} = 1.693 \times 10^{-6}$$
- For $\text{Nd}^{3+}$:
  $$D_{\text{Nd}} = \frac{3.90}{(6.31 \times 10^8) \times (1.00 \times 10^{-4})} = \frac{3.90}{6.31 \times 10^4} = 6.181 \times 10^{-5}$$

The separation factor is:
$$\alpha_{\text{sep}} = \frac{D_{\text{Nd}}}{D_{\text{Eu}}} = \frac{6.181 \times 10^{-5}}{1.693 \times 10^{-6}} = 36.5$$
The separation factor is an astounding $36.5$, enabling complete baseline chromatographic resolution on a compact column.

### Part 3: Elution Order and Physical Mechanism
- **Elution Order**: Europium ($\text{Eu}^{3+}$) has a vastly smaller distribution ratio ($D_{\text{Eu}} \ll D_{\text{Nd}}$) and spends far less time on the stationary resin. Therefore, **$\text{Eu}^{3+}$ elutes first**, followed much later by $\text{Nd}^{3+}$.
- **Physical Origin**: Due to the lanthanide contraction, ionic radius decreases across the series ($\text{Nd}^{3+} = 0.983\text{ Å} \to \text{Eu}^{3+} = 0.947\text{ Å}$). The smaller $\text{Eu}^{3+}$ cation possesses a higher surface charge density, forming significantly stronger coordination bonds with $\alpha\text{-HIBA}$ ($\beta_{4,\text{Eu}} / \beta_{4,\text{Nd}} \approx 40$). This massive solution complexation thermodynamic gradient completely overcomes the slight resin affinity preference, driving heavy lanthanides out of the column first."""
    }
    u6["problems"].append(prob_6_8)
    print("Enriched Units 4, 5, and 6 successfully.")
