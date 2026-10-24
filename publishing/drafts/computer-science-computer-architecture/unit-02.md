# Computer Architecture — Unit 2: Instruction sets

## 2.1 Machine Instructions

**Core model — Machine Instructions**

An ISA specifies instruction semantics rather than the physical implementation. Arithmetic, control flow, memory and system instructions operate on an architectural state.

**Original worked illustration**

An ADD r1,r2,r3 instruction in a three-register ISA means r1 gets the sum of r2 and r3; the microarchitecture may execute it with different internal datapaths.

**Boundary conditions and checks**

A particular instruction mnemonic or register set is ISA-specific; code examples are illustrative unless pinned to a named real architecture.

### Extended technical chapter: Machine Instructions

An instruction-set architecture is the contract between software and a processor implementation. It specifies programmer-visible registers, instruction encodings, operands, addressing rules, data types, and exceptions. It does not require a particular pipeline length or cache configuration. The same ISA can be implemented by a tiny microcontroller, a superscalar laptop CPU, or a teaching emulator with radically different internal hardware. Decoding instruction semantics starts from architectural state: a set of registers, a program counter, memory, and any status flags. Executing one instruction can be described as a transition from one architectural state to the next, even when the underlying implementation performs several internal micro-operations.

Consider an abstract instruction ADD r3,r1,r2. The semantic effect is r3←r1+r2 with a defined register width; all other named registers remain unchanged unless the architecture says otherwise. A load instruction instead calculates an effective address and reads the memory value residing there, which can fail if the address is invalid or not accessible. These seemingly simple transitions become important when debugging: if an instruction appears to produce the wrong output, distinguish instruction decoding, source operand selection, arithmetic, and register writeback. On a processor with precise exceptions, an instruction must not make architectural changes that violate the specified restart behavior.

Fixed-length and variable-length encodings trade off decoder complexity, program density, and compatibility. A variable-length stream can pack common operations compactly but may require additional decode work to find instruction boundaries. A fixed-length scheme simplifies some pipeline stages but might increase total code bytes for the same program. Neither format guarantees superior performance. Study a toy three-operand encoding by allocating bits to opcode, destination, and two source registers; identify the tradeoff between register count and instruction width. Compute how many distinct encodings fit in a field with k bits and distinguish syntactically possible encodings from valid documented instructions.

## 2.2 Addressing Modes

**Core model — Addressing Modes**

Addressing modes specify how operands and effective memory addresses are constructed. Common patterns include immediate, register, base plus displacement and indexed addressing.

**Original worked illustration**

If base register holds 1000 and displacement is 24, effective byte address is 1024. The instruction still needs a defined operand size and alignment.

**Boundary conditions and checks**

An effective address calculation is not a permission check: invalid or unmapped addresses can still fault after translation.

### Extended technical chapter: Addressing Modes

An addressing mode defines how an instruction obtains an operand or computes a memory address. Immediate addressing embeds a literal constant in the instruction; register addressing refers to a register; base-plus-offset addressing adds a signed displacement to a base register; indexed addressing often scales an index before addition. The precise set depends on the ISA. For array access, a base address of 0x1000, an index of seven, and a four-byte element size yield 0x1000+7×4=0x101c if the addressing mode performs that scale. This does not itself prove that the address lies inside the allocated array or that the memory reference is permitted.

Effective-address computation is separate from virtual-to-physical translation. A process can compute a valid virtual address that is not currently resident; a page-table walk or page fault handles that later. Similarly, address arithmetic may wrap in a fixed-width machine even though unbounded integer algebra would not. When reading assembly, always annotate which operands are values and which are locations containing values. Confusing the two is a recurring source of pointer bugs and security defects. A load of [r1+8] reads memory at an address; it does not merely compute r1+8 unless the instruction specifically describes an address-generation operation.

A useful experiment begins with a short trace of two loads, a store, and an arithmetic instruction. Record base registers, offsets, width, endian convention, effective addresses, memory before and after, and architectural register values. Then change one assumption at a time: use a negative displacement, move the base close to a page boundary, or increase the operand width. Explain which behavior is architecture-specific and which behavior follows directly from address arithmetic. Do not conflate the syntactic convenience of an addressing mode with a guarantee that the resulting memory access is fast; caches and page translation determine much of the actual delay.

## 2.3 Assembly

**Core model — Assembly**

Assembly turns high-level operations into explicit data movement, arithmetic and branch instructions. Calling conventions determine which registers and stack locations carry values.

**Original worked illustration**

To compute a+b in a register ISA, load a into r1, load b into r2, add into r3, then store r3. A compiler may optimize away redundant moves.

**Boundary conditions and checks**

Machine code encodings, flags and register availability vary; an invented teaching ISA should not be mistaken for production x86 or ARM syntax.

### Extended technical chapter: Assembly

Assembly language expresses a particular machine's instruction sequence using mnemonic names, labels, and directives. It exposes details compilers often hide, such as register allocation, calling conventions, memory layout, and branch targets. But assembly is not intrinsically one-to-one with machine code: assemblers may expand pseudo-instructions, choose encoding forms, resolve relocations, and emit metadata. A line labeled load-address can become several machine instructions when the address does not fit in a small immediate field. Object files preserve symbol and relocation information for a linker to combine independently compiled modules.

To read a loop, establish the initial register state, the loop invariant, the exit condition, and the effect of each iteration. Suppose a register contains an array index and a second register accumulates a sum. A correctly structured traversal should advance the index once per element, guard memory accesses with a valid bound, and update the accumulator using a width capable of representing the desired total. Assembly has no automatic array-bounds guarantee. If the loop tests after the load rather than before, it may access one invalid element even though the branch condition appears correct in isolation. Reconstruct instruction ordering, not merely arithmetic intent.

Modern compiler output is shaped by optimization, inlining, vectorization, and debug settings. A release build can omit a frame pointer or unroll a loop; a debug build may make one source statement correspond to multiple explicit memory operations. A sound exercise compares assembly for the same source compiled with two optimization settings and explains changes by observable instruction and memory effects. Avoid unsupported claims that fewer instructions always means faster. Investigate branch behavior, load dependencies, instruction-level parallelism, and code size. The real result of assembly analysis is an auditable account of what executes, not a slogan about hand-written code.

## 2.4 Calling Conventions

**Core model — Calling Conventions**

A calling convention is a contract about arguments, return values, saved registers and stack layout across a function boundary.

**Original worked illustration**

If r0 carries the first argument and r0 also carries the return value, the callee may overwrite it; a caller needing its previous value saves it first per convention.

**Boundary conditions and checks**

Ignoring callee-saved registers causes silent corruption even when the called function's arithmetic result looks correct.

### Extended technical chapter: Calling Conventions

A calling convention describes how separately compiled code communicates at function boundaries. It specifies such matters as argument registers, return-value registers, caller-saved and callee-saved registers, stack alignment, and where additional arguments reside. It is an application binary interface obligation, not a universal property of assembly language. Two functions can both be individually correct yet fail when linked if they disagree about who preserves a register. At a call boundary, preserving exactly the right architectural state allows the caller to continue with the assumptions its compiler made.

Consider a simplified convention with registers r0–r3 for the first four arguments, r0 for the result, and r4–r7 callee-saved. A function that changes r6 must save its incoming value and restore it before return. The caller must not assume r1 survives unless the convention guarantees that. When nested calls occur, an incoming argument may need to be copied to stable storage before another function overwrites caller-saved registers. An implementation can pass small structures in registers and large structures through memory; the exact convention must be consulted for the platform rather than invented from another architecture.

Stack discipline also protects debugging and exception handling. If a function subtracts space from the stack pointer, it must restore stack balance on every normal return path and maintain required alignment before calls. Unwinding mechanisms and security mitigations may impose further constraints. A laboratory should draw a stack frame and trace two nested calls with five arguments, one local array, and one preserved register. Verify at each return that the expected values, stack address, and return control state match the starting contract. Finally, discuss why calling-convention compatibility matters for foreign-function interfaces, shared libraries, and operating-system system calls.

### Integrated laboratory: encoding, calling and executing an array-sum routine

Consider a teaching ISA with 32 registers, a fixed 32-bit instruction word and separate arithmetic, load and store operations. Suppose each arithmetic instruction contains a six-bit opcode and three five-bit register indexes. Those fields consume twenty-one bits, leaving eleven bits for any additional function or modifier field. That arithmetic does not define a real ISA; it demonstrates why encoding budgets constrain instruction design. A new addressing mode requiring a full twenty-bit immediate cannot simply be added to the same encoding format without shortening or repurposing some other field, using extension words, or introducing another instruction format.

A routine sums an array of n signed 32-bit integers. Its contract is that r0 holds a base virtual address, r1 holds n, and the result returns in r0. On entry, the routine validates that n is nonnegative and that the memory region is mapped according to the caller's contract. The loop starts with index i=0 and accumulator a=0. At each iteration, it calculates effective address base+4i, loads one 32-bit value, adds the value to a in an appropriately wide accumulator, then increments i. The invariant after k iterations is a = sum of the first k elements and i=k. The loop exits when i=n. This invariant both documents the intent and identifies common implementation mistakes: incorrect element scaling, missing range check, and incrementing the index before the first load.

Trace a three-element array [5, −2, 9] beginning at virtual address 0x2000. Address calculations yield 0x2000, 0x2004 and 0x2008. If the machine is little-endian, an element −2 represented as 0xFFFFFFFE appears in memory as FE FF FF FF, but the loaded register value is still the signed integer −2 once the bytes are interpreted according to the instruction semantics. The running sums are five, three and twelve. The instruction trace should annotate address arithmetic separately from integer addition so that a student's use of the wrong scale factor is easy to see. It should also show which memory accesses cross page boundaries if the base is moved near the end of a page.

The function calls a helper routine to check the buffer length. Under a fictional convention, r0–r3 are arguments, r0 is the return value, r4–r7 are callee-saved, and the stack must be aligned to sixteen bytes before calls. If the summation routine keeps a persistent array index in r4, it must restore the incoming r4 at return. If it stores the loop accumulator in r1 and calls the helper, it must assume r1 can be overwritten unless the convention says otherwise. A caller-save strategy or a move to a preserved register avoids accidental corruption. An ABI bug can remain latent when the helper happens not to touch a register in a particular build; correctness comes from obeying the contract, not lucky traces.

Observe the assembly produced by an optimizing compiler, but do not insist on a single source-to-instruction mapping. The compiler may use a scaled-address load, combine arithmetic with address generation, unroll iterations, or vectorize. If the reference language requires overflow checks or has undefined signed overflow, the compiler's allowed transformations depend on those semantics. Preserve test inputs that include maximum and minimum signed values and arrays of lengths zero and one. A precise comparison verifies the whole function's result or documented error, then separately investigates how the code is implemented.

The final notebook contains an encoding diagram, a register-state table, a three-iteration memory trace and a call-stack diagram. Include an error case where the routine crosses into an unmapped page: the architectural result is an exception or defined error-handling path, not an arbitrary sum. Then compare the simple architecture-level interpreter with a simulated pipelined execution. Their cycle counts may differ, but their committed visible results should agree. This distinction is the foundation for treating an ISA as a stable software contract across changing hardware.

### Review lens: what does binary compatibility actually promise?

Binary compatibility generally promises that valid programs targeting a documented ISA and ABI continue to receive specified architectural behavior. It does not promise identical instruction throughput, identical cache observations or identical power consumption on each CPU generation. A function compiled for one ABI might link successfully yet fail after an undocumented calling-convention assumption is violated. Likewise, a manually written load instruction may be syntactically valid but still fault at runtime because its address is unmapped. A useful systems boundary diagram therefore distinguishes assembler, object-file format, linker, loader, ISA, ABI, operating-system mapping and microarchitecture. Each stage owns different guarantees. When debugging, locate the failed guarantee before modifying instructions. Increasing clock frequency does not repair an ABI bug, and rewriting the assembler cannot by itself make an invalid address safe. The discipline is to isolate semantic correctness from execution speed.

### Additional guided investigations for instruction-level contracts

**Encoding investigation.** A hypothetical 24-bit instruction allocates six opcode bits, four bits for a destination register, and four bits each for two sources. Six bits remain. Determine that four register bits address sixteen registers; if an instruction needs an arbitrary twelve-bit immediate as well, the existing fixed layout cannot accommodate all fields simultaneously. Propose a separate immediate format or a sequence of instructions. Explain how expanding opcode space can reduce room for other fields, and why binary compatibility constrains future encoding changes.

**Addressing investigation.** A base register contains hexadecimal 0x2FE0 and an instruction uses displacement 0x30. The effective address is 0x3010, which crosses a 4 KiB page boundary from virtual page two into page three. If an instruction reads eight bytes starting at 0x2FFC, the access spans two pages, with each page subject to mapping and permission rules. It is not enough to check only the first page. Decide how the teaching ISA reports an invalid second page without incorrectly committing a partial architectural store.

**Assembly investigation.** An array starts at address 4096 with four-byte elements. The loop loads indexes zero, one and two from addresses 4096, 4100 and 4104. If the loop increments its pointer by one byte instead of four, the next accesses overlap parts of earlier elements and may return meaningless values. Prepare a register trace demonstrating the bug. Then rewrite the loop invariant in terms of byte addresses rather than element indexes; this makes the scaling contract visible and allows a simple proof that each intended element is visited once.

**Call-boundary investigation.** The caller holds a loop counter in caller-saved r1 and a configuration pointer in callee-saved r5. It invokes a helper that uses r1 as a scratch register and modifies r5 after saving it on the stack. On return, the caller must reload its original counter if still needed, while the callee must restore r5. Ask which function is at fault if the old r1 value is lost after an unsaved call. Then check that stack alignment and restoration remain correct on an early-return error path.

### Diagnostic challenge: interface contract across separate modules

A compiled caller passes two 32-bit numbers in r0 and r1 and expects their sum in r0. An assembly callee reads both values, computes the sum, and returns, but also destroys a register designated callee-saved. A trivial single call may pass a numeric test while corrupting the surrounding program. Design a reference scenario in which the caller keeps the address of a live object in that preserved register, invokes the function, then dereferences the object. The error surfaces only after return, so source-level debugging might incorrectly blame the dereference rather than the earlier ABI violation. Fix the callee by saving and restoring the register or avoid modifying it. Add a second test where the two inputs have a sum outside the 32-bit signed range, forcing the test contract to specify overflow behavior. A cross-module function is correct only when both its numerical result and its preserved machine state meet the ABI, with stack alignment and exception paths documented.

## Three worked problems

### Machine Instructions: worked application 1

For a base-plus-offset address, base=1000 and displacement=24. Compute the effective byte address.

**Set up the model and conditions**

Add the signed displacement to the base register.

**Carry out the calculation or proof**

1000+24=1024.

**State the result and its scope**

The effective address is 1024, before translation/protection checks.

**Independent verification, conditions, and interpretation**

Base-plus-offset addressing computes an effective address from a register value and a displacement. In the abstract example, base equals 1000 and displacement equals 24, so the effective byte address is 1024. This is an arithmetic result, not a statement that virtual address 1024 is accessible. If the underlying system uses virtual memory, address translation and permission checks follow according to its memory architecture. If the referenced operand is four bytes wide, the access spans bytes 1024 through 1027. Whether unaligned access is permitted depends on the ISA and memory type. A useful independent check subtracts the base from the expected address: 1024−1000=24, which recovers the supplied displacement. With a negative displacement of −24, the effective address would be 976, provided the arithmetic is defined. In real code, base-plus-offset forms are common for reading structure fields and stack-frame variables. The study point is to keep operand address, the stored operand value and eventual physical memory location separate. None can be inferred from the others without additional mappings and state.

### Addressing Modes: worked application 2

An instruction ADD r1,r2,r3 runs with r2=7 and r3=9. Find architectural state change.

**Set up the model and conditions**

Read the two source register values 7 and 9.

**Carry out the calculation or proof**

Compute integer addition 7+9=16.

**State the result and its scope**

Write 16 into r1; r2 and r3 remain unchanged.

**Independent verification, conditions, and interpretation**

A three-register add uses architectural register values as operands. Given r2=7 and r3=9, the instruction ADD r1,r2,r3 computes 7+9=16 and writes that result to r1, subject to the defined register width. The source registers retain their values because the specified instruction has no write to them. If r1 initially held 99, its old value is replaced by sixteen; its initial contents do not enter this computation. A sequential reference model can represent the transition as new_state = old_state except r1←16 and program-counter advancement. For a fixed eight-bit width, sixteen is representable in signed and unsigned conventions and no overflow arises. Change r2 to 250 and r3 to ten to expose modular truncation and interpretation rules rather than relying on this easy case. A correct pipeline implementation must eventually retire the same architectural result, even if the physical ALU computes it in an earlier stage. The distinction between register writes, physical rename entries and architectural retirement becomes important in speculative designs. Do not confuse a source register index with a memory address.

### Assembly: worked application 3

In an example ABI, r0 is caller-saved and r4 callee-saved. Which function protects each register?

**Set up the model and conditions**

Caller-saved means caller must preserve its own needed r0 value across the call.

**Carry out the calculation or proof**

Callee-saved means the called routine must restore r4 if it modifies it.

**State the result and its scope**

The responsibilities are caller for r0 and callee for r4.

**Independent verification, conditions, and interpretation**

Caller-saved and callee-saved register rules distribute the obligation to preserve values across a function boundary. For caller-saved r0, the caller must protect its live value before invoking another function if it expects to use the old value afterward. This can mean copying the value to a callee-saved register or storing it on the stack. For callee-saved r4, any callee that changes r4 must save its incoming value and restore it before returning. A callee that never touches r4 may not need to save it at all. These rules are designations in a fictional ABI for the question; actual platforms differ. Suppose the caller keeps an important index in r0 and then calls an I/O helper. If the helper uses r0 to return a status code, the original index is lost unless the caller saved it. Suppose the helper temporarily uses r4 instead: it must restore r4 as part of returning normally. The contract ensures separately compiled functions can cooperate without inspecting each other's implementation. Correctness also requires stack alignment, return-address handling and special exception-unwinding obligations where documented.
