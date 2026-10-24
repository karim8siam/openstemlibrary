# Unit 5: Planning

*Editorial draft; not approved for live publication.*

## Classical Planning
**Classical Planning: conceptual explanation**

### Classical planning as state transformation
Classical planning asks for a sequence of actions that transforms an initial state into one satisfying a goal. A common formalism represents a state as a set of ground facts and an action by preconditions, added effects and deleted effects. In a simple robot world, Move(RoomA,RoomB) requires At(RoomA) and Connected(RoomA,RoomB), deletes At(RoomA), and adds At(RoomB). An action is applicable only when its preconditions are satisfied. The next state is (current facts minus deleted facts) union added facts, assuming the chosen formalism uses closed-world Boolean semantics.

Suppose the robot starts at Depot with a parcel available there. Pickup requires At(Depot) and ParcelAt(Depot), then adds HoldingParcel and deletes ParcelAt(Depot). Deliver requires At(Client) and HoldingParcel, then adds Delivered and deletes HoldingParcel. A planner that moves directly to Client without pickup cannot complete the goal. Searching only over locations loses the parcel status and may incorrectly report success. This illustrates that planning state variables encode action preconditions, not merely a map.

Breadth-first search finds a minimum-number-of-actions plan when actions have unit cost and the reachable state graph is finite. If actions have energy, duration or financial costs, uniform-cost search may be needed for minimum total cost. A heuristic based on the number of unmet goals can help but is not always admissible; one action may satisfy several goals at once, and another may undo earlier work. A relaxed planning graph that ignores delete effects can estimate lower bounds, but it may overlook resource conflicts and produce overly optimistic estimates. Whether that heuristic is admissible depends on how it is derived.

Partial-order planning represents only necessary ordering constraints. If two independent parcels can be prepared in either order before loading, imposing an arbitrary total order needlessly restricts flexibility. Causal links track why one action must precede another and identify threats from actions that would remove a required fact. This is different from simply permuting action names. A schedule can represent concurrent actions after checking that their preconditions and effects do not conflict.

For a lab, model a three-room delivery task and enumerate all plans up to six actions. Check every plan by independently executing its transitions, not merely by trusting the planner's declared 'goal achieved' flag. Inject an action whose delete list is accidentally omitted: the model may let the parcel remain at both locations. A good validation harness asserts invariants such as 'the parcel is in at most one location or carried' and records which transition first violates them.

## Temporal Planning
**Temporal Planning: conceptual explanation**

### Temporal planning, deadlines and resource conflicts
Real tasks have duration. A maintenance technician may inspect a pump for 20 minutes while another calibrates a sensor, but one technician cannot work at two distant sites simultaneously. A temporal plan therefore assigns start and end times to actions and constraints between them. Simple temporal networks use difference constraints such as start_B-start_A≥20 or end_B≤90. These can be transformed into inequalities on event times and checked for consistency using shortest-path reasoning on an appropriately constructed constraint graph.

Suppose task A lasts 30 minutes, task B lasts 20 minutes and task C lasts 15 minutes. If B and C both require A to finish, and different personnel can execute them concurrently, total makespan is 30+max(20,15)=50 minutes. If the same person must do B and C sequentially, the best possible makespan is at least 30+20+15=65 minutes, excluding travel. A planner that counts only summed durations would miss the 50-minute parallel schedule; a planner that assumes unlimited resources would incorrectly claim 50 minutes when only one worker is available.

Critical-path analysis identifies the longest sequence of dependency-constrained tasks, giving a lower bound on the makespan under unlimited resources. Resource-constrained project scheduling is harder because mutually exclusive uses can force additional sequencing. To avoid a misleading demonstration, list the number and capacity of each resource. A one-person machine is not interchangeable with a pool of ten workers, and two identical actions may compete for a shared battery or network bandwidth even if they do not use the same room.

Deadlines can be hard constraints or soft penalties. If a delivery must occur by 15:00 for safety, representing lateness as a small utility penalty may authorize invalid behavior. A hard deadline should reject plans that cannot satisfy it. If lateness is economically undesirable but permissible, a cost term may be appropriate. Calendar uncertainty further complicates scheduling: an estimated duration of 20 minutes is not a guarantee. Stochastic scheduling can reserve slack or optimize the probability of completing before a deadline.

Implement a toy planner with task durations, precedence edges and a configurable number of workers. Verify the critical-path lower bound against exact enumeration of schedules for tiny instances. Reject cyclic precedence constraints and negative durations. Let the user add a shared machine conflict and observe the change in makespan. A simulation that draws a Gantt chart should explain whether it demonstrates feasibility, optimality for a bounded instance, or only a heuristic schedule.

## Partial Observability
**Partial Observability: conceptual explanation**

### Partial observability and belief-space planning
A planning problem becomes partially observable when the agent cannot directly inspect all state variables needed for decisions. Rather than treating a sensor reading as truth, a probabilistic agent maintains a belief b(s), a distribution over candidate states. After action a and observation o, the belief is updated in two stages: predict b^-(s')=∑_s T(s'|s,a)b(s), then condition b'(s') proportional to O(o|s',a)b^-(s'). The normalization constant is the probability of the observation under the predicted belief.

In a two-room search task, let the target initially be in A with probability 0.7 and B with 0.3. A sensor checking A has detection probability 0.9 when the target is there and false-alarm probability 0.2 otherwise. If the sensor reports no target, the probability that the target remains in A is (0.1×0.7)/(0.1×0.7+0.8×0.3)=0.07/0.31≈0.226. The agent should therefore redirect attention toward B, but only after comparing the cost of travel and another measurement. A deterministic controller that equates a negative signal with 'certainly empty' can make a poor choice.

A partially observable Markov decision process, or POMDP, chooses policies mapping beliefs or observation histories to actions. Its exact solution can be computationally demanding because even a finite hidden state space induces a continuous belief simplex. Point-based algorithms approximate value functions on sampled beliefs, while model-predictive approaches replan after each observation. Accuracy depends on transition and observation models, and approximation error should be assessed on tasks small enough to solve exactly when possible.

Information-gathering actions are sometimes valuable even when they do not move the system toward the physical goal. A robot may spend time inspecting a corridor to avoid an expensive dead end. This is active sensing. In a task with inspection cost 2 and possible wasted travel cost 20, sensing can be rational when uncertainty is high, but not when the probability of blockage is negligible. The expected value of information connects planning directly to decision theory.

For a simulator, let learners vary the prior, sensor sensitivity and false-alarm rate and view the normalized posterior after positive or negative observations. Test that both posterior probabilities sum to one, including extreme cases. Handle an impossible observation by reporting the model inconsistency rather than dividing by zero. Show trajectories from two different hidden states that produce the same observation, explaining why belief tracking cannot be replaced by a single guessed state without losing uncertainty.

## Resource Constraints
**Resource Constraints: conceptual explanation**

### Resource constraints, invariants and feasibility
Planning with resources adds state variables such as battery energy, inventory, staff time or available bandwidth. Resources may be renewable, like a machine becoming free after a task, or consumable, like a fixed amount of fuel. A plan is feasible only if every intermediate state respects resource constraints. Merely checking that the final state has enough resources can miss an illegal temporary deficit. In a delivery example, a route consuming 6, 8 and 5 battery units requires at least 19 units before any recharge; starting with 15 units is insufficient even if the robot might recover energy later on the route.

A monotonic resource decreases with consumption and cannot increase unless a replenishment action is explicitly modeled. For battery charge E, a movement with cost c requires E≥c and updates E'=E-c. A recharge action may increase E only at approved charging stations, perhaps with duration constraints. An invariant E≥0 should hold after every action. Another invariant may limit storage capacity or enforce that a fragile item cannot be carried simultaneously with hazardous material. These constraints are properties of reachable states, not optional preferences to optimize.

Resource bounds can prune enormous planning trees early. If a remaining sequence has a proven lower-bound energy requirement exceeding available energy, no continuation through that sequence is feasible. However, an optimistic estimate is useful only if it is a valid lower bound. If a heuristic overestimates energy consumption it might prune a valid plan. Introduce resource dominance carefully: one state may dominate another when both have equivalent relevant task status and location but the first has no less remaining resource and no more accrued cost, under assumptions that additional resource can never hurt and histories do not affect future transitions.

Multiple resources create tradeoffs. A schedule minimizing energy may take longer, and one minimizing time may require expensive staff overtime. Multiobjective planning can generate a Pareto frontier rather than imposing one unexplained set of weights. Plan X may cost 10 minutes and 8 units of energy; plan Y may cost 12 minutes and 5 units. Neither dominates the other. A chosen operating policy must specify which tradeoff it accepts.

For a lab, implement a bounded resource-aware path planner and independently replay returned actions against the resource ledger. Add a recharge station, a blocked edge and a maximum payload constraint. Test off-by-one boundaries at E=c, E=c-1 and E=0. The final report should distinguish a proof of plan feasibility for the model from a guarantee that sensors, batteries or charging infrastructure will behave exactly as assumed in the real environment.

## Integrated Case Study and Model Limitations
**Integrated investigation for Planning.** The examples below illustrate the precise mathematical and operational constraints of the unit.

### Case study: laboratory research equipment scheduling
A university laboratory has one microscope, one spectrometer and two trained technicians. Three experiments require specific sequences: sample preparation, microscope inspection and spectrometry. Some preparation can occur in parallel, but the microscope can process only one sample at a time. One sample expires if spectrometry begins more than 45 minutes after preparation. This is a temporal, resource-constrained planning problem, not a shortest-path search with decorative labels.

Define actions with durations, preconditions, add effects and delete effects. Preparation produces Prepared(sample) and records the time; microscopy requires Prepared(sample) and an available microscope; spectrometry requires an inspected sample, available spectrometer and an unexpired validity window. To avoid double booking, represent equipment capacity explicitly. If Experiment A and Experiment B each need 20 minutes of microscope time, neither can overlap with the other even if the technicians are different.

Begin with a hand-built two-experiment instance where exhaustive schedule enumeration is possible. Verify that the model finds a feasible schedule, then add a third experiment and compare a greedy earliest-deadline heuristic to exact search under a fixed small state bound. Record makespan, deadline misses, equipment utilization and computational effort. If the heuristic returns a longer schedule, explain the decision that caused the difference. If no schedule exists, produce a short contradiction witness when possible rather than relying on a timeout.

Add uncertainty in a technician's arrival time. A deterministic plan may have zero slack, so a five-minute delay causes expiry. A conservative plan can add slack or include a replanning policy triggered by delays. This moves the model toward stochastic or contingent planning; do not claim classical planning alone handles the new uncertainty. Incorporate a human override, safety-training eligibility and an event log, and distinguish institutional permission from algorithmic feasibility.

A good student submission includes a machine-readable problem specification, an independently checked schedule, a resource timeline and a sensitivity analysis. Report which constraints have been verified mathematically, which times are assumptions, and what is not captured by the classroom model. Simulations are valuable because they reveal how several plausible-looking local decisions can together produce an infeasible global plan.

### Research exercise: compile planning goals into constraints
For a small finite planning horizon, Boolean decision variables can encode whether each fact holds at each time and whether each action occurs. Suppose an agent has possible locations A and B and actions MoveAB, MoveBA and Wait. Let AtA_t and AtB_t be state variables at time t; require exactly one location at each step. If MoveAB_t is selected, require AtA_t and ensure AtB_{t+1}. Additional frame constraints prevent unrelated facts from spontaneously changing. A SAT solver could then check whether a goal state is reachable in at most T steps, although real planners use many richer encodings and heuristics. This construction shows the relationship between search, logic and planning without asserting that every plan can be found efficiently.

A crucial distinction is between finding any satisfying assignment and optimizing one. Satisfiability over a fixed horizon answers whether a plan exists; minimizing number of steps requires checking horizons in increasing order or using an optimization encoding with a sound objective. If action costs differ, minimum-step plans need not minimize total cost. If two actions can happen concurrently, the encoding must say which pairs are allowed together, whether their effects conflict and what resource capacity is available. Ambiguous concurrency can make a mathematically consistent assignment physically impossible.

### State transition and invariants
Develop a two-room package-delivery task with pickup and drop-off. Define facts AtA, AtB, ParcelAtA, Holding and Delivered. The agent starts at A while the package is at A and must deliver at B. Pickup requires AtA∧ParcelAtA, adds Holding, and removes ParcelAtA. MoveAB requires AtA and replaces AtA with AtB. Deliver requires AtB∧Holding, adds Delivered and removes Holding. The plan Pickup→MoveAB→Deliver uses three actions. A naive model permitting pickup without deleting ParcelAtA violates the invariant that the package has exactly one physical status. An exhaustive simulator can find that defect by comparing state transitions with a separately written invariant checker.

Use a search engine that records the full state before and after every action. For small tasks, independently enumerate all action sequences up to length six and verify that exactly the sequences satisfying every precondition and reaching Delivered count as solutions. Some longer sequences may also reach the goal after useless waits; reporting a unique plan would be incorrect without an optimality criterion. Verify every transition, not only the final state. A plan that reaches the goal by teleporting between locations must be rejected even if its terminal facts look valid.

### Replanning with uncertainty
Now introduce a probability that the corridor between A and B is blocked. A classical plan assumes known preconditions at execution; a contingent plan may include checking the corridor, then following a branch based on the observation. To model a sensor correctly, distinguish the hidden Blocked variable from the ObservedBlocked report, which may include false positives and false negatives. If the sensor reports 'clear' incorrectly with probability 0.1, a route with severe failure cost may justify another observation. A utility model can determine whether that additional sensing is worthwhile. Do not encode uncertainty merely by drawing a randomly animated wall while leaving the planner unaware of possible changes.

A stronger experiment compares three policies: a fixed plan ignoring blockage, a policy that replans after failed movement, and a policy that checks before moving. Under each fixed set of parameters, sample the same sequence of environmental events for all policies, and measure success frequency, mean action count, sensing cost and missed deadlines. Differences between policies should be reported with sampling variability. Exact expected values can be calculated for a two-state toy world and compared against simulated averages. This checks both the probability engine and the decision logic.

### Deadline and human supervision
If the delivery must occur before a deadline, resource and temporal constraints should determine feasibility. A policy that finds a path too late has not solved the entire planning problem. For a high-stakes transfer, the simulator should include an abort or escalation action and a traceable policy version. A student should be able to show the exact precondition, transition or action-selection rule responsible for any failure. This combination of formal preconditions, finite satisfiability experiments and uncertainty-aware replanning is a more rigorous planning lesson than a path animation presented without assumptions.

### Invariant-based planning validation
A plan validator should accept a proposed action sequence only after replaying each action from the initial state. At step t, verify that preconditions hold, calculate the successor state and check global invariants before continuing. This catches two errors hidden by final-state checking: an agent may temporarily consume more energy than it has, or create a duplicate copy of an object that later disappears. State the invariants mathematically: energy E_t≥0, at most one parcel-location predicate true, and no movement while the door is open. Test an intentionally illegal sequence and record the exact first violated condition. If a planner times out without finding a plan, its status is unknown unless the search space was exhaustively covered under a finite bound.

### Worked question: STRIPS action feasibility
A robot is at Depot with a parcel there. Pickup requires AtDepot and ParcelAtDepot, then adds HoldingParcel. Deliver requires AtClient and HoldingParcel. Can the robot deliver without first performing Pickup?

**Model the question**
Inspect the Deliver preconditions: both AtClient and HoldingParcel must be true. AtClient can be obtained by moving, but HoldingParcel is initially false.

**Calculate or derive**
Under the given action library, Pickup is the action that makes HoldingParcel true. Therefore any valid delivery plan must contain Pickup before Deliver; a route that reaches Client alone is insufficient.

**Check assumptions and boundaries**
If the model allowed an alternative action to obtain the parcel at Client, the conclusion could change. The proof is relative to the given actions and initial facts.

**Answer:** No. Pickup must precede Deliver under the specified model.

### Worked question: Critical path and resource restriction
Task A takes 30 minutes. After A, tasks B (20 minutes) and C (15 minutes) become available. Find the fastest makespan with unlimited workers and with one shared worker for B,C.

**Model the question**
With independent workers, B and C can overlap once A finishes. The parallel makespan is duration(A)+max(duration(B),duration(C)).

**Calculate or derive**
Parallel result: 30+max(20,15)=50 minutes. With exactly one worker for both tasks and no preemption, B,C must run sequentially after A, so 30+20+15=65 minutes.

**Check assumptions and boundaries**
The single-worker result assumes that A does not consume the same worker in an overlapping way and there are no setup or travel delays. State resource constraints before inferring makespan.

**Answer:** 50 minutes in parallel; 65 minutes under the specified shared-worker restriction.

### Worked question: Belief update after negative sensor reading
A hidden target is in room A with probability 0.7. A sensor has detection probability 0.9 if the target is in A and false-positive rate 0.2 if in B. After a negative reading, compute P(A|negative).

**Model the question**
The likelihood of a negative sensor result if the target is in A is 0.1; if in B it is 0.8. The prior probabilities are 0.7 and 0.3.

**Calculate or derive**
P(A|negative)=0.1×0.7/(0.1×0.7+0.8×0.3)=0.07/0.31≈0.225806. The numerator is the joint probability of a target in A and receiving a negative test, which is 0.07. The competing joint probability for B and a negative report is 0.24; their sum is the total probability of the negative observation.

**Check assumptions and boundaries**
The answer is not zero; a negative test can miss the target. The posterior for room B is 1-0.225806≈0.774194 and sums to one.

**Answer:** Posterior for room A ≈22.58%.
