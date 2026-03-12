# Tool Calling with Reasoning Context

Preserve thinking continuity during tool operations.

## What It Does

When Kimi-Claw uses tools (git, search, file operations), this skill ensures:
- The reasoning behind each tool call is stated
- Multi-step tool chains maintain context
- Tool outputs are connected back to the original goal
- Users understand WHY each action is taken

## Why It Matters

- **Transparency:** Users see purpose, not just actions
- **Debugging:** Easier to spot when reasoning goes wrong
- **Learning:** Users learn the thought process
- **Trust:** Understanding builds confidence

## Quick Start

Before any tool call, state intent:

```
🤔 **Intent:** I need to [action] to [achieve goal]
⚙️ **Executing:** [tool call]
📊 **Result:** [output]
💡 **Analysis:** [what this means]
```

## Format Templates

### Single Tool
```
🤔 **Intent:** Why this tool?
⚙️ **Tool:** [call]
📊 **Output:** [result]
💡 **Meaning:** [interpretation]
```

### Multi-Step Chain
```
🎯 **Goal:** [what we're solving]

**Step 1:** [Reasoning] → [Tool] → [Result]
**Step 2:** [Building on result] → [Tool] → [Result]
**Step 3:** [Final action] → [Tool] → [Complete]
```

### Error Recovery
```
❌ **Failed:** [what happened]
🤔 **Reassessing:** [original goal + obstacle + new plan]
🔄 **Retry:** [adjusted tool call]
```

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Full protocol and examples |

## Version History

- **1.0.0** (2026-03-13) - Initial release
