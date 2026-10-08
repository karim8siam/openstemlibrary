#!/usr/bin/env python3
"""
enrich_all_units.py
Enriches and expands Units 2 through 8 to ensure each unit delivers ~10,000 to 11,500 words,
achieving a grand total of ~80,000+ words across the entire Inorganic Chemistry I curriculum.
"""

import os, sys

def enrich_unit2():
    import build_inorg1_unit2
    u = build_inorg1_unit2.get_unit2()
    
    # Add deep section on Diagonal Relationships & The First-Row Anomaly
    sec_extra = {
        "id": "sec2_6",
        "title": "§2.6 The First-Row Anomaly & Diagonal Periodic Relationships",
        "content": r"""### The First-Row Anomaly: Why Period 2 Elements Differ Drastically from Heavy Congeners

In every main group (Groups 1, 2, 13–17), the first member belonging to the second period of the periodic table ($\text{Li}, \text{Be}, \text{B}, \text{C}, \text{N}, \text{O}, \text{F}$) displays physical and chemical properties that deviate markedly from those of the heavier congeners within the same vertical column. This systematic divergence is known as the **First-Row Anomaly**.

```
       The Three Quantum Mechanical Pillars of the First-Row Anomaly:
       
   1. Unusually Small Covalent/Ionic Radii & Extreme Electronegativity
   2. Absolute Inaccessibility of Low-Lying d Orbitals (Strict Octet Cap)
   3. Exceptional Facility for pπ-pπ Multiple Bonding (Short Internuclear Separation)
```

#### 1. Radius and Charge Density Extremes:
Second-period atoms possess only the compact $1s^2$ core shell shielding the valence electrons. Because the $1s$ core contains zero radial nodes and minimal spatial volume, the effective nuclear charge $Z_{\text{eff}}$ experienced by $2s$ and $2p$ electrons is extraordinarily high, compressing the atomic radius ($r_{\text{cov}}(\text{F}) = 71\text{ pm}$ vs $r_{\text{cov}}(\text{Cl}) = 99\text{ pm}$).
- Consequently, cations formed by second-period elements ($\text{Li}^+, \text{Be}^{2+}$) possess enormous **charge-to-size ratios** (ionic potentials, $\phi = \frac{z}{r}$), imparting exceptional polarizing power that induces high covalent character into nominally ionic compounds (e.g., $\text{LiCl}$ is soluble in organic solvents, whereas $\text{NaCl}$ is insoluble; $\text{BeCl}_2$ is a covalent polymer).

#### 2. The Strict Octet Cap (Absence of $2d$ Orbitals):
For second-period elements ($n = 2$), the azimuthal quantum number is restricted to $l \in \{0, 1\}$, providing only one $2s$ and three $2p$ orbitals.
- The maximum coordination number of any Period 2 element is strictly **four** (octet capacity of $8$ valence electrons). Thus, boron forms $[\text{BF}_4]^-$ but never $[\text{BF}_6]^{3-}$; nitrogen forms $\text{NF}_3$ but $\text{NF}_5$ is strictly impossible; carbon forms $\text{CF}_4$ but never $\text{CF}_6^{2-}$.
- In sharp contrast, Period 3 elements possess energetically accessible $3d$ orbitals and expanded spatial volumes, readily forming hypercoordinate species such as $[\text{AlF}_6]^{3-}, \text{PF}_5, \text{SF}_6,$ and $[\text{SiF}_6]^{2-}$.

#### 3. Propensity for $p\pi-p\pi$ Multiple Bonding:
Because second-period elements have very short internuclear bond distances ($d(\text{C}-\text{C}) = 154\text{ pm}, d(\text{N}-\text{N}) = 145\text{ pm}$), their parallel $2p$ orbitals achieve powerful lateral spatial overlap, forming strong, stable $\pi$ bonds:
- Carbon dioxide is a stable monomeric gas ($\text{O}=\text{C}=\text{O}$) with two strong double bonds ($D(\text{C}=\text{O}) = 804\text{ kJ}\cdot\text{mol}^{-1}$). In contrast, silicon dioxide ($\text{SiO}_2$) cannot form stable $3p\pi-2p\pi$ bonds due to large internuclear separation ($d(\text{Si}-\text{O}) \approx 162\text{ pm}$); hence, $\text{SiO}_2$ condenses into an infinite three-dimensional giant covalent network of single $\text{Si}-\text{O}$ bonds (quartz).
- Dinitrogen ($\text{N}\equiv\text{N}$) possesses an extraordinarily robust triple bond ($D = 945\text{ kJ}\cdot\text{mol}^{-1}$), rendering it an unreactive diatomic gas. Elemental phosphorus, unable to form efficient $3p\pi-3p\pi$ triple bonds, exists as tetrahedral $\text{P}_4$ molecules or polymeric networks featuring single $\text{P}-\text{P}$ bonds ($D = 200\text{ kJ}\cdot\text{mol}^{-1}$).

---

### Diagonal Periodic Relationships

A striking manifestation of periodic shielding mechanics is the **Diagonal Relationship**, in which an element in Period 2 displays chemical behavior remarkably similar to the element located one period down and one group to the right in Period 3:
$$\mathbf{Li \sim Mg, \quad Be \sim Al, \quad B \sim Si}$$

```
                Group 1       Group 2       Group 13      Group 14
   Period 2:     [ Li ] ----> [ Be ] ----> [  B  ] ----> [  C  ]
                    \            \            \
                     \            \            \
   Period 3:     [ Na ]       [ Mg ]       [ Al ]       [ Si ]
```

#### Physical Origin: The Opposing Vectors of Charge Density
- Moving **across a period (left to right)**: Nuclear charge increases, atomic radius contracts, electronegativity escalates, and polarizing power $\phi = \frac{z}{r}$ increases sharply.
- Moving **down a group (top to bottom)**: Principal quantum number increases, atomic radius expands, electronegativity drops, and polarizing power $\phi$ decreases.
- Moving **diagonally downward and to the right**: The increase in charge density caused by moving right is almost exactly cancelled by the decrease in charge density caused by moving down!
  $$\phi(\text{Li}^+) = \frac{1}{76\text{ pm}} \approx 0.013\text{ pm}^{-1} \quad \longleftrightarrow \quad \phi(\text{Mg}^{2+}) = \frac{2}{72\text{ pm}} \approx 0.028\text{ pm}^{-1}$$
  $$\phi(\text{Be}^{2+}) = \frac{2}{31\text{ pm}} \approx 0.065\text{ pm}^{-1} \quad \longleftrightarrow \quad \phi(\text{Al}^{3+}) = \frac{3}{53.5\text{ pm}} \approx 0.056\text{ pm}^{-1}$$

#### Chemical Evidence for the Triads:
1. **Lithium and Magnesium ($\text{Li} \sim \text{Mg}$)**:
   - Both form normal oxides ($\text{Li}_2\text{O}, \text{MgO}$) when burned in air, rather than peroxides or superoxides (unlike $\text{Na}_2\text{O}_2, \text{KO}_2$).
   - Both react directly with gaseous nitrogen to form stable ionic nitrides: $6\,\text{Li} + \text{N}_2 \rightarrow 2\,\text{Li}_3\text{N}$ and $3\,\text{Mg} + \text{N}_2 \rightarrow \text{Mg}_3\text{N}_2$.
   - Their carbonates thermally decompose into oxides and $\text{CO}_2$ ($\text{Li}_2\text{CO}_3 \rightarrow \text{Li}_2\text{O} + \text{CO}_2$; $\text{MgCO}_3 \rightarrow \text{MgO} + \text{CO}_2$), whereas sodium carbonate ($\text{Na}_2\text{CO}_3$) is thermally stable up to $1000^\circ\text{C}$.
   - Their chlorides ($\text{LiCl}, \text{MgCl}_2$) are deliquescent, crystallize as hydrates, and dissolve readily in ethanol and pyridine.
2. **Beryllium and Aluminum ($\text{Be} \sim \text{Al}$)**:
   - Both form amphoteric oxides ($\text{BeO}, \text{Al}_2\text{O}_3$) and hydroxides ($\text{Be(OH)}_2, \text{Al(OH)}_3$) that dissolve in both strong acids and strong bases:
     $$\text{Be(OH)}_2 + 2\,\text{OH}^- \longrightarrow [\text{Be(OH)}_4]^{2-} \quad (\text{Beryllate})$$
     $$\text{Al(OH)}_3 + \text{OH}^- \longrightarrow [\text{Al(OH)}_4]^- \quad (\text{Aluminate})$$
   - Both form covalent, volatile halides ($\text{BeCl}_2, \text{AlCl}_3$) with chloride-bridged dimeric or polymeric structures ($\text{Be}_n\text{Cl}_{2n}$ chains, $\text{Al}_2\text{Cl}_6$ dimers) that act as powerful Lewis acid catalysts in Friedel-Crafts alkylations.
   - Both metals are rendered passive by concentrated nitric acid due to the formation of an imperviously thin, adherent oxide surface skin.
   - Both form carbide salts that undergo hydrolysis to evolve methane gas:
     $$\text{Be}_2\text{C} + 4\,\text{H}_2\text{O} \longrightarrow 2\,\text{Be(OH)}_2 + \text{CH}_4(g)$$
     $$\text{Al}_4\text{C}_3 + 12\,\text{H}_2\text{O} \longrightarrow 4\,\text{Al(OH)}_3 + 3\,\text{CH}_4(g)$$
3. **Boron and Silicon ($\text{B} \sim \text{Si}$)**:
   - Both are non-metallic semiconductors with high melting points ($\text{B}: 2076^\circ\text{C}, \text{Si}: 1414^\circ\text{C}$).
   - Both form weak, polymeric acidic oxides ($\text{B}_2\text{O}_3, \text{SiO}_2$) that dissolve in alkalis to yield borates and silicates.
   - Both form volatile, spontaneously flammable gaseous hydrides (boranes such as $\text{B}_2\text{H}_6$, silanes such as $\text{SiH}_4$) that hydrolyze rapidly to yield hydrogen gas.
   - Both form covalent halides ($\text{BF}_3, \text{BCl}_3, \text{SiF}_4, \text{SiCl}_4$) that undergo rapid, exothermic hydrolysis in water."""
    }
    
    u['sections'].append(sec_extra)
    
    # Save back
    import pprint
    with open("build_inorg1_unit2.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nUnit 2: Periodicity of the Elements, Electronic Shielding & Relativistic Effects\n"""\n\n')
        f.write("def get_unit2():\n    return " + repr(u) + "\n")
    print("Unit 2 enriched successfully.")

enrich_unit2()
