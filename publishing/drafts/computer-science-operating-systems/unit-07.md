# Operating Systems — Unit 7: Isolation and security

permissions; capabilities; virtualization; sandboxing

## §7.1 Permissions

**Core model — Permissions**

File permissions encode authorized operations on file system objects. Identity, groups and ACLs determine who can read, write or execute.

**Original worked illustration**

Mode 640 on a regular file grants owner read/write, group read, and others no permissions. Directory execute allows traversal, a different use from executable file permission.

**Boundary conditions and checks**

UID 0, ACLs, mount restrictions and platform policy layers can alter simple mode-bit expectations.

### Permissions and namespace-aware authorization

POSIX-style file permission bits encode read, write, and execute permissions for an owner, group, and others, subject to additional ACLs and platform rules. On regular files, execute generally means permission to execute the file as a program where allowed; on directories, execute is usually permission to traverse or search names inside. Thus mode 640 on a regular file grants owner read/write, group read, and no permissions to others, but access to that file also requires suitable directory traversal permissions. Authorization is a chain of decisions, not a single visible bit field. Ownership and ACL inheritance further complicate policy when creating files in shared directories.

The principle of least privilege starts with a task's required operations and removes unnecessary authority. A web server serving static documents needs to read a designated tree, but generally does not need permission to modify source content or access unrelated user directories. A deployment helper may need write authority to a staging location and permission to make one controlled rename, rather than global filesystem write access. Each additional right increases the potential damage from compromise. Roles and groups simplify administration but can accidentally aggregate permissions beyond what any one operation needs. An audit should identify what the service *can* do as well as what it ordinarily does.

Permissions alone do not defend against all namespace races. If an untrusted directory entry changes between authorization and use, a program can accidentally operate on a different object. Authentication also differs from authorization: determining an identity does not prove that identity may read a particular file. A lab builds an access matrix of three identities and four objects, including a directory and a regular file. For each proposed operation, first determine traversal ability, then object-level authority, then any explicit policy exceptions. Add a user-controlled symlink and discuss why a path-prefix check is insufficient. Require the student to justify a denial path and identify whether the denial originates in identity, directory traversal, object permissions, or a stronger sandbox rule. Keep examples platform-qualified instead of treating one Unix convention as universal.

## §7.2 Capabilities

**Core model — Capabilities**

Capabilities are unforgeable references that combine designation and authority. Passing a capability grants specified access without relying solely on global names.

**Original worked illustration**

A server handing a read-only file descriptor to a helper allows that helper to read the already-open object without discovering the original path.

**Boundary conditions and checks**

An ordinary integer handle is not secure unless the kernel or runtime controls which object it names and what rights accompany it.

### Capabilities, delegation, and confused-deputy hazards

Capability-based security describes authority through unforgeable references that both designate an object and convey permitted operations. A process given a read-only handle to one file need not know or receive a global path credential authorizing all files. A capability can be attenuated, for example by passing a view that permits reading but not writing, when the system supports such restriction. The model is attractive because authority becomes explicit in dataflow. Yet capability safety requires careful assumptions about handle forging, copying, revocation, and the ambient permissions that processes may already possess.

The confused-deputy problem occurs when a privileged component uses its own authority on behalf of an untrusted requester without correctly tying that action to the requester's intended rights. Imagine an image-processing service that can read a private key store for its legitimate internal work. If an API accepts any pathname and reads it using the service's privileged identity, callers may trick it into exposing restricted files. Requiring callers to provide an authorized read capability to the exact input object can align authority with the requested action. That design has to prevent the caller from substituting a broader capability in an unexpected code path and avoid assuming that a capability is equivalent to a safe file format.

Capabilities do not automatically imply strong isolation if the holder can also call an unrestricted ambient filesystem API. A meaningful capability-only sandbox must limit those alternate authority paths. Revocation is also challenging when existing handles can be copied. Systems may use indirection through revocable objects, leases with expiration, or resource teardown policies, each with trade-offs in availability and complexity. For a lab, draw a graph showing which service holds which handles before and after delegation. Have a requester attempt to read a private object through a privileged deputy under two APIs: one that accepts paths and one that requires a passed handle. Trace the authority used at every operation and evaluate whether the caller could have performed that operation directly. Include a process compromise scenario and state explicitly which residual privileges remain available.

## §7.3 Virtualization

**Core model — Virtualization**

Virtualization creates isolated guest environments sharing physical resources through a hypervisor. Hardware virtualization, paravirtualization and containers differ in what is virtualized.

**Original worked illustration**

Two VMs can run different guest kernels on one physical host. A process container normally shares the host kernel instead.

**Boundary conditions and checks**

An isolated guest can still leak through shared resources or suffer hypervisor vulnerabilities; isolation is bounded by the threat model.

### Virtual machines, hypervisors, and isolation boundaries

Virtualization presents a guest operating system with abstractions of processors, memory, interrupts, and devices. A hypervisor coordinates access to physical resources while enforcing boundaries between guests. Some virtualization support is provided by processor extensions that enable efficient transitions and nested address translation. A virtual machine can run a guest kernel distinct from the host's kernel, making it different from a conventional container that shares the host kernel while isolating process namespaces and resource usage. This distinction affects both compatibility and the consequences of a kernel vulnerability. It is a boundary claim, not proof that a VM is immune to escape bugs.

Virtual CPUs require scheduling onto physical execution resources. Oversubscription can improve utilization if guest workloads are often idle, but a CPU-heavy fleet can face contention and unpredictable tail latency. Memory can be reserved, overcommitted, shared under carefully controlled conditions, or reclaimed. Guest-visible memory pressure and host-level memory pressure are related but not identical. Virtual devices may be emulated, paravirtualized, or passed through with stronger hardware support. Each choice changes performance, attack surface, migration capability, and operational complexity.

Compare two services: one runs as a process in a namespace-isolated container, and one runs inside a dedicated guest VM. Under a host kernel bug, the attack surfaces and possible blast radii differ. Under an application bug that corrupts its own database, neither isolation method fixes the data model. Under an incompatibility requiring a different kernel module ABI, a VM may be a practical choice, whereas a standard container inherits the host's kernel constraints. A lab prepares a table with columns for guest kernel, filesystem namespace, virtualized network, CPU scheduling, memory isolation, and device access. Fill the table for processes, containers, and VMs under clearly stated deployment assumptions. Avoid ranking the choices as universally secure or fast; attack surface, maintenance, startup cost, density, and observability must be compared for the actual workload.

## §7.4 Sandboxing

**Core model — Sandboxing**

Sandboxing restricts an application's operations using process boundaries, syscall policies, filesystem restrictions and resource limits.

**Original worked illustration**

A document converter running without network access and with a read-only input directory can reduce damage from a malformed document exploit.

**Boundary conditions and checks**

A sandbox rule that still permits arbitrary host file writes is not meaningful containment for file integrity.

### Sandboxing, syscall policy, and layered defense

A sandbox constrains a program's access to resources beyond what the program requires. Mechanisms may include namespaces, file and network permissions, syscall filtering, resource quotas, virtual machines, language-level isolation, and brokered operations. Defense in depth combines independent controls so that one failure does not immediately grant unrestricted authority. The controls should be evaluated as specific policies, not as a binary 'sandboxed' label. A container image may run as a nonprivileged user yet still retain network access, host-mounted secrets, or dangerous device mappings. Conversely, denying network access does not prevent a program from reading every file it can open through remaining permissions.

An effective threat model names the adversary, the resources to protect, and which actions count as a breach. For an untrusted document renderer, desired restrictions might include read-only access to the submitted document, bounded CPU and memory use, no outbound network, no writable host filesystem, and a timeout. A renderer that can write only to a temporary directory may still consume all available storage unless disk quotas are enforced. A renderer allowed to read sensitive documents cannot be expected to keep them secret from its own output unless output review and data-minimization rules are added. Resource limits reduce denial-of-service risk but require handling legitimate high-cost tasks gracefully.

System-call restrictions can reduce attack surface but can also break legitimate dependencies, including runtime memory allocation, thread creation, or error reporting. Policies therefore need realistic workload traces and careful exception review. They should be tested against intentionally malformed input, high allocation rates, long-running loops, and attempted network or filesystem access. A lab uses a table of required capabilities for a PDF-to-image conversion service and writes a deny-by-default policy at the conceptual level. Introduce four adversarial cases: path traversal, an oversized document, attempted network exfiltration, and a crafted parser crash. For each case, state the expected isolation boundary, whether that boundary stops the entire attack, and what operational evidence demonstrates enforcement. Never treat the absence of a visible crash as evidence that the policy was exercised.

### Integrative case study — running an untrusted code evaluator

A service accepts short programs from students and returns their output. Those programs cannot be assumed benign. They might intentionally allocate excessive memory, loop forever, open sensitive files, create many processes, or attempt network communication. Treating student code as a standard internal library would grant it the same authority as the service and create an avoidable attack surface. A sound architecture separates submission parsing, execution, output capture, and result publication into components with different privileges. The execution component receives only the resources necessary for one task and produces a bounded result.

Begin with a threat model. The assets include host secrets, other students' submissions, service availability, and the integrity of output records. Possible attacks include filesystem traversal, resource exhaustion, attempts to connect to external endpoints, and exploitation of runtime or kernel vulnerabilities. A sandbox might use an isolated process namespace, mount namespace, restricted filesystem view, nonprivileged identity, CPU and memory quotas, file-descriptor limits, network restrictions, syscall filters, and possibly virtualization for a stronger guest-kernel boundary. Each defense needs a concrete policy and an independently observable test. Merely placing an application in a container image is not proof that these restrictions exist.

Suppose each submission has an allowed CPU budget of two seconds, a wall-clock deadline of five seconds, a memory allowance of 128 MiB, and output capped at one MiB. Those are design parameters rather than universal safety constants. An infinite loop may hit CPU budget. A blocked task might consume little CPU yet exceed wall-clock time, so both deadlines matter. A program that prints forever can exhaust log storage unless stdout capture is bounded. Forking a large number of processes may bypass a memory-only limit if process count is unconstrained. The service should distinguish an accepted correct answer from a timeout, forbidden operation, crash, output limit, or infrastructure error; conflating them harms both user feedback and incident diagnosis.

Execution teardown must be robust. A supervisor starts each sandbox with a unique job identifier and explicitly controls its descendants. If the user program spawns children or opens asynchronous operations, killing only the initial process may leave other work behind. A job record includes input digest, execution start and end, exit state, resource usage, and output hash, while logs avoid storing secrets. Reuse of a sandbox requires demonstrably clean state; destroying the sandbox and creating a fresh one is often operationally simpler when resources permit. If the system supports high-density workers, test whether one compromised or runaway job can monopolize the host despite nominal per-job limits.

A verification matrix includes ordinary computation, illegal file read, attempted network access, memory exhaustion, CPU loop, fork burst, invalid executable, and oversized output. For each scenario, record expected denial mechanism and actual observed behavior. A blocked outbound connection is evidence of a network rule, not proof that the sandbox is secure against every kernel escape. A VM may provide a distinct guest kernel but adds boot and management costs; a container can be adequate for a lower-risk workload if policies and host patching are strong. State residual risks and provide a patch, monitoring, and incident-response plan. This is a realistic exercise in least authority and layered defense rather than a claim of perfect isolation.

### Diagnostic exercise — attempt constrained operations

Create a policy matrix for an untrusted document renderer. Allow reading one submitted input and writing a bounded output in a temporary directory; deny arbitrary host file reads, network access, and excessive CPU or memory use. Verify actual enforcement by attempting each forbidden action in a controlled sandbox, recording the denial mechanism rather than just whether the program stopped. Assume the renderer is compromised and calculate which resources remain accessible through inherited descriptors or writable mounts. A file permission may be correct while a privileged broker still serves unintended paths; that is a confused-deputy risk. Compare an ordinary container sharing the host kernel with a separate guest VM, identifying where the kernel trust boundary changes and what operational costs increase. Conclude with residual risks: vulnerabilities in the allowed parser, overbroad output channels, and resource quotas that fail to cover process count or temporary storage.

### Boundary cases and falsifiable design claims

A read-only filesystem view is not a complete sandbox. A process may retain an inherited writable descriptor to an object outside that view, have an allowed IPC connection to a privileged broker, or possess access to secret environment variables. Denying file writes does not prevent CPU exhaustion, fork storms, or memory pressure. Network isolation can also be incomplete when an exposed local socket or shared IPC namespace provides indirect communication. An accurate claim lists every permitted channel and assesses whether the adversary can use it for exfiltration or persistence.

Least privilege can conflict with functionality if required operations are not inventoried. An application might need temporary storage for sorting, a DNS lookup for a licensed dependency, or controlled access to a logging endpoint. Disabling everything without tests could merely make the application fail. A better process records normal operation traces, extracts required privileges, applies a deny-by-default policy, and intentionally tests both allowed and forbidden cases. But traces of happy paths do not capture rare error recovery, so stress and failure injection are important before deployment.

Isolation also requires patch management and accountability. A sandbox that ran safely last month may be exposed by a newly discovered host kernel bug. Operators should know which image, kernel version, policy, and host were used for a particular execution and be able to quarantine affected outputs. An audit trail must itself avoid leaking submitted secrets. Discuss the limits of an execution service that promises 'no data leaves the sandbox' while allowing arbitrary program output: the program may encode input secrets in its output. Output channels and read permissions must be part of the same threat model.

## Three worked questions

### Permissions: worked application 1

Interpret POSIX-like file mode 640 in owner/group/other permissions.

**Set up the model and conditions**

Octal digit 6=read+write, 4=read, 0=no rights.

**Carry out the calculation or proof**

Assign digits to owner, group and other respectively.

**State the result and its scope**

Owner can read/write; group read; other has no permissions.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Octal 6 corresponds to binary 110, enabling read and write while excluding execute; octal 4 is binary 100 for read only; and octal 0 grants none. Assign the three digits to owner, group, and others to obtain owner read/write, group read, and no permissions for others. The result assumes ordinary file-mode bits without an overriding ACL or special platform-specific policy. A user trying to access the file must also have sufficient search permission through each parent directory. Mode 640 applied to a directory has different practical implications because the execute bit governs traversal. A follow-up example changes the mode to 750 and asks for owner, group, and other rights, checking that learners understand the bit sum rather than memorizing one displayed string.

### Capabilities: worked application 2

Can ordinary containers guarantee different guest kernels than the host?

**Set up the model and conditions**

Namespace-style containers isolate processes while sharing host kernel facilities.

**Carry out the calculation or proof**

VMs place separate guest kernels behind a hypervisor boundary.

**State the result and its scope**

No: standard OS-level containers share the host kernel.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

A standard container isolates a group of processes using facilities of the host operating-system kernel. It does not ordinarily boot an independent guest kernel with a completely unrelated version and driver stack. Virtual machines use a hypervisor boundary to present hardware abstractions to guest kernels; a guest VM can therefore run a different supported kernel. There are nuanced technologies that place a lightweight VM behind a container-like management interface, so the product label alone is insufficient to identify the boundary. The question explicitly asks about ordinary containers, for which sharing the host kernel is the correct answer. Validate the conclusion by comparing the observed kernel release inside and outside a container and by separately inspecting a full VM guest, recognizing that command output can still be virtualized or formatted by the environment. Security claims must name the actual enforcement mechanism.

### Virtualization: worked application 3

A program is restricted to read-only input files with no network and no host-directory writes. What does this sandbox prevent?

**Set up the model and conditions**

Read-only mounts block ordinary changes to the input data.

**Carry out the calculation or proof**

Denied networking and host writes remove two significant exfiltration and persistence channels.

**State the result and its scope**

Containment is improved but not absolute; kernel bugs and allowed read access remain within the threat model.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Read-only mounts block ordinary write operations to the exposed input path, lack of network access removes a major direct outbound channel, and prohibition of host-directory writes prevents normal persistence into those paths. These restrictions reduce authority but do not guarantee secrecy or containment against all threats. If sensitive input is legitimately readable, the program can still transform and include it in allowed output; if the kernel has a vulnerability, a sandbox escape may be possible. Resources not mentioned in the policy, such as CPU time, memory, process count, temporary storage, and inherited descriptors, may remain available. A complete threat assessment enumerates precisely what the program can read, modify, communicate, and exhaust. Test each claimed restriction with a blocked operation rather than relying only on configuration text. The result is reduced attack surface under a declared policy, not a blanket assurance of safety.
