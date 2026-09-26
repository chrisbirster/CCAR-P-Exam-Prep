# Claude Model Lifecycle and Deprecations

**Publisher:** Anthropic / Claude Platform Docs  
**Verified:** September 26, 2026  
**Official source:** https://docs.anthropic.com/en/docs/about-claude/model-deprecations

## Lifecycle states

Anthropic currently documents four lifecycle labels:

1. **Active** — fully supported and recommended.
2. **Legacy** — no longer receives updates and may be deprecated later.
3. **Deprecated** — still functional but no longer recommended; a replacement and retirement date are provided.
4. **Retired** — no longer available; requests fail.

**Supports:** D2.1.

## Migration testing

Anthropic recommends testing applications with replacement models before retirement.

**Supports:** D2.1, D4.6.

## Architecture implication

Do not encode model names as if they are permanent architecture primitives. Maintain an evaluation/migration path.

**Supports:** D2.1 as Level C interpretation.

## Time-sensitive note

Specific active models, retirement dates, and replacement recommendations change. Use the official page for current values.
