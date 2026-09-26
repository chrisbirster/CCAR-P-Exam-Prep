# CCAR-P Concept Notes

These notes are the **canonical study source** for the CCAR-P flashcard deck.

The content pipeline is:

```text
Anthropic exam blueprint + current official documentation
                    ↓
            concept notes (here)
                    ↓
          Deez logical notes
                    ↓
         generated study cards
                    ↓
               ccar-p.nut
```

The goal is to avoid generating 2,000 disconnected flashcards. Every future Deez note should be traceable to one or more concepts in these files.

## Domains

| Domain | Weight | Objectives | Notes |
| --- | ---: | ---: | --- |
| D1 — Solution Design & Architecture | 17% | 6 | [Study notes](d1-solution-design.md) |
| D2 — Models, Prompting & Context Engineering | 13% | 5 | [Study notes](d2-models-prompting-context.md) |
| D3 — Integration | 19% | 8 | [Study notes](d3-integration.md) |
| D4 — Evaluation, Testing & Optimization | 16% | 6 | [Study notes](d4-evaluation-testing-optimization.md) |
| D5 — Governance, Safety & Risk Management | 14% | 5 | [Study notes](d5-governance-safety-risk.md) |
| D6 — Stakeholder Communication & Lifecycle | 14% | 5 | [Study notes](d6-stakeholder-lifecycle.md) |
| D7 — Developer Productivity & Operational Enablement | 7% | 3 | [Study notes](d7-developer-productivity.md) |
| **Total** | **100%** | **38** | |

## How to read the notes

Each objective uses the same structure:

- **Core idea** — the concept in plain language.
- **What you need to know** — the facts and distinctions that matter.
- **Decision rules** — how an architect should reason under constraints.
- **Common traps** — plausible but weak choices.
- **Scenario** — how the concept appears in an architecture problem.
- **Exam cues** — words in a question that should trigger the concept.

These are study notes, not reconstructed exam questions. Practice scenarios are original.

## Source hierarchy

When sources disagree, use this order:

1. Anthropic's current CCAR-P exam guide.
2. Current Anthropic documentation and engineering guidance.
3. Current Model Context Protocol specification for MCP behavior.
4. These study notes.
5. Flashcards derived from these notes.

Product capabilities and model names can change faster than architecture principles. The notes therefore emphasize durable decision-making concepts and call out time-sensitive product details only when useful.

_Last reviewed: September 26, 2026._


## Verification

Before these notes become flashcards, use the [Sources & Verification](../sources-and-verification.md) matrix to distinguish:

- official blueprint statements;
- first-party Anthropic/MCP guidance;
- architecture interpretations;
- time-sensitive product details.

No `.nut` note should be published without passing that evidence gate.
