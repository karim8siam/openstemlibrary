# -*- coding: utf-8 -*-
"""
expand_kinetics_problem9.py
Injects Problem 9 across all 10 units of Molecular Motion and Reaction Kinetics.
Brings total problems from 80 to 90 (9 per unit).
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def inject_problem_9(units):
    prob9_dict = {
        "unit-1": {
            "id": "p1-9",
            "title": "Supersonic Free-Jet Terminal Mach Number & Cryogenic Temperature Freezing",
            "difficulty": "Hard",
            "statement": r"""A supersonic molecular beam source operates by expanding pure argon gas ($M = 39.948\text{ g/mol}$, $\gamma = C_p / C_v = 5/3 = 1.6667$) from a high-pressure stagnation reservoir at stagnation temperature $T_0 = 300.0\text{ K}$ and stagnation pressure $P_0 = 10.0\text{ bar}$ ($1.00 \times 10^6\text{ Pa}$) through a circular nozzle of orifice diameter $d_n = 100.0\;\mu\text{m}$ ($1.00 \times 10^{-4}\text{ m}$) into an ultra-high vacuum chamber.
According to the Anderson-Fenn aerodynamic continuum-to-free-molecular expansion theory:
- The terminal Mach number $M_\infty$ is limited by collisional cessation ("freezing"):
  $$M_\infty = A \cdot \left( \frac{P_0 d_n}{k_B T_0} \right)^{(\gamma - 1)/\gamma} = 2.05 \cdot \left( n_0 d_n \sigma \right)^{(\gamma - 1)/\gamma}$$
  For argon, experimental calibrations give the empirical Anderson relation: $M_\infty = 1.17 \cdot \left( \frac{P_0 d_n}{k_B T_0} \right)^{0.40} \approx 28.5$.

Using the 1D isentropic aerodynamic relations:
$$\frac{T}{T_0} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{-1}$$
$$\frac{P}{P_0} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{-\gamma / (\gamma - 1)}$$
and the maximum theoretical terminal flow velocity:
$$u_\infty = \sqrt{\frac{2 \gamma R T_0}{(\gamma - 1) M}}$$

(a) Calculate the maximum theoretical flow velocity $u_\infty$ of the argon beam in $\text{m/s}$.
(b) For a terminal Mach number of $M_\infty = 28.50$, calculate the frozen terminal translational temperature $T_\infty$ of the argon atoms in Kelvin.
(c) Calculate the narrowness of the velocity distribution characterized by the speed ratio $S = u_\infty / \sqrt{2 R T_\infty / M}$ and the fractional velocity spread $\Delta v / u_\infty$.""",
            "solution": r"""**Step 1: Calculate maximum theoretical flow velocity $u_\infty$**
In a free-jet expansion, all thermal enthalpy $H_0 = C_p T_0$ is converted into directed macroscopic kinetic energy $\frac{1}{2} M u_\infty^2$:
$$u_\infty = \sqrt{\frac{2 C_p T_0}{M}} = \sqrt{\frac{2 \gamma R T_0}{(\gamma - 1) M}}$$
For monoatomic argon:
$$\gamma = \frac{5}{3} \implies \gamma - 1 = \frac{2}{3} \implies \frac{\gamma}{\gamma - 1} = \frac{5/3}{2/3} = \frac{5}{2} = 2.50$$
$$2 \times \frac{\gamma}{\gamma - 1} = 5.00$$
$$u_\infty = \sqrt{\frac{5 R T_0}{M}}$$
Substitute values:
$$R = 8.314462\text{ J}/(\text{mol}\cdot\text{K}), \quad T_0 = 300.0\text{ K}, \quad M = 0.039948\text{ kg/mol}$$
$$5 R T_0 = 5 \times 8.314462 \times 300.0 = 12471.69\text{ J/mol}$$
$$u_\infty = \sqrt{\frac{12471.69}{0.039948}} = \sqrt{3.12198 \times 10^5} = 558.75\text{ m/s} \approx 558.8\text{ m/s}$$

**Step 2: Terminal translational temperature $T_\infty$**
From the isentropic temperature relation:
$$\frac{T_\infty}{T_0} = \frac{1}{1 + \frac{\gamma - 1}{2} M_\infty^2}$$
For $\gamma = 5/3$: $\frac{\gamma - 1}{2} = \frac{1}{3} \approx 0.33333$.
Given $M_\infty = 28.50$:
$$M_\infty^2 = (28.50)^2 = 812.25$$
$$\frac{\gamma - 1}{2} M_\infty^2 = \frac{812.25}{3} = 270.75$$
$$1 + \frac{\gamma - 1}{2} M_\infty^2 = 271.75$$
$$T_\infty = \frac{T_0}{271.75} = \frac{300.0\text{ K}}{271.75} = 1.10395\text{ K} \approx 1.10\text{ K}$$
The expansion has cooled the moving gas from room temperature down to **$1.10\text{ Kelvin}$**!

**Step 3: Speed ratio and fractional velocity spread**
The most probable thermal speed in the moving frame is:
$$\alpha_{\text{thermal}} = \sqrt{\frac{2 R T_\infty}{M}} = \sqrt{\frac{2 \times 8.314462 \times 1.10395}{0.039948}} = \sqrt{\frac{18.358}{0.039948}} = \sqrt{459.55} = 21.437\text{ m/s}$$
The speed ratio is:
$$S = \frac{u_\infty}{\alpha_{\text{thermal}}} = \frac{558.75\text{ m/s}}{21.437\text{ m/s}} = 26.06$$
Note that for an ideal gas, $S = \sqrt{\frac{\gamma}{2}} M_\infty = \sqrt{\frac{5}{6}} \times 28.50 = 0.91287 \times 28.50 = 26.02$.

Fractional velocity spread ($\text{FWHM}$ of thermal Gaussian distribution):
$$\Delta v_{\text{FWHM}} = 2 \sqrt{\ln 2} \cdot \alpha_{\text{thermal}} = 2 \times 0.83255 \times 21.437 = 35.69\text{ m/s}$$
Fractional spread:
$$\frac{\Delta v_{\text{FWHM}}}{u_\infty} = \frac{35.69\text{ m/s}}{558.75\text{ m/s}} = 0.06387 \approx 6.4\%$$
The beam travels with extreme monochromatic velocity purity."""
        },

        "unit-2": {
            "id": "p2-9",
            "title": "Fuoss-Onsager Conductance Equation & Bjerrum Ion-Pair Association Constant",
            "difficulty": "Hard",
            "statement": r"""In a non-aqueous electrolyte solution of lithium perchlorate ($LiClO_4$, 1:1 electrolyte) in tetrahydrofuran (THF, relative permittivity $\varepsilon_r = 7.58$, dynamic viscosity $\eta = 0.460\text{ mPa}\cdot\text{s}$ at $T = 298.15\text{ K}$), strong electrostatic ion pairing occurs:
$$Li^+ + ClO_4^- \underset{K_d}{\overset{K_A}{\rightleftharpoons}} [Li^+\cdot ClO_4^-]^0$$
Conductivity measurements at low concentrations yield:
- Limiting molar conductivity: $\Lambda_0 = 105.0\text{ S}\cdot\text{cm}^2/\text{mol} = 1.050 \times 10^{-2}\text{ S}\cdot\text{m}^2/\text{mol}$
- At concentration $C = 1.00 \times 10^{-3}\text{ M}$ ($1.00\text{ mol/m}^3$), the measured molar conductivity is $\Lambda = 26.25\text{ S}\cdot\text{cm}^2/\text{mol}$.

(a) Using the Bjerrum electrostatic ion-pairing theory, calculate the Bjerrum critical distance $q_B = \frac{e^2}{8 \pi \varepsilon_r \varepsilon_0 k_B T}$ in Ångströms for THF at $298.15\text{ K}$, and compare it with the Bjerrum distance in water ($\varepsilon_r = 78.36$).
(b) Using the Shedlovsky-Fuoss approximation $\alpha \approx \frac{\Lambda}{\Lambda_0} S(z)$ (where $S(z) \approx 1.00$ at this concentration), calculate the degree of dissociation $\alpha$ of the salt.
(c) Calculate the thermodynamic association equilibrium constant $K_A = \frac{1 - \alpha}{\alpha^2 C \gamma_\pm^2}$ assuming the mean ionic activity coefficient is $\gamma_\pm = 0.820$.""",
            "solution": r"""**Step 1: Calculate Bjerrum critical distance $q_B$**
The Bjerrum distance is the distance at which Coulombic attraction energy between opposing monovalent charges equals $2 k_B T$:
$$q_B = \frac{e^2}{8 \pi \varepsilon_r \varepsilon_0 k_B T}$$
Fundamental constants:
$$e^2 / (4 \pi \varepsilon_0) = 2.30708 \times 10^{-28}\text{ J}\cdot\text{m}$$
$$k_B T = (1.380649 \times 10^{-23}) \times 298.15 = 4.1164 \times 10^{-21}\text{ J}$$
$$\frac{e^2}{4 \pi \varepsilon_0 k_B T} = \frac{2.30708 \times 10^{-28}}{4.1164 \times 10^{-21}} = 5.6046 \times 10^{-8}\text{ m} = 560.46\text{ Å}$$

Therefore:
$$q_B = \frac{1}{2 \varepsilon_r} \left( \frac{e^2}{4 \pi \varepsilon_0 k_B T} \right) = \frac{560.46\text{ Å}}{2 \varepsilon_r} = \frac{280.23\text{ Å}}{\varepsilon_r}$$

- In Water ($\varepsilon_r = 78.36$):
  $$q_{B, \text{H}_2\text{O}} = \frac{280.23}{78.36} = 3.576\text{ Å}$$
  Because $3.58\text{ Å}$ is comparable to crystallographic ion contact radii, 1:1 salts rarely form ion pairs in water.

- In THF ($\varepsilon_r = 7.58$):
  $$q_{B, \text{THF}} = \frac{280.23}{7.58} = 36.97\text{ Å}$$
  In low-dielectric THF, ions attract each other across an enormous distance of **$37\text{ Å}$**, driving near-total ion pairing!

**Step 2: Degree of dissociation $\alpha$**
Using the conductivity ratio:
$$\alpha \approx \frac{\Lambda}{\Lambda_0} = \frac{26.25\text{ S}\cdot\text{cm}^2/\text{mol}}{105.0\text{ S}\cdot\text{cm}^2/\text{mol}} = 0.2500 = 25.0\%$$
Three quarters ($75\%$) of the salt exists as neutral $[Li^+\cdot ClO_4^-]^0$ ion pairs!

**Step 3: Calculate association equilibrium constant $K_A$**
The equilibrium for association is:
$$K_A = \frac{[Li^+\cdot ClO_4^-]}{[Li^+][ClO_4^-] \gamma_\pm^2} = \frac{C (1 - \alpha)}{(\alpha C)^2 \gamma_\pm^2} = \frac{1 - \alpha}{\alpha^2 C \gamma_\pm^2}$$
Given:
$$1 - \alpha = 1 - 0.2500 = 0.7500$$
$$\alpha^2 = (0.2500)^2 = 0.0625$$
$$C = 1.00 \times 10^{-3}\text{ M}$$
$$\gamma_\pm = 0.820 \implies \gamma_\pm^2 = (0.820)^2 = 0.6724$$

Denominator:
$$\alpha^2 C \gamma_\pm^2 = 0.0625 \times (1.00 \times 10^{-3}) \times 0.6724 = 4.2025 \times 10^{-5}\text{ M}$$

$$K_A = \frac{0.7500}{4.2025 \times 10^{-5}\text{ M}} = 1.7846 \times 10^4\text{ M}^{-1} \approx 1.78 \times 10^4\text{ M}^{-1}$$
The massive association constant confirms powerful electrostatic ion pairing in ethereal solvents."""
        },

        "unit-3": {
            "id": "p3-9",
            "title": "Dynamic Light Scattering Siegert Inversion & Gold Nanoparticle Polydispersity",
            "difficulty": "Hard",
            "statement": r"""A Dynamic Light Scattering (DLS) measurement is performed on a colloidal suspension of spherical gold nanoparticles in water ($n = 1.333$, $\eta = 0.890\text{ mPa}\cdot\text{s}$) at $T = 298.15\text{ K}$.
Laser and optics parameters:
- Diode laser wavelength: $\lambda_0 = 632.8\text{ nm}$ ($6.328 \times 10^{-7}\text{ m}$)
- Scattering angle: $\theta = 90.0^\circ$

The normalized intensity autocorrelation function $g^{(2)}(\tau) - 1 = \beta |g^{(1)}(\tau)|^2$ is analyzed via the second-order cumulant expansion:
$$\ln |g^{(1)}(\tau)| = -\bar{\Gamma} \tau + \frac{\mu_2}{2} \tau^2$$
Experimental polynomial regression yields:
- Mean decay rate: $\bar{\Gamma} = 4.560 \times 10^3\text{ s}^{-1}$
- Second cumulant: $\mu_2 = 1.250 \times 10^6\text{ s}^{-2}$

(a) Calculate the magnitude of the scattering wave vector $q$ in $\text{m}^{-1}$.
(b) Calculate the z-average translational diffusion coefficient $\bar{D} = \bar{\Gamma} / q^2$ in $\text{m}^2/\text{s}$.
(c) Using the Stokes-Einstein equation, calculate the z-average hydrodynamic diameter $d_H = 2 R_h$ in nanometers.
(d) Calculate the polydispersity index $\text{PDI} = \mu_2 / \bar{\Gamma}^2$ and comment on whether the colloidal suspension is considered monodisperse.""",
            "solution": r"""**Step 1: Calculate scattering wave vector $q$**
$$q = \frac{4 \pi n}{\lambda_0} \sin\left(\frac{\theta}{2}\right)$$
For $\theta = 90.0^\circ$: $\theta / 2 = 45.0^\circ$, so $\sin(45^\circ) = \frac{\sqrt{2}}{2} = 0.707107$.
$$q = \frac{4 \pi \times 1.333}{6.328 \times 10^{-7}\text{ m}} \times 0.707107 = \frac{16.751}{6.328 \times 10^{-7}} \times 0.707107 = (2.6471 \times 10^7) \times 0.707107 = 1.8718 \times 10^7\text{ m}^{-1}$$
Square of wave vector:
$$q^2 = (1.8718 \times 10^7\text{ m}^{-1})^2 = 3.5036 \times 10^{14}\text{ m}^{-2}$$

**Step 2: Calculate z-average diffusion coefficient $\bar{D}$**
$$\bar{D} = \frac{\bar{\Gamma}}{q^2} = \frac{4.560 \times 10^3\text{ s}^{-1}}{3.5036 \times 10^{14}\text{ m}^{-2}} = 1.3015 \times 10^{-11}\text{ m}^2/\text{s} \approx 1.30 \times 10^{-11}\text{ m}^2/\text{s}$$

**Step 3: Calculate z-average hydrodynamic diameter $d_H$**
From the Stokes-Einstein equation:
$$d_H = 2 R_h = \frac{k_B T}{3 \pi \eta \bar{D}}$$
Thermal energy:
$$k_B T = (1.380649 \times 10^{-23}) \times 298.15 = 4.1164 \times 10^{-21}\text{ J}$$
Viscosity term:
$$3 \pi \eta = 3 \pi \times (0.890 \times 10^{-3}\text{ Pa}\cdot\text{s}) = 8.38805 \times 10^{-3}\text{ Pa}\cdot\text{s}$$
$$3 \pi \eta \bar{D} = (8.38805 \times 10^{-3}) \times (1.3015 \times 10^{-11}) = 1.0917 \times 10^{-13}\text{ N}\cdot\text{s/m}$$
Hydrodynamic diameter:
$$d_H = \frac{4.1164 \times 10^{-21}\text{ J}}{1.0917 \times 10^{-13}\text{ N}\cdot\text{s/m}} = 3.7706 \times 10^{-8}\text{ m} = 37.71\text{ nm}$$
The z-average diameter is **$37.7\text{ nm}$**.

**Step 4: Polydispersity Index ($\text{PDI}$)**
$$\text{PDI} = \frac{\mu_2}{\bar{\Gamma}^2} = \frac{1.250 \times 10^6\text{ s}^{-2}}{(4.560 \times 10^3\text{ s}^{-1})^2} = \frac{1.250 \times 10^6}{2.07936 \times 10^7} = 0.0601 \approx 0.060$$
In colloid and nanoparticle metrology:
- $\text{PDI} < 0.08$: highly monodisperse standard
- $0.08 < \text{PDI} < 0.20$: narrow distribution
- $\text{PDI} > 0.40$: broad polydisperse distribution
With $\text{PDI} = 0.060$, the colloidal gold sample is **exceptionally monodisperse**."""
        },

        "unit-4": {
            "id": "p4-9",
            "title": "Gas-Phase Nitric Oxide Oxidation: Ter-Molecular vs Pre-Equilibrium Dimer Kinetics",
            "difficulty": "Hard",
            "statement": r"""The homogeneous gas-phase oxidation of nitric oxide:
$$2 NO(g) + O_2(g) \longrightarrow 2 NO_2(g)$$
exhibits an overall third-order rate law $r = k_{\text{exp}} [NO]^2 [O_2]$ and a rare **negative apparent activation energy**:
- At $T_1 = 300.0\text{ K}$, $k_{\text{exp}, 1} = 7.10 \times 10^3\text{ M}^{-2}\text{s}^{-1}$.
- At $T_2 = 600.0\text{ K}$, $k_{\text{exp}, 2} = 2.85 \times 10^3\text{ M}^{-2}\text{s}^{-1}$.

Two competing mechanisms have been proposed:
1. **Mechanism I (Dimer Pre-Equilibrium)**:
   $$2 NO \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} N_2O_2 \quad (\text{rapid pre-equilibrium, } K_1 = k_1 / k_{-1})$$
   $$N_2O_2 + O_2 \xrightarrow{k_2} 2 NO_2 \quad (\text{slow, rate-determining})$$
2. **Mechanism II (Collision Complex)**:
   $$NO + O_2 \underset{k_{-3}}{\overset{k_3}{\rightleftharpoons}} NO_3^* \quad (\text{fast})$$
   $$NO_3^* + NO \xrightarrow{k_4} 2 NO_2 \quad (\text{slow})$$

(a) Show that Mechanism I yields the experimental rate law under pre-equilibrium conditions, and express $k_{\text{exp}}$ in terms of $K_1$ and $k_2$.
(b) Derive the relationship connecting the experimental activation energy $E_{a, \text{exp}}$ to the standard enthalpy of dimerization $\Delta H_{\text{dim}}^\circ$ and the elementary barrier $E_{a, 2}$.
(c) Calculate the experimental activation energy $E_{a, \text{exp}}$ in $\text{kJ/mol}$.
(d) If the elementary bimolecular step has an activation energy of $E_{a, 2} = +8.50\text{ kJ/mol}$, calculate the dimerization enthalpy $\Delta H_{\text{dim}}^\circ$ of $2 NO \rightleftharpoons N_2O_2$.""",
            "solution": r"""**Step 1: Mechanism I rate law derivation**
From the rate-determining step:
$$r = \frac{1}{2} \frac{d[NO_2]}{dt} = k_2 [N_2O_2] [O_2]$$
From the rapid pre-equilibrium step:
$$K_1 = \frac{[N_2O_2]}{[NO]^2} \implies [N_2O_2] = K_1 [NO]^2$$
Substitute $[N_2O_2]$ into the rate equation:
$$r = k_2 K_1 [NO]^2 [O_2] = k_{\text{exp}} [NO]^2 [O_2]$$
where $k_{\text{exp}} = k_2 K_1$. This matches the experimental third-order rate law.

**Step 2: Temperature dependence and apparent activation energy**
Differentiating with respect to temperature:
$$\ln k_{\text{exp}} = \ln k_2 + \ln K_1$$
$$\frac{d \ln k_{\text{exp}}}{dT} = \frac{d \ln k_2}{dT} + \frac{d \ln K_1}{dT}$$
Using Arrhenius equation for $k_2$ and van 't Hoff equation for $K_1$:
$$\frac{E_{a, \text{exp}}}{R T^2} = \frac{E_{a, 2}}{R T^2} + \frac{\Delta H_{\text{dim}}^\circ}{R T^2}$$
Multiplying by $R T^2$:
$$E_{a, \text{exp}} = E_{a, 2} + \Delta H_{\text{dim}}^\circ$$
Because dimerization is an exothermic bond-forming reaction ($\Delta H_{\text{dim}}^\circ < 0$), if $|\Delta H_{\text{dim}}^\circ| > E_{a, 2}$, the composite activation energy $E_{a, \text{exp}}$ is **strictly negative**!

**Step 3: Calculate $E_{a, \text{exp}}$ from two-point data**
$$\ln\left(\frac{k_2}{k_1}\right) = -\frac{E_{a, \text{exp}}}{R} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$
Evaluate terms:
$$\ln\left(\frac{2.85 \times 10^3}{7.10 \times 10^3}\right) = \ln(0.40141) = -0.91278$$
$$\frac{1}{T_2} - \frac{1}{T_1} = \frac{1}{600.0} - \frac{1}{300.0} = 1.6667 \times 10^{-3} - 3.3333 \times 10^{-3} = -1.6667 \times 10^{-3}\text{ K}^{-1}$$
$$E_{a, \text{exp}} = -\frac{-0.91278 \times 8.314462\text{ J}/(\text{mol}\cdot\text{K})}{-1.6667 \times 10^{-3}\text{ K}^{-1}} = -\frac{7.5893}{1.6667 \times 10^{-3}} = -4553.6\text{ J/mol} = -4.55\text{ kJ/mol}$$
The negative activation energy ($-4.55\text{ kJ/mol}$) explains why heating slows down the reaction.

**Step 4: Calculate dimerization enthalpy $\Delta H_{\text{dim}}^\circ$**
From $E_{a, \text{exp}} = E_{a, 2} + \Delta H_{\text{dim}}^\circ$:
$$\Delta H_{\text{dim}}^\circ = E_{a, \text{exp}} - E_{a, 2} = -4.55\text{ kJ/mol} - (+8.50\text{ kJ/mol}) = -13.05\text{ kJ/mol}$$
The dimerization of $NO$ into weakly bound dinitrogen dioxide ($N_2O_2$) is exothermic by **$-13.1\text{ kJ/mol}$**."""
        },

        "unit-5": {
            "id": "p5-9",
            "title": "Exner Statistical Validation of Isokinetic Temperature vs Compensation Artifact",
            "difficulty": "Hard",
            "statement": r"""A series of five meta- and para-substituted ethyl benzoates ($X\text{-C}_6H_4\text{COOEt}$) are saponified in $85\%$ aqueous ethanol:
$$X\text{-C}_6H_4\text{COOEt} + OH^- \longrightarrow X\text{-C}_6H_4\text{COO}^- + EtOH$$
Second-order rate constants are measured at $T_1 = 298.15\text{ K}$ and $T_2 = 323.15\text{ K}$:
- Substituent 1 ($p-NO_2$): $k(T_1) = 0.1150\text{ M}^{-1}\text{s}^{-1}$, $k(T_2) = 0.8250\text{ M}^{-1}\text{s}^{-1}$
- Substituent 2 ($m-Cl$): $k(T_1) = 0.0245\text{ M}^{-1}\text{s}^{-1}$, $k(T_2) = 0.1980\text{ M}^{-1}\text{s}^{-1}$
- Substituent 3 ($H$): $k(T_1) = 0.00550\text{ M}^{-1}\text{s}^{-1}$, $k(T_2) = 0.0495\text{ M}^{-1}\text{s}^{-1}$
- Substituent 4 ($p-CH_3$): $k(T_1) = 0.00220\text{ M}^{-1}\text{s}^{-1}$, $k(T_2) = 0.0215\text{ M}^{-1}\text{s}^{-1}$
- Substituent 5 ($p-OCH_3$): $k(T_1) = 0.00110\text{ M}^{-1}\text{s}^{-1}$, $k(T_2) = 0.0118\text{ M}^{-1}\text{s}^{-1}$

(a) Construct an Eyring activation plot ($\Delta H^\ddagger$ vs $\Delta S^\ddagger$) for Substituents 1 and 5 to determine the apparent compensation slope $\beta_{\text{app}}$.
(b) Perform an Exner regression $\ln k(T_2) = a + b \ln k(T_1)$ using Substituents 1 and 5.
(c) Using Exner's formula $\beta = T_1 T_2 \frac{b - 1}{b T_1 - T_2}$, calculate the true isokinetic temperature $\beta$.
(d) State whether this series exhibits a genuine isokinetic relationship or an experimental error artifact.""",
            "solution": r"""**Step 1: Calculate Eyring parameters for Substituents 1 and 5**
Eyring equation: $k = \frac{k_B T}{h} \exp(-\Delta H^\ddagger / R T) \exp(\Delta S^\ddagger / R)$.
Taking two-point differences:
$$\Delta H^\ddagger = R \frac{T_1 T_2}{T_2 - T_1} \ln\left( \frac{k_2 T_1}{k_1 T_2} \right)$$
Here $T_1 = 298.15\text{ K}$, $T_2 = 323.15\text{ K}$, $T_2 - T_1 = 25.0\text{ K}$.
$$\frac{T_1 T_2}{T_2 - T_1} = \frac{298.15 \times 323.15}{25.0} = 3853.9\text{ K}$$
$$R \times 3853.9 = 32043.1\text{ J/mol} = 32.043\text{ kJ/mol}$$
$$\frac{T_1}{T_2} = \frac{298.15}{323.15} = 0.922637$$

- For Substituent 1 ($p-NO_2$):
  $$\frac{k_2 T_1}{k_1 T_2} = \frac{0.8250}{0.1150} \times 0.922637 = 7.1739 \times 0.922637 = 6.6189$$
  $$\ln(6.6189) = 1.8899$$
  $$\Delta H_1^\ddagger = (32.043\text{ kJ/mol}) \times 1.8899 = 60.558\text{ kJ/mol}$$
  $$\Delta S_1^\ddagger = \frac{\Delta H_1^\ddagger - R T_1 \ln\left( \frac{k_1 h}{k_B T_1} \right)}{T_1} = \frac{60558 - 78440}{298.15} = -59.98\text{ J}/(\text{mol}\cdot\text{K})$$

- For Substituent 5 ($p-OCH_3$):
  $$\frac{k_2 T_1}{k_1 T_2} = \frac{0.0118}{0.00110} \times 0.922637 = 10.727 \times 0.922637 = 9.8974$$
  $$\ln(9.8974) = 2.2922$$
  $$\Delta H_5^\ddagger = (32.043\text{ kJ/mol}) \times 2.2922 = 73.449\text{ kJ/mol}$$
  $$\Delta S_5^\ddagger = \frac{73449 - 89960}{298.15} = -55.38\text{ J}/(\text{mol}\cdot\text{K})$$

Apparent compensation slope:
$$\beta_{\text{app}} = \frac{\Delta H_5^\ddagger - \Delta H_1^\ddagger}{\Delta S_5^\ddagger - \Delta S_1^\ddagger} = \frac{73449 - 60558}{-55.38 - (-59.98)} = \frac{12891}{4.60} = 2802\text{ K}$$

**Step 2: Exner linear regression between $T_2$ and $T_1$**
$$x = \ln k(T_1), \quad y = \ln k(T_2)$$
- Sub 1: $x_1 = \ln(0.1150) = -2.1628$, $y_1 = \ln(0.8250) = -0.1924$
- Sub 5: $x_5 = \ln(0.00110) = -6.8124$, $y_5 = \ln(0.0118) = -4.4397$

Exner slope $b$:
$$b = \frac{y_1 - y_5}{x_1 - x_5} = \frac{-0.1924 - (-4.4397)}{-2.1628 - (-6.8124)} = \frac{4.2473}{4.6496} = 0.91348$$

**Step 3: Exner Isokinetic Temperature $\beta$**
$$T_1 T_2 = 298.15 \times 323.15 = 96347.17\text{ K}^2$$
$$b - 1 = 0.91348 - 1 = -0.08652$$
Numerator:
$$T_1 T_2 (b - 1) = 96347.17 \times (-0.08652) = -8335.96\text{ K}^2$$
Denominator:
$$b T_1 - T_2 = (0.91348 \times 298.15) - 323.15 = 272.35 - 323.15 = -50.80\text{ K}$$

$$\beta = \frac{-8335.96\text{ K}^2}{-50.80\text{ K}} = 164.09\text{ K} \approx 164\text{ K}$$

**Step 4: Mechanical Interpretation**
The true isokinetic temperature is $\beta = 164\text{ K}$, which lies well below the experimental operating temperature ($298 - 323\text{ K}$).
Because $b = 0.913 \approx T_1 / T_2 = 0.923$, the substituent variations alter activation enthalpy while leaving activation entropy virtually constant ($\Delta S^\ddagger \approx -58\text{ J}/(\text{mol}\cdot\text{K})$). The apparent high compensation temperature ($\beta_{\text{app}} = 2802\text{ K}$) was an experimental artifact of correlated slope-intercept errors."""
        },

        "unit-6": {
            "id": "p6-9",
            "title": "Bell-Evans-Polanyi Tunneling Correction in Multi-Coordinate Hydride Transfer",
            "difficulty": "Hard",
            "statement": r"""In the catalytic cycle of soybean lipoxygenase (SLO-1), a non-heme iron(III)-hydroxide cofactor ($Fe^{III}-OH$) abstracts a hydrogen atom from the C-11 methylene carbon of linoleic acid:
$$\text{R-CH}_2\text{-R}' + Fe^{III}-OH \longrightarrow \text{R-C}^\bullet\text{H-R}' + Fe^{II}-OH_2$$
The enzymatic reaction exhibits one of the largest known kinetic isotope effects: $\text{KIE} = k_H / k_D \approx 80.0$ at $T = 298.15\text{ K}$ with negligible temperature dependence ($E_{a, D} - E_{a, H} \approx 4.0\text{ kJ/mol}$).
Using the Bell 1D parabolic tunneling model, the quantum transmission coefficient $\kappa(T)$ is:
$$\kappa(T) = \frac{u/2}{\sin(u/2)} \quad \text{where } u = \frac{h \nu^\ddagger}{k_B T}$$
where $\nu^\ddagger$ is the imaginary frequency of the reaction coordinate at the top of the barrier ($V(x) = V_0 - \frac{1}{2} m (2 \pi \nu^\ddagger)^2 x^2$).

(a) If the imaginary barrier frequency for protium transfer is $\nu_H^\ddagger = 1200\text{ cm}^{-1}$ ($3.598 \times 10^{13}\text{ s}^{-1}$): calculate $u_H$ at $T = 298.15\text{ K}$ and the Bell transmission factor $\kappa_H$.
(b) Assuming mass scaling for the reaction coordinate $\nu_D^\ddagger = \nu_H^\ddagger / \sqrt{2} = 848.5\text{ cm}^{-1}$: calculate $u_D$ and the deuterium transmission factor $\kappa_D$.
(c) Calculate the tunneling-induced KIE factor $\kappa_H / \kappa_D$.
(d) If the semiclassical (zero-point energy) KIE without tunneling is $(\text{KIE})_{\text{sc}} = 6.20$, calculate the total predicted kinetic isotope effect $\text{KIE}_{\text{tot}} = (\text{KIE})_{\text{sc}} \times (\kappa_H / \kappa_D)$ and compare it with the experimental value of $80.0$.""",
            "solution": r"""**Step 1: Calculate $u_H$ and Bell factor $\kappa_H$ for protium**
Imaginary frequency:
$$\nu_H^\ddagger = c \tilde{\nu}_H^\ddagger = (2.99792 \times 10^{10}\text{ cm/s}) \times (1200\text{ cm}^{-1}) = 3.5975 \times 10^{13}\text{ s}^{-1}$$
Planck and Boltzmann factor:
$$\frac{h}{k_B T} = \frac{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}}{(1.380649 \times 10^{-23}\text{ J/K}) \times (298.15\text{ K})} = \frac{6.62607 \times 10^{-34}}{4.1164 \times 10^{-21}} = 1.60968 \times 10^{-13}\text{ s}$$
Dimensionless frequency parameter:
$$u_H = \frac{h \nu_H^\ddagger}{k_B T} = (1.60968 \times 10^{-13}\text{ s}) \times (3.5975 \times 10^{13}\text{ s}^{-1}) = 5.7908\text{ rad}$$
Half-angle:
$$\frac{u_H}{2} = \frac{5.7908}{2} = 2.8954\text{ rad}$$
$$\sin(u_H / 2) = \sin(2.8954\text{ rad}) = \sin(165.90^\circ) = 0.2436$$

Bell transmission factor:
$$\kappa_H = \frac{u_H / 2}{\sin(u_H / 2)} = \frac{2.8954}{0.2436} = 11.886 \approx 11.89$$
Tunneling enhances protium transfer by a factor of **$11.9$**!

**Step 2: Calculate $u_D$ and Bell factor $\kappa_D$ for deuterium**
$$\nu_D^\ddagger = \frac{\nu_H^\ddagger}{\sqrt{2}} = \frac{3.5975 \times 10^{13}}{1.41421} = 2.5438 \times 10^{13}\text{ s}^{-1}$$
$$u_D = \frac{u_H}{\sqrt{2}} = \frac{5.7908}{1.41421} = 4.0947\text{ rad}$$
Half-angle:
$$\frac{u_D}{2} = \frac{4.0947}{2} = 2.0474\text{ rad}$$
$$\sin(u_D / 2) = \sin(2.0474\text{ rad}) = \sin(117.31^\circ) = 0.8885$$

Bell transmission factor:
$$\kappa_D = \frac{u_D / 2}{\sin(u_D / 2)} = \frac{2.0474}{0.8885} = 2.3043 \approx 2.30$$

**Step 3: Tunneling-induced KIE enhancement**
$$\frac{\kappa_H}{\kappa_D} = \frac{11.886}{2.3043} = 5.158 \approx 5.16$$

**Step 4: Total predicted kinetic isotope effect**
$$\text{KIE}_{\text{tot}} = (\text{KIE})_{\text{sc}} \times \left( \frac{\kappa_H}{\kappa_D} \right) = 6.20 \times 5.158 = 31.98 \approx 32.0$$
While the 1D Bell model captures a substantial increase from $6.2$ to $32.0$, the experimental value of $80.0$ requires a full multi-dimensional Marcus-like **environmentally coupled hydrogen wavepacket tunneling** model incorporating active-site protein conformational gating."""
        },

        "unit-7": {
            "id": "p7-9",
            "title": "FCS Confocal Autocorrelation & Dynamic Two-State Protein Folding Kinetics",
            "difficulty": "Hard",
            "statement": r"""A single-molecule Fluorescence Correlation Spectroscopy (FCS) experiment investigates the rapid microsecond folding and unfolding kinetics of a fluorescently labeled miniprotein:
$$Native (N) \underset{k_u}{\overset{k_f}{\rightleftharpoons}} Unfolded (U)$$
where the native state has high fluorescence brightness ($q_N$) and the unfolded state is quenched by an intramolecular tryptophan ($q_U \approx 0$).
The confocal observation volume is calibrated using Rhodamine 6G ($D_{\text{Rh6G}} = 4.00 \times 10^{-10}\text{ m}^2/\text{s}$, transit time $\tau_{D, \text{Rh6G}} = 125.0\;\mu\text{s}$) with lateral beam radius $w_{xy} = 0.250\;\mu\text{m}$.
The measured normalized temporal autocorrelation function of the protein solution at $T = 298.15\text{ K}$ is:
$$G(\tau) = G(0) \left( 1 + \frac{\tau}{\tau_D} \right)^{-1} \left( 1 + \frac{\tau}{S^2 \tau_D} \right)^{-1/2} \left[ 1 + A_{\text{relax}} \exp\left(-\frac{\tau}{\tau_{\text{relax}}}\right) \right]$$
where the structure factor is $S = w_z / w_{xy} = 5.00$.
Non-linear least-squares fitting of $G(\tau)$ yields:
- Amplitude at zero lag: $G(0) = 0.0800$
- Translational diffusion time: $\tau_D = 350.0\;\mu\text{s}$ ($3.50 \times 10^{-4}\text{ s}$)
- Chemical relaxation amplitude: $A_{\text{relax}} = 0.350$
- Chemical relaxation time: $\tau_{\text{relax}} = 28.50\;\mu\text{s}$ ($2.85 \times 10^{-5}\text{ s}$)

(a) Calculate the average number of protein molecules $\langle N \rangle$ present in the confocal laser focal volume.
(b) Calculate the protein translational diffusion coefficient $D_{\text{protein}}$ in $\text{m}^2/\text{s}$.
(c) The relaxation amplitude is $A_{\text{relax}} = \frac{K_{\text{eq}}}{(1 + K_{\text{eq}})^2} \frac{(q_N - q_U)^2}{q_{\text{avg}}^2}$. For a dark unfolded state ($q_U = 0$), $A_{\text{relax}} = K_{\text{eq}} = [U]_{\text{eq}} / [N]_{\text{eq}} = 0.350$. Calculate the equilibrium fraction of unfolded protein $f_U$.
(d) Using $\frac{1}{\tau_{\text{relax}}} = k_f + k_u$ and $K_{\text{eq}} = k_u / k_f$, calculate the elementary folding rate constant $k_f$ and unfolding rate constant $k_u$ in $\text{s}^{-1}$.""",
            "solution": r"""**Step 1: Calculate average number of molecules $\langle N \rangle$**
From the FCS amplitude at zero correlation delay:
$$G(0) = \frac{1}{\langle N \rangle} \implies \langle N \rangle = \frac{1}{G(0)} = \frac{1}{0.0800} = 12.50\text{ molecules}$$
On average, exactly **$12.5$ molecules** occupy the femtoliter detection volume.

**Step 2: Calculate protein diffusion coefficient $D_{\text{protein}}$**
The lateral beam radius is $w_{xy} = 0.250\;\mu\text{m} = 2.50 \times 10^{-7}\text{ m}$.
The characteristic diffusion transit time is:
$$\tau_D = \frac{w_{xy}^2}{4 D} \implies D = \frac{w_{xy}^2}{4 \tau_D}$$
$$w_{xy}^2 = (2.50 \times 10^{-7}\text{ m})^2 = 6.25 \times 10^{-14}\text{ m}^2$$
$$4 \tau_D = 4 \times (3.50 \times 10^{-4}\text{ s}) = 1.40 \times 10^{-3}\text{ s}$$
$$D_{\text{protein}} = \frac{6.25 \times 10^{-14}\text{ m}^2}{1.40 \times 10^{-3}\text{ s}} = 4.464 \times 10^{-11}\text{ m}^2/\text{s} \approx 4.46 \times 10^{-11}\text{ m}^2/\text{s}$$

**Step 3: Calculate equilibrium fraction of unfolded protein $f_U$**
Given $K_{\text{eq}} = \frac{[U]_{\text{eq}}}{[N]_{\text{eq}}} = 0.350$:
$$f_U = \frac{[U]_{\text{eq}}}{[N]_{\text{eq}} + [U]_{\text{eq}}} = \frac{K_{\text{eq}}}{1 + K_{\text{eq}}} = \frac{0.350}{1 + 0.350} = \frac{0.350}{1.350} = 0.2593 \approx 25.9\%$$
At equilibrium, $74.1\%$ of the protein is folded in native conformation.

**Step 4: Calculate elementary rate constants $k_f$ and $k_u$**
The chemical relaxation rate is:
$$\frac{1}{\tau_{\text{relax}}} = k_f + k_u = \frac{1}{2.85 \times 10^{-5}\text{ s}} = 3.5088 \times 10^4\text{ s}^{-1}$$
From the equilibrium constant:
$$k_u = K_{\text{eq}} \cdot k_f = 0.350 \cdot k_f$$
Substitute into relaxation sum:
$$k_f + 0.350 k_f = 1.350 k_f = 3.5088 \times 10^4\text{ s}^{-1}$$
$$k_f = \frac{3.5088 \times 10^4\text{ s}^{-1}}{1.350} = 2.5991 \times 10^4\text{ s}^{-1} \approx 2.60 \times 10^4\text{ s}^{-1}$$
Unfolding rate constant:
$$k_u = 0.350 \times (2.5991 \times 10^4) = 9.097 \times 10^3\text{ s}^{-1} \approx 9.10 \times 10^3\text{ s}^{-1}$$
FCS directly clocks single-molecule protein folding with a folding time of $\tau_{\text{fold}} = 1/k_f = 38.5\;\mu\text{s}$!"""
        },

        "unit-8": {
            "id": "p8-9",
            "title": "Laminar Flame Propagation Speed & Mallard-Le Chatelier Thermal Zone Derivation",
            "difficulty": "Hard",
            "statement": r"""The laminar flame propagation speed $S_L$ of a stoichiometric methane-air premixed mixture ($CH_4 + 2 O_2 + 7.52 N_2$) is modeled using the classical Mallard-Le Chatelier thermal combustion theory.
Thermophysical parameters of the unburned gas mixture at $T_u = 300.0\text{ K}$ and $P = 1.00\text{ atm}$:
- Unburned gas density: $\rho_u = 1.130\text{ kg/m}^3$
- Specific heat capacity: $c_p = 1080.0\text{ J}/(\text{kg}\cdot\text{K})$
- Thermal conductivity at mean flame temperature: $\kappa = 0.0850\text{ W}/(\text{m}\cdot\text{K})$
- Adiabatic flame temperature: $T_b = 2220.0\text{ K}$
- Ignition threshold temperature: $T_i = 1200.0\text{ K}$
- Mean chemical volumetric reaction rate in the reaction zone: $\dot{\omega} = 1.250 \times 10^3\text{ kg}/(\text{m}^3\cdot\text{s})$

According to the Mallard-Le Chatelier energy balance between conductive heat preheating from the flame front and chemical heat release in the reaction zone:
$$S_L = \sqrt{\frac{\kappa}{\rho_u c_p} \frac{\dot{\omega}}{\rho_u} \left( \frac{T_b - T_i}{T_i - T_u} \right)}$$
and the preheat zone thickness is given by:
$$\delta_{\text{ph}} = \frac{\kappa}{\rho_u c_p S_L}$$

(a) Calculate thermal diffusivity $\alpha = \frac{\kappa}{\rho_u c_p}$ of the gas mixture in $\text{m}^2/\text{s}$.
(b) Calculate the dimensionless thermal driving factor $\theta_{\text{comb}} = \frac{T_b - T_i}{T_i - T_u}$.
(c) Calculate the laminar burning velocity $S_L$ in $\text{m/s}$ and $\text{cm/s}$.
(d) Calculate the preheat thermal zone thickness $\delta_{\text{ph}}$ in millimeters.""",
            "solution": r"""**Step 1: Calculate thermal diffusivity $\alpha$**
$$\rho_u c_p = (1.130\text{ kg/m}^3) \times (1080.0\text{ J}/(\text{kg}\cdot\text{K})) = 1220.4\text{ J}/(\text{m}^3\cdot\text{K})$$
$$\alpha = \frac{\kappa}{\rho_u c_p} = \frac{0.0850\text{ W}/(\text{m}\cdot\text{K})}{1220.4\text{ J}/(\text{m}^3\cdot\text{K})} = 6.9649 \times 10^{-5}\text{ m}^2/\text{s}$$

**Step 2: Calculate dimensionless thermal driving factor $\theta_{\text{comb}}$**
$$\Delta T_{\text{chem}} = T_b - T_i = 2220.0 - 1200.0 = 1020.0\text{ K}$$
$$\Delta T_{\text{preheat}} = T_i - T_u = 1200.0 - 300.0 = 900.0\text{ K}$$
$$\theta_{\text{comb}} = \frac{1020.0\text{ K}}{900.0\text{ K}} = 1.1333$$

**Step 3: Calculate laminar burning velocity $S_L$**
Chemical reaction rate term:
$$\frac{\dot{\omega}}{\rho_u} = \frac{1.250 \times 10^3\text{ kg}/(\text{m}^3\cdot\text{s})}{1.130\text{ kg/m}^3} = 1106.19\text{ s}^{-1}$$

Product inside radical:
$$\mathcal{P} = \alpha \times \left( \frac{\dot{\omega}}{\rho_u} \right) \times \theta_{\text{comb}}$$
$$\mathcal{P} = (6.9649 \times 10^{-5}\text{ m}^2/\text{s}) \times (1106.19\text{ s}^{-1}) \times (1.1333) = (0.077045) \times 1.1333 = 0.087317\text{ m}^2/\text{s}^2$$

Laminar flame speed:
$$S_L = \sqrt{0.087317\text{ m}^2/\text{s}^2} = 0.29549\text{ m/s} = 29.55\text{ cm/s}$$
This closely matches the experimental laminar burning velocity of methane-air flames ($S_{L, \text{exp}} \approx 35 - 40\text{ cm/s}$).

**Step 4: Calculate preheat zone thickness $\delta_{\text{ph}}$**
$$\delta_{\text{ph}} = \frac{\alpha}{S_L} = \frac{6.9649 \times 10^{-5}\text{ m}^2/\text{s}}{0.29549\text{ m/s}} = 2.357 \times 10^{-4}\text{ m} = 0.2357\text{ mm} \approx 0.24\text{ mm}$$
The thermal boundary layer separating room-temperature reactants from the $2220\text{ K}$ flame is only **$0.24\text{ millimeters}$** thick, creating a temperature gradient exceeding **$3.8 \times 10^6\text{ K/m}$**!"""
        },

        "unit-9": {
            "id": "p9-9",
            "title": "Briggs-Rauscher Oscillations: Oregonator Limit Cycle Periodicity",
            "difficulty": "Hard",
            "statement": r"""The Field-Körös-Noyes (FKN) mechanism for Belousov-Zhabotinsky and Briggs-Rauscher chemical oscillators is reduced to the classic three-variable **Oregonator** kinetic model:
1. $A + Y \xrightarrow{k_1} X + P$
2. $X + Y \xrightarrow{k_2} 2 P$
3. $A + X \xrightarrow{k_3} 2 X + 2 Z$
4. $2 X \xrightarrow{k_4} A + P$
5. $B + Z \xrightarrow{k_5} \frac{1}{2} f Y$

where $X = [HBrO_2]$ (bromous acid), $Y = [Br^-]$ (bromide ion inhibitor), $Z = [Ce^{4+}]$ (oxidized catalyst), $A = [BrO_3^-]$ (bromate), and $f$ is the stoichiometric bifurcation factor ($f \approx 1.00$).
In a continuously stirred tank reactor (CSTR) at $T = 298.15\text{ K}$ with constant reactant concentrations $[A] = 0.100\text{ M}$ and $[B] = 0.300\text{ M}$:
Kinetic rate constants:
- $k_1 = 1.34\text{ M}^{-1}\text{s}^{-1}$
- $k_2 = 1.60 \times 10^6\text{ M}^{-1}\text{s}^{-1}$
- $k_3 = 34.0\text{ M}^{-1}\text{s}^{-1}$
- $k_4 = 3.00 \times 10^3\text{ M}^{-1}\text{s}^{-1}$
- $k_5 = 0.400\text{ s}^{-1}$

(a) Calculate the critical inhibitor threshold concentration $[Y]_{\text{crit}} = [Br^-]_{\text{crit}} = \frac{k_3 [A]}{k_2}$ that triggers the autocatalytic explosion of $X$.
(b) When $[Y] < [Y]_{\text{crit}}$, calculate the peak autocatalytic steady-state concentration $X_{\max} \approx \frac{k_3 [A]}{2 k_4}$.
(c) The slow recovery phase of the limit cycle is governed by the reduction of oxidized catalyst $Z$ ($Ce^{4+}$) via Step 5: $\frac{d[Z]}{dt} \approx -k_5 [Z]$. If the catalyst concentration cycles between $Z_{\max} = 1.00 \times 10^{-4}\text{ M}$ and $Z_{\min} = 1.00 \times 10^{-5}\text{ M}$, calculate the relaxation oscillation period $T_{\text{osc}} \approx \frac{1}{k_5} \ln\left(\frac{Z_{\max}}{Z_{\min}}\right)$ in seconds.""",
            "solution": r"""**Step 1: Calculate critical threshold concentration $[Y]_{\text{crit}}$**
In the Oregonator scheme, intermediate $X$ ($HBrO_2$) is destroyed by inhibitor $Y$ ($Br^-$) via Step 2 with rate $k_2 [X][Y]$, and generated autocatalytically via Step 3 with rate $k_3 [A][X]$.
The net balance is:
$$\frac{d[X]}{dt} = k_3 [A][X] - k_2 [X][Y] = [X] (k_3 [A] - k_2 [Y])$$
When $k_2 [Y] > k_3 [A]$, $d[X]/dt < 0$ and autocatalysis is quenched.
When $k_2 [Y] < k_3 [A]$, the system undergoes explosive autocatalytic growth.
The critical bifurcation boundary is:
$$[Y]_{\text{crit}} = \frac{k_3 [A]}{k_2}$$
Substitute values:
$$k_3 [A] = (34.0\text{ M}^{-1}\text{s}^{-1}) \times (0.100\text{ M}) = 3.40\text{ s}^{-1}$$
$$[Y]_{\text{crit}} = \frac{3.40\text{ s}^{-1}}{1.60 \times 10^6\text{ M}^{-1}\text{s}^{-1}} = 2.125 \times 10^{-6}\text{ M} = 2.13\;\mu\text{M}$$
When bromide ion concentration drops below **$2.13\;\mu\text{M}$**, the autocatalytic switch turns ON.

**Step 2: Peak autocatalytic concentration $X_{\max}$**
When $[Y] \ll [Y]_{\text{crit}}$, Step 3 generates $X$ until limited by quadratic disproportionation (Step 4: $2 X \xrightarrow{k_4} A + P$):
$$\frac{d[X]}{dt} \approx k_3 [A][X] - 2 k_4 [X]^2 = 0 \implies [X]_{\max} = \frac{k_3 [A]}{2 k_4}$$
$$[X]_{\max} = \frac{3.40\text{ s}^{-1}}{2 \times (3.00 \times 10^3\text{ M}^{-1}\text{s}^{-1})} = \frac{3.40}{6.00 \times 10^3} = 5.667 \times 10^{-4}\text{ M} \approx 0.567\text{ mM}$$

**Step 3: Calculate oscillation period $T_{\text{osc}}$**
Because the autocatalytic spike (Steps 3 and 4) occurs on a millisecond timescale ($< 50\text{ ms}$), the vast majority of the oscillation period is spent in the slow chemical regeneration of bromide inhibitor by reduction of $Ce^{4+}$:
$$\frac{d[Z]}{dt} = -k_5 [Z] \implies [Z](t) = [Z]_{\max} e^{-k_5 t}$$
The period required to deplete $Z$ from $Z_{\max}$ to $Z_{\min}$ is:
$$t_{\text{slow}} = \frac{1}{k_5} \ln\left(\frac{Z_{\max}}{Z_{\min}}\right)$$
Given $k_5 = 0.400\text{ s}^{-1}$ and $\frac{Z_{\max}}{Z_{\min}} = \frac{1.00 \times 10^{-4}}{1.00 \times 10^{-5}} = 10.0$:
$$\ln(10.0) = 2.30259$$
$$T_{\text{osc}} \approx \frac{2.30259}{0.400\text{ s}^{-1}} = 5.756\text{ s} \approx 5.76\text{ seconds}$$
The chemical solution cycles color (e.g., amber $\leftrightarrow$ deep blue) with a period of **$5.8\text{ seconds}$**."""
        },

        "unit-10": {
            "id": "p10-9",
            "title": "Quasiclassical Trajectory (QCT) State-to-State Opacity & Differential Cross-Section",
            "difficulty": "Hard",
            "statement": r"""A Quasiclassical Trajectory (QCT) numerical simulation is executed on the London-Eyring-Polanyi-Sato (LEPS) potential energy surface for the collinear atom-diatom collision:
$$H + D_2(v=0, j=0) \longrightarrow HD(v', j') + D$$
at fixed collision energy $E_{\text{coll}} = 0.500\text{ eV}$ ($48.24\text{ kJ/mol}$, initial relative velocity $v_{\text{rel}} = 7580\text{ m/s}$).
A Monte Carlo ensemble of $N_{\text{tot}} = 10,000$ trajectories was integrated by sampling impact parameters $b$ uniformly distributed from $b = 0$ to maximum cutoff $b_{\max} = 1.40\text{ Å}$ ($1.40 \times 10^{-10}\text{ m}$).
The numerical opacity function (reaction probability as a function of impact parameter) fits the linear triangular profile:
$$P(b) = P_0 \left( 1 - \frac{b}{b_{\max}} \right) \quad \text{for } b \le b_{\max}$$
with zero-impact-parameter head-on probability $P_0 = P(0) = 0.720$.

(a) Show by integration that the total integral reactive cross-section $\sigma_r$ is given by:
    $$\sigma_r = 2 \pi \int_0^{b_{\max}} P(b) b db = \frac{\pi b_{\max}^2 P_0}{3}$$
(b) Calculate the total reaction cross-section $\sigma_r$ in Ångströms squared ($\text{Å}^2$) and in $\text{m}^2$.
(c) Calculate the bimolecular rate constant $k(E_{\text{coll}}) = v_{\text{rel}} \cdot \sigma_r$ at this monoenergetic collision velocity in $\text{m}^3/\text{s}$ and $\text{M}^{-1}\text{s}^{-1}$.
(d) Explain dynamically why head-on collisions ($b \to 0$) have maximum reaction probability while glancing collisions ($b \to b_{\max}$) fail to react.""",
            "solution": r"""**Step 1: Integration of total reaction cross-section $\sigma_r$**
The classical definition of integral reaction cross-section is:
$$\sigma_r = 2 \pi \int_0^{b_{\max}} P(b) b db$$
Substitute $P(b) = P_0 \left( 1 - \frac{b}{b_{\max}} \right)$:
$$\sigma_r = 2 \pi P_0 \int_0^{b_{\max}} \left( b - \frac{b^2}{b_{\max}} \right) db$$
Evaluate the definite integral:
$$\int_0^{b_{\max}} b db = \left[ \frac{b^2}{2} \right]_0^{b_{\max}} = \frac{b_{\max}^2}{2}$$
$$\int_0^{b_{\max}} \frac{b^2}{b_{\max}} db = \frac{1}{b_{\max}} \left[ \frac{b^3}{3} \right]_0^{b_{\max}} = \frac{b_{\max}^2}{3}$$
Difference:
$$\frac{b_{\max}^2}{2} - \frac{b_{\max}^2}{3} = \frac{b_{\max}^2}{6}$$
Multiply by $2 \pi P_0$:
$$\sigma_r = 2 \pi P_0 \left( \frac{b_{\max}^2}{6} \right) = \frac{\pi b_{\max}^2 P_0}{3}$$

**Step 2: Calculate $\sigma_r$ numerically**
Given $b_{\max} = 1.40\text{ Å}$ and $P_0 = 0.720$:
$$b_{\max}^2 = (1.40\text{ Å})^2 = 1.960\text{ Å}^2$$
$$\pi b_{\max}^2 = \pi \times 1.960 = 6.1575\text{ Å}^2$$
$$\sigma_r = \frac{6.1575 \times 0.720}{3} = 1.4778\text{ Å}^2 \approx 1.48\text{ Å}^2$$
In $\text{m}^2$:
$$\sigma_r = 1.4778 \times 10^{-20}\text{ m}^2$$

**Step 3: Calculate monoenergetic rate constant $k(E_{\text{coll}})$**
$$k(E_{\text{coll}}) = v_{\text{rel}} \cdot \sigma_r = (7580\text{ m/s}) \times (1.4778 \times 10^{-20}\text{ m}^2) = 1.1202 \times 10^{-16}\text{ m}^3/\text{s}$$
Convert to chemical molar units ($\text{M}^{-1}\text{s}^{-1} = \text{L}/(\text{mol}\cdot\text{s})$):
$$k = (1.1202 \times 10^{-16}\text{ m}^3/\text{s}) \times (10^3\text{ L/m}^3) \times (6.02214 \times 10^{23}\text{ molecules/mol})$$
$$k = 1.1202 \times 10^{-13} \times 6.02214 \times 10^{23} = 6.746 \times 10^{10}\text{ L}/(\text{mol}\cdot\text{s}) = 6.75 \times 10^{10}\text{ M}^{-1}\text{s}^{-1}$$

**Step 4: Dynamic interpretation of the opacity function**
- In **head-on collisions ($b \to 0$)**, orbital angular momentum $L = \mu v_{\text{rel}} b \to 0$. Nearly $100\%$ of the initial relative translational kinetic energy is directed along the line-of-centers directly into the collinear $H\cdots D-D$ reaction coordinate, efficiently conquering the saddle point barrier ($V^\ddagger \approx 0.42\text{ eV}$).
- In **glancing collisions ($b \to b_{\max}$)**, large orbital angular momentum creates an effective centrifugal potential barrier $V_{\text{cent}}(R) = \frac{L^2}{2 \mu R^2}$. The colliding partners are deflected before reaching the transition state saddle point, causing $P(b)$ to decay linearly to zero."""
        }
    }

    for u in units:
        uid = u["id"]
        if uid in prob9_dict:
            u["problems"].append(prob9_dict[uid])

    return units

if __name__ == "__main__":
    from build_kinetics_units_1_2_3 import get_units_1_2_3
    from build_kinetics_units_4_5_6 import get_units_4_5_6
    from build_kinetics_units_7_8_9_10 import get_units_7_8_9_10
    from expand_kinetics_problem8 import inject_problem_8

    all_u = get_units_1_2_3() + get_units_4_5_6() + get_units_7_8_9_10()
    all_u = inject_problem_8(all_u)
    all_u = inject_problem_9(all_u)
    print("Injected Problem 9 across all units successfully!")
    for u in all_u:
        print(f"  {u['id']}: {len(u['problems'])} problems (latest: {u['problems'][-1]['id']} - {u['problems'][-1]['title'][:40]}...)")
