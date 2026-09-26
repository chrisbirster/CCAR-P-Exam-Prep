# D6 — Stakeholder Communication & Lifecycle Management

**Exam weight:** 14%  
**Objectives:** D6.1–D6.5

Domain 6 tests whether you can turn technical architecture into a system that an organization can understand, approve, operate, and improve.

---

## D6.1 — Conduct structured discovery and requirement gathering

### Core idea

The architect's first job is to turn ambiguous stakeholder language into **testable requirements**.

### What you need to discover

**Business outcome**
- What changes if this succeeds?
- What is the baseline today?

**Users/workflow**
- Who uses it?
- At what point in their work?
- What system owns the current state?

**Quality**
- What does "correct" mean?
- What errors are acceptable?
- What errors are catastrophic?

**Latency/availability**
- What does "fast" mean numerically?
- Is the workload interactive, batch, or asynchronous?

**Scale/cost**
- Requests per day?
- Peak concurrency?
- Cost ceiling?

**Risk/compliance**
- Sensitive data?
- Human approval?
- Residency?
- Retention?
- Regulated decision?

**Ownership**
- Who approves requirements?
- Who owns residual risk?
- Who supports production?

### Decision rules

Convert adjectives into numbers or observable tests.

"Accurate" → pass rate on an agreed eval set.

"Fast" → p95 under X seconds.

"Reliable" → availability/error target plus fallback behavior.

### Common traps

- Accepting stakeholder implementation language as requirements.
- Designing before identifying prohibited behavior.
- No owner for unresolved assumptions.
- SLA copied from another service without business justification.

### Exam cues

Watch for: **discovery, requirements, stakeholder, assumptions, SLA, prohibited behavior, outcome**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)

---

## D6.2 — Communicate architecture decisions and trade-offs

### Core idea

A good architecture decision explains **why this option wins under these constraints**, not simply what components exist.

### Decision communication template

For each meaningful option:

1. Benefit.
2. Cost/concession.
3. Risk.
4. Reversibility/cost of change.
5. Compliance/security impact.
6. Evidence supporting the choice.

### Audience adaptation

**Executives**
- business value;
- cost;
- timeline;
- major risk.

**Engineering**
- interfaces;
- failure modes;
- operational burden;
- performance.

**Security**
- identity;
- trust boundaries;
- privileges;
- threat model.

**Compliance/legal**
- data flow;
- control ownership;
- retention/residency;
- evidence.

**Product**
- user experience;
- quality;
- latency;
- escalation behavior.

The underlying decision remains the same; the emphasis changes.

### Common traps

- Presenting architecture jargon with no business implication.
- Hiding trade-offs to make a proposal sound stronger.
- Giving every audience the same 40-slide technical explanation.
- Comparing options without the constraints that make the comparison meaningful.

### Exam cues

Watch for: **trade-off, executive, security review, recommendation, alternative, rationale**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)

---

## D6.3 — Manage stakeholder feedback and expectation alignment

### Core idea

AI systems are probabilistic. Stakeholders need **measurable expectations and a feedback mechanism**, not promises of perfection.

### What you need to know

Define:
- quality target;
- latency target;
- availability target;
- escalation threshold;
- cost envelope;
- unacceptable failure classes.

A feedback loop requires:

```text
signal
→ threshold/trigger
→ owner
→ investigation
→ action
→ verification
```

Examples:
- user thumbs-down alone is a signal, not a full evaluation;
- repeated tool failures can trigger incident review;
- cost drift can trigger routing/context analysis;
- safety incident can trigger rollback.

### Iteration vs. re-architecture

Iterate when the current pattern is sound but parameters/prompts/tools need improvement.

Re-architect when a fundamental constraint changed or the pattern itself is the bottleneck.

### Common traps

- "We'll improve based on feedback" with no mechanism or owner.
- Promising deterministic correctness from a probabilistic component.
- Treating every user complaint as a model problem.
- Staying with a fundamentally wrong architecture because prompts are easier to change.

### Exam cues

Watch for: **expectation, feedback loop, SLA, escalation, iterate, re-architect, forecast cost**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Demystifying Evals — production lifecycle](../references/demystifying-evals.md#production-lifecycle)

---

## D6.4 — Document architectures and implementation guidance

### Core idea

Architecture documentation preserves **decision context**, not just diagrams.

### Architecture Decision Record (ADR)

A useful ADR records:

- decision;
- date/status;
- context;
- constraints;
- alternatives considered;
- why alternatives were rejected;
- trade-offs;
- assumptions;
- owner;
- security/compliance implications;
- evidence;
- review trigger.

### Other useful artifacts

- context/data-flow diagrams;
- trust-boundary diagrams;
- interface contracts;
- runbooks;
- eval definitions;
- risk/control matrix;
- operational dashboards;
- rollback plan.

Documentation should let a successor understand how to operate and safely change the system without attending the original meetings.

### Decision rules

Document decisions that are expensive, risky, or hard to reverse.

Keep docs close to the system/version they describe.

### Common traps

- Diagram with no rationale.
- ADR says "use MCP" but not why.
- Documentation never updated after model/tool changes.
- Critical operational knowledge lives only in one architect's head.

### Exam cues

Watch for: **ADR, handoff, rationale, documentation, successor, runbook, decision record**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)

---

## D6.5 — Support lifecycle phases

### Core idea

A production solution moves through distinct phases, each with different artifacts and decisions.

### 1. Discovery

Outputs:
- business outcome;
- requirements;
- constraints;
- assumptions;
- initial risk classification.

### 2. Design

Outputs:
- architecture;
- integration decisions;
- threat model;
- eval plan;
- cost/latency model;
- trade-off record.

### 3. Handoff / implementation readiness

Outputs:
- interface contracts;
- implementation guidance;
- acceptance criteria;
- runbooks;
- ownership;
- deployment/rollback plan.

### 4. Monitoring

Outputs:
- dashboards;
- alerts;
- evaluation results;
- incident records;
- usage/cost data.

### 5. Iteration

Outputs:
- new regression tests;
- updated prompts/tools/models;
- ADR revisions/new decisions;
- risk/control updates.

### Decision rules

Do not use later phases to cover missing earlier work.

Example: monitoring cannot compensate for undefined success criteria; a runbook cannot repair an unclear authorization boundary.

### Common traps

- Launching before acceptance criteria exist.
- Handoff without ownership.
- Monitoring only infrastructure health.
- Iteration changes behavior without updating evals or docs.

### Exam cues

Watch for: **discovery, design, handoff, monitoring, iteration, lifecycle, ownership**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Demystifying Evals — production lifecycle](../references/demystifying-evals.md#production-lifecycle)

---

## Domain 6 summary

```text
discover
→ quantify requirements
→ communicate trade-offs
→ document decisions
→ hand off ownership
→ monitor
→ iterate from evidence
```

## Primary references

- Anthropic, “Demystifying Evals for AI Agents”  
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic, “Building Effective AI Agents”  
  https://www.anthropic.com/engineering/building-effective-agents
