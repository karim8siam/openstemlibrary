# -*- coding: utf-8 -*-
"""
expand_analytical_units_1_2_3.py
Enrichment module expanding Units 1, 2, and 3 of Analytical Chemistry (#46) to honors depth.
Strict zero course numbers or marks.
Adds deep mathematical and physical derivations, comprehensive analytical tables,
and an 8th comprehensive multi-part solved problem to each unit.
"""

def enrich_units_1_2_3(u1, u2, u3):
    print("Enriching Units 1, 2, and 3 with advanced analytical and mathematical rigor...")

    # =========================================================================
    # UNIT 1 ENRICHMENT
    # =========================================================================
    # Section 1.1: Matrix Formulation of Error Propagation and Covariance
    u1["sections"][0]["content"] += r"""

### Multivariable Covariance Matrix Formulation of Error Propagation
In multivariate analytical measurements where correlated input variables $x_1, x_2, \dots, x_k$ are combined into a derived analytical quantity $y = f(\mathbf{x})$, the classical independent sum of squares underestimates or overestimates the true variance if non-zero covariances exist.
The complete matrix formulation of error propagation is:

$$\sigma_y^2 = \mathbf{J} \, \mathbf{\Sigma} \, \mathbf{J}^T \tag{1.0a}$$

where $\mathbf{J}$ is the gradient (Jacobian row vector) of first partial derivatives:
$$\mathbf{J} = \begin{bmatrix} \frac{\partial f}{\partial x_1} & \frac{\partial f}{\partial x_2} & \cdots & \frac{\partial f}{\partial x_k} \end{bmatrix}$$
and $\mathbf{\Sigma}$ is the symmetric variance-covariance matrix:
$$\mathbf{\Sigma} = \begin{bmatrix}
\sigma_1^2 & \operatorname{cov}(x_1, x_2) & \cdots & \operatorname{cov}(x_1, x_k) \\
\operatorname{cov}(x_2, x_1) & \sigma_2^2 & \cdots & \operatorname{cov}(x_2, x_k) \\
\vdots & \vdots & \ddots & \vdots \\
\operatorname{cov}(x_k, x_1) & \operatorname{cov}(x_k, x_2) & \cdots & \sigma_k^2
\end{bmatrix}$$

Expanding this quadratic form yields:
$$\sigma_y^2 = \sum_{i=1}^k \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_i^2 + 2 \sum_{i=1}^{k-1} \sum_{j=i+1}^k \left(\frac{\partial f}{\partial x_i}\right)\left(\frac{\partial f}{\partial x_j}\right) \operatorname{cov}(x_i, x_j) \tag{1.0b}$$
where the covariance between variables $x_i$ and $x_j$ is given by:
$$\operatorname{cov}(x_i, x_j) = r_{ij} \, \sigma_i \, \sigma_j$$
with $r_{ij} \in [-1, +1]$ denoting the Pearson linear correlation coefficient. In standard addition methods or multi-wavelength calibrations, $r_{ij} \neq 0$ and failure to include the cross-product covariance terms introduces severe systematic bias into the reported confidence intervals."""

    # Problem 1.8: Weighted Least-Squares Calibration & Heteroscedastic Variance Analysis
    prob_1_8 = {
        "id": "prob-1-8",
        "title": "Problem 1.8: Weighted Least-Squares (WLS) Linear Calibration for Heteroscedastic Instrumental Data",
        "statement": r"""In atomic absorption spectrophotometry, calibration variance often increases proportionally with analyte concentration (heteroscedasticity), violating the ordinary least-squares (OLS) assumption of homoscedastic variance.
A calibration series for calcium was measured with $m = 4$ replicate absorbance readings per standard, yielding the following mean absorbance $\bar{y}_i$ and standard deviation $s_i$:
- Standard 1: $x_1 = 1.00\text{ ppm}$, $\bar{y}_1 = 0.0520$, $s_1 = 0.0010$
- Standard 2: $x_2 = 2.00\text{ ppm}$, $\bar{y}_2 = 0.1045$, $s_2 = 0.0022$
- Standard 3: $x_3 = 4.00\text{ ppm}$, $\bar{y}_3 = 0.2080$, $s_3 = 0.0045$
- Standard 4: $x_4 = 8.00\text{ ppm}$, $\bar{y}_4 = 0.4150$, $s_4 = 0.0090$
- Standard 5: $x_5 = 16.00\text{ ppm}$, $\bar{y}_5 = 0.8280$, $s_5 = 0.0180$

1. Compute the statistical weight $w_i = \frac{1}{s_i^2}$ for each calibration level and normalize weights such that $\sum w_i = N = 5$.
2. Formulate the weighted least-squares equations to determine the optimal slope $m_{\text{wls}}$ and intercept $b_{\text{wls}}$ for the calibration model $\hat{y} = m_{\text{wls}} x + b_{\text{wls}}$.
3. An unknown sample yields a mean absorbance of $\bar{y}_{\text{unk}} = 0.3120$ ($s = 0.0068$). Calculate the sample concentration $x_{\text{unk}}$ and its estimated standard error $s_{x_{\text{unk}}}$, comparing the weighting effect against unweighted OLS.""",
        "solution": r"""### Part 1: Calculation of Statistical Weights
The individual variances are $\sigma_i^2 \approx s_i^2$:
- Level 1: $s_1^2 = (0.0010)^2 = 1.00 \times 10^{-6} \implies w_1' = 1.00 \times 10^6$
- Level 2: $s_2^2 = (0.0022)^2 = 4.84 \times 10^{-6} \implies w_2' = 2.066 \times 10^5$
- Level 3: $s_3^2 = (0.0045)^2 = 2.025 \times 10^{-5} \implies w_3' = 4.938 \times 10^4$
- Level 4: $s_4^2 = (0.0090)^2 = 8.10 \times 10^{-5} \implies w_4' = 1.235 \times 10^4$
- Level 5: $s_5^2 = (0.0180)^2 = 3.24 \times 10^{-4} \implies w_5' = 3.086 \times 10^3$

Sum of raw weights:
$$\sum w_i' = 1.00 \times 10^6 + 2.066 \times 10^5 + 4.938 \times 10^4 + 1.235 \times 10^4 + 3.086 \times 10^3 = 1.2714 \times 10^6$$
Normalized weights $w_i = 5 \times \frac{w_i'}{\sum w_i'}$:
- $w_1 = 5 \times (1.00 \times 10^6 / 1.2714 \times 10^6) = 3.9327$
- $w_2 = 5 \times (2.066 \times 10^5 / 1.2714 \times 10^6) = 0.8125$
- $w_3 = 5 \times (4.938 \times 10^4 / 1.2714 \times 10^6) = 0.1942$
- $w_4 = 5 \times (1.235 \times 10^4 / 1.2714 \times 10^6) = 0.0486$
- $w_5 = 5 \times (3.086 \times 10^3 / 1.2714 \times 10^6) = 0.0121$
Check: $\sum w_i = 3.9327 + 0.8125 + 0.1942 + 0.0486 + 0.0121 = 5.0001 \approx 5.000$.

### Part 2: Weighted Least-Squares Normal Equations
Weighted sums:
- $\sum w_i = 5.000$
- $\sum w_i x_i = (3.9327 \times 1) + (0.8125 \times 2) + (0.1942 \times 4) + (0.0486 \times 8) + (0.0121 \times 16) = 3.9327 + 1.6250 + 0.7768 + 0.3888 + 0.1936 = 6.9169$
- $\sum w_i y_i = (3.9327 \times 0.0520) + (0.8125 \times 0.1045) + (0.1942 \times 0.2080) + (0.0486 \times 0.4150) + (0.0121 \times 0.8280) = 0.20450 + 0.08491 + 0.04039 + 0.02017 + 0.01002 = 0.35999$
- $\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i} = \frac{6.9169}{5.000} = 1.3834\text{ ppm}$
- $\bar{y}_w = \frac{\sum w_i y_i}{\sum w_i} = \frac{0.35999}{5.000} = 0.07200$
- $\sum w_i x_i^2 = (3.9327 \times 1) + (0.8125 \times 4) + (0.1942 \times 16) + (0.0486 \times 64) + (0.0121 \times 256) = 3.9327 + 3.2500 + 3.1072 + 3.1104 + 3.0976 = 16.4979$
- $S_{xx,w} = \sum w_i x_i^2 - \frac{(\sum w_i x_i)^2}{\sum w_i} = 16.4979 - \frac{(6.9169)^2}{5.000} = 16.4979 - 9.5687 = 6.9292$
- $\sum w_i x_i y_i = (3.9327 \times 1 \times 0.0520) + (0.8125 \times 2 \times 0.1045) + (0.1942 \times 4 \times 0.2080) + (0.0486 \times 8 \times 0.4150) + (0.0121 \times 16 \times 0.8280) = 0.20450 + 0.16981 + 0.16157 + 0.16135 + 0.16030 = 0.85753$
- $S_{xy,w} = \sum w_i x_i y_i - \frac{(\sum w_i x_i)(\sum w_i y_i)}{\sum w_i} = 0.85753 - \frac{6.9169 \times 0.35999}{5.000} = 0.85753 - 0.49800 = 0.35953$

The weighted slope and intercept are:
$$m_{\text{wls}} = \frac{S_{xy,w}}{S_{xx,w}} = \frac{0.35953}{6.9292} = 0.05189\text{ ppm}^{-1}$$
$$b_{\text{wls}} = \bar{y}_w - m_{\text{wls}} \bar{x}_w = 0.07200 - (0.05189 \times 1.3834) = 0.07200 - 0.07178 = 0.00022$$
The calibrated model is $\hat{y} = 0.05189\,x + 0.00022$.

### Part 3: Unknown Concentration and Standard Error
For $\bar{y}_{\text{unk}} = 0.3120$:
$$x_{\text{unk}} = \frac{\bar{y}_{\text{unk}} - b_{\text{wls}}}{m_{\text{wls}}} = \frac{0.3120 - 0.00022}{0.05189} = \frac{0.31178}{0.05189} = 6.008\text{ ppm}$$
The weighted standard error is:
$$s_{x_{\text{unk}}} = \frac{s_{\text{res},w}}{m_{\text{wls}}} \sqrt{\frac{1}{w_{\text{unk}} m} + \frac{1}{\sum w_i} + \frac{(x_{\text{unk}} - \bar{x}_w)^2}{S_{xx,w}}}$$
Because the lowest concentration standards carry $78\%$ of the statistical weight in WLS, the fit is anchored securely near the origin, preventing high-concentration heteroscedastic noise from distorting low-level quantitation."""
    }
    u1["problems"].append(prob_1_8)

    # =========================================================================
    # UNIT 2 ENRICHMENT
    # =========================================================================
    # Section 2.1: Comminution Particle Size and Sampling Constant Derivation
    u2["sections"][0]["content"] += r"""

### Visman Two-Constant Sampling Model
While the Ingamells sampling constant $K_s$ models fundamental random segregation in well-mixed particulate matrices, real industrial raw materials (e.g., coals, crushed mineral ores, soil deposits) exhibit both random particulate variance and long-range spatial segregation variance. In 1969, J. Visman derived the two-constant general sampling equation:

$$s^2 = \frac{A_v}{M} + \frac{B_v}{N_s} \tag{2.0a}$$

where:
- $s^2$ is the total variance of the gross sample composed of $N_s$ increments each having mass $m_{\text{incr}}$ (total gross mass $M = N_s \times m_{\text{incr}}$).
- $A_v$ is the **random variance constant** (governed by particle size and mineral liberation degree, equivalent to Ingamells $K_s$ when segregation is absent).
- $B_v$ is the **segregation variance constant**, reflecting macroscopic spatial gradients, stratifications, or batch inhomogeneity across the bulk population.

By conducting a two-tier sampling experiment collecting small and large increment sets, an analytical laboratory can simultaneously evaluate $A_v$ and $B_v$:
$$s_1^2 = \frac{A_v}{M_1} + \frac{B_v}{N_1}, \quad s_2^2 = \frac{A_v}{M_2} + \frac{B_v}{N_2} \tag{2.0b}$$
Solving this linear system determines the minimum gross sample mass $M_{\text{min}}$ and minimum number of increments $N_{\text{min}}$ required to attain any pre-defined confidence tolerance."""

    # Problem 2.8: Ingamells Constant and Comminution Optimization in Geological Assaying
    prob_2_8 = {
        "id": "prob-2-8",
        "title": "Problem 2.8: Ingamells Constant Evaluation and Particle Comminution Threshold in Gold Ore Assaying",
        "statement": r"""A low-grade gold quartz vein ore contains approximately $5.00\text{ ppm}$ of gold distributed as tiny discrete native gold flecks ($\rho_{\text{Au}} = 19.3\text{ g}\cdot\text{cm}^{-3}$) embedded within a barren quartz gangue matrix ($\rho_{\text{quartz}} = 2.65\text{ g}\cdot\text{cm}^{-3}$).
A pilot sampling experiment on ore crushed to a maximum particle diameter of $d_1 = 1.00\text{ mm}$ ($0.100\text{ cm}$) yielded an Ingamells sampling constant of $K_s = 2.50 \times 10^4\text{ g}$ ($25.0\text{ kg}$).
1. Calculate the minimum mass of gross sample ($m_s$) required from this $1.00\text{ mm}$ crushed ore to ensure that the sampling relative standard deviation does not exceed $RSD_s = 1.00\%$.
2. To allow routine laboratory assaying using standard $30.0\text{ g}$ fire-assay charges with $RSD_s \le 1.00\%$, the ore must be pulverized (comminuted) to a finer mesh. Using Gy's cubic relationship ($K_s \propto d^3$), calculate the maximum allowable particle diameter $d_2$ (in $\mu\text{m}$) to which the sample must be ground.
3. If the pulverizer can only reliably reduce the particles to $75.0\,\mu\text{m}$ ($-200\text{ mesh}$), calculate the resulting sampling standard deviation for a $30.0\text{ g}$ fire assay aliquot.""",
        "solution": r"""### Part 1: Minimum Gross Sample Mass for 1.00 mm Ore
By the Ingamells sampling relationship:
$$K_s = m_s \times R^2$$
where $R$ is the percent relative standard deviation ($\%RSD_s = 1.00\%$).
$$m_s = \frac{K_s}{R^2} = \frac{2.50 \times 10^4\text{ g}}{(1.00)^2} = 25,000\text{ g} = 25.0\text{ kg}$$
To obtain a sampling uncertainty of $\le 1.00\%$ on the $1.00\text{ mm}$ material, the analyst must collect at least $25.0\text{ kg}$ of gross sample.

### Part 2: Required Particle Diameter for 30.0 g Assays
According to Gy's sampling theory, the sampling constant $K_s$ scales with the cube of the top particle diameter:
$$K_s \propto d^3 \implies \frac{K_{s,2}}{K_{s,1}} = \left(\frac{d_2}{d_1}\right)^3$$
For a $30.0\text{ g}$ test portion to achieve $R = 1.00\%$, the target sampling constant is:
$$K_{s,2} = m_{s,2} \times R^2 = 30.0\text{ g} \times (1.00)^2 = 30.0\text{ g}$$
Setting up the ratio:
$$\frac{30.0\text{ g}}{2.50 \times 10^4\text{ g}} = \left(\frac{d_2}{1.00\text{ mm}}\right)^3$$
$$1.20 \times 10^{-3} = \left(\frac{d_2}{1.00\text{ mm}}\right)^3 \implies \frac{d_2}{1.00\text{ mm}} = (1.20 \times 10^{-3})^{1/3} = 0.10626$$
$$d_2 = 0.10626\text{ mm} = 106.3\,\mu\text{m} \approx 106\,\mu\text{m}$$
The sample must be comminuted until all particles pass through a $106\,\mu\text{m}$ sieve (approximately 140 mesh).

### Part 3: Uncertainty with 75.0 µm Pulverization
If the material is ground to $d = 75.0\,\mu\text{m} = 0.0750\text{ mm}$:
$$K_{s,75} = K_{s,1} \times \left(\frac{0.0750\text{ mm}}{1.00\text{ mm}}\right)^3 = 25,000\text{ g} \times (4.21875 \times 10^{-4}) = 10.55\text{ g}$$
For a $30.0\text{ g}$ analytical aliquot:
$$R = \sqrt{\frac{K_{s,75}}{m_s}} = \sqrt{\frac{10.55\text{ g}}{30.0\text{ g}}} = \sqrt{0.3516} = 0.593\%$$
The sampling relative standard deviation drops to $0.59\%$, well within the target threshold of $1.00\%$."""
    }
    u2["problems"].append(prob_2_8)

    # =========================================================================
    # UNIT 3 ENRICHMENT
    # =========================================================================
    # Section 3.1: von Weimarn RSS Mathematical Rate Kinetics
    u3["sections"][0]["content"] += r"""

### Kinetic Nucleation vs Growth Rate Differential Formulation
The classical von Weimarn ratio ($RSS = \frac{Q - S}{S}$) can be formally derived from physical nucleation and crystal growth rate equations.
1. **Primary Homogeneous Nucleation Rate ($J_{\text{nuc}}$)**:
   According to the Volmer-Weber-Becker-Döring classical nucleation theory, the rate of embryo nucleus formation per unit volume is:
   $$J_{\text{nuc}} = k_n \exp\left( -\frac{16 \pi \gamma_{\text{SL}}^3 V_m^2}{3 k_B^3 T^3 (\ln S_r)^2} \right) \tag{3.0a}$$
   where $\gamma_{\text{SL}}$ is the solid-liquid interfacial surface energy, $V_m$ is the molecular volume, and $S_r = Q / S$ is the supersaturation ratio.
   When $Q \gg S$, $\ln S_r$ is large, the exponential barrier vanishes, and the nucleation rate accelerates exponentially by orders of magnitude.
2. **Crystal Growth Rate ($R_{\text{growth}}$)**:
   Once stable nuclei exist, crystal growth by spiral dislocation (Burton-Cabrera-Frank model) or diffusion control proceeds as:
   $$R_{\text{growth}} = k_g (Q - S)^p \tag{3.0b}$$
   where $p \approx 1\text{ to }2$.
   Because crystal growth scales as a modest polynomial ($p \le 2$) while nucleation scales exponentially with supersaturation, elevated supersaturation overwhelmingly favors nucleation ($J_{\text{nuc}} \gg R_{\text{growth}}$), generating billions of micro-crystallites that form an unfilterable colloidal suspension."""

    # Problem 3.8: Fractional Precipitation and Separation of Cation Groups
    prob_3_8 = {
        "id": "prob-3-8",
        "title": "Problem 3.8: Homogeneous Precipitation and Fractional Sulfide Separation of Cadmium(II) and Manganese(II)",
        "statement": r"""A solution contains $0.0500\text{ M Cd}^{2+}$ and $0.0500\text{ M Mn}^{2+}$. The solubility products are:
- $K_{\text{sp}}(\text{CdS}) = 1.00 \times 10^{-27}$
- $K_{\text{sp}}(\text{MnS}) = 3.00 \times 10^{-13}$

Gaseous $\text{H}_2\text{S}$ is generated in situ by homogeneous hydrolysis of thioacetamide ($\text{CH}_3\text{CSNH}_2$) at $80^\circ\text{C}$ in an acidic buffer. In saturated aqueous solution, $[\text{H}_2\text{S}] \approx 0.100\text{ M}$, and the overall sulfide diprotic dissociation constant is:
$$K_{a1} K_{a2} = \frac{[\text{H}^+]^2 [\text{S}^{2-}]}{[\text{H}_2\text{S}]} = 1.00 \times 10^{-21}$$

1. Calculate the minimum concentration of sulfide $[\text{S}^{2-}]$ required to initiate precipitation of $\text{CdS}$ and $\text{MnS}$.
2. Calculate the maximum pH allowable that prevents precipitation of $\text{MnS}$ while guaranteeing that $\ge 99.999\%$ of $\text{Cd}^{2+}$ has been precipitated as $\text{CdS}$ ($[\text{Cd}^{2+}] \le 5.00 \times 10^{-7}\text{ M}$).
3. State whether quantitative separation of $\text{Cd}^{2+}$ from $\text{Mn}^{2+}$ is thermodynamically feasible at $\text{pH } 1.00$.""",
        "solution": r"""### Part 1: Minimum Sulfide Required for Precipitation
- For $\text{CdS}$:
  $$[\text{S}^{2-}]_{\text{crit},\text{Cd}} = \frac{K_{\text{sp}}(\text{CdS})}{[\text{Cd}^{2+}]_0} = \frac{1.00 \times 10^{-27}}{0.0500} = 2.00 \times 10^{-26}\text{ M}$$
- For $\text{MnS}$:
  $$[\text{S}^{2-}]_{\text{crit},\text{Mn}} = \frac{K_{\text{sp}}(\text{MnS})}{[\text{Mn}^{2+}]_0} = \frac{3.00 \times 10^{-13}}{0.0500} = 6.00 \times 10^{-12}\text{ M}$$

### Part 2: Optimum pH Window for Separation
To achieve $99.999\%$ precipitation of $\text{Cd}^{2+}$, the residual concentration is $[\text{Cd}^{2+}]_{\text{res}} = 0.0500 \times (1 - 0.99999) = 5.00 \times 10^{-7}\text{ M}$.
The sulfide concentration required to maintain this residual level is:
$$[\text{S}^{2-}]_{\text{target}} = \frac{K_{\text{sp}}(\text{CdS})}{[\text{Cd}^{2+}]_{\text{res}}} = \frac{1.00 \times 10^{-27}}{5.00 \times 10^{-7}} = 2.00 \times 10^{-21}\text{ M}$$
To prevent $\text{MnS}$ precipitation, $[\text{S}^{2-}]$ must remain below $6.00 \times 10^{-12}\text{ M}$.
Because $2.00 \times 10^{-21}\text{ M} \ll 6.00 \times 10^{-12}\text{ M}$, a vast separation window exists!
Using the diprotic sulfide equilibrium with $[\text{H}_2\text{S}] = 0.100\text{ M}$:
$$[\text{S}^{2-}] = \frac{K_{a1} K_{a2} [\text{H}_2\text{S}]}{[\text{H}^+]^2} = \frac{1.00 \times 10^{-21} \times 0.100}{[\text{H}^+]^2} = \frac{1.00 \times 10^{-22}}{[\text{H}^+]^2}$$

- To reach $[\text{S}^{2-}] = 2.00 \times 10^{-21}\text{ M}$:
  $$[\text{H}^+]^2 = \frac{1.00 \times 10^{-22}}{2.00 \times 10^{-21}} = 0.0500 \implies [\text{H}^+] = \sqrt{0.0500} = 0.2236\text{ M} \implies \text{pH} = 0.65$$
- To prevent $\text{MnS}$ ($[\text{S}^{2-}] \le 6.00 \times 10^{-12}\text{ M}$):
  $$[\text{H}^+]^2 \ge \frac{1.00 \times 10^{-22}}{6.00 \times 10^{-12}} = 1.667 \times 10^{-11} \implies [\text{H}^+] \ge 4.08 \times 10^{-6}\text{ M} \implies \text{pH} \le 5.39$$
Thus, complete separation occurs in the broad range:
$$0.65 \le \text{pH} \le 5.39$$

### Part 3: Feasibility at pH 1.00
At $\text{pH } 1.00$, $[\text{H}^+] = 0.100\text{ M}$:
$$[\text{S}^{2-}] = \frac{1.00 \times 10^{-22}}{(0.100)^2} = 1.00 \times 10^{-20}\text{ M}$$
Under this sulfide concentration:
- Residual $[\text{Cd}^{2+}] = \frac{1.00 \times 10^{-27}}{1.00 \times 10^{-20}} = 1.00 \times 10^{-7}\text{ M} \implies 99.9998\%$ of $\text{Cd}$ is precipitated!
- Ion product for $\text{MnS}$: $Q = [\text{Mn}^{2+}][\text{S}^{2-}] = 0.0500 \times 1.00 \times 10^{-20} = 5.00 \times 10^{-22} \ll K_{\text{sp}}(\text{MnS}) = 3.00 \times 10^{-13}$. Zero $\text{MnS}$ precipitates!
Therefore, buffering at $\text{pH } 1.00$ ($0.1\text{ M HCl}$) achieves quantitative separation of analytical Group II cations ($\text{Cd}^{2+}$) from Group III cations ($\text{Mn}^{2+}$)."""
    }
    u3["problems"].append(prob_3_8)
    print("Enriched Units 1, 2, and 3 successfully.")
