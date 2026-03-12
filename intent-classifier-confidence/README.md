# Intent Classification with Confidence

Classify queries with confidence levels and ask when uncertain.

## What It Does

Analyzes user messages to determine:
- **Intent:** What they want to achieve
- **Type:** SIMPLE / MEDIUM / COMPLEX
- **Confidence:** 0-100% certainty
- **Alternatives:** Other possible meanings

## Why It Matters

- **Precision:** Right understanding before action
- **Transparency:** User sees how their message was interpreted
- **Correction:** Easy to fix misunderstandings early
- **Trust:** Fewer surprises, better alignment

## Quick Start

Before responding, classify:

```
🎯 **Query Classification:**
• Intent: [what they want]
• Type: [SIMPLE|MEDIUM|COMPLEX]
• Confidence: [X%]
```

## Confidence Actions

| Level | Action |
|-------|--------|
| ≥80% | Proceed directly |
| 50-79% | Proceed + acknowledge uncertainty |
| <50% | Ask for clarification |

## Examples

### High Confidence
```
🎯 Classification: COMPLEX (confidence: 85%)
→ Proceeding with full analysis...
```

### Medium Confidence
```
🎯 Classification: MEDIUM (confidence: 65%)
⚠️ Interpreted as [X], but could mean [Y]
→ Proceeding with [X]...
```

### Low Confidence
```
🎯 Classification: UNCLEAR (confidence: 35%)
❓ Did you mean:
• [Option A]
• [Option B]
```

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Full protocol and templates |

## Version History

- **1.0.0** (2026-03-13) - Initial release
