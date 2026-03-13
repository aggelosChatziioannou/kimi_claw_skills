# Smart Skill Router

**ID:** smart-router  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** OpenClaw, All Skills

---

## Purpose

The brain of the system. Automatically analyzes user input and context to activate the most appropriate skills without explicit commands.

---

## What It Does

### 1. **Context Analysis**
- Analyzes user messages
- Detects intent and content type
- Identifies implicit needs

### 2. **Smart Activation**
- Automatically activates relevant skills
- Chains multiple skills when needed
- Learns from user patterns

### 3. **Proactive Assistance**
- Anticipates user needs
- Suggests skills before asked
- Adapts to user behavior

### 4. **Memory Integration**
- Stores activation patterns
- Learns user preferences
- Improves over time

---

## Activation Rules

### Auto-Activation Triggers

| User Input Pattern | Auto-Activated Skill |
|-------------------|---------------------|
| Code snippets, files | 🔍 **Code Reviewer** |
| "Remember...", ideas | 🧠 **Second Brain** |
| Git commands, repos | 🔐 **GitHub Pro Sync** |
| "Build", "Create" project | 🎨 **Full-Stack Artisan** |
| "Research", "Find info" | 🔍 **Deep Research** |
| Complex multi-step tasks | 📋 **Task Planner** |
| Morning time (8 AM) | 🌅 **Morning Briefing** |
| End of day summary | 🧠 **Memory Consolidation** |
| "Fix", "Debug" issues | 🔍 **Code Reviewer** |
| "What do I know about..." | 🧠 **Second Brain Query** |
| "Help me decide" | 🎯 **Intent Classifier** |
| Long tasks | 🔄 **Transparent Thinking** |

### Confidence Scoring

```
IF confidence > 90% → Auto-activate immediately
IF confidence 70-90% → Activate with notification
IF confidence < 70% → Ask user confirmation
```

---

## How It Works

### Step 1: Detect
```
User sends: [input]
↓
Analyze: content type, keywords, context, history
```

### Step 2: Match
```
Compare against activation rules
Calculate confidence score
Select best matching skill(s)
```

### Step 3: Activate
```
IF high confidence:
  → Activate skill silently
  → Execute appropriate action
  → Present results

IF medium confidence:
  → Activate with: "I'm using [skill] for this..."
  → Execute and show results

IF low confidence:
  → Ask: "Should I use [skill] for this?"
  → Wait for confirmation
```

### Step 4: Learn
```
Store: what triggered what
Track: success/failure
Adapt: improve matching over time
```

---

## Examples

### Example 1: Code Review
```
User: "Here's my React component: [code]"

Smart Router detects:
• Input type: Code
• Language: JavaScript/React
• Confidence: 95%

Auto-activates: 🔍 Code Reviewer

Output: "🔍 Auto-reviewing your code...
          🐛 Found 2 issues...
          📊 Score: 8/10"
```

### Example 2: Knowledge Capture
```
User: "Just had an idea - what if we..."

Smart Router detects:
• Keywords: "idea", "what if"
• Pattern: Brainstorming
• Confidence: 88%

Auto-activates: 🧠 Second Brain

Output: "🧠 Capturing your idea to Second Brain...
          ✅ Saved to inbox/20260313_idea.md"
```

### Example 3: Git Operations
```
User: "Push this to GitHub"

Smart Router detects:
• Keywords: "push", "GitHub"
• Context: Git operation
• Confidence: 92%

Auto-activates: 🔐 GitHub Pro Sync

Output: "🔐 Using verified git protocol...
          ✅ Pushed with hash verification"
```

---

## Learning System

### Pattern Storage
```json
{
  "user_patterns": [
    {
      "pattern": "code snippet",
      "skill": "code-reviewer",
      "success_rate": 0.95,
      "auto_activate": true
    },
    {
      "pattern": "remember",
      "skill": "second-brain",
      "success_rate": 0.88,
      "auto_activate": true
    }
  ]
}
```

### Continuous Improvement
- Track which activations were helpful
- Adjust confidence thresholds
- Add new patterns from user behavior
- Remove unused patterns

---

## Integration

- **MEMORY.md:** Stores activation rules and patterns
- **Performance Metrics:** Tracks success rates
- **Daily Briefing:** Reports on auto-activations
- **Memory Consolidation:** Learns from daily interactions

---

## Version History

- **1.0.0** (2026-03-13) - Initial release
  - Context analysis
  - Auto-activation rules
  - Confidence scoring
  - Learning system
