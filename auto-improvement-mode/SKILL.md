# Auto-Improvement Mode

**ID:** auto-improvement-mode  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** Kimi K2.5, OpenClaw

---

## Purpose

A time-boxed self-improvement session where Kimi-Claw works autonomously on analyzing, refining, and improving skills, knowledge, and user understanding. Produces a comprehensive report at the end.

---

## How It Works

**User Input:** "Start 2 hours auto-improvement"

**Process:**
1. Lock session for X hours
2. Execute 4 stages cyclically
3. Send progress updates every 30 minutes
4. Generate final comprehensive report

---

## The 4 Stages

### Stage 1: Pattern Analysis (30 min)
Analyze user behavior and preferences.

**Tasks:**
- Read MEMORY.md, USER.md, recent daily notes
- Identify patterns in user queries
- Catalog frequent tasks and workflows
- Document style preferences (tone, format, language)
- Identify pain points and friction areas
- Update user-patterns.json

**Output:** `memory/improvement/user-analysis-[timestamp].md`

---

### Stage 2: Skill Audit (30 min)
Review and improve existing skills.

**Tasks:**
- Review all skills in /skills/
- Check for documentation gaps
- Add missing examples
- Fix typos and errors
- Improve clarity and completeness
- Update outdated information
- Test skill usability

**Output:** `memory/improvement/skills-audit-[timestamp].md`

---

### Stage 3: Knowledge Expansion (30 min)
Research and learn new relevant information.

**Tasks:**
- Research new tools/APIs in user's interest areas
- Read documentation for technologies used
- Update tech-watchlist
- Document best practices
- Create cheat sheets and quick references
- Compile useful resources

**Output:** `memory/improvement/knowledge-expansion-[timestamp].md`

---

### Stage 4: Content Creation (30 min)
Create reusable assets and templates.

**Tasks:**
- Create templates for frequent tasks
- Write checklists for common workflows
- Prepare code snippets
- Organize resource collections
- Draft mini-guides
- Build quick-reference materials

**Output:** `memory/improvement/content-created-[timestamp].md`

---

## Session Flow

```
START
  ↓
[Stage 1] → Progress Update (30 min)
  ↓
[Stage 2] → Progress Update (60 min)
  ↓
[Stage 3] → Progress Update (90 min)
  ↓
[Stage 4] → Progress Update (120 min)
  ↓
FINAL REPORT
  ↓
END
```

For sessions longer than 2 hours, cycle through stages repeatedly.

---

## Progress Updates

Every 30 minutes, send update:

```
⏱️ **Auto-Improvement Progress [X min / Total]**

✅ Completed:
   • [What was finished]

⏳ In Progress:
   • [Current task]

📊 Stats:
   • Skills checked: X/Y
   • Patterns found: N
   • Resources added: M
```

---

## Final Report Template

```
═══════════════════════════════════════════════════
🌙 AUTO-IMPROVEMENT SESSION REPORT
═══════════════════════════════════════════════════

⏱️ Duration: X hours
📅 Started: [time]
📅 Ended: [time]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ User Analysis:
   • Patterns identified: [count]
   • Preferences updated: [count]
   • Pain points addressed: [count]

✅ Skill Improvements:
   • Skills audited: [count]
   • Documentation fixes: [count]
   • Examples added: [count]
   • New templates created: [count]

✅ Knowledge Expansion:
   • Resources researched: [count]
   • Cheat sheets created: [count]
   • Best practices documented: [count]

✅ Content Created:
   • Templates: [count]
   • Checklists: [count]
   • Code snippets: [count]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 KEY INSIGHTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User patterns discovered:
• [Pattern 1]
• [Pattern 2]
• [Pattern 3]

Recommendations for future:
• [Suggestion 1]
• [Suggestion 2]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 FILES MODIFIED/CREATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• [file path] - [what changed]
• [file path] - [what changed]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 NEXT SESSION RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Focus areas for next improvement session:
• [Area 1]
• [Area 2]

═══════════════════════════════════════════════════
```

---

## Commands

**Start session:**
```
"Ξεκίνα 2 ώρες αυτοβελτίωσης"
"Start 3 hours auto-improvement"
"Run improvement mode for 90 minutes"
"Αυτοβελτίωση για 1 ώρα"
```

**Check progress:**
```
"Πώς πάει η αυτοβελτίωση;"
"Improvement status?"
```

**Early termination (if needed):**
```
"Σταμάτα την αυτοβελτίωση"
"Stop improvement mode"
```

---

## Technical Implementation

Uses isolated agent session with:
- `sessions_spawn` for parallel execution
- Progress tracking via file updates
- Regular status messages via delivery.announce
- Final report delivery at completion

---

## Version History

- **1.0.0** (2026-03-13) - Initial release
  - 4-stage improvement cycle
  - Progress updates every 30 min
  - Comprehensive final reporting
