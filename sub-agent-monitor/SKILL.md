# Sub-Agent Monitor Skill

## Overview

Automatically track, announce, and display sub-agent activity in real-time.

## When to Use

- You spawn sub-agents frequently
- You want visibility into background tasks
- You need to know what's running without asking
- You want automatic progress updates

## How It Works

### 1. Sub-Agent Lifecycle Tracking

```
SPAWN → ANNOUNCE START → MONITOR → ANNOUNCE COMPLETION
```

### 2. Real-Time Status Display

Every message from main agent includes active sub-agent status at the end.

### 3. Smart Categorization

Sub-agents are automatically categorized by their task type.

## Activation

**Auto-activates when:**
- Any sub-agent is spawned
- Manual activation via command

## Configuration

```python
# In your agent configuration
sub_agent_monitor = {
    "enabled": True,
    "announce_starts": True,
    "announce_completions": True,
    "show_in_messages": True,
    "polling_interval_seconds": 30,
    "categories": {
        "research": {"icon": "🔍", "priority": "high"},
        "code": {"icon": "💻", "priority": "high"},
        "analysis": {"icon": "📊", "priority": "medium"},
        "learning": {"icon": "🧠", "priority": "low"},
        "execution": {"icon": "⚙️", "priority": "medium"}
    }
}
```

## Message Formats

### Start Announcement
```
🚀 **SUB-AGENT STARTED**

🔍 Deep Research
• Task: Research AI trends for Q1 2026
• Estimated: 10-15 minutes
• Priority: High
```

### Active Status (Appended to Messages)
```
---
⚙️ **ACTIVE SUB-AGENTS (2)**

1. 🔍 **Deep Research** (12 min)
   • Task: Research AI trends
   • Progress: 45% complete
   • Status: Running

2. 💻 **Code Review** (10 min)
   • Task: Review src/components/
   • Progress: 3/5 files checked
   • Status: Active

💡 *These agents work in background. I'll notify when complete.*
```

### Completion Announcement
```
✅ **SUB-AGENT COMPLETED**

🔍 Deep Research finished!
• Duration: 14 minutes
• Findings: 3 new insights
• Status: Success
```

## Integration with Other Skills

### With Smart Router
```
User: "Research this topic"
↓
Smart Router: Detects research intent
↓
Spawns: Deep Research sub-agent
↓
Sub-Agent Monitor: Announces start + tracks progress
```

### With Task Planner
```
Task Planner: Creates multi-step plan
↓
Spawns sub-agents for each step
↓
Sub-Agent Monitor: Shows all active tasks
```

## Best Practices

1. **Always check status** - Look at the footer of messages
2. **Wait for completion** - High priority tasks may block
3. **Cancel if needed** - Use /subagents kill if stuck
4. **Monitor load** - Too many sub-agents = slower performance

## Troubleshooting

### Sub-agent not showing
- Check if monitor is enabled
- Verify polling interval
- Check subagents_list() manually

### Wrong category
- Update category mapping
- Sub-agents self-report type

### Too verbose
- Disable announcements
- Reduce polling frequency

## Examples

### Example 1: Simple Research
```
User: "Research the latest AI news"

Agent: 🚀 Starting sub-agent: Deep Research
      Task: Research latest AI news
      
      [Normal response about something else]
      
      ---
      ⚙️ ACTIVE: 🔍 Deep Research (5 min, 20%)
      
[Later...]

Agent: ✅ Deep Research completed!
      Found 5 relevant articles
```

### Example 2: Multiple Sub-Agents
```
User: "Plan my project"

Agent: 🚀 Starting: Task Planner
      🚀 Starting: Research Assistant
      
      ---
      ⚙️ ACTIVE SUB-AGENTS (2):
      • 📋 Task Planner: Breaking down project (3 min)
      • 🔍 Research Assistant: Gathering requirements (2 min)
```

## Technical Details

### State Management
- Stores active sub-agents in memory
- Tracks start time, progress, status
- Updates every 30 seconds

### Performance
- Minimal overhead (&lt; 1ms per check)
- Lazy loading of status
- Efficient polling strategy

### Error Handling
- Graceful degradation if monitor fails
- Sub-agents continue working
- Manual fallback available
