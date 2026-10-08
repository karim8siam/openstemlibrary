# -*- coding: utf-8 -*-
"""
expand_analytical_honors_capstone.py
Injects advanced university honors analytical capstone case studies
into Analytical Chemistry (#46), providing real-world metrological depth.
Strict zero course numbers or marks. All math in raw strings r\"\"\"...\"\"\".
"""

def add_capstones_to_curriculum(curriculum):
    print("Injecting advanced Honors Capstone Case Studies into curriculum...")

    capstones = [
        {
            "id": "capstone-1-pharma-metrology",
            "title": "Honors Capstone 1: Metrological Traceability & ISO/GUM Combined Uncertainty Budget for Pharmaceutical API Release",
            "summary": "Full metrological derivation of measurement uncertainty for high-performance HPLC assay of a life-saving antibiotic active pharmaceutical ingredient (API) according to the Guide to the Expression of Uncertainty in Measurement (ISO GUM). Evaluates Type A repeatability, Type B balance calibration, volumetric flask thermal expansion, reference standard certified purity, and detector linearity to establish regulatory expanded uncertainty (k=2).",
            "content": r"""### Metrological Measurement Model
The mass fraction $w_{\text{API}}$ (in $\text{mg}\cdot\text{g}^{-1}$) of active pharmaceutical ingredient in a commercial formulation is determined by reversed-phase HPLC:

$$w_{\text{API}} = \frac{A_{\text{sample}} \times m_{\text{std}} \times V_{\text{sample}} \times P_{\text{std}}}{A_{\text{std}} \times m_{\text{sample}} \times V_{\text{std}}} \tag{C1.1}$$

where:
- $A_{\text{sample}}, A_{\text{std}}$: Chromatographic peak areas of sample and certified reference standard.
- $m_{\text{sample}}, m_{\text{std}}$: Masses weighed on analytical balance ($m_{\text{sample}} = 100.25\text{ mg}, m_{\text{std}} = 100.10\text{ mg}$).
- $V_{\text{sample}}, V_{\text{std}}$: Volumetric flask volumes ($100.00\text{ mL}$).
- $P_{\text{std}}$: Certified purity of reference standard ($99.80\% \pm 0.20\%$).

### Quantifying Type A and Type B Uncertainty Components
1. **Type A Uncertainty (Repeatability $u_{\text{rep}}$)**:
   Six replicate injections gave a peak area relative standard deviation of $RSD = 0.35\%$:
   $$u_r(A) = \frac{0.0035}{\sqrt{6}} = 0.00143 \implies 0.143\%$$
2. **Type B Uncertainty: Mass Weighings ($u(m)$)**:
   The analytical balance calibration certificate reports an uncertainty of $\pm 0.05\text{ mg}$ ($k=2$, normal distribution):
   $$u(m) = \frac{0.05\text{ mg}}{2} = 0.025\text{ mg} \implies u_r(m) = \frac{0.025}{100.1} = 0.0250\%$$
   Since sample and standard are weighed on the same balance, buoyancy and linearity errors are combined: $u_r(m_{\text{net}}) = \sqrt{2 \times (0.025\%)^2} = 0.035\%$.
3. **Type B Uncertainty: Volumetric Flasks ($u(V)$)**:
   - Manufacturer tolerance: $100.00 \pm 0.10\text{ mL}$ (triangular distribution):
     $$u_{\text{cal}}(V) = \frac{0.10\text{ mL}}{\sqrt{6}} = 0.0408\text{ mL}$$
   - Temperature variation ($\Delta T = \pm 4^\circ\text{C}$, rectangular distribution, water expansion coefficient $\gamma = 2.1 \times 10^{-4}\text{ K}^{-1}$):
     $$u_{\text{temp}}(V) = \frac{100.0\text{ mL} \times (4\text{ K}) \times (2.1 \times 10^{-4}\text{ K}^{-1})}{\sqrt{3}} = 0.0485\text{ mL}$$
   - Combined relative volume uncertainty:
     $$u_r(V) = \frac{\sqrt{(0.0408)^2 + (0.0485)^2}}{100.0} = 0.0634\%$$
4. **Type B Uncertainty: Standard Purity ($u(P_{\text{std}})$)**:
   Certified purity $99.80 \pm 0.20\%$ ($k=2$):
   $$u_r(P_{\text{std}}) = \frac{0.10\%}{99.80\%} = 0.100\%$$

### Combined Standard Uncertainty and Expanded Uncertainty
Combining all independent relative uncertainty components in quadrature:
$$u_c,r(w_{\text{API}}) = \sqrt{ [u_r(A)]^2 + [u_r(m_{\text{net}})]^2 + 2[u_r(V)]^2 + [u_r(P_{\text{std}})]^2 }$$
$$u_c,r(w_{\text{API}}) = \sqrt{ (0.143\%)^2 + (0.035\%)^2 + 2(0.0634\%)^2 + (0.100\%)^2 }$$
$$u_c,r(w_{\text{API}}) = \sqrt{ 0.02045 + 0.00123 + 0.00804 + 0.01000 } = \sqrt{0.03972} = 0.1993\% \approx 0.20\%$$

For reported nominal purity of $w_{\text{API}} = 99.45\%$:
- Combined standard uncertainty: $u_c = 99.45 \times 0.001993 = 0.198\%$
- **Expanded Uncertainty ($U$ at $95\%$ confidence level, $k=2$)**:
  $$U = 2 \times u_c = 2 \times 0.198\% = 0.40\%$$
The final analytical report states:
$$w_{\text{API}} = (99.45 \pm 0.40)\% \quad (k = 2, 95\% \text{ confidence level})$$"""
        },
        {
            "id": "capstone-2-trace-arsenic-speciation",
            "title": "Honors Capstone 2: Forensic Environmental Speciation: Hydride Generation AAS vs HPLC-ICP-MS for Arsenic Toxins",
            "summary": "Deep forensic investigation into toxic inorganic arsenic (As(III), As(V)) versus benign organic seafood arsenic (arsenobetaine, arsenocholine) in contaminated groundwater and municipal distribution networks. Details anion-exchange HPLC coupled with Inductively Coupled Plasma Mass Spectrometry (HPLC-ICP-MS) alongside modified Gutzeit and Ag-DDTC protocols.",
            "content": r"""### Toxicological Arsenic Speciation Formalism
Total elemental arsenic concentration is inadequate for toxicological risk assessment because arsenic toxicity spans more than four orders of magnitude depending strictly on chemical speciation:
- **Trivalent inorganic arsenite ($\text{AsO}_3^{3-}$, $\text{As(III)}$)**: Acute cellular toxin ($LD_{50} \sim 15\text{ mg}\cdot\text{kg}^{-1}$); binds to protein sulfhydryl ($-SH$) groups, disrupting pyruvate dehydrogenase.
- **Pentavalent inorganic arsenate ($\text{AsO}_4^{3-}$, $\text{As(V)}$)**: Toxic ($LD_{50} \sim 100\text{ mg}\cdot\text{kg}^{-1}$); decouples oxidative phosphorylation by uncoupling ATP synthesis as an unreactive phosphate analogue.
- **Methylated metabolites (MMA, DMA)**: Monomethylarsonic acid and dimethylarsinic acid (moderate chronic carcinogens).
- **Organoarsenic species (Arsenobetaine AsB, Arsenocholine AsC)**: Nontoxic, chemically inert dietary species excreted unchanged in urine ($LD_{50} > 10,000\text{ mg}\cdot\text{kg}^{-1}$).

```
              Chromatographic Speciation of Arsenic via HPLC-ICP-MS
      Anion-Exchange Column (Hamilton PRP-X100) -> Nebulizer -> 8000 K Ar Plasma -> MS
      Conductivity / Mass Spectrum Peak Trace:
      Signal (counts/s at m/z 75: ⁷⁵As⁺)
          ^
          |      Peak 1: AsB (Cationic/Neutral, t_R = 1.8 min)
          |     / \
          |    /   \     Peak 2: As(III) (Neutral at pH 6, t_R = 3.2 min)
          |   /     \   / \
          |  /       \ /   \     Peak 3: DMA (Monovalent, t_R = 5.4 min)
          | /         •     \   / \
          |/                 \ /   \     Peak 4: MMA (Divalent, t_R = 8.1 min)
          |                   •     \   / \
          |                          \ /   \     Peak 5: As(V) (Strongest retained, t_R = 12.5 min)
          +---------------------------•-----+---/ \---------------------------> Time (min)
```

### Anion-Exchange HPLC Speciation Protocol
1. **Stationary Phase**: Hamilton PRP-X100 ($10\,\mu\text{m}$ poly(styrene-divinylbenzene) trimethylammonium anion-exchange beads).
2. **Mobile Phase**: $10.0\text{ mM}$ ammonium dihydrogen phosphate ($(\text{NH}_4)\text{H}_2\text{PO}_4$) adjusted to $\text{pH } 6.0$ with dilute ammonia:
   - At $\text{pH } 6.0$:
     - Arsenious acid ($\text{H}_3\text{AsO}_3$, $pK_{a1} = 9.2$) is completely uncharged ($0\%$ ionized) and elutes near the column void volume ($t_R = 3.2\text{ min}$).
     - Dimethylarsinic acid ($\text{DMA}$, $pK_a = 6.2$) is $40\%$ monovalent anion, eluting at $t_R = 5.4\text{ min}$.
     - Monomethylarsonic acid ($\text{MMA}$, $pK_{a1} = 4.1, pK_{a2} = 8.7$) is predominantly monovalent ($z = -1$), eluting at $t_R = 8.1\text{ min}$.
     - Arsenic acid ($\text{H}_3\text{AsO}_4$, $pK_{a1} = 2.2, pK_{a2} = 6.97$) carries an effective charge of $z \approx -1.1$, binding strongly to the quaternary ammonium sites and eluting at $t_R = 12.5\text{ min}$.
3. **ICP-MS Detection at $m/z = 75$ ($^{75}\text{As}^+$)**:
   - Uses an octopole collision/reaction cell pressurized with helium or hydrogen gas to eliminate the polyatomic spectral interference from argon chloride ($^{40}\text{Ar}^{35}\text{Cl}^+$ at $m/z = 75$).
   - Kinetic energy discrimination (KED) slashes background from $100,000\text{ cps}$ to $< 10\text{ cps}$, achieving sub-part-per-trillion ($< 5\text{ ng}\cdot\text{L}^{-1}$) detection limits for each individual arsenic species."""
        }
    ]

    curriculum["honorsCapstones"] = capstones
    print(f"Injected {len(capstones)} Honors Capstones successfully.")
