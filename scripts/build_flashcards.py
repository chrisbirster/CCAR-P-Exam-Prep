#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLASH = ROOT / "flashcards"
SOURCE = FLASH / "source"
BATCHES = FLASH / "batches"
DOMAIN_ORDER = ["d1", "d2", "d3", "d4", "d5", "d6", "d7"]

def load_notes(priority: str) -> list[dict]:
    notes: list[dict] = []
    for domain in DOMAIN_ORDER:
        path = SOURCE / f"{priority}-{domain}.json"
        if not path.exists():
            raise SystemExit(f"missing source file: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        notes.extend(payload["notes"])
    return notes

def deez_note(note: dict) -> dict:
    return {
        "kind": "note",
        "note_type": note["note_type"],
        "fields": note["fields"],
        "tags_json": json.dumps(note["tags"], separators=(",", ":")),
    }

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--priority", default="p0")
    parser.add_argument("--deck-name")
    parser.add_argument("--batch-size", type=int, default=200)
    args = parser.parse_args()

    deck_name = deck_name or f"CCAR-P Exam Prep — {args.priority.upper()}"\n    notes = load_notes(args.priority)
    BATCHES.mkdir(parents=True, exist_ok=True)
    nut_path = FLASH / f"ccar-p-{args.priority}.nut"
    api_path = FLASH / f"ccar-p-{args.priority}-api.json"

    header = {"kind":"deck","format":"deez.nut","version":2,"name":deck_name}
    records = [header, *(deez_note(n) for n in notes)]
    nut_path.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in records) + "\n",
        encoding="utf-8",
    )

    generated_cards = sum(2 if n["note_type"] == "basic-reverse" else 1 for n in notes)
    api_payload = {
        "deck_name": deck_name,
        "priority": args.priority,
        "generated_cards": generated_cards,
        "logical_notes": len(notes),
        "notes": [
            {
                "note_type": n["note_type"],
                "fields": n["fields"],
                "tags_json": json.dumps(n["tags"], separators=(",", ":")),
            }
            for n in notes
        ],
    }
    api_path.write_text(json.dumps(api_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for old in BATCHES.glob(f"{args.priority}-*.json"):
        old.unlink()
    for start in range(0, len(notes), args.batch_size):
        batch = notes[start:start + args.batch_size]
        payload = {"notes": [
            {
                "note_type": n["note_type"],
                "fields": n["fields"],
                "tags_json": json.dumps(n["tags"], separators=(",", ":")),
            }
            for n in batch
        ]}
        number = start // args.batch_size + 1
        (BATCHES / f"{args.priority}-{number:02d}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(f"Built {len(notes)} logical notes")
    print(nut_path)
    print(api_path)

if __name__ == "__main__":
    main()
