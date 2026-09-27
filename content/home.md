# CCAR-P Exam Prep

A public study guide for the **Claude Certified Architect – Professional (CCAR-P)** exam.

This course is built around one idea:

> **Learn to make and defend architecture decisions, not just memorize Claude terminology.**

[Start with the exam objectives](objectives/) · [View the source on GitHub](https://github.com/chrisbirster/CCAR-P-Exam-Prep)

> **Independent study resource:** This project is not affiliated with, endorsed by, or sponsored by Anthropic. Anthropic's current exam guide is the authoritative source for scope, eligibility, policies, and registration.

---

## Exam blueprint

| Domain | Weight | Objectives |
| --- | ---: | ---: |
| Solution Design & Architecture | **17%** | 6 |
| Claude Models, Prompting & Context Engineering | **13%** | 5 |
| Integration | **19%** | 8 |
| Evaluation, Testing & Optimization | **16%** | 6 |
| Governance, Safety & Risk Management | **14%** | 5 |
| Stakeholder Communication & Lifecycle Management | **14%** | 5 |
| Developer Productivity & Operational Enablement | **7%** | 3 |
| **Total** | **100%** | **38** |

Integration is the largest domain, but this is a broad professional architecture exam. Every domain matters.

## The architecture mindset

When you see a scenario, work through it in this order:

```text
business outcome
    ↓
constraints
    ↓
responsibility split
    ↓
architecture pattern
    ↓
model + context
    ↓
integrations + permissions
    ↓
safety + governance
    ↓
evaluation
    ↓
operations + observability
    ↓
ownership + business value
```

A useful default question is:

> What is the simplest architecture that satisfies the stated quality, security, safety, compliance, latency, reliability, and cost constraints?

## Recommended study order

1. **Solution Design & Architecture** — establish the decision framework.
2. **Integration** — connect Claude to enterprise data, tools, and systems safely.
3. **Evaluation, Testing & Optimization** — prove the design works.
4. **Models, Prompting & Context Engineering** — optimize Claude-specific layers.
5. **Governance, Safety & Risk** — add enforceable controls and risk ownership.
6. **Stakeholder Communication & Lifecycle** — make the architecture sustainable.
7. **Developer Productivity & Operational Enablement** — enable teams to operate it without the original architect.

## How to study

### Explain

Can you describe the concept without notes?

### Compare

Can you distinguish it from plausible alternatives?

### Decide

Can you select an architecture under constraints and defend the trade-off?

For CCAR-P, **Decide** is the level that matters most.

## Planned course material

- [Exam Objectives & Study Checklist](objectives/)
- [Concept Notes — all 38 objectives](concepts/)
- [Sources & Verification](verification/)
- [Reference Library](references/)
- [Notes Audit](audit/)
- [2,000-Card Flashcard Plan](flashcards/)
- [Download P0 — 700 generated cards](flashcards/ccar-p-p0.nut)
- [Download P1 — 800 generated cards](flashcards/ccar-p-p1.nut)
- Domain-by-domain lessons
- 2,000-card Deez flashcard deck — **P0 + P1 complete: 1,500 / 2,000 cards**
- Original scenario practice
- Hands-on architecture labs
- Review checklists
- Mock architecture cases

## Flashcard plan

| Domain | Cards |
| --- | ---: |
| D1 — Solution Design & Architecture | 340 |
| D2 — Models, Prompting & Context | 260 |
| D3 — Integration | 380 |
| D4 — Evaluation, Testing & Optimization | 320 |
| D5 — Governance, Safety & Risk | 280 |
| D6 — Stakeholder & Lifecycle | 280 |
| D7 — Developer Productivity | 140 |
| **Total** | **2,000** |

Planned mix:

- **30%** concept and recall
- **20%** compare and contrast
- **40%** architecture scenarios
- **10%** failure modes and common traps

## About practice questions

This project is built from the **published exam objectives**.

Do not contribute memorized, copied, reconstructed, or confidential live exam questions. Practice questions should be original and test the skills described by the published blueprint.

---

**Next:** [Work through the CCAR-P objectives checklist →](objectives/)

_Last reviewed: September 26, 2026._
