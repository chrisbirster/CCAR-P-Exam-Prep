# D3 — Integration

**Exam weight:** 19%  
**Objectives:** D3.1–D3.8

Integration is the highest-weighted domain. It covers how Claude safely obtains information and takes action through tools, APIs, retrieval systems, MCP, and other enterprise boundaries.

---

## D3.1 — Evaluate tool/agent configuration for capability bloat

### Core idea

Every tool, credential, dataset, and side effect exposed to an agent expands both the **decision surface** and the **attack surface**.

### What you need to know

Least privilege for an agent means minimizing:

- tools it can discover;
- operations each tool permits;
- data each tool can return;
- credentials available to the runtime;
- environments it can access;
- side effects it can execute without approval.

Too many similar tools can also reduce accuracy because the model must choose among overlapping definitions.

Anthropic's tool-design guidance stresses choosing the right tools—not simply exposing everything—and current advanced tool-use guidance supports on-demand discovery to avoid huge tool-definition contexts.

### Decision rules

Give the model the smallest capability set that can accomplish the task.

Separate read and write tools when their risk differs.

Prefer bounded, task-level tools over generic "execute arbitrary query" or "run any command" interfaces when possible.

### Common traps

- "It's safe because all actions are logged."
- "The model needs every tool in case it becomes useful."
- One shared admin credential for all users.
- Exposing raw database access when a scoped business API would suffice.

### Scenario

A support assistant needs order status and refund requests. It should not receive a generic database-write tool when two scoped tools can expose exactly those operations.

### Exam cues

Watch for: **least privilege, tool bloat, excessive capability, write access, attack surface, tool selection**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Writing Effective Tools — choose the right tools](../references/writing-effective-tools.md#choose-the-right-tools)
- [Writing Effective Tools — avoid overlapping capability](../references/writing-effective-tools.md#avoid-overlapping-capability)
- [Prompt Injection Defenses — architecture implication](../references/prompt-injection-defenses.md#architecture-implication)

---

## D3.2 — Analyze authentication and authorization requirements

### Core idea

**Authentication proves identity. Authorization determines permitted actions.** The model should not invent either.

### What you need to know

A secure tool call should preserve trusted identity through the request path.

Typical flow:

```text
user authenticates
→ application establishes trusted identity
→ policy determines allowed capability
→ model proposes action
→ deterministic layer authorizes action
→ tool executes under scoped credentials
→ audit record captures actor/action/result
```

User text such as "I am an administrator" is not authentication.

A model statement such as "the user is allowed to do this" is not authorization unless the model is merely reporting a decision produced by an authoritative policy system.

For multi-tenant systems, authorization must also enforce tenant boundaries.

### Decision rules

- Establish identity before the LLM decision layer.
- Keep authorization close to the protected resource/action.
- Use scoped/delegated credentials when acting for a user.
- Re-check authorization for consequential tool calls.
- Record who initiated the action and which identity actually executed it.

### Common traps

- Passing a user role as prompt text and trusting it.
- Using one backend superuser credential for every tenant.
- Letting the model decide access policy.
- Authenticating once but never checking action-level permissions.

### Exam cues

Watch for: **identity, OAuth, scope, tenant, permission, delegated access, authorization, audit**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [MCP Specification — authorization](../references/mcp-specification.md#authorization)
- [MCP Specification — security boundary](../references/mcp-specification.md#security-boundary)
- [Safe and Trustworthy Agents — secure interactions](../references/trustworthy-agents.md#secure-interactions)

---

## D3.3 — Evaluate accuracy–latency trade-offs

### Core idea

Every extra retrieval step, reranker, model call, tool call, or verification stage adds latency. Keep stages that provide **measurable quality value**.

### What you need to know

Measure latency per stage:

```text
request
+ retrieval
+ reranking
+ model inference
+ tool calls
+ verification
= end-to-end latency
```

Track percentiles such as p95/p99, not only averages. A system that is usually fast but occasionally extremely slow may still violate an SLA.

Parallelize truly independent work. Do not parallelize steps with hidden dependencies.

### Decision rules

Add a quality-enhancing stage only when the measured improvement justifies its latency and cost.

Optimize the dominant contributor rather than the easiest component to tweak.

### Common traps

- Adding reranking "because RAG should have reranking."
- Measuring average latency only.
- Parallelizing dependent calls and creating race conditions.
- Lowering latency by removing a safety check that is actually required.

### Scenario

A second retrieval/rerank stage improves grounded accuracy by 0.3% but adds 1.5 seconds to a 2-second SLA. Unless the use case values that marginal gain more than latency, the stage is hard to justify.

### Exam cues

Watch for: **SLA, p95, p99, latency budget, parallel, reranking, trade-off**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Advanced Tool Use — programmatic tool use](../references/advanced-tool-use.md#programmatic-tool-use)
- [Contextual Retrieval — reranking](../references/contextual-retrieval.md#reranking)

---

## D3.4 — Analyze observability challenges at scale

### Core idea

A production AI request must be **reconstructable across components**.

### What you need to know

Useful telemetry can include:

- request/trace ID;
- model/version;
- prompt/config version;
- retrieval query and document IDs;
- tool names and outcomes;
- dependency latency;
- retries;
- errors;
- token counts;
- cost;
- final outcome;
- escalation/review decision.

For agents, a transcript/trajectory shows the sequence of model and tool interactions. This is especially useful when the final output alone does not explain the failure.

Do not log secrets or sensitive content indiscriminately. Observability has its own privacy and retention constraints.

### Decision rules

Propagate one trace identity across model, retrieval, tools, queues, and worker agents.

Log enough to reproduce a failure without turning logs into an uncontrolled copy of sensitive data.

### Common traps

- Separate component logs with no correlation ID.
- Logging only the final model answer.
- Logging secrets/credentials for convenience.
- Having metrics but no owner or response action.

### Exam cues

Watch for: **trace, telemetry, incident, reconstruct, correlation ID, audit, trajectory**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Multi-Agent Research — observability and evaluation](../references/multi-agent-research-system.md#observability-and-evaluation)
- [Demystifying Evals — trajectories / transcripts](../references/demystifying-evals.md#trajectories--transcripts)

---

## D3.5 — Design a RAG pipeline

### Core idea

RAG is a pipeline for selecting relevant external knowledge and placing it in context at inference time.

### Pipeline

```text
source ingestion
→ parsing
→ chunking
→ metadata enrichment
→ indexing
→ query transformation (optional)
→ retrieval
→ metadata filtering
→ reranking (optional)
→ context assembly
→ generation
→ grounding/citation checks
```

### What you need to know

**Chunking** should respect the source structure and likely query patterns. Arbitrary fixed-size chunks can split semantic units.

**Metadata** enables filtering by tenant, date, document type, access policy, jurisdiction, product, etc.

**Retrieval** finds candidates.

**Reranking** can reorder candidates using a stronger relevance signal when first-stage retrieval is broad.

**Context assembly** decides what actually enters the model window.

### Decision rules

Start with the simplest pipeline that meets retrieval quality.

Measure retrieval separately from generation. If the correct document never reaches the model, prompt changes cannot fix the underlying retrieval failure.

### Common traps

- Treating RAG as one component called "vector database."
- Ignoring document permissions during retrieval.
- Mixing obsolete and current policy without metadata.
- Debugging hallucination by changing prompts when retrieval recall is the real failure.

### Scenario

A policy assistant answers incorrectly because the current policy document ranked below an obsolete version. The architecture should address freshness/metadata/ranking rather than merely instructing Claude to "be more accurate."

### Exam cues

Watch for: **ingestion, chunking, embeddings, metadata, retrieve, rerank, grounding, citations**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Contextual Retrieval — Retrieval-Augmented Generation](../references/contextual-retrieval.md#retrieval-augmented-generation)
- [Contextual Retrieval — contextualized chunks](../references/contextual-retrieval.md#contextualized-chunks)
- [Contextual Retrieval — reranking](../references/contextual-retrieval.md#reranking)

---

## D3.6 — Apply retrieval strategies matched to the data

### Core idea

Different queries need different retrieval signals.

### Keyword retrieval

Strong for:
- exact identifiers;
- product codes;
- names;
- error strings;
- uncommon terminology.

### Semantic retrieval

Strong for:
- paraphrases;
- conceptual similarity;
- natural-language questions where wording differs from the source.

### Hybrid retrieval

Combines lexical and semantic signals. Useful when both exact terminology and conceptual similarity matter.

### Metadata filtering

Restricts candidates before/alongside ranking.

Examples:
- tenant ID;
- date;
- jurisdiction;
- security classification;
- document status.

### Live API/tool vs. retrieval

Use retrieval for relatively stable knowledge.

Use a live tool/API for current operational state.

```text
employee handbook → retrieval
current PTO balance → HR API

product manual → retrieval
current inventory → inventory API
```

### Decision rules

Choose the retrieval strategy from the query/data characteristics, not from fashion.

If freshness must be exact, query the system of record rather than hoping an index is synchronized.

### Common traps

- Embeddings for exact-ID lookup.
- RAG for current transactional state.
- Keyword-only retrieval for heavily paraphrased user questions.
- Ignoring permission filters because documents are "internal."

### Exam cues

Watch for: **exact match, semantic similarity, hybrid, freshness, current state, system of record**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Contextual Retrieval — semantic retrieval](../references/contextual-retrieval.md#semantic-retrieval)
- [Contextual Retrieval — lexical / BM25 retrieval](../references/contextual-retrieval.md#lexical--bm25-retrieval)
- [Contextual Retrieval — hybrid retrieval](../references/contextual-retrieval.md#hybrid-retrieval)
- [Contextual Retrieval — architecture interpretation: live state](../references/contextual-retrieval.md#architecture-interpretation-live-state)

---

## D3.7 — Select the appropriate integration mechanism

### Core idea

Use the integration mechanism that matches the ownership, reuse, client, and operational requirements.

### Direct API/SDK

Good when:
- one application owns both sides;
- the integration is narrow;
- you need direct control;
- a reusable AI-specific protocol adds little value.

### CLI

Useful for:
- developer workflows;
- local automation;
- existing operational tools;
- environments where command-line interfaces are already the stable contract.

### MCP

MCP standardizes how compatible AI clients connect to tools/data/capabilities. It is valuable when one tool surface should be reusable across multiple AI clients or when you want a standard discovery/invocation protocol.

MCP does **not** replace authorization, application policy, or source-system controls.

### Agent-to-agent communication

Useful when independent agent systems have genuinely separate responsibilities and need explicit handoff/contracts.

### Managed agent runtime

Useful when the organization wants infrastructure for long-running execution, state, sandboxing, or orchestration managed as a platform rather than built entirely in-house.

### Decision rules

Ask:
- How many clients need this capability?
- Who owns the interface?
- How reusable must it be?
- Where is authentication/authorization enforced?
- What operational dependency does this mechanism introduce?

### Common traps

- Choosing MCP simply because the system uses Claude.
- Wrapping a single private function in a protocol layer with no reuse benefit.
- Assuming MCP means tools are automatically safe.
- Creating agent-to-agent protocols where a normal function/tool boundary is enough.

### Exam cues

Watch for: **MCP, SDK, API, reusable tool surface, client interoperability, managed runtime**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [MCP Specification — what MCP provides](../references/mcp-specification.md#what-mcp-provides)
- [MCP Specification — capability discovery](../references/mcp-specification.md#capability-discovery)
- [MCP Specification — security boundary](../references/mcp-specification.md#security-boundary)

---

## D3.8 — Evaluate progressive discovery vs. monolithic context

### Core idea

Do not preload every possible tool or resource when the model needs only a few.

### What you need to know

Large tool catalogs have two costs:

- token/context overhead;
- selection confusion between similar tools.

Progressive discovery keeps a small high-value set visible and loads additional tools only when needed.

Anthropic's advanced tool-use work reports that very large MCP/tool libraries can consume huge portions of context before the task begins; on-demand discovery is designed to address this.

### Decision rules

Always load:
- a small set of frequent/critical tools.

Discover on demand:
- long-tail tools;
- specialist tools;
- tools from many independent systems.

Progressive discovery is a context optimization, not permission by itself. Discovery must still respect what the caller is allowed to access.

### Common traps

- Loading hundreds of tool definitions into every request.
- Confusing hidden-from-context with unauthorized.
- Building a tool-search layer for a catalog of five simple tools.

### Exam cues

Watch for: **tool catalog, context bloat, dynamic discovery, defer loading, long tail, tool confusion**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Advanced Tool Use — tool-definition context bloat](../references/advanced-tool-use.md#tool-definition-context-bloat)
- [Advanced Tool Use — on-demand tool discovery](../references/advanced-tool-use.md#on-demand-tool-discovery)
- [Agent Skills — progressive disclosure](../references/agent-skills.md#progressive-disclosure)

---

## Domain 3 summary

```text
least privilege
→ trusted identity
→ correct integration boundary
→ correct retrieval source
→ only relevant capabilities/context
→ end-to-end tracing
```

## Primary references

- Anthropic, “Writing Effective Tools for AI Agents”  
  https://www.anthropic.com/engineering/writing-tools-for-agents
- Anthropic, “Introducing Advanced Tool Use on the Claude Developer Platform”  
  https://www.anthropic.com/engineering/advanced-tool-use
- Anthropic, “Building Effective AI Agents”  
  https://www.anthropic.com/engineering/building-effective-agents
- Model Context Protocol specification  
  https://modelcontextprotocol.io/specification/
