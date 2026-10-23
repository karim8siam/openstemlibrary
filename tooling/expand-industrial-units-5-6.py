#!/usr/bin/env python3
"""
Expand Units 5 and 6 for Industrial and Official Statistics.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"

u5_text = (DRAFT_DIR / "unit-5.md").read_text(encoding="utf-8")
u6_text = (DRAFT_DIR / "unit-6.md").read_text(encoding="utf-8")

u5_addon = r"""## 5.8 Dodge-Romig Sampling Systems: AOQL and LTPD Optimization

In the late 1920s and 1930s, Harold F. Dodge and Harry G. Romig developed the **Dodge-Romig Sampling Systems** at Bell Telephone Laboratories. Unlike military standards which are indexed by AQL, Dodge-Romig plans are specifically engineered for **rectifying inspection** environments where every rejected lot is 100% sorted.

Dodge-Romig tables provide sampling plans categorized into two fundamental classes:
1. **Lot Tolerance Percent Defective (LTPD) Plans**: Designed to provide a guaranteed consumer's risk of $\beta = 0.10$ at a designated limiting quality $p_2 = LTPD$, while mathematically minimizing the Average Total Inspection ($ATI$) at the supplier's process average defect rate $\bar{p}$.
2. **Average Outgoing Quality Limit (AOQL) Plans**: Designed to guarantee that outgoing defectiveness never exceeds a pre-set ceiling ($AOQL$) under rectifying inspection, while mathematically minimizing the Average Total Inspection ($ATI$) at the process average $\bar{p}$.

### Mathematical Optimization Criterion
For a given lot size $N$ and historical process average $\bar{p}$, Dodge and Romig sought the pair $(n, c)$ that minimizes the objective function:

$$\min_{n, c} ATI(\bar{p}) = n + (1 - P_a(\bar{p}; n, c))(N - n)$$

subject to either:
$$P_a(p_2; n, c) = 0.10 \quad (\text{for LTPD plans})$$
or
$$\max_{0 \le p \le 1} AOQ(p; n, c, N) = AOQL \quad (\text{for AOQL plans})$$

By tabulating optimal combinations across standard lot size brackets ($N = 1-50, 51-100, \dots, 50,001-100,000$) and process averages $\bar{p}$, Dodge and Romig created the most cost-efficient rectifying inspection systems in manufacturing history.

## 5.9 Continuous Sampling Plans for Automated Production: CSP-1, CSP-2, and CSP-3

Traditional lot-by-lot acceptance sampling requires segregating parts into identifiable physical containers or batches. In high-speed automated continuous flow lines (e.g., continuous conveyor belt assembly of canned beverages, automotive engine blocks, or consumer electronics), halting the line to form artificial lots is logistically impossible. 

To govern continuous production flows, Harold Dodge (1943) invented **Continuous Sampling Plans (CSP)**:

### The CSP-1 Operational Protocol
CSP-1 operates as an adaptive two-mode finite state machine:
1. **Screening Mode (100% Inspection)**: At production startup, inspect $100\%$ of units consecutively in order of manufacture. Continue screening until a pre-determined **clearing clearance number** $i$ of consecutive units are found to be completely defect-free ($i$ consecutive conforming units).
2. **Sampling Mode**: Once $i$ consecutive defect-free units are observed, discontinue 100% screening. Inspect only a small fraction $f$ of units (e.g., $f = 1/5$ or $f = 1/10$), selecting units at random or systematically along the line.
3. **Reversion Trigger**: As long as sampled units are conforming, sampling continues indefinitely. The instant *a single nonconforming unit* is discovered during sampling, the line immediately reverts to **Screening Mode (100% Inspection)**, and the cycle repeats.

Dodge proved that for any specified fraction $f$ and clearing interval $i$, the outgoing quality is guaranteed never to exceed a mathematical ceiling:

$$AOQL_{\text{CSP-1}} = \frac{k_{\text{CSP}}}{i}$$

Subsequent variants (CSP-2 and CSP-3) introduce delay buffers before reverting to 100% screening, preventing line disruptions from isolated, accidental defects while preserving strict AOQL protection.
"""

u6_addon = r"""## 6.7 Structural Reliability Architecture: Fault Tree Analysis and Importance Measures

In complex mission-critical systems (e.g., nuclear power plant safety injection systems, space exploration launch vehicles, and chemical plant flare headers), reliability cannot be represented as simple series-parallel combinations. Engineers utilize **Fault Tree Analysis (FTA)** and **Reliability Block Diagrams (RBD)** to model catastrophic system failure.

### Fault Tree Methodology and Minimal Cut Sets
A Fault Tree is a top-down deductive graphical failure model connecting an undesired catastrophic **Top Event** (e.g., "Complete Loss of Flight Control") to constituent basic hardware, software, and human failures via Boolean logic gates (AND, OR, Voting gates).

Let $X_i \in \{0, 1\}$ denote the binary state of basic event $i$:
$$X_i = \begin{cases} 1 & \text{if component } i \text{ has failed} \\ 0 & \text{if component } i \text{ is operational} \end{cases}$$

The state of the Top Event is governed by the system structure function $\psi(\mathbf{X}) \in \{0, 1\}$.
A **Cut Set** is a set of basic events whose joint occurrence forces $\psi(\mathbf{X}) = 1$ (causes top event failure). A **Minimal Cut Set (MCS)** is a cut set that ceases to be a cut set if any single basic event is removed. The minimal cut sets represent the smallest combinations of primary failures sufficient to crash the entire system.

By applying Boolean algebra (De Morgan’s laws and absorption laws), any complex fault tree can be reduced to an equivalent sum of minimal cut sets $C_1, C_2, \dots, C_m$:

$$\psi(\mathbf{X}) = \bigvee_{j=1}^m \left( \bigwedge_{i \in C_j} X_i \right)$$

The exact Top Event probability $Q_{\text{sys}} = P(\psi(\mathbf{X}) = 1)$ is evaluated via the Poincaré Inclusion-Exclusion formula or upper-bounded by the union bound:

$$Q_{\text{sys}} \le \sum_{j=1}^m P(C_j) = \sum_{j=1}^m \prod_{i \in C_j} q_i$$

where $q_i = P(X_i = 1)$ is the failure probability of basic event $i$.

### Component Reliability Importance Measures
To determine which individual components contribute most critically to overall system vulnerability, reliability engineers compute quantitative importance indices:

1. **Birnbaum Structural Importance ($I_B(i)$)**:
   The probability that component $i$ is critical to system failure (i.e., the system operates when $i$ works, but crashes the instant $i$ fails):
   $$I_B(i) = \frac{\partial Q_{\text{sys}}}{\partial q_i} = P(\psi(\mathbf{X}) = 1 \mid X_i = 1) - P(\psi(\mathbf{X}) = 1 \mid X_i = 0)$$

2. **Fussell-Vesely Importance ($I_{FV}(i)$)**:
   The fractional contribution of component $i$ to total system unreliability, measuring the probability that component $i$ caused the system failure given that the system has failed:
   $$I_{FV}(i) = \frac{P(\text{At least one MCS containing } i \text{ has failed})}{Q_{\text{sys}}}$$

Components exhibiting high Birnbaum or Fussell-Vesely scores are targeted for redundancy, improved maintenance scheduling, or aerospace-grade component upgrades.

## 6.8 Physics-of-Failure: Coffin-Manson and Multimodal Fatigue Models

Beyond empirical statistical curve fitting, modern reliability engineering integrates material physics and solid mechanics under the **Physics-of-Failure (PoF)** paradigm.

### Thermomechanical Fatigue: The Coffin-Manson Model
In electronic assemblies and aerospace turbine blades, cyclic heating and cooling causes mismatched thermal expansion between adjacent materials (e.g., silicon die, copper leadframe, and solder alloy). This cyclic thermal strain produces low-cycle plastic deformation and fatigue cracking.

L. F. Coffin and S. S. Manson (1953) formulated the relationship between the cyclic plastic strain range $\Delta \varepsilon_p$ and the number of cycles to failure $N_f$:

$$\frac{\Delta \varepsilon_p}{2} = \varepsilon_f' (2 N_f)^c$$

where $\varepsilon_f'$ is the fatigue ductility coefficient and $c \approx -0.5$ to $-0.7$ is the fatigue ductility exponent.

In electronics thermal shock testing, the **Modified Coffin-Manson Acceleration Factor** between operational temperature cycle $\Delta T_{\text{use}}$ and test cycle $\Delta T_{\text{stress}}$ is:

$$AF_{\text{fatigue}} = \left( \frac{\Delta T_{\text{stress}}}{\Delta T_{\text{use}}} \right)^q \left( \frac{f_{\text{use}}}{f_{\text{stress}}} \right)^m \exp\left( \frac{E_a}{k_B} \left( \frac{1}{T_{\text{max, use}}} - \frac{1}{T_{\text{max, stress}}} \right) \right)$$

where:
- $\Delta T = T_{\text{max}} - T_{\text{min}}$: The thermal cycle amplitude.
- $q$: The Coffin-Manson temperature exponent (typically $q \approx 1.9$ to $2.5$ for lead-free SAC305 solder).
- $f$: Cycling frequency, accounting for solder creep stress relaxation.
- $E_a$: Activation energy for thermal creep diffusion ($\sim 0.12\text{ eV}$).

The Coffin-Manson equation enables automotive and aerospace engineers to simulate 15 years of daily ambient automotive thermal cycling ($25^\circ\text{C}$ to $125^\circ\text{C}$) in only 3 weeks of rapid environmental chamber cycling ($-40^\circ\text{C}$ to $+150^\circ\text{C}$).
"""

idx5 = u5_text.find("## Fully worked question 1:")
u5_new = u5_text[:idx5] + u5_addon.strip() + "\n\n" + u5_text[idx5:]
(DRAFT_DIR / "unit-5.md").write_text(u5_new, encoding="utf-8")

idx6 = u6_text.find("## Fully worked question 1:")
u6_new = u6_text[:idx6] + u6_addon.strip() + "\n\n" + u6_text[idx6:]
(DRAFT_DIR / "unit-6.md").write_text(u6_new, encoding="utf-8")

print("Units 5 and 6 expanded.")
