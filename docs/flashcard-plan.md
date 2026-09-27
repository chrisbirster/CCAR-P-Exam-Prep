# CCAR-P 2,000-Card Flashcard Plan

**Exam window:** one-week sprint  
**Target:** 2,000 generated Deez study cards  
**Source of truth:** published CCAR-P blueprint and current Anthropic preparation material

> The target is **2,000 generated cards**, not necessarily 2,000 logical notes. Deez note types such as `basic-reverse` and `cloze` can generate more than one study card from one note.

## Why 2,000?

With only one week, the objective is broad coverage plus repeated architectural decision practice.

The deck should not be 2,000 trivia prompts. It should combine:

- active recall;
- bidirectional relationships where reversal is meaningful;
- completion/association;
- exact-term recall;
- single-answer architecture decisions;
- multiple-response architecture decisions;
- process and lifecycle ordering.

The exam guide remains the authoritative source for scope.

## Domain allocation

The 2,000-card target follows the current blueprint weights exactly.

| Domain | Weight | Generated cards |
| --- | ---: | ---: |
| D1 — Solution Design & Architecture | 17% | **340** |
| D2 — Claude Models, Prompting & Context Engineering | 13% | **260** |
| D3 — Integration | 19% | **380** |
| D4 — Evaluation, Testing & Optimization | 16% | **320** |
| D5 — Governance, Safety & Risk Management | 14% | **280** |
| D6 — Stakeholder Communication & Lifecycle Management | 14% | **280** |
| D7 — Developer Productivity & Operational Enablement | 7% | **140** |
| **Total** | **100%** | **2,000** |

## Note-type allocation

Deez currently supports these authorable note types:

- `basic`
- `basic-reverse`
- `cloze`
- `type-answer`
- `multiple-choice`
- `multiple-select`
- `ordering`
- `image-occlusion`

For this exam sprint, image occlusion is intentionally excluded unless a diagram later proves valuable.

| Note type | Logical notes | Generated cards | Purpose |
| --- | ---: | ---: | --- |
| Basic | 320 | 320 | Direct concepts, rules, failure modes |
| Basic + Reverse | 220 | 440 | True bidirectional relationships |
| Cloze | 300 | 300* | Relationships, constraints, compact rules |
| Type Answer | 220 | 220 | Exact terminology and short distinctions |
| Multiple Choice | 340 | 340 | Single-best-answer architecture scenarios |
| Multiple Select | 280 | 280 | Exam-style multi-response scenarios |
| Ordering | 100 | 100 | RAG, lifecycle, incident, and workflow sequences |
| Image Occlusion | 0 | 0 | Deferred for the one-week sprint |
| **Total** | **1,780 logical notes** | **2,000 cards** | |

\* Cloze notes in the initial deck use one cloze ordinal each so generated-card totals remain predictable. Multi-cloze notes can be added later.

## Rules for choosing a note type

### Basic

Use when one direction is naturally useful.

Good:

> Why should authorization for a side effect be deterministic?

Avoid turning every definition into a Basic card when another interaction better tests the concept.

### Basic + Reverse

Use only when both directions are independently useful.

Good:

- Authentication ↔ identity
- Authorization ↔ permitted action
- Keyword retrieval ↔ exact identifier/term matching
- Semantic retrieval ↔ conceptual/paraphrased matching

Bad:

- “Why is least privilege important?” ↔ a paragraph-length answer

A reverse card should never produce a nonsensical question.

### Cloze

Use for compact relationships and decision rules.

Example:

> Live transactional state should normally come from the {{c1::system of record}}, not a stale retrieval index.

Keep the missing span meaningful and small.

### Type Answer

Use when the answer should be short and exact.

Examples:

- “What protocol standardizes reusable tool/data surfaces for compatible AI clients?” → `MCP`
- “What testing mode evaluates a candidate without exposing users to its outputs?” → `shadow testing`

Do not use type-answer for long prose.

### Multiple Choice

Use for single-best-answer architecture decisions.

Each distractor must be plausible. Avoid giveaway options.

The explanation should state:

1. why the selected answer fits the constraints;
2. why the strongest distractor does not.

### Multiple Select

Use heavily because the Professional exam includes multiple-response questions.

Each option should be independently testable. Avoid “all of the above.”

The explanation should identify every correct option and briefly reject the tempting incorrect ones.

### Ordering

Use when sequence itself matters.

Good targets:

- RAG pipeline stages;
- discovery → design → handoff → monitoring → iteration;
- incident diagnosis;
- evaluation/change gates;
- authentication/authorization flow.

Do not use ordering for arbitrary lists with no meaningful sequence.

## P0 build status

**P0 is complete:** 630 logical Deez notes generate exactly **700 study cards** across all 38 objectives.

Download/import:

- [P0 Deez deck](../flashcards/ccar-p-p0.nut)
- [P0 API payload](../flashcards/ccar-p-p0-api.json)
- [P0 source notes](../flashcards/source/README.md)

Verified P0 generated-card allocation:

| Domain | P0 cards |
| --- | ---: |
| D1 | 119 |
| D2 | 91 |
| D3 | 133 |
| D4 | 112 |
| D5 | 98 |
| D6 | 98 |
| D7 | 49 |
| **Total** | **700** |

Verified P0 logical-note mix:

| Type | Logical notes | Generated cards |
| --- | ---: | ---: |
| Basic | 90 | 90 |
| Basic + Reverse | 70 | 140 |
| Cloze | 80 | 80 |
| Type Answer | 60 | 60 |
| Multiple Choice | 150 | 150 |
| Multiple Select | 140 | 140 |
| Ordering | 40 | 40 |
| **Total** | **630** | **700** |

The committed source files are audited in CI and must reproduce the committed `.nut`, API payload, and batches byte-for-byte.

## P1 build status

**P1 is complete:** 710 logical Deez notes generate exactly **800 study cards** across all 38 objectives.

Download/import:

- [P1 Deez deck](../flashcards/ccar-p-p1.nut)
- [P1 API payload](../flashcards/ccar-p-p1-api.json)
- [P0/P1 source notes](../flashcards/source/README.md)

Verified P1 generated-card allocation:

| Domain | P1 cards |
| --- | ---: |
| D1 | 136 |
| D2 | 104 |
| D3 | 152 |
| D4 | 128 |
| D5 | 112 |
| D6 | 112 |
| D7 | 56 |
| **Total** | **800** |

Verified P1 logical-note mix:

| Type | Logical notes | Generated cards |
| --- | ---: | ---: |
| Basic | 140 | 140 |
| Basic + Reverse | 90 | 180 |
| Cloze | 130 | 130 |
| Type Answer | 90 | 90 |
| Multiple Choice | 130 | 130 |
| Multiple Select | 100 | 100 |
| Ordering | 30 | 30 |
| **Total** | **710** | **800** |

P0 + P1 now provide **1,500 generated cards**. The cross-priority audit rejects duplicate normalized prompts across both tiers.

The remaining P2 allocation is intentionally preserved at exactly 500 generated cards.

## Priority tiers

Two thousand cards is more material than most people can deeply learn from zero in seven days. Every note therefore receives a priority tag.

### P0 — Must know

**700 generated cards**

Core decision rules, common architecture trade-offs, security boundaries, evaluation logic, RAG/tool distinctions, HITL, and high-value exam scenarios.

Study these first and repeatedly.

### P1 — Strong coverage

**800 generated cards — complete**

Broader scenarios, nuances, integrations, operational trade-offs, and secondary concepts.

### P2 — Breadth / edge cases

**500 generated cards**

Less-common cases, additional comparison prompts, and reinforcement.

If review time becomes constrained, do not sacrifice P0 retention to finish P2.

## Tagging convention

Every logical note should have enough metadata to slice the deck.

Example:

```text
ccarp
d3
obj:d3.7
priority:p0
kind:scenario
source:official
```

Common `kind:` values:

- `concept`
- `compare`
- `decision`
- `scenario`
- `failure-mode`
- `security`
- `evaluation`
- `sequence`

## Quality requirements

Every card should satisfy all of these:

- [ ] Tests one clear idea.
- [ ] Has enough context to answer without guessing what the author meant.
- [ ] Does not depend on another card being visible.
- [ ] Uses current terminology.
- [ ] Avoids invented product limits or undocumented guarantees.
- [ ] Distinguishes policy/control from prompt guidance.
- [ ] Uses plausible distractors for choice questions.
- [ ] Avoids unnecessary reversal.
- [ ] Includes objective and priority tags.
- [ ] Can be answered quickly during spaced repetition.

## API batching

Deez's bulk-note endpoint supports large requests, but the course importer should use smaller atomic batches for easier recovery.

Recommended batch size:

```text
200 logical notes per POST
```

That keeps failures easy to identify and retry while remaining efficient.

## One-week review strategy

### Day 1
D1 + D3 P0 cards. Establish architecture and integration fundamentals.

### Day 2
D4 + D2 P0 cards. Evaluation, models, prompting, and context.

### Day 3
D5 + D6 P0 cards. Safety, governance, stakeholder, lifecycle.

### Day 4
D7 P0 plus P1 across all domains. Begin mixed scenarios.

### Day 5
P1 completion. Heavy multiple-choice and multiple-select review.

### Day 6
Missed cards first. Mixed-domain scenario gauntlet. Add P2 only after weak P0/P1 areas improve.

### Day 7
No coverage chasing. Review missed/due P0 and P1 cards, decision rules, and scenario traps.

## Card-generation order

Generate in this order:

1. P0 scenario cards across all 38 objectives.
2. P0 direct-recall cards needed to support those scenarios.
3. P1 scenarios.
4. P1 recall/reinforcement.
5. P2 breadth.

This prevents the deck from reaching 2,000 cards by padding easy definitions before the high-value material exists.
