import re
from pathlib import Path

d = Path("publishing/drafts/statistics-probability-demography-and-population-statistics")

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

# Boost Unit 1
u1_p = d / "unit-1.md"
u1 = u1_p.read_text(encoding="utf-8")
u1_extra = """
### Systematic Comparison of Sprague, Beers, and Greville Interpolation Methods
When demographers must reconstruct single-year population distributions from five-year age data, osculatory interpolation techniques provide the mathematical bridge between aggregate reporting and fine-grained demographic analysis. Osculatory interpolation differs from ordinary Lagrange polynomial interpolation in that adjacent polynomial arcs not only intersect at the boundary points between age groups, but also share identical first and second derivatives. This smooth tangential blending eliminates artificial kinks, discontinuous jumps, and negative values at group boundaries.

1. **Sprague's Fifth-Difference Formula**: Developed by Thomas Bond Sprague in 1880, this classical formula fits a fourth-degree or fifth-degree polynomial through six consecutive five-year age groups. The central age group is subdivided into five single-year ages using pre-calculated matrix weights. Sprague ensures that the graduated single-year counts sum exactly to the observed five-year total while minimizing the third and fifth differences across boundaries. However, Sprague formulas can occasionally produce slight oscillations or negative numbers near extreme boundaries (e.g., ages 0–4 or ages 85+).
2. **Beers' Modified Interpolation Coefficients**: In 1945, Henry Beers developed two sets of interpolation coefficients: the "ordinary" formula (which maintains exact group totals) and the "minimized fifth-difference" formula (which permits slight smoothing adjustments to the group totals themselves to eliminate boundary distortions). Beers formulas are widely recognized as superior for graduating data from developing nations where the initial five-year groups already suffer from age-heaping leakage across boundaries.
3. **Greville's Method**: Thomas N. E. Greville integrated actuarial graduation theory with cubic spline interpolation. Greville established that by minimizing a linear combination of squared third differences, one obtains a smoothing operator that preserves the underlying linear demographic trend while effectively dampening observational noise.

Applying these graduation techniques before constructing life tables prevents spurious oscillations in central death rates and ensures that infant and child mortality estimates are not corrupted by digit heaping at ages 5, 10, and 15.
"""
u1 = u1.replace("## Fully worked question 2", u1_extra + "\n## Fully worked question 2")
u1_p.write_text(u1, encoding="utf-8")
print(f"Boosted Unit 1: {prose_count(u1)} words")

# Boost Unit 2
u2_p = d / "unit-2.md"
u2 = u2_p.read_text(encoding="utf-8")
u2_extra = """
### Mathematical Modeling of Stable Age-Sex Structures and Coale-Lopez Ergodicity
A central theorem in mathematical demography, formulated by Ansley J. Coale and Alvaro Lopez in 1961, is the **Weak Ergodicity of Age Structures**. Weak ergodicity addresses whether the long-run age distribution of a population is determined by its contemporary vital rates or by its remote historical origin.

#### Theorem of Weak Ergodicity:
Let two arbitrary closed populations, A and B, have completely different initial age distributions at time t = 0. Suppose that both populations are subjected to the exact same, potentially time-varying, schedules of age-specific fertility and mortality over subsequent decades. Then, as time tends to infinity, the relative age distributions of the two populations converge asymptotically toward each other.

In other words, human age structures possess an **exponential forgetting property**: the demographic memory of past catastrophes, baby booms, civil wars, and historical epidemics fades continuously over time. Within approximately two to three generations (60 to 90 years), the contemporary age distribution reflects exclusively the vital rate schedules experienced over the preceding century, while the initial baseline structure is completely forgotten.

This mathematical property allows demographers to reconstruct stable age structures using Leslie projection matrices and establish that long-run population aging is entirely driven by persistent changes in fertility and adult survival, rather than historical population spikes.

### The Role of Female Reproductive Cohorts and Effective Fecundity
Within the broad working-age group (15–64), demographers isolate the sub-cohort of women in reproductive ages, conventionally defined as ages 15–49. The proportional share of women in this age bracket, and its internal distribution between young reproductive ages (15–29) and late reproductive ages (30–49), exerts a decisive influence on the momentum of population growth.

When a population emerges from high fertility, the proportion of women entering peak childbearing ages (20–29) surges dramatically due to past birth cohorts. Even if every young woman reduces her personal fertility to the replacement level (TFR = 2.1), the sheer numerical concentration of reproductive women causes the absolute number of annual births to continue rising for several decades. This phenomenon, known as **demographic momentum**, ensures that population stabilization lags behind fertility decline by half a century.
"""
u2 = u2.replace("## Fully worked question 2", u2_extra + "\n## Fully worked question 2")
u2_p.write_text(u2, encoding="utf-8")
print(f"Boosted Unit 2: {prose_count(u2)} words")
