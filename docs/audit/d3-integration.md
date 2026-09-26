# D3 — Integration Audit

**Domain 3 source collection:** [D3.md](D3.md)

## D3.1 — Capability bloat

**Source packet:** [D3.1-sources.md](D3.1-sources.md)

**Status:** VERIFIED WITH INTERPRETATION  
**Audited:** September 26, 2026

### Blueprint fit

The CCAR-P blueprint explicitly includes:

> Evaluate tool/agent configuration for capability bloat.

So the section is unquestionably in scope.

### Claim audit

#### "Every tool, credential, dataset, and side effect exposed to an agent expands the attack surface."

**Result:** VERIFIED.

Anthropic's current trustworthy-agent guidance says that the more open an agent's environment is and the more tools it can use, the more an attacker can do after compromise. Anthropic also advises customers to think carefully about which tools, data, permissions, and environments they expose to agents.

**Evidence:**  
- [Trustworthy Agents — secure interactions](../references/trustworthy-agents.md#secure-interactions)
- [How We Contain Claude — external content and tools](../references/how-we-contain-claude.md#external-content-and-tools)

#### "...expands the decision surface."

**Result:** VALID INTERPRETATION.

This is useful architecture language, but "decision surface" is our term rather than an Anthropic-defined concept. Keep it, but do not create a flashcard implying Anthropic defines the phrase.

#### Least privilege means minimizing tools, permissions, data, credentials, and environments.

**Result:** VERIFIED PRINCIPLE.

Anthropic's current containment guidance explicitly recommends granular tool permissions and environmental restrictions. Its trustworthy-agent material advises careful control over tools, data, permissions, and operating environments.

**Evidence:**  
- [How We Contain Claude — granular permissions](../references/how-we-contain-claude.md#granular-permissions)
- [How We Contain Claude — environment boundaries](../references/how-we-contain-claude.md#environment-boundaries)
- [Trustworthy Agents — risk grows with consequential action](../references/trustworthy-agents.md#risk-grows-with-consequential-action)

#### Too many similar tools can hurt tool selection.

**Result:** VERIFIED.

Anthropic's Advanced Tool Use article says common failures include incorrect tool selection and parameters, especially when tools have similar names. Its tool-design guidance recommends clear, distinct tool boundaries and specifications.

**Evidence:**  
- [Advanced Tool Use — tool-definition context bloat](../references/advanced-tool-use.md#tool-definition-context-bloat)
- [Writing Effective Tools — avoid overlapping capability](../references/writing-effective-tools.md#avoid-overlapping-capability)

#### "Separate read and write tools when their risk differs."

**Result:** VALID INTERPRETATION, STRONGLY SUPPORTED.

Anthropic explicitly contrasts read-only access with write access to production as different blast radii. The exact "separate them into different tools" formulation is our design recommendation.

**Evidence:**  
- [How We Contain Claude — granular permissions](../references/how-we-contain-claude.md#granular-permissions)

#### Prefer bounded task-level tools over generic arbitrary query/command tools.

**Result:** VALID INTERPRETATION.

Anthropic supports clear tool boundaries, well-defined inputs/outputs, and containment. However, "always prefer a task-level tool" would be too absolute: developer/coding agents may legitimately need broad shell/tool access inside a strong sandbox.

**Required wording:** use "prefer bounded tools **when the use case does not require general-purpose capability**."

### Corrections required

The current note is mostly correct. One sentence should be softened:

**Current:**
> Prefer bounded, task-level tools over generic "execute arbitrary query" or "run any command" interfaces when possible.

**Audited wording:**
> Prefer bounded, task-level tools when the use case does not require general-purpose capability; when broad tools are necessary, constrain their environment, credentials, and permissions.

This avoids teaching "generic tools are always wrong," which would conflict with real Claude Code-style agent architectures.

### Flashcard implications

Safe P0 facts:

- More agent tools/permissions increase potential blast radius.
- Tool permissions should be scoped to the task.
- Model instructions do not replace hard environmental/permission boundaries.
- Similar/overlapping tool definitions can increase selection errors.
- Read-only and write access have materially different risk.

Good scenario card:

> An agent only needs to read order status, but it has a production database credential with write access. What should the architect change first?

Expected concept: reduce permissions/capability to the minimum needed rather than relying on prompting or logging.

Do **not** create:

> Anthropic defines "decision surface" as ...

That phrase is ours.

### Verdict

D3.1 is strong after the wording adjustment above. It is ready to become flashcard source material once the concept note is updated.
