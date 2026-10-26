# Unit 6: Earthquake Sequences, Statistics, and Tectonic Context

## Guiding question

How should catalogs and fault records be interpreted without predicting individual earthquakes?

**Fictional unit investigation.** A fictional region has one large mainshock, a dense aftershock sequence, and a temporary sensor deployment that lowered the detection threshold. Students compare observed counts under incompatible catalog-completeness regimes.

## Physical context

Catalog counts are conditional on instruments, magnitude scale, study region and observation window. Statistics can describe patterns and provide probabilistic scenarios but cannot reliably specify the time, location and magnitude of an individual future event.

## Learning workflow

Before beginning, distinguish the scientific question, the measured quantity and the latent parameter that the student hopes to infer. Assign physical units, name a plausible alternate hypothesis, and state what data are fictional. For earthquake sequences, distinguish a time-limited incomplete catalogue from a stationary stochastic process. Magnitude detection thresholds and event clustering can produce apparent trends. The experiments are deliberately simplified so their calculations can be independently checked. They are not validated field instruments, real-time forecasts, or site-specific hazard assessments.

### Lesson 6.1: Plate boundaries and intraplate deformation

**Learning goals.** Explain the mechanism, translate the problem into measurable quantities, test an alternative interpretation and defend an uncertainty statement.

**Physical foundation.** Earthquakes occur at divergent, convergent and transform boundaries and within plates under complex inherited stresses. Depth and mechanism distributions constrain tectonics but can be misread if location quality is uneven. In the broader unit, Catalog counts are conditional on instruments, magnitude scale, study region and observation window. Statistics can describe patterns and provide probabilistic scenarios but cannot reliably specify the time, location and magnitude of an individual future event.

**Observational method.** Plot synthetic depth sections across an ideal subduction region and contrast them with a shallow intraplate cluster. Specify the coordinate frame, observation period, relevant units, acquisition and calibration limitations before interpreting the resulting figure.

**Common interpretive trap.** A linear cloud of catalog points does not itself define a fault trace when uncertainties span several kilometres. A neat numeric solution does not remove this interpretive ambiguity. Ask which further independent measurement could reveal whether the preferred explanation is incorrect.

**Applied investigation.** Develop tectonic hypotheses and list the independent geological or geodetic evidence required. Provide a labeled sketch, a short reproducible table and a paragraph separating observed evidence from inferred process.

#### Interpretation and quantitative example

**Worked case 6.1: Gutenberg–Richter toy cumulative count.** Synthetic input: `2.94` Mw. Apply the explicitly declared relationship `Math.pow(10,6-x)` to obtain **1148.15 events**. Restrictions: Assumes a=6, b=1 in an invented fixed space/time window and complete catalog. For this worked exercise, treat the input as a declared hypothetical value rather than a measurement. Copy the formula into a fresh calculation and check the unit conversion independently. Vary the input by ten percent and decide whether the output changes proportionally or nonlinearly. Explain which real-world conditions violate the assumptions listed. If the numeric result seems implausibly precise, round it appropriately and describe a physically meaningful range instead of inventing calibration. The purpose is transparent reasoning, not an official estimate. Keep catalog thresholds and observation windows fixed when comparing rates. A newly installed sensor can increase recorded small events without any increase in physical occurrence. A simple count law is useful for checking order of magnitude, but observational duration and magnitude completeness must be stated before statistical inference.

#### Evidence design and falsification

Choose one prediction that would differ under a competing mechanism. A useful prediction has a measurable sign, timing, spectral or spatial signature rather than an undefined expectation that a map should look different. Explain how the predicted quantity would be calculated before looking at the fictional test record. If both explanations remain consistent with the evidence, report the unresolved alternatives and the next practical observation needed. Here, the principal source of ambiguity is stated explicitly: A linear cloud of catalog points does not itself define a fault trace when uncertainties span several kilometres. Keep a processing log with coordinate reference, UTC times, units, processing order and exclusion rules. Compare pre- and post-processing records and explain discrepancies. In the conclusion, identify which claim survives the most consequential alternative parameterization. Reproducibility means another researcher could regenerate the result and find the same limitations, not simply the same decimal answer. End the notebook by explaining how the proposed investigation (Develop tectonic hypotheses and list the independent geological or geodetic evidence required.) addresses at least one weakness of the primary model.

**Knowledge check.** (1) Which claim is directly observed and which is inferred? (2) How would an alternate model change the expected observation? (3) Which number must be accompanied by uncertainty? (4) Why is the worked result unsuitable as a real-time safety conclusion?

### Lesson 6.2: Gutenberg–Richter frequency–magnitude relation

**Learning goals.** Explain the mechanism, translate the problem into measurable quantities, test an alternative interpretation and defend an uncertainty statement.

**Physical foundation.** Over some magnitude ranges, earthquake count generally decreases approximately exponentially with increasing magnitude on a logarithmic plot. The empirical b-value depends on completeness, sampling and process mix. In the broader unit, Catalog counts are conditional on instruments, magnitude scale, study region and observation window. Statistics can describe patterns and provide probabilistic scenarios but cannot reliably specify the time, location and magnitude of an individual future event.

**Observational method.** Estimate b from two cumulative synthetic magnitude counts and test the influence of choosing a different completeness threshold. Specify the coordinate frame, observation period, relevant units, acquisition and calibration limitations before interpreting the resulting figure.

**Common interpretive trap.** Straight extrapolation far beyond the observed range can be misleading, particularly for short catalogs. A neat numeric solution does not remove this interpretive ambiguity. Ask which further independent measurement could reveal whether the preferred explanation is incorrect.

**Applied investigation.** Fit two count models and describe how uncertainty increases at the rare-event end. Provide a labeled sketch, a short reproducible table and a paragraph separating observed evidence from inferred process.

#### Interpretation and quantitative example

**Worked case 6.2: At least one event in ten years.** Synthetic input: `0.18064` events/year. Apply the explicitly declared relationship `1-Math.exp(-10*x)` to obtain **0.835756 probability**. Restrictions: Independent stationary Poisson example; not a fault-specific forecast. For this worked exercise, treat the input as a declared hypothetical value rather than a measurement. Copy the formula into a fresh calculation and check the unit conversion independently. Vary the input by ten percent and decide whether the output changes proportionally or nonlinearly. Explain which real-world conditions violate the assumptions listed. If the numeric result seems implausibly precise, round it appropriately and describe a physically meaningful range instead of inventing calibration. The purpose is transparent reasoning, not an official estimate. Keep catalog thresholds and observation windows fixed when comparing rates. A newly installed sensor can increase recorded small events without any increase in physical occurrence. A simple count law is useful for checking order of magnitude, but observational duration and magnitude completeness must be stated before statistical inference.

#### Evidence design and falsification

Reconstruct the inference backwards. Start with the headline result and locate every conversion, classification and assumption required to obtain it. An estimate based on a chosen velocity, phase pick or site parameter should be labelled conditional on those inputs. Review the same steps after making one intentional mistake in the input metadata; document which output would become misleading and why. Here, the principal source of ambiguity is stated explicitly: Straight extrapolation far beyond the observed range can be misleading, particularly for short catalogs. Method A: compute a baseline result using the stated relation, preserving all units. Method B: perturb one relevant input and record the change. Method C: replace the simplest assumption with an alternative that would be plausible at the study scale; if you cannot recalculate it with the available information, state what is missing. Method D: compare with an independent kind of observation, if available. This order avoids hiding assumptions under additional significant figures. End the notebook by explaining how the proposed investigation (Fit two count models and describe how uncertainty increases at the rare-event end.) addresses at least one weakness of the primary model.

**Knowledge check.** (1) Which claim is directly observed and which is inferred? (2) How would an alternate model change the expected observation? (3) Which number must be accompanied by uncertainty? (4) Why is the worked result unsuitable as a real-time safety conclusion?

### Lesson 6.3: Aftershocks, Omori decay, and event clustering

**Learning goals.** Explain the mechanism, translate the problem into measurable quantities, test an alternative interpretation and defend an uncertainty statement.

**Physical foundation.** Aftershock occurrence rates often decline with elapsed time, and some sequences have triggered events over broad areas. Temporal clustering invalidates naive independent-event assumptions for short windows. In the broader unit, Catalog counts are conditional on instruments, magnitude scale, study region and observation window. Statistics can describe patterns and provide probabilistic scenarios but cannot reliably specify the time, location and magnitude of an individual future event.

**Observational method.** Plot fictional daily aftershock counts, compare an empirical decay fit and show the effect of magnitude completeness changes. Specify the coordinate frame, observation period, relevant units, acquisition and calibration limitations before interpreting the resulting figure.

**Common interpretive trap.** Declining aftershock rates do not prove that a region is safe or determine whether a later larger event will occur. A neat numeric solution does not remove this interpretive ambiguity. Ask which further independent measurement could reveal whether the preferred explanation is incorrect.

**Applied investigation.** Explain the assumptions needed to estimate a time-dependent catalog rate. Provide a labeled sketch, a short reproducible table and a paragraph separating observed evidence from inferred process.

#### Interpretation and quantitative example

**Worked case 6.3: Gutenberg–Richter toy cumulative count.** Synthetic input: `3.94` Mw. Apply the explicitly declared relationship `Math.pow(10,6-x)` to obtain **114.815 events**. Restrictions: Assumes a=6, b=1 in an invented fixed space/time window and complete catalog. For this worked exercise, treat the input as a declared hypothetical value rather than a measurement. Copy the formula into a fresh calculation and check the unit conversion independently. Vary the input by ten percent and decide whether the output changes proportionally or nonlinearly. Explain which real-world conditions violate the assumptions listed. If the numeric result seems implausibly precise, round it appropriately and describe a physically meaningful range instead of inventing calibration. The purpose is transparent reasoning, not an official estimate. Keep catalog thresholds and observation windows fixed when comparing rates. A newly installed sensor can increase recorded small events without any increase in physical occurrence. A simple count law is useful for checking order of magnitude, but observational duration and magnitude completeness must be stated before statistical inference.

#### Evidence design and falsification

A strong evidence chain identifies what the observer physically controls. Specify waveform or map provenance, the acquisition time standard, the instrument or field method, the adopted calibration, and an independent comparison. Is the observed pattern repeatable across genuinely separate records or did it arise after multiple views of the same data? Where an observation is transformed into a calculated quantity, retain its original units and values. Write an audit note on which data would be decisive and which are merely compatible. Here, the principal source of ambiguity is stated explicitly: Declining aftershock rates do not prove that a region is safe or determine whether a later larger event will occur. Create a four-row evidence matrix: observed quantity, inferred physical quantity, principal confounder, and proposed falsifying observation. Mark an entry as measured only when acquisition metadata is known. Repeat the matrix for a second hypothesis instead of dismissing it without calculation. This discipline prevents a tidy narrative from substituting for testable physical interpretation. End the notebook by explaining how the proposed investigation (Explain the assumptions needed to estimate a time-dependent catalog rate.) addresses at least one weakness of the primary model.

**Knowledge check.** (1) Which claim is directly observed and which is inferred? (2) How would an alternate model change the expected observation? (3) Which number must be accompanied by uncertainty? (4) Why is the worked result unsuitable as a real-time safety conclusion?

### Lesson 6.4: Fault slip rates, recurrence, and paleoseismology

**Learning goals.** Explain the mechanism, translate the problem into measurable quantities, test an alternative interpretation and defend an uncertainty statement.

**Physical foundation.** Geologic offsets and geodetic velocities inform long-term deformation budgets. Individual earthquake intervals vary, and dated rupture evidence may preserve an incomplete history. In the broader unit, Catalog counts are conditional on instruments, magnitude scale, study region and observation window. Statistics can describe patterns and provide probabilistic scenarios but cannot reliably specify the time, location and magnitude of an individual future event.

**Observational method.** Construct a toy dated trench-event sequence with age intervals rather than single ages and compare with a slip-rate budget. Specify the coordinate frame, observation period, relevant units, acquisition and calibration limitations before interpreting the resulting figure.

**Common interpretive trap.** Average recurrence interval is not a clock; clustered ruptures and paleoseismic preservation can invalidate regular-cycle stories. A neat numeric solution does not remove this interpretive ambiguity. Ask which further independent measurement could reveal whether the preferred explanation is incorrect.

**Applied investigation.** Build an uncertainty table that separates dating precision from missing-event uncertainty. Provide a labeled sketch, a short reproducible table and a paragraph separating observed evidence from inferred process.

#### Interpretation and quantitative example

**Worked case 6.4: At least one event in ten years.** Synthetic input: `0.30539` events/year. Apply the explicitly declared relationship `1-Math.exp(-10*x)` to obtain **0.952825 probability**. Restrictions: Independent stationary Poisson example; not a fault-specific forecast. For this worked exercise, treat the input as a declared hypothetical value rather than a measurement. Copy the formula into a fresh calculation and check the unit conversion independently. Vary the input by ten percent and decide whether the output changes proportionally or nonlinearly. Explain which real-world conditions violate the assumptions listed. If the numeric result seems implausibly precise, round it appropriately and describe a physically meaningful range instead of inventing calibration. The purpose is transparent reasoning, not an official estimate. Keep catalog thresholds and observation windows fixed when comparing rates. A newly installed sensor can increase recorded small events without any increase in physical occurrence. A simple count law is useful for checking order of magnitude, but observational duration and magnitude completeness must be stated before statistical inference.

#### Evidence design and falsification

When comparing scenarios, preserve the same measurement geometry if possible. A change in a source parameter may look like a path effect when stations or filters differ. Design a sensitivity table with columns for adopted value, plausible range, reason for uncertainty and effect on inference. Distinguish an instrumental limitation from a physical ambiguity: improving sampling can solve the former while the latter may need an entirely different experiment. Here, the principal source of ambiguity is stated explicitly: Average recurrence interval is not a clock; clustered ruptures and paleoseismic preservation can invalidate regular-cycle stories. Build the result graph only after labelling its axes and quantities. Include a plausible range of inputs rather than a single favorable selection. Annotate any discontinuity, threshold or saturated measurement. Next, state whether the curve demonstrates a general law, a restricted approximation or merely the numerical behavior of an arbitrary toy formula. The caption should not promise resolution that the data cannot support. End the notebook by explaining how the proposed investigation (Build an uncertainty table that separates dating precision from missing-event uncertainty.) addresses at least one weakness of the primary model.

**Knowledge check.** (1) Which claim is directly observed and which is inferred? (2) How would an alternate model change the expected observation? (3) Which number must be accompanied by uncertainty? (4) Why is the worked result unsuitable as a real-time safety conclusion?

### Lesson 6.5: Probability, triggering, and forecasting limits

**Learning goals.** Explain the mechanism, translate the problem into measurable quantities, test an alternative interpretation and defend an uncertainty statement.

**Physical foundation.** Poisson models describe simplified independent occurrence; clustered seismicity needs richer models. Operational earthquake forecasts state space, magnitude and time windows with quantified uncertainty. In the broader unit, Catalog counts are conditional on instruments, magnitude scale, study region and observation window. Statistics can describe patterns and provide probabilistic scenarios but cannot reliably specify the time, location and magnitude of an individual future event.

**Observational method.** Calculate an idealized exceedance probability from a prescribed annual event rate and compare independent and clustered scenarios conceptually. Specify the coordinate frame, observation period, relevant units, acquisition and calibration limitations before interpreting the resulting figure.

**Common interpretive trap.** A nonzero annual probability is not a deterministic prediction, and a low probability does not guarantee safety. A neat numeric solution does not remove this interpretive ambiguity. Ask which further independent measurement could reveal whether the preferred explanation is incorrect.

**Applied investigation.** Draft a numerical forecast statement with a clearly defined threshold and end date. Provide a labeled sketch, a short reproducible table and a paragraph separating observed evidence from inferred process.

#### Interpretation and quantitative example

**Worked case 6.5: Gutenberg–Richter toy cumulative count.** Synthetic input: `4.94` Mw. Apply the explicitly declared relationship `Math.pow(10,6-x)` to obtain **11.4815 events**. Restrictions: Assumes a=6, b=1 in an invented fixed space/time window and complete catalog. For this worked exercise, treat the input as a declared hypothetical value rather than a measurement. Copy the formula into a fresh calculation and check the unit conversion independently. Vary the input by ten percent and decide whether the output changes proportionally or nonlinearly. Explain which real-world conditions violate the assumptions listed. If the numeric result seems implausibly precise, round it appropriately and describe a physically meaningful range instead of inventing calibration. The purpose is transparent reasoning, not an official estimate. Keep catalog thresholds and observation windows fixed when comparing rates. A newly installed sensor can increase recorded small events without any increase in physical occurrence. A simple count law is useful for checking order of magnitude, but observational duration and magnitude completeness must be stated before statistical inference.

#### Evidence design and falsification

Choose one prediction that would differ under a competing mechanism. A useful prediction has a measurable sign, timing, spectral or spatial signature rather than an undefined expectation that a map should look different. Explain how the predicted quantity would be calculated before looking at the fictional test record. If both explanations remain consistent with the evidence, report the unresolved alternatives and the next practical observation needed. Here, the principal source of ambiguity is stated explicitly: A nonzero annual probability is not a deterministic prediction, and a low probability does not guarantee safety. Keep a processing log with coordinate reference, UTC times, units, processing order and exclusion rules. Compare pre- and post-processing records and explain discrepancies. In the conclusion, identify which claim survives the most consequential alternative parameterization. Reproducibility means another researcher could regenerate the result and find the same limitations, not simply the same decimal answer. End the notebook by explaining how the proposed investigation (Draft a numerical forecast statement with a clearly defined threshold and end date.) addresses at least one weakness of the primary model.

**Knowledge check.** (1) Which claim is directly observed and which is inferred? (2) How would an alternate model change the expected observation? (3) Which number must be accompanied by uncertainty? (4) Why is the worked result unsuitable as a real-time safety conclusion?

## Unit 6 capstone: Clean a deliberately inconsistent synthetic event catalog, choose and justify a completeness threshold, estimate a b-value and count-decay relationship, and write a probability statement that names model assumptions, observation windows and uncertainties.

**Research scenario:** A fictional region has one large mainshock, a dense aftershock sequence, and a temporary sensor deployment that lowered the detection threshold. Students compare observed counts under incompatible catalog-completeness regimes. The goal is to produce a reasoned comparison of at least two defensible models, not to reverse-engineer a predetermined answer. Start by recording each input variable with units, a confidence grade and a plausible range. Name the forward calculation associated with each inference and outline how the inputs enter the formula. Preserve the fabricated dataset in its supplied CSV form and cite its generation method; these records do not correspond to real earthquakes or real sensor networks.

**Procedure.** First, draw a map or schematic that makes geometric assumptions visible. Second, check station or sample identifiers and the relationship of the observation period to the question. Third, compute baseline statistics and at least one worked relation by hand before using the browser model. Fourth, investigate a competing hypothesis using an independently chosen measurement or a perturbation of a consequential parameter. Fifth, repeat after withholding one doubtful observation. Compare whether the scientific conclusion survives that choice. Keep catalog thresholds and observation windows fixed when comparing rates. A newly installed sensor can increase recorded small events without any increase in physical occurrence. A simple count law is useful for checking order of magnitude, but observational duration and magnitude completeness must be stated before statistical inference.

**Required outputs.** Submit a two-page technical brief with a hypothesis table, raw and corrected values, an equation inventory, an uncertainty budget, a labelled graphic and a short limitations section. Include all model parameters. Do not omit unsuccessful tests and do not represent computer-generated data as measured field observations. Students should record their own explanations rather than copying one another's interpretation. Discuss how different station distributions or sampling choices could cause an apparently significant spatial pattern without a corresponding physical change.

**Extensions.** Catalog counts are conditional on instruments, magnitude scale, study region and observation window. Statistics can describe patterns and provide probabilistic scenarios but cannot reliably specify the time, location and magnitude of an individual future event. Write an explicit counterfactual: what observation would undermine the main hypothesis? Consider what a larger dataset could resolve and what it would leave uncertain. Finally, design an accessible presentation of the result with a descriptive figure caption, a plain-language explanation of each symbol, and a table of numerical values for readers who cannot interpret a colored graph. Re-evaluate the result against professional source and public-safety boundaries before suggesting a consequential application.

**Peer-review rubric.** Assign 0–4 points each for correctness of units, explicit assumptions, data provenance, comparison with alternatives, uncertainty treatment, computational reproducibility and ethical communication. A polished figure without units, or a convincing narrative without a falsifiable test, should not receive full credit. Explain in prose why the least certain input affects confidence, and identify at least one result that could change with additional observations.
