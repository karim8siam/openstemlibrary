# -*- coding: utf-8 -*-
"""
expand_analytical_monograph.py
Injects advanced University Honors Research Monographs into all 9 units
of Analytical Chemistry (#46), elevating mathematical and theoretical depth.
Strict zero course numbers or marks. All math in raw strings r\"\"\"...\"\"\".
"""

def add_monographs_to_all_units(units):
    print("Injecting advanced University Honors Monographs across all 9 units...")

    monographs = [
        # Unit 1
        r"""

---

## Advanced University Honors Research Monograph: Bayesian Metrology vs Frequentist Decision Limits
In traditional analytical chemistry, measurement uncertainty is evaluated primarily through frequentist null hypothesis testing ($p$-values, Student's $t$, Fisher's $F$). However, when testing compliance near regulatory decision thresholds (e.g., European Union or EPA maximum residue limits), frequentist hypothesis testing produces paradoxes where sample size inflates false rejection rates.
The modern ISO/BIPM Guide to the Expression of Uncertainty in Measurement (GUM) and GUM Supplement 1 formulate analytical measurement through **Bayesian probability metrology**:

$$P(\theta \mid \mathbf{y}) = \frac{P(\mathbf{y} \mid \theta) \, P(\theta)}{\int P(\mathbf{y} \mid \theta) \, P(\theta) \, d\theta} \tag{M1.1}$$

where $\theta$ represents the true measurand concentration, $P(\theta)$ is the prior state of knowledge regarding sample provenance, $P(\mathbf{y} \mid \theta)$ is the instrumental likelihood function, and $P(\theta \mid \mathbf{y})$ is the posterior probability distribution.
Under a non-informative Jeffreys prior, the posterior credible interval converges toward the classical Student's $t$ interval; however, in forensic and clinical settings where historical calibration drift and blank baseline contamination exist, hierarchical Bayesian Markov Chain Monte Carlo (MCMC) modeling yields conformable decision risk probabilities:
$$R_{\text{consumer}} = \int_{\theta_{\text{limit}}}^{\infty} P(\theta \mid \mathbf{y}) \, d\theta \tag{M1.2}$$
This eliminates arbitrary significance level cutoffs ($\alpha = 0.05$) in favor of exact risk quantification.""",

        # Unit 2
        r"""

---

## Advanced University Honors Research Monograph: Pierre Gy's Theory of Sampling (TOS) & The Seven Errors
Pierre Gy's unified Theory of Sampling (TOS) is the only mathematically complete physical theory governing particulate sampling in science and industry. Gy proved that the total sampling variance $s_{\text{TE}}^2$ is the direct sum of seven fundamentally independent sampling errors:

$$s_{\text{TE}}^2 = s_{\text{FSE}}^2 + s_{\text{GSE}}^2 + s_{\text{PE}}^2 + s_{\text{WE}}^2 + s_{\text{IDE}}^2 + s_{\text{IEE}}^2 + s_{\text{IPE}}^2 \tag{M2.1}$$

1. **Fundamental Sampling Error ($s_{\text{FSE}}^2$)**: Arises from constitution heterogeneity (inherent differences between individual mineral grains). It is the only error that cannot be eliminated by mechanical design; it can only be reduced by comminution (reducing top particle size $d$).
   $$s_{\text{FSE}}^2 = C \, d^3 \left( \frac{1}{M_s} - \frac{1}{M_L} \right) \tag{M2.2}$$
   where $C$ is the sampling constant, $M_s$ is sample mass, and $M_L$ is lot mass.
2. **Grouping and Segregation Error ($s_{\text{GSE}}^2$)**: Arises from distribution heterogeneity (gravitational settling, density stratification). Suppressed by collecting many small increments ($N \ge 30$) rather than few large scoops.
3. **Increment Delimitation Error ($s_{\text{IDE}}^2$)**: Geometric error caused when the sampling cutter does not cut a strictly parallel, complete cross-section of the stream.
4. **Increment Extraction Error ($s_{\text{IEE}}^2$)**: Physical error when particles bounce out of or are deflected away from the cutter blade edges.
5. **Preparation Errors ($s_{\text{PE}}^2$)**: Cross-contamination, dust loss, moisture absorption, or chemical alteration during crushing and milling.
Compliance with ISO 3082 and ASTM E300 mandates that $s_{\text{IDE}}^2 = s_{\text{IEE}}^2 = 0$ by strict mechanical cutter geometry, ensuring that total error approaches the irreducible physical fundamental limit $s_{\text{FSE}}^2$.""",

        # Unit 3
        r"""

---

## Advanced University Honors Research Monograph: DLVO Theory of Colloidal Stability & Double-Layer Dynamics
In gravimetric analysis and qualitative group separation, whether a precipitate forms a crystalline, fast-filtering mass or remains a dispersed colloidal sol is governed by the **Derjaguin-Landau-Verwey-Overbeek (DLVO)** theory of colloidal stability.
The total interaction potential $V_{\text{total}}(H)$ between two colloidal particles separated by surface-to-surface distance $H$ is the sum of attractive London-van der Waals forces ($V_A$) and repulsive electrostatic electrical double layer forces ($V_R$):

$$V_{\text{total}}(H) = V_A(H) + V_R(H) = -\frac{A_H \, r_p}{12 H} + 2\pi \varepsilon_0 \varepsilon_r r_p \psi_0^2 \ln\left(1 + e^{-\kappa H}\right) \tag{M3.1}$$

where $A_H$ is the Hamaker constant, $r_p$ is particle radius, $\psi_0$ is surface potential (approximated by zeta potential $\zeta$), and $\kappa$ is the inverse Debye screening length:
$$\kappa = \sqrt{\frac{2 e^2 N_A I}{\varepsilon_0 \varepsilon_r k_B T}} \tag{M3.2}$$

```
                         DLVO Potential Energy Landscape
       Potential Energy V(H)
           ^
           |                  Primary Maximum (Repulsive Energy Barrier ΔV)
           |                     /\
           |                    /  \
           |                   /    \
           |                  /      \------- Secondary Minimum (Flocculation)
           0 ----------------+----------------\----------------------------> Distance H
           |                /                  \
           |               /                    \
           |              /                      \
           v  Primary Minimum (Irreversible Coagulation)
```

When an inert electrolyte (e.g., $0.1\text{ M NH}_4\text{NO}_3$) is added or the solution is heated:
1. Ionic strength $I$ increases, increasing $\kappa$ and compressing the electrical double layer.
2. The repulsive energy barrier $\Delta V$ drops below thermal kinetic energy ($k_B T$).
3. Colloidal particles cross the barrier into the deep primary minimum, undergoing rapid, irreversible coagulation into dense, easily filterable macro-aggregates.""",

        # Unit 4
        r"""

---

## Advanced University Honors Research Monograph: Molecular Mechanics & Bite Angles in Polydentate Chelation
The stability of multidentate metal chelates is determined by an intricate interplay of coordination geometry, metal ionic radius, and ligand conformational strain energy.
Using molecular mechanics force fields (MM3 and DFT/B3LYP), the total strain energy $\Delta U_{\text{strain}}$ associated with coordinating a multidentate ligand to a metal center is partitioned into four fundamental components:

$$\Delta U_{\text{strain}} = \sum K_b (b - b_0)^2 + \sum K_\theta (\theta - \theta_0)^2 + \sum \frac{V_n}{2} [1 + \cos(n\phi - \gamma)] + \sum \left( \frac{A}{r^{12}} - \frac{B}{r^6} \right) \tag{M4.1}$$

1. **The Coordinate Bite Angle ($\beta_{\text{bite}}$)**:
   For an ideal octahedral metal center ($\text{O}_h$), the target donor-metal-donor angle is $\theta_0 = 90^\circ$. For a 5-membered chelate ring formed by ethylenediamine or EDTA, the natural bite angle is $\beta_{\text{bite}} \approx 84^\circ\text{--}88^\circ$, which introduces negligible angle distortion ($\Delta U_\theta \approx 0$).
2. **Ligand Pre-organization Thermodynamics**:
   The stability difference between linear polyamines (e.g., trien) and macrocyclic equivalents (e.g., cyclam) is quantified by the pre-organization principle (Donald Cram):
   $$\Delta G^\circ = \Delta H^\circ - T(\Delta S^\circ_{\text{trans}} + \Delta S^\circ_{\text{rot}} + \Delta S^\circ_{\text{conf}}) \tag{M4.2}$$
   In open-chain ligands, coordinating to a metal freezes out dozens of rotational degrees of freedom ($\Delta S^\circ_{\text{conf}} \ll 0$). In macrocyclic and cryptand frameworks, the donor nitrogen atoms are already held in their optimal coordinate orientation in the free ligand, eliminating the conformational entropy penalty and yielding colossal stability constants ($\log K_f > 30$).""",

        # Unit 5
        r"""

---

## Advanced University Honors Research Monograph: High-Resolution Continuum Source AAS (HR-CS AAS)
In conventional atomic absorption spectroscopy, each element requires a separate, dedicated hollow cathode lamp emitting narrow resonance lines. In 2004, the commercialization of **High-Resolution Continuum Source AAS (HR-CS AAS)** fundamentally transformed atomic spectroscopy by replacing hundreds of individual lamps with a single, ultra-stable high-pressure Xenon short-arc lamp:

```
                  HR-CS AAS Echelle Optical Train Architecture
      Xe Short-Arc Lamp     Flame / Graphite Furnace     Double Monochromator:
      Continuum Source       Atomizer Chamber             Prism Pre-separator +
      (185 - 900 nm)        (Analyte Absorption)          Echelle Grating (High Order)
      +---------------+      +----------------------+     +--------------------------+
      |  Xe Arc Bulb  |----->|                      |---->| Orders 30-120 Dispersed  |
      +---------------+      +----------------------+     +-------------+------------+
                                                                        |
                                                                        v
                                                                 Linear CCD Array
                                                                 (Simultaneous Pixels)
```

### Optical and Mathematical Resolution Metrics
1. **Double Monochromator with Echelle Grating**:
   A quartz prism acts as an order sorter, followed by an Echelle diffraction grating blazed at a steep angle ($\theta_B \approx 65^\circ\text{ to }75^\circ$) operating in high diffraction orders ($m = 30\text{ to }120$).
   The resolving power is:
   $$R = \frac{\lambda}{\Delta \lambda} = m \, N_g \approx 100,000\text{ to }150,000 \tag{M5.1}$$
   yielding an unprecedented optical spectral bandpass of $\Delta \lambda \approx 1.5\text{ to }2.0\text{ pm per pixel}$ at $200\text{ nm}$.
2. **Linear CCD Array Pixel-Level Background Correction**:
   A linear array of $512$ charge-coupled device (CCD) pixels records the exact atomic absorption profile across the central pixels ($\text{CP}$) simultaneously with the immediate adjacent baseline pixels ($\text{BP}$):
   $$A_{\text{corrected}}(\lambda) = A_{\text{CP}} - \frac{1}{k} \sum_{i=1}^k A_{\text{BP},i} \tag{M5.2}$$
   Because background is measured at the exact identical instant as the analyte, high-frequency lamp flicker noise and dynamic furnace smoke transients are eliminated with mathematical perfection, expanding linear dynamic range by three orders of magnitude.""",

        # Unit 6
        r"""

---

## Advanced University Honors Research Monograph: Coupled Intraparticle Fickian Diffusion & Column Mass Transfer
In high-pressure ion-exchange chromatography, chromatographic peak broadening is governed by non-equilibrium mass-transfer kinetics inside the porous resin matrix. The migration of an analyte ion through the bed is modeled by the **General Rate Model (GRM)** of chromatography:

$$\frac{\partial C_i}{\partial t} + u_0 \frac{\partial C_i}{\partial z} = D_{\text{ax}} \frac{\partial^2 C_i}{\partial z^2} - \frac{3(1 - \varepsilon_b)}{\varepsilon_b \, R_p} k_{\text{film}} \left( C_i - \left. C_{p,i} \right|_{r = R_p} \right) \tag{M6.1}$$

Coupled with the radial intraparticle Fickian diffusion equation within the spherical bead ($0 \le r \le R_p$):
$$\varepsilon_p \frac{\partial C_{p,i}}{\partial t} + (1 - \varepsilon_p) \frac{\partial q_i}{\partial t} = D_{\text{pore}} \frac{1}{r^2} \frac{\partial}{\partial r}\left( r^2 \frac{\partial C_{p,i}}{\partial r} \right) \tag{M6.2}$$
where $C_i$ is mobile phase concentration, $C_{p,i}$ is intraparticle pore liquid concentration, $q_i$ is adsorbed stationary concentration, $\varepsilon_b$ is interstitial bed porosity, $\varepsilon_p$ is particle internal porosity, $R_p$ is bead radius, $k_{\text{film}}$ is the external film mass-transfer coefficient, and $D_{\text{pore}}$ is effective intraparticle pore diffusivity:
$$D_{\text{pore}} = \frac{\varepsilon_p \, D_m}{\tau_p} \tag{M6.3}$$
with $\tau_p \approx 2\text{--}6$ denoting the pore tortuosity factor.
This rigorous continuum model proves that reducing resin bead diameter from $10\,\mu\text{m}$ to $3\,\mu\text{m}$ decreases intraparticle diffusion equilibrium time by a factor of $(10/3)^2 \approx 11$, dramatically sharpening elution bands and enabling rapid sub-5-minute ion separations.""",

        # Unit 7
        r"""

---

## Advanced University Honors Research Monograph: Quantum Mechanical Franck-Condon Principle & Vibronic Transitions
The electronic absorption spectra of molecular chromophores in UV-Visible spectrophotometry consist of broad, envelope-like bands rather than sharp atomic lines. This spectral broadening is a direct manifestation of the quantum mechanical **Born-Oppenheimer approximation** and the **Franck-Condon principle**.

```
                Franck-Condon Nuclear Coordinate Energy Diagram
       Potential Energy E(R)
           ^
           |                  Excited State (E₁)
           |                       /‾‾‾‾‾‾\      v' = 2
           |                      /  •--•  \     v' = 1
           |                     /    •     \    v' = 0
           |                    +------------+
           |                         ^ Vertical Transition (ΔR ≈ 0)
           |                         | (Electronic transition is instantaneous: 10⁻¹⁵ s)
           |                  Ground State (E₀)
           |                       /‾‾‾‾‾‾\
           |                      /  •--•  \     v = 1
           |                     /    •     \    v = 0
           |                    +------------+
           0 ------------------------+-------------------------------------> Nuclear Distance R
                                     R₀
```

Because an electronic transition occurs on an attosecond timescale ($\tau_{\text{elec}} \sim 10^{-15}\text{ s}$) while nuclear vibrations require femtoseconds ($\tau_{\text{vib}} \sim 10^{-13}\text{ s}$), the nuclei remain essentially stationary during photon absorption ("vertical transition", $\Delta R \approx 0$).
The transition probability (and therefore the molar absorptivity $\varepsilon(\nu)$) is governed by the square of the transition dipole moment integral $\mathbf{M}_{if}$:

$$\varepsilon(\nu) \propto |\mathbf{M}_{if}|^2 = \left| \int \psi_{e,f}^* \, \hat{\boldsymbol{\mu}}_e \, \psi_{e,i} \, d\tau_e \right|^2 \times \left| \int \chi_{v',f}^* \, \chi_{v,i} \, dR \right|^2 \tag{M7.1}$$

The second integral is the **Franck-Condon overlap integral** between the ground vibrational wave function $\chi_{v,i}$ and the excited vibrational wave function $\chi_{v',f}$.
In condensed fluid solutions, collisional dephasing and continuous dielectric solvent cage fluctuations (Marcus solvation theory) smear out the discrete vibronic lines into the familiar smooth Gaussian absorption profiles observed in experimental spectrophotometry.""",

        # Unit 8
        r"""

---

## Advanced University Honors Research Monograph: Hildebrand Solubility Parameters & Cavitation Free Energy
The thermodynamic partition coefficient $K_D$ of a neutral solute between an aqueous phase and an organic solvent can be modeled from first principles using **Regular Solution Theory** and the concept of **Hildebrand solubility parameters** ($\delta$):

$$\delta = \sqrt{c_{\text{coh}}} = \sqrt{\frac{\Delta H_{\text{vap}} - RT}{V_m}} \tag{M8.1}$$

where $c_{\text{coh}}$ is the cohesive energy density, $\Delta H_{\text{vap}}$ is the enthalpy of vaporization, and $V_m$ is the molar volume of the pure liquid.
The standard Gibbs free energy of transfer $\Delta G_{\text{transfer}}^\circ$ is partitioned into three physical components:
$$\Delta G_{\text{transfer}}^\circ = \Delta G_{\text{cavitation}}^\circ + \Delta G_{\text{electrostatic}}^\circ + \Delta G_{\text{dispersion}}^\circ \tag{M8.2}$$
1. **Cavitation Free Energy ($\Delta G_{\text{cavitation}}^\circ$)**: The reversible work required to create a cavity within the solvent network large enough to accommodate the solute molecule. Because water possesses an immense cohesive energy density ($\delta_{\text{water}} = 47.9\text{ MPa}^{1/2}$) held by strong hydrogen bonding networks, creating a cavity in water carries a massive free energy penalty ($\Delta G_{\text{cav,aq}} \gg 0$).
2. **Hydrophobic Squeezing Driving Force**: Nonpolar organic solvents (e.g., hexane $\delta = 14.9\text{ MPa}^{1/2}$, chloroform $\delta = 19.0\text{ MPa}^{1/2}$) have much lower cohesive energy densities. The system minimizes total Gibbs free energy by expelling the hydrophobic solute from water into the organic solvent, allowing water molecules to re-form hydrogen bonds.
This fundamental cavitation thermodynamic driving force explains why distribution ratios $K_D$ increase exponentially with solute molecular surface area and hydrophobic alkyl chain length.""",

        # Unit 9
        r"""

---

## Advanced University Honors Research Monograph: J. Calvin Giddings' Stochastic Theory of Chromatography
In 1955, J. Calvin Giddings published the **Stochastic Theory of Chromatography**, proving that chromatographic zone spreading is fundamentally governed by a Poisson random walk of individual solute molecules migrating down the column.
A single solute molecule alternates randomly between two discrete physical states:
1. **Mobile State**: Moving forward at interstitial fluid velocity $v_m$ for a random time $\tau_m$ governed by exponential probability density:
   $$P(\tau_m) = k_a \exp(-k_a \tau_m) \tag{M9.1}$$
2. **Stationary State**: Adsorbed and motionless for a random time $\tau_s$ governed by:
   $$P(\tau_s) = k_d \exp(-k_d \tau_s) \tag{M9.2}$$
where $k_a$ is the adsorption rate constant and $k_d$ is the desorption rate constant.

By applying the Central Limit Theorem to the cumulative sum of $N_s$ random sorption-desorption steps over total migration time $t$, Giddings proved that the spatial probability density distribution $P(z, t)$ asymptotically converges to a Gaussian distribution:

$$\sigma_z^2 = 2 D_{\text{eff}} \, t = 2 \left( D_{\text{eddy}} + D_m + \frac{k'}{(1 + k')^2} \frac{u^2}{k_d} \right) t \tag{M9.3}$$

Dividing by migration distance $L = u t / (1 + k')$ yields the exact theoretical plate height:
$$H = \frac{\sigma_z^2}{L} = 2 \frac{D_{\text{eddy}}}{u} + \frac{2 D_m}{u} + \frac{2 k'}{(1 + k')^2} \frac{u}{k_d} \tag{M9.4}$$
This stochastic formulation provides the profound physical link uniting microscopic quantum collision kinetics with macroscopic chromatographic band shapes."""
    ]

    for i, u in enumerate(units):
        u["sections"][-1]["content"] += monographs[i]
        print(f"  Injected Monograph into {u['title']}")
