#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "flashcards" / "source"

PROFILES = {
    "p0": {
        "domain_cards": {"d1":119,"d2":91,"d3":133,"d4":112,"d5":98,"d6":98,"d7":49},
        "type_notes": {
            "basic":90,"basic-reverse":70,"cloze":80,"type-answer":60,
            "multiple-choice":150,"multiple-select":140,"ordering":40,
        },
        "logical_notes": 630,
        "generated_cards": 700,
    },
    "p1": {
        "domain_cards": {"d1":136,"d2":104,"d3":152,"d4":128,"d5":112,"d6":112,"d7":56},
        "type_notes": {
            "basic":140,"basic-reverse":90,"cloze":130,"type-answer":90,
            "multiple-choice":130,"multiple-select":100,"ordering":30,
        },
        "logical_notes": 710,
        "generated_cards": 800,
    },
    "p2": {
        "domain_cards": {"d1":85,"d2":65,"d3":95,"d4":80,"d5":70,"d6":70,"d7":35},
        "type_notes": {
            "basic":90,"basic-reverse":60,"cloze":90,"type-answer":70,
            "multiple-choice":60,"multiple-select":40,"ordering":30,
        },
        "logical_notes": 440,
        "generated_cards": 500,
    },
}

FIELD_COUNTS = {
    "basic":2,"basic-reverse":2,"cloze":2,"type-answer":2,
    "multiple-choice":4,"multiple-select":4,"ordering":3,
}
CARD_MULTIPLIER = {
    "basic":1,"basic-reverse":2,"cloze":1,"type-answer":1,
    "multiple-choice":1,"multiple-select":1,"ordering":1,
}
KINDS = {"concept","compare","decision","scenario","failure-mode","security","evaluation","sequence"}

def fail(errors: list[str], message: str) -> None:
    errors.append(message)

def parse_json_field(value: str, label: str, errors: list[str], note_id: str):
    try:
        return json.loads(value)
    except Exception as exc:
        fail(errors, f"{note_id}: invalid JSON in {label}: {exc}")
        return None

def normalized_prompt(note: dict) -> str:
    if not note.get("fields"):
        return ""
    text = re.sub(r"\{\{c\d+::(.*?)\}\}", r"\1", note["fields"][0])
    return re.sub(r"\W+", " ", text.lower()).strip()

def validate_note(note: dict, priority: str, errors: list[str]) -> int:
    note_id = note.get("id", "<missing-id>")
    required = {"id","objective","priority","kind","evidence","source_refs","note_type","fields","tags"}
    missing = required - note.keys()
    if missing:
        fail(errors, f"{note_id}: missing keys {sorted(missing)}")
        return 0

    nt = note["note_type"]
    if nt not in FIELD_COUNTS:
        fail(errors, f"{note_id}: unsupported note_type {nt}")
        return 0
    if len(note["fields"]) != FIELD_COUNTS[nt]:
        fail(errors, f"{note_id}: {nt} requires {FIELD_COUNTS[nt]} fields")

    obj = note["objective"].lower()
    domain = obj.split(".", 1)[0]
    tags = note["tags"]
    required_tags = {
        "ccarp",domain,f"obj:{obj}",f"priority:{priority}",
        f"kind:{note['kind']}","source:approved",
    }
    missing_tags = required_tags - set(tags)
    if missing_tags:
        fail(errors, f"{note_id}: missing tags {sorted(missing_tags)}")
    if note["kind"] not in KINDS:
        fail(errors, f"{note_id}: unknown kind {note['kind']}")
    if note["priority"] != priority:
        fail(errors, f"{note_id}: {priority} source contains priority={note['priority']}")
    if note["evidence"] != "human-approved":
        fail(errors, f"{note_id}: evidence must be human-approved")
    if not note["source_refs"]:
        fail(errors, f"{note_id}: source_refs empty")

    if nt == "cloze":
        ordinals = set(re.findall(r"\{\{c(\d+)::.+?\}\}", note["fields"][0]))
        if ordinals != {"1"}:
            fail(errors, f"{note_id}: {priority} cloze must contain exactly c1")

    if nt in {"multiple-choice","multiple-select"}:
        choices = parse_json_field(note["fields"][1], "Choices", errors, note_id)
        if isinstance(choices, list):
            ids = [x.get("id") for x in choices if isinstance(x, dict)]
            if len(ids) != len(choices) or len(ids) != len(set(ids)) or any(not x for x in ids):
                fail(errors, f"{note_id}: choice IDs must be present and unique")
            if len(choices) < 3:
                fail(errors, f"{note_id}: choice question needs at least 3 options")
            valid = set(ids)
            if nt == "multiple-choice":
                if note["fields"][2] not in valid:
                    fail(errors, f"{note_id}: correct MCQ ID not in choices")
            else:
                correct = parse_json_field(note["fields"][2], "Correct", errors, note_id)
                if not isinstance(correct, list) or not correct:
                    fail(errors, f"{note_id}: multiple-select Correct must be a non-empty array")
                elif len(correct) != len(set(correct)) or not set(correct).issubset(valid):
                    fail(errors, f"{note_id}: invalid multiple-select correct IDs")

    if nt == "ordering":
        items = parse_json_field(note["fields"][1], "Items", errors, note_id)
        if isinstance(items, list):
            ids = [x.get("id") for x in items if isinstance(x, dict)]
            if len(items) < 3:
                fail(errors, f"{note_id}: ordering needs at least 3 items")
            if len(ids) != len(items) or len(ids) != len(set(ids)) or any(not x for x in ids):
                fail(errors, f"{note_id}: ordering IDs must be present and unique")
    return CARD_MULTIPLIER[nt]

def load_priority(priority: str, errors: list[str]) -> list[dict]:
    notes: list[dict] = []
    for domain in PROFILES[priority]["domain_cards"]:
        path = SOURCE / f"{priority}-{domain}.json"
        if not path.exists():
            fail(errors, f"missing {path}")
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        notes.extend(payload.get("notes", []))
    return notes

def audit_priority(priority: str) -> list[str]:
    profile = PROFILES[priority]
    errors: list[str] = []
    all_notes: list[dict] = []
    per_domain_cards: dict[str,int] = {}

    for domain, expected_cards in profile["domain_cards"].items():
        path = SOURCE / f"{priority}-{domain}.json"
        if not path.exists():
            fail(errors, f"missing {path}")
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        notes = payload.get("notes", [])
        all_notes.extend(notes)
        cards = sum(validate_note(n, priority, errors) for n in notes)
        per_domain_cards[domain] = cards
        if cards != expected_cards:
            fail(errors, f"{domain}: generated cards {cards}, expected {expected_cards}")

    ids = [n.get("id") for n in all_notes]
    for duplicate, count in Counter(ids).items():
        if duplicate and count > 1:
            fail(errors, f"duplicate note id: {duplicate}")

    prompts = [normalized_prompt(n) for n in all_notes]
    for duplicate, count in Counter(prompts).items():
        if duplicate and count > 1:
            fail(errors, f"duplicate normalized prompt ({count}x): {duplicate[:120]}")

    type_counts = Counter(n.get("note_type") for n in all_notes)
    if dict(type_counts) != profile["type_notes"]:
        fail(errors, f"note type counts {dict(type_counts)} != {profile['type_notes']}")

    generated = sum(CARD_MULTIPLIER[n["note_type"]] for n in all_notes)
    if len(all_notes) != profile["logical_notes"]:
        fail(errors, f"logical notes {len(all_notes)}, expected {profile['logical_notes']}")
    if generated != profile["generated_cards"]:
        fail(errors, f"generated cards {generated}, expected {profile['generated_cards']}")

    objectives = {n["objective"] for n in all_notes}
    expected_objectives = {
        *(f"D1.{i}" for i in range(1,7)), *(f"D2.{i}" for i in range(1,6)),
        *(f"D3.{i}" for i in range(1,9)), *(f"D4.{i}" for i in range(1,7)),
        *(f"D5.{i}" for i in range(1,6)), *(f"D6.{i}" for i in range(1,6)),
        *(f"D7.{i}" for i in range(1,4)),
    }
    if objectives != expected_objectives:
        fail(errors, f"objective coverage mismatch; missing={sorted(expected_objectives-objectives)} extra={sorted(objectives-expected_objectives)}")

    if not errors:
        print(f"{priority.upper()} audit passed: {len(all_notes)} logical notes -> {generated} generated cards")
        print("Domain generated-card counts:", per_domain_cards)
        print("Logical note-type counts:", dict(type_counts))
    return errors

def audit_cross_priority(priorities: list[str]) -> list[str]:
    errors: list[str] = []
    seen_ids: dict[str,str] = {}
    seen_prompts: dict[str,str] = {}
    for priority in priorities:
        notes = load_priority(priority, errors)
        for note in notes:
            note_id = note.get("id", "")
            if note_id in seen_ids:
                fail(errors, f"cross-priority duplicate note id: {note_id}")
            seen_ids[note_id] = priority
            prompt = normalized_prompt(note)
            if prompt in seen_prompts:
                fail(errors, f"cross-priority duplicate prompt: {prompt[:120]} ({seen_prompts[prompt]} / {priority})")
            seen_prompts[prompt] = priority
    if not errors:
        print(f"Cross-priority audit passed for {', '.join(priorities)}")
    return errors

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--priority", choices=sorted(PROFILES), action="append")
    parser.add_argument("--cross-priority", action="store_true")
    args = parser.parse_args()

    priorities = args.priority or ["p0"]
    errors: list[str] = []
    for priority in priorities:
        errors.extend(audit_priority(priority))
    if args.cross_priority and len(priorities) > 1:
        errors.extend(audit_cross_priority(priorities))

    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        raise SystemExit(1)

if __name__ == "__main__":
    main()
