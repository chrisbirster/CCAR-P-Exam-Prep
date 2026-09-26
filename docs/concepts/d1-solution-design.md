# D1 — Solution Design & Architecture

**Exam weight:** 17%  
**Objectives:** D1.1–D1.6

Domain 1 asks whether you can take an ambiguous business request and turn it into a **defensible architecture**. The strongest answer is usually not the most sophisticated architecture. Anthropic's guidance on effective agents repeatedly recommends starting with the simplest solution that works and adding agentic complexity only when it produces measurable value.

---

## D1.1 — Translate business problems into Claude-based AI solutions

### Core idea

Architecture starts with the **business outcome**, not with Claude, agents, MCP, or RAG.

A stakeholder may say "we need an AI agent," but that is a proposed implementation. The architect must discover the actual outcome, such as reducing ticket-resolution time, improving document review quality, or automating a bounded workflow.

### What you need to know

Separate requirements into four buckets:

**Outcome requirements** describe the value to create. Examples: reduce handle time by 30%, automate 60% of a workflow, or improve first-pass quality.

**Functional requirements** describe what the solution must do. Examples: classify requests, retrieve policies, create a draft, call a CRM tool.

**Non-functional requirements** constrain how it must operate. Examples: p95 latency, availability, data residency, audit retention, throughput, cost per request.

**Risk constraints** define what the solution must not do without stronger controls. Examples: issue a refund over a threshold, expose another tenant's data, or make a regulated decision without review.

A Claude solution is appropriate when language understanding, synthesis, classification, planning, or generation adds value. Deterministic software remains better for exact authorization, hard rules, arithmetic thresholds, schema checks, and other conditions where correctness must not depend on probabilistic output.

### Decision rules

1. Define the outcome before the component diagram.
2. Convert vague goals into measurable targets.
3. Identify hard constraints before selecting the model or pattern.
4. Decide what Claude owns and what deterministic software owns.
5. Define success and failure criteria before implementation.

### Common traps

**"The stakeholder asked for an agent, so use an agent."**  
Treat "agent" as a hypothesis, not a requirement.

**"Use the strongest model everywhere."**  
Model selection comes after workload and quality requirements.

**"The prompt will make it safe."**  
Prompts are behavioral guidance. Hard security and authorization guarantees belong outside the model.

### Scenario

A company wants "an autonomous finance agent." Discovery reveals that the actual need is to summarize invoices, classify expense categories, and flag policy exceptions. Final approval must remain with finance.

A bounded workflow with deterministic policy checks and human approval may satisfy the outcome better than a fully autonomous agent.

### Exam cues

Watch for: **business outcome, requirements, constraints, SLA, data residency, budget, risk, human approval, success criteria**.

---

## D1.2 — Design end-to-end architectures

### Core idea

A production Claude system is a **whole request path**, not a model call.

A useful architecture traces the journey from input through validation, context gathering, model inference, tools, verification, output, telemetry, and feedback.

### What you need to know

Typical stages include:

```text
request
  → authentication
  → input validation
  → context/retrieval
  → model inference
  → tool calls
  → deterministic verification
  → output/action
  → logging/metrics
  → evaluation/feedback
```

At each boundary ask:

- What data crosses the boundary?
- Which identity is attached?
- Who authorizes the next action?
- What happens if the dependency fails?
- Can the step be retried safely?
- Where is state stored?
- What evidence is logged?
- Is the failure visible to an operator?

A **system of record** is the authoritative source for current operational state. Do not accidentally make an LLM conversation, vector index, or cached summary the authoritative source for a transactional fact.

### Decision rules

Design the **failure path** at the same time as the happy path.

For every external dependency, decide whether to retry, fall back, queue, escalate, or fail closed.

For stateful workflows, define ownership of state explicitly. A model's context is not automatically durable application state.

### Common traps

- Omitting observability from the initial design.
- Treating the vector database as the system of record.
- Retrying non-idempotent side effects blindly.
- Letting each agent maintain its own conflicting copy of critical state.
- Designing only the request path and not recovery.

### Scenario

A customer-support assistant retrieves policy, drafts a response, and can issue credits. The model may decide a credit is useful, but a deterministic service verifies account ownership, amount limits, and permission before the credit API executes.

### Exam cues

Watch for: **end-to-end, failure handling, retry, fallback, state, system of record, trust boundary, observability**.

---

## D1.3 — Select appropriate architectural patterns

### Core idea

Choose among a **single augmented call, workflow, agent, or hybrid** based on uncertainty and control requirements.

Anthropic distinguishes workflows from agents: workflows follow predefined code paths; agents dynamically decide how to accomplish the task.

### Pattern: augmented LLM

Use when one model call plus context, retrieval, or tools can solve the task reliably.

Best when:
- the task is bounded;
- the output contract is clear;
- one inference step is enough;
- additional orchestration does not materially improve quality.

### Pattern: workflow

Use when the process can be enumerated in advance.

Common workflow patterns include:

- prompt chaining;
- routing;
- parallelization;
- evaluator-optimizer;
- fixed tool pipelines.

Workflows trade some flexibility for predictability and observability.

### Pattern: agent

Use when:
- required steps cannot be reliably predicted;
- the model must adapt based on tool results;
- the task is open-ended;
- dynamic planning provides measurable benefit.

Agents usually cost more, take longer, and introduce more opportunities for compounding error.

### Pattern: hybrid

Many production systems combine deterministic workflow stages with a bounded agent inside one stage.

Example:

```text
deterministic intake
  → agent investigates case
  → deterministic policy gate
  → human approval if high risk
  → deterministic execution
```

### Decision rules

Prefer the least autonomous pattern that meets the requirement.

Escalate complexity only when an evaluation demonstrates that the simpler design fails an important quality target.

### Common traps

- Choosing an agent because the task has multiple steps.
- Confusing "uses tools" with "is an agent."
- Adding multiple agents when a single agent plus good tools is sufficient.
- Ignoring the latency and cost of repeated inference.

### Exam cues

Watch for: **predictable steps, open-ended task, dynamic planning, fixed sequence, autonomy, latency, cost, observability**.

---

## D1.4 — Design multi-agent systems and orchestration strategies

### Core idea

Multiple agents are useful when they create **meaningful isolation, parallelism, or specialization**. They are not automatically better than one capable agent.

### What you need to know

A common pattern is **orchestrator-workers**:

1. Orchestrator interprets the goal.
2. It decomposes the task.
3. Workers perform bounded subtasks.
4. Results return through explicit contracts.
5. Orchestrator checks coverage and synthesizes.

Multi-agent design should define:

- worker responsibility;
- input schema;
- output schema;
- timeout behavior;
- retry behavior;
- trace propagation;
- partial-result handling;
- disagreement handling;
- state ownership.

Three strong reasons for multi-agent separation are:

- **context isolation** — workers need separate context to avoid pollution;
- **parallel execution** — independent workstreams can run concurrently;
- **specialization** — different tasks benefit from distinct instructions/tools/models.

### Decision rules

Use multiple agents only when the decomposition boundary improves the system.

Ask: could a single agent with a scoped tool call or subroutine accomplish the same result more simply?

### Common traps

**Agent-per-step architecture.**  
Breaking every step into an agent creates coordination overhead without clear value.

**Unverified synthesis.**  
The coordinator assumes workers completed all required work.

**Shared mutable state everywhere.**  
Workers overwrite or interpret common state inconsistently.

**No trace continuity.**  
Operations cannot reconstruct which worker produced a faulty conclusion.

### Scenario

A due-diligence system must research financial, legal, and technical dimensions independently. Three specialist workers can run in parallel with isolated context, then a coordinator checks required sections and synthesizes a report.

### Exam cues

Watch for: **parallel, specialist, coordinator, workers, context isolation, handoff, synthesis, disagreement**.

---

## D1.5 — Apply decomposition techniques for complex problem solving

### Core idea

Decomposition makes a hard task easier by turning it into **bounded subproblems with explicit contracts**.

### What you need to know

Useful patterns include:

**Prompt chaining** — each stage consumes the previous stage's output.

**Routing** — classify the request and send it to the right specialized path.

**Parallelization** — independent subtasks run concurrently, then results are combined.

**Evaluator-optimizer** — generate, evaluate against criteria, refine.

**Orchestrator-workers** — the model dynamically determines subtasks.

The architectural value comes from making responsibilities clear, not from maximizing the number of model calls.

### Decision rules

Decompose when:
- subtasks require different context;
- different stages need different models or tools;
- intermediate output can be validated;
- independent steps can run in parallel;
- a failure should be isolated rather than contaminate the entire run.

Keep work together when decomposition would force excessive context transfer or create coordination cost larger than the benefit.

### Common traps

- Decomposing by organizational team rather than information/control boundary.
- Passing enormous worker transcripts instead of concise outputs.
- Using an LLM for deterministic transformations that code can perform more reliably.
- Adding a critique loop without measurable criteria.

### Exam cues

Watch for: **decompose, route, parallelize, validate intermediate output, isolate context, evaluator**.

---

## D1.6 — Align solutions to business value

### Core idea

A technically impressive architecture can still be a poor solution if it does not produce enough value for its cost and risk.

### What you need to know

Tie architecture metrics to business metrics.

Technical measures:
- accuracy/task success;
- latency;
- throughput;
- availability;
- token use;
- cost per task;
- escalation rate.

Business measures:
- time saved;
- cases resolved;
- revenue protected/created;
- error reduction;
- employee productivity;
- customer satisfaction;
- cycle-time reduction.

A simple value chain is:

```text
baseline
  → technical improvement
  → operational change
  → measurable business outcome
  → ongoing operating cost
```

### Decision rules

Define a baseline before claiming improvement.

Evaluate total solution cost, not only model-token cost. Include engineering complexity, human review, infrastructure, monitoring, incident response, and compliance overhead.

### Common traps

- Optimizing token cost while degrading task success.
- Reporting model accuracy without connecting it to a business result.
- Comparing two architectures without accounting for operational complexity.
- Treating human review as free.

### Scenario

Architecture A costs half as much per request but doubles escalation to human reviewers. Architecture B has higher model cost but lower total operational cost because it reduces manual review. The business comparison must include both.

### Exam cues

Watch for: **ROI, baseline, productivity, total cost, throughput, SLO, measurable outcome**.

---

## Domain 1 summary

Remember this sequence:

```text
outcome
→ constraints
→ responsibility split
→ simplest viable architecture
→ failure boundaries
→ evaluation
→ business value
```

## Primary references

- Anthropic, “Building Effective AI Agents”  
  https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, “Effective Context Engineering for AI Agents”  
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
