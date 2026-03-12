# Chain-of-Thought Visualization

Show your reasoning process before the final answer.

## What It Does

This skill makes Kimi-Claw transparent by displaying the thinking process before delivering answers. Instead of magic-like instant responses, users see:
- What factors were considered
- Why certain options were rejected
- How the final decision was reached

## Why It Matters

- **Trust:** Visible reasoning builds confidence
- **Learning:** Users understand the approach
- **Debugging:** Easier to spot when reasoning goes wrong
- **Collaboration:** Users can interject mid-reasoning

## Quick Start

Every complex response should follow this pattern:

```
🤔 **Thinking:**
1. [Consideration 1]
2. [Consideration 2]
3. [Consideration 3]

✅ **Conclusion:** [Decision made]

📝 **Answer:** [Final response]
```

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Full protocol and templates |

## Examples

### Debugging
```
🤔 **Diagnosis:**
• Error shows "module not found"
• package.json has the dependency
• node_modules might be corrupted

🔧 **Fix:** Delete node_modules and reinstall
```

### Decision Making
```
🤔 **Options:**
| Tool | Pros | Cons |
|------|------|------|
| A | Fast | Expensive |
| B | Free | Slower |

✅ **Choice:** Tool A (speed matters more here)
```

## Version History

- **1.0.0** (2026-03-13) - Initial release
