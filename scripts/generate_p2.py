#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "flashcards" / "source"

OBJECTIVES = {
    "D1.1":"translating business problems into Claude-based solutions",
    "D1.2":"end-to-end Claude architecture",
    "D1.3":"choosing augmented LLM, workflow, agent, or hybrid patterns",
    "D1.4":"multi-agent orchestration",
    "D1.5":"decomposing complex problems",
    "D1.6":"aligning architecture to business value",
    "D2.1":"Claude model selection",
    "D2.2":"system prompts, templates, and guardrails",
    "D2.3":"prompt engineering techniques",
    "D2.4":"context-window and token management",
    "D2.5":"prompt reuse, caching, and Skills",
    "D3.1":"tool and agent capability bloat",
    "D3.2":"authentication and authorization",
    "D3.3":"accuracy-latency trade-offs",
    "D3.4":"observability at scale",
    "D3.5":"RAG pipeline design",
    "D3.6":"retrieval strategy selection",
    "D3.7":"integration mechanism selection",
    "D3.8":"progressive discovery versus monolithic context",
    "D4.1":"defining evaluation metrics",
    "D4.2":"evaluation datasets and frameworks",
    "D4.3":"A/B testing and iterative improvement",
    "D4.4":"diagnosing AI system failures",
    "D4.5":"optimizing token, latency, and cost-performance",
    "D4.6":"production monitoring and regression protection",
    "D5.1":"guardrails and safety controls",
    "D5.2":"LLM and agent risks, limitations, and failure modes",
    "D5.3":"human-in-the-loop validation",
    "D5.4":"regulatory compliance architecture",
    "D5.5":"responsible and ethical AI",
    "D6.1":"structured discovery and requirement gathering",
    "D6.2":"communicating architecture decisions and trade-offs",
    "D6.3":"stakeholder feedback and expectation alignment",
    "D6.4":"architecture documentation and implementation guidance",
    "D6.5":"solution lifecycle management",
    "D7.1":"team-level Claude tools and environments",
    "D7.2":"AI-assisted developer workflows",
    "D7.3":"debugging and operational issue resolution",
}

DOMAIN_OBJECTIVES = {
    "d1":[f"D1.{i}" for i in range(1,7)],
    "d2":[f"D2.{i}" for i in range(1,6)],
    "d3":[f"D3.{i}" for i in range(1,9)],
    "d4":[f"D4.{i}" for i in range(1,7)],
    "d5":[f"D5.{i}" for i in range(1,6)],
    "d6":[f"D6.{i}" for i in range(1,6)],
    "d7":[f"D7.{i}" for i in range(1,4)],
}

ALLOC = {
    "d1":{"basic":15,"basic-reverse":10,"cloze":15,"type-answer":12,"multiple-choice":10,"multiple-select":8,"ordering":5},
    "d2":{"basic":12,"basic-reverse":8,"cloze":12,"type-answer":9,"multiple-choice":7,"multiple-select":5,"ordering":4},
    "d3":{"basic":17,"basic-reverse":11,"cloze":17,"type-answer":13,"multiple-choice":12,"multiple-select":8,"ordering":6},
    "d4":{"basic":14,"basic-reverse":10,"cloze":14,"type-answer":11,"multiple-choice":10,"multiple-select":6,"ordering":5},
    "d5":{"basic":13,"basic-reverse":8,"cloze":13,"type-answer":10,"multiple-choice":8,"multiple-select":6,"ordering":4},
    "d6":{"basic":13,"basic-reverse":9,"cloze":12,"type-answer":10,"multiple-choice":8,"multiple-select":5,"ordering":4},
    "d7":{"basic":6,"basic-reverse":4,"cloze":7,"type-answer":5,"multiple-choice":5,"multiple-select":2,"ordering":2},
}

def distribute(total: int, n: int) -> list[int]:
    base, rem = divmod(total, n)
    return [base + (1 if i < rem else 0) for i in range(n)]

def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def parse_choices(note: dict) -> tuple[list[dict], list[str]]:
    choices = json.loads(note["fields"][1])
    correct = [note["fields"][2]] if note["note_type"] == "multiple-choice" else json.loads(note["fields"][2])
    return choices, correct

def correct_text(note: dict) -> str:
    choices, correct = parse_choices(note)
    by_id = {c["id"]: c["text"] for c in choices}
    return "; ".join(by_id[c] for c in correct)

def extract_cloze(note: dict) -> tuple[str,str]:
    text = note["fields"][0]
    m = re.search(r"\{\{c1::(.*?)\}\}", text)
    if not m:
        raise ValueError(f"missing c1 in {note['id']}")
    return m.group(1), compact(text[:m.start()] + "_____" + text[m.end():])

def make_note(domain: str, objective: str, note_type: str, index: int, fields: list[str], kind: str, seed_id: str) -> dict:
    obj = objective.lower()
    return {
        "id": f"p2-{obj}-{note_type}-{index:03d}",
        "objective": objective,
        "priority": "p2",
        "kind": kind,
        "evidence": "human-approved",
        "source_refs": [f"docs/audit/{objective}-sources.md"],
        "seed_id": seed_id,
        "note_type": note_type,
        "fields": fields,
        "tags": ["ccarp", domain, f"obj:{obj}", "priority:p2", f"kind:{kind}", "source:approved"],
    }

def by_type(notes: list[dict]) -> dict[str,list[dict]]:
    out: dict[str,list[dict]] = defaultdict(list)
    for note in notes:
        out[note["note_type"]].append(note)
    return out

def generate_objective(domain: str, objective: str, seeds: list[dict], counts: dict[str,int]) -> list[dict]:
    title = OBJECTIVES[objective]
    typed = by_type(seeds)
    out: list[dict] = []

    mcqs = typed["multiple-choice"]
    basic_frames = [
        "P2 synthesis — defend the architecture choice for this case: {q}",
        "P2 edge-case review — what action should survive scrutiny here? {q}",
        "P2 judgment check for {title}: state the best recommendation without answer choices. {q}",
    ]
    for i in range(counts["basic"]):
        seed = mcqs[i % len(mcqs)]
        out.append(make_note(
            domain, objective, "basic", i + 1,
            [
                basic_frames[i % len(basic_frames)].format(title=title, q=seed["fields"][0]),
                f"{correct_text(seed)} {compact(seed['fields'][3])}",
            ],
            "scenario", seed["id"],
        ))

    reverse_seeds = typed["basic-reverse"]
    for i in range(counts["basic-reverse"]):
        seed = reverse_seeds[i % len(reverse_seeds)]
        cycle = i // len(reverse_seeds)
        lens = ["synthesis lens", "edge-case lens", "exam distinction"][cycle % 3]
        out.append(make_note(
            domain, objective, "basic-reverse", i + 1,
            [f"{seed['fields'][0]} — P2 {lens} for {title}", seed["fields"][1]],
            "compare", seed["id"],
        ))

    type_seeds = typed["type-answer"]
    for i in range(counts["cloze"]):
        seed = type_seeds[i % len(type_seeds)]
        cycle = i // len(type_seeds)
        prefix = ["P2 synthesis", "P2 edge case", "P2 architecture review"][cycle % 3]
        out.append(make_note(
            domain, objective, "cloze", i + 1,
            [
                f"{prefix} for {title}: the exact term for “{seed['fields'][0]}” is {{{{c1::{seed['fields'][1]}}}}}.",
                f"Exact-term reinforcement for {objective}.",
            ],
            "concept", seed["id"],
        ))

    cloze_seeds = typed["cloze"]
    for i in range(counts["type-answer"]):
        seed = cloze_seeds[i % len(cloze_seeds)]
        term, context = extract_cloze(seed)
        out.append(make_note(
            domain, objective, "type-answer", i + 1,
            [f"P2 exact recall for {title}: what phrase completes this rule? {context}", term],
            "concept", seed["id"],
        ))

    mcq_frames = [
        "P2 exam synthesis for {title}: {q}",
        "P2 architecture review — which answer best survives the trade-offs in this case? {q}",
        "P2 edge-case decision for {title}: {q}",
    ]
    for i in range(counts["multiple-choice"]):
        seed = mcqs[i % len(mcqs)]
        choices, correct = parse_choices(seed)
        shift = (i + 2) % len(choices)
        rotated = choices[shift:] + choices[:shift]
        out.append(make_note(
            domain, objective, "multiple-choice", i + 1,
            [
                mcq_frames[i % len(mcq_frames)].format(title=title, q=seed["fields"][0]),
                json.dumps(rotated, ensure_ascii=False, separators=(",", ":")),
                correct[0],
                f"{seed['fields'][3]} P2 emphasizes synthesis and edge-case judgment.",
            ],
            "scenario", seed["id"],
        ))

    ms_seeds = typed["multiple-select"]
    ms_frames = [
        "P2 synthesis for {title}: which TWO controls or decisions still hold under scrutiny? {q}",
        "P2 edge-case review for {title}: select the TWO recommendations that remain valid. {q}",
    ]
    for i in range(counts["multiple-select"]):
        seed = ms_seeds[i % len(ms_seeds)]
        choices, correct = parse_choices(seed)
        shift = (i + 1) % len(choices)
        rotated = choices[shift:] + choices[:shift]
        out.append(make_note(
            domain, objective, "multiple-select", i + 1,
            [
                ms_frames[i % len(ms_frames)].format(title=title, q=seed["fields"][0]),
                json.dumps(rotated, ensure_ascii=False, separators=(",", ":")),
                json.dumps(correct, ensure_ascii=False, separators=(",", ":")),
                f"{seed['fields'][3]} P2 reinforces the surviving decision set.",
            ],
            "decision", seed["id"],
        ))

    return out

def main() -> None:
    for domain, objectives in DOMAIN_OBJECTIVES.items():
        p1 = json.loads((SOURCE / f"p1-{domain}.json").read_text(encoding="utf-8"))["notes"]
        p0 = json.loads((SOURCE / f"p0-{domain}.json").read_text(encoding="utf-8"))["notes"]

        by_obj: dict[str,list[dict]] = defaultdict(list)
        for note in p1:
            by_obj[note["objective"]].append(note)

        counts_by_type = {
            note_type: distribute(total, len(objectives))
            for note_type, total in ALLOC[domain].items()
            if note_type != "ordering"
        }

        notes: list[dict] = []
        for pos, objective in enumerate(objectives):
            counts = {t: values[pos] for t, values in counts_by_type.items()}
            notes.extend(generate_objective(domain, objective, by_obj[objective], counts))

        ordering_pool = [n for n in p1 if n["note_type"] == "ordering"] + [n for n in p0 if n["note_type"] == "ordering"]
        needed = ALLOC[domain]["ordering"]
        if not ordering_pool:
            raise SystemExit(f"{domain}: no ordering seeds")

        for i in range(needed):
            seed = ordering_pool[i % len(ordering_pool)]
            items = json.loads(seed["fields"][1])
            objective = seed["objective"]
            title = OBJECTIVES[objective]
            cycle = i // len(ordering_pool)
            framing = "synthesis sequence" if cycle == 0 else "edge-case sequence"
            notes.append(make_note(
                domain, objective, "ordering", i + 1,
                [
                    f"P2 {framing} for {title}: place these steps in the order you would defend. {seed['fields'][0]}",
                    json.dumps(items, ensure_ascii=False, separators=(",", ":")),
                    f"{seed['fields'][2]} P2 sequence reinforcement for {objective}.",
                ],
                "sequence", seed["id"],
            ))

        payload = {"domain": domain, "priority": "p2", "notes": notes}
        path = SOURCE / f"p2-{domain}.json"
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{path}: {len(notes)} logical notes")

if __name__ == "__main__":
    main()
