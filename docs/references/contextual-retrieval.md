# Contextual Retrieval

**Publisher:** Anthropic  
**Published:** September 19, 2024  
**Verified:** September 26, 2026  
**Official source:** https://www.anthropic.com/engineering/contextual-retrieval

## Retrieval-Augmented Generation

Anthropic describes RAG as retrieving relevant information from a knowledge base and adding it to the model's prompt/context.

**Supports:** D3.5.

## Semantic retrieval

Embedding-based retrieval can find semantically related passages even when wording differs.

**Supports:** D3.5, D3.6.

## Lexical / BM25 retrieval

Lexical search can preserve exact-word and exact-term matching that semantic search may miss.

**Supports:** D3.6.

## Hybrid retrieval

Combining lexical and semantic retrieval can improve coverage where both exact terminology and conceptual similarity matter.

**Supports:** D3.6.

## Reranking

Reranking can improve ordering of retrieved candidates after first-stage retrieval.

**Supports:** D3.3, D3.5, D3.6.

## Contextualized chunks

The Contextual Retrieval approach adds document-level context to chunks before indexing to reduce ambiguity.

**Supports:** D3.5.

## Architecture interpretation: live state

The article is about knowledge retrieval. Our study rule that rapidly changing transactional state should usually come from its authoritative operational API is an architecture heuristic, not a direct quote from this source.

**Supports:** D3.6 as Level C interpretation.
