# -*- coding: utf-8 -*-
"""
build_analytical_units_4_5_6.py
Builds Units 4, 5, and 6 for Analytical Chemistry (#46):
- Unit 4: Complexometric Titrations: Principles, Ligand Dynamics & Water Hardness
- Unit 5: Advanced Atomic Spectroscopy: AAS, AES, AFS & Atomization Systems
- Unit 6: Ion-Exchange Chromatography: Resins, Equilibria & Analytical Separations
Strictly Zero Course Numbers or Marks. All math in raw strings r\"\"\"...\"\"\".
"""

def get_units_4_5_6():
    units = [
        # =====================================================================
        # UNIT 4
        # =====================================================================
        {
            "id": "unit-4-complexometric-titrations-edta",
            "unitNumber": 4,
            "title": "Unit 4: Complexometric Titrations: Principles, Metal Titrants & Water Hardness",
            "leadSummary": "Comprehensive physical and analytical treatise on chelate coordination thermodynamics, EDTA acid-base polyprotic equilibria, conditional formation constants, metallochromic indicator mechanisms (Eriochrome Black T, Calmagite), auxiliary complexing agents, masking/demasking strategies, and rigorous differential titrations of total, calcium, and magnesium water hardness.",
            "simulations": ["sim_chem_edta_complexometric_titration"],
            "sections": [
                {
                    "id": "sec-4-1",
                    "secNumber": "4.1",
                    "title": "Principles of Chelation: Thermodynamic Driving Forces & The Chelate Effect",
                    "content": r"""Complexometric titrations are based on the formation of stable, soluble, stoichiometric coordination complexes between dissolved metal cations (Lewis acids) and electron-pair donor species known as ligands (Lewis bases):
$$M^{n+}(aq) + L(aq) \rightleftharpoons [ML]^{n+}(aq) \quad K_f = \frac{[ML^{n+}]}{[M^{n+}][L]}$$

### Monodentate Versus Multidentate Ligands
When simple unidentate ligands such as ammonia ($\text{NH}_3$) or cyanide ($\text{CN}^-$) coordinate to a transition metal ion (e.g., $\text{Ni}^{2+}$ or $\text{Cu}^{2+}$), the reaction proceeds through a stepwise sequence of equilibria:
$$M + L \rightleftharpoons ML \quad (K_1)$$
$$ML + L \rightleftharpoons ML_2 \quad (K_2)$$
$$\dots$$
$$ML_{n-1} + L \rightleftharpoons ML_n \quad (K_n)$$
Because the stepwise formation constants $K_1, K_2, \dots, K_n$ typically differ by less than two to three orders of magnitude, multiple partially coordinated intermediate species ($ML, ML_2, ML_3, \dots$) coexist simultaneously over a wide range of reagent additions. Consequently, titration curves with unidentate ligands exhibit diffuse, ill-defined inflections that preclude accurate visual or potentiometric end-point detection.

```
       Monodentate Stepwise Addition vs Hexadentate Chelate Addition
   [M(H₂O)₆]²⁺ + 6 NH₃ ⇌ [M(NH₃)₆]²⁺ + 6 H₂O      (ΔS° ≈ 0, ΔG° moderately favorable)
   [M(H₂O)₆]²⁺ + EDTA⁴⁻ ⇌ [M(EDTA)]²⁻ + 6 H₂O     (ΔS° >> 0, ΔG° highly exergonic!)
   ────────────────────────────────────────────────────────────────────────────────
   1 multidentate ligand displaces 6 water molecules → massive entropy increase!
```

### The Chelate Effect: Thermodynamic Entropy Driving Force
When a multidentate chelating agent containing multiple donor atoms within a single flexible molecular framework coordinates to a metal, it forms one or more stable chelate rings (most stable as 5- or 6-membered rings).
Consider the displacement of six coordinated water molecules from hydrated nickel(II):
1. With six unidentate ammonia ligands:
$$[\text{Ni}(\text{H}_2\text{O})_6]^{2+} + 6\,\text{NH}_3 \rightleftharpoons [\text{Ni}(\text{NH}_3)_6]^{2+} + 6\,\text{H}_2\text{O} \quad (\log \beta_6 = 8.61)$$
Net particle count change: $7 \text{ particles} \to 7 \text{ particles} \implies \Delta S^\circ \approx 0$.
2. With three bidentate ethylenediamine (en) ligands:
$$[\text{Ni}(\text{H}_2\text{O})_6]^{2+} + 3\,\text{en} \rightleftharpoons [\text{Ni}(\text{en})_3]^{2+} + 6\,\text{H}_2\text{O} \quad (\log \beta_3 = 18.28)$$
Net particle count change: $4 \text{ particles} \to 7 \text{ particles} \implies \Delta S^\circ \gg 0$.
3. With one hexadentate $\text{EDTA}^{4-}$ ligand:
$$[\text{Ni}(\text{H}_2\text{O})_6]^{2+} + \text{EDTA}^{4-} \rightleftharpoons [\text{Ni}(\text{EDTA})]^{2-} + 6\,\text{H}_2\text{O} \quad (\log K_f = 18.6)$$
Net particle count change: $2 \text{ particles} \to 7 \text{ particles} \implies \Delta S^\circ = +240\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$.

According to the Gibbs free energy relation:
$$\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$$
The massive positive entropy of liberation ($+T\Delta S^\circ$) drives the free energy deeply negative, boosting stability constants by ten to twelve orders of magnitude! Furthermore, hexadentate ligands bind in an exact **$1:1$ stoichiometric ratio**, yielding a sharp, vertical potentiometric inflection at the equivalence point.""",
                    "simulations": ["sim_chem_edta_complexometric_titration"]
                },
                {
                    "id": "sec-4-2",
                    "secNumber": "4.2",
                    "title": "EDTA Chemistry: Polyprotic Acid Equilibria & Fractional Composition α_Y4-",
                    "content": r"""Ethylenediaminetetraacetic acid (EDTA), denoted chemically as $\text{H}_4\text{Y}$, is a hexadentate ligand possessing six Lewis basic donor atoms: two tertiary amine nitrogens and four carboxylate oxygens.

```
                         Structure of Free EDTA (H₄Y)
                           HOOC-CH₂          CH₂-COOH
                                   \        /
                                    N-CH₂-CH₂-N
                                   /        \
                           HOOC-CH₂          CH₂-COOH
                               (pKa1=0.0, pKa2=1.5, pKa3=2.0, pKa4=2.66, pKa5=6.16, pKa6=10.24)
```

### Acid-Base Equilibria of EDTA
In aqueous solution, EDTA behaves as a hexaprotic acid ($\text{H}_6\text{Y}^{2+}$), where the two amine nitrogens are diprotonated:
$$\text{H}_6\text{Y}^{2+} \xrightleftharpoons{K_{a1}} \text{H}_5\text{Y}^+ + \text{H}^+ \quad (pK_{a1} \approx 0.0)$$
$$\text{H}_5\text{Y}^+ \xrightleftharpoons{K_{a2}} \text{H}_4\text{Y} + \text{H}^+ \quad (pK_{a2} \approx 1.5)$$
$$\text{H}_4\text{Y} \xrightleftharpoons{K_{a3}} \text{H}_3\text{Y}^- + \text{H}^+ \quad (pK_{a3} = 2.00)$$
$$\text{H}_3\text{Y}^- \xrightleftharpoons{K_{a4}} \text{H}_2\text{Y}^{2-} + \text{H}^+ \quad (pK_{a4} = 2.66)$$
$$\text{H}_2\text{Y}^{2-} \xrightleftharpoons{K_{a5}} \text{HY}^{3-} + \text{H}^+ \quad (pK_{a5} = 6.16)$$
$$\text{HY}^{3-} \xrightleftharpoons{K_{a6}} \text{Y}^{4-} + \text{H}^+ \quad (pK_{a6} = 10.24)$$

The fully deprotonated tetra-anion $\text{Y}^{4-}$ is the active chelating species that wraps octahedrally around metal cations.

### Derivation of the Fractional Composition $\alpha_{\text{Y}^{4-}}$
Let $c_T$ (or $C_{\text{EDTA}}$) represent the total analytical concentration of all uncomplexed EDTA species in solution:
$$c_T = [\text{H}_4\text{Y}] + [\text{H}_3\text{Y}^-] + [\text{H}_2\text{Y}^{2-}] + [\text{HY}^{3-}] + [\text{Y}^{4-}]$$
(neglecting negligible traces of $\text{H}_5\text{Y}^+$ and $\text{H}_6\text{Y}^{2+}$ at $\text{pH} > 2$).
The fraction present as the active tetra-anion $\alpha_{\text{Y}^{4-}}$ is defined as:
$$\alpha_{\text{Y}^{4-}} = \frac{[\text{Y}^{4-}]}{c_T}$$

Expressing each protonated species in terms of $[\text{Y}^{4-}]$, $[\text{H}^+]$, and the acid dissociation constants ($K_1, K_2, K_3, K_4$ representing $K_{a3}, K_{a4}, K_{a5}, K_{a6}$):
$$[\text{HY}^{3-}] = \frac{[\text{H}^+][\text{Y}^{4-}]}{K_4}$$
$$[\text{H}_2\text{Y}^{2-}] = \frac{[\text{H}^+]^2 [\text{Y}^{4-}]}{K_3 K_4}$$
$$[\text{H}_3\text{Y}^-] = \frac{[\text{H}^+]^3 [\text{Y}^{4-}]}{K_2 K_3 K_4}$$
$$[\text{H}_4\text{Y}] = \frac{[\text{H}^+]^4 [\text{Y}^{4-}]}{K_1 K_2 K_3 K_4}$$

Substituting these expressions into $c_T$ and factoring out $[\text{Y}^{4-}]$ yields the exact expression:
$$\alpha_{\text{Y}^{4-}} = \frac{K_1 K_2 K_3 K_4}{[\text{H}^+]^4 + K_1 [\text{H}^+]^3 + K_1 K_2 [\text{H}^+]^2 + K_1 K_2 K_3 [\text{H}^+] + K_1 K_2 K_3 K_4}$$

| Solution pH | Fractional Abundance $\alpha_{\text{Y}^{4-}}$ | Predominant Uncomplexed Species |
| :---: | :---: | :---: |
| **2.0** | $3.7 \times 10^{-14}$ | $\text{H}_3\text{Y}^-$ ($pK_a = 2.00$) |
| **4.0** | $3.6 \times 10^{-9}$ | $\text{H}_2\text{Y}^{2-}$ |
| **6.0** | $2.2 \times 10^{-5}$ | $\text{H}_2\text{Y}^{2-} / \text{HY}^{3-}$ |
| **8.0** | $5.4 \times 10^{-3}$ | $\text{HY}^{3-}$ |
| **10.0** | **$0.35$** | $\text{HY}^{3-} \approx \text{Y}^{4-}$ |
| **12.0** | **$0.98$** | $\text{Y}^{4-}$ ($98\%$ free tetra-anion) |

At acidic pH values ($\text{pH} \le 4$), $\alpha_{\text{Y}^{4-}}$ collapses to near-zero ($10^{-9}\text{ to }10^{-14}$) because hydronium ions compete aggressively for carboxylate and amine sites. Consequently, maintaining alkaline buffer conditions is mandatory for chelating alkaline-earth metals.""",
                    "simulations": []
                },
                {
                    "id": "sec-4-3",
                    "secNumber": "4.3",
                    "title": "Conditional Formation Constants & Auxiliary Complexing Agents",
                    "content": r"""The thermodynamic formation constant $K_f$ describes the binding of the free tetra-anion $\text{Y}^{4-}$ to a metal cation:
$$M^{n+} + \text{Y}^{4-} \rightleftharpoons [MY]^{(n-4)} \quad K_f = \frac{[MY^{(n-4)}]}{[M^{n+}][\text{Y}^{4-}]}$$

### The Conditional Formation Constant ($K'_f$)
Because the true equilibrium concentration of free $[\text{Y}^{4-}]$ is only a tiny fraction of the total uncomplexed EDTA ($[\text{Y}^{4-}] = \alpha_{\text{Y}^{4-}} c_T$), we substitute this relation into the equilibrium expression:
$$K_f = \frac{[MY^{(n-4)}]}{[M^{n+}](\alpha_{\text{Y}^{4-}} c_T)} \implies K_f \cdot \alpha_{\text{Y}^{4-}} = \frac{[MY^{(n-4)}]}{[M^{n+}] c_T}$$
We define the **pH-Conditional Formation Constant** $K'_f$:
$$K'_f = K_f \cdot \alpha_{\text{Y}^{4-}} = \frac{[MY^{(n-4)}]}{[M^{n+}] c_T}$$
The conditional constant $K'_f$ describes the effective thermodynamic stability of the complex at a specified, constant pH.

```
       Effect of pH on Conditional Stability Constants
   log K'f
    ▲
 25 ┼──────────────────────────────────── Fe³⁺ (log Kf = 25.1)
    │                       _.-'
 20 ┼──────────────────_.-''───────────── Zn²⁺ (log Kf = 16.5)
    │             _.-''
 15 ┼────────_.-''─────────────────────── Ca²⁺ (log Kf = 10.65)
    │   _.-''
 10 ┼─''───────────────────────────────── Mg²⁺ (log Kf = 8.79)
    │  ══════════════════════════════════ Minimum threshold (log K'f ≥ 8.0)
  5 ┼
    └──┬─────┬─────┬─────┬─────┬─────┬──► pH
       2     4     6     8    10    12
```

### Minimum pH for Quantitative EDTA Titrations
For a titration to yield a sharp, well-defined end point (accuracy within $\pm 0.1\%$), the conditional formation constant must satisfy:
$$K'_f \ge 10^8 \implies \log K'_f \ge 8.0$$
- $\text{Fe}^{3+}$ ($\log K_f = 25.1$): Quantitatively titrated at $\text{pH } \ge 1.5$.
- $\text{Zn}^{2+}, \text{Cu}^{2+}, \text{Pb}^{2+}$ ($\log K_f \approx 16\text{--}18$): Quantitatively titrated at $\text{pH } \ge 4.0\text{--}5.0$.
- $\text{Ca}^{2+}$ ($\log K_f = 10.65$): Requires $\text{pH } \ge 7.5\text{--}8.0$.
- $\text{Mg}^{2+}$ ($\log K_f = 8.79$): Requires $\text{pH } \ge 9.5\text{--}10.0$.
This mathematical hierarchy forms the foundation of **selective masking via pH control**: $\text{Fe}^{3+}$ can be titrated in the presence of $\text{Ca}^{2+}$ and $\text{Mg}^{2+}$ at $\text{pH } 2.0$ without interference.

### Auxiliary Complexing Agents ($\alpha_M$)
Many transition metal cations ($\text{Zn}^{2+}, \text{Cu}^{2+}, \text{Ni}^{2+}$) precipitate as insoluble metal hydroxides in alkaline solution ($\text{pH } 9\text{--}10$) where EDTA is active. To keep them in solution, an **auxiliary complexing agent** (such as ammonia, tartrate, or citrate) is added.
Ammonia forms soluble amine complexes with zinc:
$$\text{Zn}^{2+} + i\,\text{NH}_3 \rightleftharpoons [\text{Zn}(\text{NH}_3)_i]^{2+} \quad (\beta_i)$$
The total uncomplexed zinc concentration is:
$$c_M = [\text{Zn}^{2+}] + [\text{Zn}(\text{NH}_3)^{2+}] + \dots + [\text{Zn}(\text{NH}_3)_4^{2-}]$$
The fraction of free, uncomplexed metal ion is:
$$\alpha_M = \frac{[\text{Zn}^{2+}]}{c_M} = \frac{1}{1 + \sum_{i=1}^4 \beta_i [\text{NH}_3]^i}$$
Incorporating both pH and auxiliary ligand effects yields the **Fully Adjusted Conditional Constant** $K''_f$:
$$K''_f = K_f \cdot \alpha_{\text{Y}^{4-}} \cdot \alpha_M = \frac{[MY^{(n-4)}]}{c_M \cdot c_T}$$""",
                    "simulations": []
                },
                {
                    "id": "sec-4-4",
                    "secNumber": "4.4",
                    "title": "Derivation of Rigorous EDTA Titration Curves (pM vs Volume)",
                    "content": r"""An EDTA titration curve plots the negative logarithm of the free metal ion concentration, $pM = -\log_{10}[M^{n+}]$, as a function of the titrant volume $V_{\text{EDTA}}$.

### Mathematical Derivation of the Three Titration Zones
Consider the titration of $V_0\text{ mL}$ of $C_{M,0}\text{ M}$ metal ion $M^{n+}$ with $C_{\text{EDTA}}\text{ M}$ standard EDTA at buffered pH (known $\alpha_{\text{Y}^{4-}}$ and $K'_f$).
The equivalence point volume $V_{\text{eq}}$ is:
$$V_{\text{eq}} = \frac{V_0 \cdot C_{M,0}}{C_{\text{EDTA}}}$$

#### 1. Region 1: Pre-Equivalence Point ($0 \le V < V_{\text{eq}}$)
Free metal ion is in stoichiometric excess. The uncomplexed $[M^{n+}]$ is governed by remaining unreacted analyte:
$$[M^{n+}] \approx \frac{C_{M,0} V_0 - C_{\text{EDTA}} V}{V_0 + V}$$
$$pM = -\log_{10}[M^{n+}]$$
The dissociation of $[MY]$ contributes a negligible amount of free metal prior to the equivalence point.

#### 2. Region 2: The Equivalence Point ($V = V_{\text{eq}}$)
All metal has been converted to the chelate $[MY]^{(n-4)}$. The analytical concentration of the chelate is:
$$c_{MY} = \frac{C_{M,0} V_0}{V_0 + V_{\text{eq}}}$$
Free metal ion arises solely from the minor dissociation of the complex:
$$[MY]^{(n-4)} \rightleftharpoons M^{n+} + \text{EDTA}'$$
At stoichiometry, $[M^{n+}] = c_T$. Substituting into the conditional constant:
$$K'_f = \frac{c_{MY} - [M^{n+}]}{[M^{n+}] \cdot c_T} \approx \frac{c_{MY}}{[M^{n+}]^2}$$
Solving for $[M^{n+}]$:
$$[M^{n+}] = \sqrt{\frac{c_{MY}}{K'_f}}$$
$$pM_{\text{eq}} = -\log_{10}\left(\sqrt{\frac{c_{MY}}{K'_f}}\right) = \frac{1}{2}\left(\log_{10} K'_f - \log_{10} c_{MY}\right)$$
This fundamental equation shows that the height of the equivalence point step increases with higher conditional stability constants $K'_f$.

#### 3. Region 3: Post-Equivalence Point ($V > V_{\text{eq}}$)
EDTA is in stoichiometric excess. The concentration of uncomplexed EDTA is:
$$c_T = \frac{C_{\text{EDTA}} (V - V_{\text{eq}})}{V_0 + V}$$
The chelate concentration is:
$$c_{MY} = \frac{C_{M,0} V_0}{V_0 + V}$$
Rearranging the conditional constant:
$$[M^{n+}] = \frac{c_{MY}}{K'_f \cdot c_T} = \frac{C_{M,0} V_0}{K'_f \cdot C_{\text{EDTA}} (V - V_{\text{eq}})}$$
$$pM = \log_{10} K'_f + \log_{10}\left(\frac{C_{\text{EDTA}} (V - V_{\text{eq}})}{C_{M,0} V_0}\right)$$""",
                    "simulations": []
                },
                {
                    "id": "sec-4-5",
                    "secNumber": "4.5",
                    "title": "Metallochromic Indicators: Eriochrome Black T, Calmagite & Indicator Thresholds",
                    "content": r"""End points in complexometric titrations are detected using **metallochromic indicators**—organic dyes that function as chelating agents themselves, displaying contrasting optical absorption spectra in their free versus metal-bound forms.

### Eriochrome Black T (EBT) Mechanism
Eriochrome Black T is an azo dye possessing sulfonic and phenolic groups. It functions as a diprotic acid-base indicator:
$$\text{H}_2\text{In}^- \text{ (Wine Red)} \xrightleftharpoons{pK_{a1}=6.3} \text{HIn}^{2-} \text{ (Sky Blue)} \xrightleftharpoons{pK_{a2}=11.5} \text{In}^{3-} \text{ (Orange)}$$

```
                   Eriochrome Black T Indicator Color Shift
        pH < 6.3                    pH 7.0 - 11.0                   pH > 11.5
        H₂In⁻                        HIn²⁻                         In³⁻
       Wine Red                    Sky Blue                       Orange
          │                            │                             │
          └─────────────┬──────────────┴──────────────┬──────────────┘
                        │ + M²⁺ (e.g., Mg²⁺, Ca²⁺)    │
                        ▼                             ▼
                   [M-In]⁻ Chelate              [M-In]⁻ Chelate
                      Wine Red                     Wine Red
   ──────────────────────────────────────────────────────────────────────────
   At pH 10:  [M-In]⁻ (Wine Red) + EDTA⁴⁻ ⇌ [M-EDTA]²⁻ + HIn²⁻ (Sky Blue)
```

In the standard buffered analytical range of $\text{pH } 10.0$, uncomplexed EBT exists predominantly as the blue species $\text{HIn}^{2-}$.
When added to a solution containing $\text{Mg}^{2+}$ or $\text{Ca}^{2+}$, a portion of the metal coordinates with the indicator to form a wine-red chelate:
$$\text{Mg}^{2+} + \text{HIn}^{2-} \text{ (Sky Blue)} \rightleftharpoons [\text{MgIn}]^- \text{ (Wine Red)} + \text{H}^+$$

### Thermodynamic End-Point Displacement
As EDTA titrant is added, it complexes all free metal ions first. At the equivalence point, the titrant displaces the indicator from the metal-dye complex because $K'_f(\text{M-EDTA}) \gg K'_f(\text{M-In})$:
$$[\text{MgIn}]^- \text{ (Wine Red)} + \text{EDTA}' \to [\text{Mg(EDTA)}]^{2-} + \text{HIn}^{2-} \text{ (Sky Blue)}$$
The solution turns sharply from **wine red to clear sky blue**.

### Mathematical Stability Threshold for Metallochromic Indicators
For a crisp end point with negligible titrimetric error:
1. The metal-indicator complex must be sufficiently stable to prevent premature dissociation:
$$\log K'_{\text{M-In}} \ge 4.0$$
2. The metal-EDTA chelate must be significantly more stable than the metal-indicator complex so that EDTA can liberate the dye quantitatively:
$$\log K'_f(\text{M-EDTA}) - \log K'_{\text{M-In}} \ge 2.0$$
If $K'_{\text{M-In}} > K'_f(\text{M-EDTA})$, the indicator is **blocked**—EDTA cannot displace the metal, and no color change occurs. This occurs when trace $\text{Cu}^{2+}, \text{Ni}^{2+}, \text{Fe}^{3+}$, or $\text{Co}^{2+}$ block EBT; these interferents must be masked with potassium cyanide prior to titration.""",
                    "simulations": []
                },
                {
                    "id": "sec-4-6",
                    "secNumber": "4.6",
                    "title": "Masking & Demasking Strategies in Complexometry",
                    "content": r"""When an analytical sample contains a mixture of multiple polyvalent metal cations, selective titration of a single analyte requires suppressing the reactivity of interfering metals. This is accomplished via **masking**.

### Masking Mechanisms
A **masking agent** is a reagent that prevents an interfering chemical species from reacting with EDTA without physically removing it via phase separation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       Common Analytical Masking Reagents                    │
├───────────────────────┬───────────────────────┬─────────────────────────────┤
│ Masking Reagent       │ Masked Interferents   │ Chemical Mechanism          │
├───────────────────────┼───────────────────────┼─────────────────────────────┤
│ Potassium Cyanide     │ Fe²⁺, Co²⁺, Ni²⁺,     │ Forms inert cyano complexes │
│ (KCN)                 │ Cu²⁺, Zn²⁺, Cd²⁺      │ [Ni(CN)₄]²⁻, [Fe(CN)₆]⁴⁻    │
├───────────────────────┼───────────────────────┼─────────────────────────────┤
│ Ammonium Fluoride     │ Fe³⁺, Al³⁺, Ti⁴⁺,     │ Forms stable fluoro adducts │
│ (NH₄F)                │ Be²⁺                  │ [FeF₆]³⁻, [AlF₆]³⁻          │
├───────────────────────┼───────────────────────┼─────────────────────────────┤
│ Triethanolamine (TEA) │ Fe³⁺, Al³⁺, Mn²⁺      │ Forms soluble alkanolamine  │
│                       │                       │ chelates at pH 10-12        │
├───────────────────────┼───────────────────────┼─────────────────────────────┤
│ Ascorbic Acid /       │ Fe³⁺ → Fe²⁺           │ Selective redox reduction   │
│ Hydroxylamine         │                       │ to non-interfering state    │
├───────────────────────┼───────────────────────┼─────────────────────────────┤
│ BAL (Dimercaprol)     │ Hg²⁺, Bi³⁺, Pb²⁺, As  │ Strong bis-thiol chelation  │
└───────────────────────┴───────────────────────┴─────────────────────────────┘
```

### Demasking
**Demasking** is the process by which a masked substance is liberated from its complex to allow subsequent quantitative titration.
*Example: Stepwise Titration of Magnesium and Zinc*:
1. An aliquot containing $\text{Mg}^{2+}$ and $\text{Zn}^{2+}$ is buffered to $\text{pH } 10$.
2. Potassium cyanide ($\text{KCN}$) is added: $\text{Zn}^{2+}$ forms the stable tetracyanozincate complex $[\text{Zn(CN)}_4]^{2-}$ ($\log \beta_4 = 16.7$). Magnesium does not coordinate cyanide.
3. The free $\text{Mg}^{2+}$ is titrated with standard EDTA.
4. Formaldehyde or chloral hydrate is added to demask zinc:
$$[\text{Zn(CN)}_4]^{2-} + 4\,\text{HCHO} + 4\,\text{H}_2\text{O} \to \text{Zn}^{2+} + 4\,\text{HOCH}_2\text{CN} + 4\,\text{OH}^-$$
Formaldehyde reacts irreversibly with cyanide to form formaldehyde cyanohydrin. The liberated $\text{Zn}^{2+}$ is then titrated with EDTA.""",
                    "simulations": []
                },
                {
                    "id": "sec-4-7",
                    "secNumber": "4.7",
                    "title": "Determination of Water Hardness: Ca2+ vs Mg2+ Differential Titration",
                    "content": r"""Water hardness is a measure of the capacity of water to precipitate soap, driven primarily by dissolved polyvalent mineral cations, predominantly calcium ($\text{Ca}^{2+}$) and magnesium ($\text{Mg}^{2+}$). Hardness is universally reported in terms of equivalent concentration of calcium carbonate ($\text{mg}\cdot\text{L}^{-1}\text{ CaCO}_3$ or $\text{ppm CaCO}_3$).

### Classification of Water Hardness
1. **Temporary (Carbonate) Hardness**: Caused by dissolved calcium and magnesium hydrogen carbonates ($\text{Ca(HCO}_3)_2, \text{Mg(HCO}_3)_2$). Expelled by boiling, precipitating scale:
$$\text{Ca}^{2+} + 2\,\text{HCO}_3^- \xrightarrow{\Delta} \text{CaCO}_3(s)\downarrow + \text{CO}_2\uparrow + \text{H}_2\text{O}$$
2. **Permanent (Non-Carbonate) Hardness**: Caused by sulfates, chlorides, and nitrates of calcium and magnesium ($\text{CaSO}_4, \text{CaCl}_2, \text{MgSO}_4$). Cannot be removed by boiling.
3. **Total Hardness**: The sum of temporary and permanent hardness ($[\text{Ca}^{2+}] + [\text{Mg}^{2+}]$).

### The Classical Two-Step Differential Titration Protocol

#### Step 1: Determination of Total Hardness ($\text{Ca}^{2+} + \text{Mg}^{2+}$)
- A water aliquot is buffered to $\mathbf{\text{pH } 10.0}$ using an ammonium chloride/ammonia buffer ($\text{NH}_4\text{Cl} / \text{NH}_3$).
- Eriochrome Black T indicator is added (solution turns wine red).
- Titration with standardized $0.01\text{ M}$ disodium EDTA ($\text{Na}_2\text{H}_2\text{Y}$) complexes both $\text{Ca}^{2+}$ and $\text{Mg}^{2+}$:
$$\text{Ca}^{2+} + \text{H}_2\text{Y}^{2-} \to [\text{CaY}]^{2-} + 2\,\text{H}^+$$
$$\text{Mg}^{2+} + \text{H}_2\text{Y}^{2-} \to [\text{MgY}]^{2-} + 2\,\text{H}^+$$
- At the end point ($V_1$), EDTA extracts $\text{Mg}^{2+}$ from the wine-red $[\text{MgIn}]^-$ complex, releasing free blue indicator:
$$[\text{MgIn}]^- \text{ (Wine Red)} + \text{EDTA} \to [\text{Mg(EDTA)}]^{2-} + \text{HIn}^{2-} \text{ (Sky Blue)}$$
- Total hardness calculation:
$$\text{Total Hardness (mg/L CaCO}_3) = \frac{V_1 \cdot M_{\text{EDTA}} \cdot 100.0867\text{ g/mol}}{V_{\text{water sample}}\text{ (L)}}$$

#### Step 2: Selective Determination of Calcium Hardness Alone
- A second identical water aliquot is adjusted to $\mathbf{\text{pH } 12.0\text{--}13.0}$ using concentrated sodium hydroxide ($\text{NaOH}$).
- At $\text{pH } 12.5$, magnesium precipitates quantitatively as gelatinous magnesium hydroxide:
$$\text{Mg}^{2+} + 2\,\text{OH}^- \to \text{Mg(OH)}_2(s)\downarrow \quad (K_{\text{sp}} = 5.6 \times 10^{-12})$$
- Calcium remains soluble ($K_{\text{sp}}(\text{Ca(OH)}_2) = 5.5 \times 10^{-6}$).
- Hydroxynaphthol blue or **Murexide** (ammonium purpurate) indicator is added (solution turns salmon pink/red with calcium).
- Titration with standard EDTA complexs only calcium until the end point ($V_2$), where Murexide turns purple-violet:
$$\text{Calcium Hardness (mg/L CaCO}_3) = \frac{V_2 \cdot M_{\text{EDTA}} \cdot 100.0867}{V_{\text{water sample}}}$$

#### Step 3: Calculation of Magnesium Hardness by Difference
$$\text{Magnesium Hardness (mg/L CaCO}_3) = \text{Total Hardness} - \text{Calcium Hardness}$$
$$\text{Actual } [\text{Mg}^{2+}]\text{ (mg/L)} = \text{Magnesium Hardness} \times \left(\frac{M_{\text{Mg}}}{M_{\text{CaCO}_3}}\right) = \text{Magnesium Hardness} \times 0.2430$$""",
                    "simulations": []
                }
            ],
            "problems": [
                {
                    "id": "prob-4-1",
                    "problemNumber": "4.1",
                    "title": "Fractional Composition α_Y4- and Conditional Formation Constant of Calcium-EDTA",
                    "difficulty": "Foundational",
                    "statement": r"""The absolute thermodynamic formation constant for the calcium-EDTA chelate at $25^\circ\text{C}$ is:
$$K_f = 5.0 \times 10^{10} \quad (\log K_f = 10.65)$$
Given the four successive acid dissociation constants for EDTA ($\text{H}_4\text{Y}$):
$$K_1 = 1.02 \times 10^{-2}, \quad K_2 = 2.14 \times 10^{-3}, \quad K_3 = 6.92 \times 10^{-7}, \quad K_4 = 5.50 \times 10^{-11}$$
1. Calculate the fractional composition $\alpha_{\text{Y}^{4-}}$ at $\text{pH } 10.00$ ($[\text{H}^+] = 1.0 \times 10^{-10}\text{ M}$).
2. Calculate the conditional formation constant $K'_f$ for $[\text{Ca(EDTA)}]^{2-}$ at $\text{pH } 10.00$.
3. Repeat the calculation of $\alpha_{\text{Y}^{4-}}$ and $K'_f$ at $\text{pH } 4.00$, and explain why calcium cannot be accurately titrated at $\text{pH } 4.00$.""",
                    "solution": r"""### Step 1: Calculation of $\alpha_{\text{Y}^{4-}}$ at pH 10.00
Let $[\text{H}^+] = 1.0 \times 10^{-10}\text{ M}$.
The denominator of $\alpha_{\text{Y}^{4-}}$ is:
$$D = [\text{H}^+]^4 + K_1 [\text{H}^+]^3 + K_1 K_2 [\text{H}^+]^2 + K_1 K_2 K_3 [\text{H}^+] + K_1 K_2 K_3 K_4$$
Compute the terms:
1. $[\text{H}^+]^4 = (10^{-10})^4 = 10^{-40}$ (negligible)
2. $K_1 [\text{H}^+]^3 = (1.02 \times 10^{-2})(10^{-30}) = 1.02 \times 10^{-32}$ (negligible)
3. $K_1 K_2 [\text{H}^+]^2 = (1.02 \times 10^{-2})(2.14 \times 10^{-3})(10^{-20}) = 2.18 \times 10^{-25}$ (negligible)
4. $K_1 K_2 K_3 [\text{H}^+] = (2.18 \times 10^{-5})(6.92 \times 10^{-7})(10^{-10}) = 1.51 \times 10^{-21}$
5. $K_1 K_2 K_3 K_4 = (1.51 \times 10^{-11})(5.50 \times 10^{-11}) = 8.305 \times 10^{-22}$

The denominator is dominated by the last two terms:
$$D = 1.51 \times 10^{-21} + 8.305 \times 10^{-22} = 2.3405 \times 10^{-21}$$
The fractional composition is:
$$\alpha_{\text{Y}^{4-}} = \frac{K_1 K_2 K_3 K_4}{D} = \frac{8.305 \times 10^{-22}}{2.3405 \times 10^{-21}} = \mathbf{0.3548 \approx 0.35}$$

### Step 2: Conditional Constant $K'_f$ at pH 10.00
$$K'_f = K_f \cdot \alpha_{\text{Y}^{4-}} = (5.0 \times 10^{10}) \times 0.3548 = \mathbf{1.77 \times 10^{10}} \quad (\log K'_f = 10.25)$$
Because $\log K'_f = 10.25 \gg 8.0$, calcium forms an exceptionally stable complex, and the titration at $\text{pH } 10$ will produce a sharp, vertical potentiometric and indicator inflection.

### Step 3: Calculation at pH 4.00
At $\text{pH } 4.00$ ($[\text{H}^+] = 1.0 \times 10^{-4}\text{ M}$):
Term 3 ($K_1 K_2 [\text{H}^+]^2$) dominates:
$$K_1 K_2 [\text{H}^+]^2 = (2.18 \times 10^{-5})(10^{-8}) = 2.18 \times 10^{-13}$$
The numerator remains $K_1 K_2 K_3 K_4 = 8.305 \times 10^{-22}$.
$$\alpha_{\text{Y}^{4-}} = \frac{8.305 \times 10^{-22}}{2.29 \times 10^{-13}} = \mathbf{3.63 \times 10^{-9}}$$
The conditional constant at $\text{pH } 4.00$ collapses to:
$$K'_f = (5.0 \times 10^{10}) \times (3.63 \times 10^{-9}) = \mathbf{181.5} \quad (\log K'_f = 2.26)$$
*Conclusion*: Because $\log K'_f = 2.26 \ll 8.0$, calcium binding is virtually nonexistent at $\text{pH } 4.00$. Protonation completely disables EDTA from complexing $\text{Ca}^{2+}$.""",
                    "hints": ["Calculate the product K1*K2*K3*K4 first.", "At pH 10, only the [H+] and constant terms in the denominator are non-negligible."]
                },
                {
                    "id": "prob-4-2",
                    "problemNumber": "4.2",
                    "title": "Complete Mathematical Derivation of an EDTA Titration Curve",
                    "difficulty": "Honors Problem",
                    "statement": r"""A $50.0\text{ mL}$ aliquot of $0.0100\text{ M }\text{Mg}^{2+}$ is titrated with $0.0100\text{ M}$ standard EDTA buffered at $\text{pH } 10.00$ ($\alpha_{\text{Y}^{4-}} = 0.35$).
The absolute formation constant of $[\text{Mg(EDTA)}]^{2-}$ is $K_f = 6.2 \times 10^8$ ($\log K_f = 8.79$).

Calculate the exact value of $p\text{Mg} = -\log_{10}[\text{Mg}^{2+}]$ at the following titrant additions:
1. $V = 0.0\text{ mL}$ (Initial point)
2. $V = 25.0\text{ mL}$ (Halfway to equivalence)
3. $V = 49.9\text{ mL}$ ($0.1\text{ mL}$ before equivalence)
4. $V = 50.0\text{ mL}$ (Exact stoichiometric equivalence point)
5. $V = 50.1\text{ mL}$ ($0.1\text{ mL}$ after equivalence)
6. $V = 60.0\text{ mL}$ ($10.0\text{ mL}$ excess EDTA)""",
                    "solution": r"""### Step 1: Pre-Calculations
1. Equivalence point volume:
$$V_{\text{eq}} = \frac{(50.0\text{ mL})(0.0100\text{ M})}{0.0100\text{ M}} = 50.0\text{ mL}$$
2. Conditional formation constant:
$$K'_f = K_f \cdot \alpha_{\text{Y}^{4-}} = (6.2 \times 10^8) \times 0.35 = \mathbf{2.17 \times 10^8} \quad (\log K'_f = 8.336)$$

### Point 1: V = 0.0 mL
$$[\text{Mg}^{2+}] = 0.0100\text{ M} \implies p\text{Mg} = -\log_{10}(0.0100) = \mathbf{2.00}$$

### Point 2: V = 25.0 mL
Pre-equivalence point:
$$[\text{Mg}^{2+}] = \frac{(50.0\text{ mL})(0.0100\text{ M}) - (25.0\text{ mL})(0.0100\text{ M})}{50.0 + 25.0} = \frac{0.500 - 0.250}{75.0} = \frac{0.250}{75.0} = 3.333 \times 10^{-3}\text{ M}$$
$$p\text{Mg} = -\log_{10}(3.333 \times 10^{-3}) = \mathbf{2.48}$$

### Point 3: V = 49.9 mL
$$[\text{Mg}^{2+}] = \frac{(50.0 \times 0.0100) - (49.9 \times 0.0100)}{50.0 + 49.9} = \frac{0.0010\text{ mmol}}{99.9\text{ mL}} = 1.001 \times 10^{-5}\text{ M}$$
$$p\text{Mg} = -\log_{10}(1.001 \times 10^{-5}) = \mathbf{5.00}$$

### Point 4: V = 50.0 mL (Equivalence Point)
Total volume = $100.0\text{ mL}$.
Concentration of chelate formed:
$$c_{\text{MgY}} = \frac{(50.0)(0.0100)}{100.0} = 5.00 \times 10^{-3}\text{ M}$$
From equilibrium $[\text{MgY}] \rightleftharpoons \text{Mg}^{2+} + \text{EDTA}'$, where $[\text{Mg}^{2+}] = c_T$:
$$K'_f = \frac{c_{\text{MgY}}}{[\text{Mg}^{2+}]^2} \implies [\text{Mg}^{2+}] = \sqrt{\frac{c_{\text{MgY}}}{K'_f}} = \sqrt{\frac{5.00 \times 10^{-3}}{2.17 \times 10^8}} = \sqrt{2.304 \times 10^{-11}} = 4.80 \times 10^{-6}\text{ M}$$
$$p\text{Mg} = -\log_{10}(4.80 \times 10^{-6}) = \mathbf{5.32}$$

### Point 5: V = 50.1 mL (Post-Equivalence)
Total volume = $100.1\text{ mL}$.
Excess uncomplexed EDTA:
$$c_T = \frac{(50.1 - 50.0) \times 0.0100}{100.1} = \frac{0.0010\text{ mmol}}{100.1\text{ mL}} = 9.99 \times 10^{-6}\text{ M}$$
Chelate concentration:
$$c_{\text{MgY}} = \frac{0.500\text{ mmol}}{100.1\text{ mL}} = 4.995 \times 10^{-3}\text{ M}$$
From conditional constant:
$$[\text{Mg}^{2+}] = \frac{c_{\text{MgY}}}{K'_f \cdot c_T} = \frac{4.995 \times 10^{-3}}{(2.17 \times 10^8) \times (9.99 \times 10^{-6})} = \frac{4.995 \times 10^{-3}}{2167.8} = 2.304 \times 10^{-6}\text{ M}$$
$$p\text{Mg} = -\log_{10}(2.304 \times 10^{-6}) = \mathbf{5.64}$$

### Point 6: V = 60.0 mL (Excess EDTA)
Total volume = $110.0\text{ mL}$.
$$c_T = \frac{(60.0 - 50.0) \times 0.0100}{110.0} = \frac{0.100\text{ mmol}}{110.0\text{ mL}} = 9.091 \times 10^{-4}\text{ M}$$
$$c_{\text{MgY}} = \frac{0.500\text{ mmol}}{110.0\text{ mL}} = 4.545 \times 10^{-3}\text{ M}$$
$$[\text{Mg}^{2+}] = \frac{4.545 \times 10^{-3}}{(2.17 \times 10^8) \times (9.091 \times 10^{-4})} = \frac{4.545 \times 10^{-3}}{1.9727 \times 10^5} = 2.304 \times 10^{-8}\text{ M}$$
$$p\text{Mg} = -\log_{10}(2.304 \times 10^{-8}) = \mathbf{7.64}$$

Notice the rapid increase in $p\text{Mg}$ from $2.00$ up to $7.64$ across the titration coordinate.""",
                    "hints": ["At equivalence point, [M] = sqrt(c_MY / K'_f).", "Post-equivalence, [M] = c_MY / (K'_f * c_T)."]
                },
                {
                    "id": "prob-4-3",
                    "problemNumber": "4.3",
                    "title": "Determination of Total, Calcium, and Magnesium Water Hardness",
                    "difficulty": "Intermediate",
                    "statement": r"""A $100.0\text{ mL}$ aliquot of municipal drinking water is analyzed for hardness:
- **Portion 1**: Buffered at $\text{pH } 10.0$ with $\text{NH}_3/\text{NH}_4\text{Cl}$. Eriochrome Black T indicator is added. The solution consumes $28.40\text{ mL}$ of $0.01050\text{ M}$ EDTA to reach the sky-blue end point.
- **Portion 2**: A second $100.0\text{ mL}$ aliquot is adjusted to $\text{pH } 12.5$ with $50\text{ wt}\% \ \text{NaOH}$ to precipitate magnesium hydroxide. Murexide indicator is added. The solution consumes $19.20\text{ mL}$ of the same $0.01050\text{ M}$ EDTA to reach the purple-violet end point.

Calculate:
1. The **Total Hardness** in $\text{mg}\cdot\text{L}^{-1}\text{ CaCO}_3$.
2. The **Calcium Hardness** in $\text{mg}\cdot\text{L}^{-1}\text{ CaCO}_3$ and the actual concentration of $\text{Ca}^{2+}$ in $\text{mg}\cdot\text{L}^{-1}$.
3. The **Magnesium Hardness** in $\text{mg}\cdot\text{L}^{-1}\text{ CaCO}_3$ and the actual concentration of $\text{Mg}^{2+}$ in $\text{mg}\cdot\text{L}^{-1}$.
(Molar masses: $\text{CaCO}_3 = 100.087, \text{Ca} = 40.078, \text{Mg} = 24.305\text{ g}\cdot\text{mol}^{-1}$).""",
                    "solution": r"""### Step 1: Total Hardness Calculation (Portion 1)
Total millimoles of $(\text{Ca}^{2+} + \text{Mg}^{2+})$:
$$n_{\text{total}} = V_1 \cdot M_{\text{EDTA}} = 28.40\text{ mL} \times 0.01050\text{ mmol/mL} = 0.2982\text{ mmol}$$
Mass of equivalent $\text{CaCO}_3$:
$$m_{\text{CaCO}_3} = 0.2982\text{ mmol} \times 100.087\text{ mg/mmol} = 29.846\text{ mg}$$
Sample volume = $100.0\text{ mL} = 0.1000\text{ L}$.
$$\text{Total Hardness} = \frac{29.846\text{ mg}}{0.1000\text{ L}} = \mathbf{298.46\,\text{mg/L CaCO}_3}$$

### Step 2: Calcium Hardness (Portion 2)
Millimoles of $\text{Ca}^{2+}$ alone:
$$n_{\text{Ca}} = V_2 \cdot M_{\text{EDTA}} = 19.20\text{ mL} \times 0.01050\text{ mmol/mL} = 0.2016\text{ mmol}$$
Mass of equivalent $\text{CaCO}_3$:
$$m_{\text{CaCO}_3, \text{Ca}} = 0.2016\text{ mmol} \times 100.087\text{ mg/mmol} = 20.178\text{ mg}$$
$$\text{Calcium Hardness} = \frac{20.178\text{ mg}}{0.1000\text{ L}} = \mathbf{201.78\,\text{mg/L CaCO}_3}$$

Actual concentration of $\text{Ca}^{2+}$:
$$[\text{Ca}^{2+}] = \frac{0.2016\text{ mmol} \times 40.078\text{ mg/mmol}}{0.1000\text{ L}} = \frac{8.0797\text{ mg}}{0.1000\text{ L}} = \mathbf{80.80\,\text{mg/L Ca}^{2+}}$$

### Step 3: Magnesium Hardness by Difference
$$\text{Magnesium Hardness} = \text{Total Hardness} - \text{Calcium Hardness} = 298.46 - 201.78 = \mathbf{96.68\,\text{mg/L CaCO}_3}$$

Millimoles of $\text{Mg}^{2+}$:
$$n_{\text{Mg}} = n_{\text{total}} - n_{\text{Ca}} = 0.2982 - 0.2016 = 0.0966\text{ mmol}$$
Actual concentration of $\text{Mg}^{2+}$:
$$[\text{Mg}^{2+}] = \frac{0.0966\text{ mmol} \times 24.305\text{ mg/mmol}}{0.1000\text{ L}} = \frac{2.3479\text{ mg}}{0.1000\text{ L}} = \mathbf{23.48\,\text{mg/L Mg}^{2+}}$$""",
                    "hints": ["Portion 1 measures Ca + Mg; Portion 2 at pH 12.5 measures Ca alone.", "Magnesium hardness is obtained by subtracting Calcium hardness from Total hardness."]
                },
                {
                    "id": "prob-4-4",
                    "problemNumber": "4.4",
                    "title": "Effect of Auxiliary Complexing Agents: Zinc-Ammonia-EDTA Equilibria",
                    "difficulty": "Advanced",
                    "statement": r"""Zinc(II) is titrated with $0.0100\text{ M}$ EDTA at $\text{pH } 9.00$ ($\alpha_{\text{Y}^{4-}} = 5.2 \times 10^{-2}$) in an ammonia buffer where the unprotonated ammonia concentration is $[\text{NH}_3] = 0.100\text{ M}$.
Given parameters at $25^\circ\text{C}$:
- $[\text{Zn(EDTA)}]^{2-}$: Absolute formation constant $K_f = 3.2 \times 10^{16}$ ($\log K_f = 16.50$)
- Zinc-ammine cumulative formation constants ($\beta_i$):
  $$\beta_1 = 1.6 \times 10^2, \quad \beta_2 = 3.8 \times 10^4, \quad \beta_3 = 5.0 \times 10^6, \quad \beta_4 = 1.1 \times 10^9$$

1. Calculate the fraction of free zinc ion $\alpha_{\text{Zn}^{2+}}$ in the $0.100\text{ M }\text{NH}_3$ buffer.
2. Calculate the fully adjusted conditional formation constant $K''_f$.
3. Compare $K''_f$ with the unadjusted $K_f$ and explain why auxiliary complexing agents are essential despite reducing effective binding stability.""",
                    "solution": r"""### Step 1: Calculation of $\alpha_{\text{Zn}^{2+}}$
The total concentration of unchelated zinc is:
$$c_{\text{Zn}} = [\text{Zn}^{2+}] + [\text{Zn(NH}_3)^{2+}] + [\text{Zn(NH}_3)_2^{2+}] + [\text{Zn(NH}_3)_3^{2+}] + [\text{Zn(NH}_3)_4^{2+}]$$
The fraction of free ion is:
$$\alpha_{\text{Zn}^{2+}} = \frac{1}{1 + \beta_1[\text{NH}_3] + \beta_2[\text{NH}_3]^2 + \beta_3[\text{NH}_3]^3 + \beta_4[\text{NH}_3]^4}$$
Compute the terms for $[\text{NH}_3] = 0.100\text{ M}$:
- $\beta_1 [\text{NH}_3] = (1.6 \times 10^2)(0.100) = 16$
- $\beta_2 [\text{NH}_3]^2 = (3.8 \times 10^4)(0.0100) = 380$
- $\beta_3 [\text{NH}_3]^3 = (5.0 \times 10^6)(1.0 \times 10^{-3}) = 5.0 \times 10^3$
- $\beta_4 [\text{NH}_3]^4 = (1.1 \times 10^9)(1.0 \times 10^{-4}) = 1.1 \times 10^5$

Denominator:
$$D = 1 + 16 + 380 + 5000 + 110000 = 115397 \approx 1.154 \times 10^5$$
The fraction of free zinc ion is:
$$\alpha_{\text{Zn}^{2+}} = \frac{1}{1.154 \times 10^5} = \mathbf{8.665 \times 10^{-6}}$$
Only about $1$ in every $115,000$ zinc ions is free; the remaining $99.999\%$ are sequestered as ammine complexes.

### Step 2: Fully Adjusted Conditional Formation Constant ($K''_f$)
$$K''_f = K_f \cdot \alpha_{\text{Y}^{4-}} \cdot \alpha_{\text{Zn}^{2+}}$$
$$K''_f = (3.2 \times 10^{16}) \times (5.2 \times 10^{-2}) \times (8.665 \times 10^{-6}) = (1.664 \times 10^{15}) \times (8.665 \times 10^{-6}) = \mathbf{1.442 \times 10^{10}} \quad (\log K''_f = 10.16)$$

### Step 3: Comparison and Analytical Significance
- The absolute constant is $K_f = 3.2 \times 10^{16}$ ($\log K_f = 16.50$).
- The fully adjusted constant is $K''_f = 1.44 \times 10^{10}$ ($\log K''_f = 10.16$).
*Insight*: The presence of ammonia buffer lowers the effective stability by more than six orders of magnitude ($10^{6.34}$).
However, because $\log K''_f = 10.16 \gg 8.0$, the reaction remains overwhelmingly quantitative.
Crucially, without ammonia, zinc would precipitate at $\text{pH } 9.0$ as insoluble zinc hydroxide ($\text{Zn(OH)}_2$, $K_{\text{sp}} = 3.0 \times 10^{-17}$), terminating the titration. The auxiliary ammine complexation prevents hydroxide precipitation while permitting complete transfer of zinc to the thermodynamically superior EDTA chelate.""",
                    "hints": ["Calculate the ammine distribution polynomial sum(beta_i * [NH3]^i).", "Fully adjusted constant K''_f = K_f * alpha_Y * alpha_M."]
                },
                {
                    "id": "prob-4-5",
                    "problemNumber": "4.5",
                    "title": "Thermodynamics of Masking and Demasking Cyanide in Zinc-Nickel Mixtures",
                    "difficulty": "Honors Problem",
                    "statement": r"""A $50.0\text{ mL}$ alloy solution contains $0.0100\text{ M }\text{Ni}^{2+}$ and $0.0100\text{ M }\text{Zn}^{2+}$. Both ions react strongly with EDTA at $\text{pH } 10.0$ ($\log K_f(\text{Ni}) = 18.62, \log K_f(\text{Zn}) = 16.50$).
Potassium cyanide ($\text{KCN}$) is added to mask both ions as cyano complexes:
- $[\text{Ni(CN)}_4]^{2-}$: Overall formation constant $\beta_4 = 1.0 \times 10^{31}$
- $[\text{Zn(CN)}_4]^{2-}$: Overall formation constant $\beta_4 = 5.0 \times 10^{16}$

1. In a solution where free uncomplexed cyanide is maintained at $[\text{CN}^-] = 0.050\text{ M}$, calculate the fraction of free $\text{Ni}^{2+}$ and free $\text{Zn}^{2+}$.
2. Explain chemically why formaldehyde ($\text{HCHO}$) selectively demasks $[\text{Zn(CN)}_4]^{2-}$ but leaves $[\text{Ni(CN)}_4]^{2-}$ completely intact.
3. Write the balanced equation for the selective demasking reaction and the subsequent titration with EDTA.""",
                    "solution": r"""### Step 1: Fraction of Free Metal in Cyanide Media
For $[\text{CN}^-] = 0.050\text{ M}$, $[\text{CN}^-]^4 = (0.050)^4 = 6.25 \times 10^{-6}\text{ M}^4$.
1. For Nickel(II):
$$\alpha_{\text{Ni}^{2+}} = \frac{1}{1 + \beta_4[\text{CN}^-]^4} \approx \frac{1}{(1.0 \times 10^{31})(6.25 \times 10^{-6})} = \frac{1}{6.25 \times 10^{25}} = \mathbf{1.60 \times 10^{-26}}$$
Conditional constant with EDTA ($\alpha_{\text{Y}} = 0.35$):
$$K'_f(\text{Ni}) = (4.17 \times 10^{18})(0.35)(1.60 \times 10^{-26}) = \mathbf{2.3 \times 10^{-8}} \ll 1$$
Nickel is completely, irreversibly masked.

2. For Zinc(II):
$$\alpha_{\text{Zn}^{2+}} = \frac{1}{1 + \beta_4[\text{CN}^-]^4} \approx \frac{1}{(5.0 \times 10^{16})(6.25 \times 10^{-6})} = \frac{1}{3.125 \times 10^{11}} = \mathbf{3.20 \times 10^{-12}}$$
Both metals are completely masked from EDTA in the presence of excess free cyanide.

### Step 2: Selective Demasking Chemistry of Formaldehyde
Formaldehyde undergoes nucleophilic addition with free cyanide ions to form the extremely stable, non-coordinating formaldehyde cyanohydrin (glycolonitrile):
$$\text{HCHO} + \text{CN}^- + \text{H}_2\text{O} \rightleftharpoons \text{HO-CH}_2\text{-CN} + \text{OH}^- \quad (K_{\text{form}} \approx 10^{12})$$
- Because $\beta_4$ for $[\text{Zn(CN)}_4]^{2-}$ ($5.0 \times 10^{16}$) is moderate, shifting the free cyanide equilibrium by formaldehyde addition drops $[\text{CN}^-]$ so low that the zinc complex dissociates completely.
- In contrast, $[\text{Ni(CN)}_4]^{2-}$ has a colossal formation constant of $\beta_4 = 1.0 \times 10^{31}$ (nearly 15 orders of magnitude more stable than zinc!). Formaldehyde cannot displace cyanide from the ultra-stable square-planar low-spin $d^8$ $[\text{Ni(CN)}_4]^{2-}$ complex.

### Step 3: Balanced Reactions
1. Selective Demasking Reaction:
$$[\text{Zn(CN)}_4]^{2-} + 4\,\text{HCHO} + 4\,\text{H}_2\text{O} \to \text{Zn}^{2+} + 4\,\text{HOCH}_2\text{CN} + 4\,\text{OH}^-$$
2. Titration of Liberated Zinc with EDTA:
$$\text{Zn}^{2+} + \text{H}_2\text{Y}^{2-} \to [\text{Zn(EDTA)}]^{2-} + 2\,\text{H}^+$$
The liberated zinc is titrated quantitatively using Eriochrome Black T indicator, achieving complete separation from nickel in a single volumetric vessel.""",
                    "hints": ["Calculate the ammine/cyano polynomial denominator beta_4 * [CN-]^4.", "Compare the stability of Ni(CN)4^2- (beta=10^31) vs Zn(CN)4^2- (beta=5*10^16)."]
                },
                {
                    "id": "prob-4-6",
                    "problemNumber": "4.6",
                    "title": "Extraction-Complexation Stoichiometry of Copper Diethyldithiocarbamate",
                    "difficulty": "Intermediate",
                    "statement": r"""Copper(II) reacts quantitatively with sodium diethyldithiocarbamate ($\text{Na-DDTC}$, $\text{Na}^+[(\text{C}_2\text{H}_5)_2\text{N-CSS}]^-$) in neutral or slightly alkaline solution to form an intensely golden-brown neutral chelate that is extracted quantitatively into carbon tetrachloride ($\text{CCl}_4$):
$$\text{Cu}^{2+} + 2\,\text{DDTC}^- \rightleftharpoons \text{Cu(DDTC)}_2(s/\text{org})$$
1. Draw the chelate coordination structure around the copper center, identifying the donor atoms and ring size.
2. If a $25.0\text{ mL}$ aliquot of electroplating wastewater containing $12.5\text{ mg}\cdot\text{L}^{-1}\text{ Cu}^{2+}$ is reacted with an excess of $\text{Na-DDTC}$ and extracted into $10.0\text{ mL}$ of $\text{CCl}_4$, calculate the molar concentration of $\text{Cu(DDTC)}_2$ in the organic extract, assuming $100\%$ extraction efficiency ($M_{\text{Cu}} = 63.546\text{ g}\cdot\text{mol}^{-1}$).
3. If the molar absorptivity of $\text{Cu(DDTC)}_2$ in $\text{CCl}_4$ at $\lambda = 436\text{ nm}$ is $\varepsilon = 12,800\text{ L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$, calculate the theoretical absorbance in a $1.00\text{-cm}$ cuvette.""",
                    "solution": r"""### Step 1: Chelate Coordination Structure
- Ligand: Diethyldithiocarbamate coordinates as a bidentate mono-anionic sulfur donor through both sulfur atoms ($S, S'$ coordination).
- Complex: $\text{Cu(DDTC)}_2$ forms a neutral bis-chelate with a distorted square-planar or square-pyramidal geometry around the $\text{Cu}^{2+}$ ($d^9$) center.
- Ring Size: Each chelate ring consists of four atoms ($\text{Cu}-\text{S}-\text{C}-\text{S}$), forming a stable four-membered metallacycle. The neutral charge imparts exceptional hydrophobicity, driving extraction into organic solvents.

### Step 2: Molar Concentration in Organic Extract
Mass of copper in $25.0\text{ mL}$ ($0.0250\text{ L}$) aliquot:
$$m_{\text{Cu}} = 0.0250\text{ L} \times 12.5\text{ mg/L} = 0.3125\text{ mg} = 3.125 \times 10^{-4}\text{ g}$$
Moles of copper:
$$n_{\text{Cu}} = \frac{3.125 \times 10^{-4}\text{ g}}{63.546\text{ g}\cdot\text{mol}^{-1}} = 4.9177 \times 10^{-6}\text{ mol}$$

Because extraction efficiency is $100\%$ and the organic volume is $V_{\text{org}} = 10.0\text{ mL} = 0.0100\text{ L}$:
$$[\text{Cu(DDTC)}_2]_{\text{org}} = \frac{4.9177 \times 10^{-6}\text{ mol}}{0.0100\text{ L}} = \mathbf{4.918 \times 10^{-4}\text{ M}}$$

### Step 3: Absorbance Calculation via Beer-Lambert Law
$$A = \varepsilon \cdot b \cdot c$$
Given $\varepsilon = 12,800\text{ L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$, $b = 1.00\text{ cm}$, and $c = 4.918 \times 10^{-4}\text{ M}$:
$$A = (12,800\text{ L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}) \times (1.00\text{ cm}) \times (4.918 \times 10^{-4}\text{ mol}\cdot\text{L}^{-1}) = \mathbf{6.295}$$
*Analytical Note*: An absorbance of $6.3$ is off-scale for standard spectrophotometers (photodetector saturation occurs above $A \approx 2.0$). In practice, the analyst would either take a smaller aliquot ($1.0\text{ mL}$) or dilute the organic extract by a factor of $10$ to bring the absorbance into the optimal linear range ($A \approx 0.63$).""",
                    "hints": ["Compute total moles of copper extracted into the organic volume.", "Use Beer-Lambert law A = eps * b * c."]
                },
                {
                    "id": "prob-4-7",
                    "problemNumber": "4.7",
                    "title": "Thermodynamic Proof of Indicator Blocking by Trace Transition Metals",
                    "difficulty": "Honors Problem",
                    "statement": r"""A water hardness sample contains $0.010\text{ M }\text{Ca}^{2+}$ and a trace contamination of $1.0 \times 10^{-4}\text{ M }\text{Cu}^{2+}$.
The analyst buffers the solution to $\text{pH } 10.0$ and adds Eriochrome Black T indicator.
Given:
- $[\text{Cu(EDTA)}]^{2-}$: $K_f = 6.3 \times 10^{18}$
- $[\text{Cu(EBT)}]^-$: Conditional stability constant $K'_{\text{Cu-EBT}} = 1.0 \times 10^{16}$
- $[\text{Mg(EDTA)}]^{2-}$: $K'_f = 2.2 \times 10^8$
- $[\text{Mg(EBT)}]^-$: $K'_{\text{Mg-EBT}} = 1.0 \times 10^5$

1. Explain mathematically why trace copper causes **indicator blocking**.
2. How does the addition of $0.1\text{ g}$ of potassium cyanide ($\text{KCN}$) eliminate indicator blocking?""",
                    "solution": r"""### Step 1: Mathematical Proof of Indicator Blocking
For a metallochromic indicator to function effectively:
$$K'_f(\text{M-EDTA}) \gg K'_{\text{M-Ind}}$$
EDTA must be able to displace the metal from the indicator at the equivalence point:
$$[\text{M-Ind}] + \text{EDTA} \rightleftharpoons [\text{M-EDTA}] + \text{Ind}$$
The equilibrium constant for indicator displacement is:
$$K_{\text{disp}} = \frac{K'_f(\text{M-EDTA})}{K'_{\text{M-Ind}}}$$

- For Magnesium:
$$K_{\text{disp}}(\text{Mg}) = \frac{2.2 \times 10^8}{1.0 \times 10^5} = 2.2 \times 10^3$$
Because $K_{\text{disp}} \gg 1$, EDTA readily extracts magnesium from the dye, yielding a sharp wine-red to blue transition.

- For Copper:
$$K'_{\text{Cu-EBT}} = 1.0 \times 10^{16}$$
The stability of the copper-indicator complex is so immense ($10^{16}$) that the ligand exchange kinetics with EDTA are prohibitively sluggish ($\Delta G^\ddagger$ barrier is high). Furthermore, even at a slight excess of EDTA, the displacement equilibrium cannot pull copper away from EBT rapidly.
The indicator remains trapped as the wine-red $[\text{Cu-EBT}]^-$ complex indefinitely, completely preventing the appearance of the blue end point. The indicator is **permanently blocked**.

### Step 2: Elimination via Cyanide Masking
Adding potassium cyanide ($\text{KCN}$) introduces excess cyanide ions, which react with copper to form the exceptionally stable tetracyanocuprate(I) complex ($[\text{Cu(CN)}_4]^{3-}$, $\beta_4 \approx 10^{27}$):
$$\text{Cu}^{2+} + \text{CN}^- \text{ (redox/complexation)} \to [\text{Cu(CN)}_4]^{3-}$$
Cyanide lowers the free copper ion activity to $< 10^{-25}\text{ M}$, far below the threshold required to coordinate with Eriochrome Black T. The indicator remains uncoordinated by copper, allowing unhindered titration of calcium and magnesium.""",
                    "hints": ["Calculate the displacement equilibrium constant K_disp = K'_f(M-EDTA) / K'_(M-Ind).", "Blocking occurs when the metal-indicator complex is kinetically inert and thermodynamically too stable."]
                }
            ]
        },

        # =====================================================================
        # UNIT 5
        # =====================================================================
        {
            "id": "unit-5-advanced-atomic-spectroscopy",
            "unitNumber": 5,
            "title": "Unit 5: Advanced Atomic Spectroscopy: AAS, AES, AFS & Atomization Systems",
            "leadSummary": "Exhaustive treatment of atomic electronic transitions, Russell-Saunders term symbols, Boltzmann population ratios, spectral line broadening mechanisms (Doppler, Lorentz, natural), Hollow Cathode Lamp discharge physics, optical Czerny-Turner monochromator diffraction gratings, electrothermal graphite furnace atomization (GFAAS), and background correction systems (Deuterium, Zeeman splitting, Smith-Hieftje).",
            "simulations": ["sim_chem_atomic_absorption_flameless_zeeman"],
            "sections": [
                {
                    "id": "sec-5-1",
                    "secNumber": "5.1",
                    "title": "Quantum Physics of Atomic Transitions: Boltzmann Population Ratios & AAS vs AES vs AFS",
                    "content": r"""Atomic spectroscopy encompasses analytical techniques that measure the absorption, emission, or fluorescence of electromagnetic radiation by free, gas-phase atoms or elemental ions. Because isolated atoms possess discrete quantized electronic energy levels without vibrational or rotational degrees of freedom, atomic spectra consist of narrow, discrete spectral lines.

### The Boltzmann Distribution Law
In any thermal atomization cell (such as an air-acetylene flame at $2400\text{ K}$ or a graphite furnace at $2700\text{ K}$), the distribution of atoms between the ground electronic state ($E_0$) and an excited electronic state ($E_j$) is governed by statistical thermodynamics according to the **Maxwell-Boltzmann distribution**:
$$\frac{N_j}{N_0} = \frac{g_j}{g_0} \exp\left(-\frac{\Delta E}{k_B T}\right) = \frac{g_j}{g_0} \exp\left(-\frac{h c}{\lambda k_B T}\right)$$
where:
- $N_j$ and $N_0$ are the number densities of atoms in the excited and ground states, respectively.
- $g_j$ and $g_0$ are the quantum statistical weights (degeneracies) of the excited and ground states, given by $g = 2J + 1$ (where $J$ is the total angular momentum quantum number).
- $\Delta E = E_j - E_0 = \frac{h c}{\lambda}$ is the excitation transition energy.
- $k_B$ is the Boltzmann constant ($1.3806 \times 10^{-23}\text{ J}\cdot\text{K}^{-1}$).
- $T$ is the absolute thermodynamic temperature of the atom cell (in Kelvin).

```
        Boltzmann Population Ratio (Nj / N0) at Flame Temperatures (2500 K)
   Element    Transition (λ)    ΔE (eV)     g_j / g_0    N_j / N_0 (Excited Fraction)
   ─────────────────────────────────────────────────────────────────────────────
   Na         589.0 nm          2.10 eV     2            1.72 × 10⁻⁴ (0.017%)
   Mg         285.2 nm          4.35 eV     3            5.28 × 10⁻⁹ (0.0000005%)
   Zn         213.9 nm          5.80 eV     3            7.30 × 10⁻¹² (Trillionths)
   ─────────────────────────────────────────────────────────────────────────────
   > 99.98% of atoms remain in the ground state (N₀) even at flame temperatures!
```

### The Three Atomic Spectroscopy Modalities

```
  1. Atomic Absorption (AAS)      2. Atomic Emission (AES)     3. Atomic Fluorescence (AFS)
     hν_in                           Thermal Heat                     hν_in
      ──► [Atom*]                     ──► [Atom*]                      ──► [Atom*]
            │                               │                                │
            ▼ (Ground state absorption)     ▼ (Photon emitted)               ▼ (Photon emitted)
     Measures attenuation of         Measures intensity of          Measures re-emitted
     external source beam:           thermal radiative decay:       photons at 90°:
     A = log(I₀ / I)                 I_em ∝ N_j                     I_F ∝ I₀ · N₀ · φ
```

#### 1. Atomic Absorption Spectroscopy (AAS)
Measures the resonant absorption of monochromatic radiation from an external light source by unexcited ground-state atoms ($N_0$). Because $> 99.9\%$ of atoms reside in the ground state, AAS is inherently robust against minor flame temperature fluctuations.

#### 2. Atomic Emission Spectroscopy (AES / OES)
Measures the radiant power emitted when thermally excited atoms ($N_j$) relax radiatively back to lower energy levels. Because $N_j$ is exponentially dependent upon temperature ($\exp(-\Delta E / k_B T)$), atomic emission signals are acutely sensitive to flame temperature stability.

#### 3. Atomic Fluorescence Spectroscopy (AFS)
Free atoms in the ground state are excited by an intense light source (laser or high-intensity discharge lamp), and the re-emitted fluorescent photons are detected perpendicularly ($90^\circ$) to minimize source scatter. Signal intensity is directly proportional to source power.""",
                    "simulations": ["sim_chem_atomic_absorption_flameless_zeeman"]
                },
                {
                    "id": "sec-5-2",
                    "secNumber": "5.2",
                    "title": "Spectral Fine Structure: Sodium Doublet vs Magnesium Singlet Transitions",
                    "content": r"""The discrete wavelengths observed in atomic spectroscopy are defined by atomic term symbols governed by Russell-Saunders ($L-S$) coupling schemes:
$$^{2S+1}L_J$$
where $S$ is the total spin quantum number, $2S+1$ is the spin multiplicity, $L$ is the total orbital angular momentum quantum number ($S, P, D, F$ corresponding to $L = 0, 1, 2, 3$), and $J = |L - S|, \dots, L + S$ is the total angular momentum.

### The Sodium Atom ($Z = 11$): Spin-Orbit Doublet Splitting
Neutral sodium possesses an electronic configuration of $1s^2 2s^2 2p^6 3s^1$ (alkali metal with a single valence electron, $S = 1/2$, multiplicity $2S+1 = 2$, doublet system).
- **Ground State**: The valence electron occupies the $3s$ orbital ($L = 0, S = 1/2 \implies J = 1/2$). Term symbol: **$^2S_{1/2}$** (degeneracy $g = 2(1/2) + 1 = 2$).
- **Excited State**: Absorption promotes the electron to the $3p$ orbital ($L = 1, S = 1/2$).
  Because the magnetic moment of the electron spin interacts with the magnetic field generated by its orbital motion (spin-orbit coupling $\hat{H}_{\text{SO}} = \xi(r) \mathbf{L} \cdot \mathbf{S}$), the $3p$ state splits into two discrete energy levels:
  1. $J = 1 - 1/2 = 1/2 \implies \mathbf{^2P_{1/2}}$ ($g = 2(1/2) + 1 = 2$)
  2. $J = 1 + 1/2 = 3/2 \implies \mathbf{^2P_{3/2}}$ ($g = 2(3/2) + 1 = 4$)

```
                 Sodium Energy Level Diagram (Spin-Orbit Doublet)
                           3p ²P₃/₂ (g = 4) ───
                                                 ▲ ΔE_SO = 0.0021 eV (17 cm⁻¹)
                           3p ²P₁/₂ (g = 2) ───
                                │           │
                    589.6 nm    │           │   589.0 nm
                    (D₁ Line)   │           │   (D₂ Line)
                                ▼           ▼
                           3s ²S₁/₂ (g = 2) ─────────────────── (Ground State)
```

The electric dipole selection rules ($\Delta L = \pm 1, \Delta J = 0, \pm 1$) permit two resonance transitions:
1. $3s \ ^2S_{1/2} \to 3p \ ^2P_{1/2}$ at **$\lambda = 589.592\text{ nm}$** (the $\mathbf{D_1}$ line).
2. $3s \ ^2S_{1/2} \to 3p \ ^2P_{3/2}$ at **$\lambda = 589.002\text{ nm}$** (the $\mathbf{D_2}$ line).
Because the $^2P_{3/2}$ state possesses a statistical degeneracy of $g = 4$ versus $g = 2$ for $^2P_{1/2}$, the **$D_2$ line is exactly twice as intense as the $D_1$ line** ($I_{D_2} / I_{D_1} = 2.0$).

### The Magnesium Atom ($Z = 12$): Singlet System
Neutral magnesium has two valence electrons ($3s^2$). In the ground state, electron spins are paired antiparallel ($S = 0$, multiplicity $2S+1 = 1$, singlet system).
- **Ground State**: $3s^2 \ \mathbf{^1S_0}$ ($L = 0, S = 0, J = 0$).
- **Excited States**: Promoting one electron yields:
  - Singlet: $3s3p \ \mathbf{^1P_1}$ ($S = 0, L = 1, J = 1$).
  - Triplet: $3s3p \ \mathbf{^3P_{0, 1, 2}}$ ($S = 1, L = 1, J = 0, 1, 2$).
According to selection rule $\Delta S = 0$ (spin-forbidden intercombination), singlet-triplet transitions are forbidden. The primary resonance absorption is a single, sharp spectral line:
$$3s^2 \ ^1S_0 \to 3s3p \ ^1P_1 \quad \text{at } \mathbf{\lambda = 285.213\text{ nm}}$$""",
                    "simulations": []
                },
                {
                    "id": "sec-5-3",
                    "secNumber": "5.3",
                    "title": "Spectral Line Broadening: Natural, Doppler & Collisional (Lorentz) Broadening",
                    "content": r"""According to classical quantum electrodynamics, an electronic transition should yield an infinitely narrow spectral line. In real atomization cells, however, atomic absorption and emission lines exhibit finite bandwidths, typically $\Delta \lambda \approx 0.002\text{--}0.005\text{ nm}$ ($2\text{--}5\text{ pm}$). Three physical mechanisms govern spectral line broadening:

### 1. Natural Line Broadening ($\Delta \lambda_N$)
Arises fundamentally from the Heisenberg uncertainty principle:
$$\Delta E \cdot \Delta t \ge \frac{\hbar}{2} \implies \Delta \nu_N \approx \frac{1}{2\pi \tau}$$
where $\tau$ is the radiative lifetime of the excited state (typically $\tau \approx 10^{-8}\text{ s}$ for allowed electric dipole transitions).
$$\Delta \nu_N \approx \frac{1}{2\pi (10^{-8}\text{ s})} \approx 1.6 \times 10^7\text{ Hz} \implies \Delta \lambda_N \approx 10^{-5}\text{ nm} \ (0.01\text{ pm})$$
Natural broadening is negligible compared to Doppler and pressure broadening.

### 2. Doppler Broadening ($\Delta \lambda_D$)
Arises from the Maxwellian thermal velocity distribution of gas-phase atoms moving relative to the optical observer. Atoms moving toward the light source absorb photons at lower frequencies, while atoms moving away absorb at higher frequencies.
The Doppler full-width at half-maximum (FWHM) is derived from statistical mechanics:
$$\Delta \nu_D = \nu_0 \sqrt{\frac{8 k_B T \ln 2}{M c^2}} \implies \frac{\Delta \lambda_D}{\lambda_0} = \sqrt{\frac{8 k_B T \ln 2}{M c^2}} = 7.16 \times 10^{-7} \sqrt{\frac{T}{M}}$$
where $T$ is temperature in Kelvin and $M$ is atomic mass in atomic mass units ($\text{g}\cdot\text{mol}^{-1}$).
- For sodium ($M = 23$) at $T = 2500\text{ K}$:
$$\frac{\Delta \lambda_D}{589\text{ nm}} = 7.16 \times 10^{-7} \sqrt{\frac{2500}{23}} = 7.16 \times 10^{-7} \times 10.42 = 7.46 \times 10^{-6}$$
$$\Delta \lambda_D \approx 0.0044\text{ nm} \ (4.4\text{ pm})$$
Doppler broadening dominates at high flame and plasma temperatures.

### 3. Collisional (Lorentz / Pressure) Broadening ($\Delta \lambda_L$)
Arises from electrostatic collisions between the radiating analyte atom and surrounding bath gas molecules (argon, $\text{N}_2$, $\text{CO}_2$, $\text{H}_2\text{O}$). Collisions perturb the outer electronic valence orbitals, shortening the effective lifetime $\tau_{\text{coll}}$:
$$\Delta \nu_L = \frac{1}{\pi \tau_{\text{coll}}} \propto \frac{P}{\sqrt{T}}$$
At atmospheric pressure ($1\text{ bar}$) inside a flame, $\Delta \lambda_L \approx 0.002\text{--}0.005\text{ nm}$, matching Doppler broadening in magnitude.

```
       Comparison: Monochromator Bandpass vs Atomic Absorption Line
   Transmittance / Absorbance
    ▲
    │      ┌─────────────────────────────┐
    │      │  Optical Monochromator      │
    │      │  Bandpass (Δλ ≈ 0.2 - 1 nm) │  Broad transmission window
    │      └──────────────┬──────────────┘
    │                     │
    │                    / \                Atomic Absorption Line
    │                   /   \               (Δλ ≈ 0.002 nm = 2 pm)
    │                  /     \              500× narrower!
    └───┼─────────────┼───────┼─────────────┼───► Wavelength λ
       588.0        589.0   589.6         590.0
```

### The AAS Linewidth Dilemma & The Need for Hollow Cathode Lamps
Because atomic absorption lines are extraordinarily narrow ($\Delta \lambda \approx 0.002\text{ nm}$), a conventional continuous light source (xenon arc or tungsten lamp) dispersed through the finest optical monochromator (bandpass $\Delta \lambda_{\text{mono}} \approx 0.2\text{ nm}$) would deliver radiation that is **$100\text{ to }500\text{ times wider}$** than the atomic absorption line!
Over $99\%$ of the photons reaching the detector would bypass atomic absorption, diluting the signal and destroying the linearity of Beer's law. This fundamental physical dilemma necessitated the invention of the **Hollow Cathode Lamp**.""",
                    "simulations": []
                },
                {
                    "id": "sec-5-4",
                    "secNumber": "5.4",
                    "title": "Light Sources: Hollow Cathode Lamp (HCL) Discharge Physics & Self-Reversal",
                    "content": r"""To resolve the linewidth dilemma, Sir Alan Walsh (1955) introduced the **Hollow Cathode Lamp (HCL)**—a sharp-line emission source that produces emission lines significantly narrower than the absorption profile of atoms in the flame ($\Delta \lambda_{\text{emission}} < \Delta \lambda_{\text{flame}}$).

### Internal Architecture and Physics of the HCL
A hollow cathode lamp consists of a sealed glass cylinder with a quartz optical window, evacuated and back-filled with an inert filler gas (ultra-pure neon or argon) at low pressure ($1\text{--}5\text{ torr}$ / $130\text{--}650\text{ Pa}$).

```
                     Hollow Cathode Lamp (HCL) Physics
      ┌───────────────────────────────────────────────────────────────┐
      │  Inert Gas (Ne, 2 torr)                                       │
      │                                                               │
      │   Tungsten Anode (+)                                          │
      │   ───► e⁻ ──► Ne + e⁻ ──► Ne⁺ + 2e⁻ (Ionization)              │
      │                                                               │
      │   Hollow Cathode Cup (-) [Constructed of Pure Element, e.g. Cu]
      │   ┌────────┐                                                  │
      │   │        │ ◄─── Accelerated Ne⁺ Sputtering Impact           │
      │   │   Cu*  │ ───► Ejected neutral Cu⁰ atoms into plasma cloud  │
      │   │        │ ───► Collision: Cu⁰ + Ne* ──► Cu* ──► Cu⁰ + hν   │
      │   └────────┘      (Sharp Line Emission: Δλ ≈ 0.001 nm)        │
      └───────────────────────────────────────────────────────────────┘
```

#### 1. Sputtering Mechanism
1. A potential difference of $300\text{--}500\text{ V}$ applied across the tungsten anode and hollow cylindrical cathode initiates a glow discharge.
2. Filler gas atoms are ionized by electron impact: $\text{Ne} + e^- \to \text{Ne}^+ + 2\,e^-$.
3. The heavy cations ($\text{Ne}^+$) accelerate across the electric potential gradient and strike the interior surface of the cathode cup with high kinetic energy.
4. Sputtering impact physically dislodges neutral analyte atoms from the cathode surface into the vapor phase inside the hollow cavity: $\text{Ne}^+ + M(s) \to \text{Ne} + M^0(g)$.

#### 2. Collisional Excitation & Sharp Emission
1. The sputtered gas-phase metal atoms collide with energetic electrons and metastable neon atoms, undergoing electronic excitation: $M^0 + e^- \to M^* + e^-$.
2. The excited metal atoms decay radiatively back to the ground state, emitting the characteristic atomic resonance spectrum: $M^* \to M^0 + h\nu$.
3. Because the lamp operates at low temperature ($< 400\text{ K}$) and low pressure ($2\text{ torr}$), both Doppler broadening ($\propto \sqrt{T}$) and collisional broadening ($\propto P$) are minimal. The resulting emission lines have linewidths of only $\Delta \lambda \approx 0.001\text{ nm}$—half the width of the flame absorption line!

### The Self-Reversal (Self-Absorption) Defect
Operating an HCL at excessively high lamp current produces **self-reversal**:
1. High current creates a dense cloud of unexcited ground-state atoms ($M^0$) near the open mouth of the cathode cavity.
2. The sharp photons emitted by excited atoms deep within the core cavity pass through this cold outer cloud.
3. The cold atoms absorb the exact center of the resonance line (where absorption probability is highest), while the line wings escape.
4. **Result**: The emission profile develops a central dip or crater (self-reversal), destroying analytical sensitivity and inducing severe non-linear calibration curvature.""",
                    "simulations": []
                },
                {
                    "id": "sec-5-5",
                    "secNumber": "5.5",
                    "title": "Optical Monochromators: Czerny-Turner Layout, Reflection Gratings & Dispersion",
                    "content": r"""In AAS, the optical monochromator does not isolate the resonance absorption linewidth (which is governed by the HCL); its role is to isolate the target analytical line from adjacent non-absorbing filler gas emission lines (neon/argon lines) and other elemental lines emitted by the cathode.

### The Czerny-Turner Optical Configuration
The standard optical layout in atomic spectrometers is the **Czerny-Turner reflection monochromator**:

```
                       Czerny-Turner Monochromator
                        Entrance Slit S₁
                             │
                             ▼
                    ┌──────────────────┐
                    │ Collimating      │
                    │ Concave Mirror M₁│
                    └────────┬─────────┘
                             │ Parallel Beam
                             ▼
                    ┌──────────────────┐
                    │ Reflection       │ ──► Disperses light by diffraction:
                    │ Blazed Grating G │     n λ = d (sin α + sin β)
                    └────────┬─────────┘
                             │ Angularly Separated Rays
                             ▼
                    ┌──────────────────┐
                    │ Focusing         │
                    │ Concave Mirror M₂│
                    └────────┬─────────┘
                             │
                             ▼
                        Exit Slit S₂ ──► Photomultiplier Detector (PMT)
```

### The Grating Equation
Diffraction gratings consist of an aluminized glass substrate ruled with thousands of microscopic parallel grooves (e.g., $1200\text{ to }2400\text{ lines/mm}$).
Constructive interference occurs when the optical path difference between light rays reflected from adjacent grooves equals an integer number of wavelengths $n$:
$$n\,\lambda = d (\sin \alpha + \sin \beta)$$
where:
- $n$ is the diffraction order ($n = \pm 1, \pm 2, \dots$).
- $d$ is the groove spacing ($d = 1 / N_{\text{grooves}}$, e.g., $1 / 1200\text{ mm} = 8.333 \times 10^{-4}\text{ mm} = 833.3\text{ nm}$).
- $\alpha$ is the angle of incidence relative to the grating normal.
- $\beta$ is the angle of diffraction.

### Grating Performance Figures of Merit

#### 1. Angular Dispersion ($D_\theta$)
$$D_\theta = \frac{d\beta}{d\lambda} = \frac{n}{d \cos \beta}$$

#### 2. Reciprocal Linear Dispersion ($D^{-1}$)
Defines the wavelength spread (in nanometers) dispersed per millimeter across the focal plane:
$$D^{-1} = \frac{d\lambda}{dx} = \frac{d \cos \beta}{n \cdot f}$$
where $f$ is the focal length of the focusing mirror $M_2$.
For $d = 833.3\text{ nm}$, $n = 1$, $\beta \approx 0$, and $f = 500\text{ mm}$:
$$D^{-1} = \frac{833.3\text{ nm}}{500\text{ mm}} = \mathbf{1.67\text{ nm/mm}}$$

#### 3. Spectral Bandpass (Effective Bandwidth, $\Delta \lambda_{\text{eff}}$)
The slice of wavelengths transmitted through exit slit of physical width $w$:
$$\Delta \lambda_{\text{eff}} = w \cdot D^{-1}$$
For an exit slit width $w = 0.20\text{ mm}$ and $D^{-1} = 1.67\text{ nm/mm}$:
$$\Delta \lambda_{\text{eff}} = (0.20\text{ mm}) \times (1.67\text{ nm/mm}) = \mathbf{0.334\text{ nm}}$$

#### 4. Resolving Power ($R$)
The ability to resolve two adjacent wavelengths $\lambda$ and $\lambda + \Delta \lambda$:
$$R = \frac{\lambda}{\Delta \lambda} = n \cdot N_{\text{total}}$$
where $N_{\text{total}}$ is the total number of illuminated grooves on the grating face. For a $50\text{-mm}$ grating ruled at $1200\text{ grooves/mm}$ in first order:
$$R = 1 \times (50 \times 1200) = \mathbf{60,000}$$
At $\lambda = 589\text{ nm}$, the minimum resolvable difference is:
$$\Delta \lambda = \frac{589\text{ nm}}{60,000} = \mathbf{0.0098\text{ nm}}$$
Easily resolving the sodium doublet ($D_2 - D_1 = 0.59\text{ nm}$).""",
                    "simulations": []
                },
                {
                    "id": "sec-5-6",
                    "secNumber": "5.6",
                    "title": "Atom Cells: Flame Premix Burners vs Electrothermal Graphite Furnace (GFAAS)",
                    "content": r"""The atom cell converts liquid analyte solutions into free gas-phase atoms. Two primary atomization systems dominate atomic absorption spectroscopy: **premix flame burners** and **electrothermal graphite furnaces (GFAAS)**.

### 1. Flame Atomization: Premix Laminar Flow Burner
A pneumatic nebulizer draws liquid sample through a capillary via the Bernoulli effect, impacting an impact bead to generate an aerosol mist.
- **Nebulization Efficiency**: Only $5\text{--}10\%$ of aerosol droplets ($< 5\,\mu\text{m}$) reach the flame; $90\text{--}95\%$ drains to waste.
- **Burner Head**: Utilizes a long, narrow single-slot titanium burner head ($10\text{ cm}$ for air-acetylene; $5\text{ cm}$ for $\text{N}_2\text{O}$-acetylene) aligned collinear with the optical light beam to maximize optical pathlength $b$ in Beer's law ($A = \varepsilon b c$).

| Flame Gas Mixture | Max Temperature ($^\circ\text{C}$) | Max Burn Velocity ($\text{cm/s}$) | Analytical Applications |
| :--- | :---: | :---: | :--- |
| **Air - Acetylene ($\text{C}_2\text{H}_2$)** | $2300^\circ\text{C}$ | $160\text{ cm/s}$ | Base metals ($\text{Cu, Zn, Fe, Pb, Cd, Na, K, Mg}$) |
| **Nitrous Oxide ($\text{N}_2\text{O}$) - Acetylene** | $2900^\circ\text{C}$ | $285\text{ cm/s}$ | Refractory oxide formers ($\text{Al, Si, Ti, V, Mo, B}$) |
| **Air - Propane** | $1925^\circ\text{C}$ | $45\text{ cm/s}$ | Readily atomized alkali metals ($\text{Na, K, Li}$) |

*Refractory Element Problem*: Elements such as $\text{Al}, \text{Si}, \text{Ti}$ form refractory metal-oxygen bonds ($\text{BDE} > 500\text{ kJ/mol}$) that cannot be cleaved at $2300^\circ\text{C}$. The hot, reducing cyanogen radicals ($:\text{CN}$) present in fuel-rich $\text{N}_2\text{O}-\text{C}_2\text{H}_2$ flames ($2900^\circ\text{C}$) scavenge oxygen, enabling free atom production.

### 2. Electrothermal Atomization (Graphite Furnace AAS / GFAAS)
Introduced by Boris L'vov, GFAAS replaces the continuous flame with an electrothermally heated pyrolytic graphite tube ($28\text{ mm}$ length, $6\text{ mm}$ internal diameter). A micro-aliquot ($10\text{--}50\,\mu\text{L}$) is injected onto an internal **L'vov platform**.

```
                GFAAS 4-Stage Thermal Heating Temperature Program
     Temperature (°C)
      3000 ▲
           │                                          Clean (2600°C)
      2500 ┼                             Atomize      ┌─────────┐
           │                             (2400°C)    /           \
      2000 ┼                           ┌───────────┐/             \
           │                          /             \
      1500 ┼                         /
           │            Ash/Pyrolysis
      1000 ┼            (800°C)
           │          ┌───────────────┐
       500 ┼         /                 \
           │  Dry (110°C)
           │┌──────┐/
         0 └┴──────┴────────────────────────────────────────────────► Time (s)
            0     30      60          90          100        110
```

#### The Four Stages of the GFAAS Thermal Cycle
1. **Drying Stage ($100\text{--}130^\circ\text{C}$, $30\text{ s}$)**: Evaporates the aqueous or organic solvent smoothly without boiling or sample splattering.
2. **Pyrolysis / Ashing Stage ($400\text{--}1200^\circ\text{C}$, $30\text{ s}$)**: Thermally volatilizes and chars matrix salts, organic proteins, and lipids before analyte atomization, minimizing matrix background interference. Chemical modifiers (e.g., $\text{Pd(NO}_3)_2 + \text{Mg(NO}_3)_2$) are co-injected to thermally stabilize volatile analytes (such as $\text{As}, \text{Pb}, \text{Cd}$).
3. **Atomization Stage ($2000\text{--}2700^\circ\text{C}$, $3\text{--}5\text{ s}$)**: The furnace is rapidly heated at $> 2000^\circ\text{C/s}$ under stopped purge gas flow. Analyte vaporizes into a stagnant, hot argon atmosphere, generating a transient absorbance peak.
4. **Clean / Bakeout Stage ($2600\text{--}2800^\circ\text{C}$, $3\text{ s}$)**: A blast of purge gas expels any refractory residues to prevent cross-run memory effects.

### Sensitivity Comparison: Flame AAS vs GFAAS
- **Flame AAS**: Sample is diluted into high gas flow; residence time in light path is $\sim 10^{-4}\text{ s}$. Detection limits: $1\text{--}100\,\mu\text{g}\cdot\text{L}^{-1}$ ($\text{ppb}$).
- **GFAAS**: $100\%$ of injected mass ($20\,\mu\text{L}$) is atomized into a confined tube; residence time is $\sim 1\text{ s}$ ($10,000\times$ longer). Absolute detection limits: $10^{-12}\text{ to }10^{-14}\text{ g}$ ($1\text{--}10\text{ picograms}$), representing a **$100\text{ to }1000\text{-fold}$ sensitivity enhancement** over flame.""",
                    "simulations": []
                },
                {
                    "id": "sec-5-7",
                    "secNumber": "5.7",
                    "title": "Background Correction Systems: Deuterium Continuum, Zeeman & Smith-Hieftje",
                    "content": r"""In graphite furnace and complex flame matrices, non-specific attenuation (broadband molecular absorption from matrix salts such as $\text{NaCl}$, plus light scattering from unvaporized smoke particles) creates severe false-positive background absorbance ($A_{\text{total}} = A_{\text{analyte}} + A_{\text{background}}$). Eliminating background requires advanced instrumental correction systems:

### 1. Deuterium ($\text{D}_2$) Continuum Background Correction
Utilizes two co-aligned light sources chopped alternately through the atom cell:
1. **Hollow Cathode Lamp (HCL)**: Emits sharp atomic resonance lines. Absorbed by both analyte atoms and broadband background:
$$A_1 = A_{\text{analyte}} + A_{\text{background}}$$
2. **Deuterium Arc Lamp ($\text{D}_2$)**: Emits a broad continuous spectrum over $190\text{--}400\text{ nm}$. Because the atomic line is tiny ($0.002\text{ nm}$) relative to the monochromator bandpass ($0.5\text{ nm}$), analyte atoms absorb $< 0.5\%$ of the continuum light. The $\text{D}_2$ lamp measures strictly the broadband background:
$$A_2 \approx A_{\text{background}}$$
3. **Electronic Subtraction**:
$$A_{\text{corrected}} = A_1 - A_2 = A_{\text{analyte}}$$
*Limitations*: Ineffective above $380\text{ nm}$ (where $\text{D}_2$ intensity drops) and fails when background exhibits structured molecular absorption lines within the monochromator bandpass.

### 2. Zeeman Effect Background Correction
The most powerful, universal correction system, utilizing quantum mechanical splitting of atomic energy levels under an intense magnetic field ($B \approx 0.8\text{--}1.0\text{ Tesla}$).

```
                  Normal Zeeman Splitting in a Magnetic Field
                    Zero Magnetic Field (B = 0)        Applied Field (B ≈ 1 Tesla)
                                                          σ⁺ Component (Parallel - ΔM = +1)
                                                       ┌─── λ₀ - Δλ_Z
                    Single Resonance Line              │
                    ─────────────────────  ────────►   ├─── π Component (Perpendicular - ΔM = 0)
                            λ₀                         │    λ₀ (Analyte + Background)
                                                       │
                                                       └─── σ⁻ Component (Parallel - ΔM = -1)
                                                            λ₀ + Δλ_Z
```

#### Transverse AC Zeeman Geometry
1. An electromagnet surrounds the graphite furnace perpendicular to the optical beam.
2. When the magnetic field is turned **OFF ($B = 0$)**: The detector measures total absorption (atomic resonance + broadband background):
$$A_{\text{field off}} = A_{\text{analyte}} + A_{\text{background}}$$
3. When the magnetic field is turned **ON ($B \approx 1\text{ T}$)**: The atomic absorption line splits into:
   - A central $\pi$ component at $\lambda_0$, polarized parallel to the magnetic field.
   - Two side $\sigma^\pm$ components shifted symmetrically away from $\lambda_0$ by $\Delta \lambda_Z = \pm \frac{e B}{4\pi m_e c} \lambda_0^2 \approx \pm 0.01\text{ nm}$, polarized perpendicular to the field.
4. A static linear polarizer transmits only light polarized perpendicular to the magnetic field. Consequently, the central $\pi$ component is blocked, and the $\sigma$ components are shifted completely outside the narrow HCL emission profile!
   Analyte atoms cannot absorb light at $\lambda_0$. However, broadband background molecules are unaffected by the magnetic field and absorb normally:
$$A_{\text{field on}} = A_{\text{background}}$$
5. Real-time subtraction yields pure analyte signal:
$$A_{\text{net}} = A_{\text{field off}} - A_{\text{field on}} = A_{\text{analyte}}$$
*Advantages*: Uses the exact same light source and path; corrects up to $A_{\text{background}} \approx 2.0$ across all wavelengths ($190\text{--}900\text{ nm}$).

### 3. Smith-Hieftje High-Current Pulse Background Correction
Exploits lamp self-reversal without requiring external magnets:
1. The HCL is driven alternately with **low current ($5\text{ mA}$)** and **high-current pulses ($300\text{--}500\text{ mA}$)**.
2. At low current: Emits a sharp line $\to$ measures $A_{\text{analyte}} + A_{\text{background}}$.
3. At high current: Sputters a dense cold atom cloud inside the cathode cavity $\to$ the center of the resonance line self-reverses completely. The emission dip prevents analyte absorption, leaving only emission wings that measure $A_{\text{background}}$.
4. Subtraction yields $A_{\text{analyte}}$. Economical and robust, though it shortens lamp lifetime.""",
                    "simulations": []
                }
            ],
            "problems": [
                {
                    "id": "prob-5-1",
                    "problemNumber": "5.1",
                    "title": "Boltzmann Population Calculation of Sodium and Magnesium in Flames",
                    "difficulty": "Foundational",
                    "statement": r"""1. The yellow resonance doublet of sodium occurs at an average wavelength of $\lambda = 589.0\text{ nm}$. The ground state is $3s \ ^2S_{1/2}$ ($g_0 = 2$) and the excited state is $3p \ ^2P_{3/2}$ ($g_j = 4$).
   Calculate the Boltzmann excited-to-ground state population ratio $N_j / N_0$ for sodium in an air-acetylene flame at $T_1 = 2500\text{ K}$ and an oxy-acetylene flame at $T_2 = 3000\text{ K}$.
2. The resonance line of magnesium occurs at $\lambda = 285.2\text{ nm}$. The ground state is $3s^2 \ ^1S_0$ ($g_0 = 1$) and the excited state is $3s3p \ ^1P_1$ ($g_j = 3$).
   Calculate $N_j / N_0$ for magnesium at $T = 2500\text{ K}$.
3. Calculate the percentage increase in emission signal for sodium when flame temperature increases by $10\text{ K}$ from $2500\text{ K}$ to $2510\text{ K}$, and compare this with the stability of the atomic absorption signal.
(Constants: $h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}$, $c = 2.998 \times 10^8\text{ m}\cdot\text{s}^{-1}$, $k_B = 1.3806 \times 10^{-23}\text{ J}\cdot\text{K}^{-1}$).""",
                    "solution": r"""### Step 1: Sodium Population Ratio ($N_j / N_0$)
Transition energy for sodium ($\lambda = 589.0\text{ nm} = 5.890 \times 10^{-7}\text{ m}$):
$$\Delta E = \frac{h c}{\lambda} = \frac{(6.626 \times 10^{-34}\text{ J}\cdot\text{s})(2.998 \times 10^8\text{ m/s})}{5.890 \times 10^{-7}\text{ m}} = 3.3726 \times 10^{-19}\text{ J}$$
Converting to $\text{eV}$:
$$\Delta E = \frac{3.3726 \times 10^{-19}\text{ J}}{1.6022 \times 10^{-19}\text{ J/eV}} = 2.105\text{ eV}$$

1. At $T_1 = 2500\text{ K}$:
$$k_B T_1 = (1.3806 \times 10^{-23})(2500) = 3.4515 \times 10^{-20}\text{ J}$$
$$\frac{\Delta E}{k_B T_1} = \frac{3.3726 \times 10^{-19}}{3.4515 \times 10^{-20}} = 9.7714$$
$$\frac{N_j}{N_0} = \frac{g_j}{g_0} \exp\left(-\frac{\Delta E}{k_B T_1}\right) = \left(\frac{4}{2}\right) e^{-9.7714} = 2 \times (5.706 \times 10^{-5}) = \mathbf{1.141 \times 10^{-4} \ (0.0114\%)}$$

2. At $T_2 = 3000\text{ K}$:
$$k_B T_2 = (1.3806 \times 10^{-23})(3000) = 4.1418 \times 10^{-20}\text{ J}$$
$$\frac{\Delta E}{k_B T_2} = \frac{3.3726 \times 10^{-19}}{4.1418 \times 10^{-20}} = 8.1428$$
$$\frac{N_j}{N_0} = 2 \times e^{-8.1428} = 2 \times (2.908 \times 10^{-4}) = \mathbf{5.816 \times 10^{-4} \ (0.0582\%)}$$
Raising temperature from $2500\text{ K}$ to $3000\text{ K}$ increases the excited fraction by more than a factor of $5$!

### Step 2: Magnesium Population Ratio at 2500 K
Transition energy ($\lambda = 285.2\text{ nm} = 2.852 \times 10^{-7}\text{ m}$):
$$\Delta E = \frac{(6.626 \times 10^{-34})(2.998 \times 10^8)}{2.852 \times 10^{-7}} = 6.9652 \times 10^{-19}\text{ J} = 4.347\text{ eV}$$
At $T = 2500\text{ K}$:
$$\frac{\Delta E}{k_B T} = \frac{6.9652 \times 10^{-19}}{3.4515 \times 10^{-20}} = 20.180$$
$$\frac{N_j}{N_0} = \left(\frac{3}{1}\right) e^{-20.180} = 3 \times (1.7215 \times 10^{-9}) = \mathbf{5.165 \times 10^{-9}}$$
Only $5$ out of every billion magnesium atoms are excited at $2500\text{ K}$.

### Step 3: Temperature Sensitivity Comparison (Emission vs Absorption)
At $T = 2510\text{ K}$:
$$\frac{\Delta E}{k_B T} = \frac{3.3726 \times 10^{-19}}{(1.3806 \times 10^{-23})(2510)} = \frac{3.3726 \times 10^{-19}}{3.4653 \times 10^{-20}} = 9.7325$$
$$\left(\frac{N_j}{N_0}\right)_{2510} = 2 \times e^{-9.7325} = 2 \times (5.932 \times 10^{-5}) = 1.1865 \times 10^{-4}$$
Percentage change in emission signal ($I_{\text{em}} \propto N_j$):
$$\% \Delta I_{\text{em}} = \left(\frac{1.1865 \times 10^{-4} - 1.1412 \times 10^{-4}}{1.1412 \times 10^{-4}}\right) \times 100\% = \mathbf{+3.97\%}$$
A tiny fluctuation of only $10\text{ K}$ causes a **$\sim 4\%$ error in atomic emission**!

For atomic absorption ($A \propto N_0$):
$$N_0 = N_{\text{total}} - N_j \approx N_{\text{total}} (1 - 0.000114)$$
The fractional change in $N_0$ is:
$$\% \Delta N_0 \approx 0.004\% \ (40\text{ ppm})$$
The atomic absorption signal varies by less than $0.004\%$, proving why AAS is orders of magnitude less sensitive to flame temperature fluctuations than AES.""",
                    "hints": ["Calculate Delta E = h * c / lambda in Joules first.", "Ratio N_j / N_0 = (g_j / g_0) * exp(-Delta E / (k_B * T))."]
                },
                {
                    "id": "prob-5-2",
                    "problemNumber": "5.2",
                    "title": "Doppler and Collisional Linewidth Derivation for Cadmium in Flames",
                    "difficulty": "Intermediate",
                    "statement": r"""Cadmium is determined by flame AAS at its primary resonance line:
$$\lambda_0 = 228.80\text{ nm} \quad (M_{\text{Cd}} = 112.41\text{ g}\cdot\text{mol}^{-1})$$
The air-acetylene flame operates at $T = 2450\text{ K}$.
1. Calculate the Doppler broadening full-width at half-maximum in both frequency ($\Delta \nu_D$, in $\text{Hz}$) and wavelength ($\Delta \lambda_D$, in $\text{nm}$).
2. If the collisional (Lorentz) broadening at atmospheric pressure is estimated as $\Delta \lambda_L = 0.0032\text{ nm}$, calculate the total Voigt profile linewidth $\Delta \lambda_{\text{total}}$ using the empirical approximation $\Delta \lambda_{\text{total}} \approx \frac{\Delta \lambda_L}{2} + \sqrt{\left(\frac{\Delta \lambda_L}{2}\right)^2 + (\Delta \lambda_D)^2}$.
3. Compare the total absorption linewidth with the bandpass of a monochromator possessing a reciprocal linear dispersion of $D^{-1} = 2.0\text{ nm/mm}$ and an exit slit width of $w = 0.50\text{ mm}$.""",
                    "solution": r"""### Step 1: Doppler Broadening Calculation
Doppler fractional linewidth equation:
$$\frac{\Delta \lambda_D}{\lambda_0} = 7.16 \times 10^{-7} \sqrt{\frac{T}{M}}$$
Substitute $T = 2450\text{ K}$ and $M = 112.41\text{ g/mol}$:
$$\frac{\Delta \lambda_D}{\lambda_0} = 7.16 \times 10^{-7} \sqrt{\frac{2450}{112.41}} = 7.16 \times 10^{-7} \sqrt{21.795} = 7.16 \times 10^{-7} \times 4.6685 = 3.3427 \times 10^{-6}$$
Doppler linewidth in wavelength:
$$\Delta \lambda_D = (228.80\text{ nm}) \times (3.3427 \times 10^{-6}) = \mathbf{7.648 \times 10^{-4}\text{ nm} = 0.000765\text{ nm} \ (0.765\text{ pm})}$$

Doppler linewidth in frequency:
$$\nu_0 = \frac{c}{\lambda_0} = \frac{2.998 \times 10^8\text{ m/s}}{2.2880 \times 10^{-7}\text{ m}} = 1.3103 \times 10^{15}\text{ Hz}$$
$$\Delta \nu_D = \nu_0 \times (3.3427 \times 10^{-6}) = (1.3103 \times 10^{15}) \times (3.3427 \times 10^{-6}) = \mathbf{4.380 \times 10^9\text{ Hz} = 4.38\text{ GHz}}$$

### Step 2: Total Voigt Linewidth
Given $\Delta \lambda_L = 0.0032\text{ nm}$ and $\Delta \lambda_D = 0.000765\text{ nm}$:
$$\frac{\Delta \lambda_L}{2} = 0.0016\text{ nm}$$
$$\Delta \lambda_{\text{total}} \approx 0.0016 + \sqrt{(0.0016)^2 + (0.000765)^2} = 0.0016 + \sqrt{2.56 \times 10^{-6} + 0.585 \times 10^{-6}} = 0.0016 + \sqrt{3.145 \times 10^{-6}} = 0.0016 + 0.001773 = \mathbf{0.00337\text{ nm} \ (3.37\text{ pm})}$$
Notice that collisional broadening dominates for heavy elements at atmospheric pressure.

### Step 3: Comparison with Monochromator Bandpass
Monochromator effective bandpass:
$$\Delta \lambda_{\text{mono}} = w \cdot D^{-1} = (0.50\text{ mm}) \times (2.0\text{ nm/mm}) = \mathbf{1.00\text{ nm}}$$
Ratio of monochromator bandpass to atomic linewidth:
$$\frac{\Delta \lambda_{\text{mono}}}{\Delta \lambda_{\text{total}}} = \frac{1.00\text{ nm}}{0.00337\text{ nm}} = \mathbf{297}$$
The monochromator transmits a band that is nearly **$300\text{ times broader}$** than the atomic absorption line, proving why a continuous light source cannot be utilized in AAS without losing virtually all sensitivity.""",
                    "hints": ["Use Delta lambda_D / lambda_0 = 7.16e-7 * sqrt(T / M).", "Monochromator bandpass is slit width multiplied by reciprocal linear dispersion."]
                },
                {
                    "id": "prob-5-3",
                    "problemNumber": "5.3",
                    "title": "Diffraction Grating Dispersion, Blaze Angle and Resolving Power",
                    "difficulty": "Intermediate",
                    "statement": r"""A Czerny-Turner monochromator in an atomic absorption spectrometer uses a reflection grating ruled with $1800\text{ grooves/mm}$ over a width of $50.0\text{ mm}$. The focal length of the collimating and focusing mirrors is $f = 400\text{ mm}$.
1. Calculate the groove spacing $d$ in nanometers.
2. Calculate the reciprocal linear dispersion $D^{-1}$ (in $\text{nm/mm}$) in first order ($n = 1$) near the normal ($\beta \approx 0$).
3. What exit slit width $w$ (in $\mu\text{m}$) must be set to achieve an effective spectral bandpass of $\Delta \lambda_{\text{eff}} = 0.20\text{ nm}$?
4. Calculate the theoretical chromatic resolving power $R$ in first order, and find the minimum wavelength difference $\Delta \lambda$ that can be resolved near $\lambda = 300.0\text{ nm}$.""",
                    "solution": r"""### Step 1: Groove Spacing ($d$)
$$d = \frac{1\text{ mm}}{1800\text{ grooves}} = \frac{1.0 \times 10^{-3}\text{ m}}{1800} = 5.5556 \times 10^{-7}\text{ m} = \mathbf{555.56\text{ nm}}$$

### Step 2: Reciprocal Linear Dispersion ($D^{-1}$)
For first order ($n = 1$) and near-normal diffraction ($\cos \beta \approx 1$):
$$D^{-1} = \frac{d \cos \beta}{n \cdot f} = \frac{555.56\text{ nm}}{1 \times (400\text{ mm})} = \mathbf{1.3889\text{ nm/mm}}$$

### Step 3: Required Slit Width for 0.20 nm Bandpass
By definition:
$$\Delta \lambda_{\text{eff}} = w \cdot D^{-1} \implies w = \frac{\Delta \lambda_{\text{eff}}}{D^{-1}}$$
$$w = \frac{0.20\text{ nm}}{1.3889\text{ nm/mm}} = 0.1440\text{ mm} = \mathbf{144\,\mu\text{m}}$$

### Step 4: Chromatic Resolving Power ($R$)
Total number of ruled grooves:
$$N_{\text{total}} = (1800\text{ grooves/mm}) \times (50.0\text{ mm}) = 90,000\text{ grooves}$$
Resolving power in first order:
$$R = n \cdot N_{\text{total}} = 1 \times 90,000 = \mathbf{90,000}$$
Minimum resolvable wavelength separation at $\lambda = 300.0\text{ nm}$:
$$R = \frac{\lambda}{\Delta \lambda} \implies \Delta \lambda = \frac{\lambda}{R} = \frac{300.0\text{ nm}}{90,000} = \mathbf{0.00333\text{ nm} = 3.33\text{ pm}}$$""",
                    "hints": ["Groove spacing d = 1 / grooves_per_mm.", "Reciprocal linear dispersion D^-1 = d / f for normal diffraction in first order."]
                },
                {
                    "id": "prob-5-4",
                    "problemNumber": "5.4",
                    "title": "Quantum Zeeman Splitting Energy and Polarization Vector Resolution",
                    "difficulty": "Honors Problem",
                    "statement": r"""A transverse AC Zeeman atomic absorption spectrometer applies a magnetic field of $B = 0.90\text{ Tesla}$ across a graphite furnace tube.
The normal Zeeman effect splits an atomic resonance line ($\lambda_0 = 285.213\text{ nm}$, magnesium $^1S_0 \to \ ^1P_1$) into a central $\pi$ component and two symmetrically displaced $\sigma^\pm$ components according to:
$$\Delta E_Z = \mu_B \cdot B \cdot \Delta M_J$$
where $\mu_B = \frac{e\hbar}{2 m_e} = 9.274 \times 10^{-24}\text{ J}\cdot\text{T}^{-1}$ (the Bohr magneton) and $\Delta M_J = 0$ for the $\pi$ component, $\Delta M_J = \pm 1$ for the $\sigma^\pm$ components.

1. Calculate the Zeeman energy shift $\Delta E_Z$ (in Joules and $\text{eV}$) for the $\sigma^\pm$ transitions.
2. Calculate the corresponding frequency shift $\Delta \nu_Z$ and wavelength shift $\Delta \lambda_Z$ (in $\text{nm}$).
3. Explain how a static linear polarizer oriented perpendicular to the magnetic field vector isolates the non-specific background absorbance during the field-on cycle.""",
                    "solution": r"""### Step 1: Zeeman Energy Shift
For $\Delta M_J = \pm 1$ and $B = 0.90\text{ T}$:
$$\Delta E_Z = \mu_B \cdot B = (9.274 \times 10^{-24}\text{ J}\cdot\text{T}^{-1}) \times (0.90\text{ T}) = \mathbf{8.3466 \times 10^{-24}\text{ J}}$$
In electron-volts:
$$\Delta E_Z = \frac{8.3466 \times 10^{-24}\text{ J}}{1.6022 \times 10^{-19}\text{ J/eV}} = \mathbf{5.209 \times 10^{-5}\text{ eV}}$$

### Step 2: Frequency and Wavelength Shifts
Frequency shift:
$$\Delta \nu_Z = \frac{\Delta E_Z}{h} = \frac{8.3466 \times 10^{-24}\text{ J}}{6.626 \times 10^{-34}\text{ J}\cdot\text{s}} = \mathbf{1.2597 \times 10^{10}\text{ Hz} = 12.60\text{ GHz}}$$
Wavelength shift ($\Delta \lambda_Z = \frac{\lambda_0^2}{c} \Delta \nu_Z$):
$$\lambda_0 = 285.213\text{ nm} = 2.85213 \times 10^{-7}\text{ m}$$
$$\Delta \lambda_Z = \frac{(2.85213 \times 10^{-7}\text{ m})^2}{2.998 \times 10^8\text{ m/s}} \times (1.2597 \times 10^{10}\text{ s}^{-1}) = \frac{8.1346 \times 10^{-14}}{2.998 \times 10^8} \times (1.2597 \times 10^{10}) = (2.7133 \times 10^{-22}) \times (1.2597 \times 10^{10}) = 3.418 \times 10^{-12}\text{ m} = \mathbf{0.00342\text{ nm} = 3.42\text{ pm}}$$

### Step 3: Optical Isolation Mechanism via Polarization
- In transverse Zeeman geometry, the magnetic field $\mathbf{B}$ is oriented vertically.
- When $B = 0.90\text{ T}$ is active:
  - The $\pi$ component remains exactly at $\lambda_0$ ($285.213\text{ nm}$), but its electric vector is polarized **parallel** to $\mathbf{B}$ (vertical).
  - The $\sigma^\pm$ components are shifted by $\pm 0.00342\text{ nm}$ away from $\lambda_0$, outside the sharp HCL emission profile ($0.001\text{ nm}$). Their electric vectors are polarized **perpendicular** to $\mathbf{B}$ (horizontal).
- A static linear polarizer installed in the beam path is oriented **horizontally** (perpendicular to $\mathbf{B}$).
  - It completely blocks the vertically polarized $\pi$ component.
  - The horizontally polarized $\sigma^\pm$ components cannot absorb light at $\lambda_0$ because their absorption wavelengths have been shifted away.
  - Consequently, **analyte atoms absorb zero light** at $\lambda_0$ during the field-on cycle!
  - Unstructured background smoke and molecular absorption bands are non-magnetic and unpolarized; they absorb horizontal photons normally.
- Thus, the field-on cycle measures pure $A_{\text{background}}$, which is electronically subtracted from the field-off cycle ($A_{\text{analyte}} + A_{\text{background}}$) to yield flawless background correction.""",
                    "hints": ["Zeeman energy shift is mu_B * B.", "Wavelength shift Delta lambda = lambda^2 / c * Delta nu."]
                },
                {
                    "id": "prob-5-5",
                    "problemNumber": "5.5",
                    "title": "Method of Standard Additions in GFAAS Blood Lead Analysis",
                    "difficulty": "Intermediate",
                    "statement": r"""Blood lead ($\text{Pb}$) analysis by GFAAS suffers from severe matrix suppression caused by residual sodium chloride and organic protein residue. To eliminate matrix effects, an analyst uses the **Method of Standard Additions**.
Equal $0.500\text{-mL}$ aliquots of whole blood are spiked with increasing volumes of a $10.0\,\mu\text{g}\cdot\text{mL}^{-1}$ lead standard, diluted to $10.00\text{ mL}$ with a matrix modifier solution ($0.2\text{ wt}\% \ \text{NH}_4\text{H}_2\text{PO}_4 + 0.1\text{ wt}\% \ \text{Triton X-100}$), and analyzed by GFAAS at $283.3\text{ nm}$:

| Flask | Blood Aliquot (mL) | Lead Spike Volume (mL) | Spike Added ($\mu\text{g/mL}$ in flask) | Absorbance ($A$) |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0.500 | 0.000 | 0.000 | 0.142 |
| 2 | 0.500 | 0.050 | 0.050 | 0.285 |
| 3 | 0.500 | 0.100 | 0.100 | 0.431 |
| 4 | 0.500 | 0.150 | 0.150 | 0.570 |

1. Perform a linear least-squares regression of absorbance ($y$) versus added standard concentration ($x$, in $\mu\text{g/mL}$).
2. Calculate the lead concentration $C_{\text{flask}}$ in the diluted measurement solution from the $x$-intercept.
3. Calculate the original lead concentration in the undiluted blood sample in $\mu\text{g}\cdot\text{dL}^{-1}$.""",
                    "solution": r"""### Step 1: Linear Least-Squares Regression
Data points ($x_i, y_i$) for $N = 4$:
- $(0.000, 0.142)$
- $(0.050, 0.285)$
- $(0.100, 0.431)$
- $(0.150, 0.570)$

Summations:
- $\sum x_i = 0.000 + 0.050 + 0.100 + 0.150 = 0.300 \implies \bar{x} = 0.075\,\mu\text{g/mL}$
- $\sum y_i = 0.142 + 0.285 + 0.431 + 0.570 = 1.428 \implies \bar{y} = 0.357$
- $\sum x_i^2 = 0 + 0.0025 + 0.0100 + 0.0225 = 0.0350$
- $S_{xx} = \sum x_i^2 - \frac{(\sum x_i)^2}{N} = 0.0350 - \frac{0.0900}{4} = 0.0350 - 0.0225 = 0.0125$
- $\sum x_i y_i = (0)(0.142) + (0.050)(0.285) + (0.100)(0.431) + (0.150)(0.570) = 0 + 0.01425 + 0.04310 + 0.08550 = 0.14285$
- $S_{xy} = \sum x_i y_i - \frac{(\sum x_i)(\sum y_i)}{N} = 0.14285 - \frac{(0.300)(1.428)}{4} = 0.14285 - 0.10710 = 0.03575$

Slope ($m$):
$$m = \frac{S_{xy}}{S_{xx}} = \frac{0.03575}{0.0125} = \mathbf{2.860\,(\mu\text{g/mL})^{-1}}$$
Intercept ($c$):
$$c = \bar{y} - m\bar{x} = 0.357 - (2.860)(0.075) = 0.357 - 0.2145 = \mathbf{0.1425}$$
Calibration equation: $A = 2.860\,C_{\text{added}} + 0.1425$.

### Step 2: Diluted Concentration from $x$-Intercept
Setting $A = 0$:
$$C_{\text{flask}} = \frac{c}{m} = \frac{0.1425}{2.860} = \mathbf{0.04983\,\mu\text{g}\cdot\text{mL}^{-1}}$$

### Step 3: Lead Concentration in Original Blood Sample
Dilution factor:
$$\text{DF} = \frac{V_{\text{flask}}}{V_{\text{blood}}} = \frac{10.00\text{ mL}}{0.500\text{ mL}} = 20.0$$
Concentration in blood:
$$C_{\text{blood}} = C_{\text{flask}} \times \text{DF} = 0.04983\,\mu\text{g/mL} \times 20.0 = \mathbf{0.9965\,\mu\text{g}\cdot\text{mL}^{-1}}$$
Converting to $\mu\text{g}\cdot\text{dL}^{-1}$ ($1\text{ dL} = 100\text{ mL}$):
$$C_{\text{blood}} = 0.9965\,\mu\text{g/mL} \times 100\text{ mL/dL} = \mathbf{99.65\,\mu\text{g}\cdot\text{dL}^{-1}}$$
*Clinical Diagnostic Note*: An adult blood lead level of $\sim 100\,\mu\text{g/dL}$ indicates severe, life-threatening acute lead poisoning requiring immediate chelation therapy (e.g. with EDTA or dimercaprol).""",
                    "hints": ["In standard addition, the unknown concentration in the diluted flask is intercept / slope.", "Multiply by the dilution factor (10.0 / 0.50) to get the original blood concentration."]
                },
                {
                    "id": "prob-5-6",
                    "problemNumber": "5.6",
                    "title": "Refractory Oxide Dissociation Thermodynamics in N2O-Acetylene Flames",
                    "difficulty": "Honors Problem",
                    "statement": r"""Aluminum cannot be detected by flame AAS in an air-acetylene flame ($T = 2300^\circ\text{C}$), but yields high sensitivity in a fuel-rich nitrous oxide-acetylene flame ($T = 2950^\circ\text{C}$).
Given:
- Dissociation enthalpy of aluminum monoxide gas: $\text{AlO}(g) \rightleftharpoons \text{Al}(g) + \text{O}(g) \quad (\Delta H^\circ_{\text{diss}} = +512\text{ kJ}\cdot\text{mol}^{-1})$
- Dissociation enthalpy of copper monoxide gas: $\text{CuO}(g) \rightleftharpoons \text{Cu}(g) + \text{O}(g) \quad (\Delta H^\circ_{\text{diss}} = +268\text{ kJ}\cdot\text{mol}^{-1})$

1. Using the van 't Hoff equation $\ln\left(\frac{K_2}{K_1}\right) = -\frac{\Delta H^\circ}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$, calculate the ratio by which the dissociation equilibrium constant $K_p$ for $\text{AlO}$ increases when switching from $T_1 = 2573\text{ K}$ ($2300^\circ\text{C}$) to $T_2 = 3223\text{ K}$ ($2950^\circ\text{C}$).
2. Explain the crucial chemical role of cyanogen ($:\text{CN}$) and dicarbon ($:\text{C}_2$) radicals in the fuel-rich $\text{N}_2\text{O}-\text{C}_2\text{H}_2$ "red feather" zone.""",
                    "solution": r"""### Step 1: van 't Hoff Equilibrium Ratio Calculation
$$\Delta H^\circ = 512,000\text{ J}\cdot\text{mol}^{-1}, \quad R = 8.314\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$$
$$T_1 = 2573.15\text{ K}, \quad T_2 = 3223.15\text{ K}$$
Inverse temperature difference:
$$\frac{1}{T_2} - \frac{1}{T_1} = \frac{1}{3223.15} - \frac{1}{2573.15} = 3.10255 \times 10^{-4} - 3.8863 \times 10^{-4} = -7.8375 \times 10^{-5}\text{ K}^{-1}$$

Evaluate the van 't Hoff exponent:
$$\ln\left(\frac{K_2}{K_1}\right) = -\frac{512,000\text{ J/mol}}{8.314\text{ J/mol}\cdot\text{K}} \times (-7.8375 \times 10^{-5}\text{ K}^{-1}) = -(61582.8) \times (-7.8375 \times 10^{-5}) = +4.8265$$
Taking the exponential:
$$\frac{K_2}{K_1} = \exp(4.8265) = \mathbf{124.8}$$
The dissociation equilibrium constant $K_p$ for $\text{AlO}$ increases by a factor of **$125$** simply due to the higher flame temperature!

### Step 2: Role of Scavenging Radicals in the "Red Feather" Zone
In addition to the higher temperature, fuel-rich $\text{N}_2\text{O}-\text{C}_2\text{H}_2$ flames possess a distinct luminous interzonal region known as the **"red feather" zone**.
1. This zone is rich in highly reactive reducing radicals: cyanogen ($:\text{CN}$), dicarbon ($:\text{C}_2$), and methylidyne ($:\text{CH}$).
2. These carbonaceous radicals act as ferocious oxygen scavengers:
$$\text{AlO}(g) + :\text{CN}(g) \to \text{Al}(g) + \text{OCN}(g) \quad (\Delta H \ll 0)$$
$$\text{AlO}(g) + \text{C}(g) \to \text{Al}(g) + \text{CO}(g) \quad (\Delta H^\circ = -564\text{ kJ/mol})$$
3. By reducing the partial pressure of atomic oxygen ($P_{\text{O}}$) in the flame to $< 10^{-8}\text{ bar}$, Le Châtelier's principle shifts the dissociation equilibrium completely to the right, liberating free neutral ground-state aluminum atoms ($\text{Al}^0$) for atomic absorption measurement.""",
                    "hints": ["Use the van 't Hoff equation with Delta H in J/mol.", "Temperature in Kelvin: T(K) = T(C) + 273.15."]
                },
                {
                    "id": "prob-5-7",
                    "problemNumber": "5.7",
                    "title": "Comparison of Instrumental Figures of Merit: AAS vs AES vs AFS",
                    "difficulty": "Foundational",
                    "statement": r"""Compare Atomic Absorption Spectroscopy (AAS), Atomic Emission Spectroscopy (AES), and Atomic Fluorescence Spectroscopy (AFS) across the following instrumental and performance parameters:
1. Primary light source requirement.
2. Optical geometry (angle of detector relative to source/flame).
3. Primary source of analytical signal and relationship to analyte concentration.
4. Sensitivity to flame temperature fluctuations.
5. Multielement simultaneous analysis capability.""",
                    "solution": r"""### Comprehensive Comparison of AAS, AES, and AFS

| Parameter | Atomic Absorption (AAS) | Atomic Emission (AES / ICP-OES) | Atomic Fluorescence (AFS) |
| :--- | :--- | :--- | :--- |
| **1. Light Source** | Requires element-specific line source (Hollow Cathode Lamp, HCL) | No external light source; excitation is purely thermal | High-intensity source (Xenon arc, hollow cathode, tunable laser) |
| **2. Optical Geometry** | Collinear ($180^\circ$ linear path: HCL $\to$ Flame $\to$ Monochromator) | Direct line-of-sight ($0^\circ$ to flame or radial/axial to ICP torch) | Perpendicular ($90^\circ$ detection) to eliminate source transmission scatter |
| **3. Analytical Signal** | Absorbance: $A = \log_{10}(I_0 / I) \propto N_0 \cdot b \cdot c$ (governed by Beer's law) | Radiant emission intensity: $I_{\text{em}} \propto N_j \propto c \cdot \exp(-\Delta E / k_B T)$ | Fluorescence intensity: $I_F \propto I_0 \cdot \phi \cdot N_0 \cdot c$ (linear with source power $I_0$) |
| **4. Temperature Sensitivity** | Minimal sensitivity: $> 99.9\%$ of atoms reside in ground state $N_0$ | Extreme exponential sensitivity via Boltzmann factor $\exp(-\Delta E / k_B T)$ | Minimal sensitivity (fluorescence originates from ground state $N_0$) |
| **5. Multielement Analysis** | Primarily sequential single-element (each element requires its own HCL) | Exceptional simultaneous multielement (up to 70 elements in ICP-OES) | Primarily single-element or dual-element (limited commercial multielement) |

*Key Analytical Insight*:
- **AAS** remains the global reference standard for dedicated, robust, low-cost single-element determinations in clinical and environmental laboratories.
- **ICP-AES / ICP-OES** dominates high-throughput industrial and geological laboratories requiring rapid simultaneous quantification of dozens of elements across 5 to 6 orders of linear dynamic range.
- **AFS** excels specifically in sub-ppb trace analysis of hydride-forming elements ($\text{As, Se, Sb, Bi}$) and cold-vapor mercury ($\text{Hg}$) due to near-zero background at $90^\circ$ detection.""",
                    "hints": ["AAS measures absorption at 180 degrees; AES measures thermal emission; AFS measures fluorescence at 90 degrees.", "Consider the Boltzmann temperature dependence for emission vs absorption."]
                }
            ]
        },

        # =====================================================================
        # UNIT 6
        # =====================================================================
        {
            "id": "unit-6-ion-exchange-methods",
            "unitNumber": 6,
            "title": "Unit 6: Ion-Exchange Chromatography: Resins, Equilibria & Analytical Separations",
            "leadSummary": "Comprehensive physical and analytical chemistry of ion-exchange resins: cross-linked polystyrene-divinylbenzene (PS-DVB) matrices, functional group classifications (SAC, WAC, SBA, WBA), mass-action selectivity coefficients, column dynamics and breakthrough capacity curves, and quantitative separations of zinc from magnesium and chloride from bromide.",
            "simulations": ["sim_chem_ion_exchange_breakthrough_curve"],
            "sections": [
                {
                    "id": "sec-6-1",
                    "secNumber": "6.1",
                    "title": "Ion-Exchange Resin Macromolecular Architecture: PS-DVB Matrices & Swelling",
                    "content": r"""**Ion-exchange chromatography (IEC)** is a liquid chromatographic separation technique based on the reversible electrostatic stoichiometric exchange of ions in an aqueous mobile phase with counter-ions bound to an insoluble, solid macromolecular matrix (**ion-exchange resin**).

### Macromolecular Architecture of Synthetic Resins
Modern analytical ion-exchange resins are synthesized by suspension copolymerization of **styrene** with **divinylbenzene (DVB)**, producing spherical, cross-linked copolymer beads.

```
                  Cross-Linked Polystyrene-Divinylbenzene (PS-DVB)
              -CH-CH₂-CH-CH₂-CH-CH₂-CH-CH₂-
               │       │       │       │
              (C₆H₄)  (C₆H₄)  (C₆H₄)  (C₆H₄)
               │       │       │       │
               │      -CH-CH₂-CH-CH₂-  │   ◄── Divinylbenzene Cross-Link Bridge
               │       │       │       │       (typically 4% to 12% DVB)
              (C₆H₄)  (C₆H₄)  (C₆H₄)  (C₆H₄)
               │       │       │       │
              -CH-CH₂-CH-CH₂-CH-CH₂-CH-CH₂-
                       │
                     -SO₃⁻ H⁺  ◄── Functionalized Fixed Ionic Site (SAC)
```

#### Degree of Cross-Linking (% DVB)
Divinylbenzene acts as a bifunctional bridging agent that connects adjacent linear polystyrene chains into a 3D network:
- **Low Cross-Linking ($2\text{--}4\text{ wt}\% \ \text{DVB}$)**: Highly flexible, porous network that swells excessively in water. Facilitates rapid mass-transfer diffusion of large hydrated ions or biopolymers, but exhibits poor mechanical strength and crushes under column pressure.
- **Medium Cross-Linking ($8\text{ wt}\% \ \text{DVB}$, e.g., Dowex 50W-X8)**: The standard analytical benchmark. Balances mechanical rigidity with rapid ionic diffusion kinetics.
- **High Cross-Linking ($12\text{--}16\text{ wt}\% \ \text{DVB}$)**: Rigid, dense, non-swelling network with narrow micropores. Displays exceptional mechanical stability and high selectivity for small ions, but excludes large hydrated complexes due to steric hindrance.

### Resin Swelling Thermodynamics
When dry ion-exchange resin beads are immersed in water, polar water molecules diffuse into the interior network to solvate the fixed ionic groups and counter-ions:
1. An interior **osmotic pressure** ($\Pi \approx 50\text{--}300\text{ bar}$) develops, driving expansion of the polymer network until balanced by the mechanical elastic contractile tension of the cross-linked chains.
2. Resins swell more extensively in dilute solutions than in concentrated salt solutions (where external osmotic pressure suppresses water uptake).
3. Resins with lower cross-linking swell significantly more than tightly cross-linked resins.""",
                    "simulations": ["sim_chem_ion_exchange_breakthrough_curve"]
                },
                {
                    "id": "sec-6-2",
                    "secNumber": "6.2",
                    "title": "Resin Classifications: SAC, WAC, SBA, WBA & Chelating Functional Groups",
                    "content": r"""The chromatographic selectivity, operating pH window, and capacity of an ion-exchange resin are determined by the chemical identity of the fixed functional groups covalently bonded to the aromatic rings of the polystyrene matrix:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 Classification of Analytical Ion-Exchange Resins            │
├─────────┬──────────────────────┬──────────────────────┬─────────────────────┤
│ Type    │ Fixed Functional Grp │ Commercial Example   │ Effective pH Range  │
├─────────┼──────────────────────┼──────────────────────┼─────────────────────┤
│ **SAC** │ Sulfonic Acid        │ Dowex 50W, Amberlite │ Full range          │
│         │ ($-\text{SO}_3^-\text{H}^+$)   │ IR-120               │ ($\text{pH } 1-14$) │
├─────────┼──────────────────────┼──────────────────────┼─────────────────────┤
│ **WAC** │ Carboxylic Acid      │ Amberlite IRC-50,    │ Alkaline / Neutral  │
│         │ ($-\text{COOH}$)     │ Chelex               │ ($\text{pH } 5-14$) │
├─────────┼──────────────────────┼──────────────────────┼─────────────────────┤
│ **SBA** │ Quaternary Ammonium  │ Dowex 1 (Type I),    │ Full range          │
│         │ ($-\text{CH}_2\text{N}^+(\text{CH}_3)_3$) │ Dowex 2 (Type II)│ ($\text{pH } 1-14$) │
├─────────┼──────────────────────┼──────────────────────┼─────────────────────┤
│ **WBA** │ Polyalkylamine       │ Amberlite IRA-67,    │ Acidic / Neutral    │
│         │ ($-\text{CH}_2\text{NHR}_2$) │ Dowex MWA-1        │ ($\text{pH } 0-7$)  │
└─────────┴──────────────────────┴──────────────────────┴─────────────────────┘
```

#### 1. Strong Acid Cation (SAC) Resins
- **Functional Group**: Sulfonic acid ($-\text{SO}_3^-\text{H}^+$) groups introduced via electrophilic aromatic sulfonation with concentrated sulfuric acid.
- **Characteristics**: Strongly acidic ($pK_a < 0$). Completely ionized across the entire pH scale ($\text{pH } 0\text{--}14$). Capable of exchanging cations from neutral, acidic, and alkaline solutions.

#### 2. Weak Acid Cation (WAC) Resins
- **Functional Group**: Carboxylic acid ($-\text{COOH}$) groups.
- **Characteristics**: Weakly acidic ($pK_a \approx 4\text{--}6$). At $\text{pH } < 4$, the groups are un-ionized ($-\text{COOH}$) and exchange capacity drops to zero. Highly active in neutral and alkaline solutions ($\text{pH } > 6$). Displays extraordinary selectivity for divalent alkaline-earth and transition metal ions over alkali metals.

#### 3. Strong Base Anion (SBA) Resins
- **Functional Group**: Quaternary ammonium salts introduced via chloromethylation followed by amination:
  - *Type I*: Trimethylammonium ($-\text{CH}_2\text{N}^+(\text{CH}_3)_3\text{Cl}^-$). Extremely basic, full pH ionization, highest chemical stability.
  - *Type II*: Dimethylethanolammonium ($-\text{CH}_2\text{N}^+(\text{CH}_3)_2(\text{CH}_2\text{CH}_2\text{OH})\text{Cl}^-$). Slightly less basic, more readily regenerated with $\text{NaOH}$.

#### 4. Weak Base Anion (WBA) Resins
- **Functional Group**: Primary, secondary, or tertiary amines ($-\text{NH}_2, -\text{NHR}, -\text{NR}_2$).
- **Characteristics**: Protonated to cationic form ($-\text{NHR}_2^+\text{Cl}^-$) only in acidic solution ($\text{pH } < 7$). In basic solution ($\text{pH } > 9$), they deprotonate to neutral amines, losing anion exchange capacity.

#### 5. Chelating Resins (e.g., Chelex-100)
- Possesses paired iminodiacetate functional groups ($-\text{CH}_2\text{N}(\text{CH}_2\text{COO}^-)_2$).
- Acts as a bonded tridentate chelator, exhibiting selectivities for heavy transition metals ($\text{Cu}^{2+}, \text{Pb}^{2+}, \text{Zn}^{2+}, \text{Cd}^{2+}$) that exceed alkali metal affinities by factors of $> 10^4$, enabling trace metal extraction from saturated seawater.""",
                    "simulations": []
                },
                {
                    "id": "sec-6-3",
                    "secNumber": "6.3",
                    "title": "Ion-Exchange Thermodynamics: Mass-Action Law & Selectivity Sequences",
                    "content": r"""Ion exchange is a reversible stoichiometric chemical equilibrium between mobile counter-ions in solution ($s$) and stationary counter-ions bound to resin fixed sites ($r$).

### Mass-Action Law of Cation Exchange
Consider the exchange of a monovalent cation $B^+$ for an initially bound cation $A^+$ on a strong acid cation resin:
$$A^+(r) + B^+(s) \rightleftharpoons B^+(r) + A^+(s)$$
At thermodynamic equilibrium, the **Selectivity Coefficient** $K_{A,B}$ is formulated in terms of molar concentrations:
$$K_{A,B} = \frac{[B^+]_r \cdot [A^+]_s}{[A^+]_r \cdot [B^+]_s}$$
For ions of unequal charge, such as a divalent cation $B^{2+}$ replacing a monovalent cation $A^+$:
$$2\,A^+(r) + B^{2+}(s) \rightleftharpoons B^{2+}(r) + 2\,A^+(s)$$
$$K_{A,B} = \frac{[B^{2+}]_r \cdot [A^+]_s^2}{[A^+]_r^2 \cdot [B^{2+}]_s}$$
where brackets $[ \ ]_r$ denote concentrations within the resin phase (typically $\text{meq/g}$ or $\text{meq/mL}$ of wet resin bed) and $[ \ ]_s$ denotes concentrations in the bulk aqueous solution.

### Physical Factors Governing Selectivity Sequences
Resins do not bind all ions equally. Cation and anion selectivity sequences are governed by three physical principles:

```
           Factors Governing Ion-Exchange Selectivity (K_A,B)
   1. Ionic Charge (z):
      Multivalent ions are held far more strongly than monovalent ions:
      Th⁴⁺ > Fe³⁺ > Al³⁺ >> Ca²⁺ > Mg²⁺ >> Na⁺ > Li⁺

   2. Hydrated Ionic Radius:
      For ions of equal charge, ions with smaller HYDRATED radii are preferred:
      Cs⁺ > Rb⁺ > K⁺ > Na⁺ > Li⁺   (Bare Li⁺ is tiny, but heavily hydrated!)

   3. Polarizability and Covalent Coordination:
      Highly polarizable ions that interact with aromatic polystyrene rings:
      Ag⁺ > Tl⁺ > Cs⁺ >> Na⁺
```

#### The Hydrated Radius Paradox (Alkali Metal Sequence)
Crystallographic bare ionic radii follow: $\text{Li}^+ (0.76\text{ \AA}) < \text{Na}^+ (1.02\text{ \AA}) < \text{K}^+ (1.38\text{ \AA}) < \text{Cs}^+ (1.67\text{ \AA})$.
However, because small ions possess high charge density, $\text{Li}^+$ coordinates a large, tightly bound hydration shell:
$$\text{Hydrated Radius: } \text{Li}^+_{\text{hyd}} (3.4\text{ \AA}) > \text{Na}^+_{\text{hyd}} (2.8\text{ \AA}) > \text{K}^+_{\text{hyd}} (2.3\text{ \AA}) > \text{Cs}^+_{\text{hyd}} (1.9\text{ \AA})$$
Coulomb's Law states that electrostatic attraction between the fixed sulfonate site and the cation center is inversely proportional to the square of the distance of closest approach ($F \propto 1/r_{\text{hyd}}^2$).
Consequently, the weakly hydrated $\text{Cs}^+$ approaches closest and binds most tightly:
$$\mathbf{\text{Cs}^+ > \text{Rb}^+ > \text{K}^+ > \text{NH}_4^+ > \text{Na}^+ > \text{H}^+ > \text{Li}^+}$$

#### Divalent Cation Selectivity Sequence
$$\mathbf{\text{Pb}^{2+} > \text{Ba}^{2+} > \text{Sr}^{2+} > \text{Ca}^{2+} > \text{Ni}^{2+} > \text{Cu}^{2+} > \text{Co}^{2+} > \text{Zn}^{2+} > \text{Mg}^{2+}}$$

#### Anion Selectivity Sequence on Strong Base Resins
$$\mathbf{\text{Citrate}^{3-} > \text{SO}_4^{2-} > \text{I}^- > \text{NO}_3^- > \text{Br}^- > \text{Cl}^- > \text{HCO}_3^- > \text{CH}_3\text{COO}^- > \text{OH}^- > \text{F}^-}$$""",
                    "simulations": []
                },
                {
                    "id": "sec-6-4",
                    "secNumber": "6.4",
                    "title": "Column Breakthrough Dynamics: Total vs Dynamic Breakthrough Capacity",
                    "content": r"""In analytical column chromatography, ion exchange is performed in a packed cylindrical glass or polymer column through which the sample solution percolates continuously.

### Ion-Exchange Capacity Metrics
1. **Total Theoretical Exchange Capacity ($Q_{\text{total}}$)**: The total number of chemically exchangeable functional groups per unit mass of dry resin (expressed in milliequivalents per gram, $\text{meq}\cdot\text{g}^{-1}$) or per unit volume of packed wet resin bed ($\text{meq}\cdot\text{mL}^{-1}$):
   - Typical SAC resin (Dowex 50W): $\sim 5.0\text{ meq/g dry} \ (1.8\text{--}2.0\text{ meq/mL wet})$.
   - Typical SBA resin (Dowex 1): $\sim 3.5\text{ meq/g dry} \ (1.2\text{--}1.4\text{ meq/mL wet})$.
2. **Breakthrough Capacity ($Q_B$)**: The quantity of target ion that can be loaded onto the column before that ion appears in the column effluent above a designated threshold concentration (typically $1\%$ of the feed concentration $C_0$).

```
                      Column Breakthrough Curve
     Effluent Conc (C / C₀)
      1.0 ▲                                            Exhaustion Point
          │                                            (C = C₀)
          │                                        ┌───────────────
          │                                       /
      0.5 ┼                                      /
          │                                     /
          │            Breakthrough Point      /
          │            (C = 0.01 C₀)          /
      0.0 └────────────┐─────────────────────/─────────────────────►
          0            V_B                   V_E             Volume (mL)
                       │◄── Working Zone ───►│
```

### Breakthrough Curve Parameters
As feed solution containing analyte concentration $C_0$ passes through the column:
1. Initially, all analyte ions are exchanged into the upper resin layers; effluent concentration $C = 0$.
2. As the resin saturates, the active mass-transfer zone advances down the column.
3. At volume $V_B$ (**breakthrough volume**), analyte begins to bleed through ($C/C_0 = 0.01\text{ to }0.05$).
4. The effluent concentration rises sigmoidally until reaching $V_E$ (**exhaustion volume**), where the entire bed is saturated ($C = C_0$).

The dynamic breakthrough capacity is calculated as:
$$Q_B = \frac{C_0 \cdot V_B}{m_{\text{resin}}} \quad \text{or} \quad Q_B = \frac{C_0 \cdot V_B}{V_{\text{bed}}}$$
Breakthrough capacity is always lower than total theoretical capacity ($Q_B < Q_{\text{total}}$) because of finite intra-particle diffusion kinetics, high mobile-phase flow velocity, and non-ideal axial dispersion.""",
                    "simulations": []
                },
                {
                    "id": "sec-6-5",
                    "secNumber": "6.5",
                    "title": "Column Chromatography Transport Theory: Distribution Ratio & Retention Volume",
                    "content": r"""The chromatographic transport of an ionic solute along an ion-exchange column is governed by the principles of linear elution chromatography.

### The Distribution Ratio ($D_g$ and $D_v$)
The equilibrium partition of a solute ion between the resin stationary phase and the aqueous mobile phase is defined by the **distribution ratio** ($D$):
1. **Weight Distribution Coefficient ($D_g$)**:
$$D_g = \frac{\text{amount of solute per gram of dry resin}}{\text{amount of solute per mL of solution}} = \frac{(C_r / m_{\text{dry}})}{(C_s / V_{\text{soln}})} \quad (\text{mL}\cdot\text{g}^{-1})$$
2. **Volume Distribution Coefficient ($D_v$)**:
$$D_v = \frac{\text{amount of solute per mL of packed resin bed}}{\text{amount of solute per mL of solution}} = D_g \cdot \rho_{\text{bed}}$$
where $\rho_{\text{bed}}$ is the packed bed bulk density ($\text{g dry resin / mL packed bed}$).

### Retention Volume ($V_R$) and Column Parameters
The total retention volume $V_R$ (the volume of mobile phase required to elute the center of a solute band through the column) is related to the distribution coefficient by the fundamental chromatographic equation:
$$V_R = V_0 + D_v \cdot V_s = V_0 + D_g \cdot m_{\text{resin}}$$
where:
- $V_0$ is the **void volume** (interstitial liquid volume between resin beads, typically $\sim 35\text{--}40\%$ of total column volume).
- $V_s$ is the volume of the stationary resin phase.
- $m_{\text{resin}}$ is the dry mass of resin in the bed.

### Separation Factor ($\alpha$)
The chromatographic resolution between two adjacent ionic components $1$ and $2$ depends on their **separation factor** (selectivity ratio):
$$\alpha = \frac{D_{g,2}}{D_{g,1}} = \frac{V_{R,2} - V_0}{V_{R,1} - V_0}$$
- If $\alpha = 1.0$: Components co-elute simultaneously; no separation occurs.
- If $\alpha \ge 1.5\text{--}2.0$: Baseline chromatographic separation is achieved on analytical columns.
Analytical chemists modulate $\alpha$ by introducing complexing ligands into the mobile phase (e.g., chloride, citrate, $\alpha$-hydroxyisobutyrate) that selectively convert target cations into neutral or anionic complexes.""",
                    "simulations": []
                },
                {
                    "id": "sec-6-6",
                    "secNumber": "6.6",
                    "title": "Analytical Separation of Zn2+ and Mg2+ via Chloro-Anionic Complexes on Anion Resins",
                    "content": r"""A classic triumph of ion-exchange chromatography is the quantitative separation of zinc ($\text{Zn}^{2+}$) from magnesium ($\text{Mg}^{2+}$). Although both are divalent metal cations that co-elute on cation exchangers, they exhibit dramatically disparate coordination chemistry with chloride ions.

### Chemical Principles of the Separation
1. **Magnesium ($\text{Mg}^{2+}$)**: A hard Lewis acid that forms virtually no chloro complexes with chloride in aqueous solution. Across all hydrochloric acid concentrations ($0.1\text{--}12\text{ M }\text{HCl}$), magnesium remains entirely in its cationic, hydrated form $[\text{Mg}(\text{H}_2\text{O})_6]^{2+}$.
2. **Zinc ($\text{Zn}^{2+}$)**: An intermediate Lewis acid that readily coordinates chloride in a stepwise equilibrium:
$$\text{Zn}^{2+} + \text{Cl}^- \rightleftharpoons [\text{ZnCl}]^+ \quad (K_1)$$
$$[\text{ZnCl}]^+ + \text{Cl}^- \rightleftharpoons \text{ZnCl}_2(aq) \quad (K_2)$$
$$\text{ZnCl}_2 + \text{Cl}^- \rightleftharpoons [\text{ZnCl}_3]^- \quad (K_3)$$
$$[\text{ZnCl}_3]^- + \text{Cl}^- \rightleftharpoons [\text{ZnCl}_4]^{2-} \quad (K_4)$$
In $2.0\text{ M }\text{HCl}$, zinc is converted predominantly into the tetrachlorozincate divalent anion $[\text{ZnCl}_4]^{2-}$.

```
                 Zn²⁺ / Mg²⁺ Separation on Strong Base Anion Resin
        Feed Mixture in 2 M HCl: Mg²⁺ (cation) + [ZnCl₄]²⁻ (anion)
                               │
                               ▼
        ┌─────────────────────────────────────────────────────────────┐
        │  Strong Base Anion Exchange Column (Dowex 1-X8, Cl⁻ form)   │
        ├─────────────────────────────────────────────────────────────┤
        │  1. Elution with 2 M HCl:                                   │
        │     • Mg²⁺ (cation) is repelled by fixed -N⁺(CH₃)₃ sites.   │
        │       Elutes immediately in void volume (V_R ≈ V₀)!         │
        │     • [ZnCl₄]²⁻ binds intensely to quaternary ammonium:     │
        │       2 R-N⁺(CH₃)₃ Cl⁻ + [ZnCl₄]²⁻ ⇌                        │
        │         [R-N⁺(CH₃)₃]₂[ZnCl₄]²⁻ + 2 Cl⁻  (D_g > 1000)       │
        ├─────────────────────────────────────────────────────────────┤
        │  2. Elution with Deionized Water (0.0 M HCl):               │
        │     • Lowers [Cl⁻] → [ZnCl₄]²⁻ dissociates to Zn²⁺ + 4 Cl⁻  │
        │     • Neutralized zinc desorbs rapidly and elutes clean!    │
        └─────────────────────────────────────────────────────────────┘
```

### Quantitative Experimental Protocol
1. **Column Preparation**: Pack a glass column with $5.0\text{ g}$ of Dowex 1-X8 ($100\text{--}200\text{ mesh}$, chloride form). Equilibrate with $2.0\text{ M }\text{HCl}$.
2. **Sample Loading**: Load $5.0\text{ mL}$ of test solution containing $0.05\text{ M }\text{Zn}^{2+}$ and $0.05\text{ M }\text{Mg}^{2+}$ in $2.0\text{ M }\text{HCl}$.
3. **Elution of Magnesium**: Elute with $50\text{ mL}$ of $2.0\text{ M }\text{HCl}$ at a flow rate of $1.5\text{ mL/min}$. Magnesium passes unhindered into the effluent, while zinc is retained in a tight band at the top of the column.
4. **Elution of Zinc**: Switch the mobile phase to pure deionized water ($\text{H}_2\text{O}$). As chloride is rinsed away, $[\text{ZnCl}_4]^{2-}$ dissociates back to $\text{Zn}^{2+}$, which is expelled from the anion resin and collected quantitatively in a second beaker.
5. **Quantification**: Both fractions are quantified by standard EDTA titration at $\text{pH } 10$ using Eriochrome Black T indicator.""",
                    "simulations": []
                },
                {
                    "id": "sec-6-7",
                    "secNumber": "6.7",
                    "title": "Analytical Separation of Halides (Cl- and Br-) on Anion Exchangers",
                    "content": r"""The quantitative resolution of chloride ($\text{Cl}^-$) and bromide ($\text{Br}^-$) in saline mixtures or seawater presents a major classical challenge because both precipitate simultaneously with silver nitrate as silver halides ($\text{AgCl}$ and $\text{AgBr}$). Anion exchange chromatography provides clean, quantitative baseline resolution.

### Selectivity Foundations on Strong Base Anion Resins
On a strong base anion exchange resin (such as Amberlite IRA-400 or Dowex 1-X8, quaternary ammonium functional groups), the anion selectivity sequence is governed by ionic polarizability and hydration enthalpy:
$$\mathbf{\text{I}^- > \text{NO}_3^- > \text{Br}^- > \text{Cl}^- > \text{F}^-}$$
- **Hydration Enthalpy**: Chloride ($\text{Cl}^-$, radius $1.81\text{ \AA}$) has higher charge density than bromide ($\text{Br}^-$, radius $1.96\text{ \AA}$). Consequently, chloride is more strongly hydrated in the aqueous phase ($\Delta H_{\text{hyd}}(\text{Cl}^-) = -381\text{ kJ/mol}$ vs $\Delta H_{\text{hyd}}(\text{Br}^-) = -347\text{ kJ/mol}$).
- **Resin Preference**: The organic polystyrene resin phase prefers the less hydrated, more polarizable bromide ion. The selectivity coefficient for the exchange is:
$$R\text{-Cl} + \text{Br}^-(aq) \rightleftharpoons R\text{-Br} + \text{Cl}^-(aq) \quad K_{\text{Cl,Br}} \approx 2.8$$
Bromide is held nearly three times more strongly than chloride.

### Separation Protocol via Selective Nitrate Elution
Using sodium nitrate ($\text{NaNO}_3$) as the competing eluent:
1. **Chloride Elution Stage**: The column is eluted with dilute sodium nitrate ($0.10\text{--}0.25\text{ M }\text{NaNO}_3$).
   Because chloride has a low distribution ratio ($D_{\text{Cl}} \ll D_{\text{NO}_3}$), chloride is displaced rapidly and elutes first in a clean, sharp chromatographic peak.
2. **Bromide Elution Stage**: After all chloride has emerged from the column, the eluent concentration is increased to $0.50\text{--}1.0\text{ M }\text{NaNO}_3$.
   The elevated nitrate concentration drives the displacement of the more strongly bound bromide, eluting it as a separate, resolved fraction.
3. **Detection and Analysis**: The eluted fractions are quantified by Volhard or Mohr argentometric titrations, or by flow-through conductivity detection in modern ion chromatography (IC).""",
                    "simulations": []
                }
            ],
            "problems": [
                {
                    "id": "prob-6-1",
                    "problemNumber": "6.1",
                    "title": "Total Exchange Capacity Determination of a Strong Acid Cation Resin",
                    "difficulty": "Foundational",
                    "statement": r"""The total exchange capacity of a strong acid cation exchange resin (Dowex 50W, hydrogen form, $-\text{SO}_3^-\text{H}^+$) is determined titrimetrically:
A $2.000\text{ g}$ sample of air-dried resin beads is packed into a glass column. A $250.0\text{-mL}$ volume of $0.500\text{ M }\text{NaCl}$ solution is passed slowly through the column to displace all exchangeable hydronium ions:
$$R\text{-SO}_3^-\text{H}^+ + \text{Na}^+ \rightleftharpoons R\text{-SO}_3^-\text{Na}^+ + \text{H}^+$$
The effluent and washings are collected quantitatively in a volumetric flask and diluted to $500.0\text{ mL}$.
A $50.00\text{-mL}$ aliquot of this effluent consumes $38.40\text{ mL}$ of standardized $0.05120\text{ M }\text{NaOH}$ to reach the phenolphthalein end point.
In a separate determination, a $1.000\text{ g}$ sample of the air-dried resin is dried in an oven at $110^\circ\text{C}$ to constant mass, yielding $0.7850\text{ g}$ of bone-dry resin.

Calculate:
1. The total milliequivalents of exchangeable $\text{H}^+$ displaced from the $2.000\text{ g}$ resin sample.
2. The total exchange capacity of the resin in $\text{meq}\cdot\text{g}^{-1}$ of **wet (air-dried) resin**.
3. The total exchange capacity of the resin in $\text{meq}\cdot\text{g}^{-1}$ of **bone-dry resin**.""",
                    "solution": r"""### Step 1: Total Milliequivalents of Displaced H+
Millimoles of $\text{H}^+$ neutralized in the $50.00\text{-mL}$ aliquot:
$$n_{\text{aliquot}} = V_{\text{NaOH}} \cdot M_{\text{NaOH}} = 38.40\text{ mL} \times 0.05120\text{ mmol/mL} = 1.96608\text{ mmol}$$
Because the total effluent was diluted to $500.0\text{ mL}$, the aliquot represents a $1/10$ fraction:
$$\text{Total } n_{\text{H}^+} = 1.96608\text{ mmol} \times \left(\frac{500.0\text{ mL}}{50.00\text{ mL}}\right) = 1.96608 \times 10 = \mathbf{19.6608\text{ meq}}$$

### Step 2: Capacity per Gram of Air-Dried Resin
The initial resin mass was $2.000\text{ g}$:
$$Q_{\text{air-dried}} = \frac{19.6608\text{ meq}}{2.000\text{ g}} = \mathbf{9.830\text{ meq}\cdot\text{g}^{-1}}$$

### Step 3: Capacity per Gram of Bone-Dry Resin
Moisture determination shows that $1.000\text{ g}$ air-dried resin contains $0.7850\text{ g}$ bone-dry resin:
$$\text{Dry mass fraction} = 0.7850$$
The bone-dry mass of the $2.000\text{ g}$ test portion was:
$$m_{\text{dry}} = 2.000\text{ g} \times 0.7850 = 1.5700\text{ g}$$
The bone-dry exchange capacity is:
$$Q_{\text{bone-dry}} = \frac{19.6608\text{ meq}}{1.5700\text{ g}} = \mathbf{12.523\text{ meq}\cdot\text{g}^{-1}}$$
*Validation*: Typical industrial SAC resins possess dry capacities between $4.5$ and $5.5\text{ meq/g}$. Highly sulfonated analytical grades or dry resins reach $10\text{--}12\text{ meq/g}$. The calculation demonstrates the crucial importance of stating whether capacity is reported on an air-dried or bone-dry basis.""",
                    "hints": ["Compute total moles in 500 mL by multiplying aliquot moles by 10.", "Divide by dry mass to get bone-dry capacity."]
                },
                {
                    "id": "prob-6-2",
                    "problemNumber": "6.2",
                    "title": "Selectivity Coefficient and Ion-Exchange Equilibrium Speciation",
                    "difficulty": "Intermediate",
                    "statement": r"""A $5.00\text{ g}$ sample of a strong acid cation exchange resin in the sodium form ($R\text{-Na}$) having a total capacity of $4.80\text{ meq}\cdot\text{g}^{-1}$ is equilibrated with $100.0\text{ mL}$ of a solution containing $0.0500\text{ M }\text{Cs}^+$.
The selectivity coefficient for cesium over sodium on this resin is:
$$K_{\text{Na,Cs}} = \frac{[\text{Cs}^+]_r [\text{Na}^+]_s}{[\text{Na}^+]_r [\text{Cs}^+]_s} = 3.20$$
1. Write the mass-balance equations for total exchange capacity and total cesium in the closed batch system.
2. Calculate the equilibrium concentration of $\text{Cs}^+$ remaining in the aqueous solution ($[\text{Cs}^+]_s$).
3. Calculate the fraction of total cesium extracted into the resin phase.""",
                    "solution": r"""### Step 1: Equilibrium Equations
Total resin capacity:
$$\text{Total meq in resin} = (5.00\text{ g}) \times (4.80\text{ meq/g}) = 24.00\text{ meq}$$
Initial cesium in solution:
$$n_{\text{Cs, initial}} = (100.0\text{ mL}) \times (0.0500\text{ mmol/mL}) = 5.00\text{ mmol}$$

Let $x$ be the millimoles of $\text{Cs}^+$ adsorbed onto the resin at equilibrium.
Then:
- Milliequivalents of $\text{Cs}^+$ in resin: $[\text{Cs}^+]_r \cdot m = x$
- Milliequivalents of $\text{Na}^+$ remaining in resin: $[\text{Na}^+]_r \cdot m = 24.00 - x$
- Milliequivalents of $\text{Cs}^+$ in solution: $[\text{Cs}^+]_s \cdot V = 5.00 - x$
- Milliequivalents of $\text{Na}^+$ released into solution: $[\text{Na}^+]_s \cdot V = x$

Substitute these into the selectivity expression (volumes and masses cancel):
$$K_{\text{Na,Cs}} = \frac{x \cdot x}{(24.00 - x)(5.00 - x)} = 3.20$$
$$\frac{x^2}{120.0 - 29.00\,x + x^2} = 3.20$$

### Step 2: Solving Quadratic Equation for Adsorbed Cesium
$$x^2 = 3.20 (120.0 - 29.00\,x + x^2) = 384.0 - 92.80\,x + 3.20\,x^2$$
$$2.20\,x^2 - 92.80\,x + 384.0 = 0$$
Using the quadratic formula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$:
$$x = \frac{92.80 \pm \sqrt{(-92.80)^2 - 4(2.20)(384.0)}}{2(2.20)} = \frac{92.80 \pm \sqrt{8611.84 - 3379.2}}{4.40} = \frac{92.80 \pm \sqrt{5232.64}}{4.40} = \frac{92.80 \pm 72.337}{4.40}$$
Physical root ($x \le 5.00$):
$$x = \frac{92.80 - 72.337}{4.40} = \frac{20.463}{4.40} = \mathbf{4.651\text{ mmol}}$$

### Step 3: Equilibrium Solution Concentration and Extraction Percentage
Equilibrium millimoles of $\text{Cs}^+$ in solution:
$$n_{\text{Cs}, s} = 5.00 - 4.651 = 0.349\text{ mmol}$$
Aqueous concentration in $100.0\text{ mL}$:
$$[\text{Cs}^+]_s = \frac{0.349\text{ mmol}}{100.0\text{ mL}} = \mathbf{3.49 \times 10^{-3}\text{ M}}$$

Percentage of cesium extracted:
$$\% \text{Extracted} = \left(\frac{4.651}{5.00}\right) \times 100\% = \mathbf{93.02\%}$$
*Analytical Insight*: Because $K_{\text{Na,Cs}} = 3.20 > 1$, cesium selectively displaces sodium, achieving $> 93\%$ recovery in a single batch equilibrium.""",
                    "hints": ["Set up the equilibrium expression in terms of millimoles exchanged x.", "Solve the quadratic equation ensuring x < initial cesium moles."]
                },
                {
                    "id": "prob-6-3",
                    "problemNumber": "6.3",
                    "title": "Column Breakthrough Capacity and Bed Volume Dynamics",
                    "difficulty": "Intermediate",
                    "statement": r"""A chromatographic column is packed with $20.0\text{ mL}$ of wet strong acid cation resin in the hydrogen form ($R\text{-H}$). Hard tap water containing $180.0\text{ mg}\cdot\text{L}^{-1}\text{ Ca}^{2+}$ ($M = 40.078\text{ g}\cdot\text{mol}^{-1}$) is pumped through the column at a flow rate of $5.0\text{ mL/min}$.
Effluent monitoring reveals that calcium breakthrough ($C = 0.01\,C_0$) occurs after $4.20\text{ L}$ of tap water has passed through the bed. Total bed exhaustion occurs after $5.50\text{ L}$.
1. Calculate the calcium feed concentration $C_0$ in milliequivalents per milliliter ($\text{meq/mL}$).
2. Calculate the dynamic breakthrough capacity ($Q_B$) in $\text{meq/mL}$ of packed bed.
3. Calculate the number of Bed Volumes (BV) processed prior to breakthrough.
4. Calculate the degree of column utilization ($\% \text{Utilization} = \frac{Q_B}{Q_{\text{total}}} \times 100\%$, where $Q_{\text{total}}$ is obtained from the exhaustion point).""",
                    "solution": r"""### Step 1: Calcium Feed Concentration ($C_0$)
Concentration in $\text{g/L}$:
$$C_0 = 180.0\text{ mg/L} = 0.1800\text{ g/L}$$
Molar concentration:
$$M_{\text{Ca}} = \frac{0.1800\text{ g/L}}{40.078\text{ g/mol}} = 4.4912 \times 10^{-3}\text{ mol/L}$$
Because calcium is divalent ($z = 2$), each mole corresponds to $2$ equivalents:
$$C_0 = (4.4912 \times 10^{-3}\text{ mol/L}) \times 2 = 8.9825 \times 10^{-3}\text{ eq/L} = \mathbf{8.9825 \times 10^{-3}\text{ meq/mL}}$$

### Step 2: Dynamic Breakthrough Capacity ($Q_B$)
Breakthrough volume $V_B = 4.20\text{ L} = 4200\text{ mL}$.
Total milliequivalents of calcium captured up to breakthrough:
$$n_B = V_B \cdot C_0 = (4200\text{ mL}) \times (8.9825 \times 10^{-3}\text{ meq/mL}) = 37.726\text{ meq}$$
Packed bed volume $V_{\text{bed}} = 20.0\text{ mL}$.
Breakthrough capacity:
$$Q_B = \frac{37.726\text{ meq}}{20.0\text{ mL}} = \mathbf{1.886\text{ meq/mL wet resin}}$$

### Step 3: Bed Volumes Processed (BV)
$$\text{BV} = \frac{V_B}{V_{\text{bed}}} = \frac{4200\text{ mL}}{20.0\text{ mL}} = \mathbf{210\text{ Bed Volumes}}$$
The column can treat $210$ times its own volume of hard water before calcium begins to bleed into the effluent.

### Step 4: Total Exhaustion Capacity and Column Utilization
Total exhaustion volume $V_E = 5.50\text{ L} = 5500\text{ mL}$.
Total capacity captured:
$$n_{\text{total}} \approx \frac{V_B + V_E}{2} \times C_0 \quad \text{(for symmetrical breakthrough)}$$
Using the conservative exhaustion limit:
$$n_{\text{exhaust}} = (5500\text{ mL}) \times (8.9825 \times 10^{-3}\text{ meq/mL}) = 49.40\text{ meq}$$
$$Q_{\text{exhaust}} = \frac{49.40\text{ meq}}{20.0\text{ mL}} = 2.470\text{ meq/mL}$$
Column utilization at breakthrough:
$$\% \text{Utilization} = \left(\frac{1.886}{2.470}\right) \times 100\% = \mathbf{76.36\%}$$
Over $76\%$ of the column's total exchange capacity is utilized before breakthrough occurs.""",
                    "hints": ["Remember that normality = molarity * valence (z = 2 for Ca2+).", "Bed volumes BV = V_breakthrough / V_bed."]
                },
                {
                    "id": "prob-6-4",
                    "problemNumber": "6.4",
                    "title": "Quantitative Separation of Zinc and Magnesium: Elution Volume Calculations",
                    "difficulty": "Honors Problem",
                    "statement": r"""A $10.0\text{-mL}$ column of Dowex 1-X8 strong base anion exchange resin (bed volume $V_b = 10.0\text{ mL}$, void volume $V_0 = 3.80\text{ mL}$) is used to separate $\text{Mg}^{2+}$ and $\text{Zn}^{2+}$.
In $2.0\text{ M }\text{HCl}$, the distribution ratios are:
- $D_v(\text{Mg}^{2+}) = 0.0$ (no anionic complex formation)
- $D_v([\text{ZnCl}_4]^{2-}) = 850$
In pure deionized water ($0.0\text{ M }\text{HCl}$):
- $D_v(\text{Zn}^{2+}) = 0.15$

1. Calculate the retention volume $V_R$ for magnesium in $2.0\text{ M }\text{HCl}$.
2. Calculate the theoretical retention volume $V_R$ for zinc in $2.0\text{ M }\text{HCl}$, and show that zinc cannot be eluted within reasonable laboratory time without altering mobile phase composition.
3. Calculate the retention volume for zinc after switching the eluent to pure water.""",
                    "solution": r"""### Step 1: Magnesium Retention Volume in 2.0 M HCl
Chromatographic retention volume equation:
$$V_R = V_0 + D_v \cdot V_s$$
Resin stationary phase volume:
$$V_s = V_b - V_0 = 10.0\text{ mL} - 3.80\text{ mL} = 6.20\text{ mL}$$
For magnesium, $D_v = 0.0$:
$$V_R(\text{Mg}) = 3.80\text{ mL} + (0.0)(6.20\text{ mL}) = \mathbf{3.80\text{ mL}}$$
*Result*: Magnesium emerges at the void volume ($3.80\text{ mL}$); it is completely unretarded and elutes immediately.

### Step 2: Zinc Retention Volume in 2.0 M HCl
For $[\text{ZnCl}_4]^{2-}$, $D_v = 850$:
$$V_R(\text{Zn}) = 3.80\text{ mL} + (850 \times 6.20\text{ mL}) = 3.80 + 5270 = \mathbf{5273.8\text{ mL} \approx 5.27\text{ L!}}$$
At a typical flow rate of $2.0\text{ mL/min}$, eluting zinc in $2.0\text{ M }\text{HCl}$ would require:
$$t = \frac{5274\text{ mL}}{2.0\text{ mL/min}} = 2637\text{ min} \approx \mathbf{44\text{ hours!}}$$
Zinc is effectively locked onto the resin column as long as $[\text{HCl}] \ge 2.0\text{ M}$.

### Step 3: Zinc Retention Volume in Pure Water
Upon switching to pure water, $[\text{Cl}^-] \to 0$, causing $[\text{ZnCl}_4]^{2-}$ to dissociate completely back to $\text{Zn}^{2+}$. In water, $D_v = 0.15$:
$$V_R(\text{Zn, water}) = 3.80\text{ mL} + (0.15 \times 6.20\text{ mL}) = 3.80 + 0.93 = \mathbf{4.73\text{ mL}}$$
*Result*: In water, zinc elutes rapidly in less than $5\text{ mL}$ ($< 2.5\text{ minutes}$ at $2\text{ mL/min}$)!
This demonstrates the power of **chemically triggered elution (displacement chromatography)** in ion-exchange separations.""",
                    "hints": ["Use the fundamental chromatographic retention formula V_R = V_0 + D_v * V_s.", "Stationary phase volume V_s = bed volume - void volume."]
                },
                {
                    "id": "prob-6-5",
                    "problemNumber": "6.5",
                    "title": "Resolution and Plate Height in Halide Anion Exchange Chromatography",
                    "difficulty": "Advanced",
                    "statement": r"""A mixture of chloride ($\text{Cl}^-$) and bromide ($\text{Br}^-$) is separated on an anion exchange column ($L = 25.0\text{ cm}$) using $0.20\text{ M }\text{NaNO}_3$ eluent at a flow rate of $1.00\text{ mL/min}$:
- Dead time: $t_0 = 1.20\text{ min}$
- Chloride peak: Retention time $t_{R1} = 4.50\text{ min}$, base peak width $W_1 = 0.60\text{ min}$
- Bromide peak: Retention time $t_{R2} = 9.80\text{ min}$, base peak width $W_2 = 1.10\text{ min}$

1. Calculate the capacity factors (retention factors) $k'_1$ and $k'_2$ for chloride and bromide.
2. Calculate the selectivity factor $\alpha = k'_2 / k'_1$.
3. Calculate the number of theoretical plates $N$ and plate height $H$ (in $\text{mm}$) for each peak.
4. Calculate the chromatographic resolution $R_s$ and state whether baseline separation is achieved ($R_s \ge 1.50$).""",
                    "solution": r"""### Step 1: Capacity Factors (Retention Factors $k'$)
By definition:
$$k' = \frac{t_R - t_0}{t_0}$$
1. For Chloride ($\text{Cl}^-$):
$$k'_1 = \frac{4.50 - 1.20}{1.20} = \frac{3.30}{1.20} = \mathbf{2.750}$$
2. For Bromide ($\text{Br}^-$):
$$k'_2 = \frac{9.80 - 1.20}{1.20} = \frac{8.60}{1.20} = \mathbf{7.167}$$

### Step 2: Selectivity Factor ($\alpha$)
$$\alpha = \frac{k'_2}{k'_1} = \frac{7.167}{2.750} = \mathbf{2.606}$$
Because $\alpha = 2.61 > 1.5$, the resin provides outstanding thermodynamic selectivity for bromide over chloride.

### Step 3: Theoretical Plates ($N$) and Plate Height ($H$)
Using the base peak width equation:
$$N = 16 \left(\frac{t_R}{W}\right)^2$$
1. For Chloride:
$$N_1 = 16 \left(\frac{4.50}{0.60}\right)^2 = 16 \times (7.50)^2 = 16 \times 56.25 = \mathbf{900\text{ plates}}$$
Plate height ($L = 25.0\text{ cm} = 250\text{ mm}$):
$$H_1 = \frac{L}{N_1} = \frac{250\text{ mm}}{900} = \mathbf{0.278\text{ mm}}$$

2. For Bromide:
$$N_2 = 16 \left(\frac{9.80}{1.10}\right)^2 = 16 \times (8.909)^2 = 16 \times 79.37 = \mathbf{1270\text{ plates}}$$
Plate height:
$$H_2 = \frac{L}{N_2} = \frac{250\text{ mm}}{1270} = \mathbf{0.197\text{ mm}}$$

### Step 4: Chromatographic Resolution ($R_s$)
$$R_s = \frac{2 (t_{R2} - t_{R1})}{W_1 + W_2} = \frac{2 (9.80 - 4.50)}{0.60 + 1.10} = \frac{2 (5.30)}{1.70} = \frac{10.60}{1.70} = \mathbf{6.235}$$
*Conclusion*: Baseline separation requires $R_s \ge 1.50$. The experimental resolution of $R_s = 6.24$ is well beyond baseline, representing complete baseline resolution with a wide gap between peaks.""",
                    "hints": ["Capacity factor k' = (t_R - t_0) / t_0.", "Resolution R_s = 2 * (t_R2 - t_R1) / (W1 + W2)."]
                },
                {
                    "id": "prob-6-6",
                    "problemNumber": "6.6",
                    "title": "Water Deionization Mass Balance and Mixed-Bed Polishing",
                    "difficulty": "Foundational",
                    "statement": r"""A university water purification plant deionizes tap water containing $350.0\text{ mg}\cdot\text{L}^{-1}$ total dissolved solids (TDS), consisting on average of:
- Cations: $2.50\text{ meq}\cdot\text{L}^{-1} \ (\text{Ca}^{2+}, \text{Mg}^{2+}, \text{Na}^+)$
- Anions: $2.50\text{ meq}\cdot\text{L}^{-1} \ (\text{HCO}_3^-, \text{SO}_4^{2-}, \text{Cl}^-)$
The water passes through a two-bed deionizer system:
1. Bed 1: Strong acid cation exchanger ($R\text{-H}$), volume $50.0\text{ L}$, capacity $1.80\text{ meq/mL}$.
2. Bed 2: Strong base anion exchanger ($R\text{-OH}$), volume $60.0\text{ L}$, capacity $1.20\text{ meq/mL}$.

Calculate:
1. The volume of pure water (in Liters) that can be demineralized before Bed 1 exhausts.
2. The volume of pure water that can be demineralized before Bed 2 exhausts.
3. Which bed is the limiting bed?
4. Explain why a **mixed-bed** polisher (intimate blend of $R\text{-H}$ and $R\text{-OH}$ beads) produces water with higher electrical resistivity ($18.2\text{ M}\Omega\cdot\text{cm}$) than two separate beds in series.""",
                    "solution": r"""### Step 1: Demineralization Volume for Bed 1 (SAC, R-H)
Total capacity of Bed 1:
$$\text{Total meq} = (50.0\text{ L} \times 1000\text{ mL/L}) \times (1.80\text{ meq/mL}) = 50,000\text{ mL} \times 1.80 = \mathbf{90,000\text{ meq}}$$
Cation load in tap water = $2.50\text{ meq/L}$.
Volume of water treatable by Bed 1:
$$V_{\text{SAC}} = \frac{90,000\text{ meq}}{2.50\text{ meq/L}} = \mathbf{36,000\text{ L}}$$

### Step 2: Demineralization Volume for Bed 2 (SBA, R-OH)
Total capacity of Bed 2:
$$\text{Total meq} = (60.0\text{ L} \times 1000\text{ mL/L}) \times (1.20\text{ meq/mL}) = 60,000\text{ mL} \times 1.20 = \mathbf{72,000\text{ meq}}$$
Anion load in tap water = $2.50\text{ meq/L}$.
Volume of water treatable by Bed 2:
$$V_{\text{SBA}} = \frac{72,000\text{ meq}}{2.50\text{ meq/L}} = \mathbf{28,800\text{ L}}$$

### Step 3: Limiting Bed
$$\mathbf{\text{Bed 2 (Strong Base Anion) is the limiting bed}}$$
The entire two-bed system will exhaust when **$28,800\text{ L}$** of water has been processed.

### Step 4: The Mixed-Bed Thermodynamic Neutralization Driving Force
- In a two-bed system in series:
  - Bed 1 exchanges cations for $\text{H}^+$, producing dilute mineral acid ($\text{HCl}, \text{H}_2\text{SO}_4$).
  - As $[\text{H}^+]$ increases, the mass-action equilibrium $R\text{-H} + M^+ \rightleftharpoons R\text{-M} + \text{H}^+$ is opposed by the high concentration of acid, causing minor "leakage" of weakly held cations (e.g., $\text{Na}^+$).
  - Bed 2 then exchanges anions for $\text{OH}^-$, but leaked sodium passes through as $\text{NaOH}$, limiting resistivity to $\sim 1\text{--}5\text{ M}\Omega\cdot\text{cm}$.
- In a **mixed-bed polisher**:
  - Cation and anion beads are intermingled intimately within millimeters of each other.
  - As soon as a cation exchanges for $\text{H}^+$ and an anion exchanges for $\text{OH}^-$, the two ions immediately react in an ultra-fast neutralization reaction to form neutral water:
    $$\text{H}^+ + \text{OH}^- \rightleftharpoons \text{H}_2\text{O} \quad (K_{\text{neut}} = 10^{14})$$
  - The neutralization drives both product concentrations ($[\text{H}^+]$ and $[\text{OH}^-]$) to $10^{-7}\text{ M}$, pulling both ion-exchange equilibria to $100\%$ completion by Le Châtelier's principle.
  - All electrolyte leakage is eliminated, yielding theoretically pure water with maximum resistivity of **$18.2\text{ M}\Omega\cdot\text{cm}$ at $25^\circ\text{C}$**.""",
                    "hints": ["Compute total capacity in meq for each bed by multiplying bed volume in mL by capacity in meq/mL.", "The bed with the lower total treatable volume is the limiting bed."]
                },
                {
                    "id": "prob-6-7",
                    "problemNumber": "6.7",
                    "title": "Chelating Resin Kinetics and Trace Metal Preconcentration from Seawater",
                    "difficulty": "Honors Problem",
                    "statement": r"""A trace metal environmental laboratory uses a column of Chelex-100 chelating resin ($1.00\text{ g}$ dry mass, functionalized with iminodiacetate groups) to preconcentrate copper ($\text{Cu}^{2+}$) from seawater.
Seawater contains a colossal background of alkali and alkaline-earth salts ($0.45\text{ M }\text{Na}^+, 0.05\text{ M }\text{Mg}^{2+}, 0.01\text{ M }\text{Ca}^{2+}$) and trace copper at $2.0\,\mu\text{g}\cdot\text{L}^{-1}$ ($M_{\text{Cu}} = 63.55\text{ g}\cdot\text{mol}^{-1}$).
The selectivity coefficients on Chelex-100 are:
- $K_{\text{Na,Cu}} \approx 1.2 \times 10^7$
- $K_{\text{Na,Ca}} \approx 4.0 \times 10^2$
- $K_{\text{Na,Mg}} \approx 2.5 \times 10^2$

1. Explain why conventional SAC resins fail completely for trace metal extraction from seawater.
2. A $2.00\text{-L}$ sample of seawater is passed through the Chelex-100 column. Copper is quantitatively retained while sodium passes unhindered.
3. The retained copper is eluted with $10.0\text{ mL}$ of $2.0\text{ M }\text{HNO}_3$. Calculate the preconcentration factor and the final concentration of copper in the eluate in $\mu\text{g}\cdot\text{mL}^{-1}$.""",
                    "solution": r"""### Step 1: Why Conventional SAC Resins Fail in Seawater
On a conventional strong acid cation resin (Dowex 50W), selectivity is governed strictly by electrostatic charge:
$$K_{\text{Na,Cu}} \approx 3.0$$
Because seawater contains $0.45\text{ M }\text{Na}^+$ ($450,000\,\mu\text{M}$) versus only $0.00003\,\mu\text{M }\text{Cu}^{2+}$, sodium ions outnumber copper by a factor of $> 10^7$.
On an SAC resin, sodium swamps all exchange sites, displacing copper into the waste effluent.
In contrast, Chelex-100 functions via **coordinate covalent chelation** through its iminodiacetate nitrogen and two carboxylate oxygens:
$$\text{Resin-N}(\text{CH}_2\text{COO}^-)_2 + \text{Cu}^{2+} \rightleftharpoons \text{Resin-Chelex-Cu}$$
Because copper(II) forms an ultra-stable five-membered chelate ($K_{\text{Na,Cu}} \approx 1.2 \times 10^7$), copper binds selectively, completely ignoring the high sodium background.

### Step 2: Copper Mass in 2.00 L Seawater Sample
$$m_{\text{Cu}} = 2.00\text{ L} \times 2.0\,\mu\text{g/L} = 4.00\,\mu\text{g Cu}$$

### Step 3: Elution and Preconcentration Factor
The retained copper is eluted with $V_{\text{eluate}} = 10.0\text{ mL} = 0.0100\text{ L}$.
1. Preconcentration Factor:
$$\text{PF} = \frac{V_{\text{sample}}}{V_{\text{eluate}}} = \frac{2000\text{ mL}}{10.0\text{ mL}} = \mathbf{200\text{-fold Preconcentration}}$$

2. Final Concentration in Eluate:
$$C_{\text{eluate}} = \frac{4.00\,\mu\text{g}}{10.0\text{ mL}} = \mathbf{0.400\,\mu\text{g}\cdot\text{mL}^{-1} = 400\,\mu\text{g}\cdot\text{L}^{-1}}$$
*Analytical Result*: The copper concentration is boosted from an undetectable $2.0\,\mu\text{g/L}$ to $400\,\mu\text{g/L}$, which is readily quantified by flame AAS with high precision.""",
                    "hints": ["Preconcentration factor is original sample volume divided by elution volume.", "Final concentration = initial mass of analyte / final eluate volume."]
                }
            ]
        }
    ]
    return units

if __name__ == '__main__':
    u = get_units_4_5_6()
    print(f"Generated Units 4-6: {len(u)} units")
    for unit in u:
        print(f"  {unit['title']}: {len(unit['sections'])} sections, {len(unit['problems'])} problems")
