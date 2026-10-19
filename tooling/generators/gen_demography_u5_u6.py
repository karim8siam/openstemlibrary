import re
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-demography-and-population-statistics")

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

# ==============================================================================
# UNIT 5: Measures of Fertility, Nuptiality & Reproduction
# ==============================================================================
u5_content = """# Unit 5: Measures of Fertility, Nuptiality & Reproduction

Fertility is the demographic engine of generational renewal, governing the entry of new human beings into society through biological birth. In demography, a crucial conceptual distinction is maintained between **fecundity**—the physiological biological capacity of an individual or couple to conceive and produce viable offspring—and **fertility**—the actual realization of live births in an empirical population. Because childbearing is physiologically constrained to women within the reproductive lifespan (conventionally defined as ages 15 to 49) and is profoundly shaped by marital arrangements, modern contraceptive technology, socio-economic norms, and biological postpartum amenorrhea, measuring fertility requires a sophisticated hierarchy of refined rates, synthetic cohort indicators, and reproduction indices.

## 5.1 The Hierarchy of Aggregate Fertility Measures: CBR, GFR, and GMFR

Demographic analysis evaluates fertility through increasingly refined exposure bases, systematically narrowing the denominator to isolate the population at genuine biological and legal risk of childbearing.

### The Crude Birth Rate (CBR)
The simplest and most widely available measure of fertility is the **Crude Birth Rate ($CBR$)**, defined as the total number of registered live births $B$ occurring in a designated population during a calendar year divided by the mid-year total population $P_{\\text{mid}}$, conventionally expressed per $1{,}000$ person-years:

$$CBR = \\frac{B}{P_{\\text{mid}}} \\times 1{,}000$$

Like the crude death rate, the Crude Birth Rate is heavily confounded by the underlying age and sex distribution of the population. A population with a high proportion of children or elderly citizens will automatically record a depressed $CBR$, even if adult women of childbearing age exhibit exceptionally high reproductive intensity. Conversely, a population undergoing a demographic dividend with a high concentration of young adults will exhibit an elevated $CBR$ even if individual family sizes are modest.

### The General Fertility Rate (GFR)
To eliminate the distortion caused by males, children, and elderly persons who cannot give birth, demographers restrict the denominator to women of reproductive age. The **General Fertility Rate ($GFR$)** is defined as the number of live births per $1{,}000$ women aged 15 to 49:

$$GFR = \\frac{B}{W_{15-49}} \\times 1{,}000$$

where $W_{15-49} = \\sum_{x=15}^{49} F_x$ is the mid-year population of women in the reproductive age span. In some national statistical bureaus, the reproductive interval is defined as ages 15 to 44 ($W_{15-44}$); however, the United Nations demographic standard employs the 15–49 bracket.

The algebraic relationship between the Crude Birth Rate and the General Fertility Rate reveals the structural role of population composition:

$$CBR = \\frac{B}{P} = \\left( \\frac{B}{W_{15-49}} \\right) \\times \\left( \\frac{W_{15-49}}{P} \\right) = \\frac{GFR}{1{,}000} \\times \\left( \\frac{W_{15-49}}{P} \\right) \\times 1{,}000$$

$$CBR = GFR \\times \\left( \\frac{W_{15-49}}{P} \\right)$$

where $\\frac{W_{15-49}}{P}$ is the proportion of women of childbearing age in the total national population.

### The General Marital Fertility Rate (GMFR)
In societies where childbearing outside legal matrimony or formal cohabitation is rare or socially sanctioned, demographers further refine the denominator to married women. The **General Marital Fertility Rate ($GMFR$)** is:

$$GMFR = \\frac{B_M}{M W_{15-49}} \\times 1{,}000$$

where $B_M$ is the number of legitimate live births born to married women, and $M W_{15-49}$ is the mid-year population of legally married women aged 15 to 49.

## 5.2 Age-Specific Fertility Rates (ASFR) and the Total Fertility Rate (TFR)

Because the physiological probability of conception and pregnancy varies dramatically across the reproductive years—peaking in the twenties and declining steadily to near-zero by age 48 due to ovarian follicular depletion and biological menopause—demographers decompose fertility into single-year or quinquennial age intervals.

### The Age-Specific Fertility Rate (ASFR)
Let $B_x$ denote the number of live births born to mothers in age group $[x, x+n)$ during a calendar year, and let $_n W_x$ denote the mid-year population of women in that exact age group. The **Age-Specific Fertility Rate**, denoted by $_n f_x$ (or $ASFR_x$), is:

$$_n f_x = \\frac{_n B_x}{_n W_x}$$

In conventional demographic tables, fertility is reported across seven standard five-year age intervals ($n = 5$): 15–19, 20–24, 25–29, 30–34, 35–39, 40–44, and 45–49.

Across human populations, the curve of $_5 f_x$ against age exhibits an inverted U-shaped bell curve:
- **Ages 15–19**: Characterized by low or moderate fertility depending on the mean age at marriage and adolescent education levels.
- **Ages 20–29**: Represents the physiological and reproductive peak in almost all societies. In early-marrying developing nations, peak fertility occurs in the 20–24 bracket (early-peak pattern). In modern post-industrial societies with prolonged university education and career establishment, the peak shifts to ages 30–34 (late-peak pattern).
- **Ages 35–49**: Fertility declines rapidly, terminating at age 50.

### The Total Fertility Rate (TFR)
The **Total Fertility Rate ($TFR$)** is universally acknowledged as the single most important summary index of fertility in demographic science. The $TFR$ is a **synthetic cohort measure**: it represents the average number of children that would be born alive to a hypothetical woman if she were to survive through all her reproductive years (from age 15 to 50) and experience at each age the exact age-specific fertility rates observed in the contemporary population during the reference year.

#### Mathematical Derivation of TFR:
In continuous formulation, $TFR$ is the integral of the continuous age-specific fertility schedule $f(x)$ over the reproductive window $[15, 50]$:

$$TFR = \\int_{15}^{50} f(x) \\, dx$$

In discrete five-year grouped demographic data ($n = 5$), the integral is evaluated as five times the sum of the quinquennial rates:

$$TFR = 5 \\times \\sum_{i=1}^7 {_5 f_{15 + 5(i-1)}} = 5 \\times \\left[ {_5 f_{15}} + {_5 f_{20}} + {_5 f_{25}} + {_5 f_{30}} + {_5 f_{35}} + {_5 f_{40}} + {_5 f_{45}} \\right]$$

If rates are expressed per $1{,}000$ women ($ASFR_x = 1{,}000 \\cdot {_5 f_x}$), then:

$$TFR = \\frac{5 \\times \\sum_{x} ASFR_x}{1{,}000}$$

#### Decisive Advantages of the TFR:
1. **Purged of Age-Structural Bias**: Because the age-specific rates $_5 f_x$ are evaluated within homogeneous female age cohorts, the $TFR$ is completely independent of the age composition and sex ratio of the living population.
2. **Intuitive Scale**: Unlike crude rates which are expressed per thousand, the $TFR$ is expressed on an intuitive, human scale: the average number of children per woman (e.g., $1.85$ children per woman).

## 5.3 Generational Replacement: Gross and Net Reproduction Rates

While the Total Fertility Rate measures total childbearing across both sexes, the long-term demographic survival and generational replacement of a population depends strictly on the birth of **female offspring**, because only females can bear children in the subsequent generation.

### The Gross Reproduction Rate (GRR)
The **Gross Reproduction Rate ($GRR$)** represents the average number of **female daughters** that would be born to a hypothetical woman if she were to survive to the end of her reproductive life (age 50) subject to the prevailing age-specific fertility schedule.

Let $B_F$ denote female live births and $B$ denote total live births. Let $p_f$ denote the proportion of female births:

$$p_f = \\frac{B_F}{B} = \\frac{1}{1 + \\frac{SRB}{100}} = \\frac{100}{100 + SRB}$$

Under the standard biological sex ratio at birth ($SRB \\approx 105$ males per 100 females):

$$p_f = \\frac{100}{100 + 105} = \\frac{100}{205} \\approx 0.4878$$

Assuming the sex ratio at birth is constant across all maternal age groups:

$$GRR = p_f \\times TFR = 0.4878 \\times TFR$$

Alternatively, if age-specific fertility rates for female births alone ($f_x^F = \\frac{B_x^F}{W_x}$) are known:

$$GRR = 5 \\times \\sum_{x} {_5 f_x^F}$$

The Gross Reproduction Rate establishes an absolute upper bound on generational replacement, because it assumes **zero mortality** among women prior to age 50.

### The Net Reproduction Rate (NRR)
In reality, not all newborn girls survive to reach childbearing age, and those who enter the reproductive span face mortality risks that may terminate their lives before completing age 50. The **Net Reproduction Rate ($NRR$)** incorporates female mortality schedules directly into the fertility calculation.

The $NRR$ represents the average number of female daughters that will be born to a newborn female infant, taking into account the prevailing schedules of both age-specific fertility and age-specific female mortality.

#### Mathematical Formulation of NRR:
In continuous mathematical demography, let $l(x)$ denote the female life table survival function with radix $l_0 = 1$ (so that $l(x)$ represents the exact probability that a newborn girl survives to age $x$). Let $f_F(x)$ denote the continuous force of female childbearing at age $x$. The Net Reproduction Rate is the integral:

$$NRR = \\int_{15}^{50} l(x) \\, f_F(x) \\, dx = p_f \\int_{15}^{50} l(x) \\, f(x) \\, dx$$

In discrete five-year life table and demographic accounting:

$$NRR = p_f \\times \\sum_{x} \\left( \\frac{_5 L_x^F}{5 \\cdot l_0^F} \\right) \\times \\left( 5 \\cdot {_5 f_x} \\right) = p_f \\times \\sum_{x} \\left( \\frac{_5 L_x^F}{l_0^F} \\right) {_5 f_x}$$

where $_5 L_x^F$ is the female life table person-years lived in interval $[x, x+5)$, and $l_0^F = 100{,}000$ is the female life table radix.

### Demographic Significance of the NRR:
The numerical value of the Net Reproduction Rate determines the long-term mathematical destiny of a closed population:
1. **$NRR > 1.00$**: Each generation of mothers is replaced by a larger generation of daughters. The population has an intrinsic positive rate of natural increase ($r > 0$) and will experience long-run exponential growth.
2. **$NRR = 1.00$**: Exact **Replacement-Level Fertility**. Each generation of mothers is replaced by exactly one daughter who survives through her reproductive life. In the long run, the population will stabilize into a stationary state with zero growth ($r = 0$).
3. **$NRR < 1.00$**: **Sub-Replacement Fertility**. Each generation of mothers is replaced by a numerically smaller generation of daughters. If sustained, the population enters persistent demographic decline ($r < 0$) and long-run contraction.

#### Why Replacement-Level TFR Equals 2.1 in Modern Societies:
To achieve $NRR = 1.00$:
$$NRR = p_f \\cdot S_{\\text{mean}} \\cdot TFR = 1.00$$
where $S_{\\text{mean}} = \\frac{L_{\\text{mean}}}{l_0}$ is the average probability that a newborn female survives to mean childbearing age (around age 28). In low-mortality post-industrial societies with high life expectancy, $S_{\\text{mean}} \\approx 0.985$ to $0.990$.
Substituting $p_f \\approx 0.4878$:

$$TFR_{\\text{replacement}} = \\frac{1.00}{0.4878 \\times 0.988} \\approx \\frac{1.00}{0.4819} \\approx 2.075 \\approx 2.10$$

In developing countries with high child mortality ($S_{\\text{mean}} \\approx 0.80-0.85$), replacement-level $TFR$ must be considerably higher—frequently $2.4$ to $2.8$ children per woman—to compensate for female mortality before adulthood.

## 5.4 Nuptiality Analysis: Singulate Mean Age at Marriage (SMAM)

Marriage (nuptiality) represents the legal and social framework within which the vast majority of human childbearing historically occurred. Postponing marriage directly truncates the duration of marital exposure to conception, serving as a primary driver of historical fertility declines.

### Hajnal's Singulate Mean Age at Marriage (SMAM)
In 1953, John Hajnal formulated an ingenious demographic method to calculate the mean age at first marriage from census cross-sectional data on marital status, without requiring retrospective marriage registries or longitudinal cohort tracking.

The **Singulate Mean Age at Marriage ($SMAM$)** represents the average number of years lived in the never-married (single) state by a synthetic cohort of individuals who marry before exact age 50.

#### Mathematical Algorithm for Hajnal's SMAM:
Let $s_x$ denote the proportion of individuals who are never married (single) in five-year age group $[x, x+5)$, obtained directly from a census cross-tabulation of marital status by age.
1. Compute the total person-years lived in the single state between age 0 and age 50 by a synthetic cohort of size 1:
   Assume everyone is single from birth to age 15:
   $$Y_{0-15} = 15 \\times 1.00 = 15.0$$
   Sum the person-years lived single in the seven five-year intervals from age 15 to 49:
   $$Y_{15-50} = 5 \\times \\sum_{k=1}^7 s_{15 + 5(k-1)} = 5 \\times (s_{15} + s_{20} + s_{25} + s_{30} + s_{35} + s_{40} + s_{45})$$
   Total single person-years lived up to age 50:
   $$A = 15.0 + Y_{15-50}$$
2. Estimate the proportion of the cohort who remain permanently single at age 50 (never marry throughout life). By convention, this is estimated as the average of the proportions single in the 45–49 and 50–54 brackets:
   $$s_{50} = \\frac{s_{45} + s_{50}}{2}$$
3. The person-years lived by those who remain permanently single up to age 50 is:
   $$B = 50 \\times s_{50}$$
4. The net person-years lived in the single state by those individuals who **do marry** before age 50 is:
   $$C = A - B$$
5. The proportion of the synthetic cohort who marry before age 50 is:
   $$D = 1.00 - s_{50}$$
6. **The Singulate Mean Age at Marriage** is:

$$SMAM = \\frac{C}{D} = \\frac{A - 50 \\cdot s_{50}}{1 - s_{50}}$$

Hajnal's $SMAM$ remains the worldwide demographic standard for tracking generational trends in marriage timing and adolescent transition.

## 5.5 Bongaarts' Framework of Proximate Determinants of Fertility

In 1978 and 1982, John Bongaarts formulated the definitive mathematical framework explaining how socio-economic and cultural factors translate into observed fertility levels through intermediate biological and behavioral variables, known as **proximate determinants**.

Bongaarts demonstrated that although human females have a biological maximum reproductive capacity (the **Total Fecundity Rate**, $TF$, empirically estimated at an average of $15.3$ children per woman), no actual human society exhibits a $TFR$ near 15. Four primary proximate determinants account for ninety-six percent of the variance in fertility across human societies:
1. **Proportion Married / In Union ($C_m$)**: The dampening effect of delayed marriage, non-marriage, or marital dissolution.
2. **Contraception ($C_c$)**: The dampening effect of modern and traditional contraceptive methods, weighted by their clinical efficacy.
3. **Induced Abortion ($C_a$)**: The dampening effect of voluntary pregnancy terminations.
4. **Postpartum Infecundability ($C_i$)**: The dampening effect of prolonged breastfeeding and lactational amenorrhea, which biologically delays the resumption of ovulation after childbirth.

### Bongaarts' Multiplicative Fertility Model:
Bongaarts expressed the Total Fertility Rate as a multiplicative chain:

$$TFR = C_m \\times C_c \\times C_a \\times C_i \\times TF$$

Each index $C$ is a dimensionless parameter bounded between $0$ and $1$:
- If an index equals $1.00$, the corresponding factor exerts zero inhibiting effect on fertility (e.g., $C_c = 1.00$ means zero contraceptive use).
- If an index equals $0.00$, the corresponding factor completely suppresses fertility.

#### Mathematical Definitions of the Four Bongaarts Indices:
1. **Index of Marriage ($C_m$)**:
   $$C_m = \\frac{TFR}{TMFR} \\approx \\frac{\\sum f(x)}{\\sum m(x)} \\approx \\frac{\\sum m(x) \\cdot \\mu(x)}{\\sum m(x)}$$
   where $m(x)$ is the age-specific marital fertility rate and $\\mu(x)$ is the proportion of women currently married at age $x$.
2. **Index of Contraception ($C_c$)**:
   $$C_c = 1 - 1.08 \\cdot u \\cdot e$$
   where $u$ is the contraceptive prevalence rate among married women of childbearing age, $e$ is the average method-mix contraceptive efficacy (ranging from $0.70$ for traditional withdrawal to $0.99$ for intrauterine devices and sterilization), and $1.08$ is a biological correction factor accounting for sterile couples who do not require contraception.
3. **Index of Induced Abortion ($C_a$)**:
   $$C_a = \\frac{TFR}{TFR + 0.4 \\cdot (1 + u) \\cdot TAR}$$
   where $TAR$ is the Total Abortion Rate per woman.
4. **Index of Postpartum Infecundability ($C_i$)**:
   $$C_i = \\frac{20}{18.5 + i}$$
   where $i$ is the average duration of postpartum amenorrhea (in months) induced by prolonged breastfeeding. In the absence of breastfeeding, the normal inter-pregnancy ovulatory interval is approximately $20$ months ($1.5$ months of postpartum infecundability + $7.5$ months of time-to-conception + $2$ months of spontaneous fetal loss + $9$ months of gestation = $20$ months). Prolonged lactation expands $i$, driving $C_i$ downward to $0.60$ or $0.50$.

Bongaarts' model allows demographers to isolate precisely how much of a national fertility decline is attributable to expanding family planning programs ($C_c$) versus rising age at marriage ($C_m$).

## Fully worked question 1: Comprehensive Calculation of CBR, GFR, ASFR, and TFR

### Question
A provincial census office and vital registration bureau in an agricultural province compile demographic data for calendar year 2024. The female population by five-year age intervals and the registered live births classified by mother's attained age are summarized below:

| Maternal Age Interval | Female Population ($W_x$) | Registered Live Births ($B_x$) |
| :---: | :---: | :---: |
| **15–19** | $320{,}000$ | $12{,}800$ |
| **20–24** | $300{,}000$ | $48{,}000$ |
| **25–29** | $280{,}000$ | $56{,}000$ |
| **30–34** | $260{,}000$ | $39{,}000$ |
| **35–39** | $240{,}000$ | $21{,}600$ |
| **40–44** | $210{,}000$ | $6{,}300$ |
| **45–49** | $190{,}000$ | $950$ |
| **Total (15–49)** | $1{,}800{,}000$ | $184{,}650$ |

The total enumerated population of the province (including all males, children, and elderly persons of both sexes) is $N = 6{,}500{,}000$.

1. Compute the Crude Birth Rate ($CBR$) per $1{,}000$ total population and the General Fertility Rate ($GFR$) per $1{,}000$ women of childbearing age. Verify the algebraic link between $CBR$ and $GFR$.
2. Calculate the Age-Specific Fertility Rate ($ASFR_x$) per $1{,}000$ women for every five-year age bracket.
3. Compute the Total Fertility Rate ($TFR$) per woman. Assuming a standard biological sex ratio at birth of $SRB = 105$ boys per 100 girls, compute the Gross Reproduction Rate ($GRR$).

### Solution, step 1: Compute Aggregate Fertility Rates (CBR and GFR)
Total registered live births: $B = 184{,}650$.
Total provincial population: $N = 6{,}500{,}000$.
Total female childbearing population ($15-49$): $W_{15-49} = 1{,}800{,}000$.

1. **The Crude Birth Rate ($CBR$)**:
   $$CBR = \\frac{B}{N} \\times 1{,}000 = \\frac{184{,}650}{6{,}500{,}000} \\times 1{,}000 \\approx 28.4077 \\implies 28.41 \\text{ per 1,000 total population}$$

2. **The General Fertility Rate ($GFR$)**:
   $$GFR = \\frac{B}{W_{15-49}} \\times 1{,}000 = \\frac{184{,}650}{1{,}800{,}000} \\times 1{,}000 = 102.5833 \\implies 102.58 \\text{ per 1,000 women aged 15–49}$$

**Verification of Decomposition Identity:**
The proportion of women of childbearing age in the population is:
$$\\frac{W_{15-49}}{N} = \\frac{1{,}800{,}000}{6{,}500{,}000} \\approx 0.276923$$
Multiplying by $GFR$:
$$CBR = 102.5833 \\times 0.276923 \\approx 28.4077$$
The structural identity $CBR = GFR \\times \\frac{W_{15-49}}{N}$ is verified.

### Solution, step 2: Calculate Age-Specific Fertility Rates (ASFR)
We compute $ASFR_x = \\frac{B_x}{W_x} \\times 1{,}000$ for each five-year cohort:
1. **Ages 15–19**:
   $$ASFR_{15-19} = \\frac{12{,}800}{320{,}000} \\times 1{,}000 = 40.00 \\text{ per 1,000}$$
2. **Ages 20–24**:
   $$ASFR_{20-24} = \\frac{48{,}000}{300{,}000} \\times 1{,}000 = 160.00 \\text{ per 1,000}$$
3. **Ages 25–29**:
   $$ASFR_{25-29} = \\frac{56{,}000}{280{,}000} \\times 1{,}000 = 200.00 \\text{ per 1,000}$$
4. **Ages 30–34**:
   $$ASFR_{30-34} = \\frac{39{,}000}{260{,}000} \\times 1{,}000 = 150.00 \\text{ per 1,000}$$
5. **Ages 35–39**:
   $$ASFR_{35-39} = \\frac{21{,}600}{240{,}000} \\times 1{,}000 = 90.00 \\text{ per 1,000}$$
6. **Ages 40–44**:
   $$ASFR_{40-44} = \\frac{6{,}300}{210{,}000} \\times 1{,}000 = 30.00 \\text{ per 1,000}$$
7. **Ages 45–49**:
   $$ASFR_{45-49} = \\frac{950}{190{,}000} \\times 1{,}000 = 5.00 \\text{ per 1,000}$$

Notice that fertility exhibits a broad peak across ages 20 to 34, reaching an absolute zenith in the 25–29 age bracket ($200.00$ per $1{,}000$).

### Solution, step 3: Calculate TFR and GRR
Sum the Age-Specific Fertility Rates:

$$\\sum ASFR = 40.00 + 160.00 + 200.00 + 150.00 + 90.00 + 30.00 + 5.00 = 675.00 \\text{ per 1,000}$$

Because each age bracket spans five years ($n = 5$):

$$TFR = \\frac{5 \\times \\sum ASFR}{1{,}000} = \\frac{5 \\times 675.00}{1{,}000} = \\frac{3{,}375.00}{1{,}000} = 3.375 \\text{ children per woman}$$

Under current childbearing patterns, a woman surviving through her reproductive years would give birth to an average of $3.38$ children.

Now compute the Gross Reproduction Rate ($GRR$).
The proportion of female births under $SRB = 105$ is:

$$p_f = \\frac{100}{100 + 105} = \\frac{100}{205} \\approx 0.487805$$

The Gross Reproduction Rate is:

$$GRR = p_f \\times TFR = 0.487805 \\times 3.375 = 1.64634 \\approx 1.65 \\text{ daughters per woman}$$

**Demographic Conclusion**:
Under zero mortality, each generation of mothers would be replaced by $1.65$ daughters—a potential generational expansion of $65\\%$.

## Fully worked question 2: Computation of Net Reproduction Rate (NRR) with Life Table Female Survival

### Question
To determine whether a middle-income country has reached generational replacement fertility, a demographic team links age-specific fertility rates with the national female abridged life table. The empirical age-specific fertility rates ($ASFR_x$ per woman) and the female life table person-years lived per newborn female ($S_x = \\frac{_5 L_x^F}{5 \\cdot l_0^F}$) are given below:

| Age Interval ($x$ to $x+5$) | ASFR per Woman ($_5 f_x$) | Female Survival Probability ($S_x$) |
| :---: | :---: | :---: |
| **15–19** | $0.0240$ | $0.9820$ |
| **20–24** | $0.0880$ | $0.9780$ |
| **25–29** | $0.1220$ | $0.9730$ |
| **30–34** | $0.1040$ | $0.9670$ |
| **35–39** | $0.0520$ | $0.9590$ |
| **40–44** | $0.0180$ | $0.9480$ |
| **45–49** | $0.0020$ | $0.9320$ |

The sex ratio at birth in the vital registry is $SRB = 106.0$ male births per 100 female births.

1. Compute the Total Fertility Rate ($TFR$) and the Gross Reproduction Rate ($GRR$).
2. Compute the Net Reproduction Rate ($NRR$) by evaluating the product of age-specific fertility, cohort survival, and female birth proportion across all seven reproductive intervals.
3. Determine whether the population is above, at, or below replacement level, and calculate the mean generation length $T$ and the intrinsic annual rate of natural increase $r$ under the Lotka approximation.

### Solution, step 1: Calculate TFR and GRR
Sum the age-specific fertility rates per woman:

$$\\sum {_5 f_x} = 0.0240 + 0.0880 + 0.1220 + 0.1040 + 0.0520 + 0.0180 + 0.0020 = 0.4100$$

Since the interval width is $n = 5$ years:

$$TFR = 5 \\times \\sum {_5 f_x} = 5 \\times 0.4100 = 2.050 \\text{ children per woman}$$

The proportion of female births under $SRB = 106.0$ is:

$$p_f = \\frac{100}{100 + 106.0} = \\frac{100}{206.0} \\approx 0.485437$$

The Gross Reproduction Rate is:

$$GRR = p_f \\times TFR = 0.485437 \\times 2.050 = 0.995146 \\approx 0.9951 \\text{ daughters per woman}$$

Notice that even under the impossible assumption of zero female mortality, $GRR < 1.00$ ($0.9951$), meaning that even without mortality, women are failing to replace themselves.

### Solution, step 2: Calculate the Net Reproduction Rate (NRR)
The discrete life table formula for the Net Reproduction Rate is:

$$NRR = p_f \\times 5 \\times \\sum_{x} \\left( S_x \\cdot {_5 f_x} \\right)$$

We evaluate the product $S_x \\cdot {_5 f_x}$ for each age group:
- **Ages 15–19**: $0.9820 \\times 0.0240 = 0.023568$
- **Ages 20–24**: $0.9780 \\times 0.0880 = 0.086064$
- **Ages 25–29**: $0.9730 \\times 0.1220 = 0.118706$
- **Ages 30–34**: $0.9670 \\times 0.1040 = 0.100568$
- **Ages 35–39**: $0.9590 \\times 0.0520 = 0.049868$
- **Ages 40–44**: $0.9480 \\times 0.0180 = 0.017064$
- **Ages 45–49**: $0.9320 \\times 0.0020 = 0.001864$

Summing across all intervals:

$$\\sum \\left( S_x \\cdot {_5 f_x} \\right) = 0.023568 + 0.086064 + 0.118706 + 0.100568 + 0.049868 + 0.017064 + 0.001864 = 0.397692$$

Multiplying by $5$:

$$5 \\times \\sum \\left( S_x \\cdot {_5 f_x} \\right) = 5 \\times 0.397692 = 1.988460$$

Now multiply by the female birth proportion $p_f = 0.485437$:

$$NRR = 0.485437 \\times 1.988460 \\approx 0.965272 \\implies 0.9653$$

The Net Reproduction Rate is $0.9653$ surviving daughters per woman.

### Solution, step 3: Demographic Replacement Status and Lotka Dynamics
1. **Replacement Status**:
   Because $NRR = 0.9653 < 1.000$, the population is strictly **below replacement level**. Each cohort of mothers will be replaced by a cohort of surviving daughters that is approximately $3.47\\%$ smaller ($1 - 0.9653 = 0.0347$).
2. **Mean Length of Generation ($T$)**:
   The mean age of childbearing in the stationary population (mean length of generation $T$) is the weighted average age of mothers:
   $$T = \\frac{\\sum (x + 2.5) \\cdot S_x \\cdot {_5 f_x}}{\\sum S_x \\cdot {_5 f_x}}$$
   Evaluating the numerator with midpoints $17.5, 22.5, 27.5, 32.5, 37.5, 42.5, 47.5$:
   - $17.5 \\times 0.023568 = 0.412440$
   - $22.5 \\times 0.086064 = 1.936440$
   - $27.5 \\times 0.118706 = 3.264415$
   - $32.5 \\times 0.100568 = 3.268460$
   - $37.5 \\times 0.049868 = 1.870050$
   - $42.5 \\times 0.017064 = 0.725220$
   - $47.5 \\times 0.001864 = 0.088540$
   Sum of numerator: $11.565565$.
   $$T = \\frac{11.565565}{0.397692} \\approx 29.08 \\text{ years}$$
   The mean length of generation is $29.08$ years.
3. **Intrinsic Rate of Natural Increase ($r$)**:
   Using Lotka's classical logarithmic approximation:
   $$r \\approx \\frac{\\ln(NRR)}{T}$$
   $$\\ln(0.965272) = -0.035346$$
   $$r \\approx \\frac{-0.035346}{29.08} \\approx -0.001215 \\implies -0.1215\\% \\text{ per annum}$$

In the long run, once the age structure stabilizes, this population will contract naturally at an annual rate of $0.12\\%$ per year (a loss of $1.2$ persons per thousand annually) in the absence of net immigration.

## Fully worked question 3: Bongaarts Proximate Determinants Decomposition and SMAM Estimation

### Question
A national demographic and health survey (DHS) in a transitional country provides the following marital status distribution and fertility parameters for women of reproductive age:

1. **Census Marital Status Cross-Tabulation (Percentage Never-Married $s_x$ by Five-Year Age Group)**:
   - Ages 15–19: $s_{15} = 0.880$ (88.0% single)
   - Ages 20–24: $s_{20} = 0.520$ (52.0% single)
   - Ages 25–29: $s_{25} = 0.240$ (24.0% single)
   - Ages 30–34: $s_{30} = 0.110$ (11.0% single)
   - Ages 35–39: $s_{35} = 0.060$ (6.0% single)
   - Ages 40–44: $s_{40} = 0.040$ (4.0% single)
   - Ages 45–49: $s_{45} = 0.030$ (3.0% single)
   - Ages 50–54: $s_{50} = 0.025$ (2.5% single)
2. **Fertility and Family Planning Parameters**:
   - Total Fertility Rate: $TFR = 2.80$
   - Total Marital Fertility Rate: $TMFR = 4.20$
   - Contraceptive prevalence among married women: $u = 0.58$ (58.0%)
   - Average contraceptive method-mix efficacy: $e = 0.90$ (90.0%)
   - Total Abortion Rate: $TAR = 0.15$
   - Average duration of breastfeeding and postpartum amenorrhea: $i = 11.5 \\text{ months}$
   - Total Fecundity Rate: $TF = 15.3$

1. Compute Hajnal's Singulate Mean Age at Marriage ($SMAM$) for females.
2. Calculate the four Bongaarts proximate determinants indices: $C_m, C_c, C_a,$ and $C_i$.
3. Evaluate the Bongaarts multiplicative model $TFR_{\\text{model}} = C_m \\times C_c \\times C_a \\times C_i \\times TF$, compare with the observed $TFR = 2.80$, and determine which proximate determinant exerts the strongest inhibiting effect on provincial fertility.

### Solution, step 1: Compute Hajnal's SMAM
Following Hajnal's computational steps:
1. Person-years lived single before age 15:
   $$Y_{0-15} = 15.0$$
2. Sum of proportions single from age 15 to 49:
   $$\\sum_{k=1}^7 s_{15 + 5(k-1)} = 0.880 + 0.520 + 0.240 + 0.110 + 0.060 + 0.040 + 0.030 = 1.880$$
   Person-years lived single between 15 and 50:
   $$Y_{15-50} = 5 \\times 1.880 = 9.40$$
3. Total single person-years up to age 50:
   $$A = 15.0 + 9.40 = 24.40$$
4. Proportion remaining permanently single at age 50:
   $$s_{50\\text{-eff}} = \\frac{s_{45} + s_{50}}{2} = \\frac{0.030 + 0.025}{2} = 0.0275$$
   Person-years lived by permanent celibates:
   $$B = 50 \\times 0.0275 = 1.375$$
5. Net single person-years lived by those who marry before age 50:
   $$C = A - B = 24.40 - 1.375 = 23.025$$
6. Proportion who marry before age 50:
   $$D = 1.00 - s_{50\\text{-eff}} = 1.00 - 0.0275 = 0.9725$$
7. **Singulate Mean Age at Marriage**:
   $$SMAM = \\frac{C}{D} = \\frac{23.025}{0.9725} \\approx 23.676 \\implies 23.68 \\text{ years}$$

Women in this population marry on average at $23.68$ years of age, and approximately $97.25\\%$ marry before reaching age 50.

### Solution, step 2: Calculate Bongaarts' Proximate Determinant Indices
1. **Index of Marriage ($C_m$)**:
   $$C_m = \\frac{TFR}{TMFR} = \\frac{2.80}{4.20} \\approx 0.6667$$
   Non-marriage and delayed marriage reduce potential marital fertility by approximately $33.3\\%$.
2. **Index of Contraception ($C_c$)**:
   $$C_c = 1 - 1.08 \\cdot u \\cdot e = 1 - 1.08 \\times 0.58 \\times 0.90 = 1 - 0.56376 = 0.43624 \\approx 0.4362$$
   Contraceptive practice reduces fertility by $56.4\\%$.
3. **Index of Induced Abortion ($C_a$)**:
   $$C_a = \\frac{TFR}{TFR + 0.4 \\cdot (1 + u) \\cdot TAR} = \\frac{2.80}{2.80 + 0.4 \\times (1 + 0.58) \\times 0.15}$$
   Denominator term:
   $$0.4 \\times 1.58 \\times 0.15 = 0.0948$$
   $$C_a = \\frac{2.80}{2.80 + 0.0948} = \\frac{2.80}{2.8948} \\approx 0.9672$$
   Induced abortion reduces fertility by $3.3\\%$.
4. **Index of Postpartum Infecundability ($C_i$)**:
   Given $i = 11.5 \\text{ months}$:
   $$C_i = \\frac{20}{18.5 + i} = \\frac{20}{18.5 + 11.5} = \\frac{20}{30.0} \\approx 0.6667$$
   Lactational amenorrhea and extended breastfeeding reduce fertility by $33.3\\%$.

### Solution, step 3: Multiplicative Model Synthesis and Inhibiting Hierarchy
We evaluate the combined Bongaarts product:

$$TFR_{\\text{model}} = C_m \\times C_c \\times C_a \\times C_i \\times TF$$

$$TFR_{\\text{model}} = 0.6667 \\times 0.4362 \\times 0.9672 \\times 0.6667 \\times 15.3$$

Multiplying step by step:
- $C_m \\times C_c = 0.6667 \\times 0.4362 = 0.2908$
- $0.2908 \\times C_a = 0.2908 \\times 0.9672 = 0.2813$
- $0.2813 \\times C_i = 0.2813 \\times 0.6667 = 0.1875$
- $0.1875 \\times TF = 0.1875 \\times 15.3 \\approx 2.869 \\approx 2.87 \\text{ children per woman}$

The model estimate ($2.87$) closely reproduces the empirical Total Fertility Rate ($2.80$) within a $2.5\\%$ margin of error, demonstrating model fidelity.

**Hierarchical Inhibiting Diagnosis**:
To determine the relative strength of each determinant, we rank the indices by their departure from unity ($1.00 - C_k$):
1. **Contraception ($C_c = 0.4362$)**: Reduces potential fertility by **$56.38\\%$** — The single most powerful fertility inhibitor.
2. **Marriage / Delayed Nuptiality ($C_m = 0.6667$)**: Reduces potential fertility by **$33.33\\%$** — Second most powerful factor.
3. **Postpartum Infecundability ($C_i = 0.6667$)**: Reduces potential fertility by **$33.33\\%$** — Equal second factor.
4. **Induced Abortion ($C_a = 0.9672$)**: Reduces potential fertility by **$3.28\\%$** — Minor factor in this setting.

**Policy Synthesis**:
Contraception is the primary proximate mechanism suppressing fertility from biological fecundity ($15.3$) down to $2.80$. However, because $C_m = 0.67$ and $C_i = 0.67$, rising age at marriage and traditional breastfeeding customs provide substantial fertility suppression. If urbanization diminishes breastfeeding durations ($C_i$ rising toward 1.0) without a compensatory increase in contraceptive prevalence, fertility could paradoxically rise, highlighting the critical importance of integrated reproductive health planning.
"""

(OUT_DIR / "unit-5.md").write_text(u5_content, encoding="utf-8")
print(f"Unit 5: {prose_count(u5_content)} words")
