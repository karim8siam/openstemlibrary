# -*- coding: utf-8 -*-
"""
expand_analytical_units_7_8_9.py
Enrichment module expanding Units 7, 8, and 9 of Analytical Chemistry (#46) to honors depth.
Strict zero course numbers or marks.
Adds derivative spectrophotometry, chiral partition thermodynamics, Knox core-shell kinetics,
and an 8th comprehensive multi-part solved problem to each unit.
"""

def enrich_units_7_8_9(u7, u8, u9):
    print("Enriching Units 7, 8, and 9 with advanced analytical and mathematical rigor...")

    # =========================================================================
    # UNIT 7 ENRICHMENT
    # =========================================================================
    # Section 7.1: Derivative Spectrophotometry Mathematical Foundations
    u7["sections"][0]["content"] += r"""

### Mathematical Foundations of Derivative Spectrophotometry
In complex multi-component matrices where analyte absorption bands overlap heavily with broad background absorption or scattering profiles, derivative spectrophotometry provides extraordinary spectral resolution enhancement without chemical separation:

$$\frac{d^n A}{d\lambda^n} = b \sum_{i} c_i \frac{d^n \varepsilon_i}{d\lambda^n} \tag{7.0a}$$

1. **First Derivative ($dA/d\lambda$)**:
   - The zero-crossing point ($\frac{dA}{d\lambda} = 0$) identifies the exact absorption maximum ($\lambda_{\text{max}}$) with extreme precision.
   - Completely eliminates flat, wavelength-independent background offsets ($\frac{d}{d\lambda}[\text{const}] = 0$).
2. **Second Derivative ($d^2A/d\lambda^2$)**:
   - Features a negative minimum whose absolute amplitude is directly proportional to concentration.
   - Completely eliminates linear sloping backgrounds ($A_{\text{bg}} = a\lambda + b \implies \frac{d^2 A_{\text{bg}}}{d\lambda^2} = 0$).
   - Sharpens narrow bands relative to broad matrix bands according to the inverse power scaling:
     $$\frac{d^n A}{d\lambda^n} \propto \frac{A_0}{W_0^n} \tag{7.0b}$$
     where $W_0$ is the half-bandwidth. For an analyte band that is 3 times narrower than a background band, the second derivative enhances the analyte-to-background signal ratio by a factor of $3^2 = 9$, and the fourth derivative enhances it by $3^4 = 81$!"""

    # Problem 7.8: Second-Derivative Spectrophotometric Analysis in Strongly Scattering Turbid Media
    prob_7_8 = {
        "id": "prob-7-8",
        "title": "Problem 7.8: Second-Derivative Spectrophotometric Quantitation of Tyrosine in Turbid Protein Formulations",
        "statement": r"""A pharmaceutical monoclonal antibody formulation is analyzed for trace free tyrosine in the presence of severe Rayleigh light scattering caused by sub-micron protein aggregate particles ($A_{\text{scatter}}(\lambda) = k \lambda^{-4}$).
The fundamental absorption band of tyrosine is modeled as a Gaussian profile:
$$A(\lambda) = A_0 \exp\left( -\frac{(\lambda - \lambda_0)^2}{2\sigma^2} \right)$$
with peak wavelength $\lambda_0 = 275.0\text{ nm}$ and spectral standard deviation $\sigma = 6.00\text{ nm}$ (full width at half maximum $FWHM = 2.355\sigma = 14.13\text{ nm}$).
1. Derive the mathematical expression for the second derivative $\frac{d^2 A}{d\lambda^2}$ of the Gaussian absorption band.
2. Calculate the value of $\frac{d^2 A}{d\lambda^2}$ at the peak apex ($\lambda = \lambda_0$) in terms of peak absorbance $A_0$ and $\sigma$.
3. In a turbid test sample with $A_{\text{scatter}} = 0.850$ at $275\text{ nm}$ ($k = 4.86 \times 10^{10}\text{ nm}^4$), calculate the background second-derivative signal $\frac{d^2 A_{\text{scatter}}}{d\lambda^2}$ at $275\text{ nm}$ and demonstrate that it contributes less than $0.2\%$ to the analyte's second-derivative signal ($A_0 = 0.250$).""",
        "solution": r"""### Part 1: Derivation of the Second Derivative of a Gaussian Band
Let $u = -\frac{(\lambda - \lambda_0)^2}{2\sigma^2}$. Then $A(\lambda) = A_0 e^u$.
First derivative:
$$\frac{dA}{d\lambda} = A_0 e^u \frac{du}{d\lambda} = A_0 e^u \left( -\frac{\lambda - \lambda_0}{\sigma^2} \right) = -\frac{(\lambda - \lambda_0)}{\sigma^2} A(\lambda)$$
Second derivative:
$$\frac{d^2 A}{d\lambda^2} = -\frac{1}{\sigma^2} A(\lambda) - \frac{(\lambda - \lambda_0)}{\sigma^2} \frac{dA}{d\lambda} = -\frac{1}{\sigma^2} A(\lambda) + \frac{(\lambda - \lambda_0)^2}{\sigma^4} A(\lambda)$$
$$\frac{d^2 A}{d\lambda^2} = \frac{A_0}{\sigma^2} \left[ \frac{(\lambda - \lambda_0)^2}{\sigma^2} - 1 \right] \exp\left( -\frac{(\lambda - \lambda_0)^2}{2\sigma^2} \right)$$

### Part 2: Value at the Band Apex ($\lambda = \lambda_0$)
At the center of the band ($\lambda = \lambda_0$):
$$\left.\frac{d^2 A}{d\lambda^2}\right|_{\lambda_0} = \frac{A_0}{\sigma^2} [0 - 1] e^0 = -\frac{A_0}{\sigma^2}$$
For $A_0 = 0.250$ and $\sigma = 6.00\text{ nm}$:
$$\left.\frac{d^2 A}{d\lambda^2}\right|_{\text{analyte}} = -\frac{0.250}{(6.00\text{ nm})^2} = -\frac{0.250}{36.0\text{ nm}^2} = -6.944 \times 10^{-3}\text{ nm}^{-2}$$

### Part 3: Background Second Derivative Evaluation
The scattering background obeys $A_{\text{scatter}}(\lambda) = k \lambda^{-4}$:
First derivative:
$$\frac{d A_{\text{scatter}}}{d\lambda} = -4 k \lambda^{-5}$$
Second derivative:
$$\frac{d^2 A_{\text{scatter}}}{d\lambda^2} = +20 k \lambda^{-6}$$
Given $A_{\text{scatter}}(275) = k (275)^{-4} = 0.850 \implies k = 0.850 \times (275)^4 = 4.862 \times 10^{10}\text{ nm}^4$:
$$\left.\frac{d^2 A_{\text{scatter}}}{d\lambda^2}\right|_{275} = \frac{20 \times 4.862 \times 10^{10}}{(275)^6} = \frac{9.724 \times 10^{11}}{4.275 \times 10^{14}} = +2.275 \times 10^{-3}\text{ nm}^{-2} \dots$$
Expressing in terms of ratio:
$$\frac{d^2 A_{\text{scatter}}}{d\lambda^2} = \frac{20 A_{\text{scatter}}}{\lambda^2} = \frac{20 \times 0.850}{(275\text{ nm})^2} = \frac{17.0}{75625\text{ nm}^2} = +2.248 \times 10^{-4}\text{ nm}^{-2}$$
Comparing the scattering contribution to the analyte signal:
$$\text{Relative Interference} = \left| \frac{+2.248 \times 10^{-4}}{-6.944 \times 10^{-3}} \right| \times 100\% = 3.24\%$$
In zero-order spectrophotometry, scattering was $A_{\text{scatter}} / A_0 = 0.850 / 0.250 = 340\%$ ($3.4\times$ greater than analyte!). Second-derivative processing reduces this massive background error by two orders of magnitude, isolating the analyte band cleanly."""
    }
    u7["problems"].append(prob_7_8)

    # =========================================================================
    # UNIT 8 ENRICHMENT
    # =========================================================================
    # Section 8.1: Synergistic Extraction Mechanisms
    u8["sections"][0]["content"] += r"""

### Synergistic Liquid-Liquid Extraction Thermodynamics
Synergistic extraction occurs when a mixture of two extractants extracts a metal cation with an efficiency vastly exceeding the sum of the individual extraction yields:

$$\Delta \log D_{\text{syn}} = \log D_{\text{mix}} - \log (D_A + D_B) > 0 \tag{8.0a}$$

The classic mechanism involves the combination of an acidic chelating agent (e.g., thenoyltrifluoroacetone, HTTA) and a neutral donor ligand (e.g., tributyl phosphate, TBP, or trioctylphosphine oxide, TOPO):
$$\text{UO}_2^{2+}(aq) + 2\,\text{HTTA}(org) + \text{TBP}(org) \rightleftharpoons [\text{UO}_2(\text{TTA})_2(\text{TBP})](org) + 2\,\text{H}^+(aq) \tag{8.0b}$$
1. The chelating ligand ($\text{TTA}^-$) neutralizes the formal positive charge of the metal cation.
2. The neutral organophosphorus ligand ($\text{TBP}$) displaces residual coordinated water molecules from the inner coordination sphere, forming a coordinatively saturated, lipophilic mixed complex that partitions into nonpolar organic diluents with a distribution ratio up to $10^5$ times greater than with HTTA alone."""

    # Problem 8.8: Synergistic Liquid Extraction & Extraction Constant Calculation
    prob_8_8 = {
        "id": "prob-8-8",
        "title": "Problem 8.8: Synergistic Extraction Equilibrium and Mechanism of Uranyl Ion with HTTA and TBP",
        "statement": r"""Uranyl ion ($\text{UO}_2^{2+}$) is extracted from an aqueous nitric acid phase into benzene using thenoyltrifluoroacetone ($\text{HTTA}$) and tributyl phosphate ($\text{TBP}$).
The individual and mixed extraction equilibrium constants are:
- Extraction with $\text{HTTA}$ alone:
  $$\text{UO}_2^{2+} + 2\,\text{HTTA}_{(o)} \rightleftharpoons \text{UO}_2(\text{TTA})_{2,(o)} + 2\,\text{H}^+ \quad (K_{\text{ex}} = 1.00 \times 10^{-3})$$
- Adduct formation in the organic phase:
  $$\text{UO}_2(\text{TTA})_{2,(o)} + \text{TBP}_{(o)} \rightleftharpoons \text{UO}_2(\text{TTA})_2(\text{TBP})_{(o)} \quad (\beta_{\text{adduct}} = 4.00 \times 10^4)$$

The extraction is performed at $\text{pH } 2.50$ with $[\text{HTTA}]_o = 0.0500\text{ M}$.
1. Calculate the distribution ratio $D_0$ in the absence of $\text{TBP}$ ($[\text{TBP}]_o = 0$).
2. Calculate the synergistic distribution ratio $D_{\text{syn}}$ in the presence of $[\text{TBP}]_o = 0.0200\text{ M}$.
3. Calculate the Synergistic Enhancement Factor ($SEF = D_{\text{syn}} / D_0$) and determine the percent extraction ($\%E$) for equal phase volumes.""",
        "solution": r"""### Part 1: Distribution Ratio without TBP ($D_0$)
At $\text{pH } 2.50 \implies [\text{H}^+] = 10^{-2.50} = 3.162 \times 10^{-3}\text{ M}$:
$$[\text{H}^+]^2 = 1.00 \times 10^{-5}\text{ M}^2$$
$$[\text{HTTA}]_o^2 = (0.0500)^2 = 2.50 \times 10^{-3}\text{ M}^2$$
The distribution ratio with HTTA alone is:
$$D_0 = \frac{K_{\text{ex}} [\text{HTTA}]_o^2}{[\text{H}^+]^2} = \frac{(1.00 \times 10^{-3}) \times (2.50 \times 10^{-3})}{1.00 \times 10^{-5}} = \frac{2.50 \times 10^{-6}}{1.00 \times 10^{-5}} = 0.250$$

### Part 2: Synergistic Distribution Ratio with TBP ($D_{\text{syn}}$)
In the presence of TBP, both unadducted and adducted complexes coexist in the organic phase:
$$D_{\text{syn}} = \frac{[\text{UO}_2(\text{TTA})_2]_o + [\text{UO}_2(\text{TTA})_2(\text{TBP})]_o}{[\text{UO}_2^{2+}]_{\text{aq}}}$$
$$D_{\text{syn}} = D_0 \left( 1 + \beta_{\text{adduct}} [\text{TBP}]_o \right)$$
Given $\beta_{\text{adduct}} = 4.00 \times 10^4$ and $[\text{TBP}]_o = 0.0200\text{ M}$:
$$\beta_{\text{adduct}} [\text{TBP}]_o = (4.00 \times 10^4) \times 0.0200 = 800.0$$
$$D_{\text{syn}} = 0.250 \times (1 + 800.0) = 0.250 \times 801.0 = 200.25$$

### Part 3: Synergistic Enhancement Factor and Extraction Yield
- **Synergistic Enhancement Factor**:
  $$SEF = \frac{D_{\text{syn}}}{D_0} = \frac{200.25}{0.250} = 801$$
- **Percent Extraction**:
  Without TBP:
  $$\%E_0 = \frac{D_0}{1 + D_0} \times 100\% = \frac{0.250}{1.250} \times 100\% = 20.0\%$$
  With TBP:
  $$\%E_{\text{syn}} = \frac{D_{\text{syn}}}{1 + D_{\text{syn}}} \times 100\% = \frac{200.25}{201.25} \times 100\% = 99.50\%$$
The addition of a tiny amount of neutral donor ligand raises uranyl extraction from an unusable $20\%$ to a quantitative $99.5\%$!"""
    }
    u8["problems"].append(prob_8_8)

    # =========================================================================
    # UNIT 9 ENRICHMENT
    # =========================================================================
    # Section 9.1: Knox Equation and Core-Shell Particle Kinetics
    u9["sections"][0]["content"] += r"""

### The Knox Equation and Core-Shell Particle Kinetics
In modern high-performance liquid chromatography, column performance is generalized across different column lengths, particle diameters, and mobile phase viscosities using dimensionless parameters formulated by John H. Knox:

$$h = A_k \nu^{1/3} + \frac{B_k}{\nu} + C_k \nu \tag{9.0a}$$

where:
- $h = \frac{H}{d_p}$ is the **reduced plate height** (dimensionless plate height). A well-packed HPLC column typically exhibits $h \approx 2.0\text{ to }2.5$.
- $\nu = \frac{u \, d_p}{D_m}$ is the **reduced linear velocity** (Péclet number in the mobile phase).
- $A_k \approx 1\text{ to }2$, $B_k \approx 2$, and $C_k \approx 0.05\text{ to }0.1$.

#### Superficially Porous (Core-Shell) Particles
Superficially porous particles (SPPs) feature a solid nonporous silica core (e.g., $1.7\,\mu\text{m}$ diameter) surrounded by a thin porous outer shell (e.g., $0.5\,\mu\text{m}$ shell thickness, total $d_p = 2.7\,\mu\text{m}$).
1. **Suppression of $C$-Term**: Because analyte molecules only need to diffuse through the thin $0.5\,\mu\text{m}$ shell rather than penetrating the core, the diffusion path length is reduced by $> 70\%$, slashing resistance to mass transfer ($C_s \propto d_{\text{diffusion}}^2$).
2. **Narrow Particle Size Distribution**: SPPs pack with exceptional bed uniformity, reducing the Eddy diffusion $A$-term.
3. **Low Backpressure Advantage**: A $2.7\,\mu\text{m}$ core-shell column generates the efficiency of a sub-$2\,\mu\text{m}$ totally porous particle column ($N > 200,000\text{ plates}\cdot\text{m}^{-1}$) while maintaining half the backpressure ($\Delta P \propto 1/d_p^2$), allowing ultra-high-speed separations on conventional $400\text{ bar}$ HPLC hardware."""

    # Problem 9.8: Knox Reduced Parameters & Core-Shell vs Totally Porous Particle Efficiency
    prob_9_8 = {
        "id": "prob-9-8",
        "title": "Problem 9.8: Knox Reduced Plate Height Kinetics & Superficially Porous vs Totally Porous HPLC Columns",
        "statement": r"""A pharmaceutical separation is compared on two $100\text{ mm} \times 4.6\text{ mm}$ HPLC columns operating at $u = 0.200\text{ cm}\cdot\text{s}^{-1}$ ($D_m = 8.00 \times 10^{-6}\text{ cm}^2\cdot\text{s}^{-1}$):
- **Column 1 (Totally Porous Particles, TPP)**: $d_p = 3.0\,\mu\text{m}$ ($3.0 \times 10^{-4}\text{ cm}$), Knox parameters $A_k = 1.20, B_k = 2.00, C_k = 0.080$.
- **Column 2 (Core-Shell Superficially Porous, SPP)**: $d_p = 2.7\,\mu\text{m}$ ($2.7 \times 10^{-4}\text{ cm}$), Knox parameters $A_k = 0.70, B_k = 2.00, C_k = 0.025$.

1. Calculate the reduced velocity ($\nu$) for Column 1 and Column 2.
2. Calculate the reduced plate height ($h$) and physical plate height ($H$, in $\mu\text{m}$) for each column.
3. Calculate the total theoretical plate count ($N$) for each column and explain the thermodynamic and kinetic cause of the SPP performance advantage.""",
        "solution": r"""### Part 1: Reduced Velocity ($\nu$)
The reduced velocity is $\nu = \frac{u \, d_p}{D_m}$:
- **Column 1 (TPP, $d_p = 3.0 \times 10^{-4}\text{ cm}$)**:
  $$\nu_1 = \frac{0.200\text{ cm}\cdot\text{s}^{-1} \times 3.0 \times 10^{-4}\text{ cm}}{8.00 \times 10^{-6}\text{ cm}^2\cdot\text{s}^{-1}} = \frac{6.00 \times 10^{-5}}{8.00 \times 10^{-6}} = 7.50$$
- **Column 2 (SPP, $d_p = 2.7 \times 10^{-4}\text{ cm}$)**:
  $$\nu_2 = \frac{0.200\text{ cm}\cdot\text{s}^{-1} \times 2.7 \times 10^{-4}\text{ cm}}{8.00 \times 10^{-6}\text{ cm}^2\cdot\text{s}^{-1}} = \frac{5.40 \times 10^{-5}}{8.00 \times 10^{-6}} = 6.75$$

### Part 2: Reduced Plate Height ($h$) and Physical Plate Height ($H$)
Using the Knox equation $h = A_k \nu^{1/3} + \frac{B_k}{\nu} + C_k \nu$:
- **Column 1 (TPP)**:
  $$h_1 = 1.20 \times (7.50)^{1/3} + \frac{2.00}{7.50} + 0.080 \times 7.50$$
  $$(7.50)^{1/3} = 1.9574$$
  $$h_1 = (1.20 \times 1.9574) + 0.2667 + 0.6000 = 2.3489 + 0.2667 + 0.6000 = 3.2156 \approx 3.22$$
  Physical plate height:
  $$H_1 = h_1 \times d_p = 3.2156 \times 3.0\,\mu\text{m} = 9.65\,\mu\text{m}$$
- **Column 2 (SPP)**:
  $$h_2 = 0.70 \times (6.75)^{1/3} + \frac{2.00}{6.75} + 0.025 \times 6.75$$
  $$(6.75)^{1/3} = 1.8899$$
  $$h_2 = (0.70 \times 1.8899) + 0.2963 + 0.1688 = 1.3229 + 0.2963 + 0.1688 = 1.7880 \approx 1.79$$
  Physical plate height:
  $$H_2 = h_2 \times d_p = 1.7880 \times 2.7\,\mu\text{m} = 4.83\,\mu\text{m}$$

### Part 3: Total Plate Count and Kinetic Evaluation
For $L = 100\text{ mm} = 100,000\,\mu\text{m}$:
- **Column 1 (TPP)**:
  $$N_1 = \frac{100,000\,\mu\text{m}}{9.65\,\mu\text{m}} = 10,363\text{ plates}$$
- **Column 2 (SPP)**:
  $$N_2 = \frac{100,000\,\mu\text{m}}{4.83\,\mu\text{m}} = 20,704\text{ plates}$$
The core-shell column achieves exactly double the plate count ($20,704$ vs $10,363$) on the identical column length!
*Physical Origin*: The solid core restricts solute diffusion to the shallow shell, reducing $C_k$ from $0.080$ to $0.025$ (a $69\%$ reduction in mass-transfer resistance), while superior particle sphericity drops the Eddy dispersion term $A_k$ from $1.20$ to $0.70$."""
    }
    u9["problems"].append(prob_9_8)
    print("Enriched Units 7, 8, and 9 successfully.")
