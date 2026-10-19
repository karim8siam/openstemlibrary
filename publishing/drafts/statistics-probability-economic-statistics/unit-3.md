# Unit 3: Time Series Analysis: Decomposition Models & Secular Trend Estimation

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
  $$\frac{1}{m} \sum_{s=1}^{m} S_s = 1.00 \quad \left( \text{or } \sum_{s=1}^{m} S_s = m 
\right)$$
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
$$M_{t + 0.5} = \frac{1}{4} \left( Y_t + Y_{t+1} + Y_{t+2} + Y_{t+3} 
\right)$$

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
$$\frac{dY_t}{dt} = r Y_t \left( 1 - \frac{Y_t}{L} 
\right)$$

The logistic model forms the standard empirical framework for modeling market penetration of durable consumer goods (smartphones, electric vehicles, broadband internet) where peer adoption dynamics generate symmetric diffusion.

---


---

## Advanced Trend Extraction: Orthogonal Polynomials and Modern Filtering

While standard Ordinary Least Squares polynomial fitting provides intuitive trend equations, fitting higher-degree polynomials via normal equations encounters severe numerical instability due to multicollinearity between powers of time ($t, t^2, t^3$). To overcome this, mathematical statisticians employ **Orthogonal Polynomials**, while macroeconomic policy relies on frequency-domain filters.

### 1. Orthogonal Polynomials (Chebyshev-Gram Polynomials)
A set of polynomials $\{\phi_0(t), \phi_1(t), \dots, \phi_p(t)\}$ defined on discrete observation points $t = 1, 2, \dots, N$ is mutually orthogonal if:

$$\sum_{t=1}^{N} \phi_r(t) \phi_s(t) = 0 \quad \text{for all } r \ne s$$

Expressing the polynomial trend as a linear combination of orthogonal basis functions:

$$T_t = c_0 \phi_0(t) + c_1 \phi_1(t) + c_2 \phi_2(t) + \dots + c_p \phi_p(t)$$

Because all cross-product terms vanish ($\sum \phi_r \phi_s = 0$), the normal equations decouple completely. Each parameter $c_r$ can be estimated independently without inverting a matrix:

$$c_r = \frac{\sum_{t=1}^{N} Y_t \phi_r(t)}{\sum_{t=1}^{N} [\phi_r(t)]^2}$$

The standardized Chebyshev-Gram polynomials for centered coordinates $x = t - \bar{t}$ are:
- $\phi_0(x) = 1$
- $\phi_1(x) = x$
- $\phi_2(x) = x^2 - \frac{N^2 - 1}{12}$
- $\phi_3(x) = x^3 - \left( \frac{3N^2 - 7}{20} \right) x$

**Practical Advantage**: Adding a higher-order term (e.g., expanding from a quadratic to a cubic trend) does not alter the numerical values of previously estimated lower-order coefficients ($c_0, c_1, c_2$), enabling sequential hypothesis testing of polynomial degree.

### 2. The Hodrick-Prescott (HP) Filter
In modern business cycle analysis and central banking, parametric polynomial trends are largely replaced by the **Hodrick-Prescott (HP) Filter** (Robert Hodrick and Edward Prescott, 1980). The HP filter decomposes an economic time series $y_t$ into a smooth trend component $\tau_t$ and a cyclical component $c_t = y_t - \tau_t$ by solving an explicit penalized optimization problem:

$$\min_{\{\tau_t\}_{t=1}^{T}} \left\{ \sum_{t=1}^{T} (y_t - \tau_t)^2 + \lambda \sum_{t=2}^{T-1} [(\tau_{t+1} - \tau_t) - (\tau_t - \tau_{t-1})]^2 \right\}$$

The objective function balances two competing goals:
1. **Goodness of Fit**: Minimizing the sum of squared cyclical deviations $\sum (y_t - \tau_t)^2$.
2. **Smoothness of Trend**: Penalizing second differences (acceleration or curvature) of the trend line via the regularization parameter $\lambda$.

#### The Smoothing Parameter $\lambda$:
- As $\lambda \to 0$, curvature is unconstrained, and the trend matches the data identically ($\tau_t = y_t$).
- As $\lambda \to \infty$, second differences are penalized to zero, forcing the trend to become a strictly linear OLS regression line.

By matching the filter's frequency response to standard business cycle durations (cycles between 2 and 8 years), economists adopt canonical values for $\lambda$:
- **Quarterly Data**: $\lambda = 1{,}600$
- **Monthly Data**: $\lambda = 14{,}400$
- **Annual Data**: $\lambda = 100$ (or $\lambda = 6.25$ in modern literature)

#### The End-Point Bias Problem:
At the sample boundaries ($t=1$ and $t=T$), the second-difference penalty operates with fewer adjacent points. Consequently, the HP trend is heavily drawn toward the most recent data observations. Central banks must exercise caution when interpreting the HP trend at the current edge of the business cycle.


---

## Stochastic Trends, Unit Roots, and the Nelson-Plosser Revolution

For decades, econometricians treated macroeconomic time series as **Trend-Stationary Processes ($TSP$)**: deterministic linear or polynomial trends accompanied by stationary cyclical fluctuations:

$$Y_t = \alpha + \beta t + \epsilon_t, \quad \epsilon_t \sim I(0)$$

Under a trend-stationary specification, economic shocks are purely temporary: after a recession or supply disruption, the economy inevitably reverts back to its predetermined deterministic trend path.

### 1. Difference-Stationary Processes and Random Walks
In a landmark 1982 empirical paper, Charles Nelson and Charles Plosser tested historical macroeconomic series (real GNP, industrial production, employment, real wages) and overturned this classical paradigm. They demonstrated that most macroeconomic series are **Difference-Stationary Processes ($DSP$)** containing a **Stochastic Trend (Unit Root)**:

$$Y_t = \mu + Y_{t-1} + u_t, \quad u_t \sim I(0)$$

Iterating backwards from an initial value $Y_0$:

$$Y_t = Y_0 + \mu t + \sum_{j=1}^{t} u_j$$

In a difference-stationary process:
- $\mu t$ represents a deterministic drift rate.
- $\sum_{j=1}^{t} u_j$ is a cumulative stochastic trend (a random walk with drift).

#### The Permanent Effect of Shocks:
In a unit root process, the variance expands linearly with time: $\text{Var}(Y_t) = t \sigma_u^2 \to \infty$ as $t \to \infty$. Every historical shock $u_t$ enters the summation with a coefficient of unity and permanently shifts the level of the time series forever. Recessions are not mere temporary dips below a deterministic trend; they permanently alter the long-run path of potential output.

### 2. Testing for Unit Roots: The Augmented Dickey-Fuller (ADF) Test
To test whether an economic series follows a deterministic trend or a stochastic unit root, David Dickey and Wayne Fuller (1979, 1981) formulated the **Dickey-Fuller Test**.
Consider the autoregressive model:

$$Y_t = \alpha + \beta t + \rho Y_{t-1} + \sum_{k=1}^{p} \gamma_k \Delta Y_{t-k} + e_t$$

Subtracting $Y_{t-1}$ from both sides:

$$\Delta Y_t = \alpha + \beta t + \delta Y_{t-1} + \sum_{k=1}^{p} \gamma_k \Delta Y_{t-k} + e_t$$

where $\delta = \rho - 1$.
The hypotheses are:
- **Null Hypothesis ($H_0$)**: $\delta = 0 \iff \rho = 1$ (The series contains a unit root / stochastic trend).
- **Alternative Hypothesis ($H_1$)**: $\delta < 0 \iff \rho < 1$ (The series is trend-stationary).

Under the null hypothesis, the standard $t$-statistic $t_\delta = \hat{\delta} / \text{SE}(\hat{\delta})$ does not follow a Student's $t$-distribution, but rather the non-standard **Dickey-Fuller distribution** (characterized by Brownian motion integrals). If the test fails to reject $H_0$, detrending via simple OLS regression produces spurious results, and the series must be transformed via first-differencing: $\Delta Y_t = Y_t - Y_{t-1}$.

---

## Structural Breaks in Trend: Perron's Breakthrough

In 1989, Pierre Perron demonstrated that standard Dickey-Fuller tests are dramatically biased toward erroneously finding a unit root if the true underlying data-generating process is a trend-stationary series with an unmodeled **Structural Break** (such as the 1929 Great Depression or the 1973 OPEC oil price shock).

Perron formulated models allowing for abrupt changes in trend parameters:
1. **Crash Model (Level Shift)**: An abrupt vertical jump in the trend intercept:
   $$Y_t = \alpha_1 + (\alpha_2 - \alpha_1) D_U(t) + \beta t + \epsilon_t$$
   where $D_U(t) = 1$ if $t > T_B$ (break date) and $0$ otherwise.
2. **Changing Growth Model (Slope Break)**: A permanent shift in the trend slope:
   $$Y_t = \alpha + \beta_1 t + (\beta_2 - \beta_1) D_T(t) + \epsilon_t$$
   where $D_T(t) = t - T_B$ if $t > T_B$ and $0$ otherwise.
3. **Combined Model (Simultaneous Jump and Slope Rotation)**.

Perron established that when major macroeconomic shocks are modeled as structural breaks, many aggregate economic time series revert to trend-stationarity, demonstrating that secular trends consist of long periods of steady growth punctuated by rare structural regime shifts.


---

## State-Space Representation and Kalman Filtering in Trend Estimation

While classical moving averages and polynomial trends operate as static descriptive smoothers, modern macroeconomic forecasting relies on **State-Space Models** and the **Kalman Filter** (Rudolf E. Kálmán, 1960). State-space models treat secular trend and seasonality as unobserved dynamic state variables that evolve stochastically over time, updating parameter estimates recursively as new real-time economic data arrive.

### 1. The Local Linear Trend Model
In Andrew Harvey's structural time series framework, a univariate economic series $Y_t$ is decomposed into an unobserved stochastic level $\mu_t$ and a stochastic slope $\beta_t$:

- **Measurement (Observation) Equation**:
  $$Y_t = \mu_t + \epsilon_t, \quad \epsilon_t \sim \text{NID}(0, \sigma_\epsilon^2)$$
  The observed economic variable $Y_t$ reflects the true underlying trend level $\mu_t$ plus irregular white-noise measurement error $\epsilon_t$.
- **State Transition Equations**:
  $$\mu_{t+1} = \mu_t + \beta_t + \eta_t, \quad \eta_t \sim \text{NID}(0, \sigma_\eta^2)$$
  $$\beta_{t+1} = \beta_t + \zeta_t, \quad \zeta_t \sim \text{NID}(0, \sigma_\zeta^2)$$
  The trend level advances by the slope increment $\beta_t$ plus an unexpected level shock $\eta_t$. The slope parameter itself evolves as a random walk driven by slope disturbances $\zeta_t$.

### 2. Recursive Kalman Filter Algorithm
The Kalman filter estimates the optimal conditional expectation of the unobserved state vector $\alpha_t = [\mu_t, \beta_t]^T$ given information available up to time $t-1$ (prediction step) and updates it once $Y_t$ is observed (correction step):

1. **Prediction Step**:
   $$\alpha_{t|t-1} = T \alpha_{t-1|t-1}$$
   $$P_{t|t-1} = T P_{t-1|t-1} T^T + Q$$
   where $T = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$, $P$ is the state error covariance matrix, and $Q = \text{diag}(\sigma_\eta^2, \sigma_\zeta^2)$ is the disturbance covariance matrix.
2. **Measurement Prediction Error (Innovation)**:
   $$v_t = Y_t - Z \alpha_{t|t-1}, \quad F_t = Z P_{t|t-1} Z^T + \sigma_\epsilon^2$$
   where $Z = [1, \; 0]$.
3. **Updating Step (Kalman Gain Correction)**:
   $$K_t = P_{t|t-1} Z^T F_t^{-1}$$
   $$\alpha_{t|t} = \alpha_{t|t-1} + K_t v_t$$
   $$P_{t|t} = (I - K_t Z) P_{t|t-1}$$

The **Kalman Gain ($K_t$)** dictates how heavily the filter adjusts the estimated secular trend in response to real-time surprise innovations $v_t$. If measurement noise is high ($\sigma_\epsilon^2$ large), $K_t$ is small, and the filter smooths through the shock. If trend volatility is high, $K_t$ is large, allowing the trend line to bend quickly to structural economic transitions.


---

## Fourier Flexible Form Detrending in Nonlinear Series

When long-term economic time series exhibit smooth, non-linear structural transitions that cannot be adequately captured by low-degree polynomials or rigid break dates, econometricians employ the **Fourier Flexible Form Detrending Approach** (A. Ronald Gallant, 1981; Walter Enders and Junsoo Lee, 2012).

### Mathematical Specification
The secular trend is specified as a linear combination of a deterministic polynomial drift and a finite trigonometric Fourier series:

$$T_t = \alpha_0 + \beta t + \sum_{k=1}^{F} \left[ \gamma_k \sin\left( \frac{2\pi k t}{N} \right) + \delta_k \cos\left( \frac{2\pi k t}{N} \right) \right]$$

where:
- $N$ is the total sample size.
- $k$ represents the integer frequency of the oscillation ($k = 1, 2, \dots$).
- $F$ is the maximum number of cumulative harmonic frequencies.

### Theoretical Advantages:
1. **Universal Approximation**: By the Stone-Weierstrass theorem, a Fourier series can approximate any arbitrary, smooth, continuous non-linear function to any desired degree of precision.
2. **Smooth Break Modeling**: Instead of imposing discontinuous, knife-edge dummy variable break dates (which often cause severe pre-test bias), low-frequency Fourier terms ($k = 1$ or $k = 2$) trace out smooth, gradual structural regime transitions across decades (such as post-war industrial reconstruction or gradual digital automation).
3. **Model Selection**: Econometricians select the optimal harmonic frequency $k^*$ by minimizing the Bayesian Information Criterion (BIC) or Akaike Information Criterion (AIC), providing a data-driven, non-parametric secular trend line that preserves degrees of freedom.

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
N a_q + c_q \sum x_t^2 = \sum Y_t \
a_q \sum x_t^2 + c_q \sum x_t^4 = \sum x_t^2 Y_t
\end{cases} \implies \begin{cases}
7 a_q + 28 c_q = 894.5 \
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
$$S_1 = \sum_{t=0}^{m-1} (k + a b^t) = m k + a \left( \frac{1 - b^m}{1 - b} 
\right)$$
$$S_2 = \sum_{t=m}^{2m-1} (k + a b^t) = m k + a b^m \left( \frac{1 - b^m}{1 - b} 
\right)$$
$$S_3 = \sum_{t=2m}^{3m-1} (k + a b^t) = m k + a b^{2m} \left( \frac{1 - b^m}{1 - b} 
\right)$$

Taking successive differences to eliminate the constant term $m k$:
$$D_1 = S_2 - S_1 = a (b^m - 1) \left( \frac{1 - b^m}{1 - b} 
\right) = - a \frac{(1 - b^m)^2}{1 - b} = a \frac{(b^m - 1)^2}{1 - b}$$
$$D_2 = S_3 - S_2 = a b^m \frac{(b^m - 1)^2}{1 - b}$$

Taking the ratio of the two differences:
$$\frac{D_2}{D_1} = \frac{S_3 - S_2}{S_2 - S_1} = b^m$$

Hence, the parameter $b$ is given by:
$$b = \left( \frac{S_3 - S_2}{S_2 - S_1} 
\right)^{1/m}$$

Once $b$ is determined, parameter $a$ is recovered from $D_1$:
$$a = \frac{(S_2 - S_1)(b - 1)}{(b^m - 1)^2} = \frac{(S_2 - S_1)(b - 1)}{(b^m - 1)(b^m - 1)}$$
More directly:
$$S_2 - S_1 = a b^0 (b^m - 1) \frac{b^m - 1}{b - 1} \implies a = \frac{(S_2 - S_1)(1 - b)}{(1 - b^m)^2} \times (-1) = \frac{(S_2 - S_1)(b - 1)}{(1 - b^m)^2}$$

Finally, parameter $k$ is obtained from $S_1$:
$$k = \frac{1}{m} \left[ S_1 - a \left( \frac{1 - b^m}{1 - b} 
\right) 
\right]$$

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
   $$a \left( \frac{1 - b^3}{1 - b} 
\right) = -44.78 \times 2.4518 \approx -109.79$$
   $$S_1 - a \left( \frac{1 - b^3}{1 - b} 
\right) = 66.8 - (-109.79) = 66.8 + 109.79 = 176.59$$
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
