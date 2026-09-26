# Writing Effective Tools for AI Agents

**Publisher:** Anthropic  
**Published:** September 11, 2025  
**Verified:** September 26, 2026  
**Official source:** https://www.anthropic.com/engineering/writing-tools-for-agents

## Choose the right tools

Anthropic warns that more tools do not always improve outcomes and that tools should be intentionally selected for agent use.

**Supports:** D3.1.

## Avoid overlapping capability

Too many overlapping tools can confuse tool selection and increase mistakes.

**Supports:** D3.1, D3.8.

## Clear tool boundaries and namespacing

Tools should have distinct purposes and clear names/boundaries.

**Supports:** D3.1, D7.1.

## Return high-signal context

Tool responses should return useful information without wasting the model's limited context on irrelevant data.

**Supports:** D2.4, D3.1, D4.5.

## Tool specifications are part of the interface

Descriptions and schemas influence how reliably an agent chooses and invokes tools.

**Supports:** D3.1, D4.4.

## Evaluate tools with agents

Anthropic recommends evaluation-driven iteration on tool design.

**Supports:** D4.2, D4.4.
