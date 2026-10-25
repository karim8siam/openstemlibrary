# Unit 6: Cell behavior

## Introduction

Cells are mechanical and chemical agents of their environments. Adhesion, migration, polarity, and matrix interactions form a coupled system: attachment transmits forces, protrusion redistributes molecules, and the extracellular environment responds mechanically and biochemically. Neither speed nor apparent cell shape is an adequate stand-alone measure of migration. An unbiased random walk can generate noticeable short-term displacements; an adhesion can strengthen or weaken under force according to its molecular mechanism. Students should use trajectories, geometric measurements, and controlled substrate properties to separate correlation from force-dependent causation. The simplified models used in this unit are explicit null hypotheses, not complete descriptions of tissues.



## 6.1 Adhesion

### Central mechanism and vocabulary

Cells attach to neighbors and extracellular matrix through adhesion molecules whose cytoplasmic partners communicate with the cytoskeleton. Integrins can link extracellular ligands to actin-associated complexes and respond to force; cadherin-mediated contacts help organize cell–cell junctions. Adhesion involves binding kinetics, receptor clustering, mechanical loading, and signaling. Increasing adhesive ligand density can initially aid spreading but may eventually reduce migration speed by making release difficult. A single-cell adhesion assay and a tissue-level barrier measurement are not interchangeable.

### Why this mechanism matters

The central issue in **adhesion** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Cells attach to neighbors and extracellular matrix through adhesion molecules whose cytoplasmic partners communicate with the cytoskeleton. Description and mechanism are not equivalent.

Consider a thought experiment involving **adhesion**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms. For this topic, examine the meaning of force, displacement, adhesion, and geometry on matched scales; ask which additional time point, reference marker, or independent assay would break the ambiguity. This is especially important because correlated substrate changes can make population averages deceptively stable even when individuals change substantially.

### Mechanism from molecular to cellular scale

A mechanism for adhesion should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: A single-cell adhesion assay and a tissue-level barrier measurement are not interchangeable.

### Experimental evidence and its interpretation

Compare spreading area on surfaces with controlled ligand density, measuring traction and cell viability in parallel. To examine single-bond mechanics, analyze lifetimes across applied forces while avoiding wholesale extrapolation from one molecule to an entire focal adhesion. Include nonbinding surfaces and matched substrate stiffness controls.

**Measure forces and trajectories.** Begin with a prespecified comparison that changes one primary factor and holds other plausible causes as constant as practicable. For adhesion, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on adhesion, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for adhesion.

### Competing explanations, limitations, and quality controls

The simplest slip-bond equation predicts shorter lifetime as force increases, yet some biological bonds display catch-bond behavior in particular force regimes. Adhesion protein intensity is not itself a calibrated force reading.

A persuasive conclusion about adhesion has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in adhesion after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A cell spreads more widely on a highly adhesive surface but migrates more slowly than on a moderately adhesive surface. The simple story that stronger adhesion always improves movement therefore fails. Productive crawling requires traction at the front and timely adhesion release at the rear; excessive stable attachment can impede net translation. A laboratory changes ligand density while matching substrate stiffness, uses traction microscopy to measure force distribution, and tracks cells over several hours. At the molecular scale, bond lifetime under force can follow a slip-bond approximation for some adhesive interactions. Other bonds show catch-bond behavior, and multi-protein adhesion structures redistribute loads dynamically. Students should distinguish lifetime of a single idealized bond from total persistence of a cellular contact. That distinction links the simulator's force-dependent curve to a realistic multiscale hypothesis.


## 6.2 Migration

### Central mechanism and vocabulary

Directed cell migration involves polarity establishment, protrusion at the front, adhesions that transmit traction, and coordinated rear release. Cells can also migrate with amoeboid modes or within three-dimensional environments that require distinct mechanics. The speed and persistence of a trajectory answer different questions: a cell may move quickly but return near its starting point. Chemotaxis describes directional bias relative to a gradient; random motility can look directional over a short observation window by chance.

### Why this mechanism matters

The central issue in **migration** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Directed cell migration involves polarity establishment, protrusion at the front, adhesions that transmit traction, and coordinated rear release. Description and mechanism are not equivalent.

Consider a thought experiment involving **migration**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for migration should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Chemotaxis describes directional bias relative to a gradient; random motility can look directional over a short observation window by chance.

### Experimental evidence and its interpretation

Track cell centroids in a controlled chemical gradient and compare observed displacement parallel to the gradient with a gradient-free condition. Estimate mean-square displacement across time lags to distinguish persistent from diffusive movement. Use fiduciary marks to correct stage drift and avoid excluding slow or dividing cells without a predefined rule.

For migration, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on migration, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for migration.

### Competing explanations, limitations, and quality controls

A two-dimensional random-walk model is an instructive null case, not a universal migration law. Cells can alter shape without translating, and imaging intervals that are too long can conceal reversals or division events.

A persuasive conclusion about migration has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in migration after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A cell travels a convoluted 120-µm path but ends only 30 µm from where it started. Its path length, instantaneous speed, and net displacement answer different questions. In an isotropic random-walk null model, mean-square displacement grows proportionally to time; directed migration can generate a stronger displacement bias along an environmental gradient. The experiment tracks many cells at fixed imaging intervals and estimates movement along and across the gradient separately. Drift of the microscope stage can masquerade as weak chemotaxis, so stationary reference beads are crucial. If a subset of slow cells disappears from analysis because short trajectories are discarded, the remaining sample may overestimate migration speed. The learning goal is to ask whether a visually striking track exceeds the distribution expected from undirected motion, rather than selecting one appealing cell to represent the population.


## 6.3 Polarity

### Central mechanism and vocabulary

Polarity means an asymmetric distribution of structures or biochemical activities that supports oriented function. Epithelial apical–basal polarity sorts membrane proteins into different surface domains and organizes junctional barriers. Migrating cells exhibit front–rear differences in actin dynamics, phosphoinositide signaling, and trafficking. Symmetry breaking may be initiated by external gradients or stochastic local amplification, then stabilized by feedback and cytoskeletal transport. Polarity can be transient and reorganize in response to altered environment.

### Why this mechanism matters

The central issue in **polarity** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Polarity means an asymmetric distribution of structures or biochemical activities that supports oriented function. Description and mechanism are not equivalent.

Consider a thought experiment involving **polarity**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for polarity should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Polarity can be transient and reorganize in response to altered environment.

### Experimental evidence and its interpretation

Image two polarity markers and quantify their angular distributions around the same cell boundary. Perturb one proposed transport or feedback component, then ask whether asymmetry magnitude, orientation, or persistence changes. Include cell-shape controls because an elongated cell can bias naive edge-intensity measurements.

For polarity, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on polarity, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for polarity.

### Competing explanations, limitations, and quality controls

A polarized marker is a readout, not necessarily the cause of polarity. Projected imaging can hide apical and basal domains, and population-averaged fluorescence may conceal cells with opposite polarization directions.

A persuasive conclusion about polarity has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in polarity after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A polarized epithelial culture exhibits a marker on one cell surface and a second marker on another. The organization helps maintain directional transport, but it may be disrupted when a wound induces cells to migrate. In a movie, the first marker seems to disappear while protrusive actin becomes enriched on the advancing edge. The investigator must establish whether the cells lost apical–basal polarity, reorganized into a front–rear axis, or simply changed orientation relative to the imaging plane. Three-dimensional z-stack acquisition and a junction integrity assay reduce that ambiguity. A signaling inhibitor that blocks edge accumulation might also slow wound closure by affecting metabolism, so a rescue strategy and viability controls strengthen causal inference. Students should describe both magnitude and direction of polarity and avoid inferring an intrinsic axis from population-averaged fluorescence alone.


## 6.4 Extracellular matrix

### Central mechanism and vocabulary

The extracellular matrix contains structural proteins, proteoglycans, and associated factors that provide mechanical context and biochemical cues. Collagen networks, laminins, fibronectin, and hydrated polysaccharides vary among tissues and remodel under cellular forces and enzyme activity. Substrate stiffness can influence differentiation and migration through mechanotransduction; however, ligand composition, pore size, and viscoelastic response often covary with stiffness in experimental materials. ECM is an active part of the tissue system, not passive packing material around cells.

### Why this mechanism matters

The central issue in **extracellular matrix** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: The extracellular matrix contains structural proteins, proteoglycans, and associated factors that provide mechanical context and biochemical cues. Description and mechanism are not equivalent.

Consider a thought experiment involving **extracellular matrix**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for extracellular matrix should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: ECM is an active part of the tissue system, not passive packing material around cells.

### Experimental evidence and its interpretation

Grow cells on hydrogels with matched ligand density but differing elasticity and assay morphology, traction, and a downstream mechanosensitive reporter. Measure the actual gel modulus rather than relying only on a vendor nominal value. Compare two-dimensional substrates with a three-dimensional matrix only after stating geometric and transport differences.

For extracellular matrix, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on extracellular matrix, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for extracellular matrix.

### Competing explanations, limitations, and quality controls

A stiff substrate effect may be mediated by altered adsorption or surface chemistry. Collagen density affects both pore structure and stiffness, so interpreting a single perturbation as purely mechanical can be misleading.

A persuasive conclusion about extracellular matrix has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in extracellular matrix after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

Two hydrogels have nominal elastic moduli of 1 and 20 kPa, and cultured cells show different spreading areas. A stiffness-sensitive mechanism is plausible, but manufacturing changes might also alter surface ligand adsorption, pore structure, or diffusion of medium components. A controlled experiment quantifies ligand density and mechanical response of each gel before seeding the same authenticated cell line at matched density. The student records spreading, traction stress, and a mechanosensitive nuclear reporter over time. If the higher-modulus surface increases nuclear accumulation while a ligand-blocking condition reverses the effect, the result supports a mechanically linked signaling account, yet it still does not isolate one direct molecule. Three-dimensional collagen matrices add geometry and remodeling, making direct comparison with a flat gel more complex. Mechanical context should be treated as part of the biological treatment, not a background nuisance.


## Fully worked problems

### CB-U6-P1: Slip-bond force dependence

**Question:** An idealized slip bond has unloaded lifetime τ0=100 s and characteristic molecular distance xb=0.4 nm. At 10 pN and kBT=4.1 pN·nm, estimate lifetime.

- 1. Use τ=τ0 exp[−F xb/(kBT)] for a simple slip-bond model.
- 2. Compute the dimensionless exponent −(10×0.4)/4.1≈−0.9756.
- 3. Calculate exp(−0.9756)≈0.377.
- 4. Therefore τ≈37.7 seconds under this model.
- 5. Catch bonds and multi-bond adhesions can behave differently; do not generalize this result to every cell adhesion complex.

**Verified final result:** About 37.7 s

### CB-U6-P2: Two-dimensional random migration

**Question:** For a two-dimensional unbiased random-walk model with diffusion-like motility D=0.8 µm²/min, find RMS displacement after 25 minutes.

- 1. For an isotropic two-dimensional diffusive model, mean-square displacement is 4Dt.
- 2. Compute MSD=4×0.8×25=80 µm².
- 3. Take square root: RMS displacement=sqrt(80)=8.94 µm.
- 4. This statistic measures displacement from origin, not total trajectory path length.
- 5. Persistent directionality, confinement, chemotaxis, and tracking error change the fitted scaling law.

**Verified final result:** About 8.94 µm RMS displacement

### CB-U6-P3: Migration directionality index

**Question:** A cell follows a 120-µm tracked path but ends 30 µm from its initial position. Compute a straightness index and explain its limitations.

- 1. Straightness index is net displacement divided by total path length.
- 2. Use the same length unit for numerator and denominator.
- 3. Compute 30/120 = 0.25.
- 4. A low index can indicate turning or retracing; it does not alone identify biased chemotaxis.
- 5. State imaging interval, track censoring rules, and stage-drift correction before comparing cells.

**Verified final result:** Straightness index = 0.25



## Integrative study: migrating cells on patterned extracellular matrix

A researcher places motile cells onto a patterned hydrogel containing alternating bands of low and high matrix-ligand density. Over several hours cells preferentially occupy one band. The result may involve adhesion, migration direction, altered proliferation, or survival. A final occupancy image cannot distinguish movement toward a region from differential retention or cell loss. Begin by tracking individually labeled cells from the moment of plating, recording their position, area, orientation, and division events. Include fiducial markers fixed to the substrate to correct stage drift. A patterned experiment is particularly vulnerable to optical or staining differences between bands, so quantify detection sensitivity in each region.

The force-generating and moving machinery should be measured separately. Adhesion complexes couple to the cytoskeleton, and protrusion forces must be balanced by rear release. A simple slip-bond lifetime model decreases exponentially with force, but a mature adhesion may contain interacting bonds that do not follow this form. Varying substrate stiffness without controlling ligand presentation can change both chemistry and mechanics. Ideally, compare patterns that independently vary each factor. Track traction fields or substrate deformations while observing focal adhesion markers; high marker intensity is only a proxy for molecular abundance unless calibrated against force.

A null model for undirected two-dimensional migration predicts mean-square displacement 4Dt for effective diffusivity D. In a patterned setting with directional gradients and confinement, that simple law is not automatically valid. Plot mean-square displacement over time lags and inspect whether migration is persistent, diffusive, or biased. A cell that moves fast in circles can have a much smaller net displacement than one that moves more slowly in a consistent direction. A straightness index complements speed, but neither proves chemotaxis without a defined external orientation.

Polarization provides another dimension: a cell can orient its front–rear axis before appreciable translation, or maintain an apical–basal axis in a stationary epithelial sheet. Measure the location of polarity markers relative to the matrix pattern and to cell shape. The result of this capstone is a proposal for disentangling adhesion preference, motion, polarity, mechanical constraints, and cell birth or death. It should include a plan for biological replicates, uncertainty summaries, and at least one control that breaks the tempting but unsupported inference that occupying a region means migrating toward it.

## Unit synthesis and interpretation

A migration-analysis capstone begins with two tracks: one 100 µm long ending 10 µm from its start, and another 45 µm long ending 40 µm away. The first has greater path length while the second has greater net displacement and straightness. A randomized motility model helps distinguish whether either displacement exceeds chance expectations; a directional gradient supplies an external reference axis. But substrate ligand density, stiffness, and cell polarity may change together. An experiment therefore uses matched hydrogels, fiducial drift markers, and independent cell-viability estimates. The model of a single slip bond under force is not the same model as attachment stability of an entire cell. Students should identify two routes by which an apparent migration difference could arise without changing motor activity, such as stronger rear adhesion or cell division along a track.

## Interactive model specifications

### Ideal slip-bond lifetime

**Question tested by the model:** what behavior is predicted for a simple slip bond under tensile loading? Lifetime follows τ=τ0 exp[−Fxb/(kBT)], here using τ0=100 s and kBT≈4.1 pN·nm. At F=10 pN and xb=0.4 nm, lifetime is about 37.7 s. Increasing force shortens lifetime under this model. That trend cannot represent every integrin or cadherin interaction because force can stabilize some catch-bond states and whole adhesive structures distribute force among many bonds. Interpret the curve as an explicit falsifiable baseline for one molecular-scale process.

### Random-migration RMS distance

**Question tested by the model:** what displacement scale results from unbiased two-dimensional diffusive migration? The mean-square displacement is 4Dt and the plotted root-mean-square displacement is sqrt(4Dt). With D=0.8 µm²/min and t=25 min the prediction is about 8.94 µm. This is the square root of the average squared *net displacement*, not the total distance a cell walks along its path. Persistent polarity, directed chemical gradients, confinement, and tracking noise can break the predicted scaling. Compare a measured trajectory distribution against this null model rather than labeling every noticeable displacement as chemotaxis.

