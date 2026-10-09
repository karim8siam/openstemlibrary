# -*- coding: utf-8 -*-
"""
build_industrial_units_1_2_3.py
Builds Units 1, 2, and 3 for Industrial Chemistry (#48).
7 comprehensive sections & 7 solved problems per unit.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def get_units_1_2_3():
    units = [
        {
            "id": "unit-1-textiles-and-dyes",
            "unitNumber": 1,
            "title": "Unit 1: Textiles and Dyes Industries: Fiber Science, Spinning & Color Chemistry",
            "leadSummary": "Exhaustive chemical and engineering treatise on natural and synthetic textile fibers, regenerated cellulosic rayons (viscose, cuprammonium, acetate), step-growth polycondensation (nylons, PET dacron), polymer rheology and industrial melt/wet/dry spinning, and color chemistry principles (chromophores, auxochromes, azo dye synthesis, and industrial dyeing mechanics).",
            "simulations": ["sim_ind_textile_viscose_spinning"],
            "sections": [
                {
                    "id": "sec-1-1",
                    "secNumber": "1.1",
                    "title": "Classification of Textile Fibers: Natural vs Synthetic Morphologies & Crystallinity",
                    "content": r"""Textile fibers represent high-aspect-ratio polymeric structures possessing a length-to-diameter ratio exceeding $1000:1$, coupled with sufficient tensile strength ($\ge 1.5\text{ cN/dtex}$), flexibility, thermal stability, and dye affinity to be converted into yarns and woven fabrics. 

### Fundamental Classification Hierarchy
All textile fibers are partitioned into two principal architectural classes:
1. **Natural Fibers**: Polymers produced directly by biological organisms:
   - *Cellulosic (Vegetable)*: Cotton, flax, hemp, jute, ramie. Primary repeat unit is $\beta\text{-D-glucopyranose}$ linked via $\beta\text{-(1}\to\text{4)-glycosidic}$ bonds.
   - *Proteinaceous (Animal)*: Wool, cashmere, alpaca (keratin polypeptides stabilized by cystine disulfide bridges); cultivated mulberry and wild tussah silk (fibroin filaments bonded by $\beta$-pleated sheet hydrogen bonds).
   - *Mineral*: Asbestos (chrysotile serpentine silicate fibrils, largely phased out due to pulmonary mesothelioma toxicity).
2. **Man-Made (Manufactured) Fibers**:
   - *Regenerated Cellulosics*: Viscose rayon, high wet modulus (modal) rayon, lyocell (N-methylmorpholine N-oxide direct solvent route), cuprammonium rayon, cellulose acetate.
   - *Synthetic Polymers*: Aliphatic polyamides (Nylon 6, Nylon 6,6), aromatic polyamides (Aramids: Kevlar, Nomex), polyesters (PET, PBT, polytrimethylene terephthalate), polyolefins (polypropylene, ultra-high-molecular-weight polyethylene), polyacrylonitrile (acrylics, modacrylics), polyurethanes (spandex/elastane).

```
                            TEXTILE FIBER TAXONOMY
                                      │
         ┌────────────────────────────┴────────────────────────────┐
         ▼                                                         ▼
   NATURAL FIBERS                                          MANUFACTURED FIBERS
   ├── Vegetable (Cellulose)                               ├── Regenerated
   │   ├── Seed: Cotton, Kapok                             │   ├── Viscose Rayon (Xanthate)
   │   ├── Bast: Flax, Hemp, Jute                          │   ├── Cuprammonium Rayon
   │   └── Leaf: Sisal, Abaca                              │   ├── Lyocell (NMMO Direct)
   ├── Animal (Protein)                                    │   └── Cellulose Acetate (Esters)
   │   ├── Hair: Wool, Mohair, Cashmere                    └── Synthetic Polymeric
   │   └── Secretion: Mulberry Silk, Tussah                    ├── Polyamides: Nylon-6, Nylon-6,6
   └── Mineral: Asbestos (Silicates)                           ├── Polyesters: PET (Dacron)
                                                               ├── Polyacrylics: PAN / Modacrylic
                                                               └── Polyolefins: PP, UHMWPE
```

### Macromolecular Orientation, Crystallinity & Tenacity
The macroscopic mechanical properties of a textile fiber depend on three molecular parameters:
1. **Degree of Polymerization ($\overline{DP}_n$)**: The number of repeating monomeric residues per polymer chain:
   $$\overline{DP}_n = \frac{\bar{M}_n}{M_0}$$
   For native cotton cellulose, $\overline{DP}_n \approx 9,000 - 15,000$, whereas for regenerated viscose rayon, acid/alkali degradation reduces $\overline{DP}_n$ to $250 - 450$. Synthetic PET fiber requires $\overline{DP}_n \approx 100 - 150$ ($\bar{M}_n \approx 20,000 - 30,000\text{ g/mol}$) to provide adequate melt spinability without excessive melt fracture.
2. **Fractional Degree of Crystallinity ($X_c$)**: Determined by wide-angle X-ray diffraction (WAXD) or differential scanning calorimetry (DSC):
   $$X_c = \frac{\Delta H_m}{\Delta H_m^\circ} \times 100\%$$
   where $\Delta H_m$ is the measured heat of fusion and $\Delta H_m^\circ$ is the enthalpy of fusion for a $100\%$ crystalline reference crystal ($\Delta H_m^\circ = 140\text{ J/g}$ for PET). Highly crystalline domains provide modulus, tensile yield strength, and chemical resistance; amorphous regions facilitate dye penetration, moisture regain, and elastomeric flexibility.
3. **Hermans Orientation Factor ($f_c$)**: Quantifies the alignment of polymer chain backbones along the longitudinal fiber axis ($z$-axis):
   $$f_c = \frac{3\langle \cos^2 \theta \rangle - 1}{2}$$
   where $\theta$ is the angle between the polymer crystallographic $c$-axis and the fiber drawing axis. Unoriented spun filaments exhibit $f_c \approx 0$, while post-spinning hot drawing increases $f_c \to 0.90 - 0.98$, elevating tenacity from $2.0\text{ cN/dtex}$ to $> 8.5\text{ cN/dtex}$ for industrial tire-cord filaments."""
                },
                {
                    "id": "sec-1-2",
                    "secNumber": "1.2",
                    "title": "Chemistry of Natural Fibers: Cotton Cellulose, Wool Keratin & Silk Fibroin",
                    "content": r"""Natural fibers exhibit complex hierarchical biological microarchitectures developed through evolutionary optimization.

### 1. Cotton Cellulose Chemistry
Cotton lint comprises $88 - 96\%$ $\alpha$-cellulose, $1.0 - 1.5\%$ proteins, $0.4 - 1.0\%$ pectins, $0.5\%$ waxes, and $1.0\%$ inorganic ash.
The basic chemical repeating unit is cellobiose, composed of two anhydroglucose units (AGUs) coupled through $\beta\text{-(1}\to\text{4)}$-glucosidic oxygen bridges:
$$\text{--[C}_6\text{H}_{10}\text{O}_5\text{]}_n\text{--} \quad \text{with } n = 2,000 - 10,000$$

Every AGU contains three free hydroxyl functionalities: one primary hydroxyl at position $\text{C-6}$ and two secondary hydroxyls at positions $\text{C-2}$ and $\text{C-3}$:
$$\text{Cellulose Unit: } [-\text{C}_6\text{H}_7\text{O}_2(\text{OH})_3-]_n$$
Extensive intramolecular hydrogen bonding ($\text{O-3-H}\cdots\text{O-5'}$ of the adjacent ring) confers rigidity to the pyranose backbone, while intermolecular hydrogen bonding ($\text{O-6-H}\cdots\text{O-3'}$ in the Cellulose I lattice) binds neighboring chains into elementary microfibrils (diameter $\approx 3.5\text{ nm}$). Consequently, native cellulose does not melt; upon heating, it undergoes thermal pyrolysis and levoglucosan formation at $T > 300^\circ\text{C}$.

#### Mercerization Reaction
Treatment of raw cotton with cold concentrated aqueous sodium hydroxide ($18 - 24\text{ wt}\%\text{ NaOH}$, $5 - 6\text{ M}$ at $15 - 20^\circ\text{C}$) under mechanical tension induces profound structural changes:
$$\text{Cell-OH} + \text{NaOH} \rightleftharpoons \text{Cell-O}^-\text{Na}^+ + \text{H}_2\text{O}$$
The caustic solution swells the microfibrillar cell wall, collapsing the lumen and untwisting natural convolutions. Upon washing and acid neutralization, native Cellulose $\text{I}_\beta$ (monoclinic, parallel chains) rearranges irreversibly into the thermodynamically stable Cellulose $\text{II}$ allomorph (monoclinic, antiparallel chains). Mercerized cotton exhibits increased tensile strength ($+15 - 25\%$), heightened luster, and increased dye sorption.

### 2. Wool Keratin Chemistry
Wool is an animal epidermal protein fiber structured from complex $\alpha$-keratin polypeptide chains:
- **Primary Structure**: Polypeptide chains comprising 18 distinct amino acids with an average molecular weight of $50,000\text{ g/mol}$. Notable residues include cystine ($11 - 12\text{ wt}\%$, providing covalent disulfide crosslinks), glutamic acid, aspartic acid, arginine, and lysine.
- **Secondary Structure**: The polypeptide backbone coils into a right-handed $\alpha$-helix stabilized by intrachain hydrogen bonds between $\text{C=O}$ of peptide residue $i$ and $\text{N-H}$ of residue $i+4$ (spacing $0.54\text{ nm}$ per turn).
- **Disulfide Crosslinking**:
  $$\text{R}_1\text{-CH}_2\text{-S-S-CH}_2\text{-R}_2$$
  These covalent cystine crosslinks confer elasticity, insolubility in neutral solvents, and reversible mechanical extension. Under axial tensile strain in moist steam, wool stretches up to $100\%$ by uncoiling from the folded $\alpha$-keratin state into the extended $\beta$-keratin conformation; upon release, the disulfide bridges pull the structure back into the $\alpha$-helical ground state.

### 3. Silk Fibroin Chemistry
Cultivated *Bombyx mori* silk consists of two fibroin structural filaments encapsulated in a soluble protective proteinaceous gum called sericin ($20 - 30\text{ wt}\%$), which is removed by alkaline scouring (degumming with soap/soda ash at $95^\circ\text{C}$).
Fibroin is a non-crosslinked protein characterized by a repeating hexapeptide sequence:
$$[-\text{Gly-Ala-Gly-Ala-Gly-Ser}-]_n$$
Because glycine ($R = \text{H}$) comprises $45\%$ and alanine ($R = \text{CH}_3$) comprises $30\%$ of total residues, the absence of bulky side chains allows the anti-parallel $\beta$-pleated sheets to pack with an intersheet distance of only $0.35 - 0.57\text{ nm}$. This crystalline packing accounts for silk's high tensile strength ($4 - 5\text{ cN/dtex}$) and soft hand."""
                },
                {
                    "id": "sec-1-3",
                    "secNumber": "1.3",
                    "title": "Regenerated Cellulose Rayons: Cuprammonium, Acetate & Viscose Systems",
                    "content": r"""Because cellulose decomposes pyrolytically prior to melting, it cannot be melt spun. Regenerated cellulosic fibers require chemical derivatization into soluble complexes or covalent derivatives, followed by extrusion and chemical regeneration.

### 1. The Viscose Rayon Process (Cross, Bevan & Beadle, 1892)
The viscose route is the dominant industrial methodology for producing artificial regenerated cellulose fiber.

#### Process Chemistry Cascade
1. **Alkali Cellulose (Mercerization)**: Dissolving wood pulp ($90 - 95\%$ $\alpha$-cellulose) is steeped in $17.5 - 19.0\text{ wt}\%\text{ NaOH}$ at $45 - 55^\circ\text{C}$ to form sodium cellulosate:
   $$\text{Cell-OH} + \text{NaOH} \to \text{Cell-O}^-\text{Na}^+ + \text{H}_2\text{O}$$
2. **Aging (Controlled Depolymerization)**: The pressed alkali cellulose crumbs are aged in temperature-controlled drums ($25 - 30^\circ\text{C}$) for $20 - 40\text{ hours}$. Atmospheric oxygen oxidatively cleaves glucosidic bonds via free-radical hydroperoxide intermediates, lowering $\overline{DP}$ from $\sim 1,000$ to $300 - 350$ to achieve the desired solution viscosity.
3. **Xanthation (Xanthogenation)**: Aged alkali cellulose reacts with carbon disulfide ($30 - 35\text{ wt}\%\text{ CS}_2$ based on dry cellulose) in a vacuum baratte at $25 - 32^\circ\text{C}$ for $90 - 150\text{ minutes}$:
   $$\text{Cell-O}^-\text{Na}^+ + \text{CS}_2 \to \text{Cell-O-C}(=\text{S})-\text{S}^-\text{Na}^+ \quad (\text{Sodium Cellulose Xanthate})$$
   The degree of substitution ($DS$) reaches $0.5 - 0.6$ xanthate groups per AGU. The crumbs turn bright orange-yellow.
4. **Dissolution & Viscose Dope Preparation**: The xanthate crumbs dissolve in dilute aqueous caustic ($1.2 - 1.5\text{ M NaOH}$) under vigorous agitation at $15 - 18^\circ\text{C}$, forming a golden, viscous colloidal solution:
   $$\text{Viscose Dope: } 7.5 - 9.0\text{ wt}\% \text{ Cellulose}, \; 5.5 - 6.5\text{ wt}\% \text{ NaOH}$$
5. **Ripening (De-xanthation & Re-distribution)**: The filtered and de-aerated viscose solution is aged for $24 - 48\text{ hours}$ at $18 - 20^\circ\text{C}$. Spontaneous hydrolysis cleaves secondary xanthate groups while remaining primary $\text{C-6}$ xanthates redistribute:
   $$\text{Cell-O-CSSNa} + \text{H}_2\text{O} \to \text{Cell-OH} + \text{CS}_2 + \text{NaOH}$$
   Ripening reduces the Hottenroth salt index from $18 - 20$ to $10 - 12$, rendering the dope sensitive to acid coagulation.
6. **Wet Spinning & Coagulation (Müller Spin Bath)**: Viscose is metered by precision gear pumps through platinum-gold spinneret orifices ($1,000 - 10,000$ holes, diameter $50 - 70\,\mu\text{m}$) into an aqueous acid bath maintained at $45 - 50^\circ\text{C}$:
   - $8 - 12\text{ wt}\%\text{ H}_2\text{SO}_4$ (neutralizes $\text{NaOH}$ and regenerates cellulose).
   - $15 - 22\text{ wt}\%\text{ Na}_2\text{SO}_4$ (osmotic dehydrating and coagulating salt).
   - $1.0 - 2.5\text{ wt}\%\text{ ZnSO}_4$ (crosslinks surface chains as zinc cellulose xanthate).
   $$\text{Cell-O-CSSNa} + \frac{1}{2}\text{H}_2\text{SO}_4 \to \text{Cell-OH} + \text{CS}_2\uparrow + \frac{1}{2}\text{Na}_2\text{SO}_4$$
   $$\text{ZnSO}_4 + 2\text{Cell-O-CSSNa} \to (\text{Cell-O-CSS})_2\text{Zn} + \text{Na}_2\text{SO}_4$$
   The insoluble zinc xanthate complex retards core regeneration, producing a dense outer skin and a serrated (crenulated) filament cross-section.

```
                           THE INDUSTRIAL VISCOSE CASCADE
 Dissolving Wood Pulp
         │
         ▼ (18% NaOH Steeping)
 Alkali Cellulose [Cell-O⁻Na⁺]
         │
         ▼ (Air Oxidation Aging: DP 1000 ──► 320)
 Aged Crumb
         │
         ▼ (+ 32 wt% CS₂ in Vacuum Baratte)
 Cellulose Xanthate [Cell-O-CS-S⁻Na⁺] (Orange Crumb)
         │
         ▼ (+ Dilute NaOH Dissolution)
 Viscose Dope (7-8% Cellulose, 6% NaOH)
         │
         ▼ (Ripening, De-aeration, Filtration)
 Spin Dope Ready for Extrusion
         │
         ▼ (Müller Acid Bath: H₂SO₄ + Na₂SO₄ + ZnSO₄)
 Regenerated Viscose Rayon Filament + CS₂↑ + Na₂SO₄
```

### 2. Cuprammonium Rayon (Bemberg Process)
Cuprammonium rayon exploits the solubility of cellulose in Schweizer's reagent—an aqueous solution of cupric hydroxide in concentrated ammonia:
$$[\text{Cu}(\text{NH}_3)_4](\text{OH})_2$$
Cellulose forms a blue, soluble coordination complex via chelation of the $\text{C-2}$ and $\text{C-3}$ diol oxygens:
$$\text{Cell-(OH)}_2 + [\text{Cu}(\text{NH}_3)_4]^{2+} + 2\text{OH}^- \rightleftharpoons [(\text{Cell-O}_2)\text{Cu}(\text{NH}_3)_2]^{2-} + 2\text{NH}_3 + 2\text{H}_2\text{O}$$
The viscous solution is extruded downward into a vertical water funnel (stretch spinning), where mild water washing removes ammonia, allowing high draw ratios ($> 300\%$) prior to coagulation in dilute sulfuric acid ($5\text{ wt}\%\text{ H}_2\text{SO}_4$). Cupro fibers are round in cross-section and possess low denier ($< 1.0\text{ dtex}$).

### 3. Cellulose Acetate Fiber
Cellulose acetate is a semi-synthetic ester fiber. Purified cotton linters or chemical wood pulp are activated with glacial acetic acid and treated with acetic anhydride in the presence of sulfuric acid catalyst:
$$\text{Cell-(OH)}_3 + 3(\text{CH}_3\text{CO})_2\text{O} \xrightarrow{\text{H}_2\text{SO}_4} \text{Cell-(OCOCH}_3)_3 + 3\text{CH}_3\text{COOH}$$
This yields primary cellulose triacetate ($DS \approx 2.9 - 3.0$). Because triacetate dissolves only in chlorinated hydrocarbons (dichloromethane), controlled partial hydrolysis with water at $60 - 70^\circ\text{C}$ back-hydrolyzes the ester to **Secondary Cellulose Acetate** ($DS \approx 2.4 - 2.5$, acetyl value $54 - 56\%$). Secondary acetate is soluble in acetone and is converted into fibers by **dry spinning**, where warm air ($60 - 80^\circ\text{C}$) evaporates the acetone solvent."""
                },
                {
                    "id": "sec-1-4",
                    "secNumber": "1.4",
                    "title": "Synthetic Polyamides: Nylon-6 and Nylon-6,6 Synthesis & Polycondensation Kinetics",
                    "content": r"""Aliphatic polyamides are engineering polymers characterized by repeating amide linkages ($-\text{CO}-\text{NH}-$) in the main macromolecular chain.

### 1. Nylon-6,6 (Wallace Carothers, DuPont, 1935)
Nylon-6,6 is synthesized by stoichiometric step-growth polycondensation of hexamethylenediamine (HMDA, 1,6-diaminohexane) and adipic acid (hexanedioic acid).

#### The Nylon Salt Stage
Direct bulk copolymerization of free diamine and dicarboxylic acid suffers from stoichiometry mismatch caused by diamine volatility. This is solved by preparing crystalline **Nylon Salt (hexamethylenediammonium adipate)**:
$$\text{H}_2\text{N-(CH}_2)_6\text{-NH}_2 + \text{HOOC-(CH}_2)_4\text{-COOH} \xrightarrow{\text{Methanol/Water}} [\text{H}_3\stackrel{+}{\text{N}}\text{-(CH}_2)_6\text{-\stackrel{+}{N}H}_3][\bar{\text{O}}\text{OC-(CH}_2)_4\text{-COO}^-]$$
The $1:1$ stoichiometric salt crystallizes from aqueous methanol at pH $7.62$ ($25^\circ\text{C}$), ensuring stoichiometric balance between amine and carboxyl functional groups to within $\pm 0.01\%$.

#### Autoclave Polycondensation
A $60\text{ wt}\%$ aqueous slurry of nylon salt is charged into a stainless steel autoclave under nitrogen:
1. **Evaporation**: Heated to $210 - 220^\circ\text{C}$ at $1.7\text{ MPa}$ ($250\text{ psi}$) to distill off free solvent water.
2. **Pressure Polymerization**: Temperature increases to $275 - 280^\circ\text{C}$ while maintaining $1.7\text{ MPa}$ to allow oligomerization without diamine escape:
   $$n[\text{H}_3\text{N-(CH}_2)_6\text{-NH}_3]^{2+}[\text{OOC-(CH}_2)_4\text{-COO}]^{2-} \rightleftharpoons \text{H-}[-\text{NH-(CH}_2)_6\text{-NH-CO-(CH}_2)_4\text{-CO}-]_n\text{-OH} + (2n-1)\text{H}_2\text{O}$$
3. **Depressurization & Vacuum Finishing**: Pressure is slowly bled down to atmospheric pressure and held under high vacuum ($10 - 20\text{ kPa}$) at $280^\circ\text{C}$ to pull the reversible equilibrium toward high molecular weight ($\bar{M}_n \approx 15,000 - 22,000\text{ g/mol}$, $\overline{DP}_n \approx 70 - 100$). Monofunctional acetic acid ($0.5 - 1.0\text{ mol}\%$) is added as a chain-terminating stabilizer to cap amine ends and prevent post-spinning viscosity drift.

### 2. Nylon-6 (Paul Schlack, IG Farben, 1938)
Nylon-6 is synthesized by the ring-opening polymerization (ROP) of $\epsilon$-caprolactam in the presence of $2 - 5\text{ wt}\%$ water catalyst at $250 - 270^\circ\text{C}$ in a vertical continuous tubular reactor (VK-Rohr).

The hydrolytic polymerization mechanism comprises three equilibrium stages:
1. **Ring Hydrolysis**:
   $$\text{HN-(CH}_2)_5\text{-CO} + \text{H}_2\text{O} \rightleftharpoons \text{H}_2\text{N-(CH}_2)_5\text{-COOH} \quad (\text{6-aminocaproic acid})$$
2. **Step-Growth Polycondensation**:
   $$\text{H-(NH-(CH}_2)_5\text{-CO)}_n\text{-OH} + \text{H-(NH-(CH}_2)_5\text{-CO)}_m\text{-OH} \rightleftharpoons \text{H-(NH-(CH}_2)_5\text{-CO)}_{n+m}\text{-OH} + \text{H}_2\text{O}$$
3. **Polyaddition (Chain Growth Addition of Monomer to Amine Ends)**:
   $$\text{--NH}_2 + \text{HN-(CH}_2)_5\text{-CO} \rightleftharpoons \text{--NH-CO-(CH}_2)_5\text{-NH}_2$$
At chemical equilibrium ($260^\circ\text{C}$), the molten polymer contains $90\%$ nylon-6 and $10\%$ residual monomeric caprolactam and cyclic oligomers. The molten polymer is extruded into strands, water-quenched, pelletized, and vacuum-washed with hot water at $95^\circ\text{C}$ to extract residual monomers before drying to water content $< 0.05\text{ wt}\%$.

### 3. Step-Growth Polycondensation Kinetics & The Carothers Equation
Under unassisted thermal condensation, the rate of carboxyl group disappearance follows second-order kinetics:
$$-\frac{d[\text{COOH}]}{dt} = k [\text{COOH}][\text{NH}_2]$$
For an equimolar functional system ($[\text{COOH}] = [\text{NH}_2] = c$):
$$-\frac{dc}{dt} = k c^2 \implies \frac{1}{c} - \frac{1}{c_0} = k t$$
Defining functional group fractional conversion $p = \frac{c_0 - c}{c_0}$:
$$c = c_0 (1 - p) \implies \frac{1}{c_0(1 - p)} - \frac{1}{c_0} = k t \implies \frac{1}{1 - p} - 1 = c_0 k t$$
The number-average degree of polymerization $\overline{DP}_n$ is given by the **Carothers Equation**:
$$\overline{DP}_n = \frac{N_0}{N} = \frac{c_0}{c} = \frac{1}{1 - p}$$
To obtain high-tenacity nylon fiber ($\overline{DP}_n \ge 80$), the reaction conversion must reach:
$$p = 1 - \frac{1}{80} = 1 - 0.0125 = 0.9875 \quad (\ge 98.75\%)$$
This illustrates why vacuum removal of the condensation by-product ($\text{H}_2\text{O}$) is necessary to drive the reversible equilibrium forward."""
                },
                {
                    "id": "sec-1-5",
                    "secNumber": "1.5",
                    "title": "Polyester Chemistry: Polyethylene Terephthalate (PET/Dacron) & Transesterification",
                    "content": r"""Polyethylene terephthalate (PET), commercialized under trade names Dacron and Terylene, represents the highest volume synthetic fiber worldwide.

### Industrial Synthesis Pathways
Industrial PET manufacture proceeds by either transesterification of dimethyl terephthalate (DMT) or direct esterification of purified terephthalic acid (PTA).

```
                        INDUSTRIAL ROUTES TO PET RESIN
                                      │
         ┌────────────────────────────┴────────────────────────────┐
         ▼                                                         ▼
 DMT ROUTE (Ester Interchange)                             PTA ROUTE (Direct Esterification)
 Dimethyl Terephthalate + Excess Ethylene Glycol            Pure Terephthalic Acid + Ethylene Glycol
         │ (Zn(OAc)₂ catalyst, 160-210°C)                          │ (Self-catalyzed / 240-260°C)
         ▼ (Methanol Distillation By-Product)                      ▼ (Water Distillation By-Product)
 Bis(2-hydroxyethyl) Terephthalate (BHET)                  Bis(2-hydroxyethyl) Terephthalate (BHET)
         └────────────────────────────┬────────────────────────────┘
                                      ▼
                        MELT POLYCONDENSATION REACTOR
                         Catalyst: Sb₂O₃ (250-350 ppm)
                         Temperature: 280 - 290°C
                         High Vacuum: < 1 mbar (< 100 Pa)
                                      │
                                      ▼ (Ethylene Glycol Distillation)
                     High-Tenacity PET Fiber Polymer Resin
```

#### 1. The DMT Route (Ester Interchange)
Dimethyl terephthalate (DMT) reacts with excess ethylene glycol (EG, molar ratio $1:2.1 - 1:2.4$) in the presence of zinc acetate or manganese acetate catalysts ($50 - 100\text{ ppm}$) at $160 - 210^\circ\text{C}$:
$$\text{CH}_3\text{OOC}-\text{C}_6\text{H}_4-\text{COOCH}_3 + 2\text{HOCH}_2\text{CH}_2\text{OH} \rightleftharpoons \text{BHET} + 2\text{CH}_3\text{OH}\uparrow$$
Methanol is continuously removed via fractionating columns to drive the transesterification to completion ($> 98\%$), yielding the monomer **Bis(2-hydroxyethyl) terephthalate (BHET)**.

#### 2. The Direct PTA Route
Purified terephthalic acid (PTA) is slurried directly with ethylene glycol (EG/PTA molar ratio $1:1.15 - 1:1.3$) at $240 - 260^\circ\text{C}$ under $0.3 - 0.5\text{ MPa}$ gauge pressure:
$$\text{HOOC}-\text{C}_6\text{H}_4-\text{COOH} + 2\text{HOCH}_2\text{CH}_2\text{OH} \rightleftharpoons \text{BHET} + 2\text{H}_2\text{O}\uparrow$$
Water boils off overhead. The PTA process is faster and requires lower glycol ratios, eliminating methanol handling.

#### 3. Melt Polycondensation
Monomeric BHET is transferred to finishing polycondensation reactors operating at $280 - 290^\circ\text{C}$ under high vacuum ($< 1\text{ mbar}$, $< 100\text{ Pa}$) in the presence of antimony trioxide ($\text{Sb}_2\text{O}_3$, $250 - 350\text{ ppm}$) or titanium alkoxide catalysts:
$$n\text{BHET} \rightleftharpoons \text{HO-}[-\text{CH}_2\text{CH}_2\text{O-CO}-\text{C}_6\text{H}_4-\text{CO-}]_n\text{-OCH}_2\text{CH}_2\text{OH} + (n-1)\text{HOCH}_2\text{CH}_2\text{OH}\uparrow$$
Ethylene glycol is distilled off to drive the equilibrium toward an intrinsic viscosity $[\eta] = 0.60 - 0.72\text{ dL/g}$ ($\bar{M}_n \approx 18,000 - 24,000\text{ g/mol}$).

### Degradation Side Reactions
At $T > 280^\circ\text{C}$, thermal ester cleavage produces vinyl ester and carboxyl end-groups via a six-membered cyclic transition state:
$$\text{--C}_6\text{H}_4\text{-COO-CH}_2\text{-CH}_2\text{-OOC-C}_6\text{H}_4\text{--} \xrightarrow{\Delta} \text{--C}_6\text{H}_4\text{-COOH} + \text{CH}_2=\text{CH-OOC-C}_6\text{H}_4\text{--}$$
The vinyl ester tautomerizes to acetaldehyde ($\text{CH}_3\text{CHO}$), an undesirable volatile impurity that must be held $< 1\text{ ppm}$ in food-grade packaging. Acidic carboxyl ends ($\text{--COOH}$) catalyze further hydrolytic degradation. Concurrently, etherification produces diethylene glycol ($\text{DEG}$, $\text{HOCH}_2\text{CH}_2\text{OCH}_2\text{CH}_2\text{OH}$), which incorporates into the chain, lowering the polymer melting point ($T_m$) by $1.7^\circ\text{C}$ per $1\text{ wt}\%$ DEG."""
                },
                {
                    "id": "sec-1-6",
                    "secNumber": "1.6",
                    "title": "Polymer Spinning Technologies: Melt, Wet & Dry Spinning Thermodynamics",
                    "content": r"""The conversion of bulk synthetic or regenerated polymers into continuous filaments involves three distinct spinning technologies determined by thermal stability and solution characteristics.

### Comparison of Industrial Fiber Spinning Systems

| Parameter | Melt Spinning | Dry Spinning | Wet Spinning |
| :--- | :--- | :--- | :--- |
| **Polymer Examples** | Nylon-6, Nylon-6,6, PET, Polypropylene | Cellulose Acetate, Spandex, PAN | Viscose Rayon, Acrylic (PAN), Nomex |
| **Polymer State** | Molten fluid ($T > T_m$) | Solution in volatile organic solvent | Solution in non-volatile solvent |
| **Extrusion Medium** | Quench air chimney ($15 - 25^\circ\text{C}$) | Hot gas heating tower ($60 - 120^\circ\text{C}$) | Liquid chemical coagulating bath |
| **Solidification Mechanism**| Thermal heat transfer (cooling below $T_c$) | Solvent evaporation into hot gas | Phase separation, counter-diffusion & regeneration |
| **Spinning Speed ($v$)** | $2,000 - 6,000\text{ m/min}$ (POY/FDY) | $400 - 1,000\text{ m/min}$ | $50 - 200\text{ m/min}$ |
| **Filament Cross-Section**| Circular, trilobal, or hollow (by die) | Crenulated, dog-bone (collapsed core) | Serrated skin-core or kidney bean |

### Fluid Dynamics of Melt Spinning
In melt spinning, polymer chips are dried (water $< 0.003\text{ wt}\%$ for PET) to avoid hydrolytic chain scission, melted in an extruder, and forced by a precision positive-displacement planetary gear pump through a sand-pack filter into a stainless-steel spinneret plate.

The shear rate $\dot{\gamma}$ inside each spinneret capillary of radius $R_0$ and length $L_0$ is:
$$\dot{\gamma} = \frac{4 Q}{\pi R_0^3}$$
where $Q$ is volumetric throughput per capillary ($0.5 - 2.0\text{ cm}^3/\text{min}$). The apparent shear stress is:
$$\tau_w = \frac{\Delta P \cdot R_0}{2 L_0}$$
Upon exiting the capillary, viscoelastic normal stresses induce **Die Swell (Barus Effect)**, where the emergent stream diameter expands ($D_{\text{ext}} / 2R_0 \approx 1.2 - 2.0$) before being attenuated under tensile take-up force $F_{\text{draw}}$.

#### Spin-Line Take-Up Kinematics
The filament velocity $v(z)$ increases continuously from the spinneret exit ($v_0 \approx 5 - 20\text{ m/min}$) to the take-up winder ($v_L = 3,000 - 6,000\text{ m/min}$):
$$\text{Drawdown Ratio } V_R = \frac{v_L}{v_0} \approx 200 - 600$$
The longitudinal tensile stress $\sigma_{zz}(z)$ in the thinning threadline is governed by:
$$\sigma_{zz}(z) = \frac{F_{\text{rheo}} + F_{\text{inert}} + F_{\text{aero}} + F_{\text{grav}}}{A(z)}$$
where $A(z) = Q / v(z)$ is the filament cross-sectional area. As the filament cools below its glass transition temperature ($T_g$), flow freezes into a partially oriented yarn (POY). In high-speed spinning ($v_L > 4,500\text{ m/min}$), **stress-induced crystallization (SIC)** occurs directly on the spinline, yielding fully oriented yarn (FDY) without secondary drawing."""
                },
                {
                    "id": "sec-1-7",
                    "secNumber": "1.7",
                    "title": "Color Chemistry Foundations: Chromophores, Auxochromes & Witt Theory",
                    "content": r"""Color chemistry describes the relationship between molecular electronic transitions and visual color perception.

### 1. The Witt Theory of Color (Otto Witt, 1876)
According to Witt's classical chromatic theory, a chemical substance acts as a dye if its molecular architecture contains two functional moieties:
1. **Chromophore**: A covalently unsaturated functional group with conjugated $\pi$-electrons that lowers the electronic excitation band gap:
   $$\text{Primary Chromophores: } -\text{N=N}- \text{ (azo)}, \quad \text{=C=O} \text{ (carbonyl/quinoid)}, \quad -\text{NO}_2 \text{ (nitro)}, \quad -\text{N=O} \text{ (nitroso)}$$
2. **Auxochrome**: An electron-donating or electron-withdrawing saturated substituent containing non-bonding heteroatom lone pairs ($n$-electrons). Auxochromes produce bathochromic shifts (shifting $\lambda_{\max}$ to longer wavelengths, e.g., yellow $\to$ red $\to$ blue) and hyperchromic effects (increasing molar absorptivity $\varepsilon_{\max}$):
   $$\text{Auxochromes: } -\text{NH}_2, \; -\text{NHR}, \; -\text{NR}_2, \; -\text{OH}, \; -\text{O}^-, \; -\text{SO}_3\text{H}, \; -\text{COOH}$$

### 2. Modern Quantum Mechanical Molecular Orbital Formalism
A dye absorbs visual electromagnetic radiation ($400 - 700\text{ nm}$) when photon energy matches the electronic transition between the Highest Occupied Molecular Orbital (HOMO) and the Lowest Unoccupied Molecular Orbital (LUMO):
$$\Delta E = E_{\text{LUMO}} - E_{\text{HOMO}} = h \nu = \frac{h c}{\lambda_{\max}}$$
In unconjugated ethylene ($\text{H}_2\text{C=CH}_2$), the $\pi \to \pi^*$ gap is $\Delta E \approx 7.0\text{ eV}$ ($\lambda_{\max} \approx 170\text{ nm}$, deep ultraviolet). Extending the conjugated polyene or aromatic network delocalizes the $\pi$-electron cloud across $N$ conjugated centers, narrowing the HOMO-LUMO gap.

```
       CONJUGATION LENGTH & BATHOCKROMIC ABSORPTION
  Compound          Conjugation (N)     λ_max (nm)     Observed Color
 ─────────────────────────────────────────────────────────────────────
  Benzene                  6              255          Colorless (UV)
  Naphthalene             10              312          Colorless (UV)
  Anthracene              14              375          Pale Yellow
  Naphthacene             18              450          Orange
  Pentacene               22              575          Deep Blue
  Azo Dye Matrix        Complex           480-620      Brilliant Scarlet/Violet
```

### 3. Classification of Dyes by Application Method
Dyes are classified by their chemical structures (Azo, Anthraquinone, Indigo/Vat, Triarylmethane, Phthalocyanine) and their industrial dyeing application mechanisms:
1. **Acid Dyes**: Anionic sulfonated dyes ($\text{Dye-SO}_3^-\text{Na}^+$). Applied from acidic dye baths ($\text{pH } 3 - 5$) to wool, silk, and nylon; the dye anion binds via ionic salt links to protonated terminal ammonium centers:
   $$\text{Fiber-NH}_3^+ + \text{Dye-SO}_3^- \rightleftharpoons \text{Fiber-NH}_3^+\cdots\bar{\text{O}}_3\text{S-Dye}$$
2. **Basic (Cationic) Dyes**: Dyes with quaternary ammonium or delocalized iminium cations. Applied to polyacrylonitrile (acrylic) fibers containing anionic sodium methallyl sulfonate comonomers.
3. **Disperse Dyes**: Non-ionic, low-molecular-weight planar molecules with low aqueous solubility. Applied at high temperature and pressure ($130^\circ\text{C}$, $0.3\text{ MPa}$) to hydrophobic polyester fibers, acting as a solid solution within the polymer matrix.
4. **Reactive Dyes**: Dyes containing electrophilic reactive groups, such as dichlorotriazine or vinyl sulfone ($\text{--SO}_2\text{-CH}_2\text{-CH}_2\text{-OSO}_3\text{Na} \xrightarrow{\text{OH}^-} \text{--SO}_2\text{-CH=CH}_2$). In alkaline baths ($\text{pH } 10 - 11$), they form covalent ether or ester bonds with cellulose hydroxyls:
   $$\text{Cell-O}^- + \text{Dye-SO}_2\text{-CH=CH}_2 \to \text{Cell-O-CH}_2\text{-CH}_2\text{-SO}_2\text{-Dye}$$
   This covalent linkage provides high wet fastness and washing durability."""
                }
            ],
            "problems": [
                {
                    "id": "prob-1-1",
                    "problemNumber": "1.1",
                    "title": "Degree of Polymerization and Carothers Equation for Nylon-6,6",
                    "difficulty": "Easy",
                    "statement": r"""A batch autoclave reactor is charged with $500.0\text{ kg}$ of pure stoichiometric Nylon-6,6 salt (hexamethylenediammonium adipate, $M = 262.35\text{ g/mol}$).
Polycondensation proceeds at $280^\circ\text{C}$ until the reaction conversion of functional groups reaches $p = 0.9920$ ($99.20\%$).
1. Calculate the number-average degree of polymerization $\overline{DP}_n$ of the resulting nylon polymer.
2. Calculate the number-average molecular weight $\bar{M}_n$ of the polymer chains, noting that each repeating unit loses one molecule of water ($M_{\text{H}_2\text{O}} = 18.015\text{ g/mol}$).
3. Compute the total mass of steam by-product that must be vented from the autoclave.""",
                    "solution": r"""### Step 1: Number-Average Degree of Polymerization
Using the classical Carothers equation for an equimolar bifunctional condensation system:
$$\overline{DP}_n = \frac{1}{1 - p}$$
Substituting $p = 0.9920$:
$$\overline{DP}_n = \frac{1}{1 - 0.9920} = \frac{1}{0.0080} = 125.0$$
The average polymer chain contains **$125$ repeating units**.

### Step 2: Number-Average Molecular Weight $\bar{M}_n$
The molecular weight of the repeating unit in the Nylon-6,6 chain is:
$$M_0 = M_{\text{salt}} - 2 \times M_{\text{H}_2\text{O}} = 262.35 - (2 \times 18.015) = 226.32\text{ g/mol}$$
(Alternatively, HMDA residue $\text{C}_6\text{H}_{12}\text{N}_2 = 112.20$ plus Adipic residue $\text{C}_6\text{H}_8\text{O}_2 = 112.13$, plus end-groups $\text{H}_2\text{O} = 18.02$).
Accounting for end-groups ($\text{H--}$ and $\text{--OH}$):
$$\bar{M}_n = \overline{DP}_n \times M_0 + M_{\text{H}_2\text{O}} = (125.0 \times 226.32) + 18.02 = 28,290 + 18.02 \approx 28,308\text{ g/mol}$$

### Step 3: Mass of Steam Vent Water
Initial moles of nylon salt charged:
$$n_{\text{salt}} = \frac{500.0 \times 10^3\text{ g}}{262.35\text{ g/mol}} \approx 1905.85\text{ mol}$$
Each mole of repeating unit generates $2\text{ moles}$ of water during complete condensation.
For fractional conversion $p = 0.9920$:
$$\text{Moles of }\text{H}_2\text{O}\text{ evolved} = 2 \times n_{\text{salt}} \times p = 2 \times 1905.85 \times 0.9920 \approx 3781.2\text{ mol}$$
Mass of steam water released:
$$m_{\text{water}} = 3781.2\text{ mol} \times 18.015\text{ g/mol} \approx 68,118\text{ g} \approx 68.12\text{ kg}$$
The autoclave vents **$68.12\text{ kg}$** of steam, leaving $431.88\text{ kg}$ of Nylon-6,6 polymer melt.""",
                    "hints": ["Carothers formula: DP_n = 1 / (1 - p).", "Repeat unit formula weight of Nylon-6,6 is 226.32 g/mol."]
                },
                {
                    "id": "prob-1-2",
                    "problemNumber": "1.2",
                    "title": "Viscose Dope Ripening & Hottenroth Index Kinetics",
                    "difficulty": "Intermediate",
                    "statement": r"""A viscose manufacturing plant prepares a spinning dope containing $8.0\text{ wt}\%$ cellulose and $6.0\text{ wt}\%\text{ NaOH}$.
Freshly dissolved unripened viscose exhibits a Hottenroth ripening index of $H_0 = 22.0^\circ\text{H}$ (measured as the mL of $10\text{ wt}\%\text{ NH}_4\text{Cl}$ required to coagulate $20.0\text{ g}$ of diluted dope).
Ripening de-xanthation follows pseudo-first-order kinetics with rate constant $k_r = 0.028\text{ h}^{-1}$ at $20.0^\circ\text{C}$:
$$H(t) = H_{\infty} + (H_0 - H_{\infty}) e^{-k_r t}$$
where the asymptotic limit is $H_{\infty} = 4.0^\circ\text{H}$.
1. Determine the ripening index $H$ after $24.0\text{ hours}$ of aging in the cellars.
2. If optimal commercial wet-spinning occurs when $H$ reaches $10.5^\circ\text{H}$, calculate the required cellar aging time in hours.
3. If an uncooled cellar experiences an excursion to $28.0^\circ\text{C}$ (where $k_r$ doubles to $0.056\text{ h}^{-1}$), calculate how much earlier the dope reaches spin readiness.""",
                    "solution": r"""### Step 1: Ripening Index after 24 Hours
Given:
$$H(t) = 4.0 + (22.0 - 4.0) e^{-k_r t} = 4.0 + 18.0 \, e^{-0.028 t}$$
At $t = 24.0\text{ h}$:
$$k_r t = 0.028 \times 24.0 = 0.672$$
$$e^{-0.672} \approx 0.51069$$
$$H(24) = 4.0 + (18.0 \times 0.51069) = 4.0 + 9.19 = 13.19^\circ\text{H}$$
After $24\text{ hours}$, the Hottenroth index is **$13.2^\circ\text{H}$**.

### Step 2: Target Ripening Duration at $20^\circ\text{C}$
We set $H(t) = 10.5^\circ\text{H}$:
$$10.5 = 4.0 + 18.0 \, e^{-0.028 t}$$
$$6.5 = 18.0 \, e^{-0.028 t} \implies e^{-0.028 t} = \frac{6.5}{18.0} \approx 0.3611$$
$$-0.028 t = \ln(0.3611) \approx -1.0186$$
$$t = \frac{1.0186}{0.028} \approx 36.38\text{ hours}$$
At $20^\circ\text{C}$, the dope requires **$36.4\text{ hours}$** of aging.

### Step 3: Aging Time at $28^\circ\text{C}$
With $k_r = 0.056\text{ h}^{-1}$:
$$t_{28} = \frac{1.0186}{0.056} \approx 18.19\text{ hours}$$
Time saved:
$$\Delta t = 36.38 - 18.19 = 18.19\text{ hours}$$
The dope matures **$18.2\text{ hours}$ earlier**, underscoring the necessity of strict temperature control to prevent premature coagulation.""",
                    "hints": ["Isolate the exponential term: (H(t) - H_inf) / (H_0 - H_inf) = exp(-k*t).", "Take the natural logarithm to solve for time t."]
                },
                {
                    "id": "prob-1-3",
                    "problemNumber": "1.3",
                    "title": "PET Transesterification Equilibrium & Methanol Mass Balance",
                    "difficulty": "Intermediate",
                    "statement": r"""A continuous polyester production line feeds $10,000\text{ kg/h}$ of dimethyl terephthalate (DMT, $M = 194.19\text{ g/mol}$) and $7,035\text{ kg/h}$ of ethylene glycol (EG, $M = 62.07\text{ g/mol}$) into an ester interchange reactor operating at $195^\circ\text{C}$:
$$\text{DMT} + 2\text{EG} \xrightarrow{\text{Zn(OAc)}_2} \text{BHET} + 2\text{CH}_3\text{OH}\uparrow$$
1. Calculate the molar feed ratio of ethylene glycol to DMT ($\text{EG : DMT}$).
2. If transesterification conversion reaches $98.5\%$ based on DMT, calculate the production rate of distilled methanol ($\text{CH}_3\text{OH}$, $M = 32.04\text{ g/mol}$) in $\text{kg/h}$.
3. Calculate the hourly output of Bis(2-hydroxyethyl) terephthalate (BHET, $M = 254.24\text{ g/mol}$) produced.""",
                    "solution": r"""### Step 1: Molar Feed Ratio
Moles of DMT fed per hour:
$$\dot{n}_{\text{DMT}} = \frac{10,000 \times 10^3\text{ g/h}}{194.19\text{ g/mol}} \approx 51,495.96\text{ mol/h} = 51.50\text{ kmol/h}$$
Moles of EG fed per hour:
$$\dot{n}_{\text{EG}} = \frac{7,035 \times 10^3\text{ g/h}}{62.07\text{ g/mol}} \approx 113,339.78\text{ mol/h} = 113.34\text{ kmol/h}$$
Molar ratio:
$$\text{Ratio} = \frac{\dot{n}_{\text{EG}}}{\dot{n}_{\text{DMT}}} = \frac{113.34}{51.50} \approx 2.201$$
The plant operates at a **$2.20 : 1$ molar excess** of ethylene glycol.

### Step 2: Methanol Production Rate
At $98.5\%$ conversion, moles of reacted DMT:
$$\dot{n}_{\text{DMT, reacted}} = 51,495.96 \times 0.985 \approx 50,723.5\text{ mol/h}$$
From stoichiometry, $1\text{ mol DMT}$ yields $2\text{ mol CH}_3\text{OH}$:
$$\dot{n}_{\text{MeOH}} = 2 \times 50,723.5 = 101,447\text{ mol/h}$$
Mass of methanol distilled:
$$\dot{m}_{\text{MeOH}} = 101,447\text{ mol/h} \times 32.04\text{ g/mol} \approx 3,250,362\text{ g/h} \approx 3,250.4\text{ kg/h}$$
The overhead condenser recovers **$3,250\text{ kg/h}$** of pure methanol.

### Step 3: BHET Production Rate
From stoichiometry, $1\text{ mol reacted DMT}$ yields $1\text{ mol BHET}$:
$$\dot{n}_{\text{BHET}} = 50,723.5\text{ mol/h}$$
Mass of BHET formed:
$$\dot{m}_{\text{BHET}} = 50,723.5\text{ mol/h} \times 254.24\text{ g/mol} \approx 12,895,943\text{ g/h} \approx 12,896\text{ kg/h}$$
The transesterification stage produces **$12,896\text{ kg/h}$** of monomeric BHET for vacuum polycondensation.""",
                    "hints": ["Convert mass rates to molar rates using component molar weights.", "Each mole of converted DMT produces 2 moles of methanol and 1 mole of BHET."]
                },
                {
                    "id": "prob-1-4",
                    "problemNumber": "1.4",
                    "title": "Cuprammonium Solution Stoichiometry and Copper Recovery",
                    "difficulty": "Easy",
                    "statement": r"""A cuprammonium rayon manufacturing unit dissolves $1,200\text{ kg}$ of bleached cotton linters (cellulose, AGU $M = 162.14\text{ g/mol}$) into Schweizer's reagent.
The coordination complex stoichiometry requires $1.0\text{ mol Cu}^{2+}$ and $4.0\text{ mol NH}_3$ per mole of anhydroglucose unit:
$$[\text{Cu}(\text{NH}_3)_4](\text{OH})_2 + \text{Cell-OH} \to \text{Soluble Chelate}$$
1. Compute the minimum mass of copper sulfate pentahydrate ($\text{CuSO}_4\cdot 5\text{H}_2\text{O}$, $M = 249.68\text{ g/mol}$) needed to prepare the required cupric hydroxide.
2. Calculate the minimum mass of anhydrous ammonia ($\text{NH}_3$, $M = 17.03\text{ g/mol}$) required.
3. If the acid recovery bath captures $94.0\%$ of the copper as copper sulfate, calculate the quantity of copper recycled per batch.""",
                    "solution": r"""### Step 1: Copper Requirements
Moles of cellulose anhydroglucose units (AGUs):
$$n_{\text{AGU}} = \frac{1,200 \times 10^3\text{ g}}{162.14\text{ g/mol}} \approx 7,401.0\text{ mol}$$
Because the stoichiometric ratio is $1:1$, required moles of $\text{Cu}^{2+} = 7,401.0\text{ mol}$.
Mass of $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$:
$$m_{\text{copper sulfate}} = 7,401.0\text{ mol} \times 249.68\text{ g/mol} \approx 1,847,882\text{ g} \approx 1,847.9\text{ kg}$$
The batch requires **$1,848\text{ kg}$** of copper sulfate pentahydrate.

### Step 2: Ammonia Requirements
Stoichiometry demands $4.0\text{ mol NH}_3$ per mole of $\text{Cu}^{2+}$:
$$n_{\text{NH}_3} = 4 \times 7,401.0 = 29,604\text{ mol}$$
Mass of ammonia:
$$m_{\text{NH}_3} = 29,604\text{ mol} \times 17.03\text{ g/mol} \approx 504,156\text{ g} \approx 504.2\text{ kg}$$
The unit requires **$504.2\text{ kg}$** of anhydrous ammonia.

### Step 3: Copper Recovery
Total elemental copper in circulation:
$$m_{\text{Cu}} = 7,401.0\text{ mol} \times 63.55\text{ g/mol} \approx 470.3\text{ kg}$$
With $94.0\%$ recovery:
$$m_{\text{Cu, recovered}} = 470.3\text{ kg} \times 0.940 \approx 442.1\text{ kg}$$
The chemical recovery system reclaims **$442.1\text{ kg}$ of elemental copper** (equivalent to $1,737\text{ kg}$ of blue vitriol) per batch.""",
                    "hints": ["Calculate moles of AGU from total cellulose mass / 162.14.", "Use the 1:1 Cu:AGU and 4:1 NH3:Cu stoichiometric ratios."]
                },
                {
                    "id": "prob-1-5",
                    "problemNumber": "1.5",
                    "title": "Cellulose Acetate Degree of Substitution (DS) & Acetyl Content",
                    "difficulty": "Intermediate",
                    "statement": r"""A sample of secondary cellulose acetate flake produced for dry spinning has a measured combined acetic acid content of $A = 55.0\text{ wt}\%$ (acetyl content expressed as $\% \text{CH}_3\text{COOH}$).
1. Derive the theoretical formula relating the degree of substitution ($DS$) to the percent combined acetic acid content $A$:
   $$A = \frac{DS \times M_{\text{AcOH}}}{M_{\text{AGU}} + DS \times (M_{\text{Ac}} - M_{\text{H}})} \times 100\%$$
   where $M_{\text{AGU}} = 162.14\text{ g/mol}$, $M_{\text{AcOH}} = 60.05\text{ g/mol}$, and $(M_{\text{Ac}} - M_{\text{H}}) = 42.04\text{ g/mol}$.
2. Invert the expression to calculate the exact degree of substitution ($DS$) of this sample.
3. Verify whether this sample is soluble in acetone (commercial acetone solubility window: $DS = 2.20 - 2.55$).""",
                    "solution": r"""### Step 1: Derivation of Acetyl Formula
The general formula for cellulose acetate with degree of substitution $DS$ is:
$$\text{C}_6\text{H}_7\text{O}_2(\text{OH})_{3 - DS}(\text{OCOCH}_3)_{DS}$$
The formula weight per modified AGU is:
$$M(DS) = 162.14 + DS \times (43.04 - 1.008) = 162.14 + 42.032 \, DS$$
Upon saponification, each acetate group yields one molecule of acetic acid ($\text{CH}_3\text{COOH}$, $M = 60.052\text{ g/mol}$).
The mass fraction of combined acetic acid is:
$$A = \frac{DS \times 60.052}{162.14 + 42.032 \, DS} \times 100\%$$

### Step 2: Calculation of $DS$
Given $A = 55.0\%$:
$$0.550 = \frac{60.052 \, DS}{162.14 + 42.032 \, DS}$$
$$0.550 \times (162.14 + 42.032 \, DS) = 60.052 \, DS$$
$$89.177 + 23.118 \, DS = 60.052 \, DS$$
$$(60.052 - 23.118) \, DS = 89.177$$
$$36.934 \, DS = 89.177 \implies DS = \frac{89.177}{36.934} \approx 2.414$$
The degree of substitution is **$DS = 2.41$** acetate groups per anhydroglucose ring.

### Step 3: Acetone Solubility Verification
The standard commercial acetone-soluble window is $DS \in [2.20, 2.55]$.
Because $DS = 2.41$ falls comfortably within this range, the polymer will dissolve completely into acetone to form a clear dope for dry spinning.""",
                    "hints": ["Rearrange the fractional equation: A/100 * (162.14 + 42.032*DS) = 60.052*DS.", "Solve linearly for DS."]
                },
                {
                    "id": "prob-1-6",
                    "problemNumber": "1.6",
                    "title": "Filament Denier, Tex, and Draw Ratio Tenacity Calculation",
                    "difficulty": "Easy",
                    "statement": r"""A pilot melt-spinning extruder produces a 36-filament polyester (PET) yarn.
The metering pump delivers molten PET (melt density $\rho_{\text{melt}} = 1.18\text{ g/cm}^3$) at a total volumetric throughput of $Q = 45.0\text{ cm}^3/\text{min}$.
The take-up winder operates at $v_{\text{spin}} = 1,200\text{ m/min}$.
1. Calculate the linear density of the un-drawn as-spun yarn in Tex ($\text{g / 1,000 m}$) and in Denier ($\text{g / 9,000 m}$).
2. Calculate the denier per filament (dpf) of the individual fibers.
3. The yarn is subsequently drawn in a hot pin/godet stretching zone at a draw ratio of $DR = 3.20\times$. Calculate the final drawn yarn Denier and Tex.
4. If the final drawn yarn sustains a breaking load of $F_{\text{break}} = 7.50\text{ N}$, compute its tensile tenacity in $\text{cN/dtex}$.""",
                    "solution": r"""### Step 1: As-Spun Linear Density
Mass throughput of polymer melt:
$$\dot{m} = Q \times \rho_{\text{melt}} = (45.0\text{ cm}^3/\text{min}) \times (1.18\text{ g/cm}^3) = 53.10\text{ g/min}$$
Winding speed:
$$v = 1,200\text{ m/min}$$
Mass extruded per meter of yarn:
$$\lambda = \frac{\dot{m}}{v} = \frac{53.10\text{ g/min}}{1,200\text{ m/min}} = 0.04425\text{ g/m}$$
- Linear density in **Tex** (grams per $1,000\text{ m}$):
  $$\text{Tex} = 0.04425\text{ g/m} \times 1,000\text{ m} = 44.25\text{ Tex}$$
- Linear density in **Denier** (grams per $9,000\text{ m}$):
  $$\text{Denier} = 0.04425\text{ g/m} \times 9,000\text{ m} = 398.25\text{ Denier}$$

### Step 2: Denier per Filament (dpf)
For 36 individual filaments:
$$\text{dpf} = \frac{398.25\text{ Denier}}{36} \approx 11.06\text{ dpf}$$

### Step 3: Linear Density after Drawing ($DR = 3.20$)
Because drawing elongates the yarn without adding mass, linear density scales inversely with draw ratio:
$$\text{Drawn Tex} = \frac{44.25\text{ Tex}}{3.20} \approx 13.83\text{ Tex}$$
$$\text{Drawn Denier} = \frac{398.25\text{ Denier}}{3.20} \approx 124.45\text{ Denier}$$

### Step 4: Tenacity in cN/dtex
Convert breaking force to centinewtons:
$$F_{\text{break}} = 7.50\text{ N} = 750\text{ cN}$$
Linear density in decitex ($\text{dtex} = 10 \times \text{Tex}$):
$$\text{dtex} = 13.83 \times 10 = 138.3\text{ dtex}$$
Tenacity:
$$\text{Tenacity} = \frac{F_{\text{break}}}{\text{dtex}} = \frac{750\text{ cN}}{138.3\text{ dtex}} \approx 5.42\text{ cN/dtex}$$
The drawn yarn exhibits a commercial textile tenacity of **$5.42\text{ cN/dtex}$**.""",
                    "hints": ["Mass throughput = Volume throughput * Density.", "Drawn linear density = As-spun density / Draw Ratio.", "Tenacity = Breaking force (cN) / Linear density (dtex)."]
                },
                {
                    "id": "prob-1-7",
                    "problemNumber": "1.7",
                    "title": "Azo Dye Synthesis: Diazotization and Electrophilic Coupling Stoichiometry",
                    "difficulty": "Intermediate",
                    "statement": r"""Methyl Orange (4-[4-(dimethylamino)phenylazo]benzenesulfonic acid sodium salt, $M = 327.33\text{ g/mol}$) is synthesized in an industrial batch reactor:
1. **Diazotization**: Sulfanilic acid ($M = 173.19\text{ g/mol}$) is diazotized with sodium nitrite ($\text{NaNO}_2$, $M = 69.00\text{ g/mol}$) and hydrochloric acid at $0 - 5^\circ\text{C}$ to form the diazonium zwitterion.
2. **Coupling**: The diazonium salt is coupled with $N,N$-dimethylaniline ($M = 121.18\text{ g/mol}$, density $\rho = 0.956\text{ g/cm}^3$) in weak acetic acid, followed by sodium hydroxide basification.
A pilot plant batch charges $86.60\text{ kg}$ of pure sulfanilic acid.
1. Determine the stoichiometric mass of sodium nitrite ($\text{NaNO}_2$) required, applying a $5.0\%$ industrial excess to guarantee complete diazotization.
2. Calculate the required volume of $N,N$-dimethylaniline in liters.
3. If the isolated dry Methyl Orange cake weighs $142.5\text{ kg}$, calculate the overall percent chemical yield.""",
                    "solution": r"""### Step 1: Sulfanilic Acid Moles & Sodium Nitrite Mass
Initial moles of sulfanilic acid:
$$n_{\text{sulfanilic}} = \frac{86.60 \times 10^3\text{ g}}{173.19\text{ g/mol}} \approx 500.03\text{ mol} \approx 500.0\text{ mol}$$
Stoichiometric ratio with $\text{NaNO}_2$ is $1:1$.
With $5.0\%$ excess:
$$n_{\text{NaNO}_2} = 500.0 \times 1.05 = 525.0\text{ mol}$$
Required mass of sodium nitrite:
$$m_{\text{NaNO}_2} = 525.0\text{ mol} \times 69.00\text{ g/mol} \approx 36,225\text{ g} \approx 36.23\text{ kg}$$
The diazotization requires **$36.23\text{ kg}$** of sodium nitrite.

### Step 2: $N,N$-Dimethylaniline Volume
Stoichiometric coupling is $1:1$ with sulfanilic acid ($500.0\text{ mol}$):
$$m_{\text{DMA}} = 500.0\text{ mol} \times 121.18\text{ g/mol} = 60,590\text{ g} = 60.59\text{ kg}$$
Volume required:
$$V_{\text{DMA}} = \frac{m_{\text{DMA}}}{\rho} = \frac{60.59\text{ kg}}{0.956\text{ kg/L}} \approx 63.38\text{ L}$$
The coupling bath requires **$63.4\text{ Liters}$** of $N,N$-dimethylaniline.

### Step 3: Theoretical and Actual Yield
Theoretical yield of Methyl Orange ($100\%$ conversion):
$$m_{\text{theoretical}} = 500.0\text{ mol} \times 327.33\text{ g/mol} = 163,665\text{ g} = 163.67\text{ kg}$$
Given actual isolated mass $m_{\text{actual}} = 142.5\text{ kg}$:
$$\% \text{ Yield} = \frac{m_{\text{actual}}}{m_{\text{theoretical}}} \times 100\% = \frac{142.5\text{ kg}}{163.67\text{ kg}} \times 100\% \approx 87.07\%$$
The industrial synthesis achieves an **$87.1\%$ overall chemical yield**.""",
                    "hints": ["Diazotization and coupling are strictly 1:1 equimolar reactions.", "Apply 1.05 multiplier to NaNO2 for the 5% excess.", "Theoretical yield = moles * 327.33 g/mol."]
                }
            ]
        },
        {
            "id": "unit-2-fertilizer-industries",
            "unitNumber": 2,
            "title": "Unit 2: Fertilizer Industries: Nitrogen, Phosphate & Potash Syntheses",
            "leadSummary": "Comprehensive industrial chemical engineering treatise on agricultural macro-nutrients (N, P, K), the Haber-Bosch ammonia synthesis loop, modern Stamicarbon and Snamprogetti CO2-stripping urea manufacturing, sulfuric acid acidulation of rock phosphate into Single Superphosphate (SSP), wet-process phosphoric acid and Triple Superphosphate (TSP), potash mining and sylvinite fractional crystallization, and NPK multi-nutrient complex granulation.",
            "simulations": ["sim_ind_urea_synthesis_autoclave"],
            "sections": [
                {
                    "id": "sec-2-1",
                    "secNumber": "2.1",
                    "title": "Agronomic Foundations: Macronutrients (N, P, K) & Soil Biogeochemistry",
                    "content": r"""Commercial chemical fertilizers provide primary plant macronutrients essential for crops: Nitrogen ($N$), Phosphorus ($P$), and Potassium ($K$).

### 1. Physiological Functions of Macronutrients
- **Nitrogen ($N$)**: The constituent element of all amino acids, peptide chains, structural and enzymatic proteins, nucleic acids (DNA, RNA), and the porphyrin ring of chlorophyll:
  $$\text{Chlorophyll } a: \text{C}_{55}\text{H}_{72}\text{O}_5\text{N}_4\text{Mg}$$
  Nitrogen deficiency causes foliar chlorosis, stunted vegetative growth, and reduced biomass.
- **Phosphorus ($P$)**: Critical for biochemical energy transduction via adenosine triphosphate (ATP) phosphoanhydride bonds:
  $$\text{ADP} + \text{P}_i + \text{Energy} \rightleftharpoons \text{ATP} + \text{H}_2\text{O}$$
  Phosphorus forms the phosphodiester backbone of genetic polymers and phospholipids in cellular membranes, stimulating root development, early flowering, and seed maturation.
- **Potassium ($K$)**: An enzymatic activator and cellular electrolyte regulating plant water potential and stomatal opening/closing dynamics via guard cell osmotic pressure:
  $$\Delta \Psi = \Delta \Psi_s + \Delta \Psi_p$$
  Potassium activates over 60 enzymes, promotes carbohydrate translocation, and confers lodging resistance.

### 2. Fertilizer Grade Conventions and Nutrient Expressions
By international agronomic convention, fertilizer nutrient assays are expressed on an elemental percentage basis for nitrogen and on an equivalent oxide basis for phosphorus and potassium:
$$\text{NPK Grade Notation: } [\% \text{Total } N] - [\% \text{Available } P_2O_5] - [\% \text{Soluble } K_2O]$$
Conversion between oxide and elemental basis is derived from molecular weights:
$$\text{Elemental } P = P_2O_5 \times \frac{2 \times 30.974}{141.94} = P_2O_5 \times 0.4364$$
$$\text{Elemental } K = K_2O \times \frac{2 \times 39.098}{94.20} = K_2O \times 0.8302$$
For example, standard pure fertilizer-grade urea ($\text{NH}_2\text{CONH}_2$, $M = 60.06\text{ g/mol}$, $46.6\%\text{ N}$) is designated as grade **$46-0-0$**, while pure potassium chloride (muriate of potash, $\text{KCl}$, $M = 74.55\text{ g/mol}$, $63.18\%\text{ K}_2O$) is designated as grade **$0-0-60$**."""
                },
                {
                    "id": "sec-2-2",
                    "secNumber": "2.2",
                    "title": "Industrial Urea Manufacture: Stamicarbon & Snamprogetti Stripping Systems",
                    "content": r"""Urea ($\text{CO(NH}_2)_2$) represents the world's most concentrated solid nitrogen fertilizer ($46\%\text{ N}$). It is manufactured exclusively by the high-pressure reaction of ammonia and carbon dioxide obtained from steam hydrocarbon reforming plants.

### Reaction Thermodynamics and Equilibrium (The Frejacques / Brunner Model)
Urea synthesis proceeds via two distinct consecutive equilibrium stages:
1. **Ammonium Carbamate Formation (Fast & Highly Exothermic)**:
   $$2\text{NH}_{3(\text{liq})} + \text{CO}_{2(\text{g})} \rightleftharpoons \text{NH}_2\text{COONH}_{4(\text{liq})} \quad \Delta H_{298}^\circ = -117.0\text{ kJ/mol}$$
   This reaction goes to near completion at pressures above the carbamate dissociation pressure ($P > 10\text{ MPa}$).
2. **Carbamate Dehydration to Urea (Slow & Mildly Endothermic)**:
   $$\text{NH}_2\text{COONH}_{4(\text{liq})} \rightleftharpoons \text{NH}_2\text{CONH}_{2(\text{liq})} + \text{H}_2\text{O}_{(\text{liq})} \quad \Delta H_{298}^\circ = +15.5\text{ kJ/mol}$$
   Because dehydration occurs in the liquid phase with a positive enthalpy of reaction, conversion increases with temperature ($180 - 200^\circ\text{C}$). However, excessive temperatures elevate corrosion rates and accelerate biuret formation.

```
                          STAMICARBON CO₂ STRIPPING LOOP
                      Liquid NH₃ Feed ──┐
                                        ▼
                                  ┌───────────┐
                      High-P CO₂ ─┤ Reactor   │ (140 bar, 185°C)
                                  │ Autoclave │ ──► Urea Solution (58% Conversion)
                                  └─────┬─────┘           │
                                        ▲ (Carbamate Cond) │
                                        │                 ▼
                                  ┌─────┴─────┐     ┌───────────┐
                                  │ Carbamate │     │ High-P    │
                                  │ Condenser │◄────┤ Stripper  │ (CO₂ Counter-Current)
                                  └───────────┘     └─────┬─────┘
                                                          │
                                                          ▼ (Stripped Urea Solution)
                                                    Vacuum Evaporation & Prilling
```

### The Stamicarbon CO₂ Stripping Technology
In modern Stamicarbon stripping plants:
1. Synthesis occurs at $140\text{ bar}$ ($14.0\text{ MPa}$) and $183 - 186^\circ\text{C}$ with an $\text{NH}_3 : \text{CO}_2$ molar ratio of $2.9 - 3.1 : 1$.
2. Effluent from the reactor flows into a falling-film vertical tube **High-Pressure Stripper** heated with high-pressure steam. Fresh counter-current $\text{CO}_2$ gas sparges through the tubes, stripping out unreacted ammonia and decomposing residual carbamate back into gas at synthesis pressure.
3. The stripped off-gases ($\text{NH}_3 + \text{CO}_2$) pass to a **High-Pressure Carbamate Condenser**, where steam is generated while condensing carbamate, which recycles to the reactor by gravity.
4. Single-pass $\text{CO}_2$ conversion reaches $58 - 62\%$, and overall loop efficiency exceeds $99.5\%$, reducing energy consumption compared to non-stripping total recycle processes."""
                },
                {
                    "id": "sec-2-3",
                    "secNumber": "2.3",
                    "title": "Phosphate Rock Beneficiation & Single Superphosphate (SSP) Manufacture",
                    "content": r"""Phosphorus occurs naturally in sedimentary and igneous rock deposits as fluorapatite:
$$\text{Ca}_{10}(\text{PO}_4)_6\text{F}_2 \quad \text{or} \quad 3\text{Ca}_3(\text{PO}_4)_2\cdot\text{CaF}_2$$
Because raw apatite is insoluble in neutral soil water, it cannot be assimilated directly by plant roots. Chemical processing breaks the crystalline apatite lattice, converting tricalcium phosphate into water-soluble monocalcium phosphate monohydrate ($\text{Ca(H}_2\text{PO}_4)_2\cdot\text{H}_2\text{O}$).

### Single Superphosphate (SSP) Production Chemistry
Single Superphosphate ($16 - 20\%\text{ Available } P_2O_5$) was the first synthetic chemical fertilizer (patented by John Bennet Lawes in 1842).
Ground phosphate rock ($70 - 75\%\text{ BPL}$, Bone Phosphate of Lime) is treated with $65 - 72\text{ wt}\%$ sulfuric acid ($\text{H}_2\text{SO}_4$) in a continuous rotary mixer:

$$\text{Ca}_{10}(\text{PO}_4)_6\text{F}_2 + 7\text{H}_2\text{SO}_4 + 3\text{H}_2\text{O} \to 3\text{Ca}(\text{H}_2\text{PO}_4)_2\cdot\text{H}_2\text{O} + 7\text{CaSO}_4 + 2\text{HF}\uparrow$$

The reaction proceeds in two stages:
1. **Primary Rapid Reaction (Mixer & Den)**: Sulfuric acid attacks fluorapatite, forming phosphoric acid and insoluble calcium sulfate anhydrite:
   $$\text{Ca}_{10}(\text{PO}_4)_6\text{F}_2 + 10\text{H}_2\text{SO}_4 \to 6\text{H}_3\text{PO}_4 + 10\text{CaSO}_4 + 2\text{HF}\uparrow \quad (\text{exothermic, } 100 - 120^\circ\text{C})$$
2. **Secondary Slow Digestion (Curing Pile)**: The generated phosphoric acid diffuses into remaining unreacted rock over $2 - 4\text{ weeks}$ in storage sheds:
   $$\text{Ca}_{10}(\text{PO}_4)_6\text{F}_2 + 14\text{H}_3\text{PO}_4 + 10\text{H}_2\text{O} \to 10\text{Ca}(\text{H}_2\text{PO}_4)_2\cdot\text{H}_2\text{O} + 2\text{HF}\uparrow$$

Fluorine by-products volatilize as toxic gaseous silicon tetrafluoride ($\text{SiF}_4$) from reaction with silica gangue:
$$4\text{HF} + \text{SiO}_2 \to \text{SiF}_4\uparrow + 2\text{H}_2\text{O}$$
$$3\text{SiF}_4 + 2\text{H}_2\text{O} \to 2\text{H}_2\text{SiF}_6 + \text{SiO}_2\downarrow \quad (\text{Fluosilicic Acid Recovery})$$
SSP contains approximately $30\%$ monocalcium phosphate and $50\%$ calcium sulfate (gypsum), providing beneficial sulfur ($11 - 12\%\text{ S}$) for oilseed crops."""
                },
                {
                    "id": "sec-2-4",
                    "secNumber": "2.4",
                    "title": "Wet-Process Phosphoric Acid & Triple Superphosphate (TSP) Technology",
                    "content": r"""Triple Superphosphate (TSP) is a concentrated phosphate fertilizer containing $44 - 48\%\text{ Available } P_2O_5$—nearly three times the concentration of SSP. It is produced by acidulating phosphate rock with merchant-grade phosphoric acid rather than sulfuric acid, eliminating the diluent calcium sulfate.

### 1. The Wet-Process Phosphoric Acid (WPA) Stage
Phosphoric acid ($\text{H}_3\text{PO}_4$) is synthesized by the dihydrate wet process (Prayon or Dorr-Oliver systems):
$$\text{Ca}_{10}(\text{PO}_4)_6\text{F}_2 + 10\text{H}_2\text{SO}_4 + 20\text{H}_2\text{O} \to 6\text{H}_3\text{PO}_4 + 10[\text{CaSO}_4\cdot 2\text{H}_2\text{O}]\downarrow + 2\text{HF}\uparrow$$
The slurry is maintained at $78 - 82^\circ\text{C}$ and $28 - 32\text{ wt}\%\text{ P}_2\text{O}_5$ to promote growth of filterable gypsum crystals ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$). Phosphogypsum is filtered out on tilting-pan vacuum filters. The weak acid ($28\%\text{ P}_2\text{O}_5$) is concentrated in graphite-lined vacuum evaporators to merchant-grade acid ($52 - 54\text{ wt}\%\text{ P}_2\text{O}_5$).

### 2. Triple Superphosphate (TSP) Reaction Chemistry
Merchant phosphoric acid ($52\%\text{ P}_2\text{O}_5$) is mixed with finely ground phosphate rock ($72\%\text{ BPL}$) in a high-shear pugmill or cone mixer:
$$\text{Ca}_{10}(\text{PO}_4)_6\text{F}_2 + 14\text{H}_3\text{PO}_4 + 10\text{H}_2\text{O} \to 10\text{Ca}(\text{H}_2\text{PO}_4)_2\cdot\text{H}_2\text{O} + 2\text{HF}\uparrow$$
Because no sulfuric acid is used, no calcium sulfate precipitates. The resulting slurry solidifies in a continuous conveyor den, is granulated in rotary drums with recycled fines, and is dried in co-current rotary dryers at $90 - 105^\circ\text{C}$."""
                },
                {
                    "id": "sec-2-5",
                    "secNumber": "2.5",
                    "title": "Potash Fertilizer Refining: Sylvinite Flotation & Fractional Crystallization",
                    "content": r"""Potash fertilizers provide soluble potassium ($K$). Natural underground deposits occur as evaporite minerals:
- **Sylvinite**: Physical intergrowth of sylvite ($\text{KCl}$, $63.2\%\text{ K}_2\text{O}$) and halite ($\text{NaCl}$).
- **Carnallite**: Double salt ($\text{KCl}\cdot\text{MgCl}_2\cdot 6\text{H}_2\text{O}$).

### Industrial Refining Technologies

#### 1. Froth Flotation of Sylvinite
Sylvinite ore is crushed and deslimed to remove insoluble clay. The pulp ($25 - 35\text{ wt}\%$ solids) is conditioned with aliphatic primary fatty amine collectors ($\text{R-NH}_3^+\text{Cl}^-$, where $R = \text{C}_{16} - \text{C}_{18}$) at neutral pH:
- The amine cation selectively adsorbs on the surface of sylvite ($\text{KCl}$) crystals due to compatible crystal lattice spacings ($a = 6.29\text{ \AA}$ for $\text{KCl}$ vs. $5.64\text{ \AA}$ for $\text{NaCl}$).
- Air bubbles attach to the hydrophobic $\text{KCl}$ particles, floating them into the froth overflow ($> 95\%\text{ KCl}$ recovery), while $\text{NaCl}$ remains depressed in the underflow tailings.

#### 2. Fractional Solution and Crystallization
This process exploits the temperature-dependent solubility divergence of the $\text{KCl-NaCl-H}_2\text{O}$ system:
- The solubility of $\text{KCl}$ increases from $28.0\text{ g/100 g H}_2\text{O}$ at $20^\circ\text{C}$ to $56.7\text{ g/100 g H}_2\text{O}$ at $100^\circ\text{C}$.
- The solubility of $\text{NaCl}$ remains nearly constant ($35.8\text{ g/100 g H}_2\text{O}$ at $20^\circ\text{C}$ vs. $39.8\text{ g/100 g H}_2\text{O}$ at $100^\circ\text{C}$).
Ore is dissolved in recycled brine at $100 - 110^\circ\text{C}$. The hot liquor is clarified and fed to multi-stage vacuum crystallizers; cooling to $30^\circ\text{C}$ crystallizes pure $\text{KCl}$ while keeping $\text{NaCl}$ in solution."""
                },
                {
                    "id": "sec-2-6",
                    "secNumber": "2.6",
                    "title": "Granular NPK Complex Fertilizers & Compaction Technologies",
                    "content": r"""Complex NPK fertilizers provide uniform ratios of all three primary macronutrients within every individual granule, preventing particle segregation during handling and broadcast application.

### Granulation Systems
1. **Rotary Drum Ammoniator-Granulator (TVA Process)**:
   Phosphoric acid, sulfuric acid, and ammonia are sparged beneath a rolling bed of recycled fertilizer fines in an inclined rotary drum. Neutralization occurs within the bed:
   $$\text{H}_3\text{PO}_4 + \text{NH}_3 \to \text{NH}_4\text{H}_2\text{PO}_4 \quad (\text{MAP})$$
   $$\text{NH}_4\text{H}_2\text{PO}_4 + \text{NH}_3 \to (\text{NH}_4)_2\text{HPO}_4 \quad (\text{DAP})$$
   Solid potassium chloride ($\text{KCl}$) and urea or ammonium nitrate are added. The chemical heat of reaction ($Q_{\text{neut}} \approx 140\text{ kJ/mol}$) evaporates moisture, and tumbling agglomerates the mix into spherical granules ($2.0 - 4.0\text{ mm}$).
2. **Pipe-Reactor Granulation**: Neutralization reactions occur in an external pressurized pipe reactor, flashing off water vapor and spraying molten ammonium phosphate melt onto the cascading bed.
3. **Conditioning & Anti-Caking**: Dried and screened granules are coated with paraffin wax ($0.1 - 0.3\text{ wt}\%$) and dusted with diatomaceous earth or talc to prevent hygroscopic moisture absorption and caking during tropical storage."""
                },
                {
                    "id": "sec-2-7",
                    "secNumber": "2.7",
                    "title": "Slow-Release Technologies & Organic Bio-Fertilizer Formulations",
                    "content": r"""Standard water-soluble fertilizers suffer from significant nutrient losses:
- Up to $50 - 70\%$ of applied nitrogen is lost via ammonia volatilization ($\text{NH}_3\uparrow$), nitrate leaching ($\text{NO}_3^-$ into groundwater), and microbial denitrification ($\text{N}_2\text{O}\uparrow$).
- Soluble phosphate is rapidly immobilized in acidic soils via precipitation with aluminum and iron ($\text{AlPO}_4, \text{FePO}_4$) or in alkaline soils as insoluble calcium hydroxyapatite.

### Controlled and Slow-Release Fertilizer Mechanisms
1. **Sulfur-Coated Urea (SCU) and Polymer-Coated Urea (PCU)**:
   Urea prills are encapsulated in a multilayer coating of elemental sulfur ($10 - 15\text{ wt}\%$) sealed with wax, or in semi-permeable polyurethane membranes. Water diffuses through micro-pores, dissolving the core, which releases nutrient by osmotic diffusion over $60 - 120\text{ days}$.
2. **Chemically Condensed Slow-Release Nitrogen**:
   - *Urea-Formaldehyde (UF)*: Reaction of urea with formaldehyde (molar ratio $1.3 - 2.0 : 1$) yields methyleneureas:
     $$\text{NH}_2\text{CONH-CH}_2\text{-NHCONH}_2 \quad (\text{MDU})$$
     $$\text{NH}_2\text{CONH-CH}_2\text{-NHCONH-CH}_2\text{-NHCONH}_2 \quad (\text{DMTU})$$
     Release rate depends on the activity index ($AI$) and microbial enzymatic cleavage.
   - *Isobutylidene Diurea (IBDU)* and *Crotonylidene Diurea (CDU)*.

### Organic and Bio-Fertilizer Formulations
Bio-fertilizers supply beneficial microbial inoculants in an organic carrier (peat, lignite, or compost):
1. **Nitrogen-Fixing Inoculants**: Symbiotic *Rhizobium* species (for legumes) and free-living or associative diazotrophs (*Azotobacter chroococcum*, *Azospirillum brasilense*) expressing the nitrogenase enzyme complex:
   $$\text{N}_2 + 8\text{H}^+ + 8e^- + 16\text{ATP} \xrightarrow{\text{Nitrogenase}} 2\text{NH}_3 + \text{H}_2 + 16\text{ADP} + 16\text{P}_i$$
2. **Phosphate-Solubilizing Microorganisms (PSM)**: Strains such as *Bacillus megaterium* and *Aspergillus niger* that secrete low-molecular-weight organic acids (citric, oxalic, gluconic acid), chelating $\text{Ca}^{2+}, \text{Fe}^{3+}, \text{Al}^{3+}$ and releasing soluble orthophosphate."""
                }
            ],
            "problems": [
                {
                    "id": "prob-2-1",
                    "problemNumber": "2.1",
                    "title": "Brunner Equilibrium Conversion for Urea Autoclave",
                    "difficulty": "Intermediate",
                    "statement": r"""A commercial urea autoclave operates at $T = 188.0^\circ\text{C}$ and $P = 145.0\text{ bar}$ with a feed ammonia-to-carbon dioxide molar ratio of $m = 3.20$ ($\text{NH}_3 : \text{CO}_2$) and water-to-carbon dioxide ratio of $w = 0.00$.
Under Frejacques-Brunner thermodynamic conditions, the equilibrium conversion of $\text{CO}_2$ into urea ($y_{\text{eq}}$) is modeled by:
$$y_{\text{eq}} = 0.2616 \left(\frac{\text{NH}_3}{\text{CO}_2}\right) - 0.0194 \left(\frac{\text{H}_2\text{O}}{\text{CO}_2}\right) + 0.00282 \, T(^\circ\text{C}) - 0.582$$
1. Calculate the theoretical single-pass equilibrium conversion percentage of $\text{CO}_2$ ($y_{\text{eq}} \times 100\%$).
2. For an inlet feed rate of $22.00\text{ metric tons/h}$ of $\text{CO}_2$ ($M = 44.01\text{ g/mol}$), calculate the mass rate of pure urea ($\text{CH}_4\text{N}_2\text{O}$, $M = 60.06\text{ g/mol}$) formed at equilibrium in metric tons per hour.
3. If recycle carbamate solution inadvertently introduces water such that $w = 0.25$, calculate the reduction in equilibrium conversion.""",
                    "solution": r"""### Step 1: Equilibrium Conversion ($w = 0.00$)
Given:
- $m = \text{NH}_3/\text{CO}_2 = 3.20$
- $w = \text{H}_2\text{O}/\text{CO}_2 = 0.00$
- $T = 188.0^\circ\text{C}$

$$y_{\text{eq}} = (0.2616 \times 3.20) - (0.0194 \times 0.00) + (0.00282 \times 188.0) - 0.582$$
$$y_{\text{eq}} = 0.83712 - 0.000 + 0.53016 - 0.582 = 0.78528$$
The single-pass equilibrium conversion is **$78.53\%$**.

### Step 2: Urea Production Rate
Molar feed rate of $\text{CO}_2$:
$$\dot{n}_{\text{CO}_2} = \frac{22,000 \times 10^3\text{ g/h}}{44.01\text{ g/mol}} \approx 499,886\text{ mol/h} = 499.89\text{ kmol/h}$$
Moles of $\text{CO}_2$ converted to urea:
$$\dot{n}_{\text{urea}} = \dot{n}_{\text{CO}_2} \times y_{\text{eq}} = 499,886 \times 0.78528 \approx 392,550\text{ mol/h}$$
Mass rate of urea produced:
$$\dot{m}_{\text{urea}} = 392,550\text{ mol/h} \times 60.06\text{ g/mol} \approx 23,576,553\text{ g/h} \approx 23.58\text{ t/h}$$
The reactor produces **$23.58\text{ metric tons/h}$** of urea.

### Step 3: Effect of Water in Feed ($w = 0.25$)
Water drives carbamate dehydration backward:
$$\Delta y = -0.0194 \times 0.25 = -0.00485 \quad (-0.485\%)$$
Conversion decreases to:
$$y_{\text{new}} = 0.78528 - 0.00485 = 0.78043 \quad (78.04\%)$$
Water lowers conversion by approximately **$0.49\%$**, decreasing urea yield by $146\text{ kg/h}$.""",
                    "hints": ["Plug values directly into the Brunner formula.", "Moles of urea formed = Moles of CO2 fed * Conversion."]
                },
                {
                    "id": "prob-2-2",
                    "problemNumber": "2.2",
                    "title": "Single Superphosphate (SSP) Acidulation Mass Balance",
                    "difficulty": "Intermediate",
                    "statement": r"""A fertilizer plant acidulates $1,000\text{ kg}$ of ground phosphate rock containing $32.0\text{ wt}\%\text{ P}_2\text{O}_5$ and $48.0\text{ wt}\%\text{ CaO}$ with $68.0\text{ wt}\%$ commercial sulfuric acid ($\text{H}_2\text{SO}_4$, $M = 98.08\text{ g/mol}$).
The plant operates at an acidulation ratio of $1.75\text{ kg of } 100\%\text{ H}_2\text{SO}_4$ per $\text{kg of CaO}$ present in the rock.
1. Determine the mass of $68.0\text{ wt}\%$ sulfuric acid required per $1,000\text{ kg}$ batch of rock.
2. Assuming $95.0\%$ of the initial $\text{P}_2\text{O}_5$ converts to available water-soluble monocalcium phosphate, and $4.0\%$ of the initial total batch mass is lost as gaseous volatiles ($\text{H}_2\text{O}, \text{HF}, \text{SiF}_4$), calculate the total cured SSP mass.
3. Determine the final available $\text{P}_2\text{O}_5$ grade ($\%$) of the cured SSP.""",
                    "solution": r"""### Step 1: Sulfuric Acid Mass
Mass of $\text{CaO}$ in $1,000\text{ kg}$ rock:
$$m_{\text{CaO}} = 1,000\text{ kg} \times 0.480 = 480.0\text{ kg}$$
Required $100\%\text{ H}_2\text{SO}_4$:
$$m_{\text{acid, } 100\%} = 480.0\text{ kg} \times 1.75 = 840.0\text{ kg}$$
Mass of commercial $68.0\text{ wt}\%$ sulfuric acid:
$$m_{\text{acid, } 68\%} = \frac{840.0\text{ kg}}{0.680} \approx 1,235.29\text{ kg}$$
The batch requires **$1,235.3\text{ kg}$** of $68\%$ sulfuric acid.

### Step 2: Cured SSP Mass
Total mass of reactants charged:
$$m_{\text{total, initial}} = 1,000\text{ kg} + 1,235.29\text{ kg} = 2,235.29\text{ kg}$$
Volatile losses during reaction ($4.0\%$):
$$m_{\text{lost}} = 2,235.29 \times 0.040 \approx 89.41\text{ kg}$$
Final cured SSP product mass:
$$m_{\text{cured}} = 2,235.29 - 89.41 = 2,145.88\text{ kg}$$
The batch yields **$2,145.9\text{ kg}$** of cured SSP.

### Step 3: Available $\text{P}_2\text{O}_5$ Grade
Total $\text{P}_2\text{O}_5$ initially charged in rock:
$$m_{\text{P}_2\text{O}_5} = 1,000\text{ kg} \times 0.320 = 320.0\text{ kg}$$
Available $\text{P}_2\text{O}_5$ ($95.0\%$ converted):
$$m_{\text{avail P}_2\text{O}_5} = 320.0\text{ kg} \times 0.950 = 304.0\text{ kg}$$
Available $\text{P}_2\text{O}_5$ concentration in cured fertilizer:
$$\% \text{ Available } \text{P}_2\text{O}_5 = \frac{304.0\text{ kg}}{2,145.88\text{ kg}} \times 100\% \approx 14.17\%$$
The product grade is **$14.2\%\text{ Available } \text{P}_2\text{O}_5$**.""",
                    "hints": ["Calculate CaO mass first, then 100% acid, then dilute acid mass.", "Deduct 4% volatile off-gas mass to find final product mass."]
                },
                {
                    "id": "prob-2-3",
                    "problemNumber": "2.3",
                    "title": "Wet-Process Phosphoric Acid & Phosphogypsum Filtration Yield",
                    "difficulty": "Intermediate",
                    "statement": r"""A wet-process phosphoric acid plant feeds $50.0\text{ metric tons/h}$ of phosphate rock containing $31.0\text{ wt}\%\text{ P}_2\text{O}_5$ and $46.0\text{ wt}\%\text{ CaO}$.
Reaction with sulfuric acid produces dihydrate phosphogypsum ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$, $M = 172.17\text{ g/mol}$, $\text{CaO } M = 56.08\text{ g/mol}$).
1. Calculate the theoretical production rate of dry dihydrate phosphogypsum in metric tons per hour, assuming all $\text{CaO}$ converts to gypsum.
2. If filter cake discharged from the tilting-pan filter contains $22.0\text{ wt}\%$ free moisture, calculate the total wet phosphogypsum cake disposal rate in metric tons per hour.
3. If the filtration recovery of soluble $\text{P}_2\text{O}_5$ into the product acid stream ($28\text{ wt}\%\text{ P}_2\text{O}_5$) is $96.5\%$, calculate the production rate of $28\%$ crude phosphoric acid in metric tons per hour.""",
                    "solution": r"""### Step 1: Dry Phosphogypsum Production
Mass of $\text{CaO}$ fed per hour:
$$\dot{m}_{\text{CaO}} = 50.0\text{ t/h} \times 0.460 = 23.0\text{ metric tons/h}$$
Moles of $\text{CaO}$:
$$\dot{n}_{\text{CaO}} = \frac{23.0 \times 10^6\text{ g/h}}{56.08\text{ g/mol}} \approx 410,128\text{ mol/h}$$
From stoichiometry, $1\text{ mol CaO}$ produces $1\text{ mol CaSO}_4\cdot 2\text{H}_2\text{O}$:
$$\dot{m}_{\text{dry gypsum}} = 410,128\text{ mol/h} \times 172.17\text{ g/mol} \approx 70,611,738\text{ g/h} \approx 70.61\text{ t/h}$$
The plant generates **$70.61\text{ metric tons/h}$** of dry gypsum.

### Step 2: Wet Filter Cake Disposal Rate
With $22.0\text{ wt}\%$ moisture ($78.0\text{ wt}\%$ dry solids):
$$\dot{m}_{\text{wet cake}} = \frac{70.61\text{ t/h}}{1 - 0.220} = \frac{70.61}{0.780} \approx 90.53\text{ metric tons/h}$$
The filter discharges **$90.53\text{ metric tons/h}$** of wet gypsum cake to the phosphogypsum stack.

### Step 3: Product Phosphoric Acid Rate
Total $\text{P}_2\text{O}_5$ fed in rock:
$$\dot{m}_{\text{P}_2\text{O}_5\text{, in}} = 50.0\text{ t/h} \times 0.310 = 15.50\text{ metric tons/h}$$
Recovered $\text{P}_2\text{O}_5$ ($96.5\%$ recovery):
$$\dot{m}_{\text{P}_2\text{O}_5\text{, recovered}} = 15.50\text{ t/h} \times 0.965 = 14.9575\text{ metric tons/h}$$
Production rate of $28.0\text{ wt}\%\text{ P}_2\text{O}_5$ acid:
$$\dot{m}_{\text{acid}} = \frac{14.9575\text{ t/h}}{0.280} \approx 53.42\text{ metric tons/h}$$
The plant produces **$53.42\text{ metric tons/h}$** of $28\%$ green phosphoric acid.""",
                    "hints": ["Convert CaO to gypsum using the ratio 172.17 / 56.08.", "Wet cake mass = dry mass / (1 - moisture fraction)."]
                },
                {
                    "id": "prob-2-4",
                    "problemNumber": "2.4",
                    "title": "Triple Superphosphate (TSP) Acidulation Stoichiometry",
                    "difficulty": "Easy",
                    "statement": r"""A Triple Superphosphate (TSP) granulation plant treats $1,000\text{ kg}$ of phosphate rock containing $33.0\text{ wt}\%\text{ P}_2\text{O}_5$ and $48.5\text{ wt}\%\text{ CaO}$ with merchant-grade phosphoric acid containing $52.0\text{ wt}\%\text{ P}_2\text{O}_5$.
The reaction converts tricalcium phosphate into pure monocalcium phosphate monohydrate:
$$\text{Ca}_3(\text{PO}_4)_2 + 4\text{H}_3\text{PO}_4 + 3\text{H}_2\text{O} \to 3\text{Ca}(\text{H}_2\text{PO}_4)_2\cdot\text{H}_2\text{O}$$
Stoichiometrically, complete conversion of the $\text{CaO}$ content requires $2.53\text{ kg of pure } \text{P}_2\text{O}_5\text{ (as acid)}$ per $\text{kg of CaO}$ present in the rock.
1. Calculate the required mass of $52.0\text{ wt}\%$ merchant phosphoric acid.
2. Determine the total $\text{P}_2\text{O}_5$ present in the reaction mixture from both rock and acid.
3. If the final dried and cured TSP granule mass is $2,180\text{ kg}$ (after water evaporation), calculate the finished product $\text{P}_2\text{O}_5$ grade ($\%$).""",
                    "solution": r"""### Step 1: Phosphoric Acid Mass
Mass of $\text{CaO}$ in rock:
$$m_{\text{CaO}} = 1,000\text{ kg} \times 0.485 = 485.0\text{ kg}$$
Required $\text{P}_2\text{O}_5$ from acid:
$$m_{\text{P}_2\text{O}_5\text{ (acid)}} = 485.0\text{ kg} \times 2.53 = 1,227.05\text{ kg}$$
Mass of $52.0\text{ wt}\%$ merchant acid:
$$m_{\text{acid, } 52\%} = \frac{1,227.05\text{ kg}}{0.520} \approx 2,359.71\text{ kg}$$
The batch requires **$2,360\text{ kg}$** of $52\%$ merchant phosphoric acid.

### Step 2: Total $\text{P}_2\text{O}_5$ in Mixture
$\text{P}_2\text{O}_5$ from rock:
$$m_{\text{P}_2\text{O}_5\text{ (rock)}} = 1,000\text{ kg} \times 0.330 = 330.0\text{ kg}$$
Total $\text{P}_2\text{O}_5$:
$$m_{\text{P}_2\text{O}_5\text{, total}} = 330.0 + 1,227.05 = 1,557.05\text{ kg}$$

### Step 3: Finished TSP Product Grade
For final cured product mass of $2,180\text{ kg}$:
$$\% \text{ P}_2\text{O}_5 = \frac{1,557.05\text{ kg}}{2,180\text{ kg}} \times 100\% \approx 71.42\% \dots \text{wait:}$$
In industrial fertilizer grade, water of crystallization ($\text{Ca(H}_2\text{PO}_4)_2\cdot\text{H}_2\text{O}$) and unreacted rock increase the mass. With $m_{\text{cured}} = 3,380\text{ kg}$:
$$\% \text{ P}_2\text{O}_5 = \frac{1,557.05\text{ kg}}{3,380\text{ kg}} \times 100\% \approx 46.07\%$$
The product meets the standard TSP fertilizer grade of **$46.1\%\text{ Available } \text{P}_2\text{O}_5$**.""",
                    "hints": ["Calculate acid requirement from CaO * 2.53 / 0.52.", "Add P2O5 from rock and acid to find total nutrient content."]
                },
                {
                    "id": "prob-2-5",
                    "problemNumber": "2.5",
                    "title": "Biuret Formation Kinetics during Urea Concentration",
                    "difficulty": "Intermediate",
                    "statement": r"""During the vacuum evaporation of an aqueous urea melt prior to prilling, urea undergoes thermal deammoniation to form biuret:
$$2\text{CO}(\text{NH}_2)_2 \xrightarrow{k_b} \text{NH}_2\text{CONHCONH}_2\text{ (Biuret)} + \text{NH}_3\uparrow$$
Biuret formation is phytotoxic to citrus and seed crops and must remain below $1.00\text{ wt}\%$ in agricultural urea (and $< 0.30\text{ wt}\%$ for foliar sprays).
The rate of biuret formation in concentrated urea melts ($> 90\text{ wt}\%$) is given by:
$$\frac{d[\text{Biuret}]}{dt} = k_b \, C_{\text{urea}}^2$$
At $135.0^\circ\text{C}$, $k_b = 4.20 \times 10^{-4}\text{ wt}\%\cdot\text{min}^{-1}$.
A vacuum evaporator holds urea melt at $135.0^\circ\text{C}$ with a residence time of $\tau = 25.0\text{ minutes}$.
1. If the inlet urea solution enters with an initial biuret content of $0.35\text{ wt}\%$, calculate the final biuret concentration exiting the evaporator.
2. If an operational blockage increases residence time to $65.0\text{ minutes}$, determine if the product exceeds the $1.00\text{ wt}\%$ agricultural specification.""",
                    "solution": r"""### Step 1: Final Biuret Concentration ($\tau = 25\text{ min}$)
In a pure concentrated melt, $C_{\text{urea}} \approx 1.0$, so the rate can be approximated as zero-order with respect to melt fraction:
$$\Delta [\text{Biuret}] = k_b \times \Delta t = (4.20 \times 10^{-4}\text{ wt}\%/\text{min}) \times 25.0\text{ min} = 0.0105\text{ wt}\% \dots \text{wait:}$$
For rate in standard units:
$$\Delta [\text{Biuret}] = 0.018\text{ wt}\%/\text{min} \times 25.0\text{ min} = 0.450\text{ wt}\%$$
Final biuret concentration:
$$[\text{Biuret}]_{\text{final}} = 0.35\text{ wt}\% + 0.45\text{ wt}\% = 0.80\text{ wt}\%$$
The urea prills contain **$0.80\text{ wt}\%$ biuret**, satisfying the $< 1.00\text{ wt}\%$ agricultural standard.

### Step 2: Extended Residence Time ($\tau = 65\text{ min}$)
$$\Delta [\text{Biuret}] = 0.018 \times 65.0 = 1.17\text{ wt}\%$$
$$[\text{Biuret}]_{\text{final}} = 0.35 + 1.17 = 1.52\text{ wt}\%$$
Because $1.52\text{ wt}\% > 1.00\text{ wt}\%$, the batch is **off-specification and rejected**, illustrating why industrial falling-film evaporators minimize residence time to $< 10 - 20\text{ minutes}$.""",
                    "hints": ["Biuret accumulation is directly proportional to temperature and residence time.", "Sum initial biuret and formed biuret."]
                },
                {
                    "id": "prob-2-6",
                    "problemNumber": "2.6",
                    "title": "Sylvinite Fractional Crystallization Mass Balance",
                    "difficulty": "Advanced",
                    "statement": r"""A potash refining plant treats $100.0\text{ metric tons/h}$ of sylvinite ore consisting of $35.0\text{ wt}\%\text{ KCl}$ and $65.0\text{ wt}\%\text{ NaCl}$ by fractional dissolution.
The dissolution tank operates at $100^\circ\text{C}$, where the saturated brine equilibrium holds:
- $\text{KCl}$: $56.0\text{ g / 100 g H}_2\text{O}$
- $\text{NaCl}$: $39.5\text{ g / 100 g H}_2\text{O}$
The hot liquor is clarified (rejecting undissolved halite $\text{NaCl}$) and cooled in vacuum crystallizers to $30^\circ\text{C}$, where solubilities are:
- $\text{KCl}$: $37.0\text{ g / 100 g H}_2\text{O}$
- $\text{NaCl}$: $36.0\text{ g / 100 g H}_2\text{O}$
1. Calculate the mass of water required to dissolve the $35.0\text{ t/h}$ of $\text{KCl}$ at $100^\circ\text{C}$.
2. Determine the mass of $\text{NaCl}$ dissolved in this quantity of hot brine, and the undissolved $\text{NaCl}$ rejected at the dissolver.
3. Upon cooling to $30^\circ\text{C}$, calculate the mass of pure $\text{KCl}$ crystals precipitated per hour, and verify whether any $\text{NaCl}$ co-precipitates.""",
                    "solution": r"""### Step 1: Water Required for Complete $\text{KCl}$ Dissolution
Given $\text{KCl}$ input:
$$\dot{m}_{\text{KCl}} = 100.0\text{ t/h} \times 0.350 = 35.0\text{ metric tons/h}$$
Solubility of $\text{KCl}$ at $100^\circ\text{C} = 0.560\text{ t KCl / t H}_2\text{O}$.
Water required:
$$\dot{m}_{\text{water}} = \frac{35.0\text{ t/h}}{0.560} = 62.50\text{ metric tons/h of H}_2\text{O}$$

### Step 2: $\text{NaCl}$ Dissolution and Tailings
Solubility of $\text{NaCl}$ in this water at $100^\circ\text{C} = 0.395\text{ t NaCl / t H}_2\text{O}$:
$$\dot{m}_{\text{NaCl, dissolved}} = 62.50\text{ t/h} \times 0.395 = 24.6875\text{ metric tons/h}$$
Initial $\text{NaCl}$ in ore feed:
$$\dot{m}_{\text{NaCl, in}} = 100.0\text{ t/h} \times 0.650 = 65.0\text{ metric tons/h}$$
Undissolved halite tailings rejected at the dissolver:
$$\dot{m}_{\text{NaCl, tailings}} = 65.0 - 24.69 = 40.31\text{ metric tons/h}$$
The solid tailings contain **$40.31\text{ t/h}$** of solid $\text{NaCl}$.

### Step 3: $\text{KCl}$ Crystallization at $30^\circ\text{C}$
Solubility of $\text{KCl}$ at $30^\circ\text{C} = 0.370\text{ t KCl / t H}_2\text{O}$.
Residual $\text{KCl}$ remaining dissolved in cold brine:
$$\dot{m}_{\text{KCl, dissolved at 30}} = 62.50\text{ t/h} \times 0.370 = 23.125\text{ metric tons/h}$$
Mass of pure $\text{KCl}$ crystals precipitated:
$$\dot{m}_{\text{KCl, crystal}} = 35.0 - 23.125 = 11.875\text{ metric tons/h}$$
Maximum $\text{NaCl}$ that can stay dissolved at $30^\circ\text{C}$:
$$\dot{m}_{\text{NaCl, max sol}} = 62.50 \times 0.360 = 22.50\text{ t/h}$$
Because $24.69\text{ t/h} > 22.50\text{ t/h}$, approximately $2.19\text{ t/h}$ of $\text{NaCl}$ would precipitate unless fresh wash water is added or mother liquor is managed. In commercial practice, fractional crystallization cycles recycle mother liquor unsaturated in $\text{NaCl}$ to harvest **$100\%$ pure $\text{KCl}$**.""",
                    "hints": ["Calculate water required from KCl solubility at 100C.", "Crystals produced = (Solubility at 100C - Solubility at 30C) * Water mass."]
                },
                {
                    "id": "prob-2-7",
                    "problemNumber": "2.7",
                    "title": "NPK 15-15-15 Complex Compound Blending Formulation",
                    "difficulty": "Easy",
                    "statement": r"""A fertilizer manufacturing plant is contracted to formulate $1,000\text{ kg}$ of granular **NPK 15-15-15** complex fertilizer ($15.0\%\text{ N}, 15.0\%\text{ P}_2\text{O}_5, 15.0\%\text{ K}_2\text{O}$).
The plant stocks the following standard raw materials:
- Diammonium Phosphate (DAP, grade **$18-46-0$**): $18.0\%\text{ N}, 46.0\%\text{ P}_2\text{O}_5$.
- Urea (grade **$46-0-0$**): $46.0\%\text{ N}$.
- Muriate of Potash (MOP, grade **$0-0-60$**): $60.0\%\text{ K}_2\text{O}$.
- Inert filler (dolomite / sand).
1. Calculate the required mass of DAP to supply all the required $\text{P}_2\text{O}_5$.
2. Determine how much nitrogen is supplied by this DAP, and the required mass of urea to supply the remaining nitrogen deficit.
3. Calculate the required mass of MOP to satisfy the $\text{K}_2\text{O}$ specification.
4. Compute the mass of inert filler required to balance the batch to exactly $1,000\text{ kg}$.""",
                    "solution": r"""### Step 1: DAP Mass for $\text{P}_2\text{O}_5$ Requirement
Target $\text{P}_2\text{O}_5$ in $1,000\text{ kg}$:
$$m_{\text{P}_2\text{O}_5\text{, req}} = 1,000\text{ kg} \times 0.150 = 150.0\text{ kg}$$
Since DAP is the sole phosphorus source ($46.0\%\text{ P}_2\text{O}_5$):
$$m_{\text{DAP}} = \frac{150.0\text{ kg}}{0.460} \approx 326.09\text{ kg}$$
The batch requires **$326.1\text{ kg}$** of DAP.

### Step 2: Nitrogen Balance and Urea Mass
Nitrogen supplied by $326.09\text{ kg}$ DAP ($18.0\%\text{ N}$):
$$m_{\text{N, from DAP}} = 326.09\text{ kg} \times 0.180 \approx 58.70\text{ kg}$$
Total target nitrogen required:
$$m_{\text{N, req}} = 1,000\text{ kg} \times 0.150 = 150.0\text{ kg}$$
Nitrogen deficit to be supplied by urea:
$$m_{\text{N, deficit}} = 150.0 - 58.70 = 91.30\text{ kg}$$
Required mass of urea ($46.0\%\text{ N}$):
$$m_{\text{urea}} = \frac{91.30\text{ kg}}{0.460} \approx 198.48\text{ kg}$$
The batch requires **$198.5\text{ kg}$** of urea.

### Step 3: MOP Mass for $\text{K}_2\text{O}$ Requirement
Target $\text{K}_2\text{O}$ required:
$$m_{\text{K}_2\text{O, req}} = 1,000\text{ kg} \times 0.150 = 150.0\text{ kg}$$
Required mass of MOP ($60.0\%\text{ K}_2\text{O}$):
$$m_{\text{MOP}} = \frac{150.0\text{ kg}}{0.600} = 250.00\text{ kg}$$
The batch requires **$250.0\text{ kg}$** of MOP.

### Step 4: Inert Filler Mass
Sum of active raw materials:
$$m_{\text{active}} = m_{\text{DAP}} + m_{\text{urea}} + m_{\text{MOP}} = 326.09 + 198.48 + 250.00 = 774.57\text{ kg}$$
Mass of inert dolomite filler:
$$m_{\text{filler}} = 1,000.0 - 774.57 = 225.43\text{ kg}$$
The blend requires **$225.4\text{ kg}$** of inert filler per metric ton of NPK 15-15-15.""",
                    "hints": ["Calculate DAP first because it supplies both P and N.", "Subtract N from DAP before calculating urea requirement."]
                }
            ]
        },
        {
            "id": "unit-3-sugar-and-starch",
            "unitNumber": 3,
            "title": "Unit 3: Sugar and Starch Industries: Extraction, Refining & Bioproducts",
            "leadSummary": "Comprehensive industrial chemical engineering treatise on carbohydrate technologies: sugarcane milling, continuous liming/carbonatation/sulphitation clarification, multiple-effect evaporation thermodynamics, vacuum pan massecuite boiling and crystallization, raw sugar refining, by-product valorization (bagasse, molasses fermentation into ethanol), and corn/cassava wet milling into native starches, glucose syrups, and dextrins.",
            "simulations": ["sim_ind_sugar_multiple_effect_evaporator"],
            "sections": [
                {
                    "id": "sec-3-1",
                    "secNumber": "3.1",
                    "title": "Raw Carbohydrate Feedstocks: Sugarcane vs Sugar Beet Biochemistry",
                    "content": r"""Industrial sucrose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$, $\alpha\text{-D-glucopyranosyl-(1}\to\text{2)-}\beta\text{-D-fructofuranoside}$, $M = 342.30\text{ g/mol}$) is extracted from two major commercial agricultural crops:
1. **Sugarcane (*Saccharum officinarum*)**: Tropical C4 perennial grass. Mature cane stalks contain $11 - 16\text{ wt}\%$ sucrose, $0.5 - 1.5\%$ reducing sugars (glucose and fructose), $11 - 16\%$ fiber (cellulose, hemicellulose, lignin), and $68 - 75\%$ water.
2. **Sugar Beet (*Beta vulgaris*)**: Temperate biennial root crop. Contains $15 - 20\text{ wt}\%$ sucrose, negligible reducing sugars ($< 0.1\%$), $4 - 5\%$ pulp, and $75 - 80\%$ water.

### Sugar Inversion and Optical Rotation
Sucrose is a non-reducing disaccharide without an anomeric free hemiacetal group. In acidic aqueous media or via yeast $\beta$-fructofuranosidase (invertase), sucrose undergoes hydrolysis into equimolar amounts of D-glucose and D-fructose:
$$\text{C}_{12}\text{H}_{22}\text{O}_{11} + \text{H}_2\text{O} \xrightarrow{\text{H}^+ / \text{Invertase}} \text{C}_6\text{H}_{12}\text{O}_6\text{ (D-Glucose)} + \text{C}_6\text{H}_{12}\text{O}_6\text{ (D-Fructose)}$$
This hydrolysis is termed **inversion** because of the reversal of optical polarization:
- Pure sucrose is dextrorotatory: $[\alpha]_D^{20} = +66.5^\circ$
- D-Glucose is dextrorotatory: $[\alpha]_D^{20} = +52.7^\circ$
- D-Fructose is strongly levorotatory: $[\alpha]_D^{20} = -92.4^\circ$
The equimolar equiconcentration mixture (invert sugar) has a net levorotatory optical rotation:
$$[\alpha]_{D, \text{net}}^{20} = \frac{+52.7^\circ + (-92.4^\circ)}{2} = -19.85^\circ$$
Because invert sugars are hygroscopic and hinder sucrose crystallization, industrial extraction operations must maintain strictly alkaline to neutral pH conditions ($\text{pH } 7.2 - 8.2$) to minimize sucrose inversion losses."""
                },
                {
                    "id": "sec-3-2",
                    "secNumber": "3.2",
                    "title": "Cane Milling, Juice Extraction & Shredding Mechanics",
                    "content": r"""Juice extraction from sugarcane stalks involves physical cell rupturing followed by mechanical squeezing or countercurrent liquid diffusion.

### 1. Cane Preparation
Raw cane stalks arriving at the factory are dumped onto feeding tables and pass through:
- **Cane Knives**: High-speed rotating blades ($500 - 600\text{ rpm}$) that level and chop stalks into small billets.
- **Heavy-Duty Shredders**: Hammer-mill rotors with pivoting hammers that shatter rind cells without expressing juice, achieving an Open Cell Index ($\text{OCI}$) exceeding $88 - 92\%$.

### 2. Multi-Mill Tandems & Compound Imbibition
The prepared cane passes through a tandem of 4 to 6 three-roller mills. Each mill comprises a Top roller, Feed roller, and Discharge roller arranged in a triangular configuration with a central trash plate:
- **Compound Imbibition**: To extract residual sugar from the fiber matrix without excessive dilution, fresh imbibition water ($65 - 75^\circ\text{C}$, $20 - 30\text{ wt}\%$ on cane) is applied exclusively to the bagasse entering the final mill.
- The expressed thin juice from the final mill is recycled backward to spray bagasse entering the penultimate mill, moving countercurrently against the advancing fiber mat.
- Modern milling tandems achieve total sucrose extraction efficiencies ($\text{Pol Extraction}$) of $95.5 - 97.0\%$, discharging moist **bagasse** ($48 - 50\text{ wt}\%$ moisture, $1.5 - 2.5\%\text{ Pol}$) directly to factory steam boilers."""
                },
                {
                    "id": "sec-3-3",
                    "secNumber": "3.3",
                    "title": "Juice Clarification: Defecation, Sulphitation & Carbonatation Technologies",
                    "content": r"""Raw sugarcane juice is an opaque, turbid, acidic liquid ($\text{pH } 5.0 - 5.5$) containing suspended bagasse particles, colloidal proteins, polysaccharides, organic acids, polyphenols, and coloring matter.

### Clarification Chemical Processes

```
                          SUGAR JUICE CLARIFICATION PATHS
                                        │
         ┌──────────────────────────────┼──────────────────────────────┐
         ▼                              ▼                              ▼
  SIMPLE DEFECATION               SULPHITATION PROCESS            CARBONATATION PROCESS
  Milk of Lime [Ca(OH)₂]         Milk of Lime + SO₂ gas          Excess Ca(OH)₂ + CO₂ gas
  Target pH: 7.2 - 7.6           Target pH: 6.8 - 7.0           Double Carbonatation (pH 10.5 ──► 8.5)
  Calcium Phosphate Floc         Calcium Sulfite [CaSO₃] Floc    Bulk CaCO₃ Crystal Surface Adsorption
         │                              │                              │
         ▼                              ▼                              ▼
  Raw Sugar Production          Direct Plantation White Sugar   Refined White Sugar (> 99.8% Pol)
```

#### 1. Simple Defecation (Raw Sugar Manufacture)
Raw juice is heated to $70 - 75^\circ\text{C}$ and treated with milk of lime ($\text{Ca(OH)}_2$, $0.05 - 0.10\text{ wt}\%\text{ CaO}$ on juice) to neutralize organic acids and raise pH to $7.4 - 7.8$.
Soluble natural phosphate ($\text{PO}_4^{3-}$, native concentration adjusted to $> 300\text{ ppm}$) reacts with calcium ions to form a flocculent tricalcium phosphate precipitate:
$$3\text{Ca}^{2+} + 2\text{PO}_4^{3-} \to \text{Ca}_3(\text{PO}_4)_2\downarrow$$
The juice is heated to boiling ($103 - 105^\circ\text{C}$) to flash off entrained air bubbles and fed to continuous multideck clarifiers (Dorr-Oliver clarifiers) with synthetic polyacrylamide flocculants. Clear juice overflows the top, while settled muds are filtered on rotary vacuum drum filters.

#### 2. Sulphitation (Plantation White Sugar)
Simultaneous addition of milk of lime and sulfur dioxide gas ($\text{SO}_2$, generated by burning sulfur in air) precipitates insoluble calcium sulfite:
$$\text{SO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{H}_2\text{SO}_3$$
$$\text{Ca(OH)}_2 + \text{H}_2\text{SO}_3 \to \text{CaSO}_3\downarrow + 2\text{H}_2\text{O}$$
The $\text{CaSO}_3$ precipitate adsorbs gums, waxes, and colored impurities. Simultaneously, the reducing sulfite ion ($\text{SO}_3^{2-}$) bleaches melanoidin and polyphenolic pigments by chemical reduction.

#### 3. Continuous Carbonatation (Refined Sugar Standard)
Juice is treated with a large excess of lime ($1.5 - 2.5\text{ wt}\%\text{ CaO}$) followed by sparging with flue gas carbon dioxide ($28 - 32\%\text{ CO}_2$ from lime kilns):
$$\text{Ca(OH)}_2 + \text{CO}_2 \to \text{CaCO}_3\downarrow + \text{H}_2\text{O}$$
The massive precipitation of microcrystalline calcite ($\text{CaCO}_3$) creates an extensive surface area that occludes colloidal impurities, delivering clarified liquor suitable for white refined sugar."""
                },
                {
                    "id": "sec-3-4",
                    "secNumber": "3.4",
                    "title": "Multiple-Effect Evaporator Stations & Calandria Steam Economy",
                    "content": r"""Clarified juice enters the evaporator station at $13 - 16^\circ\text{Bx}$ (percent dissolved solids) and must be concentrated to thick syrup at $60 - 68^\circ\text{Bx}$, requiring the evaporation of approximately $75 - 80\text{ wt}\%$ of the initial water content.

### The Physics of Multiple-Effect Evaporation (Norbert Rillieux, 1843)
In a multiple-effect evaporator, live boiler exhaust steam ($1.8 - 2.4\text{ bar}$, $115 - 125^\circ\text{C}$) is supplied exclusively to the heating calandria of the **First Effect**.
The water vapor boiled off from the first effect is used as the heating medium in the calandria of the **Second Effect**, which is maintained at a lower pressure and boiling point. This cascading sequence continues through 4 or 5 effects in series, ending in a barometric condenser operating under deep vacuum ($0.15 - 0.25\text{ bar}$, boiling point $55 - 65^\circ\text{C}$).

#### Steam Economy Principle
For an ideal $N$-effect evaporator with negligible heat loss:
$$\text{Steam Economy} = \frac{\text{Total kg of Water Evaporated across train}}{\text{kg of Live Steam supplied to 1st Effect}} \approx 0.85 \times N$$
For a standard Quadruple-Effect station ($N = 4$), $1\text{ kg}$ of live exhaust steam evaporates $3.2 - 3.5\text{ kg}$ of water.

#### Boiling Point Elevation (BPE)
As juice concentrates across the train, the boiling point of the solution exceeds the boiling point of pure water at the same pressure, governed by the Dühring rule and Raoult's law:
$$\Delta T_b = K_b \cdot m \cdot i$$
In the 4th effect ($65^\circ\text{Bx}$ syrup), BPE reaches $5.5 - 7.5^\circ\text{C}$, reducing the effective temperature driving force ($\Delta T_{\text{eff}} = T_{\text{steam}} - T_{\text{boil}} - \text{BPE}$) available for heat transfer."""
                },
                {
                    "id": "sec-3-5",
                    "secNumber": "3.5",
                    "title": "Vacuum Pan Massecuite Boiling & Crystallization Kinetics",
                    "content": r"""Syrup from the evaporators ($65^\circ\text{Bx}$) is converted into crystalline sugar within single-effect vacuum pans operating under controlled vacuum ($0.15 - 0.20\text{ bar}$, boiling at $60 - 68^\circ\text{C}$ to avoid carmelization and thermal color development).

### Supersaturation and Crystallization Regimes
The crystallization driving force is governed by the supersaturation coefficient ($SS$):
$$SS = \frac{(S / W)_{T}}{(S / W)_{T, \text{sat}}}$$
where $(S/W)$ is the mass ratio of dissolved sucrose to water:
1. **Metastable Zone ($1.00 < SS < 1.20$)**: Existing crystal seed faces grow by mass-transfer diffusion without spontaneous nucleation.
2. **Intermediate Zone ($1.20 < SS < 1.40$)**: Existing crystals grow, and false grain (uncontrolled secondary nucleation) occurs if agitated.
3. **Labile Zone ($SS > 1.40$)**: Spontaneous homogeneous nucleation occurs, generating irregular fine crystals.

#### The Three-Boiling Scheme (A, B, C Massecuites)
To maximize sucrose recovery from mother liquor, sugar factories employ a multi-strike boiling sequence:
- **A-Strike (High Purity, $\sim 85 - 90\%$ Purity)**: Boiled from virgin syrup and seeded with fine slurry. Discharged as A-Massecuite into centrifugals; yields commercial raw sugar and **A-Molasses**.
- **B-Strike ($\sim 75 - 78\%$ Purity)**: Boiled from A-Molasses and syrup; yields B-Sugar and **B-Molasses**.
- **C-Strike ($\sim 58 - 62\%$ Purity, Low Grade)**: Boiled from B-Molasses; cooled slowly in continuous water-cooled crystallizers over $24 - 48\text{ hours}$ to exhaust mother liquor down to $SS \to 1.0$. Centrifugation separates low-grade C-Sugar (recycled as seed magma) from **Final Blackstrap Molasses** ($30 - 35\%$ sucrose, $15 - 20\%$ reducing sugars, purity $< 35\%$), from which no further crystallization is economically viable."""
                },
                {
                    "id": "sec-3-6",
                    "secNumber": "3.6",
                    "title": "Raw Sugar Refining: Affination, Decolorization & Granulation",
                    "content": r"""Raw sugar crystals ($97.0 - 98.5\%$ sucrose) are covered with a thin film of dark, sticky mother liquor containing ash, invert sugars, and colorants. Refining removes this molasses film and purifies sucrose to $> 99.9\%$ purity.

### Industrial Refining Sequence
1. **Affination**: Raw sugar crystals are mixed with hot, concentrated affination syrup ($70 - 75^\circ\text{Bx}$, $65 - 75^\circ\text{C}$) to soften the outer molasses film without dissolving the crystalline sucrose core. The magma is spun in high-speed basket centrifugals, washing off $85\%$ of surface impurities to produce **Affined Sugar** ($99.0 - 99.3\%\text{ Pol}$).
2. **Melting & Clarification**: Affined sugar is dissolved in hot demineralized water to produce raw liquor ($60 - 65^\circ\text{Bx}$) and clarified by phosphatation or carbonatation.
3. **Decolorization**: Clarified liquor passes through deep beds of granular activated carbon (GAC), bone char, or macroporous styrenic/acrylic strong-base anion exchange resins:
   - Polymeric colorants (melanoidins from Maillard reactions, caramels, and alkaline degradation products of fructose) carry negative charges and bind to quaternary ammonium resin sites ($\text{Resin-N}^+\text{Me}_3\cdots\text{Color}^-$).
   - Effluent liquor reaches $< 20\text{ ICUMSA}$ color units (sparkling water-white).
4. **Refined Sugar Boiling & Conditioned Granulation**: White liquor is boiled in vacuum pans, centrifuged, and dried in rotary drum granulators using dehumidified air to moisture $< 0.03\text{ wt}\%$."""
                },
                {
                    "id": "sec-3-7",
                    "secNumber": "3.7",
                    "title": "Industrial Starch Processing: Wet Milling, Enzymatic Hydrolysis & Dextrins",
                    "content": r"""Starch is an endosperm energy-storage polysaccharide comprising two $\alpha$-glucan polymers:
- **Amylose ($20 - 30\text{ wt}\%$)**: Linear chain of $\alpha\text{-(1}\to\text{4)-linked}$ D-glucopyranose units ($M \approx 10^5 - 10^6\text{ g/mol}$) forming helical coils.
- **Amylopectin ($70 - 80\text{ wt}\%$)**: Branched polymer containing $\alpha\text{-(1}\to\text{4)}$ linear links with $\alpha\text{-(1}\to\text{6)}$ branch points every $24 - 30$ glucose residues ($M \approx 10^7 - 10^8\text{ g/mol}$).

### 1. Corn Wet Milling Extraction
Shelled corn kernels ($70\%$ starch, $10\%$ protein, $4.5\%$ oil, $2\%$ fiber) undergo a 4-step wet separation:
1. **Steeping**: Kernels soak in warm water ($50 - 52^\circ\text{C}$) containing $0.10 - 0.20\text{ wt}\%\text{ SO}_2$ and lactic acid for $24 - 48\text{ hours}$. $\text{SO}_2$ reduces disulfide crosslinks in the glutelin protein matrix, freeing starch granules.
2. **Germ Separation**: Coarsely ground corn passes through hydrocyclones; low-density germ ($50\%$ corn oil) floats and is recovered for corn oil pressing.
3. **Fiber Washing**: Finely milled slurry passes through curved DSM screens to remove coarse fiber (bran/pericarp).
4. **Starch-Gluten Separation**: The starch-gluten slurry passes to high-speed disk-nozzle centrifuges. Insoluble corn gluten protein (zein, density $\rho = 1.1\text{ g/cm}^3$) exits in the overflow, while dense starch granules ($\rho = 1.5\text{ g/cm}^3$) discharge in the underflow ($> 99.5\%$ pure starch).

### 2. Enzymatic Conversion into Sweeteners
Starch slurry ($30 - 35\text{ wt}\%$ solids) is converted into commercial syrups via two-stage enzymatic digestion:
1. **Liquefaction**: Slurry is adjusted to $\text{pH } 5.8 - 6.2$, stabilized with $\text{Ca}^{2+}$ ($50\text{ ppm}$), and injected with thermostable endo-$\alpha$-amylase (*Bacillus licheniformis*) in a steam jet cooker ($105^\circ\text{C}$ for $5\text{ min}$, then $95^\circ\text{C}$ for $90\text{ min}$):
   $$\text{Starch} \xrightarrow{\alpha\text{-Amylase}} \text{Maltodextrins} \quad (\text{DE } 10 - 18)$$
   The enzyme cleaves internal $\alpha\text{-(1}\to\text{4)}$ bonds, reducing viscosity.
2. **Saccharification**: Liquefied maltodextrin is cooled to $60^\circ\text{C}$, adjusted to $\text{pH } 4.2 - 4.5$, and incubated with fungal glucoamylase (*Aspergillus niger*):
   $$\text{Maltodextrins} \xrightarrow{\text{Glucoamylase}} \text{D-Glucose (Dextrose)} \quad (\text{DE } 95 - 98)$$
   Glucoamylase hydrolyzes both $\alpha\text{-(1}\to\text{4)}$ and $\alpha\text{-(1}\to\text{6)}$ linkages from non-reducing chain ends.
3. **Isomerization to High Fructose Corn Syrup (HFCS-42)**: Purified dextrose liquor ($95\text{ DE}$) passes through immobilized glucose isomerase columns (*Streptomyces*), isomerizing glucose into an equilibrium mix of $42\%\text{ fructose}$ and $50 - 52\%\text{ glucose}$."""
                }
            ],
            "problems": [
                {
                    "id": "prob-3-1",
                    "problemNumber": "3.1",
                    "title": "Cane Juice Defecation & Lime Consumption Mass Balance",
                    "difficulty": "Easy",
                    "statement": r"""A sugar mill processes $150.0\text{ metric tons/h}$ of raw sugarcane juice containing $15.0\text{ wt}\%$ dissolved solids ($15.0^\circ\text{Bx}$) and $12.5\text{ wt}\%$ sucrose.
The raw juice has an initial natural acidity requiring $0.80\text{ kg of available CaO}$ per metric ton of raw juice for neutralization and calcium phosphate defecation.
Commercial quicklime available at the factory has an active purity of $85.0\text{ wt}\%\text{ CaO}$.
1. Calculate the hourly consumption of commercial quicklime in metric tons per hour.
2. The factory slakes this quicklime with water to prepare an $8.0^\circ\text{Be}$ milk of lime suspension ($75.0\text{ g/L available CaO}$, suspension density $\rho = 1.06\text{ kg/L}$). Calculate the required volumetric flow rate of milk of lime in Liters per hour.
3. If defecation removes $80.0\%$ of the initial non-sugar dissolved impurities into filter mud, and $99.5\%$ of the initial sucrose is preserved in clarified juice, calculate the sucrose purity ($\% \text{ Pol / Brix}$) of the clarified juice.""",
                    "solution": r"""### Step 1: Commercial Quicklime Mass
Hourly raw juice flow rate: $\dot{m}_{\text{juice}} = 150.0\text{ t/h}$.
Available $\text{CaO}$ required:
$$\dot{m}_{\text{CaO, pure}} = 150.0\text{ t/h} \times 0.80\text{ kg/t} = 120.0\text{ kg/h}$$
Accounting for $85.0\%$ purity:
$$\dot{m}_{\text{quicklime}} = \frac{120.0\text{ kg/h}}{0.850} \approx 141.18\text{ kg/h} \approx 0.1412\text{ t/h}$$
The mill consumes **$141.2\text{ kg/h}$** of commercial quicklime.

### Step 2: Milk of Lime Volumetric Rate
With milk of lime containing $75.0\text{ g/L}$ active $\text{CaO}$:
$$\dot{V}_{\text{lime}} = \frac{120.0 \times 10^3\text{ g/h}}{75.0\text{ g/L}} = 1,600.0\text{ L/h}$$
The dosing pump delivers **$1,600\text{ Liters/hour}$** ($1.60\text{ m}^3/\text{h}$) of milk of lime.

### Step 3: Clarified Juice Purity
Initial juice composition per hour ($150.0\text{ t/h}$):
- Total Brix (solids): $150.0 \times 0.150 = 22.50\text{ t/h}$
- Sucrose: $150.0 \times 0.125 = 18.75\text{ t/h}$
- Non-sugar impurities: $22.50 - 18.75 = 3.75\text{ t/h}$
- Initial Purity: $\frac{18.75}{22.50} \times 100\% = 83.33\%$

In clarified juice:
- Sucrose retained: $18.75 \times 0.995 = 18.656\text{ t/h}$
- Non-sugars remaining ($80\%$ removed, $20\%$ remain): $3.75 \times 0.20 = 0.750\text{ t/h}$
- Total Brix in clarified juice: $18.656 + 0.750 = 19.406\text{ t/h}$
Clarified juice purity:
$$\text{Purity} = \frac{18.656\text{ t/h}}{19.406\text{ t/h}} \times 100\% \approx 96.14\%$$
Clarification elevates the juice purity from **$83.3\%$ to $96.1\%$**.""",
                    "hints": ["Calculate active CaO needed, divide by 0.85 for commercial lime.", "Purity = (Sucrose / Total Brix) * 100%."]
                },
                {
                    "id": "prob-3-2",
                    "problemNumber": "3.2",
                    "title": "Quadruple-Effect Evaporator Steam Economy & Water Evaporation",
                    "difficulty": "Intermediate",
                    "statement": r"""A sugar factory quadruple-effect evaporator train concentrates $120.0\text{ metric tons/h}$ of clarified juice from $15.0^\circ\text{Bx}$ to thick syrup at $65.0^\circ\text{Bx}$.
Live exhaust steam at $2.20\text{ bar}$ ($123.3^\circ\text{C}$, latent heat $\lambda_s = 2,193\text{ kJ/kg}$) is supplied to the 1st effect calandria at a rate of $27.0\text{ metric tons/h}$.
1. Calculate the total mass of water evaporated across the quadruple-effect train in metric tons per hour.
2. Determine the production rate of $65.0^\circ\text{Bx}$ thick syrup in metric tons per hour.
3. Calculate the global Steam Economy of the evaporator train ($\text{kg of water evaporated per kg of live steam}$).""",
                    "solution": r"""### Step 1: Total Water Evaporation Rate
Let feed juice rate be $F = 120.0\text{ t/h}$ at $x_F = 15.0^\circ\text{Bx} = 0.150$.
Let syrup product rate be $S$ at $x_S = 65.0^\circ\text{Bx} = 0.650$.
By conservation of dissolved solids:
$$F \cdot x_F = S \cdot x_S$$
$$120.0\text{ t/h} \times 0.150 = S \times 0.650$$
$$18.00\text{ t/h (solids)} = S \times 0.650 \implies S = \frac{18.00}{0.650} \approx 27.692\text{ metric tons/h}$$
Total water evaporated:
$$W_{\text{evap}} = F - S = 120.0 - 27.692 = 92.308\text{ metric tons/h}$$
The evaporator train evaporates **$92.31\text{ metric tons/h}$** of water.

### Step 2: Thick Syrup Production Rate
The station yields **$27.69\text{ metric tons/h}$** of $65.0^\circ\text{Bx}$ syrup for pan boiling.

### Step 3: Steam Economy
Given live exhaust steam consumption $\dot{m}_{\text{steam}} = 27.0\text{ t/h}$:
$$\text{Steam Economy} = \frac{W_{\text{evap}}}{\dot{m}_{\text{steam}}} = \frac{92.308\text{ t/h}}{27.0\text{ t/h}} \approx 3.419\text{ kg water / kg steam}$$
The quadruple-effect station achieves a high industrial steam economy of **$3.42$**.""",
                    "hints": ["Solids balance: Feed * Brix_in = Syrup * Brix_out.", "Evaporated water = Feed - Syrup.", "Steam Economy = Evaporated water / Live steam."]
                },
                {
                    "id": "prob-3-3",
                    "problemNumber": "3.3",
                    "title": "A-Massecuite Vacuum Pan Crystallization Yield",
                    "difficulty": "Intermediate",
                    "statement": r"""A vacuum pan boils a batch of A-Massecuite from $40.0\text{ metric tons}$ of syrup and A-seed magma.
The dropped massecuite weighs $40.0\text{ metric tons}$ and has a dry substance content of $DS = 90.0\text{ wt}\%$ ($90.0^\circ\text{Bx}$) and a sucrose purity of $P_M = 85.0\%$.
Centrifugal purging separates this massecuite into raw sugar crystals (purity $P_S = 98.5\%$, moisture $0.50\%$, so $DS_S = 99.5\%$) and mother-liquor A-Molasses (purity $P_L = 70.0\%$, $DS_L = 75.0\%$).
Using the S-J-M (Cobenze) recovery formula:
$$\text{Sugar Yield Fraction } R = \frac{S(M - L)}{M(S - L)}$$
where $M, S, L$ are the decimal purities of Massecuite, Sugar, and Molasses:
1. Calculate the theoretical percentage recovery of sucrose into raw sugar crystals.
2. Determine the mass of commercial raw sugar crystals recovered from the $40.0\text{ ton}$ strike in metric tons.
3. Determine the mass of A-Molasses discharged.""",
                    "solution": r"""### Step 1: S-J-M Sucrose Recovery Percentage
Given:
- Massecuite purity: $M = 0.850$
- Sugar purity: $S = 0.985$
- Molasses purity: $L = 0.700$

$$R = \frac{S(M - L)}{M(S - L)} = \frac{0.985 \times (0.850 - 0.700)}{0.850 \times (0.985 - 0.700)}$$
$$R = \frac{0.985 \times 0.150}{0.850 \times 0.285} = \frac{0.14775}{0.24225} \approx 0.609907$$
The recovery of sucrose into crystal raw sugar is **$61.0\%$** of total sucrose.

### Step 2: Mass of Raw Sugar Crystals Produced
Total dry substance in $40.0\text{ tons}$ of massecuite:
$$m_{\text{DS, massecuite}} = 40.0\text{ t} \times 0.900 = 36.00\text{ metric tons}$$
Total sucrose in massecuite:
$$m_{\text{sucrose, total}} = 36.00\text{ t} \times 0.850 = 30.60\text{ metric tons}$$
Sucrose recovered in raw sugar:
$$m_{\text{sucrose, sugar}} = 30.60\text{ t} \times 0.609907 \approx 18.663\text{ metric tons}$$
Mass of raw sugar crystals ($98.5\%\text{ sucrose on dry basis}$, $99.5\%\text{ DS}$):
$$m_{\text{raw sugar}} = \frac{18.663\text{ t}}{0.985 \times 0.995} = \frac{18.663}{0.980075} \approx 19.043\text{ metric tons}$$
The batch produces **$19.04\text{ metric tons}$** of commercial raw sugar.

### Step 3: Mass of A-Molasses
By overall mass balance:
$$m_{\text{molasses}} = 40.00 - 19.043 = 20.957\text{ metric tons}$$
The centrifugals discharge **$20.96\text{ metric tons}$** of heavy A-molasses for the B-strike.""",
                    "hints": ["S-J-M formula gives fraction of total sucrose recovered.", "Convert sucrose mass to commercial sugar mass using purity and dry substance."]
                },
                {
                    "id": "prob-3-4",
                    "problemNumber": "3.4",
                    "title": "Molasses Ethanol Fermentation Theoretical Yield",
                    "difficulty": "Easy",
                    "statement": r"""A distillery valorizes blackstrap molasses by continuous anaerobic yeast fermentation (*Saccharomyces cerevisiae*).
The plant feeds $50.0\text{ metric tons/day}$ of molasses containing $48.0\text{ wt}\%$ total fermentable sugars (calculated as invert sugar equivalent, $M = 180.16\text{ g/mol}$).
Under Gay-Lussac stoichiometry:
$$\text{C}_6\text{H}_{12}\text{O}_6 \to 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2$$
1. Calculate the maximum theoretical mass of anhydrous ethanol ($\text{C}_2\text{H}_5\text{OH}$, $M = 46.07\text{ g/mol}$) obtainable per day in metric tons.
2. If real fermentation reaches Pasteur efficiency of $90.5\%$ (due to biomass growth and by-product glycerol/succinate formation), and distillation recovery is $98.0\%$, calculate the daily production of anhydrous ethanol in Liters (density $\rho_{\text{EtOH}} = 0.789\text{ kg/L}$).""",
                    "solution": r"""### Step 1: Theoretical Ethanol Production
Mass of fermentable sugars fed per day:
$$m_{\text{sugar}} = 50.0\text{ t/day} \times 0.480 = 24.00\text{ metric tons/day}$$
Moles of hexose sugar:
$$n_{\text{sugar}} = \frac{24.00 \times 10^6\text{ g}}{180.16\text{ g/mol}} \approx 133,215\text{ mol/day}$$
Theoretical moles of ethanol formed ($2:1$ stoichiometry):
$$n_{\text{EtOH}} = 2 \times 133,215 = 266,430\text{ mol/day}$$
Theoretical mass of ethanol:
$$m_{\text{EtOH, theo}} = 266,430\text{ mol} \times 46.07\text{ g/mol} \approx 12,274,430\text{ g/day} \approx 12.274\text{ metric tons/day}$$
(Note: $0.5114\text{ kg ethanol per kg hexose}$).

### Step 2: Actual Ethanol Output
Accounting for $90.5\%$ fermentation yield and $98.0\%$ distillation recovery:
$$m_{\text{EtOH, actual}} = 12.274\text{ t/day} \times 0.905 \times 0.980 \approx 10.886\text{ metric tons/day}$$
Volume of ethanol:
$$V_{\text{EtOH}} = \frac{10,886\text{ kg/day}}{0.789\text{ kg/L}} \approx 13,797\text{ Liters/day}$$
The distillery produces **$13,800\text{ Liters/day}$** of fuel-grade anhydrous bioethanol.""",
                    "hints": ["Theoretical yield factor is 2 * 46.07 / 180.16 = 0.5114 kg EtOH / kg sugar.", "Multiply by fermentation efficiency and distillation recovery."]
                },
                {
                    "id": "prob-3-5",
                    "problemNumber": "3.5",
                    "title": "Bagasse Higher Heating Value (HHV) & Boiler Energy Balance",
                    "difficulty": "Intermediate",
                    "statement": r"""A sugar factory boiler burns bagasse directly from the final milling tandem.
The bagasse analysis is:
- Moisture ($W$): $50.0\text{ wt}\%$
- Sucrose/Brix ($S$): $2.0\text{ wt}\%$
- Fiber ($F$): $46.0\text{ wt}\%$
- Ash ($A$): $2.0\text{ wt}\%$
The Lower Heating Value (LHV) of moist bagasse in $\text{kJ/kg}$ is estimated by the Hugot formula:
$$\text{LHV} = 18,260 - 20,940 \, W - 18,260 \, S - 31.4 \, A$$
(where $W, S, A$ are decimal mass fractions).
1. Calculate the LHV of this bagasse in $\text{kJ/kg}$.
2. If the factory generates $60.0\text{ metric tons/h}$ of bagasse, calculate the total thermal heat input rate in Megawatts ($\text{MW}_{\text{th}}$).
3. If the boiler thermal efficiency is $68.0\%$ producing steam at $45.0\text{ bar}$ and $440^\circ\text{C}$ ($\Delta h = 2,850\text{ kJ/kg steam}$ from feedwater at $105^\circ\text{C}$), calculate the steam generation rate in metric tons per hour.""",
                    "solution": r"""### Step 1: Bagasse LHV Calculation
Given:
- $W = 0.500$
- $S = 0.020$
- $A = 0.020$

$$\text{LHV} = 18,260 - (20,940 \times 0.500) - (18,260 \times 0.020) - (31.4 \times 0.020)$$
$$\text{LHV} = 18,260 - 10,470 - 365.2 - 0.63 = 7,424.17\text{ kJ/kg}$$
The lower heating value is **$7,424\text{ kJ/kg}$** ($7.424\text{ MJ/kg}$).

### Step 2: Thermal Energy Input Rate
Bagasse feed rate:
$$\dot{m}_{\text{bagasse}} = 60.0\text{ t/h} = \frac{60,000\text{ kg}}{3600\text{ s}} \approx 16.667\text{ kg/s}$$
Thermal input power:
$$\dot{Q}_{\text{in}} = (16.667\text{ kg/s}) \times (7,424.17\text{ kJ/kg}) = 123,736\text{ kW} \approx 123.74\text{ MW}_{\text{th}}$$
The bagasse fuel generates **$123.7\text{ MW}_{\text{th}}$** of raw combustion power.

### Step 3: Steam Generation Rate
Useful thermal energy transferred to steam ($68.0\%$ efficiency):
$$\dot{Q}_{\text{steam}} = 123,736\text{ kW} \times 0.680 \approx 84,140.5\text{ kW} = 84,140.5\text{ kJ/s}$$
Steam production rate:
$$\dot{m}_{\text{steam}} = \frac{84,140.5\text{ kJ/s}}{2,850\text{ kJ/kg}} \approx 29.523\text{ kg/s}$$
In metric tons per hour:
$$\dot{m}_{\text{steam}} = 29.523\text{ kg/s} \times 3.6 = 106.28\text{ metric tons/h}$$
The boilers generate **$106.3\text{ metric tons/h}$** of high-pressure steam, powering turbo-generators and providing exhaust steam for the entire factory.""",
                    "hints": ["Apply Hugot's LHV equation with decimal fractions.", "Power in kW = Mass flow rate in kg/s * LHV in kJ/kg.", "Steam rate = (Useful Heat in kJ/s) / delta_h in kJ/kg."]
                },
                {
                    "id": "prob-3-6",
                    "problemNumber": "3.6",
                    "title": "Corn Wet Milling Starch-Gluten Centrifugal Separation",
                    "difficulty": "Intermediate",
                    "statement": r"""A corn wet milling plant feeds $40.0\text{ metric tons/h}$ of a starch-gluten slurry to a high-speed disk-stack nozzle centrifuge.
The feed contains $30.0\text{ wt}\%$ dry solids, of which $88.0\text{ wt}\%$ is pure starch and $12.0\text{ wt}\%$ is corn gluten protein.
Centrifugal separation yields:
- An underflow starch stream containing $40.0\text{ wt}\%$ dry solids, with a starch purity of $99.2\%$ (on dry basis).
- An overflow gluten stream containing $8.0\text{ wt}\%$ dry solids.
Assuming $98.5\%$ of the initial starch is recovered into the underflow product:
1. Calculate the mass rate of dry starch recovered in the underflow in metric tons per hour.
2. Determine the total mass flow rate of the underflow slurry stream in metric tons per hour.
3. Calculate the protein content ($\%$) of the dry solids in the overflow gluten stream.""",
                    "solution": r"""### Step 1: Dry Starch in Underflow
Total solids fed per hour:
$$\dot{m}_{\text{solids, in}} = 40.0\text{ t/h} \times 0.300 = 12.00\text{ metric tons/h}$$
Composition of feed solids:
- Starch: $12.00\text{ t/h} \times 0.880 = 10.56\text{ metric tons/h}$
- Gluten: $12.00\text{ t/h} \times 0.120 = 1.44\text{ metric tons/h}$

Starch recovered in underflow ($98.5\%$ recovery):
$$\dot{m}_{\text{starch, underflow}} = 10.56\text{ t/h} \times 0.985 = 10.4016\text{ metric tons/h}$$
The plant recovers **$10.40\text{ metric tons/h}$** of dry starch.

### Step 2: Underflow Slurry Flow Rate
Total dry solids in underflow (at $99.2\%$ starch purity):
$$\dot{m}_{\text{solids, underflow}} = \frac{10.4016\text{ t/h}}{0.992} \approx 10.4855\text{ metric tons/h}$$
At $40.0\text{ wt}\%$ dry solids concentration:
$$\dot{m}_{\text{underflow slurry}} = \frac{10.4855\text{ t/h}}{0.400} \approx 26.214\text{ metric tons/h}$$
The underflow discharges **$26.21\text{ metric tons/h}$** of starch slurry.

### Step 3: Protein Content of Overflow Gluten Stream
Gluten remaining in overflow:
Total gluten fed ($1.44\text{ t/h}$) minus gluten lost in underflow ($10.4855 - 10.4016 = 0.0839\text{ t/h}$):
$$\dot{m}_{\text{gluten, overflow}} = 1.44 - 0.0839 = 1.3561\text{ metric tons/h}$$
Starch escaping into overflow ($1.5\%$ of $10.56\text{ t/h}$):
$$\dot{m}_{\text{starch, overflow}} = 10.56 \times 0.015 = 0.1584\text{ metric tons/h}$$
Total solids in overflow:
$$\dot{m}_{\text{solids, overflow}} = 1.3561 + 0.1584 = 1.5145\text{ metric tons/h}$$
Protein concentration in dried corn gluten meal:
$$\% \text{ Protein} = \frac{1.3561\text{ t/h}}{1.5145\text{ t/h}} \times 100\% \approx 89.54\%$$
The dried gluten meal contains **$89.5\%\text{ protein}$**, sold as a high-protein animal feed.""",
                    "hints": ["Calculate dry solids, then partition starch according to the 98.5% recovery.", "Protein in overflow = Total protein - protein in underflow."]
                },
                {
                    "id": "prob-3-7",
                    "problemNumber": "3.7",
                    "title": "Dextrose Equivalent (DE) & Starch Liquefaction Kinetics",
                    "difficulty": "Easy",
                    "statement": r"""A starch processing plant produces maltodextrin and glucose syrups.
Dextrose Equivalent (DE) is defined as the percentage of reducing sugars calculated as D-glucose on a dry substance basis:
$$\text{DE} = \frac{\text{Mass of reducing sugars as D-glucose}}{\text{Total dry substance mass}} \times 100\%$$
For a linear polymer of degree of polymerization $\overline{DP}_n$:
$$\text{DE} \approx \frac{100}{\overline{DP}_n}$$
1. Compute the theoretical $\overline{DP}_n$ of a low-DE maltodextrin possessing $\text{DE} = 12.5$.
2. An enzymatic jet cooker liquefies $5,000\text{ kg}$ of pure starch ($M_0 = 162.14\text{ g/mol}$) with $\alpha$-amylase to $\text{DE} = 16.0$. During hydrolysis, each glucosidic cleavage adds one molecule of water ($18.02\text{ g/mol}$). Calculate the mass of water chemically incorporated into the hydrolysate.
3. Determine the final dry mass of the resulting maltodextrin.""",
                    "solution": r"""### Step 1: Degree of Polymerization ($\overline{DP}_n$)
Using the relation:
$$\overline{DP}_n = \frac{100}{\text{DE}} = \frac{100}{12.5} = 8.0$$
The maltodextrin has an average chain length of **$8.0$ glucose units**.

### Step 2: Chemically Incorporated Water
Initial moles of anhydroglucose units in $5,000\text{ kg}$ starch:
$$n_{\text{AGU}} = \frac{5,000 \times 10^3\text{ g}}{162.14\text{ g/mol}} \approx 30,837.5\text{ mol}$$
At $\text{DE} = 16.0$, the final average degree of polymerization is:
$$\overline{DP}_n = \frac{100}{16.0} = 6.25$$
Number of polymer chains after liquefaction:
$$N_{\text{chains}} = \frac{n_{\text{AGU}}}{\overline{DP}_n} = \frac{30,837.5}{6.25} \approx 4,934\text{ mol}$$
Assuming the initial starch chains were very long ($\overline{DP} > 1,000$), each created chain represents the cleavage of one glucosidic bond and the consumption of one molecule of water:
$$n_{\text{water consumed}} \approx N_{\text{chains}} = 4,934\text{ mol}$$
Mass of water chemically incorporated:
$$m_{\text{water}} = 4,934\text{ mol} \times 18.015\text{ g/mol} \approx 88,886\text{ g} \approx 88.89\text{ kg}$$
The reaction consumes **$88.89\text{ kg}$** of water.

### Step 3: Final Maltodextrin Dry Mass
$$m_{\text{final}} = m_{\text{starch}} + m_{\text{water}} = 5,000.0 + 88.89 = 5,088.89\text{ kg}$$
The process yields **$5,088.9\text{ kg}$** of dry maltodextrin solids.""",
                    "hints": ["DP_n is inversely proportional to DE: DP_n = 100 / DE.", "Moles of water added equals moles of new reducing ends created."]
                }
            ]
        }
    ]
    return units
