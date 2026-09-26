# D2 — Claude Models, Prompting & Context Engineering

**Exam weight:** 13%  
**Objectives:** D2.1–D2.5

Domain 2 asks whether you can choose and configure the **model + instructions + context** layer intelligently. The key idea is that model selection, prompting, and context are architectural variables that must be evaluated against quality, latency, and cost.

---

## D2.1 — Select appropriate Claude models based on trade-offs

### Core idea

Choose a model based on the **task's required capability**, not prestige or habit.

### What you need to know

Model selection is a constrained optimization problem involving:

- quality/capability;
- latency;
- throughput;
- token cost;
- workload complexity;
- tool-use requirements;
- context needs;
- operational risk.

Different workflow stages may justify different models.

A high-capability model may plan or handle exceptional cases while a faster/cheaper model executes routine work. Conversely, using multiple models adds routing and regression complexity, so it should earn its place.

Current model lineups also change. Anthropic maintains model lifecycle states such as active, deprecated, and retired. Architecture should therefore avoid assuming a model name is permanent.

### Decision rules

1. Establish an eval suite for the actual task.
2. Choose the least expensive/lowest-latency model that clears the quality threshold.
3. Route difficult cases upward only if routing improves total economics or quality.
4. Treat model migration as a production change.
5. Re-run regression, latency, safety, and cost tests after changing models.

### Common traps

- "Always use the strongest model."
- "Always use the cheapest model."
- Comparing models on generic benchmarks instead of your workload.
- Swapping models without regression testing.
- Hard-coding assumptions about model behavior indefinitely.

### Scenario

A support workflow has 90% routine classification requests and 10% difficult exception cases. An evaluated router may send routine traffic to a fast model and difficult cases to a stronger model, provided misrouting risk is acceptable.

### Exam cues

Watch for: **capability, model selection, latency, cost, routing, migration, regression**.

---

## D2.2 — Design system prompts, templates, and guardrails

### Core idea

Prompts define **behavioral instructions and context**, but they are not a substitute for enforceable controls.

### What you need to know

A strong system prompt typically establishes:

- role;
- task scope;
- success criteria;
- important constraints;
- output contract;
- tool-use expectations;
- escalation behavior.

Separate stable instructions from untrusted input. User or retrieved content should not be able to silently rewrite fixed policy.

Prompt templates help reuse stable instructions while injecting request-specific variables.

### Behavioral guidance vs. control

Prompt:

> Only issue refunds under $500.

This is useful guidance, but not a security boundary.

Deterministic service:

```text
if refund_amount > allowed_limit:
    deny_or_require_approval()
```

This is enforceable.

Use prompts to explain *how to behave*. Use code, permissions, schemas, policies, and approval systems to enforce *what must be true*.

### Decision rules

- Put stable policy/instructions in the highest-trust prompt layer.
- Keep untrusted content visibly separated.
- Make output contracts explicit.
- Use schemas/validators when downstream systems require structure.
- Enforce authorization outside the model.

### Common traps

- Using a system prompt as access control.
- Allowing retrieved documents to contain unbounded instructions.
- Mixing policy, examples, user data, and retrieved text without structure.
- Writing vague negative instructions instead of explicit desired behavior.

### Exam cues

Watch for: **system prompt, template, guardrail, untrusted content, structural enforcement, authorization**.

---

## D2.3 — Apply prompt-engineering techniques

### Core idea

Use the **lightest prompting technique that passes the eval**.

### What you need to know

**Zero-shot**  
Clear direct instructions without examples. Start here when the task is straightforward.

**Few-shot / multishot**  
Provide representative examples. Useful for ambiguous categorization, formatting, tone, or edge cases. Anthropic's current prompting guidance recommends relevant, diverse examples and notes that several examples can improve consistency.

**Structured prompting**  
Separate instructions, context, examples, and inputs using explicit structure such as XML-style tags when the prompt is complex.

**Structured output**  
Specify a clear schema or output contract when downstream software must parse the result.

**Decomposition**  
Break a complex task into smaller reasoning or workflow stages when a single prompt is unreliable or intermediate validation is valuable.

### Decision rules

Prompt engineering should be driven by failures in evaluation.

If zero-shot already passes, adding examples may waste tokens and create maintenance burden.

If examples are used, make them representative rather than numerous.

### Common traps

- Adding huge prompts before establishing a baseline.
- Using examples that all cover the easy case.
- Overfitting a prompt to the eval set.
- Assuming "more reasoning" always improves output.
- Solving a data/retrieval problem by endlessly rewriting the prompt.

### Scenario

A classifier confuses two similar request types. Adding a few high-quality boundary examples may fix the distinction more directly than adding another model call.

### Exam cues

Watch for: **zero-shot, few-shot, examples, structured output, XML, prompt iteration**.

---

## D2.4 — Optimize context windows and token usage

### Core idea

The context window is a scarce **working set**, not a database.

### What you need to know

Distinguish four concepts:

**Active context** — information currently visible to the model.

**Retrieval** — selecting information from an external corpus when needed.

**Application state** — authoritative structured state stored outside the model.

**Memory/summary** — compressed or persisted information used to continue work.

More context is not automatically better. Irrelevant or stale context can compete with important information and increase cost/latency.

Anthropic's context-engineering guidance emphasizes just-in-time retrieval, compaction, structured note-taking, and context isolation for long-horizon agents.

### Context strategies

**Upfront context**  
Best when the information set is bounded, small enough, and repeatedly relevant.

**Just-in-time retrieval**  
Best when the corpus is large and only a subset is relevant to a given step.

**Compaction/summarization**  
Useful when long-running conversations exceed practical context limits. Preserve decisions, constraints, unresolved work, and important evidence.

**Context isolation**  
Use separate workers/subagents when independent tasks would otherwise pollute one another's context.

### Decision rules

Ask: does Claude need this information **now** to make the next decision?

Keep identifiers and retrieval handles outside the context when full content can be fetched only when needed.

### Common traps

- Loading every document and every tool definition upfront.
- Treating chat history as durable state.
- Summarizing away critical constraints.
- Keeping raw tool results long after their meaning has been extracted.
- Assuming a larger window eliminates relevance problems.

### Exam cues

Watch for: **context window, token budget, compaction, memory, just-in-time, long horizon, context pollution**.

---

## D2.5 — Implement prompt reuse strategies

### Core idea

Reuse stable prompt/context components to reduce cost, latency, and maintenance—but preserve freshness.

### What you need to know

**Prompt caching** is useful when a large stable prefix is reused across requests. Stable content should be organized so that reusable material changes less often than request-specific material.

Good candidates:
- long policy documents;
- large stable instructions;
- reusable examples;
- common reference material.

Poor candidates:
- frequently changing transactional data;
- per-request user state;
- volatile policy that must be immediately current.

**Reusable Skills/procedures** package repeatable operational knowledge and resources for agents. Treat shared prompt assets and Skills as versioned software/configuration: review them, test them, and control who can change them.

### Decision rules

Cache or reuse when:
- content is expensive to send repeatedly;
- content is stable enough;
- reuse does not violate freshness or isolation requirements.

Invalidate or bypass reuse when correctness requires current data.

### Common traps

- Caching rapidly changing business state.
- Letting cached content outlive a policy change.
- Treating shared prompts as unmanaged text snippets.
- Reusing a giant prompt across unrelated workloads.

### Scenario

A legal-review workflow uses the same 80-page policy manual for thousands of requests. Stable reference content is a strong caching candidate, while the current matter status should still come from the live system of record.

### Exam cues

Watch for: **prompt caching, stable prefix, reuse, Skills, versioning, freshness**.

---

## Domain 2 summary

Think:

```text
task requirement
→ model threshold
→ clear instructions
→ only relevant context
→ reuse stable context safely
→ evaluate after every meaningful change
```

## Primary references

- Anthropic Claude Platform, “Prompting Best Practices”  
  https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables
- Anthropic, “Effective Context Engineering for AI Agents”  
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic, model deprecation/lifecycle documentation  
  https://docs.anthropic.com/en/docs/about-claude/model-deprecations
- Anthropic, “Equipping Agents for the Real World with Agent Skills”  
  https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
