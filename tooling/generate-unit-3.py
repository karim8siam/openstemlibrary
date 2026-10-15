# tooling/generate-unit-3.py
import os

out_path = "publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-3.md"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

unit3_text = r"""# Unit 3: Statistical Graphics, Grammar of Graphics, Exploratory Data Analysis, and Diagnostic Visualizations

## 3.1 The Theoretical Foundations of Statistical Graphics: Bertin's Semiology and Wilkinson's Grammar

Data visualization in modern statistical computing is not merely an aesthetic endeavor or a collection of ad-hoc charting recipes. Rather, statistical graphics constitute a formal, mathematically rigorous visual language designed to decode quantitative structures, diagnose model violations, and facilitate exploratory data analysis (EDA). The intellectual architecture of contemporary visualization engines—most notably `ggplot2` in R and `seaborn` / `plotnine` in Python—is founded upon two landmark theoretical frameworks: Jacques Bertin's **Semiology of Graphics** (1967) and Leland Wilkinson's **The Grammar of Graphics** (1999).

### Jacques Bertin and the Semiology of Visual Signs

In 1967, French cartographer and visual theorist Jacques Bertin published *Sémiologie Graphique*, establishing the foundational vocabulary of visual information encoding. Bertin demonstrated that any visual display encodes information by mapping data attributes to retinal marks and spatial positions on a two-dimensional visual plane.

Bertin identified two fundamental **spatial variables**:
1. Horizontal spatial position ($x$).
2. Vertical spatial position ($y$).

Superimposed upon these two spatial coordinates are six **retinal visual variables**:
1. **Size**: The physical area, length, or radius of a geometric symbol.
2. **Value (Lightness / Luminance)**: The perceived brightness of a mark along a grayscale gradient from black to white.
3. **Texture (Pattern / Grain)**: The frequency, granularity, or coarseness of hatch patterns or stippling.
4. **Color Hue**: The spectral wavelength of the mark (e.g., red, green, blue).
5. **Orientation**: The angle of rotation of a line or directional glyph.
6. **Shape**: The geometric contour of a mark (e.g., circle, square, triangle, cross).

#### Bertin's Perceptual Properties
Bertin categorized these visual variables according to four fundamental perceptual capabilities:
- **Associative**: Does the variable allow viewers to perceive marks as belonging to the same group without implying an ordering? (Hue, shape, and texture are associative).
- **Selective**: Does the variable enable viewers to instantly isolate and focus upon a specific category among distractors (preattentive visual pop-out)? (Position, size, and hue are highly selective).
- **Ordered**: Does the variable instinctively convey a natural ranking or directional hierarchy? (Position, size, and value are intrinsically ordered; hue and shape are non-ordered).
- **Quantitative**: Does the variable allow viewers to perceive the numerical ratio or metric distance between two values? (Only spatial position and length/size provide direct quantitative perception).

### Leland Wilkinson's Grammar of Graphics

In 1999, statistician and computer scientist Leland Wilkinson revolutionized computational visualization with *The Grammar of Graphics*. Wilkinson rejected the traditional paradigm of treating charts as discrete, rigid "chart types" (e.g., pie charts, bar charts, scatter plots, box plots). Instead, he recognized that every statistical graphic is a composition of independent, modular, orthogonal mathematical layers:

$$\text{Graphic} = \text{Data} \oplus \text{Trans} \oplus \text{Scale} \oplus \text{Coord} \oplus \text{Element} \oplus \text{Guide}$$

```text
Wilkinson's Grammar of Graphics Architecture:
+-----------------------------------------------------------+
| Themes & Guides (Labels, Legends, Typography, Margins)   |
| Coordinate System (Cartesian, Polar, Map Projection)      |
| Facets (Trellis / Lattice Conditioning Partitions)        |
| Geometric Elements (Points, Lines, Polygons, Bars, Ribbons)|
| Statistical Transformations (Identity, Bin, Density, Smooth)|
| Scales (Linear, Log, Power, Categorical to Retinal Mappings)|
| Aesthetic Mappings (Aesthetics: x, y, color, size, shape)  |
| Data Source (Tidy Tabular Data Frame)                     |
+-----------------------------------------------------------+
```

#### The Orthogonal Grammatical Components
1. **Data**: An underlying tabular data frame in tidy format.
2. **Aesthetic Mappings (`aes`)**: Mathematical mappings linking columns in the data frame to visual channels (e.g., mapping `body_mass` to $x$-position, `flipper_length` to $y$-position, and `species` to color hue).
3. **Statistical Transformations (`stat`)**: Mathematical algorithms that transform raw input data into intermediate summary statistics prior to rendering. For example, `stat_bin` aggregates continuous values into histogram count bins; `stat_density` evaluates a continuous kernel density estimate; `stat_smooth` fits a generalized additive model (GAM) or local polynomial regression (LOESS) with pointwise confidence ribbons.
4. **Geometric Objects (`geom`)**: The physical visual marks rendered on the screen: points (`geom_point`), lines (`geom_line`), bars (`geom_bar`), ribbons (`geom_ribbon`), or contours (`geom_contour`). Crucially, geometry and statistics are decoupled: a bar geometry can render raw values (`stat_identity`) or aggregated counts (`stat_bin`).
5. **Scales (`scale`)**: Invertible mathematical functions mapping data domain values to visual aesthetic ranges:
   $$f_{scale}: \mathcal{D}_{data} \to \mathcal{R}_{aesthetic}$$
   For continuous variables, scales perform linear, logarithmic, square-root, or logit transformations. For categorical variables, scales map discrete factor levels to color palettes, line types, or symbol shapes. Scales are also responsible for generating axes, tick marks, and legend keys.
6. **Coordinate Systems (`coord`)**: The geometric space in which marks are positioned. While standard Cartesian coordinates ($\mathbb{R}^2$) predominate, the grammar effortlessly supports polar coordinates (`coord_polar`, which transforms stacked bar charts into pie charts or Coxcomb diagrams) and map projections.
7. **Faceting (`facet`)**: Conditioning displays (based on Trellis graphics developed by Becker, Cleveland, and Shyu) that partition the dataset into small-multiples sub-panels based on one or more categorical conditioning variables.

---

## 3.2 Declarative Layered Grammars vs Imperative Canvas Visualizations

A fundamental architectural distinction exists between the visualization paradigms of R and Python: the **declarative layered grammar** represented by R's `ggplot2` (and Python's `plotnine`) versus the **imperative, stateful canvas** model represented by Python's `matplotlib`.

### The Declarative Layered Paradigm (`ggplot2`)

Created by Hadley Wickham in 2005, `ggplot2` is an explicit, idiomatic implementation of Wilkinson's Grammar of Graphics for R.

In a declarative visualization system, the programmer specifies **what** the visual relationships are, rather than imperatively scripting **how** the computer should draw pixels, lines, or legend boxes:

```r
library(ggplot2)

ggplot(data = penguins, aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_point(alpha = 0.7, size = 2.5) +
  geom_smooth(method = "lm", se = TRUE) +
  scale_color_viridis_d(option = "plasma") +
  facet_wrap(~ island) +
  theme_minimal()
```

#### Key Architectural Virtues of Declarative Grammars:
1. **Automatic Legend and Axis Generation**: Because aesthetic mappings (`aes(color = species)`) explicitly bind data columns to visual channels, `ggplot2` automatically constructs legends, assigns consistent color scales across facets, and synchronizes axis limits without manual intervention.
2. **Layer Composability**: Visual elements are combined using the `+` operator. Layers can share the global dataset and aesthetic mappings or specify local, independent datasets.
3. **Separation of Content and Theme**: Graphical themes (`theme_minimal()`, `theme_bw()`) control purely aesthetic parameters (font families, grid line colors, background shading, legend margins) completely independently of the mathematical data mappings.

### The Imperative Canvas Paradigm (`matplotlib`)

Originating from John Hunter's work in 2003, `matplotlib` was designed to replicate the procedural, imperative plotting model of MATLAB.

In an imperative system, the programmer manipulates a stateful canvas through sequential procedure calls:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))

# Imperative manual looping across categories
for sp, grp in penguins.groupby("species"):
    ax.scatter(grp["flipper_length_mm"], grp["body_mass_g"], label=sp, alpha=0.7)

ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")
ax.set_title("Penguin Morphology")
ax.legend()
plt.show()
```

#### Comparative Architectural Evaluation:
- **`matplotlib` Strengths**: Unrivaled low-level control. Every individual pixel, tick line, spline boundary, and bounding box is directly accessible via the Object-Oriented API (`Figure`, `Axes`, `Artist`, `Line2D`). This fine-grained control is ideal for developing custom GUI controls, complex multi-panel publication figures, and dynamic animations.
- **`matplotlib` Weaknesses**: Verbose and error-prone for exploratory data analysis. Computing linear fits with confidence envelopes, constructing multi-variable legends, or generating small-multiples grids requires extensive procedural boilerplate.
- **`seaborn` as a High-Level Bridge**: Michael Waskom developed `seaborn` to provide a declarative statistical interface on top of `matplotlib`. `seaborn` automates statistical aggregations, error bands, and categorical palettes while allowing low-level customization via the underlying `matplotlib.axes.Axes` objects.

---

## 3.3 Kernel Density Estimation: Bandwidth Selection, AMISE, and Boundary Kernels

In exploratory data analysis, estimating the probability density function $f(x)$ of a continuous random variable from an empirical sample $X_1, \dots, X_n$ is a central objective. While histograms provide an intuitive visualization, their appearance is hypersensitive to arbitrary bin width and bin origin choices. To construct smooth, continuous, non-parametric density estimates, statisticians deploy **Kernel Density Estimation (KDE)**, pioneered by Emanuel Parzen (1962) and Murray Rosenblatt (1956).

### Mathematical Formulation of the Rosenblatt–Parzen Kernel Estimator

Given an independent and identically distributed (i.i.d.) sample $X_1, X_2, \dots, X_n$ drawn from an unknown continuous distribution with density $f(x)$, the kernel density estimator is defined as:

$$\hat{f}_h(x) = \frac{1}{n h} \sum_{i=1}^n K\left( \frac{x - X_i}{h} \right)$$

where:
- $K(u)$ is the **kernel function**, typically chosen to be a symmetric, zero-mean probability density function satisfying:
  $$\int_{-\infty}^\infty K(u) \, du = 1, \quad \int_{-\infty}^\infty u K(u) \, du = 0, \quad \sigma_K^2 = \int_{-\infty}^\infty u^2 K(u) \, du > 0$$
- $h > 0$ is the **bandwidth (or smoothing parameter)**, controlling the spatial dispersion of the kernel weights around each sample point $X_i$.

```text
Kernel Density Construction (Superposition of Local Kernel Functions):
            ^ \hat{f}_h(x) (Aggregated Density)
           / \
          /   \     /\
         /     \___/  \
        +----------------------------------------+
         |     |    |   |     |    | (Data Points)
         X1    X2   X3  X4    X5   X6
          \___/ (Individual Kernel Weights K((x - Xi)/h))
```

### Typology of Standard Kernel Functions

Common symmetric kernel functions include:
1. **Gaussian Kernel**:
   $$K(u) = \frac{1}{\sqrt{2\pi}} e^{-u^2 / 2}$$
   Smooth, infinitely differentiable, but has infinite support ($u \in \mathbb{R}$).
2. **Epanechnikov Kernel**:
   $$K(u) = \frac{3}{4} (1 - u^2) \cdot \mathbb{I}(|u| \le 1)$$
   Optimal in the sense of minimizing asymptotic mean integrated squared error (AMISE). Has compact support on $[-1, 1]$.
3. **Biweight (Quartic) Kernel**:
   $$K(u) = \frac{15}{16} (1 - u^2)^2 \cdot \mathbb{I}(|u| \le 1)$$
4. **Triangular Kernel**:
   $$K(u) = (1 - |u|) \cdot \mathbb{I}(|u| \le 1)$$

While the choice of kernel function $K(u)$ affects local smoothness and computational complexity, the mathematical quality of the density estimate is overwhelmingly governed by the **bandwidth $h$**:
- **Under-smoothing ($h$ too small)**: $\hat{f}_h(x)$ exhibits high variance, displaying spurious bimodal spikes and sampling noise.
- **Over-smoothing ($h$ too large)**: $\hat{f}_h(x)$ exhibits high bias, flattening true multimodal peaks and truncating distribution tails.

### Statistical Error Metrics: MISE and AMISE

To evaluate estimator performance globally, statisticians analyze the **Mean Integrated Squared Error (MISE)**:

$$\text{MISE}(h) = \mathbb{E} \left[ \int_{-\infty}^\infty (\hat{f}_h(x) - f(x))^2 \, dx \right] = \int_{-\infty}^\infty \text{MSE}(\hat{f}_h(x)) \, dx$$

Using the classical bias-variance decomposition:

$$\text{MSE}(\hat{f}_h(x)) = \text{Var}(\hat{f}_h(x)) + \left[ \text{Bias}(\hat{f}_h(x)) \right]^2$$

Through Taylor series expansions of $f(x - u h)$ around $x$, assuming $f$ has continuous second derivatives $f''(x)$, the asymptotic bias and variance are derived as:

$$\text{Bias}(\hat{f}_h(x)) = \frac{1}{2} h^2 \sigma_K^2 f''(x) + \mathcal{O}(h^4)$$
$$\text{Var}(\hat{f}_h(x)) = \frac{R(K)}{n h} f(x) + \mathcal{O}\left( \frac{1}{n} \right)$$
where $R(K) = \int_{-\infty}^\infty K(u)^2 \, du$ is the roughness of the kernel.

Integrating over all $x \in \mathbb{R}$ yields the **Asymptotic Mean Integrated Squared Error (AMISE)**:

$$\text{AMISE}(h) = \frac{R(K)}{n h} + \frac{1}{4} h^4 \sigma_K^4 R(f'')$$

where $R(f'') = \int_{-\infty}^\infty [f''(x)]^2 \, dx$ is the roughness of the true, unknown density's second derivative.

Differentiating $\text{AMISE}(h)$ with respect to $h$ and setting the derivative to zero yields the **Optimal AMISE Bandwidth**:

$$h_{opt} = \left( \frac{R(K)}{\sigma_K^4 R(f'') n} \right)^{1/5} \propto n^{-1/5}$$

The optimal bandwidth decays at the slow asymptotic rate of $n^{-1/5}$, meaning that quadrupling the sample size only reduces the optimal bandwidth by a factor of $4^{-0.2} \approx 0.758$.

### Practical Bandwidth Selection Rules

Because the optimal bandwidth depends on the unknown quantity $R(f'')$, practical estimation requires data-driven heuristics:

#### 1. Silverman's Rule of Thumb
If the true underlying density is assumed to be Gaussian $\mathcal{N}(\mu, \sigma^2)$, then $R(f'') = \frac{3}{8 \sqrt{\pi} \sigma^5}$. For a standard Gaussian kernel, $R(K) = \frac{1}{2\sqrt{\pi}}$ and $\sigma_K^2 = 1$. Substituting these values into the optimal bandwidth formula yields **Silverman's Rule of Thumb**:

$$h_{Silverman} = \left( \frac{4 \hat{\sigma}^5}{3 n} \right)^{1/5} \approx 1.06 \, \hat{\sigma} \, n^{-1/5}$$

To make the rule robust against outliers and heavy tails, Bernard Silverman (1986) replaced the sample standard deviation $\hat{\sigma}$ with a robust dispersion metric:

$$\hat{A} = \min\left( \hat{\sigma}, \frac{\text{IQR}}{1.349} \right)$$
$$h_{Silverman, robust} = 0.9 \, \hat{A} \, n^{-1/5}$$

#### 2. Sheather–Jones Plug-in Method (SJ)
While Silverman's rule works well for unimodal bell-shaped distributions, it severely over-smooths multimodal or skewed densities. Simon Sheather and Michael Jones (1991) developed a sophisticated pilot plug-in method (`bw = "SJ"` in R). The algorithm uses pilot bandwidths to directly estimate $R(f'')$ and $R(f''')$ from the empirical sample, converging at an optimal asymptotic rate of $n^{-5/14}$, representing the gold standard for exploratory density estimation.

### Boundary Bias and Boundary Correction Kernels

A severe pathology of standard kernel density estimation occurs when estimating densities for random variables with bounded physical domains (e.g., strictly positive variables like income, survival time, or concentration $x \ge 0$).

Near the boundary $x = 0$, the symmetric kernel $K((x - X_i)/h)$ places substantial probability mass in the impossible negative domain $(-\infty, 0)$. Consequently, the standard estimator suffers from **boundary bias**:
$$\mathbb{E}[\hat{f}_h(0)] \to \frac{1}{2} f(0) \quad \text{as } h \to 0$$
The estimator systematically underestimates the true density at the boundary by approximately $50\%$!

#### Remediation Techniques:
1. **Reflection Boundary Method (Boneva et al., 1971)**:
   Reflect the data points symmetrically across the boundary: $\tilde{X}_i = -X_i$. Construct the estimator on the augmented sample:
   $$\hat{f}_{ref}(x) = \hat{f}_h(x) + \hat{f}_h(-x) \quad \text{for } x \ge 0$$
   This eliminates $O(h)$ boundary bias whenever $f'(0) = 0$.
2. **Logarithmic / Box–Cox Transformations**:
   Transform the bounded data onto an unbounded support: $Y_i = \log(X_i)$. Estimate the smooth density $\hat{g}(y)$ on the real line, and transform back using the change-of-variables Jacobian:
   $$\hat{f}(x) = \hat{g}(\log x) \cdot \frac{1}{x} \quad \text{for } x > 0$$

---

## 3.4 Bivariate Diagnostics: Hexbins, Contours, Q-Q Plots, and Residual Analytics

Visualizing relationships between two or more variables is fundamental to statistical inference. As dataset sizes scale to hundreds of thousands of observations, traditional scatter plots suffer from severe **overplotting**, where thousands of overlapping dots coalesce into a solid black mass, obscuring underlying density gradients.

### High-Density Bivariate Encodings: Hexagonal Binning and 2D Contours

To visualize massive bivariate samples $(X_i, Y_i)_{i=1}^n$:

#### 1. Hexagonal Binning (`geom_hex`)
Introduced by Daniel Carr and colleagues (1987), hexagonal binning tessellates the 2D coordinate plane into regular hexagonal bins. 
- Why hexagons rather than rectangular grids? Hexagons have 12-fold symmetry, meaning that each hexagon has six equidistant neighbors (unlike rectangular pixels, whose diagonal neighbors are $\sqrt{2}$ times farther than horizontal/vertical neighbors). Hexagonal smoothing minimizes directional visual artifacts.
- The algorithm maps each point $(X_i, Y_i)$ into its enclosing hexagon and encodes the localized point count via a continuous color scale.

#### 2. Bivariate 2D Density Contours (`geom_density_2d`)
The 2D continuous kernel density estimator is defined as:

$$\hat{f}_{\mathbf{H}}(\mathbf{x}) = \frac{1}{n \det(\mathbf{H})^{1/2}} \sum_{i=1}^n K\left( \mathbf{H}^{-1/2} (\mathbf{x} - \mathbf{X}_i) \right)$$

where $\mathbf{H}$ is a $2 \times 2$ symmetric positive-definite bandwidth matrix. Evaluating $\hat{f}_{\mathbf{H}}(\mathbf{x})$ over a fine spatial grid allows the extraction of **contour level sets**:

$$\mathcal{C}_c = \{ (x, y) \in \mathbb{R}^2 : \hat{f}_{\mathbf{H}}(x, y) = c \}$$

Level sets are plotted as closed topographic contour lines or filled color bands, revealing bivariate skewness, multimodal clusters, and non-linear correlation structures.

### Normal Quantile–Quantile (Q-Q) Plots and Finite-Sample Confidence Bands

In parametric inference, verifying whether a continuous variable or regression residual vector follows a Gaussian distribution $\mathcal{N}(\mu, \sigma^2)$ is a critical diagnostic step.

The **Quantile–Quantile (Q-Q) Plot** graphs the ordered empirical sample quantiles against the theoretical quantiles of the reference distribution.

#### Construction Protocol:
1. Sort the sample of size $n$ into ascending order statistics:
   $$X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$$
2. For each rank $i \in \{1, \dots, n\}$, determine an empirical cumulative probability plotting position $p_i \in (0, 1)$. Standard formulations include:
   - **Hazen (1889)**: $p_i = \frac{i - 0.5}{n}$
   - **Weibull (1939)**: $p_i = \frac{i}{n + 1}$
   - **Blom (1958)**: $p_i = \frac{i - 3/8}{n + 1/4}$ (Optimal for approximating the expected values of Gaussian order statistics).
3. Compute the theoretical standard normal quantiles:
   $$q_i = \Phi^{-1}(p_i)$$
   where $\Phi^{-1}$ is the inverse standard normal cumulative distribution function (probit function).
4. Plot the Cartesian coordinate pairs $(q_i, X_{(i)})$.

If the sample is drawn from $\mathcal{N}(\mu, \sigma^2)$, the points fall along a straight line with intercept $\mu$ and slope $\sigma$:
$$X_{(i)} \approx \mu + \sigma q_i$$
- **Heavy Tails**: An S-shaped curve curving upward on the right and downward on the left indicates heavier tails than Gaussian (e.g., Student's $t$ or Cauchy).
- **Light Tails**: An inverted S-curve indicates truncated or uniform distributions.
- **Positive Skewness**: A convex upward curvature indicates right-skewness (e.g., log-normal or exponential).

#### Finite-Sample Confidence Envelopes
To distinguish genuine departures from normality from random sampling fluctuations, modern Q-Q plots superimpose **pointwise or simultaneous confidence envelopes**. Under the null hypothesis that $X \sim \mathcal{N}(\mu, \sigma^2)$, the $i$-th order statistic $X_{(i)}$ has asymptotic variance:

$$\text{Var}(X_{(i)}) \approx \frac{p_i (1 - p_i)}{n \left[ \phi(\Phi^{-1}(p_i)) \right]^2}$$

where $\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$ is the standard normal density. Constructing pointwise $95\%$ envelopes:

$$\text{Upper}_i = \hat{\mu} + \hat{\sigma} q_i + 1.96 \, \hat{\sigma} \sqrt{\frac{p_i (1 - p_i)}{n \phi(q_i)^2}}$$
$$\text{Lower}_i = \hat{\mu} + \hat{\sigma} q_i - 1.96 \, \hat{\sigma} \sqrt{\frac{p_i (1 - p_i)}{n \phi(q_i)^2}}$$

Points breaching the confidence envelope provide statistically significant evidence of distributional violation.

### Diagnostic Visualizations for Ordinary Least Squares (OLS)

In linear regression analysis $\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\epsilon}$, verifying the Gauss–Markov assumptions (linearity, homoscedasticity, independence, normality) is accomplished through four canonical residual diagnostic plots:

1. **Residuals vs Fitted (Tukey–Anscombe Plot)**:
   Plots raw residuals $e_i = y_i - \hat{y}_i$ against fitted values $\hat{y}_i$. A non-linear smoothed trend line indicates unmodeled curvature (omitted non-linear terms or interaction effects).
2. **Scale-Location (Spread-Location) Plot**:
   Plots $\sqrt{|r_i|}$ (where $r_i = \frac{e_i}{\hat{\sigma} \sqrt{1 - h_{ii}}}$ is the internally studentized residual and $h_{ii}$ is the leverage) against fitted values $\hat{y}_i$. A non-horizontal trend line indicates **heteroscedasticity** (non-constant error variance $\text{Var}(\epsilon_i) \ne \sigma^2$).
3. **Normal Q-Q of Studentized Residuals**:
   Assesses residual normality for valid finite-sample hypothesis testing.
4. **Residuals vs Leverage with Cook's Distance Envelopes**:
   Plots studentized residuals $r_i$ against diagonal leverage values $h_{ii} = \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top$. Superimposes contour lines for **Cook's Distance**:
   $$D_i = \frac{r_i^2}{p} \left( \frac{h_{ii}}{1 - h_{ii}} \right)$$
   Points with $D_i > 0.5$ or $D_i > 1.0$ indicate highly influential observations whose exclusion would substantially alter the estimated regression parameter vector $\hat{\boldsymbol{\beta}}$.

---

## 3.5 Perceptual Uniformity, Color Spaces, and Visual Accessibility Standards

The choice of color palette in statistical computing is not a matter of subjective artistic preference. The human visual system processes color through complex biological mechanisms involving retinal photoreceptors (rods and cone cells) and neural post-processing pathways in the primary visual cortex. Improper color choices can distort empirical data distributions, introduce visual artifacts, and render visualizations completely illegible to readers with color vision deficiencies.

### The Psychophysics of Visual Perception

Visual perception is governed by psychophysical laws formulated in the 19th and 20th centuries:

#### 1. The Weber–Fechner Law
Ernst Weber and Gustav Fechner established that the perceived intensity of a physical stimulus scales logarithmically with the actual physical stimulus magnitude:

$$\Delta I = k \cdot I \implies S = k \ln \left( \frac{I}{I_0} \right)$$

where $I$ is the physical intensity, $\Delta I$ is the just-noticeable difference (JND), and $S$ is the perceived sensory sensation. Consequently, the human eye perceives changes in luminance and contrast relative to background intensity rather than in absolute terms.

#### 2. The Cleveland–McGill Perceptual Accuracy Hierarchy
In a landmark 1984 study, statisticians William S. Cleveland and Robert McGill conducted empirical psychophysical experiments to rank visual encodings by decoding accuracy. Their hierarchy represents the bedrock of modern statistical graphic design:

```text
Cleveland-McGill Decoding Accuracy Hierarchy (Most to Least Accurate):
  [ 1. Position along a Common Scale (e.g. Scatter plot, Dot plot) ]     (MOST ACCURATE)
  [ 2. Position along Identical, Non-Aligned Scales (e.g. Small Multiples) ]
  [ 3. Length (e.g. Bar chart) ]
  [ 4. Direction / Angle / Slope (e.g. Pie chart, Wind rose) ]
  [ 5. Area (e.g. Bubble chart, Treemap) ]
  [ 6. Volume / 3D Curvature ]
  [ 7. Color Value (Luminance / Brightness Gradients) ]
  [ 8. Color Hue / Saturation / Chromatic Intensity ]                    (LEAST ACCURATE)
```

**Direct Practical Rule**: Whenever numerical values must be decoded with high quantitative precision, map the variable to **position along a common scale**. Reserve color hue exclusively for categorical grouping, and color luminance for secondary continuous heatmaps.

### The Pathology of Rainbow Colormaps ("Jet")

For decades, scientific software packages (MATLAB, early Python libraries) defaulted to the **Rainbow ("Jet")** colormap, which sweeps through blue, cyan, green, yellow, and red.

Modern color scientists and perceptual psychologists have proven that Rainbow colormaps are **catastrophically flawed**:
1. **Non-Monotonic Luminance**: The perceived brightness of Jet fluctuates wildly across the spectrum:
   - Green and yellow have very high perceived luminance.
   - Blue and red have very low perceived luminance.
   As a result, the colormap creates artificial visual "stripes" and sharp boundaries where none exist in the underlying mathematical data (e.g., at the transition from cyan to yellow).
2. **Perceptual Non-Uniformity**: The rate of perceived color change $\Delta E$ per unit change in data $\Delta X$ is highly irregular:
   $$\frac{d(\Delta E)}{dX} \ne \text{constant}$$
   A small numeric change in a yellow region appears massive to human viewers, while a large numeric change in a green region is completely invisible.
3. **Inversion Under Grayscale Printing**: When photocopied or printed in black-and-white, dark blue and dark red collapse to identical dark gray shades, making high and low values indistinguishable.

### Perceptually Uniform Color Spaces: CIELAB and CAM02

To eliminate perceptual distortions, the International Commission on Illumination (CIE) developed the **CIELAB ($L^* a^* b^*$)** and **CIECAM02** color spaces.

In CIELAB:
- $L^*$: Represents perceptual lightness (luminance), calibrated strictly to match human retinal response from 0 (pure black) to 100 (diffuse white).
- $a^*$: Represents the green-red chromatic axis.
- $b^*$: Represents the blue-yellow chromatic axis.

A colormap is defined as **Perceptually Uniform** if the Euclidean distance between any two colors in CIELAB space is directly proportional to the numerical difference between the data values they represent:

$$\Delta E^*_{ab} = \sqrt{(\Delta L^*)^2 + (\Delta a^*)^2 + (\Delta b^*)^2} \propto |\Delta X|$$

#### Modern Scientific Colormaps
In 2015, Stéfan van der Walt and Nathaniel Smith engineered four mathematically validated, perceptually uniform colormaps for scientific computing:
- **Viridis**: Sweeps monotonically from dark purple through teal to bright yellow. Monotonically increasing in lightness $L^*$.
- **Plasma**: High-contrast purple-pink-yellow gradient.
- **Magma**: Deep black to bright white through orange-red.
- **Inferno**: Optimized for thermal and radiation displays.
- **Cividis**: Specifically optimized for readers with color vision deficiencies.

### Color Vision Deficiencies (CVD) and Accessibility Standards

Approximately $8\%$ of men and $0.5\%$ of women of Northern European descent suffer from **Color Vision Deficiencies (CVD)**, caused by genetic alterations in retinal photopigments:
1. **Deuteranopia / Deuteranomaly**: Absence or anomaly of M-cone cells (green-blindness). This is the most common form, affecting $>95\%$ of all CVD individuals.
2. **Protanopia / Protanomaly**: Absence or anomaly of L-cone cells (red-blindness).
3. **Tritanopia / Tritanomaly**: Rare absence of S-cone cells (blue-blindness).

#### Universal Design Rules for Statistical Graphics:
- **Avoid Red-Green Contrasts**: Never use red and green alone to signify binary contrasts (such as "positive vs negative" or "treatment vs control"). Under deuteranopia and protanopia, both red and green collapse to identical muddy brownish-yellow hues.
- **Use Red-Blue or Orange-Purple**: Categorical contrasts should use orange and blue or purple and green.
- **Dual Visual Encoding**: Always reinforce color distinctions with secondary non-color visual channels (e.g., pairing distinct colors with distinct point shapes, line dash patterns, or direct text labels).
- **Luminance Monotonicity**: Ensure that continuous heatmaps remain legible when converted entirely to grayscale by enforcing monotonic variation in $L^*$.

---

## Fully worked question 1: Analytical Derivation of Optimal Gaussian Kernel Bandwidth via Asymptotic Mean Integrated Squared Error (AMISE)

### Question
A financial statistician models high-frequency equity price returns using a continuous kernel density estimator $\hat{f}_h(x)$ constructed from an i.i.d. sample of $n$ log-return observations $X_1, \dots, X_n$. The estimation employs a standard Gaussian kernel:

$$K(u) = \frac{1}{\sqrt{2\pi}} e^{-u^2 / 2}$$

1. Derive the roughness $R(K) = \int_{-\infty}^\infty [K(u)]^2 \, du$ and second moment $\sigma_K^2 = \int_{-\infty}^\infty u^2 K(u) \, du$ for the standard Gaussian kernel.
2. Under standard regularity conditions where $f(x)$ possesses continuous square-integrable derivatives up to order 2, write down the asymptotic bias $\text{Bias}(\hat{f}_h(x))$ and asymptotic variance $\text{Var}(\hat{f}_h(x))$, and formulate the Asymptotic Mean Integrated Squared Error $\text{AMISE}(h)$.
3. Assume that the true underlying data-generating distribution is a Gaussian distribution $X \sim \mathcal{N}(0, \sigma^2)$. Derive the exact analytical expression for the roughness of the second derivative:
   $$R(f'') = \int_{-\infty}^\infty [f''(x)]^2 \, dx$$
4. Solve for the global optimal bandwidth $h_{opt}$ that minimizes $\text{AMISE}(h)$ as a function of sample size $n$ and true standard deviation $\sigma$. For an empirical sample of $n = 100,000$ returns with sample standard deviation $\hat{\sigma} = 0.015$, compute the numeric optimal bandwidth $h_{opt}$ to six decimal places.

---

### Solution, step 1: Derive the roughness and second moment of the Gaussian kernel

**Solution, step 1: Derive the roughness and second moment of the Gaussian kernel.**

We are given the standard Gaussian kernel:
$$K(u) = \frac{1}{\sqrt{2\pi}} e^{-u^2 / 2}$$

#### 1. Kernel Roughness $R(K)$:
By definition, the roughness is the integral of the square of the kernel:

$$R(K) = \int_{-\infty}^\infty [K(u)]^2 \, du = \int_{-\infty}^\infty \left( \frac{1}{\sqrt{2\pi}} e^{-u^2 / 2} \right)^2 du = \frac{1}{2\pi} \int_{-\infty}^\infty e^{-u^2} \, du$$

Recall the standard Gaussian integral:
$$\int_{-\infty}^\infty e^{-a u^2} \, du = \sqrt{\frac{\pi}{a}}$$
Setting $a = 1$:
$$\int_{-\infty}^\infty e^{-u^2} \, du = \sqrt{\pi}$$

Therefore:
$$R(K) = \frac{1}{2\pi} \sqrt{\pi} = \frac{1}{2\sqrt{\pi}}$$

#### 2. Second Moment $\sigma_K^2$:
By definition:
$$\sigma_K^2 = \int_{-\infty}^\infty u^2 K(u) \, du = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty u^2 e^{-u^2 / 2} \, du$$

This is the variance of a standard normal random variable $U \sim \mathcal{N}(0, 1)$:
$$\sigma_K^2 = \mathbb{E}[U^2] = 1$$

---

### Solution, step 2: Formulate AMISE(h)

**Solution, step 2: Formulate AMISE(h).**

The kernel estimator is:
$$\hat{f}_h(x) = \frac{1}{n h} \sum_{i=1}^n K\left( \frac{x - X_i}{h} \right)$$

1. **Asymptotic Bias**:
   Taylor-expanding $f(x - u h)$ around $x$:
   $$\mathbb{E}[\hat{f}_h(x)] = \int_{-\infty}^\infty \frac{1}{h} K\left( \frac{x - y}{h} \right) f(y) \, dy = \int_{-\infty}^\infty K(u) f(x - u h) \, du$$
   $$= \int_{-\infty}^\infty K(u) \left[ f(x) - u h f'(x) + \frac{1}{2} u^2 h^2 f''(x) + \mathcal{O}(h^3) \right] du$$
   Using $\int K(u) du = 1$, $\int u K(u) du = 0$, and $\int u^2 K(u) du = \sigma_K^2 = 1$:
   $$\mathbb{E}[\hat{f}_h(x)] = f(x) + \frac{1}{2} h^2 f''(x) + \mathcal{O}(h^4)$$
   $$\text{Bias}(\hat{f}_h(x)) = \frac{1}{2} h^2 f''(x) + \mathcal{O}(h^4)$$

2. **Asymptotic Variance**:
   $$\text{Var}(\hat{f}_h(x)) = \frac{1}{n} \text{Var}\left( \frac{1}{h} K\left( \frac{x - X}{h} \right) \right) \approx \frac{1}{n h^2} \mathbb{E}\left[ K\left( \frac{x - X}{h} \right)^2 \right]$$
   $$= \frac{1}{n h} \int_{-\infty}^\infty K(u)^2 f(x - u h) \, du \approx \frac{R(K)}{n h} f(x) = \frac{1}{2\sqrt{\pi} n h} f(x)$$

3. **Asymptotic Mean Integrated Squared Error (AMISE)**:
   $$\text{AMISE}(h) = \int_{-\infty}^\infty \text{Var}(\hat{f}_h(x)) \, dx + \int_{-\infty}^\infty [\text{Bias}(\hat{f}_h(x))]^2 \, dx$$
   Using $\int_{-\infty}^\infty f(x) \, dx = 1$:
   $$\text{AMISE}(h) = \frac{1}{2\sqrt{\pi} n h} + \frac{1}{4} h^4 R(f'')$$
   where $R(f'') = \int_{-\infty}^\infty [f''(x)]^2 \, dx$.

---

### Solution, step 3: Derive R(f'') for a Gaussian target distribution

**Solution, step 3: Derive R(f'') for a Gaussian target distribution.**

Let $f(x)$ be the density of $\mathcal{N}(0, \sigma^2)$:
$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{x^2}{2\sigma^2} \right)$$

1. **First Derivative $f'(x)$**:
   $$f'(x) = -\frac{x}{\sigma^2} f(x)$$

2. **Second Derivative $f''(x)$**:
   Using the product rule:
   $$f''(x) = -\frac{1}{\sigma^2} f(x) - \frac{x}{\sigma^2} f'(x) = -\frac{1}{\sigma^2} f(x) + \frac{x^2}{\sigma^4} f(x) = \left( \frac{x^2 - \sigma^2}{\sigma^4} \right) f(x)$$

3. **Square of the Second Derivative $[f''(x)]^2$**:
   $$[f''(x)]^2 = \frac{(x^2 - \sigma^2)^2}{\sigma^8} \frac{1}{2\pi \sigma^2} \exp\left( -\frac{x^2}{\sigma^2} \right)$$
   $$= \frac{1}{2\pi \sigma^{10}} (x^4 - 2\sigma^2 x^2 + \sigma^4) \exp\left( -\frac{x^2}{\sigma^2} \right)$$

4. **Integration across $\mathbb{R}$**:
   Let us evaluate the standard Gaussian moment integrals:
   $$\int_{-\infty}^\infty x^{2k} \exp\left( -a x^2 \right) dx$$
   With $a = 1/\sigma^2$:
   - For $k = 0$: $\int_{-\infty}^\infty e^{-x^2 / \sigma^2} dx = \sigma \sqrt{\pi}$
   - For $k = 1$: $\int_{-\infty}^\infty x^2 e^{-x^2 / \sigma^2} dx = \frac{\sigma^3 \sqrt{\pi}}{2}$
   - For $k = 2$: $\int_{-\infty}^\infty x^4 e^{-x^2 / \sigma^2} dx = \frac{3 \sigma^5 \sqrt{\pi}}{4}$

Substitute these into the integral:
$$\int_{-\infty}^\infty (x^4 - 2\sigma^2 x^2 + \sigma^4) \exp\left( -\frac{x^2}{\sigma^2} \right) dx = \sigma^5 \sqrt{\pi} \left( \frac{3}{4} - 2\left(\frac{1}{2}\right) + 1 \right) = \sigma^5 \sqrt{\pi} \left( \frac{3}{4} \right) = \frac{3\sqrt{\pi} \sigma^5}{4}$$

Multiply by the leading constant $\frac{1}{2\pi \sigma^{10}}$:

$$R(f'') = \frac{1}{2\pi \sigma^{10}} \times \frac{3\sqrt{\pi} \sigma^5}{4} = \frac{3\sqrt{\pi}}{8\pi \sigma^5} = \frac{3}{8\sqrt{\pi} \sigma^5}$$

This establishes the exact roughness of the second derivative of a normal density.

---

### Solution, step 4: Solve for optimal bandwidth and compute numerical value

**Solution, step 4: Solve for optimal bandwidth and compute numerical value.**

Substitute $R(f'') = \frac{3}{8\sqrt{\pi} \sigma^5}$ and $R(K) = \frac{1}{2\sqrt{\pi}}$ into $\text{AMISE}(h)$:

$$\text{AMISE}(h) = \frac{1}{2\sqrt{\pi} n h} + \frac{1}{4} h^4 \left( \frac{3}{8\sqrt{\pi} \sigma^5} \right) = \frac{1}{2\sqrt{\pi} n h} + \frac{3 h^4}{32\sqrt{\pi} \sigma^5}$$

To find the minimum, set the derivative with respect to $h$ to zero:

$$\frac{d}{dh} \text{AMISE}(h) = -\frac{1}{2\sqrt{\pi} n h^2} + \frac{12 h^3}{32\sqrt{\pi} \sigma^5} = 0$$

$$-\frac{1}{2\sqrt{\pi} n h^2} + \frac{3 h^3}{8\sqrt{\pi} \sigma^5} = 0$$

$$\frac{3 h^3}{8\sqrt{\pi} \sigma^5} = \frac{1}{2\sqrt{\pi} n h^2}$$

Multiply both sides by $h^2 \sqrt{\pi}$:
$$\frac{3 h^5}{8 \sigma^5} = \frac{1}{2 n} \implies h^5 = \frac{8 \sigma^5}{6 n} = \frac{4 \sigma^5}{3 n}$$

Taking the fifth root:

$$h_{opt} = \left( \frac{4}{3} \right)^{1/5} \sigma \, n^{-1/5}$$

Evaluating the constant numerical coefficient:
$$\left( \frac{4}{3} \right)^{1/5} = (1.3333333)^{0.2} \approx 1.05922384 \approx 1.06$$

This completes the theoretical derivation of Silverman's classic rule:
$$h_{opt} \approx 1.05922 \, \sigma \, n^{-1/5}$$

#### Numerical Computation:
Given $n = 100,000 = 10^5$ and $\hat{\sigma} = 0.015$:
$$n^{-1/5} = (10^5)^{-0.2} = 10^{-1} = 0.1$$

Now calculate:
$$h_{opt} = 1.05922384 \times 0.015 \times 0.1 = 1.05922384 \times 0.0015 = 0.00158883576$$

Rounding to six decimal places:
$$h_{opt} \approx 0.001589$$

The optimal smoothing bandwidth is $h \approx 0.001589$.

---

## Fully worked question 2: Construction and Theoretical Quantile Mapping of Normal Q-Q Plots with Finite-Sample Envelope Bounds

### Question
A clinical pharmacologist conducts a bioequivalence trial with $n = 10$ subjects, measuring drug elimination half-life residuals $Y_1, \dots, Y_{10}$. The observed sample residuals, sorted into ascending order statistics, are:

$$\mathbf{y}_{( )} = [-1.82, -1.05, -0.68, -0.35, -0.08, 0.15, 0.42, 0.78, 1.12, 1.95]$$

1. Using Blom's plotting position formula:
   $$p_i = \frac{i - 3/8}{n + 1/4}$$
   compute the empirical probability $p_i$ and corresponding theoretical standard normal quantile $q_i = \Phi^{-1}(p_i)$ for all ten observations ($i = 1, \dots, 10$).
2. Calculate the sample mean $\bar{y}$ and sample standard deviation $s$ of the residuals.
3. Formulate the equation of the theoretical reference line $y = \bar{y} + s \cdot q$.
4. For the extreme order statistics ($i = 1$ and $i = 10$), derive the asymptotic standard error of the order statistic under the null hypothesis of normality:
   $$\text{SE}(Y_{(i)}) \approx \frac{s}{\phi(q_i)} \sqrt{\frac{p_i (1 - p_i)}{n}}$$
   and construct the individual $95\%$ pointwise confidence intervals. Determine whether the observed extreme residuals fall within the $95\%$ envelope.

---

### Solution, step 1: Compute Blom plotting positions and theoretical quantiles

**Solution, step 1: Compute Blom plotting positions and theoretical quantiles.**

With $n = 10$, the denominator in Blom's formula is:
$$n + 1/4 = 10 + 0.25 = 10.25$$
The numerator is $i - 3/8 = i - 0.375$.

Thus:
$$p_i = \frac{i - 0.375}{10.25}$$

We evaluate $p_i$ and $q_i = \Phi^{-1}(p_i)$ for $i = 1, \dots, 10$:

- **$i = 1$**:
  $$p_1 = \frac{0.625}{10.25} \approx 0.060976 \implies q_1 = \Phi^{-1}(0.060976) \approx -1.5466$$
- **$i = 2$**:
  $$p_2 = \frac{1.625}{10.25} \approx 0.158537 \implies q_2 = \Phi^{-1}(0.158537) \approx -1.0005$$
- **$i = 3$**:
  $$p_3 = \frac{2.625}{10.25} \approx 0.256098 \implies q_3 = \Phi^{-1}(0.256098) \approx -0.6554$$
- **$i = 4$**:
  $$p_4 = \frac{3.625}{10.25} \approx 0.353659 \implies q_4 = \Phi^{-1}(0.353659) \approx -0.3754$$
- **$i = 5$**:
  $$p_5 = \frac{4.625}{10.25} \approx 0.451220 \implies q_5 = \Phi^{-1}(0.451220) \approx -0.1226$$
- **$i = 6$**:
  $$p_6 = \frac{5.625}{10.25} \approx 0.548780 \implies q_6 = \Phi^{-1}(0.548780) \approx +0.1226$$
- **$i = 7$**:
  $$p_7 = \frac{6.625}{10.25} \approx 0.646341 \implies q_7 = \Phi^{-1}(0.646341) \approx +0.3754$$
- **$i = 8$**:
  $$p_8 = \frac{7.625}{10.25} \approx 0.743902 \implies q_8 = \Phi^{-1}(0.743902) \approx +0.6554$$
- **$i = 9$**:
  $$p_9 = \frac{8.625}{10.25} \approx 0.841463 \implies q_9 = \Phi^{-1}(0.841463) \approx +1.0005$$
- **$i = 10$**:
  $$p_{10} = \frac{9.625}{10.25} \approx 0.939024 \implies q_{10} = \Phi^{-1}(0.939024) \approx +1.5466$$

Notice the perfect symmetry about zero: $q_{11 - i} = -q_i$.

---

### Solution, step 2: Calculate sample mean and standard deviation

**Solution, step 2: Calculate sample mean and standard deviation.**

Given the ordered residuals:
$$\mathbf{y}_{( )} = [-1.82, -1.05, -0.68, -0.35, -0.08, 0.15, 0.42, 0.78, 1.12, 1.95]$$

1. **Sample Mean $\bar{y}$**:
   $$\sum_{i=1}^{10} y_{(i)} = -1.82 - 1.05 - 0.68 - 0.35 - 0.08 + 0.15 + 0.42 + 0.78 + 1.12 + 1.95 = 0.44$$
   $$\bar{y} = \frac{0.44}{10} = 0.044$$

2. **Sum of Squares and Sample Variance $s^2$**:
   Let us compute $\sum y_i^2$:
   $$(-1.82)^2 = 3.3124$$
   $$(-1.05)^2 = 1.1025$$
   $$(-0.68)^2 = 0.4624$$
   $$(-0.35)^2 = 0.1225$$
   $$(-0.08)^2 = 0.0064$$
   $$(0.15)^2 = 0.0225$$
   $$(0.42)^2 = 0.1764$$
   $$(0.78)^2 = 0.6084$$
   $$(1.12)^2 = 1.2544$$
   $$(1.95)^2 = 3.8025$$
   $$\sum_{i=1}^{10} y_i^2 = 3.3124 + 1.1025 + 0.4624 + 0.1225 + 0.0064 + 0.0225 + 0.1764 + 0.6084 + 1.2544 + 3.8025 = 10.8704$$

   The sample variance is:
   $$s^2 = \frac{1}{n - 1} \left( \sum y_i^2 - n \bar{y}^2 \right) = \frac{1}{9} \left( 10.8704 - 10 \times (0.044)^2 \right)$$
   $$= \frac{1}{9} (10.8704 - 0.01936) = \frac{10.85104}{9} \approx 1.20567$$

3. **Sample Standard Deviation $s$**:
   $$s = \sqrt{1.20567} \approx 1.0980$$

---

### Solution, step 3: Reference line formulation

**Solution, step 3: Reference line formulation.**

The standard Q-Q reference line passes through the distribution parameters $(\bar{y}, s)$:

$$y(q) = \bar{y} + s \cdot q = 0.044 + 1.0980 \cdot q$$

Let us check the expected values at the theoretical quantiles:
- At $q = 0$: $y(0) = 0.044$
- At $q_1 = -1.5466$: $y(q_1) = 0.044 + 1.0980 \times (-1.5466) = 0.044 - 1.6982 = -1.6542$
- At $q_{10} = +1.5466$: $y(q_{10}) = 0.044 + 1.0980 \times (+1.5466) = 0.044 + 1.6982 = +1.7422$

---

### Solution, step 4: Confidence envelopes for extreme order statistics

**Solution, step 4: Confidence envelopes for extreme order statistics.**

For $i = 10$:
- $p_{10} = 0.939024$
- $q_{10} = 1.5466$
- The standard normal probability density at $q_{10}$ is:
  $$\phi(q_{10}) = \frac{1}{\sqrt{2\pi}} e^{-q_{10}^2 / 2} = \frac{1}{\sqrt{2\pi}} e^{-(1.5466)^2 / 2} = \frac{1}{\sqrt{2\pi}} e^{-1.1960} \approx 0.398942 \times 0.30240 \approx 0.12064$$

Now compute the asymptotic standard error:
$$\text{SE}(Y_{(10)}) \approx \frac{s}{\phi(q_{10})} \sqrt{\frac{p_{10} (1 - p_{10})}{n}}$$
$$\sqrt{\frac{0.939024 \times (1 - 0.939024)}{10}} = \sqrt{\frac{0.939024 \times 0.060976}{10}} = \sqrt{\frac{0.057258}{10}} = \sqrt{0.0057258} \approx 0.075669$$

Substitute $s = 1.0980$ and $\phi(q_{10}) = 0.12064$:
$$\text{SE}(Y_{(10)}) \approx \frac{1.0980}{0.12064} \times 0.075669 \approx 9.10146 \times 0.075669 \approx 0.6887$$

The $95\%$ pointwise confidence interval for the 10th order statistic is:
$$\text{Expected}_{10} \pm 1.96 \times \text{SE}(Y_{(10)}) = 1.7422 \pm 1.96 \times 0.6887 = 1.7422 \pm 1.3499$$
$$\text{CI}_{95}(Y_{(10)}) = [0.3923, 3.0921]$$

- Observed value: $y_{(10)} = 1.95$.
- Because $0.3923 \le 1.95 \le 3.0921$, the extreme positive observation falls **comfortably within the $95\%$ envelope**.

By symmetry, for $i = 1$:
$$\text{SE}(Y_{(1)}) \approx 0.6887$$
$$\text{CI}_{95}(Y_{(1)}) = -1.6542 \pm 1.3499 = [-3.0041, -0.3043]$$
- Observed value: $y_{(1)} = -1.82$.
- Because $-3.0041 \le -1.82 \le -0.3043$, the extreme negative observation also falls **strictly within the $95\%$ envelope**.

#### Conclusion:
There is no statistically significant evidence of heavy tails or departure from normality; the residuals conform to the Gaussian assumption.

---

## Fully worked question 3: Visual Perception Principles: Weber–Fechner Law and Comparative Visual Decoding Efficiency Across Graphic Encodings

### Question
An institutional biostatistics director redesigns a quarterly executive dashboard summarizing mortality rates across $K = 5$ regional hospital networks:

$$\text{Mortality Rates (\%)}: \mathbf{M} = [A: 4.2\%, \, B: 5.8\%, \, C: 7.1\%, \, D: 8.5\%, \, E: 12.0\%]$$

The design team evaluates three alternative visualization proposals:
- **Design 1 (Angle / Pie Chart)**: Encodes mortality percentage as the central angle of a circular sector: $\theta_k = 360^\circ \times (M_k / \sum M_j)$.
- **Design 2 (Area / Proportional Bubble Chart)**: Encodes mortality as circular disks where disk area is proportional to mortality: $\text{Area}_k \propto M_k$.
- **Design 3 (Position along a Common Linear Scale / Dot Plot)**: Encodes mortality directly as linear horizontal position on a standardized axis $[0\%, 15\%]$.

1. Formulate Stevens' Power Law relating subjective perceived magnitude $\psi(I)$ to physical stimulus magnitude $I$:
   $$\psi(I) = c \cdot I^\beta$$
   State the empirical psychophysical exponent $\beta$ for length ($\beta_{length}$), area ($\beta_{area}$), and volume ($\beta_{volume}$).
2. Suppose an observer compares Hospital $B$ ($5.8\%$) and Hospital $E$ ($12.0\%$). The true physical ratio is:
   $$R_{true} = \frac{M_E}{M_B} = \frac{12.0}{5.8} \approx 2.069$$
   Using Stevens' Power Law with empirical area exponent $\beta_{area} = 0.70$ (Flannery's compensation rule), calculate the **subjectively perceived ratio** $\hat{R}_{area}$ under Design 2. By what percentage does the viewer underestimate the relative disparity between hospitals?
3. Calculate the central angles $\theta_B$ and $\theta_E$ under Design 1. Explain the perceptual mechanism (apparent visual flattening, Weber-Fechner angle distortion) that hampers human discrimination between acute angles.
4. Based on the Cleveland-McGill perceptual hierarchy, explain why Design 3 provides mathematically optimal quantitative decoding, and discuss the implications for visual integrity in medical communication.

---

### Solution, step 1: Stevens' Power Law and psychophysical exponents

**Solution, step 1: Stevens' Power Law and psychophysical exponents.**

In 1957, Harvard psychophysicist Stanley Smith Stevens formulated **Stevens' Power Law**, superseding the logarithmic Weber–Fechner law for sensory modalities with power response:

$$\psi(I) = c \cdot I^\beta$$

where:
- $I$ is the objective physical magnitude of the stimulus.
- $\psi(I)$ is the subjective psychological magnitude perceived by the human central nervous system.
- $c$ is a scaling constant.
- $\beta$ is the empirical psychophysical modality exponent.

#### Empirical Exponents for Visual Encodings:
1. **Length (1D Linear Position / Distance)**:
   $$\beta_{length} \approx 0.95 \text{ to } 1.05 \approx 1.0$$
   Human perception of length is essentially **unbiased and linear**. A line twice as long is perceived as exactly twice as long.
2. **Area (2D Geometric Surfaces / Disks / Circles)**:
   $$\beta_{area} \approx 0.65 \text{ to } 0.75 \approx 0.70$$
   Human perception of area suffers from severe **systematic compression (underestimation)**. As physical area expands, the perceived increase lags behind reality.
3. **Volume (3D Objects / Spheres / Bars with Perspective)**:
   $$\beta_{volume} \approx 0.50 \text{ to } 0.60 \approx 0.55$$
   Human perception of 3D volume exhibits catastrophic compression.

---

### Solution, step 2: Perceived ratio under Design 2 (Area Encoding)

**Solution, step 2: Perceived ratio under Design 2 (Area Encoding).**

Under Design 2, disk areas are configured proportional to mortality rates:
$$\text{Area}_k = c_0 \cdot M_k$$

The true physical ratio between Hospital $E$ and Hospital $B$ is:
$$R_{true} = \frac{M_E}{M_B} = \frac{12.0}{5.8} \approx 2.068966$$

Applying Stevens' Power Law with empirical exponent $\beta_{area} = 0.70$:
$$\psi(\text{Area}_E) = c \cdot (\text{Area}_E)^{0.70} = c \cdot (c_0 M_E)^{0.70}$$
$$\psi(\text{Area}_B) = c \cdot (\text{Area}_B)^{0.70} = c \cdot (c_0 M_B)^{0.70}$$

The perceived psychological ratio $\hat{R}_{area}$ is:

$$\hat{R}_{area} = \frac{\psi(\text{Area}_E)}{\psi(\text{Area}_B)} = \left( \frac{M_E}{M_B} \right)^{0.70} = (2.068966)^{0.70}$$

Let us compute $(2.068966)^{0.70}$:
$$\ln(2.068966) \approx 0.727049$$
$$0.70 \times 0.727049 = 0.508934$$
$$\hat{R}_{area} = \exp(0.508934) \approx 1.6635$$

#### Percentage Underestimation:
While Hospital $E$ actually has more than double ($207\%$) the mortality rate of Hospital $B$, human viewers perceiving disk areas perceive Hospital $E$ as being only $1.66\times$ higher!

$$\text{Underestimation Error} = \frac{\hat{R}_{area} - R_{true}}{R_{true}} = \frac{1.6635 - 2.0690}{2.0690} = \frac{-0.4055}{2.0690} \approx -19.6\%$$

The viewer **underestimates the true relative disparity by nearly $20\%$**! In public health governance, this perceptual illusion dangerously minimizes apparent institutional performance gaps.

---

### Solution, step 3: Central angles under Design 1 (Pie Chart)

**Solution, step 3: Central angles under Design 1 (Pie Chart).**

First, compute the total sum of mortality rates across the 5 hospitals:
$$\sum_{j=1}^5 M_j = 4.2 + 5.8 + 7.1 + 8.5 + 12.0 = 37.6\%$$

The central angle for each sector is:
$$\theta_k = 360^\circ \times \left( \frac{M_k}{37.6} \right)$$

1. **Hospital $B$ ($5.8\%$)**:
   $$\theta_B = 360^\circ \times \frac{5.8}{37.6} = 360^\circ \times 0.154255 \approx 55.53^\circ$$

2. **Hospital $E$ ($12.0\%$)**:
   $$\theta_E = 360^\circ \times \frac{12.0}{37.6} = 360^\circ \times 0.319149 \approx 114.89^\circ$$

#### Perceptual Weaknesses of Angle Discrimination:
Psychophysical experiments by Cleveland and McGill demonstrated that human observers do not directly decode the interior vertex angle $\theta$; rather, they rely on a subconscious compromise between **arc length along the circumference** and **sector chord length**.
- Acute angles ($\theta < 60^\circ$, such as $\theta_B = 55.5^\circ$) are systematically judged as smaller than they are, while obtuse angles ($\theta > 90^\circ$, such as $\theta_E = 114.9^\circ$) are judged as larger.
- Furthermore, tilting or rotating the pie chart introduces perspective distortion, altering visible 3D ellipse chords and completely destroying quantitative calibration.

---

### Solution, step 4: Cleveland–McGill synthesis and recommendation of Design 3

**Solution, step 4: Cleveland–McGill synthesis and recommendation of Design 3.**

In Design 3 (Cleveland Dot Plot):
- Each hospital is represented by a crisp geometric dot positioned along an aligned linear horizontal axis spanning $0\%$ to $15\%$.
- The perceptual task belongs to **Rank 1 of the Cleveland–McGill hierarchy: Position along a Common Scale**.

#### Why Design 3 is Mathematically Optimal:
1. **Linear Exponent ($\beta = 1.0$)**:
   Length and position along an axis exhibit $\beta = 1.0$. The perceived ratio matches the physical ratio:
   $$\hat{R}_{pos} = \left( \frac{12.0}{5.8} \right)^{1.0} = 2.069$$
   Zero perceptual distortion or compression.
2. **Minimal Visual Noise**:
   Unlike bar charts (which fill large rectangular areas with ink, encouraging viewers to judge area or length rather than endpoint position), dot plots maximize the **data-ink ratio** (Edward Tufte, 1983).
3. **Direct Confidence Interval Integration**:
   A dot plot effortlessly accommodates horizontal error bars displaying binomial $95\%$ Wilson score confidence intervals for each hospital's mortality rate, allowing executives to visually distinguish statistically significant variations from random chance.

Therefore, **Design 3 is unequivocally the superior graphical choice for scientific and managerial decision-making**.
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(unit3_text)

print("Successfully written deep Unit 3!")
