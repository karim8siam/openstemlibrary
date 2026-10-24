# Unit 2: Variables and expressions

## Primitive Types

## Primitive Types: the computational contract

**Core idea.** Integer, float, string, and boolean values support different operations. Do not conflate the printable representation with the value type. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
measurements = [3, 5, 7]
label = 'sample'
valid = len(measurements) > 0
print(type(label).__name__, valid)
```

**Expected result:** `str True`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For primitive types, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Before implementation, identify which facts are input data and which are policy. A function that hardcodes mutable policy is fragile even when its first output is correct. Try a case where the given value is missing or physically impossible; decide whether to reject, default or request clarification. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 1

# Extended laboratory: values, representations, operators, and numerical reliability

A variable is a name that refers to a value during an execution. That compact description hides several different questions. What kind of value is involved? Which operations are meaningful for it? Can the object be changed in place, or will a new object be created? Can the value be stored or transmitted without changing its meaning? In scientific programming, a wrong answer often begins with the wrong representation rather than the wrong equation. Understanding variables and expressions means learning to separate a mathematical concept from the bytes and operations used to represent it.

## Types describe supported operations, not just appearances

Python distinguishes integers, floating-point numbers, strings, booleans, and compound objects. The integer `12` and the string `"12"` may look nearly identical when printed, but their operations are different. Adding three to the integer produces fifteen; concatenating `"3"` to the string produces `"123"`. If the task is to calculate a count, a string is an unsuitable internal representation even when a text field supplies the input. Parse the string at the boundary, validate the resulting integer, and then perform arithmetic on the typed value. Keeping parsing separate from calculation makes errors easier to diagnose.

Booleans deserve special attention because Python treats them as a subtype of integers. An expression such as `True + True` evaluates to two. That is legal Python behavior, but it is not evidence that booleans should be accepted wherever a numeric measurement is required. A function validating a temperature might accidentally accept `True` as a temperature of one degree. Its contract should reject boolean inputs if the application distinguishes physical quantities from truth values. The language's type hierarchy provides a set of possible operations; the application's domain policy may permit a narrower set.

Compound objects introduce relationships between names and values. If `a` refers to a list and `b = a`, both names refer to the same list object. Appending to `b` changes the object observed through `a`. If instead `b = a.copy()`, the new list has a separate outer container, although nested mutable objects may still be shared. This explains why a function can modify a caller's state even when it never returns an output. A sound interface documents whether arguments are read-only, copied, or mutated. Scientific notebooks often become difficult to reproduce when an earlier cell mutates a shared data object without making that dependency visible.


## Assignment is not mathematical equality

In mathematics, writing `x = x + 1` is contradictory when `x` represents a fixed number. In an imperative program, the same notation means to evaluate the expression on the right using the current binding and then assign the result to the name on the left. The original value and the new value are part of different program states. A trace table makes this clear: start with x equal to four; evaluate four plus one; rebind x to five. In a subsequent loop iteration, the next evaluation uses five. This distinction is the basis of counters, running totals, and iterative numerical algorithms.

Equality testing uses a different operation. Python uses `==` to ask whether values compare equal, not to assign a value. Two separate lists can compare equal because they contain equal elements, even though they are distinct objects. The identity operator `is` asks whether two references point to the same object. Identity is appropriate for sentinels such as `None`, but generally not as a substitute for numeric or string equality. Distinguishing assignment, equality, and identity prevents a large class of subtle errors in data processing.



## Operators

## Operators: the computational contract

**Core idea.** Quotient, remainder and true division represent different mathematical operations; their types and interpretations matter. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
x = 13
print(x // 5, x % 5, x / 5)
```

**Expected result:** `2 3 2.6`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For operators, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Make a trace table with at least four rows: the initial state, two transitions and the final state. If a proposed shortcut skips a state, show why the output remains equivalent. The trace is a method of reasoning, not a substitute for full testing. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 2

## Operators encode assumptions

Addition, division, exponentiation, and comparison are concise notations for operations that have domain and type constraints. Integer floor division and remainder make a useful case study. For positive integers twenty-nine and six, the quotient is four and the remainder is five because `29 = 6*4 + 5`. Python's `//` operator performs floor division, so negative operands require care. For example, `-7 // 3` is negative three, not negative two, because negative three is the greatest integer less than or equal to negative seven thirds. Its companion remainder is two, preserving `-7 = (-3)*3 + 2`. Someone assuming truncation toward zero may produce incorrect indexing or bucket calculations for negative inputs.

Operator precedence also matters. The expression `a + b * c` multiplies before adding. Parentheses make the intended grouping explicit, particularly in translated formulas with several denominators. A unit test at one convenient numerical point may not expose a precedence error if a multiplier happens to be zero or one. Prefer expressions whose structure mirrors the underlying equation, with named intermediate quantities when that improves clarity. Compact code is not automatically auditable code.

Comparison is not always a straightforward mathematical ordering. Floating-point values can contain a special not-a-number value, often written NaN. Comparisons involving NaN are not ordinary total-order comparisons: NaN is not equal to itself, and neither less-than nor greater-than relations behave as they do for finite real numbers. Sorting or filtering numerical arrays that may contain NaN requires an explicit policy for missing or invalid measurements. A program should not silently assume that every numeric-looking value participates in a conventional ordering.


## Conversion should never erase evidence without permission

Suppose a laboratory instrument exports a column of readings as strings. Some cells contain `"12.4"`, some contain whitespace, and one contains `"sensor offline"`. A naive loop that replaces every conversion error with zero changes the scientific meaning of the dataset. Zero is a possible measurement; offline is a missing observation. Treating them as identical can bias a mean and conceal an instrument failure. Better choices include recording the raw value and an error code, rejecting the file with a precise location, or representing invalid readings separately from valid numeric values.

Integer conversion from a float can lose fractional information. Python's `int(-2.9)` gives negative two by truncating toward zero. That is not the same as the floor, which is negative three. Neither should be used as an unstated rounding policy for bills, distances, or time intervals. Choose the appropriate operation and document it. Rounding to a number of decimal places is also distinct from representing a value exactly to that precision. After rounding a floating-point number to two decimal places, the internal binary representation may still be approximate.

When two systems exchange data, type conversion becomes part of a protocol. A timestamp might be represented as an ISO-formatted string, a Unix count of seconds, or a date-time object. Those representations require a timezone convention and a decision about daylight-saving transitions. A JSON document can carry numbers and strings, but it does not automatically preserve every language's numeric range or special floating-point values. A receiving application should validate the schema rather than trusting the sender's type choices.



## Conversion

## Conversion: the computational contract

**Core idea.** Parsing is a boundary between an untrusted text representation and a validated numeric value. Invalid text must be handled explicitly. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
raw = '42'
value = int(raw)
print(value + 8)
```

**Expected result:** `50`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For conversion, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Test a normal input, an empty input where meaningful, a boundary input and a malformed input. Explain whether the program should return a result, raise an exception or ask for a new value. This separates mathematical domain assumptions from interface behavior. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 3

## Why floating-point arithmetic deserves a separate model

Many decimal fractions do not have finite binary expansions. A stored floating-point value is typically the nearest representable approximation to the requested real number. This is why adding `0.1` and `0.2` may produce a value that is not exactly equal to the stored representation of `0.3`. It is an expected consequence of a finite representation, not a random Python bug. The important engineering question is what comparison is appropriate for the domain. Approximate scientific computations may use a tolerance; exact integer counts should generally use integer equality.

An absolute tolerance tests whether the difference between two approximations is small in the original units. A relative tolerance tests whether the difference is small compared with the scale of the values. The two ideas answer different questions. Comparing measurements near zero using only a relative tolerance can be problematic because the reference scale is tiny. Comparing very large magnitudes using only an absolute tolerance may be too strict. A carefully chosen combination can be useful, but a copied constant such as `1e-12` has no automatic scientific justification. Tie the tolerance to input resolution, accumulated numerical error, and the risk of false acceptance.

Loss of significance is another issue. If two very large, nearly equal approximations are subtracted, the result may have far fewer reliable digits than the operands appeared to have. Consider a physical model that computes a small difference between two large energies. Even if each energy is represented to many digits, rounding error may dominate their difference. Algebraically equivalent formulations can behave differently numerically. Whenever possible, reformulate an expression to avoid unnecessary subtraction of nearly equal numbers and compare against an independent computation or higher-precision reference.

Overflow, underflow, and finite range require explicit treatment. A computation may overflow to infinity when an intermediate result exceeds the representable range; another may underflow toward zero when the magnitude becomes too small. The product of many probabilities is a common example: even moderately small probabilities multiplied repeatedly can underflow. Statistical software often uses sums of logarithms to preserve numerical information, with appropriate handling of zeros and invalid values. The correct representation depends on the operations to be performed, not only the expected final answer.


## A practical numeric audit: the weighted mean

Suppose readings are 8, 12, and 20 with weights 1, 2, and 1. The weighted mean is `(1*8 + 2*12 + 1*20)/(1+2+1) = 52/4 = 13`. A correct implementation should distinguish the measurement list from the weight list, require equal lengths, reject an empty list, and decide whether negative weights are permissible. For ordinary nonnegative frequency weights, the total weight must be positive. A program that computes a result when all weights are zero has violated the model regardless of whether Python raises an error.

Write a test with one nonzero weight: the result should equal the corresponding observation if the other weights are zero. Write another with equal weights: it should equal the ordinary arithmetic mean. Multiplying every weight by the same positive constant should not change the weighted mean. That property supplies a useful metamorphic test, meaning a known relationship between different inputs can validate the implementation without requiring a separately calculated expected answer for every case. It is especially valuable when numerical outputs are difficult to calculate by hand.

Now alter the input representation. If the measurements arrive as strings, the parser should report which entry fails conversion. If they arrive in a spreadsheet, missing cells must be distinguished from recorded zeros. If they arrive with physical units, combining temperatures and lengths in one mean is not meaningful merely because all are numbers. The algorithm's mathematical correctness depends on assumptions about comparable quantities. Input validation belongs to the scientific model, not only to user-interface cleanliness.



## Numerical Precision

## Numerical Precision: the computational contract

**Core idea.** Binary floating point approximates many decimal fractions. Decide tolerances from measurement accuracy, not by copying an arbitrary epsilon. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
x = 0.1 + 0.2
print(x == 0.3)
print(abs(x - 0.3) < 1e-12)
```

**Expected result:** `False
True`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For numerical precision, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Compare readability, asymptotic work and memory use with a plausible alternative. For small datasets, clarity may dominate micro-optimization. For huge datasets, count the operations rather than relying on a vague claim that one language construct is faster. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 4

## Decimal accounting and exact counts

Monetary calculations reveal why representation choices cannot be universal. A price of 0.10 units and a price of 0.20 units often need to add to exactly 0.30 units in financial records. One approach uses integer minor units, such as cents, and keeps accounting rules in integer arithmetic. Another uses decimal arithmetic with an explicit rounding context. Both still require a documented policy for tax, discounts, and rounding order. Changing from floating point to decimals does not by itself decide whether discounts apply before tax or whether rounding occurs per item or on the total.

Contrast that with a scientific experiment where sensor resolution is only one hundredth of a unit and model uncertainty is much larger. Representing every observation with dozens of decimal digits gives an illusion of precision rather than additional evidence. The calculation should retain enough internal precision to avoid unnecessary numerical loss, but the final report should reflect measurement uncertainty. Code correctness includes knowing what the reported digits mean.


## Build a conversion boundary with failure reporting

Consider a function that accepts a text measurement and returns either a validated finite float or a structured error. First remove permitted surrounding whitespace. Second attempt to parse a number. Third reject non-finite values if the application expects ordinary real measurements. Fourth check the allowed physical range and unit. Fifth return a value that downstream functions can use without repeating the parsing logic. Alongside the parsed number, retain the original input when an audit trail matters. An error message should distinguish malformed text from an out-of-range value, because the corrective action differs.

Test empty text, whitespace, a valid negative value where permitted, scientific notation, a clearly invalid string, and non-finite values. If a locale uses commas as decimal separators, decide whether to support that locale explicitly rather than applying an ambiguous global replacement. The string `"1,234"` may mean one thousand two hundred thirty-four or one point two three four depending on convention. Silent interpretation can produce errors of several orders of magnitude.


## Final model: a count is not a measurement

Imagine a report that includes number of participants, average participant height, a yes-or-no eligibility flag, and a timestamp. All four might be serialized as text in a CSV file. Inside a reliable program they should be interpreted differently. Participant count is a nonnegative integer; height is a numeric measurement paired with units and uncertainty; eligibility is a boolean derived from a policy; a timestamp is a date-time value under a timezone convention. Treating them as interchangeable strings makes validation harder and increases the risk of accidental concatenation or lexicographic ordering. Treating them all as floats discards information about discrete counts and semantic constraints.

The central lesson of variables and expressions is therefore not memorizing operator symbols. It is constructing a representation that preserves the meaning of the problem while supporting correct, inspectable operations. State the mathematical object, choose its program representation, specify what conversions are allowed, check the invariants, and recognize where finite numerical precision changes what can be guaranteed. Those practices make later control-flow and function designs trustworthy.


### Why does 0.1 + 0.2 == 0.3 return False in typical Python floats?

**Representation**
Most decimal tenths have infinite repeating binary expansions and are rounded to representable floating-point values.

**Comparison**
The rounded sum and stored representation of 0.3 differ by a small value, so exact equality fails.

**Repair**
Use a justified absolute or relative tolerance for approximations, or decimal arithmetic for exact financial rules.

### Compute quotient and remainder for 29 divided by 6, then reconstruct 29.

**Divide**
The floor quotient is 4 because 6·4=24 and 6·5=30 exceeds 29.

**Remainder**
The remainder is 29-24=5 and lies between 0 and 5.

**Check**
29 = 6·4 + 5. In Python, 29//6=4 and 29%6=5.

### Convert a user-supplied age string into a validated integer.

**Parse**
Strip permitted whitespace and call int; catch ValueError for non-integer text such as 2.5 or thirteen.

**Check**
Require a documented range, for example 0 through 120 if appropriate for the application.

**Respond**
Return the integer for valid input and present a clear error for invalid input. Do not silently replace bad data with zero.


### Applied investigation: Floating-point accuracy and representable ranges

Repeated addition of one tenth is not generally equivalent to doing an exact decimal sum. Standard binary floating-point stores an approximation to the infinite binary expansion of 0.1. Compare an accumulation loop with n/10 and inspect the absolute error, not only the rounded printed display. Some sums happen to round to the same machine value, while others do not. The program should distinguish an arithmetic result from a text representation and use a tolerance only when there is a meaningful scale and error budget.

For an eight-bit two’s-complement integer, the encoded signed range is −128 through 127. The 8-bit low part of 130 is 10000010, which represents −126 when interpreted as signed. Python’s standard integer does not overflow in this way, while fixed-width machine integer or explicit bit masking can. Comparing results across languages therefore requires stating the numeric type. Silent wrap, checked overflow and saturating arithmetic are different semantics, not interchangeable implementations.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.
