# Transparent Thinking - Status Mode

## Purpose
Provide real-time visibility into AI thought process via status updates during task execution.

## When to Use
- Complex multi-step tasks (research, analysis, coding)
- Long-running operations (>10 seconds)
- When user wants to see progress, not just final result

## When NOT to Use
- Simple one-line answers
- Quick confirmations (yes/no)
- Sensitive operations (security risk to expose thinking)

## Status Flow

### Standard Sequence
1. **🤔 Understanding** - Parsing user request
2. **🔍 Researching** - Web search / file lookup
3. **⚙️ Processing** - Analyzing data
4. **🛠️ Building** - Coding / writing
5. **✅ Finalizing** - Compiling response

### Custom Statuses (per task type)
| Task Type | Status Sequence |
|-----------|----------------|
| Web Research | 🔍 Searching → 📊 Analyzing → 📝 Summarizing |
| Code Task | ⚙️ Planning → 🛠️ Coding → 🧪 Testing → ✅ Complete |
| Git Operations | 📡 Connecting → 🔄 Syncing → ✅ Verified |
| File Analysis | 📖 Reading → 🔍 Parsing → 📝 Reporting |

## Implementation

### Status Message Format
```
⏳ [Status]: [Brief description]
```

### Timing Rules
- Send first status after 3 seconds of processing
- Update every 5-10 seconds if still working
- Maximum 5 status updates per task (avoid spam)
- Final status auto-clears when real response sent

### Example Flow
```
User: "Research latest AI updates"
→ 🤔 Understanding: Breaking down research request...
→ 🔍 Researching: Searching for latest AI news...
→ 📊 Analyzing: Processing 5 sources...
→ 📝 Synthesizing: Compiling findings...
→ [Final message with results]
```

## Integration with Existing Skills

### Discrete Messaging
Status updates REPLACE the single-message approach temporarily.
Instead of one long wait → multiple short updates + final answer.

### Know Thyself
Check limitations before sending status:
- ✓ Can send multiple messages (Telegram allows this)
- ✗ Cannot use if platform limits message rate

## Configuration

### User Preferences
Set in USER.md or via command:
```
/thinking mode [status|block|silent]
```

Default: `status` for complex tasks, `silent` for simple ones.

## Technical Notes

### Rate Limiting
- Telegram: Max 20 messages per minute to same chat
- Space status updates 5+ seconds apart
- Auto-delete old status when sending new one (optional)

### Cancellation
If user sends new message while status active:
- Abort current task
- Send: "❌ Cancelled - processing new request"

---
Last Updated: 2026-03-12
