# 🔍 Cron Monitor Skill

**Skill #32** - Automatic cron job health monitoring and alerting

---

## 📋 Overview

This skill automatically monitors all your cron jobs, detects issues before they become critical, and sends smart alerts via Telegram.

## 🎯 Features

- ✅ **Health Monitoring** - Tracks all cron jobs continuously
- ⚠️ **Smart Alerts** - Only sends alerts when needed (no spam)
- 📊 **Daily Summaries** - Overall health status
- 🔧 **Diagnostic Info** - Suggests fixes for common issues
- 📱 **Telegram Integration** - Alerts delivered directly to you

## 🚨 Alert Types

### Warning Alerts
- 2 consecutive failures
- Runs taking > 5 minutes
- Success rate < 80%

### Critical Alerts
- 3+ consecutive failures
- Runs taking > 10 minutes
- Success rate < 50%

## 📱 Example Notifications

**Warning:**
```
⚠️ **CRON JOB WARNING**

📋 Job: Morning Briefing
⚠️ Issues:
  • Failed 2 consecutive times
⏱️ Last Run: 2026-03-14 10:05
💡 Suggested Action: Monitor for next run
```

**Critical:**
```
🚨 **CRON JOB CRITICAL**

📋 Job: Memory Consolidation
⚠️ Issues:
  • Failed 3 times in a row
⏱️ Last Run: 2026-03-14 10:05
🔧 Suggested Action: Check logs and restart Gateway
```

**Daily Summary:**
```
📊 **CRON HEALTH SUMMARY**

📋 Total Jobs: 4
✅ Healthy: 3
⚠️ Warnings: 1

⚠️ **Overall: NEEDS ATTENTION**

📋 **Jobs Needing Attention:**
⚠️ Morning Briefing
```

## 🛠️ Commands

```
"Check cron jobs status"
"Are my cron jobs working?"
"Show cron health report"
```

## ⏰ Schedule

- **Automatic checks:** 9:00 AM, 3:00 PM, 9:00 PM (Europe/Athens)
- **Alert cooldown:** 1 hour (no duplicate alerts)

## 📁 Files

```
cron-monitor/
├── SKILL.md              # Technical documentation
├── README.md             # This file
├── cron_monitor.py       # Main monitoring logic
└── __init__.py
```

## 🔧 Configuration

Edit thresholds in `cron_monitor.py`:

```python
WARN_CONSECUTIVE_ERRORS = 2
CRITICAL_CONSECUTIVE_ERRORS = 3
WARN_DURATION_MINUTES = 5
CRITICAL_DURATION_MINUTES = 10
```

## 📝 Version History

- **1.0.0** (2026-03-14) - Initial release

---

*Made with ❤️‍🔥 by Kimi Claw*
