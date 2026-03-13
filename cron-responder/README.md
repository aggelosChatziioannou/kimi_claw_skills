# Cron Responder

Handle cron system events and forward to Telegram.

## What It Does

When cron jobs fire with `systemEvent`, this skill:
1. Receives the event
2. Generates appropriate message
3. Sends to Telegram immediately

## Events Supported

| Event | Trigger | Action |
|-------|---------|--------|
| Morning Briefing | 🌅 MORNING BRIEFING | Send daily briefing |
| Memory Consolidation | 🧠 DAILY MEMORY CONSOLIDATION | Send memory summary |
| Email Check | 📧 EMAIL CHECK | Send email summary |

## Setup

Cron job example:
```json
{
  "name": "Morning Briefing",
  "schedule": { "kind": "cron", "expr": "0 8 * * *", "tz": "Europe/Athens" },
  "sessionTarget": "main",
  "payload": { "kind": "systemEvent", "text": "🌅 MORNING BRIEFING" }
}
```

## Files

- `SKILL.md` - Full documentation
- `responder.py` - Event handler logic

## Version

1.0.0 (2026-03-13)
