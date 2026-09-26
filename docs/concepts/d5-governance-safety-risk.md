# D5 — Governance, Safety & Risk Management

**Exam weight:** 14%  
**Objectives:** D5.1–D5.5

Domain 5 is about building systems where safety is an **architecture property**, not a final prompt added before launch.

For regulatory topics, these notes explain architecture concepts and are not legal advice. Real implementations require the appropriate legal, compliance, and security experts.

---

## D5.1 — Implement guardrails and safety controls

### Core idea

Use **defense in depth**. No single control should be expected to handle every failure mode.

### Layers of control

**Model behavior**  
Useful baseline safety behavior.

**System instructions**  
Define role, scope, and expected refusal/escalation behavior.

**Input controls**  
Validate format, classify risky requests, filter prohibited inputs where appropriate.

**Context controls**  
Limit what retrieved/untrusted data can influence.

**Tool controls**  
Least privilege, scoped parameters, allowlists, sandboxing.

**Deterministic authorization**  
Hard gate for protected actions.

**Output controls**  
Schema validation, policy checks, sensitive-data checks.

**Human review**  
Used when consequence or regulation requires judgment/approval.

### Fail open vs. fail closed

For a high-risk authorization or safety check, failure should often block the action (**fail closed**).

For a low-risk optional enhancement, fallback behavior may be acceptable.

### Decision rules

Put the control at the boundary where it can actually enforce the property.

Example: refund authorization belongs in the transaction/control layer, not solely in the system prompt.

### Common traps

- One giant "safety prompt."
- Logging instead of prevention.
- Output moderation after an irreversible action already occurred.
- Giving the agent admin tools and relying on instructions not to misuse them.

### Exam cues

Watch for: **guardrail, defense in depth, fail closed, sandbox, policy gate, least privilege**.

---

## D5.2 — Identify risks, limitations, and failure modes

### Core idea

Architects should identify the failure mode, then choose **prevention, detection, and recovery** controls.

### Hallucination

Model generates unsupported or false information.

Controls:
- grounding;
- retrieval;
- citation/evidence checks;
- deterministic verification;
- human review for consequential decisions.

### Direct prompt injection

User explicitly tries to override trusted instructions.

Controls:
- instruction hierarchy;
- authorization outside the model;
- restricted tools;
- detection/monitoring.

### Indirect prompt injection

Malicious instructions are embedded in external content such as web pages, documents, emails, or tool results.

Controls:
- treat retrieved content as untrusted;
- minimize tool capability;
- isolate sensitive actions;
- require confirmation/authorization;
- sandbox risky browsing/action paths.

Anthropic notes that prompt injection remains a material risk for agents that consume untrusted content and take actions.

### Excessive agency

Agent has more autonomy or permissions than the task requires.

Controls:
- narrower tools;
- spending/action limits;
- stopping conditions;
- approval gates.

### Data exposure

Sensitive data leaks across users, tenants, tools, logs, or model context.

Controls:
- authorization;
- tenant filtering;
- data minimization;
- redaction;
- controlled logging/retention.

### Resource exhaustion

Runaway loops or repeated tool/model calls consume money/time.

Controls:
- iteration budgets;
- token/cost budgets;
- timeouts;
- rate limits;
- circuit breakers.

### Supply-chain/tool risk

Third-party tools, MCP servers, packages, or Skills can introduce malicious or faulty behavior.

Controls:
- review/provenance;
- allowlists;
- version pinning;
- sandboxing;
- least privilege.

### Common traps

- Treating all failures as "hallucinations."
- Assuming a better model eliminates security architecture.
- Giving a model secret material it never needed.

### Exam cues

Watch for: **prompt injection, hallucination, excessive agency, exfiltration, loop, supply chain, untrusted content**.

---

## D5.3 — Apply human-in-the-loop validation

### Core idea

Human involvement should scale with **consequence, irreversibility, uncertainty, and regulatory obligation**.

### Review patterns

**Pre-action approval**  
Human approves before the consequential action occurs.

Best when:
- irreversible;
- high financial/safety impact;
- legally required;
- uncertainty is high.

**Post-action review**  
Action occurs, then a human reviews.

Best when:
- actions are reversible;
- speed matters;
- risk is moderate.

**Sampled review**  
A fraction of low-risk cases are reviewed for quality/control monitoring.

Best for:
- ongoing auditing;
- drift detection;
- mature low-risk workflows.

### Decision rules

A review step is useful only if the reviewer receives enough evidence to make an informed decision.

Do not ask a human to rubber-stamp opaque model output. Show source evidence, relevant policy, proposed action, uncertainty, and reason for escalation.

### Common traps

- Human approval after the irreversible action.
- Reviewing every low-risk case and eliminating the automation value.
- Escalation threshold defined only by model confidence when consequence is more important.
- Reviewers lack source context.

### Exam cues

Watch for: **approval, escalation, confidence, irreversible, high impact, reviewer, oversight**.

---

## D5.4 — Ensure compliance with regulations

### Core idea

Translate obligations into **specific technical/operational controls and evidence**.

A reusable architecture pattern is:

```text
requirement
→ control
→ owner
→ evidence
→ review cadence
```

### What you need to know

Depending on the relevant regulation/standard, architecture may need controls around:

- data classification;
- collection/minimization;
- lawful/authorized processing;
- encryption;
- access control;
- audit logging;
- retention/deletion;
- residency;
- incident response;
- vendor/subprocessor use;
- human oversight;
- change management.

### GDPR-style considerations

Architectural questions can include:
- what personal data is processed;
- purpose and minimization;
- retention/deletion;
- subject rights workflows;
- cross-border transfers;
- automated-decision implications.

### HIPAA-style considerations

Architectural questions can include:
- protected health information boundaries;
- access control;
- audit evidence;
- appropriate vendor agreements;
- minimum-necessary handling.

### FedRAMP-style considerations

Architectural questions can include:
- authorized environment/service scope;
- control inheritance;
- logging/evidence;
- boundary definition;
- configuration/change management.

The exam concept is not memorizing statutes. It is recognizing that compliance requirements alter architecture and must map to enforceable controls and evidence.

### Common traps

- "The model provider is compliant, therefore our entire application is compliant."
- Writing "comply with GDPR" in a prompt.
- Collecting logs without a retention/access policy.
- Treating a compliance badge as a substitute for system boundary analysis.

### Exam cues

Watch for: **GDPR, HIPAA, FedRAMP, retention, residency, audit evidence, control mapping**.

---

## D5.5 — Address responsible/ethical AI considerations

### Core idea

Responsible architecture includes **fairness, transparency, accountability, and traceability** appropriate to the use case.

### Bias and fairness

Aggregate accuracy can hide poor outcomes for a subgroup.

Evaluate relevant slices when the use case affects different populations.

### Transparency

Users/operators should understand:
- when AI is involved where appropriate;
- what the system is intended to do;
- important limitations;
- when a human owns the final decision.

### Explainability

The required explanation depends on the audience.

An engineer may need a trace and retrieved evidence. A customer may need a clear reason and appeal path. A regulator may require control evidence and decision records.

### Accountability

Someone must own:
- the architecture decision;
- the residual risk;
- monitoring;
- incident response;
- policy changes.

### Traceability

Preserve enough evidence to reconstruct important decisions without retaining unnecessary sensitive content forever.

### Common traps

- Reporting only average quality.
- "The AI decided" as an ownership model.
- Treating transparency as exposing internal chain-of-thought.
- Keeping unlimited logs because "more evidence is safer."

### Exam cues

Watch for: **bias, subgroup, fairness, transparency, accountability, explainability, traceability**.

---

## Domain 5 summary

```text
threat
→ prevention
→ detection
→ recovery
→ owner
→ evidence
```

And for consequential actions:

```text
model proposes
→ deterministic controls verify
→ human approves when required
→ action executes
→ audit evidence remains
```

## Primary references

- Anthropic, “Trustworthy Agents in Practice”  
  https://www.anthropic.com/research/trustworthy-agents
- Anthropic, “Mitigating the Risk of Prompt Injections in Browser Use”  
  https://www.anthropic.com/news/prompt-injection-defenses
- Model Context Protocol specification and security guidance  
  https://modelcontextprotocol.io/specification/
