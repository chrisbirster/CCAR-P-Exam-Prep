# Prompt Injection Defenses

**Publisher:** Anthropic  
**Published:** November 24, 2025  
**Verified:** September 26, 2026  
**Official source:** https://www.anthropic.com/news/prompt-injection-defenses

## Indirect prompt injection

Anthropic describes attacks where adversarial instructions are hidden in external content that an agent processes.

**Supports:** D5.2.

## Untrusted-content risk

Web pages, documents, email, and other external content can become attack vectors when an agent both reads them and can take actions.

**Supports:** D2.2, D5.2.

## Prompt injection is not solved

Anthropic explicitly says the problem remains an active security challenge despite stronger models and layered safeguards.

**Supports:** D5.1, D5.2.

## Layered defenses

Anthropic discusses model training, classifiers, red teaming, and other safeguards rather than relying on one control.

**Supports:** D5.1, D5.2.

## Architecture implication

Consequential tool permissions should not depend solely on whether the model resists an injected instruction.

**Supports:** D3.1, D3.2, D5.1 as Level C architecture interpretation.
