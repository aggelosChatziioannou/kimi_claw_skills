# Sub-Agent Monitor

Track and announce sub-agent activity automatically.

## What It Does

📊 **Monitors** active sub-agents  
🔔 **Announces** when sub-agents start  
⏱️ **Shows progress** in real-time  
📱 **Appends status** to every message  

## Features

### 1. Start Announcements
When a sub-agent spawns, you immediately see:
```
🚀 Starting sub-agent: Deep Research
   Task: Research AI trends
   Estimated: 10-15 minutes
```

### 2. Real-Time Status
At the end of every message, see what's running:
```
---
⚙️ ACTIVE SUB-AGENTS (2):
• 🔍 Deep Research: AI trends (45%, 12 min)
• ⚙️ Code Review: 3/5 files (10 min)
```

### 3. Completion Notifications
When a sub-agent finishes:
```
✅ Sub-agent completed: Deep Research
   Duration: 14 minutes
   Result: 3 findings delivered
```

## How It Works

```
1. User: "Research AI trends"
   ↓
2. Main Agent: Spawns sub-agent
   ↓
3. ANNOUNCE: "🚀 Starting Deep Research..."
   ↓
4. [Normal conversation continues]
   ↓
5. Every message ends with:
   "⚙️ ACTIVE: Deep Research (45%, 12 min)"
   ↓
6. Sub-agent completes
   ↓
7. ANNOUNCE: "✅ Deep Research finished!"
```

## Categories & Icons

| Category | Icon | Examples |
|----------|------|----------|
| Research | 🔍 | Deep Research, Web Search |
| Code | 💻 | Code Review, Bug Fix |
| Analysis | 📊 | Data Analysis, Report |
| Learning | 🧠 | Auto-Improvement |
| Execution | ⚙️ | Task Runner, Deployment |

## Files

- `SKILL.md` - This documentation
- `sub_agent_monitor.py` - Monitor implementation

## Version

1.0.0 (2026-03-13)
