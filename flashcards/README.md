# Flashcards

The CCAR-P deck targets **2,000 generated Deez cards** across P0, P1, and P2.

## P0 — complete

The must-know P0 tier is now built and audited:

- **630 logical Deez notes**
- **700 generated study cards**
- **all 38 objectives covered**
- exact domain-weighted allocation
- exact planned P0 note-type mix
- human-approved source packet attached to every objective
- zero duplicate normalized prompts

Artifacts:

- [ccar-p-p0.nut](ccar-p-p0.nut) — shareable Deez v2 deck
- [ccar-p-p0-api.json](ccar-p-p0-api.json) — full bulk API payload
- [batches/p0-01.json](batches/p0-01.json) — 200 logical notes
- [batches/p0-02.json](batches/p0-02.json) — 200 logical notes
- [batches/p0-03.json](batches/p0-03.json) — 200 logical notes
- [batches/p0-04.json](batches/p0-04.json) — 30 logical notes
- [source/](source/) — inspectable source-of-truth logical notes

Build and audit:

```bash
python3 scripts/audit_flashcards.py
python3 scripts/build_flashcards.py --priority p0
```

## Remaining deck

The full plan remains:

- P0 — 700 generated cards — **complete**
- P1 — 800 generated cards — pending
- P2 — 500 generated cards — pending
- Total — 2,000 generated cards

See [the flashcard plan](../docs/flashcard-plan.md) for the allocation, note-type rules, quality gate, and one-week study strategy.

The deck contains original study material derived from the published exam objectives and approved public references. Do not contribute memorized, copied, reconstructed, or confidential live exam questions.
