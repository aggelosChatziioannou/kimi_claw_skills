# OPENCLAW CRON SCHEDULING FAILURE - DETAILED PROMPT FOR EXTERNAL AI MODEL

## EXECUTIVE SUMMARY

**Request:** Design a robust solution for OpenClaw cron jobs that fail with "API rate limit reached" errors. Need reliable scheduled task execution that doesn't fail silently or require constant manual intervention.

**Current System:** Kimi Claw (OpenClaw agent) - AI assistant running scheduled tasks via OpenClaw's cron system.

---

## SYSTEM CONTEXT

### What is OpenClaw?

**OpenClaw** is an AI agent framework that provides:

- **Cron job scheduling** via internal cron system
- **Browser automation** (Playwright-based)
- **File system operations**
- **Telegram/Discord messaging integration**
- **Sub-agent spawning** (isolated sessions)

**Cron System Architecture:**

```
User Request → OpenClaw Gateway → Cron Scheduler → Agent Execution
                                      ↓
                              Session Management
                              (main vs isolated)
```

**Key Configuration Options:**

1. **sessionTarget**: "main" | "isolated"
   - `"main"`: Runs in the same session as the user chat (shares context)
   - `"isolated"`: Spawns a new sub-agent session (clean state)

2. **payload.kind**: "systemEvent" | "agentTurn"
   - `"systemEvent"`: Injects text as system message (requires main session)
   - `"agentTurn"`: Runs agent with a prompt (requires isolated session)

3. **delivery**: Configuration for output routing
   - `"channel"`: Where to send results (telegram, discord, etc.)
   - `"to"`: Specific recipient ID
   - `"mode"`: "announce" | "none"

### Cron Job Schema (OpenClaw)

```json
{
  "name": "Morning Briefing",
  "schedule": {
    "kind": "cron",
    "expr": "0 8 * * *",
    "tz": "Europe/Athens"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "Generate morning briefing..."
  },
  "sessionTarget": "isolated",
  "delivery": {
    "mode": "announce",
    "channel": "telegram",
    "to": "5749686535"
  },
  "enabled": true,
  "notify": true
}
```

---

## THE PROBLEM: "API rate limit reached" Errors

### Symptom Description

**Error Message:**
```
API rate limit reached. Please try again later.
```

**Behavior:**
- Cron job is scheduled successfully
- Job appears in `cron list` as enabled
- At scheduled time, job starts
- Within seconds, fails with "API rate limit reached"
- No output delivered to user
- Job run history shows failure

### When It Happens

1. **Initial Creation:** Sometimes works for first few runs
2. **After Days/Weeks:** Starts failing consistently
3. **During Peak Hours:** More likely to fail (on-the-hour schedules)
4. **With Multiple Jobs:** Affects all scheduled jobs simultaneously

### Impact

- ❌ Morning briefing doesn't run
- ❌ Memory consolidation doesn't happen
- ❌ Daily tasks don't execute
- ❌ User has to manually trigger tasks
- ❌ Silent failures (user doesn't know it failed until checking)

---

## ATTEMPTED SOLUTIONS & RESULTS

### SOLUTION 1: sessionTarget: "main" with systemEvent (FAILED)

**Attempt:**
```json
{
  "sessionTarget": "main",
  "payload": {
    "kind": "systemEvent",
    "text": "Time for your morning briefing!"
  }
}
```

**Result:**
- ❌ Cron system rejected: "sessionTarget=main requires payload.kind=systemEvent"
- ❌ But systemEvent just injects text, doesn't execute agent logic
- ❌ Cannot run actual tasks with main session

**Why It Failed:**
- `sessionTarget: "main"` is ONLY for simple reminders
- Cannot execute agent logic (web search, file operations, etc.)
- Essentially just sends a message, doesn't "do" anything

---

### SOLUTION 2: sessionTarget: "isolated" with agentTurn (WORKS INITIALLY, THEN FAILS)

**Attempt:**
```json
{
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "Generate comprehensive morning briefing..."
  }
}
```

**Result:**
- ✅ Works for first few runs
- ❌ After several days/weeks, starts failing with "API rate limit reached"
- ❌ Multiple jobs fail simultaneously

**Error Pattern:**
```
[2026-03-13T06:00:00] Job started: morning-briefing
[2026-03-13T06:00:05] Error: API rate limit reached. Please try again later.
[2026-03-13T06:00:05] Job failed
```

---

### SOLUTION 3: Timezone-Specific Scheduling (PARTIAL SUCCESS)

**Attempt:**
Added explicit timezone to all cron jobs:
```json
{
  "schedule": {
    "kind": "cron",
    "expr": "0 8 * * *",
    "tz": "Europe/Athens"
  }
}
```

**Result:**
- ✅ Jobs run at correct local time
- ❌ Still get rate limit errors

**Why It's Not The Fix:**
- Timezone was correct but not the root cause
- Rate limiting is not timezone-related

---

### SOLUTION 4: Off-Peak Scheduling (MITIGATION)

**Attempt:**
Instead of on-the-hour (8:00, 9:00, 10:00), use off-peak times:
```json
{
  "schedule": {
    "kind": "cron",
    "expr": "17 8 * * *"  // 8:17 AM instead of 8:00 AM
  }
}
```

**Result:**
- ✅ Slightly better success rate
- ❌ Still occasional failures
- ❌ Doesn't solve underlying issue

**Why It's Partial:**
- Reduces competition with other scheduled tasks
- But doesn't address the actual rate limiting mechanism

---

### SOLUTION 5: OpenClaw Gateway Update (FIXED TEMPORARILY)

**Attempt:**
Updated OpenClaw Gateway to latest version:
```bash
openclaw gateway update
```

**Result:**
- ✅ Fixed rate limit errors for several days
- ❌ Eventually returned (suggests resource accumulation)

**Root Cause Discovered:**
The "API rate limit reached" error was actually a **bug in OpenClaw Gateway's session management**:
- Old sessions were accumulating over time
- Not being cleaned up properly
- Eventually hit internal limits
- Update fixed the bug but issue may recur

---

## CURRENT ACTIVE JOBS

```json
{
  "id": "a88c9f86-8d5c-49a1-a824-7a02edbcf6b9",
  "name": "Morning Briefing",
  "schedule": "0 8 * * *",
  "tz": "Europe/Athens",
  "status": "intermittent failures"
}
```

```json
{
  "id": "d4f039ca-f272-4856-b293-1d2663f7cddb",
  "name": "Memory Consolidation",
  "schedule": "0 10 * * *",
  "tz": "Europe/Athens",
  "status": "intermittent failures"
}
```

---

## PROBLEM ANALYSIS

### What "API rate limit reached" Actually Means

**Hypothesis 1: OpenClaw Internal Rate Limiting**
- OpenClaw Gateway has internal rate limits for:
  - Session creation
  - Agent execution
  - Message delivery
- Cron jobs may hit these limits when multiple run simultaneously

**Hypothesis 2: Session Accumulation**
- Each `sessionTarget: "isolated"` job creates a new sub-agent session
- Sessions may not be cleaned up properly
- Accumulated sessions cause resource exhaustion
- Eventually triggers rate limiting

**Hypothesis 3: External API Rate Limits**
- OpenClaw may use external services (LLM APIs, etc.)
- Cron jobs consume these API quotas
- When quota exceeded, all jobs fail

**Hypothesis 4: Race Conditions**
- Multiple cron jobs scheduled at same time
- Race condition in session management
- Some jobs get rate limited while others succeed

### Constraints

1. **Cannot use sessionTarget: "main"** - Only supports systemEvent, not agentTurn
2. **Must use sessionTarget: "isolated"** - But causes rate limit issues
3. **Cannot modify OpenClaw Gateway** - User-level agent, not admin
4. **Need reliable scheduling** - Tasks must run without manual intervention

---

## REQUEST FOR SOLUTION

Design a **production-ready, reliable scheduling system** for OpenClaw that:

### REQUIREMENTS (Must Have)

1. **Reliable Execution**
   - Tasks run when scheduled (not 50% of the time)
   - Self-healing (retries on failure)
   - No silent failures (always notify on failure)

2. **No Rate Limit Errors**
   - Work within OpenClaw's constraints
   - Or use alternative scheduling mechanism
   - Handle resource cleanup properly

3. **Autonomous Operation**
   - No manual intervention required
   - Runs 24/7 without user action
   - Self-monitoring and alerting

4. **Maintainability**
   - Easy to add/remove jobs
   - Clear status monitoring
   - Debugging capabilities

### APPROACHES TO EVALUATE

#### Option A: External Cron System

**Idea:** Use system cron (crontab) instead of OpenClaw's internal cron

**Implementation:**
```bash
# System cron calls OpenClaw CLI
0 8 * * * /usr/bin/openclaw run morning-briefing
```

**Pros:**
- Bypass OpenClaw's internal rate limits
- Uses proven, reliable system cron
- More control over execution

**Cons:**
- May not integrate with OpenClaw's session system
- Need to implement output delivery manually
- Requires OpenClaw CLI support for scheduled tasks

**Questions:**
- Can OpenClaw CLI trigger agent tasks from system cron?
- How to deliver results to Telegram?

#### Option B: External Scheduler (node-cron, Python schedule)

**Idea:** Run a separate persistent process that schedules tasks

**Implementation:**
```javascript
// Node.js scheduler
const cron = require('node-cron');

cron.schedule('0 8 * * *', () => {
  // Call OpenClaw API or spawn agent
});
```

**Pros:**
- Full control over scheduling logic
- Can implement custom retry logic
- Can spread tasks to avoid rate limits

**Cons:**
- Need persistent process (systemd service?)
- Complexity of maintaining another service
- Still need to interact with OpenClaw

#### Option C: Smart Job Spreading

**Idea:** Spread jobs across time to avoid concurrent execution

**Implementation:**
```json
{
  "morning-briefing": "17 8 * * *",    // 8:17 AM
  "memory-consolidation": "23 10 * * *" // 10:23 AM
}
```

**Pros:**
- Reduces concurrent load
- May avoid rate limits
- Simple to implement

**Cons:**
- Doesn't solve underlying issue
- Jobs may still fail individually
- Not truly scalable

#### Option D: Retry Logic with Exponential Backoff

**Idea:** Implement wrapper that retries failed jobs

**Implementation:**
```python
def run_with_retry(job_func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return job_func()
        except RateLimitError:
            wait_time = 2 ** attempt  # Exponential backoff
            time.sleep(wait_time)
    raise MaxRetriesExceeded()
```

**Pros:**
- Handles transient failures
- Better reliability
- Can be combined with other approaches

**Cons:**
- Doesn't help if rate limit is persistent
- May delay jobs significantly
- Need to implement outside OpenClaw cron

#### Option E: Single Master Cron Job

**Idea:** One cron job that orchestrates all other tasks

**Implementation:**
```json
{
  "name": "Master Scheduler",
  "schedule": "*/5 * * * *",  // Every 5 minutes
  "payload": {
    "kind": "agentTurn",
    "message": "Check which tasks need to run and execute them"
  }
}
```

**Pros:**
- Only one cron job (reduces rate limit exposure)
- Internal logic can manage timing
- Can implement custom scheduling logic

**Cons:**
- Complex implementation
- Still vulnerable to rate limits
- Single point of failure

#### Option F: OpenClaw Health Monitoring + Manual Trigger

**Idea:** Accept that cron is unreliable, implement monitoring + manual triggers

**Implementation:**
1. Cron job sends heartbeat every hour
2. If heartbeat missed, notify user
3. User manually triggers tasks

**Pros:**
- Acknowledges limitations
- User always knows status
- Simple to implement

**Cons:**
- Not truly automated
- Requires user intervention
- Defeats purpose of scheduling

---

## QUESTIONS FOR THE SOLUTION

Please provide a solution that answers:

1. **Root Cause Analysis:**
   - What is actually causing "API rate limit reached"?
   - Is it OpenClaw internal limits or external APIs?
   - How can we verify the root cause?

2. **Recommended Approach:**
   - Which of the options above do you recommend?
   - Why is it the best solution?
   - What are the trade-offs?

3. **Implementation Details:**
   - Step-by-step setup guide
   - Complete working code/configuration
   - Error handling and monitoring

4. **Alternative Solutions:**
   - What if the recommended approach doesn't work?
   - What are the backup options?

5. **Monitoring and Debugging:**
   - How to monitor job success/failure?
   - How to debug when things go wrong?
   - How to get notified of failures?

---

## ADDITIONAL CONTEXT

### OpenClaw Version
- Current: Latest (as of March 2026)
- Gateway: Updated recently to fix session accumulation bug

### Environment
- OS: Linux (Ubuntu)
- Node.js: v22.22.0
- Shell: bash
- Channel: Telegram (primary)

### User's Pattern
- ~5-10 scheduled jobs expected
- Runs 24/7 on VPS
- Prefers reliability over complexity
- Willing to use external tools if needed

### What Has Been Tried
- ✅ Different timezones
- ✅ Off-peak scheduling
- ✅ sessionTarget variations
- ✅ Gateway update
- ✅ Multiple schedule formats (cron, every, at)

### Success Criteria
- 95%+ job success rate
- No manual intervention for weeks
- Clear failure notifications
- Easy to add new jobs

---

## DELIVERABLES EXPECTED

Please provide:

1. **Root cause analysis** of the rate limiting
2. **Recommended solution** with clear justification
3. **Complete implementation** (code/config)
4. **Setup instructions** (step-by-step)
5. **Monitoring strategy** (how to know it's working)
6. **Troubleshooting guide** (when things go wrong)

---

## NOTE TO AI MODEL

This is a frustrating, persistent issue that has resisted multiple solution attempts. The user needs a solution that:
- Actually works in production
- Doesn't require constant babysitting
- Is maintainable long-term

Please be thorough, consider edge cases, and don't suggest solutions that have already been tried (see "What Has Been Tried" section).

The user is technical and can implement complex solutions if they are well-documented and reliable.

Thank you!
