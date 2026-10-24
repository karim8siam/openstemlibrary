# Unit 4: Functions and scope

## Parameters

## Parameters: the computational contract

**Core idea.** Parameters are local names bound when the function is called; document the allowed domain and dimensional meaning. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def area(width, height):
    return width * height
print(area(3, 5))
```

**Expected result:** `15`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For parameters, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Before implementation, identify which facts are input data and which are policy. A function that hardcodes mutable policy is fragile even when its first output is correct. Try a case where the given value is missing or physically impossible; decide whether to reject, default or request clarification. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 1

# Extended laboratory: functions as contracts, composition, and controlled state

A function gives a name to a reusable operation, but reuse alone is not its most important property. A well-designed function creates a boundary around assumptions: it receives inputs with defined meanings, performs an operation under those assumptions, and returns a result whose meaning the caller can understand. Once that boundary is stable, other parts of a program can rely on the contract without duplicating internal logic. This is why function design affects correctness, testability, collaboration, and maintainability even in a program with only a few hundred lines.

## Parameters separate a general rule from one particular calculation

Consider the area of a rectangle. A function that returns `width * height` is reusable because the dimensions are parameters rather than fixed literals. Yet the formula is meaningful only for appropriate inputs. If the caller provides width in metres and height in centimetres, the numerical product is not an area in square metres without conversion. If one dimension is negative, ordinary geometric area is not defined as a negative number under the intended model. The function contract must therefore say more than that it accepts two numeric inputs. It should define permissible values, units, and output semantics.

Positional parameters work well when argument order is obvious, but they can introduce silent mistakes when two values share a type. A call such as `apply_discount(10, 100)` may confuse a percentage with an amount. Keyword arguments can improve readability: `apply_discount(price=100, percent=10)`. A simple data structure may be more appropriate when many parameters always travel together. Adding a class solely to replace a two-parameter function is not automatically an improvement; every abstraction carries a maintenance cost. Design the interface according to actual data relationships and likely changes.

Default arguments are convenient but require careful thought about meaning and evaluation time. A default tax rate hardcoded into a function may become wrong when policy changes. In Python, a mutable default such as an empty list is created when the function is defined, not afresh on every call. If a function appends to that shared default, calls can affect each other unexpectedly. Use an immutable sentinel such as `None` when a new collection is intended for each call, then construct that collection inside the function. This detail matters because a parameter declaration can accidentally introduce persistent shared state.


## Returning information is different from displaying it

A function that prints a result writes to an output stream. A function that returns a result makes the value available for subsequent calculations, comparisons, storage, or display. Suppose a function computes the mean of a measurement series. If it prints the number and returns `None`, another function cannot directly compute the difference between that mean and a target value. An implementation that returns the mean can still be printed by its caller; it is useful in a spreadsheet export, a simulation, and an automated test without changing its core logic.

Return values also communicate failure, but failure conventions need care. Returning zero for both a legitimate zero calculation and a missing result makes the two situations indistinguishable. Returning `None`, a tagged result object, or raising a documented exception may be more appropriate. The choice should reflect whether absence is an expected outcome or an exceptional violation of the contract. For example, searching a list may legitimately find no match; dividing by zero may be an invalid operation. An explicit interface makes the caller responsible for handling the right cases.

Multiple return values are often expressed as tuples. A function calculating the smallest and largest readings can return `(minimum, maximum)` instead of forcing the caller to repeat a scan. That is useful when the outputs share an expensive computation, but it does not justify returning a long tuple whose positions are easy to confuse. Named structures improve clarity when several related values are returned. The guiding question is what the caller needs to know and how to make misuse difficult.


## Pure computation versus side effects

A pure function returns the same result for the same inputs and does not modify external state. A Celsius-to-Fahrenheit conversion can be pure; a function that reads the current time or writes a file is not. Pure functions are easier to test because their result depends only on values supplied explicitly. Side effects are still necessary in real applications, but isolating them makes behavior easier to predict. A registration system must save a record and send a message; placing those effects in explicit boundary functions helps keep validation and business-rule calculations deterministic.

Suppose a function that computes a bill also writes the result to disk. A unit test for the arithmetic now depends on filesystem permissions and cleanup. A better design can return a validated bill object, while a separate persistence operation stores it. An integration test checks that persistence works. The separation lets you test mathematical correctness and external effects independently. It also makes it possible to retry a failed write without recomputing the bill under a changed policy, provided the transaction semantics are designed correctly.



## Return Values

## Return Values: the computational contract

**Core idea.** Returning data rather than printing it makes the function composable, testable and usable by other functions. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def extrema(values):
    return min(values), max(values)
print(extrema([4, 9, -1]))
```

**Expected result:** `(-1, 9)`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For return values, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Make a trace table with at least four rows: the initial state, two transitions and the final state. If a proposed shortcut skips a state, show why the output remains equivalent. The trace is a method of reasoning, not a substitute for full testing. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 2

## Scope and name binding

Scope determines where a name is visible and which binding an expression refers to. A local name assigned inside a Python function normally does not rebind a similarly named global variable. If a global variable `rate` equals 0.1 and a function assigns local `rate = 0.2`, the two bindings can coexist. Reading the global value after calling the function still yields 0.1. A common beginner error occurs when a function attempts to read and assign a global name without declaring the intended scope; Python may treat the name as local and raise an error before the local assignment has completed.

Using global declarations to make every function access shared mutable state is usually a warning sign. The function's behavior then depends on context not visible in its argument list. That complicates tests and makes reusing the function in another project harder. Pass required configuration as an argument or through a clearly controlled object. Global constants that genuinely never change are less problematic than global counters, caches, or policy settings that several functions mutate. The key distinction is whether the function's external dependencies and effects remain comprehensible.

Closures provide a different form of scope. A function defined inside another function can retain access to names from its enclosing environment. This is useful for creating small configured operations, such as a converter with a chosen scale factor. If the captured values are mutable, later changes can affect the function. A closure is therefore not a guarantee of immutability or purity. Explain what is captured and whether the function is intended to observe future changes.


## Recursion is a structural claim about subproblems

A recursive function solves a problem by expressing it in terms of smaller instances of the same problem. For factorial, the mathematical recurrence is `0! = 1` and `n! = n*(n-1)!` for positive integers. A correct recursive implementation requires a base case, a valid input domain, and a strictly decreasing measure such as n. Calling the function with a negative integer without validation can cause unbounded recursion because repeatedly subtracting one never reaches zero. The base case does not help if the allowed inputs do not guarantee reaching it.

A recursion proof normally has two parts. The base case establishes that the function produces the right result for the smallest admissible input. The inductive step assumes correctness for a smaller instance and shows that the current computation produces the desired result. For factorial, assume the recursive call returns `(n-1)!`; multiplying by n yields `n!`. This argument establishes mathematical correctness under the recurrence. It says nothing about a language's recursion-depth limit or memory consumption. A theoretically correct recursion can still fail operationally for inputs that are too large.

The factorial problem is also easily expressed with a loop. An iterative implementation can maintain an accumulator equal to the product of integers already processed. It avoids building a deep call stack and may be preferable for large n. Recursion is compelling for naturally recursive structures such as trees, divide-and-conquer algorithms, and nested expressions, but not automatically best for every repetition. Compare the clarity of the recurrence, maximum depth, error handling, and available memory before selecting an implementation.


## A trace of recursive execution

To compute factorial of four, the initial call requires four times factorial of three. That call requires three times factorial of two, which requires two times factorial of one. Factorial of one can return one under a chosen base convention. On return, factorial of two becomes two, factorial of three becomes six, and factorial of four becomes twenty-four. The recursive descent postpones multiplication while subproblems are created; the return phase resolves the deferred operations. A drawing of the call stack makes this control flow visible.

If the recurrence branches into two recursive calls, as in a naive Fibonacci implementation, the number of calls may grow rapidly because identical subproblems are recomputed. Memoization or an iterative dynamic-programming formulation can avoid much of that duplication. The appropriate optimization depends on the recurrence and input range. Storing every subproblem may save computation while consuming memory. A function design review should make these trade-offs explicit rather than assuming that shorter recursive code is always more efficient.



## Recursion

## Recursion: the computational contract

**Core idea.** A recursive function needs a base case and a strictly smaller subproblem. A mathematical recurrence is not proof that an implementation terminates. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)
print(factorial(5))
```

**Expected result:** `120`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For recursion, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Test a normal input, an empty input where meaningful, a boundary input and a malformed input. Explain whether the program should return a result, raise an exception or ask for a new value. This separates mathematical domain assumptions from interface behavior. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 3

## Modules are dependency boundaries

As programs grow, related functions can be grouped into modules. The purpose is not merely to shorten individual files. Modules define responsibilities, import relationships, and reusable interfaces. Suppose a grade-reporting application contains code for validating scores, computing statistics, formatting reports, and reading files. Grouping these responsibilities can make the dependency direction clearer: the reporting layer may call calculation functions, while the calculation layer should not depend on the reporting interface. Such a design allows the same calculations to be used in a command-line program or a web application.

Circular imports appear when module A imports B while B imports A during initialization. The issue may be hidden in a small prototype but surface as a partially initialized object. One repair is to extract shared types or functions into a lower-level module C that both A and B can import. Another is to redesign responsibilities so dependencies flow in a single direction. Drawing the import graph before reorganizing files helps reveal whether the circular dependency represents genuine coupling or merely a misplaced helper function.

A module's import-time behavior also matters. A module that immediately reads a large dataset, opens a connection, or launches an application when imported is harder to test and reuse. Put executable entry-point behavior behind an explicit main function or conventional guard, while exposing importable computations separately. This makes the module useful both as a program and as a library without surprising side effects.


## A worked design: statistics from a classroom roster

Suppose a roster contains student identifiers and scores. The application should compute a class mean, classify individual scores, and create a text report. Start with independent contracts. The parser accepts structured records and rejects missing identifiers or invalid score types. The mean function takes a nonempty numeric list and returns a numeric mean. The classifier accepts a score and a policy and returns a category. The formatter accepts results and returns a string; it does not modify scores. The save operation writes that string to a chosen destination and reports filesystem errors.

For scores 70, 80, and 90, the mean is `(70 + 80 + 90)/3 = 80`. Write one test for this example, but do not stop there. Test a single score, a repeated score, an empty list, and a list containing an invalid value. Decide whether the parser or calculation function rejects non-finite floats. Test classification exactly at grade thresholds. Confirm that formatting the report does not change the input data. Finally, run an integration test that writes the report and verifies the stored contents, while keeping filesystem effects out of arithmetic tests.

If a new requirement adds a median, the program should need one new calculation and an update to report assembly, not a rewrite of the parser or grade classifier. If a different output format is requested, the calculations should remain untouched. These change scenarios demonstrate whether the decomposition corresponds to independent responsibilities. A design is not validated merely because its initial output is correct; it should also localize likely changes.


## Test doubles and dependency injection

External dependencies such as storage and email services can be supplied through parameters or small interfaces. During a test, a fake storage object can record what the program attempted to save without writing to production. This is often called dependency injection. It is useful when a function's responsibility includes coordinating external effects. The fake must reproduce the behavior relevant to the test, including possible failures; a fake that always succeeds cannot establish correct behavior under network outages or storage conflicts.

Tests should distinguish a function's contract from a particular implementation. If a sorting helper promises sorted output while preserving duplicates, test the order and multiplicities rather than the number of swap operations used internally. If a function promises not to mutate input, preserve a copy of the input and compare after the call. Such tests permit legitimate refactoring while detecting behavior that matters to callers.



## Modular Interfaces

## Modular Interfaces: the computational contract

**Core idea.** Local rebinding does not alter the module binding. Mutable objects introduce a distinct issue: mutation through an alias. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
rate = 0.1
def calculate(amount):
    rate = 0.2
    return amount * rate
print(calculate(10), rate)
```

**Expected result:** `2.0 0.1`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For modular interfaces, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Compare readability, asymptotic work and memory use with a plausible alternative. For small datasets, clarity may dominate micro-optimization. For huge datasets, count the operations rather than relying on a vague claim that one language construct is faster. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 4

## API design and error communication

A public function should have a name that communicates its purpose, not merely the fact that it does something. `validate_temperature` is clearer than `process`, and `mean_nonempty` signals a requirement that should appear in documentation. Arguments should have stable meanings; changing an argument from metres to centimetres without changing the contract breaks callers even if the function still accepts floats. Error messages should be actionable and avoid leaking irrelevant implementation details to end users, while logs may retain deeper diagnostic information for developers.

Versioning matters when a function or module becomes widely used. Adding an optional parameter with a safe default may be compatible with existing calls; reordering positional parameters may not be. Changing a returned tuple to a dictionary may be beneficial but break code that unpacks the original result. Explicit interfaces permit controlled evolution. In a small academic exercise, write a short contract and revisit it when changing requirements so that compatibility becomes a deliberate decision.


## A failure-first exercise: hidden shared state

Imagine a function that records the names of students who received an alert. It declares a default parameter `recipients=[]` and appends to it on every call. The author intended a fresh list when no recipients were supplied, but the list object is created only once when the function is defined. The second call may see names from the first. This can result in duplicate notifications or disclosure of unrelated recipient information. The function might pass a single-call demonstration, making the bug easy to miss.

The repair is to use `None` as the default and allocate a new list inside the function when no collection was supplied. Test two independent calls and verify that the second does not inherit the first call's state. If callers intentionally provide a mutable list, decide whether the function may modify that supplied object or should copy it. There is no universally correct choice, but the contract must state it. The exercise illustrates how function parameters, object identity, and scope combine to determine program behavior.


## Final synthesis

Functions bring together three forms of reasoning. Parameter and return contracts explain what computation means at the boundary. Scope and purity explain what can change inside and outside that boundary. Recursion and modular organization explain how larger problems are decomposed into reusable operations. An effective function is not judged only by its length or reusability; it is judged by whether a caller can use it correctly, test its guarantees, and understand its side effects.

As a final exercise, split a small existing script into three functions: parsing, calculation, and presentation. For each, specify valid inputs, returned outputs, and exceptions or error results. Replace hidden global state with explicit dependencies. Test each function independently and then test the composed application. If a change to presentation forces a change to calculation, revisit the boundary. That is a concrete way to evaluate modular design rather than merely adding more function definitions.


### Compute factorial(5) recursively and explain the base case.

**Definition**
Factorial obeys 0!=1 and n!=n(n-1)! for n>=1.

**Expansion**
5! = 5·4·3·2·1 = 120.

**Correctness**
The base case returns 1 at zero. For n>0 a smaller positive integer is passed, so recursion reaches the base case.

### Explain why returning a value differs from printing it.

**Return**
A function returning 4 supplies a value that can be multiplied or passed to another function.

**Print**
Printing 4 writes to an output stream, typically returning None as the function result.

**Design**
Use return for reusable computation and print at the user-interface boundary; test returned data without intercepting console output.

### Predict names after local rebinding of a variable named rate.

**Scope**
A function-local assignment to rate binds a new local name unless global/nonlocal declarations change the rule.

**Evaluate**
With global rate=0.1 and local rate=0.2, calculating 10·rate in the function gives 2.0.

**Check**
After calling the function the global name still denotes 0.1. Mutation of an object through an alias is a separate case.


### Applied investigation: Pure functions, call boundaries and recursion

A pure function maps its explicit arguments to an output without depending on mutable global state. If a function computes factorial(n), its precondition should require a nonnegative integer and its postcondition should return the product of integers from one through n. For n=0, the empty product is one. Recursive calls must reduce n until they reach the base case; otherwise the program is not guaranteed to terminate. Tail calls, stack frames and memoization affect execution properties without changing the mathematical factorial.

A local variable with the same name as a global should not silently mutate the global in languages with lexical scope. Try an example in which a function declares counter=3 while the enclosing scope has counter=10: reading the local is well-defined, but assigning to the outer binding may require explicit declaration depending on the language. The scope visualization is a teaching model and not a full interpreter; nested closures, reference capture and thread visibility require additional rules.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.
