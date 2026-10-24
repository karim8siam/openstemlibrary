# Unit 7: Code generation

*Draft; not approved for public deployment. Eight-unit manuscript with source-specific cases and independent verification pending.*

## Instruction Selection
**Instruction Selection: conceptual explanation**

Instruction selection chooses target instructions that implement the intermediate representation’s operations. A RISC target may require explicit load, arithmetic and store operations, while a CISC target may support arithmetic with memory operands. One IR expression can admit several instruction sequences with different code size, latency and register pressure. Tree-pattern matching covers basic blocks of expression trees; DAG matching and global selection can exploit common subexpressions but become more complex when dependencies or flags matter. The cheapest-looking instruction in isolation may be globally expensive when it clobbers a condition-code register or requires additional moves.

Consider an IR sequence `t1 = a*2; t2 = t1+b`. A target with an addressing form or shift-add instruction might implement it without a general multiplication. But the selected instruction must have identical overflow and signedness behavior. If a target instruction sets status flags that a later branch reads, the compiler must model that effect explicitly. Analyze instruction candidates by listing preconditions, defined outputs, clobbers, implicit operands and scheduling constraints. Then compile a small corpus of arithmetic expressions, inspect assembly and confirm behavior against the IR interpreter. Code size and performance are empirical properties; semantic equivalence is a correctness obligation.

### Design investigation: select equivalent instructions
Given IR operations `t=2*x+y`, generate two legal target sequences: an arithmetic shift plus add, and a multiplication by immediate two plus add. Determine whether both preserve signed overflow and whether the target uses the same integer width. If an addressing instruction computes `base+index*scale`, check operand constraints before replacing the arithmetic. Annotate implicit flags, clobbers and registers. For a target without a multiply instruction, show how legalization rewrites unsupported operations before selection. Validate candidate sequences with a bounded numerical input space and extreme values. An instruction’s existence in an architecture manual does not mean the deployed CPU supports every optional extension. A backend must account for feature availability explicitly.

## Calling Conventions
**Calling Conventions: conceptual explanation**

A calling convention is a protocol at a function boundary. It assigns argument and return locations, classifies registers as caller- or callee-saved, specifies stack alignment, and handles structures, varargs and hidden return pointers. A correct function body can still fail catastrophically if its prologue or epilogue violates the ABI. A compiler targeting a specific platform must cite that ABI version rather than infer rules from another CPU or operating system. Stack frame unwinding information may be required for exceptions and debugging even when the function itself never throws.

Walk through a function `f(a,b,c)` that computes a+b*c and calls a helper. Place arguments in the documented locations, save needed registers before the call, restore callee-saved state before return, and leave the stack at the required alignment. Verify return-address integrity and behavior when the helper throws. Tail calls replace a call-and-return sequence when the caller no longer needs its frame, but must respect differences between the caller and callee conventions. Cross-language calls add type layout, name mangling and ownership constraints. A foreign function that returns a borrowed buffer must not be treated as though the caller owns it automatically.

### Design investigation: ABI boundary correctness
Define a hypothetical calling convention with two argument registers and remaining arguments on the stack; one return register; and designated preserved registers. Walk through a call with three integer arguments, including where the third is stored, what the callee must restore, and how the caller retrieves the result. State that this is an invented teaching ABI rather than the actual convention of a named CPU. Then select one real documented ABI and redo the exercise based on its specification. Introduce a callback that is invoked from foreign code and verify stack alignment and saved-register preservation. Include a variable-argument call and identify extra rules or restrictions rather than assuming the fixed-arity protocol applies unchanged. Record a failing test caused by one intentionally omitted preserved-register save.

## Linking
**Linking: conceptual explanation**

A linker combines separately compiled modules into an executable or library by resolving symbols and relocations. An object file includes machine code, data, symbol information and relocation entries describing addresses that cannot be final until layout is known. For a call to `foo` defined in another object, the assembler may emit a placeholder and a relocation; the linker resolves the target symbol and adjusts the instruction encoding or creates an indirection stub if required. Undefined symbols, duplicate definitions and incompatible object formats are different errors and require precise diagnostics.

Static linking incorporates selected library content into an output artifact, while dynamic linking defers some resolution to a loader and shared-library environment. Position-independent code allows suitable sections to be relocated or mapped at different addresses using target-specific mechanisms. Symbol visibility, versioning, and link order can affect which implementation is chosen. Construct two object modules with one exported and one hidden function, plus a third module referencing both. Predict which references should resolve, which fail, and why. A successful link does not guarantee runtime compatibility: an ABI change in a shared library can corrupt calls even when symbol names remain unchanged. Record binary dependencies and check them during deployment.

### Design investigation: resolve and relocate
Create symbolic object-file records for A.o defining `f` and B.o calling `f`. Place the call at a known section offset and add a relocation referencing f. Describe how the linker computes the final address or a PC-relative displacement, including range restrictions. Add a second exported definition of f and show whether the link is ambiguous or violates a one-definition rule under your model. Add a hidden internal f in another module and explain why it need not conflict with the public symbol. Now change the dynamic library’s function signature while keeping its exported name; a name-only match can still produce an ABI error at runtime. Test link errors and ABI compatibility separately. Verify that address arithmetic uses target pointer widths and endianness, not those of the build machine.

## Target Constraints
**Target Constraints: conceptual explanation**

Target constraints include instruction width, addressable registers, alignment, endianness, vector capabilities, memory ordering and exception conventions. Little-endian and big-endian targets may store the same multibyte integer with different byte sequences; a compiler must preserve source-language values while serializing data according to the target ABI. An instruction requiring aligned operands may fault or slow down on unaligned inputs, depending on architecture. Code generation must distinguish a legal machine instruction from one supported only by an optional CPU extension.

Target information should be modeled as data rather than scattered special cases. Register sets, instruction patterns, legalization rules and scheduling information belong in a consistent backend description. Cross-compilation cannot safely run a target executable on the build machine without an emulator or remote target. Validation can inspect generated assembly and object metadata, use an emulator for small programs, and run selected integration cases on actual hardware. Concurrency raises an especially demanding issue: translating atomic source operations requires preserving the language memory model using target fences and atomic instructions. A single-threaded arithmetic test cannot establish the correctness of the backend’s concurrent code generation.

### Design investigation: verify target assumptions
Choose a target with documented stack alignment and byte order. Serialize integer 0x01020304 to four bytes and show the different byte order for little-endian and big-endian memory representations. Demonstrate why a network-format conversion cannot blindly reinterpret host memory bytes. Generate a function using an optional vector instruction, then test whether the chosen target configuration permits it. If not, the backend should legalize to supported instructions or report a controlled unsupported-feature error. Add concurrency: compile an atomic increment under the language’s memory ordering promise and describe why replacing it with plain load/add/store loses atomicity. Inspect assembly or emulator traces, and do not claim memory-model correctness from a sequential unit test alone.

## Integrated Case Study and Model Limitations
A function takes three integer arguments and returns an integer on an architecture with a documented ABI. If the compiler overwrites a callee-saved register and fails to restore it, the caller may fail only after the function returns, making the defect hard to localize. Show where arguments live before and after a call, and state who allocates the stack frame. Code generation must account for instruction encoding and address alignment. Linking then resolves the function symbol, but binary compatibility also depends on versioned layouts and calling conventions, not just a matching symbol name.

### Laboratory: from low-level IR to a linkable target object

Choose one documented target ABI, even if you initially emit pseudocode assembly rather than machine code. Specify the target’s registers, word size, stack alignment, argument assignment and return convention. Lower arithmetic instructions from the teaching IR to target operations, preserving signedness and overflow behavior. For the function `addmul(a,b,c)=a+b*c`, determine whether a multiply-add instruction exists and whether using it would preserve the required arithmetic semantics. If no single instruction suffices, emit a legal sequence and list all source and destination registers.

Construct a prologue and epilogue for a function that calls another function. Determine which live registers must be saved by the caller and which registers the callee promises to preserve. Reserve and align the stack frame correctly, then restore it along every return path. Test an exceptional exit or nonlocal transfer if your ABI/language combination supports one; otherwise explicitly exclude it. A generated function may appear correct when called only from your compiler's own output while violating a foreign caller's expectations. A small C harness or ABI conformance test provides stronger evidence than a compiler-only round trip.

Build an object-file thought experiment with two modules. Module A exports `f`, module B calls `f`, and a third source file defines a private symbol with the same spelling. The assembler can leave a relocation for B’s call; the linker resolves it to A’s externally visible symbol. The private symbol should not conflict by external linkage. Inspect a textual relocation table containing section, offset, relocation kind and target symbol. Explain why a relocation type must match the target’s address range and instruction encoding; substituting a raw absolute address into a PC-relative field is not generally valid.

Now add a dynamic library dependency and change one exported function’s ABI while keeping its public name unchanged. Source code that compiles against the new headers may run, but an old binary can misinterpret arguments or return values. Identify the versioning, visibility and compatibility policy needed to avoid accidental breaking changes. Consider 32-bit versus 64-bit integer widths, structure packing, and ownership of returned buffers. A compiler backend is not finished merely when the assembler accepts its output.

Finally design target tests with three layers. Unit-test instruction selection from small IR fragments; run generated programs under an emulator or reference VM; and test representative calls on actual target hardware when available. Add negative tests for unavailable vector instructions, invalid register classes, misaligned stack frames and oversized immediate operands. Compare outputs and side effects against the IR interpreter, not against an optimizer that shares the same lowering code. The deliverable is a documented backend contract with a traceable chain from IR semantics to machine-level effects.

### Failure clinic: correct arithmetic, broken function boundaries

A compiler's generated arithmetic function passes every local unit test. When called from a separately compiled library, the process eventually fails after returning from a function that used many registers. The backend had overwritten a register classified as callee-saved by the target ABI without restoring it. When both caller and callee were generated by the same buggy compiler, the failure was less visible because tests accidentally avoided a live value in that register. A calling convention is an external contract, not merely an internal preference.

Reproduce the problem using a foreign harness that fills preserved registers with known values, calls the generated function and verifies them after return. Add tests for stack alignment, return value location, aggregate arguments, nested calls and tail calls. Record the selected ABI document and target architecture. Do not use a hypothetical register policy while claiming conformance with a real platform. Inspect prologue and epilogue instructions and verify exceptional paths if the implementation supports unwinding.

The compiler also emits a relocation intended for a PC-relative branch as if it were an absolute address. On small test binaries, layout sometimes masks the issue, while linking a larger application causes an out-of-range target or an incorrect jump. Examine relocation type, section offset, symbol visibility, instruction encoding and addend together. A linker error about relocation range is not necessarily a bug in the linker; the compiler or assembler may have requested a relocation that cannot represent the target address.

A new version of a shared library changes a returned structure from two 32-bit fields to one 64-bit field without changing the exported symbol name. Even if the total size is the same, field layout, alignment and calling convention classification can differ. List the binary compatibility requirements and explain why source-level type-checking alone cannot protect an old consumer binary. The remedy involves ABI versioning, stable opaque handles or compatibility shims, followed by cross-version tests. Source-language semantics must survive all the way through instruction selection, frame layout, relocation and external binary boundaries.

### Worked comparative study: why target-specific correctness has layers

A correct compiler backend must translate an abstract operation into legal target instructions, then obey the ABI that surrounds those instructions. One plus one still equals two at the source level regardless of the processor, but the implementation details of signed integer overflow, stack layout, register preservation and binary relocation are target dependent. A code sequence that works as a standalone function may violate callee-saved register requirements when linked into a larger application. Conversely, a function with a correct prologue may calculate the wrong arithmetic result because the selected machine instruction interprets operands as unsigned rather than signed.

Construct three independent correctness layers. At instruction level, compare a target sequence against IR semantics for operand values including extremes and negative inputs. At function level, verify call arguments, return values, preserved registers, stack alignment and exception or unwind behavior where supported. At object/link level, validate symbol resolution, relocation types, section properties and external binary compatibility. Passing one layer does not imply another. For example, an assembler can accept a legal instruction stream whose run-time behavior violates the source's required exception ordering.

A teaching target can define its own small register and stack protocol, which is useful for learning. Label that protocol explicitly hypothetical. To target a real CPU and operating system, use the exact published ABI and instruction set supported by the deployment environment. Features such as vector instructions, atomics and unwind tables vary between target configurations. Cross-compilation additionally requires suitable emulation or hardware testing for executable behavior. A build-machine-only numeric test is not evidence that the target's calling convention works.

Compare static and dynamic library integration. Static linking resolves and incorporates selected code in one artifact; dynamic linking can defer resolution and permit shared runtime libraries. Both require compatible symbol types and binary representations. Name mangling, visibility and versioning affect interfaces. An opaque-handle API can limit the cost of internal structure changes compared with publishing raw structure layouts. A binary that links successfully may still fail when the library's calling convention or ownership rules changed. The complete verification argument must therefore reach beyond generated assembly into interoperation and deployment.

### Unit review: follow the target ABI rather than intuition

Pick a target and identify precisely which registers are caller-saved, which are callee-saved and how stack alignment is defined at a call boundary. Build a small cross-language function-call test that leaves important values live across a call. Inspect the generated prologue and epilogue, then verify relocation and symbol visibility in a linked object. A backend that passes local arithmetic tests can still violate ABI obligations, while a file that links can still use incompatible structure layouts at runtime. Repeat numerical tests with signed extremes and unavailable optional CPU features. Mark any teaching register convention explicitly as hypothetical rather than claiming it describes a named architecture.

### Worked question: Endianness demonstration
Write the byte sequence representing 0x01020304 in little-endian and big-endian memory, assuming a four-byte integer representation.

**Set up definitions and premises**
The hexadecimal integer consists of bytes 01,02,03,04 from most significant to least significant. The mathematical integer value is independent of memory byte order.

**Derive the result**
Big-endian layout places 01 at the lowest memory address, then 02,03,04. Little-endian layout places 04 first, then 03,02,01.

**Validate limits and interpretation**
Cross-platform serialized protocols need an agreed byte order; raw reinterpretation of native memory is not portable. The target ABI also determines alignment, padding and how larger structures are laid out.

**Answer:** Big endian 01 02 03 04; little endian 04 03 02 01.

### Worked question: Callee-saved registers
A caller stores an important live value in a callee-saved register before invoking a generated function. State the callee obligation and a test.

**Set up definitions and premises**
Under the documented ABI, the chosen register belongs to the set that a callee must preserve across calls. The caller may therefore assume the value will be unchanged after return.

**Derive the result**
If the function uses that register, it must restore its original value along every relevant return path. A test harness initializes the register with a sentinel, calls the function, then checks the sentinel.

**Validate limits and interpretation**
A compiler that clobbers the register may appear correct when both sides of a test do not use it simultaneously. Foreign harnesses and ABI conformance tests expose the protocol violation.

**Answer:** Restore callee-saved state before returning; verify with a sentinel caller.

### Worked question: Link symbols and relocation
Module A defines external f; module B calls f without defining it. Explain how a linker handles the reference and when it fails.

**Set up definitions and premises**
The assembler emits machine code in B with a relocation entry referencing symbol f, together with the relocation location and type. A provides a compatible externally visible definition.

**Derive the result**
At link time the symbol resolver finds A.f and computes the required address or displacement under the relocation’s target-specific rules. The linker adjusts encoded data or emits an appropriate stub when permitted.

**Validate limits and interpretation**
If f remains undefined, conflicting definitions violate rules, or the displacement cannot be represented, linking fails or requires a documented alternative. A matched name does not by itself guarantee ABI compatibility.

**Answer:** Resolve B.f to A.f and apply a compatible relocation; unresolved or incompatible references fail.
