#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLASH = ROOT / "flashcards"
BATCHES = FLASH / "batches"
PRIORITIES = ("p0", "p1", "p2")
DECK_NAME = "CCAR-P Exam Prep"
EXPECTED_LOGICAL = 1780
EXPECTED_CARDS = 2000
BATCH_SIZE = 200

def main() -> None:
    notes: list[dict] = []
    for priority in PRIORITIES:
        path = FLASH / f"ccar-p-{priority}-api.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        notes.extend(payload["notes"])

    generated = sum(2 if n["note_type"] == "basic-reverse" else 1 for n in notes)
    if len(notes) != EXPECTED_LOGICAL:
        raise SystemExit(f"combined logical notes {len(notes)} != {EXPECTED_LOGICAL}")
    if generated != EXPECTED_CARDS:
        raise SystemExit(f"combined generated cards {generated} != {EXPECTED_CARDS}")

    api = {
        "deck_name": DECK_NAME,
        "priorities": list(PRIORITIES),
        "generated_cards": generated,
        "logical_notes": len(notes),
        "notes": notes,
    }
    (FLASH / "ccar-p-combined-api.json").write_text(
        json.dumps(api, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    records = [
        {"kind":"deck","format":"deez.nut","version":2,"name":DECK_NAME},
        *[
            {
                "kind":"note",
                "note_type": n["note_type"],
                "fields": n["fields"],
                "tags_json": n["tags_json"],
            }
            for n in notes
        ],
    ]
    (FLASH / "ccar-p-combined.nut").write_text(
        "\n".join(
            json.dumps(r, ensure_ascii=False, separators=(",", ":"))
            for r in records
        ) + "\n",
        encoding="utf-8",
    )

    BATCHES.mkdir(parents=True, exist_ok=True)
    for old in BATCHES.glob("combined-*.json"):
        old.unlink()
    for start in range(0, len(notes), BATCH_SIZE):
        number = start // BATCH_SIZE + 1
        payload = {"notes": notes[start:start + BATCH_SIZE]}
        (BATCHES / f"combined-{number:02d}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(f"Built combined deck: {len(notes)} logical notes -> {generated} cards")
    print(f"Combined batches: {(len(notes) + BATCH_SIZE - 1) // BATCH_SIZE}")

if __name__ == "__main__":
    main()
