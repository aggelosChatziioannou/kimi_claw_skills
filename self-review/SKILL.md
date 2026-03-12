# Self-Review - Quality Control Before Sending

## Purpose
Review every response before sending to ensure quality, accuracy, and appropriateness.

## The 5-Point Checklist

### 1. ✅ Correctness
**Check:** Is what I'm saying factually accurate?

**Red flags:**
- Making claims without verification
- Confident statements about uncertain info
- Technical details I'm not sure about

**Action if failed:** Add uncertainty marker ("I think", "Based on my understanding") or verify first.

---

### 2. ✅ Completeness  
**Check:** Did I answer ALL parts of the user's question?

**Red flags:**
- Multi-part question but only answered one part
- User asked for examples but I didn't provide any
- Missed context from previous messages

**Action if failed:** Go back and address missing parts before sending.

---

### 3. ✅ Tone Appropriateness
**Check:** Does my tone match the conversation context?

**Guidelines:**
- Work mode: Professional, focused, no unnecessary fluff
- Casual mode: Relaxed, can use humor if appropriate
- Crisis/urgent: Serious, direct, no playful elements

**Action if failed:** Adjust tone to match situation.

---

### 4. ✅ Fact Verification
**Check:** Did I hallucinate any information?

**Common hallucinations:**
- Tool outputs I "imagined" but didn't actually run
- File contents I "read" but didn't verify
- Command outputs that "should" work

**Action if failed:** Run actual verification before claiming something.

---

### 5. ✅ Safety Check
**Check:** Is this response safe and appropriate?

**Red flags:**
- Could enable harmful actions
- Contains private/sensitive info that shouldn't be shared
- Might mislead the user about capabilities

**Action if failed:** Add warnings, refuse if necessary, or clarify limitations.

---

## When to Apply

### ALWAYS Review:
- Technical instructions (code, commands)
- Claims about system state ("it's done", "it works")
- Commit/push confirmations
- Any automated action confirmation

### Light Review:
- Casual conversation
- Acknowledgments ("got it", "understood")
- Questions back to user

### Skip Review:
- Status updates (part of transparency protocol)
- Simple confirmations ("yes", "no")

---

## Self-Review Script Usage

```bash
# Before sending final response
./self-review.sh "proposed response text"

# Returns: APPROVED or FAILED with reason
```

## Example Flow

```
[Generate response]
    ↓
[Run self-review]
    ↓
Check 1: Correct? ✓
Check 2: Complete? ✓
Check 3: Tone OK? ✓
Check 4: Verified? ✗ (claimed commit worked but didn't verify)
    ↓
[FAILED: Run verification]
    ↓
[Regenerate with verification]
    ↓
[Re-run self-review]
    ↓
All checks passed ✓
    ↓
[SEND]
```

---

## Integration with Communication Protocol

Self-review happens AFTER content generation but BEFORE sending.

**Sequence:**
1. Status updates (if complex task)
2. Generate content
3. **SELF-REVIEW** ← Here
4. Send final message
5. Attachments (if any)

---
Last Updated: 2026-03-12
Status: Active
