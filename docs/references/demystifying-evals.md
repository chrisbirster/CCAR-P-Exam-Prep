# Demystifying Evals for AI Agents

**Publisher:** Anthropic  
**Published:** January 9, 2026  
**Verified:** September 26, 2026  
**Official source:** https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

## Why agent evaluation is different

Agents operate over many turns, call tools, modify state, and adapt to intermediate results. Evaluating only one final answer can therefore miss important failures.

**Supports:** D4.1, D4.2.

## Tasks and trials

A task defines what the agent must accomplish. Repeated trials help account for stochastic behavior.

**Supports:** D4.2.

## Graders

Evaluation can use deterministic checks, model-based grading, and human judgment depending on the property being measured.

**Supports:** D4.1, D4.2.

## Trajectories / transcripts

The sequence of model and tool interactions can reveal failure modes that the final answer alone hides.

**Supports:** D3.4, D4.2, D4.4.

## Outcomes

External state can be a more authoritative success measure than what the model claims it did.

**Supports:** D4.1, D4.2, D4.4.

## Regression evaluation

Known capabilities should remain protected as the system changes.

**Supports:** D2.1, D4.4, D4.6.

## Production lifecycle

Evaluation should become part of an iterative development and monitoring process rather than a one-time prelaunch exercise.

**Supports:** D4.3, D4.6, D6.3, D6.5.
