# How Anthropic Built Its Multi-Agent Research System

**Publisher:** Anthropic  
**Published:** June 13, 2025  
**Verified:** September 26, 2026  
**Official source:** https://www.anthropic.com/engineering/multi-agent-research-system

## Orchestrator-worker architecture

Anthropic describes a lead research agent that plans work and delegates specialized subtasks to parallel subagents.

**Supports:** D1.4.

## Parallelism

Subagents explore independent directions simultaneously, which is useful for breadth-oriented tasks with separable workstreams.

**Supports:** D1.4, D1.5.

## Separation of concerns

Subagents can have distinct tools, prompts, and exploration trajectories.

**Supports:** D1.4, D2.4.

## Coordination cost

The article documents coordination failures and operational complexity that arise in multi-agent systems.

**Supports:** D1.4, D3.4, D4.4.

## Observability and evaluation

Anthropic emphasizes watching agent trajectories and building tests/evaluations around the full multi-agent system.

**Supports:** D3.4, D4.2, D4.6.

## Durable takeaway

Multi-agent systems are especially useful when independent work can genuinely run in parallel or benefit from context separation. They also introduce coordination and reliability costs that must be engineered.
