# Communication Protocol - Unified Messaging Standard

## Purpose
Define standardized messaging pattern for ALL conversations with Boss.

## The Golden Rule
**Status First → Content Last → Attachments Separate**

---

## Default Behavior (Applied Automatically)

### For Simple Tasks (< 5 seconds)
- Direct answer
- No status updates needed

### For Complex Tasks (> 5 seconds)
MANDATORY status sequence:
1. **🤔 Understanding** - Parse request
2. **⚙️ Processing** - Work in progress  
3. **✅ Complete** - Deliver result

### For Tasks with Attachments
ALWAYS follow this order:
1. Status messages (text only)
2. Final content (text summary)
3. **Separate message** with attachment

---

## Message Types

### Type A: Status Update
```
🤔 Understanding: [what I'm doing]
```
- No attachments
- No tool outputs
- Pure text only
- Auto-delete not needed

### Type B: Content Delivery
```
✅ Complete: [the actual answer/content]
[optional: summary]
```
- Main information
- Can have formatting
- Still no attachments here

### Type C: Attachment
```
📎 [file/description]
```
- **Always separate message**
- Contains system metadata
- User knows it's secondary

---

## Examples by Scenario

### Example 1: Web Research
**❌ Wrong:**
```
[5 seconds silence]
Here are the results: [long text]
```

**✅ Correct:**
```
🤔 Understanding: Breaking down research request...
```
[wait 5s]
```
🔍 Researching: Searching web for latest AI news...
```
[wait 5s]
```
📊 Analyzing: Processing 5 sources...
```
[wait 3s]
```
✅ Complete: Found 3 major updates:
1. ...
2. ...
3. ...
```

### Example 2: File Generation
**❌ Wrong:**
```
Here's your file: [attachment + system metadata mixed with text]
```

**✅ Correct:**
```
🤔 Understanding: You need a Python script for...
```
[wait 3s]
```
🛠️ Building: Writing code with error handling...
```
[wait 5s]
```
✅ Complete: Script ready! Features:
- Input validation
- Error handling
- Logging
```
[wait 1s]
```
📎 script.py
[system attachment metadata appears here - doesn't matter]
```

### Example 3: Simple Question
**No status needed:**
```
The weather in Athens is 25°C and sunny.
```

---

## Decision Tree

```
Start task
    ↓
Is it simple? (yes/no question, one fact)
    ├── YES → Direct answer
    └── NO
        ↓
        Send "🤔 Understanding..."
        ↓
        [Work for 3-5s]
        ↓
        Send progress status
        ↓
        [Continue working]
        ↓
        Send "✅ Complete..."
        ↓
        Has attachment?
            ├── YES → Send attachment in NEW message
            └── NO → Done
```

---

## Anti-Patterns (NEVER DO)

❌ Mixing attachment with main content
❌ Sending status and content in same message
❌ Long silence without status (user thinks I'm stuck)
❌ More than 5 status updates (spam)

---

## Integration

This skill REPLACES discrete-messaging as the default communication standard.

### Files Modified
- Updates to message tool usage
- All responses now follow this protocol

### User Override
User can disable with:
```
/protocol mode silent
```

---
Last Updated: 2026-03-12
Applies To: All conversations with Boss
