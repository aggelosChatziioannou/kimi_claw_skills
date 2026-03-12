# Performance Metrics Tracking

Data-driven improvement through analytics.

## What It Does

Tracks and analyzes:
- Task completion rates and durations
- Tool usage patterns
- Error frequencies and types
- Improvement trends over time

## Why It Matters

- **Visibility:** See actual performance, not perception
- **Trends:** Identify what's getting better/worse
- **Focus:** Prioritize real problem areas
- **Proof:** Measure improvement objectively

## Quick Start

When starting a task:
```
📊 **Metrics Start:** [task_type] at [time]
```

When completing:
```
📊 **Task Log:**
- Type: [category]
- Duration: [X minutes]
- Status: ✅|❌|⚠️
- Tools: [list]
- Errors: [count]
```

## Report Generation

Weekly summary:
```
═══════════════════════════════════════
📊 **PERFORMANCE REPORT**
═══════════════════════════════════════
Tasks: 25 | Success: 92% | Avg: 12min

📋 Top Task Types:
• Skill Creation: 5 (8min avg)
• Code Review: 8 (5min avg)
• Research: 7 (18min avg)

⚠️ Common Errors:
• Git auth: 2 occurrences
• Timeouts: 1 occurrence

🎯 Trends:
📈 Faster at skill creation (-15%)
⚠️ Git auth needs preventive check
═══════════════════════════════════════
```

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Full protocol and templates |
| `memory/performance-metrics.json` | Raw data storage |
| `memory/performance-reports/` | Generated reports |

## Data Structure

```json
{
  "timestamp": "2026-03-13T07:15:00Z",
  "type": "skill_creation",
  "duration_minutes": 7,
  "status": "success",
  "tools": ["write", "exec"],
  "errors": 0
}
```

## Version History

- **1.0.0** (2026-03-13) - Initial release
