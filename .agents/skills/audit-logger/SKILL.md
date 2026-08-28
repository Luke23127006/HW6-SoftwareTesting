---
name: audit-logger
description: Append an immutable AI Audit entry after each relevant HW06 interaction, recording the exact user prompt, tool/time, concise AI-response summary, and artifact references.
---

# Audit Logger

## Purpose

Make AI Audit logging automatic and consistent throughout HW06.

This skill applies after every HW06-related interaction that produces:

- test analysis
- test cases
- source interpretation
- code
- documentation
- report content
- modified project artifacts

Do not log unrelated casual chat.

## Input

Capture:

- exact user prompt
- concise factual AI response summary
- AI tool/model
- local timestamp
- created/modified artifact paths
- optional full-output file

## Output

Append to:

```text
docs/ai-audit.md
```

Optional full/raw output:

```text
ai-logs/AI-XXX.md
```

## Append-Only Rule

Never edit or overwrite an earlier interaction.

Interaction IDs must increase:

```text
AI-001
AI-002
AI-003
...
```

## Entry Format

Use:

```markdown
## AI-018

**Tool:** ChatGPT / GPT-5.6 Sol  
**Time:** 2026-08-28 01:30:00 +07

### Prompt

```text
<exact user prompt>
```

### AI Response Summary

<short factual summary>

### Artifacts

- `tests/login/generated-tests.yaml`
- `tests/login/coverage.json`

### Full Output Reference

`NOT_RETAINED`
```

## Prompt

The prompt must be verbatim.

Do not summarize or clean up the user's wording in the Prompt field.

## Response Summary

Summarize only what the AI actually produced.

Good:

```text
Generated 38 login test cases covering equivalence partitions,
lockout state, SQL injection probes, and response schema.
```

Bad:

```text
Successfully completed the API-testing task perfectly.
```

## Tool

When known, include both product/tool and model.

Example:

```text
ChatGPT / GPT-5.6 Sol
```

## Timestamp

Use the local timezone:

```text
Asia/Ho_Chi_Minh
```

## Artifacts

List concrete files changed.

If none:

```text
None
```

## Full Output

The compact audit log uses a summary by default.

If retaining the raw response is required or useful, save it under:

```text
ai-logs/AI-XXX.md
```

and reference it.

## Script

Example:

```bash
python .agents/skills/audit-logger/scripts/append_audit.py   --prompt-file prompt.txt   --summary-file summary.txt   --tool "ChatGPT / GPT-5.6 Sol"   --artifact tests/login/generated-tests.yaml
```


## Completion Protocol

1. Write only to the output paths documented by this skill.
2. Never fabricate execution results, screenshots, GitHub links, issue numbers, commit hashes, human-review decisions, or evidence.
3. Preserve traceability to the API specification, FR requirements, SEC requirements, and assignment rules.
4. If the source material does not define a value, write `SPEC_UNDEFINED` or record an ambiguity instead of guessing.
5. After completing an HW06-related user request, follow the root `AGENTS.md` audit rule and append an AI Audit entry.

