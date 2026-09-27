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

Every source note records its objective, note type, kind, human-approved evidence state, source packet, fields, and tags.

Build with: `python3 scripts/build_flashcards.py --priority p0`

Audit with: `python3 scripts/audit_flashcards.py`

The auditor rejects malformed interaction fields, missing tags/source references, duplicate prompts, wrong counts, missing objectives, and P0 cloze notes that would create more than one card.
