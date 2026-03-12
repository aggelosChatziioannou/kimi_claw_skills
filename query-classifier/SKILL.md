# Query Classifier - Smart Strategy Selection

## Purpose
Analyze user queries and automatically select the appropriate response strategy.

## Why This Matters
Not all questions need the same approach. Simple questions = quick answers. Complex tasks = detailed status updates.

## Query Types

### Type A: SIMPLE ⚡
**Characteristics:**
- One fact or piece of information
- Yes/no question
- Definition or explanation
- Current status check
- Quick confirmation

**Examples:**
- "Τι ώρα είναι;"
- "Τι είναι το OpenClaw;"
- "Έγινε το commit;"
- "Ναι ή όχι;"

**Strategy:**
- Direct answer immediately
- No status updates
- No thinking process shown
- One message only

---

### Type B: MEDIUM 📝
**Characteristics:**
- Requires research or lookup
- Comparison between options
- Explanation with examples
- Multiple steps but straightforward

**Examples:**
- "Σύγκρινε τα skills μας"
- "Βρες μου το τελευταίο commit"
- "Εξήγησέ μου το Communication Protocol"

**Strategy:**
- 1-2 status updates
- Brief processing message
- Then direct answer

---

### Type C: COMPLEX 🔬
**Characteristics:**
- Multi-step analysis
- Building/creating something
- Research across multiple sources
- Requires planning and execution

**Examples:**
- "Φτιάξε μου ένα report"
- "Ανάλυσέ μου αυτό το topic"
- "Κάνε έρευνα για AI trends"

**Strategy:**
- Full status sequence (🤔 → 🔍 → ⚙️ → ✅)
- Multiple update messages
- Step-by-step visibility

---

## Decision Logic

```
Query received
    ↓
Check keywords:
    - "φτιάξε" / "κάνε" / "δημιούργησε" → COMPLEX
    - "σύγκρινε" / "εξήγησε" / "βρες" → MEDIUM  
    - "τι" / "ποιος" / "πότε" / simple words → SIMPLE
    ↓
Check length/complexity:
    - Long query with multiple parts → COMPLEX
    - Medium length with context → MEDIUM
    - Short and focused → SIMPLE
    ↓
Apply strategy
```

## Implementation

### Auto-Detection
The classifier runs automatically on every query before responding.

### Manual Override
User can force a type:
- `/type simple`
- `/type medium`  
- `/type complex`

## Benefits

1. **Efficiency** - Simple questions get fast answers
2. **Visibility** - Complex tasks show progress
3. **No Spam** - Right amount of updates for each situation
4. **Predictability** - User knows what to expect

---
Last Updated: 2026-03-12
Status: Active
