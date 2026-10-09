# -*- coding: utf-8 -*-
"""
expand_kinetics_deep.py
Enriches sections across all 10 units of Molecular Motion and Reaction Kinetics with
rigorous reference tables, Chapman-Enskog transport matrices, non-Arrhenius models,
integrated rate matrices, and analytical differential proofs.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def enrich_deep_content(units):
    enrichments = {
        "unit-1": {
            "sec-1-1": r"""

### Reference Table: Gas Transport Properties & Molecular Dimensions at 298.15 K and 1.00 atm
Below are benchmark experimental transport properties and collision dimensions derived from viscosity and thermal conductivity measurements using the Lennard-Jones (12-6) potential model:

| Gas Species | Formula | Molar Mass $M$ ($\text{g/mol}$) | Hard-Sphere Diameter $d$ ($\text{Å}$) | Mean Free Path $\lambda$ ($\text{nm}$) | Viscosity $\eta$ ($\mu\text{Pa}\cdot\text{s}$) | Thermal Conductivity $\kappa$ ($\text{mW}/(\text{m}\cdot\text{K})$) | Self-Diffusion $D$ ($10^{-5}\text{ m}^2/\text{s}$) |
|---|---|---|---|---|---|---|---|
| **Hydrogen** | $H_2$ | $2.016$ | $2.72$ | $112.5$ | $8.85$ | $182.9$ | $14.5$ |
| **Helium** | $He$ | $4.003$ | $2.18$ | $175.4$ | $19.86$ | $155.7$ | $17.2$ |
| **Methane** | $CH_4$ | $16.043$ | $3.80$ | $57.8$ | $11.05$ | $34.3$ | $2.25$ |
| **Nitrogen** | $N_2$ | $28.013$ | $3.75$ | $59.3$ | $17.81$ | $26.0$ | $2.05$ |
| **Carbon Monoxide** | $CO$ | $28.010$ | $3.76$ | $59.0$ | $17.75$ | $25.1$ | $2.04$ |
| **Oxygen** | $O_2$ | $31.999$ | $3.61$ | $64.0$ | $20.65$ | $26.7$ | $2.18$ |
| **Argon** | $Ar$ | $39.948$ | $3.64$ | $63.0$ | $22.62$ | $17.9$ | $1.90$ |
| **Carbon Dioxide** | $CO_2$ | $44.010$ | $3.99$ | $52.4$ | $14.95$ | $16.8$ | $1.10$ |
| **Sulfur Hexafluoride**| $SF_6$ | $146.056$ | $5.13$ | $31.7$ | $15.30$ | $13.6$ | $0.58$ |

### Chapman-Enskog Transport Theory for Realistic Potentials
In real gases, molecules are not rigid hard spheres; intermolecular attractions ($r^{-6}$) and Pauli repulsions ($r^{-12}$) alter collision dynamics. The rigorous Chapman-Enskog solution of the Boltzmann transport equation yields:
$$\eta = \frac{5}{16} \frac{\sqrt{\pi m k_B T}}{\pi \sigma^2 \Omega^{(2,2)*}(T^*)}$$
$$D = \frac{3}{8} \frac{\sqrt{\pi k_B^3 T^3 / m}}{P \pi \sigma^2 \Omega^{(1,1)*}(T^*)}$$
where $\sigma$ is the collision diameter, $T^* = k_B T / \epsilon$ is the reduced temperature relative to the Lennard-Jones well depth $\epsilon$, and $\Omega^{(l,s)*}(T^*)$ are dimensionless collision integrals. At high temperatures ($T^* \gg 1$), $\Omega^* \to 1$ and hard-sphere scaling is recovered; at low temperatures, attractive well trapping increases $\Omega^*$, enhancing the effective collision cross-section."""
        },

        "unit-2": {
            "sec-2-1": r"""

### Benchmark Table: Limiting Molar Ionic Conductivities & Hydrodynamic Radii in Water at 298.15 K
At infinite dilution, inter-ionic electrostatic couplings vanish, yielding independent limiting molar conductivities $\lambda_i^\circ$:

| Ion | $z_i$ | $\lambda_i^\circ$ ($\text{S}\cdot\text{cm}^2/\text{mol}$) | Mobility $u_i$ ($10^{-8}\text{ m}^2/(\text{V}\cdot\text{s})$) | Stokes Radius $r_{\text{Stokes}}$ ($\text{Å}$) | Crystal Radius $r_{\text{cryst}}$ ($\text{Å}$) | Hydration Number $n_{\text{hyd}}$ |
|---|---|---|---|---|---|---|
| $\text{H}^+ (\text{H}_3\text{O}^+)$ | $+1$ | $349.65$ | $36.23$ | $0.26$ | $1.00$ | Grotthuss mechanism |
| $\text{Li}^+$ | $+1$ | $38.68$ | $4.01$ | $2.38$ | $0.76$ | $5.2$ |
| $\text{Na}^+$ | $+1$ | $50.10$ | $5.19$ | $1.84$ | $1.02$ | $3.5$ |
| $\text{K}^+$ | $+1$ | $73.50$ | $7.62$ | $1.25$ | $1.38$ | $1.9$ |
| $\text{Rb}^+$ | $+1$ | $77.80$ | $8.06$ | $1.18$ | $1.52$ | $1.2$ |
| $\text{Cs}^+$ | $+1$ | $77.26$ | $8.01$ | $1.19$ | $1.67$ | $1.0$ |
| $\text{NH}_4^+$ | $+1$ | $73.55$ | $7.62$ | $1.25$ | $1.48$ | $1.8$ |
| $\text{Mg}^{2+}$ | $+2$ | $106.10$ ($53.05$ eq) | $5.50$ | $3.47$ | $0.72$ | $12.0$ |
| $\text{Ca}^{2+}$ | $+2$ | $119.00$ ($59.50$ eq) | $6.17$ | $3.10$ | $1.00$ | $8.0$ |
| $\text{La}^{3+}$ | $+3$ | $209.10$ ($69.70$ eq) | $7.22$ | $3.97$ | $1.03$ | $16.0$ |
| $\text{OH}^-$ | $-1$ | $198.30$ | $20.55$ | $0.46$ | $1.37$ | Grotthuss mechanism |
| $\text{F}^-$ | $-1$ | $55.40$ | $5.74$ | $1.66$ | $1.33$ | $2.7$ |
| $\text{Cl}^-$ | $-1$ | $76.35$ | $7.91$ | $1.21$ | $1.81$ | $0.0$ |
| $\text{Br}^-$ | $-1$ | $78.10$ | $8.09$ | $1.18$ | $1.96$ | $0.0$ |
| $\text{I}^-$ | $-1$ | $76.84$ | $7.96$ | $1.20$ | $2.20$ | $0.0$ |
| $\text{SO}_4^{2-}$ | $-2$ | $160.00$ ($80.00$ eq) | $8.29$ | $2.30$ | $2.30$ | Structure breaker |

### Quantum Origin of the Grotthuss Proton Conduction
The anomalously high limiting conductivity of hydronium ($\lambda^\circ = 349.7$) and hydroxide ($\lambda^\circ = 198.3$) arises from structural proton translocation across the hydrogen-bonded water network rather than physical hydrodynamic Stokes diffusion:
1. An excess proton forms an Eigen cation ($\text{H}_9\text{O}_4^+$) coordinated to three water molecules.
2. Fluctuation of the surrounding second hydration shell compresses an adjacent hydrogen bond, converting the Eigen complex into a Zundel cation ($\text{H}_5\text{O}_2^+$) with a symmetric low-barrier double-well potential.
3. Fast quantum tunneling and adiabatic barrier crossing transfer the proton in $\tau_{\text{hop}} \approx 1.5\text{ ps}$, followed by rapid hydrogen-bond cleavage and reorientation."""
        },

        "unit-3": {
            "sec-3-1": r"""

### Master Table: Diffusion Coefficients Across States of Matter & Molecular Sizes
Diffusion coefficients span more than twelve orders of magnitude from light gases to solid-state crystals:

| Medium / Phase | Diffusing Species | Temperature ($T$) | Diffusion Coefficient $D$ ($\text{m}^2/\text{s}$) | Characteristic Time $\tau = L^2 / (2D)$ for $L = 10\;\mu\text{m}$ |
|---|---|---|---|---|
| **Gas ($1\text{ atm}$)** | $H_2$ in Air | $298\text{ K}$ | $7.8 \times 10^{-5}$ | $0.64\;\mu\text{s}$ |
| **Gas ($1\text{ atm}$)** | $CO_2$ in Air | $298\text{ K}$ | $1.6 \times 10^{-5}$ | $3.1\;\mu\text{s}$ |
| **Gas ($1\text{ atm}$)** | Benzene in Air | $298\text{ K}$ | $8.8 \times 10^{-6}$ | $5.7\;\mu\text{s}$ |
| **Liquid (Aqueous)** | Water self-diffusion | $298\text{ K}$ | $2.299 \times 10^{-9}$ | $21.7\text{ ms}$ |
| **Liquid (Aqueous)** | $NaCl$ (mutual) | $298\text{ K}$ | $1.61 \times 10^{-9}$ | $31.1\text{ ms}$ |
| **Liquid (Aqueous)** | Glucose ($M = 180$) | $298\text{ K}$ | $6.73 \times 10^{-10}$ | $74.3\text{ ms}$ |
| **Liquid (Aqueous)** | Bovine Serum Albumin ($66\text{ kDa}$)| $298\text{ K}$ | $6.07 \times 10^{-11}$ | $824\text{ ms}$ |
| **Liquid (Aqueous)** | Tobacco Mosaic Virus ($40\text{ MDa}$)| $298\text{ K}$ | $4.6 \times 10^{-12}$ | $10.9\text{ s}$ |
| **Viscous Liquid** | Glycerol self-diffusion | $298\text{ K}$ | $1.7 \times 10^{-12}$ | $29.4\text{ s}$ |
| **Polymer Melt** | Polystyrene in melt | $450\text{ K}$ | $1.0 \times 10^{-15}$ | $14\text{ hours}$ |
| **Solid Crystal** | $C$ in $\alpha\text{-Fe}$ (interstitial) | $1200\text{ K}$ | $1.0 \times 10^{-10}$ | $500\text{ ms}$ |
| **Solid Crystal** | $Au$ in $Cu$ (substitutional) | $1200\text{ K}$ | $5.0 \times 10^{-14}$ | $1000\text{ s}$ |
| **Solid Crystal** | $Cu$ in $Cu$ self-diffusion | $300\text{ K}$ | $10^{-34}$ | $> 10^{18}\text{ years}$ |"""
        },

        "unit-4": {
            "sec-4-1": r"""

### Master Classification Table: Analytical Solutions to Empirical Rate Laws

| Reaction Order | Differential Rate Law | Integrated Rate Law | Linear Coordinate Plot | Slope ($m$) & Intercept ($b$) | Rate Constant Units | Half-Life Expression ($t_{1/2}$) | Three-Quarter Life ($t_{3/4}$) |
|---|---|---|---|---|---|---|---|
| **Zero Order** ($n=0$) | $-\frac{d[A]}{dt} = k$ | $[A]_t = [A]_0 - k t$ | $[A]_t \text{ vs } t$ | $m = -k$, $b = [A]_0$ | $\text{M}\cdot\text{s}^{-1}$ | $t_{1/2} = \frac{[A]_0}{2 k}$ | $t_{3/4} = \frac{3 [A]_0}{4 k}$ |
| **First Order** ($n=1$) | $-\frac{d[A]}{dt} = k [A]$ | $\ln[A]_t = \ln[A]_0 - k t$ | $\ln[A]_t \text{ vs } t$ | $m = -k$, $b = \ln[A]_0$ | $\text{s}^{-1}$ | $t_{1/2} = \frac{\ln 2}{k}$ | $t_{3/4} = \frac{\ln 4}{k} = 2 t_{1/2}$ |
| **Second Order (symmetric)** | $-\frac{d[A]}{dt} = k [A]^2$ | $\frac{1}{[A]_t} = \frac{1}{[A]_0} + k t$ | $\frac{1}{[A]_t} \text{ vs } t$ | $m = +k$, $b = \frac{1}{[A]_0}$ | $\text{M}^{-1}\cdot\text{s}^{-1}$ | $t_{1/2} = \frac{1}{k [A]_0}$ | $t_{3/4} = \frac{3}{k [A]_0} = 3 t_{1/2}$ |
| **Second Order (asymmetric)**| $-\frac{d[A]}{dt} = k [A][B]$ | $\ln\left(\frac{[B]_t [A]_0}{[A]_t [B]_0}\right) = ([B]_0 - [A]_0) k t$ | $\ln\left(\frac{[B]_t}{[A]_t}\right) \text{ vs } t$ | $m = ([B]_0 - [A]_0) k$ | $\text{M}^{-1}\cdot\text{s}^{-1}$ | Dependent on $[B]_0 / [A]_0$ | Dependent on $[B]_0 / [A]_0$ |
| **Third Order (symmetric)** | $-\frac{d[A]}{dt} = k [A]^3$ | $\frac{1}{[A]_t^2} = \frac{1}{[A]_0^2} + 2 k t$ | $\frac{1}{[A]_t^2} \text{ vs } t$ | $m = +2k$, $b = \frac{1}{[A]_0^2}$ | $\text{M}^{-2}\cdot\text{s}^{-1}$ | $t_{1/2} = \frac{3}{2 k [A]_0^2}$ | $t_{3/4} = \frac{15}{2 k [A]_0^2} = 5 t_{1/2}$ |
| **$n$-th Order ($n \ne 1$)** | $-\frac{d[A]}{dt} = k [A]^n$ | $\frac{1}{[A]_t^{n-1}} = \frac{1}{[A]_0^{n-1}} + (n-1) k t$ | $\frac{1}{[A]_t^{n-1}} \text{ vs } t$ | $m = (n-1)k$ | $\text{M}^{1-n}\cdot\text{s}^{-1}$ | $t_{1/2} = \frac{2^{n-1} - 1}{(n-1) k [A]_0^{n-1}}$ | $t_{3/4} = \frac{4^{n-1} - 1}{(n-1) k [A]_0^{n-1}}$ |
| **Reversible First-Order** | $-\frac{d[A]}{dt} = k_1 [A] - k_{-1} [B]$ | $\ln\left(\frac{[A]_0 - [A]_{\text{eq}}}{[A]_t - [A]_{\text{eq}}}\right) = (k_1 + k_{-1}) t$| $\ln([A]_t - [A]_{\text{eq}}) \text{ vs } t$| $m = -(k_1 + k_{-1})$ | $\text{s}^{-1}$ | $t_{1/2} = \frac{\ln 2}{k_1 + k_{-1}}$ | Relaxation time $\tau = \frac{1}{k_1 + k_{-1}}$ |"""
        },

        "unit-5": {
            "sec-5-1": r"""

### Thermodynamic Activation Parameters Matrix for Prototypical Reactions
Applying Eyring Transition State Theory to rate constants across varied chemical mechanisms demonstrates how activation enthalpy ($\Delta H^\ddagger$), activation entropy ($\Delta S^\ddagger$), and activation free energy ($\Delta G^\ddagger$) govern reaction velocity at $298.15\text{ K}$:

| Reaction Mechanism | Prototypical Example | $k(298\text{ K})$ | $E_a$ ($\text{kJ/mol}$) | $\Delta H^\ddagger$ ($\text{kJ/mol}$) | $\Delta S^\ddagger$ ($\text{J}/(\text{mol}\cdot\text{K})$) | $\Delta G^\ddagger$ ($\text{kJ/mol}$) |
|---|---|---|---|---|---|---|
| **Radical Recombination** | $2 CH_3^\bullet \longrightarrow C_2H_6$ | $2.5 \times 10^{10}\text{ M}^{-1}\text{s}^{-1}$ | $0.0$ | $-2.5$ | $-52.0$ | $+13.0$ |
| **Bimolecular Radical Transfer**| $OH^\bullet + CH_4 \longrightarrow H_2O + CH_3^\bullet$ | $6.4 \times 10^6\text{ M}^{-1}\text{s}^{-1}$ | $+18.5$ | $+16.0$ | $-65.0$ | $+35.4$ |
| **Unimolecular Isomerization** | $\text{Cyclopropane} \longrightarrow \text{Propene}$ | $1.2 \times 10^{-15}\text{ s}^{-1}$ | $+272.0$ | $+269.5$ | $+40.0$ | $+257.6$ |
| **Bimolecular Gas Diels-Alder** | $1,3\text{-Butadiene} + \text{Ethene} \longrightarrow \text{Cyclohexene}$ | $3.2 \times 10^{-18}\text{ M}^{-1}\text{s}^{-1}$| $+115.0$ | $+112.5$ | $-142.0$ | $+154.8$ |
| **Alkaline Ester Hydrolysis** | $EtOAc + OH^- \longrightarrow AcO^- + EtOH$ | $0.11\text{ M}^{-1}\text{s}^{-1}$ | $+47.0$ | $+44.5$ | $-110.0$ | $+77.3$ |
| **Acid Sucrose Inversion** | $\text{Sucrose} + H_3O^+ \longrightarrow \text{Glc} + \text{Fru}$ | $1.8 \times 10^{-4}\text{ M}^{-1}\text{s}^{-1}$ | $+108.0$ | $+105.5$ | $+32.0$ | $+96.0$ |
| **Enzyme Turnover ($k_{\text{cat}}$)**| Carbonic Anhydrase ($CO_2 + H_2O$)| $1.0 \times 10^6\text{ s}^{-1}$ | $+38.0$ | $+35.5$ | $-10.0$ | $+38.5$ |"""
        },

        "unit-6": {
            "sec-6-1": r"""

### Master Reference Table: Kinetic Isotope Effects Across Chemical Coordinates

| Isotope Substitution | Mechanistic Coordinate Type | Prototypical Transformation | Expected Semiclassical KIE ($298\text{ K}$) | Observed Experimental KIE | Physical Mechanism |
|---|---|---|---|---|---|
| **$^1H / ^2H$ ($H/D$)** | Primary ($C-H$ cleavage) | $PhCH_2Br + OH^- \longrightarrow PhCH_2OH$ ($S_N2$) | $2.0 - 3.5$ | $2.3$ | Partial bond breaking in transition state |
| **$^1H / ^2H$ ($H/D$)** | Primary ($C-H$ cleavage) | 2-Phenylethyl bromide $+ EtO^-$ ($E2$) | $6.0 - 7.5$ | $7.1$ | Symmetric linear Transition State |
| **$^1H / ^2H$ ($H/D$)** | Primary ($H^+$ transfer) | Lipoxygenase / Dehydrogenase | $6.5$ (max semiclassical) | **$25 - 80$** | **Quantum Mechanical Wavepacket Tunneling** |
| **$^1H / ^2H$ ($H/D$)** | $\alpha$-Secondary ($sp^3 \to sp^2$)| $t\text{-BuCl} \longrightarrow t\text{-Bu}^+ + Cl^-$ ($S_N1$) | $1.15 - 1.25$ | $1.22$ | Out-of-plane bending vibration softening |
| **$^1H / ^2H$ ($H/D$)** | $\alpha$-Secondary ($sp^2 \to sp^3$)| Nucleophilic addition to ketone | $0.80 - 0.90$ (inverse) | $0.85$ | Steric crowding and bending stiffening |
| **$^1H / ^2H$ ($H/D$)** | $\beta$-Secondary | Hydrolysis of $(CD_3)_3CCl$ | $1.20 - 1.40$ | $1.33$ | Hyperconjugative delocalization into empty p-orbital |
| **$^{12}C / ^{13}C$** | Primary ($C-C$ cleavage) | Malonic acid decarboxylation | $1.03 - 1.05$ | $1.045$ | Zero-point energy shift in heavy atom stretch |
| **$^{14}N / ^{15}N$** | Primary ($N-N$ cleavage) | Diazonium salt decomposition | $1.02 - 1.04$ | $1.038$ | Nitrogen extrusion |
| **$^{35}Cl / ^{37}Cl$** | Primary ($C-Cl$ leaving group)| Solvolysis of alkyl chlorides | $1.008 - 1.011$ | $1.009$ | Leaving group carbon-chlorine bond rupture |"""
        },

        "unit-7": {
            "sec-7-1": r"""

### Unimolecular Fall-Off Parameters Reference Table
High-pressure limiting rate constants ($k_\infty$), low-pressure second-order constants ($k_0$), transition half-pressures ($P_{1/2}$), and Hinshelwood effective oscillator counts ($s$):

| Unimolecular Reaction | Temperature ($T$) | $k_\infty$ ($\text{s}^{-1}$) | $k_0$ ($\text{M}^{-1}\text{s}^{-1}$) | Transition Pressure $P_{1/2}$ | Effective Oscillators $s$ | Real Vibrational Modes $3N-6$ |
|---|---|---|---|---|---|---|
| $\text{Cyclopropane} \longrightarrow \text{Propene}$ | $770\text{ K}$ | $1.56 \times 10^{-3}$ | $3.68 \times 10^2$ | $4.2\text{ Torr}$ | $12$ | $21$ |
| $CH_3NC \longrightarrow CH_3CN$ | $503\text{ K}$ | $3.55 \times 10^{-4}$ | $2.80 \times 10^2$ | $1.3\text{ Torr}$ | $8$ | $12$ |
| $CH_3N=NCH_3 \longrightarrow C_2H_6 + N_2$ | $600\text{ K}$ | $3.40 \times 10^{-4}$ | $8.50 \times 10^1$ | $33.0\text{ Torr}$ | $12$ | $24$ |
| $C_2H_5Cl \longrightarrow C_2H_4 + HCl$ | $700\text{ K}$ | $2.20 \times 10^{-3}$ | $1.15 \times 10^2$ | $15.5\text{ Torr}$ | $9$ | $18$ |
| $N_2O_5 \longrightarrow NO_2 + NO_3$ | $300\text{ K}$ | $4.50 \times 10^{-1}$ | $2.20 \times 10^3$ | $0.18\text{ Torr}$ | $10$ | $15$ |"""
        },

        "unit-8": {
            "sec-8-1": r"""

### Hydrocarbon Combustion & Explosion Limits Reference Matrix

| Fuel / Oxidizer System | Stoichiometric Composition | Lower Explosion Limit (LEL, $\%$) | Upper Explosion Limit (UEL, $\%$) | Autoignition Temp ($T_{\text{auto}}$, $^\circ\text{C}$) | Laminar Flame Speed $S_L$ ($\text{cm/s}$) | Adiabatic Flame Temp ($T_b$, $\text{K}$) |
|---|---|---|---|---|---|---|
| **Hydrogen / Air** | $29.6\%\text{ }H_2$ | $4.0\%$ | $75.0\%$ | $560^\circ\text{C}$ | $210$ | $2380$ |
| **Methane / Air** | $9.5\%\text{ }CH_4$ | $5.0\%$ | $15.0\%$ | $580^\circ\text{C}$ | $38$ | $2220$ |
| **Propane / Air** | $4.0\%\text{ }C_3H_8$ | $2.1\%$ | $9.5\%$ | $470^\circ\text{C}$ | $43$ | $2260$ |
| **Ethylene / Air** | $6.5\%\text{ }C_2H_4$ | $2.7\%$ | $36.0\%$ | $450^\circ\text{C}$ | $68$ | $2375$ |
| **Acetylene / Air** | $7.7\%\text{ }C_2H_2$ | $2.5\%$ | $100.0\%$ (pure decomposition) | $305^\circ\text{C}$ | $155$ | $2540$ |
| **Carbon Monoxide / Air**| $29.6\%\text{ }CO$ | $12.5\%$ | $74.0\%$ | $609^\circ\text{C}$ | $45$ (moist) | $2385$ |"""
        },

        "unit-9": {
            "sec-9-1": r"""

### Comprehensive Enzyme Inhibition Diagnostic Matrix
Comparison of classical reversible inhibition modes in Michaelis-Menten kinetics:

| Inhibition Type | Enzyme Binding Equilibrium | Apparent $V_{\max}'$ | Apparent $K_m'$ | Double Reciprocal Lineweaver-Burk Intercepts | High $[S]$ Behavior | Prototypical Biological Example |
|---|---|---|---|---|---|---|
| **Competitive** | Inhibitor binds only to free enzyme $E$ ($K_I$) | $V_{\max}$ (unchanged) | $K_m \left( 1 + \frac{[I]}{K_I} \right) > K_m$ | Identical y-intercept ($1/V_{\max}$), x-intercept shifts right | Completely overcome by high substrate $[S]$ | Methotrexate inhibiting Dihydrofolate Reductase |
| **Uncompetitive**| Inhibitor binds only to $ES$ complex ($K_I'$) | $\frac{V_{\max}}{1 + [I]/K_I'} < V_{\max}$ | $\frac{K_m}{1 + [I]/K_I'} < K_m$ | Parallel lines! Both slope unchanged, y and x intercepts shift | Cannot be overcome by high substrate $[S]$ | Lithium inhibiting Inositol Monophosphatase |
| **Non-Competitive (Pure)** | Inhibitor binds equally to $E$ and $ES$ ($K_I = K_I'$) | $\frac{V_{\max}}{1 + [I]/K_I} < V_{\max}$ | $K_m$ (unchanged) | Identical x-intercept ($-1/K_m$), y-intercept shifts upward | $V_{\max}$ permanently depressed | Heavy metal ions ($Pb^{2+}, Hg^{2+}$) binding cysteine thiols |
| **Mixed Inhibition** | Inhibitor binds both $E$ and $ES$ with $K_I \ne K_I'$ | $\frac{V_{\max}}{1 + [I]/K_I'} < V_{\max}$ | $K_m \frac{1 + [I]/K_I}{1 + [I]/K_I'}$ | Lines intersect in second or third quadrant (left of y-axis) | Both $V_{\max}$ and $K_m$ altered | Non-nucleoside reverse transcriptase inhibitors |"""
        },

        "unit-10": {
            "sec-10-1": r"""

### Polanyi Rules & Potential Energy Surface Topology Matrix

| Reaction Class | Canonical Chemical Reaction | $\Delta H_r^\circ$ ($\text{kJ/mol}$) | Barrier Location | Polanyi Classification | Optimum Energy for Reaction | Product Energy Disposal |
|---|---|---|---|---|---|---|
| **Exothermic** | $F + H_2 \longrightarrow HF + H$ | $-134.0$ | Entrance Valley | **Early Barrier (Attractive PES)** | **Translational Energy** ($E_{\text{trans}}$) | High Product Vibration ($v' = 2, 3$) |
| **Exothermic** | $H + Cl_2 \longrightarrow HCl + Cl$ | $-188.0$ | Entrance Valley | **Early Barrier (Attractive PES)** | **Translational Energy** ($E_{\text{trans}}$) | High Product Vibration ($v' = 3 - 6$) |
| **Thermoneutral**| $H + H_2 \longrightarrow H_2 + H$ | $0.0$ | Symmetric Saddle Point | **Central Barrier** | Both Translation & Vibration | Moderate Translation & Vibration |
| **Endothermic** | $H + HF \longrightarrow H_2 + F$ | $+134.0$ | Exit Valley | **Late Barrier (Repulsive PES)** | **Reactant Vibration** ($E_{\text{vib}}$) | High Product Translation ($E_{\text{trans}}'$) |
| **Endothermic** | $Cl + HCl \longrightarrow Cl_2 + H$| $+188.0$ | Exit Valley | **Late Barrier (Repulsive PES)** | **Reactant Vibration** ($E_{\text{vib}}$) | High Product Translation ($E_{\text{trans}}'$) |
| **Harpoon Reaction**| $K + Br_2 \longrightarrow KBr + Br$ | $-175.0$ | Long-Range Curve Crossing | **Harpoon Electron Jump ($R_c \approx 8\text{ Å}$)**| Low Thermal Energy Suffices | Forward Stripping Rebound ($KBr$) |"""
        }
    }

    for u in units:
        uid = u["id"]
        if uid in enrichments:
            for s in u["sections"]:
                sid = s["id"]
                if sid in enrichments[uid]:
                    s["content"] += enrichments[uid][sid]

    return units

if __name__ == "__main__":
    from build_kinetics_units_1_2_3 import get_units_1_2_3
    from build_kinetics_units_4_5_6 import get_units_4_5_6
    from build_kinetics_units_7_8_9_10 import get_units_7_8_9_10
    from expand_kinetics_section8 import inject_section_8
    from expand_kinetics_problem8 import inject_problem_8
    from expand_kinetics_problem9 import inject_problem_9

    all_u = get_units_1_2_3() + get_units_4_5_6() + get_units_7_8_9_10()
    all_u = inject_section_8(all_u)
    all_u = inject_problem_8(all_u)
    all_u = inject_problem_9(all_u)
    all_u = enrich_deep_content(all_u)
    print("Enriched deep content across all units successfully!")
