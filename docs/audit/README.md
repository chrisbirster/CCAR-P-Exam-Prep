# CCAR-P Notes Audit

This folder records the **objective-by-objective audit** of the study notes before flashcard generation.

## Audit goal

For every objective, verify five things:

1. **Scope fidelity** — does the concept actually map to the CCAR-P blueprint?
2. **Factual correctness** — are product/protocol claims current and accurate?
3. **Evidence quality** — is each important claim supported by a primary source?
4. **Labeling** — are Anthropic facts separated from our architecture interpretations?
5. **Exam usefulness** — is the note focused enough to generate useful flashcards?

## Status values

- **UNREVIEWED** — not audited yet.
- **VERIFIED** — accurate and adequately sourced.
- **VERIFIED WITH INTERPRETATION** — facts are correct, but some decision rules are our architecture heuristics and must be labeled as such.
- **CORRECTED** — audit found and fixed an error or stale statement.
- **NEEDS SOURCE** — plausible claim lacks adequate primary evidence.
- **TIME-SENSITIVE** — correct only as of a specific date/version.

## Audit order

We use a risk-weighted order rather than numerical domain order:

1. **D3 Integration** — 19%; MCP, tools, auth, RAG, progressive discovery.
2. **D2 Models / Prompting / Context** — product guidance changes rapidly.
3. **D5 Governance / Safety / Risk** — security and regulatory claims need careful wording.
4. **D4 Evaluation / Testing / Optimization** — technical methodology.
5. **D1 Solution Design / Architecture** — durable architecture patterns.
6. **D6 Stakeholders / Lifecycle** — mostly durable interpretation.
7. **D7 Developer Productivity** — smaller weight, product details can be time-sensitive.

Within D3, audit:

```text
D3.1 capability bloat
→ D3.2 authn/authz
→ D3.7 integration mechanism / MCP
→ D3.8 progressive discovery
→ D3.5 RAG
→ D3.6 retrieval
→ D3.3 latency
→ D3.4 observability
```

## Progress

| Objective | Status | Audit |
| --- | --- | --- |
| D3.1 | AI REVIEWED — AWAITING HUMAN | [Sources](D3.1-sources.md) · [Audit](d3-integration.md#d31--capability-bloat) |
| D3.2 | UNREVIEWED | |
| D3.3 | UNREVIEWED | |
| D3.4 | UNREVIEWED | |
| D3.5 | UNREVIEWED | |
| D3.6 | UNREVIEWED | |
| D3.7 | UNREVIEWED | |
| D3.8 | UNREVIEWED | |
| D2.1–D2.5 | UNREVIEWED | |
| D5.1–D5.5 | UNREVIEWED | |
| D4.1–D4.6 | UNREVIEWED | |
| D1.1–D1.6 | UNREVIEWED | |
| D6.1–D6.5 | UNREVIEWED | |
| D7.1–D7.3 | UNREVIEWED | |

No flashcard should be considered final until its source objective has passed this audit.
