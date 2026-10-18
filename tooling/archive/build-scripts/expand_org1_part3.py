# expand_org1_part3.py
# Deep academic enrichment for Unit 5 and Unit 6 of Organic Chemistry I
# Aromaticity, Wheland Intermediates, Hammett Equation, SN1/SN2/E1/E2, Benzyne & Grignard Reagents

def expand_unit5(u5):
    # Deepen Section 1: Benzene Structure & Resonance Energy
    u5["sections"][0]["content"] += r"""

### Thermochemical & Homodesmotic Derivation of Aromatic Resonance Energy

To isolate the genuine aromatic resonance energy ($RE$) of benzene without confounding strain or hybridization changes, physical organic chemists utilize **homodesmotic reactions**, where the number of bonds of each formal type (single/double) and carbon hybridization states ($sp^2/sp^3$) are exactly matched on both sides of the balanced equation:

$$\text{Benzene} + 3\,\text{Ethylene} \longrightarrow 3\,\text{1,3-Butadiene (trans)} \tag{5.1a}$$

#### Evaluation of Homodesmotic Enthalpy:
Using high-precision gas-phase standard enthalpies of formation ($\Delta H_f^\circ$ at $298.15\text{ K}$):
- $\Delta H_f^\circ(\text{Benzene}) = +82.9\text{ kJ/mol}$
- $\Delta H_f^\circ(\text{Ethylene}) = +52.4\text{ kJ/mol} \implies 3 \times (+52.4) = +157.2\text{ kJ/mol}$
- $\Delta H_f^\circ(\text{1,3-Butadiene}) = +110.0\text{ kJ/mol} \implies 3 \times (+110.0) = +330.0\text{ kJ/mol}$

$$\Delta H_{\text{homodesmotic}} = 3\,\Delta H_f^\circ(\text{1,3-butadiene}) - [\Delta H_f^\circ(\text{benzene}) + 3\,\Delta H_f^\circ(\text{ethylene})] \tag{5.1b}$$
$$\Delta H_{\text{homodesmotic}} = +330.0 - (82.9 + 157.2) = \mathbf{+89.9\text{ kJ/mol}} \quad (21.5\text{ kcal/mol}) \tag{5.1c}$$
When added to the conjugated resonance energy of three butadiene units ($3 \times 15.5\text{ kJ/mol} = 46.5\text{ kJ/mol}$), the total resonance stabilization energy of benzene reaches **$136.4\text{ kJ/mol}$ ($32.6\text{ kcal/mol}$)**, in outstanding agreement with the empirical value derived from heats of hydrogenation ($152\text{ kJ/mol}$)."""

    # Deepen Section 2: Hückel Rule & Ring Current Spectroscopy
    u5["sections"][1]["content"] += r"""

### Diatropic Ring Currents & Chemical Shifts in Annulenes

When a planar aromatic ring is placed in an external magnetic field $\vec{B}_0$, the delocalized $\pi$ electrons circulate in closed loops according to Lenz's law.
This induced circulation generates an **induced magnetic field $\vec{B}_{\text{ind}}$**:
1. **Diatropic Ring Current (Aromatic, $4n+2\pi$)**:
   - Inside the ring, $\vec{B}_{\text{ind}}$ opposes the external field $\vec{B}_0$ (shielding).
   - Outside the perimeter, the magnetic field lines loop around, reinforcing $\vec{B}_0$ (deshielding).
   - **Spectroscopic Consequence**: Protons located on the exterior of the ring are intensely deshielded ($\delta = 7.0 - 8.5\text{ ppm}$ in benzene). Protons held directly above or inside the aromatic cavity experience intense shielding!
2. **Spectacular Evidence from [18]Annulene**:
   [18]Annulene ($C_{18}H_{18}$, $n=4, 18\pi$ electrons, aromatic) is sufficiently large to hold six interior protons inside the cavity and twelve exterior protons around the perimeter.
   - At $-60^\circ\text{C}$ in $^1\text{H}$ NMR:
     - The **12 outer protons** resonate far downfield at **$\delta = +9.28\text{ ppm}$** (intensely deshielded)!
     - The **6 inner protons** resonate far upfield at **$\delta = -2.99\text{ ppm}$** (three parts per million above tetramethylsilane)!
3. **Paratropic Ring Current (Antiaromatic, $4n\pi$)**:
   In planar antiaromatic systems (such as [16]annulene), paramagnetic ring currents circulate in the opposite direction.
   - Interior protons are shifted downfield ($\delta \approx +10.5\text{ ppm}$), while exterior protons are shifted upfield ($\delta \approx +5.2\text{ ppm}$), providing an absolute physical diagnostic for antiaromaticity."""

    # Deepen Section 3: Wheland Intermediate & Kinetic Isotope Effects
    u5["sections"][2]["content"] += r"""

### Kinetic Isotope Effects ($k_H / k_D$) in Electrophilic Aromatic Substitution

The general electrophilic aromatic substitution proceeds via a two-step mechanism:

$$\text{Ar}-\text{H} + \text{E}^+ \xrightleftharpoons[k_{-1}]{k_1} [\text{Ar}(\text{H})\text{E}]^+ \; (\text{Wheland } \sigma\text{-complex}) \xrightarrow{k_2} \text{Ar}-\text{E} + \text{H}^+ \tag{5.3a}$$

Applying the steady-state approximation to the Wheland intermediate:
$$v = -\frac{d[\text{ArH}]}{dt} = \frac{k_1 k_2 [\text{ArH}][\text{E}^+]}{k_{-1} + k_2} \tag{5.3b}$$

#### 1. Regime A: Rate-Determining $\sigma$-Complex Formation ($k_2 \gg k_{-1}$):
When proton transfer from the arenium ion to the base is significantly faster than the reverse loss of electrophile:
$$v \approx k_1 [\text{ArH}][\text{E}^+] \tag{5.3c}$$
- The rate depends solely on $k_1$ (electrophilic attack on the $\pi$ cloud).
- The $\text{C}-\text{H}$ bond is NOT broken in the rate-determining transition state.
- **Primary Kinetic Isotope Effect**: Replacing benzene with hexadeuteriobenzene ($\text{C}_6\text{D}_6$) yields:
  $$\frac{k_H}{k_D} \approx 1.00 \pm 0.05 \tag{5.3d}$$
- Observed in **nitration, chlorination, bromination, and Friedel-Crafts alkylation**.

#### 2. Regime B: Rate-Determining Deprotonation ($k_{-1} \gg k_2$):
When the electrophile is a good leaving group or electrophilic attack is rapidly reversible:
$$v \approx \frac{k_1 k_2}{k_{-1}} [\text{ArH}][\text{E}^+] \tag{5.3e}$$
- The overall rate is directly proportional to $k_2$, the rate constant for $\text{C}-\text{H}$ bond cleavage!
- **Zero-Point Energy Difference**: The zero-point vibrational energy of a $\text{C}-\text{H}$ bond ($\sim 17.5\text{ kJ/mol}$) exceeds that of a $\text{C}-\text{D}$ bond ($\sim 12.6\text{ kJ/mol}$). The activation barrier for cleaving $\text{C}-\text{D}$ is higher by $\sim 5\text{ kJ/mol}$:
  $$\frac{k_H}{k_D} = \exp\left(\frac{\Delta E_{\text{ZPE}}}{RT}\right) \approx 6.5 - 7.5 \tag{5.3f}$$
- Observed in **aromatic iodination** ($\text{I}^+$ is expelled rapidly, $k_{-1} \gg k_2$, giving $k_H/k_D = 4.0 - 5.5$) and **sulfonation** under dilute acidic conditions ($k_H/k_D = 2.0 - 3.0$). This confirms the dual-step kinetic nature of EAS!"""

    # Deepen Section 4: Classic EAS Reactions & Acylation
    u5["sections"][3]["content"] += r"""

### Nitronium Ion Generation Kinetics & Clemmensen vs Wolff-Kishner Reductions

The generation of the electrophile in nitration and the subsequent reduction of Friedel-Crafts acylation products represent central synthetic milestones:

#### 1. Equilibrium Kinetics of Nitronium Ion Generation:
In "mixed acid" ($\text{HNO}_3 + \text{H}_2\text{SO}_4$), sulfuric acid acts as a strong Brønsted acid toward nitric acid:
$$\text{HNO}_3 + 2\,\text{H}_2\text{SO}_4 \xrightleftharpoons[K_{\text{nit}}]{\quad} \mathbf{\text{NO}_2^+} + \text{H}_3\text{O}^+ + 2\,\text{HSO}_4^- \tag{5.5a}$$
- Cryoscopic freezing-point measurements in pure sulfuric acid reveal a van 't Hoff factor of $i = 4.0$, confirming the generation of four distinct ions per molecule of nitric acid dissolved.
- Raman spectroscopy shows a distinct intense Raman band at $\nu = 1400\text{ cm}^{-1}$ corresponding to the symmetric stretching mode of the linear, centrosymmetric nitronium ion ($[\text{O}=\stackrel{\oplus}{\text{N}}=\text{O}]$).

#### 2. Reduction of Friedel-Crafts Acylation Adducts to Alkylbenzenes:
Because Friedel-Crafts alkylation suffers from polyalkylation and carbocation rearrangement, primary alkylbenzenes are prepared via acylation followed by complete carbonyl deoxygenation:

1. **Clemmensen Reduction (Acidic Regime)**:
   $$\text{Ar}-\text{CO}-\text{R} + \text{Zn(Hg)} + \text{conc. HCl} \xrightarrow{\Delta} \mathbf{\text{Ar}-\text{CH}_2-\text{R}} + \text{ZnCl}_2 + \text{H}_2\text{O} \tag{5.5b}$$
   - **Mechanism**: Operates via heterogeneous single-electron transfer at the amalgamated zinc surface. Organozinc carbenoid intermediates ($\text{Ar}-\text{CH}(\text{ZnCl})-\text{R}$) are protonated by $\text{HCl}$ to avoid free carbocations.
   - Suitable for acid-stable molecules; fails if base-sensitive or acid-labile groups are present.

2. **Wolff-Kishner Reduction (Basic Regime)**:
   $$\text{Ar}-\text{CO}-\text{R} + \text{NH}_2\text{NH}_2 + \text{KOH} \xrightarrow[\Delta, \; 180-200^\circ\text{C}]{\text{diethylene glycol}} \mathbf{\text{Ar}-\text{CH}_2-\text{R}} + \mathbf{\text{N}_2\uparrow} + \text{H}_2\text{O} \tag{5.5c}$$
   - **Mechanism**: Condensation forms a hydrazone ($\text{Ar}-\text{C}(=\text{NNH}_2)\text{R}$). Deprotonation by hydroxide yields a resonance-stabilized azo anion ($[\text{Ar}-\text{C}(\text{R})=\text{N}-\bar{\text{N}}\text{H} \leftrightarrow \text{Ar}-\bar{\text{C}}(\text{R})-\text{N}=\text{NH}]$).
   - Protonation at carbon followed by second deprotonation causes irreversible expulsion of molecular nitrogen gas ($\text{N}_2\uparrow$, driving force $\Delta G^\circ \ll 0$), generating a carbanion that is protonated by solvent to give the alkylbenzene."""

    # Deepen Section 6: Hammett Equation
    u5["sections"][5]["content"] += r"""

### Mathematical Derivation and Physical Significance of the Hammett Equation

In 1937, Louis Plack Hammett discovered that the effects of meta- and para-substituents on the reactivity of benzene derivatives correlate linearly with their effect on the ionization equilibrium of benzoic acid:

#### 1. Definition of the Substituent Constant $\sigma$:
The ionization of benzoic acid in water at $25.0^\circ\text{C}$ is selected as the universal reference reaction:
$$\text{Ar}-\text{COOH} + \text{H}_2\text{O} \xrightleftharpoons[K]{\quad} \text{Ar}-\text{COO}^- + \text{H}_3\text{O}^+ \tag{5.11a}$$
Setting the reaction constant for benzoic acid ionization to $\rho \equiv 1.000$ by definition:
$$\sigma_X \equiv \log\left(\frac{K_X}{K_H}\right) = pK_a(\text{unsubstituted}) - pK_a(X\text{-substituted}) \tag{5.11b}$$
- If substituent $X$ is electron-withdrawing ($-\text{NO}_2, -\text{CN}$), it stabilizes the benzoate anion, increasing $K_X$ and decreasing $pK_a$: $\mathbf{\sigma > 0}$.
- If substituent $X$ is electron-donating ($-\text{OCH}_3, -\text{CH}_3$), it destabilizes the anion: $\mathbf{\sigma < 0}$.

#### 2. The General Hammett Linear Free-Energy Relationship:
For any reaction of meta- or para-substituted benzene derivatives with rate constant $k_X$ or equilibrium constant $K_X$:
$$\log\left(\frac{k_X}{k_H}\right) = \rho \sigma_X, \quad \log\left(\frac{K_X}{K_H}\right) = \rho \sigma_X \tag{5.11c}$$

#### 3. Physical Diagnostic Meaning of the Reaction Constant $\rho$:
The slope $\rho$ quantifies the **sensitivity of the reaction to electrical effects** and diagnoses the **charge development in the transition state**:
- **$\rho > 0$ (Positive Slope)**: Negative charge is created (or positive charge destroyed) at the reaction center in the transition state. Electron-withdrawing substituents accelerate the reaction. (e.g., alkaline saponification of ethyl benzoates: $\rho = +2.54$).
- **$\rho < 0$ (Negative Slope)**: Positive charge is created (or negative charge destroyed) in the transition state. Electron-donating substituents accelerate the reaction. (e.g., solvolysis of cumyl chlorides: $\rho = -4.54$).
- **Large Magnitude ($|\rho| > 2$)**: Direct ionic or carbocation-like charge build-up at the reaction center.
- **Small Magnitude ($|\rho| < 1$)**: Radical or concerted pericyclic transition state with minimal charge polarization."""
    return u5


def expand_unit6(u6):
    # Deepen Section 2: SN2 Dynamics & Walden Inversion
    u6["sections"][1]["content"] += r"""

### Phillips-Kenyon Proof of Walden Inversion & Hughes-Ingold Kinetics

The stereospecific inversion of configuration in bimolecular nucleophilic substitution ($S_N2$) was definitively verified in 1923 by Henry Phillips and Joseph Kenyon through an elegant cycle involving optically active $(+)$-2-octanol:

```
               (+)-2-Octanol  [alpha] = +10.3 deg
                     |
       Tosylation    |  (Retention: C-O bond unbroken)
       (TsCl / Py)   v
               (+)-2-Octyl Tosylate
                     |
       Acetate SN2   |  (INVERSION: C-O bond broken by AcO-)
       (AcO- / DMF)  v
               (-)-2-Octyl Acetate  [alpha] = -7.0 deg
                     |
       Saponification|  (Retention: Acyl C-O broken, alkyl C-O untouched)
       (OH- / H2O)   v
               (-)-2-Octanol  [alpha] = -10.3 deg  (100% Inverted!)
```

#### Stereochemical Proof Analysis:
1. In Step 1 (tosylation), only the $\text{O}-\text{H}$ bond of octanol is cleaved; the chiral carbon stereocenter is never touched, so configuration is retained ($100\%$).
2. In Step 3 (saponification of the ester), nucleophilic hydroxide attacks the carbonyl carbon, cleaving the acyl-oxygen bond; the chiral alkyl stereocenter remains untouched, ensuring retention ($100\%$).
3. Because the starting material $(+)$-2-octanol is converted into pure $(-)$-2-octanol with an exact reversal of specific rotation, the inversion **must have occurred exclusively during the nucleophilic displacement of the tosylate group by acetate**!
This experiment established the concerted backside attack geometry of the $S_N2$ mechanism beyond all doubt."""

    # Deepen Section 3: SN1 Dynamics & Winstein Ion Pairs
    u6["sections"][2]["content"] += r"""

### The Winstein Ion-Pair Continuum & Racemization vs Inversion

In unimolecular nucleophilic substitution ($S_N1$), the rate-determining step is heterolytic dissociation of the carbon-halogen bond.
In 1956, Saul Winstein proved that ionization does not instantaneously generate free, independent ions, but proceeds through an equilibrium cascade of ion pairs:

$$\text{R}-\text{X} \xrightleftharpoons[k_{-1}]{k_1} \mathbf{[\text{R}^+ \, \text{X}^-] \text{ (Intimate / Contact Ion Pair)}} \xrightleftharpoons[k_{-2}]{k_2} \mathbf{[\text{R}^+ \parallel \text{X}^-] \text{ (Solvent-Separated Ion Pair)}} \xrightleftharpoons[k_{-3}]{k_3} \mathbf{\text{R}^+ + \text{X}^- \text{ (Free Dissociated Ions)}} \tag{6.5a}$$

#### Mechanistic & Stereochemical Consequences:
1. **Intimate Ion Pair ($[\text{R}^+ \, \text{X}^-]$)**:
   - The carbocation and leaving group anion are in direct van der Waals contact, enclosed within a common solvent cage.
   - The departing anion blocks the front face of the planar carbocation.
   - If the nucleophile captures the carbocation at this stage, attack occurs **exclusively from the rear face**, resulting in **net stereochemical inversion ($60-90\%$ inversion)**!
2. **Solvent-Separated Ion Pair ($[\text{R}^+ \parallel \text{X}^-]$)**:
   - One or more solvent molecules have inserted between the cation and anion.
   - Frontside attack is now partially accessible, yielding diminished stereospecificity.
3. **Free Dissociated Ions ($\text{R}^+ + \text{X}^-$)**:
   - Both ions diffuse independently through the bulk solution.
   - Attack occurs with equal probability from either face of the planar carbocation, producing **complete racemization ($50\% R, 50\% S$)**.
- **Solvent Effect**: In highly ionizing, polar protic solvents (e.g., water, trifluoroacetic acid), dissociation to free ions is rapid, leading to predominantly racemic products. In less polar solvents (e.g., acetone, ether), intimate ion pair collapse dominates, resulting in substantial net inversion ($10-30\%$ optical activity retained)!"""

    # Deepen Section 4: E1cB Mechanism
    u6["sections"][3]["content"] += r"""

### The $E1\text{cB}$ Mechanism: Carbanion Intermediates & Kinetic Criteria

The Elimination Unimolecular conjugate Base ($E1\text{cB}$) pathway operates when the substrate possesses an unusually acidic $\beta$-hydrogen and a relatively poor leaving group:

$$\text{Base} + \text{H}-\text{C}_\beta-\text{C}_\alpha-\text{X} \xrightleftharpoons[k_{-1}]{k_1} \text{Base}-\text{H}^+ + [:\bar{\text{C}}_\beta-\text{C}_\alpha-\text{X}] \; (\text{Carbanion Conjugate Base}) \xrightarrow{k_2} \text{C}=\text{C} + \text{X}^- \tag{6.8a}$$

#### Kinetic Regimes:
1. **$(E1\text{cB})_{\text{reversible}}$ ($k_{-1}[\text{Base-H}^+] \gg k_2$)**:
   - Carbanion formation is fast and reversible. The rate-determining step is the subsequent expulsion of the leaving group ($k_2$).
   - Deuterium exchange experiments in $\text{MeOD} / \text{MeO}^-$ show that unreacted starting material incorporates deuterium rapidly prior to elimination:
     $$v = \frac{k_1 k_2}{k_{-1}} \frac{[\text{Substrate}][\text{Base}]}{[\text{Base-H}^+]} \tag{6.8b}$$
2. **$(E1\text{cB})_{\text{irreversible}}$ ($k_2 \gg k_{-1}[\text{Base-H}^+]$)**:
   - Proton abstraction by base is rate-determining, and the carbanion collapses immediately to alkene.
   - Exhibits clean second-order kinetics ($v = k_1 [\text{Substrate}][\text{Base}]$) and a large primary kinetic isotope effect ($k_H / k_D \approx 3 - 6$), but zero deuterium exchange in recovered starting material.
- **Classic Substrates**: Aldol condensation dehydration ($\beta$-hydroxy carbonyls losing $\text{OH}^-$), eliminations of $\beta$-fluoro sulfones, and eliminations with $\beta$-nitro groups."""

    # Deepen Section 6: Benzyne Mechanism
    u6["sections"][5]["content"] += r"""

### Experimental Verification of the Benzyne Intermediate: Isotope Labeling & Trapping

When unactivated chlorobenzene is treated with potassium amide in liquid ammonia at $-33^\circ\text{C}$, aniline is formed rapidly. In 1953, John D. Roberts conclusively verified the existence of the transient symmetrical **benzyne intermediate** using carbon-14 isotopic labeling:

#### Roberts' $^{14}\text{C}$ Isotopic Experiment:
1. Roberts synthesized chlorobenzene labeled exclusively at the C1 position with carbon-14 ($[1\text{-}^{14}\text{C}]\text{-chlorobenzene}$):
   $$\text{C}_6\text{H}_5\text{Cl} \xrightarrow{\text{KNH}_2 / \text{NH}_3} \text{Aniline} \tag{6.14a}$$
2. If substitution occurred via direct displacement, the amino group would be attached exclusively to the labeled carbon ($100\% [1\text{-}^{14}\text{C}]\text{-aniline}$).
3. **Experimental Result**: The isolated aniline showed that:
   - **$48.5\%$** of the $^{14}\text{C}$ label was at C1 (bearing the amino group).
   - **$51.5\%$** of the $^{14}\text{C}$ label was at C2 (adjacent to the amino group)!
4. **Mechanistic Explanation**:
   Deprotonation by amide at C2 followed by loss of chloride generates a symmetrical **1,2-dehydrobenzene (benzyne)** intermediate:
   $$[1\text{-}^{14}\text{C}]\text{-Chlorobenzene} \xrightarrow{-\text{HCl}} [1,2\text{-Benzyne with } \text{C}1=\text{C}2 \text{ triple bond}] \tag{6.14b}$$
   Amide ion attacks either the labeled C1 or the unlabeled C2 with exactly equal probability ($50:50$), proving the intermediacy of benzyne!

#### Diels-Alder Trapping of Benzyne:
Because the in-plane $\pi$ bond of benzyne is formed by overlap of $sp^2$ orbitals tilted away from parallel by $60^\circ$, it is intensely strained ($\sim 210\text{ kJ/mol}$ of strain energy) and acts as an ultra-reactive dienophile.
Generating benzyne in the presence of furan traps it quantitatively in a $[4+2]$ cycloaddition to form **1,4-epoxy-1,4-dihydronaphthalene (endoxide)** in $>85\%$ yield!"""
    return u6
