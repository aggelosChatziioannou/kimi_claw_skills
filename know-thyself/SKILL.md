# Know Thyself - Kimi-Claw Architecture & Limitations

## Purpose
Document the technical boundaries of Kimi-Claw vs OpenClaw to prevent proposing impossible solutions.

## Critical Rule
**ALWAYS check this skill before proposing any architecture involving:**
- HTTP servers/webhooks
- 24/7 background processes  
- Local machine access
- Persistent connections

---

## Kimi-Claw vs OpenClaw Comparison

### Hosting Model
| Aspect | Kimi-Claw (Me) | OpenClaw |
|--------|----------------|----------|
| Location | Kimi Cloud servers | Your local machine/VPS |
| Runtime | Containerized sandbox | Native OS process |
| Uptime | Session-based (wake on message) | Persistent daemon |
| Network | No inbound ports | Can open ports (localhost:18789) |

### Capabilities Matrix

#### ❌ CANNOT DO (Kimi-Claw)
- Open HTTP server/ports
- Listen for webhooks from external services
- Run background tasks without user message trigger
- Access user's local filesystem (outside workspace)
- SSH to external servers
- Persistent WebSocket connections
- Real-time bidirectional communication with browser

#### ✅ CAN DO (Kimi-Claw)
- File operations in `/root/.openclaw/workspace/`
- Git operations (push/pull/commit)
- Web search and browsing
- Execute bash commands in container
- Scheduled tasks via OpenClaw Gateway cron (if configured)
- Telegram/Discord integration via channels
- Code generation and editing

#### ✅ CAN DO (OpenClaw ONLY)
- Local HTTP gateway (port 18789)
- Receive webhooks from GitHub/Stripe/etc
- 24/7 autonomous operation
- Access local devices (camera, location via Nodes)
- BYOC (Bring Your Own Claw) hybrid setup

---

## Daily Update Check Protocol

### When to Run
- Every morning during Memory Consolidation
- Before proposing any new architecture
- When user asks about capabilities

### Checklist
1. Search for "Kimi Claw updates 2026"
2. Search for "OpenClaw new features"
3. Check if any limitations have been removed
4. Update this SKILL.md if changes detected

### Search Queries
```
Kimi Claw new features March 2026
OpenClaw vs Kimi Claw differences updates
Moonshot AI Kimi Claw capabilities changes
```

---

## Pre-Flight Verification Script

Before proposing ANY solution, ask:

1. **Does it require HTTP server/ports?**
   - YES → STOP. Propose alternative or ask user to use OpenClaw
   
2. **Does it need 24/7 background processing?**
   - YES → Check if OpenClaw Gateway cron is available
   - If not → STOP. Explain limitation
   
3. **Does it need real-time bidirectional communication?**
   - YES → STOP. Propose polling-based alternative
   
4. **Does it access user's local machine?**
   - YES → STOP. I only have container workspace access

---

## Common Mistakes to Avoid

### ❌ WRONG: "I'll set up a webhook server"
**Why:** I cannot receive HTTP requests
**RIGHT:** "I'll check via polling/API call when you message me"

### ❌ WRONG: "This will run in the background"
**Why:** I only run when you message me (unless Gateway cron is set)
**RIGHT:** "I'll set up a cron job via Gateway (if available) or run on-demand"

### ❌ WRONG: "I'll access your local files"
**Why:** I'm in a cloud container
**RIGHT:** "Please upload files to the workspace or use GitHub"

### ❌ WRONG: "The dashboard will send commands to me"
**Why:** No inbound HTTP possible
**RIGHT:** "I'll generate static dashboard, you view it and message me commands"

---

## Verification Example

**User asks:** "Can you make a real-time dashboard that updates automatically?"

**My response should be:**
> Boss, I cannot support real-time features because:
> 1. I don't have persistent HTTP server capability
> 2. I wake up only when you message me
> 
> **Alternatives I CAN do:**
> - Static dashboard that updates when I push new version
> - Cron-based updates (if you have OpenClaw Gateway)
> - You message me "check status" and I generate fresh view

---

## Recent Updates (March 2026)

### March 9, 2026 - New Channel Integrations
- ✅ **Weibo** integration added
- ✅ **WeChat Work (企业微信)** integration added  
- ✅ **Feishu/Lark** bot integration confirmed
- Users can now control Kimi-Claw through these apps

### February 15, 2026 - Kimi Claw Launch Features
- 5,000+ ClawHub skills available
- 40GB cloud storage
- 24/7 uptime capability (via cloud infrastructure)
- Pro-Grade Search with live data (Yahoo Finance)
- BYOC (Bring Your Own Claw) for hybrid setups

## Data Residency Note
**IMPORTANT:** Kimi-Claw operates on Chinese infrastructure (Moonshot AI, Beijing). Data jurisdiction under Chinese law (PIPL).

## Last Updated
2026-03-12 - Added March 2026 updates

## Next Check
Daily during Memory Consolidation
