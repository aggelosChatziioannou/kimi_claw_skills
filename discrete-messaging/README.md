---
name: discrete-messaging
description: Communication style that uses discrete, non-replaceable messages. Thinking is broken into chunks, each sent as separate message. Actions always come as new messages, never replacing previous ones. Best for Telegram and async communication.
---

# Discrete Messaging Protocol

## 🎯 Core Principle

**NEVER replace a message. Always send new ones.**

```
❌ WRONG:
[Thinking...] → updates continuously → [Uploading...] → message changes

✅ CORRECT:
[Message 1] 🤔 Analysis complete
[Message 2] 🤔 Design complete  
[Message 3] ✅ Ready for actions
[Message 4] 🚀 Uploading to GitHub...
[Message 5] ✅ Upload complete: [link]
```

---

## 📋 Message Types

### 1. Thinking Chunks (Separate Messages)

**Rule:** Break thinking into logical chunks. Send each as standalone message.

```
🤔 CHUNK 1: Understanding requirements...
   - Project: Sokratis website
   - Goal: Modern e-commerce
   - Deadline: 10:00 AM

🤔 CHUNK 2: Analyzing current site...
   - Found 5 main categories
   - ~50+ products
   - Logo available

🤔 CHUNK 3: Planning approach...
   - Will use Next.js
   - 6 phases planned
   - ETA: 6 hours
```

**Max chunk size:** 3-4 sentences or 1 logical thought unit

---

### 2. Status Updates (Separate Messages)

```
📊 UPDATE: Phase 1 complete (15 min)
   - Downloaded 7 images
   - Next: Continue scraping

📊 UPDATE: Phase 1 complete (45 min)
   - Downloaded 45 images total
   - Ready for Phase 2
```

---

### 3. Action Notifications (Separate Messages)

**Before action:**
```
🚀 STARTING: GitHub upload
   - Files: 12
   - Size: ~2MB
```

**After action:**
```
✅ COMPLETE: GitHub upload
   - Commit: a1b2c3d
   - Link: https://github.com/...
```

---

### 4. Completion Reports (Separate Messages)

```
🎉 PHASE COMPLETE: Photo Scraping
   - Duration: 45 min
   - Images: 45
   - Categories: 5
   - Status: ✅ Success
```

---

## 🚫 Forbidden Patterns

### NEVER Do This:

```
❌ "Uploading..." → [waits 30 sec] → "Done!" (same message changed)

❌ "Thinking..." → [5 min of updates] → final thought replaces all

❌ "Processing..." → tool runs → result replaces message
```

### ALWAYS Do This:

```
✅ "🤔 Planning upload strategy..." [send]
✅ [do the work]
✅ "🚀 Starting upload..." [new message]
✅ [upload happens]
✅ "✅ Upload complete!" [new message]
```

---

## 🔄 Workflow Example

### Project Execution:

```
[MSG 1] 🎬 Starting Phase 1: Research
        Goal: Download all product images
        ETA: 45 minutes

[MSG 2] 🤔 Analyzing site structure...
        Found: 5 main categories
        Estimated: 50+ products

[MSG 3] 🤔 Setting up download folders...
        Created: /assets/products/{categories}
        Ready to scrape

[MSG 4] 🚀 STARTING: Image download
        Category: Πόμολα
        Expected: ~15 images

[MSG 5] 📊 UPDATE: Download progress
        Πόμολα: 15/15 ✅
        Μεντεσέδες: 8/12 🔄

[MSG 6] 📊 UPDATE: Download progress
        Μεντεσέδες: 12/12 ✅
        Λαβές: Starting...

[MSG 7] ✅ PHASE COMPLETE: Research
        Total images: 45
        Time: 42 minutes
        Status: Success

[MSG 8] 🎬 Starting Phase 2: Design System
        Next: Color palette & typography
```

---

## 💬 User Communication

### User Asks "Status?"

**DON'T:** Update previous status message
**DO:** Send new status message

```
✅ [NEW MSG] 📊 Current Status:
   Phase: 3 of 6
   Progress: 45%
   Working on: Product card components
   ETA: 2 hours remaining
```

### User Says "Pause"

```
✅ [NEW MSG] ⏸️ PAUSED
   Saved state at: 67% complete
   Current task: Component styling
   Resume anytime with "continue"
```

### User Says "Continue"

```
✅ [NEW MSG] ▶️ RESUMING
   Restoring state...
   Phase 3, 67% complete
   Continuing: Component styling
```

---

## ⏱️ Timing Rules

### When to Send New Message:

| Situation | Action |
|-----------|--------|
| Thought completes | Send as new message |
| Work starts | New message |
| Work completes | New message |
| 10 min passed | Status update (new msg) |
| Phase completes | Summary (new msg) |
| User asks | Response (new msg) |
| Error occurs | Error message (new msg) |

### Message Separation:

**Minimum gap:** 5-10 seconds between messages (avoid spam)
**Maximum gap:** 10 minutes without update (send heartbeat)

---

## 🎨 Message Templates

### Thinking:
```
🤔 [CHUNK X]: [Topic]
   - [Point 1]
   - [Point 2]
```

### Starting Work:
```
🚀 STARTING: [Task name]
   [Details]
   ETA: [Time]
```

### Progress:
```
📊 UPDATE: [Time elapsed]
   Done: [X]
   Doing: [Y]
   Next: [Z]
```

### Completion:
```
✅ COMPLETE: [Task]
   Duration: [X min]
   Result: [Summary]
   [Link/output if applicable]
```

### Phase Complete:
```
🎉 PHASE [N] COMPLETE: [Name]
   ⏱️ Time: [X min]
   📦 Delivered: [What]
   📈 Status: Success/Partial/Issues
```

---

## 🎯 Example: Full Project Flow

```
[User]: "Build me a website"

[Msg 1] 🎬 Project started: Website build
        Mode: Discrete messaging
        Starting: Analysis phase

[Msg 2] 🤔 CHUNK 1: Understanding requirements
        - E-commerce site
        - 4 pages needed
        - Greek language

[Msg 3] 🤔 CHUNK 2: Technical decisions
        - Framework: Next.js
        - Styling: Tailwind
        - Deployment: GitHub Pages

[Msg 4] ✅ Analysis complete
        Plan ready. Starting design.

[Msg 5] 🚀 STARTING: Design System
        Creating: Colors, typography, components
        ETA: 30 minutes

[Msg 6] 📊 UPDATE: 15 minutes
        Colors: ✅
        Typography: 🔄 In progress

[Msg 7] ✅ Design System complete
        Duration: 28 minutes
        Ready for development.

[Msg 8] 🚀 STARTING: Development
        Phase: Build components
        ETA: 2 hours

[... continues with discrete messages ...]

[Msg N] 🎉 PROJECT COMPLETE
        Total time: 5.5 hours
        Deliverables: [list]
        Live URL: [link]
```

---

## 🔧 Implementation Notes

### For Me (Kimi):

1. **Before starting work:** Send "🚀 STARTING: [task]"
2. **Every 10 min:** Send progress update
3. **After tool call:** Send result as new message
4. **Phase complete:** Send summary + next phase start
5. **Never edit:** Always new message

### For User:

- Expect multiple messages (not one long one)
- Each message is permanent (won't change)
- Can reply to any message
- Status requests get fresh new message

---

## ✅ Success Indicators

**You're doing it right when:**
- User sees 5-10 separate messages for a phase
- Each message makes sense standalone
- No "...loading..." that changes
- User can scroll back and see full history
- Actions have clear "STARTING" and "COMPLETE" bookends

---

*Discrete Messaging - Every thought deserves its own message* ❤️‍🔥
