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

# Unit 5 addition: Easterlin Relative Cohort Size Hypothesis
u5 = (d / "unit-5.md").read_text(encoding="utf-8")
u5_add = """
### The Easterlin Relative Income Hypothesis of Cyclical Fertility
In 1980, the economic demographer Richard A. Easterlin formulated the **Relative Income Hypothesis** (the Easterlin Effect) to explain persistent cyclical fluctuations in fertility across industrialized economies, such as the American post-war baby boom (1946–1964) followed by the baby bust (1965–1980).

Easterlin posited that young adults' propensity to marry and have children is not determined by their absolute level of real income, but by their **relative economic status**—the ratio of their actual material earning potential to their subjective material aspirations:

$$\text{Relative Status} = \frac{\text{Actual Earning Capacity}}{\text{Material Aspirations}}$$

Subjective material aspirations are established during childhood and adolescence in their parents' households. The actual earning capacity of young labor market entrants is heavily governed by the size of their birth cohort relative to older age groups (labor market crowding):
1. **Small Birth Cohort (e.g., 1930s Depression generation)**: When a small cohort enters the labor market, entry-level labor is scarce. Young workers experience low unemployment, rapid promotional advancement, and high relative wages. Because their actual wages far exceed the modest material standards of their childhood, young couples feel economically secure, marry early, and have large families, creating a baby boom!
2. **Large Birth Cohort (e.g., 1950s Baby Boom generation)**: When massive birth cohorts enter the labor market twenty years later, entry-level workers face intense competition, depressed real wages, and blocked promotions. Because their wages cannot easily match the elevated consumer lifestyles of their parents' affluent households, young couples experience economic distress, delay marriage, and drastically curtail childbearing, generating a baby bust.

Easterlin's model demonstrates how cohort size creates endogenous, self-generating demographic cycles with a periodic wavelength of approximately two generations (40 to 50 years).
"""
u5 = u5.replace("## Fully worked question 3", u5_add + "\n## Fully worked question 3")
(d / "unit-5.md").write_text(u5, encoding="utf-8")

# Unit 6 addition: Chaos and Bifurcation in Discrete Population Dynamics
u6 = (d / "unit-6.md").read_text(encoding="utf-8")
u6_add = """
### Non-Linear Discrete Dynamics, Bifurcations, and Deterministic Chaos (Robert May)
In 1976, the theoretical physicist and ecologist Robert M. May published a landmark paper in *Nature* entitled "Simple mathematical models with very complicated dynamics." May demonstrated that when population growth is modeled in discrete annual generations rather than continuous time, the discrete logistic map exhibits breathtaking mathematical complexity, including period-doubling bifurcations and deterministic chaos!

Consider the discrete non-dimensional logistic difference equation:

$$x_{t+1} = R \, x_t (1 - x_t)$$

where x_t in [0, 1] represents population density as a fraction of carrying capacity, and R > 0 is the discrete growth parameter.
As the intrinsic growth parameter R is systematically varied, the dynamical behavior of the population undergoes profound topological phase transitions:
1. **Extinction Regime (0 < R <= 1)**: The population is non-viable and decays monotonically to zero (x_t -> 0).
2. **Monotonic Stable Equilibrium (1 < R <= 3)**: The population converges smoothly to a unique, stable non-zero carrying capacity point x^* = (R - 1) / R. For 2 < R <= 3, convergence exhibits damped oscillatory behavior.
3. **Period-Doubling Bifurcation (3 < R <= 3.449)**: The single stable fixed point becomes unstable and splits into a stable two-point cycle: the population alternates perpetually between high density and low density every two generations!
4. **Cascade of Period Doublings (3.449 < R < 3.57)**: As R increases, the system bifurcates into a 4-cycle, then an 8-cycle, 16-cycle, and 2^k-cycle in rapid succession. The spacing between successive bifurcation thresholds converges to Mitchell Feigenbaum's universal mathematical constant:
   $$\delta = \lim_{k \to \infty} \frac{R_k - R_{k-1}}{R_{k+1} - R_k} \approx 4.6692016$$
5. **Deterministic Chaos (R >= 3.57)**: Beyond the Feigenbaum point R_\infty ~ 3.5699456, periodic predictability breaks down completely! The population trajectory wanders ergodically across the interval, exhibiting extreme sensitivity to initial conditions (the butterfly effect). Two populations starting with imperceptible differences (e.g., 0.500000 versus 0.500001) diverge exponentially over time, rendering long-term demographic forecasting impossible even in a purely deterministic universe without random noise.

May's revelation transformed ecological demography, demonstrating that irregular, volatile population crashes do not necessarily require external catastrophes (such as droughts or plagues); they can emerge purely from the endogenous non-linear feedback of reproduction itself.
"""
u6 = u6.replace("## Fully worked question 1", u6_add + "\n## Fully worked question 1")
(d / "unit-6.md").write_text(u6, encoding="utf-8")

print("Added Easterlin and May Chaos sections!")
