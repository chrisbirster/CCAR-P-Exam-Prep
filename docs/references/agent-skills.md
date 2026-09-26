# Agent Skills

**Publisher:** Anthropic  
**Published:** October 16, 2025  
**Verified:** September 26, 2026  
**Official source:** https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

## Skills package reusable expertise

Anthropic describes Skills as folders containing instructions, scripts, and resources that equip agents with specialized procedural knowledge.

**Supports:** D2.5, D7.1.

## Progressive disclosure

Skill metadata can be loaded first, then full instructions/resources loaded only when the Skill is relevant.

**Supports:** D2.4, D2.5, D3.8.

## Composability and portability

Skills are intended to package reusable capabilities rather than rebuild bespoke agents for each use case.

**Supports:** D2.5, D7.1.

## Governance interpretation

Our recommendation to review, version, and control shared Skills is an operational/security interpretation built on the fact that Skills can include instructions, code, and external-resource behavior.

**Supports:** D2.5, D5.2, D7.1.
