#!/usr/bin/env python3
"""
Ensure Economic Statistics comfortably crosses 30,500 pure prose words.
"""
import re
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-economic-statistics")

def prose_count(text):
    text = re.sub(r"\$\$[\s\S]*?\$\$", " ", text)
    text = re.sub(r"\$[^$\n]+\$", " ", text)
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`[^`\n]+`", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^#+\s.*$", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*+]\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    words = re.findall(r"\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b", text)
    return len(words)

def inject_before_worked_questions(content, addition):
    marker = "## Worked Questions and Solutions"
    if marker in content:
        parts = content.split(marker)
        return parts[0] + addition + "\n" + marker + parts[1]
    else:
        return content + "\n" + addition

u7_ras = """
---

## Updating Input-Output Matrices: The RAS Biproportional Method

Because comprehensive national input-output tables require extensive nationwide enterprise censuses, national statistical bureaus typically compile full benchmark tables only once every five or ten years. In the intervening years, macroeconomic planners possess updated aggregate sectoral gross outputs ($X_i$), total intermediate deliveries ($u_i = \\sum_{j} x_{ij}$), and total intermediate purchases ($v_j = \\sum_{i} x_{ij}$), but lack the detailed interior cell transactions $x_{ij}$.

To update an existing baseline technology matrix $A^0$ to a target year without conducting a full census, mathematical statisticians employ the **RAS Biproportional Adjustment Method** (Richard Stone, 1961).

### 1. The Biproportional Model Formulation
The RAS algorithm assumes that changes in technical coefficients over time reflect two distinct, independent economic forces:
1. **The Substitution Effect ($r_i$)**: A row multiplier reflecting secular substitution across all consuming industries toward or away from input $i$ (e.g., universal substitution of digital telecommunications for paper, or plastics for steel).
2. **The Fabrication Effect ($s_j$)**: A column multiplier reflecting technological changes in the fabrication depth or degree of processing in industry $j$ (e.g., automation reducing total intermediate materials relative to gross output).

The updated technical coefficient matrix $A^1$ is formulated as the biproportional product:

$$A^1 = \\hat{r} A^0 \\hat{s}$$

where $\\hat{r} = \\text{diag}(r_1, r_2, \\dots, r_n)$ is a diagonal matrix of row scaling factors, and $\\hat{s} = \\text{diag}(s_1, s_2, \\dots, s_n)$ is a diagonal matrix of column scaling factors.

In element-wise terms:
$$a_{ij}^1 = r_i a_{ij}^0 s_j$$

### 2. The Iterative Balancing Algorithm
The vectors $r$ and $s$ are determined iteratively to satisfy two simultaneous marginal constraints:
- **Row Sum Constraint**: $\\sum_{j=1}^{n} a_{ij}^1 X_j^1 = u_i^1$ (Total intermediate deliveries match observed target rows).
- **Column Sum Constraint**: $\\sum_{i=1}^{n} a_{ij}^1 X_j^1 = v_j^1$ (Total intermediate purchases match observed target columns).

The algorithm alternates between:
- Step 1: Scaling rows to match intermediate deliveries $u^1$.
- Step 2: Scaling columns of the resulting matrix to match intermediate purchases $v^1$.

Michael Bacharach (1970) proved that if the baseline matrix $A^0$ is non-negative and connected, the iterative RAS algorithm converges uniquely to the global minimum of the Kullback-Leibler information divergence:
$$\\min \\sum_{i=1}^{n} \\sum_{j=1}^{n} x_{ij}^1 \\ln\\left( \\frac{x_{ij}^1}{x_{ij}^0} \\right)$$
The updated matrix preserves all structural zero entries, guarantees strictly non-negative technical coefficients, and satisfies all macro-accounting identities.
"""

u8_ramsey = """
---

## Price Elasticity and Public Utility Regulation: Ramsey-Boiteux Pricing

In natural monopoly utility markets (such as national electrical power grids, municipal water supply networks, postal networks, and passenger railway infrastructure), high fixed infrastructure costs mean that average costs decline continuously over relevant market demand (economies of scale). If regulators force the utility to price at marginal cost ($P = MC$), the firm incurs severe operational deficits and bankrupts ($P < AC$). If the utility is left unregulated, it charges monopoly prices, generating massive deadweight welfare loss.

To resolve this dilemma, Frank Ramsey (1927) and Marcel Boiteux (1956) formulated the theory of **Optimal Second-Best Regulated Pricing (Ramsey-Boiteux Pricing)**.

### Mathematical Formulation
Consider a multi-product regulated public utility producing $n$ distinct services (e.g., residential peak electricity, commercial off-peak electricity, industrial power).
The regulator seeks to maximize total societal consumer surplus subject to the financial self-sufficiency constraint that the utility earns zero economic loss (total revenues cover total costs):

$$\\max_{\\{p_1, \\dots, p_n\\}} W(p_1, \\dots, p_n) \\quad \\text{subject to } \\sum_{i=1}^{n} p_i q_i(p_i) - C(q_1, \\dots, q_n) \\ge 0$$

Formulating the Lagrangian with shadow multiplier $\\lambda > 0$:
$$\\mathcal{L} = W(p) + \\lambda \\left[ \\sum_{i=1}^{n} p_i q_i(p_i) - C(q) \\right]$$

Differentiating with respect to each price $p_i$ and assuming zero cross-price substitution across independent services yields the **Inverse Elasticity Rule for Optimal Taxation and Regulation**:

$$\\frac{p_i - MC_i}{p_i} = \\left( \\frac{\\lambda}{1 + \\lambda} \\right) \\frac{1}{|\\eta_{i, p}|}$$

where:
- $\\frac{p_i - MC_i}{p_i}$ is the proportional markup over marginal cost.
- $|\\eta_{i, p}|$ is the absolute own-price elasticity of demand for service $i$.
- $\\frac{\\lambda}{1 + \\lambda} \\in (0, 1)$ is the normalized Ramsey shadow price of the public utility's budget constraint.

### Economic and Equity Implications:
The Ramsey rule establishes that to minimize societal deadweight loss while balancing the utility's budget:
- Services with highly **price-inelastic demand** (e.g., basic residential lighting where $|\\eta_p| \\approx 0.2$) must bear a **high percentage markup** over marginal cost.
- Services with highly **price-elastic demand** (e.g., industrial manufacturing power with competitive on-site alternatives where $|\\eta_p| \\approx 1.5$) must receive a **low percentage markup** close to marginal cost.

While mathematically efficient in minimizing Harberger deadweight triangles, pure Ramsey pricing can produce regressive distributional consequences by charging captive residential households higher markups than footloose corporate consumers, requiring regulators to integrate distributional equity weights into statutory rate-setting tariffs.
"""

additions = {
    7: u7_ras,
    8: u8_ramsey,
}

for unit_num, add_text in additions.items():
    file_path = OUT_DIR / f"unit-{unit_num}.md"
    content = file_path.read_text(encoding="utf-8")
    new_content = inject_before_worked_questions(content, add_text)
    file_path.write_text(new_content, encoding="utf-8")
    print(f"Unit {unit_num} finished: {prose_count(new_content)} words")
