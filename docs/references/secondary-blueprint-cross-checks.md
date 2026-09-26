# Secondary Blueprint Cross-Checks

**Purpose:** preserve the public secondary sources used to cross-check the CCAR-P v1.0 domain weights and task statements when the official Partner Academy exam guide is not directly accessible.

**Status:** Secondary evidence only  
**Verified:** September 26, 2026

> These sites are **not authoritative** for the exam. Anthropic's current CCAR-P Exam Guide is the source of truth. We use these pages only to independently cross-check the public blueprint structure until we can audit against the official guide itself.

## Claude Certification Guide

https://claudecertificationguide.com/ccar-p

Used to cross-check:
- domain names;
- domain weights;
- several published task statements.

## KokoKnows AI — Claude Architect Professional

https://kokoknows.ai/trainings/claude-architect-professional/integration

Used to cross-check:
- Domain 3 Integration objectives;
- wording around authentication/authorization;
- connection protocol selection.

## Claude Mock Exams — Architect Professional / Integration

https://claudemockexams.com/architect-professional/integration

Used to cross-check:
- Domain 3 Integration task coverage;
- retrieval strategy;
- observability;
- progressive discovery.

## Claude Architect Guide

https://claudearchitectguide.com/guide

Used to cross-check:
- high-level exam-domain structure;
- Integration as the highest-weighted domain.

## How these sources may be used

Allowed:
- confirm that multiple independent public reproductions agree on the same blueprint structure;
- spot possible transcription discrepancies that should be checked against the official guide.

Not allowed:
- override Anthropic's official exam guide;
- treat their study advice as official Anthropic guidance;
- use their practice questions as evidence for technical claims;
- use them as the primary source for flashcard answers when a first-party source exists.

## Current audit rule

For every flashcard:

```text
Exam scope → official CCAR-P guide preferred
Technical fact → Anthropic/MCP primary source preferred
Secondary source → cross-check only
Architecture heuristic → explicitly labeled interpretation
```

If the official CCAR-P Exam Guide PDF becomes available to this project, these secondary sources become optional corroboration rather than necessary blueprint evidence.
