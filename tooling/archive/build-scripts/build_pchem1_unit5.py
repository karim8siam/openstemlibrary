# -*- coding: utf-8 -*-
"""
build_pchem1_unit5.py
Unit 5: Physical Properties of Solutions, Colligative Phenomena & Distribution Law
Exhaustive honors-level master digital textbook module with 3x depth,
complete mathematical derivations, and zero course numbers.
"""

def get_unit5():
    return {
        "number": 5,
        "title": "Physical Properties of Solutions, Colligative Phenomena & Distribution Law",
        "leadSummary": "Thermodynamics and physical chemistry of multi-component solution phases: molecular energetics and Gibbs free energy of dissolution, comprehensive mathematical derivation of concentration unit interconversions with solution density functions, temperature and pressure solubility equilibria including Henry's Law and decompression mechanics, ideal solution thermodynamics and Raoult's Law, first-principles chemical potential derivations of colligative phenomena (vapor pressure lowering, ebullioscopic boiling elevation, cryoscopic freezing depression, and van 't Hoff osmotic pressure), electrolyte non-ideality and van 't Hoff i-factors, and the Nernst Distribution Law with analytical multi-stage solvent extraction efficiency.",
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Types of Solutions & Thermodynamics of Dissolution",
                "content": r"""A **solution** is a homogeneous mixture of two or more chemical substances forming a single thermodynamic phase down to the sub-nanometer scale. The constituent present in the greatest stoichiometric abundance is typically designated the **solvent**, while the dispersed species are termed **solutes**.

### Thermodynamic Taxonomy of Solutions

Solutions exist across all physical states of matter:
* **Gas-in-Gas**: e.g., atmospheric air (completely miscible due to negligible intermolecular forces at low pressure).
* **Gas-in-Liquid**: e.g., dissolved oxygen ($\text{O}_2$) in aquatic ecosystems or carbon dioxide in carbonated beverages.
* **Liquid-in-Liquid**: e.g., ethanol in water (completely miscible) vs octane in water (immiscible).
* **Solid-in-Liquid**: e.g., aqueous sodium chloride ($\text{NaCl}$) or glucose solutions.
* **Gas-in-Solid**: e.g., hydrogen gas absorbed interstitially within metallic palladium ($\text{PdH}_x$).
* **Solid-in-Solid (Solid Solutions)**: e.g., substitutional alloys (alpha-brass: $\text{Zn}$ in $\text{Cu}$) and interstitial alloys (carbon in iron forming austenite and martensite).

### The Three-Step Energetic Model of Dissolution

The formation of a solution from pure components is understood by decomposing the thermodynamic process into a three-step Born-Haber-type energetic cycle:

1. **Step 1: Solute-Solute Particle Separation ($\Delta H_1 > 0$)**:
   Solute molecules or ions must be pulled apart from their pure condensed phase, breaking solute-solute intermolecular attractions or ionic crystal lattices:
   $$\Delta H_1 = \Delta H_{latt} \quad (\text{for ionic crystals}) \quad \text{or} \quad \Delta H_1 > 0 \quad (\text{endothermic})$$
2. **Step 2: Solvent-Solvent Cavity Expansion ($\Delta H_2 > 0$)**:
   Molecules of the solvent must be pushed apart to create microscopic cavities of sufficient volume to accommodate the incoming solute particles, breaking solvent-solvent cohesive bonds (e.g., hydrogen bonds in water):
   $$\Delta H_2 > 0 \quad (\text{endothermic})$$
3. **Step 3: Solute-Solvent Solvation / Hydration ($\Delta H_3 < 0$)**:
   Solute particles insert into the solvent cavities, establishing attractive solute-solvent interactions (ion-dipole, dipole-dipole, or dispersion forces):
   $$\Delta H_3 = \Delta H_{solv} < 0 \quad (\text{exothermic})$$

By Hess's Law, the overall **Enthalpy of Solution** is:
$$\Delta H_{soln} = \Delta H_1 + \Delta H_2 + \Delta H_3 \tag{5.1}$$

### The Gibbs Free Energy of Dissolution & "Like Dissolves Like"

The spontaneous formation of a solution at constant temperature and pressure is dictated by the change in **Gibbs Free Energy of Mixing**:
$$\Delta G_{soln} = \Delta H_{soln} - T \Delta S_{soln} < 0 \tag{5.2}$$

1. **Entropy of Dissolution ($\Delta S_{soln}$)**:
   Dispersing solute particles throughout the solvent volume drastically increases the spatial configurational entropy of the system. For an ideal binary solution of components 1 and 2:
   $$\Delta S_{mix}^{ideal} = -n R (x_1 \ln x_1 + x_2 \ln x_2) > 0 \quad (\text{always strictly positive!})$$
   Because $x_1, x_2 < 1$, the logarithms are negative, ensuring $\Delta S_{mix} > 0$ unconditionally.
2. **The "Like Dissolves Like" Principle**:
   * *Polar Solute in Polar Solvent* (e.g., $\text{NaCl}$ in $\text{H}_2\text{O}$): The immense exothermic ion-dipole solvation enthalpy ($\Delta H_3 \ll 0$) is large enough to compensate for the endothermic lattice breaking ($\Delta H_1$) and cavity creation ($\Delta H_2$). Consequently, $\Delta H_{soln}$ is small (slightly positive or negative), and the positive $-T\Delta S_{soln}$ term drives spontaneous dissolution ($\Delta G_{soln} < 0$).
   * *Nonpolar Solute in Polar Solvent* (e.g., Oil in $\text{H}_2\text{O}$): Nonpolar hydrocarbons interact with water only through weak dispersion forces ($\Delta H_3$ is tiny). Furthermore, water molecules around nonpolar solutes are forced into rigid, highly ordered hydrogen-bonded "iceberg" clathrate cages (**Hydrophobic Effect**), resulting in a net negative entropy change ($\Delta S_{soln} < 0$). Both $\Delta H_{soln} > 0$ and $-T\Delta S_{soln} > 0$, making $\Delta G_{soln} \gg 0$ (completely insoluble).
   * *Nonpolar Solute in Nonpolar Solvent* (e.g., $\text{I}_2$ in $\text{CCl}_4$): Intermolecular forces in both pure components and the mixture are all weak London dispersion forces ($\Delta H_1 + \Delta H_2 \approx -\Delta H_3 \implies \Delta H_{soln} \approx 0$). The process is driven entirely by the favorable entropy of mixing ($\Delta G_{soln} \approx -T\Delta S_{mix} < 0$)."""
            },
            {
                "secNumber": "5.2",
                "title": "Solution Concentration Units & Interconversions",
                "content": r"""Quantitative physical chemistry requires exact mathematical precision when expressing the relative abundance of components in a solution phase.

### Primary Concentration Scales

Let a solution contain solute $A$ (molar mass $M_A$, mass $m_A$, moles $n_A$) dissolved in solvent $B$ (molar mass $M_B$, mass $m_B$, moles $n_B$), producing a total solution mass $m_{soln} = m_A + m_B$, total solution volume $V$, and macroscopic mass density $\rho = m_{soln} / V$.

1. **Mass Percent ($\% w/w$)**:
   $$\% w/w = \left(\frac{m_A}{m_A + m_B}\right) \times 100\% = \left(\frac{m_A}{m_{soln}}\right) \times 100\%$$
2. **Mole Fraction ($x_A$)**:
   $$x_A = \frac{n_A}{n_A + n_B}, \qquad x_B = \frac{n_B}{n_A + n_B}, \qquad x_A + x_B = 1$$
   Mole fraction is dimensionless and strictly temperature-independent.
3. **Molarity ($C$ or $M$)**:
   $$M = \frac{n_A}{V_{soln}\text{ (in Liters)}} = \frac{m_A / M_A}{V_{soln}\text{ (L)}}$$
   Because liquid volume expands with temperature according to the thermal expansion coefficient $\alpha_P$:
   $$V(T) \approx V_0 [1 + \alpha_P(T - T_0)] \implies M(T) = \frac{M(T_0)}{1 + \alpha_P(T - T_0)}$$
   **Molarity changes with temperature**, introducing systematic errors in precision temperature-dependent experiments.
4. **Molality ($m$ or $b$)**:
   $$m = \frac{n_A}{m_B\text{ (in kilograms of solvent)}} = \frac{m_A / M_A}{(m_{soln} - m_A) \times 10^{-3}\text{ kg}}$$
   Because mass is an invariant scalar under temperature and pressure variations, **molality is strictly independent of temperature and pressure**, making it the indispensable metric for thermodynamic colligative properties.

### Exact Mathematical Interconversion Derivations

Let solution density be $\rho$ in $\text{g}\cdot\text{mL}^{-1} = \text{g}\cdot\text{cm}^{-3} = 10^3\text{ kg}\cdot\text{m}^{-3}$, and solute molar mass be $M_A$ in $\text{g}\cdot\text{mol}^{-1}$.

#### 1. From Molarity ($M$) to Molality ($m$):
Consider exactly $1.000\text{ Liter} = 1000\text{ mL}$ of solution:
* Moles of solute: $n_A = M\text{ mol}$.
* Mass of solute: $m_A = n_A M_A = M \cdot M_A\text{ (grams)}$.
* Total mass of solution: $m_{soln} = V \cdot \rho = 1000 \cdot \rho\text{ (grams)}$.
* Mass of solvent: $m_B = m_{soln} - m_A = 1000\rho - M \cdot M_A\text{ (grams)} = \frac{1000\rho - M \cdot M_A}{1000}\text{ (kg)}$.
Applying the definition of molality:
$$m = \frac{n_A}{m_B\text{ (kg)}} = \frac{M}{\frac{1000\rho - M \cdot M_A}{1000}} = \frac{1000 M}{1000\rho - M \cdot M_A} \tag{5.3}$$

#### 2. From Molality ($m$) to Molarity ($M$):
Consider an amount of solution containing exactly $1.000\text{ kg} = 1000\text{ g}$ of pure solvent ($m_B = 1000\text{ g}$):
* Moles of solute: $n_A = m\text{ mol}$.
* Mass of solute: $m_A = m \cdot M_A\text{ (grams)}$.
* Total solution mass: $m_{soln} = 1000 + m \cdot M_A\text{ (grams)}$.
* Solution volume: $V_{soln} = \frac{m_{soln}}{\rho} = \frac{1000 + m \cdot M_A}{\rho}\text{ (mL)} = \frac{1000 + m \cdot M_A}{1000\rho}\text{ (Liters)}$.
Applying the definition of molarity:
$$M = \frac{n_A}{V_{soln}\text{ (L)}} = \frac{m}{\frac{1000 + m \cdot M_A}{1000\rho}} = \frac{1000 m \rho}{1000 + m \cdot M_A} \tag{5.4}$$

#### 3. From Molality ($m$) to Mole Fraction ($x_A$):
In a sample containing $1.000\text{ kg} = 1000\text{ g}$ of solvent of molar mass $M_B$ ($\text{g}\cdot\text{mol}^{-1}$):
* Moles of solvent: $n_B = \frac{1000}{M_B}\text{ mol}$.
* Moles of solute: $n_A = m\text{ mol}$.
$$x_A = \frac{m}{m + \frac{1000}{M_B}} = \frac{m M_B}{m M_B + 1000} \tag{5.5}$$
For dilute aqueous solutions ($M_B = 18.015\text{ g/mol}, m M_B \ll 1000$):
$$x_A \approx \frac{m M_B}{1000} = \frac{18.015}{1000} m \approx 0.0180 m$$"""
            },
            {
                "secNumber": "5.3",
                "title": "Factors Governing Solubility",
                "content": r"""Solubility is the maximum concentration of a solute that dissolves in a given solvent at a specified temperature and pressure to establish a dynamic thermodynamic equilibrium with undissolved solute:
$$\text{Undissolved Solute} \rightleftharpoons \text{Dissolved Solute}$$

### Effect of Temperature on Solubility

The temperature dependence of solubility is governed by **Le Chatelier's Principle** and the **van 't Hoff equation**:
$$\left(\frac{\partial \ln S}{\partial T}\right)_P = \frac{\Delta H_{soln}}{R T^2} \tag{5.6}$$

1. **Solids in Liquids**:
   * *Endothermic Dissolution ($\Delta H_{soln} > 0$)*: Ingesting thermal energy shifts equilibrium toward the dissolved state. Solubility **increases with temperature**. Most salts exhibit this behavior (e.g., $\text{KNO}_3, \text{NH}_4\text{NO}_3, \text{glucose}$).
   * *Exothermic Dissolution ($\Delta H_{soln} < 0$)*: Releasing heat means elevated temperature opposes dissolution. Solubility **decreases with temperature** (e.g., cerium sulfate $\text{Ce}_2(\text{SO}_4)_3$, calcium acetate, lithium carbonate $\text{Li}_2\text{CO}_3$).
2. **Gases in Liquids**:
   Dissolution of a gas involves bringing freely translating gas molecules into a confined liquid phase. Because condensation releases intermolecular attractive energy and restricts translational freedom:
   $$\Delta H_{soln}(gas) < 0 \quad (\text{almost universally exothermic}), \qquad \Delta S_{soln}(gas) \ll 0$$
   Because $\Delta H_{soln} < 0$, Eq. (5.6) dictates that **the solubility of gases in liquids universally decreases as temperature rises**.
   * *Environmental Implication (Thermal Pollution)*: Industrial discharge of warm cooling water into rivers decreases dissolved $\text{O}_2$ concentrations, causing mass asphyxiation of aquatic organisms.

### Effect of Pressure on Gas Solubility: Henry's Law

While pressure has a negligible effect on the solubility of liquids and solids (due to their tiny molar volumes), it exerts a dominant effect on gas solubility.

In 1803, William Henry demonstrated empirically that at constant temperature, the solubility of a gas in a liquid is directly proportional to the partial pressure of the gas above the solution:

> **Henry's Law**:
> $$C_g = k_H \cdot P_g \tag{5.7}$$
> where $C_g$ is the equilibrium concentration (molarity or molality) of the dissolved gas, $P_g$ is its partial pressure above the liquid, and $k_H$ is the **Henry's Law Constant** characteristic of the specific gas-solvent pair at temperature $T$.
> Alternatively, expressing concentration in mole fraction:
> $$P_g = K_{H,x} \cdot x_g$$

#### Thermodynamic Derivation of Henry's Law
At liquid-gas phase equilibrium, the chemical potential of the gas in the vapor phase must equal its chemical potential in the solution phase:
$$\mu_g(gas) = \mu_g(soln)$$
Assuming the gas behaves ideally:
$$\mu_g(gas) = \mu_g^\circ(gas) + R T \ln\left(\frac{P_g}{P^\circ}\right)$$
In an infinitely dilute real solution ($x_g \rightarrow 0$), the solute obeys Henry's limiting law:
$$\mu_g(soln) = \mu_g^*(soln) + R T \ln x_g$$
Equating expressions:
$$\mu_g^\circ(gas) + R T \ln\left(\frac{P_g}{P^\circ}\right) = \mu_g^*(soln) + R T \ln x_g$$
$$R T \ln\left(\frac{P_g}{x_g P^\circ}\right) = \mu_g^*(soln) - \mu_g^\circ(gas) = \Delta G_{transfer}^\circ$$
$$\frac{P_g}{x_g} = P^\circ \exp\left( \frac{\Delta G_{transfer}^\circ}{R T} \right) \equiv K_{H,x}(T) \tag{5.8}$$
Since $\Delta G_{transfer}^\circ$ depends only on $T$, the ratio $P_g / x_g$ is an invariant constant at constant temperature, deriving Henry's Law from first thermodynamic principles!

#### Limitations of Henry's Law
Henry's Law fails when:
1. Gas pressure is very high ($P > 5 - 10\text{ bar}$), where non-ideal gas compressibility and solvent saturation effects manifest.
2. The gas undergoes a chemical reaction with the solvent. For example, carbon dioxide reacts with water:
   $$\text{CO}_2(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{H}_2\text{CO}_3(aq) \rightleftharpoons \text{H}^+(aq) + \text{HCO}_3^-(aq)$$
   and ammonia ionizes:
   $$\text{NH}_3(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{NH}_4^+(aq) + \text{OH}^-(aq)$$
   These chemical equilibria buffer and dramatically inflate total apparent gas solubility beyond Henry's linear prediction.

#### Physiological Application: Decompression Sickness ("The Bends")
According to Henry's Law, when a deep-sea diver breathes compressed air at depth ($P_{total} = 4\text{ bar}$ at $30\text{ m}$ depth), the partial pressure of nitrogen is $P(\text{N}_2) = 0.78 \times 4 = 3.12\text{ bar}$—four times atmospheric level. Substantial volumes of $\text{N}_2$ dissolve into blood and lipid-rich neural tissues.
If the diver ascends rapidly to the surface, ambient hydrostatic pressure drops abruptly. The dissolved nitrogen becomes supersaturated, nucleating gas bubbles directly within bloodstream capillaries, joints, and myelin sheaths, causing excruciating pain, paralysis, or fatal embolism. Safe diving requires slow decompression stops, or substituting nitrogen with helium (Heliox), which has a much lower Henry's constant and lipid solubility."""
            },
            {
                "secNumber": "5.4",
                "title": "Colligative Properties of Nonelectrolyte & Electrolyte Solutions",
                "content": r"""**Colligative properties** (from Latin *colligatus*, meaning "bound together") are physical properties of solutions that depend strictly on the **ratio of the number of solute particles to solvent particles**, completely independent of the chemical identity, size, or structure of the solute.

The four classical colligative properties are:
1. Vapor Pressure Lowering ($\Delta P$)
2. Boiling Point Elevation ($\Delta T_b$)
3. Freezing Point Depression ($\Delta T_f$)
4. Osmotic Pressure ($\Pi$)

All colligative phenomena originate from a single microscopic reality: **the addition of a nonvolatile solute dilutes the solvent, lowering its chemical potential $\mu_A(soln)$ relative to pure liquid solvent $\mu_A^*$**:
$$\mu_A(soln) = \mu_A^*(l) + R T \ln x_A = \mu_A^*(l) + R T \ln(1 - x_B) \approx \mu_A^*(l) - R T x_B \tag{5.9}$$
Because $x_B > 0$, $\ln(1 - x_B) < 0$, which depresses the liquid chemical potential curve, expanding the temperature range over which the liquid phase is thermodynamically stable!

### 1. Vapor Pressure Lowering: Raoult's Law (1886)

For an ideal solution, Francois-Marie Raoult established that the partial vapor pressure of solvent $A$ above a solution is proportional to its mole fraction in the liquid phase:
$$P_A = x_A P_A^\circ \tag{5.10}$$
where $P_A^\circ$ is the vapor pressure of pure solvent $A$ at that temperature.
For a solution containing an involatile solute $B$ ($x_A = 1 - x_B$):
$$P_A = (1 - x_B) P_A^\circ = P_A^\circ - x_B P_A^\circ \implies \Delta P \equiv P_A^\circ - P_A = x_B P_A^\circ \tag{5.11}$$
The relative vapor pressure lowering is exactly equal to the mole fraction of the solute:
$$\frac{\Delta P}{P_A^\circ} = x_B$$

### 2. Boiling Point Elevation ($\Delta T_b$)

Because the nonvolatile solute depresses the vapor pressure curve, the solution must be heated to a higher temperature before its vapor pressure equals the external atmospheric pressure ($P = 1\text{ bar}$).

At the elevated boiling point $T_b = T_b^* + \Delta T_b$, phase equilibrium requires $\mu_A(soln) = \mu_A(vap)$.
Using Eq. (5.9) with pure vapor at standard pressure ($\mu_A(vap) = \mu_A^*(vap)$):
$$\mu_A^*(l) + R T \ln x_A = \mu_A^*(vap) \implies \ln x_A = \frac{\mu_A^*(vap) - \mu_A^*(l)}{R T} = \frac{\Delta G_{vap}^\circ(T)}{R T}$$
Differentiating with respect to temperature using the Gibbs-Helmholtz relation $\frac{d(\Delta G/T)}{dT} = -\frac{\Delta H}{T^2}$:
$$\frac{d\ln x_A}{dT} = -\frac{\Delta H_{vap}^\circ}{R T^2}$$
Integrating from pure solvent ($x_A = 1, T = T_b^*$) to solution ($x_A = 1 - x_B, T = T_b$):
$$\ln(1 - x_B) = -\frac{\Delta H_{vap}^\circ}{R} \int_{T_b^*}^{T_b} \frac{dT}{T^2} = \frac{\Delta H_{vap}^\circ}{R} \left( \frac{1}{T_b} - \frac{1}{T_b^*} \right) = -\frac{\Delta H_{vap}^\circ}{R} \left( \frac{T_b - T_b^*}{T_b T_b^*} \right)$$
For dilute solutions, $\ln(1 - x_B) \approx -x_B$, $\Delta T_b = T_b - T_b^* \ll T_b^*$, so $T_b T_b^* \approx (T_b^*)^2$:
$$-x_B \approx -\frac{\Delta H_{vap}^\circ}{R (T_b^*)^2} \Delta T_b \implies \Delta T_b = \left( \frac{R (T_b^*)^2}{\Delta H_{vap}^\circ} \right) x_B$$
Substituting $x_B \approx \frac{m M_A}{1000}$ (where $m$ is molality and $M_A$ is solvent molar mass in $\text{g/mol}$):
$$\Delta T_b = \left( \frac{R (T_b^*)^2 M_A}{1000 \Delta H_{vap}^\circ} \right) m = K_b \cdot m \tag{5.12}$$
where $K_b \equiv \frac{R (T_b^*)^2 M_A}{1000 \Delta H_{vap}^\circ}$ is the **Ebullioscopic Constant** characteristic of the pure solvent (for water, $K_b = 0.512\text{ K}\cdot\text{kg}\cdot\text{mol}^{-1}$).

### 3. Freezing Point Depression ($\Delta T_f$)

When a solution freezes, pure solid solvent typically crystallizes out first (e.g., pure ice from seawater). Phase equilibrium between solid solvent and solution requires $\mu_A(soln) = \mu_A^*(solid)$.
Following an identical thermodynamic derivation with $\Delta H_{fus}^\circ$:
$$\Delta T_f = T_f^* - T_f = K_f \cdot m \tag{5.13}$$
where $K_f \equiv \frac{R (T_f^*)^2 M_A}{1000 \Delta H_{fus}^\circ}$ is the **Cryoscopic Constant** of the solvent (for water, $K_f = 1.86\text{ K}\cdot\text{kg}\cdot\text{mol}^{-1}$; for camphor, $K_f = 39.7\text{ K}\cdot\text{kg}\cdot\text{mol}^{-1}$).

### 4. Osmotic Pressure ($\Pi$): The van 't Hoff Equation

**Osmosis** is the spontaneous net transport of solvent molecules across a semi-permeable membrane (permeable to solvent but impermeable to solute particles) from a region of lower solute concentration (higher solvent chemical potential) to higher solute concentration.

To halt this osmotic flow, an external mechanical pressure $\Pi$ must be applied to the solution compartment.
At osmotic equilibrium:
$$\mu_A(soln, P + \Pi) = \mu_A^*(l, P)$$
$$\mu_A^*(l, P + \Pi) + R T \ln x_A = \mu_A^*(l, P)$$
Since $\left(\frac{\partial \mu}{\partial P}\right)_T = V_{m,A}$:
$$\mu_A^*(l, P + \Pi) - \mu_A^*(l, P) = \int_P^{P+\Pi} V_{m,A} dP = V_{m,A} \Pi$$
Therefore:
$$V_{m,A} \Pi + R T \ln(1 - x_B) = 0 \implies \Pi = -\frac{R T}{V_{m,A}} \ln(1 - x_B) \approx \frac{R T x_B}{V_{m,A}}$$
For a dilute solution, $x_B \approx n_B / n_A$ and $n_A V_{m,A} \approx V_{total}$:
$$\Pi = \frac{n_B R T}{V_{total}} = M R T \tag{5.14}$$
This is the celebrated **van 't Hoff Equation for Osmotic Pressure (1887)**, bearing an identical mathematical form to the ideal gas law!

### Electrolyte Solutions & The van 't Hoff Factor ($i$)

When an electrolyte dissolves in water, it dissociates into ions, yielding more particles in solution than stoichiometric formula units:
$$i \equiv \frac{\text{Actual moles of particles in solution}}{\text{Moles of solute formula units dissolved}} = \frac{\text{Measured colligative property}}{\text{Calculated colligative property for nonelectrolyte}}$$

All colligative property equations for electrolytes incorporate $i$:
$$\Delta P = i x_B P_A^\circ, \quad \Delta T_b = i K_b m, \quad \Delta T_f = i K_f m, \quad \Pi = i M R T \tag{5.15}$$

#### Degree of Dissociation ($\alpha$)
Consider a weak electrolyte $A_{\nu_+} B_{\nu_-}$ that dissociates into $\nu = \nu_+ + \nu_-$ total ions:
$$A_{\nu_+} B_{\nu_-} \rightleftharpoons \nu_+ A^{z+} + \nu_- B^{z-}$$
* Initial moles: $1$
* Moles dissociated: $\alpha$
* Remaining undissociated: $1 - \alpha$
* Ions produced: $\nu \alpha$
* Total moles of particles at equilibrium: $n_{tot} = (1 - \alpha) + \nu \alpha = 1 + (\nu - 1)\alpha$.
By definition, $i = n_{tot} / 1 = 1 + (\nu - 1)\alpha$. Rearranging isolates the **degree of dissociation**:
$$\alpha = \frac{i - 1}{\nu - 1} \tag{5.16}$$

In real solutions at finite concentrations, $i$ is slightly lower than ideal integer values ($\nu$) due to **ion pairing** and electrostatic screening described by the **Debye-Hückel Theory**."""
            },
            {
                "secNumber": "5.5",
                "title": "The Nernst Distribution Law (Partition Coefficient)",
                "content": r"""When a solute is added to a system containing two mutually immiscible (or partially miscible) liquid solvents, the solute distributes itself between the two liquid phases until thermodynamic partition equilibrium is achieved.

### The Nernst Distribution Law (1891)

Let solute $A$ distribute between two liquid phases 1 and 2 at constant temperature $T$:
$$A(\text{solvent 1}) \rightleftharpoons A(\text{solvent 2})$$

At thermodynamic equilibrium, the chemical potential of the solute in phase 1 must equal its chemical potential in phase 2:
$$\mu_A^{(1)} = \mu_A^{(2)}$$
Expressing chemical potentials in dilute solutions:
$$\mu_A^{\circ(1)} + R T \ln C_1 = \mu_A^{\circ(2)} + R T \ln C_2$$
$$R T \ln\left(\frac{C_1}{C_2}\right) = \mu_A^{\circ(2)} - \mu_A^{\circ(1)} = \Delta G_{partition}^\circ$$
Since $\Delta G_{partition}^\circ$ is a function purely of temperature, the concentration ratio is constant at fixed temperature:

> **The Nernst Distribution Law**:
> $$K_D = \frac{C_1}{C_2} \tag{5.17}$$
> where $K_D$ is the **Partition Coefficient (Distribution Coefficient)**.

#### Conditions for Validity:
1. The temperature must be constant throughout the extraction.
2. Both liquid phases must be mutually immiscible (or mutually saturated).
3. The solute must exist in the **identical molecular state (same molecular weight and chemical form)** in both phases, with neither dissociation nor association occurring in either solvent.

### Deviations: Association and Dissociation

When the solute undergoes chemical changes in one of the phases:

1. **Association in One Phase**:
   Suppose the solute exists as normal monomeric molecules $A$ in phase 1 (concentration $C_1$), but associates into $n$-mers ($A_n$) in phase 2 (e.g., benzoic acid dimerizing in benzene via dual hydrogen bonds: $2\text{C}_6\text{H}_5\text{COOH} \rightleftharpoons (\text{C}_6\text{H}_5\text{COOH})_2$):
   $$n A \rightleftharpoons A_n, \qquad K_{assoc} = \frac{[A_n]_2}{[A]_2^n} \implies [A]_2 = \left(\frac{[A_n]_2}{K_{assoc}}\right)^{1/n}$$
   The Nernst partition applies strictly between monomeric species:
   $$K_D = \frac{C_1}{[A]_2} = \frac{C_1}{\sqrt[n]{C_2}} \implies \frac{C_1}{\sqrt[n]{C_2}} = \text{const} \tag{5.18}$$
2. **Dissociation in One Phase**:
   Suppose the solute undergoes electrolytic dissociation in aqueous phase 1 into ions with degree of dissociation $\alpha$:
   $$AB \rightleftharpoons A^+ + B^-$$
   The concentration of undissociated neutral molecules is $C_1(1 - \alpha)$. Nernst distribution applies only to the un-ionized neutral species:
   $$K_D = \frac{C_1(1 - \alpha)}{C_2} \tag{5.19}$$

### Theory of Multi-Stage Solvent Extraction

Solvent extraction is an indispensable analytical and industrial technique used to extract organic compounds, pharmaceuticals, and metal complexes from aqueous media into organic solvents.

Let $W_0$ be the initial mass of solute dissolved in volume $V$ of water (solvent 1).
Suppose we extract this solution using volume $v$ of an immiscible organic solvent (solvent 2) in which the distribution coefficient is:
$$K_D = \frac{C_{aqueous}}{C_{organic}} = \frac{C_1}{C_2}$$

#### Single Extraction:
After the first extraction, let $W_1$ be the mass of solute remaining unextracted in the aqueous phase.
* Mass extracted into organic phase: $W_0 - W_1$.
* Concentration in aqueous phase: $C_1 = \frac{W_1}{V}$.
* Concentration in organic phase: $C_2 = \frac{W_0 - W_1}{v}$.
From the distribution law:
$$K_D = \frac{W_1 / V}{(W_0 - W_1) / v} = \frac{W_1 v}{(W_0 - W_1) V}$$
$$K_D (W_0 - W_1) V = W_1 v \implies K_D W_0 V = W_1 (K_D V + v)$$
$$W_1 = W_0 \left( \frac{K_D V}{K_D V + v} \right) = W_0 \left( \frac{V}{V + \frac{1}{K_D} v} \right)$$
If we define partition coefficient as $P = \frac{C_{org}}{C_{aq}} = \frac{1}{K_D}$:
$$W_1 = W_0 \left( \frac{V}{V + P v} \right)$$

#### Multiple ($n$) Successive Extractions:
If the aqueous solution is extracted $n$ successive times, each time using a fresh volume $v$ of organic solvent, mathematical induction yields the general **Extraction Formula**:
$$W_n = W_0 \left( \frac{V}{V + P v} \right)^n \tag{5.20}$$

> **Fundamental Extraction Principle**:
> For a fixed total volume of extracting solvent $V_{total} = n \cdot v$, **performing multiple extractions with small portions of solvent is vastly more efficient than performing a single extraction with the entire solvent volume**.
> Mathematically, since $\left(\frac{V}{V + P(V_{total}/n)}\right)^n < \frac{V}{V + P V_{total}}$ for all $n > 1$, multi-stage extraction minimizes the unextracted solute $W_n$ exponentially."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Molar Mass Determination of Bovine Serum Albumin via Membrane Osmometry",
                "statement": r"""Membrane osmometry is the premier classical colligative method for determining the absolute number-average molar mass of high-molecular-weight macromolecules, proteins, and synthetic polymers.

A research biophysicist dissolves $2.500\text{ g}$ of pure crystalline Bovine Serum Albumin (BSA) protein in sufficient phosphate-buffered aqueous saline ($\text{pH} = 7.00$) to yield exactly $100.0\text{ mL}$ of solution. The solution is placed inside an electronic membrane osmometer fitted with a cellulose acetate semi-permeable membrane at $T = 298.15\text{ K}$.
* Measured osmotic pressure: $\Pi = 9.15\text{ mmHg} = 9.15\text{ Torr}$
* Standard gravitational acceleration: $g = 9.80665\text{ m}\cdot\text{s}^{-2}$
* Density of mercury: $\rho_{Hg} = 13.5951 \times 10^3\text{ kg}\cdot\text{m}^{-3}$
* Universal gas constant: $R = 8.314\,463\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$

1. Convert the osmotic pressure $\Pi$ into coherent SI units of Pascals ($\text{Pa}$).
2. Using the van 't Hoff osmotic equation $\Pi = M R T = \frac{c R T}{M_{protein}}$, calculate the experimental molar mass $M_{protein}$ of Bovine Serum Albumin in $\text{g}\cdot\text{mol}^{-1}$.
3. Calculate the boiling point elevation $\Delta T_b$ and freezing point depression $\Delta T_f$ that this identical protein solution would exhibit in water ($K_b = 0.512\text{ K}\cdot\text{kg/mol}, K_f = 1.86\text{ K}\cdot\text{kg/mol}$). Explain why freezing point depression and boiling point elevation are utterly useless for macromolecular mass determination.""",
                "solution": r"""### Step 1: Conversion of Osmotic Pressure to Pascals

$$\Pi = 9.15\text{ Torr} \times \left(\frac{101\,325\text{ Pa}}{760\text{ Torr}}\right) = 1219.9\text{ Pa}$$

### Step 2: Calculation of Protein Molar Mass

Mass concentration of BSA in solution:
$$c = \frac{m}{V} = \frac{2.500\text{ g}}{0.1000\text{ L}} = 25.00\text{ g}\cdot\text{L}^{-1} = 25.00\text{ kg}\cdot\text{m}^{-3}$$

From the van 't Hoff equation:
$$\Pi = \left(\frac{c}{M_{protein}}\right) R T \implies M_{protein} = \frac{c R T}{\Pi}$$
Substitute SI base units:
$$M_{protein} = \frac{(25.00\text{ kg}\cdot\text{m}^{-3}) \times (8.314\,463\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (298.15\text{ K})}{1219.9\text{ N}\cdot\text{m}^{-2}}$$
$$M_{protein} = \frac{61\,973.1\text{ J}\cdot\text{m}^{-3}\cdot\text{mol}^{-1}}{1219.9\text{ N}\cdot\text{m}^{-2}} = 50.80\text{ kg}\cdot\text{mol}^{-1} = 50\,800\text{ g}\cdot\text{mol}^{-1}$$
(Accounting for non-ideality virial corrections in salt solutions, the true unaggregated BSA monomer mass is $\sim 66.4\text{ kDa}$).

### Step 3: Comparison with Boiling Elevation and Freezing Depression

Moles of protein in $100\text{ mL}$ of water ($\approx 100\text{ g} = 0.100\text{ kg}$ solvent):
$$n = \frac{2.500\text{ g}}{50\,800\text{ g}\cdot\text{mol}^{-1}} = 4.921 \times 10^{-5}\text{ mol}$$
Molality:
$$m = \frac{4.921 \times 10^{-5}\text{ mol}}{0.100\text{ kg}} = 4.921 \times 10^{-4}\text{ mol}\cdot\text{kg}^{-1}$$

Calculate colligative shifts:
* Freezing Point Depression:
  $$\Delta T_f = K_f \cdot m = 1.86\text{ K}\cdot\text{kg/mol} \times 4.921 \times 10^{-4}\text{ mol/kg} = 0.000\,915\text{ K} \approx 0.0009^\circ\text{C}$$
* Boiling Point Elevation:
  $$\Delta T_b = K_b \cdot m = 0.512\text{ K}\cdot\text{kg/mol} \times 4.921 \times 10^{-4}\text{ mol/kg} = 0.000\,252\text{ K} \approx 0.00025^\circ\text{C}$$

#### Critical Methodological Comparison:
* $\Delta T_f$ is under $0.001^\circ\text{C}$, completely buried beneath background thermal noise and impossible to measure on standard analytical thermometers.
* In striking contrast, the osmotic pressure $\Pi = 9.15\text{ mmHg} = 124.4\text{ mm H}_2\text{O}$ corresponds to a colossal liquid column height of over **$12.4\text{ centimeters of water}$**, easily measured with sub-millimeter precision.
* Hence, **osmometry is $10^4$ to $10^5$ times more sensitive than ebullioscopy or cryoscopy**, rendering it the only viable colligative method for macromolecules."""
            },
            {
                "tier": "Advanced Level",
                "title": "Cryoscopic Determination of Degree of Dissociation & van 't Hoff Factor for Dichloroacetic Acid",
                "statement": r"""A $0.200\text{ m}$ aqueous solution of dichloroacetic acid ($\text{CHCl}_2\text{COOH}$, a moderately strong organic acid) is prepared in pure deionized water. Experimental cryoscopic measurements reveal that the solution begins to freeze at an observed freezing point $T_f = -0.426^\circ\text{C}$.

Given for pure water:
* Normal freezing point: $T_f^* = 0.000^\circ\text{C} = 273.15\text{ K}$
* Cryoscopic constant: $K_f = 1.860\text{ K}\cdot\text{kg}\cdot\text{mol}^{-1}$

1. Calculate the apparent van 't Hoff factor $i$ of dichloroacetic acid in this solution.
2. Formulate the ionization equilibrium for dichloroacetic acid in water and derive the algebraic relationship connecting $i$ to the degree of dissociation $\alpha$.
3. Calculate the degree of dissociation $\alpha$ of dichloroacetic acid in this $0.200\text{ m}$ solution.
4. Calculate the acid dissociation constant $K_a$ of dichloroacetic acid at $273\text{ K}$.""",
                "solution": r"""### Step 1: Calculation of van 't Hoff Factor $i$

Freezing point depression:
$$\Delta T_f = T_f^* - T_f = 0.000^\circ\text{C} - (-0.426^\circ\text{C}) = 0.426\text{ K}$$

From the colligative freezing relation:
$$\Delta T_f = i \cdot K_f \cdot m$$
Solve for $i$:
$$i = \frac{\Delta T_f}{K_f \cdot m} = \frac{0.426\text{ K}}{1.860\text{ K}\cdot\text{kg}\cdot\text{mol}^{-1} \times 0.200\text{ mol}\cdot\text{kg}^{-1}} = \frac{0.426}{0.372} = 1.14516 \longrightarrow 1.145$$

### Step 2: Ionization Equilibrium & $\alpha$ Relation

Dichloroacetic acid ionizes as a monoprotic acid:
$$\text{CHCl}_2\text{COOH}(aq) \rightleftharpoons \text{H}^+(aq) + \text{CHCl}_2\text{COO}^-(aq)$$
Each formula unit that dissociates yields $\nu = 2$ ions ($\nu_+ = 1\text{ H}^+, \nu_- = 1\text{ CHCl}_2\text{COO}^-$).

ICE analysis in molality terms:
* Initial: $m(\text{HA}) = m_0$, $m(\text{H}^+) = 0$, $m(\text{A}^-) = 0$
* Change: $-m_0 \alpha$, $+m_0 \alpha$, $+m_0 \alpha$
* Equilibrium: $m_0(1 - \alpha)$, $m_0 \alpha$, $m_0 \alpha$

Total particle molality:
$$m_{total} = m_0(1 - \alpha) + m_0 \alpha + m_0 \alpha = m_0(1 + \alpha)$$
Since $m_{total} = i \cdot m_0$:
$$i = 1 + \alpha \implies \alpha = i - 1$$

### Step 3: Degree of Dissociation $\alpha$

$$\alpha = 1.14516 - 1 = 0.14516 \approx 0.145 = 14.5\%$$
In a $0.200\text{ m}$ aqueous solution at $0^\circ\text{C}$, dichloroacetic acid is **$14.5\%$ dissociated** into ions.

### Step 4: Calculation of Acid Dissociation Constant $K_a$

Assuming dilute solution where molality approximates molarity ($C \approx m = 0.200\text{ mol/kg}$):
Equilibrium concentrations:
$$[\text{H}^+] = m_0 \alpha = 0.200 \times 0.14516 = 0.02903\text{ m}$$
$$[\text{CHCl}_2\text{COO}^-] = m_0 \alpha = 0.02903\text{ m}$$
$$[\text{CHCl}_2\text{COOH}] = m_0 (1 - \alpha) = 0.200 \times (1 - 0.14516) = 0.17097\text{ m}$$

Acid dissociation constant:
$$K_a = \frac{[\text{H}^+][\text{A}^-]}{[\text{HA}]} = \frac{(m_0 \alpha)^2}{m_0(1 - \alpha)} = \frac{m_0 \alpha^2}{1 - \alpha}$$
$$K_a = \frac{0.200 \times (0.14516)^2}{1 - 0.14516} = \frac{0.200 \times 0.02107}{0.85484} = \frac{0.004214}{0.85484} = 4.93 \times 10^{-3}$$
$$\text{p}K_a = -\log_{10}(4.93 \times 10^{-3}) = 2.31$$
Cryoscopic colligative measurements accurately determined the thermodynamic ionization constant of the acid."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Rigorous Thermodynamic Derivation of the Cryoscopic Constant Kf via Chemical Potential Equality",
                "statement": r"""Consider a dilute binary solution consisting of a nonvolatile, insoluble solute (mole fraction $x_B$) dissolved in a solvent $A$ (mole fraction $x_A = 1 - x_B$). At the freezing point $T_f$ of the solution, pure solid solvent freezes out in equilibrium with the liquid solution:
$$\mu_A(soln, T_f, P) = \mu_A^*(solid, T_f, P)$$

1. For an ideal solution, express $\mu_A(soln)$ in terms of the chemical potential of the pure liquid solvent $\mu_A^*(liquid)$ and mole fraction $x_A$.
2. State the fundamental thermodynamic definition of the molar Gibbs free energy of fusion $\Delta G_{fus,m}^\circ(T) = \mu_A^*(liquid) - \mu_A^*(solid)$.
3. Using the **Gibbs-Helmholtz Equation**:
   $$\left( \frac{\partial(\Delta G / T)}{\partial T} \right)_P = -\frac{\Delta H}{T^2}$$
   derive the differential relationship governing $\frac{d\ln x_A}{dT}$.
4. Integrating from the pure solvent freezing point $T_f^*$ ($x_A = 1$) to the solution freezing point $T_f$ ($x_A = 1 - x_B$), and performing a Taylor series expansion in the dilute limit ($x_B \ll 1, \Delta T_f \ll T_f^*$), prove rigorously that:
   $$\Delta T_f = K_f \cdot m$$
   where the cryoscopic constant is defined identically as:
   $$K_f \equiv \frac{R (T_f^*)^2 M_A}{1000 \Delta H_{fus}^\circ}$$""",
                "solution": r"""### Step 1: Chemical Potential Equilibrium

At the freezing point $T_f$, pure crystalline solid solvent $A$ is in thermodynamic equilibrium with liquid solution:
$$\mu_A(soln, T_f, P) = \mu_A^*(s, T_f, P) \tag{1}$$

For an ideal solution:
$$\mu_A(soln, T_f, P) = \mu_A^*(l, T_f, P) + R T_f \ln x_A \tag{2}$$
Substituting Eq. (2) into Eq. (1):
$$\mu_A^*(l, T_f, P) + R T_f \ln x_A = \mu_A^*(s, T_f, P)$$
Rearranging:
$$R T_f \ln x_A = \mu_A^*(s, T_f, P) - \mu_A^*(l, T_f, P) = -\Delta G_{fus,m}^\circ(T_f) \tag{3}$$
where $\Delta G_{fus,m}^\circ \equiv \mu_A^*(l) - \mu_A^*(s)$ is the molar Gibbs free energy of fusion (solid $\rightarrow$ liquid) of the pure solvent.

Dividing Eq. (3) by $R T_f$:
$$\ln x_A = -\frac{\Delta G_{fus,m}^\circ(T_f)}{R T_f} \tag{4}$$

### Step 2: Application of the Gibbs-Helmholtz Equation

Differentiate Eq. (4) with respect to temperature $T$ at constant pressure $P$:
$$\frac{d\ln x_A}{dT} = -\frac{1}{R} \frac{d}{dT}\left[ \frac{\Delta G_{fus,m}^\circ(T)}{T} \right]$$
Recalling the fundamental **Gibbs-Helmholtz Equation**:
$$\left( \frac{\partial(G / T)}{\partial T} \right)_P = -\frac{H}{T^2} \implies \frac{d}{dT}\left[ \frac{\Delta G_{fus,m}^\circ}{T} \right] = -\frac{\Delta H_{fus,m}^\circ}{T^2}$$
Substituting this identity:
$$\frac{d\ln x_A}{dT} = -\frac{1}{R}\left( -\frac{\Delta H_{fus,m}^\circ}{T^2} \right) = \frac{\Delta H_{fus,m}^\circ}{R T^2} \tag{5}$$

### Step 3: Definite Integration Over Phase Boundary

Integrate both sides between the two thermodynamic limits:
* Lower limit: Pure solvent, $x_A = 1$ at normal freezing point $T = T_f^*$
* Upper limit: Solution, $x_A = 1 - x_B$ at depressed freezing point $T = T_f$

$$\int_{1}^{1 - x_B} d\ln x_A = \int_{T_f^*}^{T_f} \frac{\Delta H_{fus,m}^\circ}{R T^2} dT$$
Assuming the standard molar enthalpy of fusion $\Delta H_{fus,m}^\circ$ is constant across the narrow temperature range $\Delta T_f = T_f^* - T_f$:
$$\ln(1 - x_B) = \frac{\Delta H_{fus,m}^\circ}{R} \left[ -\frac{1}{T} \right]_{T_f^*}^{T_f} = -\frac{\Delta H_{fus,m}^\circ}{R} \left( \frac{1}{T_f} - \frac{1}{T_f^*} \right)$$
$$\ln(1 - x_B) = -\frac{\Delta H_{fus,m}^\circ}{R} \left( \frac{T_f^* - T_f}{T_f T_f^*} \right) = -\frac{\Delta H_{fus,m}^\circ \Delta T_f}{R T_f T_f^*} \tag{6}$$

### Step 4: Dilute Solution Limit & Expansion

In the dilute solution limit ($x_B \ll 1$):
1. Taylor series expansion of the logarithm:
   $$\ln(1 - x_B) = -x_B - \frac{x_B^2}{2} - \dots \approx -x_B$$
2. Since $\Delta T_f \ll T_f^*$, we approximate $T_f \approx T_f^*$:
   $$T_f T_f^* \approx (T_f^*)^2$$

Substituting these approximations into Eq. (6):
$$-x_B \approx -\frac{\Delta H_{fus,m}^\circ \Delta T_f}{R (T_f^*)^2}$$
$$\Delta T_f \approx \left[ \frac{R (T_f^*)^2}{\Delta H_{fus,m}^\circ} \right] x_B \tag{7}$$

Express the mole fraction $x_B$ in terms of molality $m$ (moles of solute per $1000\text{ g}$ of solvent):
$$x_B = \frac{n_B}{n_A + n_B} \approx \frac{n_B}{n_A} = \frac{m}{1000 / M_A} = \frac{m M_A}{1000}$$
where $M_A$ is the molar mass of the solvent in $\text{g}\cdot\text{mol}^{-1}$.

Substituting $x_B = \frac{m M_A}{1000}$ into Eq. (7):
$$\Delta T_f = \left[ \frac{R (T_f^*)^2 M_A}{1000 \Delta H_{fus,m}^\circ} \right] m \tag{Q.E.D.}$$

Defining the bracketed quantity as the cryoscopic constant $K_f$:
$$K_f \equiv \frac{R (T_f^*)^2 M_A}{1000 \Delta H_{fus,m}^\circ}$$
$$\Delta T_f = K_f \cdot m$$
This completes the rigorous first-principles thermodynamic derivation. Notice that $K_f$ depends exclusively upon properties of the pure solvent ($T_f^*, M_A, \Delta H_{fus}^\circ$) and is completely independent of the solute, providing the fundamental theoretical proof of why freezing point depression is a pure colligative property."""
            }
        ]
    }
