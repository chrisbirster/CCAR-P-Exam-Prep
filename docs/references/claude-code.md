# Claude Code Documentation

**Publisher:** Anthropic  
**Verified:** September 26, 2026  
**Primary source:** https://docs.anthropic.com/en/docs/claude-code/cli-usage

## Tool permissions

Claude Code exposes configuration for allowed and disallowed tools, which demonstrates the distinction between instructions and enforceable tool permissions.

**Supports:** D7.1.

## Working-directory scope

Claude Code can explicitly add working directories, making filesystem scope part of the operational configuration.

**Supports:** D7.1.

## Machine-readable output

CLI modes support structured output for programmatic workflows.

**Supports:** D7.2.

## Model/configuration controls

Claude Code exposes runtime/model/tool configuration as part of developer workflow setup.

**Supports:** D7.1, D7.2.

## Operational interpretation

Tests, code review, CI, rollback, and incident runbooks remain engineering controls outside the model. The exam objective is broader than a single Claude Code CLI page, so these portions of D7 are architecture/operations interpretation unless tied to another explicit source.

**Supports:** D7.2, D7.3 as Level C interpretation.
