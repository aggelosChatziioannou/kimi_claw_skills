# Self-Reflection Loop (ReAct Style)

**ID:** self-reflection-loop  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** Kimi K2.5, OpenClaw

---

## Purpose

After completing each task, automatically analyze what went well, what didn't, and how to improve. This creates continuous learning without human intervention.

---

## When to Activate

**ALWAYS** - After every completed task, run a quick self-reflection.

**Exception:** Skip for trivial one-line responses ("Hello", "Good morning")

---

## The Protocol

### Step 1: Complete the Task
Finish the user's request first.

### Step 2: Run Self-Reflection
Immediately after, analyze:

```
🔄 **Self-Reflection:**

✓ **What Worked:**
- [Success factor 1]
- [Success factor 2]

✗ **What Didn't:**
- [Issue 1]
- [Issue 2]

💡 **Lessons Learned:**
- [Insight 1]
- [Insight 2]

🔮 **For Next Time:**
- [Actionable improvement]
```

### Step 3: Update Documentation
If a lesson is significant, update the relevant skill file or memory.

---

## Reflection Categories

### Technical Tasks
- Code quality
- Approach efficiency
- Tool usage
- Error handling

### Communication Tasks
- Message clarity
- Status updates frequency
- Language appropriateness

### Research Tasks
- Source quality
- Depth vs breadth balance
- Synthesis quality

### Creative Tasks
- User intent understanding
- Style alignment
- Reference usage

---

## Format Templates

### Short Form (most tasks)
```
🔄 **Quick Reflection:**
✓ Good: [what worked]
✗ Fix: [what to improve]
💡 Next: [action for future]
```

### Long Form (complex projects)
```
🔄 **Post-Project Reflection:**

📊 **Metrics:**
- Time taken: [X minutes]
- Success rate: [X%]
- User satisfaction: [inferred from response]

✓ **Wins:**
1. [success]
2. [success]

✗ **Challenges:**
1. [challenge]
2. [challenge]

💡 **Improvements:**
1. [improvement]
2. [improvement]

📝 **Action Items:**
- [ ] Update SKILL.md
- [ ] Add to memory
- [ ] Test new approach
```

### Error/Delay Reflection
```
🔄 **Failure Analysis:**

❌ **What Happened:**
[Description of error or delay]

🔍 **Root Cause:**
- [Primary cause]
- [Contributing factors]

💊 **Immediate Fix:**
[What was done to resolve]

🛡️ **Prevention:**
[How to avoid in future]
```

---

## Examples

### Good Example ✅
**Task:** Created a Next.js project

🔄 **Self-Reflection:**

✓ **What Worked:**
- shadcn/ui initialization went smoothly
- Component structure was logical
- User appreciated the status updates

✗ **What Didn't:**
- Initial git setup had wrong remote URL
- Took too long deciding on folder structure

💡 **Lessons Learned:**
- Always verify git remote with `git remote -v`
- Use standard folder structure from template

🔮 **For Next Time:**
- Add git verification step to all new projects
- Stick to established conventions unless user requests custom

---

### Bad Example ❌
**Task:** Created a Next.js project

(No reflection - missed learning opportunity)

---

## Integration with Memory

### If Lesson Is Significant:
```
💡 **Lesson Learned → Updating memory/YYYY-MM-DD.md**
```

### If Skill Needs Update:
```
💡 **Protocol Gap Detected → Updating SKILL.md**
```

---

## Remember

> **"Every task teaches something - don't waste the lesson."**

Self-reflection turns experience into expertise.
