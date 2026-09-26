# D7 — Developer Productivity & Operational Enablement

**Exam weight:** 7%  
**Objectives:** D7.1–D7.3

Domain 7 asks whether a team can use Claude effectively and operate the resulting systems without permanent dependence on one architect.

---

## D7.1 — Configure Claude tools and environments for teams

### Core idea

Team productivity improves when Claude's environment has **shared guidance, scoped capabilities, and enforceable controls**.

### What you need to know

Common team-level building blocks can include:

- project instructions;
- shared prompt/configuration assets;
- MCP/tool configuration;
- permissions;
- hooks;
- sandboxing;
- subagent definitions;
- reusable Skills/procedures;
- model selection rules;
- cost/spending controls.

The critical distinction is:

**Instruction** influences model behavior.

**Control** enforces what the model/runtime is permitted to do.

Examples:

- "Do not modify production" is an instruction.
- No production credentials + network/tool restriction is a control.

- "Run tests before committing" is an instruction.
- Required CI checks are a control.

### Decision rules

Standardize high-value shared behavior at the team/repository level.

Use sandboxing and permission boundaries for actions that should not depend on model compliance.

Version shared instructions/Skills like other operational assets.

### Common traps

- One huge instruction file with no enforcement.
- Every developer has a different tool configuration.
- Broad credentials because setup is easier.
- Skills/plugins added without provenance or review.

### Exam cues

Watch for: **Claude Code, team config, hook, permission, sandbox, Skill, shared tool, guardrail**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Claude Code — tool permissions](../references/claude-code.md#tool-permissions)
- [Claude Code — working-directory scope](../references/claude-code.md#working-directory-scope)
- [Agent Skills — Skills package reusable expertise](../references/agent-skills.md#skills-package-reusable-expertise)

---

## D7.2 — Improve developer workflows using AI-assisted tooling

### Core idea

AI assistance can accelerate engineering, but **verification and accountability remain human/system responsibilities**.

### Good uses

- repository exploration;
- implementation drafts;
- refactoring;
- test creation;
- debugging;
- code review;
- documentation;
- incident analysis.

### What good enablement includes

**Clear task context**  
Provide goals, constraints, relevant files, and acceptance criteria.

**Verification tools**  
Tests, linters, type checks, security scans, preview environments.

**Scoped permissions**  
Default to local/reversible actions; raise approval for shared/destructive actions.

**Reviewability**  
Developers should understand the generated change well enough to own it.

### Decision rules

The more consequential the change, the stronger the independent verification required.

Use agents to accelerate the engineering loop, not bypass CI, code review, or security boundaries.

### Common traps

- Merging because tests passed without reviewing whether tests are sufficient.
- Asking an agent to "make it work" with production credentials.
- Generated code nobody on the team understands.
- Disabling safeguards because the agent finds them inconvenient.

### Exam cues

Watch for: **developer workflow, coding assistant, tests, code review, verification, productivity**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Claude Code — machine-readable output](../references/claude-code.md#machine-readable-output)
- [Claude Code — operational interpretation](../references/claude-code.md#operational-interpretation)

---

## D7.3 — Support debugging and operational issue resolution

### Core idea

Teams need repeatable ways to move from **symptom → evidence → likely layer → fix → verification**.

### Symptom map

| Symptom | Likely areas to inspect |
| --- | --- |
| Quality declines | model/prompt version, retrieval corpus/index, input drift |
| Latency rises | context growth, dependency latency, cache misses, extra calls |
| Tool failures | credentials, scopes, schema/contract, rate limits, dependency outage |
| Cost rises | model routing, context size, call count, cache hit rate |
| Agent loses work | state persistence, orchestration, worker result handling |
| Wrong tenant data | authorization/filtering boundary — treat as security incident |

### Runbook contents

A good runbook includes:

- alert/symptom;
- dashboards/logs to inspect;
- known causes;
- safe diagnostic steps;
- rollback/fallback;
- escalation owner;
- evidence to preserve;
- post-incident regression test.

### Operational enablement

The architecture is not truly handed off if only the original architect can debug it.

Build:
- trace visibility;
- known failure patterns;
- clear ownership;
- escalation paths;
- rehearsed rollback.

### Common traps

- "Ask the model why it failed" as the primary incident process.
- No correlation across tool/model logs.
- A runbook that assumes production admin access for everyone.
- Fixing an incident without creating a regression test.

### Exam cues

Watch for: **runbook, incident, debug, latency, tool failure, cost spike, operational handoff**.


### References

- [CCAR-P Exam Guide v1.0](../references/ccar-p-exam-guide-v1.md)
- [Claude Code — operational interpretation](../references/claude-code.md#operational-interpretation)
- [Demystifying Evals — trajectories / transcripts](../references/demystifying-evals.md#trajectories-transcripts)
- [Demystifying Evals — regression evaluation](../references/demystifying-evals.md#regression-evaluation)

---

## Domain 7 summary

```text
shared guidance
+ scoped permissions
+ verification
+ observable systems
+ runbooks
+ team ownership
= operational enablement
```

## Primary references

- Anthropic Claude Platform, “Prompting Best Practices”  
  https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables
- Anthropic, “Equipping Agents for the Real World with Agent Skills”  
  https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Anthropic, “Effective Context Engineering for AI Agents”  
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
