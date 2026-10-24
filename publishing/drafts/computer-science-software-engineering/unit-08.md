# Software Engineering — Unit 8: Professional practice

*Draft instructional manuscript. Not independently peer reviewed.*

Original engineering case studies, failure analysis, design exercises, and locally testable simulations for professional practice.

## 8.1 Ethics

**Ethics: conceptual explanation**

Ethics in software begins with foreseeable impacts on users, non-users and institutions. An attendance system can produce unjust disciplinary decisions if it silently treats offline students as absent. Stakeholder consent, contestability and evidence of harm matter beyond simply meeting a functional requirement.

### Engineering depth and worked reasoning

Professional ethics begins by recognizing that engineering choices distribute benefits and harms among people who may not have chosen to use the system. Accuracy, privacy, safety, security, fairness, transparency, and meaningful remedies can conflict with speed or commercial pressure. Ethical analysis requires identifying affected parties, evidence, uncertainty, and alternatives—not attaching an ethics label to a finished design.

Consider the obligation to report known severe flaws, avoid deceptive claims, protect confidential information, respect intellectual property, and decline unsafe shortcuts. A team should establish escalation channels for concerns that conflict with a manager’s preferences. Transparency includes communicating limitations of automated decisions and making user-facing corrections possible where outcomes affect opportunities or reputation.

An education platform automatically labels students as “at risk” using attendance data, then restricts scholarships. Attendance can be missing for reasons unrelated to academic engagement, and the model may disproportionately penalize students who lack reliable devices. Even a statistically accurate classifier in aggregate does not by itself justify consequential individual decisions. Require justification, appeal, monitoring, and human governance.

Analyze a proposal to publish an AI-generated ranking of student reliability. List the claimed benefits, foreseeable harms, omitted stakeholders, proxy variables, and alternatives. Design a review that includes people affected by the ranking and provides a correction path. Write a decision memo that is candid about uncertainty and refuses to use an unsupported accuracy number.

### Investigation: evaluate a harmful predictive feature
A support portal proposes a “dropout risk” score based on missed online activity. Examine who defines the positive label, how historical policy affects training data, and whether intervention changes the outcome being predicted. Build a stakeholder map emphasizing students with inaccessible connections and those who take approved alternative courses. Require an explicit appeal and correction process and identify evidence needed to justify the intended intervention. Explain why a high ranking correlation or a strong AUC alone does not validate punitive decisions. Propose a lower-risk alternative that lets students voluntarily request help without revealing an opaque score to unrelated staff.

### Ethical review can require refusing a feature
Engineers should ask whether the claimed benefit justifies potential harms before optimizing a proposed algorithm. In student analytics, absence from an online platform can be caused by limited access, disability, employment, or alternate learning arrangements. Treating inactivity as character failure creates a social conclusion unsupported by the data. Identify affected groups, alternative interventions, meaningful appeals, and oversight. Use statistical evaluation only within an ethically defensible purpose. A recommendation for voluntary support outreach may be safer than automatic punishment even if both could be technically implemented. Engineering responsibility includes clearly communicating uncertainty and resisting deceptive assertions about accuracy, fairness, or guaranteed outcomes. A design that cannot provide correction and accountability may be inappropriate to deploy.

## 8.2 Accessibility

**Accessibility: conceptual explanation**

Accessibility concerns keyboard navigation, perceivable information, text scaling and assistive-technology semantics. A custom button that works by mouse but cannot receive keyboard focus excludes users. Automated accessibility scans help identify patterns but require human testing for meaningful workflows.

### Engineering depth and worked reasoning

Accessibility is a property of interaction across diverse bodies, devices, and environments. It is not achieved by adding an icon or a high-contrast palette alone. Semantic structure, keyboard operability, assistive-technology compatibility, visible focus, readable error messages, appropriate contrast, and predictable behavior must be considered during design and testing. Accessibility failures are functional failures for the users excluded.

Use WCAG 2.2 as an evidence-based reference for web requirements while confirming the applicable legal and contractual obligations for a particular deployment. For a form, associate instructions and errors with inputs, preserve user data after validation errors, avoid keyboard traps, and test zoom and reflow on narrow screens. Simulations must expose their current parameter and output textually, not only through bar color.

A drag-and-drop timetable seems intuitive on a desktop but becomes unusable to keyboard-only users. Adding an aria-label to a canvas does not make the interaction operable. Provide equivalent buttons or structured controls that allow assignment and removal, then test the full workflow with keyboard and representative assistive technology.

Audit a reservation page at 200% zoom and on a narrow viewport. Navigate without a pointer, inspect programmatic labels, run a screen reader through status messages, and verify that a disabled action has an understandable explanation. Record steps to reproduce each barrier. Distinguish automated checks for detectable markup errors from human tests for comprehensibility and workflow completion.

### Investigation: manual accessibility verification
Take a form for reporting broken laboratory equipment. Navigate from page entry to confirmation using Tab, Shift+Tab, Enter, and Space without a mouse. At high zoom, verify that instructions and actions remain visible without horizontal scrolling. Deliberately submit missing data and check focus movement, associated error text, and preservation of previously entered answers. Use a screen reader to hear the name and value of a simulation control and its updated numerical output. Record the precise browser and assistive technology versions for reproducibility. Automated validators may catch missing labels; they cannot determine whether instructions are understandable to a first-time student.

### Accessibility needs complete user journeys
A form can pass a superficial color-contrast scanner while remaining impossible to use without a mouse. Evaluate focus order, clear labels, keyboard interaction, reflow, descriptive errors, and announced status changes from task start through task completion. Provide text output for interactive mathematical models because shape and color alone cannot convey their meaning. If a simulation uses a slider, test that keyboard arrow keys adjust values and that a screen reader exposes the control's name, range, and current setting. At high zoom, avoid horizontal overflow and obscured buttons. Accessibility requirements should appear in design acceptance criteria and automated regression checks where possible. Manual testing with representative users remains essential for meaning, comprehension, and actual usability.

## 8.3 Privacy

**Privacy: conceptual explanation**

Privacy engineering minimizes unnecessary personal data collection and limits processing purpose, retention and access. Encrypting a database does not justify retaining sensitive fields indefinitely. Logs and backups are part of the data system and require their own handling rules.

### Engineering depth and worked reasoning

Privacy engineering translates data-use promises into verifiable system constraints. Begin with purpose limitation: why is each field collected, who can access it, how long is it necessary, and what happens at deletion or correction? Map the entire data lifecycle, including caches, logs, backups, exports, analytics, and support screenshots. Authentication controls access to the system; authorization controls whether a particular user may access a particular record.

Design least-privilege permission rules and test them at resource boundaries. Protect secrets in transit and at rest where appropriate, but do not treat encryption as a replacement for data minimization. Define retention based on real obligations, not arbitrary forever storage. Include incident detection, notice processes, and deletion requests that account for technical constraints such as immutable backups.

A developer removes a student’s profile from the primary database while keeping full names and grades in search indices and debug logs. The interface reports “data deleted,” but the factual claim is false. A truthful system must define which records are deleted immediately, which are retained for documented reasons, and when copies in backup media expire or become inaccessible.

Produce a data inventory for enrollment and attendance records. Identify sensitive fields, lawful or institutional purpose assumptions, authorized actors, retention periods, key storage, and log redaction. Design negative authorization tests for cross-course queries. Explain which claims require consultation with the institution’s privacy office because regulations and policies vary by location.

### Investigation: personal-data flow mapping
Follow student email addresses from account creation through the database, application cache, audit log, metrics exporter, backup, and customer-support ticket. At each boundary mark purpose, access control, retention, and deletion semantics. Remove unneeded fields from analytics rather than relying solely on encryption. Simulate a cross-student authorization attempt and confirm that denial does not leak record existence through response differences. Prepare a truthful deletion explanation that identifies retained records required for legitimate institutional audit and the limits of backup deletion. Consult applicable law and institutional policy before claiming a particular retention period is compulsory.

### Data inventories precede security claims
A privacy policy can promise deletion, but engineers must inspect where the data actually flows. Personal information often appears in application logs, analytic events, cached responses, test copies, support tickets, and backups long after the primary row is removed. Map each processing purpose, recipient, retention rule, and deletion capability. Minimize collected fields before choosing encryption or access-control controls; preventing unnecessary collection is often the simplest risk reduction. Resource-level authorization must be checked when data are requested, not only when users log in. Securely redact observability data without making incidents impossible to investigate. Explain where legal or institutional requirements need expert interpretation rather than inventing universal retention mandates. Privacy engineering is measurable through inventory completeness, access tests, and audited lifecycle behavior.

## 8.4 Software Sustainability

**Software Sustainability: conceptual explanation**

Sustainability includes operational cost, energy consumption, maintainability and long-term support. A performance optimization that doubles infrastructure requirements may not be a net improvement. Measure resource usage against an explicit workload and avoid claims of environmental benefit without a defensible baseline.

### Engineering depth and worked reasoning

Software sustainability considers resource use across computation, storage, networking, hardware lifetime, and maintenance. Lower CPU use does not automatically imply lower environmental impact if the design increases data transfer, user retries, or discarded devices. Choose a meaningful functional unit—such as energy per completed enrollment transaction—and measure under representative workloads before making sustainability claims.

Techniques include efficient queries, cache design with sensible invalidation, reducing unnecessary polling, using scalable compression, optimizing image delivery, and scheduling nonurgent batch work where feasible. Every optimization must preserve correctness and accessibility. An API that halves transfer size but doubles failed requests might make overall resource use worse.

A team claims carbon neutrality from a synthetic benchmark using a single fixed energy coefficient, ignoring server utilization and regional electricity sources. The simulation may help teach sensitivity to assumptions, but cannot substantiate an environmental marketing claim. Separate measured energy, modeled electricity emissions, and policy-level claims; publish uncertainty transparently.

Instrument a representative user journey, record request counts and transferred bytes, measure response time and compute where feasible, and compare two designs under identical conditions. Change one factor at a time while retaining correctness checks. Present benefits and costs with uncertainty. Develop an optimization backlog and reject an improvement that degrades keyboard navigation or recovery behavior.

### Investigation: resource use per successful task
Compare an activity dashboard that polls every five seconds with one that retrieves updates when the user opens the page. For a hypothetical thirty-minute session, the polling version makes 360 requests; document how reconnects, caching, and page visibility would change that count. Measure or estimate bytes transferred, server work, and delay under clearly stated assumptions. Verify that reduced polling does not hide critical corrections or make the page inaccessible to assistive technology. The defensible claim is a reduction in measured work under an observed test case, not a universal carbon saving. Report the expected user benefit and the uncertainty in any conversion from energy use to emissions.

### Sustainable design uses an explicit functional unit
Comparisons of energy or bandwidth should keep user success fixed. If one design uses fewer server requests but causes users to repeat the same action, the improvement may disappear. Define a functional unit such as one successful grant submission, then include processing, storage, transfer, retries, and recovery overhead. Record device, workload, region, and measurement method. Simple simulation coefficients can teach that energy grows with task count, but they are not evidence of real environmental savings. Avoid claims about total carbon emissions without measured consumption and an appropriate emissions model. Efficiency changes must preserve correctness, privacy, and accessibility, since shifting burden to users is not a sustainable optimization. Report uncertainty and show enough procedure that another engineer could reproduce the comparison.

## 8.5 Integrated Engineering Studio: Professional practice

A speech-to-text system transcribes classroom discussions. Its users include people who never signed up but whose voices are recorded. The design must address consent, retention, transcription error appeals and accessibility of controls. Run keyboard-only and screen-reader tests on the consent dialog, and assess whether one-click “accept all” is coercive when rejection is hidden. Limit transcript access by purpose and role; ensure backups and diagnostics follow deletion policy. Energy measurements should be reported with workload, hardware and region rather than a generic claim that the product is sustainable.

### Studio case: privacy, accessibility, and resource use in a student support platform

A university wants to analyze attendance and course activity to identify students who may need support. The institution can offer useful assistance, but automated risk labels also create potential harm. Missing activity may reflect unreliable connectivity, disability, illness, caregiving, or alternative learning arrangements rather than disengagement. Before building a prediction feature, define the intended intervention, evidence that it helps, permissible data sources, appeal process, and institutional oversight.

Begin with data minimization. List every field: student identifier, attendance observations, enrollment history, communications, device metadata, and support notes. For each field specify purpose, retention, authorized recipients, and whether it is necessary at all. A general-purpose analytics feed should not receive detailed counseling notes merely because the database makes them easy to export. Test record-level authorization with deliberately unrelated student identities, and redact sensitive data from operational telemetry.

Next perform an accessibility walkthrough. A support form must operate by keyboard and at high zoom, with every error message programmatically associated with its input. A simulation representing risk estimates needs an accessible textual output and an explanation of uncertainty; a colored chart alone cannot convey the conclusion. Try the workflow on a small screen and with a screen reader, including what happens after a failed submission. Automated lint tools are not substitutes for people completing the task.

Investigate sustainability without overstating claims. Instrument a defined functional unit, such as one successfully completed support request, and measure CPU or energy consumption, transferred bytes, retries, and database writes where feasible. Compare a constantly polling dashboard with an event-notified update. A faster average response does not necessarily mean less energy, and synthetic watts-per-request models are only demonstrations of sensitivity until checked against real hardware and traffic.

The final decision memo must answer difficult questions: Could a student challenge a false label? How are support staff instructed not to treat a model score as a verdict? What happens when the platform has insufficient data? Who may authorize wider use? Which metrics reveal harm rather than merely adoption? Reject deployment if these questions have no defensible answers. Ethical engineering requires changing or abandoning attractive features when safeguards cannot justify their foreseeable consequences.

### Review of professional responsibility
Evaluate the student support platform from the perspective of someone incorrectly labelled as disengaged. They need to understand what information was used, whether they can correct factual errors, who sees the result, and what consequences follow. If the product cannot answer these questions, a model-quality metric does not fix the governance problem. Conduct keyboard and assistive-technology checks of the correction workflow, not only its homepage. Verify that access controls prevent a professor from viewing counseling notes unrelated to their responsibilities. If energy optimization delays urgent corrections or exposes personal data through shared caching, reject it despite lower resource use. The objective is a service that can be justified to the people affected by it, under explicit evidence and oversight.

# Fully worked questions

## Polling volume under a simple user-session model

A student support dashboard polls the server every five seconds for a continuous thirty-minute session. Ignoring connection failures and initial page-load requests, how many scheduled polling requests occur? What tradeoffs arise from replacing polling with event-driven updates?

**Analyze the assumptions.** Convert thirty minutes to 1,800 seconds. Divide by five seconds per scheduled poll: 1,800/5 = 360 polling requests per continuously active session under the stated interval model.

**Develop the result.** Multiply by representative session counts only after considering inactivity, browser background throttling, cache hits, payload size, and server cost. Event-driven notifications may reduce unnecessary requests but add connection management and recovery complexity.

**Check interpretation and failure cases.** Measure energy and bytes under the real workload before claiming emissions savings. Verify that change alerts remain accessible to keyboard and screen-reader users and that reconnecting clients reconcile missed updates.

**Answer.** 360 scheduled polls per continuous thirty-minute session in this simplified model.

## Data-retention arithmetic and its boundaries

A hypothetical application records one thousand non-identifying analytics events per day and retains a rolling thirty-day window. At a steady rate, approximately how many events are retained? Why does the count not justify keeping personal data?

**Analyze the assumptions.** At a steady rate of 1,000 events per day across thirty complete days, approximate stored event count is 1,000 × 30 = 30,000. A real system must specify whether the current partial day is counted.

**Develop the result.** Data volume is not a privacy authorization. Purpose, necessity, access control, security, and applicable institutional or legal policies govern retention. Backups, caches, exports, and logs may hold additional copies beyond the primary window.

**Check interpretation and failure cases.** Test deletion or expiration at the window boundary and describe exceptions transparently. If the events contain identifiable students, determine whether the proposed collection is needed at all and document who approved the processing.

**Answer.** Approximately 30,000 rolling events at steady rate; retention requires separate justification.

## Accessibility when a simulation has a visual chart

A simulation displays a colored bar chart and an input slider. A keyboard-only reader cannot determine the currently selected value, and a screen reader announces only “graphic.” Describe a compliant interaction design and the tests it needs.

**Analyze the assumptions.** Give the input an explicit label, keyboard-operable range limits, and a programmatically exposed current value. Present the calculated output as text with its units and assumptions. A graphic may supplement these elements but should not be the sole communication channel.

**Develop the result.** Test Tab and arrow-key interaction, focus visibility, and updated output announcements. Verify the chart remains usable at high zoom and on narrow screens. A text summary should describe the relevant trend without relying on color names.

**Check interpretation and failure cases.** Automated markup linting helps detect unlabeled elements, but a manual screen-reader walkthrough is necessary to evaluate whether someone can understand the model and complete the learning task.

**Answer.** Use accessible controls, text output, and manual assistive-technology verification; color-only visualization is insufficient.

# Further reading

- IEEE Computer Society: SWEBOK V4.0 Topics: https://www.computer.org/education/bodies-of-knowledge/software-engineering/topics
- ISO/IEC 25010:2023: Product quality model: https://www.iso.org/standard/78176.html
- NIST SP 800-218: Secure Software Development Framework: https://csrc.nist.gov/pubs/sp/800/218/final
- W3C Web Content Accessibility Guidelines (WCAG) 2.2: https://www.w3.org/TR/WCAG22/
