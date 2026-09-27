# Flashcard Source

This directory contains inspectable logical-note source files. Generated `.nut` and API artifacts are derived from these files.

## Final deck contract

The completed CCAR-P deck contains exactly:

- **1,780 logical Deez notes**
- **2,000 generated study cards**
- **all 38 objectives**
- zero duplicate normalized prompts across P0 + P1 + P2

### Priority tiers

| Tier | Logical notes | Generated cards |
| --- | ---: | ---: |
| P0 | 630 | 700 |
| P1 | 710 | 800 |
| P2 | 440 | 500 |
| **Total** | **1,780** | **2,000** |

### Final note-type allocation

| Type | Logical notes | Generated cards |
| --- | ---: | ---: |
| basic | 320 | 320 |
| basic-reverse | 220 | 440 |
| cloze | 300 | 300 |
| type-answer | 220 | 220 |
| multiple-choice | 340 | 340 |
| multiple-select | 280 | 280 |
| ordering | 100 | 100 |
| **Total** | **1,780** | **2,000** |

### P2 domain targets

D1 85, D2 65, D3 95, D4 80, D5 70, D6 70, D7 35 = **500 cards**.

P1 is deterministically generated from approved P0 evidence seeds with `scripts/generate_p1.py`. P2 is deterministically generated from approved P1 evidence seeds with `scripts/generate_p2.py`.

Every source note retains:
- objective;
- priority;
- card kind;
- human-approved evidence state;
- objective source packet;
- seed provenance;
- Deez note type;
- fields;
- tags.

Build:

```bash
python3 scripts/generate_p1.py
python3 scripts/generate_p2.py
python3 scripts/audit_flashcards.py --priority p0 --priority p1 --priority p2 --cross-priority
python3 scripts/build_flashcards.py --priority p0
python3 scripts/build_flashcards.py --priority p1
python3 scripts/build_flashcards.py --priority p2
python3 scripts/build_combined_flashcards.py
```

The audit rejects malformed interaction fields, missing tags/source references, duplicate IDs/prompts, incorrect domain/type totals, missing objectives, and cloze notes that would unexpectedly create multiple cards.
