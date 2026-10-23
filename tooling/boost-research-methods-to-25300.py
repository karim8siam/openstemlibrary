from pathlib import Path

p3 = Path("publishing/drafts/statistics-probability-statistical-research-methods/unit-3.md")
t3 = p3.read_text(encoding="utf-8")

extra_u3 = r"""
## 3.12 Practical Rules for Constructing Psychometric Scales
When researchers develop novel self-report psychometric inventories, adhering to established psychometric standards prevents common measurement artifacts:
1. Item Pool Generation: Begin with a broad pool of candidate items (typically 3 to 4 times the desired final scale length) generated via comprehensive literature review, qualitative stakeholder interviews, and clinical focus groups.
2. Cognitive Pretesting: Administer candidate items to a pilot cohort using "think-aloud" protocols to identify ambiguous wording, confusing double negatives, and culturally specific idioms.
3. Item Difficulty and Discrimination Indexing: In binary or Likert items, examine item endorsement frequency $p$. Items with extreme difficulty ($p < 0.10$ or $p > 0.90$) exhibit low variance and provide minimal discrimination, whereas items near $p \approx 0.50$ maximize statistical information.
4. Corrected Item-Total Correlations: Compute the point-biserial or Pearson correlation between each item and the total scale score excluding that item ($r_{i(t-i)}$). Discard any items exhibiting $r_{i(t-i)} < 0.30$.
5. Cross-Validation of Factorial Structure: Perform Exploratory Factor Analysis (EFA) on an initial calibration sample, followed by Confirmatory Factor Analysis (CFA) on an entirely independent validation sample to verify configural and metric stability.
"""

t3 = t3.replace("## 3.11 Unit 3 Methodological Synthesis and Review", extra_u3.strip() + "\n\n## 3.11 Unit 3 Methodological Synthesis and Review")
p3.write_text(t3, encoding="utf-8")

p5 = Path("publishing/drafts/statistics-probability-statistical-research-methods/unit-5.md")
t5 = p5.read_text(encoding="utf-8")

extra_u5 = r"""
## 5.13 Power and Sample Size for Longitudinal and Repeated-Measures Designs
In longitudinal studies where participants are measured repeatedly across $T$ measurement occasions, statistical power is governed by the within-subject correlation $\rho$ between repeated measures.
For a repeated-measures design testing a between-within interaction (e.g., comparing treatment vs control trajectory across $T$ time points), the required total sample size is:
$$N = \frac{2 (z_{\alpha/2} + z_\beta)^2 (1 - \rho)}{T \cdot f^2}$$
Notice that as the within-subject correlation $\rho$ increases toward $1.0$, the factor $(1 - \rho)$ shrinks dramatically. Positive autocorrelation between repeated observations eliminates between-subject noise, multiplying statistical efficiency. A longitudinal design with $T = 4$ measurement occasions and autocorrelation $\rho = 0.70$ requires less than one-third the sample size of an equivalent cross-sectional design.
"""

t5 = t5.replace("## 5.7 Unit 5 Methodological Synthesis and Review", extra_u5.strip() + "\n\n## 5.7 Unit 5 Methodological Synthesis and Review")
p5.write_text(t5, encoding="utf-8")

print("Added text to Units 3 and 5.")
