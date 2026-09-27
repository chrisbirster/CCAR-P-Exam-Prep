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

ALLOC = {
    "d1":{"basic":23,"basic-reverse":16,"cloze":22,"type-answer":15,"multiple-choice":22,"multiple-select":17,"ordering":5},
    "d2":{"basic":19,"basic-reverse":12,"cloze":17,"type-answer":12,"multiple-choice":16,"multiple-select":13,"ordering":3},
    "d3":{"basic":27,"basic-reverse":18,"cloze":24,"type-answer":17,"multiple-choice":24,"multiple-select":19,"ordering":5},
    "d4":{"basic":23,"basic-reverse":14,"cloze":21,"type-answer":15,"multiple-choice":21,"multiple-select":16,"ordering":4},
    "d5":{"basic":20,"basic-reverse":12,"cloze":19,"type-answer":12,"multiple-choice":18,"multiple-select":14,"ordering":5},
    "d6":{"basic":19,"basic-reverse":12,"cloze":18,"type-answer":13,"multiple-choice":19,"multiple-select":14,"ordering":5},
    "d7":{"basic":9,"basic-reverse":6,"cloze":9,"type-answer":6,"multiple-choice":10,"multiple-select":7,"ordering":3},
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

def distribute(total: int, n: int) -> list[int]:
    base, rem = divmod(total, n)
    return [base + (1 if i < rem else 0) for i in range(n)]

def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def parse_choices(note: dict) -> tuple[list[dict], list[str]]:
    choices = json.loads(note["fields"][1])
    if note["note_type"] == "multiple-choice":
        correct = [note["fields"][2]]
    else:
        correct = json.loads(note["fields"][2])
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
    term = m.group(1)
    context = text[:m.start()] + "_____" + text[m.end():]
    return term, compact(context)

def make_note(domain: str, objective: str, note_type: str, index: int, fields: list[str], kind: str, seed_id: str) -> dict:
    obj = objective.lower()
    return {
        "id": f"p1-{obj}-{note_type}-{index:03d}",
        "objective": objective,
        "priority": "p1",
        "kind": kind,
        "evidence": "human-approved",
        "source_refs": [f"docs/audit/{objective}-sources.md"],
        "seed_id": seed_id,
        "note_type": note_type,
        "fields": fields,
        "tags": ["ccarp", domain, f"obj:{obj}", "priority:p1", f"kind:{kind}", "source:approved"],
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

    # Applied recall: remove answer choices from approved scenarios.
    mcqs = typed["multiple-choice"]
    basic_templates = [
        "Without answer choices, what is the best architecture response to this scenario? {q}",
        "Resolve this production scenario for {title}: {q}",
        "What should an architect recommend in this {title} situation? {q}",
        "State the preferred architecture action for this design-review scenario: {q}",
    ]
    for i in range(counts["basic"]):
        seed = mcqs[i % len(mcqs)]
        answer = correct_text(seed)
        explanation = compact(seed["fields"][3])
        out.append(make_note(
            domain, objective, "basic", i + 1,
            [basic_templates[i % len(basic_templates)].format(title=title, q=seed["fields"][0]),
             f"{answer} {explanation}"],
            "scenario", seed["id"],
        ))

    # Bidirectional reinforcement: approved term/definition plus cloze terms.
    reverse_pool: list[tuple[str,str,str,str]] = []
    for seed in typed["basic-reverse"]:
        reverse_pool.append((seed["fields"][0], seed["fields"][1], seed["id"], "definition"))
    for seed in typed["cloze"]:
        term, context = extract_cloze(seed)
        reverse_pool.append((term, f"Phrase that completes this {title} rule: {context}", seed["id"], "rule application"))
    seen_terms: set[str] = set()
    for i in range(counts["basic-reverse"]):
        term, definition, seed_id, lens = reverse_pool[i % len(reverse_pool)]
        cycle = i // len(reverse_pool)
        term_key = term.casefold()
        if cycle == 0 and term_key in seen_terms:
            label = f"{term} — {lens} in {title}"
        elif cycle == 0:
            label = f"{term} — {objective} application"
        elif cycle % 2 == 1:
            label = f"{term} — operational use in {title}"
        else:
            label = f"{term} — design-review use in {title}"
        seen_terms.add(term_key)
        out.append(make_note(
            domain, objective, "basic-reverse", i + 1,
            [label, definition],
            "compare", seed_id,
        ))

    # Cloze: term-in-context from reverse pairs and exact-answer seeds.
    cloze_pool: list[tuple[str,str,str]] = []
    for seed in typed["basic-reverse"]:
        cloze_pool.append((
            seed["fields"][0],
            f"In {title}, {{term}} is the concept described as: {seed['fields'][1]}",
            seed["id"],
        ))
    for seed in typed["type-answer"]:
        cloze_pool.append((
            seed["fields"][1],
            f"For {title}, the precise answer to “{seed['fields'][0]}” is {{term}}.",
            seed["id"],
        ))
    for i in range(counts["cloze"]):
        term, template, seed_id = cloze_pool[i % len(cloze_pool)]
        cycle = i // len(cloze_pool)
        sentence = template.replace("{term}", f"{{{{c1::{term}}}}}")
        if cycle % 3 == 1:
            sentence = f"During an operational review, apply this {title} rule: {sentence}"
        elif cycle % 3 == 2:
            sentence = f"In a design-review context for {title}: {sentence}"
        out.append(make_note(
            domain, objective, "cloze", i + 1,
            [sentence, f"Applied reinforcement for {objective}."],
            "concept", seed_id,
        ))

    # Exact-term recall from definitions and cloze rules.
    type_pool: list[tuple[str,str,str]] = []
    for seed in typed["basic-reverse"]:
        type_pool.append((
            f"Within {title}, what term matches this definition: {seed['fields'][1]}",
            seed["fields"][0],
            seed["id"],
        ))
    for seed in typed["cloze"]:
        term, context = extract_cloze(seed)
        type_pool.append((
            f"What phrase completes this approved {title} rule? {context}",
            term,
            seed["id"],
        ))
    for i in range(counts["type-answer"]):
        prompt, answer, seed_id = type_pool[i % len(type_pool)]
        out.append(make_note(
            domain, objective, "type-answer", i + 1,
            [prompt, answer],
            "concept", seed_id,
        ))

    # Re-framed single-best-answer scenarios.
    mcq_templates = [
        "A design reviewer is evaluating this scenario: {q} Which recommendation should they defend?",
        "Apply the approved {title} guidance to this case: {q}",
        "Which response best preserves the architecture principles in this situation? {q}",
    ]
    for i in range(counts["multiple-choice"]):
        seed = mcqs[i % len(mcqs)]
        choices, correct = parse_choices(seed)
        shift = (i + 1) % len(choices)
        rotated = choices[shift:] + choices[:shift]
        out.append(make_note(
            domain, objective, "multiple-choice", i + 1,
            [
                mcq_templates[i % len(mcq_templates)].format(title=title, q=seed["fields"][0]),
                json.dumps(rotated, separators=(",", ":")),
                correct[0],
                f"{seed['fields'][3]} This P1 variant tests the same approved principle in a re-framed design review.",
            ],
            "scenario", seed["id"],
        ))

    # Decision reinforcement from approved good/bad option sets.
    ms_seeds = typed["multiple-select"]
    ms_templates = [
        "During a {title} review, which TWO statements remain aligned with the approved guidance? {q}",
        "Which TWO recommendations should survive an architecture review focused on {title}? Context: {q}",
        "For {title}, select the TWO options that preserve the approved design principles. {q}",
    ]
    for i in range(counts["multiple-select"]):
        seed = ms_seeds[i % len(ms_seeds)]
        choices, correct = parse_choices(seed)
        shift = (i + 2) % len(choices)
        rotated = choices[shift:] + choices[:shift]
        out.append(make_note(
            domain, objective, "multiple-select", i + 1,
            [
                ms_templates[i % len(ms_templates)].format(title=title, q=seed["fields"][0]),
                json.dumps(rotated, separators=(",", ":")),
                json.dumps(correct, separators=(",", ":")),
                f"{seed['fields'][3]} This variant reinforces the approved decision set for {objective}.",
            ],
            "decision", seed["id"],
        ))

    return out

def main() -> None:
    for domain, objectives in DOMAIN_OBJECTIVES.items():
        p0_path = SOURCE / f"p0-{domain}.json"
        p0 = json.loads(p0_path.read_text(encoding="utf-8"))["notes"]
        by_obj: dict[str,list[dict]] = defaultdict(list)
        for note in p0:
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

        ordering = [n for n in p0 if n["note_type"] == "ordering"]
        needed = ALLOC[domain]["ordering"]
        if len(ordering) < needed:
            raise SystemExit(f"{domain}: only {len(ordering)} P0 ordering seeds for {needed} P1 notes")
        for i, seed in enumerate(ordering[:needed], 1):
            items = json.loads(seed["fields"][1])
            notes.append(make_note(
                domain, seed["objective"], "ordering", i,
                [
                    f"Put these steps in the operational order you would defend during a P1 design review: {seed['fields'][0]}",
                    json.dumps(items, separators=(",", ":")),
                    f"{seed['fields'][2]} Sequence reinforcement for {seed['objective']}.",
                ],
                "sequence", seed["id"],
            ))

        output = {"domain":domain,"priority":"p1","notes":notes}
        path = SOURCE / f"p1-{domain}.json"
        path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{path}: {len(notes)} logical notes")

if __name__ == "__main__":
    main()
