# Advanced Tool Use on the Claude Developer Platform

**Publisher:** Anthropic  
**Published:** November 24, 2025  
**Verified:** September 26, 2026  
**Official source:** https://www.anthropic.com/engineering/advanced-tool-use

## Tool-definition context bloat

Anthropic describes tool libraries where definitions and results can consume very large portions of the context window before useful work begins.

**Supports:** D2.4, D3.8.

## On-demand tool discovery

Large tool catalogs can be discovered and loaded only when needed rather than preloaded into every request.

**Supports:** D3.8.

## Programmatic tool use

Some tool workflows can use code/programmatic processing to reduce repeated model-visible intermediate data.

**Supports:** D3.3, D4.5.

## Progressive discovery is not authorization

This is an architecture interpretation: hiding a tool from immediate context is an efficiency/selection mechanism, not a substitute for access control.

**Supports:** D3.2, D3.8.

## Time-sensitive note

Specific beta feature names and availability can change. Flashcards should prefer the durable concept—on-demand discovery and reduced context/tool-selection overhead—unless the current product detail is explicitly required.
