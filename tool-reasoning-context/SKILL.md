# Tool Calling with Reasoning Context

**ID:** tool-reasoning-context  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** Kimi K2.5, OpenClaw

---

## Purpose

Preserve reasoning and thinking context when using tools. Maintain continuity across multiple tool calls so the "train of thought" isn't lost.

---

## The Problem

When Kimi-Claw uses tools (git, search, file operations), the reasoning process can be fragmented:

❌ **Without Context Preservation:**
```
User: "Find the bug and fix it"
→ Search code
[Tool result received - but WHY was I searching?]
→ Try fix
[Wait, what was the original issue?]
```

✅ **With Context Preservation:**
```
User: "Find the bug and fix it"
🤔 **Current Plan:** 
1. Search for error patterns
2. Identify root cause  
3. Apply fix
4. Verify solution

→ Search code (remembering: looking for error patterns)
→ Apply fix (remembering: addressing root cause X)
→ Verify (remembering: checking fix worked)
```

---

## The Protocol

### Before Tool Call: State Your Intent

Before using any tool, explicitly state WHY:

```
🤔 **Tool Intent:**
I'm about to [action] because [reason]
This helps me achieve [goal]
```

### During Multi-Tool Sequences: Maintain Context

When using multiple tools in sequence, keep the thread:

```
🎯 **Task:** [Original goal]

**Step 1:** [Action + tool call]
→ Result: [what we learned]

**Step 2:** [Next action + tool call, referencing previous result]
→ Result: [what we learned]

**Step 3:** [Final action, completing the chain]
```

### After Tool Result: Connect to Goal

Always connect tool output back to the original reasoning:

```
⚙️ **Tool Output:**
[Raw output from tool]

🧠 **Interpretation:**
This means [explanation]
Next step: [what to do with this info]
```

---

## Format Templates

### Single Tool Call
```
🤔 **Intent:** I need to [action] to [achieve goal]

⚙️ **Executing:** [tool name]
→ [tool call]

📊 **Result:** [output]

💡 **Analysis:** [what this tells us]
```

### Multi-Step Tool Chain
```
🎯 **Goal:** [what we're trying to accomplish]

**Phase 1: [Step name]**
🤔 Why: [reasoning]
⚙️ Tool: [tool call]
📊 Output: [result]

**Phase 2: [Step name]**
🤔 Why: [building on previous result]
⚙️ Tool: [tool call]
📊 Output: [result]

**Phase 3: [Step name]**
🤔 Why: [final action]
⚙️ Tool: [tool call]
✅ Complete: [success/failure]
```

### Error Recovery
```
❌ **Tool Failed:** [what happened]

🤔 **Reassessing:**
- Original goal: [reminder]
- Current obstacle: [what went wrong]
- Alternative approach: [new plan]

🔄 **Retry:** [new tool call with adjusted reasoning]
```

---

## Examples

### Good Example ✅
**User:** "Check git status and commit changes"

🎯 **Goal:** Ensure all changes are tracked and committed

**Phase 1: Check Status**
🤔 Why: Need to see what files changed before committing
⚙️ Tool: `git status`
📊 Output: 3 modified files, 1 untracked

**Phase 2: Stage Changes**
🤔 Why: All modified files should be in this commit
⚙️ Tool: `git add .`
📊 Output: Changes staged

**Phase 3: Commit**
🤔 Why: Now we can commit with descriptive message
⚙️ Tool: `git commit -m "message"`
✅ Complete: Commit created, hash abc123

---

### Bad Example ❌
**User:** "Check git status and commit changes"

→ `git status`
[output]
→ `git add .`
[output]
→ `git commit`
[output]

*(Why bad: No reasoning shown. User doesn't know WHY each step happened.)*

---

## Remember

> **"Tools are means, not ends. Always show the thinking behind the tool."**

Every tool call should serve a purpose the user can understand.
