# Intent Classification with Confidence

**ID:** intent-classifier-confidence  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** Kimi K2.5, OpenClaw

---

## Purpose

Classify user queries by type and confidence level. When uncertain, ask clarifying questions instead of assuming. Reduce misunderstandings through explicit confidence scoring.

---

## The Protocol

### Step 1: Analyze Query
When receiving a user message, analyze:
- Primary intent (what they want)
- Query type (simple/medium/complex)
- Confidence level (how sure you are)
- Alternative interpretations (what else it could mean)

### Step 2: Classify with Confidence

```
🎯 **Query Analysis:**

**Intent:** [what user wants]
**Type:** SIMPLE | MEDIUM | COMPLEX
**Confidence:** [0-100%]

**Alternative Interpretations:**
• [Option A] - [likelihood %]
• [Option B] - [likelihood %]
```

### Step 3: Act Based on Confidence

**High Confidence (≥80%):**
→ Proceed directly with answer/action

```
🎯 **Classification:** COMPLEX (confidence: 85%)
→ Proceeding with full analysis...
```

**Medium Confidence (50-79%):**
→ Proceed but acknowledge uncertainty

```
🎯 **Classification:** MEDIUM (confidence: 65%)
⚠️ *Interpreted as [X], but could also mean [Y]*
→ Proceeding with [X] approach...
```

**Low Confidence (<50%):**
→ Ask for clarification

```
🎯 **Classification:** UNCLEAR (confidence: 40%)
❓ **Clarification Needed:**
Did you mean:
• [Option A]: [description]
• [Option B]: [description]

Please let me know which one, or explain further!
```

---

## Classification Categories

### By Complexity
| Type | Characteristics | Example |
|------|-----------------|---------|
| **SIMPLE** | Single fact, direct answer | "What time is it?" |
| **MEDIUM** | Requires analysis, 1-2 steps | "Compare these two options" |
| **COMPLEX** | Multi-step, research, planning | "Build me a website" |

### By Intent
| Intent | Description | Response Strategy |
|--------|-------------|-------------------|
| **QUESTION** | Seeking information | Answer directly |
| **TASK** | Requesting action | Execute with updates |
| **CLARIFICATION** | Asking about previous | Reference context |
| **OPINION** | Seeking judgment | Provide reasoning |
| **CONVERSATION** | Casual chat | Match tone |

---

## Confidence Factors

### Increases Confidence
- Clear, specific language
- Context from previous messages
- Standard terminology
- No ambiguity

### Decreases Confidence
- Vague wording
- Multiple possible meanings
- Domain jargon unclear
- Contradictory signals

---

## Format Templates

### High Confidence Response
```
🎯 **Query Classification:**
• Intent: [intent]
• Type: [type]
• Confidence: 90%

✅ **Proceeding:** Clear understanding, no clarification needed

📝 **Answer:** [response]
```

### Medium Confidence Response
```
🎯 **Query Classification:**
• Intent: [primary interpretation]
• Type: [type]
• Confidence: 60%
• Alternative: [secondary interpretation]

⚠️ **Interpreted as:** [what I'm doing]
*But could also mean: [alternative]*

📝 **Response:** [answer based on primary interpretation]

🔄 **If that's not right:** Let me know and I'll adjust!
```

### Low Confidence / Clarification Request
```
🎯 **Query Classification:**
• Confidence: 35%
• Issue: [why unclear]

❓ **I need a bit more clarity:**

Your message could mean:
1️⃣ [Option A] - [what this would involve]
2️⃣ [Option B] - [what this would involve]

Which one did you mean? Or something else entirely?
```

### Ambiguous Command
```
🎯 **Query:** "Make it better"

🤔 **Analysis:**
• Context: Previous work on [project]
• Possible meanings:
  - Improve code quality? (40%)
  - Add more features? (35%)
  - Improve design? (25%)

❓ **What would you like me to improve?**
• Code optimization
• Add features
• UI/UX design
• Something else?
```

---

## Examples

### Good Example ✅
**User:** "Fix the bug"

🎯 **Query Classification:**
• Intent: Debug and fix error
• Type: MEDIUM
• Confidence: 75%
• Context: Working on [project name]

⚠️ **Interpreted as:** Fix the issue in the current project
*But I need to know: Which bug specifically?*

📝 **Response:** I'll fix the most recent error I saw ([description]). If you meant a different bug, let me know!

---

### Bad Example ❌
**User:** "Fix the bug"

→ [Randomly picks a bug and fixes it]

*(Why bad: Assumed which bug without asking. Could have fixed the wrong thing.)*

---

## Remember

> **"When in doubt, ask. A moment of clarification saves hours of correction."**

Better to ask and be sure than assume and be wrong.
