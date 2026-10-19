# Unit 4: Measurement of Seasonal Variations & Cyclical Fluctuations

## The Economics and Mechanics of Seasonality

Seasonal variations represent repetitive, intra-annual periodic patterns that recur systematically within fixed intervals—such as months, quarters, weeks, or days. In economic analysis, identifying and isolating seasonality is vital for two distinct analytical purposes:
1. **Deseasonalization (Seasonal Adjustment)**: Removing recurring calendar distortions from raw economic data so that underlying cyclical expansions, contractions, and structural trends can be evaluated in real time without being obscured by predictable holiday rushes or winter slowdowns.
2. **Operational Planning**: Exploiting known seasonal patterns to optimize inventory procurement, logistics scheduling, agricultural storage, electrical peak-load generation, and working capital cash reserves.

Seasonality stems from two primary drivers:
- **Natural and Climatic Factors**: Agricultural sowing and harvesting calendars, winter heating demand, summer cooling surges, and weather constraints on maritime shipping and civil construction.
- **Institutional and Social Conventions**: Calendar milestones such as tax filing deadlines, school calendar reopenings, holiday shopping surges (Black Friday, Christmas), and religious festivals (Eid-ul-Fitr, Diwali).

To quantify seasonal effects, statisticians construct **Seasonal Indices**. In the multiplicative model ($Y_t = T_t 	imes S_t 	imes C_t 	imes I_t$), a seasonal index is expressed as a percentage centered on 100%. An index of 115% for the fourth quarter indicates that seasonal factors elevate fourth-quarter activity by 15% above the annual baseline, while an index of 82% for the first quarter reflects an 18% seasonal contraction.

---

## Classical Methods for Estimating Seasonal Indices

Over the past century, several statistical methodologies have been developed to isolate seasonal factors from time series.

### 1. The Method of Simple Averages
The method of simple averages is the most rudimentary procedure for estimating seasonal indices. It assumes that the time series contains no secular trend ($T_t = 	ext{constant}$) or that the trend has already been removed.

The algorithm proceeds as follows:
1. Arrange the data in a two-dimensional grid of $Y_{y,s}$, where rows denote years ($y = 1, \dots, K$) and columns denote seasons ($s = 1, \dots, m$, where $m=4$ for quarters, $m=12$ for months).
2. Compute the unweighted arithmetic mean for each seasonal column across all $K$ years:
   $$ar{Y}_s = rac{1}{K} \sum_{y=1}^{K} Y_{y,s}$$
3. Compute the grand mean across all seasons:
   $$ar{Y} = rac{1}{m} \sum_{s=1}^{m} ar{Y}_s$$
4. Compute the unadjusted seasonal index for season $s$:
   $$	ilde{S}_s = rac{ar{Y}_s}{ar{Y}} 	imes 100$$
5. Because $\sum_{s=1}^{m} 	ilde{S}_s$ must equal $100m$, apply a normalization factor $k = rac{100m}{\sum 	ilde{S}_s}$ to obtain normalized seasonal indices:
   $$S_s = k 	imes 	ilde{S}_s$$

**Theoretical Flaw**: If the time series possesses an upward secular trend, later seasons within each year will consistently register higher values solely due to trend growth rather than genuine seasonal demand. Consequently, the simple averages method produces upwardly biased indices for late calendar seasons.

### 2. The Ratio-to-Trend (Percentage-to-Trend) Method
The ratio-to-trend method explicitly corrects for secular trend by fitting a parametric trend line (linear, polynomial, or exponential) to the original series.

1. Fit an OLS trend equation $T_t = a + b t$ to the raw series.
2. Compute the estimated trend value $T_t$ for every observation period.
3. In a multiplicative model, divide the observed value by its trend value:
   $$R_t = rac{Y_t}{T_t} = rac{T_t 	imes S_t 	imes C_t 	imes I_t}{T_t} = S_t 	imes C_t 	imes I_t$$
   The resulting ratio $R_t$ isolates the combined seasonal, cyclical, and irregular component.
4. Group the ratios by season across years and compute the median or trimmed mean for each season, effectively neutralizing cyclical and random outliers.
5. Normalize the seasonal indices to sum to $100m$.

While superior to simple averages, the ratio-to-trend method depends heavily on the correctness of the fitted trend specification. If the true trend is non-linear and an OLS linear trend is imposed, trend misspecification leaks directly into the seasonal ratios.

### 3. The Ratio-to-Moving Average Method (The Benchmark Approach)
The **Ratio-to-Moving Average** method (formalized by the National Bureau of Economic Research and serving as the mathematical bedrock for the U.S. Census Bureau's X-11, X-12-ARIMA, and X-13ARIMA-SEATS procedures) is the most robust, non-parametric decomposition technique.

Instead of imposing a parametric trend curve, it utilizes a Centered Moving Average ($	ext{CMA}_t$) to filter out both seasonal and high-frequency irregular variations simultaneously, leaving a clean estimate of the combined trend-cycle component:
$$	ext{CMA}_t pprox T_t 	imes C_t$$

The ratio of observed data to the centered moving average yields:
$$z_t = rac{Y_t}{	ext{CMA}_t} = rac{T_t 	imes S_t 	imes C_t 	imes I_t}{T_t 	imes C_t} = S_t 	imes I_t$$

The ratio $z_t$ isolates the pure seasonal and irregular fluctuations. By averaging these ratios across multiple years for each specific season using a modified mean or median, random shocks ($I_t$) cancel out, isolating the pure seasonal index $S_s$.

---

## The Link Relative Method (Karl Pearson)

Developed by Karl Pearson, the **Link Relative Method** measures period-to-period relative changes without requiring explicit trend fitting or moving average centering.

1. **Calculate Link Relatives**: For each observation, calculate the percentage ratio relative to the immediately preceding period:
   $$	ext{LR}_t = rac{Y_t}{Y_{t-1}} 	imes 100$$
2. **Seasonal Link Relative Averages**: For each season $s$, compute the arithmetic mean or median of the link relatives across all available years: $\overline{	ext{LR}}_s$.
3. **Chaining to Base Period**: Choose Season 1 as the arbitrary base ($	ext{CR}_1 = 100$). Convert the seasonal link relatives into **Chain Relatives** ($	ext{CR}_s$) relative to Season 1:
   $$	ext{CR}_2 = rac{\overline{	ext{LR}}_2 	imes 	ext{CR}_1}{100} = \overline{	ext{LR}}_2$$
   $$	ext{CR}_3 = rac{\overline{	ext{LR}}_3 	imes 	ext{CR}_2}{100}$$
   $$	ext{CR}_m = rac{\overline{	ext{LR}}_m 	imes 	ext{CR}_{m-1}}{100}$$
4. **Closing the Loop and Estimating Trend Discrepancy**: Chaining the link relative of Season 1 back from Season $m$ yields a new estimate for Season 1:
   $$	ext{CR}_1' = rac{\overline{	ext{LR}}_1 	imes 	ext{CR}_m}{100}$$
   If the series has no secular trend, $	ext{CR}_1'$ equals 100. If an upward trend exists, $	ext{CR}_1' > 100$. The excess difference $\Delta = 	ext{CR}_1' - 100$ reflects cumulative secular growth over the course of the year.
5. **Trend Correction**: Distribute the cumulative discrepancy evenly across the seasons. The linear trend adjustment factor is:
   $$d = rac{	ext{CR}_1' - 100}{m}$$
   The trend-corrected chain relatives ($	ext{CCR}_s$) are:
   $$	ext{CCR}_s = 	ext{CR}_s - (s - 1) d, \quad s = 1, 2, \dots, m$$
6. **Normalization**: Normalize $	ext{CCR}_s$ so that the average seasonal index across all $m$ seasons is exactly 100%:
   $$S_s = rac{	ext{CCR}_s}{rac{1}{m} \sum_{j=1}^{m} 	ext{CCR}_j} 	imes 100$$

---

## Cyclical Fluctuations: The Residual Method and Business Cycles

Once secular trend ($T_t$) and seasonal indices ($S_t$) have been estimated, cyclical oscillations ($C_t$) can be isolated via the **Residual Method**.

In the multiplicative model:
$$	ext{Deseasonalized Series } D_t = rac{Y_t}{S_t} = T_t 	imes C_t 	imes I_t$$
Dividing the deseasonalized series by the secular trend $T_t$ yields the cyclical-irregular residual:
$$rac{D_t}{T_t} = rac{Y_t}{T_t 	imes S_t} = C_t 	imes I_t$$

Expressed as a percentage:
$$	ext{Cyclical Residual } \% = \left( rac{Y_t}{T_t 	imes S_t} 
ight) 	imes 100$$

To purge high-frequency irregular noise ($I_t$) from the cyclical-irregular residual, economists apply a short weighted moving average filter (such as a 3-month or 5-quarter Spencer/Henderson smoothing filter), isolating the underlying business cycle trajectory $C_t$.

### NBER Reference Cycles and Turning Points
Following the foundational methodology of Arthur Burns and Wesley Clair Mitchell at the National Bureau of Economic Research (NBER), the cyclical component is decomposed into recurring phases demarcated by specific turning points:
- **Peak**: The cyclical maximum signaling the end of an expansion and the onset of contraction.
- **Contraction (Recession)**: A broad, sustained decline in economic activity across multiple sectors, lasting from peak to trough.
- **Trough**: The cyclical minimum marking the end of recession and the initiation of recovery.
- **Expansion**: The upward phase from trough to subsequent peak.

---


---

## Advanced Seasonal Adjustment: The Census X-13ARIMA-SEATS Architecture

While the classical Ratio-to-Moving Average method established the conceptual foundation of seasonal decomposition, contemporary national statistical offices rely on sophisticated algorithmic suites, primarily the U.S. Census Bureau's **X-13ARIMA-SEATS** program (combining the empirical X-11/X-12 moving average filters with the European SEATS model-based ARIMA signal extraction).

### 1. The Multi-Stage X-11 Filtering Pipeline
The X-11 algorithm operates through an iterative, cascading sequence of moving average filters designed to separate trend-cycle, seasonal, and irregular components while isolating extreme outliers:

1. **Step 1: Preliminary Trend-Cycle Estimation**:
   A 12-month (or 4-quarter) centered moving average is fitted to raw data $Y_t$ to produce a preliminary trend-cycle estimate $T_t^{(1)}$.
2. **Step 2: Preliminary Seasonal-Irregular Ratios**:
   In a multiplicative model, ratios $SI_t^{(1)} = Y_t / T_t^{(1)}$ are computed.
3. **Step 3: Preliminary Seasonal Filtering via $3 \times 3$ Moving Average**:
   To isolate preliminary seasonal factors from $SI_t^{(1)}$, a weighted 5-term moving average (a 3-term average of a 3-term average, denoted $3 \times 3$) is computed separately for each calendar month across years:
   $$S_t^{(1)} = \frac{1}{9} SI_{t-24} + \frac{2}{9} SI_{t-12} + \frac{3}{9} SI_t + \frac{2}{9} SI_{t+12} + \frac{1}{9} SI_{t+24}$$
4. **Step 4: Preliminary Deseasonalization**:
   The raw series is divided by the normalized seasonal factor: $D_t^{(1)} = Y_t / S_t^{(1)}$.
5. **Step 5: Refined Trend Extraction via the Henderson Filter**:
   The Henderson moving average filter (typically 13 terms for monthly data, with specialized symmetric cubic-preserving weights) is applied to $D_t^{(1)}$ to generate an improved trend-cycle estimate $T_t^{(2)}$.
6. **Step 6: Iterative Convergence and Outlier Downweighting**:
   Ratios $SI_t^{(2)} = Y_t / T_t^{(2)}$ are scrutinized for extreme outliers exceeding $2.5\sigma$. Outliers are replaced with modified values, and a wider $3 \times 5$ or $3 \times 9$ seasonal filter is deployed, yielding final seasonal indices $S_t^*$ and deseasonalized series $D_t^*$.

### 2. Calendar and Working-Day Adjustments
Raw macroeconomic figures are distorted not only by seasonal weather, but by calendar mechanics:
- **Trading Day / Working Day Variations**: Different months contain varying numbers of Mondays, Fridays, or weekend days. If a month contains five Saturdays and five Sundays, retail sales or construction activity will diverge sharply from a month with five working weekdays.
- **Moving Holiday Effects**: Major religious and cultural holidays (such as Easter, Chinese New Year, Passover, and Eid) shift across calendar months from year to year. X-13ARIMA models these events using regression variables with ARIMA errors (RegARIMA), estimating holiday coefficients prior to seasonal decomposition.

---

## Frequency-Domain Spectral Analysis of Seasonality

In mathematical statistics, seasonality can be analyzed in the frequency domain via **Spectral Density Analysis**. A covariance-stationary time series $Y_t$ possesses an autocovariance function $\gamma(k) = \text{Cov}(Y_t, Y_{t-k})$.
The **Spectral Density Function** $f(\omega)$ is the Fourier transform of the autocovariance sequence:

$$f(\omega) = \frac{1}{2\pi} \left[ \gamma(0) + 2 \sum_{k=1}^{\infty} \gamma(k) \cos(\omega k) \right], \quad \omega \in [0, \pi]$$

where $\omega$ denotes angular frequency in radians per unit time. The area under the spectral density function over any frequency band represents the proportion of total series variance generated by oscillations in that frequency band.

### Detecting Seasonal Harmonics
For monthly time series, annual seasonality corresponds to a fundamental cycle of period 12 months, corresponding to angular frequency:
$$\omega_1 = \frac{2\pi}{12} = \frac{\pi}{6} \approx 0.5236 \text{ radians}$$

Non-sinusoidal seasonal patterns also generate sharp spectral spikes at the harmonic frequencies:
- $\omega_2 = 2 \times \frac{2\pi}{12} = \frac{2\pi}{6}$ (6-month semi-annual harmonic)
- $\omega_3 = 3 \times \frac{2\pi}{12} = \frac{\pi}{2}$ (4-month quarterly harmonic)
- $\omega_4 = 4 \times \frac{2\pi}{12} = \frac{2\pi}{3}$ (3-month harmonic)
- $\omega_5 = 5 \times \frac{2\pi}{12} = \frac{5\pi}{6}$ (2.4-month harmonic)
- $\omega_6 = \pi$ (2-month bi-monthly harmonic)

A properly deseasonalized economic time series must display a smooth spectral density function devoid of prominent peaks at these six canonical seasonal harmonic frequencies.


---

## Seasonal Unit Roots: The HEGY Statistical Framework

Just as annual time series can exhibit non-stationary stochastic trends, seasonal quarterly or monthly series can exhibit **Stochastic Seasonality**—where the seasonal pattern itself evolves randomly over time rather than remaining fixed.

In 1990, Svend Hylleberg, Robert Engle, Clive Granger, and Byung Sam Yoo developed the celebrated **HEGY Test** for seasonal unit roots in quarterly time series.

### The Seasonal Lag Operator Polynomial
For a quarterly series, the annual seasonal differencing operator is:

$$\Delta_4 Y_t = Y_t - Y_{t-4} = (1 - L^4) Y_t$$

Factoring the fourth-degree polynomial $(1 - L^4)$ into its roots:

$$1 - L^4 = (1 - L)(1 + L)(1 + L^2) = (1 - L)(1 + L)(1 - iL)(1 + iL)$$

This factorization reveals four distinct unit roots located on the complex unit circle, each corresponding to a specific frequency:
1. **Zero Frequency Root ($L = 1$)**: The standard non-seasonal long-run unit root (governing secular trend drift).
2. **Semi-Annual Frequency Root ($L = -1$)**: Cycles with period 2 quarters (6 months), angular frequency $\omega = \pi$.
3. **Annual Complex Roots ($L = \pm i$)**: Cycles with period 4 quarters (12 months), angular frequency $\omega = \pm \pi/2$.

The HEGY regression model filters the series into four orthogonal components:
$$\Delta_4 Y_t = \pi_1 y_{1, t-1} + \pi_2 y_{2, t-1} + \pi_3 y_{3, t-1} + \pi_4 y_{3, t-2} + \sum_{k=1}^{p} \phi_k \Delta_4 Y_{t-k} + \epsilon_t$$

where:
- $y_{1t} = (1 + L + L^2 + L^3) Y_t$ (filters out all seasonal roots, preserving zero frequency).
- $y_{2t} = -(1 - L + L^2 - L^3) Y_t$ (preserves semi-annual frequency).
- $y_{3t} = -(1 - L^2) Y_t$ (preserves annual frequency).

Testing $\pi_1 = 0$ tests for a zero-frequency unit root, $\pi_2 = 0$ tests for a semi-annual unit root, and a joint $F$-test on $\pi_3 = \pi_4 = 0$ tests for annual seasonal unit roots. If seasonal unit roots exist, standard dummy variable seasonal adjustment is statistically invalid, and seasonal differencing must be performed.

---

## Early Warning Composite Leading Indicators and Turning Point Forecasting

To forecast macroeconomic business cycle turning points before they appear in lagging GDP data, economic institutions construct **Composite Leading Indicators (CLI)** based on the methodology pioneered by Wesley Mitchell and Arthur Burns at the NBER.

### 1. Classification of Macroeconomic Indicators
- **Leading Indicators**: Variables whose cyclical peaks and troughs consistently precede aggregate GDP turning points by 3 to 12 months. Key leading indicators include:
  - New manufacturing export orders.
  - Housing permits and residential building starts.
  - Stock market equity indices (e.g., S&P 500).
  - Yield curve term spread (10-year Treasury bond yield minus 3-month Treasury bill yield).
  - Consumer confidence and manufacturer sentiment surveys (PMI).
- **Coincident Indicators**: Variables that move in tandem with aggregate GDP (industrial production, real personal income less transfers, non-farm payroll employment, retail trade sales).
- **Lagging Indicators**: Variables that reach turning points several months after the economy has already turned (average duration of unemployment, prime lending rates, commercial loan balances, unit labor costs).

### 2. The Conference Board Aggregation Algorithm
The composite leading index is constructed through standardized steps:
1. Compute period-to-period percent changes $r_{it}$ for each component series.
2. Standardize each component by dividing by its long-run historical standard deviation $s_i$:
   $$v_{it} = \frac{r_{it}}{s_i}$$
3. Compute the unweighted or weighted average of the standardized movements:
   $$R_t = \sum_{i=1}^{m} w_i v_{it}$$
4. Standardize the composite sum $R_t$ and chain-link it to create the continuous Composite Leading Indicator index.

### 3. Hamilton's Markov-Switching Business Cycle Model
In 1989, James Hamilton formulated a non-linear regime-switching model capturing the asymmetric dynamics of expansions and contractions:

$$Y_t = \mu_{S_t} + \phi (Y_{t-1} - \mu_{S_{t-1}}) + \epsilon_t$$

where $S_t \in \{0, 1\}$ is an unobserved discrete state variable:
- $S_t = 0$: Economic Contraction / Recession (with mean growth $\mu_0 < 0$).
- $S_t = 1$: Economic Expansion / Boom (with mean growth $\mu_1 > 0$).

The transition between regimes follows a first-order Markov chain governed by constant transition probabilities:
$$p_{00} = P(S_t = 0 \mid S_{t-1} = 0), \quad p_{11} = P(S_t = 1 \mid S_{t-1} = 1)$$

Using maximum likelihood via the Hamilton filter, economists calculate the real-time probability that an economy has slipped into recession: $P(S_t = 0 \mid \Omega_t)$, providing policymakers with objective probabilistic recession nowcasts.


---

## Real-Time Macroeconomic Nowcasting with Mixed-Frequency Data

Central banks and economic ministries face a persistent informational timing mismatch: while key macroeconomic aggregates like Gross Domestic Product (GDP) are published with a lag of several months and only at quarterly frequencies, financial markets, industrial sensors, and consumer transaction systems generate daily, weekly, and monthly data in real time.
To bridge this gap, modern economic statistics deploys **Macroeconomic Nowcasting**.

### 1. Mixed Data Sampling (MIDAS) Regressions
Introduced by Eric Ghysels (2004), **MIDAS Regressions** allow researchers to regress a low-frequency dependent variable (quarterly GDP growth, $Y_t$) directly on high-frequency explanatory variables (monthly industrial production, weekly unemployment claims, daily bond yields, $X_t^{(m)}$) without first aggregating the high-frequency series into arbitrary quarterly averages.

A standard MIDAS model is formulated as:

$$Y_t = \beta_0 + \beta_1 B(L^{1/m}; \theta) X_t^{(m)} + \epsilon_t$$

where:
- $L^{1/m}$ is a fractional lag operator such that $L^{j/m} X_t^{(m)} = X_{t - j/m}^{(m)}$.
- $B(L^{1/m}; \theta) = \sum_{j=0}^{K} w(j; \theta) L^{j/m}$ is a distributed lag polynomial governed by a parsimonious parameter vector $\theta$.
- Common weighting functions include the **Exponential Almon Polynomial**:
  $$w(j; \theta_1, \theta_2) = \frac{\exp(\theta_1 j + \theta_2 j^2)}{\sum_{k=0}^{K} \exp(\theta_1 k + \theta_2 k^2)}$$
  and the **Beta Density Lag Function**.

By estimating smooth non-linear lag weights, MIDAS extracts predictive signals from the most recent high-frequency intra-quarter data points, updating the nowcast of current-quarter GDP as new high-frequency data arrive.

### 2. Dynamic Factor Models (DFM)
Formalized by Domenico Giannone, Lucrezia Reichlin, and David Small (2008), the **Dynamic Factor Model (DFM)** extracts a small number of unobserved common macroeconomic latent factors $f_t$ from hundreds of heterogeneous economic time series:

$$X_{i,t} = \lambda_i^T f_t + e_{i,t}$$
$$f_t = A f_{t-1} + u_t$$

where $\lambda_i$ is the factor loading vector and $e_{i,t}$ is idiosyncratic series-specific noise.
Using state-space Kalman filtering under missing data patterns ("ragged edges"), the DFM processes incoming monthly and weekly economic news releases, continuously computing the news contribution of each statistical release to the updated GDP estimate.


---

## Band-Pass Frequency Filtering: Baxter-King and Christiano-Fitzgerald Filters

In modern empirical macroeconomics, the classical Burns and Mitchell definition of a business cycle corresponds to fluctuations in economic activity with periodicities ranging between **6 quarters (1.5 years)** and **32 quarters (8 years)**. Fluctuations with periodicities shorter than 6 quarters are classified as high-frequency irregular noise or seasonal remnants, while fluctuations lasting longer than 8 years reflect low-frequency secular trends.

To isolate this precise economic frequency band without distorting phase timing, econometricians employ **Band-Pass Frequency Filters**.

### 1. The Ideal Band-Pass Filter
In the frequency domain, an ideal band-pass filter possesses a frequency response function that equals 1 inside the pass-band $[\omega_L, \omega_U]$ and 0 outside:

$$\alpha(\omega) = \begin{cases} 1, & \omega_L \le |\omega| \le \omega_U \\ 0, & \text{otherwise} \end{cases}$$

where $\omega_L = \frac{2\pi}{32} \approx 0.1963$ radians and $\omega_U = \frac{2\pi}{6} \approx 1.0472$ radians.

The inverse Fourier transform yields the theoretical infinite-order symmetric time-domain filter weights:

$$a_j = \begin{cases} \frac{\omega_U - \omega_L}{\pi}, & j = 0 \\ \frac{\sin(\omega_U j) - \sin(\omega_L j)}{\pi j}, & j = \pm 1, \pm 2, \dots \end{cases}$$

Applying the ideal filter requires infinite historical and future data: $y_t^* = \sum_{j=-\infty}^{\infty} a_j y_{t-j}$. Because finite samples cannot implement an infinite filter, finite approximations must be constructed.

### 2. The Baxter-King (BK) Filter
Marianne Baxter and Robert King (1999) proposed an optimal finite approximation by truncating the infinite filter at a symmetric lag lead length $K$ (typically $K = 12$ quarters for quarterly data):

$$\min_{\{\hat{a}_j\}} \int_{-\pi}^{\pi} |\alpha(\omega) - \hat{\alpha}(\omega)|^2 d\omega \quad \text{subject to } \hat{\alpha}(0) = \sum_{j=-K}^{K} \hat{a}_j = 0$$

The zero-frequency constraint $\sum \hat{a}_j = 0$ guarantees that the BK filter completely eliminates any linear or deterministic trend from the series, rendering non-stationary $I(1)$ series stationary without introducing phase shift distortions.
However, because the filter is symmetric, it results in the loss of $K$ observations at the beginning and $K$ observations at the end of the sample (a loss of 3 years of data at each boundary).

### 3. The Christiano-Fitzgerald (CF) Full-Sample Asymmetric Filter
To prevent data loss at sample boundaries, Lawrence Christiano and Terry Fitzgerald (2003) developed an asymmetric filter that computes cyclical estimates across the entire sample period $t = 1, \dots, T$.
Under the assumption that the time series follows a random walk with drift ($y_t = \mu + y_{t-1} + \epsilon_t$), the CF filter computes time-varying weights $\hat{b}_{j,t}$ that minimize the mean squared approximation error conditional on all available observations:

$$y_t^{\text{CF}} = \sum_{j=-(T-t)}^{t-1} \hat{b}_{j,t} y_{t+j}$$

At the center of a long series, the CF filter approaches the symmetric Baxter-King weights; at the sample boundaries (such as the most recent quarter), the filter uses asymmetric weights, eliminating endpoint data loss and enabling real-time business cycle monitoring for central banks.


---

## The Bry-Boschan Business Cycle Dating Algorithm

While parametric and econometric filters smooth time series, national statistical committees—most notably the NBER Business Cycle Dating Committee in the United States and the CEPR Business Cycle Dating Committee in Europe—formally date the peaks and troughs of economic business cycles using objective, non-parametric turning point algorithms. The international benchmark for programmatic cycle dating is the **Bry-Boschan Algorithm** (Gerhard Bry and Charlotte Boschan, 1971).

### 1. Algorithmic Architecture
Operating on seasonally adjusted monthly or quarterly time series (such as real personal income, industrial production, and payroll employment), the algorithm identifies local extrema through a hierarchical screening sequence:

1. **Step 1: Outlier Replacement and Extreme Value Smoothing**:
   Spurious spikes attributable to severe weather strikes or statistical anomalies are identified via a Spencer moving average and replaced with modified values.
2. **Step 2: Initial Turning Point Identification on 12-Month Moving Average**:
   Potential peaks and troughs are identified on a smooth 12-month moving average of the series. A month $t$ is identified as a candidate peak if its value exceeds all values within a 5-month symmetric neighborhood:
   $$Y_t > Y_{t \pm k}, \quad k = 1, 2, \dots, 5$$
   Similarly, a candidate trough is identified if $Y_t < Y_{t \pm k}$.
3. **Step 3: Refinement on Intermediate Henderson Curves**:
   The candidate turning points are mapped onto a shorter Henderson moving average filter (e.g., 7-term or 9-term), searching within $\pm 4$ months of the Step 2 dates to ensure that the turning point reflects the genuine turning apex rather than filter distortion.
4. **Step 4: Final Pinpointing on the Deseasonalized Series**:
   The turning point date is transferred to the unsmoothed deseasonalized economic series, selecting the absolute local maximum or minimum within a neighborhood of the Henderson turning point.

### 2. Censoring and Duration Constraints
To ensure economic credibility and conformity with classical business cycle theory, the algorithm enforces strict duration and alternation rules:
- **Alternation Constraint**: Peaks and troughs must strictly alternate. If two consecutive peaks occur without an intervening trough, the lower peak is eliminated.
- **Phase Duration Constraint**: The minimum duration of an economic phase (from peak to trough, or from trough to peak) must be at least **5 months (or 2 quarters)**. Shorter dips are classified as pause corrections rather than full recessions.
- **Full Cycle Duration Constraint**: The minimum duration of a complete cycle (from peak to peak, or from trough to trough) must be at least **15 months (or 5 quarters)**.
- **Boundary Censoring**: No turning point can be placed within the first 6 months or last 6 months of a time series, preventing unstable nowcast revisions at sample boundaries.


---

## The Beveridge-Nelson Trend-Cycle Decomposition

In macroeconomic time series analysis, Stephen Beveridge and Charles Nelson (1981) introduced a fundamental model-based decomposition that defines the secular trend of an integrated time series strictly in terms of long-horizon conditional expectations.

### 1. Conceptual Definition of the Beveridge-Nelson Trend
Consider a time series $Y_t$ that is stationary in first differences: $\Delta Y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \dots = \mu + C(L) \epsilon_t$, where $C(L) = \sum_{j=0}^{\infty} c_j L^j$ is an invertible moving-average lag polynomial with $c_0 = 1$.

Beveridge and Nelson defined the **Secular Trend ($T_t$)** at time $t$ as the long-horizon forecast of the level of the series, adjusted for the deterministic drift rate $\mu$:

$$T_t = \lim_{k \to \infty} \left[ E_t(Y_{t+k}) - k \mu \right]$$

The trend represents the level the economic series would reach once all transient, self-reversing cyclical shocks have completely dissipated.

### 2. Derivation of the Trend and Cyclical Components
Decomposing the lag polynomial via the algebraic polynomial identity:
$$C(L) = C(1) + (1 - L) C^*(L)$$
where $C(1) = \sum_{j=0}^{\infty} c_j$ is the sum of moving average coefficients, and $c_j^* = -\sum_{i=j+1}^{\infty} c_i$.

Substituting into the first-differenced equation:
$$\Delta Y_t = \mu + C(1) \epsilon_t + \Delta C^*(L) \epsilon_t$$

Integrating both sides:
$$Y_t = T_t + C_t$$
where:
- **The Beveridge-Nelson Trend**:
  $$T_t = T_{t-1} + \mu + C(1) \epsilon_t$$
  The secular trend evolves as a pure random walk with constant drift $\mu$ and innovation shock variance $[C(1)]^2 \sigma_\epsilon^2$.
- **The Beveridge-Nelson Cycle**:
  $$C_t = C^*(L) \epsilon_t = -\sum_{j=0}^{\infty} \left( \sum_{i=j+1}^{\infty} c_i \right) \epsilon_{t-j}$$
  The cyclical component is a strictly covariance-stationary process.

A vital insight of the Beveridge-Nelson decomposition is that the trend innovation and the cyclical innovation are driven by the **exact same random shock $\epsilon_t$**, meaning that economic shocks alter both the long-run permanent trend and the short-run business cycle simultaneously.

## Worked Questions and Solutions

### Question 1: Seasonal Decomposition via Ratio-to-Moving Average
An agricultural distribution board tracks quarterly grain shipments (in thousands of metric tons) over a four-year period:

| Year | Q1 | Q2 | Q3 | Q4 |
| :---: | :---: | :---: | :---: | :---: |
| **2021** | 72.0 | 118.0 | 90.0 | 58.0 |
| **2022** | 78.0 | 126.0 | 98.0 | 64.0 |
| **2023** | 86.0 | 138.0 | 108.0 | 70.0 |
| **2024** | 92.0 | 148.0 | 116.0 | 76.0 |

1. Compute 4-quarter centered moving averages ($	ext{CMA}_t$) for all eligible quarters.
2. Calculate the seasonal-irregular percentage ratios $z_t = (Y_t / 	ext{CMA}_t) 	imes 100$.
3. Compute the unadjusted seasonal index for each quarter using the arithmetic mean of the available quarterly ratios, apply the normalization factor, and report the final seasonal indices.
4. Deseasonalize the raw shipment data for all four quarters of 2024, and evaluate the underlying economic trend between Q2 and Q3 of 2024.

### Solution, step 1: Computation of Centered Moving Averages
We arrange the 16 observations sequentially ($t = 1, \dots, 16$) and compute 4-quarter moving totals ($	ext{MT}_4$), uncentered moving averages ($M$), and centered moving averages ($	ext{CMA}$):

- **2021**:
  - Q1 ($t=1$): $72.0$
  - Q2 ($t=2$): $118.0$
  - Q3 ($t=3$): $90.0$.
    - $	ext{MT}_{1-4} = 72 + 118 + 90 + 58 = 338.0 \implies M_{2.5} = 84.50$
    - $	ext{MT}_{2-5} = 118 + 90 + 58 + 78 = 344.0 \implies M_{3.5} = 86.00$
    - $	ext{CMA}_3 = rac{84.50 + 86.00}{2} = 85.25$
  - Q4 ($t=4$): $58.0$.
    - $	ext{MT}_{3-6} = 90 + 58 + 78 + 126 = 352.0 \implies M_{4.5} = 88.00$
    - $	ext{CMA}_4 = rac{86.00 + 88.00}{2} = 87.00$

- **2022**:
  - Q1 ($t=5$): $78.0$.
    - $	ext{MT}_{4-7} = 58 + 78 + 126 + 98 = 360.0 \implies M_{5.5} = 90.00$
    - $	ext{CMA}_5 = rac{88.00 + 90.00}{2} = 89.00$
  - Q2 ($t=6$): $126.0$.
    - $	ext{MT}_{5-8} = 78 + 126 + 98 + 64 = 366.0 \implies M_{6.5} = 91.50$
    - $	ext{CMA}_6 = rac{90.00 + 91.50}{2} = 90.75$
  - Q3 ($t=7$): $98.0$.
    - $	ext{MT}_{6-9} = 126 + 98 + 64 + 86 = 374.0 \implies M_{7.5} = 93.50$
    - $	ext{CMA}_7 = rac{91.50 + 93.50}{2} = 92.50$
  - Q4 ($t=8$): $64.0$.
    - $	ext{MT}_{7-10} = 98 + 64 + 86 + 138 = 386.0 \implies M_{8.5} = 96.50$
    - $	ext{CMA}_8 = rac{93.50 + 96.50}{2} = 95.00$

- **2023**:
  - Q1 ($t=9$): $86.0$.
    - $	ext{MT}_{8-11} = 64 + 86 + 138 + 108 = 396.0 \implies M_{9.5} = 99.00$
    - $	ext{CMA}_9 = rac{96.50 + 99.00}{2} = 97.75$
  - Q2 ($t=10$): $138.0$.
    - $	ext{MT}_{9-12} = 86 + 138 + 108 + 70 = 402.0 \implies M_{10.5} = 100.50$
    - $	ext{CMA}_{10} = rac{99.00 + 100.50}{2} = 99.75$
  - Q3 ($t=11$): $108.0$.
    - $	ext{MT}_{10-13} = 138 + 108 + 70 + 92 = 408.0 \implies M_{11.5} = 102.00$
    - $	ext{CMA}_{11} = rac{100.50 + 102.00}{2} = 101.25$
  - Q4 ($t=12$): $70.0$.
    - $	ext{MT}_{11-14} = 108 + 70 + 92 + 148 = 418.0 \implies M_{12.5} = 104.50$
    - $	ext{CMA}_{12} = rac{102.00 + 104.50}{2} = 103.25$

- **2024**:
  - Q1 ($t=13$): $92.0$.
    - $	ext{MT}_{12-15} = 70 + 92 + 148 + 116 = 426.0 \implies M_{13.5} = 106.50$
    - $	ext{CMA}_{13} = rac{104.50 + 106.50}{2} = 105.50$
  - Q2 ($t=14$): $148.0$.
    - $	ext{MT}_{13-16} = 92 + 148 + 116 + 76 = 432.0 \implies M_{14.5} = 108.00$
    - $	ext{CMA}_{14} = rac{106.50 + 108.00}{2} = 107.25$
  - Q3 ($t=15$): $116.0$ (Lost)
  - Q4 ($t=16$): $76.0$ (Lost)

### Solution, step 2: Calculate Seasonal-Irregular Ratios ($z_t = rac{Y_t}{	ext{CMA}_t} 	imes 100$)
- **2021**:
  - Q3: $rac{90.0}{85.25} 	imes 100 pprox 105.57\%$
  - Q4: $rac{58.0}{87.00} 	imes 100 pprox 66.67\%$
- **2022**:
  - Q1: $rac{78.0}{89.00} 	imes 100 pprox 87.64\%$
  - Q2: $rac{126.0}{90.75} 	imes 100 pprox 138.84\%$
  - Q3: $rac{98.0}{92.50} 	imes 100 pprox 105.95\%$
  - Q4: $rac{64.0}{95.00} 	imes 100 pprox 67.37\%$
- **2023**:
  - Q1: $rac{86.0}{97.75} 	imes 100 pprox 87.98\%$
  - Q2: $rac{138.0}{99.75} 	imes 100 pprox 138.35\%$
  - Q3: $rac{108.0}{101.25} 	imes 100 pprox 106.67\%$
  - Q4: $rac{70.0}{103.25} 	imes 100 pprox 67.80\%$
- **2024**:
  - Q1: $rac{92.0}{105.50} 	imes 100 pprox 87.20\%$
  - Q2: $rac{148.0}{107.25} 	imes 100 pprox 138.00\%$

### Solution, step 3: Seasonal Index Averaging and Normalization
We compile the available ratios into quarterly columns and compute the arithmetic mean:

| Year | Q1 | Q2 | Q3 | Q4 |
| :---: | :---: | :---: | :---: | :---: |
| **2021** | — | — | 105.57 | 66.67 |
| **2022** | 87.64 | 138.84 | 105.95 | 67.37 |
| **2023** | 87.98 | 138.35 | 106.67 | 67.80 |
| **2024** | 87.20 | 138.00 | — | — |
| **Mean ($	ilde{S}_s$)** | **87.61%** | **138.40%** | **106.06%** | **67.28%** |

Calculations:
- $ar{S}_{	ext{Q1}} = rac{87.64 + 87.98 + 87.20}{3} = 87.6067 pprox 87.61\%$
- $ar{S}_{	ext{Q2}} = rac{138.84 + 138.35 + 138.00}{3} = 138.3967 pprox 138.40\%$
- $ar{S}_{	ext{Q3}} = rac{105.57 + 105.95 + 106.67}{3} = 106.0633 pprox 106.06\%$
- $ar{S}_{	ext{Q4}} = rac{66.67 + 67.37 + 67.80}{3} = 67.2800 pprox 67.28\%$

Sum of unadjusted seasonal indices:
$$\sum_{s=1}^{4} 	ilde{S}_s = 87.61 + 138.40 + 106.06 + 67.28 = 399.35$$

The sum falls slightly short of the target 400.00. We compute the normalization factor:
$$k = rac{400.00}{399.35} pprox 1.0016276$$

Applying the normalization factor:
- $S_{	ext{Q1}} = 87.6067 	imes 1.0016276 pprox \mathbf{87.75\%}$
- $S_{	ext{Q2}} = 138.3967 	imes 1.0016276 pprox \mathbf{138.62\%}$
- $S_{	ext{Q3}} = 106.0633 	imes 1.0016276 pprox \mathbf{106.24\%}$
- $S_{	ext{Q4}} = 67.2800 	imes 1.0016276 pprox \mathbf{67.39\%}$

Check sum: $87.75 + 138.62 + 106.24 + 67.39 = 400.00\%$.

### Solution, step 4: Deseasonalization of 2024 Data
To deseasonalize observed values, we divide each by its normalized seasonal index:
$$D_t = rac{Y_t}{S_s / 100}$$

For 2024:
- **2024 Q1**:
  $$D_{	ext{Q1}} = rac{92.0}{0.8775} pprox \mathbf{104.84} 	ext{ thousand tons}$$
- **2024 Q2**:
  $$D_{	ext{Q2}} = rac{148.0}{1.3862} pprox \mathbf{106.77} 	ext{ thousand tons}$$
- **2024 Q3**:
  $$D_{	ext{Q3}} = rac{116.0}{1.0624} pprox \mathbf{109.19} 	ext{ thousand tons}$$
- **2024 Q4**:
  $$D_{	ext{Q4}} = rac{76.0}{0.6739} pprox \mathbf{112.78} 	ext{ thousand tons}$$

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

1. Calculate the link relatives ($	ext{LR}_t = rac{Y_t}{Y_{t-1}} 	imes 100$) for every quarterly transition.
2. Determine the arithmetic mean of the link relatives for each of the four quarters.
3. Compute the uncorrected chain relatives ($	ext{CR}_s$) with base Q1 = 100, calculate the loop-closing discrepancy $	ext{CR}_1'$, and evaluate the linear trend correction factor $d$.
4. Compute the trend-corrected chain relatives and normalize them to produce the final quarterly seasonal indices.

### Solution, step 1: Calculation of Link Relatives
The link relative formula is $	ext{LR}_t = rac{Y_t}{Y_{t-1}} 	imes 100$:

- **Year 1**:
  - Q1: Base, no prior quarter.
  - Q2: $rac{45.0}{30.0} 	imes 100 = 150.00\%$
  - Q3: $rac{60.0}{45.0} 	imes 100 pprox 133.33\%$
  - Q4: $rac{25.0}{60.0} 	imes 100 pprox 41.67\%$

- **Year 2**:
  - Q1: $rac{33.0}{25.0} 	imes 100 = 132.00\%$
  - Q2: $rac{50.0}{33.0} 	imes 100 pprox 151.52\%$
  - Q3: $rac{66.0}{50.0} 	imes 100 = 132.00\%$
  - Q4: $rac{28.0}{66.0} 	imes 100 pprox 42.42\%$

- **Year 3**:
  - Q1: $rac{36.0}{28.0} 	imes 100 pprox 128.57\%$
  - Q2: $rac{55.0}{36.0} 	imes 100 pprox 152.78\%$
  - Q3: $rac{72.0}{55.0} 	imes 100 pprox 130.91\%$
  - Q4: $rac{31.0}{72.0} 	imes 100 pprox 43.06\%$

- **Year 4**:
  - Q1: $rac{40.0}{31.0} 	imes 100 pprox 129.03\%$
  - Q2: $rac{61.0}{40.0} 	imes 100 = 152.50\%$
  - Q3: $rac{80.0}{61.0} 	imes 100 pprox 131.15\%$
  - Q4: $rac{34.0}{80.0} 	imes 100 = 42.50\%$

### Solution, step 2: Average Link Relatives
We average the available link relatives for each quarter:

- **Quarter 1** (transitions from preceding year's Q4):
  $$\overline{	ext{LR}}_1 = rac{132.00 + 128.57 + 129.03}{3} = rac{389.60}{3} pprox 129.87\%$$
- **Quarter 2** (transitions from Q1):
  $$\overline{	ext{LR}}_2 = rac{150.00 + 151.52 + 152.78 + 152.50}{4} = rac{606.80}{4} = 151.70\%$$
- **Quarter 3** (transitions from Q2):
  $$\overline{	ext{LR}}_3 = rac{133.33 + 132.00 + 130.91 + 131.15}{4} = rac{527.39}{4} pprox 131.85\%$$
- **Quarter 4** (transitions from Q3):
  $$\overline{	ext{LR}}_4 = rac{41.67 + 42.42 + 43.06 + 42.50}{4} = rac{169.65}{4} pprox 42.41\%$$

### Solution, step 3: Chain Relatives and Trend Discrepancy
Setting Q1 as base ($	ext{CR}_1 = 100.00$):
- $	ext{CR}_1 = 100.00$
- $	ext{CR}_2 = rac{\overline{	ext{LR}}_2 	imes 	ext{CR}_1}{100} = rac{151.70 	imes 100.00}{100} = 151.70$
- $	ext{CR}_3 = rac{\overline{	ext{LR}}_3 	imes 	ext{CR}_2}{100} = rac{131.85 	imes 151.70}{100} pprox 200.02$
- $	ext{CR}_4 = rac{\overline{	ext{LR}}_4 	imes 	ext{CR}_3}{100} = rac{42.41 	imes 200.02}{100} pprox 84.83$

Loop-closing calculation for Q1 of the following year:
$$	ext{CR}_1' = rac{\overline{	ext{LR}}_1 	imes 	ext{CR}_4}{100} = rac{129.87 	imes 84.83}{100} pprox 110.17$$

The new chain relative for Q1 is $110.17$, which exceeds the original base of $100.00$ by:
$$\Delta = 	ext{CR}_1' - 100.00 = 110.17 - 100.00 = 10.17$$

This $+10.17\%$ excess reflects annual secular growth across the four quarters.
We compute the per-quarter linear trend correction factor $d$:
$$d = rac{\Delta}{4} = rac{10.17}{4} pprox 2.5425$$

### Solution, step 4: Trend Correction and Final Seasonal Indices
We adjust the chain relatives by subtracting $(s - 1) d$:
- **Quarter 1 ($s=1$)**:
  $$	ext{CCR}_1 = 	ext{CR}_1 - 0 	imes d = 100.00$$
- **Quarter 2 ($s=2$)**:
  $$	ext{CCR}_2 = 	ext{CR}_2 - 1 	imes d = 151.70 - 2.54 = 149.16$$
- **Quarter 3 ($s=3$)**:
  $$	ext{CCR}_3 = 	ext{CR}_3 - 2 	imes d = 200.02 - 5.085 = 194.94$$
- **Quarter 4 ($s=4$)**:
  $$	ext{CCR}_4 = 	ext{CR}_4 - 3 	imes d = 84.83 - 7.6275 = 77.20$$

Sum of trend-corrected chain relatives:
$$\sum_{s=1}^{4} 	ext{CCR}_s = 100.00 + 149.16 + 194.94 + 77.20 = 521.30$$
The arithmetic mean is:
$$\overline{	ext{CCR}} = rac{521.30}{4} = 130.325$$

Normalizing so that the mean equals 100%:
$$S_s = rac{	ext{CCR}_s}{130.325} 	imes 100$$

- $S_{	ext{Q1}} = rac{100.00}{130.325} 	imes 100 pprox \mathbf{76.73\%}$
- $S_{	ext{Q2}} = rac{149.16}{130.325} 	imes 100 pprox \mathbf{114.45\%}$
- $S_{	ext{Q3}} = rac{194.94}{130.325} 	imes 100 pprox \mathbf{149.58\%}$
- $S_{	ext{Q4}} = rac{77.20}{130.325} 	imes 100 pprox \mathbf{59.24\%}$

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

1. Calculate the secular trend value $T_t$ and the combined trend-seasonal baseline $B_t = (T_t 	imes S_t) / 100$ for each of the eight quarters.
2. Isolate the cyclical-irregular residual ratio $(C_t 	imes I_t) = (Y_t / B_t) 	imes 100$ for all eight quarters.
3. Apply a 3-quarter weighted moving average filter with symmetric weights $[0.25, 0.50, 0.25]$ to smooth out irregular noise $I_t$, extracting the pure cyclical index $C_t$ for quarters 2 through 7.
4. Identify the timing of the business cycle peak and trough over this two-year period, and characterize the macroeconomic cyclical stance in Year 2 Q4.

### Solution, step 1: Secular Trend and Combined Baseline
We evaluate $T_t = 500.0 + 10.0 t$ and $B_t = rac{T_t 	imes S_t}{100}$:

- **Quarter 1 ($t=1$, Y1 Q1)**:
  - $T_1 = 500 + 10(1) = 510.0$
  - $B_1 = rac{510.0 	imes 92.0}{100} = 469.20$
- **Quarter 2 ($t=2$, Y1 Q2)**:
  - $T_2 = 500 + 10(2) = 520.0$
  - $B_2 = rac{520.0 	imes 104.0}{100} = 540.80$
- **Quarter 3 ($t=3$, Y1 Q3)**:
  - $T_3 = 500 + 10(3) = 530.0$
  - $B_3 = rac{530.0 	imes 108.0}{100} = 572.40$
- **Quarter 4 ($t=4$, Y1 Q4)**:
  - $T_4 = 500 + 10(4) = 540.0$
  - $B_4 = rac{540.0 	imes 96.0}{100} = 518.40$
- **Quarter 5 ($t=5$, Y2 Q1)**:
  - $T_5 = 500 + 10(5) = 550.0$
  - $B_5 = rac{550.0 	imes 92.0}{100} = 506.00$
- **Quarter 6 ($t=6$, Y2 Q2)**:
  - $T_6 = 500 + 10(6) = 560.0$
  - $B_6 = rac{560.0 	imes 104.0}{100} = 582.40$
- **Quarter 7 ($t=7$, Y2 Q3)**:
  - $T_7 = 500 + 10(7) = 570.0$
  - $B_7 = rac{570.0 	imes 108.0}{100} = 615.60$
- **Quarter 8 ($t=8$, Y2 Q4)**:
  - $T_8 = 500 + 10(8) = 580.0$
  - $B_8 = rac{580.0 	imes 96.0}{100} = 556.80$

### Solution, step 2: Cyclical-Irregular Residual Ratios
We compute $(C_t 	imes I_t) = rac{Y_t}{B_t} 	imes 100$:

- $t = 1$: $rac{475.0}{469.20} 	imes 100 pprox \mathbf{101.24\%}$
- $t = 2$: $rac{548.0}{540.80} 	imes 100 pprox \mathbf{101.33\%}$
- $t = 3$: $rac{582.0}{572.40} 	imes 100 pprox \mathbf{101.68\%}$
- $t = 4$: $rac{530.0}{518.40} 	imes 100 pprox \mathbf{102.24\%}$
- $t = 5$: $rac{492.0}{506.00} 	imes 100 pprox \mathbf{97.23\%}$
- $t = 6$: $rac{565.0}{582.40} 	imes 100 pprox \mathbf{97.01\%}$
- $t = 7$: $rac{585.0}{615.60} 	imes 100 pprox \mathbf{95.03\%}$
- $t = 8$: $rac{515.0}{556.80} 	imes 100 pprox \mathbf{92.49\%}$

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
