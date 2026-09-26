# Building Effective AI Agents

**Publisher:** Anthropic  
**Published:** December 19, 2024  
**Verified:** September 26, 2026  
**Official source:** https://www.anthropic.com/engineering/building-effective-agents

> Anthropic notes that parts of the tooling landscape in this older article have changed. We use it primarily for durable architecture patterns, not current product limits.

## Simple, composable architecture

Anthropic reports that successful implementations commonly use simple, composable patterns rather than unnecessarily complex frameworks.

**Supports:** D1.1, D1.3, D1.5, D1.6.

## Workflows vs. agents

The article distinguishes:

- **workflows** — LLMs and tools orchestrated through predefined code paths;
- **agents** — LLMs dynamically directing their own process and tool use.

This distinction is central to architecture-pattern selection.

**Supports:** D1.3.

## Prompt chaining

A task can be split into a fixed sequence where each model call processes the previous output. Intermediate gates can validate progress.

**Supports:** D1.5.

## Routing

An input can be classified and sent to a specialized downstream path.

**Supports:** D1.5.

## Parallelization

Independent subtasks can execute concurrently and their results can later be aggregated.

**Supports:** D1.5, D1.4.

## Orchestrator-workers

A central LLM can dynamically decompose a task, delegate subtasks, and synthesize worker results.

**Supports:** D1.4, D1.5.

## Evaluator-optimizer

One model call can generate while another evaluates against criteria and requests refinement.

**Supports:** D1.5, D4.2.

## Complexity trade-off

The durable takeaway is to add autonomy and orchestration complexity when it creates measurable value rather than treating "agentic" as an automatic upgrade.

**Supports:** D1.1, D1.3, D1.6.
