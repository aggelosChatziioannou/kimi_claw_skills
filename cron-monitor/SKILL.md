# Cron Monitor Skill

**ID:** cron-monitor  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** OpenClaw with cron system

---

## Purpose

Automatically monitor cron job health, detect failures, and send alerts before issues become critical.

## How It Works

### Architecture

```
Heartbeat / Manual Check
  ↓
List all cron jobs
  ↓
For each job:
  → Check last run status
  → Check consecutive errors
  → Check duration trends
  → Compare with thresholds
  ↓
If issues detected:
  → Send Telegram alert
  → Provide diagnostic info
  → Suggest fixes
```

### Data Tracked

| Metric | Warning Threshold | Critical Threshold |
|--------|-------------------|-------------------|
| Consecutive Errors | 2 | 3 |
| Last Run Duration | > 5 min | > 10 min |
| Success Rate (24h) | < 80% | < 50% |
| Time Since Last Run | > 2x schedule | > 3x schedule |

---

## Commands

### Manual Check
```
"Check cron jobs status"
"Are my cron jobs working?"
"Cron health check"
```

### Get Report
```
"Show cron job statistics"
"Cron job report"
```

---

## Notifications

### Warning Alert
```
⚠️ **CRON JOB WARNING**

Job: Morning Briefing
Status: 2 consecutive errors
Last Run: 2026-03-14 10:05 (failed)
Suggested Action: Check logs
```

### Critical Alert
```
🚨 **CRON JOB CRITICAL**

Job: Memory Consolidation
Status: FAILED 3 times in a row!
Last Error: API rate limit
Action Required: Update OpenClaw
```

### Daily Summary
```
📊 **CRON DAILY SUMMARY**

✅ Morning Briefing: 1/1 success
✅ Memory Consolidation: 1/1 success
⚠️ Gemini Reminder: 0/1 (pending)

Overall Health: 95% ✅
```

---

## Cron Schedule

```json
{
  "schedule": {
    "hours": [9, 15, 21],
    "timezone": "Europe/Athens"
  }
}
```

---

## Files

| File | Purpose |
|------|---------|
| `cron_monitor.py` | Main monitoring logic |
| `health_checker.py` | Health analysis |
| `alert_manager.py` | Alert generation |
| `config.yaml` | Thresholds configuration |

---

## Security

- Read-only access to cron jobs
- No job modification without permission
- Secure alert delivery

---

## Version History

- **1.0.0** (2026-03-14) - Initial release
  - Job health monitoring
  - Consecutive error detection
  - Telegram alerts
  - Daily summaries
