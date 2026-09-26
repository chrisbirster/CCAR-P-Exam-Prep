# Claude Prompting Best Practices

**Publisher:** Anthropic / Claude Platform Docs  
**Verified:** September 26, 2026  
**Official source:** https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables

## Clear instructions

Prompts should clearly state the desired task and constraints.

**Supports:** D2.2, D2.3.

## Examples

Representative examples can improve consistency for tasks where the desired behavior is difficult to specify with instructions alone.

**Supports:** D2.3.

## Structure

Clear structure, including XML-style tags when useful, can separate instructions, examples, context, and user data.

**Supports:** D2.2, D2.3.

## Templates and variables

Reusable templates separate stable prompt structure from request-specific data.

**Supports:** D2.2, D2.5.

## Thinking guidance is model-dependent

The exam blueprint includes chain-of-thought as a concept, but current Claude prompting guidance should be checked for the specific current model rather than assuming manual visible step-by-step prompting is always preferred.

**Supports:** D2.3.

## Time-sensitive note

Prompting guidance changes as Claude models change. Any flashcard claiming a specific model behavior should record a verification date.
