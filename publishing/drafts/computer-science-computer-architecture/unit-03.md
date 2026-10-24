# Computer Architecture — Unit 3: Processor datapaths

## 3.1 Arithmetic Units

**Core model — Arithmetic Units**

An arithmetic logic unit computes a selected operation on bit vectors. Correct behavior distinguishes signed from unsigned comparison, carries and overflow flags.

**Original worked illustration**

For unsigned 8-bit values, 250+10 produces result 4 and carry 1. For signed two's complement, the same bits represent -6+10=4 with no signed overflow.

**Boundary conditions and checks**

Carry and signed overflow are different signals; testing only the output low bits misses errors in arithmetic-status reporting.

### Extended technical chapter: Arithmetic Units

The arithmetic logic unit transforms operand bit patterns into a result and, in many designs, associated condition flags. At a conceptual level, one full-adder stage accepts two operand bits and an incoming carry and produces a sum bit and outgoing carry. Cascading stages yields a ripple-carry adder, but the longest path grows with word width because carry information may travel through every bit position. More advanced adders rearrange the carry logic to reduce critical-path delay at the expense of additional gates, wires, or power. This is an architectural tradeoff because increasing the speed of one component may require more silicon area or energy.

A four-bit example makes the timing dependency visible. Compute binary 1011+0110. At bit zero, 1+0 produces sum one and carry zero. At bit one, 1+1 produces sum zero and carry one. At bit two, 0+1+carry produces sum zero and carry one. At bit three, 1+0+carry produces sum zero and carry one, so the low four-bit result is 0001 with carry-out one. The unrestricted sum is seventeen. Under unsigned four-bit interpretation the result has overflowed. Under signed four-bit interpretation, the operands are −5 and +6 and the result +1 is representable; a signed overflow flag should not fire. Flags therefore depend on meaning, not merely the internal addition network.

Multiplication and division introduce more complex latency and resource decisions. A simple shift-and-add multiplier can reuse arithmetic hardware across cycles; a fully parallel multiplier consumes more gates but supports a different throughput target. An integer multiplier's output may be twice the operand width if the full mathematical product must be retained. Floating-point arithmetic adds rounding, exceptional values, and non-associativity under finite precision. A verification exercise should test zeros, one-hot operands, maximum positive and minimum negative signed values, and random vectors against an independent mathematical model. State exactly when the hardware truncates output, since a test oracle that silently performs unbounded arithmetic will report apparent failures that are really mismatched contracts.

## 3.2 Register Files

**Core model — Register Files**

A register file provides named storage locations and read/write ports. Throughput can be limited by port conflicts even when an arithmetic unit is fast.

**Original worked illustration**

A simple three-operand instruction reads r2 and r3 and writes r1; a two-read-one-write register file can support the access pattern in one idealized cycle.

**Boundary conditions and checks**

Architectural registers are not identical to physical renamed registers in out-of-order CPUs; bypass paths affect timing.

### Extended technical chapter: Register Files

A register file provides a small, fast set of architecturally or microarchitecturally visible storage locations. The implementation must accommodate the instruction issue width and operand access pattern. A single-issue integer datapath may require two reads and one write each cycle for a common three-register operation. A wider superscalar design might require more read and write ports, and multiported storage becomes expensive in area and routing. Register renaming can map a limited set of architectural register names onto a larger pool of physical registers, removing false dependencies while retaining the programmer-visible abstraction.

For a simple synchronous register file, write timing matters. Suppose instruction A writes register r5 on a rising edge, while instruction B reads r5 during the same cycle. A teaching simulator must say whether the read sees the old value, the new value, or forwarded data from another datapath point. These alternatives may be implemented by different circuits. A timing diagram with half-cycle assumptions often clarifies what a vague statement such as 'register updated this cycle' conceals. Zero registers in some ISAs ignore writes by specification; treating such a register like ordinary storage corrupts the architectural state model.

A register is not equivalent to a cache line. Registers are individually named by instructions; cache capacity, association and replacement govern memory data accessed by addresses. Compiler register allocation decides which live variables can stay in architectural registers and which must spill to memory. Pressure grows when many values are simultaneously live, particularly across calls. An experiment can start with a short instruction trace containing RAW dependencies, renames, and one spilled value. Record the live range of each value, the register contents at each step, and the additional loads and stores needed under a smaller register budget. This connects physical port design, instruction scheduling, and compiler decisions without pretending that register count alone determines application performance.

## 3.3 Control Logic

**Core model — Control Logic**

Control logic interprets instruction fields into datapath control signals. Hardwired and microprogrammed controllers make different implementation tradeoffs.

**Original worked illustration**

A load instruction typically selects base+offset in an address adder, requests memory read, and writes returned data to a register. A store routes source-register data to memory write instead.

**Boundary conditions and checks**

Incorrect control sequencing can write a stale result even if all arithmetic blocks are individually correct.

### Extended technical chapter: Control Logic

A processor's control logic maps decoded instructions and the current execution state into steering signals for the datapath. A textbook single-cycle machine may express its controller as combinational logic: opcode and function bits determine which register indices to read, whether the ALU should add or compare, whether memory is accessed, and whether a register write occurs. A multicycle design introduces states so that instruction fetch, decode, execution and writeback can reuse hardware over several clock periods. The two arrangements may implement the same ISA despite different timing and control circuits.

A control table is more reliable than a paragraph saying an instruction 'uses the ALU.' For a register-register addition, ALU sources come from two registers, the operation is addition, register write is enabled, and memory write is disabled. For a store, the ALU computes an effective address, memory write is enabled, and the destination-register write is disabled. For a conditional branch, a comparison and branch-target selection update the program counter only when the condition holds. Every instruction should have a defined behavior for signals it does not use; leaving a dangerous memory-write signal effectively unconstrained is a correctness bug, not merely an untidy design.

Timing and verification become important when a controller contains a finite-state machine. Enumerate each state, legal incoming transition, output control word, and condition for advancement. Test what happens following a reset, an illegal instruction encoding, a stall, and an exception. A control path that updates memory twice after a stalled store can produce a visible error even though every individual arithmetic signal is correct. Hardware descriptions should make incomplete assignments and unintended storage explicit; combinational logic typically requires outputs to be assigned on all branches. In an educational design, model control before connecting it to the datapath, then assert that forbidden simultaneous actions never occur.

## 3.4 Instruction Execution

**Core model — Instruction Execution**

Instruction execution includes fetch, decode, operand acquisition, execution, memory access and writeback as applicable. Different instruction types traverse different subsets.

**Original worked illustration**

A register-only ADD need not access data memory, while a LOAD needs an effective address and read response before architectural writeback.

**Boundary conditions and checks**

A pedagogical five-stage diagram is a model, not a universal literal description of superscalar, microcoded or variable-latency processors.

### Extended technical chapter: Instruction Execution

Instruction execution is a sequence of state transformations: fetch instruction bytes using the program counter, decode the operation and operands, read required state, perform computation or effective-address generation, access memory when applicable, and commit architectural results. The familiar five-stage description is one possible decomposition, not an ISA requirement. Some instructions complete in very few internal steps; others decompose into many micro-operations. The central correctness condition is that the externally visible result matches the architectural instruction sequence, including defined exception and memory behavior.

Trace a load followed by an addition. Initially r1=0x1000 and memory at address 0x1008 contains 12. The load calculates the address r1+8, obtains 12 from memory after translation and hierarchy access, and places it into r2. The following add r3,r2,5 writes 17. In a pipelined implementation, the second instruction might decode before the first has written r2 back to the register file. Forwarding or stalling must prevent it from using the old r2. In a non-pipelined abstract interpreter, sequencing is simpler, but the architectural result should still be seventeen. Architectural equivalence does not imply identical timing.

Precise exceptions complicate the story. If the load faults on an inaccessible page, the machine must provide the documented exception semantics, generally without allowing a younger instruction to retire a result that should not exist after the fault. Speculative execution may have performed internal work on the younger instruction, but retirement rules preserve architectural order. Draw a short trace with program counter values, operand reads, ALU outputs, memory effects and writes. Then introduce a fault and state which updates are permitted to become architectural. This prepares the ground for understanding reorder buffers, branch speculation, memory ordering, and side-channel boundaries in later units.

### Integrated laboratory: from instruction semantics to a testable datapath

Build an abstract thirty-two-bit datapath with a register file, one ALU, an instruction decoder, a program counter and a small memory interface. The initial instruction subset contains ADD, XOR, LOAD, STORE and a conditional branch. The reference model is a sequential state transition that updates architectural state one instruction at a time. Begin by writing an instruction table: each row names its source registers, destination register if any, ALU function, memory action and program-counter rule. The table acts as a specification for the control logic. A signal combination that accidentally enables both a register write and a store can now be identified as an error rather than explained away as an implementation detail.

The ALU's fixed-width behavior must be explicit. When it adds hexadecimal FFFFFFFF and 00000001, the low 32-bit result is zero and a carry-out occurs for unsigned arithmetic. Interpreting the first operand as signed gives negative one, so the signed mathematical sum is zero with no signed overflow. Feed the ALU random operand pairs and compare its low result with (a+b) modulo 2^32. Separately compute the expected signed-overflow flag from operand and result signs. This independent oracle catches a frequent flaw in student designs: using carry-out as the signed-overflow flag. Extend the test to subtraction, zero detection and comparison, documenting which flags each operation is permitted to alter.

Now analyze register-file timing. Suppose one instruction writes r3 on the rising clock edge and the next instruction reads r3 early in its own decode stage. The result depends on the defined pipeline scheduling and whether forwarding is implemented. A single-cycle model might read all operands and write at the end of a cycle, whereas a multicycle design may have an explicit writeback state. Avoid relying on ambiguous phrases such as 'the value is ready during the cycle.' Annotate availability points at clock boundaries or at specified combinational outputs. The design should also define register zero if the ISA includes one: attempted writes may be discarded, and reads always return zero.

Control-path testing benefits from adversarial inputs. After reset, the program counter must start at the defined location and no stale write-enable signal may perform a store. For an unrecognized opcode, the implementation may raise an illegal-instruction exception or enter a defined trap state; it must not execute a random mixture of bits as a valid instruction. A memory stall should prevent the same store from committing twice. A branch-taken decision should replace the sequential next program counter while respecting any documented alignment rule. These are behavioral properties that can be expressed as assertions over state and control outputs, not simply observed in one preferred waveform.

Test a five-instruction program: load the value 12 from a mapped address into r2; add five into r3; store r3 into a result address; compare r3 to 17; branch to a success label. With correct initial state, the stored value is seventeen and the success path is selected. Change the loaded value to eleven: the stored result becomes sixteen and the branch should fall through. Inject a fault on the load: neither the later store nor branch should architecturally commit if the specified exception model is precise. Compare committed state after each instruction with the sequential reference interpreter. This is more meaningful than merely showing that a clock signal toggles.

For evaluation, record coverage by instruction class, operand boundary, control state and memory condition. A design that passes ten ordinary additions but never exercises a taken branch or an invalid address has weak evidence of correctness. Include reset during a pending memory transaction and explain what the model chooses to guarantee. Finally, discuss cost: additional forwarding paths or multiple ALUs can improve throughput but alter control complexity, timing and energy. Datapath design is a negotiation among correctness, cycle time, throughput and implementation resources, all under one architectural contract.

### Review lens: architectural state versus internal state

Two processor implementations can be architecturally equivalent while their internal states differ radically. One may use a single-cycle controller, another an instruction pipeline and a third a reorder buffer with speculation. A conformance test compares the committed register values, memory effects and exceptions mandated by the ISA. It should not require speculative instructions to occupy the same transient buffers or produce the same internal waveform. This distinction also imposes discipline on performance models: a fast ALU alone does not establish a fast processor if decode, cache access or retirement is the bottleneck. When a test fails, capture the first instruction whose committed outcome diverges from a reference model. Tracing the earliest divergence is typically more informative than comparing the final register dump after many incorrect operations. Only after correctness is established should cycle count become the optimization metric.

### Additional guided investigations for state-machine hardware

**Adder verification.** For a four-bit unsigned adder, test operands 15 and 1. Their mathematical sum sixteen produces low nibble zero and carry-out one. Test operands seven and one under signed four-bit interpretation: seven plus one yields bit pattern 1000, interpreted as negative eight, so signed overflow occurs despite an ordinary bit-level sum. Design separate assertions for carry and signed overflow. A correct testbench should generate expected results using wider mathematical integers instead of copying the same combinational logic used inside the circuit.

**Register-file verification.** Give two instructions the same destination architectural register but distinct computed values. If the first writes nine and the second writes fourteen, a third instruction must observe fourteen after both retire. In an out-of-order or forwarded design, blindly choosing the oldest bypass source could return nine. Draw a priority network that chooses the most recent valid producer. Also test write-enable false, destination zero if reserved, and simultaneous read and write behavior according to the explicitly declared register-file timing contract.

**Controller verification.** Define control signals RegWrite, MemRead, MemWrite, Branch and ALUOp. For a STORE, expect MemWrite enabled, register write disabled and an address-generation ALU operation. For an ADD, expect register write enabled and both memory read and write disabled. Build a truth table for each legal opcode, then test an illegal encoding. The illegal state must invoke the specified trap behavior rather than combining leftover control values from a previous instruction. This is especially important in finite-state controllers with stalled transactions.

**Architectural trace verification.** Initialize memory[1008]=12 and r2=1000. Execute LOAD r1,[r2+8], ADD r3,r1,5 and STORE r3,[r2+12]. Sequential architectural results are r1=12, r3=17 and memory[1012]=17. Inject an exception into the load and assert that the later store does not become architecturally visible under the chosen precise-exception model. Check the final memory independently of internal ALU waveforms, since two different microarchitectures should preserve the same visible contract.

### Diagnostic challenge: choose the correct output flag

An eight-bit ALU adds 01111111 and 00000001. The mathematical unsigned sum is 128, within the range zero through 255, so there is no unsigned carry-out. But as signed operands, 127+1 overflows the signed maximum of 127, and the resulting pattern 10000000 denotes −128. Now compare 11111111+00000001. It creates carry-out one and low-byte result zero, yet as signed values −1+1=0 causes no signed overflow. A testbench that equates these two flags fails one of the cases. Build a truth table using operand sign bits and result sign bits, and verify the signed overflow rule for addition: overflow occurs when operands have the same sign but result has the opposite sign. Add subtraction cases separately because borrowing and subtraction-overflow definitions need their own logic. This exercise forces a design to specify the interpretation of output flags rather than deriving them from ambiguous English descriptions.

## Three worked problems

### Arithmetic Units: worked application 1

Compute unsigned 8-bit sum 250+10 and carry flag.

**Set up the model and conditions**

Arithmetic result is 260, exceeding maximum unsigned 8-bit 255.

**Carry out the calculation or proof**

Low eight bits are 260 mod 256=4; a carry out occurs.

**State the result and its scope**

Stored result is 4 and carry flag is one.

**Independent verification, conditions, and interpretation**

Unsigned eight-bit addition computes 250+10=260 as an unrestricted integer. Since an eight-bit output can store residues from zero through 255, divide 260 by 256: quotient one and remainder four. The low eight bits therefore contain 00000100, and unsigned carry-out is one. Check this by converting 250 to 11111010 and ten to 00001010 and performing column addition. The higher carry is not stored in the low-byte result. Signed arithmetic interprets the same bit pattern 11111010 as −6; −6+10=4 is representable, so the signed-overflow flag should be zero even though unsigned carry-out is one. This contrast catches the common error of using one flag as a universal indication of arithmetic overflow. If the program requires exact mathematical 260, it must use a wider result, detect the carry or apply appropriate saturation. If the ISA provides a narrowing conversion, its specified semantics determine whether the high bits are silently discarded. The answer is complete only when it states both the low output and the carry convention.

### Register Files: worked application 2

A register-file design has two read ports and one write port. Can a simple three-register add read two operands and write a result in one ideal cycle?

**Set up the model and conditions**

A three-register ADD needs two source values and one destination update.

**Carry out the calculation or proof**

Two read ports satisfy the source accesses; one write port satisfies the result update.

**State the result and its scope**

Yes, provided timing and writeback policy allow those accesses in the model.

**Independent verification, conditions, and interpretation**

A conventional ADD rD,rA,rB consumes two source values and produces one destination value. A register file offering two independent read ports and one write port has the port count needed to support these three logical accesses in an ideal cycle. That fact alone does not guarantee the complete instruction finishes in one clock period. Decoder time, register read delay, ALU propagation, write setup and the architectural timing model must also fit the cycle budget. In a pipelined machine, reads might occur during decode and writes several stages later; simultaneous accesses from different instructions can increase port demand. If the program writes and reads the same register in one cycle, the design must define or resolve read-during-write behavior. Bypass paths can supply the newly computed value without waiting for writeback. The answer therefore has two layers: port counts suffice for one isolated register-register add under the assumed model, but timing and surrounding traffic can require further resources or scheduling. An adequate testbench uses two distinct sources, identical-source operands, destination equal to a source, and a suppressed write to a reserved register if the ISA defines one.

### Control Logic: worked application 3

For LOAD r1,[r2+8], identify address, memory and writeback stages.

**Set up the model and conditions**

Read base register r2 and compute effective address r2+8.

**Carry out the calculation or proof**

Issue a memory read and wait for returned data under memory timing rules.

**State the result and its scope**

Write the loaded value into r1; an ordinary ALU-only instruction does not need this data-memory read.

**Independent verification, conditions, and interpretation**

For LOAD r1,[r2+8], the effective address is computed by an addition involving r2 and the immediate displacement eight. The memory stage reads the data found at that address after required translation and access checks. The retrieved value is written into r1 during architectural writeback. A register-register arithmetic instruction may also use the ALU, but it does not need to read data memory simply because it has an execute stage. Distinguish instruction fetch, which reads the instruction stream, from a data-memory access performed by LOAD. If r2=1000 and memory at address 1008 contains 23, a correctly executed load leaves r1=23. If that location is unmapped, the defined fault behavior replaces the normal writeback, so the example cannot assume r1 changes. With a pipelined implementation, loaded data may appear late enough that a subsequent ADD depending on r1 must stall despite bypassing. A precise explanation labels address generation, translation/protection, data access, and register commitment separately. Conflating these stages is the root of many incorrect datapath sketches.
