# tooling/generate-unit-1.py
import os
import re

out_path = "publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-1.md"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

# Build deep sections for Unit 1
unit1_text = r"""# Unit 1: Programming Foundations for Statistical Data: Object Models, Vectors, Data Frames, and Memory Structures in Python and R

## 1.1 Object Models, Dynamic Typing, and Scalar Representations

Statistical computing fundamentally differs from general-purpose systems programming. While commercial software engineering frequently prioritizes input-output throughput, network latency, microservice orchestration, or asynchronous event concurrency, statistical computation revolves around the manipulation, aggregation, and mathematical transformation of structured numerical arrays. Every statistical estimation algorithm—from calculating an elementary sample variance or evaluating a kernel density estimate to fitting high-dimensional penalized regressions or simulating Markov chains—is executed on physical hardware governed by memory hierarchies, CPU caches, and register widths. Consequently, the choice of data representation and the runtime memory overhead imposed by statistical programming languages directly dictate both execution velocity and maximum tractable dataset size.

In contemporary empirical science, econometric modeling, and applied machine learning, two interpreted dynamic languages predominate: Python and R. Although both provide high-level, dynamically typed interactive environments that facilitate rapid exploratory analysis, their underlying object models, internal representations, and memory management paradigms diverge in profound ways that fundamentally impact computational efficiency.

### The CPython Object Architecture and Dynamic Boxing Overhead

In standard Python (CPython), every variable, function, module, and primitive value is represented as a heap-allocated `PyObject` structure. Python does not possess raw primitive scalar types in the sense of C, C++, or Fortran. Even a simple 64-bit floating-point number is an encapsulated, reference-counted heap object.

Under the CPython C API, a floating-point number is represented by the `PyFloatObject` struct:

```c
typedef struct {
    PyObject_HEAD
    double ob_fval;
} PyFloatObject;
```

The macro `PyObject_HEAD` expands to two critical metadata fields:
1. `ob_refcnt`: A 64-bit integer tracking the active reference count of the object for garbage collection purposes.
2. `ob_type`: A 64-bit pointer pointing to the type descriptor struct (`PyTypeObject`), which defines how operations such as addition, string representation, and attribute access are dispatched at runtime.

Because a 64-bit C `double` requires 8 bytes of raw storage, the enclosing `PyObject` header adds an additional 16 bytes (8 bytes for `ob_refcnt` plus 8 bytes for `ob_type`). Accounting for memory allocator padding and alignment constraints, a single Python `float` occupies **24 bytes of memory**—exactly three times the 8 bytes required to store the numerical bits themselves.

Similarly, an integer in Python 3 is an instance of `PyLongObject`, which supports arbitrary precision arithmetic. The structure contains `PyVarObject_HEAD` (including an 8-byte reference count, an 8-byte type pointer, and an 8-byte size field) followed by an array of 30-bit integer digits (`digit ob_digit[1]`). Consequently, even a small integer like `42` consumes **28 bytes of memory** on a 64-bit operating system.

Furthermore, consider a standard Python list containing $N$ floating-point values:

```python
x = [1.5, 2.7, 3.9, ...]
```

A Python list is not a contiguous array of numbers. It is an instance of `PyListObject`, which maintains a dynamically resizable array of pointers (`PyObject** ob_item`). Therefore, each list element requires:
- 8 bytes for the memory pointer stored inside the list's pointer buffer.
- 24 bytes for the separate `PyFloatObject` allocated elsewhere on the memory heap.

Thus, storing $N$ numbers in a native Python list requires at least $32 N$ bytes of memory, compared to the theoretical minimum of $8 N$ bytes. 

Beyond this four-fold memory penalty lies a far more devastating performance bottleneck: **pointer chasing and cache thrashing**. When a loop iterates through a standard Python list:

```python
total = 0.0
for val in x:
    total += val
```

At every iteration, the CPU must dereference a pointer to inspect the heap address of `val`, check its `ob_type` pointer to verify that addition is defined, extract the raw `ob_fval` double, perform the addition, allocate a brand-new `PyFloatObject` on the heap to store the intermediate result (or update reference counts), and repeat. Because individual `PyFloatObject` instances are scattered across arbitrary, non-contiguous regions of the system RAM heap, the CPU hardware prefetcher cannot predict future memory accesses. Every iteration triggers an L1/L2 CPU cache miss, forcing the processor to stall while waiting hundreds of clock cycles for data to arrive from main memory. This dynamic boxing overhead explains why native Python loops are routinely 50 to 200 times slower than compiled C code.

### Garbage Collection and the Cyclic Detector

In CPython, memory management is primarily handled by deterministic **reference counting**. Each time an object reference is duplicated (for instance, by variable assignment or passing an argument to a function), `ob_refcnt` is incremented. When a variable goes out of scope or is deleted, `ob_refcnt` is decremented. When `ob_refcnt` reaches zero, the memory occupied by the object is immediately reclaimed.

However, reference counting fails when objects contain circular references (e.g., container $A$ references container $B$, and container $B$ references container $A$). To resolve circularities, CPython incorporates a generational cyclic garbage collector (`gc`). The cyclic collector prepends a 16-byte `PyGC_Head` header to all container objects (lists, dictionaries, custom class instances), further increasing memory overhead:

```c
typedef union _gc_head {
    struct {
        union _gc_head *gc_next;
        union _gc_head *gc_prev;
        Py_ssize_t gc_refs;
    } gc;
    long double dummy;  /* force alignment */
} PyGC_Head;
```

The collector divides container objects into three generations (Generation 0, 1, and 2) based on survival across collection cycles. Objects in Generation 0 are inspected frequently. Surviving objects are promoted to older generations. During collection, the algorithm temporarily subtracts internal reference counts across container graphs to isolate unreachable reference islands and deallocate orphaned memory. For data-intensive statistical programs processing millions of records, frequent cyclic collector sweeps can introduce unpredictable latency spikes unless explicitly disabled or tuned via `gc.disable()`.

### The R S-Expression (SEXP) Architecture and Homogeneous Vector Primitives

The design philosophy of R, inherited from the classical S language developed by John Chambers, Rick Becker, and Allan Wilks at Bell Laboratories, was engineered explicitly for data analysis. Consequently, R avoids the individual scalar boxing trap by establishing the **homogeneous vector** as its fundamental, atomic unit of computation.

In R, there is no scalar type. The scalar assignment:

```r
x <- 42.5
```

does not create an isolated boxed number. It creates an atomic vector of length $n = 1$ whose storage mode is `double` (internally `REALSXP`).

Under the GNU R C core, all R data structures are encapsulated as **S-expressions (SEXPs)**. A `SEXPREC` header occupies a fixed footprint of **32 bytes** on 64-bit architectures, comprising:
- A 32-bit `sxpinfo` bitfield encoding the SEXP type (`TYPEOF`), garbage collection mark bits, object bit, and reference tracking bits (`REFCNT`).
- Three 64-bit pointer fields: `attrib` (pointing to the linked list of metadata attributes), `gengc_next_node`, and `gengc_prev_node` (used by the generational garbage collector).

Crucially, when R allocates an atomic vector of length $N$ (such as `numeric(N)` or `integer(N)`), it allocates the 32-byte SEXP header followed immediately by a **single contiguous memory buffer** containing the raw payload of $N$ primitive numbers:

$$\text{Total Memory (bytes)} = 32 + \text{itemsize} \times N$$

where $\text{itemsize} = 8$ for double-precision reals (`REALSXP`) and $\text{itemsize} = 4$ for 32-bit integers (`INTSXP`).

Because the payload is stored contiguously in memory, R atomic vectors exhibit outstanding spatial cache locality. When a compiled vectorized internal primitive executes across an R vector, the CPU prefetcher loads contiguous 64-byte cache lines, keeping the execution pipelines continuously saturated without pointer dereferencing delays.

### The Atomic Type Hierarchy in R

R defines six fundamental atomic vector types:
1. **Logical (`LGLSXP`)**: 32-bit signed integers taking values `0` (FALSE), `1` (TRUE), and `-2147483648` (NA). While a single boolean mathematically requires only 1 bit, R stores logicals as 4-byte integers to facilitate fast word-aligned CPU access and accommodate the ternary sentinel value for missingness.
2. **Integer (`INTSXP`)**: 32-bit signed two's-complement integers spanning the range $[-2^{31} + 1, 2^{31} - 1]$, with $-2^{31}$ reserved as the missing value sentinel `NA_integer_`.
3. **Double / Real (`REALSXP`)**: 64-bit IEEE 754 floating-point numbers conforming to standard double precision (53 bits of significand, 11 bits of exponent). Missing values are represented by specific IEEE quiet NaN bit patterns.
4. **Complex (`CPLXSXP`)**: Pairs of 64-bit doubles representing real and imaginary parts (16 bytes per element).
5. **Character (`STRSXP`)**: A vector of pointers pointing into the global R string pool (`CHARSXP`). By deduplicating identical string literals in a global hash table, R ensures that storing thousands of duplicate categorical labels incurs zero redundant memory allocation.
6. **Raw (`RAWSXP`)**: Uninterpreted 8-bit bytes (0 to 255), essential for low-level cryptographic hashing, binary file I/O, and serialization protocols.

### Missing Value Representation Across Languages

A crucial distinction in statistical data processing is the handling of missing observations. In pure mathematics and systems programming, missingness is often conflated with floating-point invalidity (NaN) or null pointer references (`NULL` / `None`). In empirical statistics, however, missingness represents an unobserved state of nature requiring rigorous three-valued logical propagation.

In Python:
- Native Python represents missingness using the singleton object `None` (an instance of `NoneType`). However, `None` cannot be stored in a contiguous C numerical array without boxing every element back into a `PyObject*` pointer.
- Standard NumPy arrays traditionally rely on IEEE 754 `NaN` (`numpy.nan`) to signal missing floating-point values. Because `NaN` is a valid floating-point bit pattern, arrays retain contiguous C memory efficiency. However, `NaN` is inherently floating-point: integer arrays in classical NumPy cannot store `NaN` without being implicitly cast to `float64`, which risks losing exact integer precision for values exceeding $2^{53}$. Modern pandas addresses this via nullable array backends (`Int64Dtype`, `boolean`), which maintain a companion boolean bitmask tracking missingness alongside the primitive data buffer.

In R:
- Missingness is natively integrated into the type system via dedicated sentinels:
  - `NA_real_`: A quiet NaN with a specific lower word payload (`0x7FF0000000001954`).
  - `NA_integer_`: The smallest 32-bit signed integer ($-2^{31} = -2147483648$).
  - `NA_character_`: A reserved pointer entry in the global string pool.
  - `NA_logical_`: The integer value $-2147483648$ interpreted in logical contexts.
- These sentinels allow R to support three-valued Kleene logic natively across all vector operations without requiring external libraries or altering array storage modes.

---

## 1.2 NumPy Multidimensional Arrays: Memory Buffers, Strides, and Cache Locality

To overcome Python's dynamic boxing overhead and provide native, C-speed array computation, Travis Oliphant and the scientific Python community unified Numeric and Numarray into **NumPy** in 2006. The central mathematical object of NumPy is the $N$-dimensional array: the `ndarray`.

### Architecture of the `ndarray`

A NumPy `ndarray` cleanly separates array metadata from the underlying memory payload. It consists of a compact Python header object that points to a flat, contiguous block of allocated memory:

```text
+-------------------------------------------------------+
|                   ndarray object                      |
|-------------------------------------------------------|
|  data pointer : void* --------> [ Flat Memory Buffer ]|
|  dtype        : float64                               |
|  ndim         : 2                                     |
|  shape        : (4, 3)                                |
|  strides      : (24, 8)                               |
|  flags        : C_CONTIGUOUS, OWNDATA, WRITEABLE      |
+-------------------------------------------------------+
```

Under the NumPy C API, `PyArrayObject` contains:
- `data`: A `char*` pointer to the initial byte of the memory buffer.
- `nd`: An integer denoting the number of dimensions ($d$).
- `dimensions`: An array of integers of length $d$ specifying the size of each axis (the shape).
- `strides`: An array of integers of length $d$ specifying the number of bytes that must be skipped to advance by one element along each dimension.
- `descr`: A pointer to the `PyArray_Descr` struct defining the data type (`dtype`), item size, byte order (endianness), and alignment.
- `flags`: A bitmask tracking buffer properties, including `C_CONTIGUOUS`, `F_CONTIGUOUS`, `OWNDATA`, `ALIGNED`, and `WRITEABLE`.

### Strides Arithmetic and Flat Index Computation

The strides mechanism is the computational engine of NumPy. It enables arbitrary multidimensional slicing, transposition, flipping, and reshaping in $O(1)$ constant time without copying a single byte of memory.

Given an array of dimension $d$ with shape $(n_0, n_1, \dots, n_{d-1})$ and strides $(s_0, s_1, \dots, s_{d-1})$, the byte offset of an element with multidimensional index $(i_0, i_1, \dots, i_{d-1})$ relative to the base pointer `data` is calculated as:

$$\text{Byte Offset}(i_0, i_1, \dots, i_{d-1}) = \sum_{k=0}^{d-1} i_k \times s_k$$

To access the element, the runtime simply casts the pointer:

$$\text{Address} = \text{data} + \sum_{k=0}^{d-1} i_k \times s_k$$

### Row-Major (C-Contiguous) vs Column-Major (Fortran-Contiguous) Order

The physical memory of a computer is a one-dimensional sequence of byte addresses. To store a multidimensional matrix or tensor, the multidimensional coordinate space must be mapped onto this linear address space.

There are two primary conventions for linearizing multidimensional arrays:

1. **Row-Major Order (C-Contiguous)**:
   In row-major order, elements within the same row are stored consecutively in memory. As the linear address increases, the rightmost (last) index advances the fastest.
   For a two-dimensional matrix of shape $(N, M)$ with item size $b$ bytes:
   $$s_0 = M \times b, \quad s_1 = b$$
   For example, in a $3 \times 4$ array of `float64` ($b = 8$ bytes):
   $$\text{shape} = (3, 4), \quad \text{strides} = (32, 8)$$

2. **Column-Major Order (Fortran-Contiguous)**:
   In column-major order, elements within the same column are stored consecutively in memory. As the linear address increases, the leftmost (first) index advances the fastest.
   For a two-dimensional matrix of shape $(N, M)$ with item size $b$ bytes:
   $$s_0 = b, \quad s_1 = N \times b$$
   For a $3 \times 4$ array of `float64`:
   $$\text{shape} = (3, 4), \quad \text{strides} = (8, 24)$$

By default, NumPy creates arrays in C-contiguous order, whereas R, MATLAB, and Fortran store all matrices and higher-dimensional arrays in Fortran-contiguous order.

### Hardware Cache Implications of Memory Strides

Modern microprocessor architectures do not transfer data from main memory to CPU registers byte-by-byte. Instead, memory is transferred in discrete chunks called **cache lines**, typically 64 bytes in size on x86-64 and ARM architectures.

When a thread accesses a 64-bit double at a specific address, the entire 64-byte cache line containing that double and the next 7 adjacent doubles ($8 \times 8 = 64$ bytes) is loaded into the L1 data cache.

Consider computing row sums versus column sums on a large $N \times M$ matrix stored in C-contiguous order:

**Scenario A: Row Summation (C-Contiguous Traversals)**
```python
# Sequential access along inner dimension
total = 0.0
for i in range(N):
    for j in range(M):
        total += A[i, j]
```
Here, index $j$ increments by 1. The byte offset advances by $s_1 = 8$ bytes at each step. Access is sequential. The first access fetches a 64-byte cache line containing 8 doubles. The subsequent 7 iterations read directly from the ultra-fast L1 cache (latency $\sim 1$ nanosecond). The CPU hardware prefetcher detects the sequential linear access pattern and automatically prefetches subsequent cache lines from RAM before the execution pipeline even requests them. Cache utilization is $100\%$.

**Scenario B: Column Summation (Strided Strided Traversal)**
```python
# Strided access along outer dimension
total = 0.0
for j in range(M):
    for i in range(N):
        total += A[i, j]
```
Here, index $i$ increments by 1. The byte offset advances by $s_0 = M \times 8$ bytes at each step. If $M$ is large (e.g., $M = 100,000$), each step jumps $800,000$ bytes across memory. Every single memory access lands on a completely different cache line! Only one 8-byte value is used out of the 64 bytes transferred, wasting $87.5\%$ of memory bus bandwidth. Furthermore, older cache lines are evicted before they can be reused. This phenomenon, known as **cache thrashing**, can cause strided traversal to execute 10 to 50 times slower than contiguous traversal.

### Zero-Copy Array Transformations: Views vs Copies

Because NumPy arrays rely on strides, many complex geometric transformations do not require memory allocation:
- **Transposition (`A.T`)**: Transposing an array of shape $(N, M)$ with strides $(s_0, s_1)$ simply constructs a new `ndarray` header with shape $(M, N)$ and strides $(s_1, s_0)$, pointing to the exact same memory buffer.
- **Slicing (`A[::2, ::3]`)**: Strided slicing adjusts the base pointer and multiplies the strides ($s_0 \times 2, s_1 \times 3$). No data is copied.
- **Reshaping (`A.reshape(...)`)**: If the requested dimensions are compatible with the existing stride geometry, `reshape` returns a view. If the layout is non-contiguous and cannot be represented by uniform strides, NumPy allocates a new contiguous buffer, performing a memory copy.

Statisticians must be cautious with views: modifying an element in a view in-place mutates the data in the original parent array, because both headers share the same underlying memory buffer.

---

## 1.3 R Atomic Vectors, Factors, Lists, Attributes, and S3/S4 Object Paradigms

While Python relies on external libraries like NumPy to provide high-performance arrays, R embeds vectorized structures directly into its core language syntax. To organize complex statistical models, summary tables, and categorical classifications, R combines atomic vectors with an extensible **attribute metadata system**.

### The Attribute System in R

In GNU R, any S-expression can carry arbitrary metadata in the form of an **attribute pairlist**. Attributes are key-value pairs attached to the `attrib` pointer in the `SEXPREC` header.

R reserves several special attributes that alter how the runtime interprets and prints vectors:
1. `names`: A character vector assigning string labels to individual elements of a vector or list.
2. `dim`: An integer vector transforming a flat 1D atomic vector into a multidimensional array or 2D matrix.
3. `dimnames`: A list of character vectors providing row, column, and higher-order labels.
4. `class`: A character vector designating the object-oriented class memberships of the structure, governing generic method dispatch.

When the `dim` attribute is attached to a vector:

```r
x <- 1:12
attr(x, "dim") <- c(3, 4)
```

The underlying memory payload of `x` is not altered or reallocated. It remains a contiguous 12-element integer buffer. The presence of the `dim` attribute instructs R to treat `x` as a $3 \times 4$ matrix, indexing it via column-major rules ($x_{i, j} = \text{payload}[(j - 1) \times 3 + i]$).

### Factors: Categorical Encoding and Memory Compression

In statistical modeling, categorical explanatory variables (such as gender, treatment group, socioeconomic stratum, or geographic district) represent discrete levels rather than continuous numerical values.

R represents categorical variables via **factors**. Internally, a factor is an atomic **integer vector** (`INTSXP`) decorated with two mandatory attributes:
1. `levels`: A character vector (`STRSXP`) containing the unique textual category labels.
2. `class`: Set to the string `"factor"` (or `c("ordered", "factor")` for ordinal scales).

Consider a dataset containing $N = 10,000,000$ survey responses where each respondent indicates one of three marital statuses: `"Single"`, `"Married"`, or `"Divorced"`.
- If stored as a raw character vector in naive languages without string pooling, each entry requires full string storage.
- In R, storing this variable as a factor allocates an integer vector of length $10^7$ (occupying $4 \times 10^7$ bytes $\approx 40$ MB) and a single levels vector of length 3 (occupying less than 200 bytes).
The integer values $1, 2, 3$ act as internal indices pointing into the `levels` array.

#### Contrasts and the Design Matrix
Beyond memory compactness, factors serve a vital mathematical function in statistical modeling. When a factor enters a linear model formula:

```r
fit <- lm(y ~ treatment, data = df)
```

The modeling engine consults the factor's `contrasts` attribute (or global options). By default, unordered factors use **dummy (treatment) coding**, mapping a categorical factor with $K$ levels into $K - 1$ binary indicator columns in the regression design matrix $\mathbf{X}$, establishing the first level as the baseline reference category.

### Generic Vectors: Lists (`VECSXP`)

While atomic vectors must be strictly homogeneous (every element must possess the identical data type), empirical data collections frequently require heterogeneous groupings. R fulfills this requirement via the **generic vector**, or **list** (`VECSXP`).

Under the R C API, a `VECSXP` is a contiguous vector of `SEXP` pointers:

```text
+-------------------------------------------------------------+
|                     VECSXP (List)                           |
|-------------------------------------------------------------|
|  attrib pointer : points to names ("model", "resids", ...)  |
|  length         : 3                                         |
|  payload        : [ SEXP* ptr0, SEXP* ptr1, SEXP* ptr2 ]    |
+-------------------------------------------------------------+
                            |            |            |
                            v            v            v
                       (Double Vec)  (Char Vec)  (Nested List)
```

Because each list element is a pointer to an independent SEXP located on the R heap, lists can hold arbitrary mixtures of integers, doubles, matrices, functions, and nested lists. 

In R statistical workflows, almost all complex model outputs—including the results of `lm()`, `glm()`, `prcomp()`, and `kmeans()`—are returned as named lists carrying specific `class` attributes.

### Object-Oriented Paradigms in R: S3, S4, and R6

R features multiple concurrent object-oriented programming paradigms, reflecting its evolution from exploratory data analysis to enterprise software engineering:

#### 1. The S3 System (Informal, Single-Dispatch Generic Functions)
S3 is R's original, most pervasive object system. It is informal, lightweight, and based on generic function dispatch. An S3 object is simply a base type (typically a list or atomic vector) with a `class` attribute.

When an S3 generic function like `summary(obj)` or `plot(obj)` is called, the generic function executes `UseMethod("summary", obj)`. The dispatch engine inspects the `class` vector of `obj`. If `class(obj)` is `"lm"`, the engine searches for a method named `summary.lm()`. If found, it invokes `summary.lm(obj)`. If no class-specific method exists, it falls back to `summary.default()`.

S3 provides minimal formal encapsulation: any user can arbitrarily assign or modify class attributes and internal list elements without validation checks:

```r
# Informal S3 creation
model_obj <- list(coefficients = c(2.5, -1.2), residuals = c(0.1, -0.3, 0.2))
class(model_obj) <- "my_linear_model"

# Method definition
print.my_linear_model <- function(x, ...) {
    cat("Custom Model Coefficients:\n")
    print(x$coefficients)
}
```

#### 2. The S4 System (Formal Classes, Validated Slots, Multiple Dispatch)
Introduced in John Chambers' *Programming with Data* (1998) to enforce rigor in large-scale bioinformatics (such as the Bioconductor project), S4 is a formal, strictly typed object system.

An S4 class is defined explicitly using `setClass()`, specifying named fields known as **slots** and their required data types:

```r
setClass("StatisticalSample",
    slots = list(
        data = "numeric",
        strata = "factor",
        weights = "numeric",
        sample_size = "integer"
    ),
    validity = function(object) {
        if (length(object@data) != length(object@weights)) {
            return("Dimensions of data and weights must match.")
        }
        return(TRUE)
    }
)
```

Key S4 characteristics include:
- **Formal Validation**: Objects are instantiated via `new("StatisticalSample", ...)`. R automatically validates slot types and executes custom validity functions.
- **Slot Access**: Fields are accessed via the `@` operator (e.g., `sample@data`), preventing accidental typo-induced attribute creation.
- **Multiple Dispatch**: S4 generic methods are defined via `setGeneric()` and `setMethod()`. Unlike S3, S4 dispatch can consider the types of **multiple arguments simultaneously** ($f(x, y)$ can dispatch to distinct implementations depending on the joint classes of both $x$ and $y$).

#### 3. R6 and Mutable Reference Classes
Both S3 and S4 adhere to functional programming principles: objects are immutable by default and follow copy-on-modify semantics. 

However, certain computing patterns—such as managing database connections, streaming data pipelines, GUI state managers, and hardware communication—require **mutable reference semantics**, where modifying an object updates its internal state in-place across all referencing variables.

The `R6` package provides encapsulated, reference-based OOP. An R6 object is built upon an R `environment`. Because environments are passed by reference rather than copied, methods inside an R6 class can modify internal fields using `self$field <- new_value` without triggering memory duplication.

---

## 1.4 Copy-on-Modify Semantics vs Pointer References and Memory Mutation

Memory allocation and variable assignment semantics represent one of the most significant behavioral divergences between Python and R. A comprehensive grasp of these mechanics is essential to prevent catastrophic memory consumption and quadratic performance bottlenecks when working with massive empirical datasets.

### R's Copy-on-Modify (CoM) Semantics

In R, data structures behave according to **functional programming principles**: functions should not have side effects on their inputs, and modifying a data object should not silently alter other variables bound to that same data.

To guarantee functional purity without incurring prohibitive memory duplication at every assignment, R utilizes **Copy-on-Modify (CoM)** (also known as copy-on-write).

When a variable is assigned to another variable:

```r
x <- c(1.0, 2.0, 3.0, 4.0)
y <- x
```

R does **not** allocate a second 4-element buffer. Instead, both `x` and `y` point to the identical memory address on the R heap.

To track how many symbols reference a given memory payload, the R `SEXPREC` header maintains reference-tracking metadata. In modern versions of R (R 3.1.0+), this is managed by the `REFCNT` (reference count) field in `sxpinfo`:
- When `x` is initially created, its `REFCNT` is 1.
- When `y <- x` executes, `REFCNT` is incremented to 2.

Now, consider what happens when a mutating operation is applied to `y`:

```r
y[1] <- 99.0
```

Before modifying the memory buffer, the R runtime checks the `REFCNT` of the underlying SEXP:
1. If $\text{REFCNT} = 1$: The object is referenced by only one symbol. R modifies the memory buffer **in-place** without allocating new memory.
2. If $\text{REFCNT} > 1$: The object is shared by multiple symbols. Modifying the buffer in-place would violate functional isolation by silently changing `x`. Therefore, R allocates a brand-new contiguous memory buffer, copies the existing elements into the new buffer, updates the requested element ($y[1] = 99.0$), decrements the `REFCNT` of the original buffer, binds `y` to the new buffer with $\text{REFCNT} = 1$, and leaves `x` pointing undisturbed to the original data.

```text
Initial Assignment (y <- x):
  Symbol 'x' ---> [ SEXP Header: REFCNT=2 ] ---> [ 1.0 | 2.0 | 3.0 | 4.0 ]
  Symbol 'y' ------------^

After Mutation (y[1] <- 99.0):
  Symbol 'x' ---> [ SEXP Header: REFCNT=1 ] ---> [ 1.0 | 2.0 | 3.0 | 4.0 ]
  
  Symbol 'y' ---> [ SEXP Header: REFCNT=1 ] ---> [ 99.0 | 2.0 | 3.0 | 4.0 ]
                  (Newly Allocated Heap Buffer)
```

#### Shallow vs Deep Copies in Data Frames
A standard R `data.frame` is represented internally as a named list of equal-length atomic vectors, where each list element corresponds to a column.

Because of this columnar list architecture, Copy-on-Modify in R is **shallow**:
- If a data frame `df` has 100 columns and 1,000,000 rows (occupying $\sim 800$ MB of RAM), and you execute:
  ```r
  df2 <- df
  df2$column_50[1] <- 42.0
  ```
- R does **not** duplicate all 100 columns. It creates a new list container (`VECSXP`), copies the pointers for the 99 unmodified columns (incrementing their individual reference counts), and allocates a new memory buffer **only for column 50**. The total memory allocated during the modification is merely 8 MB (the size of one column) plus the tiny list header, rather than 800 MB!

#### The Quadratic Memory Allocation Trap in Procedural Loops
A classic pitfall encountered by novice statistical programmers in R is iteratively growing a vector or data frame inside a procedural loop:

```r
# CATASTROPHIC ANTI-PATTERN
result <- numeric(0)
for (i in 1:N) {
    result <- c(result, compute_stat(i))
}
```

At iteration $i$, `result` has length $i - 1$. The concatenation function `c(result, ...)` cannot expand the existing memory buffer in-place because atomic vectors are fixed-size allocations. Consequently, at iteration $i$, R must:
1. Allocate a new heap buffer of size $i \times 8$ bytes.
2. Copy all $i - 1$ existing doubles from the old buffer to the new buffer.
3. Write the new value at position $i$.
4. Mark the old buffer for garbage collection.

The total number of memory write operations across $N$ iterations is:

$$\sum_{i=1}^N (i - 1) = \frac{(N - 1) N}{2} = \mathcal{O}(N^2)$$

For $N = 100,000$, the runtime performs approximately $5 \times 10^9$ unnecessary memory copy operations and allocations, causing execution to grind to a halt.

**The Solution: Vector Preallocation**
By preallocating the vector to its known terminal size before entering the loop:

```r
result <- numeric(N)  # Single O(N) allocation
for (i in 1:N) {
    result[i] <- compute_stat(i)  # In-place modification (REFCNT = 1)
}
```

The memory is allocated exactly once. Because `result` is referenced solely by one symbol, `result[i] <- ...` executes in-place in $\mathcal{O}(1)$ time, yielding total $\mathcal{O}(N)$ complexity.

### Python Reference Semantics and In-Place Mutation

In stark contrast to R's functional Copy-on-Modify paradigm, Python adheres strictly to **reference semantics** (call-by-object-reference).

In Python, variable names are simply pointers (tags) bound to heap objects:

```python
a = [1, 2, 3]
b = a
```

Here, `a` and `b` point to the identical `PyListObject`. If we mutate the object via `b`:

```python
b.append(4)
print(a)  # Outputs [1, 2, 3, 4]!
```

The underlying list is mutated in-place. The modification is immediately visible through symbol `a`. Python does not create a defensive copy unless explicitly instructed via `b = a.copy()` or `copy.deepcopy(a)`.

In NumPy arrays, in-place mutations are executed via indexed slice assignments:

```python
import numpy as np

X = np.ones((1000, 1000))
Y = X  # Y is a reference to X

# Mutating in-place
X[:] = X * 2  # Mutates the underlying memory buffer in-place
```

If a programmer writes `X = X * 2`, Python evaluates the right-hand side, allocates a brand-new 8 MB array, and rebinds the variable name `X` to the new array, leaving `Y` pointing to the original unmodified array. Understanding when an operation mutates in-place (`X[:] = ...`) versus rebinds (`X = ...`) is critical for managing memory consumption in large-scale machine learning workflows.

---

## 1.5 Vectorized Array Broadcasting, SIMD Instructions, and Avoiding Interpreter Loops

Both Python and R are interpreted languages governed by bytecode evaluation loops. In standard CPython, the evaluation loop (`_PyEval_EvalFrameDefault` in `Python/ceval.c`) fetches, decodes, and dispatches bytecode instructions one by one. In GNU R, the AST interpreter (`eval` in `src/main/eval.c`) traverses expression trees.

Because dynamic type checking, argument unpacking, and method lookup occur at every interpreter step, executing scalar operations inside nested procedural loops incurs massive runtime overhead. To achieve high performance, statistical computing relies on **vectorization** and **array broadcasting**.

### Vectorization: Delegating Loops to Compiled Machine Code

In statistical computing, "vectorization" does not merely refer to writing concise code without `for` loops. Fundamentally, vectorization means **delegating execution to tightly compiled low-level C, C++, or Fortran loops** that operate over contiguous memory buffers without returning control to the high-level interpreter between individual scalar operations.

When an addition operation $z = x + y$ is evaluated across two 1,000,000-element vectors:
- **Interpreted Loop**: The high-level interpreter must execute $1,000,000$ loop iterations. In each iteration, it performs bytecode decoding, type inspection, boxing, unboxing, reference count adjustments, and branch prediction checks. Total overhead: $\sim 100$ CPU cycles per addition.
- **Vectorized Kernel**: The interpreter executes a single dispatch call into a compiled C routine (e.g., NumPy's `PyUFunc_Double_Add` or R's `vsize_t` internal vector loop). The compiled kernel executes a single tight assembly loop over raw contiguous memory pointers:
  ```c
  for (size_t i = 0; i < n; i++) {
      z[i] = x[i] + y[i];
  }
  ```
  Total overhead: $\sim 1$ CPU cycle (or fraction of a cycle) per addition.

### Hardware-Level SIMD Parallelism

Modern microprocessors incorporate **SIMD (Single Instruction, Multiple Data)** execution units, including Intel/AMD AVX2 and AVX-512, and ARM NEON.

A standard scalar CPU register holds a single 64-bit value. In contrast, an AVX-512 register is **512 bits wide**, capable of holding **eight 64-bit double-precision floating-point numbers** simultaneously.

When a compiled vectorized kernel is compiled with SIMD vectorization enabled (e.g., via `-mavx2` or `-mavx512f`):
1. The CPU loads eight consecutive 64-bit doubles from vector $x$ into register `ymm0` or `zmm0` in a single clock cycle.
2. The CPU loads eight consecutive 64-bit doubles from vector $y$ into register `ymm1` or `zmm1`.
3. A single SIMD instruction (`_mm512_add_pd`) executes all eight additions simultaneously in the arithmetic logic unit (ALU).
4. The eight results are stored back to main memory or cache in a single instruction.

```text
Scalar Arithmetic (1 operation per cycle):
  x[0] + y[0] ---> z[0]
  x[1] + y[1] ---> z[1]
  x[2] + y[2] ---> z[2]
  ...

SIMD Vector Arithmetic (8 operations per cycle with AVX-512):
  [ x[0] | x[1] | x[2] | x[3] | x[4] | x[5] | x[6] | x[7] ]
                             +
  [ y[0] | y[1] | y[2] | y[3] | y[4] | y[5] | y[6] | y[7] ]
                             =
  [ z[0] | z[1] | z[2] | z[3] | z[4] | z[5] | z[6] | z[7] ]
```

Because SIMD instructions require contiguous memory alignment, native Python lists of boxed `PyObject*` pointers can **never** be auto-vectorized by hardware SIMD execution units. Homogeneous contiguous arrays (NumPy `ndarray` and R atomic vectors) are an absolute prerequisite for SIMD execution.

### The Formal Theory of Array Broadcasting

In empirical data analysis, mathematical operations frequently occur between arrays of different dimensions or shapes. For example, centering a dataset requires subtracting a 1D vector of column means $\boldsymbol{\mu} \in \mathbb{R}^M$ from a 2D data matrix $\mathbf{X} \in \mathbb{R}^{N \times M}$:

$$\tilde{x}_{ij} = x_{ij} - \mu_j$$

In naive programming environments, performing this operation requires explicitly allocating an $N \times M$ matrix containing $N$ duplicated rows of $\boldsymbol{\mu}$, consuming $O(N M)$ redundant memory.

NumPy and modern array frameworks solve this through **broadcasting**: a formal algebraic system that evaluates elementwise operations between arrays of differing shapes **without copying data**.

#### The Broadcasting Compatibility Rules
Two arrays $\mathbf{A}$ and $\mathbf{B}$ are compatible for broadcasting if, starting from their trailing (rightmost) dimensions and moving backward:
1. The dimensions are equal ($n_{A, k} = n_{B, k}$), OR
2. One of the dimensions is exactly 1 ($n_{A, k} = 1$ or $n_{B, k} = 1$).

If an array has fewer dimensions than the other, its shape is prepended with 1s until both shapes match in rank.

#### The Zero-Stride Mechanism
How does NumPy evaluate $\mathbf{X} - \boldsymbol{\mu}$ without allocating memory for the expanded version of $\boldsymbol{\mu}$?

The solution lies in the **strides** vector:
- Suppose $\mathbf{X}$ has shape $(N, M) = (10000, 50)$ and strides $(50 \times 8, 8) = (400, 8)$.
- The mean vector $\boldsymbol{\mu}$ has shape $(50,)$ and strides $(8,)$.
- To broadcast $\boldsymbol{\mu}$ across $\mathbf{X}$, NumPy prepends a dimension of size 1: shape becomes $(1, 50)$ and strides $(0, 8)$.
- Next, NumPy sets the outer dimension to $10,000$ to match $\mathbf{X}$. However, instead of allocating memory and copying the 50 values 10,000 times, NumPy sets the stride for the expanded dimension to **zero**:
  $$\text{shape}(\boldsymbol{\mu}_{broadcast}) = (10000, 50), \quad \text{strides}(\boldsymbol{\mu}_{broadcast}) = (0, 8)$$

Recall the flat memory offset formula:

$$\text{Byte Offset}(i, j) = i \times s_0 + j \times s_1 = i \times 0 + j \times 8 = 8 j$$

Because $s_0 = 0$, the row index $i$ is multiplied by zero! As the compiled loop advances through rows $i = 0, 1, 2, \dots, 9999$, the memory pointer for $\boldsymbol{\mu}$ never moves along the row axis—it continuously reads the exact same 50 memory addresses from L1 cache! 

Broadcasting achieves the computational outcome of an $N \times M$ array operation with zero memory allocation penalty, optimal cache residency, and maximum SIMD efficiency.

---

## Fully worked question 1: Memory Layout, Stride Calculation, and Cache-Friendly Matrix Traversal in NumPy Arrays

### Question
A biostatistical research group processes large-scale clinical genomics datasets. A core computational kernel involves extracting summary statistics across a high-dimensional observation matrix $\mathbf{Z} \in \mathbb{R}^{R \times C}$ containing $R = 8,192$ participant samples and $C = 16,384$ single-nucleotide polymorphisms (SNPs), stored as 64-bit IEEE double-precision floats (`float64`, 8 bytes per element).

The matrix is allocated in memory as a standard C-contiguous NumPy array:

$$\mathbf{Z} \in \mathbb{R}^{8192 \times 16384}$$

1. Calculate the exact memory footprint of the raw data buffer in megabytes (MB) and gigabytes (GB).
2. Compute the exact shape and strides tuple $(s_0, s_1)$ in bytes for $\mathbf{Z}$.
3. An analyst creates a transposed view $\mathbf{W} = \mathbf{Z}^\top$. State the shape, strides, and memory flags of $\mathbf{W}$. Does constructing $\mathbf{W}$ trigger a heap memory allocation of the payload buffer?
4. Two algorithms are evaluated to compute the total sum of all elements in $\mathbf{W}$:
   - **Algorithm 1 (Row-Major Loop)**: Sums row-by-row along the outer dimension of $\mathbf{W}$.
   - **Algorithm 2 (Column-Major Loop)**: Sums column-by-column along the inner dimension of $\mathbf{W}$.
   Assuming a CPU with a 64-byte L1 data cache line size and a least-recently-used (LRU) cache replacement policy, analyze the hardware memory traffic, cache line hit rates, and explain which algorithm executes faster and why.

---

### Solution, step 1: Calculate the memory footprint of the raw data buffer

**Solution, step 1: Calculate the memory footprint of the raw data buffer.**

The total number of floating-point elements $N$ in the matrix $\mathbf{Z}$ is given by the product of its dimensions:

$$N = R \times C = 8,192 \times 16,384$$

Expressing both dimensions as powers of 2:
$$R = 2^{13} = 8,192$$
$$C = 2^{14} = 16,384$$
$$N = 2^{13} \times 2^{14} = 2^{27} = 134,217,728 \text{ elements}$$

Each element is a 64-bit double-precision float, requiring $b = 8 = 2^3$ bytes. The total memory size in bytes is:

$$\text{Bytes} = N \times b = 2^{27} \times 2^3 = 2^{30} \text{ bytes}$$

Using standard binary digital storage units:
$$1 \text{ KiB} = 2^{10} \text{ bytes} = 1,024 \text{ bytes}$$
$$1 \text{ MiB} = 2^{20} \text{ bytes} = 1,048,576 \text{ bytes}$$
$$1 \text{ GiB} = 2^{30} \text{ bytes} = 1,073,741,824 \text{ bytes}$$

Therefore:
$$\text{Memory Footprint} = \frac{2^{30}}{2^{20}} \text{ MiB} = 1,024 \text{ MiB}$$
$$\text{Memory Footprint} = \frac{2^{30}}{2^{30}} \text{ GiB} = 1.0 \text{ GiB (exactly 1,073,741,824 bytes)}$$

The raw data buffer occupies exactly $1.0\text{ GiB}$ ($1,024\text{ MiB}$) of contiguous physical RAM.

---

### Solution, step 2: Compute shape and strides tuple for Z

**Solution, step 2: Compute shape and strides tuple for Z.**

For an array stored in C-contiguous order, the rightmost index (the column index) advances consecutively in memory. 
- The column stride $s_1$ represents the byte distance between adjacent columns in the same row:
  $$s_1 = b = 8 \text{ bytes}$$
- The row stride $s_0$ represents the byte distance between adjacent rows in the same column. Advancing by one row requires skipping an entire row of $C = 16,384$ elements:
  $$s_0 = C \times b = 16,384 \times 8 = 131,072 \text{ bytes}$$

Expressed in powers of 2:
$$s_0 = 2^{14} \times 2^3 = 2^{17} = 131,072 \text{ bytes}$$
$$s_1 = 2^3 = 8 \text{ bytes}$$

Therefore:
- $\text{shape}(\mathbf{Z}) = (8192, 16384)$
- $\text{strides}(\mathbf{Z}) = (131072, 8)$

---

### Solution, step 3: Analyze the transposed view W = Z.T

**Solution, step 3: Analyze the transposed view W = Z.T.**

In NumPy, transposing a 2D matrix exchanges its axis dimensions and strides without modifying or copying the underlying data payload buffer.

1. **Shape of $\mathbf{W}$**:
   $$\text{shape}(\mathbf{W}) = (C, R) = (16384, 8192)$$

2. **Strides of $\mathbf{W}$**:
   $$\text{strides}(\mathbf{W}) = (s_1(\mathbf{Z}), s_0(\mathbf{Z})) = (8, 131072)$$

3. **Memory Allocation**:
   Constructing $\mathbf{W} = \mathbf{Z}^\top$ does **not** trigger any heap memory allocation for data elements. It merely allocates a tiny `PyArrayObject` descriptor struct ($\sim 96$ bytes) whose data pointer points to the identical $1.0\text{ GiB}$ buffer allocated for $\mathbf{Z}$.

4. **Array Flags**:
   - `OWNDATA`: `False` (the array does not own the data buffer; it references $\mathbf{Z}$).
   - `C_CONTIGUOUS`: `False` (advancing by one element along the trailing dimension requires jumping $131,072$ bytes, so it is not row-contiguous).
   - `F_CONTIGUOUS`: `True` (advancing along the leading dimension requires jumping only $8$ bytes, which corresponds exactly to Fortran column-major order).
   - `WRITEABLE`: `True`.

---

### Solution, step 4: Hardware cache analysis of matrix traversal algorithms on W

**Solution, step 4: Hardware cache analysis of matrix traversal algorithms on W.**

Let us evaluate the memory access patterns of the two summation algorithms operating on $\mathbf{W}$:

#### Algorithm 1: Row-Major Traversal on W
The algorithm iterates over rows $i \in [0, 16383]$ and columns $j \in [0, 8191]$:

```python
total = 0.0
for i in range(16384):
    for j in range(8192):
        total += W[i, j]
```

To determine the memory location accessed at step $(i, j)$:

$$\text{Byte Offset}(i, j) = i \times s_0(\mathbf{W}) + j \times s_1(\mathbf{W}) = i \times 8 + j \times 131072$$

In the inner loop, row index $i$ is fixed, and column index $j$ increments by 1.
The memory address advances by:

$$\Delta \text{Offset} = s_1(\mathbf{W}) = 131,072 \text{ bytes} = 128 \text{ KiB}$$

At each step of the inner loop, the access pointer jumps $128\text{ KiB}$ forward through main memory.
- A CPU cache line is $64$ bytes, accommodating $64 / 8 = 8$ doubles.
- Because each jump is $131,072$ bytes, every single inner-loop read lands in a completely different cache line!
- Only 8 bytes out of every 64-byte fetched cache line are consumed. The remaining 56 bytes ($87.5\%$ of memory bus bandwidth) are transferred into cache but never used before being evicted.
- **Cache Hit Rate**: For large matrices where the working set ($1.0\text{ GiB}$) drastically exceeds the L1 data cache capacity (typically $32\text{ KiB}$ to $48\text{ KiB}$ per core), every memory access results in an **L1 cache miss**. The hit rate is essentially **$0\%$**.
- The processor continually stalls, waiting $\sim 50 - 100\text{ ns}$ per access for DRAM retrieval.

#### Algorithm 2: Column-Major Traversal on W
The algorithm iterates over columns $j \in [0, 8191]$ in the outer loop and rows $i \in [0, 16383]$ in the inner loop:

```python
total = 0.0
for j in range(8192):
    for i in range(16384):
        total += W[i, j]
```

In the inner loop, column index $j$ is fixed, and row index $i$ increments by 1.
The memory address advances by:

$$\Delta \text{Offset} = s_0(\mathbf{W}) = 8 \text{ bytes}$$

At each step of the inner loop, the memory address advances contiguously by exactly 8 bytes!
- When $i = 0$, the read misses L1 cache. The memory controller fetches a 64-byte cache line containing elements for $i = 0, 1, 2, 3, 4, 5, 6, 7$.
- For the subsequent 7 iterations ($i = 1, \dots, 7$), the elements are already present in L1 cache. Access latency is $\sim 1\text{ ns}$ (0 clock cycles of wait time).
- Furthermore, the hardware stream prefetcher in the CPU detects the stride of $+8$ bytes and issues speculative burst read requests to L2/L3 cache and DRAM, pre-filling cache lines well before the CPU executes the instructions.
- **Cache Hit Rate**: Exactly 7 out of every 8 accesses hit the L1 cache directly:
  $$\text{Hit Rate} = \frac{7}{8} = 87.5\%$$
  When accounting for L2/L3 prefetching, effective stall cycles drop to near zero.

#### Conclusion:
**Algorithm 2 executes dramatically faster than Algorithm 1** (typically between $8\times$ and $25\times$ speedup on modern hardware), despite performing the exact same mathematical additions. Algorithm 2 respects the physical layout of the memory buffer ($s_0(\mathbf{W}) = 8$), maximizing spatial cache locality and hardware prefetcher efficiency.

---

## Fully worked question 2: Copy-on-Modify Overhead Analysis and In-Place Reference Mutation in R Data Structures

### Question
An ecological monitoring agency analyzes continuous environmental sensor logs. A dataset containing $N = 500,000$ hourly atmospheric readings is imported into GNU R as a numeric vector $x$:

```r
x <- rnorm(500000)
```

1. Based on the R `SEXPREC` architecture, calculate the exact memory footprint in bytes and megabytes (MB) of the vector $x$.
2. An analyst executes the following R code to filter and transform anomalous values:
   ```r
   y <- x
   y[y < -3.0] <- -3.0
   ```
   Explain the exact internal state of the `SEXPREC` headers, the reference counting mechanism (`REFCNT`), and whether memory duplication occurs during the assignment `y <- x` and during the indexed replacement `y[y < -3.0] <- -3.0`.
3. A junior programmer writes a simulation script that aggregates cumulative sensor records across $K = 50,000$ iterations using dynamic vector growth:
   ```r
   cumulative_records <- numeric(0)
   for (k in 1:K) {
       cumulative_records <- c(cumulative_records, sensor_reading(k))
   }
   ```
   Derive the total number of floating-point numbers copied across the $K$ iterations. Calculate the cumulative memory allocated in gigabytes (GB) assuming 8 bytes per double.
4. Contrast this with the preallocated formulation:
   ```r
   cumulative_records <- numeric(K)
   for (k in 1:K) {
       cumulative_records[k] <- sensor_reading(k)
   }
   ```
   Quantify the asymptotic computational complexity and total memory allocation of the preallocated version.

---

### Solution, step 1: Calculate the memory footprint of vector x

**Solution, step 1: Calculate the memory footprint of vector x.**

In GNU R, a numeric atomic vector of type `REALSXP` consists of:
1. A `SEXPREC` header struct containing `sxpinfo` (4 bytes), alignment padding (4 bytes), and three 64-bit pointers (`attrib`, `gengc_next_node`, `gengc_prev_node`, totaling 24 bytes). Total header size: **32 bytes**.
2. A 64-bit integer recording vector length: **8 bytes**. (In 64-bit R with long-vector support, vector length and true length are stored in a 16-byte metadata block).
3. The contiguous memory buffer payload containing $N = 500,000$ double-precision floats, where each double occupies $8$ bytes.

The payload memory is:

$$\text{Payload} = 500,000 \times 8 = 4,000,000 \text{ bytes}$$

Total memory footprint:

$$\text{Total Bytes} = \text{Header} + \text{Payload} = 48 + 4,000,000 = 4,000,048 \text{ bytes}$$

In megabytes (using $1\text{ MB} = 10^6\text{ bytes}$ decimal or $1\text{ MiB} = 2^{20} = 1,048,576\text{ bytes}$ binary):
$$\text{Memory (decimal)} = \frac{4,000,048}{10^6} \approx 4.00005 \text{ MB}$$
$$\text{Memory (binary MiB)} = \frac{4,000,048}{1,048,576} \approx 3.8147 \text{ MiB}$$

The vector occupies approximately $4.0\text{ MB}$ of contiguous memory.

---

### Solution, step 2: Analyze reference counting and Copy-on-Modify during assignment and mutation

**Solution, step 2: Analyze reference counting and Copy-on-Modify during assignment and mutation.**

1. **Step A: Creation of `x`**
   - The expression `x <- rnorm(500000)` allocates a 4 MB `REALSXP` buffer on the R heap.
   - The symbol `x` is bound to this SEXP in the current environment.
   - In R's internal `sxpinfo` bitfield, the reference tracking field is initialized: $\text{REFCNT} = 1$.

2. **Step B: Assignment `y <- x`**
   - The assignment does **not** allocate memory or duplicate the 500,000 floats.
   - The symbol `y` is bound to the exact same memory address as `x`.
   - The R runtime increments the reference counter: $\text{REFCNT} = 2$.
   - Both `x` and `y` share the same 4 MB buffer in physical RAM.

3. **Step C: Logical Indexing Evaluation `y < -3.0`**
   - R evaluates the predicate `y < -3.0`, allocating a temporary logical vector (`LGLSXP`) of length 500,000.
   - Because logicals are 4 bytes each, this temporary vector consumes $500,000 \times 4 = 2,000,000$ bytes ($\sim 2$ MB).

4. **Step D: Indexed Replacement `y[...] <- -3.0`**
   - The runtime intercepts the assignment to `y`. Before mutating memory, it inspects the reference count of the SEXP bound to `y`.
   - Because $\text{REFCNT} = 2$, in-place modification is forbidden (it would mutate `x`, violating functional purity).
   - **Copy-on-Modify is triggered**:
     - R allocates a brand-new 4 MB heap buffer.
     - It copies all 500,000 elements from the original buffer into the new buffer.
     - It modifies the elements satisfying the condition in the new buffer, setting them to $-3.0$.
     - It decrements the reference count of the original buffer ($\text{REFCNT}(x) = 1$).
     - It binds `y` to the new buffer with $\text{REFCNT}(y) = 1$.
   - After this step, `x` and `y` point to completely separate memory addresses, each owning its independent 4 MB buffer.

---

### Solution, step 3: Derive total copied elements and cumulative memory allocation in the dynamic loop

**Solution, step 3: Derive total copied elements and cumulative memory allocation in the dynamic loop.**

Let us trace the dynamic growth loop across iterations $k = 1, 2, \dots, K$, where $K = 50,000$:

```r
cumulative_records <- numeric(0)
for (k in 1:K) {
    cumulative_records <- c(cumulative_records, sensor_reading(k))
}
```

- At iteration $k = 1$: `cumulative_records` has length 0. A new vector of length 1 is allocated. Number of previous elements copied: $0$.
- At iteration $k = 2$: `cumulative_records` has length 1. A new vector of length 2 is allocated. The 1 existing element is copied.
- At iteration $k = 3$: `cumulative_records` has length 2. A new vector of length 3 is allocated. The 2 existing elements are copied.
- At general iteration $k$: `cumulative_records` has length $k - 1$. R allocates a new buffer of length $k$, copies all $k - 1$ existing elements, and writes the new element at index $k$.

#### Total Number of Copied Elements:
The total number of floating-point numbers copied across all $K$ iterations is given by the arithmetic progression:

$$C_{total} = \sum_{k=1}^K (k - 1) = 0 + 1 + 2 + \dots + (K - 1) = \frac{(K - 1) K}{2}$$

Substituting $K = 50,000$:

$$C_{total} = \frac{49,999 \times 50,000}{2} = 49,999 \times 25,000 = 1,249,975,000 \text{ copied doubles}$$

Over **1.249 billion floating-point numbers** are copied!

#### Cumulative Memory Allocated:
At iteration $k$, R allocates a new buffer of size $k \times 8$ bytes.
The cumulative memory allocated across all $K$ iterations is:

$$M_{total} = \sum_{k=1}^K (8 \times k) = 8 \sum_{k=1}^K k = 8 \times \frac{K (K + 1)}{2} = 4 K (K + 1) \text{ bytes}$$

Substituting $K = 50,000$:

$$M_{total} = 4 \times 50,000 \times 50,001 = 200,000 \times 50,001 = 10,000,200,000 \text{ bytes}$$

Converting to gigabytes:
$$\text{Gigabytes (decimal)} = \frac{10,000,200,000}{10^9} \approx 10.0002 \text{ GB}$$
$$\text{Gigabytes (binary GiB)} = \frac{10,000,200,000}{2^{30}} = \frac{10,000,200,000}{1,073,741,824} \approx 9.3134 \text{ GiB}$$

Even though the final data object contains only 50,000 doubles ($400\text{ KB}$ of data), the dynamic concatenation loop forces the memory manager to allocate and discard over **9.3 GiB** of transient heap memory! This causes severe garbage collector thrashing and degrades performance to $\mathcal{O}(K^2)$.

---

### Solution, step 4: Analyze the preallocated implementation

**Solution, step 4: Analyze the preallocated implementation.**

In the preallocated version:

```r
cumulative_records <- numeric(K)
for (k in 1:K) {
    cumulative_records[k] <- sensor_reading(k)
}
```

1. **Memory Allocation**:
   Before entering the loop, `numeric(K)` performs a **single allocation** of a vector of length $K = 50,000$:
   $$\text{Memory} = 48 + 50,000 \times 8 = 400,048 \text{ bytes} \approx 0.38 \text{ MiB}$$

2. **In-Place Mutation**:
   Inside the loop, `cumulative_records` is referenced by only one symbol (`REFCNT = 1`).
   When `cumulative_records[k] <- ...` is evaluated, the R runtime detects $\text{REFCNT} = 1$ and modifies the memory buffer **in-place**.
   No memory is copied, and no new buffers are allocated.

3. **Complexity Comparison**:
   - Number of elements copied: **0**.
   - Total memory allocated: **400 KB** (compared to $9.3\text{ GiB}$ in the dynamic version, a reduction of over $25,000\times$).
   - Time complexity: **$\mathcal{O}(K)$** linear time (compared to $\mathcal{O}(K^2)$ quadratic time).

---

## Fully worked question 3: Vectorized Broadcasting Algebra and Vectorized Execution Benchmarking vs Nested Procedural Loops

### Question
An applied statistician fitting a Gaussian mixture model must compute the pairwise squared Euclidean distance matrix between $M = 2,000$ spatial sensor locations $\mathbf{X} \in \mathbb{R}^{M \times D}$ and $K = 50$ multivariate cluster centroids $\mathbf{C} \in \mathbb{R}^{K \times D}$ in dimension $D = 20$.

The squared Euclidean distance between observation $\mathbf{x}_i \in \mathbb{R}^D$ and centroid $\mathbf{c}_k \in \mathbb{R}^D$ is defined as:

$$d_{ik}^2 = \|\mathbf{x}_i - \mathbf{c}_k\|_2^2 = \sum_{d=1}^D (x_{id} - c_{kd})^2$$

The full distance matrix is $\mathbf{D} \in \mathbb{R}^{M \times K}$, where $D_{ik} = d_{ik}^2$.

1. Derive the shape and strides transformation required to compute the entire matrix $\mathbf{D}$ using NumPy array broadcasting without explicit procedural loops.
2. Formulate the matrix algebraic expansion of $\|\mathbf{x}_i - \mathbf{c}_k\|_2^2$ in terms of matrix multiplication:
   $$\|\mathbf{x}_i - \mathbf{c}_k\|_2^2 = \|\mathbf{x}_i\|_2^2 + \|\mathbf{c}_k\|_2^2 - 2 \mathbf{x}_i^\top \mathbf{c}_k$$
   and demonstrate how this expansion enables computation via highly optimized BLAS Level 3 matrix multiplication (`DGEMM`).
3. Compare the theoretical floating-point operation count (FLOPs) and memory footprint of the broadcasting approach versus the BLAS GEMM approach.
4. Construct a formal execution model comparing a naive three-level nested Python loop versus the vectorized BLAS formulation. Quantify the interpreter overhead ratio assuming the interpreter requires 80 clock cycles per scalar operation while compiled SIMD/BLAS requires 0.5 clock cycles per FLOP.

---

### Solution, step 1: Broadcasting shape and strides derivation

**Solution, step 1: Broadcasting shape and strides derivation.**

We are given:
- Data matrix $\mathbf{X}$ with shape $(M, D) = (2000, 20)$.
- Centroid matrix $\mathbf{C}$ with shape $(K, D) = (50, 20)$.

To compute pairwise differences $x_{id} - c_{kd}$ across all pairs $(i, k)$ and dimensions $d$ simultaneously, we expand both arrays to 3-dimensional tensors:
- We want $\mathbf{X}_{diff}[i, k, d] = \mathbf{X}[i, d] - \mathbf{C}[k, d]$.

1. **Reshaping $\mathbf{X}$**:
   Insert a new axis at dimension 1 (representing clusters $K$):
   $$\mathbf{X}_{3D} = \mathbf{X}[:, \text{np.newaxis}, :] \implies \text{shape} = (M, 1, D) = (2000, 1, 20)$$
   Assuming C-contiguous storage with $b = 8$ bytes:
   $$\text{strides}(\mathbf{X}_{3D}) = (D \times b, D \times b, b) = (160, 160, 8)$$

2. **Reshaping $\mathbf{C}$**:
   Insert a new axis at dimension 0 (representing observations $M$):
   $$\mathbf{C}_{3D} = \mathbf{C}[\text{np.newaxis}, :, :] \implies \text{shape} = (1, K, D) = (1, 50, 20)$$
   $$\text{strides}(\mathbf{C}_{3D}) = (K \times D \times b, D \times b, b) = (8000, 160, 8)$$

3. **Broadcasting Evaluation**:
   When evaluating the difference $\boldsymbol{\Delta} = \mathbf{X}_{3D} - \mathbf{C}_{3D}$:
   - Dimension 0: $\mathbf{X}$ has size $M=2000$, $\mathbf{C}$ has size $1$. Broadcasting matches to $2000$. The stride for dimension 0 in $\mathbf{C}$ becomes $0$.
   - Dimension 1: $\mathbf{X}$ has size $1$, $\mathbf{C}$ has size $K=50$. Broadcasting matches to $50$. The stride for dimension 1 in $\mathbf{X}$ becomes $0$.
   - Dimension 2: Both arrays have size $D=20$. Compatible directly.
   The resulting broadcast tensor has shape:
   $$\text{shape}(\boldsymbol{\Delta}) = (M, K, D) = (2000, 50, 20)$$

4. **Summation over Dimension $D$**:
   Squaring and summing along axis 2 computes $\mathbf{D}$:
   $$\mathbf{D} = \sum_{d=0}^{D-1} \boldsymbol{\Delta}[:, :, d]^2 = \text{np.sum}((\mathbf{X}_{3D} - \mathbf{C}_{3D})**2, \text{axis}=2)$$
   The resulting distance matrix has shape $(M, K) = (2000, 50)$.

---

### Solution, step 2: BLAS GEMM matrix algebraic expansion

**Solution, step 2: BLAS GEMM matrix algebraic expansion.**

Expand the squared Euclidean norm for row vectors $\mathbf{x}_i$ and $\mathbf{c}_k$:

$$\|\mathbf{x}_i - \mathbf{c}_k\|_2^2 = (\mathbf{x}_i - \mathbf{c}_k)(\mathbf{x}_i - \mathbf{c}_k)^\top = \mathbf{x}_i \mathbf{x}_i^\top - 2 \mathbf{x}_i \mathbf{c}_k^\top + \mathbf{c}_k \mathbf{c}_k^\top$$

Notice that:
- $\mathbf{x}_i \mathbf{x}_i^\top = \|\mathbf{x}_i\|_2^2 = \sum_{d=1}^D x_{id}^2$ is the squared Euclidean norm of observation $i$.
- $\mathbf{c}_k \mathbf{c}_k^\top = \|\mathbf{c}_k\|_2^2 = \sum_{d=1}^D c_{kd}^2$ is the squared Euclidean norm of centroid $k$.
- $\mathbf{x}_i \mathbf{c}_k^\top$ is the $(i, k)$-th entry of the matrix product $\mathbf{X} \mathbf{C}^\top$.

Let us define:
- $\mathbf{u} \in \mathbb{R}^M$ as the column vector of row norms of $\mathbf{X}$: $u_i = \|\mathbf{x}_i\|_2^2 = \sum_{d=1}^D x_{id}^2$.
- $\mathbf{v} \in \mathbb{R}^K$ as the row vector of row norms of $\mathbf{C}$: $v_k = \|\mathbf{c}_k\|_2^2 = \sum_{d=1}^D c_{kd}^2$.

The entire $M \times K$ distance matrix can be written in compact matrix notation:

$$\mathbf{D} = \mathbf{u} \mathbf{1}_K^\top + \mathbf{1}_M \mathbf{v} - 2 \mathbf{X} \mathbf{C}^\top$$

where:
- $\mathbf{1}_K \in \mathbb{R}^K$ and $\mathbf{1}_M \in \mathbb{R}^M$ are vectors of ones.
- $\mathbf{u} \mathbf{1}_K^\top$ broadcasts the column vector $\mathbf{u}$ across all $K$ columns.
- $\mathbf{1}_M \mathbf{v}$ broadcasts the row vector $\mathbf{v}$ down all $M$ rows.
- $\mathbf{X} \mathbf{C}^\top$ is a standard matrix-matrix product between an $M \times D$ matrix and a $D \times K$ matrix.

This formulation maps the primary computational workload into a single **BLAS Level 3 `DGEMM`** routine:
$$\mathbf{P} = \mathbf{X} \mathbf{C}^\top$$
`DGEMM` achieves peak theoretical floating-point performance on modern multi-core CPUs by utilizing cache blocking, register tiling, and multi-threaded SIMD parallelization.

---

### Solution, step 3: Flop count and memory footprint comparison

**Solution, step 3: Flop count and memory footprint comparison.**

Let us compare the two approaches for $M = 2,000$, $K = 50$, and $D = 20$:

#### Approach A: 3D Broadcasting Difference
1. **Memory Allocation**:
   Evaluating $\mathbf{X}_{3D} - \mathbf{C}_{3D}$ creates an intermediate tensor of shape $(M, K, D) = (2000, 50, 20) = 2,000,000$ doubles.
   $$\text{Intermediate Memory} = 2,000,000 \times 8 \text{ bytes} = 16,000,000 \text{ bytes} \approx 15.26 \text{ MiB}$$
   Squaring creates another intermediate tensor of $15.26\text{ MiB}$ (unless executed in-place).
   Total temporary memory: $\approx 30.5\text{ MiB}$.
2. **Floating-Point Operations (FLOPs)**:
   - Subtractions: $M \times K \times D = 2,000 \times 50 \times 20 = 2,000,000$ ops.
   - Squaring: $M \times K \times D = 2,000,000$ ops.
   - Summation over $D$: $M \times K \times (D - 1) = 2,000 \times 50 \times 19 = 1,900,000$ ops.
   - Total FLOPs: $2,000,000 + 2,000,000 + 1,900,000 = 5,900,000 \text{ FLOPs} \approx 5.9 \times 10^6 \text{ FLOPs}$.

#### Approach B: Matrix Multiplication (BLAS GEMM)
1. **Memory Allocation**:
   - Vector $\mathbf{u} \in \mathbb{R}^M$: $2,000 \times 8 = 16,000$ bytes ($16\text{ KB}$).
   - Vector $\mathbf{v} \in \mathbb{R}^K$: $50 \times 8 = 400$ bytes.
   - Matrix product $\mathbf{P} = \mathbf{X} \mathbf{C}^\top \in \mathbb{R}^{M \times K}$: $2,000 \times 50 \times 8 = 800,000$ bytes ($800\text{ KB}$).
   - Output matrix $\mathbf{D}$: $800\text{ KB}$.
   - Total memory: $\approx 1.6\text{ MB}$ (nearly **$20\times$ less memory** than 3D broadcasting!).
2. **Floating-Point Operations (FLOPs)**:
   - Norms of $\mathbf{X}$ ($\mathbf{u}$): $M \times D$ multiplications $+ M \times (D - 1)$ additions $= 40,000 + 38,000 = 78,000$ FLOPs.
   - Norms of $\mathbf{C}$ ($\mathbf{v}$): $K \times D$ multiplications $+ K \times (D - 1)$ additions $= 1,000 + 950 = 1,950$ FLOPs.
   - Matrix product $\mathbf{X} \mathbf{C}^\top$: $2 \times M \times K \times D = 2 \times 2,000 \times 50 \times 20 = 4,000,000$ FLOPs.
   - Broadcasting additions/scaling: $M \times K \times 3 = 2,000 \times 50 \times 3 = 300,000$ FLOPs.
   - Total FLOPs: $78,000 + 1,950 + 4,000,000 + 300,000 = 4,379,950 \text{ FLOPs} \approx 4.38 \times 10^6 \text{ FLOPs}$.

#### Summary:
The BLAS GEMM formulation requires **$25\%$ fewer FLOPs** and consumes **$20\times$ less memory**, while executing via hardware-optimized BLAS Level 3 kernels that operate near peak hardware FLOPS.

---

### Solution, step 4: Construct formal execution model comparing naive loops vs vectorized BLAS

**Solution, step 4: Construct formal execution model comparing naive loops vs vectorized BLAS.**

Consider evaluating the distance matrix via a naive procedural Python loop:

```python
D = np.zeros((M, K))
for i in range(M):
    for k in range(K):
        acc = 0.0
        for d in range(D_dim):
            diff = X[i, d] - C[k, d]
            acc += diff * diff
        D[i, k] = acc
```

#### 1. Naive Python Interpreter Overhead:
In the procedural loop, the inner body executes $M \times K \times D = 2,000 \times 50 \times 20 = 2,000,000$ times.
At each scalar iteration:
- The CPython bytecode interpreter executes multiple opcodes (`BINARY_SUBSCR`, `BINARY_SUBTRACT`, `BINARY_MULTIPLY`, `INPLACE_ADD`).
- Each opcode involves dynamic type checks, reference count updates, and boxing/unboxing overhead.
- Given the specification that the interpreter consumes $C_{interp} = 80$ CPU clock cycles per scalar operation:
  $$\text{Total Clock Cycles (Interpreter)} = 2,000,000 \times 80 = 160,000,000 \text{ clock cycles}$$
- On a $3.0\text{ GHz}$ CPU ($3.0 \times 10^9$ cycles/second), the execution time is:
  $$T_{loop} = \frac{160 \times 10^6}{3.0 \times 10^9} \approx 0.0533 \text{ seconds} = 53.3 \text{ ms}$$

#### 2. Vectorized BLAS GEMM Execution:
In the vectorized BLAS formulation:
- Total FLOPs $\approx 4.38 \times 10^6$ operations.
- The compiled C/assembly routines utilize SIMD vector units (e.g., AVX2 fused multiply-accumulate `FMA3`, executing 16 double FLOPs per cycle per core).
- Given the specification of $C_{BLAS} = 0.5$ clock cycles per FLOP (achieving 2 FLOPs per clock cycle on a single core):
  $$\text{Total Clock Cycles (BLAS)} = 4.38 \times 10^6 \times 0.5 = 2,190,000 \text{ clock cycles}$$
- Execution time on the same $3.0\text{ GHz}$ CPU:
  $$T_{BLAS} = \frac{2.19 \times 10^6}{3.0 \times 10^9} \approx 0.00073 \text{ seconds} = 0.73 \text{ ms}$$

#### 3. Overhead Ratio and Speedup Factor:
The theoretical speedup ratio is:

$$\text{Speedup} = \frac{T_{loop}}{T_{BLAS}} = \frac{53.3 \text{ ms}}{0.73 \text{ ms}} \approx 73.0\times$$

When multi-threading is enabled across 8 CPU cores, OpenBLAS/MKL parallelizes the `DGEMM` operation across threads, pushing execution time below $0.15\text{ ms}$, yielding an effective speedup exceeding **$350\times$** compared to the interpreted procedural Python loop.
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(unit1_text)

print("Successfully written deep Unit 1!")
