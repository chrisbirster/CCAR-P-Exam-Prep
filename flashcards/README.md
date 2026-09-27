# Flashcards

The CCAR-P deck targets **2,000 generated Deez cards** across P0, P1, and P2.

## P0 — complete

- **630 logical notes**
- **700 generated cards**
- all 38 objectives
- must-know architecture/security/evaluation coverage

Artifacts:

- [ccar-p-p0.nut](ccar-p-p0.nut)
- [ccar-p-p0-api.json](ccar-p-p0-api.json)
- [batches/p0-01.json](batches/p0-01.json)
- [batches/p0-02.json](batches/p0-02.json)
- [batches/p0-03.json](batches/p0-03.json)
- [batches/p0-04.json](batches/p0-04.json)

## P1 — complete

- **710 logical notes**
- **800 generated cards**
- all 38 objectives
- broader scenarios, applied recall, nuance, and operational trade-offs
- zero duplicate normalized prompts across P0 + P1

Artifacts:

- [ccar-p-p1.nut](ccar-p-p1.nut)
- [ccar-p-p1-api.json](ccar-p-p1-api.json)
- [batches/p1-01.json](batches/p1-01.json) — 200 notes
- [batches/p1-02.json](batches/p1-02.json) — 200 notes
- [batches/p1-03.json](batches/p1-03.json) — 200 notes
- [batches/p1-04.json](batches/p1-04.json) — 110 notes

[Inspect the source contract](source/).

## Combined deck

Use this if you want one deck in deez.run instead of separate P0 and P1 decks.

- **1,340 logical notes**
- **1,500 generated cards**
- deck name: **CCAR-P Exam Prep**
- preserves `priority:p0` and `priority:p1` tags
- preserves all objective/source tags

Artifacts:

- [ccar-p-combined.nut](ccar-p-combined.nut)
- [ccar-p-combined-api.json](ccar-p-combined-api.json)
- [batches/combined-01.json](batches/combined-01.json) — 200 notes
- [batches/combined-02.json](batches/combined-02.json) — 200 notes
- [batches/combined-03.json](batches/combined-03.json) — 200 notes
- [batches/combined-04.json](batches/combined-04.json) — 200 notes
- [batches/combined-05.json](batches/combined-05.json) — 200 notes
- [batches/combined-06.json](batches/combined-06.json) — 200 notes
- [batches/combined-07.json](batches/combined-07.json) — 140 notes

## Progress

- P0 — 700 cards — **complete**
- P1 — 800 cards — **complete**
- P2 — 500 cards — pending
- **Built so far: 1,500 / 2,000 generated cards**

Build and audit:

```bash
python3 scripts/generate_p1.py
python3 scripts/audit_flashcards.py --priority p0 --priority p1 --cross-priority
python3 scripts/build_flashcards.py --priority p0
python3 scripts/build_flashcards.py --priority p1
```

See [the flashcard plan](../docs/flashcard-plan.md) for the final allocation and one-week study strategy.

The deck contains original study material derived from the published exam objectives and approved public references. Do not contribute memorized, copied, reconstructed, or confidential live exam questions.
