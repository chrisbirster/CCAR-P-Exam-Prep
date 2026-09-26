# Model Context Protocol Specification

**Publisher:** Model Context Protocol  
**Verified:** September 26, 2026  
**Official specification:** https://modelcontextprotocol.io/specification/

## What MCP provides

MCP defines a standard protocol for AI applications/clients to interact with servers that expose capabilities such as tools and resources.

**Supports:** D3.7.

## Capability discovery

MCP standardizes discovery and invocation of server capabilities.

**Supports:** D3.7, D3.8.

## Authorization

Current MCP authorization guidance uses explicit authorization mechanisms rather than treating the model prompt as access control.

**Supports:** D3.2, D3.7.

## Security boundary

MCP standardizes communication; it does not make every exposed capability safe by itself. Servers and applications still need appropriate authentication, authorization, validation, and least privilege.

**Supports:** D3.1, D3.2, D3.7 as partly protocol fact and partly architecture interpretation.

## Versioning warning

MCP is independently versioned and evolves quickly. Flashcards should prefer durable protocol concepts unless the exact current protocol revision is part of the learning objective.

## Companion documentation

MCP Apps authorization documentation currently describes OAuth-based authorization approaches for protected tools:

https://apps.extensions.modelcontextprotocol.io/api/documents/authorization.html
