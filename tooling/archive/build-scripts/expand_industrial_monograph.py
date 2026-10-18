# -*- coding: utf-8 -*-
"""
expand_industrial_monograph.py
Injects University Honors research monographs & industrial engineering case studies
into the sections of all 10 units of Industrial Chemistry.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def inject_monographs(units):
    monographs = {
        "unit-1-textiles-and-dyes": r"""

### University Honors Industrial Case Study: The High-Modulus Para-Aramid (Kevlar) Polymerization Reactor
Poly($p$-phenylene terephthalamide) (PPTA / Kevlar) is synthesized by low-temperature solution polycondensation of $p$-phenylenediamine (PPD) and terephthaloyl chloride (TPLC) in anhydrous $N$-methylpyrrolidone (NMP) containing calcium chloride ($\text{CaCl}_2$):
$$\text{PPD} + \text{TPLC} \overset{\text{NMP} / \text{CaCl}_2}{\longrightarrow} [-\text{NH-C}_6\text{H}_4\text{-NH-CO-C}_6\text{H}_4\text{-CO-}]_n + 2n\text{HCl}$$
- **Role of $\text{CaCl}_2$**: Calcium cations coordinate with NMP carbonyl oxygens and amide protons, disrupting inter-chain hydrogen bonds to prevent premature polymer precipitation before high degree of polymerization ($\overline{DP}_n > 150$) is achieved.
- **Liquid Crystalline Dope Rheology**: At concentrations above $14\text{ wt}\%$ in concentrated ($98 - 100\%$) sulfuric acid ($\text{H}_2\text{SO}_4$), rigid rod PPTA molecules align spontaneously into a **nematic lyotropic liquid crystalline phase**.
- **Dry-Jet Wet Spinning**: The dope is extruded at $80 - 90^\circ\text{C}$ across an air gap ($10 - 20\text{ mm}$) before plunging into a cold water coagulation bath ($1 - 5^\circ\text{C}$). Elongational extensional flow in the air gap achieves near-perfect axial orientation of polymer chains, producing fibers with a tensile modulus exceeding **$120 - 180\text{ GPa}$** and tenacity $> 28\text{ cN/dtex}$.""",

        "unit-2-fertilizer-industries": r"""

### University Honors Industrial Case Study: The Autoclave Corrosion & Passive Passivation in Urea Synthesis
In high-pressure urea synthesis reactors ($150 - 200\text{ bar}$, $180 - 200^\circ\text{C}$), ammonium carbamate ($\text{NH}_2\text{COONH}_4$) is aggressively corrosive to stainless steels, dissolving standard 316L metallurgy within hours:
- **Oxygen Passivation Mechanism**: To protect the austenitic stainless steel liner (or modern urea-grade duplex 25-22-2 / 29Cr-9Ni-3Mo), gaseous oxygen (dilute air, $0.2 - 0.6\text{ vol}\%$) is continuously injected into the feed $\text{CO}_2$ stream.
- **Surface Electrochemical Film**: The injected oxygen maintains the redox potential of the steel in the stable passive zone, regenerating an insoluble protective chromium-iron oxide passive film:
  $$2\text{Cr} + 3\text{H}_2\text{O} \longrightarrow \text{Cr}_2\text{O}_3 + 6\text{H}^+ + 6e^-$$
- **Stripper Tube Metallurgy**: In thermal or $\text{CO}_2$-stripping loops, high wall temperatures ($205 - 215^\circ\text{C}$) demand advanced titanium or bimetallic zirconium tubes ($\text{Zr} 702$) that resist carbamate boiling erosion-corrosion without requiring air injection.""",

        "unit-3-sugar-and-starch": r"""

### University Honors Industrial Case Study: Dextran Contamination & Enzymatic Polysaccharide Mitigation
When sugarcane experiences post-harvest delays in tropical climates, epiphytic bacteria (*Leuconostoc mesenteroides*) metabolize sucrose into extracellular high-molecular-weight **Dextran** ($\alpha\text{-(1}\to\text{6)}$-linked D-glucan with $\alpha\text{-(1}\to\text{3)}$ branch points, $M_w > 10^6\text{ g/mol}$):
$$\text{Sucrose} \overset{\text{Dextransucrase}}{\longrightarrow} \text{Dextran} + \text{D-Fructose}$$
- **Process Havoc**: Dextran drastically elevates juice and syrup viscosity, distorting sucrose crystal growth into elongated needle-shaped "cigar" crystals that cannot be separated in centrifugal baskets.
- **Biotechnological Remedy**: Industrial cane mills inject thermo-tolerant fungal **dextranase** enzymes ($50 - 65^\circ\text{C}$) into mixed juice clarifiers, cleaving internal $\alpha\text{-(1}\to\text{6)}$ linkages into low-viscosity isomalto-oligosaccharides, restoring normal cubic crystal habit and sucrose crystallization velocity.""",

        "unit-4-cement-and-lime": r"""

### University Honors Industrial Case Study: Alkali-Silica Reaction (ASR) Gel Swelling & Concrete Destruction
The Alkali-Silica Reaction (ASR), often called "concrete cancer," is a destructive chemical reaction between reactive amorphous silica aggregates (chert, opal, strained quartz) and high-alkali cement pore fluids ($\text{pH } > 13.5$, rich in $\text{Na}^+$ and $\text{K}^+$):
$$\equiv \text{Si-O-Si} \equiv \ + \ 2\text{OH}^- \longrightarrow 2\,(\equiv \text{Si-O}^-) + \text{H}_2\text{O}$$
$$\equiv \text{Si-O}^- + \text{Na}^+ / \text{K}^+ + n\text{H}_2\text{O} \longrightarrow \text{Alkali-Silica Hydrated Gel}$$
- **Osmotic Swelling Pressure**: The hygroscopic alkali silicate gel absorbs surrounding moisture from capillaries, generating massive internal hydrostatic swelling pressures ($> 4 - 10\text{ MPa}$).
- **Failure Mode**: Because concrete has a low tensile strength ($\sim 3 - 4\text{ MPa}$), this osmotic expansion exceeds the tensile yield limit, producing characteristic map cracking, joint misalignment, and aggregate pop-outs.
- **Prevention**: Limiting total equivalent alkali in cement to $< 0.60\text{ wt}\%\text{ Na}_2\text{O}_{\text{equiv}}$ ($\% \text{Na}_2\text{O} + 0.658\% \text{K}_2\text{O}$) and blending pozzolans (fly ash, silica fume, lithium nitrate admixtures).""",

        "unit-5-soaps-and-detergents": r"""

### University Honors Industrial Case Study: Linear Alkylbenzene Sulfonate (LAS) Micellar Dynamic Solubilization
In laundry washing, detergency occurs via three distinct physicochemical mechanisms:
1. **Roll-up Mechanism**: Surfactant molecules adsorb at the liquid-oil and liquid-fiber interfaces, increasing the contact angle of oily droplets ($\theta > 90^\circ$). Interfacial tension forces detach the droplet as an intact sphere into the aqueous liquor.
2. **Solubilization inside Micellar Cores**: Above the Critical Micelle Concentration (CMC), non-polar hydrophobic soil components (squalene, paraffin hydrocarbons) partition into the hydrocarbon core of spherical and cylindrical LAS micelles ($2 - 5\text{ nm}$ diameter).
3. **Electrostatic Double-Layer Dispersion**: Negatively charged sulfonate headgroups ($-\text{SO}_3^-$) coat detached soil particles, generating high negative zeta potentials ($\zeta \approx -50\text{ mV}$). Strong electrostatic repulsion prevents redeposition onto similarly charged cotton fabric surfaces.""",

        "unit-6-pulp-and-paper": r"""

### University Honors Industrial Case Study: Smelt-Water Explosions in Recovery Boiler Dissolving Tanks
A catastrophic physical hazard in Kraft recovery boiler operation is the **Smelt-Water Explosion**:
- **Explosion Physics**: Molten smelt discharged at $850^\circ\text{C}$ consists of liquid ionic salts ($\text{Na}_2\text{S} + \text{Na}_2\text{CO}_3$). If a water boiler tube ruptures above the hearth, liquid water pours into the pool of molten smelt.
- **Rapid Phase Transition (RPT)**: Because smelt temperature is far above the superheat limit of water ($300^\circ\text{C}$), water is trapped beneath the heavy liquid smelt. Violent nucleate boiling transitions into an explosive vapor explosion:
  $$1\text{ liter of liquid water flashes into } 1,600\text{ liters of steam in microseconds!}$$
  The resulting shock wave generates peak pressures exceeding $100\text{ bar}$, capable of ripping the heavy steel boiler shell apart.
- **Mitigation**: Automated Emergency Drain Systems (EDS), high-energy steam shattering jets at smelt spouts, and acoustic leak detectors on furnace boiler tubes.""",

        "unit-7-glass-and-ceramics": r"""

### University Honors Industrial Case Study: Nickel Sulfide (NiS) Spontaneous Toughened Glass Fracture
Architectural thermally toughened (tempered) glass panels occasionally suffer spontaneous catastrophic shattering years after installation:
- **Phase Inversion Thermodynamics**: Raw glass batch containing trace nickel ($< 1\text{ ppb}$) and sulfur can form microscopic nickel sulfide inclusions ($\text{NiS}$, $50 - 500\,\mu\text{m}$).
- At melting temperatures ($> 1400^\circ\text{C}$), $\text{NiS}$ exists as the high-temperature hexagonal $\alpha\text{-phase}$.
- During rapid air quenching of toughening, $\alpha\text{-NiS}$ is frozen in a metastable state at room temperature.
- Over years in ambient service, metastable $\alpha\text{-NiS}$ slowly transforms into the stable rhombohedral $\beta\text{-NiS}$:
  $$\alpha\text{-NiS} \longrightarrow \beta\text{-NiS} \quad (\Delta V = +4.0\% \text{ volumetric expansion!})$$
- Because the core of toughened glass is under intense residual tensile stress ($> 100\text{ MPa}$), this $4\%$ expansion acts as an internal crack wedging source, initiating instantaneous catastrophic branching fractures across the entire glass sheet.
- **Heat Soak Testing (EN 14179)**: Glass panels are held at $290^\circ\text{C}$ for $2 - 4\text{ hours}$ in an oven to deliberately induce conversion and shatter defective panels before installation.""",

        "unit-8-caustic-chlorine": r"""

### University Honors Industrial Case Study: Wet Chlorine Crevice Corrosion in Titanium Exchangers
Titanium is the universal metal of choice for handling wet chlorine gas because a stable, self-healing rutile passive oxide film ($\text{TiO}_2$) forms instantaneously in the presence of trace moisture ($> 0.5\text{ wt}\%\text{ H}_2\text{O}$):
$$\text{Ti} + 2\text{H}_2\text{O} \longrightarrow \text{TiO}_2 + 4\text{H}^+ + 4e^-$$
- **The Dry Chlorine Fire Hazard**: In bone-dry chlorine gas ($< 20\text{ ppm H}_2\text{O}$), the protective oxide film cannot self-repair. If mechanical scratching exposes virgin titanium metal, a violent, auto-igniting exothermic chlorination fire erupts:
  $$\text{Ti}(s) + 2\text{Cl}_2(g) \longrightarrow \text{TiCl}_4(l) \quad (\Delta H = -804\text{ kJ/mol})$$
  The titanium metal burns vigorously in dry chlorine at room temperature, releasing dense white clouds of boiling $\text{TiCl}_4$.
- **Crevice Corrosion**: In gasket joints of plate heat exchangers where brine flow stagnates and temperature exceeds $75^\circ\text{C}$, localized acid buildup ($\text{pH} < 1$) breaks down passivity. Modern chlor-alkali exchangers specify palladium-stabilized titanium (ASTM Grade 7, $\text{Ti}-0.15\%\text{Pd}$) to prevent crevice initiation.""",

        "unit-9-petroleum-and-fuels": r"""

### University Honors Industrial Case Study: Refractory Thiophenic Heterocycle Steric Hindrance in Ultra-Deep HDS
To achieve Euro VI / Tier 3 specifications ($< 10\text{ ppm sulfur}$), refineries must eliminate 4,6-dimethyldibenzothiophene (4,6-DMDBT):
- **Steric Hindrance Barrier**: The two bulky methyl groups ($\text{-CH}_3$) at positions 4 and 6 project directly adjacent to the heterocyclic sulfur atom, sterically shielding it from direct perpendicular coordination onto the active metallic Mo/W edge sites of the $\text{Co-Mo-S}$ catalyst crystallites.
- **Alternative Hydrogenation Pathway**:
  Rather than direct desulfurization (DDS), 4,6-DMDBT must follow the much slower hydrogenation (HYD) pathway:
  1. Complete saturation of one adjacent benzene ring to form 4,6-dimethyl-tetrahydrodibenzothiophene.
  2. The non-planar, buckled cyclohexenyl ring pulls the methyl groups out of the plane, relieving steric strain.
  3. The sulfur atom coordinates to the catalyst site and undergoes $\text{C-S}$ cleavage.
- **Industrial Response**: Modern ultra-deep HDS catalysts utilize highly stacked $\text{Ni-Mo-W}$ clusters on wide-pore mesoporous supports operating at elevated hydrogen pressures ($60 - 80\text{ bar}$) with high hydrogen-to-oil treat gas ratios.""",

        "unit-10-metallurgy-and-steel": r"""

### University Honors Industrial Case Study: Hydrogen-Induced Delay Cracking (HIC) & Ladle RH Degassing
In ultra-high-strength structural steels (yield strength $> 800 - 1,000\text{ MPa}$), microscopic atomic hydrogen dissolved during steelmaking induces delayed, catastrophic brittle failure:
- **Hydrogen Trapping & Recombination**: In the liquid state ($1600^\circ\text{C}$), molten steel dissolves up to $6 - 8\text{ ppm}$ of atomic hydrogen ($[\text{H}]$). During cooling and solidification, hydrogen solubility plummets by an order of magnitude.
- Supersaturated interstitial hydrogen diffuses to micro-voids, non-metallic inclusions ($\text{Al}_2\text{O}_3, \text{MnS}$), and grain boundary dislocations, recombining into molecular hydrogen gas ($\text{H}_2$):
  $$2[\text{H}] \longrightarrow \text{H}_2(g)$$
- The trapped molecular gas develops enormous internal hydrostatic pressures ($> 1,000 - 5,000\text{ MPa}$), nucleating microcracks and internal "flakes" that fracture under low external service stresses.
- **Ruhrstahl-Heraeus (RH) Vacuum Circulation Degasser**:
  Molten steel is drawn through two refractory snorkels into a vacuum chamber ($p < 1.0\text{ mbar}$). Argon gas lift bubbles circulate the steel at $120 - 150\text{ tons/min}$. Under deep vacuum, Sieverts' law drives hydrogen desorption, stripping dissolved hydrogen down to **$< 1.0 - 1.2\text{ ppm}$** in under $15 - 20\text{ minutes}$."""
    }

    for u in units:
        uid = u["id"]
        if uid in monographs:
            # Append monograph to the last section (Section 8) of the unit
            if len(u["sections"]) >= 8:
                sec = u["sections"][-1]
                if "University Honors Industrial Case Study" not in sec["content"]:
                    sec["content"] += monographs[uid]

    return units
