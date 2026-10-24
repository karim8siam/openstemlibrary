# Unit 6: Program organization

## Files

## Files: the computational contract

**Core idea.** File operations are effects: location, permission, encoding, failure modes and cleanup belong in the design. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
from pathlib import Path
p = Path('output.txt')
p.write_text('hello\n', encoding='utf-8')
print(p.read_text(encoding='utf-8').strip())
```

**Expected result:** `hello`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For files, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Before implementation, identify which facts are input data and which are policy. A function that hardcodes mutable policy is fragile even when its first output is correct. Try a case where the given value is missing or physically impossible; decide whether to reject, default or request clarification. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 1

# Extended laboratory: files, modules, errors, and object boundaries

A program becomes a system when it must retain information between executions or communicate with something it does not control. Reading a file, saving a report, loading a configuration, and importing a module all create dependencies beyond local arithmetic. These dependencies can fail in ways that are difficult to reproduce with a simple input number. Files may be absent, inaccessible, truncated, or encoded unexpectedly. Modules may not be installed or may initialize in an unexpected order. Objects may share mutable state across callers. Understanding how to manage these boundaries is essential for moving from a classroom snippet to software that remains reliable after the original author stops supervising it.

## Treat files as external state

Suppose a script saves experiment results to `results.txt`. The simplest Python implementation opens a path and writes text. But correct behavior requires more questions. Is the path relative to the current working directory or to the script's own directory? Should an existing file be overwritten, appended to, or rejected? What text encoding will be used? Does writing a result guarantee that the data has reached durable storage? What happens if the process terminates after writing half the content? The apparent simplicity of file operations does not remove these obligations.

Use context managers to manage resources whose lifetime must be controlled. Opening a file inside a `with` block ensures the file object is closed when control leaves the block, including when an exception occurs. This reduces resource leaks and improves clarity. Yet closing is not the same as atomic replacement. For a report that must never be observed half-written, a common strategy is to write a complete temporary file in the target directory and then rename or replace the destination where the operating system and filesystem provide the required atomic semantics. The exact durability guarantees are environment-specific and should not be assumed without testing.

Reading files also requires a schema. A CSV column named `score` might contain `"85"`, an empty string, or `"N/A"`. The parser should distinguish absent information from a legitimate score of zero. A text file may use UTF-8, but a legacy export may use another encoding; decoding errors should be reported rather than silently corrupting text. If a file is untrusted, validate its size and format before letting it control expensive operations or filesystem paths. Input from disk is not automatically safer than input from a web form.


## A safe file-processing pipeline

Consider a program that reads a roster, calculates average scores, and writes a summary. Separate the pipeline into reading bytes or text, parsing records, validating the schema, calculating statistics, formatting a report, and writing output. This sequence gives each layer a testable responsibility. A parser test can supply an in-memory string containing malformed rows without creating real files. An arithmetic test can provide already validated numbers. An integration test can read a small temporary file and verify the resulting report. Breaking the pipeline apart reduces the need to debug everything simultaneously.

The validation stage should report the location of a problem. A message saying `row 17: score must be a finite number` gives a user a route to repair the file. A generic `ValueError` message may not. Decide whether invalid rows cause the entire import to fail or whether valid rows may be accepted with a separate error report. Partial acceptance is a domain policy, not something a broad exception handler should decide accidentally. A scientific analysis may require rejecting the entire dataset if any measurement is missing; another application may allow missing entries under a documented imputation policy.


## Errors are information, not obstacles to be hidden

An exception communicates that an operation could not complete under its assumptions. The meaning of an exception depends on where it occurred. A missing configuration file may be recoverable if the application has a documented default configuration. A missing required calibration file may make every downstream measurement invalid and should stop the run. Catch an exception at a layer that can make a meaningful decision or add context. Catching every exception and continuing with made-up values can transform a detectable failure into a plausible but incorrect result.

Different failure modes deserve different handling. A `FileNotFoundError` may call for asking the user to choose another path. A `PermissionError` may require changing the destination or access rights. A parsing error may require editing the file contents. A programmer error such as calling a non-existent method should generally remain visible during development rather than being disguised as a missing file. Logging enough context to reproduce a failure is helpful, but logs must not expose confidential data unnecessarily.

An exception handler should also preserve cleanup. Resources acquired before the failure may need to be released. Context managers and `finally` blocks support this, but they must be designed around the actual operation. If a task writes several files, cleaning up a temporary file is different from rolling back already committed external state. A multi-step operation involving files, emails, and databases may need explicit recovery or idempotence rules rather than only a `try`/`except` block.



## Exceptions

## Exceptions: the computational contract

**Core idea.** Exceptions communicate exceptional cases. Catch at a layer that can recover or add useful context; avoid broad silent swallowing. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def positive_root(x):
    if x < 0: raise ValueError('negative input')
    return x ** 0.5
print(positive_root(9))
```

**Expected result:** `3.0`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For exceptions, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Make a trace table with at least four rows: the initial state, two transitions and the final state. If a proposed shortcut skips a state, show why the output remains equivalent. The trace is a method of reasoning, not a substitute for full testing. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 2

## Failure values versus exceptions

Not every absence should be an exception. A dictionary lookup for an optional configuration key may return a default; a search function may return an optional result when no match exists. In contrast, opening a required scientific input file may appropriately raise if the file cannot be found. Choose based on the function's contract. If a function returns `None` on failure, callers must check for it before arithmetic. If it raises, callers must understand which exceptions are expected and where recovery is possible. Ambiguous conventions lead to bugs when zero, an empty collection, or a false boolean is accidentally interpreted as failure.

A useful rule is to avoid returning arbitrary sentinel values that might be valid outputs. Returning negative one as a missing index may work when valid indices are nonnegative, but a signed numeric computation may legitimately return negative one. Consider a tagged result such as a tuple `(success, value)` or a small object with explicit status when the operation has several meaningful outcomes. The additional structure can be justified by reducing ambiguity.


## Modules as a dependency graph

A module groups definitions and controls how code is imported. It lets a statistics function be reused by both a command-line report and a web service. However, importing a module is also an execution event: top-level code runs during import. If a module begins reading production files or making network connections at import time, tests that merely import the module can trigger unwanted effects. Isolate entry-point execution, commonly behind a main function, and keep reusable definitions free of unnecessary initialization behavior.

Plan import relationships by dependency direction. A low-level calculation module should not need to import a high-level user-interface module that happens to call it. If both need a shared data structure, place that structure in a lower-level module they can both import. This helps avoid circular dependencies and clarifies ownership. The structure resembles the original problem decomposition: interfaces should depend on stable computations, not the other way around.

A module is also a unit of versioning. A function exposed for other programs may be relied upon in ways the author did not anticipate. Changing parameter names, argument order, return types, or exception behavior can break dependent code. Document public interfaces, add tests for promised behavior, and refactor internal implementation behind those interfaces when possible. This keeps change localized while preserving correctness for callers.


## Objects model state and operations together

Object-oriented programming can be useful when a domain has an entity whose state must obey invariants over time. A counter maintains a numeric value and offers operations such as increment and reset. A registration object may move through pending, confirmed, and cancelled states. A measurement device may have a calibration setting and an operation to acquire readings. Grouping state and operations in an object can keep constraints close to the code that changes them. But creating a class for every small computation often adds complexity without a corresponding modeling benefit.

Imagine a `Counter` object with an integer value. An invariant might require that its value always be nonnegative. Its increment method increases the value, while a decrement method must reject attempts to go below zero. If callers can assign any value directly to a public attribute, they may bypass the invariant. A design can provide controlled operations and validation, while recognizing that Python's conventions do not create an absolute security boundary around every field. The objective is clear ownership and correct use, not a claim that a class prevents all misuse.

Identity and equality are important object concepts. Two records may contain the same fields but represent different entities. A student record with the same name and course may belong to two distinct students. Value equality is not always entity identity. Decide whether objects represent immutable values, such as a two-dimensional vector, or independently evolving entities, such as a registration record. That decision affects copying, hashing, comparisons, and storage.



## Modules

## Modules: the computational contract

**Core idea.** Module boundaries organize ownership and isolate dependencies. Import direction affects cycles and deployment. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
# geometry.py
def perimeter(w, h):
    return 2 * (w + h)
# from geometry import perimeter
# print(perimeter(3, 4))
```

**Expected result:** `14 (after importing and calling)`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For modules, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Test a normal input, an empty input where meaningful, a boundary input and a malformed input. Explain whether the program should return a result, raise an exception or ask for a new value. This separates mathematical domain assumptions from interface behavior. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 3

## Inheritance versus composition

Inheritance can express a genuine subtype relationship when instances of the derived type can satisfy the promises of the base type. It should not be used merely because two classes share a few lines of code. Composition—building a component from other components—is often clearer. For example, a report generator can contain a formatter and a storage service without inheriting from either. The dependency relationship is explicit, and components can be replaced independently in tests.

When inheritance is used, verify behavioral compatibility. A derived class that changes a promised operation so that callers can no longer rely on it violates the base interface even if the code runs. Consider whether error conditions, return types, and invariants remain consistent. Treat inheritance as an interface contract, not just a syntax feature for reusing implementation details.


## Case study: storing experiment results

Build an experiment recorder that accepts a timestamp, device identifier, measured value, and unit. The program must validate a record before storing it, append accepted records, and allow a report to summarize measurements for a selected device. A small value-like record type can represent a validated observation. A recorder object can manage the in-memory collection and persistence policy. A pure summary function can compute statistics from the validated records. The distinction keeps measurement arithmetic independent of the details of how data is stored.

Suppose three temperature readings are 20.0, 21.5, and 22.5 degrees Celsius. Their mean is `(20.0 + 21.5 + 22.5)/3 = 64/3`, approximately 21.333 degrees Celsius. That result should carry an appropriate precision statement based on the input data, not an arbitrary long list of decimal digits. Before computing, verify that the three observations use compatible units. If a reading is recorded in Fahrenheit, convert it explicitly before combining. A numeric list alone does not preserve enough metadata to guarantee meaningful aggregation.

Test the recorder's invalid-input behavior: a missing unit, a malformed timestamp, a non-finite measurement, and a duplicate observation identifier where identifiers are supposed to be unique. Test writing to an unavailable directory and confirm the failure is reported without claiming the measurement was saved. After a successful write, read the file back and compare against the expected record set. These checks connect data validation, error handling, storage, and object state.


## Atomicity and idempotence

If a program may be retried after an interruption, repeating an operation should not accidentally duplicate an irreversible effect. An idempotent operation can be applied more than once with the same intended state result. Writing a report by replacing its complete contents may be idempotent under a suitable design; appending the same observation on every retry is not. A record identifier can help detect duplicates, but only if the storage layer enforces uniqueness consistently. This becomes important when automated workflows restart after an error.

Consider a sequence that saves a registration and then sends a confirmation email. The save may succeed while the email fails. A simple retry of the entire sequence may save a duplicate registration. A more reliable design records a stable registration ID and tracks whether the notification has been sent. Retrying then resumes the incomplete step without repeating completed effects. This is beyond the needs of a first Python script, but it follows directly from the same principle: distinguish computation from side effects, and make state transitions explicit.



## Basic Object Design

## Basic Object Design: the computational contract

**Core idea.** An object groups state with operations that maintain invariants. A class is not required when a pure function is simpler. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
class Counter:
    def __init__(self): self.value = 0
    def increment(self): self.value += 1
c = Counter(); c.increment(); print(c.value)
```

**Expected result:** `1`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For basic object design, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Compare readability, asymptotic work and memory use with a plausible alternative. For small datasets, clarity may dominate micro-optimization. For huge datasets, count the operations rather than relying on a vague claim that one language construct is faster. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 4

## Testing at different boundaries

A unit test for a parser checks text-to-data conversion. A unit test for an arithmetic function checks a mathematical result. An integration test for file persistence checks that bytes are actually stored and recovered. An end-to-end test checks the full workflow, potentially including user input and output. These levels answer different questions. It is possible for every pure function to pass while the complete application fails because filenames are wrong or permissions are missing. It is also possible for an end-to-end demonstration to pass while error handling remains completely untested.

Use temporary directories for tests that create files, and clean them up after the test. Mock an external service when the objective is to inspect how the program reacts to a service response, but add separate integration evidence when possible. Keep fixtures small and representative. A test that silently swallows all exceptions is not useful evidence; it may succeed when the application has failed. Make failures visible and associate them with the intended contract.


## A debugging exercise: the disappearing report

A script writes `summary.txt` using a relative path. The developer runs it from one directory and sees the output. A scheduled task runs the same script from another working directory and reports success, but the expected file is missing. The script may have written to a different path. The defect is an unstated assumption about the working directory. One repair is to use a configurable absolute destination; another is to resolve a location relative to a well-defined project root. The correct choice depends on whether the program is meant to write into the caller's working directory or its own project area.

Instrument the script to report the resolved destination without exposing unrelated sensitive paths. Add a test that invokes the function from two different working directories and verifies the intended path convention. If a report must be preserved across deployments, do not assume that a temporary hosting filesystem is durable. This example shows that system context can invalidate behavior even when the file-writing function is locally correct.


## Final synthesis

Files, exceptions, modules, and objects extend programming into the management of boundaries. Files introduce persistence, encoding, permissions, and partial failure. Exceptions communicate that assumptions were not met and require deliberate recovery policies. Modules organize dependencies and stable interfaces. Objects model evolving state and the operations that preserve its invariants. The common lesson is that reliable software must account for the environment around a computation, not merely its inner arithmetic.

Before moving to testing and debugging, design a tiny record importer with a pure parser, a validator, a storage operation, and a reporting function. State the error conditions at each boundary and test them separately. Then simulate a failure between saving a record and sending a confirmation. Describe how a retry avoids duplicating the record. A design that handles those conditions transparently is more valuable than one that merely runs successfully on a perfect input file.


### Design exception handling for a missing configuration file.

**Separate**
File reading can raise FileNotFoundError; parsing may independently fail even if the file exists.

**Handle**
Catch missing-file errors at the layer that can choose a default, request a path or stop with an actionable message.

**Preserve**
Do not catch every exception and claim success; unrelated programming defects must remain visible.

### Explain when a class improves a counter implementation.

**State**
A counter has a numeric state and operations such as increment and reset.

**Invariant**
The object can enforce nonnegative integer state and centralize state-changing behavior.

**Alternative**
If no persistent state or invariant is needed, a pure function is simpler; choose classes for real modeling needs.

### Prevent a circular-import dependency between modules A and B.

**Detect**
If module A imports B and B imports A at initialization, partially constructed module objects can cause failures.

**Refactor**
Move shared value objects or functions into module C, which both A and B import.

**Verify**
Draw A→C and B→C; there is no cycle. Test importing each module independently.


### Applied investigation: Errors, interfaces and component boundaries

A reusable module should distinguish input errors from failures of external resources. For example, parsing an invalid integer is different from failing to open a file. Validation errors can be handled near the caller with a clear message; I/O failures may require retry, permission diagnostics or graceful shutdown. A blanket exception handler that returns an empty result hides faults and can damage data integrity.

Dependency direction determines how easily a component can be tested. A parser that directly writes to disk is harder to test than one that receives text and returns structured values; the caller can decide whether to persist the result. Write a module contract specifying the accepted input, returned data and possible failures. Substitute an in-memory test double for the file system to test both success and failure paths. The simple module-count model does not measure maintainability; observable behavior under change is a better criterion.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.
