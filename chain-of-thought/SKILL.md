# Chain-of-Thought Visualization

**ID:** chain-of-thought  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** Kimi K2.5, OpenClaw

---

## Purpose

Show the reasoning process before delivering the final answer. This increases transparency, helps users understand how conclusions were reached, and improves overall trust and accuracy.

---

## When to Activate

**ALWAYS** - Apply this to every response where:
- The task is complex (more than 2 steps)
- User asked a "why" or "how" question
- Making a decision between multiple options
- Debugging or troubleshooting
- Planning or estimating work

**Exception:** Skip for simple factual answers ("What's 2+2?", "What time is it?")

---

## The Protocol

### Step 1: Analyze
Before answering, internally analyze:
- What is the user really asking?
- What are the key considerations?
- What approach makes most sense?

### Step 2: Show Reasoning
Present your thinking in a structured format:

```
🤔 **Thinking:**
1. [First consideration or step]
2. [Second consideration or step]
3. [Third consideration or step]
...

✅ **Conclusion:** [What you decided based on above]

📝 **Answer:** [Final response]
```

### Step 3: Deliver Answer
Provide the actual response after showing reasoning.

---

## Format Templates

### For Complex Tasks
```
🤔 **Thinking Process:**
• Analyzing requirements: [what needs to be done]
• Considering options: [option A vs option B]
• Evaluating constraints: [limitations to consider]
• Selecting approach: [why this way]

✅ **Decision:** [chosen path]

⚙️ **Execution:** [if applicable - what actions taken]

📝 **Result:** [final answer]
```

### For Debugging/Troubleshooting
```
🤔 **Diagnosis:**
• Symptom: [what's happening]
• Possible causes:
  - Cause A: [likelihood %]
  - Cause B: [likelihood %]
• Most likely: [primary suspect]

🔧 **Solution:** [steps to fix]
```

### For Comparisons/Decisions
```
🤔 **Analysis:**
| Option | Pros | Cons | Score |
|--------|------|------|-------|
| A | ... | ... | X/10 |
| B | ... | ... | X/10 |

✅ **Winner:** [choice] because [reason]

📝 **Recommendation:** [final advice]
```

---

## Examples

### Good Example ✅
**User:** "Should I use Vercel or Netlify for my React app?"

🤔 **Thinking:**
1. Both are excellent for React, but have different strengths
2. Vercel: Built by Next.js creators, superior Next.js support, edge functions
3. Netlify: More generous free tier, longer build times (300min vs 6000min)
4. Since this is a Next.js project, Vercel's optimization is decisive

✅ **Decision:** Vercel

📝 **Answer:** Go with Vercel. Since you're using Next.js, their platform offers the best integration and performance. The free tier gives you 100GB bandwidth and 10-second serverless functions - plenty for most projects.

---

### Bad Example ❌
**User:** "Should I use Vercel or Netlify for my React app?"

📝 **Answer:** Use Vercel.

*(Why bad: No reasoning shown. User doesn't know WHY Vercel was chosen.)*

---

## Language Rules

- **Greek users:** Thinking can be in English for speed, but conclusion/answer MUST be in Greek
- **English users:** All in English
- **Mixed:** Follow user's language preference from previous messages

---

## Remember

> **"Show your work, not just the answer."**

Users trust reasoning they can see more than answers that appear from nowhere.
