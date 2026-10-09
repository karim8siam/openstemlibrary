# -*- coding: utf-8 -*-
"""
expand_kinetics_monograph.py
Injects University Honors Research Monographs & Advanced Chemical Dynamics Case Studies
into the sections of all 10 units of Molecular Motion and Reaction Kinetics.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def inject_monographs(units):
    monographs = {
        "unit-1": {
            "sec-1-3": r"""

### University Honors Research Monograph: The Stern-Gerlach Experiment & Spatial Velocity Selection
In 1922, Otto Stern and Walther Gerlach utilized thermal effusion of silver atoms from an electrically heated oven into a high-vacuum chamber to test spatial quantization:
- **Effusion Collimation**: Silver atoms effused through a narrow pinhole ($d \approx 0.1\text{ mm}$) at $T = 1300\text{ K}$, passing through two micro-machined slits to form a ribbon-like molecular beam with transverse angular divergence $< 0.1^\circ$.
- **Inhomogeneous Magnetic Field**: The effusing beam traversed a $3.5\text{ cm}$ magnetic gap between a knife-edge pole piece and a grooved opposing pole, creating an intense transverse field gradient:
  $$\frac{\partial B_z}{\partial z} \approx 10^3\text{ T/m}$$
- **Deflection Force**: The net magnetic force acting on an effusing silver atom of magnetic moment $\vec{\mu}$ was:
  $$F_z = \mu_z \frac{\partial B_z}{\partial z}$$
- **Velocity Dispersion Elimination**: Because classical Maxwell-Boltzmann effusion produces a broad velocity distribution ($f(v) \propto v^3 \exp(-M v^2 / 2 R T)$), classical mechanics predicted a continuous smeared distribution on the glass plate detector. Instead, Stern and Gerlach observed the beam splitting cleanly into two discrete, symmetrically displaced parabolic deposits ($z = \pm 0.1\text{ mm}$), providing the first direct experimental proof of electron spin quantization ($m_s = \pm 1/2$) and spatial orientation quantization in atomic physics."""
        },

        "unit-2": {
            "sec-2-5": r"""

### University Honors Research Monograph: Solid-State Lithium Fast-Ion Conduction in LLZO Garnet Electrolytes
Next-generation all-solid-state lithium batteries replace flammable organic liquid electrolytes with superionic ceramics such as cubic garnet-type $\text{Li}_7\text{La}_3\text{Zr}_2\text{O}_{12}$ (c-LLZO):
- **Crystal Architecture**: Cubic LLZO features a rigid metal-oxygen framework consisting of dodecahedral $\text{LaO}_8$ and octahedral $\text{ZrO}_6$ polyhedra. Lithium ions occupy partially filled tetrahedral ($24d$) and octahedral ($96h$) interstitial sites forming a contiguous 3D percolating network.
- **Doping and High-Entropy Stabilization**: Trivalent or pentavalent cation substitution (e.g., $\text{Al}^{3+}$ or $\text{Ta}^{5+}$ on $Zr$ sites) stabilizes the highly conductive cubic phase over the ordered, poorly conducting tetragonal polymorph at room temperature, creating optimal lithium vacancy concentrations ($[V_{\text{Li}}']$).
- **Hopping Dynamics & High Bulk Conductivity**: The collective concerted hopping of lithium ions across adjacent $24d - 96h - 24d$ cages achieves exceptional bulk ionic conductivity:
  $$\kappa_{\text{bulk}} > 1.0 \times 10^{-3}\text{ S/cm at } 298.15\text{ K}$$
  with activation energy $E_a \approx 0.28 - 0.32\text{ eV}$.
- **Interfacial Chemo-Mechanics**: Unlike liquid electrolytes that conformally wet electrodes, solid-solid interfaces suffer from contact constriction resistances and chemo-mechanical stress fracture during electrochemical stripping and plating, requiring ultra-thin atomic layer deposition (ALD) interlayers."""
        },

        "unit-3": {
            "sec-3-5": r"""

### University Honors Research Monograph: Anomalous Subdiffusion & Macromolecular Crowding in Cell Biology
Inside living biological cells, the aqueous cytoplasm is not a dilute Newtonian solvent, but a densely crowded viscoelastic gel packed with proteins, RNA, cytoskeletal filaments, and organelles occupying $20 - 40\%$ of total cell volume ($200 - 400\text{ g/L}$ macromolecular density):
- **Breakdown of Fickian Scaling**: Instead of the classical linear Einstein Brownian mean-squared displacement $\langle r^2(t) \rangle = 6 D t$, fluorescent correlation spectroscopy and single-particle tracking (SPT) reveal power-law subdiffusive scaling:
  $$\langle r^2(t) \rangle = 6 \Gamma_\alpha t^\alpha \quad \text{with } 0 < \alpha < 1$$
  where $\alpha \approx 0.70 - 0.85$ in mammalian cytoplasm, and $\Gamma_\alpha$ is the anomalous transport coefficient ($\text{m}^2/\text{s}^\alpha$).
- **Physical Mechanisms of Subdiffusion**:
  1. **Steric Obstruction & Fractal Percolation**: Dense networks of actin microfilaments and microtubules impose geometric tortuosity, trapping molecules in transient dead-ends.
  2. **Continuous-Time Random Walks (CTRW)**: Non-specific transient binding interactions between diffusing enzymes and cytoplasmic macromolecules generate heavy-tailed power-law waiting time distributions ($\psi(t) \propto t^{-(1+\alpha)}$).
  3. **Viscoelastic Hydrodynamics (Fractional Brownian Motion)**: Cytoplasmic polymer relaxation times span multiple orders of magnitude, generating long-range temporal memory in drag forces.
- **Consequences for In Vivo Reaction Kinetics**: Subdiffusion dramatically slows down large macromolecular search times while accelerating local geminate radical and enzyme-substrate re-encounters."""
        },

        "unit-4": {
            "sec-4-5": r"""

### University Honors Research Monograph: Microfluidic Flow Kinetics & Automated Machine-Learning Profiling
Continuous-flow microchemical reactors have transformed empirical reaction kinetics from laborious manual batch aliquot sampling into continuous, autonomous real-time multidimensional mapping:
- **Peclet and Reynolds Number Hydrodynamics**: In microchannels of hydraulic diameter $D_h \approx 200 - 500\;\mu\text{m}$, fluid flow is strictly laminar:
  $$\text{Re} = \frac{\rho u D_h}{\eta} < 100$$
  Turbulent back-mixing is eliminated, while molecular diffusion distances are miniature ($< 100\;\mu\text{m}$), ensuring complete radial mixing in milliseconds.
- **Plug-Flow Reaction Profiling**: Under plug-flow conditions, axial distance $z$ downstream from the mixing junction translates linearly to reaction residence time:
  $$\tau_{\text{res}} = \frac{z}{u} = \frac{V_{\text{channel}}}{Q_{\text{total}}}$$
  Varying total volumetric pumping rate $Q_{\text{total}}$ rapidly sweeps reaction times from $10\text{ ms}$ to $10\text{ minutes}$.
- **Closed-Loop Bayesian Optimization**: Coupling microfluidic flow reactors to in-line high-pressure NMR, HPLC-MS, and ATR-FTIR flow cells enables machine learning algorithms (Bayesian optimization with Gaussian process regression) to automatically map multi-variable kinetic response surfaces ($T$, $P$, catalyst loading, residence time), resolving full multi-step reaction mechanisms and rate constants in under 48 hours."""
        },

        "unit-5": {
            "sec-5-5": r"""

### University Honors Research Monograph: Marcus Electron Transfer Theory & The Inverted Region
Rudolph A. Marcus (Nobel Prize in Chemistry 1992) revolutionized chemical kinetics by developing the microscopic theory of outer-sphere electron transfer ($D + A \longrightarrow D^+ + A^-$):
- **Parabolic Potential Energy Surfaces**: The reactant ($D\cdots A$) and product ($D^+\cdots A^-$) states are modeled as multi-dimensional harmonic oscillator potential wells along a collective solvent polarization and nuclear reorganization coordinate $q$.
- **Free Energy Barrier Formulation**: The Gibbs activation free energy is related to the standard driving force $\Delta G^\circ$ and total reorganization energy $\lambda$:
  $$\Delta G^\ddagger = \frac{(\lambda + \Delta G^\circ)^2}{4 \lambda}$$
  where $\lambda = \lambda_{\text{in}} + \lambda_{\text{out}}$ accounts for internal bond length distortions ($\lambda_{\text{in}}$) and dielectric solvent dipole reorientations ($\lambda_{\text{out}}$).
- **The Three Kinetic Regimes**:
  1. **Normal Regime ($-\Delta G^\circ < \lambda$)**: Increasing thermodynamic driving force ($-\Delta G^\circ$) lowers $\Delta G^\ddagger$, accelerating electron transfer ($\ln k \propto -\Delta G^\circ$).
  2. **Barrierless Regime ($-\Delta G^\circ = \lambda$)**: $\Delta G^\ddagger = 0$, achieving the maximum possible activationless transfer rate.
  3. **The Marcus Inverted Region ($-\Delta G^\circ > \lambda$)**: Counter-intuitively, making the reaction even more thermodynamically favorable causes $\Delta G^\ddagger$ to **increase**, slowing down the rate!
- **Experimental Proof**: Gerhard Closs and John Miller (1984) confirmed the inverted region using rigid steroid spacer molecules, a discovery fundamental to photosynthesis and solar cell design."""
        },

        "unit-6": {
            "sec-6-5": r"""

### University Honors Research Monograph: Proton-Coupled Electron Transfer (PCET) & Vibronic Coupling
Proton-Coupled Electron Transfer (PCET) governs fundamental energy conversion processes in nature, including the water-splitting catalytic cycle of Photosystem II and biological respiration in Cytochrome c Oxidase:
- **Mechanistic Classification**:
  1. **Consecutive Pathways (ETPT / PTET)**: Electron transfer precedes proton transfer ($ETPT$), generating high-energy charged intermediates, or proton transfer precedes electron transfer ($PTET$).
  2. **Concerted PCET (CPET)**: The electron and proton transfer concurrently in a single elementary quantum step without passing through stable high-energy intermediates.
- **Quantum Mechanical Vibronic Transitions**: Because the electron is light ($m_e$) and the proton is heavy ($m_p$), but both are quantum particles, CPET is modeled as a non-adiabatic transition between mixed electron-proton vibronic states:
  $$k_{\text{CPET}} = \frac{2 \pi}{\hbar} \sum_\mu P_\mu \sum_\nu |V_{\mu\nu}|^2 \frac{1}{\sqrt{4 \pi \lambda k_B T}} \exp\left( -\frac{(\Delta G_{\mu\nu}^\circ + \lambda)^2}{4 \lambda k_B T} \right)$$
- **Proton Wavepacket Overlap Integral**: The electronic coupling matrix element is modulated by the Franck-Condon overlap of reactant and product proton vibrational wavefunctions:
  $$V_{\mu\nu} = V_{\text{el}} \langle \phi_\mu^{(p)} | \phi_\nu^{(p)} \rangle$$
  Because proton vibrational wavefunctions decay exponentially with donor-acceptor distance $R_{DA}$, CPET rates and kinetic isotope effects ($\text{KIE} = k_H / k_D \approx 10 - 50$) depend acutely on active-site proton donor-acceptor distance gating."""
        },

        "unit-7": {
            "sec-7-5": r"""

### University Honors Research Monograph: Roaming Radical Dynamics in Unimolecular Photodissociation
For nearly a century, unimolecular chemical reactions were assumed to proceed either through the conventional minimum-energy transition state saddle point or by direct homolytic bond dissociation into asymptotic radical fragments. In 2004, Suits, Bowman, and co-workers discovered an unprecedented reaction pathway known as **Roaming**:
- **Discovery in Formaldehyde ($H_2CO \overset{h\nu}{\longrightarrow} H_2 + CO$)**:
  At excitation energies just above the radical threshold ($H_2CO \longrightarrow H^\bullet + HCO^\bullet$):
  1. An excited $C-H$ bond stretches almost to complete homolytic dissociation ($R_{CH} \approx 4 - 6\text{ Å}$).
  2. The leaving hydrogen atom lacks sufficient kinetic energy to overcome long-range electrostatic polarization and escape into the vacuum continuum.
  3. Instead of dissociating or returning to the saddle point, the tethered $H^\bullet$ atom "roams" around the remaining $HCO^\bullet$ radical fragment at large intermolecular distances.
  4. The roaming hydrogen abstracts the other hydrogen atom ($H + HCO \longrightarrow H_2 + CO$), forming molecular products without ever traversing the conventional concerted transition state!
- **Dynamic Signatures**: Conventional transition-state passage produces highly rotationally excited $CO$ with low vibrational excitation. Roaming produces rotationally cold $CO$ ($J \approx 1 - 10$) and vibrationally hot $H_2$ ($v = 6 - 8$), establishing a completely new paradigm in unimolecular chemical dynamics."""
        },

        "unit-8": {
            "sec-8-5": r"""

### University Honors Research Monograph: Cool Flame Oscillations & Low-Temperature Hydrocarbon Autoignition
In advanced Homogeneous Charge Compression Ignition (HCCI) engines, hydrocarbon combustion exhibits two-stage autoignition accompanied by faint blue chemiluminescent **cool flames** ($T = 550 - 750\text{ K}$):
- **Radical Addition to Dioxygen**:
  Alkyl radicals formed by initial $H$-atom abstraction react reversibly with molecular oxygen:
  $$R^\bullet + O_2 \rightleftharpoons RO_2^\bullet$$
- **Intramolecular Radical Isomerization**:
  The alkylperoxy radical ($RO_2^\bullet$) undergoes intramolecular hydrogen abstraction via a cyclic six-membered transition state to form a hydroperoxyalkyl radical ($^\bullet QOOH$):
  $$RO_2^\bullet \rightleftharpoons ^\bullet QOOH$$
- **Chain Branching via Second $O_2$ Addition**:
  At intermediate temperatures, $^\bullet QOOH$ adds a second oxygen molecule:
  $$^\bullet QOOH + O_2 \rightleftharpoons ^\bullet OOQOOH \longrightarrow \text{Ketohydroperoxide} + OH^\bullet$$
  The fragile $O-O$ peroxide bond of the ketohydroperoxide decomposes into two additional radicals ($OH^\bullet + \text{alkoxy radical}$), yielding net degenerate chain branching that drives first-stage autoignition.
- **Negative Temperature Coefficient (NTC) Regime**:
  As temperature rises above $750\text{ K}$, the equilibrium $R^\bullet + O_2 \rightleftharpoons RO_2^\bullet$ shifts back toward reactants, while $RO_2^\bullet$ decomposes to non-branching conjugate alkene $+ HO_2^\bullet$. Overall oxidation rate paradoxically **decreases** with increasing temperature, creating the NTC phenomenon."""
        },

        "unit-9": {
            "sec-9-5": r"""

### University Honors Research Monograph: Chemical Turing Patterns & Spiral Waves in Reaction-Diffusion Media
Alan Turing (1952) proved mathematically that a system of reacting and diffusing chemicals can spontaneously break spatial symmetry, generating stable stationary periodic concentration patterns (spots, stripes) from a completely uniform initial state:
- **Turing Instability Conditions**:
  Consider two chemical species: an autocatalytic **activator** ($u$) and an **inhibitor** ($v$):
  $$\frac{\partial u}{\partial t} = f(u, v) + D_u \nabla^2 u$$
  $$\frac{\partial v}{\partial t} = g(u, v) + D_v \nabla^2 v$$
  For Turing instability to emerge:
  1. The uniform steady state must be stable in the absence of spatial diffusion.
  2. The inhibitor must diffuse substantially faster than the activator:
     $$d = \frac{D_v}{D_u} \gg 1 \quad (\text{typically } d > 5 - 20)$$
  This "local activation, long-range inhibition" principle concentrates activator into local peaks while rapid inhibitor diffusion prevents neighboring regions from igniting.
- **Experimental Observation in the CIMA Reaction**:
  Turing patterns were first confirmed experimentally by De Kepper and co-workers (1990) in the Chlorite-Iodide-Malonic Acid (CIMA) reaction using a polyacrylamide hydrogel containing immobilized starch indicator. Reversible complexation of triiodide with immobilized starch reduced effective activator diffusion ($D_{I_3^-} \ll D_{\text{chlorite}}$), satisfying Turing's diffusion disparity criterion."""
        },

        "unit-10": {
            "sec-10-5": r"""

### University Honors Research Monograph: Quantum Resonances & Feshbach Bound States in the F + H2 Reaction
The benchmark elementary bimolecular reaction $F(^2P) + H_2 \longrightarrow HF(v', j') + H$ is the gold standard of modern quantum reaction dynamics:
- **Reactive Scattering Resonances**:
  In crossed molecular beam experiments with Velocity Map Imaging, Yuan T. Lee, K. Liu, and X. Yang detected sharp step-function peaks in the backward-scattered differential cross-section for producing $HF(v'=3)$ at precise collision energies ($E_{\text{coll}} \approx 0.040 - 0.052\text{ eV}$).
- **The Feshbach Transition State Bound State**:
  Full quantum 3D wavepacket calculations on highly accurate ab initio potential energy surfaces (such as the FXZ and CBS surfaces) revealed that these resonance spikes arise from **quasi-bound quantum states** trapped inside a dynamic potential well located in the transition state region:
  $$F\cdots H-H \rightleftharpoons [F\cdots H\cdots H]^\ddagger \longrightarrow HF(v'=3) + H$$
  Because the entrance channel is vibrationally adiabatic, the colliding system is temporarily trapped in a metastable quantum state for several vibrational periods ($\sim 30 - 50\text{ fs}$) before tunneling out into the exit channel, proving that chemical reactions exhibit discrete quantum bound states at the transition state barrier."""
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
    from build_kinetics_units_1_2_3 import get_units_1_2_3
    from build_kinetics_units_4_5_6 import get_units_4_5_6
    from build_kinetics_units_7_8_9_10 import get_units_7_8_9_10
    from expand_kinetics_section8 import inject_section_8
    from expand_kinetics_problem8 import inject_problem_8
    from expand_kinetics_problem9 import inject_problem_9
    from expand_kinetics_deep import enrich_deep_content

    all_u = get_units_1_2_3() + get_units_4_5_6() + get_units_7_8_9_10()
    all_u = inject_section_8(all_u)
    all_u = inject_problem_8(all_u)
    all_u = inject_problem_9(all_u)
    all_u = enrich_deep_content(all_u)
    all_u = inject_monographs(all_u)
    print("Injected research monographs across all units successfully!")
