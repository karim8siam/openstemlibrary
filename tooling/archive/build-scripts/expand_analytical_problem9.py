# -*- coding: utf-8 -*-
"""
expand_analytical_problem9.py
Injects Problem 9 across all 9 units of Analytical Chemistry (#46),
bringing every unit to 9 comprehensive solved problems (81 solved problems total).
Strict zero course numbers or marks. All math in raw strings r\"\"\"...\"\"\".
"""

def add_problem9_to_all_units(units):
    print("Injecting Problem 9 across all 9 units (achieving 81 solved problems total)...")

    prob9_data = [
        # Unit 1: Problem 1.9
        {
            "id": "prob-1-9",
            "title": "Problem 1.9: Multi-Laboratory Collaborative Study: Youden Two-Sample Diagram & Systematic vs Random Error Decomposition",
            "statement": r"""In an international proficiency testing study, ten analytical laboratories analyzed two blind test samples of powdered milk ($X$ and $Y$) for calcium concentration (in $\text{mg}\cdot\text{g}^{-1}$).
The certified reference values are $X_0 = 12.50\text{ mg}\cdot\text{g}^{-1}$ and $Y_0 = 12.80\text{ mg}\cdot\text{g}^{-1}$.
The paired results $(x_i, y_i)$ reported by the 10 laboratories are:
- Lab 1: $(12.45, 12.76)$
- Lab 2: $(12.52, 12.83)$
- Lab 3: $(12.30, 12.58)$
- Lab 4: $(12.68, 13.01)$
- Lab 5: $(12.48, 12.79)$
- Lab 6: $(12.85, 13.18)$
- Lab 7: $(12.38, 12.66)$
- Lab 8: $(12.55, 12.86)$
- Lab 9: $(12.20, 12.45)$
- Lab 10: $(12.60, 12.92)$

1. For each laboratory, compute the coordinate transformation variables:
   $$D_i = \frac{x_i - y_i}{\sqrt{2}}, \quad S_i = \frac{x_i + y_i}{\sqrt{2}}$$
2. Calculate the sample standard deviations $s_D$ and $s_S$.
3. Using Youden's variance decomposition:
   $$\sigma_{\text{random}} = s_D, \quad \sigma_{\text{systematic}} = \sqrt{\frac{s_S^2 - s_D^2}{2}}$$
   Calculate the pure random standard deviation ($\sigma_{\text{random}}$) and the between-laboratory systematic bias standard deviation ($\sigma_{\text{systematic}}$).
4. State whether systematic laboratory bias or within-laboratory random variability dominates the collaborative error budget.""",
            "solution": r"""### Part 1: Transformation Variables $(D_i, S_i)$
Let us tabulate the differences and sums:
- Lab 1: $x_1 - y_1 = -0.31$, $x_1 + y_1 = 25.21 \implies D_1 = -0.2192, S_1 = 17.8262$
- Lab 2: $x_2 - y_2 = -0.31$, $x_2 + y_2 = 25.35 \implies D_2 = -0.2192, S_2 = 17.9252$
- Lab 3: $x_3 - y_3 = -0.28$, $x_3 + y_3 = 24.88 \implies D_3 = -0.1980, S_3 = 17.5928$
- Lab 4: $x_4 - y_4 = -0.33$, $x_4 + y_4 = 25.69 \implies D_4 = -0.2333, S_4 = 18.1655$
- Lab 5: $x_5 - y_5 = -0.31$, $x_5 + y_5 = 25.27 \implies D_5 = -0.2192, S_5 = 17.8686$
- Lab 6: $x_6 - y_6 = -0.33$, $x_6 + y_6 = 26.03 \implies D_6 = -0.2333, S_6 = 18.4060$
- Lab 7: $x_7 - y_7 = -0.28$, $x_7 + y_7 = 25.04 \implies D_7 = -0.1980, S_7 = 17.7059$
- Lab 8: $x_8 - y_8 = -0.31$, $x_8 + y_8 = 25.41 \implies D_8 = -0.2192, S_8 = 17.9676$
- Lab 9: $x_9 - y_9 = -0.25$, $x_9 + y_9 = 24.65 \implies D_9 = -0.1768, S_9 = 17.4302$
- Lab 10: $x_{10} - y_{10} = -0.32$, $x_{10} + y_{10} = 25.52 \implies D_{10} = -0.2263, S_{10} = 18.0454$

### Part 2: Calculation of Standard Deviations $s_D$ and $s_S$
- **For $D$**:
  Mean $\bar{D} = -0.2143$.
  Deviations $(D_i - \bar{D})$:
  $\sum (D_i - \bar{D})^2 = 0.002824$
  $$s_D = \sqrt{\frac{0.002824}{9}} = \sqrt{0.0003138} = 0.0177\text{ mg}\cdot\text{g}^{-1}$$
- **For $S$**:
  Mean $\bar{S} = 17.8933$.
  Deviations $(S_i - \bar{S})$:
  $\sum (S_i - \bar{S})^2 = 0.7618$
  $$s_S = \sqrt{\frac{0.7618}{9}} = \sqrt{0.08464} = 0.2910\text{ mg}\cdot\text{g}^{-1}$$

### Part 3: Decomposition into Random and Systematic Variances
- **Pure Random Precision**:
  $$\sigma_{\text{random}} = s_D = 0.0177\text{ mg}\cdot\text{g}^{-1}$$
- **Between-Laboratory Systematic Bias Standard Deviation**:
  $$\sigma_{\text{systematic}} = \sqrt{\frac{s_S^2 - s_D^2}{2}} = \sqrt{\frac{(0.2910)^2 - (0.0177)^2}{2}} = \sqrt{\frac{0.08468 - 0.00031}{2}} = \sqrt{\frac{0.08437}{2}} = \sqrt{0.04218} = 0.2054\text{ mg}\cdot\text{g}^{-1}$$

### Part 4: Analytical Assessment
The ratio of systematic to random standard deviation is:
$$\frac{\sigma_{\text{systematic}}}{\sigma_{\text{random}}} = \frac{0.2054}{0.0177} = 11.6$$
Systematic between-laboratory bias exceeds within-laboratory random variability by more than an order of magnitude ($11.6\times$). This confirms that individual laboratories maintain excellent internal precision, but differ systematically due to calibration curve standards, pipetting calibration offsets, or instrument drift."""
        },

        # Unit 2: Problem 2.9
        {
            "id": "prob-2-9",
            "title": "Problem 2.9: Visman Two-Constant Sampling Experiment on Run-of-Mine Coal",
            "statement": r"""A mining analytical laboratory conducted a Visman two-tier sampling trial on a bulk shipment of run-of-mine coal to determine ash content variability:
1. **Series 1 (Small Increments)**: $N_1 = 30$ increments of mass $m_1 = 0.200\text{ kg}$ each were collected (total gross mass $M_1 = 6.00\text{ kg}$), yielding an experimental ash variance of $s_1^2 = 0.650 (\% \text{ ash})^2$.
2. **Series 2 (Large Increments)**: $N_2 = 30$ increments of mass $m_2 = 2.000\text{ kg}$ each were collected (total gross mass $M_2 = 60.0\text{ kg}$), yielding an experimental ash variance of $s_2^2 = 0.110 (\% \text{ ash})^2$.

Using the Visman equation $s^2 = \frac{A_v}{M} + \frac{B_v}{N}$:
1. Calculate Visman's random variance constant ($A_v$) and segregation variance constant ($B_v$).
2. To satisfy commercial contract specifications, the sampling variance must not exceed $s^2 \le 0.040 (\% \text{ ash})^2$. If the sampling protocol is designed to collect increments of mass $m_{\text{incr}} = 1.00\text{ kg}$, calculate the minimum number of increments ($N_{\text{min}}$) and minimum gross sample mass ($M_{\text{min}}$) required.""",
            "solution": r"""### Part 1: Determination of Visman Constants $A_v$ and $B_v$
From the Visman model:
$$1) \quad 0.650 = \frac{A_v}{6.00} + \frac{B_v}{30}$$
$$2) \quad 0.110 = \frac{A_v}{60.0} + \frac{B_v}{30}$$

Subtract equation (2) from equation (1):
$$0.650 - 0.110 = A_v \left( \frac{1}{6.00} - \frac{1}{60.0} \right) + 0$$
$$0.540 = A_v \left( \frac{10 - 1}{60.0} \right) = A_v \left( \frac{9}{60.0} \right) = 0.150\,A_v$$
$$A_v = \frac{0.540}{0.150} = 3.600\text{ kg}\cdot(\% \text{ ash})^2$$

Substitute $A_v$ into equation (2):
$$0.110 = \frac{3.600}{60.0} + \frac{B_v}{30} = 0.0600 + \frac{B_v}{30}$$
$$\frac{B_v}{30} = 0.110 - 0.0600 = 0.0500$$
$$B_v = 30 \times 0.0500 = 1.500\text{ }(\% \text{ ash})^2$$

### Part 2: Minimum Increments and Mass for $s^2 \le 0.040$
For increments of mass $m_{\text{incr}} = 1.00\text{ kg}$, total gross mass is $M = N \times m_{\text{incr}} = N \times 1.00\text{ kg} = N\text{ kg}$.
Substitute into the Visman equation:
$$s^2 = \frac{A_v}{N} + \frac{B_v}{N} = \frac{A_v + B_v}{N}$$
Setting $s^2 \le 0.040$:
$$\frac{3.600 + 1.500}{N} \le 0.040$$
$$\frac{5.100}{N} \le 0.040 \implies N \ge \frac{5.100}{0.040} = 127.5$$
Rounding up to the next integer:
$$N_{\text{min}} = 128\text{ increments}$$
$$M_{\text{min}} = 128 \times 1.00\text{ kg} = 128.0\text{ kg}$$
To ensure contract compliance ($s^2 \le 0.040$), the automated cross-belt sampler must collect at least $128$ increments totaling $128\text{ kg}$ of coal."""
        },

        # Unit 3: Problem 3.9
        {
            "id": "prob-3-9",
            "title": "Problem 3.9: Homogeneous Gravimetric Determination of Nickel with Dimethylglyoxime and Urea",
            "statement": r"""A $1.0000\text{ g}$ sample of a cupronickel alloy is dissolved in nitric acid, treated with tartaric acid to complex iron, and analyzed for nickel using precipitation from homogeneous solution (PFHS).
To the acidic solution ($[\text{H}^+] \approx 0.1\text{ M}$), an excess of dimethylglyoxime ($\text{HDMG}$) and $10.0\text{ g}$ of urea are added. The mixture is heated to $95^\circ\text{C}$ for 90 minutes. Urea hydrolyzes slowly to raise the pH uniformly to $8.0$, precipitating scarlet-red nickel dimethylglyoximate:
$$\text{Ni}^{2+} + 2\,\text{HDMG} + 2\,\text{NH}_3 \to \text{Ni(DMG)}_2(\text{s})\downarrow + 2\,\text{NH}_4^+$$
The precipitate is filtered through a pre-weighed sintered glass crucible, washed with ice water, and dried to constant weight at $110^\circ\text{C}$:
- Mass of empty crucible: $24.8152\text{ g}$
- Mass of crucible + dried precipitate: $26.1428\text{ g}$
Molar masses: $\text{Ni} = 58.693\text{ g}\cdot\text{mol}^{-1}$, $\text{Ni(DMG)}_2 = 288.91\text{ g}\cdot\text{mol}^{-1}$.

1. Calculate the mass of $\text{Ni(DMG)}_2$ precipitate collected.
2. Determine the gravimetric factor ($GF$) for nickel in $\text{Ni(DMG)}_2$.
3. Calculate the weight percentage ($\% \text{ w/w}$) of nickel in the alloy.
4. Explain why homogeneous urea precipitation produces a purer and denser precipitate than direct dropwise ammonia neutralization.""",
            "solution": r"""### Part 1: Mass of Precipitate
$$\text{Mass}_{\text{ppt}} = 26.1428\text{ g} - 24.8152\text{ g} = 1.3276\text{ g}$$

### Part 2: Gravimetric Factor (GF)
The gravimetric factor is:
$$GF = \frac{M(\text{Ni})}{M(\text{Ni(DMG)}_2)} = \frac{58.693\text{ g}\cdot\text{mol}^{-1}}{288.91\text{ g}\cdot\text{mol}^{-1}} = 0.203153$$

### Part 3: Nickel Weight Percentage in Alloy
Mass of pure nickel in sample:
$$\text{Mass}_{\text{Ni}} = \text{Mass}_{\text{ppt}} \times GF = 1.3276\text{ g} \times 0.203153 = 0.26971\text{ g}$$
Weight percentage in the $1.0000\text{ g}$ sample:
$$\% \text{ Ni} = \left(\frac{0.26971\text{ g}}{1.0000\text{ g}}\right) \times 100\% = 26.97\%$$

### Part 4: Analytical Advantages of Urea PFHS
In direct dropwise ammonia neutralization, local regions near the burette tip experience instantaneous alkaline conditions ($\text{pH} > 9$), causing sudden, massive relative supersaturation ($RSS \gg 10^4$). This precipitates an unwieldy, voluminous, bulky gelatinous mass that traps mother liquor and coprecipitates foreign metal ions.
In contrast, urea hydrolysis occurs uniformly at the molecular scale throughout the boiling solution. Relative supersaturation remains close to unity ($RSS \approx 0$). Coarse, dense, well-crystallized needles of $\text{Ni(DMG)}_2$ grow slowly on existing crystal surfaces, eliminating coprecipitation of copper and iron and filtering in seconds."""
        },

        # Unit 4: Problem 4.9
        {
            "id": "prob-4-9",
            "title": "Problem 4.9: Masking and Demasking Multi-Metal Titration of a Fusible Solder Alloy (Bi, Pb, Cd)",
            "statement": r"""A $0.5000\text{ g}$ sample of a low-melting fusible solder alloy containing bismuth, lead, and cadmium is dissolved in nitric acid and diluted to $250.0\text{ mL}$ in a volumetric flask.
A sequence of EDTA titrations with standard $0.01000\text{ M}$ EDTA is performed on $50.00\text{ mL}$ aliquots:
1. **Aliquot 1**: Adjusted to $\text{pH } 1.5$ with nitric acid. Using xylenol orange indicator, titration to the yellow endpoint requires $12.40\text{ mL}$ of EDTA.
2. **Aliquot 2**: Adjusted to $\text{pH } 5.5$ with hexamine buffer. Using xylenol orange indicator, titration to the yellow endpoint requires $36.20\text{ mL}$ of EDTA.
3. **Aliquot 3**: Adjusted to $\text{pH } 5.5$ with hexamine buffer, then treated with excess 1,10-phenanthroline to mask cadmium selectively. Titration with EDTA requires $25.80\text{ mL}$.

Calculate:
1. The percentage of bismuth ($\% \text{ Bi}$) in the alloy ($M(\text{Bi}) = 208.98\text{ g}\cdot\text{mol}^{-1}$).
2. The percentage of lead ($\% \text{ Pb}$) in the alloy ($M(\text{Pb}) = 207.2\text{ g}\cdot\text{mol}^{-1}$).
3. The percentage of cadmium ($\% \text{ Cd}$) in the alloy ($M(\text{Cd}) = 112.41\text{ g}\cdot\text{mol}^{-1}$).""",
            "solution": r"""### Part 1: Bismuth Determination (Aliquot 1)
At $\text{pH } 1.5$, only $\text{Bi}^{3+}$ forms a sufficiently stable EDTA complex ($\log K_f = 27.9$, conditional constant $\log K'_f > 10$), while $\text{Pb}^{2+}$ and $\text{Cd}^{2+}$ do not react:
$$n_{\text{Bi,aliquot}} = 0.01000\text{ M} \times 0.01240\text{ L} = 1.240 \times 10^{-4}\text{ mol}$$
In the full $250.0\text{ mL}$ flask (aliquot factor $250 / 50 = 5$):
$$n_{\text{Bi,total}} = 1.240 \times 10^{-4} \times 5 = 6.200 \times 10^{-4}\text{ mol}$$
$$\text{Mass}_{\text{Bi}} = 6.200 \times 10^{-4}\text{ mol} \times 208.98\text{ g}\cdot\text{mol}^{-1} = 0.12957\text{ g}$$
$$\% \text{ Bi} = \left(\frac{0.12957\text{ g}}{0.5000\text{ g}}\right) \times 100\% = 25.91\%$$

### Part 2: Lead Determination (Aliquot 2 vs Aliquot 3)
In Aliquot 2 at $\text{pH } 5.5$, all three metals ($\text{Bi}^{3+}, \text{Pb}^{2+}, \text{Cd}^{2+}$) react with EDTA:
$$V_{\text{total}} = 36.20\text{ mL}$$
In Aliquot 3 at $\text{pH } 5.5$, cadmium is completely masked by 1,10-phenanthroline ($[\text{Cd}(\text{phen})_3]^{2+}$), leaving only $\text{Bi}^{3+}$ and $\text{Pb}^{2+}$ to titrate:
$$V_{\text{Bi+Pb}} = 25.80\text{ mL}$$
The volume consumed solely by lead is:
$$V_{\text{Pb}} = V_{\text{Bi+Pb}} - V_{\text{Bi}} = 25.80\text{ mL} - 12.40\text{ mL} = 13.40\text{ mL}$$
$$n_{\text{Pb,aliquot}} = 0.01000\text{ M} \times 0.01340\text{ L} = 1.340 \times 10^{-4}\text{ mol}$$
$$n_{\text{Pb,total}} = 1.340 \times 10^{-4} \times 5 = 6.700 \times 10^{-4}\text{ mol}$$
$$\text{Mass}_{\text{Pb}} = 6.700 \times 10^{-4}\text{ mol} \times 207.2\text{ g}\cdot\text{mol}^{-1} = 0.13882\text{ g}$$
$$\% \text{ Pb} = \left(\frac{0.13882\text{ g}}{0.5000\text{ g}}\right) \times 100\% = 27.76\%$$

### Part 3: Cadmium Determination
The volume consumed solely by cadmium is:
$$V_{\text{Cd}} = V_{\text{total}} - V_{\text{Bi+Pb}} = 36.20\text{ mL} - 25.80\text{ mL} = 10.40\text{ mL}$$
$$n_{\text{Cd,aliquot}} = 0.01000\text{ M} \times 0.01040\text{ L} = 1.040 \times 10^{-4}\text{ mol}$$
$$n_{\text{Cd,total}} = 1.040 \times 10^{-4} \times 5 = 5.200 \times 10^{-4}\text{ mol}$$
$$\text{Mass}_{\text{Cd}} = 5.200 \times 10^{-4}\text{ mol} \times 112.41\text{ g}\cdot\text{mol}^{-1} = 0.05845\text{ g}$$
$$\% \text{ Cd} = \left(\frac{0.05845\text{ g}}{0.5000\text{ g}}\right) \times 100\% = 11.69\%$$
Sum of components: $25.91\% + 27.76\% + 11.69\% = 65.36\%$ (the remaining $34.64\%$ is tin)."""
        },

        # Unit 5: Problem 5.9
        {
            "id": "prob-5-9",
            "title": "Problem 5.9: High-Resolution Continuum Source AAS (HR-CS AAS) Determination of Arsenic in Estuarine Sediments",
            "statement": r"""A $0.5000\text{ g}$ certified estuarine sediment sample is digested in a closed microwave vessel using $\text{HNO}_3 / \text{HF} / \text{HCl}$ and diluted to $50.00\text{ mL}$.
Analysis is conducted by High-Resolution Continuum Source Graphite Furnace AAS (HR-CS GFAAS) at the primary arsenic resonance doublet at $\lambda = 193.696\text{ nm}$.
A linear 512-pixel CCD array records the spectral environment across pixels 200–250.
- Central analytical pixels (CP: pixels 224–226) record total absorbance: $A_{\text{CP}} = 0.285$.
- Adjacent baseline correction pixels (BP: pixels 215–219 and 231–235, 10 pixels total) record mean background: $\bar{A}_{\text{BP}} = 0.125$.

A matrix-matched calibration curve constructed from blank-corrected net absorbance gave the linear regression:
$$A_{\text{net}} = 0.0160 \times (\text{conc in }\mu\text{g}\cdot\text{L}^{-1}) + 0.0008$$
1. Calculate the net corrected arsenic absorbance ($A_{\text{net}}$).
2. Calculate the concentration of arsenic in the digest solution (in $\mu\text{g}\cdot\text{L}^{-1}$).
3. Calculate the mass fraction of arsenic in the original sediment sample in $\text{mg}\cdot\text{kg}^{-1}$ ($\text{ppm}$).""",
            "solution": r"""### Part 1: Net Corrected Absorbance
In HR-CS AAS, pixel-level simultaneous baseline correction subtracts the mean of the adjacent non-absorbing baseline pixels:
$$A_{\text{net}} = A_{\text{CP}} - \bar{A}_{\text{BP}} = 0.285 - 0.125 = 0.160$$

### Part 2: Arsenic Concentration in Digest Solution
From the calibration curve:
$$C_{\text{As}} = \frac{A_{\text{net}} - 0.0008}{0.0160} = \frac{0.160 - 0.0008}{0.0160} = \frac{0.1592}{0.0160} = 9.95\,\mu\text{g}\cdot\text{L}^{-1}$$

### Part 3: Sediment Mass Fraction
The mass of arsenic in the $50.00\text{ mL}$ ($0.05000\text{ L}$) digest is:
$$\text{Mass}_{\text{As}} = 9.95\,\mu\text{g}\cdot\text{L}^{-1} \times 0.05000\text{ L} = 0.4975\,\mu\text{g}$$
The concentration in the $0.5000\text{ g}$ ($0.5000 \times 10^{-3}\text{ kg}$) sediment sample is:
$$w_{\text{As}} = \frac{0.4975\,\mu\text{g}}{0.5000 \times 10^{-3}\text{ kg}} = 995\,\mu\text{g}\cdot\text{kg}^{-1} = 0.995\text{ mg}\cdot\text{kg}^{-1} = 0.995\text{ ppm}$$"""
        },

        # Unit 6: Problem 6.9
        {
            "id": "prob-6-9",
            "title": "Problem 6.9: Dual-Column Suppressed Ion Chromatography of Acid Rain Anions",
            "statement": r"""An environmental testing laboratory analyzes an acid rain sample using chemically suppressed ion chromatography on an anion-exchange column (Dionex IonPac AS14) with a $3.5\text{ mM Na}_2\text{CO}_3 / 1.0\text{ mM NaHCO}_3$ eluent at $1.20\text{ mL}\cdot\text{min}^{-1}$.
1. Explain the chemical transformations occurring in the dynamic membrane suppressor and calculate the residual background conductance of the converted eluent (given equivalent conductances: $\lambda_{\text{H}^+} = 350\text{ S}\cdot\text{cm}^2\cdot\text{equiv}^{-1}$, $\lambda_{\text{HCO}_3^-} = 44.5\text{ S}\cdot\text{cm}^2\cdot\text{equiv}^{-1}$, $K_{a1}(\text{H}_2\text{CO}_3) = 4.5 \times 10^{-7}$).
2. An injected sample of acid rain yielded the following chromatographic peaks:
   - Peak 1 ($t_R = 2.15\text{ min}$): Fluoride ($\text{F}^-$)
   - Peak 2 ($t_R = 3.65\text{ min}$): Chloride ($\text{Cl}^-$)
   - Peak 3 ($t_R = 5.20\text{ min}$): Nitrate ($\text{NO}_3^-$)
   - Peak 4 ($t_R = 8.40\text{ min}$): Sulfate ($\text{SO}_4^{2-}$)
   Given void time $t_M = 1.10\text{ min}$, calculate the retention factors $k'$ for all four anions and justify the observed elution order based on ionic charge and polarizability.""",
            "solution": r"""### Part 1: Chemical Suppression Reactions and Background Conductance
In the membrane suppressor, sodium ions in the eluent are exchanged for hydronium ions across a cation-exchange membrane:
$$2\,\text{Na}^+ + \text{CO}_3^{2-} + 2\,\text{H}^+ \to 2\,\text{Na}^+ + \text{H}_2\text{CO}_3$$
$$\text{Na}^+ + \text{HCO}_3^- + \text{H}^+ \to \text{Na}^+ + \text{H}_2\text{CO}_3$$
Total initial carbonate species concentration: $C_{\text{total}} = 3.5\text{ mM} + 1.0\text{ mM} = 4.5 \times 10^{-3}\text{ M H}_2\text{CO}_3$.
Because carbonic acid is a very weak acid ($K_{a1} = 4.5 \times 10^{-7}$):
$$[\text{H}^+] = [\text{HCO}_3^-] \approx \sqrt{K_{a1} C_{\text{total}}} = \sqrt{(4.5 \times 10^{-7}) \times (4.5 \times 10^{-3})} = \sqrt{2.025 \times 10^{-9}} = 4.50 \times 10^{-5}\text{ M}$$
The specific conductance $\kappa$ is:
$$\kappa = \frac{1}{1000} \left( \lambda_{\text{H}^+} [\text{H}^+] + \lambda_{\text{HCO}_3^-} [\text{HCO}_3^-] \right) = \frac{1}{1000} (350 + 44.5) \times (4.50 \times 10^{-5}) = 1.77 \times 10^{-5}\text{ S}\cdot\text{cm}^{-1} = 17.7\,\mu\text{S}\cdot\text{cm}^{-1}$$
Chemical suppression collapses the conductance from $> 1200\,\mu\text{S}\cdot\text{cm}^{-1}$ to a quiet baseline of $< 18\,\mu\text{S}\cdot\text{cm}^{-1}$.

### Part 2: Retention Factors and Elution Order Mechanism
The retention factor is $k' = \frac{t_R - t_M}{t_M}$ with $t_M = 1.10\text{ min}$:
- **Fluoride**: $k'_{\text{F}} = \frac{2.15 - 1.10}{1.10} = \frac{1.05}{1.10} = 0.955$
- **Chloride**: $k'_{\text{Cl}} = \frac{3.65 - 1.10}{1.10} = \frac{2.55}{1.10} = 2.318$
- **Nitrate**: $k'_{\text{NO}_3} = \frac{5.20 - 1.10}{1.10} = \frac{4.10}{1.10} = 3.727$
- **Sulfate**: $k'_{\text{SO}_4} = \frac{8.40 - 1.10}{1.10} = \frac{7.30}{1.10} = 6.636$

*Physical Justification of Elution Order*:
1. **Charge Effect**: Monovalent anions ($\text{F}^-, \text{Cl}^-, \text{NO}_3^-$) elute much earlier than divalent anions ($\text{SO}_4^{2-}$). The electroselectivity of anion resins scales with ionic charge ($z$), binding divalent sulfate twice as strongly.
2. **Hydration and Polarizability Effect**: Among monovalent anions, fluoride has the smallest crystal radius and largest hydrated radius, interacting weakly with quaternary ammonium sites ($\text{F}^-$ elutes first). As polarizability increases ($\text{F}^- < \text{Cl}^- < \text{NO}_3^-$), hydrated radius shrinks and hydrophobic interaction with the resin polystyrene backbone increases, producing the observed sequence: $\text{F}^- < \text{Cl}^- < \text{NO}_3^- < \text{SO}_4^{2-}$."""
        },

        # Unit 7: Problem 7.9
        {
            "id": "prob-7-9",
            "title": "Problem 7.9: Multi-Wavelength Job's Method Resolution of Stepwise ML and ML2 Complexes",
            "statement": r"""A transition metal $M$ reacts with an organic ligand $L$ to form two consecutive absorbing complexes, $ML$ and $ML_2$:
$$M + L \rightleftharpoons ML \quad (K_1), \quad ML + L \rightleftharpoons ML_2 \quad (K_2)$$
Job's method of continuous variations was conducted at constant total concentration $C_{\text{total}} = C_M + C_L = 2.00 \times 10^{-4}\text{ M}$ across varying ligand mole fractions ($x_L = 0.1\text{ to }0.9$).
Absorbance measurements in a $1.000\text{ cm}$ cell at two diagnostic wavelengths gave:
- **At $\lambda_1 = 450\text{ nm}$**: The Job's curve displays a distinct maximum at $x_L = 0.500$ with $A_{450} = 0.620$.
- **At $\lambda_2 = 610\text{ nm}$**: The Job's curve displays a distinct maximum at $x_L = 0.667$ with $A_{610} = 0.840$.
Neither uncomplexed $M$ nor free $L$ absorbs at either wavelength.

1. Prove mathematically why the maximum at $450\text{ nm}$ indicates the $1:1$ complex ($ML$) while the maximum at $610\text{ nm}$ indicates the $1:2$ complex ($ML_2$).
2. Calculate the molar absorptivity $\varepsilon_{ML}$ at $450\text{ nm}$ (assuming dissociation is negligible at the peak).
3. Calculate the molar absorptivity $\varepsilon_{ML_2}$ at $610\text{ nm}$ (assuming complete conversion at $x_L = 0.667$).""",
            "solution": r"""### Part 1: Proof of Stoichiometry from Peak Positions
From the Job's method condition for complex $M_m L_n$:
$$x_{L,\text{max}} = \frac{n}{m + n}$$
- For $\lambda_1 = 450\text{ nm}$, $x_{L,\text{max}} = 0.500$:
  $$0.500 = \frac{n}{m + n} \implies m + n = 2n \implies m = n = 1$$
  This proves unambiguously that the absorbing chromophore at $450\text{ nm}$ has $1:1$ stoichiometry ($ML$).
- For $\lambda_2 = 610\text{ nm}$, $x_{L,\text{max}} = 0.667 = \frac{2}{3}$:
  $$\frac{2}{3} = \frac{n}{m + n} \implies 2m + 2n = 3n \implies n = 2m \implies m = 1, n = 2$$
  This proves that the absorbing species at $610\text{ nm}$ has $1:2$ stoichiometry ($ML_2$).

### Part 2: Molar Absorptivity of ML at 450 nm
At $x_L = 0.500$:
$$C_M = 0.500 \times 2.00 \times 10^{-4}\text{ M} = 1.00 \times 10^{-4}\text{ M}$$
$$C_L = 1.00 \times 10^{-4}\text{ M}$$
Assuming complete formation of $ML$, $[ML]_{\text{max}} = 1.00 \times 10^{-4}\text{ M}$.
Using Beer's law ($b = 1.000\text{ cm}$):
$$\varepsilon_{ML,450} = \frac{A_{450}}{b \times [ML]_{\text{max}}} = \frac{0.620}{1.000\text{ cm} \times 1.00 \times 10^{-4}\text{ M}} = 6200\text{ L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$$

### Part 3: Molar Absorptivity of ML2 at 610 nm
At $x_L = 0.667 = 2/3$:
$$C_M = \frac{1}{3} \times 2.00 \times 10^{-4}\text{ M} = 6.667 \times 10^{-5}\text{ M}$$
$$C_L = \frac{2}{3} \times 2.00 \times 10^{-4}\text{ M} = 1.333 \times 10^{-4}\text{ M}$$
Under stoichiometric equivalence, $[ML_2]_{\text{max}} = C_M = 6.667 \times 10^{-5}\text{ M}$.
Using Beer's law:
$$\varepsilon_{ML_2,610} = \frac{A_{610}}{b \times [ML_2]_{\text{max}}} = \frac{0.840}{1.000\text{ cm} \times 6.667 \times 10^{-5}\text{ M}} = 12,600\text{ L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$$"""
        },

        # Unit 8: Problem 8.9
        {
            "id": "prob-8-9",
            "title": "Problem 8.9: Multi-Stage Countercurrent Extraction of Neodymium and Praseodymium with D2EHPA",
            "statement": r"""Neodymium ($\text{Nd}^{3+}$) and praseodymium ($\text{Pr}^{3+}$) are separated industrially by countercurrent liquid-liquid extraction from an aqueous nitric acid feed into kerosene containing di-(2-ethylhexyl)phosphoric acid ($\text{D2EHPA}$, $[\text{HA}]_2$).
Under operational conditions:
- Distribution ratio of Neodymium: $D_{\text{Nd}} = 1.80$
- Distribution ratio of Praseodymium: $D_{\text{Pr}} = 1.20$
The phase volume ratio is adjusted to $V_{org} / V_{aq} = 0.680$.

1. Calculate the extraction factors $E_{\text{Nd}} = D_{\text{Nd}} \left(\frac{V_{org}}{V_{aq}}\right)$ and $E_{\text{Pr}} = D_{\text{Pr}} \left(\frac{V_{org}}{V_{aq}}\right)$.
2. Calculate the fraction $p$ and $q$ in the organic and aqueous phases per stage for both lanthanides.
3. In a multi-stage countercurrent cascade with $N = 12$ theoretical extraction stages, calculate the recovery of neodymium in the organic extract and the residual contamination of praseodymium using Kremser's equation:
   $$\text{Fraction unextracted } q_N = \frac{E - 1}{E^{N+1} - 1}$$""",
            "solution": r"""### Part 1: Extraction Factors
With $V_{org} / V_{aq} = 0.680$:
$$E_{\text{Nd}} = D_{\text{Nd}} \times 0.680 = 1.80 \times 0.680 = 1.224$$
$$E_{\text{Pr}} = D_{\text{Pr}} \times 0.680 = 1.20 \times 0.680 = 0.816$$
Notice the brilliant engineering choice of flow ratio: $E_{\text{Nd}} > 1.0$ (drives Nd into organic phase), while $E_{\text{Pr}} < 1.0$ (keeps Pr in aqueous phase)!

### Part 2: Single-Stage Phase Fractions
- **Neodymium**:
  $$p_{\text{Nd}} = \frac{E_{\text{Nd}}}{1 + E_{\text{Nd}}} = \frac{1.224}{2.224} = 0.5504, \quad q_{\text{Nd}} = 1 - 0.5504 = 0.4496$$
- **Praseodymium**:
  $$p_{\text{Pr}} = \frac{E_{\text{Pr}}}{1 + E_{\text{Pr}}} = \frac{0.816}{1.816} = 0.4493, \quad q_{\text{Pr}} = 1 - 0.4493 = 0.5507$$

### Part 3: Kremser Cascade Performance after N = 12 Stages
- **For Neodymium ($E_{\text{Nd}} = 1.224, N = 12$)**:
  $$E^{N+1} = (1.224)^{13} = 13.91$$
  $$q_{12,\text{Nd}} = \frac{1.224 - 1}{13.91 - 1} = \frac{0.224}{12.91} = 0.01735$$
  Fraction extracted into organic product:
  $$\%E_{\text{Nd}} = (1 - q_{12,\text{Nd}}) \times 100\% = (1 - 0.01735) \times 100\% = 98.26\%$$
- **For Praseodymium ($E_{\text{Pr}} = 0.816, N = 12$)**:
  $$E^{N+1} = (0.816)^{13} = 0.0718$$
  $$q_{12,\text{Pr}} = \frac{0.816 - 1}{0.0718 - 1} = \frac{-0.184}{-0.9282} = 0.1982$$
  Fraction remaining in aqueous raffinette: $19.82\% \implies$ Fraction entering organic: $80.18\%$.
  To reach $> 99.9\%$ purity, a center-feed scrub section is coupled to the cascade, washing out the co-extracted praseodymium with dilute acid."""
        },

        # Unit 9: Problem 9.9
        {
            "id": "prob-9-9",
            "title": "Problem 9.9: Comprehensive Two-Dimensional Gas Chromatography (GCxGC-FID) Petrochemical Analysis",
            "statement": r"""A sample of commercial diesel fuel is analyzed by comprehensive two-dimensional gas chromatography ($\text{GC}\times\text{GC}$-FID):
- **1D Column**: $30.0\text{ m} \times 0.25\text{ mm}$ DB-1 nonpolar column, $N_1 = 120,000$ plates, separating boiling points from $150^\circ\text{C}$ to $360^\circ\text{C}$ over a $45.0\text{ min}$ run.
- **Modulator**: Dual-stage cryogenic loop modulator, modulation period $P_M = 4.00\text{ s}$.
- **2D Column**: $1.5\text{ m} \times 0.10\text{ mm}$ DB-WAX polar column, $N_2 = 6,400$ plates, completing fast separations within $4.00\text{ s}$.

1. Calculate the first-dimension peak capacity $n_{c,1}$ and second-dimension peak capacity $n_{c,2}$ (assuming average peak widths $W_1 = 15.0\text{ s}$ and $W_2 = 120\text{ ms}$).
2. Calculate the total theoretical 2D peak capacity ($n_{c,\text{total}}$).
3. Two co-eluting diesel isomers ($A$ and $B$) have identical boiling points ($t_{R,1} = 22.40\text{ min}$ on 1D) but differ in aromatic ring count. On the second column, they elute at $^2t_{R,A} = 1.20\text{ s}$ and $^2t_{R,B} = 2.80\text{ s}$ with $W_2 = 0.120\text{ s}$.
   Calculate the second-dimension chromatographic resolution ($^2R_s$) between the two isomers.""",
            "solution": r"""### Part 1: Individual Dimension Peak Capacities
- **First Dimension ($^1\text{D}$)**:
  Total gradient run time $t_G = 45.0\text{ min} = 2700\text{ s}$, average peak width $W_1 = 15.0\text{ s}$:
  $$n_{c,1} = 1 + \frac{t_G}{W_1} = 1 + \frac{2700\text{ s}}{15.0\text{ s}} = 1 + 180 = 181\text{ peaks}$$
- **Second Dimension ($^2\text{D}$)**:
  Separation cycle time equals modulation period $P_M = 4.00\text{ s}$, average peak width $W_2 = 120\text{ ms} = 0.120\text{ s}$:
  $$n_{c,2} = 1 + \frac{P_M}{W_2} = 1 + \frac{4.00\text{ s}}{0.120\text{ s}} = 1 + 33.3 = 34.3 \approx 34\text{ peaks}$$

### Part 2: Total Comprehensive Two-Dimensional Peak Capacity
Because the two dimensions operate on orthogonal physical retention mechanisms (boiling point dispersion vs $\pi\text{--}\pi$ polar interaction), peak capacities multiply:
$$n_{c,\text{total}} = n_{c,1} \times n_{c,2} = 181 \times 34 = 6,154\text{ theoretical peaks!}$$
A standard 1D column can resolve fewer than $200$ components; the $\text{GC}\times\text{GC}$ platform expands separation space by over $30$-fold, resolving $> 6,000$ individual petrochemical constituents.

### Part 3: Second-Dimension Resolution Between Isomers
On the secondary column:
$$\Delta ^2t_R = ^2t_{R,B} - ^2t_{R,A} = 2.80\text{ s} - 1.20\text{ s} = 1.60\text{ s}$$
Average baseline peak width $W_2 = 0.120\text{ s}$:
$$^2R_s = \frac{\Delta ^2t_R}{W_2} = \frac{1.60\text{ s}}{0.120\text{ s}} = 13.3$$
While completely unresolved in the primary dimension ($R_s = 0$), the isomers achieve an overwhelming baseline resolution of $^2R_s = 13.3$ in the secondary polar dimension, demonstrating the definitive power of comprehensive multidimensional chromatography."""
        }
    ]

    for i, u in enumerate(units):
        p = prob9_data[i]
        u["problems"].append(p)
        print(f"  Added Problem 9 to {u['title']}")
