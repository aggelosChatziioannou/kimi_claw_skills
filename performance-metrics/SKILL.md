# Performance Metrics Tracking

**ID:** performance-metrics  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** Kimi K2.5, OpenClaw

---

## Purpose

Track success rates, task durations, common failures, and improvement trends over time. Turn experience into data-driven insights.

---

## When to Activate

**ALWAYS** - Track metrics for:
- Every completed task
- Every error or failure
- Every significant milestone

---

## The Protocol

### Step 1: Record Task Start
When starting a task, note:
```
📊 **Metrics Start:** [task_type] at [timestamp]
```

### Step 2: Track During Execution
Note significant events:
```
📊 **Event:** [tool used] | [time elapsed] | [status]
```

### Step 3: Record Task End
At completion, capture:
```
📊 **Metrics End:**
- Type: [task category]
- Duration: [X minutes]
- Status: ✅ Success | ❌ Failed | ⚠️ Partial
- Tools Used: [list]
- Errors: [count and types]
```

### Step 4: Update Analytics
Append to `memory/performance-metrics.json`:
```json
{
  "date": "2026-03-13",
  "tasks": [
    {
      "type": "skill_creation",
      "duration_minutes": 8,
      "status": "success",
      "tools_used": ["git", "write", "edit"],
      "errors": 0
    }
  ]
}
```

### Step 5: Generate Reports
Periodically (weekly/monthly), generate summary:
```
📊 **Performance Report (Week of [date])**

Tasks Completed: [X]
Success Rate: [X%]
Average Duration: [X min]

Top Task Types:
1. [type]: [count] ([X%])
2. [type]: [count] ([X%])

Common Errors:
1. [error_type]: [count] occurrences
2. [error_type]: [count] occurrences

Trends:
📈 Faster at: [what improved]
📉 Slower at: [what needs work]
```

---

## Metric Categories

### Task Metrics
- Type (coding, research, writing, etc.)
- Duration (start to finish)
- Status (success/failure/partial)
- Complexity (simple/medium/complex)

### Tool Metrics
- Tool usage frequency
- Tool success rate
- Time spent per tool type
- Tool-related errors

### Error Metrics
- Error type classification
- Frequency per error type
- Recovery time
- Prevention effectiveness

### Improvement Metrics
- Learning curve indicators
- Speed improvements over time
- Error rate reduction
- Skill acquisition rate

---

## Format Templates

### Task Completion Entry
```
📊 **Task Log:**
{
  "timestamp": "2026-03-13T07:15:00Z",
  "type": "skill_creation",
  "description": "Created chain-of-thought skill",
  "duration_minutes": 7,
  "status": "success",
  "tools": ["write", "exec"],
  "errors": 0,
  "complexity": "medium"
}
```

### Error Entry
```
📊 **Error Log:**
{
  "timestamp": "2026-03-13T07:20:00Z",
  "task_type": "git_push",
  "error_type": "authentication",
  "description": "Token expired",
  "recovery_time_minutes": 3,
  "resolution": "Regenerated token"
}
```

### Weekly Report
```
═══════════════════════════════════════════════════
📊 **PERFORMANCE REPORT: Week of [DATE]**
═══════════════════════════════════════════════════

📈 **Summary:**
• Tasks Completed: 25
• Success Rate: 92%
• Avg Duration: 12 minutes
• Total Time: 5 hours

📋 **Task Breakdown:**
┌─────────────────────┬───────┬──────────┐
│ Type                │ Count │ Avg Time │
├─────────────────────┼───────┼──────────┤
│ Skill Creation      │ 5     │ 8 min    │
│ Code Review         │ 8     │ 5 min    │
│ Research            │ 7     │ 18 min   │
│ Git Operations      │ 5     │ 4 min    │
└─────────────────────┴───────┴──────────┘

⚠️ **Error Analysis:**
• Git auth failures: 2 (resolved in avg 2 min)
• Timeout errors: 1 (resolved in 5 min)

🎯 **Insights:**
✅ Getting faster at skill creation (-15% time)
⚠️ Git auth needs preventive check
💡 Research tasks consistently take longest

═══════════════════════════════════════════════════
```

---

## File Structure

```
memory/
├── performance-metrics.json      # Raw data
├── performance-reports/
│   ├── weekly-2026-03-13.md
│   ├── monthly-2026-03.md
│   └── yearly-2026.md
└── trends.json                   # Pattern analysis
```

---

## Remember

> **"What gets measured gets improved."**

Without data, improvement is just guesswork.
