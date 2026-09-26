# How We Contain Claude Across Products

**Publisher:** Anthropic  
**Verified:** September 26, 2026  
**Official source:** https://www.anthropic.com/engineering/how-we-contain-claude

## Environment boundaries

Anthropic describes hard environmental boundaries such as process sandboxes, VMs, filesystem restrictions, and network/egress controls as a way to constrain what an agent can reach.

**Supports:** D3.1, D5.1, D7.1.

## Credentials and blast radius

A key security principle in the source is that credentials or resources an agent cannot reach cannot be exfiltrated or misused by that agent.

**Supports:** D3.1, D3.2, D5.1.

## Model controls are probabilistic

Anthropic distinguishes model-layer controls such as prompts/classifiers from hard environmental boundaries and notes that probabilistic model controls cannot provide absolute enforcement alone.

**Supports:** D2.2, D5.1.

## External content and tools

External sources such as MCP servers, connectors, files, and web content can introduce both code/supply-chain risk and prompt-injection risk.

**Supports:** D3.1, D5.2.

## Granular permissions

Anthropic explicitly notes that limiting tool permissions reduces blast radius; for example, read-only access is safer than write access to production systems.

**Supports:** D3.1, D3.2.

## Durable takeaway

Agent security should combine:

- constrained environment;
- appropriately scoped tools and permissions;
- model-layer safeguards;
- careful handling of untrusted external content.

The exact product mechanisms can change, but the defense-in-depth principle is durable.
