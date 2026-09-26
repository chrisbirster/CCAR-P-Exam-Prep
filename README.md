# CCAR-P Exam Prep

**Study site:** https://chrisbirster.github.io/CCAR-P-Exam-Prep/


Community study material for the **Claude Certified Architect – Professional (CCAR-P)** exam.

This repository is designed to help students move from “I know Claude” to **“I can make and defend production architecture decisions involving Claude.”**

> [!IMPORTANT]
> This is an independent study resource. It is **not affiliated with, endorsed by, or sponsored by Anthropic**.  
> Always use Anthropic's current exam guide as the authoritative source for exam scope, policies, eligibility, and registration.

## Start Here

1. Read the [CCAR-P Exam Objectives](docs/exam-objectives.md).
2. Study the [Concept Notes](docs/concepts/README.md) for all 38 objectives.
3. Use the [2,000-card Flashcard Plan](docs/flashcard-plan.md).
4. Use the checklist to mark weak areas.
5. Study by **exam weight**, not by personal preference.
6. Practice scenario questions that force architecture trade-offs.
7. Re-check Anthropic's official guide before sitting the exam.

## Exam Blueprint

| Domain | Weight | Objectives |
|---|---:|---:|
| 1. Solution Design & Architecture | 17% | 6 |
| 2. Claude Models, Prompting & Context Engineering | 13% | 5 |
| 3. Integration | 19% | 8 |
| 4. Evaluation, Testing & Optimization | 16% | 6 |
| 5. Governance, Safety & Risk Management | 14% | 5 |
| 6. Stakeholder Communication & Lifecycle Management | 14% | 5 |
| 7. Developer Productivity & Operational Enablement | 7% | 3 |
| **Total** | **100%** | **38** |

**Integration is the largest domain at 19%.** Solution Design & Architecture and Evaluation, Testing & Optimization are also heavily represented. The Professional exam rewards architectural judgment across all seven areas, so no domain should be treated as optional.

## What This Exam Is Really Testing

CCAR-P is not primarily a product-trivia exam.

For a given scenario, you should be able to reason through:

```text
business outcome
    ↓
constraints
    ↓
architecture pattern
    ↓
model + context
    ↓
integrations + permissions
    ↓
safety controls
    ↓
evaluation
    ↓
operations + observability
    ↓
ownership + business value
```

A useful question to ask throughout your preparation is:

> What is the simplest architecture that satisfies the stated quality, safety, security, compliance, latency, reliability, and cost constraints?

## Recommended Study Order

The numbered domain order is not necessarily the best learning order.

A practical sequence is:

1. **Solution Design & Architecture** — establish the decision framework.
2. **Integration** — connect Claude to real enterprise systems safely.
3. **Evaluation, Testing & Optimization** — prove the design works.
4. **Models, Prompting & Context Engineering** — optimize the Claude-specific layers.
5. **Governance, Safety & Risk** — apply enforceable controls.
6. **Stakeholder Communication & Lifecycle** — make the architecture sustainable.
7. **Developer Productivity & Operational Enablement** — help teams operate it without you.

## How We Will Use This Repository

Planned study materials:

```text
docs/
  exam-objectives.md       ← master CCAR-P checklist

flashcards/
  ...                      ← Deez study decks

practice/
  ...                      ← original scenario exercises

labs/
  ...                      ← hands-on architecture exercises
```

The goal is to build study material around the **published blueprint**, not reproduce confidential or live exam questions.

## Study Philosophy

### Learn decisions, not definitions

Instead of only memorizing:

> MCP is a protocol for connecting AI applications to tools and data.

Be ready to answer:

> Why would an architect choose MCP over a direct API integration in this scenario, and what new security or operational boundary does that choice introduce?

### Separate probabilistic and deterministic responsibilities

Claude is useful for language understanding, synthesis, classification, reasoning, planning, and generation.

Deterministic software should normally enforce things such as:

- authorization;
- hard business rules;
- schema validation;
- numeric thresholds;
- access controls;
- irreversible side-effect approval.

### Evaluate before optimizing

Before changing a model, prompt, retrieval strategy, agent design, or tool configuration, define:

```text
dataset + metric + acceptance threshold + rollback condition
```

## Official Resources

Use these first whenever there is a disagreement between a community resource and Anthropic:

- **Anthropic Partner Academy — Claude Certified Architect – Professional Prep Course**
- **Anthropic Partner Academy — Certification FAQ**
- **Anthropic Partner Academy — Partner Certifications**
- **Anthropic documentation**
- **Model Context Protocol specification**

Certification is currently offered through the Claude Partner Network. Check Anthropic's current eligibility requirements before planning an exam date.

## Contributions

Contributions that improve clarity, fix inaccuracies, add original labs, or create better explanations are welcome.

Please **do not submit memorized, copied, reconstructed, or confidential live exam questions**. Practice content should be original and designed to exercise the published objectives.

## Accuracy

The CCAR-P program can change. Material in this repository should include a “last verified” date where appropriate.

The master objectives document is currently based on **CCAR-P v1.0, effective July 2026**, and was last reviewed on **September 26, 2026**.


## Website Build

The public site is generated as static HTML and deployed with GitHub Pages.

The build intentionally stays small:

- `zig build` is the single build entrypoint.
- `scripts/build.py` is a dependency-free Markdown-to-HTML generator using only Python's standard library.
- `content/home.md` and `docs/exam-objectives.md` are the content sources.
- `site/style.css` provides the minimal responsive light/dark styling.
- output is written to `dist/`.
- GitHub Actions deploys `dist/` to GitHub Pages on every push to `main`.

To build locally:

```bash
zig build
python3 -m http.server 8000 --directory dist
```

Then open `http://localhost:8000`.

The static-site approach and restrained developer-site aesthetic were inspired by Andrew Kelley's public website repository, while the generator, templates, and styling in this repository are original.
