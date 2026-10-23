#!/usr/bin/env python3
"""
Add DPU / DPMO conversion to Unit 3 to cross 25,000 words.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"

u3_path = DRAFT_DIR / "unit-3.md"
u3_text = u3_path.read_text(encoding="utf-8")

u3_add = r"""
## 3.13 Conversion Between Defect Metrics: DPU, DPO, and DPMO

In Six Sigma enterprise quality frameworks, attribute defect data must be normalized to enable cross-departmental benchmarking across products of radically differing complexity. A printed circuit board with $2,000$ solder joints cannot be compared directly with a stamped bracket containing only $4$ holes using raw defect counts.

To normalize defect data across varying assembly complexity:
1. **Defects Per Unit ($DPU$)**: The average number of defects observed per finished product unit:
   $$DPU = \frac{\text{Total Defects Found}}{\text{Total Units Inspected}} = \frac{D}{N}$$
2. **Defects Per Opportunity ($DPO$)**: The ratio of observed defects to the total number of distinct opportunities for defect generation across the inspected units:
   $$DPO = \frac{\text{Total Defects Found}}{\text{Total Units Inspected} \times \text{Defect Opportunities per Unit}} = \frac{D}{N \times O}$$
   where $O$ is the number of opportunities for error per product unit.
3. **Defects Per Million Opportunities ($DPMO$)**: Normalizing $DPO$ to a standard scale of one million:
   $$DPMO = DPO \times 1,000,000$$

Converting $DPMO$ to the equivalent Six Sigma quality level via the inverse standard normal distribution:
$$\text{Sigma Level} = \Phi^{-1}(1 - DPMO / 1,000,000) + 1.5$$
This mathematical conversion bridges the gap between discrete attribute counts and continuous Six Sigma process capability metrics.
"""

idx3 = u3_text.find("## Fully worked question 1:")
u3_text = u3_text[:idx3] + u3_add.strip() + "\n\n" + u3_text[idx3:]
u3_path.write_text(u3_text, encoding="utf-8")
print("Unit 3 boosted with DPU/DPMO.")
