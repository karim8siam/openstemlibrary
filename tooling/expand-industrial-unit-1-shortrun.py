#!/usr/bin/env python3
"""
Add Short-Run SPC to Unit 1 to cross 25,000 words.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"

u1_path = DRAFT_DIR / "unit-1.md"
u1_text = u1_path.read_text(encoding="utf-8")

u1_add = r"""
## 1.11 Short-Run Statistical Process Control and Deviation from Nominal Charts

Traditional Shewhart control charts were formulated for high-volume mass production lines manufacturing thousands of identical parts across months of continuous operation. In modern flexible manufacturing systems, aerospace machine shops, and job-shop environments, production runs are short—often consisting of only 20 to 50 parts before the machine is retooled for a completely different part geometry or customer contract. In such low-volume, high-mix environments, waiting for 25 subgroups of identical parts to establish Phase I control limits is impossible.

To monitor short production runs across diverse part families on a single machine tool, quality statisticians utilize **Short-Run SPC** methodologies:

### 1. Deviation from Nominal (DNOM) Charts
When a single CNC machining center mills different parts that have different nominal design targets $T_i$ but share similar process variability $\sigma$, the raw measurement $X$ is replaced with the **Deviation from Nominal**:

$$Y_{ij} = X_{ij} - T_i$$

Because the nominal target is subtracted, the transformed variable $Y$ has an expected value of zero ($\mathbb{E}[Y] = 0$) regardless of which specific part is currently being machined. Subgroup averages of deviations $\bar{Y}$ and ranges $R_Y$ are plotted on a single unified control chart across consecutive production runs of completely different parts.

### 2. Standardized Short-Run $\bar{X}$ and $R$ Charts
When consecutive parts differ not only in nominal targets $T_i$ but also in process variability $\sigma_i$ (due to differing tolerances, material hardness, or tool diameters), DNOM is insufficient. Quality engineering applies **Standardized Short-Run Charts**:

For part family $i$ with target $T_i$ and expected average range $\bar{R}_i$, compute the standardized statistics for subgroup $k$:

$$Z_{\bar{X}, k} = \frac{\bar{X}_k - T_i}{\bar{R}_i / (d_2 \sqrt{n})} = \frac{\bar{X}_k - T_i}{A_2 \bar{R}_i / 3}$$

$$W_{R, k} = \frac{R_k}{\bar{R}_i}$$

The standardized mean statistic $Z_{\bar{X}}$ is plotted against fixed universal control limits at $CL = 0, \pm 3$. The standardized range statistic $W_R$ is plotted against center line $CL = 1.0$ with limits at $D_3$ and $D_4$. 

Standardized short-run charting enables a single machine operator to maintain continuous real-time statistical process control across dozens of different part orders on a single control chart, eliminating the traditional barrier to SPC in high-mix manufacturing.
"""

idx1 = u1_text.find("## Fully worked question 1:")
u1_text = u1_text[:idx1] + u1_add.strip() + "\n\n" + u1_text[idx1:]
u1_path.write_text(u1_text, encoding="utf-8")
print("Unit 1 boosted with Short-Run SPC.")
