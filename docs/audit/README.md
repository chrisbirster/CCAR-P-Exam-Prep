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

## Domain collections

- [D1 — Solution Design & Architecture](D1.md) — 6 packets
- [D2 — Models, Prompting & Context](D2.md) — 5 packets
- [D3 — Integration](D3.md) — 8 packets
- [D4 — Evaluation, Testing & Optimization](D4.md) — 6 packets
- [D5 — Governance, Safety & Risk](D5.md) — 5 packets
- [D6 — Stakeholder & Lifecycle](D6.md) — 5 packets
- [D7 — Developer Productivity](D7.md) — 3 packets

**Total:** 38 objective source packets.

## Progress

| Objective | Status | Sources |
| --- | --- | --- |
| D1.1 | SOURCES READY — AWAITING HUMAN | [Sources](D1.1-sources.md) |
| D1.2 | SOURCES READY — AWAITING HUMAN | [Sources](D1.2-sources.md) |
| D1.3 | SOURCES READY — AWAITING HUMAN | [Sources](D1.3-sources.md) |
| D1.4 | SOURCES READY — AWAITING HUMAN | [Sources](D1.4-sources.md) |
| D1.5 | SOURCES READY — AWAITING HUMAN | [Sources](D1.5-sources.md) |
| D1.6 | SOURCES READY — AWAITING HUMAN | [Sources](D1.6-sources.md) |
| D2.1 | SOURCES READY — AWAITING HUMAN | [Sources](D2.1-sources.md) |
| D2.2 | SOURCES READY — AWAITING HUMAN | [Sources](D2.2-sources.md) |
| D2.3 | SOURCES READY — AWAITING HUMAN | [Sources](D2.3-sources.md) |
| D2.4 | SOURCES READY — AWAITING HUMAN | [Sources](D2.4-sources.md) |
| D2.5 | SOURCES READY — AWAITING HUMAN | [Sources](D2.5-sources.md) |
| D3.1 | AI REVIEWED — AWAITING HUMAN | [Sources](D3.1-sources.md) |
| D3.2 | SOURCES READY — AWAITING HUMAN | [Sources](D3.2-sources.md) |
| D3.3 | SOURCES READY — AWAITING HUMAN | [Sources](D3.3-sources.md) |
| D3.4 | SOURCES READY — AWAITING HUMAN | [Sources](D3.4-sources.md) |
| D3.5 | SOURCES READY — AWAITING HUMAN | [Sources](D3.5-sources.md) |
| D3.6 | SOURCES READY — AWAITING HUMAN | [Sources](D3.6-sources.md) |
| D3.7 | SOURCES READY — AWAITING HUMAN | [Sources](D3.7-sources.md) |
| D3.8 | SOURCES READY — AWAITING HUMAN | [Sources](D3.8-sources.md) |
| D4.1 | SOURCES READY — AWAITING HUMAN | [Sources](D4.1-sources.md) |
| D4.2 | SOURCES READY — AWAITING HUMAN | [Sources](D4.2-sources.md) |
| D4.3 | SOURCES READY — AWAITING HUMAN | [Sources](D4.3-sources.md) |
| D4.4 | SOURCES READY — AWAITING HUMAN | [Sources](D4.4-sources.md) |
| D4.5 | SOURCES READY — AWAITING HUMAN | [Sources](D4.5-sources.md) |
| D4.6 | SOURCES READY — AWAITING HUMAN | [Sources](D4.6-sources.md) |
| D5.1 | SOURCES READY — AWAITING HUMAN | [Sources](D5.1-sources.md) |
| D5.2 | SOURCES READY — AWAITING HUMAN | [Sources](D5.2-sources.md) |
| D5.3 | SOURCES READY — AWAITING HUMAN | [Sources](D5.3-sources.md) |
| D5.4 | SOURCES READY — AWAITING HUMAN | [Sources](D5.4-sources.md) |
| D5.5 | SOURCES READY — AWAITING HUMAN | [Sources](D5.5-sources.md) |
| D6.1 | SOURCES READY — AWAITING HUMAN | [Sources](D6.1-sources.md) |
| D6.2 | SOURCES READY — AWAITING HUMAN | [Sources](D6.2-sources.md) |
| D6.3 | SOURCES READY — AWAITING HUMAN | [Sources](D6.3-sources.md) |
| D6.4 | SOURCES READY — AWAITING HUMAN | [Sources](D6.4-sources.md) |
| D6.5 | SOURCES READY — AWAITING HUMAN | [Sources](D6.5-sources.md) |
| D7.1 | SOURCES READY — AWAITING HUMAN | [Sources](D7.1-sources.md) |
| D7.2 | SOURCES READY — AWAITING HUMAN | [Sources](D7.2-sources.md) |
| D7.3 | SOURCES READY — AWAITING HUMAN | [Sources](D7.3-sources.md) |

**Human-approved:** 0 / 38

No flashcard should be considered final until its source objective has passed this audit.
