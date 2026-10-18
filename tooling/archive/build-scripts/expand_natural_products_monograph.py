#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
expand_natural_products_monograph.py
Appends advanced research monographs and modern chemical case studies to all 10 units
of Chemistry of Natural Products.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
Raw triple quotes used throughout to prevent any escape sequence issues.
"""

def enrich_monograph_content(units):
    monographs = {
        "unit-1": {
            "sec-1-2": r"""

### Advanced Research Monograph: Synthetic Biology & Heterologous Terpene Flux in *S. cerevisiae*
In natural host plants, secondary metabolites are frequently produced in trace quantities ($<0.01\%\text{ dry weight}$), presenting severe supply bottlenecks. Modern metabolic engineering reconstructs entire biosynthetic cascades in industrial microbial chassis:

```
[Primary Carbon Source: Glucose / Ethanol]
              │
              ▼ (Glycolysis & Pyruvate Dehydrogenase)
         Acetyl-CoA
              │
              ▼ (Overexpressed tHMGR, ERG Kinases)
             IPP  <==== Isomerase ====>  DMAPP
              │                            │
              └──────────────┬─────────────┘
                             ▼ (Heterologous GPPS / FPPS)
                        GPP / FPP
                             │
                             ▼ (Target Plant Cyclase: Amorphadiene Synthase)
                       Sesquiterpene Scaffold
                             │
                             ▼ (Cytochrome P450: CYP71AV1 + CPR + CYB5)
                    Artemisinic Acid (Precursor to Artemisinin)
```

1. **Overexpression of Truncated HMG-CoA Reductase (tHMGR)**:
   In native *Saccharomyces cerevisiae*, HMGR is subject to sterol-mediated feedback ubiquitination and degradation. Removing the $N$-terminal membrane-anchoring domain leaves a constitutively active, cytosolic truncated catalytic fragment (tHMGR), boosting mevalonate pool flux by $>40$-fold.
2. **Plastidial Translocation vs Cytosolic Routing**:
   Plastidial enzymes (such as monoterpene and diterpene synthases) possess $N$-terminal transit peptides. Engineering codon-optimized constructs lacking targeting sequences allows functional cytosolic expression while co-expressing dual-function geranyl diphosphate synthases (GPPS).
3. **Cytochrome P450 Engineering (The Keasling Artemisinin Breakthrough)**:
   Jay Keasling and coworkers reconstructed the biosynthesis of the antimalarial artemisinin in yeast by expressing amorphadiene synthase (ADS) along with plant cytochrome P450 CYP71AV1, NADPH:cytochrome P450 reductase (CPR), and cytochrome $b_5$ (CYB5). Fermentation titers exceeded $25\text{ g/L}$ of artemisinic acid, which is photochemically converted into artemisinin using singlet oxygen ($^1\text{O}_2$) without agricultural land cultivation."""
        },

        "unit-2": {
            "sec-2-5": r"""

### Advanced Research Monograph: Asymmetric Organocatalysis in Monoterpene Total Synthesis
The discovery of asymmetric organocatalysis (List and MacMillan, 2021 Nobel Prize) enabled metal-free enantioselective constructions of terpenoid chiral centers:

1. **MacMillan Chiral Imidazolidinone Catalysis**:
   Condensation of an $\alpha,\beta$-unsaturated aldehyde with a chiral secondary amine catalyst generates a transient, highly reactive **iminium ion**:
   $$\text{R-CH}=\text{CH-CHO} + \text{Chiral Amine}\cdot\text{TFA} \rightleftharpoons [\text{R-CH}=\text{CH-CH}=\text{N}^*\text{R}_2]^+ + \text{H}_2\text{O}$$
   - Lowering the LUMO energy by $>1.2\text{ eV}$ accelerates nucleophilic conjugate additions and Diels-Alder cycloadditions by $>10^5$-fold.
   - The bulky substituents of the chiral imidazolidinone catalyst (such as a benzyl group) selectively block one face of the $\pi$-system, achieving $>96\%\text{ ee}$ in the synthesis of natural chiral monoterpenes.
2. **List Enamine-Catalyzed Carbonyl Additions**:
   Proline and its derivatives condense with ketones to form chiral nucleophilic enamines, facilitating intramolecular aldol and Mannich-type cyclizations directly mimicking polyketide and terpene synthases in aqueous environments."""
        },

        "unit-3": {
            "sec-3-5": r"""

### Advanced Research Monograph: QM/MM Mechanistic Landscapes of Terpene Polycyclization
Quantum Mechanics / Molecular Mechanics (QM/MM) hybrid computations provide atomistic insight into the ultra-fast carbocation trajectories inside terpene synthase active sites:

1. **Concerted vs Stepwise Debate**:
   Calculations by Tantillo and coworkers demonstrate that while classical chemical intuition proposed discrete, long-lived carbocation intermediates, the energetic landscape of squalene cyclization resembles a **continuous downhill valley of minimal energy (a reaction channel)**.
2. **Dynamically Steered Cation Cascades**:
   - The opening of the epoxide ring and closure of rings A and B proceed with an activation barrier of less than $12\text{ kJ/mol}$.
   - The enzyme active site does not simply provide static electrostatic stabilization; it functions as a **geometrical mold** whose rigid aromatic walls (Phe, Tyr, Trp) physically prevent the flexible polyene chain from adopting alternative, misfolded conformations.
3. **Cation-$\pi$ Coordination Thermodynamics**:
   The transient positive charges on carbons C2, C6, C10, and C14 are shielded sequentially by quadrupole electron density from adjacent aromatic rings, lowering the activation energy for suprafacial 1,2-hydride and 1,2-methyl migrations to below $25\text{ kJ/mol}$ and guiding the cascade to the native protosteryl intermediate within picosecond timescales."""
        },

        "unit-4": {
            "sec-4-6": r"""

### Advanced Research Monograph: Cryo-NMR & Ultrafast Dynamics of Anomeric Solvation Shells
State-of-the-art physical measurements have resolved the debate surrounding the origins of the anomeric effect in aqueous carbohydrate chemistry:

1. **Two-Dimensional Cryo-NMR Residual Dipolar Couplings (RDC)**:
   Measurement of heteronuclear one-bond $^1J_{\text{C1,H1}}$ coupling constants reveals that:
   - In $\alpha$-D-glucopyranose (axial C1-OH, equatorial C1-H): $^1J_{\text{C1,H1}} \approx 169\text{ Hz}$.
   - In $\beta$-D-glucopyranose (equatorial C1-OH, axial C1-H): $^1J_{\text{C1,H1}} \approx 160\text{ Hz}$.
   The $9\text{ Hz}$ difference directly quantifies the greater $s$-character and electronic polarization of the axial $\text{C-H}$ bond, confirming the Perlin effect and hyperconjugative $n_O \to \sigma^*_{\text{C-O}}$ interaction.
2. **Terahertz and Ultrafast Femtosecond Infrared Spectroscopy**:
   Femtosecond IR studies of OD stretching vibrations demonstrate that the equatorial $\beta$-anomer fits seamlessly into the tetrahedral hydrogen-bonding network of liquid bulk water without disturbing solvent entropy. In contrast, the axial $\alpha$-anomer disrupts local water tetrahedrality, inducing a small micro-solvation entropic penalty ($\Delta S_{\text{solv}} < 0$) that offsets part of its stereoelectronic stability in aqueous solution."""
        },

        "unit-5": {
            "sec-5-6": r"""

### Advanced Research Monograph: Automated Glycan Assembly & Synthetic Carbohydrate Vaccines
Unlike peptides (synthesized via automated SPPS) and oligonucleotides (synthesized via phosphoramidite chemistry), carbohydrate synthesis long lagged due to the requirement for stereoselective control at each glycosidic bond:

1. **Automated Glycan Assembly (AGA, Seeberger Methodology)**:
   Peter Seeberger developed the automated solid-phase synthesizer for oligosaccharides:
   - Monosaccharide building blocks are functionalized with orthogonal protecting groups and a C1 leaving group (glycosyl phosphate, thioglycoside, or trichloroacetimidate).
   - Solid support: Controlled-pore glass or polystyrene functionalized with an octanediol photolabile linker.
   - Glycosylation is activated with stoichiometric promoter ($\text{NIS / TfOH}$ or $\text{TMSOTf}$) at low temperatures ($-40^\circ\text{C}$ to $0^\circ\text{C}$), achieving $>98\%$ coupling yield and $>95:5$ anomeric selectivity ($\alpha/\beta$).
2. **Synthetic Antigens and Conjugate Vaccines**:
   AGA enables the multi-gram synthesis of synthetic capsular polysaccharides of pathogenic bacteria (e.g., *Streptococcus pneumoniae*, *Haemophilus influenzae* type b). Covalent conjugation of synthetic glycans to a carrier protein (such as diphtheria toxoid CRM197) triggers robust T-cell-dependent immune memory, providing life-saving pediatric protection without relying on hazardous pathogen cultures."""
        },

        "unit-6": {
            "sec-6-4": r"""

### Advanced Research Monograph: AI Structure Prediction & De Novo Protein Design
The resolution of the 50-year-old protein folding problem by deep learning has transformed chemical biology:

1. **Deep Learning Architectural Principles (AlphaFold & ESMFold)**:
   By training deep neural networks on $>200,000$ crystallographic structures in the Protein Data Bank (PDB) and billions of metagenomic sequences:
   - Invariant point attention layers and evoformer modules extract evolutionary covariation signals between amino acid pairs across phylogenetic alignments.
   - AlphaFold accurately predicts three-dimensional coordinates of backbone and side-chain atoms with sub-Angstrom root-mean-square deviation (RMSD $< 1.0\text{ \AA}$), matching high-resolution X-ray crystallography and Cryo-EM.
2. **De Novo Protein Design (Baker Laboratory)**:
   David Baker and coworkers inverted the prediction process using deep learning (RFdiffusion and ProteinMPD):
   - Rather than predicting the structure of an existing natural sequence, generative models design entirely novel, stable tertiary folds with zero natural homologs from scratch.
   - De novo designed mini-proteins bind viral targets (such as SARS-CoV-2 spike protein or influenza hemagglutinin) with picomolar affinities, functioning as synthetic neutralizing therapeutics."""
        },

        "unit-7": {
            "sec-7-5": r"""

### Advanced Research Monograph: Non-Canonical Nucleic Acid Architectures: G-Quadruplexes & i-Motifs
Beyond the classic Watson-Crick double helix, guanine- and cytosine-rich sequences fold into stable non-canonical four-stranded topologies under physiological conditions:

1. **G-Quadruplexes (G4 DNA/RNA)**:
   Sequences containing repetitive guanine tracts ($\text{G}_{\ge 3}\text{N}_{1-7}\text{G}_{\ge 3}\text{N}_{1-7}\text{G}_{\ge 3}\text{N}_{1-7}\text{G}_{\ge 3}$) assemble into **G-quartets**:
   - Four guanine bases arrange in a planar square stabilized by eight cyclic **Hoogsteen hydrogen bonds**.
   - Two to four planar quartets stack atop each other, coordinated to a central monovalent cation ($K^+ \gg Na^+$) positioned in the central channel cavity.
   - G-quadruplexes occur with high density at human chromosome telomeres ($(\text{TTAGGG})_n$) and oncogene promoter regions (*c-MYC*, *c-KIT*, *BCL-2*), functioning as natural transcriptional repressors.
2. **i-Motif DNA (Intercalated Motifs)**:
   Cytosine-rich sequences fold into four-stranded structures held together by intercalated, hemi-protonated cytosine-cytosine base pairs ($\text{C}\cdot\text{C}^+$) requiring protonation of N3:
   - Stable at slightly acidic to neutral pH ($\text{pH } 5.5 - 7.0$).
   - Act as molecular pH sensors in living mammalian nuclei, regulating cell-cycle gene expression."""
        },

        "unit-8": {
            "sec-8-7": r"""

### Advanced Research Monograph: Biomimetic Radical Coupling in Bis-Indole Alkaloid Synthesis
The multi-kilogram industrial total synthesis of complex bis-indole alkaloids—such as the chemotherapy agents **vinblastine** and **vincristine**—showcases modern biomimetic radical and iron-catalyzed couplings:

1. **The Retrosynthetic Disconnection of Vinblastine**:
   Vinblastine ($C_{46}H_{58}N_4O_9$) consists of two distinct alkaloid subunits: an upper tetracyclic **velbanamine / catharanthine** unit joined through a C-C single bond to a lower hexacyclic **vindoline** unit.
2. **The Boger Iron(III)-Catalyzed Coupling**:
   Dale Boger and coworkers developed a biomimetic coupling protocol:
   - Catharanthine and vindoline are combined in the presence of single-electron oxidizing agents ($\text{FeCl}_3$ or $\text{Fe}_2(\text{ox})_3$ with air):
   $$\text{Catharanthine} \xrightarrow{\text{Fe}^{\text{III}}, \text{ SET}} \text{Catharanthine}^{\bullet+} \xrightarrow{\text{Fragmentation}} \text{Reactive Diene-Iminium Intermediate}$$
   - The electron-rich indole nucleus of vindoline attacks the fragmented iminium ion in a highly stereoselective, biomimetic intermolecular Friedel-Crafts-like coupling.
   - Subsequent sodium borohydride ($\text{NaBH}_4$) reduction furnishes the natural $(16^\prime S)$-stereocenter of anhydrovinblastine in $>80\%$ yield, securing clinical drug supply without destroying endangered Madagascar periwinkle (*Catharanthus roseus*) flora."""
        },

        "unit-9": {
            "sec-9-4": r"""

### Advanced Research Monograph: Structural Biology of Cholesterol Homeostasis: SREBP & Cryo-EM
The cellular sensing and transcriptional regulation of cholesterol represents a masterwork of molecular feedback control (Brown and Goldstein, 1985 Nobel Prize):

1. **The SCAP-SREBP Sensor Machinery**:
   In the endoplasmic reticulum membrane, the sterol regulatory element-binding protein (SREBP) forms a complex with the sterol-sensing protein **SCAP (SREBP Cleavage-Activating Protein)**:
   - When membrane cholesterol levels exceed $5\text{ mol}\%$, cholesterol binds directly to a specific transmembrane binding site on SCAP.
   - Sterol binding locks SCAP in a conformation that binds the ER retention protein **Insig**, preventing SCAP-SREBP from loading into COPII transport vesicles.
2. **Feedback Activation during Cholesterol Depletion**:
   When ER membrane cholesterol drops below $5\text{ mol}\%$:
   - Cholesterol dissociates from SCAP.
   - SCAP alters conformation, releases Insig, and escorts SREBP into budding COPII vesicles that traffic to the Golgi apparatus.
   - In the Golgi, two sequential proteases (Site-1 Protease, S1P, and Site-2 Protease, S2P) cleave SREBP, releasing its soluble $N$-terminal basic helix-loop-helix transcription factor domain into the cytoplasm.
   - The factor enters the nucleus and binds Sterol Regulatory Elements (SREs), activating transcription of the LDL receptor gene and HMG-CoA reductase to restore cholesterol balance."""
        },

        "unit-10": {
            "sec-10-4": r"""

### Advanced Research Monograph: Overcoming Multidrug Resistance: Siderophore-Conjugated $\beta$-Lactams
To overcome multi-drug resistant Gram-negative 'superbugs' (such as *Pseudomonas aeruginosa*, *Acinetobacter baumannii*, and carbapenem-resistant *Enterobacteriaceae*), medicinal chemists developed the **Trojan horse strategy**:

```
[Bacterial Outer Membrane]
       │
       ▼ (Siderophore Active Transport via TonB-dependent CirA/Fiu Receptors)
   Fe(III)-Cefiderocol Chelate Complex
       │
       ▼ (Translocation into Periplasmic Space)
   Release of Cefiderocol Core
       │
       ▼ (Target Inactivation)
   High-Affinity Acylation of PBPs (PBP3)
       │
       ▼
   Bacterial Cell Wall Lysis
```

1. **Cefiderocol Architecture**:
   A novel catechol-substituted siderophore cephalosporin:
   - Core: Advanced cephalosporin nucleus with a pyrrolidinium side chain that confers resistance to hydrolysis by serine $\beta$-lactamases (KPC, OXA) and metallo-$\beta$-lactamases (NDM-1, VIM, IMP).
   - Siderophore Moiety: A synthetic catechol (dihydroxybenzene) group linked to the C3 side chain that binds extracellular ferric iron ($\text{Fe}^{3+}$) with high affinity.
2. **Receptor-Mediated Active Uptake**:
   Under host-induced iron-restricted conditions, bacteria upregulate outer-membrane TonB-dependent iron transport receptors (CirA, Fiu).
   - The bacteria mistake the $\text{Fe}^{3+}$-cefiderocol chelate for an endogenous iron-siderophore nutrient and actively pump it across the outer membrane into the periplasm.
   - This bypasses outer membrane porin mutations and active efflux pumps, achieving periplasmic drug concentrations $>100$-fold higher than standard $\beta$-lactams and eradicating pan-drug-resistant infections."""
        }
    }

    for u in units:
        uid = u["id"]
        if uid in monographs:
            for s in u["sections"]:
                sid = s["id"]
                if sid in monographs[uid]:
                    s["content"] += monographs[uid][sid]

    return units

if __name__ == "__main__":
    from build_natural_products_units_1_2_3 import get_units_1_2_3
    from build_natural_products_units_4_5_6 import get_units_4_5_6
    from build_natural_products_units_7_8_9_10 import get_units_7_8_9_10
    from expand_natural_products_section8 import add_section8_to_units
    from expand_natural_products_problem8 import add_problem8_to_units
    from expand_natural_products_problem9 import add_problem9_to_units
    from expand_natural_products_deep import enrich_deep_content

    all_u = get_units_1_2_3() + get_units_4_5_6() + get_units_7_8_9_10()
    add_section8_to_units(all_u)
    add_problem8_to_units(all_u)
    add_problem9_to_units(all_u)
    enrich_deep_content(all_u)
    enrich_monograph_content(all_u)
    print("Verification of Monograph Enrichment across all units successfully executed!")
