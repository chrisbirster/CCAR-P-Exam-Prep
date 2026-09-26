# CCAR-P Sources & Verification

**Purpose:** document what is official, what is first-party technical guidance, and what is our study interpretation before any material becomes a Deez flashcard.

**Last verified:** September 26, 2026

> This repository is an independent study resource. The current Anthropic CCAR-P Exam Guide remains authoritative for exam scope. If the official Exam Guide PDF is available, it should be treated as the single source of truth for exact blueprint wording and sample-question rationales.

## Verification levels

Every concept used for flashcards should fit one of these evidence levels.

### A — Blueprint statement

The concept appears directly in the CCAR-P v1.0 blueprint/task statements.

Examples:
- select appropriate architectural patterns;
- design a RAG pipeline;
- evaluate progressive discovery vs. monolithic context;
- apply human-in-the-loop validation;
- support lifecycle phases.

These are safe to use as exam-scope facts.

### B — First-party technical guidance

The detail is supported by current Anthropic documentation, Anthropic Engineering/Research, or the current Model Context Protocol specification.

Examples:
- workflows follow predefined paths while agents dynamically direct their own tool use;
- use on-demand tool discovery to avoid large tool-definition context;
- few-shot examples should be relevant and diverse;
- model migrations should be tested before production;
- prompt injection remains an unsolved risk for agents consuming untrusted content.

These are safe to teach as current technical guidance, with a source.

### C — Architecture interpretation

The detail is a reasonable study heuristic derived from the objective and established architecture practice, but is not presented as an Anthropic rule.

Examples:
- “Prefer the least autonomous pattern that meets the requirement.”
- “Use a live API for current transactional state.”
- “A reviewer should receive enough evidence to make a meaningful decision.”

These can be useful, but flashcards must label them as decision heuristics rather than official product facts.

### D — Time-sensitive product detail

Model names, pricing, beta features, limits, exact API behavior, and MCP protocol revisions can change.

These require an explicit source and verification date before becoming a flashcard.

---

## Blueprint cross-check

The following blueprint is consistently reproduced by current public references that identify themselves as transcriptions/summaries of **CCAR-P Exam Guide v1.0, effective July 2026**.

| Domain | Weight | Objectives |
| --- | ---: | ---: |
| D1 — Solution Design & Architecture | 17% | 6 |
| D2 — Claude Models, Prompting & Context Engineering | 13% | 5 |
| D3 — Integration | 19% | 8 |
| D4 — Evaluation, Testing & Optimization | 16% | 6 |
| D5 — Governance, Safety & Risk Management | 14% | 5 |
| D6 — Stakeholder Communication & Lifecycle Management | 14% | 5 |
| D7 — Developer Productivity & Operational Enablement | 7% | 3 |
| **Total** | **100%** | **38** |

### D1 task statements

1. Translate business problems into Claude-based AI solutions.
2. Design end-to-end architectures (input → processing → output → feedback loops).
3. Select appropriate architectural patterns (workflow, agentic, augmented LLM).
4. Design multi-agent systems and orchestration strategies.
5. Apply decomposition techniques for complex problem solving.
6. Align solutions to business value pillars (efficiency, transformation, productivity, cost, performance SLAs).

### D2 task statements

1. Select appropriate Claude models based on trade-offs.
2. Design system prompts, templates, and guardrails.
3. Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought).
4. Optimize context windows and manage token usage.
5. Implement prompt reuse strategies (caching, modular prompts, Skills).

### D3 task statements

1. Evaluate tool/agent configuration for capability bloat.
2. Analyze authentication and authorization requirements to identify security gaps.
3. Evaluate accuracy-latency trade-offs and justify configuration decisions.
4. Analyze observability challenges and select monitoring strategies at scale.
5. Design a RAG pipeline with appropriate chunking and indexing strategies.
6. Apply retrieval strategies matched to data shape and query pattern.
7. Evaluate connection protocols and select the appropriate integration mechanism (MCP, API/CLI, agent-to-agent).
8. Evaluate progressive discovery vs. monolithic context strategy.

### D4 task statements

1. Define evaluation metrics (accuracy, latency, cost, safety, security).
2. Design evaluation datasets and test frameworks using mixed methodologies.
3. Conduct A/B testing and iterative improvements.
4. Diagnose system issues (prompt failure, hallucinations, model mismatch).
5. Optimize token usage, latency, and cost-performance trade-offs.
6. Monitor system performance using logging and observability tools.

### D5 task statements

1. Implement guardrails and safety controls.
2. Identify risks, limitations, and failure modes of LLM systems.
3. Apply human-in-the-loop validation strategies.
4. Ensure compliance with regulations (e.g., GDPR, HIPAA, FedRAMP).
5. Address ethical AI considerations (bias, fairness, transparency).

### D6 task statements

1. Conduct structured discovery and requirement gathering.
2. Communicate architectural decisions and trade-offs.
3. Manage stakeholder feedback loops and expectation alignment (including SLAs).
4. Document architectures and provide implementation guidance.
5. Support lifecycle phases (discovery, design, handoff, monitoring, iteration).

### D7 task statements

1. Configure Claude tools and environments for teams (e.g., Claude Code).
2. Improve developer workflows using AI-assisted tooling.
3. Support debugging and operational issue resolution.

---

## Objective-by-objective evidence matrix

| Objective | Blueprint | Primary technical evidence | Notes status |
| --- | --- | --- | --- |
| D1.1 | A | Building Effective AI Agents | A/C |
| D1.2 | A | Building Effective AI Agents; Evals guidance | A/B/C |
| D1.3 | A | Building Effective AI Agents | A/B |
| D1.4 | A | Anthropic multi-agent research system | A/B |
| D1.5 | A | Building Effective AI Agents | A/B |
| D1.6 | A | Blueprint business-value wording | A/C |
| D2.1 | A | Claude model lifecycle/deprecation docs | A/B/D |
| D2.2 | A | Prompting best practices | A/B |
| D2.3 | A | Prompting best practices | A/B/D |
| D2.4 | A | Effective Context Engineering for AI Agents | A/B |
| D2.5 | A | Agent Skills; prompt-caching docs/pricing | A/B/D |
| D3.1 | A | Writing Effective Tools; Advanced Tool Use | A/B |
| D3.2 | A | MCP authorization specification | A/B/C/D |
| D3.3 | A | Advanced Tool Use; general SLO reasoning | A/B/C |
| D3.4 | A | Evals guidance; multi-agent research traces | A/B/C |
| D3.5 | A | Contextual Retrieval | A/B |
| D3.6 | A | Contextual Retrieval | A/B/C |
| D3.7 | A | Current MCP specification | A/B/C/D |
| D3.8 | A | Advanced Tool Use; Agent Skills progressive disclosure | A/B |
| D4.1 | A | Demystifying Evals for AI Agents | A/B |
| D4.2 | A | Demystifying Evals for AI Agents | A/B |
| D4.3 | A | Blueprint + standard controlled-experiment practice | A/C |
| D4.4 | A | Demystifying Evals for AI Agents | A/B/C |
| D4.5 | A | Anthropic pricing/caching/tool-use guidance | A/B/C/D |
| D4.6 | A | Demystifying Evals for AI Agents | A/B/C |
| D5.1 | A | Safe/trustworthy agents framework | A/B/C |
| D5.2 | A | Prompt-injection defenses; trustworthy-agent guidance | A/B |
| D5.3 | A | Blueprint + risk-based architecture practice | A/C |
| D5.4 | A | Blueprint only for named regulations; legal details require primary regulatory sources | A/C |
| D5.5 | A | Blueprint + responsible-AI architecture practice | A/C |
| D6.1 | A | Blueprint + architecture requirements practice | A/C |
| D6.2 | A | Blueprint + architecture decision practice | A/C |
| D6.3 | A | Blueprint + eval/SLO practice | A/B/C |
| D6.4 | A | Blueprint + architecture documentation practice | A/C |
| D6.5 | A | Blueprint | A/C |
| D7.1 | A | Claude Code docs; Agent Skills | A/B/D |
| D7.2 | A | Claude Code docs | A/B/C |
| D7.3 | A | Claude Code docs; eval/observability guidance | A/B/C |

---

## First-party technical sources

### Anthropic — Building Effective AI Agents
https://www.anthropic.com/engineering/building-effective-agents

Supports:
- workflows vs. agents;
- prompt chaining;
- routing;
- parallelization;
- orchestrator-workers;
- evaluator-optimizer;
- preference for simple composable patterns;
- adding complexity only when it improves outcomes.

### Anthropic — Effective Context Engineering for AI Agents
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

Supports:
- context as a finite resource;
- just-in-time retrieval;
- compaction;
- structured note-taking/state;
- context isolation;
- long-horizon context management.

### Anthropic — How We Built Our Multi-Agent Research System
https://www.anthropic.com/engineering/multi-agent-research-system

Supports:
- lead-agent/subagent orchestration;
- parallel research;
- isolation of prompts/tools/trajectories;
- coordination complexity;
- multi-agent evaluation considerations.

### Anthropic — Writing Effective Tools for Agents
https://www.anthropic.com/engineering/writing-tools-for-agents

Supports:
- choosing which tools to expose;
- clear tool boundaries;
- useful tool responses;
- token efficiency;
- tool descriptions/specifications;
- evaluating tool interfaces.

### Anthropic — Advanced Tool Use
https://www.anthropic.com/engineering/advanced-tool-use

Supports:
- tool-definition context bloat;
- on-demand tool discovery;
- programmatic tool calling;
- tool-use examples;
- cases where progressive discovery is useful.

### Anthropic — Contextual Retrieval
https://www.anthropic.com/engineering/contextual-retrieval

Supports:
- RAG;
- embedding-based semantic retrieval;
- BM25/lexical retrieval;
- contextual embeddings;
- hybrid retrieval and reranking concepts.

### Anthropic — Demystifying Evals for AI Agents
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

Supports:
- tasks/trials;
- graders;
- transcripts/trajectories;
- outcomes;
- harnesses/suites;
- regression and capability evaluation;
- end-to-end agent evaluation.

### Anthropic — Prompting Best Practices
https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables

Supports:
- clear/direct instructions;
- roles;
- examples;
- XML structure;
- long-context prompting;
- current thinking/reasoning guidance;
- subagent orchestration guidance.

### Anthropic — Model Deprecations
https://docs.anthropic.com/en/docs/about-claude/model-deprecations

Supports:
- Active / Legacy / Deprecated / Retired lifecycle states;
- migration testing;
- retirement behavior.

### Anthropic — Agent Skills
https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

Supports:
- Skills as reusable instruction/script/resource packages;
- progressive disclosure;
- dynamic loading;
- portability and reuse.

### Anthropic — Prompt Injection Defenses
https://www.anthropic.com/news/prompt-injection-defenses

Supports:
- indirect prompt injection from untrusted content;
- prompt injection as an ongoing security problem;
- layered defenses;
- continued residual risk.

### Anthropic — Safe and Trustworthy Agents Framework
https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents

Supports:
- agent misuse/security risks;
- prompt injection;
- layered defenses;
- monitoring and risk reduction.

### Claude Code documentation
https://docs.anthropic.com/en/docs/claude-code/cli-usage

Supports:
- permission modes;
- allowed/disallowed tools;
- model selection;
- agent turn limits;
- MCP configuration surface.

### Model Context Protocol
https://modelcontextprotocol.io/specification/

Current protocol reference for:
- client/server protocol behavior;
- capabilities;
- authorization;
- protocol revisions;
- security-sensitive integration behavior.

The MCP specification is independently versioned. Any card about exact MCP wire behavior must record the protocol revision.

---

## Known corrections made during audit

### Model lifecycle wording

Earlier notes summarized the lifecycle as “active, deprecated, retired.”

Current Anthropic documentation also includes **Legacy**.

Correct set:

```text
Active → Legacy → Deprecated → Retired
```

Not every model necessarily spends equal time in each state, but these are the documented lifecycle labels.

### Chain-of-thought / thinking wording

The D2.3 blueprint names “chain-of-thought” as a prompt-engineering technique.

Current Anthropic model guidance is more nuanced: current Claude models may support native/adaptive thinking, and manual chain-of-thought prompting is not universally the preferred production technique.

Flashcards should therefore distinguish:

- **Blueprint scope:** know chain-of-thought as a prompting concept.
- **Current product guidance:** use the model's current supported thinking controls/guidance rather than blindly forcing visible step-by-step reasoning.

### Compliance

The blueprint explicitly names GDPR, HIPAA, and FedRAMP.

Our notes explain architectural implications, but they **must not be used as legal/compliance authority**. Any card should test architecture reasoning (data handling, access, logging, retention, deployment boundary, evidence), not invent legal requirements.

### MCP

MCP evolves quickly. The current specification has changed substantially since its early versions.

Flashcards should emphasize durable decisions:
- when standard interoperability is useful;
- capability discovery;
- authorization boundaries;
- least privilege.

Exact transport/auth fields should only become cards when tied to a specific current MCP spec revision.

---

## Flashcard publication gate

A proposed Deez note should not enter `ccar-p.nut` unless:

- [ ] It maps to at least one objective.
- [ ] Its answer is supported by Level A, B, or clearly labeled C evidence.
- [ ] Any Level D fact has a source and verification date.
- [ ] It does not turn a heuristic into a claimed Anthropic rule.
- [ ] It does not contain reconstructed/confidential exam content.
- [ ] The answer is independently understandable.
- [ ] The note type fits what is being tested.
- [ ] Distractors in choice questions are plausible but demonstrably wrong under the stated constraints.

---

## Highest-confidence source

The official **Claude Certified Architect – Professional Exam Guide v1.0** is the strongest source for:
- exact task statements;
- domain weighting;
- exam format;
- official sample questions and rationales.

Public web access to the Partner Academy copy can be restricted. If a legally obtained official Exam Guide PDF is available, add it to the private study workflow (or provide it for verification) and perform a line-by-line blueprint audit before the final 2,000-card deck is frozen.
