# tooling/generate-unit-2.py
import os

out_path = "publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-2.md"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

unit2_text = r"""# Unit 2: Data Wrangling, Tabular Transformation, Relational Joins, and Missing-Data Processing

## 2.1 Tabular Architectures: Columnar Stores, Index Structures, and Frame Internals

In statistical analysis and empirical research, data rarely presents itself as pristine, uniformly formatted numerical matrices. Instead, observational studies, clinical trials, and economic censuses yield heterogeneous tabular records: combinations of continuous measurements, discrete integer counts, categorical demographic classifications, temporal timestamps, and unstructured text fields. The fundamental abstraction for organizing such heterogeneous data across modern statistical environments is the **data frame**.

Although both Python and R provide data frame abstractions, their architectural foundations, indexing models, and internal memory layouts differ dramatically. Understanding these internal data structures is essential for designing high-throughput data wrangling workflows that scale gracefully to millions of records without exhausting system memory.

### The R Data Frame Ecosystem: Base `data.frame`, `tibble`, and `data.table`

#### 1. Base R `data.frame`
In base R, a `data.frame` is not a specialized compiled C structure; rather, it is a high-level abstraction constructed atop the foundational S-expression primitives. Specifically, an R `data.frame` is an S3 object whose base type is a **named generic vector (list, `VECSXP`)** of equal-length atomic vectors, decorated with three mandatory attributes:
- `names`: A character vector providing unique column labels.
- `row.names`: An integer or character vector providing row identifiers. (In modern R, compact row names are represented by an integer pair `c(NA, -N)`, avoiding the allocation of $N$ string pointers).
- `class`: Set to `"data.frame"`.

Because a `data.frame` is a list of columns, it constitutes a **column-oriented storage model**. Accessing or extracting an entire column (e.g., `df$age` or `df[["age"]]`) is an $O(1)$ pointer dereference. Conversely, accessing an individual row (e.g., `df[i, ]`) requires slicing across every individual column vector in the list, allocating a brand-new list of 1-element vectors, and copying attributes. Row-wise operations in base R are therefore computationally expensive and should be avoided in favor of columnar transformations.

#### 2. Modern Tidyverse `tibble`
The `tibble` package (part of the tidyverse ecosystem developed by Hadley Wickham and colleagues) re-engineers the base `data.frame` to eliminate historical idiosyncrasies that frequently introduced silent bugs into statistical pipelines:
- **No Partial Matching**: Base R allows partial column name matching (`df$a` matches `df$age`), which can silently introduce subtle errors. `tibble` strictly enforces exact column name lookups.
- **Never Converts Strings to Factors Silently**: Prior to R 4.0.0, base `data.frame` automatically converted character strings to factors (`stringsAsFactors = TRUE`), corrupting arbitrary text identifiers. `tibble` preserves character types strictly.
- **Strict Slicing Invariance**: In base R, slicing a single column via `df[, 1]` drops dimensions and collapses the output into an atomic vector unless `drop = FALSE` is specified. In contrast, `tibble` subsetting `tb[, 1]` always returns a tibble, preserving structural type stability.

#### 3. High-Performance `data.table`
For large-scale statistical computing, Matt Dowle and Arun Srinivasan developed `data.table`. While inheriting from `data.frame`, `data.table` fundamentally re-architects memory mutation and indexing:
- **In-Place Modification (`:=`)**: Unlike base R's Copy-on-Modify semantics, `data.table` uses the `:=` assignment operator to modify column vectors directly in memory via C-level pointer manipulation, bypassing memory duplication.
- **Secondary B-Tree and Radix Keys**: `data.table` allows setting sorted primary and secondary keys (`setkey(dt, id)`). Filtering and joining on keyed columns does not require linear scanning ($O(N)$); instead, it executes via binary search ($O(\log N)$) or ultra-fast radix sorting ($O(N)$ with tiny constants), achieving speedups of 10 to 100 times over standard list filtering.

### Python Tabular Architectures: pandas `DataFrame` and `Series`

In the Python ecosystem, tabular data processing is centered on the `pandas` library, created by Wes McKinney in 2008.

#### The `Series` and `Index` Architecture
A pandas `Series` is a one-dimensional labeled array comprising:
1. A 1D homogeneous NumPy array or extension array holding the raw data values.
2. An `Index` object holding row labels (integers, strings, or datetimes). The `Index` maintains an internal hash table mapping labels to integer array positions, enabling $O(1)$ label-based lookups (`.loc[]`) alongside $O(1)$ positional indexing (`.iloc[]`).

#### The `DataFrame` and the `BlockManager`
Internally, a pandas `DataFrame` (prior to pandas 2.0) organizes columns using a complex memory coordinator known as the **`BlockManager`**. Rather than storing each column as an isolated 1D array, the `BlockManager` consolidates columns of identical data types into 2D NumPy arrays called **Blocks**:
- A `FloatBlock` holding a 2D array of shape $(K_{float}, N)$, consolidating all $K_{float}$ double-precision columns.
- An `IntBlock` holding a 2D array of shape $(K_{int}, N)$, consolidating all integer columns.
- An `ObjectBlock` holding pointers to string or arbitrary Python objects.

While consolidating homogeneous columns enables fast vectorized evaluation across multiple columns simultaneously, the `BlockManager` introduces severe memory fragmentation and copy overhead during column insertions, deletions, and type conversions. 

To overcome these historical limitations, modern pandas 2.0+ and libraries like `Polars` have integrated **Apache Arrow** columnar table structures. Arrow tables store data in contiguous, immutable, chunked record batches with native bitmask-based null handling, facilitating zero-copy sharing between Python, R, and compiled C++ engines.

---

## 2.2 Relational Algebra Joins: Inner, Outer, Semi, Anti, and Join Algorithms

In observational data collection, information is routinely captured across separate domain tables. For example, in an epidemiological cohort study, participant baseline demographics are stored in a patient registry, diagnostic lab results are logged in an electronic medical records database, and prescription records are stored in a pharmacy registry. Combining these heterogeneous tables into an integrated analytic matrix requires **relational joins**.

Relational joins are formal operators of Codd's relational algebra. Let $\mathcal{R}$ and $\mathcal{S}$ denote two relations (data frames) with attribute schemas $\text{attr}(\mathcal{R})$ and $\text{attr}(\mathcal{S})$. Let $\mathcal{K} \subseteq \text{attr}(\mathcal{R}) \cap \text{attr}(\mathcal{S})$ denote the set of common join keys.

### Formal Typology of Relational Joins

1. **Inner Join ($\mathcal{R} \bowtie_{\mathcal{K}} \mathcal{S}$)**:
   Retains only tuples $(r, s) \in \mathcal{R} \times \mathcal{S}$ where the join keys match: $r[\mathcal{K}] = s[\mathcal{K}]$. Tuples in either relation lacking a corresponding partner in the other are discarded:
   $$\mathcal{R} \bowtie \mathcal{S} = \{ (r, s) : r \in \mathcal{R}, s \in \mathcal{S}, r[\mathcal{K}] = s[\mathcal{K}] \}$$

2. **Full Outer Join ($\mathcal{R} \sqsupset\bowtie\sqsubset \mathcal{S}$)**:
   Preserves all tuples from both $\mathcal{R}$ and $\mathcal{S}$. When a tuple $r \in \mathcal{R}$ has no matching tuple in $\mathcal{S}$, it is padded with missing values (`NA` / `NaN`) across the attributes of $\mathcal{S}$, and vice versa.

3. **Left Outer Join ($\mathcal{R} \rtimes \mathcal{S}$)**:
   Preserves all tuples from the left relation $\mathcal{R}$. Unmatched records in $\mathcal{R}$ are padded with nulls across $\text{attr}(\mathcal{S}) \setminus \mathcal{K}$. Records in $\mathcal{S}$ that do not match any row in $\mathcal{R}$ are discarded.

4. **Right Outer Join ($\mathcal{R} \ltimes \mathcal{S}$)**:
   The mirror image of the left join, preserving all tuples from the right relation $\mathcal{S}$.

5. **Semi-Join ($\mathcal{R} \ltimes_{semi} \mathcal{S}$)**:
   Filters the left relation $\mathcal{R}$, returning only those tuples $r \in \mathcal{R}$ for which there exists at least one matching tuple $s \in \mathcal{S}$ with $r[\mathcal{K}] = s[\mathcal{K}]$. Unlike an inner join, a semi-join **never duplicates rows of $\mathcal{R}$** if multiple matching rows exist in $\mathcal{S}$, and none of the attributes of $\mathcal{S}$ are appended to the output schema.

6. **Anti-Join ($\mathcal{R} \triangleright \mathcal{S}$)**:
   The logical complement of the semi-join. Returns only those tuples $r \in \mathcal{R}$ for which **no** matching tuple exists in $\mathcal{S}$. Anti-joins are indispensable in statistical data auditing for detecting missing study participants, dropped follow-up visits, or unmatched survey cohorts.

```text
Relational Join Taxonomy:
+-------------------+---------------------------------------------------+
| Join Type         | Output Row Retention                              |
+-------------------+---------------------------------------------------+
| Inner Join        | Keys present in BOTH R and S                      |
| Left Outer Join   | ALL keys from R; matched keys from S (else NA)    |
| Right Outer Join  | ALL keys from S; matched keys from R (else NA)    |
| Full Outer Join   | ALL keys from BOTH R and S (unmatched padded NA)  |
| Semi-Join         | Rows in R with >= 1 match in S (no S columns)     |
| Anti-Join         | Rows in R with 0 matches in S (no S columns)      |
+-------------------+---------------------------------------------------+
```

### Computational Algorithms for Relational Joins

When computing joins between tables of size $N_R = |\mathcal{R}|$ and $N_S = |\mathcal{S}|$, the execution engine must determine which rows share identical keys. Three fundamental algorithms govern join execution:

#### 1. Nested-Loop Join (Naive vs Block Nested-Loop)
The simplest algorithm iterates across every row of $\mathcal{R}$ and compares it against every row of $\mathcal{S}$:
```python
output = []
for r in R:
    for s in S:
        if r[key] == s[key]:
            output.append(merge(r, s))
```
- **Time Complexity**: $\mathcal{O}(N_R \times N_S)$ comparisons.
- If $N_R = 1,000,000$ and $N_S = 1,000,000$, a nested-loop join requires $10^{12}$ comparisons, which is computationally intractable for interactive data science.
- **Block Nested-Loop Join**: Loads a memory block of $B$ pages of $\mathcal{R}$ into RAM and scans $\mathcal{S}$ once per block, reducing disk I/O but maintaining quadratic $\mathcal{O}(N_R \times N_S)$ CPU complexity.

#### 2. Sort-Merge Join
If both tables are sorted by their join keys $\mathcal{K}$, or can be sorted efficiently:
1. Sort table $\mathcal{R}$ on $\mathcal{K}$ using $O(N_R \log N_R)$ comparisons.
2. Sort table $\mathcal{S}$ on $\mathcal{K}$ using $O(N_S \log N_S)$ comparisons.
3. Advance two pointers concurrently through the sorted tables, matching rows in a single synchronized linear sweep:
   ```text
   Pointer R ---> [ Key 10, Key 12, Key 15, Key 18 ]
   Pointer S ---> [ Key 10, Key 10, Key 15, Key 20 ]
   ```
- **Time Complexity**: $\mathcal{O}(N_R \log N_R + N_S \log N_S + (N_R + N_S))$.
- If tables are already pre-indexed or sorted, the merge phase executes in strictly linear $\mathcal{O}(N_R + N_S)$ time.

#### 3. Classic and Grace Hash Joins
The **Hash Join** is the dominant algorithm utilized by pandas (`merge`), base R (`merge`), dplyr (`left_join`), and SQL database engines for in-memory equijoins.

A hash join operates in two distinct phases:
1. **Build Phase**:
   The engine selects the smaller table (say, $\mathcal{S}$ where $N_S \le N_R$). It allocates an in-memory hash table $\mathcal{H}$. For every tuple $s \in \mathcal{S}$, it computes the hash value $h(s[\mathcal{K}])$ of the join key and inserts a pointer to tuple $s$ into the corresponding bucket of $\mathcal{H}$.
   - Time complexity of build phase: $\mathcal{O}(N_S)$.
   - Space complexity: $\mathcal{O}(N_S)$ hash table storage.
2. **Probe Phase**:
   The engine scans the larger table $\mathcal{R}$ sequentially. For every tuple $r \in \mathcal{R}$, it evaluates $h(r[\mathcal{K}])$, probes the hash table $\mathcal{H}$, and retrieves all candidate matching tuples from $\mathcal{S}$. For each candidate match, it verifies key equality ($r[\mathcal{K}] == s[\mathcal{K}]$) to guard against hash collisions, and outputs the joined row.
   - Time complexity of probe phase: $\mathcal{O}(N_R)$ expected time assuming a uniform hash distribution.

**Total Time Complexity of Hash Join**:
$$\mathcal{O}(N_R + N_S) \text{ expected linear time}$$

The hash join transforms a potentially quadratic operation into an ultra-fast linear operation. However, its performance hinges on having sufficient RAM to house the entire hash table of the build relation. When the build relation exceeds physical memory, database engines fall back to **Grace Hash Joins**, partitioning both relations into disk-backed hash buckets based on higher-order hash bits before joining bucket-by-bucket in memory.

---

## 2.3 Reshaping Algorithms: Wide vs Long Representations and Pivoting Algebra

In empirical data management, datasets are typically structured in one of two canonical forms: **wide format** or **long (tidy) format**. 

### Tidy Data Theory (Hadley Wickham)
In his seminal 2014 paper *Tidy Data*, Hadley Wickham formalized the structural mapping between mathematical variables and tabular storage:
1. Each **variable** forms a column.
2. Each **observation** forms a row.
3. Each type of **observational unit** forms a separate table.

#### Wide vs Long Formats
- **Wide Format**: Often preferred for human data entry, spreadsheet visual review, and repeated-measures multivariate ANOVA. Multiple response measurements taken across time points ($t_1, t_2, t_3$) or experimental conditions are stored in distinct adjacent columns:
  ```text
  SubjectID   Treatment   Time_1   Time_2   Time_3
     101          A        12.4     15.1     18.2
     102          B        10.8     11.2     13.9
  ```
- **Long Format**: Mandatory for modern statistical graphics (ggplot2, seaborn), mixed-effects longitudinal modeling (`lme4`, `statsmodels`), and relational database storage. Every single measurement is represented on its own row, with key indicator columns identifying the context:
  ```text
  SubjectID   Treatment   TimePoint   Measurement
     101          A        Time_1        12.4
     101          A        Time_2        15.1
     101          A        Time_3        18.2
     102          B        Time_1        10.8
     102          B        Time_2        11.2
     102          B        Time_3        13.9
  ```

### Algebraic Mechanics of Pivoting Operations

The transformation between wide and long representations is achieved via two complementary algebraic operations: **pivoting longer (melting / unpivoting)** and **pivoting wider (casting / spreading)**.

#### 1. Pivoting Longer (Unpivoting / Melt)
Let a wide table $\mathbf{W}$ contain $N$ rows, $I$ identification columns $\mathcal{X} = \{X_1, \dots, X_I\}$, and $J$ measurement value columns $\mathcal{Y} = \{Y_1, \dots, Y_J\}$.

The unpivoting operator $\mathcal{U}_{\mathcal{X}, \mathcal{Y}}(\mathbf{W})$ transforms $\mathbf{W}$ into a long table $\mathbf{L}$:
- Number of rows in $\mathbf{L}$: $N \times J$.
- Number of columns in $\mathbf{L}$: $I + 2$ (the $I$ identification variables, plus one new **name variable** storing the column header string $Y_j$, and one new **value variable** storing the scalar measurement).

Internally, this transformation is executed as a Kronecker-style index replication:
1. Replicate each row of the identification columns $\mathcal{X}$ exactly $J$ times consecutively.
2. Flatten the $N \times J$ matrix of values into a single contiguous 1D vector of length $N \times J$ in column-major or row-major order:
   $$\mathbf{v}_{long} = \text{vec}(\mathbf{Y})$$
3. Construct the categorical variable vector by repeating the column labels $Y_1, \dots, Y_J$.

In Python: `pd.melt(df, id_vars=..., value_vars=..., var_name=..., value_name=...)`
In R: `tidyr::pivot_longer(df, cols=..., names_to=..., values_to=...)` or `data.table::melt(dt, id.vars=..., measure.vars=...)`

#### 2. Pivoting Wider (Casting / Spreading)
The inverse operation transforms a long table $\mathbf{L}$ into a wide table $\mathbf{W}$.
Let $\mathbf{L}$ contain identification keys $\mathcal{X}$, a key variable $K$ taking $J$ unique categorical values $\{k_1, \dots, k_J\}$, and a value variable $V$.

Pivoting wider evaluates:
1. **Identification Grouping**: Identify the unique tuple set $\mathcal{U} = \text{unique}(\mathcal{X})$ across the identification columns. Let $M = |\mathcal{U}|$ denote the number of unique observational entities.
2. **Matrix Expansion**: Allocate a target matrix of dimension $M \times J$, initialized with missing value sentinels (`NA`).
3. **Coordinate Scattering**: For each row in $\mathbf{L}$, determine its row index $m \in \{1, \dots, M\}$ corresponding to its ID tuple and its column index $j \in \{1, \dots, J\}$ corresponding to category $k_j$. Scatter value $V$ into cell $(m, j)$:
   $$W_{m, j} = V_{m, k_j}$$
4. **Aggregation on Duplicate Collisions**: If multiple rows in $\mathbf{L}$ share the identical combination of identification keys and column key $(x, k_j)$, a direct cell collision occurs. The pivoting operator must accept an aggregation function (e.g., `mean`, `sum`, `first`) to collapse colliding values into a single scalar:
   $$W_{m, j} = f_{agg}(\{ V_i : x_i = x, k_i = k_j \})$$

In Python: `df.pivot(index=..., columns=..., values=...)` or `df.pivot_table(index=..., columns=..., values=..., aggfunc=...)`
In R: `tidyr::pivot_wider(df, names_from=..., values_from=..., values_fn=...)` or `data.table::dcast(dt, id_vars ~ col_vars, value.var=..., fun.aggregate=...)`

---

## 2.4 Missing Data Representations: IEEE 754 NaN, Nullable Types, and Three-Valued Logic

Missing data represents a pervasive challenge in empirical research. Whether caused by survey non-response, sensor telemetry failure, attrition in randomized clinical trials, or specimen contamination, the statistical computing engine must maintain mathematical consistency when evaluating expressions over unobserved values.

### The Mathematics of Three-Valued Kleene Logic

Classical Boolean logic is two-valued: a proposition is either strictly True ($\top$) or strictly False ($\bot$). 

When missing observations are introduced, Stephen Cole Kleene (1952) established **Three-Valued Logic**, incorporating the third truth value: **Unknown / Missing ($NA$)**.

Under Kleene logic, an expression containing an unknown value evaluates to True or False if and only if its truth value can be determined without knowing the unobserved state:

#### 1. Logical Conjunction (AND, $\land$):
- $\top \land NA = NA$ (If the unknown value is True, the result is True; if False, the result is False. Hence, outcome is Unknown).
- $\bot \land NA = \bot$ (**Crucial**: If one operand is False, the conjunction is guaranteed to be False regardless of what the unknown value is!).
- $NA \land NA = NA$.

#### 2. Logical Disjunction (OR, $\lor$):
- $\top \lor NA = \top$ (**Crucial**: If one operand is True, the disjunction is guaranteed to be True regardless of the unknown value!).
- $\bot \lor NA = NA$.
- $NA \lor NA = NA$.

#### 3. Logical Negation (NOT, $\neg$):
- $\neg NA = NA$.

```text
Kleene 3-Valued Truth Tables:

Conjunction (AND):          Disjunction (OR):           Negation (NOT):
+-------+---+---+----+      +-------+---+---+----+      +---+----+
| AND   | T | F | NA |      | OR    | T | F | NA |      | P | ~P |
+-------+---+---+----+      +-------+---+---+----+      +---+----+
| T     | T | F | NA |      | T     | T | T | T  |      | T | F  |
| F     | F | F | F  |      | F     | T | F | NA |      | F | T  |
| NA    | NA| F | NA |      | NA    | T | NA| NA |      | NA| NA |
+-------+---+---+----+      +-------+---+---+----+      +---+----+
```

### Implementation Divergences Between Python and R

#### 1. The R Implementation: Native Kleene Logic
GNU R natively implements exact Kleene logic across all vectorized boolean operations:

```r
TRUE | NA   # Evaluates to TRUE
FALSE & NA  # Evaluates to FALSE
FALSE | NA  # Evaluates to NA
```

This rigorous behavior extends to indexing: subsetting a vector with a logical vector containing `NA` produces an `NA` element in the resulting subset:

```r
x <- c(10, 20, 30)
x[c(TRUE, NA, FALSE)]  # Evaluates to c(10, NA)
```

To avoid propagating `NA`s into subsets, R programmers use `which()`:

```r
x[which(x > 15)]  # Drops NAs safely
```

#### 2. The Python Implementation: IEEE 754 NaN and Nullable Bitmasks
In standard Python, `numpy.nan` is an IEEE 754 floating-point constant. According to IEEE 754 specifications:
- Any arithmetic operation involving `NaN` evaluates to `NaN`: $x + \text{NaN} = \text{NaN}$.
- **Every comparison against `NaN` evaluates to False**, including self-equality:
  $$\text{NaN} == \text{NaN} \implies \text{False}!$$
To check for missingness in Python, one must never write `x == np.nan`; one must invoke `np.isnan(x)` or `pd.isna(x)`.

In standard Python boolean operations, `np.nan` is considered "truthy" because it is a non-zero object pointer:
```python
bool(np.nan)  # Evaluates to True!
```
This historical conflation of floating-point NaN with logical truthiness caused widespread bugs in conditional indexing. To solve this, modern pandas introduced dedicated **Nullable Boolean Types** (`pd.BooleanDtype()`) that implement full Kleene logic:

```python
import pandas as pd

s1 = pd.Series([True, False, None], dtype="boolean")
s2 = pd.Series([None, None, None], dtype="boolean")

# Correct Kleene propagation
s1 | s2   # Evaluates to [True, <NA>, <NA>]
s1 & False # Evaluates to [False, False, False]
```

---

## 2.5 Split-Apply-Combine Strategies, Grouped Aggregations, and Window Functions

A central paradigm in statistical data transformation is the **Split-Apply-Combine** strategy, formalized by Hadley Wickham in 2011. Complex statistical summaries, hierarchical models, and panel data transformations rarely operate on the entire dataset simultaneously. Instead, the workflow divides a dataset into meaningful statistical sub-populations (strata, geographic units, experimental cohorts), applies statistical models or estimators independently to each subgroup, and recombines the results into a unified summary table.

```text
Split-Apply-Combine Workflow:
       [ Complete Data Frame ]
                  |
        +---------+---------+
        | (Split by Factor) |
        v         v         v
     [Sub-1]   [Sub-2]   [Sub-3]
        |         |         |
        |  (Apply Estimator)|
        v         v         v
     [Est-1]   [Est-2]   [Est-3]
        +---------+---------+
                  |
        (Recombine Outputs)
                  v
       [ Summary Data Frame ]
```

### The Mathematics of Grouped Aggregation

Let a dataset $\mathcal{D} = \{ (\mathbf{x}_i, y_i) \}_{i=1}^N$ be partitioned by a grouping factor $g_i \in \{1, \dots, G\}$ into $G$ mutually disjoint index subsets:

$$\mathcal{I}_g = \{ i \in \{1, \dots, N\} : g_i = g \}, \quad \bigcup_{g=1}^G \mathcal{I}_g = \{1, \dots, N\}, \quad \mathcal{I}_g \cap \mathcal{I}_h = \emptyset \quad (g \ne h)$$

The grouped aggregation operator computes for each group $g$:

$$\theta_g = \mathcal{T}(\{ y_i : i \in \mathcal{I}_g \})$$

where $\mathcal{T}$ represents a statistical aggregation functional, such as the sample mean $\bar{y}_g = \frac{1}{n_g} \sum_{i \in \mathcal{I}_g} y_i$ or sample variance $s_g^2 = \frac{1}{n_g - 1} \sum_{i \in \mathcal{I}_g} (y_i - \bar{y}_g)^2$.

### Execution Engines: Hash Grouping vs Radix Sorting

How does a statistical computing engine partition $N$ rows into $G$ groups in memory?

#### 1. Hash Grouping (pandas `groupby`)
The engine iterates across the grouping vector $g_1, \dots, g_N$. For each element, it hashes the group key $h(g_i)$ and records the row index $i$ in a hash table mapping keys to integer index arrays.
- **Time Complexity**: $\mathcal{O}(N)$ average time.
- **Limitation**: Generating separate index lists for thousands of small groups incurs substantial memory overhead and prevents SIMD hardware vectorization across group boundaries.

#### 2. Radix Sorting (R `data.table`)
The engine performs a fast **in-place radix sort** on the grouping key vector. Because radix sorting evaluates keys bit-by-bit (or byte-by-byte) without pairwise comparisons, it runs in strictly linear $\mathcal{O}(N)$ time with tiny cache-friendly constants.
- Once sorted, all rows belonging to group $g$ occupy a **single contiguous slice of memory** $[i_{start, g}, i_{end, g}]$.
- The engine computes group summaries by sweeping a single pointer across contiguous cache lines, completely eliminating pointer chasing and hash lookups. This architectural design makes `data.table` up to $10\times$ faster than standard hash-based grouping engines.

### Window Functions vs Collapsing Aggregations

It is vital to distinguish between two classes of grouped operations:

1. **Collapsing Aggregations**:
   The operator maps an input group of $n_g$ observations to a **single scalar summary** $\theta_g \in \mathbb{R}$. The resulting table collapses from $N$ rows to $G$ rows.
   - Examples: `sum()`, `mean()`, `median()`, `sd()`, `min()`, `max()`.

2. **Window Functions (Transformations)**:
   The operator maps an input group of $n_g$ observations to an **output vector of identical length $n_g$**. The resulting table retains the original $N$ rows, with each row augmented by a group-contextual measurement.
   - **Ranking Functions**: Computing within-group ranks:
     $$r_{ij} = \text{rank}(y_{ij} \mid \mathcal{I}_g)$$
   - **Centering and Standardization**: Z-score transformation relative to group parameters:
     $$z_{ij} = \frac{y_{ij} - \bar{y}_g}{s_g}$$
   - **Cumulative Statistics**: Rolling sums, cumulative minimums, or running maximums over time within each entity:
     $$c_{it} = \sum_{\tau=1}^t y_{i\tau}$$
   - **Lag / Lead Operators**: Extracting temporal offsets $y_{i, t-1}$ or $y_{i, t+1}$ for panel autoregressions without cross-contaminating distinct subjects.

In Python: `df.groupby('stratum')['measurement'].transform(lambda x: (x - x.mean()) / x.std())`
In R: `dt[, z := (measurement - mean(measurement)) / sd(measurement), by = stratum]`

---

## Fully worked question 1: Complexity Analysis and Execution Mechanics of Hash Joins vs Nested-Loop Joins on Large Relational Frames

### Question
A national health authority links two large-scale administrative medical registers to study post-vaccination outcomes:
1. **Vaccination Registry ($\mathcal{R}$)**: Contains $N_R = 10,000,000$ immunization records. Attributes include `patient_id` (64-bit integer, 8 bytes), `vaccine_date` (8 bytes), and `clinic_id` (4 bytes). Total row size: 20 bytes.
2. **Adverse Event Registry ($\mathcal{S}$)**: Contains $N_S = 200,000$ confirmed adverse clinical events. Attributes include `patient_id` (64-bit integer, 8 bytes), `event_date` (8 bytes), and `diagnostic_code` (4 bytes). Total row size: 20 bytes.

An inner join $\mathcal{R} \bowtie_{patient\_id} \mathcal{S}$ must be executed to identify which vaccinated individuals experienced adverse reactions.

1. Calculate the raw memory size in megabytes (MB) of tables $\mathcal{R}$ and $\mathcal{S}$.
2. Analyze the computational complexity and total number of key comparisons required if the inner join is performed using a naive **Nested-Loop Join**. Assuming a single CPU core performs $2 \times 10^9$ comparisons per second, calculate the execution time in hours or days.
3. Formulate the two-phase execution mechanics of an in-memory **Hash Join**:
   - Specify which table should be designated as the **build relation** and which as the **probe relation**, explaining the theoretical rationale.
   - Assuming the hash table incurs an overhead factor of 2.5 (storing 64-bit keys, 64-bit row pointers, and bucket control headers), calculate the memory required to house the hash table in RAM.
   - Derive the expected number of key comparisons and total execution time assuming an ideal hash function with zero collisions.
4. Calculate the speedup factor achieved by the Hash Join over the Nested-Loop Join.

---

### Solution, step 1: Calculate raw memory size of tables R and S

**Solution, step 1: Calculate raw memory size of tables R and S.**

The memory footprint of each table is given by the product of its row count and row width:

1. **Table $\mathcal{R}$ (Vaccination Registry)**:
   - Row count: $N_R = 10,000,000 = 10^7$ rows.
   - Row size: $b_R = 20$ bytes.
   $$\text{Bytes}(\mathcal{R}) = 10^7 \times 20 = 200,000,000 \text{ bytes}$$
   Using decimal megabytes ($1\text{ MB} = 10^6\text{ bytes}$):
   $$\text{Size}(\mathcal{R}) = \frac{200,000,000}{10^6} = 200 \text{ MB}$$
   In binary mebibytes ($1\text{ MiB} = 2^{20} = 1,048,576\text{ bytes}$):
   $$\text{Size}(\mathcal{R}) = \frac{200,000,000}{1,048,576} \approx 190.73 \text{ MiB}$$

2. **Table $\mathcal{S}$ (Adverse Event Registry)**:
   - Row count: $N_S = 200,000 = 2 \times 10^5$ rows.
   - Row size: $b_S = 20$ bytes.
   $$\text{Bytes}(\mathcal{S}) = 200,000 \times 20 = 4,000,000 \text{ bytes}$$
   $$\text{Size}(\mathcal{S}) = \frac{4,000,000}{10^6} = 4.0 \text{ MB} \quad (\approx 3.81 \text{ MiB})$$

Both tables comfortably fit within standard computer system RAM (which typically ranges from 8 GB to 64 GB).

---

### Solution, step 2: Complexity and execution duration of Nested-Loop Join

**Solution, step 2: Complexity and execution duration of Nested-Loop Join.**

In a naive nested-loop join:
```text
For each record r in R:
    For each record s in S:
        Compare r[patient_id] == s[patient_id]
```

1. **Total Number of Key Comparisons**:
   The algorithm evaluates every pair in the Cartesian product $\mathcal{R} \times \mathcal{S}$:

   $$C_{NL} = N_R \times N_S = 10,000,000 \times 200,000 = 2 \times 10^{12} \text{ comparisons}$$

   The algorithm must perform **two trillion key comparisons**!

2. **Execution Time**:
   The processor executes $R_{comp} = 2 \times 10^9$ comparisons per second ($2\text{ GHz}$ effective comparison rate).
   The time required in seconds is:

   $$T_{NL} = \frac{C_{NL}}{R_{comp}} = \frac{2 \times 10^{12}}{2 \times 10^9} = 1,000 \text{ seconds}$$

   Converting to minutes and hours:
   $$T_{NL} = \frac{1,000}{60} \approx 16.67 \text{ minutes}$$

   Notice that if $\mathcal{S}$ were also a large registry of $10,000,000$ records (e.g., matching across two primary registries), $C_{NL}$ would equal $10^{14}$ comparisons:
   $$T_{NL, large} = \frac{10^{14}}{2 \times 10^9} = 50,000 \text{ seconds} \approx 13.89 \text{ hours}!$$

---

### Solution, step 3: Hash Join execution mechanics, memory sizing, and complexity

**Solution, step 3: Hash Join execution mechanics, memory sizing, and complexity.**

#### 1. Selection of Build vs Probe Relations:
In a classic in-memory hash join, the **smaller relation** must always be selected as the **build relation**, and the larger relation as the **probe relation**.
- Here, $N_S = 200,000 \ll N_R = 10,000,000$.
- We designate **$\mathcal{S}$ as the build relation** and **$\mathcal{R}$ as the probe relation**.
- **Theoretical Rationale**: Building the hash table on $\mathcal{S}$ minimizes hash table memory consumption, ensuring the entire hash structure resides inside the CPU's high-speed L3 hardware cache or local RAM, minimizing cache evictions during the subsequent probe phase.

#### 2. Hash Table Memory Requirement:
Each entry in the hash table requires:
- The 64-bit `patient_id` key: 8 bytes.
- A 64-bit pointer or row index pointing to the tuple in $\mathcal{S}$: 8 bytes.
- Hash bucket metadata, linked-list collision pointers, and bucket array allocation overhead: overhead multiplier $\beta = 2.5$.

$$\text{Effective Bytes per Entry} = (8 + 8) \times 2.5 = 40 \text{ bytes}$$

Total memory required for the hash table:

$$\text{Memory}(\mathcal{H}_S) = N_S \times 40 = 200,000 \times 40 = 8,000,000 \text{ bytes} = 8.0 \text{ MB}$$

In binary MiB:
$$\text{Memory}(\mathcal{H}_S) = \frac{8,000,000}{1,048,576} \approx 7.63 \text{ MiB}$$

An 8 MB hash table fits directly into the L3 cache of modern server and desktop CPUs (which commonly feature 16 MB to 64 MB of L3 cache).

#### 3. Expected Comparisons and Execution Time:
1. **Phase 1 (Build Phase on $\mathcal{S}$)**:
   - Evaluates hash function $h(s[\text{patient\_id}])$ for each of the $N_S = 200,000$ records and inserts into $\mathcal{H}_S$.
   - Number of operations: $N_S = 200,000$ hashes.
2. **Phase 2 (Probe Phase on $\mathcal{R}$)**:
   - Scans table $\mathcal{R}$ sequentially. For each of the $N_R = 10,000,000$ records, computes $h(r[\text{patient\_id}])$ and probes $\mathcal{H}_S$.
   - Assuming an ideal hash function with uniform distribution and zero collisions, probing requires **1 hash lookup and 1 equality check** per row.
   - Number of key comparisons: $N_R = 10,000,000$.

Total key comparisons across both phases:

$$C_{Hash} = N_S + N_R = 200,000 + 10,000,000 = 10,200,000 \text{ comparisons}$$

At $2 \times 10^9$ operations per second:

$$T_{Hash} = \frac{10,200,000}{2 \times 10^9} = 0.0051 \text{ seconds} = 5.1 \text{ milliseconds}$$

---

### Solution, step 4: Speedup factor calculation

**Solution, step 4: Speedup factor calculation.**

We compare the wall-clock execution time of the Nested-Loop Join versus the Hash Join:

$$\text{Speedup} = \frac{T_{NL}}{T_{Hash}} = \frac{1,000 \text{ seconds}}{0.0051 \text{ seconds}} \approx 196,078\times$$

The Hash Join executes approximately **$196,000$ times faster** than the nested-loop join, reducing execution latency from nearly 17 minutes to approximately 5 milliseconds!

---

## Fully worked question 2: Formal Algebraic Transformation of Multi-Index Hierarchical Data from Wide to Normalized Long Form

### Question
An environmental epidemiology research team tracks toxic particulate exposure across industrial monitoring stations. The raw observations are formatted as a wide data matrix $\mathbf{W} \in \mathbb{R}^{S \times (1 + T \cdot P)}$, where:
- $S = 500$ distinct monitoring stations.
- Station identifier: `station_id` (integer).
- $T = 4$ temporal quarters: `Q1`, `Q2`, `Q3`, `Q4`.
- $P = 3$ atmospheric pollutants: `PM2.5`, `NO2`, `SO2`.

The wide columns are labeled hierarchically using compound identifiers:
$$\text{Columns} = [\text{station\_id}, \text{PM2.5\_Q1}, \text{NO2\_Q1}, \text{SO2\_Q1}, \dots, \text{PM2.5\_Q4}, \text{NO2\_Q4}, \text{SO2\_Q4}]$$
Total value columns: $T \times P = 4 \times 3 = 12$ measurement columns.

The analytical protocol requires normalizing this wide matrix into a canonical **Tidy Long Form** $\mathbf{L}$:
$$\text{Schema}(\mathbf{L}) = [\text{station\_id}, \text{quarter}, \text{pollutant}, \text{concentration}]$$

1. Formulate the dimensionality (number of rows and columns) of the target normalized long table $\mathbf{L}$.
2. Define the formal algebraic mapping function $\mathcal{M}: (s, t, p) \mapsto (\text{row}, \text{col})$ that maps a wide cell coordinate into its corresponding row and column position in $\mathbf{L}$.
3. An alternative semi-long representation stores each pollutant as an independent column:
   $$\text{Schema}(\mathbf{L}_{semi}) = [\text{station\_id}, \text{quarter}, \text{PM2.5}, \text{NO2}, \text{SO2}]$$
   Evaluate the structural properties, degrees of sparsity, and statistical modeling tradeoffs (e.g. multivariate regression vs panel fixed-effects) between $\mathbf{L}$ and $\mathbf{L}_{semi}$.
4. Provide the exact mathematical transformation equations to pivot from $\mathbf{L}$ back to $\mathbf{W}$, accounting for potential duplicate cell resolutions.

---

### Solution, step 1: Dimensionality of normalized long table L

**Solution, step 1: Dimensionality of normalized long table L.**

In the wide format $\mathbf{W}$:
- Number of monitoring stations: $S = 500$.
- Each station has $T = 4$ temporal quarters.
- For each quarter, $P = 3$ pollutants are measured.
- Total measurement values per station: $T \times P = 4 \times 3 = 12$.

In the fully normalized long table $\mathbf{L}$:
- Each row represents a single atomic measurement of a specific pollutant at a specific station during a specific quarter.
- The total number of rows $N_L$ is given by the product:
  $$N_L = S \times T \times P = 500 \times 4 \times 3 = 6,000 \text{ rows}$$

- The schema consists of 4 attributes:
  1. `station_id`: Identification key (from original rows).
  2. `quarter`: Categorical factor with 4 levels (`Q1`, `Q2`, `Q3`, `Q4`).
  3. `pollutant`: Categorical factor with 3 levels (`PM2.5`, `NO2`, `SO2`).
  4. `concentration`: Continuous double-precision numerical measurement.

$$\text{Dimensions}(\mathbf{L}) = 6,000 \text{ rows} \times 4 \text{ columns}$$

---

### Solution, step 2: Formal algebraic mapping function

**Solution, step 2: Formal algebraic mapping function.**

Let the wide table $\mathbf{W}$ be indexed by station index $s \in \{0, 1, \dots, S-1\}$.
Let the temporal quarters be indexed by $t \in \{0, 1, \dots, T-1\}$ and pollutants by $p \in \{0, 1, \dots, P-1\}$.

In $\mathbf{W}$, the 12 measurement columns are organized in lexicographical block order:
$$\text{ColIndex}_W(t, p) = 1 + t \times P + p$$
where column 0 is `station_id`.

To map wide cell $\mathbf{W}[s, 1 + t \cdot P + p]$ into long table $\mathbf{L}$:

#### Row Mapping:
Assuming long table $\mathbf{L}$ is sorted primarily by station, secondarily by quarter, and tertiarily by pollutant:

$$\text{RowIndex}_L(s, t, p) = s \times (T \cdot P) + t \times P + p$$

For any given row index $r \in \{0, 1, \dots, 5999\}$ in $\mathbf{L}$, the original indices are retrieved via integer division and modulo arithmetic:
$$s = \lfloor r / (T \cdot P) \rfloor = \lfloor r / 12 \rfloor$$
$$r_{rem} = r \pmod{12}$$
$$t = \lfloor r_{rem} / P \rfloor = \lfloor r_{rem} / 3 \rfloor$$
$$p = r_{rem} \pmod 3$$

#### Column Value Assignments:
$$\mathbf{L}[r, \text{"station\_id"}] = \mathbf{W}[s, \text{"station\_id"}]$$
$$\mathbf{L}[r, \text{"quarter"}] = \text{QuarterLabels}[t]$$
$$\mathbf{L}[r, \text{"pollutant"}] = \text{PollutantLabels}[p]$$
$$\mathbf{L}[r, \text{"concentration"}] = \mathbf{W}[s, 1 + t \times P + p]$$

This bijective mapping preserves all original data values with zero information loss.

---

### Solution, step 3: Tradeoffs between fully long L and semi-long L_semi

**Solution, step 3: Tradeoffs between fully long L and semi-long L_semi.**

Consider the semi-long schema:
$$\text{Schema}(\mathbf{L}_{semi}) = [\text{station\_id}, \text{quarter}, \text{PM2.5}, \text{NO2}, \text{SO2}]$$
- Number of rows: $N_{semi} = S \times T = 500 \times 4 = 2,000$ rows.
- Number of columns: $2 + P = 2 + 3 = 5$ columns.

#### Comparative Statistical Tradeoffs:
1. **Multivariate Regression and Covariance Modeling**:
   - If the research goal is to model how pollutant levels co-vary or to predict one pollutant from another (e.g., regressing $\text{PM2.5}$ on $\text{NO2}$ and $\text{SO2}$), $\mathbf{L}_{semi}$ is vastly superior.
   - In $\mathbf{L}_{semi}$, all three pollutants measured at the same space-time point $(s, t)$ reside in the same row. Fitting a multivariate linear model or calculating the empirical covariance matrix $\boldsymbol{\Sigma}_{3 \times 3} = \text{Cov}(\text{PM2.5}, \text{NO2}, \text{SO2})$ is straightforward.
   - In fully long form $\mathbf{L}$, calculating covariance across pollutants requires complex self-joins or grouped lagging.

2. **Panel Data Fixed-Effects and Pooled Estimators**:
   - If the research goal is to pool all environmental pollutants to evaluate an overarching policy intervention (e.g., an industrial emission tax), the fully long table $\mathbf{L}$ is required.
   - In $\mathbf{L}$, one can specify a unified linear mixed-effects model with crossed random effects:
     $$y_{stp} = \beta_0 + \beta_1 \text{Treatment}_s + \alpha_s + \gamma_t + \delta_p + \epsilon_{stp}$$
     where $\alpha_s$ is station random intercept, $\gamma_t$ is seasonal effect, and $\delta_p$ is pollutant fixed effect.

3. **Missing Data and Asynchronous Sampling**:
   - If sensor technology varies such that some stations record only $\text{PM2.5}$ but never $\text{SO2}$, $\mathbf{L}_{semi}$ must store columns of explicit `NA`s, incurring structural sparsity.
   - Fully long $\mathbf{L}$ simply omits the unmeasured pollutant rows entirely, achieving optimal sparse storage without wasting memory on null cells.

---

### Solution, step 4: Mathematical transformation from L back to W (Pivoting Wider)

**Solution, step 4: Mathematical transformation from L back to W (Pivoting Wider).**

Pivoting $\mathbf{L}$ back to $\mathbf{W}$ requires evaluating a multi-key Cartesian cast.
Let row $i$ of $\mathbf{L}$ have values $(s_i, q_i, p_i, y_i)$.

1. **Unique Identification Partition**:
   Let $\mathcal{U}_S = \text{unique}(\{s_i\}_{i=1}^{N_L})$ denote the set of distinct stations, with cardinality $S = |\mathcal{U}_S| = 500$.
   Let $\mathcal{U}_Q = \{\text{Q1}, \text{Q2}, \text{Q3}, \text{Q4}\}$ and $\mathcal{U}_P = \{\text{PM2.5}, \text{NO2}, \text{SO2}\}$.

2. **Compound Column Construction**:
   Construct the Cartesian product of column keys:
   $$\mathcal{C} = \mathcal{U}_P \times \mathcal{U}_Q = \{ (p, q) : p \in \mathcal{U}_P, q \in \mathcal{U}_Q \}$$
   Each pair $(p, q)$ forms a new wide column named $p\_q$. There are $3 \times 4 = 12$ such compound columns.

3. **Cell Mapping and Duplicate Resolution**:
   For each station $s \in \mathcal{U}_S$ and each compound column $(p, q) \in \mathcal{C}$, the wide cell is populated by the aggregation operator:
   $$W[s, p\_q] = f_{agg}\left( \{ y_i : s_i = s, q_i = q, p_i = p \} \right)$$

   - If the data is uniquely identified (each station has at most one measurement per quarter and pollutant), the set contains exactly one element $\{y_i\}$, and $f_{agg}(\{y_i\}) = y_i$.
   - If no observation exists for that tuple, $W[s, p\_q] = \text{NA}$.
   - If duplicate records occur due to multiple sensors at station $s$, $f_{agg}$ collapses them using an empirical summary, such as the arithmetic mean:
     $$f_{agg}(\mathcal{Y}) = \frac{1}{|\mathcal{Y}|} \sum_{y \in \mathcal{Y}} y$$

This completes the formal algebraic round-trip transformation between wide and long representations.

---

## Fully worked question 3: Three-Valued Logical Propagation and Design-Consistent Imputation Across Grouped Tabular Data

### Question
A socio-economic household living standards survey collects income and demographic data across $G = 3$ administrative districts: North ($N$), Central ($C$), and South ($S$). 

The survey sample contains $n = 12$ households with observed monthly earnings $Y$ (in thousand dollars) and binary formal employment status $E \in \{0, 1, NA\}$:

```text
Household ID   District (G)   Employment (E)   Earnings (Y)
     1              N               1              4.2
     2              N               1              5.0
     3              N              NA              NA
     4              N               0              0.0
     5              C               1              6.5
     6              C              NA              4.8
     7              C               1              7.2
     8              C               0              0.0
     9              S               1              3.8
    10              S               0              0.0
    11              S              NA              NA
    12              S               1              4.0
```

1. Evaluate the three-valued Kleene truth value for the following logical queries across all 12 households:
   - Query A: `E == 1`
   - Query B: `(E == 1) | (Y > 4.5)`
   - Query C: `(E == 0) & (Y > 0.0)`
   State the output boolean vector for each query using ternary values $\{ \text{True}, \text{False}, NA \}$.
2. The missing earnings in households 3, 6, and 11 must be imputed. Compare two imputation strategies:
   - **Strategy 1: Global Mean Imputation**: Impute each missing $Y$ with the overall sample mean of observed earnings $\bar{Y}_{obs}$.
   - **Strategy 2: Grouped District-Conditioned Mean Imputation**: Impute each missing $Y$ with the mean of observed earnings within that household's district: $\bar{Y}_{g, obs}$.
   Calculate the imputed values under both strategies.
3. Prove mathematically why naive mean imputation (both global and grouped) causes an artificial deflation (underestimation) of the sample variance $s^2$, and derive the exact mathematical correction factor for the sample variance under mean imputation.

---

### Solution, step 1: Evaluate Three-Valued Kleene Logic queries across all households

**Solution, step 1: Evaluate Three-Valued Kleene Logic queries across all households.**

Let us evaluate the three queries row-by-row according to formal Kleene logic:

#### Household Data Summary:
- HH 1: $E = 1, Y = 4.2$
- HH 2: $E = 1, Y = 5.0$
- HH 3: $E = NA, Y = NA$
- HH 4: $E = 0, Y = 0.0$
- HH 5: $E = 1, Y = 6.5$
- HH 6: $E = NA, Y = 4.8$
- HH 7: $E = 1, Y = 7.2$
- HH 8: $E = 0, Y = 0.0$
- HH 9: $E = 1, Y = 3.8$
- HH 10: $E = 0, Y = 0.0$
- HH 11: $E = NA, Y = NA$
- HH 12: $E = 1, Y = 4.0$

#### Query A: `E == 1`
Comparing an unknown value $NA$ against 1 yields $NA$.
- HH 1, 2, 5, 7, 9, 12: $1 == 1 \implies \mathbf{True}$
- HH 4, 8, 10: $0 == 1 \implies \mathbf{False}$
- HH 3, 6, 11: $NA == 1 \implies \mathbf{NA}$

$$\text{Result A} = [\top, \top, NA, \bot, \top, NA, \top, \bot, \top, \bot, NA, \top]$$

#### Query B: `(E == 1) | (Y > 4.5)`
Recall the Kleene disjunction rule: $\top \lor NA = \top$, and $\bot \lor NA = NA$.
- HH 1: $(1==1) \lor (4.2 > 4.5) = \top \lor \bot = \mathbf{True}$
- HH 2: $(1==1) \lor (5.0 > 4.5) = \top \lor \top = \mathbf{True}$
- HH 3: $(NA == 1) \lor (NA > 4.5) = NA \lor NA = \mathbf{NA}$
- HH 4: $(0==1) \lor (0.0 > 4.5) = \bot \lor \bot = \mathbf{False}$
- HH 5: $(1==1) \lor (6.5 > 4.5) = \top \lor \top = \mathbf{True}$
- HH 6: $(NA == 1) \lor (4.8 > 4.5) = NA \lor \top = \mathbf{True}$ (**Crucial Kleene rule!** Even though $E$ is unknown, $Y > 4.5$ is True. Therefore the OR condition is guaranteed to be True!)
- HH 7: $(1==1) \lor (7.2 > 4.5) = \top \lor \top = \mathbf{True}$
- HH 8: $(0==1) \lor (0.0 > 4.5) = \bot \lor \bot = \mathbf{False}$
- HH 9: $(1==1) \lor (3.8 > 4.5) = \top \lor \bot = \mathbf{True}$
- HH 10: $(0==1) \lor (0.0 > 4.5) = \bot \lor \bot = \mathbf{False}$
- HH 11: $(NA == 1) \lor (NA > 4.5) = NA \lor NA = \mathbf{NA}$
- HH 12: $(1==1) \lor (4.0 > 4.5) = \top \lor \bot = \mathbf{True}$

$$\text{Result B} = [\top, \top, NA, \bot, \top, \top, \top, \bot, \top, \bot, NA, \top]$$

#### Query C: `(E == 0) & (Y > 0.0)`
Recall the Kleene conjunction rule: $\bot \land NA = \bot$.
- HH 1, 2, 5, 7, 9, 12: $(E == 0)$ is False. $\bot \land (\dots) = \mathbf{False}$.
- HH 4, 8, 10: $(E == 0)$ is True, but $Y > 0.0$ is False ($0.0 > 0.0$ is False). $\top \land \bot = \mathbf{False}$.
- HH 3, 11: $(NA == 0) \land (NA > 0.0) = NA \land NA = \mathbf{NA}$.
- HH 6: $(NA == 0) \land (4.8 > 0.0) = NA \land \top = \mathbf{NA}$.

$$\text{Result C} = [\bot, \bot, NA, \bot, \bot, NA, \bot, \bot, \bot, \bot, NA, \bot]$$

---

### Solution, step 2: Calculate imputed values under Strategy 1 and Strategy 2

**Solution, step 2: Calculate imputed values under Strategy 1 and Strategy 2.**

#### Strategy 1: Global Mean Imputation
The sample contains $n = 12$ total units, of which $m = 9$ have observed earnings:
$$\text{Observed } Y = \{ 4.2, 5.0, 0.0, 6.5, 4.8, 7.2, 0.0, 3.8, 0.0, 4.0 \}$$
Wait, let us list the observed values carefully:
- HH 1: 4.2
- HH 2: 5.0
- HH 4: 0.0
- HH 5: 6.5
- HH 6: 4.8
- HH 7: 7.2
- HH 8: 0.0
- HH 9: 3.8
- HH 10: 0.0
- HH 12: 4.0

Sum of observed earnings:
$$\sum Y_{obs} = 4.2 + 5.0 + 0.0 + 6.5 + 4.8 + 7.2 + 0.0 + 3.8 + 0.0 + 4.0 = 35.5$$
Number of observed units: $n_{obs} = 10$.
$$\bar{Y}_{obs} = \frac{35.5}{10} = 3.55$$

Under Strategy 1:
- Impute HH 3: $Y_3 = 3.55$
- Impute HH 6: Already observed ($Y_6 = 4.8$, no imputation needed).
- Impute HH 11: $Y_{11} = 3.55$

#### Strategy 2: Grouped District-Conditioned Mean Imputation
We calculate the observed mean within each district separately:

1. **District North ($N$)**:
   - Observed: HH 1 (4.2), HH 2 (5.0), HH 4 (0.0).
   - $n_{N, obs} = 3$.
   - $\sum Y_{N, obs} = 4.2 + 5.0 + 0.0 = 9.2$.
   - $\bar{Y}_{N, obs} = \frac{9.2}{3} \approx 3.0667$.
   - **Imputed Value for HH 3**: $Y_3 = 3.067$.

2. **District Central ($C$)**:
   - Observed: HH 5 (6.5), HH 6 (4.8), HH 7 (7.2), HH 8 (0.0).
   - $n_{C, obs} = 4$.
   - $\sum Y_{C, obs} = 6.5 + 4.8 + 7.2 + 0.0 = 18.5$.
   - $\bar{Y}_{C, obs} = \frac{18.5}{4} = 4.625$.
   - (No missing values in Central; HH 6 was observed).

3. **District South ($S$)**:
   - Observed: HH 9 (3.8), HH 10 (0.0), HH 12 (4.0).
   - $n_{S, obs} = 3$.
   - $\sum Y_{S, obs} = 3.8 + 0.0 + 4.0 = 7.8$.
   - $\bar{Y}_{S, obs} = \frac{7.8}{3} = 2.600$.
   - **Imputed Value for HH 11**: $Y_{11} = 2.600$.

Notice how District-Conditioned Imputation preserves the structural geographical gradient: Central households have higher earnings ($\bar{Y}_C = 4.625$) while South households have lower earnings ($\bar{Y}_S = 2.600$). Global imputation blurs this spatial variance.

---

### Solution, step 3: Proof of variance deflation under mean imputation and variance correction factor

**Solution, step 3: Proof of variance deflation under mean imputation and variance correction factor.**

Let a sample of size $n$ consist of $m$ observed units $y_1, \dots, y_m$ and $n - m$ missing units $y_{m+1}, \dots, y_n$.
Let the observed sample mean be:
$$\bar{y}_{obs} = \frac{1}{m} \sum_{i=1}^m y_i$$
and the observed sample variance be:
$$s_{obs}^2 = \frac{1}{m - 1} \sum_{i=1}^m (y_i - \bar{y}_{obs})^2$$

Under mean imputation, every missing unit is assigned the observed mean:
$$y_j^* = \bar{y}_{obs} \quad \text{for } j = m+1, \dots, n$$

#### 1. Mean of the Imputed Dataset:
The overall mean of the completed dataset $\mathbf{y}^* = (y_1, \dots, y_m, y_{m+1}^*, \dots, y_n^*)$ is:
$$\bar{y}^* = \frac{1}{n} \left( \sum_{i=1}^m y_i + \sum_{j=m+1}^n \bar{y}_{obs} \right) = \frac{1}{n} \left( m \bar{y}_{obs} + (n - m) \bar{y}_{obs} \right) = \bar{y}_{obs}$$
The sample mean is preserved unchanged.

#### 2. Variance of the Imputed Dataset:
Now evaluate the sample variance of the completed dataset:
$$s_{imp}^2 = \frac{1}{n - 1} \sum_{i=1}^n (y_i^* - \bar{y}^*)^2$$

Split the sum of squares into the observed and imputed subsets:
$$\sum_{i=1}^n (y_i^* - \bar{y}^*)^2 = \sum_{i=1}^m (y_i - \bar{y}_{obs})^2 + \sum_{j=m+1}^n (y_j^* - \bar{y}_{obs})^2$$

Because $y_j^* = \bar{y}_{obs}$ for all imputed units:
$$(y_j^* - \bar{y}_{obs})^2 = (\bar{y}_{obs} - \bar{y}_{obs})^2 = 0$$

Therefore, the imputed units contribute **exactly zero** to the total sum of squares:
$$\sum_{i=1}^n (y_i^* - \bar{y}^*)^2 = \sum_{i=1}^m (y_i - \bar{y}_{obs})^2 = (m - 1) s_{obs}^2$$

Substituting this into the definition of $s_{imp}^2$:

$$s_{imp}^2 = \frac{m - 1}{n - 1} s_{obs}^2$$

#### 3. Theoretical Variance Deflation:
Because $m < n$, the scaling ratio satisfies:
$$\frac{m - 1}{n - 1} < 1$$

Therefore:
$$s_{imp}^2 < s_{obs}^2$$

Mean imputation **artificially compresses the sample variance**, concentrating mass at the point estimate $\bar{y}_{obs}$ without adding stochastic variability. If an analyst computes standard errors or confidence intervals using $s_{imp}^2 / \sqrt{n}$, the confidence intervals will be severely **under-covered** (too narrow), leading to inflated Type I error rates.

#### 4. The Variance Correction Factor:
To reconstruct an unbiased estimate of the population variance $\sigma^2$ from the mean-imputed dataset, one must invert the deflation ratio:

$$\hat{\sigma}^2_{corrected} = \left( \frac{n - 1}{m - 1} \right) s_{imp}^2$$

In modern statistical practice, rather than applying deterministic mean imputation with post-hoc corrections, statisticians utilize **Multiple Imputation by Chained Equations (MICE)** or **stochastic regression imputation**, which draws imputed values from the predictive distribution $y^* \sim \mathcal{N}(\hat{\mu}, \hat{\sigma}^2)$, correctly reflecting imputation uncertainty.
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(unit2_text)

print("Successfully written deep Unit 2!")
