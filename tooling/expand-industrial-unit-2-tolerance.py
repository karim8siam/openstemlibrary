#!/usr/bin/env python3
"""
Expand Unit 2 with Tolerance Synthesis & Statistical Stack-Up Analysis.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"

u2_text = (DRAFT_DIR / "unit-2.md").read_text(encoding="utf-8")

tolerance_section = r"""## 2.10 Tolerance Synthesis: Worst-Case Versus Statistical Tolerance Stack-Up

In complex mechanical assemblies—such as automotive engines, aircraft turbine stages, and robotic gearboxes—an overall critical clearance or assembly dimension $Y$ is a function of multiple individual component dimensions:

$$Y = f(X_1, X_2, \dots, X_k)$$

For linear stacks where dimensions add or subtract along a single kinematic chain:

$$Y = a_0 + \sum_{i=1}^k a_i X_i$$

where each component dimension $X_i$ is manufactured to an engineering specification $T_i = \pm \Delta_i$ centered at nominal dimension $m_i$. Mechanical designers must establish individual tolerances $\Delta_i$ to ensure that the final assembly clearance $Y$ conforms to its overall allowable specification $T_{\text{assembly}} = \pm \Delta_Y$.

### Worst-Case Tolerance Synthesis (Arithmetic Stack-Up)
The traditional worst-case approach assumes that by extreme coincidence, all component parts simultaneously deviate to their maximum allowable extreme limits in the worst possible direction:

$$\Delta_{Y, \text{WC}} = \sum_{i=1}^k |a_i| \Delta_i$$

While worst-case tolerancing provides a $100\%$ mathematical guarantee that every possible combination of parts will assemble without interference, it represents an excessively pessimistic and economically punitive design philosophy. To satisfy a tight assembly tolerance $\Delta_Y$ under worst-case rules, individual part tolerances $\Delta_i$ must be set to minuscule values, forcing suppliers to employ slow, ultra-precision grinding and EDM machining, dramatically inflating unit manufacturing costs.

### Statistical Tolerance Synthesis (Root-Sum-Square, RSS)
Statistical tolerance synthesis exploits the mathematical properties of the variance of linear combinations of independent random variables. If each component dimension $X_i$ is an independent random variable with mean $\mu_i = m_i$ and standard deviation $\sigma_i$:

$$\mathbb{E}[Y] = a_0 + \sum_{i=1}^k a_i m_i, \qquad \sigma_Y^2 = \sum_{i=1}^k a_i^2 \sigma_i^2$$

Assuming each component manufacturing process operates at a common capability level $C_{pk}$ such that the natural tolerance spread corresponds to $\Delta_i = 3 C_{pk} \sigma_i$, we obtain the **Root-Sum-Square (RSS)** assembly tolerance:

$$\Delta_{Y, \text{RSS}} = \sqrt{\sum_{i=1}^k a_i^2 \Delta_i^2}$$

Because $\sqrt{\sum a_i^2 \Delta_i^2} < \sum |a_i| \Delta_i$ for all $k \ge 2$, the statistical tolerance band is substantially narrower than the worst-case band. Conversely, for a fixed assembly requirement $\Delta_Y$, the statistical model allows designers to allocate significantly wider tolerances $\Delta_i$ to individual components:

$$\Delta_i \approx \frac{\Delta_Y}{\sqrt{k}}$$

This tolerance expansion dramatically lowers machining costs while maintaining assembly nonconformance rates at parts-per-million levels.

### Dynamic Bender and Six-Sigma Stack Adjustments
In real manufacturing assemblies, component distributions may not be perfectly centered ($\mu_i \ne m_i$). Arthur Bender (1962) observed empirical assembly lines and proposed the **Bender Factor** of $1.5$:

$$\Delta_{Y, \text{Bender}} = 1.5 \sqrt{\sum_{i=1}^k a_i^2 \Delta_i^2}$$

Similarly, Motorola's Six Sigma design framework models potential long-term mean drift by allowing each component mean to drift by $\pm 1.5\sigma_i$. Under worst-case alignment of drifts, the assembly mean shifts by:

$$\text{Shift}_Y = 1.5 \sum_{i=1}^k |a_i| \sigma_i$$

Combining this systematic shift with random RSS variance provides the foundation for robust Six Sigma mechanical tolerance synthesis.
"""

idx = u2_text.find("## Fully worked question 1:")
u2_new = u2_text[:idx] + tolerance_section.strip() + "\n\n" + u2_text[idx:]
(DRAFT_DIR / "unit-2.md").write_text(u2_new, encoding="utf-8")
print("Tolerance section added to Unit 2.")
