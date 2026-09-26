# Effective Context Engineering for AI Agents

**Publisher:** Anthropic  
**Published:** September 29, 2025  
**Verified:** September 26, 2026  
**Official source:** https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## Context is finite

Anthropic describes context as a finite resource and frames context engineering as selecting the smallest useful set of high-signal tokens for the current inference.

**Supports:** D2.4.

## Prompt engineering vs. context engineering

Prompt engineering focuses on instructions. Context engineering also considers tools, MCP, external data, message history, and other information visible to the model.

**Supports:** D2.2, D2.4.

## Just-in-time context

Rather than preloading all potentially relevant data, agents can keep lightweight references and load data only when needed.

**Supports:** D2.4, D3.8.

## Compaction

Long-running traces can be summarized into a smaller context while preserving critical facts and decisions.

**Supports:** D2.4.

## Structured note-taking / external memory

Agents can persist structured notes outside the context window and reload them later.

**Supports:** D1.2, D2.4.

## Context isolation

Separate subagents can isolate independent contexts and reduce interference between unrelated subtasks.

**Supports:** D1.4, D2.4.

## Larger windows do not eliminate relevance problems

The source explicitly warns that larger context windows still face context-pollution and relevance concerns.

**Supports:** D2.4, D3.8.
