# Unit 7: Program reliability

## Debugging

## Debugging: the computational contract

**Core idea.** Write down the interval convention before patching an off-by-one bug. Here [lo, hi) is half-open. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def binary_search(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x: lo = mid + 1
        else: hi = mid
    return lo if lo < len(a) and a[lo] == x else -1
print(binary_search([2,4,8], 4))
```

**Expected result:** `1`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For debugging, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Before implementation, identify which facts are input data and which are policy. A function that hardcodes mutable policy is fragile even when its first output is correct. Try a case where the given value is missing or physically impossible; decide whether to reject, default or request clarification. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 1

# Extended laboratory: debugging and testing as independent evidence

Debugging begins when observed behavior conflicts with the behavior a program is supposed to provide. The fastest-looking response is to change a line that appears suspicious and run the program again. That approach sometimes works for a trivial typo, but it scales poorly because it does not establish why the failure happened. A systematic approach starts with a reproducible example, a statement of expected behavior, and evidence about the program state at the first point where expectation and observation diverge. The objective is to locate the violated assumption, not merely to make one test stop failing.

## Errors have different causes

Syntax errors prevent source code from being interpreted according to the language's grammar. Runtime errors arise when a statement executes but an operation fails, such as accessing an absent dictionary key or dividing by zero. Logical errors can be more dangerous because the program finishes normally and returns an incorrect result. A statistical program that calculates an unweighted mean when the model requires weights may print a plausible number without raising any exception. Effective debugging recognizes which category of failure is present and chooses evidence accordingly.

A stack trace shows where an exception propagated through calls. It does not always identify the conceptual origin. A division-by-zero error may occur in a reporting function because upstream validation allowed an empty group. Fixing the report by substituting zero conceals the missing-data policy rather than solving it. Trace the data backward through the function contracts and determine where the invalid state first became possible. The best fix often occurs at a boundary where an assumption should have been checked.


## Reproduce before repairing

A minimal reproducing example includes only the inputs and operations needed to trigger the defect. For a binary-search implementation that hangs, reduce the data to a sequence of two items and a target that causes the interval to stop shrinking. With such a small case, write the values of `lo`, `hi`, and `mid` at each iteration. If the same state repeats without progress, the termination measure has failed. Repairing the update rule becomes a consequence of the diagnosis rather than a guess.

Reducing a problem is different from changing it. If a bug occurs only with non-ASCII filenames, removing the filename from the reproduction destroys the relevant condition. If it occurs only under concurrent requests, running requests sequentially may hide the race. Keep the smallest environment that still exhibits the failure, and record the version of the runtime, input data, and relevant settings. Reproducibility makes a report useful to someone other than the original observer.



## Assertions

## Assertions: the computational contract

**Core idea.** Assertions document developer invariants; they are not sufficient for validating untrusted user input and may be disabled in optimized Python. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def normalize(values):
    assert len(values) > 0
    total = sum(values)
    assert total != 0
    return [v/total for v in values]
print(normalize([1,3]))
```

**Expected result:** `[0.25, 0.75]`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For assertions, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Make a trace table with at least four rows: the initial state, two transitions and the final state. If a proposed shortcut skips a state, show why the output remains equivalent. The trace is a method of reasoning, not a substitute for full testing. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 2

## Assertions document internal expectations

An assertion is an executable statement that a condition should hold at a particular point. It can help detect violations of an invariant during development. For example, after normalizing a nonnegative weight vector with positive total, an assertion may check that its values sum approximately to one. If the property fails, the program has encountered an unexpected internal state. Assertions are not substitutes for validating data supplied by users because Python assertions can be disabled under optimized execution. Input validation should remain active whenever untrusted values are accepted.

Assertions also need appropriate scope. An assertion that a floating-point sum is exactly equal to one may fail because of representation error even when the numeric result is valid under the model. Conversely, an overly generous tolerance can allow genuinely invalid values to pass. A useful assertion reflects a mathematical or program invariant whose acceptable error is understood. Avoid writing assertions simply because a value happened to appear in one successful run.


## A test is a claim with an observable oracle

A unit test needs a setup, an action, and a way to decide whether the result is correct. The oracle may be a known numerical answer, an algebraic invariant, a reference implementation, a failure expectation, or a metamorphic relationship between inputs and outputs. A test that merely executes a function without checking its result does not establish correctness. A test that checks only whether an exception was avoided may miss a silent arithmetic error.

For a temperature converter, known reference points are useful: zero degrees Celsius corresponds to thirty-two degrees Fahrenheit, and negative forty is the same numerical value on both scales. These are independently checkable facts. For a weighted mean, multiplying all weights by a positive constant should leave the result unchanged, assuming the calculation is defined. This metamorphic property supports tests over many generated datasets. It does not replace boundary checks for empty data, zero total weight, or invalid numeric values.


## Boundary analysis catches many realistic defects

For a function that accepts integers from one through ten, inputs one and ten are more informative than several arbitrary middle values. Test zero and eleven as rejected inputs if the contract excludes them. For a sequence algorithm, test empty, singleton, and repeated-element collections when appropriate. For file parsing, test empty files, missing columns, and malformed rows. Each boundary probes a transition where implementation behavior is likely to change. A test suite that uses one large, ordinary dataset can overlook basic faults because only a narrow behavior pattern is exercised.

Equivalence classes organize input spaces according to expected behavior. A sign classifier has negative, zero, and positive classes. A grade classifier has score ranges separated by thresholds. A parser may distinguish valid integers, valid decimals, empty strings, and malformed text. Test at least one representative of each class and especially the boundaries. When continuous numeric values are accepted, also consider non-finite values such as NaN or infinity if the underlying type can represent them. Scientific calculations should decide whether such values are permitted, rejected, or propagated.



## Unit Tests

## Unit Tests: the computational contract

**Core idea.** A test should have a controlled setup, action and observable oracle. Test boundaries and failure paths as well as happy paths. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def add(a,b): return a+b
def test_add_zero():
    assert add(7,0) == 7
test_add_zero()
print('passed')
```

**Expected result:** `passed`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For unit tests, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Test a normal input, an empty input where meaningful, a boundary input and a malformed input. Explain whether the program should return a result, raise an exception or ask for a new value. This separates mathematical domain assumptions from interface behavior. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 3

## Property-based testing and its limits

Property-based tests generate many inputs and verify invariants. For a sorting function, a property is that the output is nondecreasing and contains the same multiset of elements as the input. Checking only order is insufficient: returning an empty list is trivially sorted but discards data. For a reversible conversion, a round trip may approximately recover the input within justified tolerance. Random generation is useful for exploration, but it does not guarantee that rare failure cases will be sampled. Combine generated data with carefully chosen boundaries and fixed regression cases.

A property must itself be correct. For example, assuming that adding a constant to every probability leaves a distribution valid is false without normalization and nonnegativity constraints. If a test encodes an incorrect mathematical law, a correct program may fail the test or a wrong program may pass. The specification and the oracle need critical review independent of implementation. In research code, compare selected calculations against known analytical cases or independent numerical methods where possible.


## Debugging by controlled experiments

When an output is wrong, change one relevant factor at a time and observe whether the failure persists. If a simulation gives unstable results, vary the time step while holding initial conditions fixed. If the result changes dramatically under step refinement, the numerical method or stability range may be responsible. If the result is wrong even for an analytically solvable case, inspect the model or boundary conditions. If only the display is wrong, inspect the transformation from computed data to visual coordinates. This experimental style separates model, algorithm, and presentation defects.

Logging can help reveal state transitions, but uncontrolled print statements are not a substitute for a hypothesis. Log values that distinguish candidate causes and remove or reduce diagnostic logging after the issue is resolved. Never record passwords, private records, or unnecessary sensitive information in debugging output. Repeated logging inside a large loop can also distort performance measurements. A carefully chosen trace for a small case is often more effective than an enormous, unsorted stream of messages.


## Regression tests protect repairs

A regression test encodes a previously failing case so that the defect is less likely to return. If a binary-search implementation once hung on a two-element interval, preserve that input as a test after fixing the update rule. If a parser once accepted an invalid negative count, test that rejection explicitly. The regression should explain the behavior being protected, not merely freeze the internal line of code that happened to change. Good tests allow refactoring while maintaining the intended contract.

A test suite may be green while the program is still incorrect outside the covered cases. Coverage metrics report which statements or branches were executed, but execution is not validation. A test that reaches a branch without asserting the resulting behavior still counts toward coverage. Treat coverage as a map of unvisited areas and an aid to test design, not a certificate of correctness. Independent code review, mathematical reasoning, and integration tests answer questions that coverage alone cannot.



## Input Validation

## Input Validation: the computational contract

**Core idea.** Input validation must be applied at trust boundaries. Reject malformed inputs clearly instead of guessing a correction. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def parse_age(text):
    age = int(text)
    if not 0 <= age <= 120: raise ValueError('age out of range')
    return age
print(parse_age('24'))
```

**Expected result:** `24`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For input validation, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Compare readability, asymptotic work and memory use with a plausible alternative. For small datasets, clarity may dominate micro-optimization. For huge datasets, count the operations rather than relying on a vague claim that one language construct is faster. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 4

## Case study: repairing a faulty mean function

Suppose a function sums values and divides by their count. It passes a test with `[2, 4, 6]`, returning four. Then a production dataset contains an empty group and the function raises division by zero. There are several possible repairs, and the domain decides which is valid. Reject an empty group with a clear exception, return an explicit missing result, or define a special value if the mathematical application supplies one. Returning zero is not generally a correct mean for empty data. A repair that hides the failure can bias a downstream average of group means.

Now consider floating-point inputs with NaN. The ordinary sum may become NaN even when most measurements are valid. Should the function exclude missing observations, propagate an invalid result, or reject the dataset? Each choice changes the estimand being computed. If missing values are excluded, the denominator should count retained observations rather than original positions. Add a test where one value is missing and state the expected behavior explicitly. Debugging statistical code therefore often requires clarifying the model rather than editing arithmetic syntax.


## Independent checking

A powerful practice is to calculate at least some expected results without using the implementation under test. If the program computes a standard deviation, derive a small example by hand or compare it to a separately implemented formula with the correct sample or population denominator. If a simulator generates random observations, test deterministic parts against known formulas and test statistical properties with appropriate tolerance and sample size. Using the same flawed helper function to compute both the result and the expected answer makes the test circular.

For a sum, an independent implementation is easy. For complex calculations, verification may require a high-precision numerical library, a symbolic derivation, or a trusted reference dataset. Document the source and limitations of the check. If only a few examples are verified, describe that evidence accurately. Do not call a model fully validated because a test script emitted the word PASS without meaningful oracles.


## Final synthesis

Debugging and testing turn assumptions into evidence. Reproduction identifies the failure, contracts define the expected result, controlled experiments isolate causes, and regression tests preserve repairs. Assertions monitor internal invariants, while input validation guards the boundary between trusted computation and external data. Boundary tests and properties reveal different classes of mistakes; neither replaces independent mathematical review. The goal is to know what has been established, what remains uncertain, and which failure modes still matter.

As a final exercise, deliberately introduce an off-by-one error into a binary search or a list traversal. Record the smallest input that exposes it. Explain the violated invariant, change the smallest possible part of the update, and add a regression test. Then write a second test for a distinct boundary condition and state why the two checks are independent. That process develops the habit of diagnosing causes rather than chasing symptoms.


### Create unit tests for a function that divides two integers.

**Normal**
Check 10/2=5, including numeric type and precision expectations.

**Boundary**
Check a negative numerator and divisor sign rules.

**Failure**
Check divisor zero raises ZeroDivisionError (or a documented custom error), rather than silently producing nonsense.

### Locate a bug in binary search when the upper bound is exclusive.

**Invariant**
Use search interval [lo,hi), initially [0,len(a)).

**Step**
Choose mid=(lo+hi)//2; for a[mid]<x set lo=mid+1, else set hi=mid.

**Check**
Loop until lo==hi and then check membership; test empty list, first item, last item and absent targets.

### Distinguish an assertion from untrusted-input validation.

**Assertion**
assert expresses an internal development assumption and may be disabled under optimized execution.

**Validation**
Input checks must execute in production and generate predictable diagnostics for invalid user data.

**Design**
Use if/raise ValueError at input boundaries, reserving assertions for invariants that should never fail when code is correct.


### Applied investigation: Testing strategy and binary-search boundaries

A strong test suite includes ordinary cases, boundaries, malformed input, and cases chosen from the algorithm’s stated assumptions. Distinguish unit tests for a pure function from integration tests that exercise several components together. Property tests can assert that sorting preserves element multiset and produces a nondecreasing list. Those properties cover many inputs but do not by themselves prove that every possible language/runtime execution is correct.

Binary search is particularly sensitive to off-by-one errors. With a closed interval [low, high], replacing it after each comparison must exclude the tested midpoint; otherwise low and high may stop changing. For an empty array set high to −1 so the loop never enters. Test search for first, last, absent, and repeated values with a defined match policy. The number of comparisons depends on the interval convention and when equality is checked.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.
