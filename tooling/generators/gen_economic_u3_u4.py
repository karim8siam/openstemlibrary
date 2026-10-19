#!/usr/bin/env python3
"""
Generate Units 3 and 4 for Economic Statistics (Stat H-204 / Stat H-210)
"""
import re
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-economic-statistics")
OUT_DIR.mkdir(parents=True, exist_ok=True)

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

# ==========================================
# UNIT 3: TIME SERIES ANALYSIS: DECOMPOSITION MODELS & SECULAR TREND ESTIMATION
# ==========================================

u3_content = """# Unit 3: Time Series Analysis: Decomposition Models & Secular Trend Estimation

## Theoretical Foundations of Economic Time Series

An economic time series consists of an ordered sequence of quantitative observations recorded at discrete, uniformly spaced calendar intervals—such as daily exchange rates, monthly inflation rates, quarterly gross domestic product figures, or annual agricultural harvest totals. Unlike cross-sectional datasets where observational units are drawn independently from a population at a single fixed instant in time, time series data exhibit intrinsic chronological ordering, temporal persistence, serial auto-correlation, and dynamic feedback mechanisms.

In statistical economics, the classical approach to time series modeling rests on the premise that an observed aggregate macroeconomic or microeconomic sequence represents the mathematical composition of four distinct, unobservable latent components operating across differing temporal frequencies and causal mechanisms:

1. **Secular Trend ($T_t$)**: The smooth, long-term, underlying directional movement of the series over extended horizons spanning decades or generations. Secular trends reflect fundamental structural evolutions in an economy—such as sustained demographic growth, persistent capital accumulation, structural technological innovations, expanding infrastructure, or shifting consumer lifestyle preferences. Trends may be upward (e.g., long-term real GDP growth), downward (e.g., agricultural employment share in industrializing nations), or stationary.

2. **Seasonal Variations ($S_t$)**: Short-term, periodic, highly regular, and predictable oscillations that repeat within fixed annual cycles (within twelve months, four quarters, fifty-two weeks, or even seven days). Seasonal patterns are driven primarily by two overarching exogenous forces:
   - Natural climatic conditions: Seasonal temperature swings, monsoon precipitation cycles, harvest calendars, and winter daylight variations directly dictate agricultural yields, construction activity, heating energy consumption, and shipping logistics.
   - Institutional, cultural, and legal conventions: Annual calendar events such as religious festivals (Christmas, Eid, Diwali), fiscal year-end tax settlements, public school holiday schedules, and annual corporate accounting cycles induce predictable annual surges and contractions in consumer expenditure and business output.

3. **Cyclical Fluctuations ($C_t$)**: Medium-term, wave-like, oscillatory patterns tracing the recurring phases of economic expansion, peak prosperity, contraction, recession, and recovery known collectively as the business cycle. Unlike seasonal variations, cyclical movements are not strictly periodic; their cycle length varies widely (historically between two and ten or twelve years), their amplitude is non-uniform, and their turning points cannot be predicted by simple calendar rules. Cyclical fluctuations arise from endogenous macroeconomic dynamics, including inventory adjustments, credit expansion and contraction cycles, aggregate investment surges, monetary policy shifts, and systemic confidence shocks.

4. **Irregular or Random Fluctuations ($I_t$ or $\epsilon_t$)**: Erratic, unpredictable, non-systematic, high-frequency residual movements caused by transient, unforeseen random shocks. These encompass geopolitical conflicts, natural disasters (earthquakes, catastrophic floods), unexpected labor strikes, pandemic lockdowns, abrupt trade embargoes, or simple statistical measurement error. By definition, irregular shocks possess zero expected value over time and exhibit low temporal persistence.

---

## Mathematical Decomposition Models: Additive vs Multiplicative

To isolate, quantify, and forecast these four unobserved components, economists formulate mathematical decomposition models governing how the latent forces combine to generate the observed aggregate value $Y_t$ at time $t$.

### The Classical Additive Decomposition Model
The additive model assumes that the four components act independently of one another, each exerting an absolute quantitative addition or subtraction on the observed series measured in the original units of the variable:

$$Y_t = T_t + S_t + C_t + I_t$$

In this formulation:
- $T_t$ represents the baseline absolute trend level in physical or monetary units.
- $S_t$ represents an absolute positive or negative deviation from trend attributable to the calendar season, satisfying the annual zero-sum constraint:
  $$\sum_{s=1}^{m} S_s = 0$$
  where $m$ denotes the number of seasonal periods per year (e.g., $m = 4$ for quarterly series, $m = 12$ for monthly series).
- $C_t$ represents the absolute positive or negative cyclical deviation around the trend.
- $I_t$ represents a mean-zero white noise residual term with constant variance $\sigma^2_I$.

The additive specification is appropriate when the absolute magnitude of the seasonal and cyclical swings remains invariant to the underlying level of the secular trend. For instance, if an ice-cream vendor consistently sells exactly 5,000 more liters in July than the annual trend average, regardless of whether annual average sales are 20,000 liters or 100,000 liters, an additive model accurately mirrors the underlying data generating process.

### The Classical Multiplicative Decomposition Model
In most empirical macroeconomic and financial time series—such as real GDP, nominal retail sales, consumer price indices, money supply, and industrial trade volumes—the absolute amplitude of seasonal and cyclical oscillations expands proportionally as the secular trend grows over time. Under these conditions, the additive model fails, because absolute seasonal deviations would appear artificially small in early decades and artificially large in later decades.

To capture proportionate scaling, the multiplicative decomposition model expresses the observed series as the continuous product of its latent components:

$$Y_t = T_t \times S_t \times C_t \times I_t$$

In the multiplicative framework:
- $T_t$ is expressed in the original physical or monetary units of measurement (e.g., billions of dollars, metric tons).
- $S_t$ is a dimensionless percentage multiplier or index ratio centered around unity (or 100%), representing relative seasonal scaling:
  $$\frac{1}{m} \sum_{s=1}^{m} S_s = 1.00 \quad \left( \text{or } \sum_{s=1}^{m} S_s = m \right)$$
  For example, a seasonal index of $S_{\text{Q4}} = 1.25$ indicates that fourth-quarter sales routinely exceed the deseasonalized baseline trend by 25%.
- $C_t$ is a dimensionless cyclical index ratio centered around unity ($C_t = 1.00$), where values above 1.00 denote macroeconomic boom periods and values below 1.00 indicate contractionary recessions.
- $I_t$ is a dimensionless random shock ratio centered around unity ($E[I_t] = 1.00$).

### Logarithmic Transformation and Model Equivalence
A mathematically elegant bridge connects the multiplicative and additive specifications. Taking the natural logarithm of both sides of a multiplicative system transforms the non-linear product into an exact additive structure:

$$\ln(Y_t) = \ln(T_t) + \ln(S_t) + \ln(C_t) + \ln(I_t)$$

Defining $y_t = \ln(Y_t)$, $\tau_t = \ln(T_t)$, $s_t = \ln(S_t)$, $c_t = \ln(C_t)$, and $\varepsilon_t = \ln(I_t)$, we obtain:

$$y_t = \tau_t + s_t + c_t + \varepsilon_t$$

Linear estimation algorithms, least squares regression, and filtering procedures designed for additive decomposition can therefore be deployed directly on log-transformed economic series, stabilizing variance and linearizing exponential growth trajectories.

---

## Estimation of Secular Trend: Non-Parametric Smoothing

The primary objective in trend estimation is to purge high-frequency seasonal oscillations and irregular noise, revealing the underlying long-term trajectory. Smoothing methods achieve this non-parametrically without imposing rigid functional forms on the data.

### The Method of Semi-Averages
The method of semi-averages provides a rapid, intuitive baseline for estimating a linear secular trend. The procedure divides the ordered time series of $N$ observations into two equal temporal halves. If $N$ is even, each half contains $k = N/2$ observations. If $N$ is odd, the middle observation is omitted, leaving two symmetric halves of $k = (N-1)/2$ observations.

For each half, the arithmetic mean of the time index ($\bar{t}_1$ and $\bar{t}_2$) and the arithmetic mean of the observed variable ($\bar{Y}_1$ and $\bar{Y}_2$) are calculated:

$$\bar{t}_1 = \frac{1}{k} \sum_{t=1}^{k} t, \quad \bar{Y}_1 = \frac{1}{k} \sum_{t=1}^{k} Y_t$$
$$\bar{t}_2 = \frac{1}{k} \sum_{t=N-k+1}^{N} t, \quad \bar{Y}_2 = \frac{1}{k} \sum_{t=N-k+1}^{N} Y_t$$

Plotting the two coordinate points $(\bar{t}_1, \bar{Y}_1)$ and $(\bar{t}_2, \bar{Y}_2)$ on a Cartesian scatter plot and connecting them with a straight line defines the semi-average trend line. The linear equation is given by:

$$T_t = a + b t$$
$$\text{Slope } b = \frac{\bar{Y}_2 - \bar{Y}_1}{\bar{t}_2 - \bar{t}_1}$$
$$\text{Intercept } a = \bar{Y}_1 - b \bar{t}_1$$

While computationally elementary, the method of semi-averages possesses substantial limitations: it is sensitive to extreme outliers at the boundaries and presupposes that the underlying trend is strictly linear.

### Moving Average Smoothing: Odd vs Even Windows
Moving average filtering represents one of the most robust, non-parametric techniques for smoothing time series. An arithmetic moving average replaces each observation with the unweighted or weighted mean of neighboring observations spanning a symmetric temporal window of width $k$.

#### 1. Odd-Period Moving Averages ($k = 2m + 1$)
When the filter window width $k$ is an odd integer (e.g., 3-year, 5-year, or 7-year moving averages), the window possesses an unambiguous, exact integer temporal center. For a symmetric window of width $2m + 1$, the smoothed trend estimate at time $t$ is:

$$M_t = \frac{1}{2m + 1} \sum_{j=-m}^{m} Y_{t+j}$$

For example, a 5-period moving average ($m = 2$) computes:
$$M_t = \frac{Y_{t-2} + Y_{t-1} + Y_t + Y_{t+1} + Y_{t+2}}{5}$$

The moving average filter functions as a mathematical low-pass frequency filter. It attenuates high-frequency oscillations (such as seasonal variations and random noise) while transmitting low-frequency secular trends.

#### 2. Even-Period Centered Moving Averages ($k = 2m$)
When dealing with quarterly data ($k = 4$) or monthly data ($k = 12$), the filter window width is even. An unweighted average of an even number of points falls temporally halfway between two observation periods:
$$M_{t + 0.5} = \frac{1}{4} \left( Y_t + Y_{t+1} + Y_{t+2} + Y_{t+3} \right)$$

Because economic data cannot be indexed at fractional calendar periods, a second 2-period moving average filter must be applied to center the smoothed estimates onto actual observation periods. The resulting **Centered Moving Average (CMA)** is:

$$\text{CMA}_t = \frac{M_{t-0.5} + M_{t+0.5}}{2} = \frac{1}{8} Y_{t-2} + \frac{1}{4} Y_{t-1} + \frac{1}{4} Y_t + \frac{1}{4} Y_{t+1} + \frac{1}{8} Y_{t+2}$$

This symmetric 5-point weighting scheme with boundary weights of $1/8$ and interior weights of $1/4$ completely annihilates quarterly seasonality of any amplitude, preserving an undistorted estimate of the combined trend-cycle component $T_t \times C_t$.

#### The Boundary Loss Problem:
A primary theoretical drawback of moving average filters is the inevitable loss of data points at the series boundaries. For a window of width $k = 2m + 1$, the first $m$ and last $m$ observations cannot be filtered, because full bilateral neighborhoods do not exist. In macroeconomic policy, where the most recent quarters are of paramount interest, moving averages cannot generate real-time nowcasts without asymmetric boundary kernels or model-based tail extrapolations.

---

## Parametric Least Squares Trend Estimation

When economic analysis requires functional extrapolation, long-term forecasting, or formal statistical inference, parametric trend functions are fitted to empirical time series via the Method of Ordinary Least Squares (OLS).

### 1. Linear Secular Trend
The linear trend model assumes that the economic variable changes by a constant absolute amount $b$ per unit of time:

$$Y_t = a + b t + \epsilon_t, \quad t = 1, 2, \dots, N$$

The OLS parameters minimize the sum of squared vertical residuals:
$$S(a, b) = \sum_{t=1}^{N} (Y_t - a - b t)^2$$

Differentiating $S(a, b)$ with respect to $a$ and $b$ and setting the partial derivatives to zero yields the standard normal equations:

$$\sum_{t=1}^{N} Y_t = N a + b \sum_{t=1}^{N} t$$
$$\sum_{t=1}^{N} t Y_t = a \sum_{t=1}^{N} t + b \sum_{t=1}^{N} t^2$$

#### The Time-Centering Transformation:
To decouple the normal equations and simplify manual calculations, we shift the time origin to the exact midpoint of the observation range:
$$x_t = t - \bar{t} = t - \frac{N+1}{2}$$

Because $\sum x_t = 0$, the normal equations decouple into two independent, single-variable linear equations:
$$\sum Y_t = N a \implies a = \frac{\sum Y_t}{N} = \bar{Y}$$
$$\sum x_t Y_t = b \sum x_t^2 \implies b = \frac{\sum x_t Y_t}{\sum x_t^2}$$

The parameter $a$ represents the estimated trend value at the center of the sample timeline, while $b$ represents the constant rate of absolute change per unit period.

### 2. Quadratic and Polynomial Trend Models
If an economic series exhibits accelerating or decelerating growth, a linear specification introduces structural specification error. A second-degree polynomial (quadratic) trend captures constant curvature:

$$Y_t = a + b t + c t^2 + \epsilon_t$$

Using centered coordinates $x_t$ where $\sum x_t = 0$ and $\sum x_t^3 = 0$, the normal equations simplify to:

$$\sum Y = N a + c \sum x^2$$
$$\sum x Y = b \sum x^2 \implies b = \frac{\sum x Y}{\sum x^2}$$
$$\sum x^2 Y = a \sum x^2 + c \sum x^4$$

Solving the simultaneous system for $a$ and $c$:
$$a = \frac{(\sum Y)(\sum x^4) - (\sum x^2 Y)(\sum x^2)}{N \sum x^4 - (\sum x^2)^2}$$
$$c = \frac{N \sum x^2 Y - (\sum x^2)(\sum Y)}{N \sum x^4 - (\sum x^2)^2}$$

If the quadratic parameter $c > 0$, the series exhibits upward convex acceleration (increasing returns or exponential-like expansion); if $c < 0$, it exhibits downward concave deceleration (diminishing marginal returns or saturation).

### 3. Exponential Growth Trend
Many financial and demographic series grow at a constant percentage rate rather than a constant absolute increment. The continuous exponential trend is expressed as:

$$Y_t = A B^t \quad \text{or} \quad Y_t = A e^{r t}$$

Taking the natural logarithm of both sides transforms the equation into a linear form:
$$\ln(Y_t) = \ln(A) + t \ln(B)$$
Defining $y_t^* = \ln(Y_t)$, $a^* = \ln(A)$, and $b^* = \ln(B)$, the standard linear OLS formulas apply directly to $(t, y_t^*)$. Once $a^*$ and $b^*$ are estimated:
$$A = e^{a^*}, \quad B = e^{b^*}$$
The annual compound growth rate $r$ is given by $r = B - 1$ (or $r = \ln(B)$ in continuous compounding).

---

## Non-Linear Growth Curves: Gompertz and Logistic Models

Macroeconomic growth series—such as technological adoption curves, cellular network subscriptions, urbanization rates, or industrial capacity expansion—rarely exhibit unchecked exponential growth. Instead, they follow an S-shaped (sigmoidal) trajectory characterized by three distinct phases:
1. An initial slow emergence phase.
2. A rapid, near-exponential acceleration phase.
3. A gradual deceleration toward an asymptotic carrying capacity or market saturation level.

### 1. The Modified Exponential Trend
The modified exponential curve serves as the mathematical building block for sigmoidal models:

$$Y_t = k + a b^t, \quad a < 0, \quad 0 < b < 1$$

As $t \to \infty$, the term $b^t \to 0$, causing $Y_t$ to approach the upper asymptote $k$ asymptotically from below. The difference between the curve and its asymptote diminishes at a constant geometric ratio:
$$\frac{Y_{t+1} - Y_t}{Y_t - Y_{t-1}} = b$$

### 2. The Gompertz Growth Curve
Named after the British mathematician Benjamin Gompertz (1825), the Gompertz curve assumes that the *logarithm* of the variable follows a modified exponential curve:

$$Y_t = k a^{b^t}, \quad k > 0, \quad 0 < a < 1, \quad 0 < b < 1$$

Taking the natural logarithm yields:
$$\ln(Y_t) = \ln(k) + b^t \ln(a)$$
Defining $y_t^* = \ln(Y_t)$, $K^* = \ln(k)$, and $A^* = \ln(a)$, we have:
$$y_t^* = K^* + A^* b^t$$

The Gompertz curve possesses an asymmetric inflection point occurring at an early stage of growth:
$$Y_{\text{inflection}} = \frac{k}{e} \approx 0.368 k$$
Growth accelerates rapidly during the first 36.8% of expansion and decelerates over the remaining 63.2% of its trajectory. This asymmetry makes Gompertz curves suitable for modeling newly invented industrial goods, agricultural commodity yields, and mortal survival dynamics.

### 3. The Logistic (Pearl-Reed) Growth Curve
The logistic curve, formalized by Pierre François Verhulst (1838) and popularized by Raymond Pearl and Lowell Reed (1920), assumes that the *reciprocal* of the variable follows a modified exponential equation:

$$\frac{1}{Y_t} = k + a b^t \implies Y_t = \frac{L}{1 + m e^{-r t}}$$

The logistic curve is symmetric around its inflection point, which occurs precisely at half of its upper asymptotic capacity:
$$Y_{\text{inflection}} = \frac{L}{2}$$

The growth rate of the variable is proportional to both its current level and the remaining distance to carrying capacity:
$$\frac{dY_t}{dt} = r Y_t \left( 1 - \frac{Y_t}{L} \right)$$

The logistic model forms the standard empirical framework for modeling market penetration of durable consumer goods (smartphones, electric vehicles, broadband internet) where peer adoption dynamics generate symmetric diffusion.

---

## Worked Questions and Solutions

### Question 1: Least Squares Linear and Quadratic Trend Fitting
An empirical investigation into national manufacturing output records the following index of industrial production over a consecutive seven-year period ($t = 1, 2, \dots, 7$):

| Year ($t$) | 2018 ($1$) | 2019 ($2$) | 2020 ($3$) | 2021 ($4$) | 2022 ($5$) | 2023 ($6$) | 2024 ($7$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Industrial Index ($Y_t$) | 102.0 | 108.5 | 114.0 | 122.5 | 134.0 | 148.5 | 165.0 |

1. Shift the time origin to the center of the series ($x_t = t - 4$) and estimate the parameters of the linear trend equation $T_t = a + b x_t$ via Ordinary Least Squares.
2. Formulate the normal equations and estimate the parameters of the quadratic trend equation $T_t = a_q + b_q x_t + c_q x_t^2$.
3. Compute the fitted trend values for both models across all seven historical years, evaluate the Sum of Squared Errors ($\text{SSE} = \sum (Y_t - T_t)^2$) for each model, and determine whether the quadratic specification provides a superior empirical fit.
4. Generate out-of-sample projections of industrial production for the years 2025 ($t = 8$) and 2026 ($t = 9$) using both fitted models.

### Solution, step 1: OLS Linear Trend Estimation
The number of observations is $N = 7$ (an odd integer).
The temporal center is the fourth year: $\bar{t} = (7 + 1) / 2 = 4$ (representing 2021).
We apply the centering transformation $x_t = t - 4$.
The centered coordinates are:
$$x = [-3, -2, -1, 0, 1, 2, 3]$$
By construction:
$$\sum x_t = 0$$

Let us compute the required intermediate sums:
- $\sum Y_t = 102.0 + 108.5 + 114.0 + 122.5 + 134.0 + 148.5 + 165.0 = 894.5$
- $\sum x_t^2 = (-3)^2 + (-2)^2 + (-1)^2 + 0^2 + 1^2 + 2^2 + 3^2 = 9 + 4 + 1 + 0 + 1 + 4 + 9 = 28$
- Products $x_t Y_t$:
  - $t = 1$: $(-3) \times 102.0 = -306.0$
  - $t = 2$: $(-2) \times 108.5 = -217.0$
  - $t = 3$: $(-1) \times 114.0 = -114.0$
  - $t = 4$: $0 \times 122.5 = 0.0$
  - $t = 5$: $1 \times 134.0 = 134.0$
  - $t = 6$: $2 \times 148.5 = 297.0$
  - $t = 7$: $3 \times 165.0 = 495.0$
  - Sum: $\sum x_t Y_t = -306.0 - 217.0 - 114.0 + 0 + 134.0 + 297.0 + 495.0 = 289.0$

Computing the linear OLS parameters:
$$a = \frac{\sum Y_t}{N} = \frac{894.5}{7} \approx 127.7857$$
$$b = \frac{\sum x_t Y_t}{\sum x_t^2} = \frac{289.0}{28} \approx 10.3214$$

The fitted linear trend equation with origin at 2021 ($x = 0$) is:
$$T_t = 127.7857 + 10.3214 x_t$$

In terms of the original calendar index $t$ ($x_t = t - 4$):
$$T_t = 127.7857 + 10.3214 (t - 4) = 86.5001 + 10.3214 t$$

### Solution, step 2: Quadratic Trend Estimation
For the second-degree polynomial model $T_t = a_q + b_q x_t + c_q x_t^2$ with centered coordinates:
$$\sum x_t = 0 \quad \text{and} \quad \sum x_t^3 = 0$$

The parameter $b_q$ decouples completely from $a_q$ and $c_q$:
$$b_q = \frac{\sum x_t Y_t}{\sum x_t^2} = \frac{289.0}{28} \approx 10.3214$$
Notice that the linear coefficient is identical to that of the linear model.

To solve for $a_q$ and $c_q$, we need $\sum x_t^4$ and $\sum x_t^2 Y_t$:
- $x^4$: $(-3)^4 + (-2)^4 + (-1)^4 + 0^4 + 1^4 + 2^4 + 3^4 = 81 + 16 + 1 + 0 + 1 + 16 + 81 = 196$
- Products $x_t^2 Y_t$:
  - $t = 1$: $9 \times 102.0 = 918.0$
  - $t = 2$: $4 \times 108.5 = 434.0$
  - $t = 3$: $1 \times 114.0 = 114.0$
  - $t = 4$: $0 \times 122.5 = 0.0$
  - $t = 5$: $1 \times 134.0 = 134.0$
  - $t = 6$: $4 \times 148.5 = 594.0$
  - $t = 7$: $9 \times 165.0 = 1485.0$
  - Sum: $\sum x_t^2 Y_t = 918.0 + 434.0 + 114.0 + 0 + 134.0 + 594.0 + 1485.0 = 3679.0$

The simultaneous system for $a_q$ and $c_q$ is:
$$\begin{cases}
N a_q + c_q \sum x_t^2 = \sum Y_t \\
a_q \sum x_t^2 + c_q \sum x_t^4 = \sum x_t^2 Y_t
\end{cases} \implies \begin{cases}
7 a_q + 28 c_q = 894.5 \\
28 a_q + 196 c_q = 3679.0
\end{cases}$$

Multiplying the first equation by 4:
$$28 a_q + 112 c_q = 3578.0$$

Subtracting this from the second equation:
$$(196 - 112) c_q = 3679.0 - 3578.0$$
$$84 c_q = 101.0 \implies c_q = \frac{101.0}{84} \approx 1.20238$$

Substituting $c_q$ back into the first equation:
$$7 a_q + 28(1.20238) = 894.5$$
$$7 a_q + 33.6667 = 894.5 \implies 7 a_q = 860.8333 \implies a_q \approx 122.9762$$

The fitted quadratic trend equation (with origin at 2021) is:
$$T_t = 122.9762 + 10.3214 x_t + 1.2024 x_t^2$$

### Solution, step 3: Comparative Goodness-of-Fit Analysis
Let us compute the fitted values and squared residuals for both specifications:

| Year | $x_t$ | Observed $Y_t$ | Linear $T_{\text{lin}}$ | Residual $(Y - T_{\text{lin}})^2$ | Quadratic $T_{\text{quad}}$ | Residual $(Y - T_{\text{quad}})^2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 2018 | $-3$ | 102.0 | $127.786 - 30.964 = 96.822$ | $(102.0 - 96.822)^2 = 26.812$ | $122.976 - 30.964 + 10.821 = 102.833$ | $(102.0 - 102.833)^2 = 0.694$ |
| 2019 | $-2$ | 108.5 | $127.786 - 20.643 = 107.143$ | $(108.5 - 107.143)^2 = 1.841$ | $122.976 - 20.643 + 4.810 = 107.143$ | $(108.5 - 107.143)^2 = 1.841$ |
| 2020 | $-1$ | 114.0 | $127.786 - 10.321 = 117.465$ | $(114.0 - 117.465)^2 = 12.006$ | $122.976 - 10.321 + 1.202 = 113.857$ | $(114.0 - 113.857)^2 = 0.020$ |
| 2021 | $0$ | 122.5 | $127.786 + 0 = 127.786$ | $(122.5 - 127.786)^2 = 27.942$ | $122.976 + 0 + 0 = 122.976$ | $(122.5 - 122.976)^2 = 0.227$ |
| 2022 | $1$ | 134.0 | $127.786 + 10.321 = 138.107$ | $(134.0 - 138.107)^2 = 16.867$ | $122.976 + 10.321 + 1.202 = 134.499$ | $(134.0 - 134.499)^2 = 0.249$ |
| 2023 | $2$ | 148.5 | $127.786 + 20.643 = 148.429$ | $(148.5 - 148.429)^2 = 0.005$ | $122.976 + 20.643 + 4.810 = 148.429$ | $(148.5 - 148.429)^2 = 0.005$ |
| 2024 | $3$ | 165.0 | $127.786 + 30.964 = 158.750$ | $(165.0 - 158.750)^2 = 39.063$ | $122.976 + 30.964 + 10.821 = 164.761$ | $(165.0 - 164.761)^2 = 0.057$ |

Summing the squared errors:
$$\text{SSE}_{\text{linear}} = 26.812 + 1.841 + 12.006 + 27.942 + 16.867 + 0.005 + 39.063 = 124.536$$
$$\text{SSE}_{\text{quadratic}} = 0.694 + 1.841 + 0.020 + 0.227 + 0.249 + 0.005 + 0.057 = 3.093$$

The quadratic model reduces the residual sum of squares by **97.5%** (from 124.54 down to 3.09). The positive curvature parameter ($c_q = +1.2024$) confirms that industrial manufacturing output is expanding with accelerating convex momentum, reflecting cumulative capital deepening and technological scale economies.

### Solution, step 4: Out-of-Sample Trend Projections
For 2025 ($t = 8 \implies x_8 = 8 - 4 = +4$):
- **Linear Projection**:
  $$T_{2025} = 127.7857 + 10.3214(4) = 127.7857 + 41.2856 = 169.07$$
- **Quadratic Projection**:
  $$T_{2025} = 122.9762 + 10.3214(4) + 1.2024(4^2) = 122.9762 + 41.2856 + 1.2024(16) = 164.2618 + 19.2384 = 183.50$$

For 2026 ($t = 9 \implies x_9 = 9 - 4 = +5$):
- **Linear Projection**:
  $$T_{2026} = 127.7857 + 10.3214(5) = 127.7857 + 51.6070 = 179.39$$
- **Quadratic Projection**:
  $$T_{2026} = 122.9762 + 10.3214(5) + 1.2024(5^2) = 122.9762 + 51.6070 + 1.2024(25) = 174.5832 + 30.0600 = 204.64$$

The linear extrapolation understates future output by failing to account for compounding growth dynamics, projecting 183.50 in 2025 versus 169.07 for the linear model.

---

### Question 2: Moving Average Smoothing with Odd and Centered Windows
A statistical agency monitors quarterly export revenues (in millions of dollars) for an agro-industrial sector over three consecutive years (12 calendar quarters):

| Year | Q1 | Q2 | Q3 | Q4 |
| :---: | :---: | :---: | :---: | :---: |
| **Year 1** | 42.0 | 68.0 | 54.0 | 36.0 |
| **Year 2** | 48.0 | 76.0 | 62.0 | 40.0 |
| **Year 3** | 56.0 | 88.0 | 70.0 | 46.0 |

1. Explain mathematically why an unweighted 4-quarter moving average cannot be placed directly against a specific calendar quarter, and formulate the exact 2-period centering filter needed to produce Centered Moving Averages ($\text{CMA}_t$).
2. Calculate the complete series of 4-quarter moving totals, 4-quarter uncentered moving averages, and 4-quarter Centered Moving Averages ($\text{CMA}_t$) across all available quarters.
3. Quantify exactly how many quarters of data are lost at the beginning and end of the series due to moving average centering, and evaluate the trade-off between smoothing filter length and timely macroeconomic monitoring.

### Solution, step 1: Mathematical Theory of Centering
An unweighted moving average over an even window $k = 4$ computes:
$$M_{t + 0.5} = \frac{Y_t + Y_{t+1} + Y_{t+2} + Y_{t+3}}{4}$$

This arithmetic mean corresponds temporally to the midpoint between period $t+1$ and period $t+2$. In our quarterly series, the average of Q1, Q2, Q3, and Q4 represents the calendar instant between Q2 and Q3 (i.e., July 1st). Placing this value on either Q2 or Q3 introduces a half-quarter (1.5 month) phase shift or timing distortion.

To restore chronological alignment with observable quarters, we take a 2-period moving average of adjacent uncentered averages:
$$\text{CMA}_{t+1.5} = \frac{M_{t+0.5} + M_{t+1.5}}{2} = \frac{\frac{Y_t + Y_{t+1} + Y_{t+2} + Y_{t+3}}{4} + \frac{Y_{t+1} + Y_{t+2} + Y_{t+3} + Y_{t+4}}{4}}{2}$$
$$\text{CMA}_{t+1.5} = \frac{Y_t + 2Y_{t+1} + 2Y_{t+2} + 2Y_{t+3} + Y_{t+4}}{8}$$

This weighted moving average assigns a weight of $1/8$ to the boundary quarters and $2/8 = 1/4$ to the interior quarters, placing the resulting smoothed estimate at the exact temporal center of the 5-quarter window.

### Solution, step 2: Computation of 4-Quarter Centered Moving Averages
Let us index the 12 quarters sequentially from $t = 1$ (Year 1, Q1) to $t = 12$ (Year 3, Q4):

- $t = 1$: Y1 Q1 $= 42.0$
- $t = 2$: Y1 Q2 $= 68.0$
- $t = 3$: Y1 Q3 $= 54.0$
- $t = 4$: Y1 Q4 $= 36.0$
- $t = 5$: Y2 Q1 $= 48.0$
- $t = 6$: Y2 Q2 $= 76.0$
- $t = 7$: Y2 Q3 $= 62.0$
- $t = 8$: Y2 Q4 $= 40.0$
- $t = 9$: Y3 Q1 $= 56.0$
- $t = 10$: Y3 Q2 $= 88.0$
- $t = 11$: Y3 Q3 $= 70.0$
- $t = 12$: Y3 Q4 $= 46.0$

Let us calculate the 4-quarter moving totals ($\text{MT}_4$) and uncentered averages ($M$):
1. Quarters 1–4 ($t=1$ to $4$):
   $$\text{MT} = 42 + 68 + 54 + 36 = 200.0 \implies M_{2.5} = 50.00$$
2. Quarters 2–5 ($t=2$ to $5$):
   $$\text{MT} = 68 + 54 + 36 + 48 = 206.0 \implies M_{3.5} = 51.50$$
3. Quarters 3–6 ($t=3$ to $6$):
   $$\text{MT} = 54 + 36 + 48 + 76 = 214.0 \implies M_{4.5} = 53.50$$
4. Quarters 4–7 ($t=4$ to $7$):
   $$\text{MT} = 36 + 48 + 76 + 62 = 222.0 \implies M_{5.5} = 55.50$$
5. Quarters 5–8 ($t=5$ to $8$):
   $$\text{MT} = 48 + 76 + 62 + 40 = 226.0 \implies M_{6.5} = 56.50$$
6. Quarters 6–9 ($t=6$ to $9$):
   $$\text{MT} = 76 + 62 + 40 + 56 = 234.0 \implies M_{7.5} = 58.50$$
7. Quarters 7–10 ($t=7$ to $10$):
   $$\text{MT} = 62 + 40 + 56 + 88 = 246.0 \implies M_{8.5} = 61.50$$
8. Quarters 8–11 ($t=8$ to $11$):
   $$\text{MT} = 40 + 56 + 88 + 70 = 254.0 \implies M_{9.5} = 63.50$$
9. Quarters 9–12 ($t=9$ to $12$):
   $$\text{MT} = 56 + 88 + 70 + 46 = 260.0 \implies M_{10.5} = 65.00$$

Now we compute the Centered Moving Averages ($\text{CMA}_t$) by averaging adjacent pairs:
- **Quarter 3 (Y1 Q3)**:
  $$\text{CMA}_3 = \frac{M_{2.5} + M_{3.5}}{2} = \frac{50.00 + 51.50}{2} = 50.75$$
- **Quarter 4 (Y1 Q4)**:
  $$\text{CMA}_4 = \frac{M_{3.5} + M_{4.5}}{2} = \frac{51.50 + 53.50}{2} = 52.50$$
- **Quarter 5 (Y2 Q1)**:
  $$\text{CMA}_5 = \frac{M_{4.5} + M_{5.5}}{2} = \frac{53.50 + 55.50}{2} = 54.50$$
- **Quarter 6 (Y2 Q2)**:
  $$\text{CMA}_6 = \frac{M_{5.5} + M_{6.5}}{2} = \frac{55.50 + 56.50}{2} = 56.00$$
- **Quarter 7 (Y2 Q3)**:
  $$\text{CMA}_7 = \frac{M_{6.5} + M_{7.5}}{2} = \frac{56.50 + 58.50}{2} = 57.50$$
- **Quarter 8 (Y2 Q4)**:
  $$\text{CMA}_8 = \frac{M_{7.5} + M_{8.5}}{2} = \frac{58.50 + 61.50}{2} = 60.00$$
- **Quarter 9 (Y3 Q1)**:
  $$\text{CMA}_9 = \frac{M_{8.5} + M_{9.5}}{2} = \frac{61.50 + 63.50}{2} = 62.50$$
- **Quarter 10 (Y3 Q2)**:
  $$\text{CMA}_{10} = \frac{M_{9.5} + M_{10.5}}{2} = \frac{63.50 + 65.00}{2} = 64.25$$

Tabular summary:

| Period ($t$) | Calendar Quarter | Observed Export ($Y_t$) | 4-Quarter MT | Uncentered $M$ | Centered $\text{CMA}_t$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Y1 Q1 | 42.0 | — | — | — |
| 2 | Y1 Q2 | 68.0 | — | — | — |
| — | Mid 1-4 | — | 200.0 | 50.00 | — |
| 3 | Y1 Q3 | 54.0 | — | — | **50.75** |
| — | Mid 2-5 | — | 206.0 | 51.50 | — |
| 4 | Y1 Q4 | 36.0 | — | — | **52.50** |
| — | Mid 3-6 | — | 214.0 | 53.50 | — |
| 5 | Y2 Q1 | 48.0 | — | — | **54.50** |
| — | Mid 4-7 | — | 222.0 | 55.50 | — |
| 6 | Y2 Q2 | 76.0 | — | — | **56.00** |
| — | Mid 5-8 | — | 226.0 | 56.50 | — |
| 7 | Y2 Q3 | 62.0 | — | — | **57.50** |
| — | Mid 6-9 | — | 234.0 | 58.50 | — |
| 8 | Y2 Q4 | 40.0 | — | — | **60.00** |
| — | Mid 7-10 | — | 246.0 | 61.50 | — |
| 9 | Y3 Q1 | 56.0 | — | — | **62.50** |
| — | Mid 8-11 | — | 254.0 | 63.50 | — |
| 10 | Y3 Q2 | 88.0 | — | — | **64.25** |
| — | Mid 9-12 | — | 260.0 | 65.00 | — |
| 11 | Y3 Q3 | 70.0 | — | — | — |
| 12 | Y3 Q4 | 46.0 | — | — | — |

### Solution, step 3: Evaluation of Boundary Loss and Macroeconomic Implications
In this 12-quarter series:
- The first two quarters ($t = 1$ and $t = 2$, Year 1 Q1 and Q2) have no centered moving average.
- The last two quarters ($t = 11$ and $t = 12$, Year 3 Q3 and Q4) have no centered moving average.

In general, for a window of width $k = 4$ centered over $k+1 = 5$ observations, exactly $k/2 = 2$ observations are lost at the leading boundary and $k/2 = 2$ observations are lost at the trailing boundary. Out of 12 original observations, only 8 smoothed trend-cycle values ($66.7\%$) are obtained.

This loss creates a fundamental dilemma for central banks and economic ministries: the moving average provides a clean, non-parametric trend-cycle filter, but it cannot deliver real-time trend estimates for the most recent two quarters (six months). Policymakers must supplement moving averages with asymmetric boundary filters (such as Musgrave filters) or parametric ARIMA state-space forecasts to close the end-point information gap.

---

### Question 3: Non-Linear Modified Exponential Growth Fitting via Partial Sums
An empirical study of rural telecommunication infrastructure measures the percentage of households connected to fiber broadband over nine consecutive biennial periods ($N = 9$, $t = 0, 1, 2, \dots, 8$):

| Period ($t$) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Adoption % ($Y_t$) | 14.2 | 22.8 | 29.8 | 35.5 | 40.1 | 43.8 | 46.7 | 49.1 | 51.0 |

1. Formulate the modified exponential trend model $Y_t = k + a b^t$ and explain the economic significance of parameters $k$, $a$, and $b$.
2. Divide the 9 observations into three equal temporal groups of $m = 3$ observations each, compute the three partial sums $S_1, S_2, S_3$, and derive the closed-form algebraic expressions for parameters $b$, $a$, and $k$.
3. Compute the numerical estimates of $k$, $a$, and $b$, and state the fitted trend equation.
4. Calculate the theoretical upper saturation limit of broadband adoption, and forecast household adoption for periods $t = 9$ and $t = 10$.

### Solution, step 1: Formulation and Economic Interpretation
The modified exponential growth model is given by:
$$Y_t = k + a b^t, \quad t = 0, 1, \dots$$

Economic and mathematical roles of the parameters:
- **Asymptotic Limit ($k$)**: As $t \to \infty$, since $0 < b < 1$, the term $b^t \to 0$. Thus, $Y_t \to k$. The parameter $k$ represents the maximum carrying capacity or long-run market saturation level of broadband adoption in the rural population.
- **Initial Deficit Parameter ($a$)**: At initial period $t = 0$, $Y_0 = k + a$. Since adoption starts below saturation, $a < 0$, and $|a| = k - Y_0$ represents the total initial market deficit yet to be penetrated.
- **Decay Factor ($b$)**: The parameter $b \in (0, 1)$ measures the ratio of successive adoption increments:
  $$\frac{Y_{t+1} - Y_t}{Y_t - Y_{t-1}} = \frac{a b^t (b - 1)}{a b^{t-1} (b - 1)} = b$$
  A value of $b$ close to 0 indicates rapid saturation convergence, whereas $b$ close to 1 denotes protracted adoption diffusion.

### Solution, step 2: Method of Three Partial Sums
The total number of observations is $N = 9$. We partition the series into $n = 3$ contiguous groups of $m = 3$ observations each:
- **Group 1 ($t = 0, 1, 2$)**:
  $$S_1 = \sum_{t=0}^{2} Y_t = 14.2 + 22.8 + 29.8 = 66.8$$
- **Group 2 ($t = 3, 4, 5$)**:
  $$S_2 = \sum_{t=3}^{5} Y_t = 35.5 + 40.1 + 43.8 = 119.4$$
- **Group 3 ($t = 6, 7, 8$)**:
  $$S_3 = \sum_{t=6}^{8} Y_t = 46.7 + 49.1 + 51.0 = 146.8$$

Now, we express each partial sum theoretically in terms of $k, a, b$:
$$S_1 = \sum_{t=0}^{m-1} (k + a b^t) = m k + a \left( \frac{1 - b^m}{1 - b} \right)$$
$$S_2 = \sum_{t=m}^{2m-1} (k + a b^t) = m k + a b^m \left( \frac{1 - b^m}{1 - b} \right)$$
$$S_3 = \sum_{t=2m}^{3m-1} (k + a b^t) = m k + a b^{2m} \left( \frac{1 - b^m}{1 - b} \right)$$

Taking successive differences to eliminate the constant term $m k$:
$$D_1 = S_2 - S_1 = a (b^m - 1) \left( \frac{1 - b^m}{1 - b} \right) = - a \frac{(1 - b^m)^2}{1 - b} = a \frac{(b^m - 1)^2}{1 - b}$$
$$D_2 = S_3 - S_2 = a b^m \frac{(b^m - 1)^2}{1 - b}$$

Taking the ratio of the two differences:
$$\frac{D_2}{D_1} = \frac{S_3 - S_2}{S_2 - S_1} = b^m$$

Hence, the parameter $b$ is given by:
$$b = \left( \frac{S_3 - S_2}{S_2 - S_1} \right)^{1/m}$$

Once $b$ is determined, parameter $a$ is recovered from $D_1$:
$$a = \frac{(S_2 - S_1)(b - 1)}{(b^m - 1)^2} = \frac{(S_2 - S_1)(b - 1)}{(b^m - 1)(b^m - 1)}$$
More directly:
$$S_2 - S_1 = a b^0 (b^m - 1) \frac{b^m - 1}{b - 1} \implies a = \frac{(S_2 - S_1)(1 - b)}{(1 - b^m)^2} \times (-1) = \frac{(S_2 - S_1)(b - 1)}{(1 - b^m)^2}$$

Finally, parameter $k$ is obtained from $S_1$:
$$k = \frac{1}{m} \left[ S_1 - a \left( \frac{1 - b^m}{1 - b} \right) \right]$$

### Solution, step 3: Numerical Computation of Parameters
Using $m = 3$, $S_1 = 66.8$, $S_2 = 119.4$, and $S_3 = 146.8$:
$$S_2 - S_1 = 119.4 - 66.8 = 52.6$$
$$S_3 - S_2 = 146.8 - 119.4 = 27.4$$

1. **Calculate $b$**:
   $$b^3 = \frac{S_3 - S_2}{S_2 - S_1} = \frac{27.4}{52.6} \approx 0.5209125$$
   $$b = (0.5209125)^{1/3} \approx 0.8046$$

2. **Calculate $a$**:
   $$b^3 - 1 = 0.5209125 - 1 = -0.4790875$$
   $$(b^3 - 1)^2 = (-0.4790875)^2 \approx 0.229525$$
   $$b - 1 = 0.8046 - 1 = -0.1954$$
   $$a = \frac{(52.6) \times (-0.1954)}{0.229525} = \frac{-10.27804}{0.229525} \approx -44.78$$

3. **Calculate $k$**:
   $$\frac{1 - b^3}{1 - b} = \frac{1 - 0.5209125}{1 - 0.8046} = \frac{0.4790875}{0.1954} \approx 2.4518$$
   $$a \left( \frac{1 - b^3}{1 - b} \right) = -44.78 \times 2.4518 \approx -109.79$$
   $$S_1 - a \left( \frac{1 - b^3}{1 - b} \right) = 66.8 - (-109.79) = 66.8 + 109.79 = 176.59$$
   $$k = \frac{176.59}{3} \approx 58.86$$

The fitted modified exponential equation is:
$$Y_t = 58.86 - 44.78(0.8046)^t$$

Verification at initial baseline ($t = 0$):
$$Y_0 = 58.86 - 44.78(1.0) = 14.08\% \quad (\text{Observed } = 14.2\%)$$

### Solution, step 4: Saturation Limit and Forward Forecasts
- **Long-Run Saturation Limit**:
  As $t \to \infty$, $b^t \to 0$, so the maximum broadband adoption ceiling in this rural market is **$k = 58.86\%$**. Approximately 41.1% of households are projected to remain unconnected due to geographical remoteness, affordability constraints, or demographic factors.

- **Forecast for Period $t = 9$**:
  $$b^9 = (b^3)^3 = (0.5209125)^3 \approx 0.14134$$
  $$Y_9 = 58.86 - 44.78(0.14134) = 58.86 - 6.33 = \mathbf{52.53\%}$$

- **Forecast for Period $t = 10$**:
  $$b^{10} = b^9 \times b = 0.14134 \times 0.8046 \approx 0.11372$$
  $$Y_{10} = 58.86 - 44.78(0.11372) = 58.86 - 5.09 = \mathbf{53.77\%}$$

The forecasts exhibit realistic concavity, demonstrating steady saturation convergence toward the 58.86% asymptote.
"""

(OUT_DIR / "unit-3.md").write_text(u3_content, encoding="utf-8")
print(f"Unit 3: {prose_count(u3_content)} words")

# ==========================================
# UNIT 4: MEASUREMENT OF SEASONAL VARIATIONS & CYCLICAL FLUCTUATIONS
# ==========================================

u4_content = """# Unit 4: Measurement of Seasonal Variations & Cyclical Fluctuations

## The Economics and Mechanics of Seasonality

Seasonal variations represent repetitive, intra-annual periodic patterns that recur systematically within fixed intervals—such as months, quarters, weeks, or days. In economic analysis, identifying and isolating seasonality is vital for two distinct analytical purposes:
1. **Deseasonalization (Seasonal Adjustment)**: Removing recurring calendar distortions from raw economic data so that underlying cyclical expansions, contractions, and structural trends can be evaluated in real time without being obscured by predictable holiday rushes or winter slowdowns.
2. **Operational Planning**: Exploiting known seasonal patterns to optimize inventory procurement, logistics scheduling, agricultural storage, electrical peak-load generation, and working capital cash reserves.

Seasonality stems from two primary drivers:
- **Natural and Climatic Factors**: Agricultural sowing and harvesting calendars, winter heating demand, summer cooling surges, and weather constraints on maritime shipping and civil construction.
- **Institutional and Social Conventions**: Calendar milestones such as tax filing deadlines, school calendar reopenings, holiday shopping surges (Black Friday, Christmas), and religious festivals (Eid-ul-Fitr, Diwali).

To quantify seasonal effects, statisticians construct **Seasonal Indices**. In the multiplicative model ($Y_t = T_t \times S_t \times C_t \times I_t$), a seasonal index is expressed as a percentage centered on 100%. An index of 115% for the fourth quarter indicates that seasonal factors elevate fourth-quarter activity by 15% above the annual baseline, while an index of 82% for the first quarter reflects an 18% seasonal contraction.

---

## Classical Methods for Estimating Seasonal Indices

Over the past century, several statistical methodologies have been developed to isolate seasonal factors from time series.

### 1. The Method of Simple Averages
The method of simple averages is the most rudimentary procedure for estimating seasonal indices. It assumes that the time series contains no secular trend ($T_t = \text{constant}$) or that the trend has already been removed.

The algorithm proceeds as follows:
1. Arrange the data in a two-dimensional grid of $Y_{y,s}$, where rows denote years ($y = 1, \dots, K$) and columns denote seasons ($s = 1, \dots, m$, where $m=4$ for quarters, $m=12$ for months).
2. Compute the unweighted arithmetic mean for each seasonal column across all $K$ years:
   $$\bar{Y}_s = \frac{1}{K} \sum_{y=1}^{K} Y_{y,s}$$
3. Compute the grand mean across all seasons:
   $$\bar{Y} = \frac{1}{m} \sum_{s=1}^{m} \bar{Y}_s$$
4. Compute the unadjusted seasonal index for season $s$:
   $$\tilde{S}_s = \frac{\bar{Y}_s}{\bar{Y}} \times 100$$
5. Because $\sum_{s=1}^{m} \tilde{S}_s$ must equal $100m$, apply a normalization factor $k = \frac{100m}{\sum \tilde{S}_s}$ to obtain normalized seasonal indices:
   $$S_s = k \times \tilde{S}_s$$

**Theoretical Flaw**: If the time series possesses an upward secular trend, later seasons within each year will consistently register higher values solely due to trend growth rather than genuine seasonal demand. Consequently, the simple averages method produces upwardly biased indices for late calendar seasons.

### 2. The Ratio-to-Trend (Percentage-to-Trend) Method
The ratio-to-trend method explicitly corrects for secular trend by fitting a parametric trend line (linear, polynomial, or exponential) to the original series.

1. Fit an OLS trend equation $T_t = a + b t$ to the raw series.
2. Compute the estimated trend value $T_t$ for every observation period.
3. In a multiplicative model, divide the observed value by its trend value:
   $$R_t = \frac{Y_t}{T_t} = \frac{T_t \times S_t \times C_t \times I_t}{T_t} = S_t \times C_t \times I_t$$
   The resulting ratio $R_t$ isolates the combined seasonal, cyclical, and irregular component.
4. Group the ratios by season across years and compute the median or trimmed mean for each season, effectively neutralizing cyclical and random outliers.
5. Normalize the seasonal indices to sum to $100m$.

While superior to simple averages, the ratio-to-trend method depends heavily on the correctness of the fitted trend specification. If the true trend is non-linear and an OLS linear trend is imposed, trend misspecification leaks directly into the seasonal ratios.

### 3. The Ratio-to-Moving Average Method (The Benchmark Approach)
The **Ratio-to-Moving Average** method (formalized by the National Bureau of Economic Research and serving as the mathematical bedrock for the U.S. Census Bureau's X-11, X-12-ARIMA, and X-13ARIMA-SEATS procedures) is the most robust, non-parametric decomposition technique.

Instead of imposing a parametric trend curve, it utilizes a Centered Moving Average ($\text{CMA}_t$) to filter out both seasonal and high-frequency irregular variations simultaneously, leaving a clean estimate of the combined trend-cycle component:
$$\text{CMA}_t \approx T_t \times C_t$$

The ratio of observed data to the centered moving average yields:
$$z_t = \frac{Y_t}{\text{CMA}_t} = \frac{T_t \times S_t \times C_t \times I_t}{T_t \times C_t} = S_t \times I_t$$

The ratio $z_t$ isolates the pure seasonal and irregular fluctuations. By averaging these ratios across multiple years for each specific season using a modified mean or median, random shocks ($I_t$) cancel out, isolating the pure seasonal index $S_s$.

---

## The Link Relative Method (Karl Pearson)

Developed by Karl Pearson, the **Link Relative Method** measures period-to-period relative changes without requiring explicit trend fitting or moving average centering.

1. **Calculate Link Relatives**: For each observation, calculate the percentage ratio relative to the immediately preceding period:
   $$\text{LR}_t = \frac{Y_t}{Y_{t-1}} \times 100$$
2. **Seasonal Link Relative Averages**: For each season $s$, compute the arithmetic mean or median of the link relatives across all available years: $\overline{\text{LR}}_s$.
3. **Chaining to Base Period**: Choose Season 1 as the arbitrary base ($\text{CR}_1 = 100$). Convert the seasonal link relatives into **Chain Relatives** ($\text{CR}_s$) relative to Season 1:
   $$\text{CR}_2 = \frac{\overline{\text{LR}}_2 \times \text{CR}_1}{100} = \overline{\text{LR}}_2$$
   $$\text{CR}_3 = \frac{\overline{\text{LR}}_3 \times \text{CR}_2}{100}$$
   $$\text{CR}_m = \frac{\overline{\text{LR}}_m \times \text{CR}_{m-1}}{100}$$
4. **Closing the Loop and Estimating Trend Discrepancy**: Chaining the link relative of Season 1 back from Season $m$ yields a new estimate for Season 1:
   $$\text{CR}_1' = \frac{\overline{\text{LR}}_1 \times \text{CR}_m}{100}$$
   If the series has no secular trend, $\text{CR}_1'$ equals 100. If an upward trend exists, $\text{CR}_1' > 100$. The excess difference $\Delta = \text{CR}_1' - 100$ reflects cumulative secular growth over the course of the year.
5. **Trend Correction**: Distribute the cumulative discrepancy evenly across the seasons. The linear trend adjustment factor is:
   $$d = \frac{\text{CR}_1' - 100}{m}$$
   The trend-corrected chain relatives ($\text{CCR}_s$) are:
   $$\text{CCR}_s = \text{CR}_s - (s - 1) d, \quad s = 1, 2, \dots, m$$
6. **Normalization**: Normalize $\text{CCR}_s$ so that the average seasonal index across all $m$ seasons is exactly 100%:
   $$S_s = \frac{\text{CCR}_s}{\frac{1}{m} \sum_{j=1}^{m} \text{CCR}_j} \times 100$$

---

## Cyclical Fluctuations: The Residual Method and Business Cycles

Once secular trend ($T_t$) and seasonal indices ($S_t$) have been estimated, cyclical oscillations ($C_t$) can be isolated via the **Residual Method**.

In the multiplicative model:
$$\text{Deseasonalized Series } D_t = \frac{Y_t}{S_t} = T_t \times C_t \times I_t$$
Dividing the deseasonalized series by the secular trend $T_t$ yields the cyclical-irregular residual:
$$\frac{D_t}{T_t} = \frac{Y_t}{T_t \times S_t} = C_t \times I_t$$

Expressed as a percentage:
$$\text{Cyclical Residual } \% = \left( \frac{Y_t}{T_t \times S_t} \right) \times 100$$

To purge high-frequency irregular noise ($I_t$) from the cyclical-irregular residual, economists apply a short weighted moving average filter (such as a 3-month or 5-quarter Spencer/Henderson smoothing filter), isolating the underlying business cycle trajectory $C_t$.

### NBER Reference Cycles and Turning Points
Following the foundational methodology of Arthur Burns and Wesley Clair Mitchell at the National Bureau of Economic Research (NBER), the cyclical component is decomposed into recurring phases demarcated by specific turning points:
- **Peak**: The cyclical maximum signaling the end of an expansion and the onset of contraction.
- **Contraction (Recession)**: A broad, sustained decline in economic activity across multiple sectors, lasting from peak to trough.
- **Trough**: The cyclical minimum marking the end of recession and the initiation of recovery.
- **Expansion**: The upward phase from trough to subsequent peak.

---

## Worked Questions and Solutions

### Question 1: Seasonal Decomposition via Ratio-to-Moving Average
An agricultural distribution board tracks quarterly grain shipments (in thousands of metric tons) over a four-year period:

| Year | Q1 | Q2 | Q3 | Q4 |
| :---: | :---: | :---: | :---: | :---: |
| **2021** | 72.0 | 118.0 | 90.0 | 58.0 |
| **2022** | 78.0 | 126.0 | 98.0 | 64.0 |
| **2023** | 86.0 | 138.0 | 108.0 | 70.0 |
| **2024** | 92.0 | 148.0 | 116.0 | 76.0 |

1. Compute 4-quarter centered moving averages ($\text{CMA}_t$) for all eligible quarters.
2. Calculate the seasonal-irregular percentage ratios $z_t = (Y_t / \text{CMA}_t) \times 100$.
3. Compute the unadjusted seasonal index for each quarter using the arithmetic mean of the available quarterly ratios, apply the normalization factor, and report the final seasonal indices.
4. Deseasonalize the raw shipment data for all four quarters of 2024, and evaluate the underlying economic trend between Q2 and Q3 of 2024.

### Solution, step 1: Computation of Centered Moving Averages
We arrange the 16 observations sequentially ($t = 1, \dots, 16$) and compute 4-quarter moving totals ($\text{MT}_4$), uncentered moving averages ($M$), and centered moving averages ($\text{CMA}$):

- **2021**:
  - Q1 ($t=1$): $72.0$
  - Q2 ($t=2$): $118.0$
  - Q3 ($t=3$): $90.0$.
    - $\text{MT}_{1-4} = 72 + 118 + 90 + 58 = 338.0 \implies M_{2.5} = 84.50$
    - $\text{MT}_{2-5} = 118 + 90 + 58 + 78 = 344.0 \implies M_{3.5} = 86.00$
    - $\text{CMA}_3 = \frac{84.50 + 86.00}{2} = 85.25$
  - Q4 ($t=4$): $58.0$.
    - $\text{MT}_{3-6} = 90 + 58 + 78 + 126 = 352.0 \implies M_{4.5} = 88.00$
    - $\text{CMA}_4 = \frac{86.00 + 88.00}{2} = 87.00$

- **2022**:
  - Q1 ($t=5$): $78.0$.
    - $\text{MT}_{4-7} = 58 + 78 + 126 + 98 = 360.0 \implies M_{5.5} = 90.00$
    - $\text{CMA}_5 = \frac{88.00 + 90.00}{2} = 89.00$
  - Q2 ($t=6$): $126.0$.
    - $\text{MT}_{5-8} = 78 + 126 + 98 + 64 = 366.0 \implies M_{6.5} = 91.50$
    - $\text{CMA}_6 = \frac{90.00 + 91.50}{2} = 90.75$
  - Q3 ($t=7$): $98.0$.
    - $\text{MT}_{6-9} = 126 + 98 + 64 + 86 = 374.0 \implies M_{7.5} = 93.50$
    - $\text{CMA}_7 = \frac{91.50 + 93.50}{2} = 92.50$
  - Q4 ($t=8$): $64.0$.
    - $\text{MT}_{7-10} = 98 + 64 + 86 + 138 = 386.0 \implies M_{8.5} = 96.50$
    - $\text{CMA}_8 = \frac{93.50 + 96.50}{2} = 95.00$

- **2023**:
  - Q1 ($t=9$): $86.0$.
    - $\text{MT}_{8-11} = 64 + 86 + 138 + 108 = 396.0 \implies M_{9.5} = 99.00$
    - $\text{CMA}_9 = \frac{96.50 + 99.00}{2} = 97.75$
  - Q2 ($t=10$): $138.0$.
    - $\text{MT}_{9-12} = 86 + 138 + 108 + 70 = 402.0 \implies M_{10.5} = 100.50$
    - $\text{CMA}_{10} = \frac{99.00 + 100.50}{2} = 99.75$
  - Q3 ($t=11$): $108.0$.
    - $\text{MT}_{10-13} = 138 + 108 + 70 + 92 = 408.0 \implies M_{11.5} = 102.00$
    - $\text{CMA}_{11} = \frac{100.50 + 102.00}{2} = 101.25$
  - Q4 ($t=12$): $70.0$.
    - $\text{MT}_{11-14} = 108 + 70 + 92 + 148 = 418.0 \implies M_{12.5} = 104.50$
    - $\text{CMA}_{12} = \frac{102.00 + 104.50}{2} = 103.25$

- **2024**:
  - Q1 ($t=13$): $92.0$.
    - $\text{MT}_{12-15} = 70 + 92 + 148 + 116 = 426.0 \implies M_{13.5} = 106.50$
    - $\text{CMA}_{13} = \frac{104.50 + 106.50}{2} = 105.50$
  - Q2 ($t=14$): $148.0$.
    - $\text{MT}_{13-16} = 92 + 148 + 116 + 76 = 432.0 \implies M_{14.5} = 108.00$
    - $\text{CMA}_{14} = \frac{106.50 + 108.00}{2} = 107.25$
  - Q3 ($t=15$): $116.0$ (Lost)
  - Q4 ($t=16$): $76.0$ (Lost)

### Solution, step 2: Calculate Seasonal-Irregular Ratios ($z_t = \frac{Y_t}{\text{CMA}_t} \times 100$)
- **2021**:
  - Q3: $\frac{90.0}{85.25} \times 100 \approx 105.57\%$
  - Q4: $\frac{58.0}{87.00} \times 100 \approx 66.67\%$
- **2022**:
  - Q1: $\frac{78.0}{89.00} \times 100 \approx 87.64\%$
  - Q2: $\frac{126.0}{90.75} \times 100 \approx 138.84\%$
  - Q3: $\frac{98.0}{92.50} \times 100 \approx 105.95\%$
  - Q4: $\frac{64.0}{95.00} \times 100 \approx 67.37\%$
- **2023**:
  - Q1: $\frac{86.0}{97.75} \times 100 \approx 87.98\%$
  - Q2: $\frac{138.0}{99.75} \times 100 \approx 138.35\%$
  - Q3: $\frac{108.0}{101.25} \times 100 \approx 106.67\%$
  - Q4: $\frac{70.0}{103.25} \times 100 \approx 67.80\%$
- **2024**:
  - Q1: $\frac{92.0}{105.50} \times 100 \approx 87.20\%$
  - Q2: $\frac{148.0}{107.25} \times 100 \approx 138.00\%$

### Solution, step 3: Seasonal Index Averaging and Normalization
We compile the available ratios into quarterly columns and compute the arithmetic mean:

| Year | Q1 | Q2 | Q3 | Q4 |
| :---: | :---: | :---: | :---: | :---: |
| **2021** | — | — | 105.57 | 66.67 |
| **2022** | 87.64 | 138.84 | 105.95 | 67.37 |
| **2023** | 87.98 | 138.35 | 106.67 | 67.80 |
| **2024** | 87.20 | 138.00 | — | — |
| **Mean ($\tilde{S}_s$)** | **87.61%** | **138.40%** | **106.06%** | **67.28%** |

Calculations:
- $\bar{S}_{\text{Q1}} = \frac{87.64 + 87.98 + 87.20}{3} = 87.6067 \approx 87.61\%$
- $\bar{S}_{\text{Q2}} = \frac{138.84 + 138.35 + 138.00}{3} = 138.3967 \approx 138.40\%$
- $\bar{S}_{\text{Q3}} = \frac{105.57 + 105.95 + 106.67}{3} = 106.0633 \approx 106.06\%$
- $\bar{S}_{\text{Q4}} = \frac{66.67 + 67.37 + 67.80}{3} = 67.2800 \approx 67.28\%$

Sum of unadjusted seasonal indices:
$$\sum_{s=1}^{4} \tilde{S}_s = 87.61 + 138.40 + 106.06 + 67.28 = 399.35$$

The sum falls slightly short of the target 400.00. We compute the normalization factor:
$$k = \frac{400.00}{399.35} \approx 1.0016276$$

Applying the normalization factor:
- $S_{\text{Q1}} = 87.6067 \times 1.0016276 \approx \mathbf{87.75\%}$
- $S_{\text{Q2}} = 138.3967 \times 1.0016276 \approx \mathbf{138.62\%}$
- $S_{\text{Q3}} = 106.0633 \times 1.0016276 \approx \mathbf{106.24\%}$
- $S_{\text{Q4}} = 67.2800 \times 1.0016276 \approx \mathbf{67.39\%}$

Check sum: $87.75 + 138.62 + 106.24 + 67.39 = 400.00\%$.

### Solution, step 4: Deseasonalization of 2024 Data
To deseasonalize observed values, we divide each by its normalized seasonal index:
$$D_t = \frac{Y_t}{S_s / 100}$$

For 2024:
- **2024 Q1**:
  $$D_{\text{Q1}} = \frac{92.0}{0.8775} \approx \mathbf{104.84} \text{ thousand tons}$$
- **2024 Q2**:
  $$D_{\text{Q2}} = \frac{148.0}{1.3862} \approx \mathbf{106.77} \text{ thousand tons}$$
- **2024 Q3**:
  $$D_{\text{Q3}} = \frac{116.0}{1.0624} \approx \mathbf{109.19} \text{ thousand tons}$$
- **2024 Q4**:
  $$D_{\text{Q4}} = \frac{76.0}{0.6739} \approx \mathbf{112.78} \text{ thousand tons}$$

**Economic Interpretation**:
Looking at the raw shipment data, shipments appear to plummet dramatically between Q2 and Q3 of 2024 (falling from 148.0 to 116.0 thousand tons, a nominal decline of $-21.6\%$).
However, once seasonal influences are purged, the deseasonalized series reveals that underlying shipments actually expanded from **106.77 to 109.19 thousand tons** ($+2.27\%$). The observed drop was purely an artifact of normal seasonal contraction following the Q2 harvest peak. Macroeconomic policy and capacity planning must rely on the deseasonalized trajectory to avoid erroneous contractionary interventions.

---

### Question 2: Link Relative Method on Agricultural Production
An agro-statistical research institute analyzes quarterly tea harvest yields (in thousands of kilograms) across four years to establish seasonal adjustments via Karl Pearson's Link Relative Method:

| Year | Q1 | Q2 | Q3 | Q4 |
| :---: | :---: | :---: | :---: | :---: |
| **Year 1** | 30.0 | 45.0 | 60.0 | 25.0 |
| **Year 2** | 33.0 | 50.0 | 66.0 | 28.0 |
| **Year 3** | 36.0 | 55.0 | 72.0 | 31.0 |
| **Year 4** | 40.0 | 61.0 | 80.0 | 34.0 |

1. Calculate the link relatives ($\text{LR}_t = \frac{Y_t}{Y_{t-1}} \times 100$) for every quarterly transition.
2. Determine the arithmetic mean of the link relatives for each of the four quarters.
3. Compute the uncorrected chain relatives ($\text{CR}_s$) with base Q1 = 100, calculate the loop-closing discrepancy $\text{CR}_1'$, and evaluate the linear trend correction factor $d$.
4. Compute the trend-corrected chain relatives and normalize them to produce the final quarterly seasonal indices.

### Solution, step 1: Calculation of Link Relatives
The link relative formula is $\text{LR}_t = \frac{Y_t}{Y_{t-1}} \times 100$:

- **Year 1**:
  - Q1: Base, no prior quarter.
  - Q2: $\frac{45.0}{30.0} \times 100 = 150.00\%$
  - Q3: $\frac{60.0}{45.0} \times 100 \approx 133.33\%$
  - Q4: $\frac{25.0}{60.0} \times 100 \approx 41.67\%$

- **Year 2**:
  - Q1: $\frac{33.0}{25.0} \times 100 = 132.00\%$
  - Q2: $\frac{50.0}{33.0} \times 100 \approx 151.52\%$
  - Q3: $\frac{66.0}{50.0} \times 100 = 132.00\%$
  - Q4: $\frac{28.0}{66.0} \times 100 \approx 42.42\%$

- **Year 3**:
  - Q1: $\frac{36.0}{28.0} \times 100 \approx 128.57\%$
  - Q2: $\frac{55.0}{36.0} \times 100 \approx 152.78\%$
  - Q3: $\frac{72.0}{55.0} \times 100 \approx 130.91\%$
  - Q4: $\frac{31.0}{72.0} \times 100 \approx 43.06\%$

- **Year 4**:
  - Q1: $\frac{40.0}{31.0} \times 100 \approx 129.03\%$
  - Q2: $\frac{61.0}{40.0} \times 100 = 152.50\%$
  - Q3: $\frac{80.0}{61.0} \times 100 \approx 131.15\%$
  - Q4: $\frac{34.0}{80.0} \times 100 = 42.50\%$

### Solution, step 2: Average Link Relatives
We average the available link relatives for each quarter:

- **Quarter 1** (transitions from preceding year's Q4):
  $$\overline{\text{LR}}_1 = \frac{132.00 + 128.57 + 129.03}{3} = \frac{389.60}{3} \approx 129.87\%$$
- **Quarter 2** (transitions from Q1):
  $$\overline{\text{LR}}_2 = \frac{150.00 + 151.52 + 152.78 + 152.50}{4} = \frac{606.80}{4} = 151.70\%$$
- **Quarter 3** (transitions from Q2):
  $$\overline{\text{LR}}_3 = \frac{133.33 + 132.00 + 130.91 + 131.15}{4} = \frac{527.39}{4} \approx 131.85\%$$
- **Quarter 4** (transitions from Q3):
  $$\overline{\text{LR}}_4 = \frac{41.67 + 42.42 + 43.06 + 42.50}{4} = \frac{169.65}{4} \approx 42.41\%$$

### Solution, step 3: Chain Relatives and Trend Discrepancy
Setting Q1 as base ($\text{CR}_1 = 100.00$):
- $\text{CR}_1 = 100.00$
- $\text{CR}_2 = \frac{\overline{\text{LR}}_2 \times \text{CR}_1}{100} = \frac{151.70 \times 100.00}{100} = 151.70$
- $\text{CR}_3 = \frac{\overline{\text{LR}}_3 \times \text{CR}_2}{100} = \frac{131.85 \times 151.70}{100} \approx 200.02$
- $\text{CR}_4 = \frac{\overline{\text{LR}}_4 \times \text{CR}_3}{100} = \frac{42.41 \times 200.02}{100} \approx 84.83$

Loop-closing calculation for Q1 of the following year:
$$\text{CR}_1' = \frac{\overline{\text{LR}}_1 \times \text{CR}_4}{100} = \frac{129.87 \times 84.83}{100} \approx 110.17$$

The new chain relative for Q1 is $110.17$, which exceeds the original base of $100.00$ by:
$$\Delta = \text{CR}_1' - 100.00 = 110.17 - 100.00 = 10.17$$

This $+10.17\%$ excess reflects annual secular growth across the four quarters.
We compute the per-quarter linear trend correction factor $d$:
$$d = \frac{\Delta}{4} = \frac{10.17}{4} \approx 2.5425$$

### Solution, step 4: Trend Correction and Final Seasonal Indices
We adjust the chain relatives by subtracting $(s - 1) d$:
- **Quarter 1 ($s=1$)**:
  $$\text{CCR}_1 = \text{CR}_1 - 0 \times d = 100.00$$
- **Quarter 2 ($s=2$)**:
  $$\text{CCR}_2 = \text{CR}_2 - 1 \times d = 151.70 - 2.54 = 149.16$$
- **Quarter 3 ($s=3$)**:
  $$\text{CCR}_3 = \text{CR}_3 - 2 \times d = 200.02 - 5.085 = 194.94$$
- **Quarter 4 ($s=4$)**:
  $$\text{CCR}_4 = \text{CR}_4 - 3 \times d = 84.83 - 7.6275 = 77.20$$

Sum of trend-corrected chain relatives:
$$\sum_{s=1}^{4} \text{CCR}_s = 100.00 + 149.16 + 194.94 + 77.20 = 521.30$$
The arithmetic mean is:
$$\overline{\text{CCR}} = \frac{521.30}{4} = 130.325$$

Normalizing so that the mean equals 100%:
$$S_s = \frac{\text{CCR}_s}{130.325} \times 100$$

- $S_{\text{Q1}} = \frac{100.00}{130.325} \times 100 \approx \mathbf{76.73\%}$
- $S_{\text{Q2}} = \frac{149.16}{130.325} \times 100 \approx \mathbf{114.45\%}$
- $S_{\text{Q3}} = \frac{194.94}{130.325} \times 100 \approx \mathbf{149.58\%}$
- $S_{\text{Q4}} = \frac{77.20}{130.325} \times 100 \approx \mathbf{59.24\%}$

Check sum: $76.73 + 114.45 + 149.58 + 59.24 = 400.00\%$.
The adjusted seasonal indices indicate that tea harvests peak in Q3 (49.58% above annual average) and reach their seasonal low in Q4 (40.76% below average).

---

### Question 3: Isolating Cyclical Fluctuations via the Residual Method
A macroeconomic policy unit estimates the secular trend and quarterly seasonal indices for real gross domestic product (in billions of local currency) over a two-year observation window (8 quarters):

The fitted linear secular trend is:
$$T_t = 500.0 + 10.0 t, \quad t = 1, 2, \dots, 8$$

The normalized quarterly seasonal indices are:
$$S_1 = 92.0\%, \quad S_2 = 104.0\%, \quad S_3 = 108.0\%, \quad S_4 = 96.0\%$$

The observed quarterly GDP figures ($Y_t$) are:
- Year 1: Q1 ($t=1$) = 475.0, Q2 ($t=2$) = 548.0, Q3 ($t=3$) = 582.0, Q4 ($t=4$) = 530.0
- Year 2: Q1 ($t=5$) = 492.0, Q2 ($t=6$) = 565.0, Q3 ($t=7$) = 585.0, Q4 ($t=8$) = 515.0

1. Calculate the secular trend value $T_t$ and the combined trend-seasonal baseline $B_t = (T_t \times S_t) / 100$ for each of the eight quarters.
2. Isolate the cyclical-irregular residual ratio $(C_t \times I_t) = (Y_t / B_t) \times 100$ for all eight quarters.
3. Apply a 3-quarter weighted moving average filter with symmetric weights $[0.25, 0.50, 0.25]$ to smooth out irregular noise $I_t$, extracting the pure cyclical index $C_t$ for quarters 2 through 7.
4. Identify the timing of the business cycle peak and trough over this two-year period, and characterize the macroeconomic cyclical stance in Year 2 Q4.

### Solution, step 1: Secular Trend and Combined Baseline
We evaluate $T_t = 500.0 + 10.0 t$ and $B_t = \frac{T_t \times S_t}{100}$:

- **Quarter 1 ($t=1$, Y1 Q1)**:
  - $T_1 = 500 + 10(1) = 510.0$
  - $B_1 = \frac{510.0 \times 92.0}{100} = 469.20$
- **Quarter 2 ($t=2$, Y1 Q2)**:
  - $T_2 = 500 + 10(2) = 520.0$
  - $B_2 = \frac{520.0 \times 104.0}{100} = 540.80$
- **Quarter 3 ($t=3$, Y1 Q3)**:
  - $T_3 = 500 + 10(3) = 530.0$
  - $B_3 = \frac{530.0 \times 108.0}{100} = 572.40$
- **Quarter 4 ($t=4$, Y1 Q4)**:
  - $T_4 = 500 + 10(4) = 540.0$
  - $B_4 = \frac{540.0 \times 96.0}{100} = 518.40$
- **Quarter 5 ($t=5$, Y2 Q1)**:
  - $T_5 = 500 + 10(5) = 550.0$
  - $B_5 = \frac{550.0 \times 92.0}{100} = 506.00$
- **Quarter 6 ($t=6$, Y2 Q2)**:
  - $T_6 = 500 + 10(6) = 560.0$
  - $B_6 = \frac{560.0 \times 104.0}{100} = 582.40$
- **Quarter 7 ($t=7$, Y2 Q3)**:
  - $T_7 = 500 + 10(7) = 570.0$
  - $B_7 = \frac{570.0 \times 108.0}{100} = 615.60$
- **Quarter 8 ($t=8$, Y2 Q4)**:
  - $T_8 = 500 + 10(8) = 580.0$
  - $B_8 = \frac{580.0 \times 96.0}{100} = 556.80$

### Solution, step 2: Cyclical-Irregular Residual Ratios
We compute $(C_t \times I_t) = \frac{Y_t}{B_t} \times 100$:

- $t = 1$: $\frac{475.0}{469.20} \times 100 \approx \mathbf{101.24\%}$
- $t = 2$: $\frac{548.0}{540.80} \times 100 \approx \mathbf{101.33\%}$
- $t = 3$: $\frac{582.0}{572.40} \times 100 \approx \mathbf{101.68\%}$
- $t = 4$: $\frac{530.0}{518.40} \times 100 \approx \mathbf{102.24\%}$
- $t = 5$: $\frac{492.0}{506.00} \times 100 \approx \mathbf{97.23\%}$
- $t = 6$: $\frac{565.0}{582.40} \times 100 \approx \mathbf{97.01\%}$
- $t = 7$: $\frac{585.0}{615.60} \times 100 \approx \mathbf{95.03\%}$
- $t = 8$: $\frac{515.0}{556.80} \times 100 \approx \mathbf{92.49\%}$

### Solution, step 3: Smoothing with 3-Period Weighted Filter
To remove high-frequency irregular noise $I_t$, we apply the symmetric filter:
$$C_t = 0.25 (C_{t-1} I_{t-1}) + 0.50 (C_t I_t) + 0.25 (C_{t+1} I_{t+1})$$

- **Quarter 2 ($t=2$)**:
  $$C_2 = 0.25(101.24) + 0.50(101.33) + 0.25(101.68) = 25.31 + 50.665 + 25.42 = \mathbf{101.40\%}$$
- **Quarter 3 ($t=3$)**:
  $$C_3 = 0.25(101.33) + 0.50(101.68) + 0.25(102.24) = 25.3325 + 50.84 + 25.56 = \mathbf{101.73\%}$$
- **Quarter 4 ($t=4$)**:
  $$C_4 = 0.25(101.68) + 0.50(102.24) + 0.25(97.23) = 25.42 + 51.12 + 24.3075 = \mathbf{100.85\%}$$
- **Quarter 5 ($t=5$)**:
  $$C_5 = 0.25(102.24) + 0.50(97.23) + 0.25(97.01) = 25.56 + 48.615 + 24.2525 = \mathbf{98.43\%}$$
- **Quarter 6 ($t=6$)**:
  $$C_6 = 0.25(97.23) + 0.50(97.01) + 0.25(95.03) = 24.3075 + 48.505 + 23.7575 = \mathbf{96.57\%}$$
- **Quarter 7 ($t=7$)**:
  $$C_7 = 0.25(97.01) + 0.50(95.03) + 0.25(92.49) = 24.2525 + 47.515 + 23.1225 = \mathbf{94.89\%}$$

### Solution, step 4: Cyclical Stance and Turning Point Identification
- **Cyclical Peak**: The smoothed cyclical index reached its apex at **Quarter 3 ($t=3$, Year 1 Q3)** with a value of **$101.73\%$**. At this peak, economic output exceeded the trend-seasonal baseline by $1.73\%$.
- **Cyclical Contraction**: Following Quarter 3, the cyclical component entered a persistent downward trajectory, slipping below baseline ($100.0\%$) between Q4 of Year 1 and Q1 of Year 2.
- **Current Cyclical Stance in Year 2 Q4**:
  The unadjusted residual in Year 2 Q4 reached **$92.49\%$**, and the smoothed trend through Q7 stands at **$94.89\%$**. Output is currently operating between **$5.1\%$ and $7.5\%$ below potential trend capacity**. The economy is in an active contractionary phase of the business cycle, confirming that macroeconomic policy should adopt counter-cyclical stimulative measures (such as monetary easing or infrastructure investment).
"""

(OUT_DIR / "unit-4.md").write_text(u4_content, encoding="utf-8")
print(f"Unit 4: {prose_count(u4_content)} words")
