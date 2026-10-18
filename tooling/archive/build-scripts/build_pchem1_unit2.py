# -*- coding: utf-8 -*-
"""
build_pchem1_unit2.py
Unit 2: The Gaseous State: Kinetic Molecular Theory, Real Gases & Liquefaction
Exhaustive honors-level master digital textbook module with 3x depth,
complete mathematical derivations, and zero course numbers.
"""

def get_unit2():
    return {
        "number": 2,
        "title": "The Gaseous State: Kinetic Molecular Theory, Real Gases & Liquefaction",
        "leadSummary": "Comprehensive physical chemistry of gaseous matter: empirical gas laws and multi-component Dalton-Amagat stoichiometry, rigorous first-principles derivation of pressure from the Kinetic Molecular Theory of Gases, statistical mechanics of the Maxwell-Boltzmann molecular speed distribution and characteristic velocities (v_mp, v_avg, v_rms), kinetic transport phenomena (mean free path, gas viscosity, Graham's diffusion/effusion), non-ideal real gases, van der Waals equation of state, Andrews' carbon dioxide isotherms, critical state inflection thermodynamics, the Law of Corresponding States, and Joule-Thomson gas liquefaction cycles.",
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Empirical Gas Laws & The Ideal Gas Equation of State",
                "content": r"""The macroscopic investigation of gases provided the historical bridge between empirical chemistry and molecular thermodynamics. A gas is a state of matter characterized by complete spatial delocalization: its particles possess sufficient kinetic energy to overcome intermolecular attractive forces, expanding homogeneously to fill any containing vessel.

### The Historical Genesis of Empirical Gas Laws

Over two centuries of experimental physics established four foundational empirical relationships connecting the four state variables: pressure $P$, volume $V$, absolute temperature $T$, and amount of substance $n$:

1. **Boyle's Law (1662 - Robert Boyle & Edme Mariotte)**:
   For a fixed amount of gas at constant temperature (isothermal conditions, $T = \text{const}$):
   $$P \propto \frac{1}{V} \implies P V = C_1(T, n) \quad \text{or} \quad P_1 V_1 = P_2 V_2$$
   The isothermal compressibility of an ideal gas is $\kappa_T \equiv -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_T = \frac{1}{P}$.
2. **Charles's Law (1787 - Jacques Charles & Joseph Louis Gay-Lussac)**:
   For a fixed amount of gas at constant pressure (isobaric conditions, $P = \text{const}$):
   $$V \propto T \implies \frac{V}{T} = C_2(P, n) \quad \text{or} \quad \frac{V_1}{T_1} = \frac{V_2}{T_2}$$
   Extrapolating the linear isobar $V(t) = V_0(1 + \alpha_0 t)$ to zero volume ($V \rightarrow 0$) yields the universal absolute zero of temperature: $t_0 = -1/\alpha_0 = -273.15^\circ\text{C} \implies T = 0\text{ K}$.
3. **Gay-Lussac's Law / Amontons's Law (1802)**:
   For a fixed amount of gas at constant volume (isochoric conditions, $V = \text{const}$):
   $$P \propto T \implies \frac{P}{T} = C_3(V, n) \quad \text{or} \quad \frac{P_1}{T_1} = \frac{P_2}{T_2}$$
4. **Avogadro's Hypothesis (1811 - Amedeo Avogadro)**:
   Equal volumes of all gases under identical conditions of temperature and pressure contain identical numbers of molecules:
   $$V \propto n \quad (\text{at constant } T, P) \implies \frac{V}{n} = V_m(T, P)$$
   At IUPAC standard temperature and pressure ($\text{STP}: T = 273.15\text{ K}, P = 10^5\text{ Pa} = 1\text{ bar}$), the standard molar volume of an ideal gas is:
   $$V_m^\circ = \frac{R T}{P} = \frac{(8.314\,463\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (273.15\text{ K})}{10^5\text{ Pa}} = 0.022\,711\text{ m}^3\cdot\text{mol}^{-1} = 22.711\text{ L}\cdot\text{mol}^{-1}$$
   (At historical standard conditions of $1\text{ atm} = 101\,325\text{ Pa}$, $V_m = 22.414\text{ L}\cdot\text{mol}^{-1}$).

### The Ideal Gas Equation of State

Combining these four empirical laws yields the **Ideal Gas Equation of State**:
$$P V = n R T$$
where $R$ is the universal molar gas constant. Expressing amount $n = m / M$ (where $m$ is sample mass and $M$ is molar mass), the ideal gas law yields an exact equation for mass density $\rho = m / V$:
$$\rho = \frac{P M}{R T} \implies M = \frac{\rho R T}{P}$$

### Multi-Component Gaseous Mixtures

For a mixture of $k$ non-reacting ideal gases enclosed in volume $V$ at temperature $T$, each gas behaves independently as though it occupied the container alone:

1. **Dalton's Law of Partial Pressures (1801)**:
   The total pressure $P_{total}$ exerted by a mixture of ideal gases is the sum of the partial pressures $P_i$ exerted by each individual constituent:
   $$P_{total} = \sum_{i=1}^k P_i = \sum_{i=1}^k \frac{n_i R T}{V} = \left(\sum_{i=1}^k n_i\right) \frac{R T}{V} = \frac{n_{total} R T}{V}$$
2. **Mole Fraction Definition of Partial Pressure**:
   Dividing $P_i$ by $P_{total}$:
   $$\frac{P_i}{P_{total}} = \frac{n_i R T / V}{n_{total} R T / V} = \frac{n_i}{n_{total}} = x_i \implies P_i = x_i P_{total}$$
   This identity serves as the IUPAC thermodynamic definition of partial pressure for all gas mixtures, both ideal and real.
3. **Amagat's Law of Partial Volumes**:
   The total volume $V_{total}$ of an ideal gas mixture is the sum of the individual volumes $V_i$ that each gas would occupy alone at the system pressure $P$ and temperature $T$:
   $$V_{total} = \sum_{i=1}^k V_i, \qquad V_i = \frac{n_i R T}{P} = x_i V_{total}$$"""
            },
            {
                "secNumber": "2.2",
                "title": "Kinetic Molecular Theory (KMT) of Gases & First-Principles Pressure Derivation",
                "content": r"""While the empirical gas laws describe macroscopic phenomena, the **Kinetic Molecular Theory (KMT)** of gases, developed by Daniel Bernoulli (1738), Rudolf Clausius (1857), James Clerk Maxwell (1860), and Ludwig Boltzmann (1872), establishes their mechanical and statistical foundations from Newton's laws of motion.

### Fundamental Postulates of the Kinetic Molecular Theory

1. **Point-Mass Particle Approximation**: A gas consists of an immense ensemble of $N$ identical particles (atoms or molecules) of mass $m$, whose intrinsic molecular volume is negligibly small compared to the total volume $V$ occupied by the gas ($\sum V_{mol} \ll V$).
2. **Chaotic Brownian Trajectories**: Gas molecules are in continuous, chaotic, rectilinear motion in all directions, obeying Newton's classical laws of motion.
3. **Absence of Long-Range Forces**: Intermolecular attractive and repulsive forces are identically zero except during direct physical collision encounters ($U(r) = 0$ for all $r > \sigma$).
4. **Perfect Elasticity of Collisions**: Collisions between gas molecules, and between molecules and container walls, are perfectly elastic: total linear momentum and total translational kinetic energy are conserved without dissipation into thermal degradation.
5. **Thermal Equipartition**: The average translational kinetic energy of gas molecules is strictly proportional to absolute temperature $T$ and is completely independent of chemical identity or molecular mass:
   $$\overline{E_k} = \frac{1}{2}m\overline{c^2} = \frac{3}{2}k_B T$$

### First-Principles Derivation of Gas Pressure

Consider a rectangular container with dimensions $L_x, L_y, L_z$ and volume $V = L_x L_y L_z$ containing $N$ gas molecules of mass $m$. 

Let a molecule possess a velocity vector $\mathbf{c}_i = (u_i, v_i, w_i)$ where $u_i, v_i, w_i$ are the components along the $x, y, z$ axes:
$$c_i^2 = u_i^2 + v_i^2 + w_i^2$$

Consider a collision of molecule $i$ with the planar container wall perpendicular to the $x$-axis at $x = L_x$:
* Initial linear momentum before elastic impact: $p_{x, init} = +m u_i$
* Final linear momentum after specular reflection: $p_{x, final} = -m u_i$
* Momentum transferred to the wall in a single collision:
  $$\Delta p_{x, wall} = p_{x, init} - p_{x, final} = m u_i - (-m u_i) = 2m u_i$$

The molecule must travel a distance $2 L_x$ (to the opposite wall and back) before colliding with this same wall again. The time interval between successive collisions on this wall is:
$$\Delta t_i = \frac{2 L_x}{u_i}$$

By Newton's Second Law ($F = \frac{dp}{dt}$), the time-averaged force $F_{i, x}$ exerted by molecule $i$ on the wall is:
$$F_{i, x} = \frac{\Delta p_{x, wall}}{\Delta t_i} = \frac{2m u_i}{2 L_x / u_i} = \frac{m u_i^2}{L_x}$$

The total force $F_x$ exerted by all $N$ molecules on the wall of surface area $A_x = L_y L_z$ is the summation:
$$F_x = \sum_{i=1}^N \frac{m u_i^2}{L_x} = \frac{m}{L_x} \sum_{i=1}^N u_i^2 = \frac{m N}{L_x} \overline{u^2}$$
where $\overline{u^2} \equiv \frac{1}{N}\sum_{i=1}^N u_i^2$ is the mean-square velocity along the $x$-axis.

The pressure $P$ on this wall is force divided by area:
$$P = \frac{F_x}{A_x} = \frac{m N \overline{u^2}}{L_x (L_y L_z)} = \frac{m N \overline{u^2}}{V}$$

Because molecular velocities are completely isotropic (no spatial direction is preferred in an isotropic thermodynamic ensemble):
$$\overline{u^2} = \overline{v^2} = \overline{w^2}$$
Since the total mean-square speed is $\overline{c^2} = \overline{u^2} + \overline{v^2} + \overline{w^2} = 3\overline{u^2}$, it follows that:
$$\overline{u^2} = \frac{1}{3}\overline{c^2}$$

Substituting this isotropic symmetry into the pressure equation yields the **Fundamental Equation of Kinetic Molecular Theory**:
$$P = \frac{1}{3}\frac{N m \overline{c^2}}{V} = \frac{1}{3}\rho \overline{c^2} \tag{2.1}$$
where $\rho = \frac{N m}{V}$ is the mass density of the gas.

### Connection to Macroscopic Temperature & Internal Energy

Multiplying both sides of Eq. (2.1) by volume $V$ and setting total mass $N m = n M = n N_A m$:
$$P V = \frac{1}{3} N m \overline{c^2} = \frac{2}{3} N \left(\frac{1}{2}m\overline{c^2}\right) = \frac{2}{3} E_k^{trans}$$
where $E_k^{trans}$ is the total translational kinetic energy of the gas.

Equating this mechanical derivation to the macroscopic ideal gas equation $P V = n R T = N k_B T$:
$$\frac{2}{3} E_k^{trans} = N k_B T \implies E_k^{trans} = \frac{3}{2} N k_B T = \frac{3}{2} n R T$$

Dividing by the total number of molecules $N$ reveals the **microscopic statistical definition of temperature**:
$$\overline{\epsilon_k} = \frac{1}{2}m\overline{c^2} = \frac{3}{2}k_B T$$
Absolute temperature is nothing other than a direct macroscopic measure of the mean translational kinetic energy per molecule! Each translational degree of freedom ($x, y, z$) carries precisely $\frac{1}{2}k_B T$ of thermal energy, verifying the classical **Equipartition Theorem**."""
            },
            {
                "secNumber": "2.3",
                "title": "Maxwell-Boltzmann Distribution of Molecular Speeds",
                "content": r"""While the mean-square speed $\overline{c^2}$ provides an aggregate average, individual gas molecules continually exchange momentum and kinetic energy through collisions, establishing a continuous statistical distribution of speeds. In 1860, James Clerk Maxwell applied probability theory, subsequently formalized by Ludwig Boltzmann via the canonical ensemble of statistical mechanics, to deduce the exact molecular velocity distribution function.

### Derivation of the Maxwell-Boltzmann Distribution

Consider a classical gas at thermal equilibrium. The probability that a molecule has velocity components in the differential volume element $du \, dv \, dw$ centered at $(u, v, w)$ is given by the product of independent probabilities:
$$dP(u, v, w) = f_x(u) f_y(v) f_z(w) \, du \, dv \, dw = F(\mathbf{c}) \, d^3\mathbf{c}$$

By isotropic symmetry, this probability density can depend only on the magnitude of the velocity squared $c^2 = u^2 + v^2 + w^2$, requiring:
$$f_x(u) f_y(v) f_z(w) = \phi(u^2 + v^2 + w^2)$$
The only mathematical function satisfying this functional equation is an exponential:
$$f_x(u) = A \exp(-\beta u^2)$$
From the Boltzmann factor of statistical mechanics, the probability of occupying a state with kinetic energy $\epsilon_k = \frac{1}{2}m u^2$ is proportional to $\exp(-\epsilon_k / k_B T)$. Hence $\beta = \frac{m}{2 k_B T}$.

Normalizing the 1D velocity probability distribution:
$$\int_{-\infty}^{+\infty} A \exp\left(-\frac{m u^2}{2 k_B T}\right) du = 1 \implies A \sqrt{\frac{2\pi k_B T}{m}} = 1 \implies A = \left(\frac{m}{2\pi k_B T}\right)^{1/2}$$

The 3D velocity probability density in Cartesian coordinates is therefore:
$$F(u, v, w) \, du \, dv \, dw = \left(\frac{m}{2\pi k_B T}\right)^{3/2} \exp\left( -\frac{m(u^2 + v^2 + w^2)}{2 k_B T} \right) du \, dv \, dw$$

To obtain the probability distribution of molecular **speed** $c = \sqrt{u^2 + v^2 + w^2}$ (a scalar quantity $c \ge 0$), we transform from Cartesian coordinates $(u, v, w)$ to spherical velocity coordinates $(c, \theta, \phi)$:
$$d^3\mathbf{c} = c^2 \sin\theta \, dc \, d\theta \, d\phi$$
Integrating over all orientations ($0 \le \theta \le \pi, 0 \le \phi \le 2\pi$):
$$\int_0^{2\pi} d\phi \int_0^\pi \sin\theta \, d\theta = 4\pi$$

This yields the fundamental **Maxwell-Boltzmann Speed Distribution Function**:
$$f(c) \, dc = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{3/2} c^2 \exp\left(-\frac{m c^2}{2 k_B T}\right) dc \tag{2.2}$$
Or expressing in terms of molar mass $M = N_A m$ and molar gas constant $R = N_A k_B$:
$$f(c) = 4\pi \left(\frac{M}{2\pi R T}\right)^{3/2} c^2 \exp\left(-\frac{M c^2}{2 R T}\right)$$

### Characteristic Molecular Speeds

From the Maxwell-Boltzmann distribution function, physical chemists define three distinct characteristic speeds:

#### 1. The Most Probable Speed ($c_{mp}$ or $v_{mp}$)
The speed corresponding to the maximum of the probability density function $f(c)$:
$$\left.\frac{df(c)}{dc}\right|_{c = c_{mp}} = 0$$
Differentiating Eq. (2.2) with respect to $c$:
$$\frac{d}{dc} \left[ c^2 \exp\left(-\frac{M c^2}{2 R T}\right) \right] = 2c \exp\left(-\frac{M c^2}{2 R T}\right) - \frac{M c^3}{R T} \exp\left(-\frac{M c^2}{2 R T}\right) = 0$$
Dividing by $c \exp(-M c^2 / 2RT) \neq 0$:
$$2 - \frac{M c_{mp}^2}{R T} = 0 \implies c_{mp} = \sqrt{\frac{2 R T}{M}} = \sqrt{\frac{2 k_B T}{m}} \approx 1.414 \sqrt{\frac{R T}{M}}$$

#### 2. The Mean (Average) Speed ($\bar{c}$ or $v_{avg}$)
The statistical expectation value $\langle c \rangle = \int_0^\infty c f(c) dc$:
$$\bar{c} = 4\pi \left(\frac{M}{2\pi R T}\right)^{3/2} \int_0^\infty c^3 \exp\left(-\frac{M c^2}{2 R T}\right) dc$$
Using the standard definite integral $\int_0^\infty x^3 e^{-a x^2} dx = \frac{1}{2 a^2}$ with $a = \frac{M}{2 R T}$:
$$\bar{c} = 4\pi \left(\frac{M}{2\pi R T}\right)^{3/2} \left[ \frac{1}{2 (M / 2RT)^2} \right] = \sqrt{\frac{8 R T}{\pi M}} = \sqrt{\frac{8 k_B T}{\pi m}} \approx 1.596 \sqrt{\frac{R T}{M}}$$

#### 3. The Root-Mean-Square Speed ($c_{rms}$ or $v_{rms}$)
The square root of the mean-square speed $\langle c^2 \rangle = \int_0^\infty c^2 f(c) dc$:
$$\overline{c^2} = 4\pi \left(\frac{M}{2\pi R T}\right)^{3/2} \int_0^\infty c^4 \exp\left(-\frac{M c^2}{2 R T}\right) dc$$
Using the standard definite integral $\int_0^\infty x^4 e^{-a x^2} dx = \frac{3\sqrt{\pi}}{8 a^{5/2}}$:
$$\overline{c^2} = \frac{3 R T}{M} \implies c_{rms} = \sqrt{\overline{c^2}} = \sqrt{\frac{3 R T}{M}} = \sqrt{\frac{3 k_B T}{m}} \approx 1.732 \sqrt{\frac{R T}{M}}$$

#### Universal Ratio of Characteristic Speeds:
$$c_{mp} : \bar{c} : c_{rms} = \sqrt{2} : \sqrt{\frac{8}{\pi}} : \sqrt{3} \approx 1 : 1.128 : 1.225$$

At any given temperature, $c_{mp} < \bar{c} < c_{rms}$. As temperature increases, the speed distribution broadens and shifts toward higher velocities, while the peak height drops to maintain unit normalization ($\int_0^\infty f(c) dc = 1$). Conversely, at fixed temperature, heavier gases (higher $M$) possess narrower distributions peaked at lower speeds."""
            },
            {
                "secNumber": "2.4",
                "title": "Transport Properties: Gas Viscosity, Diffusion & Effusion",
                "content": r"""Transport phenomena in gases describe non-equilibrium macroscopic transport of matter (diffusion), linear momentum (viscosity), and thermal energy (heat conduction) driven by spatial gradients in concentration, velocity, and temperature.

### The Mean Free Path ($\lambda$)

The **mean free path** $\lambda$ is the average distance traversed by a gas molecule between two consecutive collisions.
Consider a molecule of effective collision diameter $d$ traveling at mean speed $\bar{c}$. In time $\Delta t$, it sweeps out a cylindrical collision volume of radius $d$:
$$V_{coll} = \pi d^2 \bar{c} \Delta t$$
The number of target centers in this volume is $\mathcal{N} = \pi d^2 \bar{c} \Delta t (N/V)$. 

If all other molecules were stationary, the collision frequency would be $Z_1 = \pi d^2 \bar{c} (N/V)$. Accounting for the relative velocity distribution of moving collision partners ($\bar{c}_{rel} = \sqrt{2}\bar{c}$):
$$Z_1 = \sqrt{2}\pi d^2 \bar{c} \left(\frac{N}{V}\right)$$
The mean free path is the total distance traveled per unit time ($\bar{c}$) divided by collision frequency $Z_1$:
$$\lambda = \frac{\bar{c}}{Z_1} = \frac{1}{\sqrt{2}\pi d^2 (N/V)} = \frac{k_B T}{\sqrt{2}\pi d^2 P} \tag{2.3}$$

Notice that **mean free path is directly proportional to temperature and inversely proportional to pressure**. For nitrogen gas at $298\text{ K}$ and $1\text{ bar}$ ($d \approx 0.37\text{ nm}$):
$$\lambda \approx \frac{(1.38 \times 10^{-23}\text{ J/K}) \times (298\text{ K})}{\sqrt{2}\pi (0.37 \times 10^{-9}\text{ m})^2 \times (10^5\text{ Pa})} \approx 6.7 \times 10^{-8}\text{ m} = 67\text{ nm}$$
Under ultra-high vacuum conditions ($P \sim 10^{-7}\text{ Pa}$), $\lambda > 100\text{ km}$, far exceeding the dimensions of laboratory vacuum chambers (Knudsen regime).

### Gas Viscosity ($\eta$)

Dynamic viscosity $\eta$ measures the internal frictional resistance to shear flow. In a gas exhibiting a linear macroscopic velocity gradient $\frac{du_x}{dz}$, molecules traveling across hypothetical plane $z$ carry linear $x$-momentum from regions of differing velocity.

By kinetic theory, the net flux of $x$-momentum transferred per unit area per unit time across plane $z$ is:
$$J_{p_x} = -\frac{1}{3}\rho \bar{c} \lambda \frac{du_x}{dz}$$
Comparing with Newton's law of viscosity $\tau_{xz} = -\eta \frac{du_x}{dz}$ yields the kinetic expression for gas viscosity:
$$\eta = \frac{1}{3}\rho \bar{c} \lambda = \frac{1}{3}\left(\frac{N m}{V}\right) \bar{c} \left(\frac{1}{\sqrt{2}\pi d^2 (N/V)}\right) = \frac{m \bar{c}}{3\sqrt{2}\pi d^2}$$
Substituting $\bar{c} = \sqrt{\frac{8 k_B T}{\pi m}}$:
$$\eta = \frac{2}{3\pi^{3/2} d^2}\sqrt{m k_B T} = \frac{2\sqrt{M R T}}{3\pi^{3/2} N_A d^2} \tag{2.4}$$

> **Maxwell's Monumental Prediction**:
> Eq. (2.4) reveals that **the viscosity of a gas is completely independent of pressure and density** at moderate pressures! Furthermore, unlike liquids whose viscosity decreases with temperature, **gas viscosity increases with the square root of temperature ($\eta \propto \sqrt{T}$)** because higher temperatures increase molecular speed and momentum transport across shear layers.

### Graham's Laws of Diffusion & Effusion

* **Effusion**: The process by which gas molecules escape from a container into a vacuum through a pinhole orifice whose diameter is substantially smaller than the mean free path ($d_{hole} \ll \lambda$), ensuring molecules exit without undergoing intermolecular collisions in the aperture.
* The rate of effusion $r_{eff}$ (molecules striking and passing through area $A$ per second) is given by the Hertz-Knudsen relation:
  $$r_{eff} = Z_w A = \frac{1}{4}\left(\frac{N}{V}\right)\bar{c} A = \frac{P A}{\sqrt{2\pi m k_B T}} = \frac{P A N_A}{\sqrt{2\pi M R T}}$$
* **Graham's Law of Effusion (1829)**: At constant $T$ and $P$, the rate of effusion of a gas is inversely proportional to the square root of its molar mass:
  $$\frac{r_1}{r_2} = \sqrt{\frac{M_2}{M_1}}$$
  This principle provided the technological foundation for the historical gaseous diffusion enrichment of uranium ($^{235}\text{UF}_6$ vs $^{238}\text{UF}_6$, with separation factor $\alpha = \sqrt{352/349} \approx 1.0043$)."""
            },
            {
                "secNumber": "2.5",
                "title": "Real Gases, van der Waals Equation & Andrews' Critical Experiments",
                "content": r"""At low temperatures and high pressures, real gases deviate markedly from ideal gas behavior. The **compressibility factor $Z$** quantifies this deviation:
$$Z \equiv \frac{P V_m}{R T} = \frac{V_{m, real}}{V_{m, ideal}}$$
For an ideal gas, $Z = 1$ identically at all conditions. For real gases:
* When $Z < 1$: Attractive intermolecular forces dominate, pulling molecules together and making the molar volume smaller than ideal ($V_{m, real} < V_{m, ideal}$).
* When $Z > 1$: Repulsive forces dominate, as finite molecular cores exclude volume, making the gas less compressible ($V_{m, real} > V_{m, ideal}$).

### The van der Waals Equation of State (1873)

Johannes Diderik van der Waals modified the ideal gas equation by introducing two physically grounded empirical correction parameters:
1. **Excluded Volume Correction ($b$)**: Gas molecules are not mathematical point masses; they possess finite impenetrable hard cores. For $n$ moles of gas, the volume accessible to molecular motion is reduced to $(V - nb)$. The parameter $b$ represents the **covolume** per mole:
   $$b = 4 N_A \left(\frac{4}{3}\pi r^3\right) = 4 V_{actual}$$
   The excluded volume is four times the actual geometric volume of the spherical molecules.
2. **Internal Cohesive Pressure Correction ($a$)**: Intermolecular attractions pull boundary molecules inward, reducing the momentum transfer imparted during container wall collisions. The reduction in pressure is proportional to the square of concentration $(n/V)^2$. Hence, the effective pressure is $P_{eff} = P + \frac{a n^2}{V^2}$.

This yields the iconic **van der Waals Equation of State**:
$$\left( P + \frac{a n^2}{V^2} \right) (V - nb) = n R T \quad \text{or} \quad \left( P + \frac{a}{V_m^2} \right) (V_m - b) = R T \tag{2.5}$$

### Andrews' Experiments on $\text{CO}_2$ & The Critical State

In 1869, Thomas Andrews measured the $P\text{-}V$ isotherms of carbon dioxide over a range of temperatures, discovering the **critical state**:
* At $T > T_c$: The isotherms are smooth monotonic curves resembling ideal gas hyperbolas; no amount of pressure can liquefy the gas.
* At $T < T_c$: As volume is decreased, pressure rises until condensation begins, whereupon the isotherm displays a flat horizontal plateau (liquid-vapor coexistence line where liquid and gas coexist in equilibrium at vapor pressure $P_{vap}$) before rising steeply in the nearly incompressible liquid phase.
* At $T = T_c$: The horizontal coexistence plateau shrinks to a single point of inflection—the **Critical Point** $(P_c, V_c, T_c)$.

At the critical point, the isotherm possesses a horizontal inflection point:
$$\left(\frac{\partial P}{\partial V_m}\right)_{T = T_c} = 0, \qquad \left(\frac{\partial^2 P}{\partial V_m^2}\right)_{T = T_c} = 0$$

Solving the van der Waals equation for pressure:
$$P = \frac{R T}{V_m - b} - \frac{a}{V_m^2}$$
Evaluating the first and second partial derivatives:
$$\left(\frac{\partial P}{\partial V_m}\right)_T = -\frac{R T}{(V_m - b)^2} + \frac{2a}{V_m^3} = 0 \implies \frac{R T_c}{(V_{m,c} - b)^2} = \frac{2a}{V_{m,c}^3}$$
$$\left(\frac{\partial^2 P}{\partial V_m^2}\right)_T = \frac{2R T}{(V_m - b)^3} - \frac{6a}{V_m^4} = 0 \implies \frac{2R T_c}{(V_{m,c} - b)^3} = \frac{6a}{V_{m,c}^4}$$

Dividing the second derivative equation by the first:
$$\frac{2}{V_{m,c} - b} = \frac{3}{V_{m,c}} \implies 2V_{m,c} = 3V_{m,c} - 3b \implies V_{m,c} = 3b \tag{2.6a}$$

Substituting $V_{m,c} = 3b$ back into the first derivative relation:
$$\frac{R T_c}{(3b - b)^2} = \frac{2a}{(3b)^3} \implies \frac{R T_c}{4b^2} = \frac{2a}{27b^3} \implies T_c = \frac{8a}{27 R b} \tag{2.6b}$$

Substituting $V_{m,c}$ and $T_c$ into the equation of state yields the critical pressure:
$$P_c = \frac{R (8a / 27Rb)}{3b - b} - \frac{a}{(3b)^2} = \frac{8a / 27b}{2b} - \frac{a}{9b^2} = \frac{4a}{27b^2} - \frac{3a}{27b^2} = \frac{a}{27b^2} \tag{2.6c}$$

> **The Universal Critical Compressibility Factor**:
> Evaluating the compressibility factor at the critical point for any van der Waals gas:
> $$Z_c = \frac{P_c V_{m,c}}{R T_c} = \frac{(a / 27b^2)(3b)}{R (8a / 27Rb)} = \frac{3a / 27b}{8a / 27b} = \frac{3}{8} = 0.375$$
> While experimental real gases yield $Z_c \approx 0.28 - 0.31$, the van der Waals theory predicts a **universal value independent of chemical identity**.

### The Law of Corresponding States

Defining dimensionless **reduced variables**:
$$P_r \equiv \frac{P}{P_c}, \qquad V_r \equiv \frac{V_m}{V_{m,c}}, \qquad T_r \equiv \frac{T}{T_c}$$
Substituting $P = P_r P_c, V_m = V_r V_{m,c}, T = T_r T_c$ into Eq. (2.5) and dividing through by critical constants yields the **Reduced van der Waals Equation**:
$$\left( P_r + \frac{3}{V_r^2} \right) \left( 3V_r - 1 \right) = 8 T_r \tag{2.7}$$
Notice that parameters $a, b$, and $R$ have completely vanished! This proves the **Principle of Corresponding States**: all fluids, when compared at the same reduced temperature and reduced pressure, possess the same reduced volume and behave identically."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Gas Stoichiometry & Multi-Component Partial Pressures in Hydrocarbon Combustion",
                "statement": r"""A rigid, constant-volume $12.50\text{ L}$ combustion bomb is initially charged with $0.450\text{ mol}$ of gaseous propane ($\text{C}_3\text{H}_8$) and $3.000\text{ mol}$ of pure oxygen gas ($\text{O}_2$) at an initial temperature $T_1 = 298.15\text{ K}$.

1. Calculate the initial partial pressures $P(\text{C}_3\text{H}_8)$ and $P(\text{O}_2)$, and the total initial pressure $P_{init}$ in the vessel.
2. The mixture is ignited electrically, undergoing complete combustion according to the stoichiometric chemical equation:
   $$\text{C}_3\text{H}_8(g) + 5\text{O}_2(g) \longrightarrow 3\text{CO}_2(g) + 4\text{H}_2\text{O}(g)$$
   Determine the limiting reactant, the moles of each gas present after complete reaction, and identify any excess reactant.
3. If the final temperature inside the vessel after combustion reaches $T_2 = 850.0\text{ K}$ (at which water is entirely in the vapor phase), calculate the final total pressure $P_{final}$ and the final partial pressures of each component assuming ideal gas behavior.""",
                "solution": r"""### Step 1: Initial Partial Pressures & Total Pressure

Using the ideal gas law with $V = 12.50\text{ L} = 1.250 \times 10^{-2}\text{ m}^3$ and $T_1 = 298.15\text{ K}$:
$$R = 0.082057\text{ L}\cdot\text{atm}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$$

Total initial moles of gas:
$$n_{init} = n(\text{C}_3\text{H}_8) + n(\text{O}_2) = 0.450\text{ mol} + 3.000\text{ mol} = 3.450\text{ mol}$$

Initial partial pressure of propane:
$$P(\text{C}_3\text{H}_8) = \frac{n(\text{C}_3\text{H}_8) R T_1}{V} = \frac{(0.450\text{ mol}) \times (0.082057) \times (298.15\text{ K})}{12.50\text{ L}} = 0.8812\text{ atm}$$

Initial partial pressure of oxygen:
$$P(\text{O}_2) = \frac{n(\text{O}_2) R T_1}{V} = \frac{(3.000\text{ mol}) \times (0.082057) \times (298.15\text{ K})}{12.50\text{ L}} = 5.8744\text{ atm}$$

Total initial pressure:
$$P_{init} = P(\text{C}_3\text{H}_8) + P(\text{O}_2) = 0.8812\text{ atm} + 5.8744\text{ atm} = 6.756\text{ atm} \quad (\approx 6.845\text{ bar})$$

### Step 2: Reaction Stoichiometry & Limiting Reactant

Stoichiometric ratio required: $\frac{n(\text{O}_2)}{n(\text{C}_3\text{H}_8)} = 5.0$.
Available ratio:
$$\frac{3.000\text{ mol O}_2}{0.450\text{ mol C}_3\text{H}_8} = 6.667 > 5.0$$
Oxygen is in excess; **propane ($\text{C}_3\text{H}_8$) is the limiting reactant**.

Stoichiometric conversion:
* Propane consumed: $0.450\text{ mol} \implies n_{final}(\text{C}_3\text{H}_8) = 0.000\text{ mol}$
* Oxygen consumed: $5 \times 0.450\text{ mol} = 2.250\text{ mol}$
  $$n_{final}(\text{O}_2) = 3.000\text{ mol} - 2.250\text{ mol} = 0.750\text{ mol}$$
* Carbon dioxide formed: $3 \times 0.450\text{ mol} = 1.350\text{ mol CO}_2$
* Water vapor formed: $4 \times 0.450\text{ mol} = 1.800\text{ mol H}_2\text{O}$

Total moles of gas post-combustion:
$$n_{final} = n(\text{O}_2) + n(\text{CO}_2) + n(\text{H}_2\text{O}) = 0.750 + 1.350 + 1.800 = 3.900\text{ mol}$$

### Step 3: Final Pressures at $T_2 = 850.0\text{ K}$

Total final pressure:
$$P_{final} = \frac{n_{final} R T_2}{V} = \frac{(3.900\text{ mol}) \times (0.082057\text{ L}\cdot\text{atm}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (850.0\text{ K})}{12.50\text{ L}}$$
$$P_{final} = \frac{272.02}{12.50} = 21.76\text{ atm} \quad (\approx 22.05\text{ bar})$$

Final partial pressures via mole fractions:
$$x(\text{O}_2) = \frac{0.750}{3.900} = 0.1923 \implies P(\text{O}_2) = 0.1923 \times 21.76\text{ atm} = 4.185\text{ atm}$$
$$x(\text{CO}_2) = \frac{1.350}{3.900} = 0.3462 \implies P(\text{CO}_2) = 0.3462 \times 21.76\text{ atm} = 7.533\text{ atm}$$
$$x(\text{H}_2\text{O}) = \frac{1.800}{3.900} = 0.4615 \implies P(\text{H}_2\text{O}) = 0.4615 \times 21.76\text{ atm} = 10.043\text{ atm}$$
Check sum: $4.185 + 7.533 + 10.043 = 21.761\text{ atm}$. Verified."""
            },
            {
                "tier": "Advanced Level",
                "title": "Escape Velocity Fraction & Kinetic Gas Escape from Planetary Atmospheres",
                "statement": r"""Planetary atmospheric retention depends upon the Maxwell-Boltzmann molecular speed distribution of atmospheric gases relative to the planetary gravitational escape velocity $v_{esc} = \sqrt{2GM / R_{planet}}$. For Earth, $v_{esc} \approx 11.2\text{ km}\cdot\text{s}^{-1} = 11\,200\text{ m}\cdot\text{s}^{-1}$. In the exosphere at an altitude of $500\text{ km}$, the ambient temperature reaches $T = 1200\text{ K}$.

1. Calculate the characteristic speeds ($v_{mp}, \bar{v}, v_{rms}$) for molecular nitrogen ($\text{N}_2, M = 28.02\text{ g}\cdot\text{mol}^{-1}$) and molecular hydrogen ($\text{H}_2, M = 2.016\text{ g}\cdot\text{mol}^{-1}$) at $1200\text{ K}$.
2. For an asymptotic high-velocity limit where $c \gg v_{mp}$, derive the analytical approximation for the fraction of molecules possessing speeds exceeding a critical threshold velocity $v^*$:
   $$F(c > v^*) = \int_{v^*}^\infty f(c) dc$$
3. Evaluate $F(c > v_{esc})$ for both $\text{N}_2$ and $\text{H}_2$ at $1200\text{ K}$ and explain from a physical chemical perspective why Earth's atmosphere is rich in nitrogen while hydrogen has escaped into space.""",
                "solution": r"""### Step 1: Characteristic Speeds at $T = 1200\text{ K}$

Universal constant $R = 8.3145\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$.

#### For Molecular Hydrogen ($\text{H}_2, M = 2.016 \times 10^{-3}\text{ kg}\cdot\text{mol}^{-1}$):
$$v_{mp} = \sqrt{\frac{2 R T}{M}} = \sqrt{\frac{2 \times 8.3145 \times 1200}{2.016 \times 10^{-3}}} = \sqrt{9.898 \times 10^6} = 3146\text{ m}\cdot\text{s}^{-1} \approx 3.15\text{ km/s}$$
$$\bar{v} = \sqrt{\frac{8 R T}{\pi M}} = \sqrt{\frac{4}{\pi}} v_{mp} = 1.1284 \times 3146 = 3550\text{ m}\cdot\text{s}^{-1} \approx 3.55\text{ km/s}$$
$$v_{rms} = \sqrt{\frac{3 R T}{M}} = \sqrt{1.5} v_{mp} = 1.2247 \times 3146 = 3853\text{ m}\cdot\text{s}^{-1} \approx 3.85\text{ km/s}$$

#### For Molecular Nitrogen ($\text{N}_2, M = 28.02 \times 10^{-3}\text{ kg}\cdot\text{mol}^{-1}$):
Since speeds scale inversely with $\sqrt{M}$:
$$\text{Scale Factor} = \sqrt{\frac{2.016}{28.02}} = \sqrt{0.07195} = 0.2682$$
$$v_{mp}(\text{N}_2) = 3146 \times 0.2682 = 844\text{ m}\cdot\text{s}^{-1} \approx 0.84\text{ km/s}$$
$$\bar{v}(\text{N}_2) = 3550 \times 0.2682 = 952\text{ m}\cdot\text{s}^{-1} \approx 0.95\text{ km/s}$$
$$v_{rms}(\text{N}_2) = 3853 \times 0.2682 = 1033\text{ m}\cdot\text{s}^{-1} \approx 1.03\text{ km/s}$$

### Step 2: High-Velocity Tail Integration of Maxwell-Boltzmann Distribution

The fraction of molecules with speed exceeding $v^*$ is:
$$F(c > v^*) = 4\pi \left(\frac{M}{2\pi R T}\right)^{3/2} \int_{v^*}^\infty c^2 \exp\left(-\frac{M c^2}{2 R T}\right) dc$$
Let $a = \frac{M}{2 R T} = \frac{1}{v_{mp}^2}$. Let $u = c$ and $dv = c e^{-a c^2} dc$.
Integrating by parts:
$$\int_{v^*}^\infty c^2 e^{-a c^2} dc = \left[ -\frac{c}{2a} e^{-a c^2} \right]_{v^*}^\infty + \frac{1}{2a} \int_{v^*}^\infty e^{-a c^2} dc$$
$$= \frac{v^*}{2a} e^{-a (v^*)^2} + \frac{\sqrt{\pi}}{4 a^{3/2}} \text{erfc}(\sqrt{a} v^*)$$

When $v^* \gg v_{mp}$ (meaning $\sqrt{a} v^* \gg 1$), we use the asymptotic expansion for the complementary error function $\text{erfc}(x) \sim \frac{e^{-x^2}}{\sqrt{\pi} x} (1 - \frac{1}{2x^2} + \dots)$.
Multiplying by the pre-factor $4\pi (a/\pi)^{3/2} = \frac{4 a^{3/2}}{\sqrt{\pi}}$:
$$F(c > v^*) \approx \frac{4 a^{3/2}}{\sqrt{\pi}} \left[ \frac{v^*}{2a} e^{-a (v^*)^2} + \frac{1}{4a^2 v^*} e^{-a (v^*)^2} \right]$$
$$F(c > v^*) \approx \frac{2}{\sqrt{\pi}} \left(\frac{v^*}{v_{mp}} + \frac{v_{mp}}{2 v^*}\right) \exp\left( -\left(\frac{v^*}{v_{mp}}\right)^2 \right) \tag{2.8}$$

### Step 3: Quantitative Atmospheric Escape Comparison

At $v^* = v_{esc} = 11\,200\text{ m/s}$:

#### For Hydrogen ($\text{H}_2$):
$$\frac{v_{esc}}{v_{mp}} = \frac{11\,200}{3146} = 3.56$$
$$\left(\frac{v_{esc}}{v_{mp}}\right)^2 = 3.56^2 = 12.67$$
$$F(\text{H}_2) \approx \frac{2}{\sqrt{\pi}} (3.56) \exp(-12.67) = (4.02) \times (3.14 \times 10^{-6}) \approx 1.26 \times 10^{-5}$$
Approximately **1 in every 80,000 hydrogen molecules** at any instant possesses speed exceeding escape velocity. Given typical collision frequencies $Z_1 \sim 10^3\text{ s}^{-1}$ in the exosphere, the entire atmospheric inventory of $\text{H}_2$ evaporates gravitationally into space on geological timescales ($10^5 - 10^6\text{ years}$—Jeans escape).

#### For Nitrogen ($\text{N}_2$):
$$\frac{v_{esc}}{v_{mp}} = \frac{11\,200}{844} = 13.27$$
$$\left(\frac{v_{esc}}{v_{mp}}\right)^2 = 13.27^2 = 176.1$$
$$F(\text{N}_2) \approx \frac{2}{\sqrt{\pi}} (13.27) \exp(-176.1) = (14.97) \times (3.3 \times 10^{-77}) \approx 5 \times 10^{-76} \approx 0$$
The probability of a nitrogen molecule reaching escape velocity is mathematically zero ($10^{-76}$). Earth retains its nitrogen-oxygen atmosphere across billions of years."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "First-Principles Derivation of Critical Constants & The Universal Law of Corresponding States",
                "statement": r"""Consider the van der Waals equation of state written in terms of molar volume $V_m$:
$$P = \frac{R T}{V_m - b} - \frac{a}{V_m^2}$$

1. At the critical point $(P_c, V_c, T_c)$, the critical isotherm possesses a horizontal inflection point:
   $$\left(\frac{\partial P}{\partial V_m}\right)_T = 0 \quad \text{and} \quad \left(\frac{\partial^2 P}{\partial V_m^2}\right)_T = 0$$
   Derive from first principles the expressions for $V_{m,c}, T_c$, and $P_c$ strictly in terms of parameters $a, b$, and $R$.
2. Prove that at the critical point, the van der Waals equation can be expressed as a cubic polynomial in $V_m$ with three degenerate real roots: $(V_m - V_{m,c})^3 = 0$. By equating coefficients with the expanded equation of state, confirm your expressions for $V_{m,c}, T_c, P_c$.
3. Prove that defining reduced dimensionless variables $P_r \equiv P/P_c, V_r \equiv V_m/V_{m,c}, T_r \equiv T/T_c$ collapses the equation of state into:
   $$\left( P_r + \frac{3}{V_r^2} \right) (3V_r - 1) = 8 T_r$$
   explaining the thermodynamic significance of the Principle of Corresponding States.""",
                "solution": r"""### Step 1: Derivative Approach to the Critical Point

Given:
$$P = \frac{R T}{V_m - b} - \frac{a}{V_m^2}$$

First derivative with respect to $V_m$ at constant $T$:
$$\left(\frac{\partial P}{\partial V_m}\right)_T = -\frac{R T}{(V_m - b)^2} + \frac{2a}{V_m^3} = 0 \implies R T = \frac{2a (V_m - b)^2}{V_m^3} \tag{1}$$

Second derivative:
$$\left(\frac{\partial^2 P}{\partial V_m^2}\right)_T = \frac{2R T}{(V_m - b)^3} - \frac{6a}{V_m^4} = 0 \implies 2R T = \frac{6a (V_m - b)^3}{V_m^4} \tag{2}$$

Substitute Eq. (1) into Eq. (2):
$$2 \left[ \frac{2a (V_{m,c} - b)^2}{V_{m,c}^3} \right] = \frac{6a (V_{m,c} - b)^3}{V_{m,c}^4}$$
Divide both sides by $\frac{2a (V_{m,c} - b)^2}{V_{m,c}^3} \neq 0$:
$$2 = \frac{3 (V_{m,c} - b)}{V_{m,c}} \implies 2 V_{m,c} = 3 V_{m,c} - 3b \implies V_{m,c} = 3b \tag{3}$$

Substitute $V_{m,c} = 3b$ back into Eq. (1):
$$R T_c = \frac{2a (3b - b)^2}{(3b)^3} = \frac{2a (4b^2)}{27b^3} = \frac{8a}{27b} \implies T_c = \frac{8a}{27 R b} \tag{4}$$

Substitute $V_{m,c} = 3b$ and $T_c$ into the equation of state to find $P_c$:
$$P_c = \frac{R (8a / 27Rb)}{3b - b} - \frac{a}{(3b)^2} = \frac{8a / 27b}{2b} - \frac{a}{9b^2} = \frac{4a}{27b^2} - \frac{3a}{27b^2} = \frac{a}{27b^2} \tag{5}$$

### Step 2: Cubic Polynomial Root Degeneracy Approach

Multiply the van der Waals equation $(P + a/V_m^2)(V_m - b) = R T$ by $V_m^2$:
$$(P V_m^2 + a)(V_m - b) = R T V_m^2$$
$$P V_m^3 - P b V_m^2 + a V_m - a b - R T V_m^2 = 0$$
Dividing by $P$:
$$V_m^3 - \left(b + \frac{R T}{P}\right) V_m^2 + \left(\frac{a}{P}\right) V_m - \frac{a b}{P} = 0 \tag{6}$$

At the critical temperature and pressure ($T = T_c, P = P_c$), the three roots of this cubic equation coalesce into a single triply degenerate root at $V_m = V_{m,c}$:
$$(V_m - V_{m,c})^3 = 0 \implies V_m^3 - 3 V_{m,c} V_m^2 + 3 V_{m,c}^2 V_m - V_{m,c}^3 = 0 \tag{7}$$

Equating corresponding polynomial coefficients between Eq. (6) and Eq. (7):
1. Coefficient of $V_m^2$:
   $$3 V_{m,c} = b + \frac{R T_c}{P_c} \tag{8}$$
2. Coefficient of $V_m$:
   $$3 V_{m,c}^2 = \frac{a}{P_c} \tag{9}$$
3. Constant term:
   $$V_{m,c}^3 = \frac{a b}{P_c} \tag{10}$$

Divide Eq. (10) by Eq. (9):
$$\frac{V_{m,c}^3}{3 V_{m,c}^2} = \frac{a b / P_c}{a / P_c} \implies \frac{V_{m,c}}{3} = b \implies V_{m,c} = 3b$$

Substitute $V_{m,c} = 3b$ into Eq. (9):
$$3 (3b)^2 = \frac{a}{P_c} \implies 27b^2 = \frac{a}{P_c} \implies P_c = \frac{a}{27b^2}$$

Substitute $V_{m,c} = 3b$ and $P_c$ into Eq. (8):
$$3 (3b) = b + \frac{R T_c}{a / 27b^2} \implies 9b - b = \frac{27b^2 R T_c}{a} \implies 8b = \frac{27b^2 R T_c}{a} \implies T_c = \frac{8a}{27 R b}$$
Both mathematical derivations yield identical critical constants.

### Step 3: Derivation of the Reduced van der Waals Equation

Express variables in reduced form: $P = P_r P_c, V_m = V_r V_{m,c}, T = T_r T_c$:
$$\left( P_r P_c + \frac{a}{V_r^2 V_{m,c}^2} \right) (V_r V_{m,c} - b) = R T_r T_c$$
Substitute $P_c = \frac{a}{27b^2}, V_{m,c} = 3b, T_c = \frac{8a}{27 R b}$:
$$\left( P_r \frac{a}{27b^2} + \frac{a}{V_r^2 (9b^2)} \right) (3b V_r - b) = R T_r \left(\frac{8a}{27 R b}\right)$$
Factor out $\frac{a}{27b^2}$ from the first bracket:
$$\frac{a}{27b^2} \left( P_r + \frac{3}{V_r^2} \right) \cdot b(3V_r - 1) = \frac{8a}{27b} T_r$$
$$\frac{a b}{27b^2} \left( P_r + \frac{3}{V_r^2} \right) (3V_r - 1) = \frac{8a}{27b} T_r$$
$$\frac{a}{27b} \left( P_r + \frac{3}{V_r^2} \right) (3V_r - 1) = \frac{8a}{27b} T_r$$
Divide both sides by $\frac{a}{27b}$:
$$\left( P_r + \frac{3}{V_r^2} \right) (3V_r - 1) = 8 T_r \tag{Q.E.D.}$$

This completes the proof. The reduced equation contains only universal numerical constants ($3, 1, 8$) and zero substance-specific parameters, establishing the rigorous theoretical foundation of corresponding states thermodynamics."""
            }
        ]
    }
