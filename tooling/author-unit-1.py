# tooling/author-unit-1.py
import os
from pathlib import Path

content = r"""# Unit 1: Programming Foundations for Statistical Data: Object Models, Vectors, Data Frames, and Memory Structures in Python and R

## 1.1 Object Models, Dynamic Typing, and Scalar Representations

Statistical computing fundamentally differs from general-purpose systems programming. While commercial software engineering frequently prioritizes input-output throughput, network latency, or asynchronous event concurrency, statistical computation revolves around the manipulation, aggregation, and mathematical transformation of structured numerical arrays. Every statistical estimation algorithm—from calculating an elementary sample variance to fitting high-dimensional penalized regressions or simulating Markov chains—is executed on physical hardware governed by memory hierarchies, CPU caches, and register widths. Consequently, the choice of data representation and the runtime memory overhead imposed by statistical programming languages directly dictate both execution velocity and maximum tractable dataset size.

In modern data science and applied statistics, two interpreted languages predominate: Python and R. Although both provide high-level, dynamically typed interactive environments that facilitate rapid exploratory analysis, their underlying object models, internal representations, and memory management paradigms diverge in profound ways that fundamentally impact computational efficiency.

### The CPython Object Architecture and Dynamic Boxing Overhead

In standard Python (CPython), every variable, function, module, and primitive value is represented as a heap-allocated `PyObject` structure. Python does not possess raw primitive scalar types in the sense of C or Fortran. Even a simple 64-bit floating-point number is an encapsulated, reference-counted heap object.

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

Because a 64-bit C `double` requires 8 bytes of raw storage, the enclosing `PyObject` header adds an additional 16 bytes (8 bytes for `ob_refcnt` plus 8 bytes for `ob_type`). Accounting for memory allocator padding and alignment constraints, a single Python `float` occupies **24 bytes of memory**—exactly three times the 8 bytes required to store the numerical bits themselves!

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

### The R S-Expression (SEXP) Architecture and Homogeneous Vector Primitives

The design philosophy of R, inherited from the classical S language developed by John Chambers and colleagues at Bell Laboratories, was engineered explicitly for data analysis. Consequently, R avoids the individual scalar boxing trap by establishing the **homogeneous vector** as its fundamental, atomic unit of computation.

In R, there is no scalar type. The scalar assignment:
```r
x <- 42.5
```
does not create an isolated boxed number. It creates an atomic vector of length $n = 1$ whose storage mode is `double` (internally `REALSXP`).

Under the GNU R C core, all R data structures are encapsulated as **S-expressions (SEXPs)**. A `SEXPREC` header occupies a fixed footprint of **32 bytes** on 64-bit architectures, comprising:
- A 32-bit `sxpinfo` bitfield encoding the SEXP type (`TYPEOF`), garbage collection flags, and reference tracking bits.
- Three 64-bit pointer fields: `attrib` (pointing to the linked list of metadata attributes), `gengc_next_node`, and `gengc_prev_node` (used by the generational garbage collector).

Crucially, when R allocates an atomic vector of length $N$ (such as `numeric(N)` or `integer(N)`), it allocates the 32-byte SEXP header followed immediately by a **single contiguous memory buffer** containing the raw payload of $N$ primitive numbers:
$$\text{Total Memory (bytes)} = 32 + \text{itemsize} \times N$$
where $\text{itemsize} = 8$ for double-precision reals (`REALSXP`) and $\text{itemsize} = 4$ for 32-bit integers (`INTSXP`).

Because the payload is stored contiguously in memory, R atomic vectors exhibit outstanding spatial cache locality. When a compiled vectorized internal primitive executes across an R vector, the CPU prefetcher loads contiguous 64-byte cache lines, keeping the execution pipelines continuously saturated.

### The Atomic Type Hierarchy in R

R defines six fundamental atomic vector types:
1. **Logical (`LGLSXP`)**: 32-bit signed integers taking values `0` (FALSE), `1` (TRUE), and `-2147483648` (NA). While a single boolean mathematically requires only 1 bit, R stores logicals as 4-byte integers to facilitate fast word-aligned CPU access and accommodate the ternary sentinel value for missingness.
2. **Integer (`INTSXP`)**: 32-bit signed two's-complement integers spanning the range $[-2^{31} + 1, 2^{31} - 1]$, with $-2^{31}$ reserved as the missing value sentinel `NA_integer_`.
3. **Double / Real (`REALSXP`)**: 64-bit IEEE 754 floating-point numbers conforming to standard double precision (53 bits of significand, 11 bits of exponent). Missing values are represented by specific IEEE quiet NaN bit patterns.
4. **Complex (`CPLXSXP`)**: Pairs of 64-bit doubles representing real and imaginary parts (16 bytes per element).
5. **Character (`STRSXP`)**: A vector of pointers pointing into the global R string pool (`CHARSXP`). By deduplicating identical string literals in a global hash table, R ensures that storing thousands of duplicate categorical labels incurs zero redundant memory allocation.
6. **Raw (`RAWSXP`)**: Uninterpreted 8-bit bytes (0 to 255), essential for low-level cryptographic hashing, binary file I/O, and serialization protocols.

---

## 1.2 NumPy Multidimensional Arrays: Memory Buffers, Strides, and Cache Locality

To overcome Python's dynamic boxing overhead and provide native, C-speed array computation, Travis Oliphant and the scientific Python community unified Numeric and Numarray into **NumPy** in 2006. The central mathematical object of NumPy is the $N$-dimensional array: the `ndarray`.

### Architecture of the `ndarray`
A NumPy `ndarray` separates array metadata from the underlying memory payload. It consists of a compact Python header object that points to a flat, contiguous block of allocated memory:

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

1. **`data`**: A pointer storing the virtual memory address of the first byte of the raw numerical buffer.
2. **`dtype`**: The data type descriptor defining element size, byte order (endianness), and interpretation (e.g., `np.float64`, `np.int32`, `np.complex128`).
3. **`shape`**: A tuple of integers $(D_0, D_1, \dots, D_{d-1})$ specifying the dimensional extent along each axis. The total number of elements in the array is:
   $$N_{total} = \prod_{k=0}^{d-1} D_k$$
4. **`strides`**: A tuple of integers $(s_0, s_1, \dots, s_{d-1})$ defining the exact number of bytes the CPU must step in memory to advance by one unit index along the corresponding axis.
5. **`flags`**: Bit flags recording whether the array owns its memory buffer (`OWNDATA`), whether it is writeable, and whether its memory layout is C-contiguous or Fortran-contiguous.

### The Mathematics of Multi-Dimensional Indexing via Strides

Consider a $d$-dimensional array with shape $(D_0, D_1, \dots, D_{d-1})$ and strides $(s_0, s_1, \dots, s_{d-1})$.
To access an element located at multi-index $(i_0, i_1, \dots, i_{d-1})$, the hardware computes the byte offset relative to the base pointer `data`:
$$\text{Byte Offset}(i_0, i_1, \dots, i_{d-1}) = \sum_{k=0}^{d-1} i_k \cdot s_k$$
The memory address of the element is therefore:
$$\text{Address}(i_0, i_1, \dots, i_{d-1}) = \text{data} + \sum_{k=0}^{d-1} i_k \cdot s_k$$

This indexing formula is universally evaluated in $O(d)$ time regardless of whether the array is contiguous, transposed, sliced, or reshaped!

#### C-Contiguous (Row-Major) Memory Layout
In C-contiguous order (standard in C and Python), the last axis varies fastest in memory. Elements along the same row are adjacent in RAM:
- The stride of the last dimension is equal to the element size: $s_{d-1} = \text{itemsize}$.
- For all preceding dimensions $k < d-1$, the stride is the product of the subsequent dimension sizes:
  $$s_k = s_{k+1} \cdot D_{k+1} = \text{itemsize} \times \prod_{j=k+1}^{d-1} D_j$$

For a 2D matrix of shape $(M, N)$ with 8-byte `float64` elements in C-order:
$$s_1 = 8 \text{ bytes}, \quad s_0 = 8 N \text{ bytes}$$

#### Fortran-Contiguous (Column-Major) Memory Layout
In Fortran-contiguous order (standard in Fortran, MATLAB, and base R), the first axis varies fastest in memory. Elements along the same column are adjacent in RAM:
- The stride of the first dimension is equal to the element size: $s_0 = \text{itemsize}$.
- For all subsequent dimensions $k \ge 1$:
  $$s_k = s_{k-1} \cdot D_{k-1} = \text{itemsize} \times \prod_{j=0}^{k-1} D_j$$

For a 2D matrix of shape $(M, N)$ with 8-byte `float64` elements in Fortran-order:
$$s_0 = 8 \text{ bytes}, \quad s_1 = 8 M \text{ bytes}$$

### Zero-Copy Views versus Memory Duplications

The stride-based architecture of NumPy enables an extraordinarily powerful computational capability: **zero-copy array views**. Many mathematical operations that appear to manipulate data can be executed in $O(1)$ time and zero additional memory by creating a new `ndarray` header with altered `shape` and `strides` pointing to the exact same underlying memory buffer.

1. **Slicing**:
   Taking a regular slice $A[::2, :]$ does not copy data. NumPy creates a view where the row stride is doubled: $s_0' = 2 s_0$.
2. **Transposition**:
   Transposing a 2D matrix $B = A^\top$ does not move a single byte of memory. It simply reverses the shape and stride tuples:
   $$\text{shape}(A^\top) = (D_1, D_0), \quad \text{strides}(A^\top) = (s_1, s_0)$$
   Transposing a million-by-million matrix takes less than one microsecond!
3. **Reshaping**:
   If an array is C-contiguous, reshaping it to a new shape $(D_0', \dots, D_{m-1}')$ such that $\prod D_j' = N_{total}$ is accomplished by calculating new strides without copying memory.

However, zero-copy views introduce a critical computational consequence: **cache non-contiguity**. If a matrix $A$ is C-contiguous, iterating across its rows is fast, but after transposing it to $B = A^\top$, iterating across rows of $B$ jumps through memory by $8 N$ bytes at each step, triggering massive CPU cache thrashing.

---

## 1.3 R Vectors, Matrices, Factors, and Object Paradigms (S3 versus S4)

While NumPy relies on object encapsulation in Python, R’s design maintains mathematical purity by treating statistical data structures as decorated vectors.

### R Matrices as Vectors with Dimension Attributes
In R, a matrix does NOT possess a distinct internal C data type. A matrix is literally a standard atomic vector that possesses a `dim` attribute:
```r
A <- matrix(1:12, nrow = 4, ncol = 3)
```
Internally, R allocates an integer vector of length 12: `c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)`. It then attaches a two-element integer vector `c(4, 3)` to the SEXP's `attrib` linked list under the tag symbol `dim`.

Because R inherits Fortran's column-major convention, matrix elements are stored down columns:
- Memory index 0 holds $A_{1, 1} = 1$
- Memory index 1 holds $A_{2, 1} = 2$
- Memory index 2 holds $A_{3, 1} = 3$
- Memory index 3 holds $A_{4, 1} = 4$
- Memory index 4 holds $A_{1, 2} = 5$
- ... and so on.

The 1D memory offset for a 2D matrix element at row $i$ and column $j$ (1-indexed) is:
$$\text{Index}_{1D}(i, j) = (i - 1) + (j - 1) \times \text{nrow}$$

### Factors: Compact Categorical Encodings and Traps
Categorical variables are ubiquitous in statistical models (treatment groups, demographic classifications, survey strata). Storing repeated text strings (e.g., `"Control"`, `"Placebo"`, `"Treatment A"`) across millions of observations would waste memory and degrade estimation speed.

An R **factor** is an integer vector decorated with two attributes:
1. `class = "factor"`
2. `levels`: A character vector of unique label strings.

If a factor contains $N$ observations spanning $K$ distinct categories:
- The raw data vector consumes $4 N$ bytes (storing integers from $1$ to $K$).
- The levels vector consumes $32 + 8 K$ bytes in the string pool.

#### The Factor Coercion Catastrophe:
Because factors are integers under the hood, calling `as.numeric(f)` on a factor whose levels are numerical strings (e.g. levels `"10"`, `"20"`, `"30"`) does NOT parse the strings. It extracts the underlying integer indices $1, 2, 3$!
To safely recover the numerical values, the statistician must index the levels vector:
```r
x_numeric <- as.numeric(levels(f))[f]
```
This historical quirk illustrates the necessity of understanding internal object representations.

### S3 versus S4 Object-Oriented Paradigms in R

Statistical software requires polymorphic behavior: calling `summary(model)` or `predict(model)` must execute different algorithms depending on whether `model` is a linear regression (`lm`), an analysis of variance (`aov`), or a generalized linear model (`glm`).

#### The S3 System: Informal Single-Dispatch
Introduced in S version 3, the S3 system is an informal, lightweight object paradigm based entirely on attributes and naming conventions:
- An object is declared an S3 class simply by assigning a character vector to its `class` attribute:
  ```r
  obj <- list(coefficients = b, residuals = e)
  class(obj) <- "my_regression"
  ```
- Polymorphic functions are implemented as **generics** that invoke `UseMethod()`:
  ```r
  summary <- function(object, ...) UseMethod("summary")
  ```
- When `summary(obj)` is called, `UseMethod()` inspects `class(obj)` and searches the namespace for a method function named `<generic>.<class>` (e.g. `summary.my_regression`).
- If found, R dispatches execution to that function; otherwise, it falls back to `<generic>.default`.

S3 is extraordinarily flexible and imposes virtually zero dispatch overhead, making it the dominant paradigm across the `stats`, `base`, and `tidyverse` packages. However, it lacks formal type validation: any user can corrupt an object by assigning an arbitrary class string or deleting essential list elements.

#### The S4 System: Formal Validated Multiple-Dispatch
Introduced in S version 4 and formalized by John Chambers, S4 provides industrial-strength object-oriented programming:
- Classes are formally declared via `setClass()` with typed fields known as **slots**:
  ```r
  setClass("LinearModel",
    slots = list(
      coefficients = "numeric",
      residuals = "numeric",
      rank = "integer"
    )
  )
  ```
- Instantiation via `new("LinearModel", ...)` rigorously validates that all slots match their declared types.
- Methods are registered via `setMethod()` and support **multiple dispatch**: the method chosen at runtime can depend on the classes of *multiple* arguments simultaneously, rather than just the first argument.

The Bioconductor project for computational genomics relies almost exclusively on S4, ensuring that massive genomic range data structures maintain strict structural validity across complex analytical pipelines.

---

## 1.4 Memory Semantics: Copy-on-Modify in R versus Reference Semantics in Python

Understanding memory allocation semantics is the dividing line between amateur scripts that grind to a halt on moderate datasets and high-performance statistical code.

### R’s Copy-on-Modify Semantics (Pass-by-Value Illusion)

In base R, objects behave as if they are strictly immutable and passed by value. When an object is assigned to a second variable or passed into a function, R guarantees that modifications made to the copy will never alter the original object:

```r
x <- c(1, 2, 3, 4, 5)
y <- x
y[1] <- 99
```
After executing this code, `y[1]` is 99, but `x[1]` remains 1.

#### The Internal Implementation: Reference Counting and Deferred Copying
To make this pass-by-value behavior practical, R does not eagerly duplicate the memory buffer when `y <- x` is executed. Instead, it utilizes **deferred copying (copy-on-modify)** managed by an internal reference counting system (`NAMED` in older R versions; `REFCNT` in modern R 4.0+).

```text
Step 1: x <- c(1, 2, 3)
[SEXP: REALSXP, REFCNT = 1] ----> [ Memory: 1.0, 2.0, 3.0 ]
       ^
       x

Step 2: y <- x
[SEXP: REALSXP, REFCNT = 2] ----> [ Memory: 1.0, 2.0, 3.0 ]
       ^                  ^
       x                  y

Step 3: y[1] <- 99 (REFCNT > 1: Mutation triggers full duplication!)
[SEXP: REALSXP, REFCNT = 1] ----> [ Memory: 1.0, 2.0, 3.0 ]  <-- x
[SEXP: REALSXP, REFCNT = 1] ----> [ Memory: 99.0, 2.0, 3.0 ] <-- y
```

When `y[1] <- 99` is evaluated, R checks the reference count of the underlying SEXP. Because `REFCNT > 1`, R detects that the memory buffer is shared. It immediately allocates a brand-new memory buffer of the same length, copies all elements from the original buffer, modifies the target element in the new copy, decrements the reference count of the old buffer, and rebinds `y` to the new SEXP.

#### The Quadratic Loop Memory Disaster:
The hidden danger of copy-on-modify occurs when an analyst iteratively grows an object inside a procedural loop:
```r
result <- numeric(0)
for (i in 1:N) {
  result <- c(result, compute_stat(i))
}
```
At iteration $i$, `result` has length $i - 1$. The concatenation `c(result, ...)` forces R to allocate a new buffer of length $i$ and copy all $i - 1$ existing elements into it.
The total number of memory write operations across $N$ iterations is:
$$\text{Total Copies} = \sum_{i=1}^N (i - 1) = \frac{N(N - 1)}{2} = O(N^2)$$
For $N = 100,000$, the processor performs over **5 billion memory copies**, turning a sub-second task into a multi-hour freeze!
Pre-allocating the vector (`result <- numeric(N)`) reduces memory allocation to a single $O(N)$ operation.

#### Exceptions: In-Place Modification in R
Base R permits true in-place modification without copying under two specific mechanisms:
1. **Environments (`ENVSXP`)**: Environments are always passed by reference. Modifying an environment inside a function mutates the original environment.
2. **`data.table` and C Extensions**: The high-performance `data.table` package bypasses R's copy-on-modify mechanism using direct memory manipulation in compiled C via the `:=` operator, achieving microsecond update speeds on multi-gigabyte tables.

### Python’s Reference Semantics and Pointer Mutation

Python operates entirely via **pass-by-assignment (reference semantics)**. Variables are not storage boxes; they are named labels bound to objects residing on the memory heap.

```python
a = [1, 2, 3]
b = a
b.append(4)
```
After appending 4 to `b`, `a` is also modified to `[1, 2, 3, 4]`! Both `a` and `b` point to the identical `PyListObject` in memory.

In NumPy:
```python
A = np.zeros((1000, 1000))
B = A
B[0, 0] = 42.0
```
`A[0, 0]` is immediately mutated to 42.0 because `B` and `A` share the identical data pointer. To force an independent memory allocation, the programmer must explicitly request `B = A.copy()`.

---

## 1.5 Vectorized Broadcasting and SIMD Execution Mechanics

The cardinal rule of high-performance statistical computing in Python and R is: **eliminate procedural loops over array elements in interpreted code**. Loops must be delegated to vectorized operations executed in pre-compiled C, C++, or Fortran libraries.

### What Vectorization Actually Does at the Hardware Level

When an interpreted loop is replaced with a vectorized statement:
- **Python**: `y = 2.5 * x + 1.0` (where `x` is a NumPy array)
- **R**: `y <- 2.5 * x + 1.0` (where `x` is an atomic vector)

the execution environment bypasses the interpreter's dynamic type checking and bytecode dispatch loop. Instead, it enters a tight C loop:

```c
void vector_saxpy(int n, double alpha, const double* x, double beta, double* y) {
    for (int i = 0; i < n; i++) {
        y[i] = alpha * x[i] + beta;
    }
}
```

Modern compilers vectorize this loop using **Single Instruction, Multiple Data (SIMD)** instructions (such as Intel AVX-2 or AVX-512, or ARM NEON):
- A standard CPU scalar register holds one 64-bit double (8 bytes).
- An AVX-2 register (`ymm0`) is 256 bits wide, holding **four 64-bit doubles** simultaneously.
- An AVX-512 register (`zmm0`) is 512 bits wide, holding **eight 64-bit doubles** simultaneously.

In a single clock cycle, a fused multiply-add (FMA) SIMD instruction executes:
$$\mathbf{y}_{[i:i+7]} = \alpha \cdot \mathbf{x}_{[i:i+7]} + \beta$$
processing eight statistical observations per CPU cycle!

### The NumPy Broadcasting Algebra

Broadcasting describes how NumPy treats arrays with differing shapes during arithmetic operations. The term broadcasting originated in NumPy, but the underlying dimensional alignment rules are universally applicable across scientific computing.

#### The Formal Broadcasting Rule:
Two dimensions are **compatible** for element-wise operations if:
1. They are equal in size ($D_{1, k} = D_{2, k}$), OR
2. One of the dimensions is equal to $1$ ($D_{1, k} = 1$ or $D_{2, k} = 1$).

If the arrays have differing numbers of dimensions, the array with fewer dimensions is prepended with dimensions of size 1 on its leading (left) side until both shapes have the same length.

#### The Magic of Zero Strides:
Consider adding a column mean vector of shape $(1, N)$ to a data matrix of shape $(M, N)$:
```python
X_centered = X - col_means  # X is (M, N), col_means is (1, N)
```
How does NumPy broadcast `col_means` across all $M$ rows without allocating an $M \times N$ matrix in memory?
The answer lies in **stride manipulation**!
NumPy creates a broadcasted view of `col_means` with:
$$\text{shape}' = (M, N), \quad \text{strides}' = (0, s_1)$$
Notice the row stride: **$s_0' = 0$ bytes**!
Whenever the row index increments ($i \to i + 1$), the memory offset increases by:
$$\Delta \text{Offset} = (i + 1 - i) \times s_0' = 1 \times 0 = 0$$
The CPU hardware reads from the exact same memory address for every row! Broadcasting achieves zero memory allocation and 100% cache efficiency through the mathematical elegance of zero strides.

---

## Fully worked question 1: Memory Layout, Stride Calculation, and Cache-Friendly Matrix Traversal

**Question.** Consider a three-dimensional double-precision floating-point tensor $\mathbf{T}$ of shape $(D_0, D_1, D_2) = (100, 200, 300)$. Each element is a standard 64-bit IEEE 754 float ($\text{itemsize} = 8 \text{ bytes}$). The total number of elements in the tensor is:
$$N = 100 \times 200 \times 300 = 6,000,000 \text{ elements}$$
and its total memory footprint is $6,000,000 \times 8 = 48,000,000 \text{ bytes} \approx 48 \text{ megabytes}$.

1. Compute the exact theoretical stride tuples $(s_0, s_1, s_2)$ in bytes under:
   - Standard C-contiguous (row-major) order.
   - Standard Fortran-contiguous (column-major) order.
2. For an element located at multi-index $(i_0, i_1, i_2) = (45, 120, 215)$, calculate the exact byte offset relative to the base data pointer `data` under both C-order and Fortran-order.
3. Suppose a statistical algorithm computes slice totals along the last axis:
   $$S(i_0, i_1) = \sum_{k=0}^{299} \mathbf{T}[i_0, i_1, k]$$
   Evaluate the hardware CPU cache implications of executing this summation across the entire tensor when $\mathbf{T}$ is stored in C-order versus when $\mathbf{T}$ is stored in Fortran-order, assuming a modern CPU with 64-byte L1 cache lines.

**Solution, step 1: Deriving the stride tuples.**
We use the general stride formulas for multi-dimensional arrays.
Given: $\text{itemsize} = 8$, $D_0 = 100$, $D_1 = 200$, $D_2 = 300$.

*Case A: C-contiguous (Row-Major) order.*
In C-order, the last axis ($k = 2$) is contiguous in memory:
$$s_2 = \text{itemsize} = 8 \text{ bytes}$$
For the middle axis ($k = 1$):
$$s_1 = D_2 \times s_2 = 300 \times 8 = 2,400 \text{ bytes}$$
For the leading axis ($k = 0$):
$$s_0 = D_1 \times s_1 = 200 \times 2,400 = 480,000 \text{ bytes}$$
Thus, the C-order stride tuple is:
$$\mathbf{s}_C = (480000, 2400, 8) \text{ bytes}$$

*Case B: Fortran-contiguous (Column-Major) order.*
In Fortran-order, the first axis ($k = 0$) is contiguous in memory:
$$s_0 = \text{itemsize} = 8 \text{ bytes}$$
For the middle axis ($k = 1$):
$$s_1 = D_0 \times s_0 = 100 \times 8 = 800 \text{ bytes}$$
For the last axis ($k = 2$):
$$s_2 = D_1 \times s_1 = 200 \times 800 = 160,000 \text{ bytes}$$
Thus, the Fortran-order stride tuple is:
$$\mathbf{s}_F = (8, 800, 160000) \text{ bytes}$$

**Solution, step 2: Computing the memory byte offset for multi-index $(45, 120, 215)$.**
The linear byte offset formula is:
$$\text{Offset} = i_0 s_0 + i_1 s_1 + i_2 s_2$$

*Under C-contiguous order:*
$$\text{Offset}_C = 45(480,000) + 120(2,400) + 215(8)$$
Compute each term:
- $45 \times 480,000 = 21,600,000$ bytes
- $120 \times 2,400 = 288,000$ bytes
- $215 \times 8 = 1,720$ bytes

Summing the terms:
$$\text{Offset}_C = 21,600,000 + 288,000 + 1,720 = 21,889,720 \text{ bytes}$$

*Under Fortran-contiguous order:*
$$\text{Offset}_F = 45(8) + 120(800) + 215(160,000)$$
Compute each term:
- $45 \times 8 = 360$ bytes
- $120 \times 800 = 96,000$ bytes
- $215 \times 160,000 = 34,400,000$ bytes

Summing the terms:
$$\text{Offset}_F = 360 + 96,000 + 34,400,000 = 34,496,360 \text{ bytes}$$

**Solution, step 3: Hardware cache line analysis.**
A modern CPU fetches memory from main RAM into L1/L2 cache in discrete blocks of 64 bytes (cache lines).
Since each double is 8 bytes, one 64-byte cache line holds exactly:
$$\frac{64 \text{ bytes}}{8 \text{ bytes/element}} = 8 \text{ consecutive elements}$$

Now consider summing along the last axis ($k = 0, 1, \dots, 299$ for fixed $i_0, i_1$):

*In C-contiguous storage ($s_2 = 8$ bytes):*
As $k$ increments by 1, the memory address advances by exactly 8 bytes.
- The 300 elements along the reduction axis reside in contiguous physical memory.
- When $k = 0$ is accessed, the CPU loads a 64-byte cache line containing elements $k = 0, 1, 2, 3, 4, 5, 6, 7$.
- Accessing $k = 0$ triggers a single cache miss; the subsequent 7 accesses ($k = 1, \dots, 7$) are **instantaneous L1 cache hits**.
- The total number of cache line fetches required to sum 300 elements is:
  $$\text{Cache Misses}_C = \lceil 300 / 8 \rceil = 38 \text{ cache lines}$$
- Spatial cache locality is near-perfect ($87.5\%$ hit rate).

*In Fortran-contiguous storage ($s_2 = 160,000$ bytes):*
As $k$ increments by 1, the memory address advances by 160,000 bytes ($160 \text{ KB}$).
- 160 KB vastly exceeds the size of a single 64-byte cache line. In fact, it exceeds the total capacity of typical L1 data caches ($32 \text{ KB}$ to $48 \text{ KB}$).
- Every single increment of $k$ lands in a completely different, non-contiguous page of RAM.
- When the CPU loads a 64-byte cache line for element $k$, it loads 7 adjacent elements along the first axis ($i_0 + 1, \dots$), none of which are used by the current summation!
- For every single one of the 300 elements, the CPU suffers an L1/L2 cache miss:
  $$\text{Cache Misses}_F = 300 \text{ cache misses}$$
- The Fortran layout incurs **nearly 8 times more memory bus transactions** and causes massive cache line evictions.

In empirical benchmarks, summing along the last axis of a large tensor is approximately **5 to 10 times faster** in C-contiguous order than in Fortran-contiguous order.

---

## Fully worked question 2: Copy-on-Modify Overhead Analysis and In-Place Reference Mutation

**Question.** A statistical geneticist is writing a simulation to generate a synthetic population of $N = 50,000$ individuals, where each individual is represented by a record containing genetic markers and phenotype scores. The researcher considers two implementations in R:

*Algorithm 1 (Naive Growing Vector):*
```r
sim_naive <- function(N) {
  population <- numeric(0)
  for (i in 1:N) {
    score <- rnorm(1)
    population <- c(population, score)
  }
  return(population)
}
```

*Algorithm 2 (Pre-Allocated Vector):*
```r
sim_prealloc <- function(N) {
  population <- numeric(N)
  for (i in 1:N) {
    population[i] <- rnorm(1)
  }
  return(population)
}
```

1. Derive from first principles the exact total number of floating-point numbers allocated and copied in memory across the entire execution of Algorithm 1 as a function of $N$, and calculate its exact numerical value for $N = 50,000$.
2. Compute the exact total bytes of memory copied by Algorithm 1, assuming 8 bytes per double, and compare this against the total memory allocated by Algorithm 2.
3. Explain the internal R reference counting (`REFCNT`) behavior during Algorithm 2: why does `population[i] <- score` modify the vector in place without triggering a full copy of the $N$-element buffer at each step?

**Solution, step 1: Deriving the cumulative elements copied in Algorithm 1.**
At iteration $i = 1$:
- `population` starts with length 0.
- `c(population, score)` allocates a new vector of length 1 and copies 0 elements.

At iteration $i = 2$:
- `population` has length 1.
- `c(population, score)` allocates a new vector of length 2 and copies the 1 existing element into it.

At general iteration $i$ ($i = 2, 3, \dots, N$):
- `population` currently has length $i - 1$.
- Concatenation `c(population, score)` allocates a new SEXP vector of length $i$.
- The R memory manager copies all $i - 1$ existing elements from the old buffer into the new buffer, and appends the single new element.
- The old buffer of length $i - 1$ is orphaned and flagged for garbage collection.

The total number of existing elements copied across all iterations from $i = 1$ to $N$ is:
$$\text{Total Elements Copied} = \sum_{i=1}^N (i - 1) = 0 + 1 + 2 + \dots + (N - 1)$$

Applying the arithmetic series summation formula:
$$\text{Total Elements Copied} = \frac{(N - 1)N}{2} = \frac{N^2 - N}{2}$$

For $N = 50,000$:
$$\text{Total Elements Copied} = \frac{50,000 \times 49,999}{2} = 25,000 \times 49,999 = 1,249,975,000 \text{ elements}$$

Algorithm 1 copies **nearly 1.25 billion elements**!

**Solution, step 2: Computing memory throughput and comparison with Algorithm 2.**
Each double-precision element occupies 8 bytes.
The total volume of memory written due to re-allocating and copying in Algorithm 1 is:
$$\text{Bytes Copied} = 1,249,975,000 \text{ elements} \times 8 \text{ bytes/element} = 9,999,800,000 \text{ bytes}$$
Converting to gigabytes (using $10^9$ bytes = 1 GB):
$$\text{Bytes Copied} \approx 10.0 \text{ gigabytes!}$$

In addition, Algorithm 1 allocates $N = 50,000$ distinct SEXP header nodes (32 bytes each) plus memory chunk descriptors, putting colossal pressure on the R generational garbage collector (`R_gc()`), which must pause execution repeatedly to reclaim the 49,999 abandoned vector buffers.

*Now evaluate Algorithm 2 (Pre-allocation):*
Algorithm 2 executes `numeric(N)` once at the beginning:
$$\text{Memory Allocated} = 32 \text{ bytes (SEXP header)} + 8 \times 50,000 \text{ bytes (payload)}$$
$$\text{Memory Allocated} = 32 + 400,000 = 400,032 \text{ bytes} \approx 400 \text{ kilobytes}$$

Comparison of memory throughput:
$$\frac{\text{Memory Copied in Algorithm 1}}{\text{Memory Allocated in Algorithm 2}} = \frac{9,999,800,000 \text{ bytes}}{400,032 \text{ bytes}} \approx 24,997.4$$

Algorithm 1 pushes **25,000 times more data through memory** than Algorithm 2! In runtime execution, Algorithm 1 requires several minutes and triggers high CPU fan noise, whereas Algorithm 2 completes in approximately 3 milliseconds.

**Solution, step 3: Internal reference counting and in-place assignment.**
In Algorithm 2:
```r
population <- numeric(N)
```
R allocates a single `REALSXP` vector of length 50,000. Because this newly created vector is bound solely to the symbol `population`, its internal reference counter is:
$$\text{REFCNT}(\text{population}) = 1$$

When the loop executes:
```r
population[i] <- rnorm(1)
```
R evaluates the sub-assignment function `[<-`.
Under GNU R’s memory semantics, `[<-` inspects the reference count of the target object:
- If $\text{REFCNT} > 1$, the vector is shared by multiple symbols (or bound in a closure), and modifying it directly would violate R's pass-by-value contract. A full copy would be mandatory.
- But if $\text{REFCNT} \le 1$, the object is **uniquely owned** by the current execution context. No other variable points to this memory buffer!

Because `REFCNT == 1`, R detects that an in-place mutation cannot be observed by any other part of the program. It executes a direct C pointer write:
$$\text{REAL}(\text{population})[i - 1] = \text{score}$$
This operation takes exactly $O(1)$ time, allocates 0 bytes of heap memory, and produces zero garbage collection overhead. This explains why pre-allocated vector updates in R achieve optimal performance.

---

## Fully worked question 3: Vectorized Broadcasting Algebra and Execution Benchmarking

**Question.** A statistical machine learning engineer is training a Gaussian Radial Basis Function (RBF) kernel matrix $\mathbf{K} \in \mathbb{R}^{M \times N}$ on two observation matrices:
- Training feature matrix $\mathbf{X} \in \mathbb{R}^{M \times P}$ containing $M = 2,000$ samples and $P = 50$ features.
- Test feature matrix $\mathbf{Z} \in \mathbb{R}^{N \times P}$ containing $N = 1,000$ samples and $P = 50$ features.

The RBF kernel function between sample $\mathbf{x}_i \in \mathbb{R}^P$ and sample $\mathbf{z}_j \in \mathbb{R}^P$ is defined as:
$$K_{ij} = \exp\left( -\gamma \|\mathbf{x}_i - \mathbf{z}_j\|^2 \right) = \exp\left( -\gamma \sum_{k=1}^P (x_{ik} - z_{jk})^2 \right)$$
where $\gamma = \frac{1}{2\sigma^2} > 0$ is a scalar bandwidth parameter.

1. If the engineer computes $\mathbf{K}$ using a nested procedural Python loop:
   ```python
   K = np.zeros((M, N))
   for i in range(M):
       for j in range(N):
           diff = X[i, :] - Z[j, :]
           K[i, j] = np.exp(-gamma * np.sum(diff ** 2))
   ```
   Calculate the exact total number of Python interpreter loop iterations, intermediate array allocations, and floating-point operations (flops) executed.
2. Formulate the fully vectorized calculation of $\mathbf{K}$ using NumPy broadcasting by expanding dimensions (`np.newaxis`), and specify the shapes and strides of the broadcasted intermediate arrays.
3. Derive the mathematically equivalent **Gram Matrix expansion identity**:
   $$\|\mathbf{x}_i - \mathbf{z}_j\|^2 = \|\mathbf{x}_i\|^2 + \|\mathbf{z}_j\|^2 - 2 \mathbf{x}_i^\top \mathbf{z}_j$$
   Express this identity in terms of optimized matrix multiplication ($\mathbf{X} \mathbf{Z}^\top$) and broadcasting. Compare the computational complexity and memory footprint of the Gram matrix expansion against the 3D broadcasting approach.

**Solution, step 1: Procedural loop execution audit.**
Given dimensions: $M = 2,000$, $N = 1,000$, $P = 50$.

*Loop iterations and calls:*
The outer loop runs $M = 2,000$ times.
The inner loop runs $N = 1,000$ times per outer iteration.
$$\text{Total Loop Iterations} = M \times N = 2,000 \times 1,000 = 2,000,000 \text{ iterations}$$

At *each* of the 2,000,000 iterations:
- Slicing `X[i, :]` creates an `ndarray` view header of shape $(50,)$.
- Slicing `Z[j, :]` creates an `ndarray` view header of shape $(50,)$.
- Computing `X[i, :] - Z[j, :]` allocates a brand-new heap memory buffer of $50 \times 8 = 400$ bytes for `diff`.
- Computing `diff ** 2` allocates another 400-byte buffer for the squared differences.
- `np.sum(...)` reduces the 50 elements into a scalar float.
- `np.exp(...)` evaluates the exponential.

Total temporary array allocations:
$$\text{Allocations} = 2,000,000 \times 2 = 4,000,000 \text{ heap allocations}$$
Total temporary memory created and immediately discarded:
$$4,000,000 \times 400 \text{ bytes} = 1,600,000,000 \text{ bytes} = 1.6 \text{ gigabytes}$$
The Python garbage collector must track and deallocate 4 million heap objects!

*Flop count:*
Per pair $(i, j)$:
- 50 subtractions
- 50 squarings (multiplications)
- 49 additions (summation)
- 1 scalar multiplication ($-\gamma$)
- 1 exponential evaluation (transcendental, $\approx 20$ flops equivalent)
$$\text{Flops per pair} = 50 + 50 + 49 + 1 + 20 = 170 \text{ flops}$$
$$\text{Total Flops} = 2,000,000 \times 170 = 340,000,000 \text{ flops} = 340 \text{ Mflops}$$
Although 340 Mflops requires only a few milliseconds on a modern CPU capable of 100 Gflops/sec, the 2 million interpreter loop dispatches and 4 million memory allocations cause this naive code to take **over 30 seconds** to complete.

**Solution, step 2: 3D Broadcasting formulation.**
To compute all pairwise differences simultaneously in compiled C code, we expand the dimensions of $\mathbf{X}$ and $\mathbf{Z}$:
- Expand $\mathbf{X}$ to shape $(M, 1, P)$ by inserting a singleton dimension along axis 1:
  `X[:, np.newaxis, :]`
- Expand $\mathbf{Z}$ to shape $(1, N, P)$ by inserting a singleton dimension along axis 0:
  `Z[np.newaxis, :, :]`

The subtraction is executed via broadcasting:
```python
diff = X[:, np.newaxis, :] - Z[np.newaxis, :, :]
K = np.exp(-gamma * np.sum(diff ** 2, axis=-1))
```

*Broadcasting alignment:*
$$\text{Shape}(\mathbf{X}_{3D}) = (2000, 1, 50)$$
$$\text{Shape}(\mathbf{Z}_{3D}) = (1, 1000, 50)$$
Broadcasting rules align the shapes:
- Axis 0: $\max(2000, 1) = 2000$
- Axis 1: $\max(1, 1000) = 1000$
- Axis 2: $\max(50, 50) = 50$
The broadcasted difference array `diff` has shape $(2000, 1000, 50)$.

*Memory footprint of the 3D difference array:*
The resulting array `diff` contains:
$$2000 \times 1000 \times 50 = 100,000,000 \text{ float64 elements}$$
Total memory required:
$$100,000,000 \times 8 \text{ bytes} = 800,000,000 \text{ bytes} = 800 \text{ megabytes}$$
While this vectorization completely eliminates the Python interpreter loop and runs in roughly 200 milliseconds, it incurs a massive **800 MB memory spike**. If $M = 20,000$, the 3D tensor would require 80 GB of RAM, causing an out-of-memory crash!

**Solution, step 3: Gram Matrix algebraic expansion and BLAS optimization.**
We expand the squared Euclidean norm algebraically:
$$\|\mathbf{x}_i - \mathbf{z}_j\|^2 = \sum_{k=1}^P (x_{ik} - z_{jk})^2 = \sum_{k=1}^P (x_{ik}^2 - 2 x_{ik} z_{jk} + z_{jk}^2)$$
$$= \sum_{k=1}^P x_{ik}^2 + \sum_{k=1}^P z_{jk}^2 - 2 \sum_{k=1}^P x_{ik} z_{jk} = \|\mathbf{x}_i\|^2 + \|\mathbf{z}_j\|^2 - 2 (\mathbf{x}_i^\top \mathbf{z}_j)$$

Notice that the cross-product term for all pairs $(i, j)$ is the $(i, j)$-th entry of the matrix product:
$$\mathbf{G} = \mathbf{X} \mathbf{Z}^\top \in \mathbb{R}^{M \times N}$$

Define the squared row-norm vectors:
$$\mathbf{r}_X = \sum_{k=1}^P x_{ik}^2 \in \mathbb{R}^{M \times 1}$$
$$\mathbf{r}_Z = \sum_{k=1}^P z_{jk}^2 \in \mathbb{R}^{1 \times N}$$

The pairwise squared Euclidean distance matrix $\mathbf{D} \in \mathbb{R}^{M \times N}$ is computed via 2D broadcasting:
$$\mathbf{D} = \mathbf{r}_X + \mathbf{r}_Z - 2 (\mathbf{X} \mathbf{Z}^\top)$$
And the kernel matrix is:
$$\mathbf{K} = \exp(-\gamma \mathbf{D})$$

*Python implementation:*
```python
r_X = np.sum(X ** 2, axis=1, keepdims=True)  # Shape (M, 1)
r_Z = np.sum(Z ** 2, axis=1, keepdims=True).T # Shape (1, N)
D = r_X + r_Z - 2.0 * np.dot(X, Z.T)          # Shape (M, N)
K = np.exp(-gamma * D)
```

*Computational complexity and memory comparison:*
1. **Memory Footprint**:
   The largest intermediate matrix created is $\mathbf{D} \in \mathbb{R}^{M \times N}$, which occupies:
   $$2,000 \times 1,000 \times 8 \text{ bytes} = 16,000,000 \text{ bytes} = 16 \text{ megabytes}$$
   Compare 16 MB against the 800 MB required by the 3D broadcasting approach—a **50-fold reduction in peak memory**!
2. **Computational Speed**:
   Computing $\mathbf{X} \mathbf{Z}^\top$ invokes the vendor-optimized BLAS (Basic Linear Algebra Subprograms) Level 3 routine `dgemm` (OpenBLAS, Intel MKL, or Apple Accelerate).
   Level 3 BLAS algorithms partition matrices into cache-sized sub-blocks, achieving peak multi-threaded AVX performance (approaching 90% of theoretical hardware FLOPS limit).
   The Gram matrix expansion executes in less than **15 milliseconds**—over **2,000 times faster** than the procedural Python loop, while consuming a tiny fraction of the memory.

---

## 1.6 Practical Synthesis, Performance Profiling, and Computational Verification

To translate memory architecture and vectorization theory into reliable statistical computing practice, analysts deploy rigorous profiling and diagnostic tools to identify memory leaks, unnecessary copies, and CPU bottlenecks before production deployment.

### Memory Footprint Profiling Tools
- **In Python**: The `sys.getsizeof()` function returns the shallow size of a single Python object, but ignores child pointers. To inspect full recursive memory structures, statisticians deploy `tracemalloc` (built into the Python standard library) or the `memory_profiler` extension:
  ```python
  import tracemalloc
  tracemalloc.start()
  # Execute statistical routine
  current, peak = tracemalloc.get_traced_memory()
  tracemalloc.stop()
  print(f"Peak memory: {peak / 1024**2:.2f} MB")
  ```
- **In R**: The `lobstr` and `pryr` packages inspect internal SEXP representations and true memory allocations:
  ```r
  library(lobstr)
  x <- 1:1e6
  obj_size(x)       # Reports exact payload + SEXP header
  obj_addr(x)       # Displays physical hexadecimal RAM address of SEXP
  ref(x)            # Prints recursive tree of pointer addresses
  ```

### Line-by-Line Execution Profiling
- **In Python**: The `cProfile` and `line_profiler` modules record the exact number of hits and cumulative time spent on each individual line of code:
  ```bash
  kernprof -l -v my_statistical_script.py
  ```
- **In R**: The `profvis` package combines R's internal sampling profiler (`Rprof()`) with an interactive D3.js flame graph visualizer:
  ```r
  library(profvis)
  profvis({
    fit <- my_estimation_algorithm(dataset)
  })
  ```
  The flame graph visually demarcates whether execution time is dominated by numerical computations in compiled C/Fortran or spent stalled in memory allocations and garbage collection passes (`<GC>`).

### Diagnostic Rules for High-Performance Statistical Engineering
1. **Never Grow an Object in a Loop**: Always pre-allocate the final vector, matrix, or data frame before initiating procedural loops.
2. **Preserve Memory Contiguity**: When designing iterative algorithms that traverse 2D arrays, align traversal direction with memory order: iterate along rows for C-contiguous arrays (Python) and along columns for Fortran-contiguous arrays (R).
3. **Exploit Level 3 BLAS Matrix Operations**: Wherever possible, reformulate pairwise operations, sums of squares, and linear filters into matrix multiplications (`np.dot` in Python, `%*%` in R) to leverage hardware-optimized BLAS libraries.
4. **Be Mindful of Dynamic Boxing**: In performance-critical numerical routines that cannot be vectorized, compile the loop to machine code using Just-In-Time (JIT) compilers (such as `numba` in Python or `cppFunction()` via `Rcpp` in R).

With these fundamental memory architectures and computational mechanics firmly established, we advance in Unit 2 to **Data Wrangling, Tabular Transformation, Relational Joins, and Missing-Data Processing**.
"""

out_dir = Path("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r")
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "unit-1.md").write_text(content, encoding="utf-8")
print("Successfully authored Unit 1!")
