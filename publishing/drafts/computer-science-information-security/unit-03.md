# Information Security — Unit 3: Systems Security

> Original educational editorial draft, 24 October 2026. The fictional North River University laboratory introduced in Units 1–2 remains the case study. This unit discusses defensive system design and small mathematical teaching models, not exploitation instructions. It has not undergone independent academic or production security review.

## Learning outcomes

After studying this unit, a reader should be able to identify spatial and temporal memory-safety failures, compare language and runtime mitigations, construct a least-privilege capability matrix, explain the assumptions behind firmware and boot integrity, distinguish process isolation from application authorization, calculate toy permission exposure and patch-coverage models, and state what these models cannot establish. A reader should also be able to specify evidence that would support or falsify a claim that a system is securely configured.

## 3.1 Memory safety: boundaries in space and time

### What a memory boundary means

A running program manipulates values held in memory. Some values are numbers or character sequences, while others represent locations at which the program expects to find objects. A memory-safety defect occurs when software accesses memory outside an object's valid bounds or lifetime, or otherwise violates the language or runtime's rules for valid access. Two broad dimensions matter. *Spatial safety* asks whether an access remains inside the intended allocation. *Temporal safety* asks whether the allocation still represents a live object at the time of access. A buffer overflow illustrates the spatial problem; use-after-free illustrates the temporal problem. Both are defects in the relationship between a program's intended objects and the memory operations actually performed.

The laboratory uses an older image-processing component to transform instrument photographs into standardized reports. A programmer expects each decoded image row to contain a fixed number of samples. If the program allocates storage for one width but copies data according to a larger, untrusted width, it may write beyond the destination object. Even if the copied bytes look like ordinary pixels, their placement can corrupt adjacent data. A separate mistake occurs if a background worker holds a pointer to an image object after another component has destroyed that object. The pointer's numerical value may remain unchanged, but the object lifetime has ended. The storage might already be used for something else. These examples demonstrate why merely checking whether a pointer is non-null does not establish safety.

The correct abstraction is not that attackers somehow possess magical access to memory. Rather, the program has been given authority to read or write memory, and a bug causes it to exercise that authority on the wrong object. Memory protection at the operating-system level usually separates processes, but a process must still manipulate many objects within its own address space. Operating-system address-space separation does not by itself prevent a buffer inside one process from overwriting another buffer belonging to that same process. Likewise, encryption of a stored image does not prevent an unsafe decoder from mishandling it after decryption. Each control addresses a different trust boundary.

### Prefer eliminating defect classes before detecting individual bugs

An important design choice is whether to continue using a memory-unsafe implementation for a new component. A memory-safe language or managed runtime can enforce bounds and lifetime rules for ordinary operations. This can prevent large categories of accidental invalid memory access, although it does not make the program immune to authorization errors, malicious dependencies, resource exhaustion, or logic flaws. Language choice should be evaluated at the actual boundary: a memory-safe front end that calls an unsafe native image library may still inherit risk from that library. Foreign-function interfaces, unsafe blocks, compiler bugs, and runtime defects deserve explicit attention rather than a slogan that one language solves security.

For existing components, organizations often combine code review, compiler hardening, sanitizers in tests, fuzzing, dependency updates, and gradual replacement. A sanitizer instruments selected executions to detect certain invalid operations; it is useful evidence when it reports a defect, but the absence of a report in finite testing is not proof of correctness. Fuzzing explores inputs that human testers may not anticipate, yet coverage depends on the harness, seeds, execution time, reachable states, and assertions. A compiler mitigation can make some exploitation paths harder while leaving the underlying defect present. None of these techniques should be described as a mathematical guarantee that all memory corruption has disappeared.

A practical migration plan begins with an inventory of which components parse untrusted inputs, which execute with broad privileges, which are exposed to the network, and which are maintained by teams able to modify them. The laboratory might first replace the image metadata parser that directly accepts uploads, then isolate a legacy codec that cannot immediately be rewritten. That sequencing is not a claim that all image parsers are more dangerous than all other code. It follows from the specific data path, permissions, update cadence, and business consequence in the fictional laboratory. A documented decision records the assumed threat, the cost of change, and what measurements would justify changing the order.

### Data validation and memory safety are different obligations

Suppose a program checks that an uploaded image claims to be at most 10,000 pixels wide. This may protect the service from excessive memory use, but it is not a complete memory-safety proof. The code could still compute `width × channels × bytesPerChannel` in an integer type too small to represent the product, allocate according to the wrapped result, and later write according to the intended result. Alternatively, a library could ignore the declared width when decoding a malformed format. The design must connect validated dimensions to checked arithmetic, actual allocation sizes, and the decoder's output contract. The general principle is to validate assumptions at every boundary where representation or ownership changes.

When reviewing a suspected defect, distinguish the *cause*, the *observable failure*, and the *security consequence*. An out-of-bounds access is a cause; a crash may be an observed failure; unauthorized data exposure is one possible consequence, not an automatic one. Some invalid accesses never manifest under a particular test run. Some crashes have causes unrelated to memory safety. Responsible engineering avoids treating an observed crash as proof of compromise, or a clean test run as proof of safety. The laboratory should preserve reproducible, non-sensitive test cases, track affected versions, fix root causes, and verify the correction with regression tests before closing the issue.

## 3.2 Privilege separation: granting only the authority a task needs

### Authority follows the component, not its good intentions

A service has privileges when it can perform operations that another actor cannot: read a protected file, bind a network port, change a configuration, create a user, or issue a laboratory report. The principle of least privilege asks that each actor receive only the permissions needed for its assigned task and only for as long as needed. It is an architectural principle, not a request for developers to promise that they will behave carefully. If an image conversion worker only needs to read a temporary upload and write a transformed image, there is no functional reason for it to read a personnel database or rotate signing keys.

In the laboratory, an incoming request crosses several components. The web gateway authenticates the user and checks which report may be requested. An upload worker validates file types and stores the raw file in a restricted staging area. An image processor reads staged files and writes normalized output. A report signer uses a separate service to apply an approved signature after policy checks. A database records the final state. If all these components run under one all-powerful account, a defect in the image processor may affect records and signing operations that are unrelated to image conversion. Separation aims to make the authority of a compromised component narrower than the authority of the whole workflow.

Privilege separation is effective only when enforcement occurs at a boundary the less-trusted component cannot simply bypass. A human-facing diagram with separate boxes does not create separation if all boxes share the same credentials, unrestricted filesystem, or administrative API token. The laboratory must specify where enforcement happens: operating-system user identities, access-control lists, separate service identities, scoped credentials, mandatory access controls, network policy, or a dedicated signing service. A component may need to communicate with a privileged service, but the privileged service must independently validate the requested operation. Otherwise a 'helper' becomes a universal privilege tunnel.

### Design a permission matrix before configuring accounts

A useful design artifact is a matrix whose rows are components and whose columns are protected operations. The image worker may receive permission to read staged images and write normalized images, but not to approve reports. The signer may receive permission to sign already-approved report digests, but not to read arbitrary uploaded content or alter user identities. The auditor may read append-only activity records without permission to rewrite them. A row containing every permission is a warning sign: perhaps the component is doing too many jobs, or perhaps the team has not mapped the workflow carefully enough.

This matrix must include temporary operations and maintenance activities. A backup process might legitimately read many records, but it should not require the ability to issue reports. A deployment service may need to install software, but that does not imply it should retain database access after deployment. A developer's emergency access may be justified during an incident, but it should be time-bound, approved, logged, and revoked when the incident ends. Distinguishing steady-state authority from exceptional authority helps avoid permanent privileges granted for a one-time repair.

Least privilege can also fail through inherited authority. A process started by an administrative account may inherit environment variables, open file handles, or access tokens. Merely changing the visible username of a worker does not necessarily remove every capability. Credentials can leak through logs, crash dumps, build artifacts, and shared volumes. Effective review follows the complete lifecycle of each credential: creation, distribution, storage, rotation, revocation, and evidence of use. This lifecycle perspective is more informative than asking whether a password was strong.

### A quantitative exposure model, with limits

To teach the difference between required and granted permissions, define a deliberately simplified *excess-grant count*. For each component, count the permissions granted but not required by its documented task; add those counts across components. Suppose a three-component service has a universe of eight possible permissions. A web gateway needs three permissions but receives five, an image worker needs two but receives six, and a report signer needs two and receives two. The excess counts are 2, 4, and 0, giving six excess grants in the model. Removing four unnecessary image-worker grants reduces the count to two. This is a transparent configuration metric, not a measure of probability that an attacker succeeds.

A simple ratio can also be reported: the number of unnecessary grants divided by all grants. In this example there are 13 granted permissions and six unnecessary grants, so the excess fraction is 6/13, about 46.15%. After removing four unnecessary grants, there are nine total grants and two unnecessary ones, giving 2/9, about 22.22%. The denominator changes when grants are removed. Comparing only percentages without recording the actual grant sets can conceal which high-impact permissions remain. A permission to read a public status page is not equivalent in consequence to permission to issue a signing key. Real reviews therefore pair the count with a qualitative description of critical capabilities and whether separation is actually enforced.

## 3.3 Boot integrity: establish trust before ordinary services start

### What a boot chain is supposed to establish

When a computer starts, firmware initializes essential hardware and passes control to later boot components, which eventually start an operating system. A security claim about the running operating system depends partly on what executed before it. If an early component can be modified without detection, later checks may run inside an environment already controlled by untrusted code. A verified boot design addresses this ordering problem by requiring selected components to be authenticated against an appropriate trust anchor before execution. A measured boot design instead records measurements that may later be assessed. The two approaches are related but not interchangeable: recording a measurement does not necessarily stop execution of an unapproved component.

The laboratory has a small fleet of instrument-control workstations. Administrators want evidence that the bootloader and critical system components match approved versions. A simplified trust chain starts from a protected initial verifier, which authenticates the next stage, which in turn authenticates the next. Every link matters. If the initial trust anchor can be replaced freely, checking later signatures has little meaning. If one stage loads an unverified module, the chain's coverage has a gap. If an attacker can roll back to an older but validly signed vulnerable component, signature verification alone may not provide the expected security outcome. Version policy and rollback protections may therefore be necessary.

Cryptographic signatures do not decide whether a particular piece of software is safe. A valid signature demonstrates a relationship to an accepted signing key and an unchanged signed artifact under the signature scheme's assumptions. It does not guarantee that the software contains no defects or that its vendor's build system was uncompromised. Conversely, a failed signature check may arise from corruption, configuration errors, unsupported updates, or unauthorized modification; the result calls for a controlled response rather than immediate attribution of malicious intent. A resilient system needs protection, detection, and recovery procedures, not only a boot-time green indicator.

### Recovery is part of the security design

Imagine a workstation that refuses to boot after a legitimate firmware update. An administrator might be tempted to disable verification permanently to restore service. That action can undermine the control the organization intended to rely upon. A stronger plan specifies a recovery path using an authenticated known-good image, documented key-management procedures, and an audit trail. It also identifies what happens if a signing key must be revoked or replaced. The laboratory's service-level requirements may demand a spare instrument or offline operating procedure while recovery is underway. Security and availability must be designed together rather than traded away at the first outage.

The boot process also has boundaries. A successfully verified kernel does not prove that every user-space application is authorized, that every running process remains uncompromised, or that all data files are correct. An attacker might exploit a runtime vulnerability after boot, steal a valid user credential, or abuse a legitimately installed service. Boot integrity is evidence about selected components at selected points in time. Runtime protection, access control, patch management, and monitoring remain necessary. Treating boot verification as a complete security certificate would confuse one layer of defense with the whole system.

A review should ask exactly what is verified, by which key, at which stage, with what failure response, and with which rollback rules. It should also ask how updates are authorized and how recovery images are protected. The laboratory could run a controlled test on a nonproduction workstation: present a deliberately invalid test image and verify that the documented rejection path occurs, then restore an approved image. Such a test evaluates a known property without requiring the creation or use of malicious firmware. The result should record the device model, firmware version, policy state, and test scope. A passing test on one workstation is not evidence that every workstation in the fleet has the same configuration.

### Distinguish coverage from assurance

For a teaching exercise, define boot-chain *verification coverage* as the number of critical stages with enforced authentication divided by the number of critical stages in a specified model. If five stages are identified and four are authenticated, coverage is 4/5, or 80%. This arithmetic is easy to verify, but the meaning is limited. A single unauthenticated stage with powerful authority may defeat the entire intended trust chain. Moreover, a nominally authenticated stage may trust a key that is no longer controlled by the organization. The coverage fraction is useful as an inventory prompt, not as a probability that a machine is secure.

A better assurance record combines stage coverage with evidence of root-of-trust protection, key custody, update validation, rollback policy, and tested recovery. These are not naturally interchangeable numbers. A review should not average them into an invented 'security score' without a justified decision model. This distinction is central to security engineering: counting controls is not the same as demonstrating that a relevant adversary cannot bypass them. The goal is to make claims narrow enough that tests and evidence can meaningfully support them.

## 3.4 Isolation: constrain failures across execution boundaries

### Separate address spaces, identities, and responsibilities

Isolation is the deliberate separation of execution or data domains so that an error in one domain does not automatically grant control over another. An operating system normally gives distinct processes separate virtual address spaces. A virtual machine can provide a guest operating system with a hardware-assisted boundary managed by a hypervisor. A container often provides namespace and resource isolation while sharing a host kernel. A browser sandbox can restrict what a rendering process may access. These mechanisms have different trust assumptions and failure modes; calling all of them 'sandboxes' without specifying the boundary is too vague for an engineering decision.

In the laboratory, a report-rendering service must process documents submitted by external collaborators. It can run in a restricted worker that lacks database credentials, cannot reach internal administration interfaces, and has limits on CPU time, memory, and output size. If the renderer crashes, the worker can be discarded without stopping the report database. The design is stronger when the worker receives only the particular input it needs and can return only a constrained result. Isolation is weaker when the worker shares writable host directories, unrestricted network access, or long-lived credentials with sensitive services.

Isolation does not replace authorization. Two isolated services can still exchange data through an API; if that API accepts any request from the worker as fully trusted, the worker may misuse the service's authority. Similarly, resource limits may protect availability without protecting confidentiality. A memory quota can prevent one document from exhausting the host, but it does not prevent a worker with a database token from reading records. Effective isolation combines execution boundaries, explicit communication interfaces, least privilege, and validation of inputs and outputs. Each element has a distinct role.

### Choose boundaries based on consequences and operational costs

A dedicated virtual machine may offer stronger separation for some workloads than a container sharing the host kernel, but it may require more resources, more patching, and more complex deployment. A separate process under a restricted identity can be sufficient for some lower-risk transformations. The choice depends on the assets at stake, the attack surface of the parser, the strength of the host configuration, and the cost of operating the boundary correctly. There is no universal rule that every component should run in its own virtual machine. Excessive complexity can itself cause configuration mistakes, delayed patches, and confusing incident response.

Consider a pipeline that receives 1,000 documents each day. If every document launches a new worker, startup cost and cleanup become significant. A pool of workers may improve throughput but increases the time that a worker remains alive and the number of documents it processes before replacement. A queue may protect the database from bursts, yet a backlog can affect availability. The laboratory should specify latency objectives, memory ceilings, failure isolation, and how worker state is cleared. Operational measurements matter because a theoretical boundary that administrators disable under load offers little practical protection.

An isolation review follows the paths that cross boundaries. Which process can create a worker? Who can change its policy? Where do logs go? Can the worker write to a shared directory consumed by a privileged service? Are secrets mounted inside the worker, or supplied only to a narrow broker? Is network access denied by default, and can the worker reach metadata or control endpoints? A diagram showing separate containers is only the beginning; configuration and runtime evidence determine whether the intended restrictions exist. The reviewer should distinguish an asserted policy from a policy observed under test.

### A bounded model for resource containment

A second teaching model examines the resource budget of a worker pool. Assume each active worker is allowed a fixed memory budget, the pool has a fixed maximum number of concurrent workers, and a separate baseline is reserved for the host. Under these declared assumptions, a conservative planned upper bound is `hostBaseline + workerLimit × perWorkerBudget`. If the host baseline is 2 GiB, eight workers are allowed, and each is limited to 384 MiB, the planned bound is 2,048 + 8 × 384 = 5,120 MiB, or 5 GiB. If the physical host has 8 GiB, the arithmetic leaves 3 GiB for other uses in this toy allocation plan.

The model does not guarantee that the real machine will stay below the number. Kernel accounting, page cache, shared memory, device allocations, overcommit, and limits configured incorrectly can invalidate the assumptions. The per-worker cap may be a policy value rather than an enforced hard limit. The model also says nothing about whether the worker can read sensitive data. It is useful for comparing planned configurations and exposing impossible capacity claims, not for certifying isolation security. A trustworthy deployment test would measure actual peak usage, verify enforcement under a benign stress workload, and observe whether a worker's failure leaves other services responsive.

### Putting the four controls together

The laboratory's upload pipeline illustrates defense in depth without suggesting that piling on controls automatically makes a system secure. A memory-safe parser reduces certain classes of invalid memory access. A least-privilege worker limits what the parser could do if a defect or logic error remains. Boot verification supplies evidence about the integrity of selected early components, reducing one category of startup uncertainty. Process isolation constrains which resources and services the worker can reach. None of these claims is absolute, and none substitutes for a tested authorization policy or a maintained update process.

A practical review therefore starts with a specific failure scenario: a malformed document reaches the rendering worker. It asks whether the parser safely handles the input; whether the worker has unnecessary privileges; whether its execution domain is appropriately restricted; whether the host and worker images are maintained and verified; and whether an alert and recovery procedure exist if the worker repeatedly fails. Each question requires its own evidence. This is a more useful form of security assurance than a single dashboard number labeled 'protected.'

## Fully worked problems

### Problem 1 — Audit excess privileges in a laboratory pipeline

**Question.** A web gateway requires three permissions and has five. An image worker requires two and has six. A report signer requires two and has two. Assume each required permission is included in the granted set, and all permissions are distinct within each component. Find the total number of unnecessary grants and their fraction of all grants. Then remove four unnecessary grants from the image worker and recompute both quantities. State why the fraction is not a risk probability.

**Step 1 — Count the grants.** Before remediation, the three excess counts are 5 − 3 = 2, 6 − 2 = 4, and 2 − 2 = 0. The total excess is 2 + 4 + 0 = **6**. All granted permissions total 5 + 6 + 2 = **13**.

**Step 2 — Compute the fraction.** Excess fraction = 6 / 13 = **0.461538…**, or approximately **46.15%**. The numerator counts excess grants; the denominator counts grants. Neither number weights the sensitivity of individual capabilities.

**Step 3 — Recompute after a specific change.** The image worker's grants decrease from six to two while its required count stays two. New excess = 2 + 0 + 0 = **2**; new granted total = 5 + 2 + 2 = **9**; new fraction = 2 / 9 = **0.222222…**, or approximately **22.22%**.

**Step 4 — Interpret carefully.** Removing grants reduces this toy configuration metric, but a remaining grant could still authorize a critical action, and an unprotected inter-service API could bypass the intended matrix. A 22.22% excess fraction does not imply a 22.22% chance of compromise. Actual risk requires threat and consequence analysis, enforcement evidence, and testing.

**Answer.** Excess grants fall from **6/13 (46.15%)** to **2/9 (22.22%)**. This is a permission-audit metric, not a security probability.

### Problem 2 — Evaluate boot-stage coverage and its blind spots

**Question.** A fictional instrument has five identified critical boot stages. Four stages are authenticated by the preceding trusted stage, while one plugin-loading stage accepts unsigned modules. Calculate the stage-verification coverage. A proposed change adds verification to the fifth stage. Recalculate coverage and explain why 100% of stages checked does not prove the system is secure.

**Step 1 — Define the denominator.** The model explicitly identifies five stages. This count is a design assumption and must not be inferred from the number of files in a firmware image. Four have enforced checks.

**Step 2 — Compute the initial coverage.** Coverage = 4 / 5 = **0.8**, or **80%**. The unverified plugin loader remains a trust-chain gap. Because it executes code, its importance may be disproportionate to the simple one-fifth count.

**Step 3 — Evaluate the proposed control.** If the fifth stage is authenticated under the same defined model, coverage becomes 5 / 5 = **100%**. This is a statement about the specified checks, not about the trustworthiness of the accepted code.

**Step 4 — State residual assumptions.** The initial trust anchor must be protected, signing keys must be appropriately controlled, update and rollback rules must be enforced, and runtime software must still resist defects and unauthorized actions. A perfectly signed vulnerable component remains vulnerable. The laboratory should test rejection and recovery on nonproduction equipment.

**Answer.** Coverage rises from **80% to 100%**, but this metric alone is not evidence of comprehensive platform security.

### Problem 3 — Plan resource isolation for a document worker pool

**Question.** A host has 8 GiB of physical memory. Its baseline reservation is 2 GiB. The design permits eight concurrent document workers, each with a configured 384 MiB budget. Under an additive toy model, calculate the planned total reservation and the remaining unreserved memory. If the worker limit rises to twelve with other values unchanged, repeat the calculation. Explain one reason this is not a guarantee of real memory use.

**Step 1 — Use consistent units.** In this exercise, 1 GiB = 1,024 MiB. Host capacity = 8 × 1,024 = **8,192 MiB**. Baseline = 2 × 1,024 = **2,048 MiB**.

**Step 2 — Compute eight-worker reservation.** Workers reserve 8 × 384 = **3,072 MiB**. Combined planned reservation = 2,048 + 3,072 = **5,120 MiB**, or **5 GiB**. Unreserved capacity = 8,192 − 5,120 = **3,072 MiB**, or **3 GiB**.

**Step 3 — Compute twelve-worker reservation.** Workers reserve 12 × 384 = **4,608 MiB**. Combined planned reservation = 2,048 + 4,608 = **6,656 MiB**, or **6.5 GiB**. Unreserved capacity = 8,192 − 6,656 = **1,536 MiB**, or **1.5 GiB**.

**Step 4 — Interpret the boundary.** This is arithmetic over declared budgets, not a measurement of real memory. Shared pages, kernel allocations, unaccounted caches, configuration errors, and unenforced limits may change actual usage. Nor does a memory cap establish confidentiality or prevent misuse of network credentials.

**Answer.** Eight workers imply **5 GiB reserved and 3 GiB unreserved**; twelve imply **6.5 GiB reserved and 1.5 GiB unreserved**, under the stated toy assumptions.

## Interactive learning models

**Model A — Least-privilege grant audit.** Change the number of required and granted permissions for one component. The model rejects configurations in which grants are fewer than requirements, and shows excess grants and their share of all grants. It cannot tell whether the remaining grants are safe or whether policy is enforced.

**Model B — Worker-pool memory budget.** Change the number of workers and per-worker memory allowance. The model shows planned aggregate reservation and remaining host capacity under an explicitly additive assumption. It does not inspect the host, enforce a limit, or make a real-world safety prediction.

## References and further verification

- NIST SP 800-218, *Secure Software Development Framework* (final version 1.1, 2022): https://csrc.nist.gov/pubs/sp/800/218/final. A later revision was an initial public draft as of October 2026; do not confuse it with the final publication.
- CISA et al., *Exploring Memory Safety in Critical Open Source Projects* (2024): https://www.cisa.gov/news-events/alerts/2024/06/26/cisa-and-partners-release-guidance-exploring-memory-safety-critical-open-source-projects.
- NIST SP 800-193, *Platform Firmware Resiliency Guidelines* (2018): https://csrc.nist.gov/pubs/sp/800/193/final. Its protection, detection, and recovery principles are distinct from a claim that any signed firmware is defect-free.
- NIST SP 800-53 Rev. 5, AC-6 (Least Privilege) and SC-39 (Process Isolation): https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final.

**Editorial boundary.** This unit uses fictitious systems and bounded mathematical demonstrations. It is not an operational configuration checklist, penetration-testing guide, security audit, or independent validation of a production environment.
