---
layout: default
title: CCAR-P Exam Objectives
description: A student-friendly checklist for all seven CCAR-P domains and 38 objectives.
permalink: /objectives/
---

# CCAR-P Exam Objectives & Study Checklist

**Certification:** Claude Certified Architect – Professional (CCAR-P)  
**Blueprint:** v1.0, effective July 2026  
**Last reviewed:** September 26, 2026

> [!IMPORTANT]
> This is an independent, student-friendly interpretation of the published CCAR-P blueprint. Objective titles and domain weights follow the published blueprint; the explanations, checklists, examples, and study guidance are original study material. Anthropic's current exam guide remains authoritative.

---

## How to Use This Document

For every objective, aim to reach three levels:

- **Explain** — you can describe the concept without notes.
- **Compare** — you can distinguish it from plausible alternatives.
- **Decide** — given constraints, you can choose an architecture and defend the trade-off.

The Professional exam rewards the third level most heavily.

---

## Blueprint at a Glance

| Domain | Weight | Objectives |
|---|---:|---:|
| D1 — Solution Design & Architecture | 17% | 6 |
| D2 — Claude Models, Prompting & Context Engineering | 13% | 5 |
| D3 — Integration | 19% | 8 |
| D4 — Evaluation, Testing & Optimization | 16% | 6 |
| D5 — Governance, Safety & Risk Management | 14% | 5 |
| D6 — Stakeholder Communication & Lifecycle Management | 14% | 5 |
| D7 — Developer Productivity & Operational Enablement | 7% | 3 |
| **Total** | **100%** | **38** |

---

# D1 — Solution Design & Architecture
**Weight: 17%**

The core question in this domain is: **Can you turn an ambiguous business problem into a defensible Claude architecture?**

## D1.1 Translate business problems into Claude-based AI solutions

- [ ] Identify the actual business outcome before selecting a model or architecture.
- [ ] Separate functional requirements from non-functional requirements.
- [ ] Identify hard constraints such as latency, budget, compliance, reliability, data residency, and human review.
- [ ] Decide what Claude should do versus deterministic software, existing systems, or people.
- [ ] Define measurable success criteria before implementation.

**Watch for:** solutions that start with “build an agent” before the problem is scoped.

## D1.2 Design end-to-end architectures

Be able to reason across the full request path:

```text
input
  → validation
  → context/retrieval
  → Claude
  → tools/external systems
  → verification
  → output
  → feedback/evaluation
```

- [ ] Identify trust boundaries.
- [ ] Identify the system of record.
- [ ] Define where state lives.
- [ ] Define retries, fallbacks, escalation, and failure recovery.
- [ ] Include telemetry and evaluation in the design from the start.

## D1.3 Select appropriate architectural patterns

Know when to choose:

- [ ] an augmented single LLM call;
- [ ] a deterministic workflow;
- [ ] an agentic system;
- [ ] a hybrid.

Evaluate choices using:

- predictability;
- reversibility;
- error cost;
- latency;
- token/API cost;
- observability;
- need for dynamic planning.

**Rule of thumb:** if the sequence can be reliably enumerated ahead of time, a workflow may be preferable to an autonomous agent.

## D1.4 Design multi-agent systems and orchestration strategies

- [ ] Know coordinator/worker and specialist-agent patterns.
- [ ] Give workers narrow responsibilities.
- [ ] Define explicit handoff contracts.
- [ ] Handle disagreement, malformed worker output, and partial completion.
- [ ] Preserve or checkpoint orchestration state.
- [ ] Propagate tracing information across agent boundaries.
- [ ] Justify why multiple agents are better than one agent plus tools.

## D1.5 Apply decomposition techniques for complex problem solving

- [ ] Break complex work into bounded tasks.
- [ ] Separate deterministic rules from probabilistic reasoning.
- [ ] Identify independent work that can be parallelized.
- [ ] Define inputs and outputs between stages.
- [ ] Recognize routing, chaining, fan-out/fan-in, critique, and validation patterns.

## D1.6 Align solutions to business value

Tie architecture decisions to outcomes such as:

- efficiency;
- productivity;
- transformation;
- quality;
- cost;
- latency;
- reliability;
- throughput;
- service-level objectives.

Be prepared to compare:

```text
baseline → expected improvement → operating cost → net value
```

### D1 Readiness

You should be able to read a scenario and explain:

1. what remains deterministic;
2. what Claude owns;
3. whether it should be a workflow or agent;
4. where human review belongs;
5. how failures are contained;
6. how success will be measured.

---

# D2 — Claude Models, Prompting & Context Engineering
**Weight: 13%**

## D2.1 Select appropriate Claude models based on trade-offs

- [ ] Compare capability, speed, latency, and cost.
- [ ] Route work by task complexity and risk.
- [ ] Avoid defaulting every task to the most capable model.
- [ ] Use evaluations to justify changing models.
- [ ] Treat model upgrades as production changes requiring regression testing.
- [ ] Consider different models for different workflow stages.

## D2.2 Design system prompts, templates, and guardrails

- [ ] Separate stable system instructions from untrusted/dynamic content.
- [ ] Define role, scope, constraints, and output contract clearly.
- [ ] Use structural enforcement when a hard guarantee is required.
- [ ] Build reusable templates without allowing variables to override fixed controls.
- [ ] Remember: prompts guide behavior; they are not authorization systems.

## D2.3 Apply prompt-engineering techniques

Understand when to use:

- [ ] zero-shot instructions;
- [ ] few-shot examples;
- [ ] explicit decomposition/reasoning;
- [ ] structured outputs;
- [ ] examples for difficult edge cases.

Use the simplest technique that reliably passes your evaluation suite.

## D2.4 Optimize context windows and token usage

Distinguish:

- active context;
- retrieval;
- persistent application state;
- conversation memory/summaries.

Know when to use:

- full upfront context;
- recent-history context;
- just-in-time retrieval;
- compaction/summarization.

Identify problems such as:

- uncontrolled context growth;
- repeated context;
- lost detail;
- token exhaustion;
- irrelevant information reducing answer quality.

## D2.5 Implement prompt reuse strategies

- [ ] Understand prompt caching.
- [ ] Place stable prefixes before request-specific content where useful.
- [ ] Recognize freshness/staleness concerns.
- [ ] Use modular prompts.
- [ ] Understand reusable Skills/procedures as governed assets.
- [ ] Version important shared prompt components.

---

# D3 — Integration
**Weight: 19% — highest-weighted domain**

The central question is: **Can Claude interact with enterprise systems without creating unnecessary capability, security, reliability, or latency problems?**

## D3.1 Evaluate tool/agent configuration for capability bloat

- [ ] Apply least privilege to available tools.
- [ ] Remove tools that are not needed for the task.
- [ ] Limit data visibility.
- [ ] Limit write/side-effect capability.
- [ ] Recognize that tool definitions increase both attack surface and decision complexity.

Logging an unnecessary capability does not make that capability safe.

## D3.2 Analyze authentication and authorization requirements

Distinguish:

- **Authentication:** Who is the caller?
- **Authorization:** What can the caller do?
- **Tenant isolation:** Which data can the caller access?
- **Auditability:** Can the action be reconstructed later?

- [ ] Identity should come from trusted authentication infrastructure.
- [ ] User-supplied role claims are not authorization.
- [ ] Tool calls should preserve source-system access controls.
- [ ] Avoid shared credentials when individual attribution matters.
- [ ] Enforce authorization for side effects deterministically.

## D3.3 Evaluate accuracy–latency trade-offs

- [ ] Measure latency by stage.
- [ ] Decide whether retrieval, reranking, extra model calls, or deeper reasoning materially improve quality.
- [ ] Optimize against actual SLA requirements.
- [ ] Consider tail latency, not only averages.
- [ ] Avoid complexity whose quality benefit cannot be measured.

## D3.4 Analyze observability challenges at scale

Trace across:

- [ ] model calls;
- [ ] retrieval;
- [ ] tool calls;
- [ ] queues;
- [ ] dependencies;
- [ ] retries;
- [ ] errors;
- [ ] agent trajectories;
- [ ] cost;
- [ ] token usage.

A production incident should be reconstructable end to end.

## D3.5 Design a RAG pipeline

Understand:

```text
ingestion
  → parsing
  → chunking
  → metadata
  → indexing
  → retrieval
  → optional reranking
  → context assembly
  → generation
  → grounding/citation checks
```

Choose chunking based on document structure, semantic boundaries, expected query types, and content format.

## D3.6 Apply retrieval strategies matched to the data

Understand when to use:

- keyword retrieval;
- semantic retrieval;
- hybrid retrieval;
- metadata filters;
- reranking/rank fusion.

**Critical distinction:** live transactional state normally belongs behind a tool/API call to the system of record, not in a stale vector index.

## D3.7 Select the appropriate integration mechanism

Be able to compare:

- direct API/SDK;
- CLI;
- Model Context Protocol (MCP);
- agent-to-agent communication;
- managed agent/runtime abstractions.

Evaluate based on:

- reuse across clients;
- security boundaries;
- ownership;
- operational complexity;
- protocol compatibility;
- interaction pattern.

**MCP is not automatically better than a direct API.** It is especially valuable when a reusable tool/data surface should serve multiple compatible AI clients.

## D3.8 Evaluate progressive discovery vs. monolithic context

- [ ] Avoid exposing every tool and resource in every request.
- [ ] Discover capabilities progressively where appropriate.
- [ ] Reduce token overhead.
- [ ] Reduce tool-selection confusion.
- [ ] Reduce visible attack surface.
- [ ] Fetch detail only when the task requires it.

---

# D4 — Evaluation, Testing & Optimization
**Weight: 16%**

## D4.1 Define evaluation metrics

Measure dimensions such as:

- [ ] task success / accuracy;
- [ ] groundedness;
- [ ] safety;
- [ ] security;
- [ ] latency;
- [ ] reliability;
- [ ] cost;
- [ ] user/business outcome.

Turn vague requirements into explicit acceptance thresholds.

## D4.2 Design evaluation datasets and frameworks

Include:

- representative cases;
- edge cases;
- adversarial inputs;
- malformed inputs;
- historical regression cases;
- multi-turn examples where appropriate.

Use the least expensive reliable evaluator:

1. deterministic/code-based checks;
2. model-based judges;
3. human review.

Calibrate model-based grading against human-labelled examples.

## D4.3 Conduct A/B testing and iterative improvements

- [ ] State a falsifiable hypothesis.
- [ ] Select the primary metric in advance.
- [ ] Keep assignment consistent where appropriate.
- [ ] Use enough observations.
- [ ] Track latency, cost, and safety as secondary metrics.
- [ ] Distinguish statistical significance from business significance.
- [ ] Know when shadow testing is safer than direct user exposure.

## D4.4 Diagnose system issues

Distinguish failures in:

- prompting;
- grounding/retrieval;
- model selection;
- tools;
- orchestration;
- underlying data;
- model/version behavior.

Fix the layer that caused the failure rather than compensating elsewhere.

## D4.5 Optimize token usage, latency, and cost-performance trade-offs

- [ ] Measure token use per request/stage.
- [ ] Identify oversized or repeated context.
- [ ] Cache reusable context where safe.
- [ ] Route simpler work to cheaper/faster models when evaluations support it.
- [ ] Remove unnecessary model/tool calls.
- [ ] Look at high-percentile latency and cost, not only averages.
- [ ] Preserve defined quality and safety thresholds while optimizing.

## D4.6 Monitor production performance

- [ ] Define operational metrics.
- [ ] Instrument model, retrieval, tools, and dependencies.
- [ ] Detect drift.
- [ ] Maintain regression suites.
- [ ] Tie alerts to an owner and response.
- [ ] Keep evaluation data representative of production traffic.

---

# D5 — Governance, Safety & Risk Management
**Weight: 14%**

## D5.1 Implement guardrails and safety controls

Understand the role of:

- model-level safeguards;
- system instructions;
- input screening;
- output screening;
- deterministic tool/action authorization;
- sandboxing;
- least privilege.

Know which controls must fail closed.

## D5.2 Identify risks, limitations, and failure modes

Study:

- hallucination;
- direct prompt injection;
- indirect prompt injection;
- excessive agency;
- tool/action abuse;
- data exposure;
- token/cost exhaustion;
- biased outcomes;
- supply-chain risk from external tools/Skills;
- silent orchestration failure.

For each risk, identify **prevention, detection, and recovery** controls.

## D5.3 Apply human-in-the-loop validation

Base review on:

- consequence of an error;
- reversibility;
- uncertainty;
- regulation;
- financial/safety impact.

Know the difference between:

- pre-action approval;
- post-action review;
- sampled review.

Reviewers need enough context to make a real decision.

## D5.4 Ensure compliance with regulations

Understand how requirements such as GDPR, HIPAA, and FedRAMP can influence:

- data handling;
- access control;
- logging;
- retention;
- deployment route/environment;
- data residency;
- evidence collection.

Use the pattern:

```text
requirement → control → owner → evidence → review cadence
```

## D5.5 Address responsible/ethical AI considerations

- [ ] Bias.
- [ ] Fairness.
- [ ] Transparency.
- [ ] Appropriate explainability.
- [ ] Accountability.
- [ ] Traceability.

Evaluate outcomes across relevant subgroups rather than relying only on aggregate metrics.

---

# D6 — Stakeholder Communication & Lifecycle Management
**Weight: 14%**

## D6.1 Conduct structured discovery and requirement gathering

Capture:

- business outcomes;
- required capabilities;
- prohibited behaviors;
- user workflows;
- cost limits;
- volume assumptions;
- quality expectations;
- latency/availability expectations;
- compliance obligations;
- dependencies;
- decision owners;
- open assumptions.

Convert words like “fast,” “accurate,” or “seamless” into measurable requirements.

## D6.2 Communicate architecture decisions and trade-offs

For each meaningful option, communicate:

1. benefit;
2. cost/concession;
3. risk;
4. cost of reversal;
5. compliance impact where relevant.

Adapt the explanation for executives, engineering, security, procurement, legal/compliance, and product teams.

## D6.3 Manage stakeholder feedback and expectation alignment

- [ ] Define measurable quality expectations.
- [ ] Set realistic SLAs for a probabilistic system.
- [ ] Define triggers for review.
- [ ] Define what happens after an SLA breach.
- [ ] Know when to iterate versus re-architect.
- [ ] Forecast cost/consumption for production.

## D6.4 Document architectures and implementation guidance

Useful architecture decision records should capture:

- decision;
- date;
- alternatives;
- rejected options and why;
- assumptions;
- trade-offs;
- owner;
- evidence/control artifacts;
- open issues;
- review criteria.

A successor should be able to operate and safely modify the system without attending the original design meetings.

## D6.5 Support lifecycle phases

Know what belongs in:

1. discovery;
2. design;
3. handoff;
4. monitoring;
5. iteration.

Do not use later-phase activity as a substitute for unfinished discovery or design work.

---

# D7 — Developer Productivity & Operational Enablement
**Weight: 7%**

## D7.1 Configure Claude tools and environments for teams

Understand concepts including:

- Claude Code project/team guidance;
- shared configuration;
- MCP/tool configuration;
- permission modes;
- hooks;
- sandboxing;
- scoped subagents;
- reusable Skills/procedures;
- model/spending guardrails.

Separate **instructions that influence behavior** from **controls that enforce permissions**.

## D7.2 Improve developer workflows using AI-assisted tooling

Apply AI assistance to:

- repository exploration;
- implementation;
- refactoring;
- testing;
- code review;
- debugging;
- documentation;
- incident investigation.

Maintain verification requirements for correctness, security, maintainability, and human understanding.

## D7.3 Support debugging and operational issue resolution

| Symptom | Investigate |
|---|---|
| Quality declines | prompt/model changes, retrieval/index drift |
| Latency rises | context growth, dependencies, cache misses |
| Tool calls fail | credentials, permissions, throttling, contracts |
| Cost rises without traffic growth | model routing, context size, caching |
| Agent work disappears | orchestration state, worker results, trace propagation |

- [ ] Create runbooks.
- [ ] Define escalation paths.
- [ ] Record known failure modes.
- [ ] Assign operational ownership.
- [ ] Enable the team to resolve recurring incidents without the original architect.

---

# Cross-Domain Decision Rules

These patterns show up repeatedly across the blueprint.

## 1. Deterministic vs. probabilistic responsibilities

Prefer deterministic controls for:

- authorization;
- access control;
- hard business rules;
- schema validation;
- numeric thresholds;
- irreversible action approval.

Use Claude for tasks where language understanding, synthesis, reasoning, classification, planning, or generation is useful.

## 2. Least privilege

Minimize:

- tools;
- credentials;
- accessible data;
- context;
- autonomous actions;
- side-effect permissions.

Observability does not replace least privilege.

## 3. System of record vs. retrieval

Use **retrieval** for relatively stable knowledge that benefits from semantic or keyword search.

Use a **tool/API** for current state controlled by another operational system.

Examples:

| Information | Prefer |
|---|---|
| Policy manual | Retrieval |
| Current account balance | Live API/tool |
| Product documentation | Retrieval |
| Current inventory count | Live API/tool |

## 4. Evaluation before optimization

Before changing a model, prompt, retrieval strategy, agent design, or tool configuration, define:

```text
dataset + metric + threshold + rollback condition
```

## 5. Human review by consequence

The greater the irreversibility, financial impact, safety impact, regulatory impact, or uncertainty, the stronger the case for human approval before action.

## 6. Architecture is constrained optimization

There is rarely one universally best architecture.

A defensible architecture is usually:

> The simplest design that meets the stated quality, security, safety, compliance, latency, reliability, and cost constraints.

---

# Master Readiness Checklist

Before the exam, practice working through scenarios in this order:

### 1. Outcome
- [ ] What business result is required?

### 2. Constraints
- [ ] What requirements eliminate otherwise-valid options?

### 3. Responsibility split
- [ ] What belongs to Claude?
- [ ] What belongs to deterministic software?
- [ ] What belongs to external systems?
- [ ] What belongs to humans?

### 4. Architecture pattern
- [ ] Single augmented call?
- [ ] Workflow?
- [ ] Agent?
- [ ] Multi-agent?
- [ ] Hybrid?

### 5. Context and integrations
- [ ] What does Claude need to know?
- [ ] What should be retrieved?
- [ ] What must be fetched live?
- [ ] Which tools/protocols are actually necessary?

### 6. Controls
- [ ] Where is identity established?
- [ ] Where is authorization enforced?
- [ ] Where are safety/privacy controls enforced?
- [ ] Where is human review required?

### 7. Evaluation
- [ ] What dataset demonstrates acceptable behavior?
- [ ] Which metrics matter?
- [ ] What threshold must be passed?

### 8. Operations
- [ ] How is the request traced?
- [ ] What happens when a dependency fails?
- [ ] How are latency and cost controlled?
- [ ] How is drift detected?

### 9. Ownership
- [ ] Who owns the architecture decision?
- [ ] Who owns residual risk?
- [ ] Who owns operational response?
- [ ] Who decides when to revisit the design?

---

# Suggested Flashcard Coverage

If using a 300-card study deck, a weight-proportional starting point is:

| Domain | Suggested cards |
|---|---:|
| D1 — Solution Design & Architecture | 51 |
| D2 — Models, Prompting & Context | 39 |
| D3 — Integration | 57 |
| D4 — Evaluation, Testing & Optimization | 48 |
| D5 — Governance, Safety & Risk | 42 |
| D6 — Stakeholder & Lifecycle | 42 |
| D7 — Developer Productivity | 21 |
| **Total** | **300** |

Recommended mix:

- **30%** concept / recall;
- **20%** compare and contrast;
- **40%** architecture scenarios;
- **10%** failure modes / common traps.

---

# Objective Tracker

## D1
- [ ] D1.1 Business problem → Claude solution
- [ ] D1.2 End-to-end architecture
- [ ] D1.3 Architecture-pattern selection
- [ ] D1.4 Multi-agent orchestration
- [ ] D1.5 Decomposition
- [ ] D1.6 Business-value alignment

## D2
- [ ] D2.1 Model selection
- [ ] D2.2 System prompts/templates/guardrails
- [ ] D2.3 Prompt-engineering techniques
- [ ] D2.4 Context/token management
- [ ] D2.5 Prompt reuse/caching/Skills

## D3
- [ ] D3.1 Tool/capability bloat
- [ ] D3.2 Authentication and authorization
- [ ] D3.3 Accuracy/latency trade-offs
- [ ] D3.4 Observability
- [ ] D3.5 RAG pipeline
- [ ] D3.6 Retrieval strategy
- [ ] D3.7 Integration mechanism
- [ ] D3.8 Progressive discovery

## D4
- [ ] D4.1 Evaluation metrics
- [ ] D4.2 Evaluation datasets/frameworks
- [ ] D4.3 A/B testing/iteration
- [ ] D4.4 Failure diagnosis
- [ ] D4.5 Token/latency/cost optimization
- [ ] D4.6 Production monitoring

## D5
- [ ] D5.1 Guardrails/safety controls
- [ ] D5.2 Risks/failure modes
- [ ] D5.3 Human-in-the-loop validation
- [ ] D5.4 Regulatory compliance
- [ ] D5.5 Responsible/ethical AI

## D6
- [ ] D6.1 Structured discovery
- [ ] D6.2 Trade-off communication
- [ ] D6.3 Feedback/expectations/SLAs
- [ ] D6.4 Architecture documentation
- [ ] D6.5 Lifecycle management

## D7
- [ ] D7.1 Team tool/environment configuration
- [ ] D7.2 AI-assisted developer workflows
- [ ] D7.3 Debugging and operational support

---

# Recommended Study Order

1. **D1 — Solution Design & Architecture**
2. **D3 — Integration**
3. **D4 — Evaluation, Testing & Optimization**
4. **D2 — Models, Prompting & Context Engineering**
5. **D5 — Governance, Safety & Risk**
6. **D6 — Stakeholder Communication & Lifecycle**
7. **D7 — Developer Productivity & Operational Enablement**

---

## Sources and Scope

This guide is organized around the CCAR-P v1.0 blueprint, effective July 2026.

Primary references to verify against:

- Anthropic Partner Academy — Claude Certified Architect – Professional Prep Course
- Anthropic Partner Academy — Partner Certifications
- Anthropic Partner Academy — Certification FAQ
- Anthropic documentation
- Model Context Protocol specification

Exam programs and product capabilities can change. Re-check the current official exam guide before final review or scheduling.
