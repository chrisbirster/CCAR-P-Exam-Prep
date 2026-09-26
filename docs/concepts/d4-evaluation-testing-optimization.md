# D4 — Evaluation, Testing & Optimization

**Exam weight:** 16%  
**Objectives:** D4.1–D4.6

Domain 4 asks whether you can prove the system works, diagnose why it fails, and improve it without accidentally sacrificing another requirement.

Anthropic's evaluation guidance emphasizes that agent systems need end-to-end evaluation because tool use, state changes, and multiple turns create failure modes that a single response score cannot capture.

---

## D4.1 — Define evaluation metrics

### Core idea

A vague goal such as "good responses" is not testable. Architecture needs **observable metrics and thresholds**.

### What you need to know

Possible quality metrics:
- task completion;
- classification accuracy;
- groundedness/faithfulness;
- citation correctness;
- policy compliance;
- tool-selection accuracy;
- action correctness.

Operational metrics:
- latency percentiles;
- availability;
- error rate;
- retry rate;
- token consumption;
- cost per completed task.

Business metrics:
- resolution time;
- human escalation;
- customer outcome;
- conversion;
- time saved.

A useful metric has a definition, measurement method, target, and owner.

### Decision rules

Use multiple metrics when success is multi-dimensional.

Define hard floors for safety/security even when the primary goal is quality or speed.

### Common traps

- One overall "accuracy" score for a complex agent.
- Optimizing a metric that does not reflect user value.
- Tracking averages when tail behavior matters.
- No threshold for what counts as acceptable.

### Scenario

A coding agent's primary metric is successful task completion, but a release gate also requires no regression in security checks and a p95 latency ceiling.

### Exam cues

Watch for: **metric, threshold, KPI, acceptance, quality, latency, cost, groundedness**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Demystifying Evals — why agent evaluation is different](../references/demystifying-evals.md#why-agent-evaluation-is-different)
- [Demystifying Evals — graders](../references/demystifying-evals.md#graders)
- [Demystifying Evals — outcomes](../references/demystifying-evals.md#outcomes)

---

## D4.2 — Design evaluation datasets and frameworks

### Core idea

An eval suite should represent the **real workload and real failure modes**.

### What you need to know

Include:
- representative routine cases;
- difficult boundary cases;
- adversarial cases;
- malformed input;
- known historical failures;
- multi-turn cases when the product is multi-turn.

Anthropic distinguishes useful evaluation components such as tasks, trials, graders, transcripts/trajectories, outcomes, harnesses, and suites.

### Grader hierarchy

Use the cheapest reliable grader.

**Code/deterministic grader**
- exact match;
- schema validation;
- unit/integration test;
- database state;
- policy rule.

**Model-based grader**
- coherence;
- groundedness;
- nuanced rubric;
- style/quality where deterministic checks are insufficient.

**Human grader**
- high-consequence or subjective judgment;
- calibration;
- unresolved disagreement.

Model graders should be calibrated against human-labeled examples rather than assumed correct.

### Outcome vs. transcript

For agents, inspect both.

A model can say "done" while the external system shows the action failed. The authoritative outcome may be database state, file contents, or external service state.

### Decision rules

Build evaluation cases from production failures as the system matures.

Run multiple trials when model variance could change the conclusion.

### Common traps

- Evaluating only the final prose response.
- Using an LLM judge for something code can verify exactly.
- Eval set contains only happy-path examples.
- Training/tuning specifically to a tiny static eval and overfitting it.

### Exam cues

Watch for: **eval dataset, grader, trial, trajectory, outcome, representative, adversarial, regression**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Demystifying Evals — tasks and trials](../references/demystifying-evals.md#tasks-and-trials)
- [Demystifying Evals — graders](../references/demystifying-evals.md#graders)
- [Demystifying Evals — trajectories / transcripts](../references/demystifying-evals.md#trajectories--transcripts)

---

## D4.3 — Conduct A/B testing and iterative improvements

### Core idea

A controlled experiment tests a **specific hypothesis** while limiting confounders.

### What you need to know

Before starting:

1. State the hypothesis.
2. Select the primary metric.
3. Define guardrail metrics.
4. Define assignment strategy.
5. Define the stopping/decision rule.

Examples of changes to test:
- model;
- prompt;
- retrieval;
- reranker;
- tool description;
- architecture pattern.

Use consistent assignment at an appropriate unit, such as user/session, when cross-exposure would contaminate results.

### Shadow testing

Shadow testing runs a candidate system on real traffic without letting its output affect the user or production state.

Useful when:
- risk is high;
- the candidate can be evaluated offline;
- you want realistic traffic without direct exposure.

### Decision rules

Separate statistical significance from practical significance. A tiny improvement can be statistically real but operationally irrelevant.

Measure secondary impacts: latency, cost, safety, escalation.

### Common traps

- Changing multiple major variables at once.
- Looking at metrics until one becomes significant.
- Ignoring cost because quality improved.
- Live-testing a risky action system when shadow testing would answer the question.

### Exam cues

Watch for: **hypothesis, A/B, control, treatment, shadow, significance, guardrail metric**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Demystifying Evals — production lifecycle](../references/demystifying-evals.md#production-lifecycle)

---

## D4.4 — Diagnose system issues

### Core idea

Fix the **layer causing the failure**.

### Failure classes

**Prompt failure**  
Instructions are unclear, contradictory, or insufficient.

**Retrieval failure**  
Relevant evidence was never retrieved or wrong evidence ranked higher.

**Model mismatch**  
The task exceeds the model's capability/reliability threshold.

**Tool failure**  
The external call fails, returns unexpected data, or has a bad interface.

**Orchestration failure**  
Correct components are coordinated incorrectly; a worker result is dropped or ordering is wrong.

**Data drift**  
Input distribution or underlying knowledge changes.

**Model behavior/version drift**  
A model upgrade changes output characteristics.

### Diagnostic sequence

```text
symptom
→ reproduce
→ inspect trace
→ identify failing stage
→ form hypothesis
→ isolate with targeted test
→ fix
→ regression test
```

### Decision rules

Use traces and stage-level metrics to isolate the failure.

Do not compensate for a bad upstream stage by making downstream prompts increasingly complex.

### Common traps

- "Hallucination" used as a catch-all diagnosis.
- Prompt rewrite when the retrieval corpus is stale.
- Model upgrade to fix a broken API tool.
- Adding retries to a deterministic authorization failure.

### Exam cues

Watch for: **diagnose, root cause, drift, retrieval error, tool error, orchestration, regression**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Demystifying Evals — trajectories / transcripts](../references/demystifying-evals.md#trajectories--transcripts)
- [Demystifying Evals — outcomes](../references/demystifying-evals.md#outcomes)
- [Demystifying Evals — regression evaluation](../references/demystifying-evals.md#regression-evaluation)

---

## D4.5 — Optimize token usage, latency, and cost-performance trade-offs

### Core idea

Optimization is multi-dimensional: reduce resource consumption **without crossing quality or safety thresholds**.

### What you need to know

Common levers:
- smaller/faster model for appropriate tasks;
- routing;
- prompt caching;
- shorter relevant context;
- just-in-time retrieval;
- fewer unnecessary model calls;
- parallel independent operations;
- batch processing where appropriate;
- programmatic processing of large tool results;
- removing redundant examples/instructions.

Measure:
- input tokens;
- output tokens;
- cached tokens where applicable;
- calls per task;
- cost per successful task;
- p50/p95/p99 latency.

### Decision rules

Optimize **cost per successful outcome**, not just cost per request.

A cheaper request that fails more often can cost more overall.

### Common traps

- Removing context that was critical to accuracy.
- Using the fastest model when retries erase the savings.
- Optimizing average latency while tail latency remains unacceptable.
- Adding a cache without a freshness policy.

### Exam cues

Watch for: **token, cache, cost, p95, model routing, batch, efficiency**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Advanced Tool Use — programmatic tool use](../references/advanced-tool-use.md#programmatic-tool-use)
- [Effective Context Engineering — context is finite](../references/effective-context-engineering.md#context-is-finite)
- [Writing Effective Tools — return high-signal context](../references/writing-effective-tools.md#return-high-signal-context)

---

## D4.6 — Monitor production performance

### Core idea

Evaluation continues after launch.

Offline evals tell you expected behavior on known tasks; production monitoring tells you whether the **real distribution and system dependencies are changing**.

### What you need to know

Monitor:
- outcome success;
- safety violations;
- retrieval quality proxies;
- tool failures;
- latency;
- token/cost trends;
- escalation;
- input-distribution changes;
- model/version changes.

Convert incidents and user complaints into new regression cases.

Define ownership:
- who receives the alert;
- what threshold triggers action;
- what the runbook says;
- when to roll back;
- when to re-evaluate architecture.

### Capability vs. regression evals

Capability evals ask: **Can the system do harder/new things?**

Regression evals ask: **Does it still do known things correctly?**

A maturing system should continuously protect known-good behavior while expanding capability.

### Common traps

- Monitoring infrastructure uptime only.
- Alerts with no owner.
- Eval suite never updated after launch.
- Production distribution changes but test set stays frozen.

### Exam cues

Watch for: **monitoring, drift, regression, alert, rollback, production, distribution**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Demystifying Evals — regression evaluation](../references/demystifying-evals.md#regression-evaluation)
- [Demystifying Evals — production lifecycle](../references/demystifying-evals.md#production-lifecycle)
- [Claude Model Lifecycle — migration testing](../references/model-lifecycle.md#migration-testing)

---

## Domain 4 summary

```text
define success
→ build representative evals
→ establish baseline
→ test change
→ diagnose by stage
→ optimize within thresholds
→ monitor production
→ turn failures into regression tests
```

## Primary references

- Anthropic, “Demystifying Evals for AI Agents”  
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic, “Building Effective AI Agents”  
  https://www.anthropic.com/engineering/building-effective-agents
