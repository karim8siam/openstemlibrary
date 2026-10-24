# Unit 8: Applied programming

## Text Processing

## Text Processing: the computational contract

**Core idea.** A tokenizer defines the units being counted. Real corpora require explicit punctuation and Unicode policies. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
text = 'A B A C'
counts = {}
for word in text.lower().split():
    counts[word] = counts.get(word,0) + 1
print(counts['a'])
```

**Expected result:** `2`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For text processing, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Before implementation, identify which facts are input data and which are policy. A function that hardcodes mutable policy is fragile even when its first output is correct. Try a case where the given value is missing or physically impossible; decide whether to reject, default or request clarification. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 1

# Extended laboratory: building an end-to-end data-processing program

A final programming-fundamentals project should connect individual skills without pretending that a collection of individually correct functions automatically forms a reliable application. Consider a command-line tool that reads a dataset of laboratory measurements, validates records, calculates basic summaries, and writes a reproducible report. The goal is not to imitate a large production platform. It is to design a small program whose assumptions, transformations, and failure cases can be understood and tested from beginning to end.

## State a complete processing contract

The tool accepts a CSV file with columns for observation ID, instrument ID, timestamp, value, and unit. A valid observation requires a nonempty stable ID, a recognized instrument name, a parseable timestamp, a finite numeric value, and a supported unit. The specification must decide whether duplicate observation IDs are errors, whether measurements in different units may be converted, and whether incomplete rows cause the whole analysis to fail. The output is a report with the number of valid observations, the number rejected, and summary statistics computed on a clearly defined set. This contract is more valuable than immediately choosing a chart library.

An important modeling decision is whether measurement values are comparable. Averaging temperatures and lengths is meaningless even though both can be stored as floating-point numbers. If the file contains several physical quantities, group by quantity and compatible unit before calculating. If conversion is supported, specify the canonical unit and conversion rule. A report should describe its selection criteria, date range, and missing-data policy so that another investigator can reproduce the same result. Formatting is part of scientific communication because a number without its interpretation is not a complete result.


## Parse and validate one record at a time

Separate the parser from the validator. The parser converts text into representations such as strings, numbers, and timestamps. The validator checks domain-specific conditions: nonempty identifier, allowed unit, finite measurement, sensible timestamp range, and uniqueness if required. Keep the raw source row or line number in the error report so the user can locate a problem. A parser that silently turns a malformed reading into zero changes the dataset and may bias every downstream statistic. A validator should not guess a unit just because one appears frequently elsewhere in the file.

For a small implementation, store successful records in a list and track seen identifiers in a set. This gives a clear way to detect duplicates during processing. When a duplicate appears, decide whether to reject both conflicting records, retain the first, or apply an explicit revision rule. The choice must be stated before coding because it changes the meaning of the analysis. A set can detect repeated IDs but does not preserve their original occurrences; retain enough information in the error log to explain the conflict.



## Numerical Tasks

## Numerical Tasks: the computational contract

**Core idea.** Mathematical formulas become reliable programs only after empty-input behavior and numeric precision are defined. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def mean(values):
    if not values: raise ValueError('empty series')
    return sum(values)/len(values)
print(mean([1,2,3,4]))
```

**Expected result:** `2.5`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For numerical tasks, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Make a trace table with at least four rows: the initial state, two transitions and the final state. If a proposed shortcut skips a state, show why the output remains equivalent. The trace is a method of reasoning, not a substitute for full testing. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 2

## Transform and summarize the data

A summary function should accept already validated records and avoid filesystem effects. Group observations by the desired key, such as instrument and measurement type. For each nonempty group, calculate its count, minimum, maximum, and arithmetic mean. For readings `2, 4, 6, 8`, the count is four, minimum two, maximum eight, and mean five. These values are simple enough to check independently. For groups with no observations, the mean is undefined; the report should display an explicit absence rather than inventing a zero.

Think carefully about outliers and measurement errors. A very large value may be a legitimate event, a sensor defect, or a unit mistake. Automatically deleting every extreme value without a documented rule can bias the findings. Keep raw records and report which ones are excluded under any declared filtering policy. Descriptive statistics describe the selected dataset; they do not establish that the data are representative or that a scientific hypothesis has been confirmed. A small programming tool should state this limitation plainly.


## A reproducible command-line interface

Provide a command-line interface with an input path, output path, and optional settings. A parser such as Python's `argparse` can check whether required arguments are present and display a help message. Input paths should be treated as data, not constructed by insecure string concatenation with shell commands. Output should be written only to the path chosen under the program's documented rules. When a path does not exist or permission is denied, report the reason and exit with an appropriate failure status rather than printing a false success message.

Defaults require justification. A default output filename may be convenient, but overwriting an existing report unexpectedly is risky. One option is to refuse overwriting unless the caller provides an explicit flag. Another is to create a timestamped file, with a clear timestamp convention. Either can be valid depending on the intended workflow. A command-line program becomes reusable when its inputs, outputs, and exit statuses are predictable enough for a shell script or automated job to coordinate it.



## Structured Data

## Structured Data: the computational contract

**Core idea.** A list of records is not a database schema. Validate required keys, types, duplicate identifiers and missing values. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
records = [{'id':1,'score':7},{'id':2,'score':9}]
print(sum(r['score'] for r in records))
```

**Expected result:** `16`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For structured data, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Test a normal input, an empty input where meaningful, a boundary input and a malformed input. Explain whether the program should return a result, raise an exception or ask for a new value. This separates mathematical domain assumptions from interface behavior. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 3

## Write outputs that can be audited

A scientific summary should include the source filename or dataset identifier, the validation rules used, the number of accepted and rejected records, and a concise statement of the calculations. If units were converted, record the canonical units and conversion convention. When an operation is approximate, avoid displaying an unjustified number of significant digits. The output does not need elaborate graphics to be useful. A text or CSV report that clearly communicates its assumptions is better than an attractive chart that conceals the selection of observations.

To avoid partially written reports, format the entire output in memory or a temporary file and then publish it using an appropriately safe replacement strategy for the environment. Report failures during writing. If a report is meant to be reproducible across machines, record software version and relevant configuration in a lightweight metadata section. Do not rely only on a notebook's hidden execution state; the full sequence of transformations should be explicit.


## Design tests from invariants

Start with a tiny known dataset. If four accepted observations have values two, four, six, and eight in the same units, the group summary must match count four, minimum two, maximum eight, and mean five. Add a malformed row and verify that the rejected count increases according to policy without changing accepted summary values. Add a duplicate ID and verify that the chosen duplicate policy is honored. Add an input file containing only invalid rows and ensure the program does not invent a mean.

Several properties support broader testing. The count of accepted plus rejected rows should equal the total rows processed, if each input row is classified exactly once. Every reported minimum should be less than or equal to every accepted value in its group, and every maximum should be greater than or equal to every accepted value. For a nonempty set of finite values, the arithmetic mean should lie between its minimum and maximum. These properties are useful independent checks, although they do not prove that the file parser assigned values to the right groups.



## Command-Line Programs

## Command-Line Programs: the computational contract

**Core idea.** Command-line parsing turns textual flags into typed settings. Provide help text, actionable errors and reproducible invocation examples. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--scale',type=float,default=1.0)
# args = parser.parse_args()
# print(args.scale * 10)
```

**Expected result:** `10.0 with default scale`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For command-line programs, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Compare readability, asymptotic work and memory use with a plausible alternative. For small datasets, clarity may dominate micro-optimization. For huge datasets, count the operations rather than relying on a vague claim that one language construct is faster. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 4

## An end-to-end failure rehearsal

Imagine the input file is readable and valid, but the output directory is read-only. A program might calculate all summaries successfully and then fail to save the report. The final user-visible result should distinguish completed computation from failed delivery. If the tool prints `report saved` before the file operation, its status is misleading. Perform the write, verify the operation returned successfully, and only then report the path. If exact durability matters, investigate the storage guarantees rather than assuming a successful language-level write proves that the data will survive a power loss.

Now imagine the tool is run twice with the same input. Its numerical summary should be the same under a deterministic processing policy. If the output filename includes the current date or time, the filenames may differ without implying that the analysis changed. If random sampling is added, a recorded seed and a documented random-number generator help reproducibility, but they do not remove sampling uncertainty. The report must separate deterministic computation from stochastic estimation so that repeated runs are interpreted correctly.


## Integrate, but retain component tests

Once the full pipeline works, keep the parser, validator, statistics, and formatter tests. End-to-end tests are useful for verifying wiring, but they can be slow and may be harder to debug when something fails. Component tests identify whether a problem lies in arithmetic, schema interpretation, or presentation. At the same time, component tests alone cannot prove that relative file paths, module imports, and command-line arguments interact correctly. A balanced test suite combines both forms of evidence and gives each one a distinct purpose.

Refactoring should be guided by duplicated responsibilities, hidden state, and difficult-to-test behavior rather than a desire to add more classes. If one function both parses text and writes an email, separating responsibilities may be beneficial. If a simple mean function is already pure, small, and clear, wrapping it in a class may add no value. Architecture is judged by how well it makes changes and failures manageable, not by the number of layers it contains.


## Final review rubric

Before regarding the program as usable, answer five questions. First, can an unfamiliar reader explain what valid input means? Second, can the reader trace how each input row contributes to the output? Third, are errors reported clearly without silently altering data? Fourth, are representative outputs checked independently rather than compared only with the same code? Fifth, can the program be run again with the same documented settings to reproduce the result? A negative answer identifies a concrete improvement to make before broader deployment.

The completed laboratory demonstrates the progression from computational thinking to a functioning data workflow. Variables represent distinct types of values, control flow maintains invariants, functions enforce contracts, data collections preserve chosen properties, external operations manage failures, and tests provide evidence about behavior. These skills remain useful when projects become larger. More complex tools add performance and concurrency concerns, but they do not replace the need for clear meaning, explicit assumptions, and independently checkable results.


### Count tokens in a string and discuss punctuation policy.

**Split**
A basic whitespace split of "A, a a." yields three tokens including punctuation differences.

**Normalize**
To count a consistently, choose explicit lowercasing and punctuation removal rules; under simple stripping, a has frequency 3.

**Scope**
Real text requires Unicode normalization and language-specific tokenization; document the limited tokenizer.

### Approximate integral from 0 to 1 of x squared using the trapezoid rule with four panels.

**Formula**
h=(1-0)/4=0.25 and T=h[(f0+f4)/2 + f1+f2+f3].

**Calculate**
Values are 0,0.0625,0.25,0.5625,1. Interior sum=0.875 and endpoint half-sum=0.5.

**Result**
T=0.25·1.375=0.34375. Exact integral=1/3≈0.333333, so absolute error≈0.0104167.

### Validate records before summing their numeric scores.

**Schema**
Require each record to include unique id and finite numeric score; reject booleans when numeric scores are required.

**Computation**
For records {id:1,score:7} and {id:2,score:9}, the sum is 16.

**Tests**
Test missing score, nonnumeric score, duplicate id and empty collection. Decide whether an empty list is valid and document the result.


### Applied investigation: Text processing and numerical integration

A basic text tokenizer must define which characters count as separators and whether case folding, Unicode normalization and punctuation removal are applied. Splitting on whitespace only will leave commas and apostrophes in tokens. For an academic search utility, normalizing terms consistently at indexing and query time is essential. A count of tokens is only meaningful when the tokenization policy is explicit.

The trapezoidal rule approximates a definite integral by summing areas beneath straight-line segments between sample points. The approximation converges under standard regularity assumptions as the step shrinks, but an oscillatory or sharply curved function can require finer spacing. For f(x)=x² on [0,1], the exact integral equals 1/3. One trapezoid gives 1/2, while two equal trapezoids give 3/8. Comparing those numerical values tests the implementation and illustrates decreasing discretization error without pretending every function behaves identically.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.
