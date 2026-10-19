# Unit 6: Mathematical Models of Population Growth

Mathematical modeling of population growth is among the oldest and most intellectually rich branches of applied mathematics, dating back to Leonardo of Pisa (Fibonacci) in 1202, Thomas Robert Malthus in 1798, and Pierre-François Verhulst in 1838. In demography, mathematical growth models serve two distinct purposes: **deductive analytical modeling** (deriving the logical trajectory of population size and structural composition under explicit biological postulates) and **empirical graduation** (fitting functional curves to historical census series to enable intercensal interpolation and medium-term demographic forecasting). In this unit, we formalize the mathematics of discrete arithmetic, geometric, continuous exponential, and Verhulst-Pearl logistic growth models.

## 6.1 Discrete Linear and Arithmetic Growth Models

The simplest mathematical formulation of population growth assumes that a population expands by a constant, absolute number of individuals in each successive temporal unit.

### Mathematical Formulation
Let $P(t)$ denote the population size at time $t$, and let $P(0) = P_0$ denote the baseline population at time $t = 0$. The **Arithmetic (Linear) Growth Model** postulates a constant absolute annual increment $b$:

$$\frac{dP(t)}{dt} = b = \text{constant}$$

Integrating from $0$ to $t$:

$$P(t) = P_0 + b \cdot t$$

Given two census enumerations at times $t_1$ and $t_2$ ($t_2 > t_1$) with counts $P(t_1)$ and $P(t_2)$, the average annual absolute increment is:

$$b = \frac{P(t_2) - P(t_1)}{t_2 - t_1}$$

The arithmetic growth rate expressed as a percentage of the baseline population is:

$$r_{\text{arithmetic}} = \frac{b}{P_0} = \frac{P(t_2) - P(t_1)}{P(t_1) \cdot (t_2 - t_1)}$$

### Demographic Limitations of the Arithmetic Model
While arithmetic models are mathematically trivial and computationally convenient for short-term linear interpolation between closely spaced censuses (e.g., estimating population on July 1 of an intercensal year), they are demographically unrealistic for long-term modeling:
1. **Biological Implausibility**: Population growth is inherently biological: people produce offspring in proportion to their numbers. A constant absolute increment $b$ implies that as the population grows larger, each individual's average contribution to growth declines continuously ($b / P(t) \to 0$).
2. **Failure of Compounding**: The arithmetic model ignores the fundamental demographic reality that newborn individuals mature into parents who produce further offspring (the demographic multiplier effect).

## 6.2 Geometric Compounding Growth Models

Recognizing the multiplicative nature of biological reproduction, the geometric growth model incorporates discrete annual compounding, analogous to compound interest in financial mathematics.

### Mathematical Formulation
Assume that the population expands at a constant proportional rate $r_g$ per calendar year, compounded once at the conclusion of each annual cycle:

$$P(t) = P_0 (1 + r_g)^t$$

Given two historical censuses separated by $t$ years:

$$(1 + r_g)^t = \frac{P(t)}{P_0}$$

Taking the $t$-th root:

$$1 + r_g = \left( \frac{P(t)}{P_0} \right)^{1/t}$$

Solving for the **Geometric Annual Growth Rate ($r_g$)**:

$$r_g = \left( \frac{P(t)}{P_0} \right)^{1/t} - 1$$

Expressed as a percentage:

$$r_g(\%) = \left[ \left( \frac{P(t)}{P_0} \right)^{1/t} - 1 \right] \times 100$$

### Intercensal Interpolation under Geometric Growth
For any fractional time $t^* \in (t_1, t_2)$, the intercensal population is interpolated via:

$$P(t^*) = P(t_1) \left( \frac{P(t_2)}{P(t_1)} \right)^{\frac{t^* - t_1}{t_2 - t_1}}$$

Geometric compounding is widely utilized by national statistical bureaus for decennial census interpolation when vital events are published at discrete annual intervals.

## 6.3 Continuous Exponential Growth Models and Doubling Time

In biological reality, human births and deaths occur continuously around the clock every second of the day, rather than in discrete annual bursts. The continuous exponential growth model formalizes this continuous instantaneous compounding.

### The Differential Equation of Exponential Growth
Let the rate of change of population size be directly proportional to the current population size:

$$\frac{dP(t)}{dt} = r \cdot P(t)$$

where $r$ represents the **intrinsic instantaneous rate of natural increase** (the Malthusian parameter).
Separating variables:

$$\frac{1}{P(t)} \, dP = r \, dt$$

Integrating both sides from $t = 0$ (where $P(0) = P_0$) to time $t$:

$$\int_{P_0}^{P(t)} \frac{1}{P} \, dP = \int_0^t r \, dt$$

$$\ln\left( \frac{P(t)}{P_0} \right) = r \cdot t$$

Exponentiating both sides yields the classical **Continuous Exponential Growth Model**:

$$P(t) = P_0 \, e^{r t}$$

### Derivation of the Continuous Growth Rate
Given two census observations $P(t_1)$ and $P(t_2)$ separated by elapsed time $\Delta t = t_2 - t_1$:

$$e^{r \Delta t} = \frac{P(t_2)}{P(t_1)}$$

Taking the natural logarithm:

$$r \Delta t = \ln\left( \frac{P(t_2)}{P(t_1)} \right)$$

$$r = \frac{\ln[P(t_2) / P(t_1)]}{t_2 - t_1} = \frac{\ln P(t_2) - \ln P(t_1)}{\Delta t}$$

### Mathematical Derivation of Doubling Time ($T_d$)
The **Doubling Time ($T_d$)** is the precise time required for a population growing at constant exponential rate $r$ to double its initial size:

$$P(T_d) = 2 \cdot P_0$$

Substitute this into the exponential equation:

$$P_0 \, e^{r T_d} = 2 \cdot P_0$$

Divide both sides by $P_0$:

$$e^{r T_d} = 2$$

Taking the natural logarithm:

$$r \cdot T_d = \ln(2) \approx 0.693147$$

Solving for $T_d$:

$$T_d = \frac{\ln(2)}{r} = \frac{0.693147}{r}$$

If the growth rate is expressed as an annual percentage $r(\%) = 100 \cdot r$:

$$T_d = \frac{100 \cdot \ln(2)}{r(\%)} = \frac{69.31}{r(\%)} \approx \frac{70}{r(\%)}$$

This celebrated demographic approximation is known worldwide as the **Rule of 70**:
- A population growing at $r = 1.0\%$ per annum doubles in approximately $70 / 1 = 70$ years.
- A population expanding at $r = 2.0\%$ per annum doubles in $70 / 2 = 35$ years.
- At an explosive rate of $r = 3.5\%$ per annum (frequently observed in mid-20th-century developing nations), the population doubles in just $70 / 3.5 = 20$ years!

## 6.4 The Verhulst–Pearl Logistic Growth Model

Unconstrained exponential growth cannot continue indefinitely in a finite physical environment. As Thomas Malthus recognized, human populations eventually encounter resource, ecological, and environmental constraints. In 1838, the Belgian mathematician Pierre-François Verhulst introduced the **Logistic Model**, which Raymond Pearl and Lowell J. Reed rediscovered and popularized in 1920.

### Differential Formulation of Logistic Growth
Verhulst postulated that the per capita growth rate is not constant, but declines linearly as population size $P(t)$ approaches an asymptotic ceiling—the **Carrying Capacity ($K$)**:

$$\frac{1}{P} \frac{dP}{dt} = r \left( 1 - \frac{P}{K} \right)$$

Rearranging:

$$\frac{dP}{dt} = r P \left( \frac{K - P}{K} \right) = \frac{r}{K} P (K - P)$$

where:
- $r > 0$ is the intrinsic rate of growth in the absence of density-dependent competition.
- $K > 0$ is the environmental carrying capacity (asymptote of the population).
- The term $\left( 1 - \frac{P}{K} \right)$ represents the environmental resistance factor. When $P \ll K$, environmental resistance is near zero, and the population grows quasi-exponentially. As $P \to K$, environmental resistance approaches unity, halting growth.

### Analytical Solution of the Logistic Differential Equation
We solve the autonomous non-linear differential equation via separation of variables:

$$\frac{dP}{P(K - P)} = \frac{r}{K} \, dt$$

Using partial fraction decomposition:

$$\frac{1}{P(K - P)} = \frac{1}{K} \left[ \frac{1}{P} + \frac{1}{K - P} \right]$$

Substitute this into the equation:

$$\frac{1}{K} \left[ \frac{1}{P} + \frac{1}{K - P} \right] dP = \frac{r}{K} \, dt$$

Multiply both sides by $K$:

$$\left[ \frac{1}{P} + \frac{1}{K - P} \right] dP = r \, dt$$

Integrate both sides:

$$\int \left( \frac{1}{P} + \frac{1}{K - P} \right) dP = \int r \, dt$$

$$\ln(P) - \ln(K - P) = r t + C_0$$

$$\ln\left( \frac{P}{K - P} \right) = r t + C_0$$

Exponentiate both sides:

$$\frac{P(t)}{K - P(t)} = C \, e^{r t} \quad \text{where } C = e^{C_0}$$

At initial time $t = 0$:

$$\frac{P_0}{K - P_0} = C$$

Let $\beta = \frac{1}{C} = \frac{K - P_0}{P_0} = \frac{K}{P_0} - 1$. Then:

$$\frac{K - P(t)}{P(t)} = \beta \, e^{-r t}$$

$$\frac{K}{P(t)} - 1 = \beta \, e^{-r t}$$

$$\frac{K}{P(t)} = 1 + \beta \, e^{-r t}$$

Inverting yields the canonical **Verhulst–Pearl Logistic Growth Function**:

$$P(t) = \frac{K}{1 + \beta \, e^{-r t}}$$

### Mathematical Properties of the Logistic S-Curve
1. **Asymptotes**:
   - As $t \to -\infty$: $P(t) \to 0$.
   - As $t \to +\infty$: $P(t) \to K$.
2. **Point of Inflection ($P^*$)**:
   The point of maximum absolute growth rate ($\frac{d^2 P}{dt^2} = 0$) is found by differentiating $\frac{dP}{dt} = \frac{r}{K} (K P - P^2)$:
   $$\frac{d^2 P}{dt^2} = \frac{r}{K} (K - 2P) \frac{dP}{dt} = 0$$
   Since $\frac{dP}{dt} > 0$, the inflection point occurs strictly when:
   $$K - 2P = 0 \implies P^* = \frac{K}{2}$$
   The population grows most rapidly in absolute numbers when it reaches **exactly half of its carrying capacity**.
3. **Time of Inflection ($t^*$)**:
   Setting $P(t^*) = K/2$:
   $$\frac{K}{1 + \beta e^{-r t^*}} = \frac{K}{2} \implies 1 + \beta e^{-r t^*} = 2 \implies \beta e^{-r t^*} = 1$$
   $$e^{r t^*} = \beta \implies t^* = \frac{\ln \beta}{r}$$
4. **Symmetry**: The logistic curve is strictly symmetric about its inflection point $(t^*, K/2)$.

## 6.5 Fitting the Logistic Curve: The Pearl–Reed Three-Point Method

To calibrate the three parameters of the logistic curve ($K, \beta, r$) to historical census data, Raymond Pearl and Lowell Reed formulated the **Three-Point Method**.

### Mathematical Derivation of the Three-Point Formula
Select three equidistant census observations along the historical timeline:
- $P_0$ at time $t = 0$
- $P_1$ at time $t = h$
- $P_2$ at time $t = 2h$
where $h$ is the constant time interval between chosen censuses (e.g., $h = 20$ years).

The logistic equations at the three points are:
$$P_0 = \frac{K}{1 + \beta}$$
$$P_1 = \frac{K}{1 + \beta e^{-r h}}$$
$$P_2 = \frac{K}{1 + \beta e^{-2 r h}}$$

Invert each equation to isolate $\frac{1}{P}$:
$$\frac{1}{P_0} = \frac{1 + \beta}{K}$$
$$\frac{1}{P_1} = \frac{1 + \beta e^{-r h}}{K}$$
$$\frac{1}{P_2} = \frac{1 + \beta e^{-2 r h}}{K}$$

Let $u = e^{-r h}$. Taking differences between adjacent reciprocals:
$$\Delta_1 = \frac{1}{P_0} - \frac{1}{P_1} = \frac{\beta (1 - u)}{K}$$
$$\Delta_2 = \frac{1}{P_1} - \frac{1}{P_2} = \frac{\beta u (1 - u)}{K}$$

Dividing $\Delta_2$ by $\Delta_1$:
$$\frac{\Delta_2}{\Delta_1} = \frac{\frac{1}{P_1} - \frac{1}{P_2}}{\frac{1}{P_0} - \frac{1}{P_1}} = u = e^{-r h}$$

Since $u = e^{-r h}$, we solve directly for the growth parameter $r$:
$$r = -\frac{1}{h} \ln(u) = -\frac{1}{h} \ln\left( \frac{\frac{1}{P_1} - \frac{1}{P_2}}{\frac{1}{P_0} - \frac{1}{P_1}} \right)$$

Once $u$ is known, Pearl and Reed established that the carrying capacity $K$ is given by:

$$K = \frac{2 P_0 P_1 P_2 - P_1^2 (P_0 + P_2)}{P_0 P_2 - P_1^2}$$

Once $K$ is determined, $\beta$ is computed directly from the initial condition:

$$\beta = \frac{K - P_0}{P_0}$$

This three-point algorithm provides an analytical solution that passes through all three benchmark census counts.


### Historical Perspectives on Demographic Growth: Malthusian vs Boserupian Paradigms
Mathematical models of population growth do not operate in an intellectual vacuum; they reflect fundamental philosophical and economic debates regarding the relationship between human reproduction, technological innovation, and finite planetary resources.

#### The Malthusian Classical Trap
In 1798, the English political economist Thomas Robert Malthus published his celebrated Essay on the Principle of Population, formulating the first quantitative law of demographic growth:
1. Population, when unchecked, increases in a geometrical ratio (exponential progression: 1, 2, 4, 8, 16, 32...).
2. Subsistence and food production increases only in an arithmetical ratio (linear progression: 1, 2, 3, 4, 5, 6...).

Because exponential growth inevitably outstrips linear growth, Malthus reasoned that population size must inevitably collide with the agricultural carrying capacity of the land. When this collision occurs, natural equilibrium is restored through two mechanisms:
- **Preventive Checks**: Voluntary behavioral reductions in the birth rate, primarily achieved through moral restraint, delayed marriage (celibacy), and family limitation.
- **Positive Checks**: Involuntary increases in the death rate caused by severe malnutrition, famine, infectious epidemic waves, and resource-driven warfare.

In mathematical terms, Malthus envisioned human society as trapped in a perpetual homeostatic cycle where any temporary improvement in living standards merely stimulates population expansion, which in turn drives wages back down to the bare biological subsistence level—the classical Malthusian Trap.

#### The Boserupian Technological Counter-Theory
In 1965, the Danish agricultural economist Ester Boserup formulated a profound counter-thesis to Malthusian determinism in her seminal work The Conditions of Agricultural Growth. Whereas Malthus viewed agricultural supply as an exogenous, autonomous ceiling that constrains demographic growth from above, Boserup demonstrated that population pressure serves as the primary endogenous catalyst that stimulates agricultural technological innovation and agricultural intensification.

Boserup traced the historical evolution of farming systems through five successive stages of land use intensity: forest fallow (twenty-year fallow cycles), bush fallow (six to eight-year cycles), short fallow (one to two-year cycles), annual cropping, and multi-cropping (producing two or three harvests per year from the same irrigated plot). Under low population densities, primitive slash-and-burn farming yields the highest output per hour of human labor, so farmers have no economic incentive to adopt labor-intensive plowing or irrigation. However, as population growth increases demographic density, the resulting land scarcity forces agriculturalists to invent and adopt intensive techniques: stone terracing, animal-drawn steel plows, organic fertilization, complex canal irrigation, and high-yield crop varieties.

In mathematical modeling, Boserup's insight transforms the carrying capacity K from a fixed, immutable ceiling into a dynamic, endogenous state variable that expands in response to population pressure:

$$\frac{dK}{dt} = \gamma \cdot \frac{dP}{dt}$$

When human intellectual capital and technological innovation expand faster than population numbers (as occurred during the Industrial Revolution and the mid-twentieth-century Green Revolution developed by Norman Borlaug), output per person increases continuously alongside expanding populations, permanently breaking the Malthusian trap.


### Multi-Stage Logistic Transitions and Demographic Multipliers
While the classical Verhulst logistic curve assumes a single, unchanging carrying capacity K, real-world human populations frequently experience multiple successive carrying capacity plateaus associated with technological and agricultural revolutions. In 1990, the mathematical physicist Cesare Marchetti demonstrated that human historical expansion can be modeled as a sequence of nested, overlapping logistic S-curves, termed **Multi-Stage Logistic Growth**.

In the first stage, traditional hunter-gatherer foraging limits population to an initial low ceiling K_1. The Neolithic agricultural revolution introduces sedentary farming, shifting the ecological carrying capacity to K_2. Millennia later, the Industrial and Scientific Revolutions unlock fossil energy, synthetic nitrogen fertilizers (the Haber–Bosch process), and modern medicine, elevating carrying capacity to K_3.

To quantify the total growth achieved during a demographic transition, demographers compute the **Demographic Multiplier (M_D)**:

$$M_D = \frac{P_{\text{post-transition}}}{P_{\text{pre-transition}}}$$

In Western European nations (such as the United Kingdom, France, and Sweden), the demographic multiplier of the eighteenth- and nineteenth-century transition was approximately 3.0 to 4.5: populations expanded by three- to four-fold between the onset of mortality decline and the final stabilization of fertility. However, in twentieth-century developing nations (such as Egypt, Mexico, Bangladesh, and the Philippines), where modern antibiotics, DDT malaria eradication, and clean water infrastructure were imported rapidly while fertility remained elevated for decades, the demographic multiplier reached 7.0 to 10.0! Understanding the magnitude of the demographic multiplier is essential for designing sustainable urban housing, national electrical grids, and water sanitation systems.


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

## Fully worked question 1: Comparative Growth Modeling: Arithmetic, Geometric, and Continuous Exponential

### Question
A national statistical bureau evaluates demographic expansion across a developing nation based on two decennial censuses:
- Census 1 (April 1, 2010): $P_{2010} = 40{,}000{,}000$ inhabitants
- Census 2 (April 1, 2020): $P_{2020} = 50{,}000{,}000$ inhabitants
The elapsed time between the two enumerations is exactly $\Delta t = 10.0$ years.

1. Calculate the annual arithmetic absolute increment $b$ and the annual arithmetic growth rate $r_{\text{arith}}$.
2. Calculate the discrete geometric annual compounding rate $r_{\text{geom}}$ and the continuous exponential instantaneous rate $r_{\text{cont}}$.
3. Project the national population to April 1, 2035 ($t = 25$ years from 2010) under all three growth regimes, and compute the continuous doubling time $T_d$.

### Solution, step 1: Arithmetic Growth Parameters
The elapsed time is $\Delta t = 10.0$ years.
The absolute population increase over the decade is:
$$\Delta P = P_{2020} - P_{2010} = 50{,}000{,}000 - 40{,}000{,}000 = 10{,}000{,}000$$

The average annual arithmetic increment is:
$$b = \frac{\Delta P}{\Delta t} = \frac{10{,}000{,}000}{10.0} = 1{,}000{,}000 \text{ persons per year}$$

The arithmetic growth rate relative to the 2010 baseline is:
$$r_{\text{arith}} = \frac{b}{P_{2010}} \times 100 = \frac{1{,}000{,}000}{40{,}000{,}000} \times 100 = 2.500\% \text{ per annum}$$

### Solution, step 2: Geometric and Continuous Growth Rates
1. **Geometric Compounding Rate ($r_{\text{geom}}$)**:
   $$r_{\text{geom}} = \left( \frac{P_{2020}}{P_{2010}} \right)^{1/10} - 1 = \left( \frac{50{,}000{,}000}{40{,}000{,}000} \right)^{0.10} - 1 = (1.25)^{0.10} - 1$$
   Computing $(1.25)^{0.10}$:
   $$\ln(1.25) = 0.22314355$$
   $$0.10 \times 0.22314355 = 0.022314355$$
   $$e^{0.022314355} \approx 1.022565$$
   $$r_{\text{geom}} = 1.022565 - 1 = 0.022565 \implies 2.2565\% \text{ per annum}$$

2. **Continuous Exponential Rate ($r_{\text{cont}}$)**:
   $$r_{\text{cont}} = \frac{\ln(P_{2020} / P_{2010})}{\Delta t} = \frac{\ln(1.25)}{10.0} = \frac{0.22314355}{10.0} = 0.02231436 \implies 2.2314\% \text{ per annum}$$

Notice the mathematical hierarchy of rates:
$$r_{\text{cont}} (2.2314\%) < r_{\text{geom}} (2.2565\%) < r_{\text{arith}} (2.500\%)$$
This hierarchy universally holds because continuous compounding generates the greatest compounding efficiency, requiring the smallest nominal rate to achieve the same decennial expansion.

### Solution, step 3: Demographic Projections to 2035 ($t = 25$ years) and Doubling Time
The elapsed time from the 2010 baseline to 2035 is $t = 25$ years.

1. **Under Arithmetic Growth**:
   $$P_{\text{arith}}(25) = P_{2010} + 25 \times b = 40{,}000{,}000 + 25 \times 1{,}000{,}000 = 65{,}000{,}000$$

2. **Under Geometric Compounding Growth**:
   $$P_{\text{geom}}(25) = P_{2010} (1 + r_{\text{geom}})^{25} = 40{,}000{,}000 \times (1.022565)^{25}$$
   $$(1.022565)^{25} = (1.25)^{2.5} = (1.25)^2 \times \sqrt{1.25} = 1.5625 \times 1.118034 = 1.746928$$
   $$P_{\text{geom}}(25) = 40{,}000{,}000 \times 1.746928 = 69{,}877{,}123$$

3. **Under Continuous Exponential Growth**:
   $$P_{\text{cont}}(25) = P_{2010} \, e^{25 \times 0.02231436} = 40{,}000{,}000 \, e^{0.5578589} = 40{,}000{,}000 \times 1.746928 = 69{,}877{,}123$$
   *(Geometric and continuous exponential compounding yield identical projections when evaluated from the same empirical endpoints).*

4. **Continuous Doubling Time ($T_d$)**:
   $$T_d = \frac{\ln(2)}{r_{\text{cont}}} = \frac{0.69314718}{0.02231436} \approx 31.06 \text{ years}$$

At the prevailing continuous growth rate of $2.23\%$, the national population will double from $40$ million to $80$ million in approximately $31.1$ years (around the year 2041).


### Non-Linear Generalizations: The Gompertz and von Bertalanffy Growth Models
While the Verhulst–Pearl logistic model assumes exact point-symmetry about its inflection point $K/2$, empirical demographic growth trajectories often exhibit marked asymmetry: human and economic expansions frequently accelerate rapidly during early phases and experience prolonged, gradual deceleration as carrying capacities are approached, or vice versa. To model asymmetric growth, mathematical demographers deploy generalized growth curves.

#### 1. The Gompertz Growth Model
Originally formulated by Benjamin Gompertz in 1825 for actuarial mortality, the Gompertz curve was adapted by demographers and econometricians to model population growth where the proportional growth rate declines exponentially over time:

$$\frac{d \ln P}{dt} = r \, e^{-\alpha t}$$

Integrating this differential relationship yields the double-exponential **Gompertz Growth Function**:

$$P(t) = K \, \exp\left( -b \, e^{-\alpha t} \right) = K \, a^{b^t}$$

where:
- $K$ is the asymptotic carrying capacity.
- $\alpha > 0$ governs the rate of growth deceleration.
- $b > 0$ is a positioning parameter related to the initial population $P_0 = K e^{-b}$.

The Gompertz curve possesses a fundamentally asymmetric inflection point:
$$\frac{d^2 P}{dt^2} = 0 \implies P^* = \frac{K}{e} \approx 0.3679 \, K$$
Unlike the symmetric logistic curve whose inflection point occurs at fifty percent of carrying capacity ($0.50 K$), the Gompertz inflection point occurs earlier, at approximately thirty-seven percent ($1/e$) of the asymptote. This makes the Gompertz model exceptionally well-suited for modeling the adoption of modern family planning techniques, urban population surges, and life expectancy expansions.

#### 2. The von Bertalanffy Growth Curve
In bio-demography and ecological population dynamics, Ludwig von Bertalanffy (1938) derived a growth model based on the physiological balance between anabolic processes (mass synthesis proportional to surface area or metabolic rate $P^m$) and catabolic breakdown (tissue loss proportional to total body mass $P$):

$$\frac{dP}{dt} = \eta P^m - \gamma P$$

When $m = 2/3$ (representing surface-area scaling in organismal biology), the analytical solution is:

$$P(t) = K \left( 1 - \beta \, e^{-k t} \right)^3$$

In spatial human demography, this model captures the growth of enclosed municipal systems where physical infrastructure development scales with municipal area while maintenance costs scale with total population.

### Rhodes' Differential Method of Logistic Fitting
In 1940, E. C. Rhodes developed an alternative technique to fit the logistic curve that utilizes all available historical census points rather than relying upon three arbitrary equidistant points.

Recall the logistic differential equation $\frac{1}{P} \frac{dP}{dt} = r - \frac{r}{K} P$. Rhodes noted that this can be expressed as a simple linear regression model:

$$y = A - B \cdot x$$

where $y = \frac{1}{P} \frac{dP}{dt}$ is the instantaneous relative growth rate, $x = P$ is the population size, the intercept is $A = r$, and the slope is $B = r / K$.

In empirical census data, the continuous derivative $\frac{dP}{dt}$ is approximated by the central difference quotient between consecutive censuses:

$$\left( \frac{dP}{dt} \right)_t \approx \frac{P_{t+1} - P_{t-1}}{t_{t+1} - t_{t-1}}$$

and the corresponding population $P$ is the mid-interval value $P_t$. By running ordinary least squares (OLS) regression of the empirical relative growth rates on population sizes across ten or more historical censuses, demographers obtain robust, noise-dampened estimates of both $r$ and $K = A / B$. This regression-based approach avoids the sensitivity to outlier years inherent in the classical three-point method.


### Numerical Calibration of Non-Linear Logistic Models via the Gauss–Newton Algorithm
While the classical Pearl–Reed three-point method provides an exact algebraic solution that passes through three chosen points, it completely discards information from all other available census years. To calibrate the logistic model P(t) = K / (1 + beta e^{-rt}) against a full longitudinal sequence of m historical censuses (t_i, P_i) for i = 1, 2, ..., m, mathematical demographers deploy non-linear least squares (NLLS) optimization.

#### Objective Function Formulation
The residual sum of squares (RSS) to be minimized across all m census observations is:

$$S(K, \beta, r) = \sum_{i=1}^m \left[ P_i - \frac{K}{1 + \beta \, e^{-r t_i}} 
\right]^2$$

Because the logistic parameters appear non-linearly inside the denominator and exponent, the first-order partial derivative equations (the normal equations) cannot be solved analytically. Demographers deploy the iterative **Gauss–Newton Algorithm** (or Levenberg–Marquardt dampening):

1. **Parameter Vector and Residuals**:
   Let theta = (K, beta, r)^T be the parameter vector. The residual vector is r(theta) with components r_i(theta) = P_i - f(t_i; theta).
2. **Jacobian Gradient Matrix (J)**:
   The elements of the m x 3 Jacobian matrix J are the partial derivatives of the model function with respect to the parameters evaluated at census year t_i:
   - Partial with respect to K:
     $$\frac{\partial f}{\partial K} = \frac{1}{1 + \beta e^{-r t_i}}$$
   - Partial with respect to beta:
     $$\frac{\partial f}{\partial \beta} = -\frac{K e^{-r t_i}}{(1 + \beta e^{-r t_i})^2}$$
   - Partial with respect to r:
     $$\frac{\partial f}{\partial r} = \frac{K \beta t_i e^{-r t_i}}{(1 + \beta e^{-r t_i})^2}$$
3. **Iterative Parameter Updating**:
   At each iteration step k, the parameter update vector delta_theta is obtained by solving the linear normal system:
   $$\mathbf{J}^T \mathbf{J} \, \Delta \boldsymbol{\theta} = \mathbf{J}^T \mathbf{r}(\boldsymbol{\theta}^{(k)})$$
   $$\boldsymbol{\theta}^{(k+1)} = \boldsymbol{\theta}^{(k)} + \Delta \boldsymbol{\theta}$$

Iterating until convergence (when ||delta_theta|| < 10^{-6}) yields the unique maximum likelihood parameter estimates under Gaussian measurement errors. Furthermore, the inverse Fisher information matrix (J^T J)^{-1} provides the asymptotic covariance matrix of the estimated carrying capacity K and growth rate r, allowing demographers to compute formal statistical standard errors for long-term population asymptotes.

## Fully worked question 2: Pearl–Reed Three-Point Calibration of the Logistic Growth Function

### Question
An ecological demographer fits a Verhulst-Pearl logistic growth model to a municipal population series enumerated across three equidistant census intervals spaced $h = 20$ years apart:
- Year 1980 ($t = 0$): $P_0 = 100{,}000$ inhabitants
- Year 2000 ($t = 20$): $P_1 = 160{,}000$ inhabitants
- Year 2020 ($t = 40$): $P_2 = 220{,}000$ inhabitants

1. Apply the Pearl-Reed three-point algorithm to calculate the environmental carrying capacity $K$ of the municipality.
2. Determine the initial scaling parameter $\beta$ and the intrinsic growth rate parameter $r$.
3. Formulate the complete mathematical logistic equation $P(t)$, determine the population and calendar year at the inflection point, and forecast the municipal population for Year 2040 ($t = 60$).

### Solution, step 1: Calculate the Carrying Capacity ($K$)
The Pearl-Reed formula for carrying capacity is:

$$K = \frac{2 P_0 P_1 P_2 - P_1^2 (P_0 + P_2)}{P_0 P_2 - P_1^2}$$

We evaluate each term systematically:
1. First numerator term:
   $$2 P_0 P_1 P_2 = 2 \times 100{,}000 \times 160{,}000 \times 220{,}000 = 7.04 \times 10^{15}$$
2. Second numerator term:
   $$P_1^2 = (160{,}000)^2 = 2.56 \times 10^{10}$$
   $$P_0 + P_2 = 100{,}000 + 220{,}000 = 320{,}000$$
   $$P_1^2 (P_0 + P_2) = 2.56 \times 10^{10} \times 320{,}000 = 8.192 \times 10^{15}$$
3. Total numerator:
   $$\text{Num} = 7.04 \times 10^{15} - 8.192 \times 10^{15} = -1.152 \times 10^{15}$$
4. Denominator:
   $$P_0 P_2 = 100{,}000 \times 220{,}000 = 2.20 \times 10^{10}$$
   $$P_1^2 = (160{,}000)^2 = 2.56 \times 10^{10}$$
   $$\text{Denom} = P_0 P_2 - P_1^2 = 2.20 \times 10^{10} - 2.56 \times 10^{10} = -0.36 \times 10^{10} = -3.60 \times 10^9$$

Dividing numerator by denominator:

$$K = \frac{-1.152 \times 10^{15}}{-3.60 \times 10^9} = \frac{1.152 \times 10^{15}}{3.60 \times 10^9} = 320{,}000$$

The carrying capacity of the municipality is $K = 320{,}000$ inhabitants.

### Solution, step 2: Calculate Parameters $\beta$ and $r$
1. **The Parameter $\beta$**:
   $$\beta = \frac{K - P_0}{P_0} = \frac{320{,}000 - 100{,}000}{100{,}000} = \frac{220{,}000}{100{,}000} = 2.200$$

2. **The Intrinsic Growth Rate $r$**:
   We evaluate the reciprocal ratio $u = e^{-r h}$:
   $$\frac{1}{P_0} = \frac{1}{100{,}000} = 1.000 \times 10^{-5}$$
   $$\frac{1}{P_1} = \frac{1}{160{,}000} = 0.625 \times 10^{-5}$$
   $$\frac{1}{P_2} = \frac{1}{220{,}000} \approx 0.454545 \times 10^{-5}$$

   $$\Delta_1 = \frac{1}{P_0} - \frac{1}{P_1} = (1.000 - 0.625) \times 10^{-5} = 0.375 \times 10^{-5}$$
   $$\Delta_2 = \frac{1}{P_1} - \frac{1}{P_2} = (0.625 - 0.454545) \times 10^{-5} = 0.170455 \times 10^{-5}$$

   $$u = e^{-20 r} = \frac{\Delta_2}{\Delta_1} = \frac{0.170455 \times 10^{-5}}{0.375 \times 10^{-5}} \approx 0.454547$$

   Taking the natural logarithm:
   $$\ln(u) = \ln(0.454547) = -0.788454$$
   $$-20 r = -0.788454 \implies r = \frac{0.788454}{20} = 0.039423 \implies 3.942\% \text{ per annum}$$

### Solution, step 3: Complete Logistic Equation, Inflection Point, and 2040 Projection
1. **The Calibrated Logistic Model**:
   $$P(t) = \frac{320{,}000}{1 + 2.200 \, e^{-0.039423 \, t}}$$
   where $t$ is years elapsed since 1980 ($t = \text{Year} - 1980$).

2. **The Inflection Point**:
   - The population at the inflection point is exactly half the carrying capacity:
     $$P^* = \frac{K}{2} = \frac{320{,}000}{2} = 160{,}000 \text{ inhabitants}$$
   - Notice that $P_1 = 160{,}000$ at Year 2000! Therefore, the inflection point occurred **exactly in the Year 2000** ($t^* = 20$).
   - Check via formula: $t^* = \frac{\ln \beta}{r} = \frac{\ln(2.200)}{0.039423} = \frac{0.788457}{0.039423} = 20.00 \text{ years}$.
   At Year 2000, municipal growth reached its maximum velocity of:
   $$\left( \frac{dP}{dt} \right)_{\text{max}} = \frac{r K}{4} = \frac{0.039423 \times 320{,}000}{4} = 3{,}153.8 \text{ persons per year}$$

3. **Forecast for Year 2040 ($t = 60$)**:
   $$-0.039423 \times 60 = -2.36538$$
   $$e^{-2.36538} = 0.093913$$
   $$1 + \beta e^{-r t} = 1 + 2.200 \times 0.093913 = 1 + 0.206609 = 1.206609$$
   $$P(60) = \frac{320{,}000}{1.206609} \approx 265{,}206 \text{ inhabitants}$$

**Demographic Synthesis**:
Between 1980 and 2000, the municipal population expanded by $60{,}000$ inhabitants ($100k \to 160k$). Between 2000 and 2020, growth slowed to $60{,}000$ ($160k \to 220k$). Between 2020 and 2040, as density-dependent constraints intensify, growth decelerates further to $45{,}206$ ($220k \to 265{,}206$), approaching the ultimate ceiling of $320{,}000$.


### Stochastic Population Dynamics and the Allee Effect
While deterministic differential equations like the Verhulst–Pearl logistic model provide smooth, predictable trajectories, real-world demographic populations are subjected to random environmental turbulence, economic crises, epidemics, and stochastic fluctuations in birth and death counts.

#### The Stochastic Logistic Model (Itô Calculus Formulation)
To incorporate continuous environmental randomness, mathematical demographers formulate the stochastic logistic differential equation driven by a standard Brownian motion (Wiener process) W(t):

$$dP(t) = r P(t) \left( 1 - \frac{P(t)}{K} 
\right) dt + \sigma P(t) \, dW(t)$$

where:
- sigma > 0 represents the environmental volatility parameter.
- dW(t) satisfies the standard Gaussian increment properties: E[dW(t)] = 0 and E[(dW(t))^2] = dt.

By applying Itô's Lemma and solving the stationary Fokker–Planck (Kolmogorov forward) equation, demographers derive the long-term stationary probability density function p(P) of population size. When sigma^2 < 2r, the population fluctuates persistently around an effective carrying capacity slightly below the deterministic ceiling K. However, if environmental volatility exceeds the intrinsic growth rate (sigma^2 > 2r), the population faces a strictly positive probability of **stochastic extinction** within finite time.

#### The Allee Effect and Minimum Critical Density Thresholds
In 1931, the ecologist Warder Clyde Allee discovered that the assumption of monotonically declining per capita growth rate fails at very low population densities. In depleted populations, individuals experience severe difficulty finding reproductive mates, maintaining social cohesion, achieving cooperative defense, and avoiding inbreeding depression. This phenomenon is known as the **Allee Effect** (depensation).

To model demographic depensation, the logistic equation is modified by introducing a critical minimum density threshold A > 0 (where 0 < A < K):

$$\frac{dP}{dt} = r P \left( \frac{P}{A} - 1 
\right) \left( 1 - \frac{P}{K} 
\right)$$

The dynamical behavior of this non-linear cubic system reveals profound topological bifurcation:
1. **If P > A**: The term (P/A - 1) is positive, and the population grows toward the carrying capacity K.
2. **If P = A**: The system is at an unstable repelling equilibrium.
3. **If P < A**: The term (P/A - 1) is negative, causing dP/dt < 0. The population suffers negative growth and spirals catastrophically downward into the **extinction vortex** (P -> 0).

In regional human demography, strong Allee dynamics are observed in remote rural villages and isolated island communities: when young adult out-migration reduces village populations below a critical threshold, local schools and maternity clinics close, local marriage markets collapse, and the community undergoes terminal depopulation.


### Empirical Ecological Validation: Raymond Pearl's Drosophila Laboratory Experiments
In the 1920s, the biologist Raymond Pearl and his colleagues at Johns Hopkins University sought empirical experimental verification of the Verhulst logistic law under strictly controlled biological laboratory conditions. Pearl recognized that testing mathematical carrying capacities in human populations is inherently complicated by technological innovations, international trade, agricultural breakthroughs, and institutional changes that dynamically alter carrying capacities over time.

To isolate the pure biological mechanisms of logistic growth, Pearl designed controlled laboratory experiments using populations of the common fruit fly, *Drosophila melanogaster*. Fruit flies were introduced into standardized glass culture bottles containing a fixed, unreplenished quantity of nutrient agar medium (banana yeast agar) maintained at a constant temperature of twenty-five degrees Celsius. Starting with an initial breeding pair (P_0 = 2), Pearl recorded census counts of adult flies every three days over a forty-day period until the population stabilized and ultimately declined.

Pearl's experimental results provided a breathtaking confirmation of the logistic S-curve:
1. **Initial Exponential Phase (Days 0 to 12)**: At low fly densities, food and space were effectively infinite. Mortality was minimal, and the fly population expanded exponentially at a constant intrinsic rate r.
2. **Inflection Point (Day 16)**: At approximately sixteen days, corresponding to half the carrying capacity of the culture bottle (P ~ K/2 ~ 450 flies), the rate of absolute daily increase reached its peak.
3. **Deceleration and Saturation (Days 18 to 32)**: As adult fly density escalated, competition for space and egg-laying surfaces intensified. Female fecundity declined sharply: crowded female flies laid fewer eggs per day, and larval competition in the agar substrate caused high juvenile mortality. The population smoothly decelerated, asymptotically plateauing at an environmental carrying capacity of approximately K ~ 950 adult flies.

Pearl subsequently fitted the logistic equation to historical human census series for the United States, France, England and Wales, and Algeria. While the logistic curve fitted 19th-century counts with remarkable mathematical precision, Pearl's subsequent projections for the mid-20th century substantially underestimated actual population expansion. Pearl projected that the United States population would asymptotically plateau at K = 197 million people around the year 2000. In reality, the US population exceeded 280 million by 2000!

This historic divergence highlights the fundamental boundary between bio-ecology and human demography: whereas fruit flies cannot alter the dimensions or nutrient content of their glass bottle, human beings continuously reinvent their ecological niche through chemical fertilizers, high-yield seed hybridization, vertical urban architectural construction, and international commercial supply chains, transforming K from an ecological prison into an expanding technological horizon.

## Fully worked question 3: Carrying Capacity Sensitivity and Velocity Analysis in Logistic Growth

### Question
A regional planning authority models the growth of an industrial metropolis under ecological zoning limits. The urban population dynamics satisfy the differential logistic law:

$$\frac{dP}{dt} = 0.05 \, P \left( 1 - \frac{P}{2{,}000{,}000} \right)$$

where $P(t)$ is population size and $t$ is measured in years. The metropolis currently has an enumerated population of $P(0) = 500{,}000$ inhabitants.

1. Identify the intrinsic growth rate $r$ and carrying capacity $K$. Calculate the current instantaneous rate of population growth in persons per year ($\frac{dP}{dt}$ at $P = 500{,}000$).
2. Determine the population size and calendar time at which the metropolis will experience its absolute peak growth velocity. Compute this maximum growth velocity.
3. Solve for the exact time $T_{90}$ required for the metropolitan population to reach $90\%$ of its carrying capacity ($P = 1{,}800{,}000$).

### Solution, step 1: Model Identification and Current Growth Velocity
From the differential equation $\frac{dP}{dt} = 0.05 P \left( 1 - \frac{P}{2{,}000{,}000} \right)$:
- Intrinsic growth rate: $r = 0.05$ ($5.0\%$ per annum)
- Environmental carrying capacity: $K = 2{,}000{,}000$ inhabitants

At current population $P(0) = 500{,}000$:
$$\frac{dP}{dt} = 0.05 \times 500{,}000 \times \left( 1 - \frac{500{,}000}{2{,}000{,}000} \right) = 25{,}000 \times (1 - 0.25) = 25{,}000 \times 0.75 = 18{,}750 \text{ persons per year}$$

The current growth velocity is $18{,}750$ additional residents per year.

### Solution, step 2: Maximum Growth Velocity and Inflection Dynamics
By the fundamental theorem of logistic growth, the growth rate $\frac{dP}{dt}$ is a quadratic function of $P$:
$$g(P) = r P - \frac{r}{K} P^2$$
The vertex of this downward-opening parabola occurs at:
$$P^* = \frac{K}{2} = \frac{2{,}000{,}000}{2} = 1{,}000{,}000 \text{ inhabitants}$$

The maximum growth velocity is:
$$\left( \frac{dP}{dt} \right)_{\text{max}} = \frac{r K}{4} = \frac{0.05 \times 2{,}000{,}000}{4} = \frac{100{,}000}{4} = 25{,}000 \text{ persons per year}$$

To find the time $t^*$ when this maximum velocity is reached, we evaluate the logistic solution:
$$\beta = \frac{K - P_0}{P_0} = \frac{2{,}000{,}000 - 500{,}000}{500{,}000} = \frac{1{,}500{,}000}{500{,}000} = 3.0$$

Setting $P(t^*) = K/2 = 1{,}000{,}000$:
$$t^* = \frac{\ln \beta}{r} = \frac{\ln(3.0)}{0.05} = \frac{1.098612}{0.05} = 21.972 \approx 21.97 \text{ years}$$

The metropolis will experience its peak growth velocity in approximately $22.0$ years, expanding by $25{,}000$ residents annually.

### Solution, step 3: Time Required to Reach 90% of Carrying Capacity
We set $P(T_{90}) = 0.90 \times K = 1{,}800{,}000$.
From the linear logit form of the logistic solution:
$$\frac{K - P(t)}{P(t)} = \beta \, e^{-r t}$$

Substitute $P = 0.90 K$:
$$\frac{K - 0.90 K}{0.90 K} = \frac{0.10 K}{0.90 K} = \frac{1}{9} = \beta \, e^{-r T_{90}}$$

Substitute $\beta = 3.0$ and $r = 0.05$:
$$\frac{1}{9} = 3.0 \, e^{-0.05 T_{90}}$$
$$e^{-0.05 T_{90}} = \frac{1}{27}$$
$$e^{0.05 T_{90}} = 27$$

Taking the natural logarithm:
$$0.05 \, T_{90} = \ln(27) = \ln(3^3) = 3 \cdot \ln(3) = 3 \times 1.098612 = 3.295837$$

Solving for $T_{90}$:
$$T_{90} = \frac{3.295837}{0.05} = 65.9167 \approx 65.92 \text{ years}$$

**Planning Synthesis**:
The metropolis will reach $90\%$ of its carrying capacity ($1.8$ million residents) in approximately $65.9$ years. Growth proceeds in three distinct phases:
1. Years 0 to 22: Accelerating growth, with annual increments expanding from $18{,}750$ to the peak of $25{,}000$.
2. Years 22 to 66: Decelerating growth, as land scarcity, traffic congestion, and zoning restrictions dampen per capita expansion.
3. Post Year 66: Asymptotic plateauing toward the carrying capacity limit of $2{,}000{,}000$.
