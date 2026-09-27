# Flashcard Source

This directory contains inspectable logical-note source files. Generated .nut and API artifacts are derived from these files.

## P0 contract

P0 covers **all 38 CCAR-P objectives** and produces exactly **630 logical notes → 700 generated study cards**.

| Type | Logical notes | Generated cards |
| --- | ---: | ---: |
| basic | 90 | 90 |
| basic-reverse | 70 | 140 |
| cloze | 80 | 80 |
| type-answer | 60 | 60 |
| multiple-choice | 150 | 150 |
| multiple-select | 140 | 140 |
| ordering | 40 | 40 |

Domain P0 generated-card targets: D1 119, D2 91, D3 133, D4 112, D5 98, D6 98, D7 49.

## P1 contract

P1 covers **all 38 objectives** and produces exactly **710 logical notes → 800 generated study cards**.

| Type | Logical notes | Generated cards |
| --- | ---: | ---: |
| basic | 140 | 140 |
| basic-reverse | 90 | 180 |
| cloze | 130 | 130 |
| type-answer | 90 | 90 |
| multiple-choice | 130 | 130 |
| multiple-select | 100 | 100 |
| ordering | 30 | 30 |
| **Total** | **710** | **800** |

Domain P1 generated-card targets: D1 136, D2 104, D3 152, D4 128, D5 112, D6 112, D7 56.

P1 is deterministically generated from the approved evidence-backed P0 seeds using `scripts/generate_p1.py`. It creates applied recall and scenario reinforcement without changing objective/source provenance.

Every source note records its objective, note type, kind, human-approved evidence state, source packet, fields, and tags. P1 notes also record the P0 seed note ID.

Build:

```bash
python3 scripts/build_flashcards.py --priority p0
python3 scripts/build_flashcards.py --priority p1
```

Audit both tiers together:

```bash
python3 scripts/audit_flashcards.py --priority p0 --priority p1 --cross-priority
```

The audit rejects malformed interaction fields, missing tags/source references, duplicate note IDs/prompts, wrong domain/type counts, missing objectives, and cloze notes that would unexpectedly create multiple cards.
