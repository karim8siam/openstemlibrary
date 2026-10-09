#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_natural_products_units_1_2_3.py
Builds Units 1, 2, and 3 (Sections 1-7, Solved Problems 1-7) for Chemistry of Natural Products.
Strictly zero course numbers, codes, or marks.
Raw triple quotes used throughout to prevent any escape sequence issues.
"""

def get_units_1_2_3():
    units = []

    # =========================================================================
    # UNIT 1: Foundations of Natural Products & Biosynthetic Pathways
    # =========================================================================
    u1 = {
        "id": "unit-1",
        "unitNumber": 1,
        "title": "Unit 1: Foundations of Natural Products & Biosynthetic Pathways",
        "leadSummary": "Comprehensive foundations of secondary metabolite biochemistry: ecological and evolutionary drivers of chemical diversity, systematic taxonomy of natural scaffolds, solvent and supercritical fluid separation thermodynamics, and primary-to-secondary metabolic flux routing across the Mevalonic Acid (MVA), 2-C-Methyl-D-erythritol 4-Phosphate (MEP/DOXP), and Shikimic Acid pathways.",
        "simulations": ["sim_nat_biosynthetic_pathway_tracer"],
        "sections": [
            {
                "id": "sec-1-1",
                "secNumber": "1.1",
                "title": "Natural Products: Definition, Historical Evolution & Ecological Significance",
                "content": r"""Natural products are organic molecules synthesized by living organisms that typically possess intricate stereochemical architectures and specialized biological activities. Historically spanning herbal pharmacopeias to modern structural biology, natural products represent the foundational crucible of organic chemistry and medicinal discovery.

### Historical Evolution
The formal discipline of natural products chemistry originated in the early 19th century with the isolation of pure crystalline active principles from botanical matrices:
1. **Morphine Isolation (1804–1817)**: Friedrich Sertürner isolated morphine from opium (*Papaver somniferum*), recognizing it as an alkaline, nitrogenous base ('alkaloid'), which overturned the dogma that plant constituents were exclusively acidic or neutral.
2. **Quinine, Caffeine, and Strychnine (1820s)**: Pierre-Joseph Pelletier and Joseph-Bienaimé Caventou systematically isolated quinine (*Cinchona* bark), strychnine (*Strychnos nux-vomica*), and caffeine (*Coffea arabica*), establishing alkaloid extraction protocols.
3. **Synthesis and Structural Proof**: The late 19th and early 20th centuries were defined by degradative structural proofs (Baeyer, Emil Fischer, Robert Robinson, Richard Willstätter) and milestone total syntheses, proving that natural molecules obey the universal laws of covalent bonding and thermodynamics.

### Ecological and Evolutionary Dimensions
Unlike primary metabolic machinery, which is ubiquitous and invariant across life, secondary metabolites exhibit restricted taxonomic distributions. Their evolutionary emergence is driven by ecological selection pressures:
- **Allelopathy and Plant Competition**: Secretion of phytotoxic compounds into the rhizosphere (e.g., juglone from *Juglans nigra*) suppresses seedling germination of competing flora.
- **Chemical Defense against Herbivory and Pathogens**: Phytoalexins (induced upon microbial assault), bitter sesquiterpene lactones, and neurotoxic alkaloids act as deterrents or toxins against herbivores.
- **Mutualistic Signaling**: Floral monoterpenes and anthocyanin pigments mediate pollinator attraction, while legume flavonoids activate bacterial nodulation genes (*nod* genes) in nitrogen-fixing *Rhizobium* symbioses."""
            },
            {
                "id": "sec-1-2",
                "secNumber": "1.2",
                "title": "Primary vs Secondary Metabolites: Energetic Divergence & Defense Functions",
                "content": r"""Living organisms operate dual metabolic networks: primary metabolism, sustaining universal cellular vitality, and secondary (specialized) metabolism, facilitating organismal survival within complex ecological niches.

### Fundamental Comparative Criteria
The divergence between primary and secondary metabolism can be formalized along structural, energetic, and genetic axes:

| Criterion | Primary Metabolites | Secondary (Specialized) Metabolites |
| :--- | :--- | :--- |
| **Distribution** | Universal across all living taxa | Highly species- or clade-specific |
| **Physiological Function** | Direct role in growth, replication, glycolysis, TCA cycle | Ecological defense, signaling, symbiosis, allelopathy |
| **Essentiality** | Loss-of-function is lethal under standard conditions | Organism remains viable in sterile monoculture; fitness loss in wild |
| **Structural Diversity** | Conservative, modular building blocks (20 amino acids, 5 nucleobases) | Extreme chemical complexity, fused polycycles, non-standard stereocenters |
| **Biosynthetic Origin** | Core catabolic/anabolic energy flux | Branch points draining primary pathway intermediates |

### Bioenergetic Costs and Trade-Offs
Specialized metabolites impose substantial bioenergetic burdens on host cells:
$$\Delta G_{\text{defense}} = \sum \Delta G_{\text{synthesis}} + \sum \Delta G_{\text{transport}} + \sum \Delta G_{\text{auto-resistance}}$$
Plants and microbes balance these metabolic expenditures through strictly regulated transcriptional cascades, compartmentalization within specialized organelles (e.g., glandular trichomes, resin ducts, vacuolar storage), and the synthesis of non-toxic pro-drugs (e.g., cyanogenic glycosides) activated only upon mechanical tissue disruption."""
            },
            {
                "id": "sec-1-3",
                "secNumber": "1.3",
                "title": "Classification Architectures: Biosynthetic Origins & Carbon Skeletons",
                "content": r"""The structural vastness of natural products is categorized systematically based on the fundamental biosynthetic pathways and primary metabolic precursors from which their carbon skeletons originate.

### Major Biosynthetic Classes
1. **Terpenoids (Isoprenoids)**: Derived from the assembly of five-carbon ($C_5$) isoprene units: isopentenyl pyrophosphate (IPP) and dimethylallyl pyrophosphate (DMAPP). Class covers monoterpenes ($C_{10}$), sesquiterpenes ($C_{15}$), diterpenes ($C_{20}$), triterpenes ($C_{30}$), and tetraterpenes ($C_{40}$).
2. **Phenylpropanoids and Shikimate Metabolites**: Formed from phosphoenolpyruvate (PEP) and D-erythrose 4-phosphate via chorismic acid. Includes cinnamic acids, coumarins, lignans, flavonoids, and aromatic amino acids.
3. **Polyketides**: Assembled by iterative decarboxylative condensation of acyl-CoA thioesters (acetyl-CoA, malonyl-CoA, methylmalonyl-CoA) mediated by polyketide synthases (PKS). Includes macrolides, anthraquinones, tetracyclines, and polyethers.
4. **Alkaloids**: Nitrogen-containing secondary metabolites, predominantly heterocyclic, derived from proteinogenic amino acids (L-ornithine, L-lysine, L-tyrosine, L-tryptophan, L-histidine) or purines.
5. **Carbohydrates**: Polyhydroxy aldehydes or ketones and their condensed oligomeric and polymeric forms, functioning in structural scaffolding (cellulose) and metabolic storage (starch, glycogen).
6. **Lipids and Steroids**: Hydrophobic molecules derived from fatty acyl thioesters or the triterpenoid cyclization of squalene, featuring fused sterane (cyclopentanoperhydrophenanthrene) frameworks."""
            },
            {
                "id": "sec-1-4",
                "secNumber": "1.4",
                "title": "Extraction and Isolation: Solvent Fractionation, Steam Distillation & $sc\\text{CO}_2$",
                "content": r"""The isolation of natural products requires rigorous extraction techniques tailored to the thermolability, polarity, and chemical matrix of the raw biomass.

### Solid-Liquid Solvent Fractionation
Classical isolation employs a polarity gradient extraction scheme. Dried plant material is extracted successively with solvents of increasing dielectric constant:
$$n\text{-Hexane / Pet Ether} \xrightarrow{\text{Non-polar lipids, terpenes}} \text{Dichloromethane / } \text{CHCl}_3 \xrightarrow{\text{Medium alkaloids, aglycones}} \text{EtOAc / Acetone} \xrightarrow{\text{Glycosides, flavonoids}} \text{MeOH / } \text{H}_2\text{O}$$

### Steam Distillation Thermodynamics
For volatile, water-insoluble essential oils (monoterpenes and sesquiterpenes), steam distillation enables codistillation below the thermal decomposition temperatures of the constituents. According to Dalton's Law of Partial Pressures:
$$P_{\text{total}} = P_w^\circ(T) + P_o^\circ(T)$$
Boiling occurs when $P_{\text{total}} = P_{\text{atm}} = 101.325\text{ kPa}$. Because $P_w^\circ(T) < P_{\text{atm}}$, boiling occurs strictly at $T_b < 100^\circ\text{C}$. The mass ratio of organic distillate ($m_o$) to condensed water ($m_w$) in the receiver is governed by their vapor pressures and molar masses ($M_o, M_w$):
$$\frac{m_o}{m_w} = \frac{P_o^\circ(T) \cdot M_o}{P_w^\circ(T) \cdot M_w}$$

### Supercritical Fluid Extraction ($sc\text{CO}_2$)
Supercritical carbon dioxide ($T_c = 31.1^\circ\text{C}$, $P_c = 7.38\text{ MPa}$) provides an inert, non-toxic, and tunable extraction medium. By modulating pressure and temperature, the fluid density $\rho(P, T)$ is varied continuously between gas-like ($0.2\text{ g/cm}^3$) and liquid-like ($0.9\text{ g/cm}^3$) values, tuning the solubility parameter $\delta$ according to Giddings' relation:
$$\delta = 1.25 \cdot P_c^{1/2} \cdot \left(\frac{\rho_r}{\rho_r(\text{liquid})}\right)$$
Small additions of polar cosolvents (modifiers such as ethanol, 1–5 mol%) dramatically enhance the extraction recovery of moderately polar polyphenols and alkaloids without leaving toxic residues."""
            },
            {
                "id": "sec-1-5",
                "secNumber": "1.5",
                "title": "The Mevalonic Acid (MVA) Pathway: From Acetyl-CoA to Isopentenyl Pyrophosphate",
                "content": r"""The Mevalonic Acid (MVA) pathway operates in the eukaryotic cytoplasm, archaea, and plant cytosol, synthesizing the fundamental $C_5$ terpene building blocks: isopentenyl pyrophosphate (IPP) and dimethylallyl pyrophosphate (DMAPP).

### Stepwise Enzymatic Cascade
1. **Acetoacetyl-CoA Thiolase Condensation**: Two molecules of acetyl-CoA undergo a Claisen condensation to form acetoacetyl-CoA:
   $$2\text{ CH}_3\text{COSCoA} \rightleftharpoons \text{CH}_3\text{COCH}_2\text{COSCoA} + \text{CoA-SH}$$
2. **HMG-CoA Synthase Condensation**: Acetoacetyl-CoA condenses with a third acetyl-CoA via stereospecific aldol addition to generate (3S)-3-hydroxy-3-methylglutaryl-CoA (HMG-CoA):
   $$\text{Acetoacetyl-CoA} + \text{Acetyl-CoA} + \text{H}_2\text{O} \to \text{HMG-CoA} + \text{CoA-SH}$$
3. **HMG-CoA Reductase (HMGR) — Rate-Determining Step**: HMGR catalyzes the irreversible, two-step, four-electron reduction of the thioester to a primary alcohol, utilizing two molecules of NADPH:
   $$\text{HMG-CoA} + 2\text{ NADPH} + 2\text{ H}^+ \to (3R)\text{-Mevalonate} + \text{CoA-SH} + 2\text{ NADP}^+$$
   This step is the major pharmacological target for statin cholesterol-lowering drugs (e.g., atorvastatin).
4. **Consecutive Phosphorylations**: Mevalonate is phosphorylated by mevalonate kinase (yielding mevalonate 5-phosphate) and phosphomevalonate kinase (yielding mevalonate 5-pyrophosphate), consuming 2 ATP:
   $$\text{Mevalonate} + 2\text{ ATP} \to \text{Mevalonate-5-PP} + 2\text{ ADP}$$
5. **Decarboxylation to IPP**: Mevalonate 5-diphosphate decarboxylase catalyzes an ATP-dependent trans-elimination with decarboxylation, affording isopentenyl pyrophosphate (IPP):
   $$\text{Mevalonate-5-PP} + \text{ATP} \to \text{IPP} + \text{ADP} + \text{P}_i + \text{CO}_2$$
6. **Isomerization to DMAPP**: Isopentenyl pyrophosphate isomerase establishes a reversible equilibrium via stereospecific protonation-deprotonation, yielding dimethylallyl pyrophosphate (DMAPP):
   $$\text{IPP} \rightleftharpoons \text{DMAPP} \quad (K_{\text{eq}} \approx 6 - 9)$$"""
            },
            {
                "id": "sec-1-6",
                "secNumber": "1.6",
                "title": "The 2-C-Methyl-D-erythritol 4-Phosphate (MEP/DOXP) Pathway",
                "content": r"""The 2-C-Methyl-D-erythritol 4-Phosphate (MEP) pathway, also termed the 1-deoxy-D-xylulose 5-phosphate (DOXP) pathway, functions in plant plastids, cyanobacteria, and major human pathogens (e.g., *Plasmodium falciparum*, *Mycobacterium tuberculosis*). It represents an alternative route to IPP and DMAPP distinct from the cytosolic MVA pathway.

### Stepwise Catalytic Mechanism
1. **DOXP Synthase (DXS)**: Condensation of pyruvate and D-glyceraldehyde 3-phosphate (GAP) mediated by thiamine pyrophosphate (TPP) with concurrent decarboxylation:
   $$\text{Pyruvate} + \text{GAP} \xrightarrow{\text{DXS, TPP}} \text{1-deoxy-D-xylulose 5-phosphate (DOXP)} + \text{CO}_2$$
2. **DOXP Reductoisomerase (IspC / Dxr)**: DOXP undergoes an intramolecular retro-aldol / aldol rearrangement followed by NADPH reduction to form 2-C-methyl-D-erythritol 4-phosphate (MEP). This enzyme is specifically inhibited by fosmidomycin:
   $$\text{DOXP} + \text{NADPH} + \text{H}^+ \xrightarrow{\text{IspC}} \text{MEP} + \text{NADP}^+$$
3. **CDP Conjugation (IspD)**: MEP reacts with cytidine triphosphate (CTP) to form 4-diphosphocytidyl-2-C-methyl-D-erythritol (CDP-ME):
   $$\text{MEP} + \text{CTP} \to \text{CDP-ME} + \text{PP}_i$$
4. **Phosphorylation and Cyclization (IspE, IspF)**: Phosphorylation of the C2 hydroxyl by IspE (ATP $\to$ ADP) followed by cyclization with elimination of CMP yields 2-C-methyl-D-erythritol 2,4-cyclodiphosphate (MEcPP).
5. **Reductive Ring Opening and Cleavage (IspG, IspH)**: Iron-sulfur cluster $[4\text{Fe}-4\text{S}]$ enzymes catalyze sequential two-electron reductions:
   $$\text{MEcPP} \xrightarrow{\text{IspG, } 2e^-} \text{HMBPP} \xrightarrow{\text{IspH, } 2e^-} \text{IPP} + \text{DMAPP}$$
   Unlike the MVA pathway where IPP is synthesized first, the MEP pathway produces both IPP and DMAPP simultaneously in a ~5:1 ratio directly from (E)-4-hydroxy-3-methyl-but-2-enyl pyrophosphate (HMBPP)."""
            },
            {
                "id": "sec-1-7",
                "secNumber": "1.7",
                "title": "The Shikimic Acid Pathway: From Erythrose 4-Phosphate to Chorismate & Aromatic Amino Acids",
                "content": r"""The shikimate pathway operates in plants, fungi, and bacteria (absent in mammals), channeling carbohydrates into aromatic secondary metabolites and the essential aromatic amino acids: L-phenylalanine, L-tyrosine, and L-tryptophan.

### Stepwise Pathway Architecture
1. **DAHP Synthase Condensation**: Phosphoenolpyruvate (PEP) and D-erythrose 4-phosphate (E4P) condense stereospecifically:
   $$\text{PEP} + \text{E4P} + \text{H}_2\text{O} \to \text{DAHP} + \text{P}_i$$
   where DAHP is 3-deoxy-D-arabino-heptulosonate 7-phosphate.
2. **Dehydroquinate Synthase (DHQS)**: Intramolecular cyclization of DAHP yields 3-dehydroquinate (DHQ), consuming and regenerating $\text{NAD}^+$ catalytically.
3. **Dehydration to 3-Dehydroshikimate**: Dehydroquinase dehydrates DHQ to introduce a double bond:
   $$\text{DHQ} \to \text{3-Dehydroshikimate} + \text{H}_2\text{O}$$
4. **Shikimate Dehydrogenase**: NADPH-dependent reduction of the C3 ketone yields shikimate:
   $$\text{3-Dehydroshikimate} + \text{NADPH} + \text{H}^+ \rightleftharpoons \text{Shikimate} + \text{NADP}^+$$
5. **Phosphorylation and EPSP Formation**: Shikimate kinase phosphorylates the C3 hydroxyl (forming shikimate 3-phosphate). Subsequently, 5-enolpyruvylshikimate-3-phosphate (EPSP) synthase condenses it with a second molecule of PEP:
   $$\text{Shikimate 3-phosphate} + \text{PEP} \xrightarrow{\text{EPSPS}} \text{EPSP} + \text{P}_i$$
   EPSP synthase is the exclusive cellular target of the broad-spectrum herbicide glyphosate (Roundup).
6. **Chorismate Synthase**: Eliminates phosphate to generate chorismate, the pivotal branch-point intermediate of aromatic secondary metabolism.
7. **Downstream Divergence**: Chorismate mutase catalyzes an intramolecular Claisen rearrangement to prephenate (leading to Phe and Tyr), whereas anthranilate synthase incorporates glutamine nitrogen to yield anthranilate (leading to Trp and indole alkaloids)."""
            }
        ],
        "problems": [
            {
                "id": "prob-1-1",
                "problemNumber": "1.1",
                "title": "Bioenergetics and Stoichiometry of Mevalonate Biosynthesis from Acetyl-CoA",
                "difficulty": "Intermediate",
                "statement": r"""Calculate the net stoichiometry, molar ATP requirement, and standard free energy change $\Delta G^{\circ\prime}$ for the complete conversion of three moles of acetyl-CoA to one mole of isopentenyl pyrophosphate (IPP) and one mole of $\text{CO}_2$ via the classical eukaryotic Mevalonic Acid (MVA) pathway. Given standard free energies of hydrolysis: $\Delta G^{\circ\prime}(\text{Acetyl-CoA hydrolysis}) = -31.5\text{ kJ/mol}$, $\Delta G^{\circ\prime}(\text{ATP hydrolysis}) = -30.5\text{ kJ/mol}$, and $\Delta G^{\circ\prime}(\text{NADPH oxidation to NADP}^+) = -220.0\text{ kJ/mol}$.""",
                "hints": [
                    r"Write down the balanced chemical equation for each step: Thiolase, HMGR, Kinases, and Decarboxylase.",
                    r"Count the moles of acetyl-CoA consumed, CoA-SH released, NADPH oxidized, and ATP hydrolyzed to ADP."
                ],
                "solution": r"""### Step 1: Balanced Stepwise Reactions
1. **Thiolase**:
   $$2\text{ Acetyl-CoA} \rightleftharpoons \text{Acetoacetyl-CoA} + \text{CoA-SH} \quad (\Delta G^{\circ\prime}_1 \approx +26.0\text{ kJ/mol})$$
2. **HMG-CoA Synthase**:
   $$\text{Acetoacetyl-CoA} + \text{Acetyl-CoA} + \text{H}_2\text{O} \to \text{HMG-CoA} + \text{CoA-SH} \quad (\Delta G^{\circ\prime}_2 \approx -37.2\text{ kJ/mol})$$
3. **HMG-CoA Reductase**:
   $$\text{HMG-CoA} + 2\text{ NADPH} + 2\text{ H}^+ \to \text{Mevalonate} + \text{CoA-SH} + 2\text{ NADP}^+ \quad (\Delta G^{\circ\prime}_3 \approx -23.4\text{ kJ/mol})$$
4. **Mevalonate Kinase + Phosphomevalonate Kinase**:
   $$\text{Mevalonate} + 2\text{ ATP} \to \text{Mevalonate-5-PP} + 2\text{ ADP} \quad (\Delta G^{\circ\prime}_4 \approx -25.6\text{ kJ/mol})$$
5. **Mevalonate Pyrophosphate Decarboxylase**:
   $$\text{Mevalonate-5-PP} + \text{ATP} \to \text{IPP} + \text{ADP} + \text{P}_i + \text{CO}_2 \quad (\Delta G^{\circ\prime}_5 \approx -33.5\text{ kJ/mol})$$

### Step 2: Summed Stoichiometric Equation
Summing all five transformation steps cancels common intermediates:
$$3\text{ Acetyl-CoA} + 3\text{ ATP} + 2\text{ NADPH} + \text{H}_2\text{O} \to \text{IPP} + 3\text{ CoA-SH} + 3\text{ ADP} + \text{P}_i + 2\text{ NADP}^+ + \text{CO}_2$$

### Step 3: Total ATP and Energetic Calculation
- **ATP Consumed**: Exactly $3\text{ moles of ATP}$ per mole of IPP synthesized.
- **Redox Equivalents**: $2\text{ moles of NADPH}$ oxidized.
- **Summed Standard Free Energy Change**:
  $$\Delta G^{\circ\prime}_{\text{net}} = (+26.0) + (-37.2) + (-23.4) + (-25.6) + (-33.5) = -93.7\text{ kJ/mol}$$
The overall reaction pathway is exergonic by $\mathbf{-93.7\text{ kJ/mol}}$, driving terpene precursor assembly irreversibly forward under physiological conditions."""
            },
            {
                "id": "prob-1-2",
                "problemNumber": "1.2",
                "title": "Decarboxylative Elimination Stereochemistry of Mevalonate Pyrophosphate Decarboxylase",
                "difficulty": "Advanced",
                "statement": r"""Mevalonate 5-pyrophosphate decarboxylase catalyzes the conversion of $(3R)$-mevalonate 5-pyrophosphate to isopentenyl pyrophosphate (IPP). Using stereospecifically deuterium-labeled substrates $(2R)\text{-}[2\text{-}^2\text{H}]\text{mevalonate 5-PP}$ and $(2S)\text{-}[2\text{-}^2\text{H}]\text{mevalonate 5-PP}$, predict the stereochemical configuration ($E$ or $Z$) of the resulting monodeuterated IPP terminal alkene. Determine whether the enzymatic elimination proceeds via a concerted anti-periplanar mechanism or a syn-periplanar pathway.""",
                "hints": [
                    r"Draw the Newman projection of (3R)-mevalonate 5-PP looking along the C3-C2 bond.",
                    r"Analyze the spatial arrangement of the departing C3-OH (phosphorylated to a phosphate leaving group) and C1 carboxylate group."
                ],
                "solution": r"""### Step 1: Phosphorylation of the C3 Hydroxyl
Mevalonate 5-diphosphate decarboxylase first phosphorylates the tertiary C3-OH group using ATP, converting a poor leaving group ($-\text{OH}$) into an excellent leaving group ($-\text{OPO}_3^{2-}$).

### Step 2: Conformation for Decarboxylative Elimination
For a concerted anti-periplanar elimination:
- The dihedral angle between the departing $\text{C}1\text{--COO}^-$ group and the departing $\text{C}3\text{--OPO}_3^{2-}$ group must be $180^\circ$.
- When looking down the $\text{C}3\text{--C}2$ bond in the $(3R)$ enantiomer, the C3 methyl group, C3 phosphate group, C2 pro-$R$ proton, and C2 pro-$S$ proton adopt a fixed staggered conformation.

### Step 3: Stereochemical Outcome
1. With $(2R)\text{-}[2\text{-}^2\text{H}]\text{mevalonate 5-PP}$, the anti-periplanar departure of $\text{CO}_2$ and $\text{PO}_4^{3-}$ forces the deuterium atom into the **cis** relationship with the methyl group at C3, producing **(E)-[4-2H]IPP**.
2. Conversely, $(2S)\text{-}[2\text{-}^2\text{H}]\text{mevalonate 5-PP}$ places the deuterium in a trans relationship to the methyl group, producing **(Z)-[4-2H]IPP**.
3. Experimental spectroscopic verification (Cornforth and Popják) confirmed this stereochemical configuration, establishing that mevalonate diphosphate decarboxylase operates strictly via a **concerted anti-periplanar mechanism**."""
            },
            {
                "id": "prob-1-3",
                "problemNumber": "1.3",
                "title": "Isotope Tracing and Carbon Routing in the MEP vs MVA Pathway",
                "statement": r"""A culture of *Mentha piperita* is grown in the presence of $[1\text{-}^{13}\text{C}]\text{D-glucose}$. In plants, monoterpenes are synthesized in plastids via the MEP pathway, whereas sesquiterpenes are formed in the cytosol via the MVA pathway. Trace the exact labeling pattern of $^{13}\text{C}$ in the $C_5$ precursor isopentenyl pyrophosphate (IPP) formed via:
(a) The MVA pathway (draining glycolytic acetyl-CoA).
(b) The MEP pathway (draining pyruvate and glyceraldehyde 3-phosphate).""",
                "hints": [
                    r"Determine which carbons of pyruvate and GAP are labeled from [1-13C]glucose via glycolysis.",
                    r"Follow the fate of C1 of pyruvate during pyruvate dehydrogenase decarboxylation.",
                    r"Follow C1, C2, C3 of pyruvate and GAP through DXS and IspC."
                ],
                "solution": r"""### Step 1: Glycolytic Fate of $[1\text{-}^{13}\text{C}]\text{Glucose}$
Via the Embden-Meyerhof-Parnas pathway:
- D-Glucose is cleaved by aldolase into glyceraldehyde 3-phosphate (GAP) and dihydroxyacetone phosphate (DHAP).
- Carbon-1 of glucose becomes Carbon-3 of DHAP, which isomerizes to Carbon-3 of GAP:
  $$\text{GAP: } \text{C}1 = \text{CHO (unlabeled)}, \quad \text{C}2 = \text{CHOH (unlabeled)}, \quad \text{C}3 = \text{CH}_2\text{OPO}_3^{2-} \; (\mathbf{^{13}\text{C-labeled}})$$
- Downstream conversion to pyruvate yields:
  $$\text{Pyruvate: } \text{C}1 = \text{COO}^- \; (\text{unlabeled}), \quad \text{C}2 = \text{C}=\text{O} \; (\text{unlabeled}), \quad \text{C}3 = \text{CH}_3 \; (\mathbf{^{13}\text{C-labeled}})$$

### Step 2: (a) MVA Pathway Fate
Pyruvate dehydrogenase decarboxylates pyruvate:
$$\text{Pyruvate} (\text{C}1\text{, C}2\text{, C}3) \to \text{Acetyl-CoA} (\text{C}1=\text{COSCoA}, \text{C}2=\text{CH}_3) + \text{CO}_2(\text{C}1)$$
Thus, in acetyl-CoA, only the methyl carbon ($\text{C}2$) contains the $^{13}\text{C}$ label.
Following the MVA assembly:
- Condensation of 3 molecules of acetyl-CoA forms mevalonate:
  $$\text{Mevalonate labeled at C}2\text{, C}4\text{, and the C}3\text{-methyl group.}$$
- Decarboxylation eliminates C1 as $\text{CO}_2$.
- In the resulting **IPP ($\text{CH}_2=\text{C}(\text{CH}_3)\text{-CH}_2\text{-CH}_2\text{-OPP}$)**:
  - $\text{C}2$ (alkene carbon), $\text{C}4$ ($\text{CH}_2$ adjacent to $\text{OPP}$), and the attached **methyl group** ($\text{C}5$) are **$^{13}\text{C}$-labeled**.
  - Total: **3 labeled carbons** out of 5.

### Step 3: (b) MEP Pathway Fate
In the DOXP synthase (DXS) reaction:
- $\text{C}3$ of pyruvate ($^{13}\text{C}$) becomes $\text{C}2$ of DOXP, while $\text{C}1$ is lost as $\text{CO}_2$.
- GAP ($^{13}\text{C}$ at $\text{C}3$) provides the remaining carbons of DOXP.
- Following the IspC-IspH enzymatic cascade to IPP:
  - Only **C1** and **C5 (methyl)** retain the $^{13}\text{C}$ label.
  - Total: **2 labeled carbons** out of 5.
This distinct $^{13}\text{C}$-labeling pattern rigorously discriminates MVA from MEP pathway flux via $^{13}\text{C}\text{-NMR}$ spectroscopy."""
            },
            {
                "id": "prob-1-4",
                "problemNumber": "1.4",
                "title": "Thermodynamic Analysis of EPSP Synthase and Glyphosate Inhibition Kinetics",
                "difficulty": "Advanced",
                "statement": r"""5-Enolpyruvylshikimate-3-phosphate (EPSP) synthase catalyzes the reversible condensation of shikimate-3-phosphate (S3P) and phosphoenolpyruvate (PEP) to form EPSP and inorganic phosphate ($P_i$). The equilibrium constant at $298\text{ K}$ and $\text{pH } 7.0$ is $K_{\text{eq}}^\prime = 0.52$. Glyphosate acts as an uncompetitive inhibitor with respect to S3P and a competitive inhibitor with respect to PEP, exhibiting an inhibition constant $K_i = 1.2\times 10^{-7}\text{ M}$.
(a) Calculate $\Delta G^{\circ\prime}$ for the forward synthesis of EPSP.
(b) If $[S3P] = 0.50\text{ mM}$, $[PEP] = 0.20\text{ mM}$, $[EPSP] = 0.08\text{ mM}$, and $[P_i] = 2.5\text{ mM}$, calculate the actual in vivo free energy change $\Delta G^\prime$. Determine whether forward flux is spontaneous under these conditions.""",
                "hints": [
                    r"Use the fundamental relation \Delta G^{\circ\prime} = -RT \ln K_{\text{eq}}^\prime.",
                    r"Calculate the reaction quotient Q = ([EPSP][P_i]) / ([S3P][PEP]).",
                    r"Compute \Delta G^\prime = \Delta G^{\circ\prime} + RT \ln Q."
                ],
                "solution": r"""### Step 1: Standard Free Energy Change ($\Delta G^{\circ\prime}$)
Using the thermodynamic relation:
$$\Delta G^{\circ\prime} = -R T \ln K_{\text{eq}}^\prime$$
Where $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $T = 298.15\text{ K}$:
$$\Delta G^{\circ\prime} = -(8.314)(298.15) \ln(0.52) = -2478.9 \times (-0.6539) = +1621\text{ J/mol} = +\mathbf{1.62\text{ kJ/mol}}$$

### Step 2: Reaction Quotient ($Q$) Calculation
The mass-action ratio $Q$ under physiological concentrations is:
$$Q = \frac{[\text{EPSP}] [P_i]}{[\text{S3P}] [\text{PEP}]}$$
Substituting the given molar concentrations:
$$Q = \frac{(0.08\times 10^{-3}\text{ M}) (2.5\times 10^{-3}\text{ M})}{(0.50\times 10^{-3}\text{ M}) (0.20\times 10^{-3}\text{ M})} = \frac{2.0\times 10^{-7}}{1.0\times 10^{-7}} = 2.0$$

### Step 3: In Vivo Free Energy Change ($\Delta G^\prime$)
$$\Delta G^\prime = \Delta G^{\circ\prime} + R T \ln Q$$
$$\Delta G^\prime = +1621\text{ J/mol} + (8.314)(298.15) \ln(2.0)$$
$$\Delta G^\prime = +1621 + (2478.9 \times 0.6931) = +1621 + 1718 = +3339\text{ J/mol} = +\mathbf{3.34\text{ kJ/mol}}$$
Because $\Delta G^\prime > 0$, the reaction as written is endergonic under these cellular concentrations. Forward metabolic flux in vivo is driven by the rapid downstream coupling of chorismate synthase, which irreversibly consumes EPSP ($\Delta G^{\circ\prime} \ll 0$), lowering $[\text{EPSP}]$ and pulling the pathway forward."""
            },
            {
                "id": "prob-1-5",
                "problemNumber": "1.5",
                "title": "Decarboxylative Claisen Condensation Energetics in Polyketide Chain Elongation",
                "difficulty": "Intermediate",
                "statement": r"""In polyketide synthases (PKS), carbon-carbon bond formation proceeds via decarboxylative condensation of a malonyl-S-ACP extender unit with an acyl-S-ACP growing chain, rather than direct Claisen condensation between two neutral thioesters. Compare the thermodynamics of:
(1) Direct Claisen condensation: $\text{Ac-SCoA} + \text{Ac-SCoA} \rightleftharpoons \text{AcAc-SCoA} + \text{CoASH} \quad (\Delta G^{\circ\prime}_1 = +26.0\text{ kJ/mol})$.
(2) Decarboxylative condensation: $\text{Ac-SCoA} + \text{Malonyl-SCoA} \to \text{AcAc-SCoA} + \text{CoASH} + \text{CO}_2(g)$.
Given that carboxylation of acetyl-CoA requires ATP hydrolysis ($\Delta G^{\circ\prime} = -19.7\text{ kJ/mol}$ for $\text{Ac-SCoA} + \text{HCO}_3^- + \text{ATP} \rightleftharpoons \text{Malonyl-SCoA} + \text{ADP} + P_i$), calculate $\Delta G^{\circ\prime}_2$ for the decarboxylative condensation and explain why nature couples ATP to the extender unit.""",
                "hints": [
                    r"Combine the thermodynamic cycle of carboxylation and decarboxylation.",
                    r"Note that \Delta G^{\circ\prime} of CO2 loss provides substantial entropic driving force."
                ],
                "solution": r"""### Step 1: Thermodynamic Coupling Cycle
The overall biological pathway to acetoacetyl-CoA driven by ATP is:
$$\text{Step A (Carboxylation): } \text{Acetyl-CoA} + \text{HCO}_3^- + \text{ATP} \rightleftharpoons \text{Malonyl-CoA} + \text{ADP} + P_i \quad (\Delta G^{\circ\prime}_A = -19.7\text{ kJ/mol})$$
$$\text{Step B (Decarboxylative condensation): } \text{Acetyl-CoA} + \text{Malonyl-CoA} \to \text{Acetoacetyl-CoA} + \text{CoASH} + \text{CO}_2 \quad (\Delta G^{\circ\prime}_B = \Delta G^{\circ\prime}_2)$$

Summing Step A and Step B yields the net reaction:
$$2\text{ Acetyl-CoA} + \text{ATP} + \text{H}_2\text{O} \to \text{Acetoacetyl-CoA} + \text{CoASH} + \text{ADP} + P_i \quad (\Delta G^{\circ\prime}_{\text{net}})$$

From the direct Claisen condensation value ($\Delta G^{\circ\prime}_1 = +26.0\text{ kJ/mol}$) and ATP hydrolysis ($\Delta G^{\circ\prime}_{\text{ATP}} = -30.5\text{ kJ/mol}$):
$$\Delta G^{\circ\prime}_{\text{net}} = \Delta G^{\circ\prime}_1 + \Delta G^{\circ\prime}_{\text{ATP}} = +26.0 - 30.5 = -4.5\text{ kJ/mol}$$

### Step 2: Calculation of $\Delta G^{\circ\prime}_2$
Since $\Delta G^{\circ\prime}_{\text{net}} = \Delta G^{\circ\prime}_A + \Delta G^{\circ\prime}_2$:
$$\Delta G^{\circ\prime}_2 = \Delta G^{\circ\prime}_{\text{net}} - \Delta G^{\circ\prime}_A = -4.5 - (-19.7) = \mathbf{-15.2\text{ kJ/mol}}$$

### Step 3: Biochemical Rationale
Direct Claisen condensation between two simple thioesters is thermodynamically uphill ($\Delta G^{\circ\prime} = +26.0\text{ kJ/mol}$), meaning the equilibrium lies overwhelmingly on the side of reactants ($K_{\text{eq}} \approx 3\times 10^{-5}$). By investing an ATP equivalent to form malonyl-CoA, the substrate is activated; subsequent decarboxylation generates an enolate carbanion intermediate at neutral pH with concurrent release of gaseous $\text{CO}_2$. The large increase in entropy ($\Delta S > 0$) renders the condensation irreversible ($\Delta G^{\circ\prime}_2 = -15.2\text{ kJ/mol}$), driving continuous polyketide chain growth."""
            },
            {
                "id": "prob-1-6",
                "problemNumber": "1.6",
                "title": "Partition Coefficient and Separation Factor in Countercurrent Extraction",
                "difficulty": "Intermediate",
                "statement": r"""A crude botanical extract contains two alkaloids, compound A and compound B, with octanol-water partition coefficients $K_D(A) = 12.5$ and $K_D(B) = 1.8$, where $K_D = C_{\text{org}} / C_{\text{aq}}$.
(a) Calculate the separation factor $\alpha_{A/B}$.
(b) In a single-stage liquid-liquid batch extraction using equal volumes of organic solvent and water ($V_{\text{org}} = V_{\text{aq}}$), calculate the fraction of each alkaloid extracted into the organic layer.
(c) Calculate how many theoretical extraction stages ($N$) are required to achieve $99.0\%$ recovery of compound A in the organic phase while retaining less than $1.0\%$ of compound B.""",
                "hints": [
                    r"The separation factor \alpha = K_D(A) / K_D(B).",
                    r"Fraction extracted in a single stage is E = K_D / (K_D + (V_{aq}/V_{org})).",
                    r"Use countercurrent stage equations for multistage extraction."
                ],
                "solution": r"""### Step 1: Separation Factor ($\alpha_{A/B}$)
$$\alpha_{A/B} = \frac{K_D(A)}{K_D(B)} = \frac{12.5}{1.8} = \mathbf{6.94}$$

### Step 2: Single-Stage Extraction Fractions
With phase volume ratio $\theta = V_{\text{org}} / V_{\text{aq}} = 1.0$:
$$\text{Extraction fraction } E = \frac{K_D \cdot \theta}{1 + K_D \cdot \theta} = \frac{K_D}{1 + K_D}$$
- For Alkaloid A:
  $$E_A = \frac{12.5}{1 + 12.5} = \frac{12.5}{13.5} = 0.9259 \implies \mathbf{92.59\%}$$
- For Alkaloid B:
  $$E_B = \frac{1.8}{1 + 1.8} = \frac{1.8}{2.8} = 0.6429 \implies \mathbf{64.29\%}$$
A single-stage extraction fails to separate them, as $64.29\%$ of unwanted B co-extracts with A.

### Step 3: Multistage Countercurrent Extraction
For countercurrent separation with stripping, the fractional recovery in $N$ ideal equilibrium stages is governed by the extraction factor $\mathcal{E} = K_D (V_{\text{org}} / V_{\text{aq}})$.
To obtain $>99\%$ recovery of A with $<1\%$ contamination of B, the required number of stages $N$ satisfies:
$$N \ge \frac{\ln\left(\frac{1 - E_A}{E_A}\right) - \ln\left(\frac{1 - E_B}{E_B}\right)}{\ln \alpha_{A/B}} \approx \frac{\ln(0.01 / 0.99) - \ln(0.99 / 0.01)}{\ln(6.94)} = \frac{-4.595 - 4.595}{1.937} = \frac{9.19}{1.937} \approx 4.74$$
Rounding up, a minimum of **5 theoretical stages** ($N = 5$) in a countercurrent chromatography column is required to achieve high-purity separation."""
            },
            {
                "id": "prob-1-7",
                "problemNumber": "1.7",
                "title": "Supercritical $\\text{CO}_2$ Density and Solubility Modeling via Peng-Robinson Equation of State",
                "difficulty": "Advanced",
                "statement": r"""In the supercritical fluid extraction ($sc\text{CO}_2$) of caffeine from green tea leaves, carbon dioxide is held at $T = 313.15\text{ K}$ ($40^\circ\text{C}$) and $P = 20.0\text{ MPa}$ ($200\text{ bar}$).
(a) Given the critical parameters of $\text{CO}_2$: $T_c = 304.13\text{ K}$, $P_c = 7.377\text{ MPa}$, and acentric factor $\omega = 0.224$, calculate the reduced temperature $T_r$ and reduced pressure $P_r$.
(b) Using the Peng-Robinson equation of state parameterization:
$$a(T) = 0.45724 \frac{R^2 T_c^2}{P_c} \left[1 + m(1 - \sqrt{T_r})\right]^2, \quad b = 0.07780 \frac{R T_c}{P_c}$$
where $m = 0.37464 + 1.54226\omega - 0.26992\omega^2$, compute the molar density $\rho_m$ ($\text{mol/L}$) and mass density $\rho$ ($\text{g/cm}^3$) of $\text{CO}_2$ under these operating conditions.""",
                "hints": [
                    r"Compute T_r = T / T_c and P_r = P / P_c.",
                    r"Calculate m = 0.37464 + 1.54226(0.224) - 0.26992(0.224)^2.",
                    r"Solve the cubic Peng-Robinson equation in compressibility factor Z: Z^3 - (1 - B)Z^2 + (A - 3B^2 - 2B)Z - (AB - B^2 - B^3) = 0."
                ],
                "solution": r"""### Step 1: Reduced Parameters
$$T_r = \frac{T}{T_c} = \frac{313.15}{304.13} = \mathbf{1.0297}$$
$$P_r = \frac{P}{P_c} = \frac{20.0}{7.377} = \mathbf{2.711}$$

### Step 2: Peng-Robinson Parameters
1. Parameter $m$:
   $$m = 0.37464 + 1.54226(0.224) - 0.26992(0.224)^2 = 0.37464 + 0.3455 - 0.0135 = 0.7066$$
2. Temperature-dependent term $\alpha(T_r)$:
   $$\alpha(T_r) = \left[1 + 0.7066(1 - \sqrt{1.0297})\right]^2 = \left[1 + 0.7066(1 - 1.01474)\right]^2 = [1 - 0.01042]^2 = 0.9793$$
3. Co-volume $b$ and attractive parameter $a$:
   $$b = 0.07780 \frac{(8.314)(304.13)}{7.377\times 10^6} = 2.665\times 10^{-5}\text{ m}^3\text{/mol} = 0.02665\text{ L/mol}$$
   $$a = 0.45724 \frac{(8.314)^2 (304.13)^2}{7.377\times 10^6} \times 0.9793 = 0.3957\text{ Pa}\cdot\text{m}^6\text{/mol}^2$$

4. Dimensionless coefficients $A$ and $B$:
   $$A = \frac{a P}{(R T)^2} = \frac{(0.3957)(20.0\times 10^6)}{[(8.314)(313.15)]^2} = \frac{7.914\times 10^6}{6.778\times 10^6} = 1.1676$$
   $$B = \frac{b P}{R T} = \frac{(2.665\times 10^{-5})(20.0\times 10^6)}{(8.314)(313.15)} = 0.2047$$

### Step 3: Compressibility Factor and Density
Solving the PR cubic equation $Z^3 - (1 - B)Z^2 + (A - 3B^2 - 2B)Z - (AB - B^2 - B^3) = 0$:
Substituting $A = 1.1676$ and $B = 0.2047$:
$$Z^3 - 0.7953 Z^2 + 0.6324 Z - 0.1887 = 0$$
The unique real root in the supercritical liquid-like regime is:
$$Z \approx 0.385$$
The molar volume $V_m$ is:
$$V_m = \frac{Z R T}{P} = \frac{(0.385)(8.314)(313.15)}{20.0\times 10^6} = 5.013\times 10^{-5}\text{ m}^3\text{/mol} = 0.05013\text{ L/mol}$$
The molar density is:
$$\rho_m = \frac{1}{V_m} = \frac{1}{0.05013\text{ L/mol}} = \mathbf{19.95\text{ mol/L}}$$
Converting to mass density ($M_{\text{CO}_2} = 44.01\text{ g/mol}$):
$$\rho = 19.95\text{ mol/L} \times 44.01\text{ g/mol} = 878\text{ g/L} = \mathbf{0.878\text{ g/cm}^3}$$
At $0.878\text{ g/cm}^3$, $sc\text{CO}_2$ exhibits liquid-like solvent power while retaining gas-like diffusivity, enabling quantitative extraction of caffeine."""
            }
        ]
    }
    units.append(u1)

    # =========================================================================
    # UNIT 2: Terpenoids I: Isoprene Rule, Acyclic & Monocyclic Monoterpenes
    # =========================================================================
    u2 = {
        "id": "unit-2",
        "unitNumber": 2,
        "title": "Unit 2: Terpenoids I: Isoprene Rule, Acyclic & Monocyclic Monoterpenes",
        "leadSummary": "Exhaustive treatment of monoterpenoid chemistry ($C_{10}H_{16}$): Wallach's classical isoprene rule, Ingold's Special Isoprene Rule, isolation of essential oils, rigorous degradative proofs of structure, alkaline cleavages, and full total syntheses of acyclic monoterpenes (myrcene, citral) and monocyclic monoterpenes (limonene).",
        "simulations": ["sim_nat_isoprene_rule_builder"],
        "sections": [
            {
                "id": "sec-2-1",
                "secNumber": "2.1",
                "title": "Terpenoids: Definition, Structural Hierarchy & Systematics ($C_5$ to $C_{40+}$)",
                "content": r"""Terpenoids (isoprenoids) constitute one of the largest and structurally most diverse classes of natural products, comprising over 80,000 characterized chemical entities. They are formally defined as compounds whose carbon frameworks are constructed from repeating five-carbon isoprene ($C_5H_8$) units.

### Structural Hierarchy and Classification
Terpenoids are classified according to the number of constituent $C_5$ isoprene units:

| Class | Isoprene Units ($n$) | Carbon Count | Typical Representative | Natural Source |
| :--- | :--- | :--- | :--- | :--- |
| **Hemiterpenes** | 1 | $C_5$ | Isoprene, Isovaleric acid | Poplar leaf emissions |
| **Monoterpenes** | 2 | $C_{10}$ | Myrcene, Limonene, Citral, Pinene | Citrus peel, turpentine, lemongrass |
| **Sesquiterpenes** | 3 | $C_{15}$ | Farnesol, Caryophyllene, Artemisinin | Sweet wormwood, chamomile |
| **Diterpenes** | 4 | $C_{20}$ | Abietic acid, Taxol, Retinol (Vit A) | Pine resin, *Taxus brevifolia* |
| **Sesterterpenes** | 5 | $C_{25}$ | Ophiobolin A, Manoalide | Marine sponges, fungi |
| **Triterpenes** | 6 | $C_{30}$ | Squalene, Lanosterol, Lupeol | Shark liver oil, plant cuticles |
| **Tetraterpenes** | 8 | $C_{40}$ | $\beta$-Carotene, Lutein, Lycopene | Carrots, tomatoes |
| **Polyterpenes** | $>8$ | $(C_5)_n$ | Natural rubber (cis), Gutta-percha (trans) | *Hevea brasiliensis* latex |"""
            },
            {
                "id": "sec-2-2",
                "secNumber": "2.2",
                "title": "The Isoprene Rule and Ingold's Special Isoprene Rule",
                "content": r"""The structural assembly of terpenoids is governed by empirical rules formulated by Otto Wallach (1887) and Sir Christopher Ingold (1925), which serve as crucial guides in structural elucidation and retrosynthesis.

### Wallach's Isoprene Rule
Wallach demonstrated that the thermal decomposition of many natural terpenes yields 2-methyl-1,3-butadiene (isoprene) as a primary pyrolysis fragment. He postulated that the carbon skeletons of all naturally occurring terpenes can be decomposed into intact isoprene units:
$$\text{Skeleton} = (C_5H_8)_n$$

### Ingold's Special Isoprene Rule
Ingold observed that in the vast majority of natural terpenoids, isoprene units are joined in a strict **head-to-tail** (1,4'-linkage) orientation:
- **Head (Position 1)**: The branched terminus carrying the methyl group ($-\text{C}(\text{CH}_3)=\text{CH}_2$).
- **Tail (Position 4)**: The unbranched terminus ($-\text{CH}_2-$).

```
        Head (C1)           Tail (C4)
           |                   |
    CH2 = C(CH3) - CH = CH2
          |
        Methyl (C2)
```
In a regular regular monoterpene ($C_{10}$), two isoprene units couple head-to-tail:
$$\text{Tail}_1 (\text{C}4) \longrightarrow \text{Head}_2 (\text{C}1^\prime)$$

### Irregular Couplings and Rule Limitations
While the Special Isoprene Rule holds for nearly all monoterpenes and sesquiterpenes, key exceptions occur in higher terpenes and specialized classes:
1. **Tail-to-Tail Coupling (4-4')**: Seen in the dimerization of farnesyl pyrophosphate to squalene ($C_{30}$) and geranylgeranyl pyrophosphate to phytoene ($C_{40}$).
2. **Head-to-Head Coupling (1-1')**: Encountered in specialized archaebacterial tetraether membrane lipids.
3. **Irregular Monoterpenes**: Pyrethrins (e.g., chrysanthemic acid) and lavandulol violate the 1,4'-coupling rule due to non-classical cyclopropane ring formation during biosynthesis."""
            },
            {
                "id": "sec-2-3",
                "secNumber": "2.3",
                "title": "Essential Oils: Isolation, Terpeneless Oils & Gas Chromatography",
                "content": r"""Essential oils are volatile, aromatic, hydrophobic secondary metabolite mixtures produced in specialized glandular trichomes, vittae, or lysigenous cavities of plants.

### Isolation Protocols
1. **Steam Distillation and Hydrodistillation**: Standard industrial methods using Clevenger-type apparatus. The vaporized oil is condensed and phase-separated in a Florentine receiver based on density differences ($\rho_{\text{oil}} < 1.0\text{ g/cm}^3$ for most terpenes; $\rho > 1.0$ for phenylpropanoid-rich oils like clove oil).
2. **Enfleurage**: Traditional cold-fat absorption method for delicate, heat-labile floral scents (jasmine, tuberose). Volatile terpenes diffuse into an odorless animal fat or vegetable lipid matrix, followed by ethanol desorption.
3. **Cold-Pressing (Expression)**: Mechanical abrading of the flavedo (citrus pericarp) yielding pristine, non-thermally degraded monoterpenes.

### Terpeneless Essential Oils
Crude citrus essential oils contain $90–95\%$ monoterpene hydrocarbons (primarily (+)-limonene), which possess low aroma impact, oxidize rapidly to foul peroxides, and exhibit poor water/alcohol solubility.
- Fractional vacuum distillation or silica gel column chromatography removes the non-polar hydrocarbon terpenes, leaving a concentrated 'terpeneless' oil enriched in oxygenated monoterpenoids (citral, linalool, geraniol).
- Terpeneless oils possess 10- to 30-fold greater olfactory potency, enhanced stability against oxidation, and superior solubility in aqueous food matrices.

### Gas Chromatographic Profiling
High-resolution capillary gas chromatography coupled to mass spectrometry (GC-MS) on chiral stationary phases (e.g., modified cyclodextrins) resolves enantiomeric terpene pairs (e.g., $(R)\text{-}(+)$-limonene vs $(S)\text{-}(-)$-limonene), providing definitive authentication against synthetic adulteration."""
            },
            {
                "id": "sec-2-4",
                "secNumber": "2.4",
                "title": "Acyclic Monoterpenoids: Structural Elucidation of Myrcene",
                "content": r"""Myrcene ($C_{10}H_{16}$) is an acyclic monoterpene hydrocarbon isolated from bay oil (*Pimenta racemosa*), hops (*Humulus lupulus*), and cannabis.

### Stepwise Structural Elucidation
1. **Molecular Formula and Degree of Unsaturation**:
   Elemental analysis and high-resolution mass spectrometry establish the molecular formula as $C_{10}H_{16}$.
   $$\text{IHD} = C + 1 - \frac{H}{2} = 10 + 1 - 8 = 3$$
   Myrcene possesses 3 degrees of unsaturation.
2. **Catalytic Hydrogenation**:
   Catalytic hydrogenation with Adams' catalyst ($\text{PtO}_2 / \text{H}_2$) absorbs exactly 3 molar equivalents of hydrogen:
   $$\text{C}_{10}\text{H}_{16} + 3\text{ H}_2 \xrightarrow{\text{Pt}} \text{C}_{10}\text{H}_{22} \quad (\text{Tetrahydromyrcene / 2,6-dimethyloctane})$$
   Because the saturated product is an acyclic alkane ($C_n H_{2n+2}$ where $n=10 \implies C_{10}H_{22}$), **myrcene must be an acyclic triene with zero rings**.
3. **Conjugated Diene System**:
   UV-Visible spectroscopy exhibits an absorption maximum at $\lambda_{\text{max}} = 224\text{ nm}$ ($\epsilon \approx 15,000$), diagnostic of an acyclic conjugated diene system. Furthermore, myrcene reacts readily with maleic anhydride in a Diels-Alder [4+2] cycloaddition to afford a crystalline adduct, confirming an acyclic 1,3-butadiene moiety.
4. **Ozonolysis and Oxidative Cleavage**:
   Ozonolysis followed by reductive zinc workup cleaves the three double bonds, yielding three distinct carbonyl fragments:
   $$\text{Myrcene} \xrightarrow{\text{O}_3, \text{ Zn/H}_2\text{O}} \text{Acetone} + 2\text{ Formaldehyde} + \text{4-Oxopentanal (Levulinaldehyde)}$$
   $$\text{CH}_3\text{COCH}_3 + 2\text{ HCHO} + \text{CH}_3\text{COCH}_2\text{CH}_2\text{CHO}$$

### Structural Reconstruction
Reconnecting the fragments at the cleaved carbonyl carbons:
- Acetone ($\text{CH}_3\text{COCH}_3$) indicates an isopropylidene group: $(\text{CH}_3)_2\text{C}=$.
- Two molecules of formaldehyde ($\text{HCHO}$) indicate two terminal methylene groups: $=\text{CH}_2$.
- Levulinaldehyde connects the isopropylidene unit to the conjugated diene:
  $$(\text{CH}_3)_2\text{C}=\text{CH}-\text{CH}_2-\text{CH}_2-\text{C}(=\text{CH}_2)-\text{CH}=\text{CH}_2$$
This proves that myrcene is **7-methyl-3-methyleneocta-1,6-diene**."""
            },
            {
                "id": "sec-2-5",
                "secNumber": "2.5",
                "title": "Acyclic Monoterpenoids: Citral — Degradation, Cyclization & Total Synthesis",
                "content": r"""Citral ($C_{10}H_{16}O$) is an acyclic $\alpha,\beta$-unsaturated monoterpene aldehyde occurring in lemongrass oil (*Cymbopogon citratus*). It exists naturally as a geometric mixture of two diastereomers: geranial (trans-citral or citral a) and neral (cis-citral or citral b).

### Structural Proof by Degradative Chemistry
1. **Molecular Formula and Functional Group**:
   Molecular formula $C_{10}H_{16}O$ ($\text{IHD} = 3$). Citral forms an oxime ($C_{10}H_{16}=\text{NOH}$) with hydroxylamine, a crystalline bisulfite adduct with $\text{NaHSO}_3$, and reduces Tollens' reagent, proving the presence of an **aldehyde group**.
2. **Carbon Skeleton and Acyclic Nature**:
   Mild reduction with sodium amalgam gives the alcohol geraniol ($C_{10}H_{18}O$); vigorous catalytic hydrogenation yields the saturated alcohol 3,7-dimethyloctan-1-ol ($C_{10}H_{22}O$). Thus, citral contains an acyclic carbon chain with two double bonds and one carbonyl group.
3. **Alkaline Cleavage (Retro-Aldol Degradation)**:
   Heating citral with aqueous potassium carbonate ($\text{K}_2\text{CO}_3$) induces a retro-aldol cleavage, yielding 6-methylhept-5-en-2-one and acetaldehyde:
   $$\text{C}_{10}\text{H}_{16}\text{O} + \text{H}_2\text{O} \xrightarrow{\text{OH}^-} (\text{CH}_3)_2\text{C}=\text{CH}-\text{CH}_2-\text{CH}_2-\text{CO}-\text{CH}_3 + \text{CH}_3\text{CHO}$$
4. **Oxidative Degradation**:
   Permanganate-periodate oxidation yields acetone, levulinic acid ($\text{CH}_3\text{COCH}_2\text{CH}_2\text{COOH}$), and oxalic acid ($\text{HOOC-COOH}$). This locates the two double bonds at C2=C3 and C6=C7.

### Cyclization to Aromatic Hydrocarbons
Heating citral with potassium bisulfate ($\text{KHSO}_4$) or aqueous sulfuric acid induces an intramolecular dehydration-cyclization yielding the aromatic hydrocarbon **p-cymene (1-methyl-4-isopropylbenzene)**:
$$\text{Citral} \xrightarrow{\text{H}^+, -\text{H}_2\text{O}} \text{p-Cymene}$$

### Total Synthesis of Citral (Barbier-Bouveault Route)
Methylheptenone is condensed with ethyl bromoacetate in the presence of zinc (Reformatsky reaction):
$$(\text{CH}_3)_2\text{C}=\text{CH}(\text{CH}_2)_2\text{COCH}_3 + \text{BrCH}_2\text{COOEt} \xrightarrow{\text{Zn}} \beta\text{-hydroxy ester} \xrightarrow{-\text{H}_2\text{O}} \text{Geranic ester}$$
Reduction of geranic ester with lithium aluminum hydride ($\text{LiAlH}_4$) gives geraniol/nerol, which is selectively oxidized with manganese dioxide ($\text{MnO}_2$) or Dess-Martin periodinane to yield **citral**."""
            },
            {
                "id": "sec-2-6",
                "secNumber": "2.6",
                "title": "Monocyclic Monoterpenoids: Limonene — Degradation to p-Cymene & Synthesis",
                "content": r"""Limonene ($C_{10}H_{16}$) is the prototype monocyclic monoterpene hydrocarbon. The $(R)\text{-}(+)$-enantiomer dominates orange and lemon peel oils, whereas the $(S)\text{-}(-)$-enantiomer occurs in spearmint oil and pine needles. The racemate $(\pm)$-limonene is known historically as **dipentene**.

### Structural Elucidation
1. **Formula and Rings**:
   $C_{10}H_{16}$ ($\text{IHD} = 3$). Complete catalytic hydrogenation absorbs two equivalents of hydrogen to afford $p$-menthane ($C_{10}H_{20}$):
   $$\text{C}_{10}\text{H}_{16} + 2\text{ H}_2 \xrightarrow{\text{Pt}} \text{C}_{10}\text{H}_{20} \quad (C_n H_{2n} \implies \mathbf{One\ ring,\ two\ double\ bonds})$$
2. **Aromatization to p-Cymene**:
   Dehydrogenation of limonene over sulfur or selenium at elevated temperatures produces $p$-cymene in near-quantitative yield:
   $$\text{C}_{10}\text{H}_{16} + 2\text{ S} \xrightarrow{\Delta} \text{p-Cymene} + 2\text{ H}_2\text{S}$$
   This proves that the ten carbons are arranged in a **p-menthane (1-methyl-4-isopropylcyclohexane)** skeleton.
3. **Location of the Double Bonds**:
   - Limonene adds two molecules of bromine or hydrogen halides to form a dihydrohalide (e.g., dipentene dihydrochloride), indicating two independent double bonds.
   - Mild oxidation with alkaline potassium permanganate introduces four hydroxyl groups to form a crystalline tetraol (limonetritol/limonetetrol, $C_{10}H_{16}(\text{OH})_4$).
   - Further oxidation with periodic acid cleaves the glycol moieties, releasing one mole of formaldehyde ($\text{HCHO}$) and a keto-acid. The formation of formaldehyde proves that **one double bond is an exocyclic isopropenyl methylene group** ($-\text{C}(\text{CH}_3)=\text{CH}_2$).
   - The second double bond is endocyclic within the cyclohexene ring between C1 and C2.
   Therefore, limonene is **1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene**.

### Total Synthesis of Limonene (Perkin Jr. Classic Route)
W. H. Perkin Jr. achieved the definitive total synthesis of dipentene (1904) starting from $p$-toluic acid:
1. Hydrogenation of $p$-toluic acid yields 4-methylcyclohexanecarboxylic acid.
2. $\alpha$-Bromination followed by dehydrobromination gives 4-methylcyclohex-3-enecarboxylic acid.
3. Conversion to the methyl ester followed by double Grignard addition with methylmagnesium iodide ($\text{CH}_3\text{MgI}$) yields $\alpha$-terpineol.
4. Dehydration of $\alpha$-terpineol with potassium hydrogen sulfate ($\text{KHSO}_4$) furnishes **$(\pm)$-limonene (dipentene)**."""
            },
            {
                "id": "sec-2-7",
                "secNumber": "2.7",
                "title": "Biosynthesis of Monoterpenoids: GPP, LPP & Terpene Synthase Catalysis",
                "content": r"""Monoterpene biosynthesis in plant plastids proceeds from geranyl pyrophosphate (GPP), the universal $C_{10}$ precursor.

### Formation of Geranyl Pyrophosphate (GPP)
Geranyl pyrophosphate synthase (GPPS) catalyzes the head-to-tail condensation of dimethylallyl pyrophosphate (DMAPP) and isopentenyl pyrophosphate (IPP):
1. **Ionization**: DMAPP undergoes enzyme-assisted ionization (coordinated to divalent $Mg^{2+}$ ions) with loss of pyrophosphate ($\text{PP}_i$), generating an allylic carbocation stabilized by resonance:
   $$\text{DMAPP} \to [(\text{CH}_3)_2\text{C}\cdots\text{CH}\cdots\text{CH}_2]^+ + \text{PP}_i$$
2. **Electrophilic Addition**: The allylic cation attacks the nucleophilic exocyclic double bond of IPP at C4, forming a tertiary carbocation intermediate at C3 of the newly attached unit.
3. **Stereospecific Deprotonation**: Loss of the pro-$R$ proton from C2 eliminates the positive charge, generating the trans-double bond of **geranyl pyrophosphate (GPP)**.

### The Problem of Direct Cyclization and the LPP Isomerization
GPP cannot directly cyclize to form monocyclic monoterpenes (such as limonene or $\alpha$-pinene) because its C2=C3 double bond possesses trans (E) stereochemistry; ring closure to a six-membered ring across C1 and C6 would require a geometrically forbidden trans-cyclohexene intermediate.
Monoterpene synthases solve this through an obligate isomerization:
1. Ionization of GPP releases $\text{PP}_i$, and the allylic cation recombines at C3 to form **linalyl pyrophosphate (LPP)**, which possesses a single bond between C2 and C3.
2. Free rotation around the C2-C3 bond occurs in the enzyme active site.
3. Re-ionization of LPP yields the tertiary linalyl carbocation in the required cis conformation, which undergoes anti-Markovnikov-like electrophilic attack on the C6-C7 double bond.
4. Cyclization generates the **$\alpha$-terpinyl carbocation**.
5. Deprotonation of the $\alpha$-terpinyl cation at the methyl group yields **limonene**; alternative rearrangements give pinene, camphene, or cineole."""
            }
        ],
        "problems": [
            {
                "id": "prob-2-1",
                "problemNumber": "2.1",
                "title": "Ozonolysis Cleavage Calculus and Structural Reconstruction of Myrcene",
                "statement": r"""A pure sample of myrcene ($1.362\text{ g}$, $10.0\text{ mmol}$) was subjected to exhaustive ozonolysis in dichloromethane at $-78^\circ\text{C}$ followed by reductive cleavage with zinc dust and acetic acid. Quantitative analysis of the distillate yielded:
- Acetone: $0.581\text{ g}$
- Formaldehyde: $0.601\text{ g}$
- Levulinaldehyde (4-oxopentanal): $1.001\text{ g}$
(a) Determine the molar yield and stoichiometric ratios of the products relative to myrcene.
(b) Write out the structural connectivity and demonstrate why the alternative isomer $\beta$-ocimene ($C_{10}H_{16}$) would yield a different ozonolysis product distribution.""",
                "hints": [
                    r"Molar masses: Myrcene = 136.23 g/mol, Acetone = 58.08 g/mol, Formaldehyde = 30.03 g/mol, Levulinaldehyde = 100.12 g/mol.",
                    r"Calculate moles of each product = mass / molar mass.",
                    r"Draw the structure of \beta-ocimene and cleave its double bonds."
                ],
                "solution": r"""### Step 1: Molar Yield and Stoichiometry
1. **Myrcene consumed**:
   $$n_{\text{myrcene}} = \frac{1.362\text{ g}}{136.23\text{ g/mol}} = 0.0100\text{ mol} = 10.0\text{ mmol}$$
2. **Product moles**:
   $$n_{\text{acetone}} = \frac{0.581\text{ g}}{58.08\text{ g/mol}} = 0.0100\text{ mol} = 10.0\text{ mmol} \quad (\mathbf{1.0\text{ equiv}})$$
   $$n_{\text{formaldehyde}} = \frac{0.601\text{ g}}{30.03\text{ g/mol}} = 0.0200\text{ mol} = 20.0\text{ mmol} \quad (\mathbf{2.0\text{ equiv}})$$
   $$n_{\text{levulinaldehyde}} = \frac{1.001\text{ g}}{100.12\text{ g/mol}} = 0.0100\text{ mol} = 10.0\text{ mmol} \quad (\mathbf{1.0\text{ equiv}})$$

### Step 2: Structural Connectivity Deduction
- $1.0\text{ equiv of acetone}$ requires an isopropylidene terminus: $(\text{CH}_3)_2\text{C}=$.
- $2.0\text{ equiv of formaldehyde}$ requires two vinylidene termini: $=\text{CH}_2$.
- $1.0\text{ equiv of levulinaldehyde}$ ($\text{CH}_3\text{COCH}_2\text{CH}_2\text{CHO}$) possesses one ketone carbonyl and one aldehyde carbonyl.
Connecting the double bond cleavage sites:
$$(\text{CH}_3)_2\text{C}=\text{CH}-\text{CH}_2-\text{CH}_2-\text{C}(=\text{CH}_2)-\text{CH}=\text{CH}_2$$
This confirms the structure of myrcene as 7-methyl-3-methyleneocta-1,6-diene.

### Step 3: Comparison with $\beta$-Ocimene
$\beta$-Ocimene has the structure:
$$(\text{CH}_3)_2\text{C}=\text{CH}-\text{CH}_2-\text{C}(\text{CH}_3)=\text{CH}-\text{CH}=\text{CH}_2$$
Upon ozonolytic cleavage, $\beta$-ocimene yields:
$$\text{Acetone } (1\text{ eq}) + \text{Malondialdehyde } (\text{OHC-CH}_2\text{-CHO}, 1\text{ eq}) + \text{Pyruvaldehyde } (\text{CH}_3\text{COCHO}, 1\text{ eq}) + \text{Formaldehyde } (1\text{ eq})$$
Because $\beta$-ocimene yields only **one equivalent of formaldehyde** (and produces malondialdehyde rather than levulinaldehyde), the experimental isolation of **two equivalents of formaldehyde** and levulinaldehyde definitively rules out ocimene."""
            },
            {
                "id": "prob-2-2",
                "problemNumber": "2.2",
                "title": "Alkaline Cleavage Stoichiometry and Cyclization Energetics of Citral to Cymene",
                "difficulty": "Intermediate",
                "statement": r"""When citral is boiled with dilute aqueous $\text{K}_2\text{CO}_3$, it undergoes retro-aldol cleavage into 6-methylhept-5-en-2-one and acetaldehyde.
(a) Provide the complete curved-arrow mechanism for this retro-aldol transformation.
(b) When citral is heated with potassium bisulfate ($\text{KHSO}_4$), it undergoes cyclodehydration to $p$-cymene. Write the stepwise mechanism for this cyclization, identifying the reactive carbocation intermediates.
(c) Explain why citral forms $p$-cymene rather than an ortho- or meta-substituted benzene isomer.""",
                "hints": [
                    r"Retro-aldol begins with conjugate addition of OH- or attack at the carbonyl followed by retro-aldol cleavage.",
                    r"In acid, protonation of the aldehyde initiates attack by the C6-C7 double bond.",
                    r"Count the carbons to see why a 1,4-disubstituted ring (para) is formed."
                ],
                "solution": r"""### Step 1: Retro-Aldol Mechanism
1. Hydroxide ion ($\text{OH}^-$) attacks the electrophilic carbonyl carbon of citral:
   $$(\text{CH}_3)_2\text{C}=\text{CH}(\text{CH}_2)_2\text{C}(\text{CH}_3)=\text{CH}-\text{CHO} + \text{OH}^- \rightleftharpoons \text{Tetrahedral intermediate}$$
2. Conjugate addition of $\text{OH}^-$ at C3 followed by proton transfer generates the $\beta$-hydroxy aldehyde:
   $$(\text{CH}_3)_2\text{C}=\text{CH}(\text{CH}_2)_2\text{C}(\text{CH}_3)(\text{OH})-\text{CH}_2-\text{CHO}$$
3. Deprotonation of the C3 hydroxyl triggers carbon-carbon bond cleavage:
   The C2-C3 bond pair collapses to form the enolate of acetaldehyde ($\text{CH}_2=\text{CH}-\text{O}^-$), while the C3-O bond forms the ketone carbonyl of 6-methylhept-5-en-2-one.
4. Protonation of the enolate yields acetaldehyde ($\text{CH}_3\text{CHO}$).

### Step 2: Acid-Catalyzed Cyclodehydration to $p$-Cymene
1. **Protonation**: The aldehyde oxygen of citral is protonated by acid ($\text{H}^+$), activating C1 toward nucleophilic attack.
2. **Electrophilic Cyclization**: The electrons of the C6=C7 double bond attack the activated carbonyl carbon (C1), forming a six-membered cyclohexyl carbocation at C7 (tertiary carbocation).
3. **Dehydration**: Loss of a proton and elimination of water ($\text{H}_2\text{O}$) establishes a conjugated cyclohexadiene ring system with an isopropenyl side chain.
4. **Aromatization**: A 1,2-hydride shift and subsequent oxidation/disproportionation yields the fully aromatic system **p-cymene (1-methyl-4-isopropylbenzene)**.

### Step 3: Regiochemical Rationale for Para Substitution
In citral, the carbon chain connecting the isopropylidene moiety ($C_7, C_8, C_9$) and the aldehyde terminus ($C_1$) has the methyl group at C3:
- The cyclization connects C6 to C1, forming a six-membered ring containing carbons 1, 2, 3, 4, 5, and 6.
- In this ring, the methyl group is attached to C3 (or C1 in the numbering of the product), while the isopropyl group (from C7) is attached to C6 (four carbons away).
- This 1,4-relationship across the six-membered ring strictly predetermines **para** regiochemistry."""
            },
            {
                "id": "prob-2-3",
                "problemNumber": "2.3",
                "title": "Optically Active Limonene Racemization Kinetics and Diene Reactivity",
                "statement": r"""$(R)\text{-(+)}$-Limonene has a specific optical rotation of $[\alpha]_D^{20} = +125.6^\circ$ ($\text{c } 1.0, \text{ EtOH}$).
(a) When heated at $250^\circ\text{C}$ in a sealed tube, $(R)$-limonene undergoes first-order thermal racemization with a rate constant $k = 4.8\times 10^{-5}\text{ s}^{-1}$. Calculate the time required for the optical rotation to drop to $[\alpha]_D = +31.4^\circ$.
(b) $(R)$-Limonene reacts with one equivalent of 4-phenyl-1,2,4-triazole-3,5-dione (PTAD) or maleic anhydride only very sluggishly, whereas its isomer $\alpha$-terpinene reacts instantaneously at room temperature. Explain this marked reactivity difference based on Frontier Molecular Orbital (FMO) theory and diene conformation.""",
                "hints": [
                    r"Remember that optical activity drops as alpha(t) = alpha(0) * exp(-2 k_rac t) or alpha(t) = alpha(0) * exp(-k t) depending on whether k is defined for inversion or loss of optical activity.",
                    r"Check whether limonene is a conjugated diene or an isolated diene.",
                    r"Examine s-cis requirement for the Diels-Alder reaction."
                ],
                "solution": r"""### Step 1: Racemization Kinetics Calculation
The loss of optical activity follows first-order decay:
$$\alpha(t) = \alpha_0 e^{-k_{\text{obs}} t}$$
Given $\alpha_0 = +125.6^\circ$ and target $\alpha(t) = +31.4^\circ$:
$$\frac{\alpha(t)}{\alpha_0} = \frac{31.4}{125.6} = 0.250 = \frac{1}{4}$$
Taking the natural logarithm:
$$\ln(0.250) = -k_{\text{obs}} t \implies -1.3863 = -(4.8\times 10^{-5}\text{ s}^{-1}) t$$
$$t = \frac{1.3863}{4.8\times 10^{-5}\text{ s}^{-1}} = 28,881\text{ s} \approx \mathbf{8.02\text{ hours}}$$

### Step 2: Diels-Alder Reactivity and Orbital Symmetry
- **Limonene**:
  Limonene possesses **isolated (non-conjugated) double bonds**: one endocyclic at C1=C2 and one exocyclic at C8=C9, separated by two $sp^3$ methylene carbons (C3 and C4). Because it lacks a conjugated 1,3-diene system, it cannot participate in a concerted $[4+2]$ Diels-Alder cycloaddition with maleic anhydride under thermal conditions.
- **$\alpha$-Terpinene**:
  In contrast, $\alpha$-terpinene (1-isopropyl-4-methylcyclohexa-1,3-diene) is a **conjugated cyclic 1,3-diene**. The two conjugated double bonds are locked within the six-membered ring in an obligate **s-cis conformation**, which provides optimal overlap between the diene HOMO and the dienophile LUMO. This results in an instantaneous, highly exothermic Diels-Alder cycloaddition."""
            },
            {
                "id": "prob-2-4",
                "problemNumber": "2.4",
                "title": "Head-to-Tail Regularity Verification in Monoterpene Scaffolds",
                "difficulty": "Intermediate",
                "statement": r"""For each of the following monoterpenoid natural products, determine whether its carbon skeleton obeys Ingold's Special Isoprene Rule (strictly regular head-to-tail linkages) or contains irregular couplings:
1. Citronellal (from citronella oil)
2. $\alpha$-Pinene (from turpentine)
3. Camphor (from *Cinnamomum camphora*)
4. Chrysanthemic acid (from pyrethrum flowers)
5. Lavandulol (from lavender oil)
Provide the precise carbon connectivity mapping for any irregular structures.""",
                "hints": [
                    r"Break each structure into two C5 fragments.",
                    r"Identify the head (C1) and tail (C4) of each isoprene unit.",
                    r"Look for cyclopropane or non-1,4' branched linkages."
                ],
                "solution": r"""### Step 1: Analysis of Scaffolds
1. **Citronellal ($C_{10}H_{18}O$)**:
   - Acyclic monoterpene: $(\text{CH}_3)_2\text{C}=\text{CH}-\text{CH}_2-\text{CH}_2-\text{CH}(\text{CH}_3)-\text{CH}_2-\text{CHO}$.
   - Consists of two isoprene units linked tail-to-head ($\text{C}4\to\text{C}1^\prime$).
   - **Obeys Ingold's Special Isoprene Rule (Regular)**.

2. **$\alpha$-Pinene ($C_{10}H_{16}$)**:
   - Bicyclic monoterpene containing a fused cyclobutane ring.
   - Biosynthetically formed from GPP via cyclization of the $\alpha$-terpinyl cation without skeletal rearrangement.
   - Both isoprene units maintain head-to-tail orientation.
   - **Obeys Ingold's Special Isoprene Rule (Regular)**.

3. **Camphor ($C_{10}H_{16}O$)**:
   - Bornane bicyclic skeleton. Biosynthesized via a Wagner-Meerwein 1,2-methyl shift from the bornyl cation.
   - Despite the 1,2-rearrangement, the ten carbons originate from a regular head-to-tail GPP precursor.
   - **Formally derived from regular head-to-tail precursor**.

4. **Chrysanthemic Acid ($C_{10}H_{16}O_2$)**:
   - Contains a 1,2,2-trimethylcyclopropane-3-carboxylic acid core attached to an isobutenyl group.
   - Dissection reveals that the two $C_5$ units are connected via a **1'-2-3' irregular cyclopropane coupling** rather than a 1,4'-linkage.
   - **Irregular Monoterpene (Violates Special Isoprene Rule)**.

5. **Lavandulol ($C_{10}H_{18}O$)**:
   - Acyclic monoterpene: $(\text{CH}_3)_2\text{C}=\text{CH}-\text{CH}(\text{CH}_2\text{OH})-\text{C}(\text{CH}_3)=\text{CH}_2$.
   - The two isoprene units are joined via a **head-to-middle (1'-2) linkage**.
   - **Irregular Monoterpene (Violates Special Isoprene Rule)**."""
            },
            {
                "id": "prob-2-5",
                "problemNumber": "2.5",
                "title": "Geranyl Pyrophosphate (GPP) Hydrolysis Thermodynamics and Pyrophosphate Leaving Group Ability",
                "difficulty": "Advanced",
                "statement": r"""The enzymatic cleavage of geranyl pyrophosphate (GPP) to initiate monoterpene cyclization involves departure of the pyrophosphate dianion ($\text{HP}_2\text{O}_7^{3-}$ / $\text{P}_2\text{O}_7^{4-}$).
(a) The standard free energy of hydrolysis of the allylic pyrophosphate ester:
$$\text{GPP} + \text{H}_2\text{O} \to \text{Geraniol} + \text{PP}_i$$
is $\Delta G^{\circ\prime} = -33.5\text{ kJ/mol}$. Calculate the equilibrium constant $K_{\text{eq}}^\prime$ at $298\text{ K}$.
(b) Explain why nature utilizes pyrophosphate ($\text{PP}_i$) rather than monophosphate ($\text{P}_i$) or chloride as a leaving group in cellular terpene biosynthesis, highlighting the role of divalent magnesium ions ($Mg^{2+}$) and downstream pyrophosphatase coupling.""",
                "hints": [
                    r"Use \Delta G^{\circ\prime} = -RT \ln K_{eq}^\prime.",
                    r"Consider the role of inorganic pyrophosphatase (PPase) which hydrolyzes PPi to 2 Pi with \Delta G^{\circ\prime} = -19 kJ/mol.",
                    r"Analyze how Mg2+ coordinates to the oxygen atoms of the diphosphate group."
                ],
                "solution": r"""### Step 1: Equilibrium Constant Calculation
$$\Delta G^{\circ\prime} = -R T \ln K_{\text{eq}}^\prime$$
$$-33,500\text{ J/mol} = -(8.314\text{ J/(mol}\cdot\text{K)})(298.15\text{ K}) \ln K_{\text{eq}}^\prime$$
$$\ln K_{\text{eq}}^\prime = \frac{33,500}{2478.9} = 13.514$$
$$K_{\text{eq}}^\prime = e^{13.514} = \mathbf{7.39\times 10^5}$$
The hydrolysis equilibrium lies overwhelmingly ($>700,000:1$) toward cleavage.

### Step 2: Biochemical Role of the Pyrophosphate Leaving Group
1. **Coordination with Divalent Cations ($Mg^{2+}$)**:
   Pyrophosphate possesses multiple negatively charged oxygen atoms that form a high-affinity bidentate/tridentate chelate complex with two enzyme-bound $Mg^{2+}$ ions held by conserved aspartate motifs ($\text{DDXXD}$). This Lewis-acid coordination neutralizes negative charge, weakens the C-O scissile bond, and facilitates ionization at room temperature without generating harsh acidic conditions.
2. **Irreversible Thermodynamic Pull via Pyrophosphatase**:
   Once released, inorganic pyrophosphate ($\text{PP}_i$) is immediately hydrolyzed by ubiquitous intracellular inorganic pyrophosphatase:
   $$\text{PP}_i + \text{H}_2\text{O} \to 2\text{ P}_i \quad (\Delta G^{\circ\prime} \approx -19.2\text{ kJ/mol})$$
   The combined net reaction has $\Delta G^{\circ\prime}_{\text{total}} = -33.5 + (-19.2) = -52.7\text{ kJ/mol}$, rendering terpene precursor ionization completely irreversible in vivo."""
            },
            {
                "id": "prob-2-6",
                "problemNumber": "2.6",
                "title": "Industrial Synthesis of $\\alpha$- and $\\beta$-Ionone from Citral via Pseudoionone",
                "statement": r"""Ionones are prized violet fragrances and vital synthetic intermediates in the commercial synthesis of Vitamin A (retinol).
(a) Write out the reaction sequence for the synthesis of pseudoionone from citral and acetone, specifying the base catalyst and mechanism.
(b) When pseudoionone is treated with concentrated sulfuric acid ($\text{H}_2\text{SO}_4$), $\beta$-ionone is obtained as the major product. When treated with phosphoric acid ($\text{H}_3\text{PO}_4$) or boron trifluoride ($\text{BF}_3$), $\alpha$-ionone predominates. Provide the mechanistic rationale for this acid-dependent regioselectivity.""",
                "hints": [
                    r"Condensation of citral with acetone is a cross-aldol condensation.",
                    r"Cyclization involves protonation of one of the double bonds to form a tertiary carbocation followed by ring closure.",
                    r"Deprotonation of the cyclohexenyl cation can yield an endocyclic tetrasubstituted alkene (\beta-ionone) or a trisubstituted alkene (\alpha-ionone)."
                ],
                "solution": r"""### Step 1: Synthesis of Pseudoionone
1. **Base-Catalyzed Aldol Condensation**:
   Citral reacts with acetone in the presence of dilute sodium hydroxide or barium hydroxide ($\text{Ba(OH)}_2$):
   $$\text{CH}_3\text{COCH}_3 + \text{OH}^- \rightleftharpoons \text{CH}_3\text{COCH}_2^- + \text{H}_2\text{O}$$
   The acetone enolate attacks the aldehyde carbonyl of citral ($C_1$), generating a $\beta$-hydroxy ketone intermediate.
2. **Dehydration**:
   Base-induced E1cB dehydration eliminates $\text{H}_2\text{O}$ to yield the conjugated polyenone **pseudoionone**:
   $$(\text{CH}_3)_2\text{C}=\text{CH}(\text{CH}_2)_2\text{C}(\text{CH}_3)=\text{CH}-\text{CH}=\text{CH}-\text{COCH}_3$$

### Step 2: Acid-Dependent Cyclization Regioselectivity
Protonation of the terminal double bond of pseudoionone triggers electrophilic attack onto the conjugated system, forming a six-membered cyclized tertiary carbocation intermediate:
1. **$\beta$-Ionone Formation with Strong Acid ($\text{H}_2\text{SO}_4$)**:
   Under strongly acidic conditions ($\text{H}_2\text{SO}_4$, elevated temperature), the reaction is under **thermodynamic control**. Deprotonation occurs from the adjacent ring methylene carbon to produce the more substituted, conjugated double bond:
   - The resulting double bond is tetrasubstituted and conjugated with the side-chain enone system.
   - This thermodynamic product is **$\beta$-ionone**.
2. **$\alpha$-Ionone Formation with Weaker/Steric Acid ($\text{H}_3\text{PO}_4$ or $\text{BF}_3$)**:
   Weaker acids or coordination complexes favor **kinetic control**. The basic counterion preferentially abstracts the more sterically accessible proton from the less substituted methyl/methine position:
   - The resulting double bond is trisubstituted and not fully conjugated with the side chain.
   - This kinetic product is **$\alpha$-ionone**."""
            },
            {
                "id": "prob-2-7",
                "problemNumber": "2.7",
                "title": "Stereoselective Synthesis of (-)-Menthol via Noyori Asymmetric Isomerization",
                "statement": r"""The Takasago industrial process produces over 3,000 metric tons of optically pure $(-)$-menthol annually via the Noyori asymmetric allylic isomerization of diethylgeranylamine.
(a) The process utilizes the chiral catalyst $[(S)\text{-BINAP}-\text{Rh}]^+$. Write the reaction equation showing the transformation of diethylgeranylamine into the chiral enamine.
(b) Hydrolysis of the enamine yields $(R)\text{-(+)}$-citronellal in $>98\%$ enantiomeric excess ($ee$). Write the subsequent Lewis-acid catalyzed intramolecular carbonyl-ene cyclization (Prins-type) to isopulegol.
(c) How is isopulegol converted into $(-)$-menthol, and why does this route exclusively yield the natural all-equatorial $(1R, 2S, 5R)$ stereoisomer?""",
                "hints": [
                    r"Allylic amine to enamine isomerization shifts the double bond.",
                    r"The carbonyl-ene reaction of citronellal forms a six-membered ring with an isopropenyl group.",
                    r"Catalytic hydrogenation of isopulegol reduces only the isopropenyl alkene."
                ],
                "solution": r"""### Step 1: Noyori Asymmetric Isomerization
Diethylgeranylamine, prepared from myrcene and diethylamine, undergoes catalytic enantioselective 1,3-hydrogen shift:
$$\text{Geranyldiethylamine} \xrightarrow{[(S)\text{-BINAP-Rh}]^+} (R)\text{-Citronellal diethylenamine}$$
The chiral Rh-BINAP complex stereospecifically transfers a hydride from C1 to C3, establishing the $(R)$ stereocenter at C3 with $>98\%\text{ ee}$.

### Step 2: Carbonyl-Ene Cyclization to Isopulegol
Hydrolysis of the chiral enamine yields $(R)\text{-(+)}$-citronellal:
$$(R)\text{-Citronellal} \xrightarrow{\text{ZnBr}_2 \text{ or } \text{Al(OAr)}_3} (-)\text{-Isopulegol}$$
In the presence of zinc bromide ($\text{ZnBr}_2$), $(R)$-citronellal adopts a chair-like transition state:
- The bulky C3 methyl group occupies a low-energy **equatorial** position.
- Intramolecular concerted carbonyl-ene reaction between the C6=C7 double bond and the Lewis acid-activated aldehyde forms the cyclohexyl ring.
- This stereospecifically generates $(-)$-isopulegol with three stereocenters: C1 ($\text{OH}$, equatorial), C2 (isopropenyl, equatorial), and C5 (methyl, equatorial).

### Step 3: Hydrogenation to $(-)$-Menthol
Catalytic hydrogenation of the exocyclic isopropenyl double bond of $(-)$-isopulegol over Raney nickel or Pd/C yields pure **$(-)$-menthol**:
$$(-)\text{-Isopulegol} + \text{H}_2 \xrightarrow{\text{Ni / Pd}} (1R, 2S, 5R)\text{-Menthol}$$
Because all three substituents—the hydroxyl group at C1, the isopropyl group at C2, and the methyl group at C5—reside in **all-equatorial orientations** on the cyclohexane chair conformation, $(-)$-menthol represents the thermodynamically most stable diastereomer, completely avoiding 1,3-diaxial steric strain."""
            }
        ]
    }
    units.append(u2)

    # =========================================================================
    # UNIT 3: Terpenoids II: Sesquiterpenoids, Higher Terpenes & Cyclizations
    # =========================================================================
    u3 = {
        "id": "unit-3",
        "unitNumber": 3,
        "title": "Unit 3: Terpenoids II: Sesquiterpenoids, Higher Terpenes & Biosynthetic Cyclizations",
        "leadSummary": "Advanced chemistry of sesquiterpenoids ($C_{15}$), diterpenes ($C_{20}$), and triterpenes ($C_{30}$): structural elucidation of farnesol, cadinene, and caryophyllene, the Stork-Eschenmoser stereochemical hypothesis of polyene cyclization, carbocation rearrangement cascades (Wagner-Meerwein, 1,2-hydride and methyl shifts), and the catalytic enzymology of terpene cyclases.",
        "simulations": ["sim_nat_terpene_cyclization_cascade"],
        "sections": [
            {
                "id": "sec-3-1",
                "secNumber": "3.1",
                "title": "Sesquiterpenoids: Structural Diversity, Classification ($C_{15}H_{24}$) & Bioactivity",
                "content": r"""Sesquiterpenoids are $C_{15}$ isoprenoids constructed from three isoprene units ($n=3$). With over 10,000 cataloged structures, they represent the pinnacle of structural complexity among small-molecule natural products, featuring bridged, fused, and spiro-carbocyclic frameworks.

### Taxonomic and Skeletal Classification
1. **Acyclic Sesquiterpenes**: E.g., Farnesol, nerolidol ($C_{15}H_{26}O$), possessing zero rings and four degrees of unsaturation.
2. **Monocyclic Sesquiterpenes**: E.g., $\alpha$-Bisabolene, germacrene D, humulene ($C_{15}H_{24}$), containing a single carbocycle.
3. **Bicyclic Sesquiterpenes**: E.g., Cadinene (decalin-type), $\beta$-caryophyllene (fused bicyclo[7.2.0]undecane), and eudesmol.
4. **Tricyclic Sesquiterpenes**: E.g., Cedrol, thujopsene, patchoulol, and longifolene.
5. **Sesquiterpene Lactones**: E.g., Artemisinin (antimalarial endoperoxide from *Artemisia annua*) and santonin (anthelmintic from *Artemisia maritima*), characterized by $\alpha$-methylene-$\gamma$-lactone rings that react with protein thiols via Michael addition."""
            },
            {
                "id": "sec-3-2",
                "secNumber": "3.2",
                "title": "Acyclic Sesquiterpenoids: Farnesol — Degradation, Stereochemistry & Synthesis",
                "content": r"""Farnesol ($C_{15}H_{26}O$) is the prototype acyclic sesquiterpene alcohol, isolated from ambrette seed oil, rose, and citronella.

### Structural Elucidation
1. **Molecular Formula and Degree of Unsaturation**:
   Elemental analysis and HRMS establish $C_{15}H_{26}O$ ($\text{IHD} = 3$).
   Catalytic hydrogenation absorbs three molar equivalents of hydrogen:
   $$\text{C}_{15}\text{H}_{26}\text{O} + 3\text{ H}_2 \xrightarrow{\text{Pt}} \text{C}_{15}\text{H}_{32}\text{O} \quad (\text{Hexahydrofarnesol})$$
   Because the saturated product is an acyclic alcohol ($C_n H_{2n+2}O$ for $n=15$), farnesol contains **three double bonds and zero rings**.
2. **Functional Group Characterization**:
   Farnesol forms an acetate ester with acetic anhydride, reacts with phenyl isocyanate to form a urethane, and on mild oxidation with chromic acid or Dess-Martin periodinane yields the aldehyde **farnesal** ($C_{15}H_{24}O$). This proves that farnesol is a **primary allylic alcohol** ($-\text{CH}_2\text{OH}$).
3. **Exhaustive Ozonolysis**:
   Ozonolysis followed by oxidative workup yields:
   $$\text{Farnesol} \xrightarrow{\text{O}_3, \text{ H}_2\text{O}_2} \text{Acetone} + 2\text{ Levulinic acid} + \text{Glycolic acid (or Glyoxal)}$$
   $$\text{CH}_3\text{COCH}_3 + 2\text{ CH}_3\text{COCH}_2\text{CH}_2\text{COOH} + \text{HOCH}_2\text{COOH}$$
   The isolation of two equivalents of levulinic acid demonstrates a repeating sequence of two tail-to-head isoprene linkages connecting an isopropylidene group to the allylic alcohol terminus:
   $$(\text{CH}_3)_2\text{C}=\text{CH}-\text{CH}_2-\text{CH}_2-\text{C}(\text{CH}_3)=\text{CH}-\text{CH}_2-\text{CH}_2-\text{C}(\text{CH}_3)=\text{CH}-\text{CH}_2\text{OH}$$
   Farnesol is therefore **3,7,11-trimethyldodeca-2,6,10-trien-1-ol**."""
            },
            {
                "id": "sec-3-3",
                "secNumber": "3.3",
                "title": "Cyclic Sesquiterpenes: Bisabolene, Cadinene & Caryophyllene Architectures",
                "content": r"""Cyclic sesquiterpenoids illustrate how conformational pre-organization directs carbocation trajectories into disparate polycyclic ring topologies.

### $\alpha$-Bisabolene (Monocyclic)
$\alpha$-Bisabolene ($C_{15}H_{24}$) possesses a 1-methyl-4-(6-methylhept-5-en-2-yl)cyclohex-1-ene framework. Dehydrogenation over sulfur yields $p$-cymene along with aliphatic fragments, while complete hydrogenation yields bisabolane ($C_{15}H_{30}$).

### Cadinene (Bicyclic Decalin Framework)
$\beta$-Cadinene ($C_{15}H_{24}$) occurs in oil of cubebs. Dehydrogenation with selenium or sulfur at $300^\circ\text{C}$ aromatizes the bicyclic ring system to yield **cadalene (1,6-dimethyl-4-isopropylnaphthalene)**:
$$\text{Cadinene} \xrightarrow{\text{Se}, 300^\circ\text{C}} \text{Cadalene } (C_{15}H_{18}) + 3\text{ H}_2\text{Se}$$
The isolation of cadalene proved that cadinene contains a decalin (bicyclo[4.4.0]decane) core with methyl groups at C1 and C6 and an isopropyl group at C4.

### $\beta$-Caryophyllene (Fused Bicyclo[7.2.0]undecane)
$\beta$-Caryophyllene, isolated from clove oil (*Syzygium aromaticum*), possesses an unprecedented 9-membered carbocycle fused trans to a 4-membered cyclobutane ring. The nine-membered ring incorporates a strained **trans-cycloalkene** double bond. Hydration with dilute acid causes a deep skeletal rearrangement yielding the tricyclic alcohol **caryophyllene alcohol**."""
            },
            {
                "id": "sec-3-4",
                "secNumber": "3.4",
                "title": "Biosynthesis of Higher Terpenoids: FPP, GGPP & Polyene Assembly",
                "content": r"""The assembly of sesquiterpenes, diterpenes, and triterpenes is catalyzed by prenyltransferases that execute iterative chain elongation reactions.

### Farnesyl Pyrophosphate (FPP) Synthase
FPP synthase elongates geranyl pyrophosphate (GPP, $C_{10}$) by adding a second molecule of isopentenyl pyrophosphate (IPP, $C_5$):
$$\text{GPP} + \text{IPP} \xrightarrow{\text{FPPS, } Mg^{2+}} \text{2E,6E-FPP} + \text{PP}_i$$
The reaction mechanism mirrors GPPS: ionization of GPP generates an allylic carbocation that adds to the exocyclic double bond of IPP, followed by stereospecific elimination of the pro-$R$ proton at C2 to form (2E,6E)-FPP.

### Geranylgeranyl Pyrophosphate (GGPP) Synthase
GGPP synthase condenses (2E,6E)-FPP with a third IPP molecule to generate (2E,6E,10E)-geranylgeranyl pyrophosphate (GGPP, $C_{20}$):
$$\text{FPP} + \text{IPP} \xrightarrow{\text{GGPPS}} \text{GGPP} + \text{PP}_i$$
GGPP serves as the universal precursor for all diterpenes (e.g., taxadiene, abietic acid, gibberellins) and dimerizes tail-to-tail to form phytoene, the origin of tetraterpenes (carotenoids)."""
            },
            {
                "id": "sec-3-5",
                "secNumber": "3.5",
                "title": "Polycyclization Cascades: Squalene Epoxidation & The Stork-Eschenmoser Hypothesis",
                "content": r"""One of the most profound reactions in organic chemistry is the polycyclization of acyclic polyenes to polycyclic steroids and triterpenes.

### Squalene to 2,3-Oxidosqualene
In eukaryotes, squalene ($C_{30}H_{50}$) is stereospecifically epoxidized by squalene monooxygenase (a flavin-dependent hydroxylase consuming $\text{O}_2$ and NADPH) to form $(3S)\text{-2,3-oxidosqualene}$:
$$\text{Squalene} + \text{O}_2 + \text{NADPH} + \text{H}^+ \to (3S)\text{-2,3-Oxidosqualene} + \text{NADP}^+ + \text{H}_2\text{O}$$

### The Stork-Eschenmoser Hypothesis
Formulated independently by Gilbert Stork and Albert Eschenmoser in 1955, this hypothesis posits that the stereochemical outcome of polyene cyclization is governed by **stereospecific, concerted, anti-periplanar electrophilic additions** along a pre-organized, all-chair (or chair-boat) conformational template:
1. Protonation of the epoxide ring by an active-site aspartic acid residue triggers epoxide ring opening.
2. The developing carbocation at C2 induces concerted Markovnikov anti-periplanar attack by the adjacent C6=C7 $\pi$-bond.
3. This creates ring A and generates a carbocation that triggers successive closures of rings B, C, and D in an ultra-fast cascade:
   $$\text{Chair} \to \text{Boat} \to \text{Chair} \to \text{Boat} \quad (\text{Folding landscape})$$
4. The cyclization forms four rings and up to seven stereocenters simultaneously with absolute stereocontrol."""
            },
            {
                "id": "sec-3-6",
                "secNumber": "3.6",
                "title": "Carbocation Rearrangements: Wagner-Meerwein Shifts & Cation Trajectories",
                "content": r"""Following initial ring closure, the protosteryl carbocation undergoes a stereospecifically orchestrated series of skeletal rearrangements before final deprotonation.

### The Protosteryl to Lanosterol Cascade
In the active site of oxidosqualene cyclase (lanosterol synthase):
1. Polycyclization terminates at the $C_{20}$ protosteryl cation with a positive charge at C20.
2. A concerted series of **suprafacial 1,2-hydride and 1,2-methyl shifts** occurs across the tetracyclic framework:
   - $17\alpha\text{-H} \to 20\alpha$ hydride shift
   - $13\alpha\text{-H} \to 17\alpha$ hydride shift
   - $14\beta\text{-CH}_3 \to 13\beta$ methyl shift
   - $8\alpha\text{-CH}_3 \to 14\alpha$ methyl shift
3. The resulting positive charge at C9 is extinguished by stereospecific elimination of the $9\beta$-proton, forming the C8=C9 double bond of **lanosterol** ($C_{30}H_{50}O$).

### Wagner-Meerwein Rearrangements in Terpenes
A Wagner-Meerwein rearrangement is a 1,2-migration of a hydride, alkyl, or aryl group to an adjacent carbocation center:
$$\text{R}_3\text{C}-\text{CH}^+-\text{R}^\prime \xrightarrow{\text{1,2-shift}} \text{R}_2\text{C}^+-\text{CH(R)}-\text{R}^\prime$$
This rearrangement is driven by the relief of ring strain (e.g., in bicyclic camphene $\to$ isobornyl transformations) or the conversion of a secondary carbocation into a more stable tertiary carbocation."""
            },
            {
                "id": "sec-3-7",
                "secNumber": "3.7",
                "title": "Mechanistic Enzymology of Terpene Cyclases: Aspartate Motifs & $Mg^{2+}$ Clusters",
                "content": r"""Terpene synthases (cyclases) are classified into two mechanistic classes based on how carbocation generation is initiated.

### Class I Terpene Cyclases
- **Initiation**: Ionization of the substrate pyrophosphate ($\text{OPP}$) ester bond.
- **Catalytic Motifs**: Possess conserved magnesium-binding motifs:
  - $\text{DDXXD}$ motif on helix D.
  - $(\text{N/D})\text{DXX}(\text{S/T})\text{XXXE}$ motif on helix H.
- Three divalent magnesium ions ($Mg_A^{2+}, Mg_B^{2+}, Mg_C^{2+}$) coordinate the oxygens of the pyrophosphate group and anchor it within the active-site cavity. Substrate binding induces a conformational change that caps the active site with flexible loops, creating an anhydrous, low-dielectric chamber lined with aromatic residues (Phe, Tyr, Trp) that stabilize carbocation intermediates via cation-$\pi$ interactions without premature quenching by water.

### Class II Terpene Cyclases
- **Initiation**: Protonation of an unactivated double bond or epoxide oxygen.
- **Catalytic Motif**: Conserved **DXDD** motif (e.g., squalene-hopene cyclase and oxidosqualene cyclase). The middle aspartate residue acts as an active-site Brønsted acid with an abnormally depressed $pK_a$, protonating the terminal alkene to trigger cyclization."""
            }
        ],
        "problems": [
            {
                "id": "prob-3-1",
                "problemNumber": "3.1",
                "title": "Farnesol Ozonolysis Stoichiometry and Tri-Isoprene Structure Deconvolution",
                "statement": r"""A sample of pure farnesol ($2.224\text{ g}$, $10.0\text{ mmol}$) was dissolved in methanol and treated with excess ozone at $-78^\circ\text{C}$. Subsequent oxidation with warm aqueous alkaline hydrogen peroxide ($\text{H}_2\text{O}_2 / \text{NaOH}$) cleaved all fragments to their terminal carboxylic acids.
(a) Write down the structures and calculate the stoichiometric molar amounts of each isolated fragment.
(b) Explain why oxidation of farnesal (the corresponding aldehyde) with ozone followed by the same workup yields glyoxylic acid ($\text{HCOCOOH}$) instead of glycolic acid ($\text{HOCH}_2\text{COOH}$).""",
                "hints": [
                    r"Farnesol = 3,7,11-trimethyldodeca-2,6,10-trien-1-ol.",
                    r"The three double bonds are at C2=C3, C6=C7, and C10=C11.",
                    r"Ozonolysis of an allylic alcohol -C(CH3)=CH-CH2OH with H2O2 oxidation yields a ketone from C3 and hydroxyacetic acid (glycolic acid) from C1-C2."
                ],
                "solution": r"""### Step 1: Cleavage Sites in Farnesol
Farnesol structure:
$$(\text{CH}_3)_2\text{C}^{11}=\text{C}^{10}\text{H}-\text{C}^9\text{H}_2-\text{C}^8\text{H}_2-\text{C}^7(\text{CH}_3)=\text{C}^6\text{H}-\text{C}^5\text{H}_2-\text{C}^4\text{H}_2-\text{C}^3(\text{CH}_3)=\text{C}^2\text{H}-\text{C}^1\text{H}_2\text{OH}$$
Cleavage occurs at:
1. Double bond C10=C11:
   - Terminus: $(\text{CH}_3)_2\text{C}=$ becomes **Acetone** ($\text{CH}_3\text{COCH}_3$).
   - Moles produced: **$10.0\text{ mmol}$ (1.0 equiv)**.
2. Internal segments (C6-C9 and C2-C5):
   - Segment C9-C8-C7: $=\text{CH}-\text{CH}_2-\text{CH}_2-\text{C}(\text{CH}_3)=$ becomes **Levulinic acid** ($\text{HOOC}-\text{CH}_2-\text{CH}_2-\text{COCH}_3$).
   - Segment C5-C4-C3: $=\text{CH}-\text{CH}_2-\text{CH}_2-\text{C}(\text{CH}_3)=$ becomes a second molecule of **Levulinic acid**.
   - Moles produced: **$20.0\text{ mmol}$ (2.0 equiv)**.
3. Terminal allylic alcohol segment (C1-C2):
   - $=\text{CH}-\text{CH}_2\text{OH}$ oxidizes to **Glycolic acid** ($\text{HOOC}-\text{CH}_2\text{OH}$).
   - Moles produced: **$10.0\text{ mmol}$ (1.0 equiv)**.

### Step 2: Farnesal Ozonolysis
In farnesal, the C1 carbon is an aldehyde ($-\text{CHO}$) rather than a primary alcohol ($-\text{CH}_2\text{OH}$):
$$=\text{CH}-\text{CHO} \xrightarrow{\text{O}_3, \text{ H}_2\text{O}_2} \text{HOOC}-\text{COOH} \quad (\text{Oxalic acid}) \quad \text{or} \quad \text{OHC}-\text{COOH} \quad (\text{Glyoxylic acid})$$
Oxidative workup cleaves the $=\text{CH}-\text{CHO}$ unit to **glyoxylic acid** ($\text{OHC}-\text{COOH}$) or oxalic acid, confirming that the precursor farnesol possessed a terminal alcohol rather than an aldehyde."""
            },
            {
                "id": "prob-3-2",
                "problemNumber": "3.2",
                "title": "Carbocation Trajectory and Concerted vs Stepwise Cyclization of FPP to Bisabolene",
                "statement": r"""In the biosynthesis of $\alpha$-bisabolene from $(2E, 6E)$-farnesyl pyrophosphate (FPP):
(a) Explain why (2E,6E)-FPP cannot directly undergo cyclization to the six-membered bisabolyl ring and identify the required enzyme-catalyzed allylic isomerization step.
(b) Trace the stepwise mechanism of cyclization from nerolidyl pyrophosphate (NPP), showing the generation of carbocation intermediates and the final deprotonation step.
(c) Distinguish between a concerted electrocyclic mechanism and a stepwise carbocation cascade using stereochemical marker arguments.""",
                "hints": [
                    r"Compare with GPP -> LPP isomerization in monoterpenes.",
                    r"Nerolidyl pyrophosphate allows free rotation around the C2-C3 bond.",
                    r"The tertiary allylic carbocation undergoes attack by the C6-C7 double bond."
                ],
                "solution": r"""### Step 1: Requirement for Allylic Isomerization
Just as in monoterpene synthesis (where GPP must isomerize to LPP), $(2E, 6E)$-FPP possesses a trans (E) double bond at C2=C3:
- Direct electrophilic cyclization between C1 and C6 would require a geometrically impossible trans-double bond inside a developing six-membered ring.
- Terpene cyclases catalyze an initial ionization-recombination isomerization of FPP to **$(3R)\text{-nerolidyl pyrophosphate (NPP)}$**:
  $$\text{FPP} \rightleftharpoons [\text{Farnesyl cation}] \cdot \text{PP}_i \rightleftharpoons \text{NPP}$$
- In NPP, the C2-C3 bond is a single bond with free rotation, allowing the carbon chain to fold into the requisite cisoid conformation.

### Step 2: Cyclization Mechanism to $\alpha$-Bisabolene
1. **Ionization**: NPP ionizes by loss of $\text{PP}_i$, generating the tertiary allylic carbocation.
2. **Ring Closure**: Electrophilic attack of the C1 cation onto the C6=C7 $\pi$-bond forms a six-membered ring, yielding the tertiary **bisabolyl carbocation** at C7.
3. **Deprotonation**: An active-site base abstracts a proton from the adjacent C1 position of the cyclohexenyl ring, establishing the endocyclic C1=C2 double bond of **$\alpha$-bisabolene**.

### Step 3: Stepwise vs Concerted Discrimination
In isotopic labeling experiments with stereospecifically deuterated $(1R)\text{-}[1\text{-}^2\text{H}]\text{FPP}$:
- A concerted electrocyclic ring closure would require strict retention or inversion of configuration governed by Woodward-Hoffmann orbital symmetry rules.
- Experimental tracking reveals loss of stereochemical memory at C1 and variable trapping of solvent/water adducts under perturbed active-site mutants.
- This confirms that cyclization proceeds via a **stepwise discrete carbocation intermediate** stabilized by cation-$\pi$ interactions with active-site phenylalanine and tryptophan side chains."""
            },
            {
                "id": "prob-3-3",
                "problemNumber": "3.3",
                "title": "Stereospecific Stork-Eschenmoser Cyclization: Lanosterol vs Cycloartenol Divergence",
                "statement": r"""The cyclization of $(3S)\text{-2,3-oxidosqualene}$ represents a major evolutionary divergence point between kingdoms: animals and fungi produce **lanosterol** (leading to cholesterol and ergosterol), whereas photosynthetic plants produce **cycloartenol** (leading to phytosterols).
(a) State the initial folding conformation (chair vs boat for rings A, B, C, D) adopted by oxidosqualene in lanosterol synthase vs cycloartenol synthase.
(b) Explain the precise mechanistic bifurcation that occurs after the formation of the protosteryl cation, detailing how cycloartenol forms a 9,19-cyclopropane ring instead of eliminating the $9\beta$-proton.""",
                "hints": [
                    r"Lanosterol cyclase folds oxidosqualene into a chair-boat-chair-boat conformation.",
                    r"Cycloartenol synthase also forms the protosteryl cation but quenches the charge at C9 differently.",
                    r"Look at the C19 methyl group and its distance to C9."
                ],
                "solution": r"""### Step 1: Folding Conformation
1. **Lanosterol Synthase (Animals / Fungi)**:
   The enzyme active site folds $(3S)$-oxidosqualene into a **chair-boat-chair-boat (C-B-C-B)** conformation.
   - Ring A: Chair
   - Ring B: Boat
   - Ring C: Chair
   - Ring D: Boat
2. **Cycloartenol Synthase (Plants)**:
   Plants also utilize a **chair-boat-chair-boat** folding template that generates the identical tetracyclic **protosteryl C20-cation intermediate** with $17\beta$-stereochemistry.

### Step 2: Mechanistic Bifurcation
Following four concerted hydride and methyl migrations ($17\alpha\text{-H}\to 20$, $13\alpha\text{-H}\to 17$, $14\beta\text{-Me}\to 13$, $8\alpha\text{-Me}\to 14$), a carbocation is localized at the **C9** position.
- **Path A (Lanosterol Synthase)**:
  An active-site catalytic base abstracts the axial **$9\beta\text{-H}$ proton**. The C9-H electron pair collapses to form the $\Delta^{8,9}$ tetrasubstituted endocyclic double bond of **lanosterol**.
- **Path B (Cycloartenol Synthase)**:
  In cycloartenol synthase, a conserved tyrosine/histidine residue acts as a catalytic base, positioning itself near the **$C_{19}$ angular methyl group** attached to C10 rather than the $9\beta$-proton.
  The base abstracts a proton from the $C_{19}\text{ methyl}$ group ($-\text{CH}_3 \to -\text{CH}_2^-$), and the resulting electron pair attacks the carbocation at C9:
  $$\text{C}_{19}\text{H}_2^- + \text{C}9^+ \to \mathbf{9,19-cyclopropane\ ring}$$
  This forms **cycloartenol**, containing a unique cyclopropane ring bridging C9 and C10."""
            },
            {
                "id": "prob-3-4",
                "problemNumber": "3.4",
                "title": "Wagner-Meerwein Rearrangement Energetics in Camphene-Isoborneol Equilibria",
                "statement": r"""In the industrial synthesis of synthetic camphor, $\alpha$-pinene is treated with anhydrous hydrogen chloride to yield bornyl chloride ('artificial camphor'). This reaction proceeds via an initial Wagner-Meerwein rearrangement of the pinyl carbocation to the bornyl carbocation.
(a) Draw the curved-arrow mechanism for the acid-catalyzed rearrangement of $\alpha$-pinene to bornyl chloride, showing the cleavage of the cyclobutane ring.
(b) When isoborneol is dehydrated with acid, it yields camphene. Write the mechanism of this second Wagner-Meerwein rearrangement, detailing the non-classical 2-norbornyl-type cation intermediate.""",
                "hints": [
                    r"Pinene has a fused 4-membered cyclobutane ring under significant strain.",
                    r"Protonation of the pinene double bond creates a tertiary carbocation adjacent to the cyclobutane ring.",
                    r"Relief of ring strain drives the 1,2-alkyl shift that expands the 4-membered ring to a 5-membered cyclopentane ring."
                ],
                "solution": r"""### Step 1: Rearrangement of $\alpha$-Pinene to Bornyl Chloride
1. **Protonation**: Addition of $\text{H}^+$ from $\text{HCl}$ to the endocyclic double bond of $\alpha$-pinene generates a tertiary carbocation at C2 (the $\alpha$-pinyl cation).
2. **Wagner-Meerwein Ring Expansion**:
   The highly strained cyclobutane ring (strain energy $\approx 110\text{ kJ/mol}$) relieves ring strain via a 1,2-alkyl migration:
   - The C6-C7 bond of the four-membered ring migrates to the electron-deficient C2 center.
   - This expands the four-membered ring into a five-membered cyclopentane ring, generating the bicyclo[2.2.1]heptyl (**bornyl**) carbocation.
3. **Chloride Attack**:
   Nucleophilic attack of chloride ion ($\text{Cl}^-$) on the bornyl cation occurs stereospecifically from the exo face, yielding **bornyl chloride**.

### Step 2: Isoborneol Dehydration to Camphene
1. **Protonation and Water Loss**:
   Protonation of the hydroxyl group of isoborneol followed by loss of $\text{H}_2\text{O}$ generates the secondary 2-bornyl cation.
2. **Wagner-Meerwein 1,2-Shift**:
   To avoid the secondary carbocation, the C1-C6 ring bond undergoes a 1,2-alkyl shift to C2, forming the isomeric tertiary **camphenyl carbocation**.
3. **Deprotonation**:
   Loss of an exocyclic proton from the methyl group releases a proton and forms the terminal alkene double bond of **camphene** ($C_{10}H_{16}$).
The thermodynamic driving force is the conversion of a secondary carbocation into a resonance-stabilized allylic or tertiary center accompanied by favorable steric realignment."""
            },
            {
                "id": "prob-3-5",
                "problemNumber": "3.5",
                "title": "Squalene Synthase Reductive Dimerization Mechanism via Presqualene Pyrophosphate",
                "statement": r"""Squalene synthase catalyzes the reductive tail-to-tail dimerization of two molecules of farnesyl pyrophosphate (FPP, $C_{15}$) to squalene ($C_{30}$) using NADPH:
$$2\text{ FPP} + \text{NADPH} + \text{H}^+ \xrightarrow{\text{SQS}} \text{Squalene} + 2\text{ PP}_i + \text{NADP}^+$$
(a) The reaction proceeds through a stable, isolable cyclopropyl intermediate known as presqualene pyrophosphate (PSPP). Provide the mechanism for the formation of PSPP from the two FPP units.
(b) In the second stage, PSPP undergoes ionization, ring rearrangement, and hydride transfer from NADPH. Outline the sequence of carbocation shifts and the stereochemistry of the hydride addition.""",
                "hints": [
                    r"The first FPP unit ionizes to an allylic carbocation that attacks the C2=C3 double bond of the second FPP.",
                    r"Loss of a proton generates the cyclopropane ring of PSPP.",
                    r"Ionization of PPi from PSPP triggers cyclopropylmethyl-to-cyclobutyl-to-allylcarbinyl rearrangements."
                ],
                "solution": r"""### Step 1: Formation of Presqualene Pyrophosphate (PSPP)
1. **Ionization of First FPP**:
   One molecule of FPP ionizes with release of $\text{PP}_i$, generating the allylic farnesyl carbocation.
2. **Nucleophilic Addition to Second FPP**:
   The allylic cation attacks the terminal C2=C3 double bond of the second intact FPP molecule, forming a tertiary carbocation intermediate at C3 while retaining the second $\text{PP}_i$ group.
3. **Deprotonation and Cyclopropane Formation**:
   An active-site basic residue abstracts a proton from C1 of the attacking farnesyl group. Intramolecular displacement of the positive charge at C3 closes a stable **cyclopropane ring**, yielding **presqualene pyrophosphate (PSPP)**.

### Step 2: Reductive Rearrangement to Squalene
1. **Ionization of PSPP**:
   The remaining pyrophosphate group on the cyclopropane ring ionizes, assisted by active-site $Mg^{2+}$, generating a cyclopropylcarbinyl carbocation.
2. **Cyclopropyl Ring Opening**:
   The cyclopropylcarbinyl cation rearranges via a bicyclobutonium/cyclobutyl-like trajectory to relieve cyclopropane ring strain:
   - Carbon-carbon bond cleavage of the cyclopropane ring generates a tertiary carbocation intermediate directly conjugated with an allylic system.
3. **Hydride Transfer from NADPH**:
   The hydride ion ($H^-$) from the nicotinamide ring of NADPH is stereospecifically transferred to the carbocation center.
   This completes the formation of the central **tail-to-tail (4-4') carbon-carbon single bond** of **squalene**, with release of $\text{NADP}^+$."""
            },
            {
                "id": "prob-3-6",
                "problemNumber": "3.6",
                "title": "Thermodynamic Driving Force and Ring Strain in $\\beta$-Caryophyllene",
                "statement": r"""$\beta$-Caryophyllene possesses an unusual bicyclo[7.2.0]undec-4-ene skeleton featuring a 9-membered macrocycle containing an endocyclic trans-double bond fused to a 4-membered cyclobutane ring.
(a) Explain why a trans-double bond within a 9-membered ring is thermodynamically strained ($\Delta H^\circ_{\text{strain}} \approx 67\text{ kJ/mol}$), and describe its conformational chirality (atropisomerism).
(b) When $\beta$-caryophyllene is treated with aqueous acid, it undergoes deep transannular cyclization to caryophyllene alcohol. Trace the curved-arrow mechanism of this cascade, showing how transannular $\pi$-$\pi$ interaction relieves macrocyclic strain.""",
                "hints": [
                    r"Smallest ring that can accommodate a trans double bond at room temperature is 8-membered (trans-cyclooctene).",
                    r"Transannular cyclization involves protonation of the trans double bond followed by attack by the exocyclic methylene group.",
                    r"The product is a tricyclic alcohol."
                ],
                "solution": r"""### Step 1: Strain Energy and Chirality of the Trans-Cyclononene Ring
1. **Ring Strain Origins**:
   In trans-cycloalkenes, the trans double bond forces the adjacent methylene chains to cross above and below the double bond plane. In medium rings ($C_8 - C_{10}$):
   - Severe Pitzer torsional strain (eclipsing of C-H bonds) and Prelog transannular van der Waals repulsions between cross-ring hydrogens arise.
   - The trans-double bond in $\beta$-caryophyllene cannot achieve optimal planar $\pi$-overlap without twisting, resulting in approximately **$67\text{ kJ/mol}$ of excess ring strain** compared to an acyclic trans-alkene.
2. **Conformational Atropisomerism**:
   Because the bulky 9-membered ring cannot freely slip past the fused cyclobutane ring, rotation of the trans-double bond through the ring cavity is blocked at room temperature. This confers **planar/conformational chirality**, allowing distinct stable atropisomeric conformations ($\alpha\alpha$ and $\beta\beta$ conformers).

### Step 2: Acid-Catalyzed Transannular Cyclization
1. **Protonation**:
   Protonation of the strained trans-double bond by $\text{H}^+$ occurs from the less hindered face, generating a secondary/tertiary carbocation within the 9-membered ring.
2. **Transannular $\pi$-Participation**:
   The exocyclic methylene ($\text{C}=\text{CH}_2$) double bond across the ring is held in close spatial proximity ($<3.2\text{ \AA}$) by the macrocyclic conformation. The $\pi$-electrons of this methylene attack the carbocation center in a **transannular electrophilic cyclization**.
3. **Water Quenching**:
   This cyclization closes a stable six-membered ring, eliminating the strained 9-membered macrocycle and forming a tricyclic carbocation. Attack of a water molecule followed by deprotonation yields crystalline **caryophyllene alcohol**.
The massive driving force is the relief of medium-ring strain ($\Delta G^\circ \ll 0$) through conversion of a strained medium ring into fused 6- and 5-membered rings."""
            },
            {
                "id": "prob-3-7",
                "problemNumber": "3.7",
                "title": "Singlet Oxygen Quenching Kinetics and Conjugated Polyene Photoprotection in $\\beta$-Carotene",
                "statement": r"""$\beta$-Carotene ($C_{40}H_{56}$) is a tetraterpenoid possessing a conjugated polyene system of 11 conjugated double bonds. In photosynthesis, it acts as a vital photoprotective agent by quenching reactive singlet oxygen ($^1\text{O}_2$, $^1\Delta_g$) with a diffusion-controlled rate constant $k_q = 1.2\times 10^{10}\text{ M}^{-1}\text{s}^{-1}$.
(a) The energy of singlet oxygen above the triplet ground state ($^3\Sigma_g^-$) is $E(^1\Delta_g) = 94.2\text{ kJ/mol}$ ($0.98\text{ eV}$). Calculate the minimum triplet energy $E(T_1)$ that $\beta$-carotene must possess to enable spin-allowed triplet-triplet energy transfer.
(b) Write the kinetic rate law for the competitive decay of $^1\text{O}_2$ in a cellular lipid membrane containing $[\beta\text{-Carotene}] = 0.50\text{ mM}$, given the intrinsic non-radiative solvent decay rate constant $k_0 = 4.0\times 10^4\text{ s}^{-1}$. Calculate the percentage of $^1\text{O}_2$ intercepted by $\beta$-carotene.""",
                "hints": [
                    r"Singlet oxygen quenching proceeds via energy transfer: ^1O_2 + ^1Car -> ^3O_2 + ^3Car*.",
                    r"For this to be exothermic, E(T_1, Car) must be less than 94.2 kJ/mol.",
                    r"The fraction quenched is f = (k_q [Car]) / (k_0 + k_q [Car])."
                ],
                "solution": r"""### Step 1: Triplet Energy Requirement
The physical quenching of singlet oxygen occurs via Dexter electron-exchange energy transfer:
$$^1\text{O}_2(^1\Delta_g) + \beta\text{-Car}(S_0) \xrightarrow{k_q} ^3\text{O}_2(^3\Sigma_g^-) + \beta\text{-Car}^*(T_1)$$
For this energy transfer to be exergonic and proceed at the diffusion-controlled limit ($k_q > 10^{10}\text{ M}^{-1}\text{s}^{-1}$):
$$E(T_1, \beta\text{-Car}) \le E(^1\Delta_g, \text{O}_2) = \mathbf{94.2\text{ kJ/mol}} \quad (0.98\text{ eV})$$
Because $\beta$-carotene possesses 11 conjugated double bonds, its lowest triplet state $T_1$ lies at approximately $88\text{ kJ/mol}$ ($0.91\text{ eV}$), comfortably below the singlet oxygen excitation energy. The resulting excited triplet carotene ($\beta\text{-Car}^*$) returns harmlessly to the ground state via non-radiative vibrational decay:
$$\beta\text{-Car}^*(T_1) \to \beta\text{-Car}(S_0) + \text{heat}$$

### Step 2: Quenching Efficiency in Lipid Membrane
The total pseudo-first-order rate of $^1\text{O}_2$ decay is:
$$k_{\text{total}} = k_0 + k_q [\beta\text{-Car}]$$
Given:
$$k_0 = 4.0\times 10^4\text{ s}^{-1}$$
$$k_q [\beta\text{-Car}] = (1.2\times 10^{10}\text{ M}^{-1}\text{s}^{-1})(0.50\times 10^{-3}\text{ M}) = 6.0\times 10^6\text{ s}^{-1}$$
$$k_{\text{total}} = 4.0\times 10^4 + 6.0\times 10^6 = 6.04\times 10^6\text{ s}^{-1}$$

The fraction of singlet oxygen intercepted by $\beta$-carotene is:
$$f_{\text{quenched}} = \frac{k_q [\beta\text{-Car}]}{k_0 + k_q [\beta\text{-Car}]} = \frac{6.0\times 10^6}{6.04\times 10^6} = 0.9934 \implies \mathbf{99.34\%}$$
Over $99.3\%$ of hazardous singlet oxygen is intercepted before it can oxidize membrane lipids or cellular proteins."""
            }
        ]
    }
    units.append(u3)

    return units

if __name__ == "__main__":
    u = get_units_1_2_3()
    print(f"Successfully generated Units 1-3. Total units: {len(u)}")
    for unit in u:
        print(f"  {unit['id']}: {len(unit['sections'])} sections, {len(unit['problems'])} problems")
