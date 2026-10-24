# Operating Systems — Unit 1: OS organization

kernels; system calls; protection domains; resource abstractions

## §1.1 Kernels

**Core model — Kernels**

A kernel mediates protected access to hardware, schedules execution and provides abstractions such as processes and files. Monolithic, modular and microkernel organizations differ in which services execute in privileged mode.

**Original worked illustration**

A user program requesting a file read passes through a system-call interface into kernel-managed file and device layers rather than directly controlling an untrusted disk controller.

**Boundary conditions and checks**

Kernel privilege is not a guarantee of bug-free behavior; large trusted codebases enlarge the impact of a kernel memory-safety error.

### Kernel responsibilities as enforceable invariants

The kernel is not simply a library that happens to sit near the hardware. It is part of the trusted computing base: code that determines whether an unprivileged process may access a device, memory mapping, file, timer, or network endpoint. The critical distinction is authority. A normal library can assist a program, but cannot safely prevent a malicious program from bypassing a check if the machine allows that program to execute arbitrary privileged instructions. Hardware privilege modes and memory translation make the boundary enforceable. A system call is a controlled transition across that boundary, not an ordinary function call with a different name. An application may propose an operation; the kernel checks whether it is legal in that process's identity and resource context.

Kernel design is therefore an exercise in balancing failure domains, performance, and operational simplicity. A monolithic kernel may put networking, drivers, file systems, and scheduling in one privileged address space. A microkernel attempts to keep a smaller privileged core and move many services into separate protected processes. Neither name alone establishes reliability. A buggy privileged driver may compromise a large monolithic system; a microkernel service can also contain vulnerabilities, and messages between services introduce more boundary crossings and complicated recovery paths. Modular organization means code can be loaded or replaced in modules; it does not automatically separate the module's authority from the kernel's. Evaluate designs by the concrete location of privilege, message and memory-copy costs, fault containment, testability, and upgrade strategy.

Consider a keyboard driver that erroneously writes outside its allocated buffer. If it executes with unconstrained kernel privileges, one mistake may corrupt unrelated privileged state. If it runs in a suitably confined user-mode service, a comparable error might terminate that service without corrupting the scheduler, though it can still interrupt input and require recovery. The containment argument depends on actual hardware-enforced permissions and exposed interfaces, not whether the implementation calls itself a service. Use a threat table with three columns: untrusted actor, protected resource, and mechanism enforcing isolation. Distinguish a software convention from a hardware-enforced boundary in each row. A useful experiment is to draw the path of a keypress through interrupt handling, driver queues, input routing, and user-space retrieval, annotating every privilege transition. Such a diagram makes the architectural trade-off testable rather than rhetorical.

## §1.2 System Calls

**Core model — System Calls**

A system call is an intentional user-to-kernel transition with arguments, validation, privileged work and a return or error code.

**Original worked illustration**

For read(fd,buffer,count), the kernel validates the descriptor and destination memory and may return fewer bytes than requested if data available is limited.

**Boundary conditions and checks**

Treating partial reads as impossible causes truncated data. Some calls can be interrupted or restarted depending on the platform contract.

### System-call interfaces, partial completion, and ownership

An application-facing call can request that the operating system perform work, but neither the call name nor its arguments guarantee that the desired physical work completes immediately. A read operation might copy available bytes out of a kernel buffer, wait for a device, return end-of-file, or return a partial result. The caller must interpret the result contract precisely. Zero bytes on an ordinary end-of-file condition means something different from temporary unavailability on a nonblocking descriptor. Interruptions by signals introduce additional control paths. Wrappers that turn every non-full read into a fatal error break on ordinary streams; wrappers that retry forever without considering EOF can hang. The correct implementation is driven by the type of descriptor, the API contract, and the application's framing requirements.

Suppose a telemetry process must decode a four-byte length header followed by a variable-length payload. If its first read returns two bytes, the next read must fill only the remainder of the header. Once the header is complete, the process validates the claimed length against a configured maximum *before* allocating the payload. Then it accumulates payload bytes until it has the declared number or encounters EOF or error. This is separate from parsing the record: TCP, pipes, and many device streams do not preserve application message boundaries. An individual call can transfer some bytes successfully and still leave a larger application operation incomplete. A robust loop records the number already transferred, bounds checks the offset, and handles termination without discarding accumulated data.

The kernel must also validate user pointers and lengths. A process might pass an address that is unmapped, a pointer to a buffer without write permission, or a length so large that an addition overflows. Careful implementations avoid trusting a user-supplied integer as proof that a memory range exists. A transfer can require pinning pages, copying data, or moving ownership of a mapped region; each has a different lifetime contract. For an asynchronous interface, the operation may outlive the function that submitted it, so buffer ownership cannot be inferred from stack scope alone. A teaching laboratory should trace two separate failure paths: a short but valid read and a validation failure before any copy. Record whether each should advance the application's offset. Avoid concluding that every platform returns identical error codes or that one high-level language call exposes every kernel transition.

## §1.3 Protection Domains

**Core model — Protection Domains**

A protection domain specifies which operations a subject is authorized to perform on which objects. User/kernel separation and process address spaces enforce important domain boundaries.

**Original worked illustration**

A process with read-only access to a file can read its content but should not be able to overwrite it through an ordinary write operation.

**Boundary conditions and checks**

The principle of least privilege does not remove covert or timing channels; a capability or ACL configuration must be tested against intended access paths.

### Protection domains and the principle of least authority

A protection domain is the collection of resources and operations a subject is authorized to use. Domains need not line up one-to-one with processes. A process may temporarily receive a file handle granting access to one object, a service may hold credentials on behalf of a client, or threads may share a process address space while using different restricted operation sets. The key question is which authority an operation needs and who may grant, attenuate, or revoke that authority. Rights should be described as specific operations, such as read contents, append records, rename a directory entry, or administer an interface, rather than the vague statement that an entity is 'trusted.'

Imagine a backup component that should only read a set of files and write encrypted archives to an output directory. Giving it unrestricted administrator privileges would make compromise disproportionately damaging. A narrower design passes handles for the required input tree and one output destination, rejects traversal outside the declared roots, and avoids granting network permission unless the backup format actually needs it. There is an additional subtlety: path-based authorization can be vulnerable to time-of-check/time-of-use changes. If code checks a name and then opens that name later, another actor may replace a symbolic link or directory entry between operations. Using an already-open authorized handle or a constrained directory-relative operation often yields a stronger relationship between the checked object and the used object.

Revocation is rarely as simple as deleting an entry from a list. An access decision may have created an outstanding file descriptor, cached a permission result, or started an asynchronous operation. A well-defined system says whether revocation prevents new accesses only or also invalidates extant handles; it must communicate failures consistently to clients. For a classroom exercise, represent rights as an access matrix with subjects in rows, protected objects in columns, and allowed operations in each cell. Compare granting a broad administrator role with passing a single object capability. Then add a compromised service and ask which objects it could modify under each scheme. Model both enforcement and delegation: a right that can be freely copied may spread far beyond the component initially receiving it. The most defensible policy is the one with an explicitly bounded failure scope.

## §1.4 Resource Abstractions

**Core model — Resource Abstractions**

Resource abstractions provide stable names and operations for variable hardware. An OS virtualizes CPU time, addresses, file handles and sockets to simplify independent applications.

**Original worked illustration**

Two processes can each refer to virtual address 0x1000 while translation maps it to different physical frames, preserving separate address spaces.

**Boundary conditions and checks**

A virtual resource is still constrained by physical capacity; overcommit can lead to page faults, throttling or out-of-memory termination.

### Resource abstractions and the boundary between interface and mechanism

Processes, files, sockets, virtual memory regions, timers, and device descriptors are abstractions because they offer stable operations over mechanisms that differ across machines. A file object does not require an application to know the geometry of a particular storage device; a virtual address does not expose the location of its physical frame; a scheduler allows a program to run without owning a physical CPU for its entire lifetime. Good abstractions hide irrelevant complexity without hiding correctness obligations. If an API promises a byte stream, its users must still handle fragmentation of application records. If an API exposes buffered output, its users must distinguish successful buffering from durable persistence after a crash.

The abstraction has a cost model. Opening a file may require namespace resolution, permission checking, object allocation, and metadata reads. Once open, repeated operations through the descriptor may avoid repeated path traversal. Memory-mapped access may avoid explicit user-level reads but can trigger page faults and complicate error behavior. Using asynchronous I/O may improve overlapping work but adds lifetime and cancellation complexity. An engineering comparison should account for total operations and state changes rather than measuring a single call on a warm cache. A choice that appears faster for short records may become slower when writes require synchronization or workloads are concurrent.

Consider a process manager that launches ten isolated workers. Each worker receives a separate address space but may inherit selected file descriptors, environment variables, or namespaces. A launch interface should document whether inherited resources are closed on execution, whether workers share an underlying open file offset, and how exit status is returned to the parent. One leak of an inherited write descriptor can prevent another process from observing end-of-file on a pipe. The file abstraction still behaves as designed; the bug is a mistake in resource lifetime management. Create a diagram with process identifiers, descriptor tables, and underlying open file descriptions. Close one descriptor and trace which references remain. Distinguish *name*, *handle*, *open-object state*, and *backing data*: conflating those layers causes incorrect assumptions about independent offsets and deletion. A practical API design review should finish with explicit preconditions, postconditions, ownership transfer rules, and the failure behavior for every operation.

### Integrative case study — designing a safe file-ingestion daemon

A small monitoring daemon receives text records from a pipe, validates them, writes accepted records to a rolling file, and exposes aggregate counts to another process. The task sounds trivial, but it spans multiple operating-system boundaries. The pipe is a byte-stream abstraction whose reads can return arbitrarily sized chunks. The rolling output file is a namespaced object whose availability and durability are different properties. The daemon's address space contains untrusted input that must not influence file names, output sizes, or privileged operations without validation. The kernel mediates reads and writes, but the daemon must maintain its own application-level invariants.

Start by defining the record format: a two-byte length field followed by no more than 4096 bytes of UTF-8 data. Require a length between one and 4096 and reject truncated records at end-of-stream. The parser keeps states NEED_HEADER, NEED_PAYLOAD, and REJECTED. If the first read yields one byte, it cannot decode a length yet. If the next yields three, it completes the two-byte header and begins accumulating payload; one remaining byte belongs to the payload rather than a new header. A robust implementation updates an explicit bytes-consumed cursor, bounds-checks every copy, and does not assume that successful read counts equal requested counts. The same logical parser should produce the same output irrespective of how the input stream is chunked. Test with one-byte chunks, a whole-record chunk, and mixed chunk sizes.

Now describe authority. Running the daemon as a privileged account with write access to all system files is unnecessary. It needs a read handle to the input pipe, write permission to one output directory, and perhaps a local metrics endpoint. Prefer a pre-opened directory handle and a controlled output basename to avoid arbitrary-path traversal. If the daemon is compromised through malformed input, its ability to damage other users' files should remain bounded by the actual permitted operations. Separate the authority needed to open the metrics endpoint from the authority needed to rotate log files. The fact that both operations happen inside one executable does not mean they need the same broad permissions.

For rotation, assume the daemon periodically writes a complete next-generation snapshot and makes it visible under a stable filename. A safe design writes a temporary file in the same intended filesystem, checks for errors, requests persistence appropriate to its platform, performs a supported atomic rename, and synchronizes relevant directory metadata when crash durability is required. A successful rename can guarantee an instantaneous namespace switch under the stated scope, but not automatically the durability of the renamed file after power failure. Demonstrate the difference by injecting a crash immediately before and after the rename. State whether the application must preserve the most recent record or merely avoid malformed output; those are different service goals.

Finally, define an acceptance test: records never exceed configured bounds, valid records appear in order, unauthorized file paths remain inaccessible, resource use stays bounded during invalid floods, and an interrupted rotation leaves an allowed old or new snapshot rather than corrupt partial data. Track bytes read, records accepted, rejection reasons, queue size, write errors, and synchronization latency. A kernel or syscall trace can show where time is spent, but the test passes only if application invariants hold. This case illustrates that the operating system provides controlled mechanisms while the application is responsible for composing them into a reliable protocol.

### Diagnostic exercise — audit a syscall boundary

Build a table for six user requests: reading from an allowed descriptor, writing through a read-only descriptor, reading into an unmapped destination, allocating an excessive buffer, accessing a device register directly, and submitting an asynchronous write with a buffer whose owner exits. For each request, identify the actor that makes the authorization decision, the operation's expected completion stage, and the resources that must remain valid. An application-side check may improve error messages but is not a substitute for kernel enforcement. In the unmapped-buffer case, the kernel must validate user memory before trusting its contents or destination. In the asynchronous case, the owner may be the runtime rather than the original stack frame. Compare system calls that transfer bytes to calls that merely enqueue a request. Mark which successes mean accepted, completed, or durable; the three words need not describe the same point in an operation's lifecycle. Finally, explain why an unsafe privileged driver creates a different failure scope than an unsafe ordinary user library.

### Boundary cases and falsifiable design claims

System-call correctness often fails at extreme inputs rather than on ordinary examples. A zero-length read can have different operational significance from reading a positive requested length and receiving zero; a negative file offset may be invalid for one object type and meaningless for another. Device-specific interfaces can impose alignment constraints that ordinary buffered files do not. Application authors should not infer portable behavior from one successful test on one filesystem. Validate arguments before allocating arrays, perform overflow-safe size arithmetic, and read return codes rather than assuming exceptions always communicate kernel failures in a uniform way. A good abstraction makes these cases explicit to callers.

A claim such as 'microkernels are always more secure' is not testable until the trusted code, privilege boundaries, and attack model have been specified. Consider whether a user-mode filesystem service can read arbitrary process memory; whether driver isolation is hardware-enforced; and whether a compromised service can ask a privileged broker to perform unrestricted operations. Performance claims also need a denominator: number of kernel transitions, bytes copied, cold versus warm caches, and concurrency level. Challenge the reader to design an experiment that could contradict the preferred architecture. The result should name latency and failure scope separately, since optimizing one metric need not improve the other.

Resource lifetime is the final subtlety. Closing a file descriptor removes one process's reference; it does not necessarily cancel another thread's use of the same open object, remove a directory name, or delete the underlying bytes. Successful process termination can also leave durable records and network requests already accepted by other systems. In a boundary worksheet, list each operation's logical object, kernel-side state, external effects, and cleanup rights. If an operation fails halfway through, ask which invariants still hold and which parts can be retried without duplication. This connects kernel organization to application-level reliability.

## Three worked questions

### Kernels: worked application 1

A process reads 100 bytes, but read() returns 40. How many bytes remain and what is a safe next step?

**Set up the model and conditions**

Partial reads are permitted by the API for many stream-like sources.

**Carry out the calculation or proof**

Subtract completed bytes: 100−40=60; advance the buffer and reissue a read as appropriate.

**State the result and its scope**

Sixty bytes remain; loop with error/end-of-file handling rather than assuming one call fills the buffer.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Treat the requested length as the size of the application-level record, not an assurance that one kernel operation supplies it. After a read returns forty of the desired hundred bytes, the remaining count is sixty. Advance the destination pointer by forty before the next read; otherwise the next successful transfer overwrites data already received. On a stream, another read may return any permitted positive count up to the remaining amount. If it returns zero under ordinary end-of-file semantics before sixty more bytes arrive, the application must report truncation rather than spin. A negative error result must be classified under the platform contract; some transient conditions justify retry and others are fatal. The arithmetic invariant is received+remaining=100, with both values bounded between zero and one hundred. Repeat the reasoning with results 40, 25, 35: the offsets become 0, 40, 65, and completion occurs at 100. This check catches incorrect pointer handling as well as incorrect total-byte accounting.

### System Calls: worked application 2

Two processes use virtual address 4096. Must this be the same physical frame?

**Set up the model and conditions**

Virtual addresses are resolved through each process's translation context.

**Carry out the calculation or proof**

Different page mappings can point at different frames for identical virtual numbers.

**State the result and its scope**

No; equality of virtual addresses does not imply shared physical memory.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Represent address translation as a lookup keyed by both process translation context and virtual page number. If process A maps virtual page one to frame five and process B maps that same virtual page one to frame nine, virtual address 4096 produces physical addresses 5×4096=20,480 and 9×4096=36,864, respectively. Their equality as virtual numbers gives no basis for equal physical frames. Conversely, processes may deliberately map a shared-memory object to the same physical frame even when their virtual addresses differ. The address offset is preserved by page translation, while permission checks still constrain reads or writes. A test should include equal virtual addresses mapped differently, different virtual addresses mapped to one frame, and a denied write to a read-only mapping. These cases separate address-space identity, physical backing, and access rights, which are logically distinct properties.

### Protection Domains: worked application 3

Explain why a read-only capability does not permit mutation of the referred file.

**Set up the model and conditions**

The handle designates a particular file object with explicitly limited authority.

**Carry out the calculation or proof**

The kernel verifies requested operations against the attached rights.

**State the result and its scope**

A write through a read-only handle must be rejected under the stated model.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Model the capability as a pair containing an object designation and a rights set, such as {read, metadata}. The requested write operation is not a member of that set, so the access check fails regardless of whether the process can guess the underlying file's pathname or identifier. Merely hiding the filename would not enforce read-only access; the operating system or a trusted reference monitor must actually reject the operation. If the process also holds a separate writable capability to the same object, the file might still be changed through that other authority path. The conclusion is therefore limited to mutation attempted *through the read-only handle*. A useful follow-up is to pass this handle to another process and ask whether delegation copies read authority, write authority, or neither. Under the stated model, only held rights may be conveyed, unless a separate privileged delegation mechanism grants more. This tests least-authority reasoning without relying on obscurity.
